from django.db.models import QuerySet

from .models import Link


def get(pk: int) -> Link:
    return Link.objects.get(pk=pk)


def get_user_links(user_pk: int) -> QuerySet:
    return Link.objects.filter(owner__pk=user_pk)
