from django import forms
from .models import *

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = {'name'}

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = {'name'}

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = {'name','last_name','addres',
        'number_phone','id_location_connect'}

class MatterForm(forms.ModelForm):
    class Meta:
        model = Matter
        fields = {'name','id_career','id_teacher'}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {'title','content'}