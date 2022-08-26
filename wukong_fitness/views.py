from django.views.generic import TemplateView
from django.contrib.auth.models import User
from wukong_fitness.models import Coach
from rest_framework import viewsets
from rest_framework import permissions
from wukong_fitness.serializers import UserSerializer, CoachSerializer



class Homepageview(TemplateView):
    template_name = 'home.html'

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CoachViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
