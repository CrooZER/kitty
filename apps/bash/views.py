from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from apps.bash.models import Reason, ReasonForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    reasons = Reason.objects.all().order_by('-created_at')
    paginator = Paginator(reasons, 5)

    page = request.GET.get('page')
    try:
        reasons = paginator.page(page)
    except PageNotAnInteger:
        reasons = paginator.page(1)
    except EmptyPage:
        reasons = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {'reasons': reasons})

def popular(request):
    reasons = Reason.objects.all().order_by('-rating')
    paginator = Paginator(reasons, 5)
    page = request.GET.get('page')
    try:
        reasons = paginator.page(page)
    except PageNotAnInteger:
        reasons = paginator.page(1)
    except EmptyPage:
        reasons = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {'reasons': reasons})

def reason(request, reason_id):
    try:
        reason = Reason.objects.get(pk=reason_id)

    except Reason.DoesNotExist:
        raise Http404
    return render_to_response('reason.html', {'reason' : reason })

def new(request):
    if request.method == 'POST':
        form = ReasonForm(request.POST)
        if form.is_valid():
            new_reason = form.save()
            if new_reason:
                HttpResponseRedirect('/')
    else:
        form = ReasonForm()
    return render (request, 'form.html', {'form': form})

