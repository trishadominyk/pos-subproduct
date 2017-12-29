# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SubproductProduct(models.Model):
	_name = 'pos_subproduct.subproduct'
	_description = 'Subproduct'

	product_id = fields.Many2one('product.template', string="Product")
	subproduct_id = fields.Many2one('product.template', string="Subproduct")

class SubproductProductInherit(models.Model):
	_inherit = 'product.template'

	subproduct_ids = fields.Many2many('pos_subproduct.subproduct', string="Subproducts")