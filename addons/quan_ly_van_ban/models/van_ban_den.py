from odoo import models, fields, api


class VanBanDen(models.Model):
    _name = 'van_ban_den'
    _description = 'Bảng chứa thông tin văn bản đến'
    _rec_name = "tieu_de"
    id = fields.Integer("ID văn bản đến", required=True)
    ngay_den = fields.Date("Ngày đến", required=True)
    so_hieu = fields.Char("Số hiệu",  store=True, readonly=True)
    co_quan_ban_hanh = fields.Char("Cơ quan ban hành", required=True)
    trich_yeu = fields.Text("Trích yếu", required=True)
    tieu_de =fields.Text("Tiêu đề", required=True)
    id_co_quan_nhan= fields.Many2one('phong_ban', string = 'Cơ quan nhận')
    tep_dinh_kem = fields.Binary("Tệp đính kèm")

    id_do_mat = fields.Many2one('do_mat', string='Độ mật')
    id_loai_van_ban = fields.Many2one('loai_van_ban', string='Loại văn bản')
    id_nam = fields.Many2one('nam', string='Năm')
    ids_cong_viec = fields.One2many('cong_viec', 'van_ban_den_ids', string='Công việc')
    id_nguoi_nhan =fields.Many2one('nhan_vien', string = 'Người nhận')
    ho_so = fields.Many2one ('ho_so', string='Hồ sơ')
    @api.model
    def create(self, vals):
        count = self.env['van_ban_den'].search_count([]) + 1
        vals['so_hieu'] = f"{count}_{fields.Date.from_string(vals['ngay_den']).strftime('%Y%m%d')}"
        return super(VanBanDen, self).create(vals)

    



 