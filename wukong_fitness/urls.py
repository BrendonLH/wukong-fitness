from django.urls import path
from .views import Homepageview, CoachList

urlpatterns = [
    path('', Homepageview.as_view(), name='home'),
    path('coaches/',CoachList.as_view(), name='coaches' ),
]