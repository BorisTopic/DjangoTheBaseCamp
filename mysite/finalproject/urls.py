from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'finalproject'
urlpatterns = [
    path('', views.home, name="home"),
    path('thecampfire/', views.thecampfire, name="thecampfire"),
    path('thecampfire/<int:post_id>', views.thecampfire_detail, name="thecampfire_detail"),
    path('thecampfirepost/', views.thecampfire_post, name="thecampfire_post"),
    path('newsletter/', views.newsletter, name="newsletter"),
    path('contact/', views.contact, name="contact")
]

urlpatterns += staticfiles_urlpatterns()