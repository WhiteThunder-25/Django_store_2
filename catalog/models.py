from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание категории')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name', ]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Товар')
    description = models.TextField(verbose_name='Описание товара', help_text="Введите описание товара")
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение товара',
        help_text='Загрузите изображение товара',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        'category',
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Введите категорию',
        related_name='products',
        null=True,
        blank=True,
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена товара')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name',]
