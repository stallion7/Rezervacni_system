from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include

from mysite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('slipka_gym/', include('slipka_gym.urls')),
    path('', RedirectView.as_view(url='slipka_gym')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)