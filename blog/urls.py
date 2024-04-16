from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog', views.blog_page, name='article' ),
    path('blog/details/<slug:slug>', views.post_details, name='details' ),
    path('saidebare',views.side_bare, name = 'sidebare')
]
