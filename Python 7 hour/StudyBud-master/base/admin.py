from django.contrib import admin

from .models import room, topic, message, user

# register your models here.

admin.site.register(user)
admin.site.register(room)
admin.site.register(topic)
admin.site.register(message)















