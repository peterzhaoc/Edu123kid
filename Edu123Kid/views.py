from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from writings.models import *
from django.core.urlresolvers import reverse
from writings.utils import permission_check

def test(request):
    content = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, 'Edu123Kid/test.html',content)
