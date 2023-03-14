from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import formResponse
from .webscraper import WebpageScraper
from django import forms

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    age= forms.IntegerField()
    favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))
# Create your views here.


# chrome_options = Options()
# chrome_options.add_argument("--headless")

# browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

def search(request):
    
    # return render(request,"home.html")
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = formResponse(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            scraper=WebpageScraper()
            # scraper.get("https://www.google.com/search?q="+form.cleaned_data['company_name'].replace(' ','+')+"+ESG+news")
            # result=scraper.getFirstEntry()
            result=scraper.scrapeMSCI(form.cleaned_data['company_name'])
            scraper.destroy()
            return render(request,'done.html',{'result':result})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'home.html', {'form': form})

from django.shortcuts import redirect

def home_redirect(request):
    response = redirect('/search/')
    return response