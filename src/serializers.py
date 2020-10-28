import datetime

from .models import LinksPair


def links_pair_api_serializer(pair: LinksPair) -> dict:
    serialized_pair = pair.to_dict()

    return serialized_pair


def links_pair_frontend_serializer(pair: LinksPair) -> dict:
    serialized_pair = pair.to_dict()

    original_url = pair.original_url
    protocol = '' if 'http' in original_url else 'https://'
    serialized_pair['redirect_url'] = protocol + original_url

    serialized_pair['expires_on'] = pair.date_created + datetime.timedelta(days=pair.days_limit)

    return serialized_pair
