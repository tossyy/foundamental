from django.contrib import admin

from .models import CustomUser, UserDetailEntrepreneur, UserDetailCounselor


admin.site.register(CustomUser)
admin.site.register(UserDetailEntrepreneur)
admin.site.register(UserDetailCounselor)
