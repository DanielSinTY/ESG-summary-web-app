from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import formResponse
# Create your views here.
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

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
            return render(request,'done.html',{'name':form.cleaned_data['company_name']})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = formResponse()

    return render(request, 'home.html', {'form': form})

from django.shortcuts import redirect

def home_redirect(request):
    response = redirect('/search/')
    return response