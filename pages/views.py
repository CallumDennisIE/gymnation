from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect
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
                "reviewed": False,
                "attending": attending,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Session.objects
        session = get_object_or_404(queryset, slug=slug)
        reviews = session.reviews.order_by('created_on')
        attending = False
        if session.attendance.filter(id=self.request.user.id).exists():
            attending = True

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.session = session
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "session_detail.html",
            {
                "session": session,
                "reviews": reviews,
                "reviewed": True,
                "attending": attending,
                "review_form": ReviewForm()
            },
        )


class SessionAttend(View):
    def post(self, request, slug):
        session = get_object_or_404(Session, slug=slug)

        if session.attendance.filter(id=request.user.id).exists():
            session.attendance.remove(request.user)
        else:
            session.attendance.add(request.user)

        return HttpResponseRedirect(reverse('session_detail', args=[slug]))


@login_required()
def get_profile_page(request):
    return render(request, 'profile.html')


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
