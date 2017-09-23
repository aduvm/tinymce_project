from django.http import HttpResponse
from django.shortcuts import render
from tinymceapp.models import  Page
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from tinymcetest import settings
# Create your views here.
def show_page(request,page_id):
    page =  Page.objects.get(id = page_id)
    return render(request, 'show_page.html',context={'page':page})

def index(request):
    return render(request,'index.html')

def save_page(request):
    title = request.POST['title']
    content = request.POST['content']
    page = Page.objects.create(title = title,content = content)
    page.save()

    return  show_page(request,page.id)
@csrf_exempt
def update_image(request):
    media_url =  '{scheme}://{host}{media}'.format( scheme=request.scheme, host=request.get_host(),media = '/media/')
    print(media_url)
    if request.method == 'POST':
        # try:

            f = request.FILES['file']
            with open(os.path.join(settings.MEDIA_ROOT,f.name), 'wb+') as image_file:
                for chunk in f.chunks():
                    image_file.write(chunk)

            location = media_url+f.name

            #print(location)


           # location = '{%static %}'
            reponse = {'location': location}
        # except Exception:
        #     print('except--->update_image')
    #reponse = {'location': 'https://www.baidu.com/img/bd_logo1.png'}
    if reponse is  None:
        reponse = {'location': ''}
    return JsonResponse(reponse)

def pages(request):
    pages = Page.objects.all()
    return render(request, 'pages.html',context = {'pages':pages})

