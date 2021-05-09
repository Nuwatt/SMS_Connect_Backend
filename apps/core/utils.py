from django.utils import timezone
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta


def generate_custom_id(initial: str, model):
    try:
        last_record = model.objects.latest('created')

        last_record_id = '{0:04}'.format(
            int(last_record.id[len(initial):]) + 1
        )
        custom_id = '{}{}'.format(
            initial,
            last_record_id
        )
    except model.DoesNotExist:
        custom_id = '{}0001'.format(
            initial,
        )

    return custom_id


def update(instance, data):
    info = model_meta.get_field_info(instance)

    for attr, value in data.items():
        if attr in info.relations and info.relations[attr].to_many:
            field = getattr(instance, attr)
            field.set(value)
        else:
            setattr(instance, attr, value)
    instance.updated = timezone.now()
    instance.save()

