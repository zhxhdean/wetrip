# coding=utf8
import re, random, time, os, datetime as dt
from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

ALLOW_SUFFIX = ['.jpg', '.jpeg', '.png', '.gif']
@csrf_exempt
def upload_image(request):    
    if 'HTTP_CONTENT_DISPOSITION' in request.META:
        # chrome/firefox html5方式上传
        disposition = request.META['HTTP_CONTENT_DISPOSITION']
        reg = re.compile(r'(filename=\")(.*)(\")')
        file_name = ''
        match = reg.search(disposition)
        if match:
            file_name = match.group(2)
        else:
            return HttpResponse(simplejson.dumps({'err':'无文件', 'msg':''}, ensure_ascii=False))
        return save_image(request.body, file_name, True)
    elif 'filedata' in request.FILES:
        # ie 普通方式上传
        file_data = request.FILES['filedata']
        file_name = file_data.name
        return save_image(file_data, file_name, False)

# 保存文件    
def save_image(file_data, file_name, html5):
    suffix = file_name[file_name.rindex('.') : len(file_name)]
    if not check_suffix(suffix):
        return HttpResponse(simplejson.dumps({'err':'上传文件格式不正确,只支持:%s' % ALLOW_SUFFIX, 'msg':''},
                                             ensure_ascii=False))
    new_file_name = '/' + str(int(time.time())) + str(random.randint(0, 1000)) + suffix
    try:
        today = dt.datetime.today()
        dir_path = '/%s/%d/%d/%d' % (settings.MEDIA_PICTURES_DIR, today.year, today.month, today.day)
        create_dir(dir_path)
        with open(settings.MEDIA_ROOT + dir_path + new_file_name , 'wb') as f:
            if html5:
                f.write(file_data)
            else:
                for d in file_data.chunks():
                    f.write(d)
        return HttpResponse(simplejson.dumps({'err':'', 'msg':''.join([settings.MEDIA_ROOT_URL , dir_path , new_file_name]) }))
    except IOError, e:
        return HttpResponse(simplejson.dumps({'err':e.strerror, 'msg':''}, ensure_ascii=False))

# 创建目录
def create_dir(dir_path):
    if not os.path.exists(settings.MEDIA_ROOT + dir_path):
        os.makedirs(settings.MEDIA_ROOT + dir_path)

# 验证上传文件后缀名
def check_suffix(suffix):
    if suffix.lower() in ALLOW_SUFFIX:
        return True
    return False
