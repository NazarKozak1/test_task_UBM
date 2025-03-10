from odoo import fields, models, api

class CustomOrder(models.Model):
    _name = 'custom.order'
    _description = 'Замовлення'

    name = fields.Char(string='Номер замовлення', required=True)
    date = fields.Date(string='Дата', default=fields.Date.today)
    supplier_id = fields.Many2one('res.partner', string='Постачальник', domain=[('contractor_type', '=', 'supplier')])
    customer_id = fields.Many2one('res.partner', string='Клієнт', domain=[('contractor_type', '=', 'customer')])
    order_line_ids = fields.One2many('custom.order.line', 'order_id', string='Товари')
    total_amount = fields.Float(string='Сумарна вартість', compute='_compute_totals')
    total_weight = fields.Float(string='Сумарна вага', compute='_compute_totals')
    total_volume = fields.Float(string='Сумарний об\'єм', compute='_compute_totals')

    @api.depends('order_line_ids')
    def _compute_totals(self):
        for record in self:
            record.total_amount = sum(line.subtotal for line in record.order_line_ids)
            record.total_weight = sum(line.product_id.weight * line.quantity for line in record.order_line_ids)
            record.total_volume = sum(line.product_id.volume * line.quantity for line in record.order_line_ids)