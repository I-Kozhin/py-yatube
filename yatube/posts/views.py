from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    latest = Post.objects.select_related('author').all()[:11]
    responce = render(
        request,
        "index.html",
        {"posts": list(latest)}
    )
    return responce


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    # posts = Post.objects.filter(group=group).order_by('-pub_date')[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
