from django.urls import path, include

urlpatterns = [
    path('blog/', include(('social_media.blog.urls', 'blog')))
    path('users/', include(('social_media.users.urls', 'users')))
]
