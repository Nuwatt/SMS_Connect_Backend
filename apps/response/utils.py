from apps.core.utils import generate_filename


def upload_answer_image_to(instance, filename):
    """
    Returns path to upload to
    :param instance: instance of model
    :param filename: original filename
    :return: path
    """
    return 'answer/{}'.format(
        generate_filename(
            filename=filename,
            keyword='answer'
        )
    )
