from django.shortcuts import redirect
from django.views import View


class FlyersView(View):
    def get(self, request):
        return redirect("https://drive.google.com/drive/folders/1x1oT07VGfopvKLiuYl-1oz7kSxa_FrQg?usp=sharing")
