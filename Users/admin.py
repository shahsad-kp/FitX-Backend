from django.contrib import admin

from Users.models import User, Height, Weight, BurnedCalorie

admin.site.register(User)
admin.site.register(Height)
admin.site.register(Weight)
