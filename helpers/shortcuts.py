from django.db import models
from django.http.response import Http404
from django.utils.translation import gettext as _

from rest_framework.response import Response


def get_object_from_qs_or_404(qs: models.QuerySet, **kwargs) -> models.QuerySet:
    try:
        return qs.objects.get(**kwargs)
    except qs.DoesNotExist as exc:
        raise Http404 from exc
