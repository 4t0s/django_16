from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import PostView, PostDetailView, CreatePost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name = 'list'),
    path('recipe/<int:id>', PostDetailView.as_view(), name = 'details'),
    path('create/', CreatePost.as_view(), name = 'create'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
