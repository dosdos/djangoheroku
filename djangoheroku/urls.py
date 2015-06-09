from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',

    # backoffice
    url(r'^backoffice/', include('backoffice.urls')),

    # django admin
    url(r'^admin/', include(admin.site.urls)),

    # robots.txt file
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

)

urlpatterns += i18n_patterns(
    # frontoffice
    url(r'', include('frontoffice.urls')),
)
