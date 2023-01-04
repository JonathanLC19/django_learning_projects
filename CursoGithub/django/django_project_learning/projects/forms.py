from django.forms import ModelForm
from django import forms
from .models import Projects

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'featured_image','demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        #--------- añadimos estilo a los campos del form desde el método con un dict que pasa la clase 
        # como key y el tipo 'input' como value para que identifique el campo como un input---------
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        #----------- de este modo lo podemos hacer campo por campo -------------
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})


