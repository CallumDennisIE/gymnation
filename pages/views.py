from django.shortcuts import render


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
