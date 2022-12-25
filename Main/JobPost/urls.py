from django.urls import path
from JobPost import views

current_app = 'Post'

urlpatterns = [
    path("", views.all_posts),
    path('add/', views.newpost, name='post-add'),
    path('<int:id>/', views.post_detail, name='post-detail'),
    path('<int:id>/edit/', views.post_edit, name='post-edit'),
    path('apply<int:id>',views.apply,name="apply"),
    path('<int:id>/delete/',views.post_delete,name="post-delete"),
]
