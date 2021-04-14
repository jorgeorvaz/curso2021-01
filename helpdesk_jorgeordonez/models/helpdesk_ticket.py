from odoo import fields, models


class HelpdeskTicket(models.Model):
    # nombre de la tabla en bbdd
    _name = 'helpdesk.ticket'
    _description = 'Ticket'

    # string es para el nombre de la vista en odoo. el nombre de la variable es para bbdd
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')

    # - Añadir los siguiente campos:
    # - Estado [Nuevo, Asignado, En proceso, Pendiente, Resuelto, Cancelado], que por defecto sea Nuevo
    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('asignado', 'Asignado'),
        ('en_proceso', 'En proceso'),
        ('pendiente', 'Pendiente'),
        ('resuelto', 'Resuelto'),
        ('cancelado', 'Cancelado')
    ], string='State', default='nuevo')
    # - Tiempo dedicado (en horas)
    time = fields.Float(string='Time')
    # - Asignado (tipo check)
    assigned = fields.Boolean(string='Assigned', readonly=True)
    # - Fecha límite
    date_limit = fields.Date(string='Date Limit')
    # - Acción correctiva (html)
    action_corrective = fields.Html(
        string='Corrective Action', help='Describe corrective actions to do')
    # - Acción preventiva (html)
    action_preventive = fields.Html(
        string='Preventive Action', help='Describe preventive actions to do')
    # El campo nombre que sea obligatorio
    # En algún campo añadir un texto de ayuda indicando su funcionalidad, luego revisar que funciona.
    # El campo Asignado:
    # - hacer que sea solo de lectura
