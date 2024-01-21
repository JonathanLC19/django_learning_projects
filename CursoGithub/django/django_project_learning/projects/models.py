from django.db import models
import uuid
from users.models import Profile

# from django.apps import apps

# Create your models here.


class Projects(models.Model):
    owner = models.ForeignKey(Profile, null= True, blank= True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null= True, blank= True)
    featured_image = models.ImageField(default='default_logo.png', null= True, blank= True)
    demo_link = models.CharField(max_length=2000, null= True, blank= True)
    source_link = models.CharField(max_length=2000, null= True, blank= True)

    # crear un atributo para relación 'Many to Many' con el objeto Tag
    tags = models.ManyToManyField('Tag', blank=True)

    # crear dos atributos que cuenten los votos y el ratio de positivos y negativos
    vote_total = models.IntegerField(default=0, null= True, blank= True)
    vote_ratio = models.IntegerField(default=0, null= True, blank= True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    """creamos una tupla de tuplas 'VOTE_TYPE' que será las opciones de elección para el atributo 'value' añadidas con parámetro 'choices'. """
    """el 1er valor de la tupla será el valor y el 2º el string que se muestra"""
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    # owner =
    project_fk = models.ForeignKey(Projects, on_delete=models.CASCADE)
    body = models.TextField(null= True, blank= True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name



"""--------------- TIMETRACKER -------------------"""


class TimeTracker(models.Model):
    project = models.OneToOneField(Projects, on_delete=models.CASCADE, related_name='time_tracker')
    total_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'TimeTracker for {self.project.title}'

# # Importa 'Projects' en el nivel donde lo necesites, no en la parte superior del archivo.
# Projects = apps.get_model('projects', 'Projects')