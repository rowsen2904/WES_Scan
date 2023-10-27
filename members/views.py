from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    UpdateView,
)
from django.utils.translation import gettext as _

from .models import Member


def redirect_view(request):
    return redirect("members-list")


class MemberListView(ListView):
    context_object_name = "members"
    queryset = (Member.objects.all()
                .prefetch_related("specializations")
                .order_by("last_activity"))
    template_name = "members/list.html"
    extra_context = {
        "title": _("WES Members")
    }
