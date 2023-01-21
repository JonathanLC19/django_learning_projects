from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'Name', 'username': 'User name'}

    def __init__(self, *args, **kwargs):
        super(CustomRegistrationForm, self).__init__(*args, **kwargs)

        #--------- añadimos estilo a los campos del form desde el método con un dict que pasa la clase 
        # como key y el tipo 'input' como value para que identifique el campo como un input---------
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        #----------- de este modo lo podemos hacer campo por campo -------------
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})
