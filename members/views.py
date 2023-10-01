from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    UpdateView,
)

from .models import Member


def redirect_view(request):
    return redirect("members-list")


class MemberListView(ListView):
    queryset = Member.objects.all()
    template_name = "members/list.html"