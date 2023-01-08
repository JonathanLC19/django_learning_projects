from django.db import models
from django.contrib.auth.models import User
import uuid

# # importar Django Signal para notificaciones en acciones concretas: https://docs.djangoproject.com/en/4.1/ref/signals/

# from django.db.models.signals import post_save, post_delete

# # usar django signals con decorators (mejor)
# from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    email= models.EmailField(max_length=500,null=True, blank=True)
    username = models.CharField(max_length=200,null=True, blank=True)
    location = models.CharField(max_length=200,null=True, blank=True)
    short_intro = models.CharField(max_length=200,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user_default.png')
    social_github = models.CharField(max_length=200,null=True, blank=True)
    social_linkedin = models.CharField(max_length=200,null=True, blank=True)
    social_twitter = models.CharField(max_length=200,null=True, blank=True)
    social_youtube = models.CharField(max_length=200,null=True, blank=True)
    social_website = models.CharField(max_length=200,null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


class Skills(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

# # ------------------------------------- DJANGO SIGNALS ----------------------------------------------

# ## Función para enviar notif. con Django Signals después de actualizar un usuario
# # def profileUpdated(sender, instance, created, **kwargs):
# #     print('Profile saved')
# #     print('Instance: ', instance)
# #     print('Created: ', created)

# # post_save.connect(profileUpdated, sender=Profile) 
# # -> comentamos después de prueba inicial para hacerlo con decorators


# ## Función para enviar notif. con Django Signals después de actualizar un usuario
# # def deleteUser(sender, instance, **kwargs):
# #     print('Deleting user...')
# #     print('Instance: ', instance)

# # post_delete.connect(deleteUser, sender=Profile) -> comentamos después de prueba inicial para hacerlo con decorators


# ## Django signals con decorators

# # @receiver(post_save, sender=Profile)
# # def profileUpdated(sender, instance, created, **kwargs):
# #     print('Profile saved')
# #     print('Instance: ', instance)
# #     print('Created: ', created)

# @receiver(post_delete, sender=Profile)
# def deleteUser(sender, instance, **kwargs):
#     # lee el atributo user de Profile para hacer match con el usuario y eliminia el usuario también
#     user = instance.user
#     user.delete()

#     print('Deleting user...')
#     print('Instance: ', instance)


# ## usar Signals para crear un Profile cada vez que se dé de alta un usuario nuevo
# @receiver(post_save, sender=User)
# def createProfile(sender, instance, created, **kwargs):
#     # aquí la función lee si created es True, esto quiere decir que el user es nuevo
#     if created:
#         user = instance
#         profile = Profile.objects.create(
#             user = user,
#             username = user.username,
#             email = user.email,
#             name = user.first_name,
#             )
#         print(f"The user {user} has been created")

# # post_save.connect(createProfile, sender=User) 
         


