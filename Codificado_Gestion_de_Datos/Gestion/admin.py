from django.contrib import admin

from Gestion.models import *

class CareerAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    fields = ("name",)
    ordering = ("id",)

class LocationAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    fields = ("name",)
    ordering = ("id",)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id","last_name","name","addres")
    fields = ("name","last_name","addres","number_phone","id_location_connect",)
    ordering = ("id",)


class MatterAdmin(admin.ModelAdmin):
    list_display = ("id","name","id_career","id_teacher")
    fields = ("name","id_career","id_teacher")
    ordering = ("id",)

class BlogAdmin(admin.ModelAdmin):
 
    def get_form(self, request, obj=None, **kwargs):
        form = super(BlogAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        return form
 
admin.site.register(Blog, BlogAdmin)

admin.site.register(Career, CareerAdmin)

admin.site.register(Location, LocationAdmin)

admin.site.register(Teacher, TeacherAdmin)

admin.site.register(Matter, MatterAdmin)
