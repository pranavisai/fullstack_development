from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST) ## we are passing in that request as POST.

    if form.is_valid(): ## if valis then we are printing to our terminal
        print("VALIDATION SUCCESS")
        print("NAME: "+ form.cleaned_data['name'])
        print("Email: "+ form.cleaned_data['email'])
        print("TEXT: "+ form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html',{'form':form})