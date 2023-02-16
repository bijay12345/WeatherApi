from django.contrib import admin
from .models import User,Weather
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):

	list_display=("id","email","name","is_admin")
	list_filter = ("is_admin",)

	fieldsets=(
		("User Credential",{"fields":("name","password")}),
		("Personal Info",{"fields":("email",)}),
		("permissions",{"fields":("is_admin",)}),
		)

	add_fieldsets = (
			(None,{
				"classes":("wide",),
				"fields":("name","email","password1","password2"),
				}),
		)
	search_fields = ("name","id")
	ordering = ("name","id")
	filter_horizontal=()


admin.site.register(User,UserModelAdmin)
admin.site.register(Weather)