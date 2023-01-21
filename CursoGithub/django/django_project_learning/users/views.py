from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomRegistrationForm

# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=request.POST['username']).exists():
            # try:
            #     user = User.object.get(username=username)
            # except:
            #     if username is None:
            #         messages.error(request, 'User does not exist')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profiles')
            else:
                messages.error(request, "Username OR password is incorrect")
        else: messages.error(request, "Username doesn't exist")

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User succesfully logged out')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomRegistrationForm()

    if request.method == 'POST':  
        form = CustomRegistrationForm(request.POST)
        # antes de finalizar el registro, guardamos en una variable 'user' y lo pasamos por la función 'lower'
        # para evitar confusión y duplicidad de usernames por las mayúsculas  
        if form.is_valid(): 
            user = form.save(commit=False)
            user.username = user.username.lower()
            # ahora ya se puede generar el usuario
            user.save()

            messages.success(request, 'Account created successfully')

            login(request, user)
            return redirect('profiles')

        else:
            messages.error(request, 'An error occurred during registration')


    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)




def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}

    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    user_profile = Profile.objects.get(id=pk)

    # los modulos Profile y Skills están relacionados con la fk. Con 'skills_set' traemos el 
    # conjunto de skills relacionadas con el 'user_profile' seleccionado y las filtra, primero
    # por las que tienen descripcion (las excluye) y, segundo, por las que no (las incluye)
    top_skills = user_profile.skills_set.exclude(description__exact="")
    other_skills = user_profile.skills_set.filter(description="")

    context = {'profile': user_profile,'topSkills': top_skills, 'otherSkills': other_skills}

    return render(request, 'users/user_profile.html', context)


# con el decorador 'login_required' y añadiendo la variable 'profile' haciendo un request de la info del usuario
# no sería necesario pasar el parámetro 'pk' en la vista como hacemos en las otras (xej.: userProfile)
@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    context = {'profile': profile}

    return render(request, 'users/account.html', context)
    