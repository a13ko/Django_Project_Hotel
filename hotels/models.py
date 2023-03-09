from django.db import models
from ckeditor.fields import RichTextField
from services.choiches import room_type
from services.mixin import SlugMixin, DateMixin
from services.slugify import slugify
from services.generator import CodeGenerator
from services.uploader import Uploader
from mptt.models import TreeForeignKey, MPTTModel
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(DateMixin, SlugMixin, MPTTModel):
    name = models.CharField(max_length=300)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.code = CodeGenerator.create_slug_shortcode(
            size=20, model_=Category
        )
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)



class Hotel(SlugMixin, DateMixin):
    name = models.CharField(max_length=200)
    address = RichTextField(blank = True, null = True)
    country = models.CharField(max_length=200, blank=True, null=True)
    

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    def save(self, *args, **kwargs):
        self.code = CodeGenerator.create_slug_shortcode(
            size=20, model_=Hotel
        )
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    

class Room(SlugMixin,DateMixin):
    room_no = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    type = models.CharField(max_length=200, choices=room_type)
    benefits = RichTextField(blank=True, null=True)
    person_count = models.PositiveIntegerField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} - {self.type} - No: {self.room_no}"

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def save(self, *args, **kwargs):
        self.code = CodeGenerator.create_slug_shortcode(
            size=20, model_=Room
        )
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class RoomGallery(DateMixin):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.upload_image_room)

    def __str__(self) -> str:
        return self.room.type
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Room Gallery'
        verbose_name_plural = 'Room Galleries'



class HotelGallery(DateMixin):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.upload_image_hotel)

    def __str__(self) -> str:
        return self.hotel.name
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Hotel Gallery'
        verbose_name_plural = 'Hotel Galleries'


class Reservation(SlugMixin, DateMixin):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    guest_name = models.CharField(max_length=200, blank=True, null=True)
    guest_email = models.EmailField(blank=True, null=True)

    def __str__(self) -> str:
        return self.hotel.name
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
