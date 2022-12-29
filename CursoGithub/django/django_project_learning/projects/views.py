from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects

# Create your views here.


"""Trabajar un for loop en template con una lista de diccionarios añadiendo la lista a 'context' dentro de la vista """
"""con key 'projects' y values como el nombre de la lista (línea 33)"""
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    # """Pasar variables desde views que renderizar en templates"""
    # msg = "Hola qué disse"

    # """Pasar conjunto de variables para ejecutar funciones lógicas en templates (If, for,...)"""
    # number = 10
    # context = {'message': msg, 'number': number, 'projects': projectsList}

    # ------------------------------------------------------------------------------------------------------

    """Pasar valores a templates con Queries en módulos. Vídeo 'Database Queries' """
    projects = Projects.objects.all()

    context = {'projects': projects}

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    # """renderizando un proyecto en el template basado en el key 'id', que pasaremos con el parámetro 'pk' de la vista"""
    # projectObj = None
    # for i in projectsList:
    #     if i['id'] == pk:
    #         projectObj = i

    # ------------------------------------------------------------------------------------------------------ 

    """renderizar proyecto en template haciendo una query que nos dé el 'id' del proyecto, que se pasará con el parámetro 'pk'. Vídeo 'Database Queries' """
    projectObj = Projects.objects.get(id=pk)

    context = {'project': projectObj}

    return render(request, 'projects/single-project.html', context)
