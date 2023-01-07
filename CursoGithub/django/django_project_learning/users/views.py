from django.shortcuts import render
from .models import Profile

# Create your views here.


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
    