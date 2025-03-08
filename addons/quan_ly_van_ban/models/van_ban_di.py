from odoo import models, fields, api


class VanBanDi(models.Model):
    _name = 'van_ban_di'
    _description = 'Bảng chứa thông tin van_ban_di'
    _rec_name = "tieu_de"
    id = fields.Integer("ID văn bản đi", required=True)
    ngay_di = fields.Date("Ngày đi", required=True)
    so_hieu = fields.Char("Số hiệu",  store=True, readonly=True)
    trich_yeu = fields.Text("Trích yếu", required=True)
    tieu_de =fields.Char("Tiêu đề", required=True)
    tep_dinh_kem = fields.Binary("Tệp đính kèm")
    ho_so = fields.Many2one ('ho_so', string='Hồ sơ')
    
    id_loai_van_ban = fields.Many2one('loai_van_ban', string='Loại văn bản')
    id_co_quan_ban_hanh = fields.Many2one('phong_ban', string='Cơ quan ban hành')
    id_nguoi_phat_hanh = fields.Many2one('nhan_vien', string='Người ký')
    dia_chi_nhan = fields.Text("Nơi nhận", required=True)
    id_do_mat = fields.Many2one('do_mat', string='Độ mật')
    id_nam = fields.Many2one('nam', string='Năm')
    @api.model
    def create(self, vals):
        count = self.env['van_ban_di'].search_count([]) + 1
        vals['so_hieu'] = f"{count}_{fields.Date.from_string(vals['ngay_di']).strftime('%Y%m%d')}"
        return super(VanBanDi, self).create(vals)



 