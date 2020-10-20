from odoo import models, fields, api

class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'
    
    @api.model
    def change_sale_name(self, name, partner_id):
        partner_name = self.env['res.partner'].browse(partner_id).name
        letters = [word[0] for word in partner_name.split()]
        
        characters = list(name)
        characters[2] = letters[0]
        characters[3] = letters[1]
        
        return ''.join(characters)
    
    
    @api.model
    def create(self, vals):
        record = super(SaleOrderInherited, self).create(vals)
        record['name'] = self.change_sale_name(vals.get('name'), vals.get('partner_id'))
        
        return record
        
        

