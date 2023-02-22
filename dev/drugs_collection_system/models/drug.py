from odoo import api, fields, models


class CollectedDrug(models.Model):
    _name = "collected.drug"
    _description = "Collected Drug Records"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    drug_type = fields.Selection(
        [("tablet", "Tablet"), ("syrup", "Syrup"), ("capsule", "Capsule")],
        string="Drug Type",
        required=True,
    )
    drug_price = fields.Float(string="Drug Price", required=True)
    drug_quantity = fields.Integer(string="Drug Quantity", required=True)
    drug_image = fields.Binary(string="Drug Image")

    def get_image(self):
        return self.drug_image

    def get_image_name(self):
        return self.drug_image_name

    def get_image_type(self):
        return self.drug_image_type
