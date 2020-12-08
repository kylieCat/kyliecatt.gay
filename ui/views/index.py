from django.shortcuts import render
from django.views import View

from linkbush import linkbush
from user.models.user import Kylie


class IndexView(View):
    def get(self, request):
        kylie = Kylie()
        context = {
            "user": kylie,
            "links": linkbush.get_user_links(kylie.pk),
            "sidebar": {
                "width": "350px"
            }
        }
        return render(request, template_name="ui/index.html", context=context)
