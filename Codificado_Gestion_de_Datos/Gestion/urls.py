from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("agregar/<str:select_form>/", views.add, name="add"),
    path("eliminar/<int:id_class>,<str:select_class>/", views.delet, name="delet"),
    path("editar/<int:id_class>,<str:select_class>/", views.edit, name="edit"),
    path("consulta/<str:select_consult>/", views.consult_dev, name="consult"),
]