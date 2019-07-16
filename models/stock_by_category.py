#-*- coding:utf-8 -*-
from openerp import models, fields, api

class product(models.Model):
    _inherit='product.template'

class stock_move(models.Model):
    _inherit='stock.move'

class stock_by_category(models.Model):
  _name='stock.by.category'
  _description='Stock por categoria de producto'

  move_id=fields.Char('Move', size=128)
  product_id=fields.Char('Producto', size=128)
  barcode=fields.Char('Barcode', size=128)
  product_categ = fields.Many2one('product.category', 'Categoria', ondelete='set null')

  @api.multi
  def write(self,values):
    result=super(stock_by_category).write(values)
    return result  


  # @api.multi
  # def _consul(self,values):
  #     reg=self.env['stock.by.category'].search([('move_id','=', '1')])
  #     return reg