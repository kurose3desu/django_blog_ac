from django.urls import path, include

from . import views
from .admin import mypage_site

from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

#index_view = TemplateView.as_view(template_name="blog/base.html")

urlpatterns = [
    path("", login_required(views.Index.as_view()), name="index"),
    path('detail/<pk>/', views.Detail.as_view(), name="detail"),
    path('create/', views.Create.as_view(), name="create"),
    path('update/<pk>', views.Update.as_view(), name="update"),
    path('delete/<pk>', views.Delete.as_view(), name="delete"),
    
    path('mypage/', mypage_site.urls),
    path('', include("django.contrib.auth.urls")),
]
