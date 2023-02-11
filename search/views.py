from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import formResponse
from .webscraper import WebpageScraper
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
            scraper.get("https://www.google.com/search?q="+form.cleaned_data['company_name'].replace(' ','+')+"news")
            
            return render(request,'done.html',{'result':scraper.getFirstEntry()})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = formResponse()

    return render(request, 'home.html', {'form': form})

from django.shortcuts import redirect

def home_redirect(request):
    response = redirect('/search/')
    return response