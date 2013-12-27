# coding=utf-8
import datetime as dt, time, random, pickle, os
from django.shortcuts import render, redirect
from django.conf import settings
from wetrip.views import upload

FILE_LIST = 'file_list'
PAGE_SIZE = 3

def index(request):        
    if request.method == 'POST':
        link = request.POST['hd_link']
        note = request.POST['tt_notes']
        if not note:
                return render(request, 'index.html', {'msg':'error'})
        if not link:
            today = dt.datetime.today()
            dir_path = '/%s/%d/%d/%d' % (settings.MEDIA_NOTES_DIR, today.year, today.month, today.day)
            upload.create_dir(dir_path)
            file_name = str(int(time.time())) + str(random.randint(0, 1000))
            return write_file(request, note, dir_path + '/' + file_name, 'wb')
        else:
            return write_file(request, note, link, 'wb')
    else:
        link = request.GET.get('l','')#第2个参数为缺省默认值
        if link:
            try:
                with open(settings.MEDIA_ROOT + link , 'rb') as f:
                    notes = f.read().decode('utf8')
                    return render(request, 'index.html', {'notes':notes, 'link':link})
            except IOError, e:
                return render(request, 'index.html', {'msg':e.strerror})
        else:
            page_index = 1
            if request.GET.get('p','1'):#第2个参数为缺省默认值
                try:
                    page_index = int(request.GET.get('p','1'))
                except ValueError:
                    page_index = 1
            total_page = (len(load_file_list()) + PAGE_SIZE - 1) / PAGE_SIZE
            forward = page_index - 1
            if forward <= 0:
                forward = 1
            backward = page_index + 1
            if backward >= total_page :
                backward = total_page
            file_list = load_file_list()[(page_index - 1) * PAGE_SIZE:page_index * PAGE_SIZE]
            return render(request, 'index.html', {'file_list':file_list, 'total_page':total_page,
                                                  'page_index':page_index, 'forward':forward,
                                                  'backward':backward})

def delete(request):
    if request.method == 'POST':
        ls = request.POST.getlist('ckb_f')
        for f in ls:
            delete_file(f)
        return render(request, 'index.html', {'msg':'success'})
    else:
        return redirect('/')
        
def write_file(request, note, file_name, mode):
    try:
        with open(settings.MEDIA_ROOT + file_name, mode) as f:
            f.write(note.encode('utf8'))
        save_file_list(file_name)
        return render(request, 'index.html', {'msg':'success', 'link':file_name})
    except IOError , e:
        return render(request, 'index.html', {'msg':e.strerror})
    
def save_file_list(file_name):
    ls = load_file_list()
    if file_name not in ls:
        ls.append(file_name)
    with open(settings.WEB_ROOT + '/' + FILE_LIST, "wb") as f:
        pickle.dump(ls, f)
 
def load_file_list():
    try:
        with open(settings.WEB_ROOT + '/' + FILE_LIST, "rb") as f:
            return pickle.load(f)
    except IOError:
        return []
    except:
        return []
    
def delete_file(file_name):
    if os.path.exists(settings.MEDIA_ROOT + '/' + file_name):
        os.remove(settings.MEDIA_ROOT + '/' + file_name)
    ls = load_file_list()
    ls.remove(unicode(file_name))
    with open(settings.WEB_ROOT + '/' + FILE_LIST, "wb") as f:
        pickle.dump(ls, f)
