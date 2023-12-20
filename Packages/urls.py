from django.urls import path
from . import views 
from .views import PackageView,PackagesDetail,NotePackageView


urlpatterns = [
    path('', views.home, name='Home'),
    path('Packages', views.package_list, name='Packages'),
    path('packages',PackageView.as_view(),name='packages'),
    path('packages/<int:package_id>/', views.package_details, name='package_details'),
    path('packages/<int:package_id>/test',PackagesDetail.as_view(),name='help'),
    path('packagenote', NotePackageView.as_view(), name="packagenote"),
] 