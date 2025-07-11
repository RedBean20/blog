import json
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from posts.models import Post


def allow_self(function):
    def wrapper(request, *args, **kwargs):
        id = kwargs["id"]
        if not Post.objects.filter(id=id, author__user=request.user).exists():
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                response_data = {
                    "status":"error",
                    "title" :"unauthorized Access",
                    "message":"you cannot access this post"
                }
                return HttpResponseRedirect(reverse("web:index"))
            else:
                return HttpResponse(json.dumps(response_data), content_type = "application/json")
        return function(request, *args, **kwargs)
    return wrapper
