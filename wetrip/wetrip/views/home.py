#coding=utf8
import datetime as dt,time,random
from django.shortcuts import render,redirect
from django.conf import settings
from wetrip.views import upload

def index(request):
    return render(request,'index.html')

def add_info(request):
    if request.method == 'POST':
        today = dt.datetime.today()
        dir_path = '/%s/%d/%d/%d' % (settings.MEDIA_NOTES_DIR,today.year,today.month,today.day)
        upload.create_dir(dir_path)
        file_name =  str(int(time.time())) + str(random.randint(0,1000))
        note = request.POST['tt_notes']
        if not note:
            return render(request,'index.html',{'msg':'error'})
        try:
            with open(settings.MEDIA_ROOT + dir_path + '/' + file_name,'w') as f:
                f.write(note)
            return render(request,'index.html',{'msg':'success'})
        except IOError ,e:            
            return render(request,'index.html',{'msg':e.strerror})
    else:
        return redirect('/')