from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render_to_response
from django.template import RequestContext


# ===========================================================================
# USER PASSES TESTS
# ===========================================================================
def is_admin(user):
    return user.is_staff


# ===========================================================================
# HOME
# ===========================================================================
@login_required(login_url='/login/')
@user_passes_test(is_admin)
def home(request, template_name="backoffice/home.html"):
    return render_to_response(template_name, {
        'session': request.session.keys(),
    }, context_instance=RequestContext(request))
