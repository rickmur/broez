from django.contrib import admin
from login.models import User, Role, RoleMap

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(RoleMap)
