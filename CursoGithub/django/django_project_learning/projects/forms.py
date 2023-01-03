from django.forms import ModelForm
from .models import Projects

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'featured_image','demo_link', 'source_link', 'tags']


