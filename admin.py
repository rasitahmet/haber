from haber.models import Haber, Resim
from django.contrib import admin

class ResimInline(admin.StackedInline):
    model = Resim
    extra = 3

class HaberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['baslik','slug','aciklama']}),
        (None,               {'fields': ['icerik']}),
        ('Yayinlanma Tarihi', {'fields': ['yay_tarihi'], 'classes': ['collapse']}),
    ]
    inlines = [ResimInline]
    prepopulated_fields = {'slug': ('baslik',)}
    list_display = ('baslik', 'aciklama', 'en_son_yayinlanan')
    list_filter = ['yay_tarihi']
    search_fields = ['baslik','aciklama','icerik']
    date_hierarchy = 'yay_tarihi'

admin.site.register(Haber, HaberAdmin)
