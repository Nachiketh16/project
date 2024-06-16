from django.urls import path
from . import views   

urlpatterns = [
    path('',views.home, name = 'home'),

    path('login',views.loginPage, name='login'),
    path('register',views.registerPage, name='register'),
    path('logout/',views.logout, name='logout'),

    path('about',views.about, name='about'),
    path('ourteam',views.ourTeam, name='ourteam'),
    path('trainning',views.trainning, name='trainning'),
    # path('haha',views.haha, name='home'),

    # path('our-team/', views.team_view, name='team'),
    path('athlete/<int:athlete_id>/', views.athlete_detail_view, name='athlete_detail'),

]
