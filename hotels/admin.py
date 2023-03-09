from django.contrib import admin
from .models import Hotel, Reservation, Room, HotelGallery, RoomGallery


class HotelImageInline(admin.TabularInline):
    model = HotelGallery
    extra = 1

class RoomImageInline(admin.TabularInline):
    model = RoomGallery
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    inlines = (HotelImageInline, )

class RoomAdmin(admin.ModelAdmin):
    inlines = (RoomImageInline, )

admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelGallery)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomGallery)
admin.site.register(Reservation)


