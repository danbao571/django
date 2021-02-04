from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('_', views.BlogTypeView.as_view(), name="get_blog_type"),
    path('test', views.TestView.as_view(), name='test')
]
