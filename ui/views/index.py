from django.shortcuts import render
from django.views import View

from linkbush import linkbush


class IndexView(View):
    def get(self, request):
        context = {
            "user": request.user,
            "links": linkbush.get_user_links(request.user.pk)
        }
        return render(request, template_name="ui/index.html", context=context)
