from django.views.generic.list import ListView

from services.models import Service


class HomeView(ListView):
    model = Service
    template_name = "pages/home.html"

    def get_queryset(self):
        return Service.objects.filter(active=True)
