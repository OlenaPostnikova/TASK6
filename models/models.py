# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6(models.Model):
#     _name = '/home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6./home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6'
#     _description = '/home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6./home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
