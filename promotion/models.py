from django.db import models
from PIL import Image


class WeddingCard(models.Model):
    title = models.CharField(max_length=100)
    card_image = models.ImageField(upload_to='card_image')
    m_name = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ImagesToCard(models.Model):
    card = models.ForeignKey(WeddingCard, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='card_image')
    image_comment = models.TextField()

    def __str__(self):
        return 'images'
