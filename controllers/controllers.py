# -*- coding: utf-8 -*-
from odoo import http

# class PosSubproduct(http.Controller):
#     @http.route('/pos_subproduct/pos_subproduct/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_subproduct/pos_subproduct/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_subproduct.listing', {
#             'root': '/pos_subproduct/pos_subproduct',
#             'objects': http.request.env['pos_subproduct.pos_subproduct'].search([]),
#         })

#     @http.route('/pos_subproduct/pos_subproduct/objects/<model("pos_subproduct.pos_subproduct"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_subproduct.object', {
#             'object': obj
#         })