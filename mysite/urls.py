from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views
from order import views as orderviews

urlpatterns = [
    path('', include ('home.urls')),
    path('user/', include ('user.urls')),
    path('content/', include('content.urls')),
    path('order/', include('order.urls')),
    path('product/', include('product.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('error/', views.error, name='error'),
    path('referanslar/', views.referanslar, name='referanslar'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('search/', views.product_search, name='product_search'),
    path('search_auto/', views.product_search_auto, name='product_search_auto'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('menu/<int:id>', views.menu, name='menu'),
    path('category/<int:id>/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('content/<int:id>/<slug:slug>/', views.contentdetail, name='contentdetail'),

    path('admin/', admin.site.urls),

    path('shopcart/', orderviews.shopcart, name='shopcart'),
    path('sss/', orderviews.faq, name='faq'),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
