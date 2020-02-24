
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from posts.views import (
    index, blog, post, search, 
    post_create, post_contact, post_update, post_delete)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('create/', post_create, name='post-create'),
    path('contact/', post_contact, name='contact'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete', post_delete, name='post-delete'),
    path('marketing/', include('marketing.urls')),
    path('account/', include('account.urls', namespace='account')),
    path('tinymce/', include('tinymce.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   