from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('super/', admin.site.urls),
    path("api/v1/auth/",include("djoser.urls")),
    path("api/v1/auth/",include("djoser.urls.jwt")),
    path("api/v1/profile/",include("apps.profiles.urls")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Real Project Admin"
admin.site.site_title = "Real Project Admin Portal"
admin.site.index_title = "Welcome to Real Project Portal"