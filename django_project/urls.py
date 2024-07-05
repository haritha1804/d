from django.contrib import admin
from django.urls import path, include  # new
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("django.contrib.auth.urls")),  # new
    path("api/", include("api.urls")),  # new
    path("", TemplateView.as_view(template_name="home.html"), name="home"), 

]

