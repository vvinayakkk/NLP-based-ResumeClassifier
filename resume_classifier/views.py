from django.shortcuts import render, redirect
from django.core.files.uploadedfile import InMemoryUploadedFile
from .utils import clean_resume, predict_category
from .forms import ResumeUploadForm

def home(request):
    return render(request, 'home.html')

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = request.FILES['resume']
            cleaned_resume = clean_resume(resume_file)
            predicted_category = predict_category(cleaned_resume)
            if isinstance(resume_file, InMemoryUploadedFile):
                resume_file.close()
            return render(request, 'resume_result.html', {
                'uploaded_resume_url': '', 
                'predicted_category': predicted_category,
            })
    else:
        form = ResumeUploadForm()

    return render(request, 'upload_resume.html', {
        'form': form
    })
