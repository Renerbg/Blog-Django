from django.urls import path
from blogs import views


app_name = 'blogs'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('post/<slug:slug>', views.PostView.as_view(), name='post'),
    path('featured/', views.Featured_Listview.as_view(), name='featured'),
    path('category/<slug:slug>', views.Category_ListView.as_view(), name='category'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
]