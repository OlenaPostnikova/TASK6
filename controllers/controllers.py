# -*- coding: utf-8 -*-
# from odoo import http


# class /home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6(http.Controller):
#     @http.route('//home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6//home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6//home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6.listing', {
#             'root': '//home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6//home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6',
#             'objects': http.request.env['/home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6./home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6'].search([]),
#         })

#     @http.route('//home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6//home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6/objects/<model("/home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6./home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/admin16/opt/odoo-16.0/repositories/olenapostnikova/task6.object', {
#             'object': obj
#         })
