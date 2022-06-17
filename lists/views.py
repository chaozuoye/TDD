from django.shortcuts import render,redirect
from lists.models import Item,List
from django.http import HttpResponse
def home_page(request):
    return render(request,'home.html')
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # if request.method == 'POST':
    #     #new_item_text = request.POST['item_text']
    #
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world/')
    #return render(request,'home.html')#render(request,'home.html',{'new_item_text':new_item_text})
# Create your views here.
def view_list(request,list_id):
    list_=List.objects.get(id=list_id)
    #items=Item.objects.filter(list=list_)
    #items=Item.objects.all()
    return render(request,'list.html',{'list':list_})#render(request)
def new_list(request):
    list_=List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect(f'/lists/{list_.id}/')
def add_item(request,list_id):
    list_=List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect(f'/lists/{list_.id}/')
