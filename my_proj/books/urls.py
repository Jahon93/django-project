from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('view/<int:pk>', views.BookView.as_view(), name='book_view'),
    path('new', views.BookCreate.as_view(), name='book_new')
]
