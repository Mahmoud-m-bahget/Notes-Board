from django.urls import include, re_path ,path
from . import views
app_name = 'note_app'
urlpatterns = [
    re_path(r'^$',views.all_notes , name = 'all_notes'),
    #for get the notes with the id
    # re_path(r'^(?P<id>\d+)$',views.detail , name = 'note_detail')
    re_path (r'^(?P<slug>[-\w]+)/$',views.detail , name = 'note_detail'),
    re_path(r'add',views.note_add , name = 'add_note'),
    re_path (r'^(?P<slug>[-\w]+)/edit$',views.edit , name = 'note_edit'),
]
