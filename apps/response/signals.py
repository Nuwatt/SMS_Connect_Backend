from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from apps.market.models import Store
from apps.response.models import Response, ResponseCycle


# @receiver(post_save, sender=ResponseCycle)
# def response_cycle_completed(sender, instance, **kwargs):
#     if instance.is_completed:
#         agent_user = instance.agent
#         response_count = agent_user.responsecycle_set.filter(
#             is_completed=True
#         ).aggregate(count=Count('questionnaire', distinct=True)).get('count')
#         agent_user.total_completed_questionnaire = response_count
#         agent_user.save()


@receiver(post_save, sender=Response)
def complete_response_cycle(sender, instance, **kwargs):
    if instance.is_completed:
        response_cycle = instance.response_cycle
        questionnaire = response_cycle.questionnaire
        questionnaire_stores = Store.objects.filter(city__questionnaire=questionnaire).count()
        completed_stores = response_cycle.response_set.filter(
            is_completed=True,
        ).aggregate(store_count=Count('store')).get('store_count')

        if questionnaire_stores == completed_stores:
            response_cycle.is_completed = True
            response_cycle.completed_at = now()
            response_cycle.save()
