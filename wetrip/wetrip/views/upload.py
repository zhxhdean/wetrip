#coding=utf8
from django.http import HttpResponse
from django.utils import simplejson
import re
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import time,os,datetime as dt
@csrf_exempt
def upload_image(request):
    dir_path = create_dir()
    if 'HTTP_CONTENT_DISPOSITION' in request.META:
        #chrome/firefox html5方式上传
        disposition = request.META['HTTP_CONTENT_DISPOSITION']
        reg = re.compile(r'(filename=\")(.*)(\")')
        filename = ''
        match = reg.search(disposition)
        if match:
            filename = match.group(2)
        else:
            return HttpResponse(simplejson.dumps({'err':'无文件','msg':''},ensure_ascii=False))
        suffix = filename[filename.rindex('.') : len(filename)]
        data = request.body
        image_name = str(int(time.time())) + suffix
        try:
            with open(settings.MEDIA_ROOT + dir_path +'/'+ image_name ,'wb') as f:
                f.write(data)
            return HttpResponse(simplejson.dumps({'err':'','msg':settings.MEDIA_DIR + dir_path +'/'+ image_name }))
        except IOError, e:
            return HttpResponse(simplejson.dumps({'err':e.strerror,'msg':''},ensure_ascii=False))

def create_dir():
    today = dt.datetime.today()
    dir_path = '/%d/%d/%d' % (today.year,today.month,today.day)
    if not os.path.exists(settings.MEDIA_ROOT + dir_path):
        os.makedirs(settings.MEDIA_ROOT + dir_path)
    return dir_path