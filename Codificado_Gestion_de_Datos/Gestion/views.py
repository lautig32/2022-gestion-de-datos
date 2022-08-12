from django.shortcuts import redirect, render
from .models import *
from .forms import *
import MySQLdb

def home(request):
    obj_career = Career.objects.all()
    obj_location = Location.objects.all()
    obj_teacher = Teacher.objects.all()
    obj_matter = Matter.objects.all()
    context = {'obj_career': obj_career, 'obj_location': obj_location, 'obj_teacher': obj_teacher, 'obj_matter': obj_matter}
    return render(request, 'gestion/home.html', context)

def add(request, select_form):
    if select_form == "career":
        if request.method == "POST":
            form = CareerForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = CareerForm()
    if select_form == "location":
        if request.method == "POST":
            form = LocationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = LocationForm()
    if select_form == "teacher":
        if request.method == "POST":
            form = TeacherForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = TeacherForm()
    if select_form == "matter":
        if request.method == "POST":
            form = MatterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = MatterForm()
    context = {'form' : form}
    return render(request, 'gestion/add.html', context)

def delet(request, id_class, select_class):
    if select_class == 'career':
        var_obj = Career.objects.get(id=id_class)
        var_obj.delete()
    if select_class == 'location':
        var_obj = Location.objects.get(id=id_class)
        var_obj.delete()
    if select_class == 'teacher':
        var_obj = Teacher.objects.get(id=id_class)
        var_obj.delete()
    if select_class == 'matter':
        var_obj = Matter.objects.get(id=id_class)
        var_obj.delete()
    return redirect('home')
    
def edit(request, id_class , select_class):
    if select_class == 'career':
        var_obj = Career.objects.get(id=id_class)
        if request.method == "POST":
            form = CareerForm(request.POST, instance=var_obj)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = CareerForm(instance=var_obj)
    if select_class == 'location':
        var_obj = Location.objects.get(id=id_class)
        if request.method == "POST":
            form = LocationForm(request.POST, instance=var_obj)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = LocationForm(instance=var_obj)
    if select_class == 'teacher':
        var_obj = Teacher.objects.get(id=id_class)
        if request.method == "POST":
            form = TeacherForm(request.POST, instance=var_obj)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = TeacherForm(instance=var_obj)
    if select_class == 'matter':
        var_obj = Matter.objects.get(id=id_class)
        if request.method == "POST":
            form = MatterForm(request.POST, instance=var_obj)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = MatterForm(instance=var_obj)
    context = {'form': form} 
    return render(request, "gestion/edit.html", context)

def consult_dev(request, select_consult):
    if select_consult == 'a':
        db = MySQLdb.connect(user='root', db='mysql_server_gestiondedatos', passwd='1425', host='localhost')
        cursor = db.cursor()
        text = "select materia.name,materia.id,materia.id_career_id,carrera.name,docente.id,docente.name from mysql_server_gestiondedatos.gestion_matter  as materia inner join mysql_server_gestiondedatos.gestion_career  as carrera on carrera.id = materia.id_career_id inner join mysql_server_gestiondedatos.gestion_teacher as docente on docente.id = materia.id_teacher_id order by materia.name;"
        cursor.execute(text)
        names = [row for row in cursor.fetchall()]
        db.close()
    if select_consult == 'b':
        db = MySQLdb.connect(user='root', db='mysql_server_gestiondedatos', passwd='1425', host='localhost')
        cursor = db.cursor()
        text = "select materia.name,materia.id,materia.id_career_id,carrera.name,docente.id,docente.name from mysql_server_gestiondedatos.gestion_matter as materia inner join mysql_server_gestiondedatos.gestion_career  as carrera on carrera.id = materia.id_career_id inner join mysql_server_gestiondedatos.gestion_teacher as docente on docente.id = materia.id_teacher_id order by docente.id,materia.name;"
        cursor.execute(text)
        names = [row for row in cursor.fetchall()]
        db.close()
    if select_consult == 'c':
        db = MySQLdb.connect(user='root', db='mysql_server_gestiondedatos', passwd='1425', host='localhost')
        cursor = db.cursor()
        text = "select carrera.name as nombre,COUNT(materia.name) as cantidad_materias from mysql_server_gestiondedatos.gestion_matter  as materia,mysql_server_gestiondedatos.gestion_career  as carrera where materia.id_career_id = carrera.id group by carrera.name;"
        cursor.execute(text)
        names = [row for row in cursor.fetchall()]
        db.close()
    if select_consult == 'd':
        db = MySQLdb.connect(user='root', db='mysql_server_gestiondedatos', passwd='1425', host='localhost')
        cursor = db.cursor()
        text = "select docente.name as nombre_docente,COUNT(materia.name) as cantidad_materias from mysql_server_gestiondedatos.gestion_teacher as docente ,mysql_server_gestiondedatos.gestion_matter  as materia where materia.id_teacher_id = docente.id group by docente.name;"
        cursor.execute(text)
        names = [row for row in cursor.fetchall()]
        db.close()
    if select_consult == 'e':
        db = MySQLdb.connect(user='root', db='mysql_server_gestiondedatos', passwd='1425', host='localhost')
        cursor = db.cursor()
        text = "select materia.name,docente.name,localidad.name,docente.number_phone from mysql_server_gestiondedatos.gestion_matter  as materia inner join	mysql_server_gestiondedatos.gestion_teacher as docente on materia.id_teacher_id = docente.id inner join mysql_server_gestiondedatos.gestion_location as localidad on docente.id_location_connect_id = localidad.id order by materia.name;"
        cursor.execute(text)
        names = [row for row in cursor.fetchall()]
        db.close()
    if select_consult == 'f':
        db = MySQLdb.connect(user='root', db='mysql_server_gestiondedatos', passwd='1425', host='localhost')
        cursor = db.cursor()
        text = "select * from mysql_server_gestiondedatos.gestion_location as localidad  where localidad.id not in (select docente.id_location_connect_id from mysql_server_gestiondedatos.gestion_teacher as docente group by docente.id_location_connect_id);"
        cursor.execute(text)
        names = [row for row in cursor.fetchall()]
        db.close()
    context = {'names' : names, 'texto' : text}
    return render(request, 'gestion/consult_dev.html', context)