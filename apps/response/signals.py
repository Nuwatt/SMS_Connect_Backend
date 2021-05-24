from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.response.models import Response


@receiver(post_save, sender=Response)
def response_complete(sender, instance, **kwargs):
    if instance.is_completed:
        agent_user = instance.agent
        response_count = agent_user.response_set.filter(
            is_completed=True
        ).aggregate(count=Count('questionnaire', distinct=True)).get('count')
        agent_user.total_completed_questionnaire = response_count
        agent_user.save()
