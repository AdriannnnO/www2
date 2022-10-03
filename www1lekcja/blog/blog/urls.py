from django.urls import path
from django.contrib import admin
from . import views

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
   path('blog/', views.question_list, name='question_list'),
   path('', views.jd, name='question_list'),
   path('<int:question_id>/', views.question_detail, name='question_detail')

]