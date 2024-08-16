from django.urls import path, include

urlpatterns = [
    path('blog/', include(('social_media.blog.urls', 'blog'))),
    path('users/', include(('social_media.users.urls', 'users'))),
    path('auth/', include(('social_media.authentication.urls','auth'))),
]
