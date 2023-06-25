from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.conf import settings
from .forms import TextForm, FileForm


def main_page(request):
    if request.method == 'POST':
        file = None
        description = None
        table = False
        count_of_rows = 0
        prediction = None

        if request.POST:
            description = request.POST['text_for_recognition']
        if request.FILES:
            file = request.FILES['data_csv']

        print()
        print(description)
        print(file)
        text_form = TextForm(request.POST)
        file_form = FileForm(request.POST)

        print(text_form.is_valid())
        if text_form.is_valid():
            predictions = [(description, 'HARD WORK')]
            table = True
            count_of_rows = 1
            
        elif file_form.is_valid():
            fs=FileSystemStorage()
            file_name = fs.save(str(file), file)
            file_url = settings.MEDIA_ROOT / file_name
            predictions = 'predict_file()'
            table = True
            count_of_rows = 3

        context = {
            'text_form': text_form, 
            'file_form': file_form, 
            'table': table, 
            'table_data': predictions,
            'count_of_rows': count_of_rows,
        }
        return render(request, 'main.html', context)
    
    elif request.method == 'GET':
        text_form = TextForm()
        file_form = FileForm()
        test = 'no'
        context = {
            'text_form': text_form, 
            'file_form': file_form, 
            'table': False, 
            'table_data': None,
            'count_of_rows': 0,
        }
        return render(request, 'main.html', context)
    

def predict_text_form():
    pass

def predict_file():
    pass

class AboutView(TemplateView):
    template_name = 'home.html'