from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.shortcuts import render
from lists.models import Item,List
# Create your views here.
def home_page(request):
   #return HttpResponse('<html><title>To-Do lists</title></html>')
   #return render(request,'home.html')
   #if request.method=='POST':
    #  return HttpResponse(request.POST.get('item_text',''))
   #item=Item()
   #item.text=request.POST.get('item_text','')
   #item.save()
   #if request.method=='POST':

   #   Item.objects.create(text=request.POST['item_text'])
    #  return redirect('/lists/the-only-list-in-the-world/')


   #else:
   #   new_item_text=''
   #items=Item.objects.all()
   return render(request,'home.html')

def view_list(request,list_id):
   list_=List.objects.get(id=list_id)
   #items=Item.objects.filter(list=list_)
   return render(request, 'list.html', {'list': list_})

def new_list(request):
   list_=List.objects.create()
   Item.objects.create(text=request.POST['item_text'],list=list_)
   return redirect(f'/lists/{list_.id}/')

def add_item(request,list_id):
   list_ = List.objects.get(id=list_id)
   Item.objects.create(text=request.POST['item_text'],list=list_)
   return redirect(f'/lists/{list_.id}/')
