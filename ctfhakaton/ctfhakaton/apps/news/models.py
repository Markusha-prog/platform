from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):
    """ Новости """
    name = models.CharField('Название новости', max_length=100, blank=True, null=True)
    photo = models.ImageField(verbose_name='Превью новости', upload_to='news/%Y/%m/%d',
                              blank=True, null=True)
    text = RichTextUploadingField('Text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'