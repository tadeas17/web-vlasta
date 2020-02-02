from django.shortcuts import render
from django.views import View
from .models import Photo, PhotoType


class HomePageView(View):

    def get(self, request):
        context = {}
        template_name = "home.html"

        context['photos'] = Photo.objects.filter(home_page_photo=True)
        context['slider_photos'] = Photo.objects.filter(slider_photo=True)
        return render(request, template_name=template_name, context=context)


class ContactView(View):

    def get(self, request):
        template_name = "najdete_nas.html"

        return render(request, template_name=template_name)


class GaleriMainView(View):

    def get(self, requset):
        template_name = "display_galeri.html"
        context = {}

        context["galeries"] = Photo.objects.filter(photo_type__main_type_photo=True, type_galeri_photo=True)
        return render(requset, template_name=template_name, context=context)


class GaleriView(View):

    def get(self, request, type=None):
        template_name = "galeri.html"
        context = {}

        if (type is None):
            context["photos"] = Photo.objects.all()

        else:
            context["photos"] = Photo.objects.filter(photo_type__type_photo=type)

        return render(request, template_name=template_name, context=context)