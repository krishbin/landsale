from django.contrib import admin
from .models import Land
from .views import create_land,update_land_form

class LandAdmin(admin.ModelAdmin):
    add_form = create_land
    form = update_land_form
    model = Land
    readonly_fields = ['location','info','area','area_unit','land_image','landownership_image','landownership_image_optional','longitude','latitude','price','is_house_or_apartment','total_no_of_rooms','no_of_bedroom','no_of_washroom','house_image']
    list_display = ('location','verified', 'area','area_unit','land_image','landownership_image','is_house_or_apartment','house_image','date_posted',)
    list_filter = ('location','verified', 'area','area_unit','date_posted',)
    fieldsets = (
    ('Land info', {'fields': ('location', 'info', 'area','area_unit','longitude','latitude','land_image','landownership_image','landownership_image_optional',)}),
    ('Permissions', {'fields': ('verified',)}),
    ('House/Apartment', {'fields': ('is_house_or_apartment','total_no_of_rooms','no_of_bedroom','no_of_washroom','house_image')}),
    )
    search_fields = ('location',)
    ordering = ('verified','date_posted',)

admin.site.register(Land,LandAdmin)
