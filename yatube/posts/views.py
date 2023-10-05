from django.shortcuts import render

from .models import Post


def index(request):
    latest = Post.objects.order_by('-pub_date')[:11]
    responce = render(request, "index.html", {"posts": latest})
    return responce
