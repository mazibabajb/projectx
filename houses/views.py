from django.shortcuts import render
from .models import Property,Suburb
from django.shortcuts import render
# Create your views here.

def home(request):
    property_listing = Property.objects.filter(is_hot=True)
    context = {
        'property_listing':property_listing
    }
    return render(request,"houses/index.html", context)  



def propeties_list(request):
    property_listing = Property.objects.all()
    context = {
        'property_listing':property_listing
    }
    return render(request, "houses/property_list.html", context)




def property_detail(request,id):
    property_listing = Property.objects.get(id=id)
    context = {
		'property_listing': property_listing,
	}
    return render(request, "houses/single.html",context)
    
    
def contact(request):
    return render(request,"houses/contact.html")


def about(request):
    return render(request,"houses/about.html")



def Suburb_list(request):
    Suburb_listing = Suburb.objects.all()
    context = {
        'Suburb_listing':Suburb_listing,
    }
    return render(request, "houses/suburb_list.html", context)     

    

