from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,'main_app/index.html')

def other(request):
    return render(request,'main_app/wishlist.html')

def relative(request):
    return render(request,'main_app/relative_url_templates.html')
    
from .models import WishList, Category
def index(request): #the index view
    wishes = WishList.objects.all() #quering all wishes with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a wish
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Wish = WishList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Wish.save() #saving the wish
            return redirect("/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a wish
            checkedlist = request.POST["checkedbox"] #checked wishes to be deleted
            for wish_id in checkedlist:
                wish = WishList.objects.get(id=int(wish_id)) #getting wish id
                wish.delete() #deleting wish
    return render(request, "index.html", {"wishes": wishes, "categories":categories})
