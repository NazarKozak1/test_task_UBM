from odoo import fields, models

class Vehicle(models.Model):
    _name = 'custom.vehicle'
    _description = 'Автомобіль'

    name = fields.Char(string='Номер авто', required=True)
    carrier_id = fields.Many2one('res.partner', string='Перевізник', domain=[('contractor_type', '=', 'carrier')])
    max_weight = fields.Float(string='Макс. вага (кг)')
    max_volume = fields.Float(string='Макс. об\'єм (м³)')