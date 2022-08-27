from django.views.generic import TemplateView
from .models import Coach
from rest_framework import generics
from wukong_fitness.serializers import CoachSerializer


class Homepageview(TemplateView):
    template_name = 'home.html'

class CoachList(generics.ListAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

class CoachDetail(generics.RetrieveAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
