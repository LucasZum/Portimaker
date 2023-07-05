from django.contrib import admin

from .models import Coliseum, Fortress, Pyramid, User

# Register your models here.
admin.site.register(User)
admin.site.register(Coliseum)
admin.site.register(Fortress)
admin.site.register(Pyramid)