from django.urls import path
from Reviews import views 
from .views import ReviewDetails


urlpatterns = [
    path('', views.home, name='Home'),
    path('reviewlist/', views.reviewlist, name="reviewlist"),
    path('save_rating/<int:review_id>/', views.save_rating, name='save_rating'),
    path('addreview', ReviewDetails.as_view(),name= 'addreview'),
    
] 
