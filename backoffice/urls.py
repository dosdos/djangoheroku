from django.conf.urls import patterns


urlpatterns = patterns(
    'backoffice.views',

    # Home
    (r'^[/]?$', 'home', {'template_name': 'backoffice/home.html'}, 'backoffice_home'),

)
