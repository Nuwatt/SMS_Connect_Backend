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
