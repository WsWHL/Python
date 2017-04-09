from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def Index(request):
    acticles = models.Article.objects.all()
    return render(request, "Blog/Index.html", {"acticles": acticles})
