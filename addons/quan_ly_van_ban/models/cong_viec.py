from odoo import models, fields, api
from datetime import date
import logging
_logger = logging.getLogger(__name__)
class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Bảng chứa thông tin công việc'
    _rec_name = "ten_cong_viec"

    ten_cong_viec = fields.Char("Tên công việc", required=True)
    yeu_cau = fields.Text("Yêu cầu xử lý", required=True)
    ngay_tao = fields.Date("Ngày tạo", required=True)
    han_xu_ly = fields.Date("Hạn xử lý", required=True)
    ngay_hoan_thanh = fields.Date("Ngày hoàn thành")
    
    tinh_trang = fields.Selection([
        ('da_nhan', 'Đã nhận'),
        ('huy', 'Huỷ'),
    ], string='Tình trạng')

    trang_thai = fields.Many2one('trang_thai', string='Trạng thái', compute="_compute_trang_thai", store=True , readonly = True)
    
    chi_dao = fields.Many2one('nhan_vien', string="Chỉ đạo", required=True)
    chu_tri_giai_quyet = fields.Many2one('nhan_vien', string="Chủ trì giải quyết")
    van_ban_den_ids = fields.Many2one('van_ban_den', string="Văn bản xử lý", required=True)


    @api.depends('ngay_hoan_thanh', 'han_xu_ly', 'tinh_trang')
    def _compute_trang_thai(self):
        _logger.info("### COMPUTE TRẠNG THÁI ĐƯỢC GỌI ###")

        # Truy vấn một lần cho hiệu suất tốt hơn
        trang_thai_dict = {tt['ten_trang_thai']: tt['id'] for tt in self.env['trang_thai'].search_read(
            [('ten_trang_thai', 'in', ['Hoàn thành', 'Hoàn thành quá hạn', 'Huỷ', 'Đã nhận', 'Đang xử lý'])], ['ten_trang_thai', 'id']
        )}

        today = date.today()  # Lấy ngày hiện tại chỉ một lần

        for record in self:
            _logger.info(f"Đang tính trạng thái cho công việc ID: {record.id}")

            if record.ngay_hoan_thanh:
                if record.han_xu_ly and record.ngay_hoan_thanh > record.han_xu_ly:
                    record.trang_thai = trang_thai_dict.get('Hoàn thành quá hạn', False)
                else:
                    record.trang_thai = trang_thai_dict.get('Hoàn thành', False)
            elif record.tinh_trang == 'huy':
                record.trang_thai = trang_thai_dict.get('Huỷ', False)
            elif record.tinh_trang == 'da_nhan':
                if record.han_xu_ly and today < record.han_xu_ly:
                    record.trang_thai = trang_thai_dict.get('Đang xử lý', False)
                else:
                    record.trang_thai = trang_thai_dict.get('Đã nhận', False)
            else:
                record.trang_thai = False  # Tránh lỗi nếu không có trạng thái phù hợp