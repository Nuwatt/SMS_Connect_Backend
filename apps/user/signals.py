from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.core.usecases import User
from apps.user.models import AgentUser, PortalUser


@receiver(post_save, sender=User)
def create_agent_user(sender, instance, **kwargs):
    user = instance
    if user.is_agent_user and not hasattr(user, 'agentuser'):
        AgentUser.objects.create(user=user)


@receiver(post_save, sender=User)
def create_portal_user(sender, instance, **kwargs):
    user = instance
    if user.is_portal_user and not hasattr(user, 'portaluser'):
        PortalUser.objects.create(user=user)


@receiver(post_save, sender=PortalUser)
def archive_portal_user(sender, instance, **kwargs):
    user = instance.user
    user.is_archived = instance.is_archived
    user.save()


@receiver(post_save, sender=AgentUser)
def archive_agent_user(sender, instance, **kwargs):
    user = instance.user
    user.is_archived = instance.is_archived
    user.save()
