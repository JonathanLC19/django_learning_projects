from django.shortcuts import render
from .models import Profile

# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}

    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    user_profile = Profile.objects.get(id=pk)
    context = {'profile': user_profile}

    return render(request, 'users/user_profile.html', context)
    