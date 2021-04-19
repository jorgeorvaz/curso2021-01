from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description', translate=True)
    date = fields.Date(string='Date')

    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('asignado', 'Asignado'),
        ('en_proceso', 'En proceso'),
        ('pendiente', 'Pendiente'),
        ('resuelto', 'Resuelto'),
        ('cancelado', 'Cancelado')
    ], string='State', default='nuevo')

    time = fields.Float(string='Time')
    assigned = fields.Boolean(string='Assigned', readonly=True)
    date_limit = fields.Date(string='Date Limit')
    action_corrective = fields.Html(
        string='Corrective Action', help='Describe corrective actions to do')
    action_preventive = fields.Html(
        string='Preventive Action', help='Describe preventive actions to do')

    def do_assign(self):
        self.ensure_one()
        self.write({
            'state': 'asignado',
            'assigned': True
        })
        # for ticket in self:
        #     ticket.state = 'asignado'
        #     ticket.assigned = True

    def proceso(self):
        self.ensure_one()
        self.state = 'en_proceso'

    def pendiente(self):
        self.ensure_one()
        self.state = 'pendiente'

    def finalizado(self):
        self.ensure_one()
        self.state = 'resuelto'

    def cancelado(self):
        self.ensure_one()
        self.state = 'cancelado'
    # @api.model
    # def close_leads(self):
    #     active_tickets = self.search[('active', '=', True)]
    #     for ticket in active_tickets:
    #         ticket.close()
