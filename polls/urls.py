from django.urls  import path # type: ignore
from . import views 

app_name='polls'
urlpatterns=[
    # path('',views.IndexView.as_view(), name='indexView'),
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.result,name='result'),
    path('<int:question_id>/vote/',views.vote,name='vote')
   
]