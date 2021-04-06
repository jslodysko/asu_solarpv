from django.db import models

# Create your models here.
class Product(models.Model):
    cell_manufacturer = models.CharField(max_length=50, blank=True, null=True)
    cell_technology = models.CharField(max_length=50, blank=True, null=True)
    encapsulation_manufacturer = models.CharField(max_length=50, blank=True, null=True)
    encapsulation_type = models.CharField(max_length=50, blank=True, null=True)
    frame_adhesive = models.CharField(max_length=50, blank=True, null=True)
    frame_type = models.CharField(max_length=50, blank=True, null=True)
    junction_box_manufacturer = models.CharField(max_length=50, blank=True, null=True)
    junction_box_type = models.CharField(max_length=50, blank=True, null=True)
    model_number = models.PositiveIntegerField(blank=True, null=True)
    number_of_cells = models.PositiveIntegerField(blank=True, null=True)
    number_of_cells_in_series = models.PositiveIntegerField(blank=True, null=True)
    number_of_diodes = models.PositiveIntegerField(blank=True, null=True)
    number_of_series_strings = models.PositiveIntegerField(blank=True, null=True)
    product_length = models.PositiveIntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    product_weight = models.PositiveIntegerField(blank=True, null=True)
    product_width = models.PositiveIntegerField(blank=True, null=True)
    substrate_type = models.CharField(max_length=50, blank=True, null=True)
    substrate_manufacturer = models.CharField(max_length=50, blank=True, null=True)
    superstrate_type = models.CharField(max_length=50, blank=True, null=True)
    superstrate_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.product_name

class Certificate(models.Model):

    certification_number = models.PositiveIntegerField(blank=True, null=True)
    cert_id = models.PositiveIntegerField(blank=True, null=True)
    issue_date = models.CharField(max_length=50, blank=True, null=True)
    model_number = models.PositiveIntegerField(blank=True, null=True)
    report_number = models.PositiveIntegerField(blank=True, null=True)
    standard_id = models.PositiveIntegerField(blank=True, null=True)
    userID = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'certificate'

    def __str__(self):
        return self.certification_number
    


class Service(models.Model):
    
    description = models.CharField(max_length=50, blank=True, null=True)
    FI_frequency = models.CharField(max_length=50, blank=True, null=True)
    is_FI_required = models.SmallIntegerField(blank=True, null=True)
    service_id = models.PositiveIntegerField(blank=True, null=True)
    service_name = models.CharField(max_length=50, blank=True, null=True)
    standard_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'service'