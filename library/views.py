from django.shortcuts import render ,get_object_or_404 ,redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def book_list(request):
    books=Book.objects.all()
    
    return render(request,"book_list.html",{"books":books})

def book_detail(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    
    return render(request,"book_detail.html",{"book":book})

def add_block(request):
    if request.method == "POST":
        form =BookForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("book_list")
        
    else:
        form =BookForm()
        
    return render(request,"add_block.html",{"form":form})

def update_book(request,book_id):
    book= get_object_or_404(Book,id=book_id)
    
    if request.method=="POST":
        form=BookForm(request.POST,instance=book)
        
        if form.is_valid():
            form.save()
            return redirect("book_detail",book_id=book.id)
        
    else:
        form=BookForm(instance=book)
        
    return render(request,"update_book.html",{"form":form,"book":book})

def delete_book(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
        
    return render(request,"delete_book.html",{"book":book})
