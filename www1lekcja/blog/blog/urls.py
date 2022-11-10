from django.urls import path
from django.contrib import admin
from . import views

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
   path('blog/', views.question_list, name='question_list'),
   path('', views.home_view),
   path('<int:question_id>/', views.question_detail, name='question_detail'),
   path('policjant/', views.policjant),
   path('newquestion/', views.question_add, name="question_add"),
   path('newchoice/', views.choice_add, name='choice_add')

]