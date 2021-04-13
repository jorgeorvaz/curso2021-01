from odoo import fields, models


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'

    # string es para el nombre de la vista en odoo. el nombre de la variable es para bbdd
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
