from odoo import models, fields, api


class VanBanDen(models.Model):
    _name = 'van_ban_den'
    _description = 'Bảng chứa thông tin văn bản đến'
    
    id = fields.Integer("ID văn bản đến", required=True)
    ngay_den = fields.Date("Ngày đến", required=True)
    so_hieu = fields.Char("Số hiệu", compute="_compute_so_hieu", store=True, readonly=True)
    co_quan_ban_hanh = fields.Char("Cơ quan ban hành", required=True)
    trich_yeu = fields.Text("Trích yếu", required=True)
    tieu_de =fields.Text("Tiêu đề", required=True)
    id_co_quan_nhan= fields.Many2one('phong_ban', string = 'Cơ quan nhận')
    tep_dinh_kem = fields.Binary("Tệp đính kèm")
    ngay_gui = fields.Date("Ngày gửi", required=True)

    id_do_mat = fields.Many2one('do_mat', string='Độ mật')
    id_loai_van_ban = fields.Many2one('loai_van_ban', string='Loại văn bản')
    id_nam = fields.Many2one('nam', string='Năm')
    ids_cong_viec = fields.One2many('cong_viec', 'van_ban_den_ids', string='Công việc')
    nguoi_gui = fields.Text("Người gửi", required=True)
    id_nguoi_nhan =fields.Many2one('nhan_vien', string = 'Người nhận')
    @api.depends('ngay_den')
    def _compute_so_hieu(self):
        for record in self:
            if record.ngay_den:
                count = self.search_count([('ngay_den', '=', record.ngay_den)])  # Đếm số lượng đã có
                record.so_hieu = f"{count + 1}_{record.ngay_den.strftime('%Y%m%d')}"
            else:
                record.so_hieu = False  # Nếu chưa có ngày đến thì không có số hiệu
    



 