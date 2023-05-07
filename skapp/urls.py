from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from skapp import views
urlpatterns = [
         path('',views.home,name='home'),
         path('department',views.depart,name='department'),
         path('docterpage',views.docters,name='docterpage'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)