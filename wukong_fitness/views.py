from django.views.generic import TemplateView


class Homepageview(TemplateView):
    template_name = 'home.html'
