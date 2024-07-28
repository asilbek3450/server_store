from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product Categories'


class Product(models.Model):
    name = models.CharField(max_length=256)
    model_name = models.CharField(max_length=256)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image_url = models.URLField()

    description = models.TextField(blank=True, null=True)
    image_file = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.image_file:
            self.image_url = self.image_file.name
        super().save(*args, **kwargs)

