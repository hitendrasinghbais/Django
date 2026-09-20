from django.urls import path 
from .views import index,book_list,book_detail,add_block,update_book,delete_book

urlpatterns = [
    path("",index, name="index"),
    path("books/",book_list,name="book_list"),
    path("books/<int:book_id>/",book_detail,name="book_detail"),
    path("add-block/",add_block,name="add_block"),
    path("books/<int:book_id>/update/",update_book,name="update_book"),
    path("books/<int:book_id>/delete/",delete_book,name="delete_book"),
]
