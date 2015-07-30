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

    # authentication
    url(r'^login/$', 'djangoheroku.views.login_user', {'template_name': 'auth/login.html'}, 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'auth/logout.html'}, 'logout'),
    url(r'^signup/?$', 'djangoheroku.views.signup_user', {'template_name': 'auth/signup.html'}, 'signup'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'auth/password_change.html'}, 'password_change'),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'auth/password_change_done.html'}, 'password_change_done'),

    # frontoffice
    url(r'', include('frontoffice.urls')),

    # Change language: en, it
    url(r'^en/$', 'djangoheroku.views.change_lang_en', {}, 'change_to_en'),
    url(r'^it/$', 'djangoheroku.views.change_lang_it', {}, 'change_to_it'),

    # third party apps
    url('', include('social.apps.django_app.urls', namespace='social')),

)
