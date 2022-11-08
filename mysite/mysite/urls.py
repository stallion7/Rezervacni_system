from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('slipka_gym/', include('slipka_gym.urls')),
    path('', RedirectView.as_view(url='slipka_gym')),

]