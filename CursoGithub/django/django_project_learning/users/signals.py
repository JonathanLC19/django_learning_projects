from .models import Profile
from django.contrib.auth.models import User


# importar Django Signal para notificaciones en acciones concretas: https://docs.djangoproject.com/en/4.1/ref/signals/
from django.db.models.signals import post_save, post_delete

# usar django signals con decorators (mejor)
from django.dispatch import receiver



# ------------------------------------- DJANGO SIGNALS ----------------------------------------------

## Función para enviar notif. con Django Signals después de actualizar un usuario
# def profileUpdated(sender, instance, created, **kwargs):
#     print('Profile saved')
#     print('Instance: ', instance)
#     print('Created: ', created)

# post_save.connect(profileUpdated, sender=Profile) 
# -> comentamos después de prueba inicial para hacerlo con decorators


## Función para enviar notif. con Django Signals después de actualizar un usuario
# def deleteUser(sender, instance, **kwargs):
#     print('Deleting user...')
#     print('Instance: ', instance)

# post_delete.connect(deleteUser, sender=Profile) -> comentamos después de prueba inicial para hacerlo con decorators


## Django signals con decorators

# @receiver(post_save, sender=Profile)
# def profileUpdated(sender, instance, created, **kwargs):
#     print('Profile saved')
#     print('Instance: ', instance)
#     print('Created: ', created)

@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    # lee el atributo user de Profile para hacer match con el usuario y eliminia el usuario también
    user = instance.user
    user.delete()

    print('Deleting user...')
    print('Instance: ', instance)


## usar Signals para crear un Profile cada vez que se dé de alta un usuario nuevo
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    # aquí la función lee si created es True, esto quiere decir que el user es nuevo
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
            )
        print(f"The user {user} has been created")

    else:
        print(f"The user {instance} has been updated")

# post_save.connect(createProfile, sender=User)