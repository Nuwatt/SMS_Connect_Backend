from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from apps.core.utils import generate_filename


def encode_uid(pk):
    return force_str(urlsafe_base64_encode(force_bytes(pk)))


def decode_uid(pk):
    return force_str(urlsafe_base64_decode(pk))


def upload_avatar_to(instance, filename):
    """
    Returns path to upload to
    :param instance: instance of model
    :param filename: original filename
    :return: path
    """
    return 'avatar/{}'.format(
        generate_filename(
            filename=filename,
            keyword=instance.fullname
        )
    )
