from django.urls import path
from .views import PostsList, PostsDetail, PostCreate, PostUpdate, PostDelete, CustomLoginView, RegistrationPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('login/', CustomLoginView.as_view(), name='login'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
   path('registration/', RegistrationPage.as_view(), name='registration'),

   path('', PostsList.as_view(), name='posts'),
   path('post/<int:pk>/', PostsDetail.as_view(), name='post'),
   path('post-create/', PostCreate.as_view(), name='post-create'),
   path('post-update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
   path('post-delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
]