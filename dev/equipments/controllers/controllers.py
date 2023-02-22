# -*- coding: utf-8 -*-
# from odoo import http


# class Equipments(http.Controller):
#     @http.route('/equipments/equipments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/equipments/equipments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('equipments.listing', {
#             'root': '/equipments/equipments',
#             'objects': http.request.env['equipments.equipments'].search([]),
#         })

#     @http.route('/equipments/equipments/objects/<model("equipments.equipments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('equipments.object', {
#             'object': obj
#         })
