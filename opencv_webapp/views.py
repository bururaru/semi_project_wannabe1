from django.shortcuts import render, redirect
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from django.conf import settings
from .opencv_browser import opencv_browser
from .opencv_moblie import opencv_mobile
from django.http      import JsonResponse
from .models import *
import datetime
# Create your views here.
def web_ver(request):
    return render(request, 'web_ver.html')

def browser(request):
    if request.method == 'POST' and request.POST['flag'] == 'Bbtn':
        flag = opencv_browser(1)
        print('browser return value', flag)
        if flag == 1:
            list = [{'browser_info': 'QR 출석을 완료했습니다. '}]
            p = Profile.objects.get(user_name='kim')
            p.user_attend = p.user_attend + 1
            p.save()
            return JsonResponse(list, safe=False)
        else:
            list = [{'browser_info': 'QR을 찾지 못했습니다. '}]
            return JsonResponse(list, safe=False)
    list = [{'browser_info': 'QR을 찾지 못했습니다. '}]
    return JsonResponse(list, safe=False)

def mobile(request):
    print('ajax - 입성')
    if request.method == 'POST':
        flag = opencv_mobile(1)
        print('mobile return value - ', flag)
        if flag == 1:
            list = [{'mobile_info': 'QR 출석을 완료했습니다. '}]
            p = Profile.objects.get(user_name='kim')
            p.user_attend = p.user_attend + 1
            p.save()
            return JsonResponse(list, safe=False)
        else:
            list = [{'mobile_info': 'QR을 찾지 못했습니다. '}]
            return JsonResponse(list, safe=False)
    else:
        list = [{'mobile_info': 'QR을 찾지 못했습니다. '}]
        return JsonResponse(list, safe=False)

def alarm_ajax(request):
    if request.method == 'POST' and request.POST['flag'] == 'Abtn':
        print(request.POST['flag'])
    # print('ajax - param - ', flag)
    list = [{'info': '신호출결이 완료 되었습니다. '}]
    return JsonResponse(list, safe=False)
