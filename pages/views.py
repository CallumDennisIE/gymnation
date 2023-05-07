from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Session
from .forms import ReviewForm


class SessionList(generic.ListView):
    model = Session
    queryset = Session.objects.order_by('-created_on')
    template_name = 'classes.html'
    paginate_by = 6


class SessionDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Session.objects
        session = get_object_or_404(queryset, slug=slug)
        reviews = session.reviews.order_by('created_on')
        attending = False
        if session.attendance.filter(id=self.request.user.id).exists():
            attending = True

        return render(
            request,
            "session_detail.html",
            {
                "session": session,
                "reviews": reviews,
                "attending": attending,
                "review_form": ReviewForm()
            },
        )


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
