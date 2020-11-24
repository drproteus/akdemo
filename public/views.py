from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.views.generic.base import TemplateView, View
from django.shortcuts import render
from random import randint
from public.models import Resource

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resources"] = Resource.objects.exclude(archived=True)
        return context

class Services(AKView):
    template_name = "public/services.html"

class Advantage(AKView):
    template_name = "public/advantage.html"

class Login(View):
    def get(self, request):
        return render(request, "public/login.html")

    def post(self, request):
        email, password = request.POST.get("inputEmail", ""), request.POST.get("inputPassword", "")
        user = authenticate(username=email, password=password)
        if user is None:
            messages.add_message(request, messages.ERROR, "Invalid email or password")
        else:
            login(request, user)
        return render(request, "public/base.html")

class Service(View):
    def get(self, request, slug):
        return render(request, f"public/services/{slug}.html")


class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, "public/base.html")
