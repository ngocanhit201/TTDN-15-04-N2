from odoo import models, fields, api


class Nam(models.Model):
    _name = 'nam'
    _description = 'Năm'
    _rec_name = "nam"

    id = fields.Integer("ID", required=True)
    nam = fields.Char("Năm", required=True)
    mo_ta = fields.Char("Mô tả")

    van_ban_di_ids = fields.One2many('van_ban_di', 'id_nam', string="Văn bản đi")
    van_ban_den_ids = fields.One2many('van_ban_den', 'id_nam', string="Văn bản đến")



    