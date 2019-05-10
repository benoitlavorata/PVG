from odoo import models, fields, _

class accrNutritiontNotification(models.Model):
    _name="accr.nutrition.notification"
    _description = 'Nutrition Notifications'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student = fields.Many2one('accr.nutrition.student', string=u'student', readonly=True, required=False, )
    color = fields.Integer(string=u'Color')
    message = fields.Text(string=u'Message', readonly=True, )