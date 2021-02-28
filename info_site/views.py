from djpjax import pjax, PJAXResponseMixin
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView


class HomeView(PJAXResponseMixin, APIView):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return render(request, 'home.html', locals())
        return render(request, 'home.html', locals())
