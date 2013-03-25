from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    def __unicode__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def user_presave(sender, instance, **kwargs):
    if instance.last_login:
        try:
            old = instance.__class__.objects.get(pk=instance.pk)
            if instance.last_login != old.last_login:
                instance.userlogin_set.create(timestamp=instance.last_login)
        except User.DoesNotExist:
            pass


post_save.connect(create_user_profile, sender=User)
pre_save.connect(user_presave, sender=User)