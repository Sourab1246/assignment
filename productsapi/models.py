from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=200)
    MRP=models.PositiveIntegerField()
    ratings=models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)],default=1)
    qty=models.PositiveIntegerField(verbose_name="quantity")
    image=models.URLField()
    in_stocks=models.BooleanField(default=True)
    description=models.TextField()
    product_types=[('clothing','clothing'),
                   ('sports','sports'),
                   ('electronics','electronics'),
                   ('books','books'),
                   ('HomeDecor','HomeDecor')]
    types=models.CharField(max_length=20,choices=product_types)

    def __str__(self) :
        return self.name
    
