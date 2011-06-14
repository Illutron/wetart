from django.shortcuts import render
from profiles.models import Profile


def index(request):
    profiles = Profile.objects.all()
    return render(request, 'index.html', {'people': profiles})