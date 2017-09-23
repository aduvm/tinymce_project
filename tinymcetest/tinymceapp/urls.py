from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^save_page/$',views.save_page,name='save_page'),
    url(r'^show_page/(?P<page_id>\d+)$', views.show_page, name='show_page'),
    url(r'^pages/$', views.pages, name='pages'),
    url(r'^update_image/$', views.update_image, name='update_image'),

]
