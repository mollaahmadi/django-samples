from django.shortcuts import render

# Create your views here.

URL_RENDER = {
    'view_home':'view_home.html',
}
def view_home(request):
    return render(request, URL_RENDER['view_home'])
