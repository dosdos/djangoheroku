from frontoffice.forms import RegistrationForm, UserProfileRegistrationForm
from frontoffice.models import UserProfile
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from django.utils.translation import ugettext_lazy as _


def login_user(request, template_name="auth/login.html"):
    """ Login the user by 'username' and 'password'.

    """

    if request.user.is_authenticated():
        # try:
        #     AdminUser.objects.get(user=request.user)
        #     return HttpResponseRedirect(reverse('backoffice_home'))
        # except AdminUser.DoesNotExist:
        #     pass
        try:
            UserProfile.objects.get(user=request.user)
            return HttpResponseRedirect(reverse('frontoffice_home'))
        except UserProfile.DoesNotExist:
            state = _("Your account has not a UserProfile. Please contact an administrator.")
            logout(request)
            return render_to_response(template_name, {
                'state': state,
            }, context_instance=RequestContext(request))

    # Try to get next param from query string
    next_url = request.GET.get('next')

    state = None
    username = None

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)

                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    # try:
                    #     AdminUser.objects.get(user=request.user)
                    #     return HttpResponseRedirect(reverse('backoffice_home'))
                    # except AdminUser.DoesNotExist:
                    #     pass
                    try:
                        UserProfile.objects.get(user=request.user)
                        return HttpResponseRedirect(reverse('frontoffice_home'))
                    except UserProfile.DoesNotExist:
                        state = _("Username and password are not correct.")
            else:
                state = _("Your account is not active. Please, contact an Administrator.")
        else:
            state = _("Username and password are not correct.")

    return render_to_response(template_name, {
        'state': state,
        'username': username,
        'next': next_url,
    }, context_instance=RequestContext(request))


def signup_user(request, template_name="auth/signup.html"):
    next_url = request.GET.get('next')

    # Create unbound forms
    user_form = RegistrationForm()
    hacker_form = UserProfileRegistrationForm()

    if request.method == 'POST':

        # Create bound forms
        user_form = RegistrationForm(request.POST)
        hacker_form = UserProfileRegistrationForm(request.POST)

        if user_form.is_valid() and hacker_form.is_valid():

            # Get user and pass from POST and save the user
            user_name = user_form.cleaned_data.get('username')
            user_pass = user_form.cleaned_data.get('password2')
            user = user_form.save()

            # Create a new hacker and set the current event to None
            user_profile = hacker_form.save(commit=False)
            user_profile.user = user
            # user_profile.signup_ip_address = get_client_ip(request)
            # user_profile.signup_city = get_client_city(request)
            # user_profile.signupn_region = get_client_region(request)
            # user_profile.signup_country = get_client_country(request)
            # user_profile.signup_mobile = get_client_browser(request)
            user_profile.save()

            # Log the user and redirect to hacker home
            user = authenticate(username=user_name, password=user_pass)
            login(request, user)

            if next_url:
                return HttpResponseRedirect(next_url)

            return HttpResponseRedirect(reverse('frontoffice_home'))

    return render_to_response(template_name, {
        'user_form': user_form,
        'hacker_form': hacker_form,
        'next': next_url,
    }, context_instance=RequestContext(request))


def change_lang_en(request):
    activate('en')
    return HttpResponseRedirect(reverse('home'))


def change_lang_it(request):
    activate('it')
    return HttpResponseRedirect(reverse('home'))
