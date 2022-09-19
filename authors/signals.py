from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from authors.models import Profile

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    print('Signal chamado', instance.username, created)
    if created: #se usuário acabou de ser criado
        profile = Profile.objects.create(author=instance) # criação de um perfil 
        profile.save()

