#-*- coding:utf-8 -*-
from openerp import models, fields, api

class product(models.Model):
    _inherit='product.category'

class stock_move(models.Model):
  _name='stock.move'
  _inherit=['stock.move']

class wizard_inventario(models.Model):
  _name='wizard.inventario'

  fecha = fields.Datetime('Fecha', required=True)
  editorial = fields.Many2one('product.category', 'Editorial')

  @api.multi
  def search_editorial(self,values):
    reg=self.env['stock.move'].search(['date','<=',self.fecha])
    print("############# self", self)
    print("############# values", values)
    return reg

class stock_by_category(models.Model):
  _name='stock.by.category'
  _description='Stock por categoria de producto'

  move_id=fields.Char('Move', size=128)
  product_id=fields.Char('Producto', size=128)
  barcode=fields.Char('Barcode', size=128)