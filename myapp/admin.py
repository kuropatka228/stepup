from django.contrib import admin
from.models import *


admin.site.register(Shoes)
admin.site.register(TopSneaker)
admin.site.register(TopSneakerCategory)

class SneakerCollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    filter_horizontal = ('sneakers',)

admin.site.register(SneakerCollection, SneakerCollectionAdmin)

class SneakerSizeInline(admin.TabularInline):
    model = SneakerSize
    extra = 1

class SneakerAdmin(admin.ModelAdmin):
    inlines = [SneakerSizeInline]

admin.site.register(Sneaker, SneakerAdmin)