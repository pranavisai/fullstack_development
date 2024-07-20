from django.shortcuts import render

#view are being defined here
def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'basic_app/index.html', context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_template.html')