from django.views.generic.base import TemplateView
from random import randint

class AKView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = self.__class__.__name__.lower()
        return context

class Home(AKView):
    template_name = "public/base.html"

class About(AKView):
    template_name = "public/about.html"

class Contact(AKView):
    template_name = "public/contact.html"

class Resources(AKView):
    template_name = "public/resources.html"

class Services(AKView):
    template_name = "public/services.html"

class Advantage(AKView):
    template_name = "public/advantage.html"
