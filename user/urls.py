from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('orders/', views.orders, name='orders'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    path('orderdetail/<int:id>', views.orderdetail, name='orderdetail'),
    path('addcontent/', views.addcontent, name='addcontent'),
    path('contents/', views.contents, name='contents'),
    path('contentedit/<int:id>', views.contentedit, name='contentedit'),
    path('contentdelete/<int:id>', views.contentdelete, name='contentdelete'),
    path('contenaddimage/<int:id>',views.contenaddimage,name='contenaddimage'),





    #path('addcomment/<int:id>', views.addcomment, name='addcomment')
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
]