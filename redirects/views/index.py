from django.shortcuts import redirect
from django.views import View


class FlyersView(View):
    def get(self, request):
        return redirect("https://drive.google.com/drive/folders/1sYJz40zDGfCox67-x1dzJPQbUQyUuWcJ?usp=sharing")
