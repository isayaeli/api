from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Beat)
admin.site.register(Instrument)
admin.site.register(Guitar)
admin.site.register(Piano)
admin.site.register(Marimba)
admin.site.register(Trumpets)
admin.site.site_header = 'Beat admn'