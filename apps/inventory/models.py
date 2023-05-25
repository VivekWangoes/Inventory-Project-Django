from django.db import models

# Create your models here.


class StockList(models.Model):
    stock_id = models.CharField(max_length=15)
    part_number = models.CharField(max_length=50)
    part_stripped = models.CharField(max_length=50)
    consignment_code = models.CharField(max_length=25, null=True)
    consignment_code_secondary = models.CharField(max_length=25, null=True)
    ac_eng_serial = models.CharField(max_length=25, null=True)
    serial_number = models.CharField(max_length=50, null=True)
    serial_number_fake = models.CharField(max_length=50, null=True)
    serial_number_display = models.CharField(max_length=50, null=True)
    applicability = models.CharField(max_length=50, null=True)
    quantity = models.PositiveIntegerField(null=True)
    condition_code = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=150, null=True)
    lot_number = models.CharField(max_length=10, null=True)
    lot_padded = models.CharField(max_length=15, null=True)


class PictureList(models.Model):
    picture_number = models.CharField(max_length=10)
    file_name = models.CharField(max_length=14)
    category = models.CharField(max_length=30, null=True)
    sub_category = models.CharField(max_length=30, null=True)
    image_url = models.CharField(max_length=150)
    original_file_name = models.CharField(max_length=30)
    batch_name = models.CharField(max_length=30)
    stock_line = models.ForeignKey(StockList, null=True, on_delete=models.PROTECT,
        related_name="stock_line")
    stock_line_matched = models.BooleanField(default=False)


class WorkerBatch(models.Model):
    batch_name = models.CharField(max_length=200, null=True)
    batch_file_name = models.CharField(max_length=200)


class WorkerData(models.Model):
    picture_id = models.ForeignKey(PictureList, on_delete=models.SET_NULL, null=True)
    batch_id = models.ForeignKey(WorkerBatch, on_delete=models.SET_NULL, null=True)
    hit_id = models.CharField(max_length=100)
    hit_type_id = models.CharField(max_length=100)
    assignment_id = models.CharField(max_length=100)
    worker_id = models.CharField(max_length=100)
    assignment_status = models.CharField(max_length=40)
    image_url = models.CharField(max_length=150)
    picture_number = models.CharField(max_length=10)
    part_number = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    ac_eng_serial = models.CharField(max_length=200)
    consignment_code = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    part_number_correct = models.BooleanField(default=True)
    part_number_entered = models.BooleanField(default=True)
    serial_number_correct = models.BooleanField(default=True)
    serial_number_entered = models.BooleanField(default=True)
    ac_eng_serial_correct = models.BooleanField(default=True)
    ac_eng_serial_entered = models.BooleanField(default=True)
    consignment_code_correct = models.BooleanField(default=True)
    consignment_code_entered = models.BooleanField(default=True)
    bonus_difficult_to_read = models.BooleanField(default=False)
    bonus_inferred_info = models.BooleanField(default=False)
    no_match_available = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)
    completed_time = models.DateTimeField(null=True)
    match_score = models.PositiveBigIntegerField(default=50)

