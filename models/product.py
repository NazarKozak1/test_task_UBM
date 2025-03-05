from odoo import fields, models

class Product(models.Model):
    _inherit = 'product.product'

    weight = fields.Float(string='Вага (кг)')
    volume = fields.Float(string='Об\'єм (м³)')
