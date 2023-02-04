from django.db import models

class Shop(models.Model):
    model = models.CharField('Модель продукта',max_length=100,blank=True,null=True)
    type = models.CharField('Тип продукта',max_length=100,blank=True,null=True)
    price = models.FloatField('Цена')
    description = models.TextField('Описание',max_length=1000,default='Description is Empty')
    image = models.ImageField('Фото',upload_to='upload/',blank=True,null=True)
    image1 = models.ImageField('Фото',upload_to='upload/',blank=True,null=True)
    image2 = models.ImageField('Фото',upload_to='upload/',blank=True,null=True)
    image3 = models.ImageField('Фото',upload_to='upload/',blank=True,null=True)
    digital = models.BooleanField('В наличии',default=False)
    cart = models.BooleanField('В карзине',default=False)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
