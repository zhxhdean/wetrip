#coding=utf8
import datetime as dt,time,random
from django.shortcuts import render
from django.conf import settings
from wetrip.views import upload

def index(request):    
    if request.method == 'POST':
        link = request.GET.get('l')
        note = request.POST['tt_notes']
        if not note:
                return render(request,'index.html',{'msg':'error'})
        if not link:
            today = dt.datetime.today()
            dir_path = '/%s/%d/%d/%d' % (settings.MEDIA_NOTES_DIR,today.year,today.month,today.day)
            upload.create_dir(dir_path)
            file_name =  str(int(time.time())) + str(random.randint(0,1000)) + '.t' 
            return write_file(request,note,dir_path + '/' + file_name,'wb')
        else:
            return write_file(request,note,link,'wb')
    else:
        link = request.GET.get('l')
        if link:
            try:
                with open(settings.MEDIA_ROOT + link ,'rb') as f:
                    notes = f.read().decode('utf8')
                    return render(request,'index.html',{'notes':notes,'link':link})
            except IOError, e:
                return render(request,'index.html',{'msg':e.strerror})
        else:
            return render(request,'index.html')


def write_file(request,note,file_name,mode):
    try:
        with open(settings.MEDIA_ROOT + file_name,mode) as f:
            f.write(note.encode('utf8'))
        return render(request,'index.html',{'msg':'success','link':file_name})
    except IOError ,e:
        return render(request,'index.html',{'msg':e.strerror})