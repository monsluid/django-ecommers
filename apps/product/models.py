from django.db import models
#from django.contrib.postgres.fields import ArrayField


# ------------------------------------------------------------------------------------>
# Model Category

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self .name


# ------------------------------------------------------------------------------------>
# Model Brand


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------------>
# Model State


class State(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'State'

    def __str__(self):
        return self.name

# ------------------------------------------------------------------------------------>
# Model Product

def product_directory_path(instance, filename):
    return 'product/{}/{}'.format(instance.name,filename)

class Product(models.Model):
    idProduct = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default = True)
    picture = models.ImageField(upload_to=product_directory_path, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=1)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    def __str__(self):
        return self .name

   




