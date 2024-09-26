from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario

# Create your views here.
def crea_curso(req, nombre, camada):

    nuevo_curso = Curso(nombre=nombre, camada=camada)
    nuevo_curso.save()

    return HttpResponse(f"""
                        <p>Curso: {nuevo_curso.nombre} - Camada {nuevo_curso.camada} creado con exito!</p>""")

def lista_cursos(req):
    
    lista = Curso.objects.all()
    print("Cursos encontrados: ", lista)
    return render(req, "cursos.html", {"lista_cursos": lista})

def inicio(req):

    return render(req, "inicio.html", {})


def cursos(req):

    return render(req, "cursos.html", {})


def profesores(req):

    return render(req, "profesores.html", {})


def estudiantes(req):

    return render(req, "estudiantes.html", {})


def entregables(req):

    return render(req, "entregables.html", {})

def curso_formulario(req):

    print(req.method)
    print('data', req.POST)

    if req.method == 'POST':

        mi_formulario = CursoFormulario(req.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

             # Validaciones básicas
            errores = []

            # Verificar si el nombre está vacío
            if not data["curso"].strip():
                errores.append("El nombre del curso no puede estar vacío.")
            
            # Verificar si la camada es un número positivo
            if data["camada"] <= 0:
                errores.append("La camada debe ser un número positivo.")

            # Si hay errores, mostrar el formulario con los errores
            if errores:
                return render(req, "curso_formulario.html", {"mi_formulario": mi_formulario, "errores": errores})

            nuevo_curso = Curso(nombre=data["curso"], camada=data["camada"])
            nuevo_curso.save()
            #return render(req, "inicio.html", {})
            return render(req, "inicio.html", {"mensaje": f"Curso: {nuevo_curso.nombre} - Camada {nuevo_curso.camada} creado con éxito!"})
        else:
            return render(req, "curso_formulario.html", {"mi_formulario": mi_formulario})
        
    else:

        mi_formulario = CursoFormulario()
        return render(req, "curso_formulario.html", {"mi_formulario": mi_formulario})
    
def busqueda_camada(req):

    return render(req, "busqueda_camada.html")

def buscar_camada(req):

    num_camada = req.GET["camada"]

    cursos = Curso.objects.filter(camada__icontains=num_camada)

    return render(req, "resultado_busqueda.html", {"cursos": cursos, "camada": num_camada})

def profesorFormulario(request):

    if request.method == 'POST':

        miformulario = ProfesorFormulario(request.POST)
        print(miformulario)

        if miformulario.is_valid():

            data = miformulario.cleaned_data

            #  # Validaciones básicas
            # errores = []

            # # Verificar si el nombre está vacío
            # if not data["curso"].strip():
            #     errores.append("El nombre del curso no puede estar vacío.")
            
            # # Verificar si la camada es un número positivo
            # if data["camada"] <= 0:
            #     errores.append("La camada debe ser un número positivo.")

            # # Si hay errores, mostrar el formulario con los errores
            # if errores:
            #     return render(request, "curso_formulario.html", {"miformulario": miformulario, "errores": errores})

            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            profesor.save()
            return render(request, "inicio.html", {"mensaje": f"Nombre: {profesor.nombre} - Apellido: {profesor.apellido} creado con éxito!"})
        else:
            return render(request, "profesorFormulario.html", {"miformulario": miformulario})
        
    else:

        miformulario = ProfesorFormulario()
    return render(request, "profesorFormulario.html", {"miformulario": miformulario})

def lista_profesores(request):
    profesores = Profesor.objects.all()  # Obtener todos los profesores
    return render(request, "profesores.html", {"profesores": profesores})