from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from solo.models import SingletonModel
from django.db import models


class Homepage(SingletonModel):
    show_section_background = models.ImageField(upload_to='backgrounds/', null=True)
    homepage_background = models.ImageField(upload_to='backgrounds/', null=True)
    header_en = RichTextField(null=True)
    subheader_en = models.CharField(null=True, blank=True, max_length=255)
    btn_text_en = models.CharField(null=True, blank=True, max_length=255)
    header_ar = RichTextField(null=True)
    subheader_ar = models.CharField(null=True, blank=True, max_length=255)
    btn_text_ar = models.CharField(null=True, blank=True, max_length=255)
    btn_color = ColorField()
    description_en = RichTextField(null=True)
    category_title_en = models.CharField(null=True, blank=True, max_length=255)
    category_description_en = RichTextField(null=True)
    furniture_title_en = models.CharField(null=True, blank=True, max_length=255)
    furniture_description_en = RichTextField(null=True)
    description_ar = RichTextField(null=True)
    category_title_ar = models.CharField(null=True, blank=True, max_length=255)
    category_description_ar = RichTextField(null=True)
    furniture_title_ar = models.CharField(null=True, blank=True, max_length=255)
    furniture_description_ar = RichTextField(null=True)
    mobile = models.CharField(max_length=20)
    other_phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    address_en = RichTextField(null=True , help_text="Address [English]")
    address_ar = RichTextField(null=True , help_text="Address [Arabic]")
    facebook_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)

    class Meta(SingletonModel.Meta):
        pass

    def __str__(self):
        return f"{self.email}"

    def categories(self):
        from furniture.models.category_model import Category
        return Category.objects.all()

    def furniture(self):
        from furniture.models.furniture_model import Furniture
        return Furniture.objects.order_by('-offer_value').filter(is_for_offer=True)[:4]
