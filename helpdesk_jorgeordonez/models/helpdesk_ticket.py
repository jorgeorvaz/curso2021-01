from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket'

    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions'
    )

    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id',
        string='Tags'
    )

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description', translate=True)
    date = fields.Date(string='Date')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to'
    )

    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('asignado', 'Asignado'),
        ('en_proceso', 'En proceso'),
        ('pendiente', 'Pendiente'),
        ('resuelto', 'Resuelto'),
        ('cancelado', 'Cancelado')
    ], string='State', default='nuevo')

    time = fields.Float(string='Time')

    assigned = fields.Boolean(
        string='Assigned', readonly=True, compute='_compute_assigned')

    date_limit = fields.Date(string='Date Limit')

    action_corrective = fields.Html(
        string='Corrective Action', help='Describe corrective actions to do')

    action_preventive = fields.Html(
        string='Preventive Action', help='Describe preventive actions to do')

    ticket_qty = fields.Integer(
        string='Ticket Qty', compute='_compute_ticket_qty')

    tag_name = fields.Char(
        string='Tag name',
    )

    def create_tag(self):
        self.ensure_one()

        # Opción 1
        self.write({
            'tag_ids': [(0, 0, {'name': self.tag_name})]
        })

    @api.depends('user_id')
    def _compute_ticket_qty(self):
        self.ticket_qty = self.env['helpdesk.ticket'].search_count(
            [('user_id', '=', self.user_id.id)])

    def do_assign(self):
        self.ensure_one()
        self.write({
            'state': 'asignado',
            'assigned': True
        })

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

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = record.user_id and True or False


class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Action'

    name = fields.Char()
    date = fields.Date()
    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='Ticket'
    )


class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = 'Tag'

    name = fields.Char()
    date = fields.Date()
    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='Ticket'
    )

    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_tag_rel',
        column1='tag_id',
        column2='ticket_id',
        string='Tags'
    )
