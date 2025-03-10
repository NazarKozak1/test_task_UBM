from odoo import fields, models, api

class CustomOrderLine(models.Model):
    _name = 'custom.order.line'
    _description = 'Рядок замовлення'

    order_id = fields.Many2one('custom.order', string='Замовлення')
    product_id = fields.Many2one('product.product', string='Товар', required=True)
    price = fields.Float(string='Ціна', related='product_id.lst_price')
    quantity = fields.Float(string='Кількість', default=1.0)
    subtotal = fields.Float(string='Вартість', compute='_compute_subtotal')

    @api.depends('price', 'quantity')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.price * line.quantity