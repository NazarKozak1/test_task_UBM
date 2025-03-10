from odoo import fields, models, api

class Route(models.Model):
    _name = 'custom.route'
    _description = 'Маршрут'

    carrier_id = fields.Many2one('res.partner', string='Перевізник', domain=[('contractor_type', '=', 'carrier')])
    vehicle_id = fields.Many2one('custom.vehicle', string='Автомобіль')
    order_ids = fields.Many2many('custom.order', string='Замовлення')
    total_weight = fields.Float(string='Сумарна вага', compute='_compute_totals')
    total_volume = fields.Float(string='Сумарний об\'єм', compute='_compute_totals')

    @api.depends('order_ids')
    def _compute_totals(self):
        for record in self:
            record.total_weight = sum(order.total_weight for order in record.order_ids)
            record.total_volume = sum(order.total_volume for order in record.order_ids)

    @api.constrains('order_ids', 'vehicle_id')
    def _check_vehicle_capacity(self):
        for record in self:
            if record.total_weight > record.vehicle_id.max_weight or record.total_volume > record.vehicle_id.max_volume:
                raise models.ValidationError('Сумарна вага або об\'єм замовлень перевищує можливості автомобіля!')