from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', unique=True)
    slug =models.SlugField(max_length=150, primary_key=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Product(models.Model):

    STATUS_CHOICES = (
        ('в наличии',('в наличии')),
        ('на складе', ('на складе')),
        ('нет в наличии',('нет в наличии')),

    )
    title = models.CharField(max_length=255, verbose_name='Название')
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='product')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS_CHOICES, default='в наличии', max_length=18)
    



    def __str__(self):
        return self.title
