# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class remove_menu_item(models.Model):
#     _name = 'remove_menu_item.remove_menu_item'
#     _description = 'remove_menu_item.remove_menu_item'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
