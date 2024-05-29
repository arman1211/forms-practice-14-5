from django.db import models


# Create your models here

class ModelForms(models.Model):
    auto_field = models.AutoField(primary_key=True)
    boolean_field = models.BooleanField()
    binary_field = models.BinaryField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField()
    # file_path_field = models.FilePathField()
    float_field = models.FloatField()
    generic_ip_address_field = models.GenericIPAddressField()
    # image_field = models.ImageField()
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    positive_big_integer_field = models.PositiveBigIntegerField()
    slug_field = models.SlugField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()


