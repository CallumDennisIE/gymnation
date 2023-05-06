from django.shortcuts import render
from django.views import generic
from .models import Session


class SessionList(generic.ListView):
    model = Session
    queryset = Session.objects.order_by('-created_on')
    template_name = 'classes.html'
    paginate_by = 6


def get_about_page(request):
    return render(request, 'about.html')


def get_our_team_page(request):
    return render(request, 'our_team.html')


def get_classes_page(request):
    return render(request, 'classes.html')


def get_contact_us_page(request):
    return render(request, 'contact_us.html')


def get_shop_page(request):
    return render(request, 'shop.html')
