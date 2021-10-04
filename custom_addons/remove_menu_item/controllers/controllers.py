# -*- coding: utf-8 -*-
# from odoo import http


# class RemoveMenuItem(http.Controller):
#     @http.route('/remove_menu_item/remove_menu_item/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/remove_menu_item/remove_menu_item/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('remove_menu_item.listing', {
#             'root': '/remove_menu_item/remove_menu_item',
#             'objects': http.request.env['remove_menu_item.remove_menu_item'].search([]),
#         })

#     @http.route('/remove_menu_item/remove_menu_item/objects/<model("remove_menu_item.remove_menu_item"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('remove_menu_item.object', {
#             'object': obj
#         })
