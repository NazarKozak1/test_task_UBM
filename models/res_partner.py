from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    contractor_type = fields.Selection([
        ('carrier', 'Перевізник'),
        ('supplier', 'Постачальник'),
        ('customer', 'Клієнт'),
    ], string='Вид контрагента')