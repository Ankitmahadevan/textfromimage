# pages/urls.py
from django.urls import path

# from .views import HomePageView
from .views import BlogCreateView
from .views import BlogDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('', BlogCreateView.as_view(), name='newppost'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='postsdetail'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)