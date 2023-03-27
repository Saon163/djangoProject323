from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name = 'index'),
]

from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('2/', views.if_else, name = 'if_else'),
    ]

from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('2/', views.if_else, name = 'if_else'),
    path('3/', views.for_loop, name = 'for_loop'),
    ]

from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('2/', views.if_else, name = 'if_else'),
    path('3/', views.for_loop, name = 'for_loop'),
    path('4/', views.ifequal_func, name = 'ifequal_function'),
    ]

from django.urls import path

from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('2/', views.if_else, name = 'if_else'),
    path('3/', views.for_loop, name = 'for_loop'),
    path('4/', views.ifequal_func, name = 'ifequal_function'),
    path('5/', views.filter_func, name = 'filter_function'),
    path('today/', views.today_is, name = 'today_is'),
    path('home/', views.home, name = 'home'),
    path('blog/',views.blog, name = 'blog'),
    path('tablecss/', views.index2, name = 'index2'),
    path('contact/',views.contact, name = 'contact'),
    path('7/',views.index3, name = 'index3'),
]

from django.urls import path

from polls import views

urlpatterns = [

    path('contact/', views.contact2, name='contact2'),
    path('data/', views.index4, name='data'),
    path('home/', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
]