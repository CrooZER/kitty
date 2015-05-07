from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from apps.bash.models import Reason
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    sort = request.GET.get('sort')
    if(sort=='first'):
        reasons = Reason.objects.all().order_by('created_at')
    elif(sort=='last'):
        reasons = Reason.objects.all().order_by('-created_at')
    elif(sort=='rating'):
        reasons =  Reason.objects.all().order_by('-rating')
    else:
        reasons = Reason.objects.all()
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