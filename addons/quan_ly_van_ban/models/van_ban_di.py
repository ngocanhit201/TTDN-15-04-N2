from odoo import models, fields, api


class VanBanDi(models.Model):
    _name = 'van_ban_di'
    _description = 'Bảng chứa thông tin van_ban_di'
    
    id = fields.Integer("ID văn bản đi", required=True)
    ngay_di = fields.Date("Ngày đi", required=True)
    so_hieu = fields.Char("Số hiệu", compute="_compute_so_hieu", store=True, readonly=True)
    trich_yeu = fields.Text("Trích yếu", required=True)
    tieu_de =fields.Text("Tiêu đề", required=True)
    tep_dinh_kem = fields.Binary("Tệp đính kèm")
    ngay_nhan =fields.Date("Ngày nhận", required=True)
    ho_so = fields.Many2one ('ho_so', string='Ho So')
    
    id_loai_van_ban = fields.Many2one('loai_van_ban', string='Loại văn bản')
    id_co_quan_ban_hanh = fields.Many2one('phong_ban', string='Cơ quan ban hành')
    id_nguoi_phat_hanh = fields.Many2one('nhan_vien', string='Người phát hành')
    nguoi_nhan = fields.Text("Người nhận", required=True)
    id_do_mat = fields.Many2one('do_mat', string='Độ mật')
    id_nam = fields.Many2one('nam', string='Năm')
    
    @api.depends('ngay_di')
    def _compute_so_hieu(self):
        for record in self:
            if record.ngay_di:
                count = self.search_count([('ngay_di', '=', record.ngay_di)])  # Đếm số lượng đã có
                record.so_hieu = f"{count + 1}_{record.ngay_di.strftime('%Y%m%d')}"
            else:
                record.so_hieu = False  # Nếu chưa có ngày đến thì không có số hiệu



 