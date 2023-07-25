from django.shortcuts import render

# Create your views here.
def index(request):
    msg="Hello, Stephen King"  
    # current_date = date.today()
    context = {
        'section':{
            'title':'latest Stories',
        },
        'story_list':  [
            {
                'headline':'Breaking News',
                'tease':'Python programming language wins multiple award in the industry',
                'get_absolute_url':'https://www.google.com',
            },
            {
                'headline':'New Feature in Django 3.5 Released',
                'tease':'it comes with exciting features for developers',
                'get_absolute_url':'https://www.google.com',
            },
            # Additional story can be added to the list
        ]
    }
    return render(request,"jonesapp/index.html",context)
def about(request):
  
    return render(request,"jonesapp/about.html")
def contact(request):
    return render(request,"jonesapp/contact.html")
