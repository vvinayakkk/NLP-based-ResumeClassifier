from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .utils import clean_resume, predict_category
from .models import Resume

class ResumeClassifierTestCase(TestCase):
    def test_upload_resume_view(self):
        url = reverse('upload_resume')
        resume_file = SimpleUploadedFile("test_resume.txt", b"Test resume content")

        # Simulate a POST request to upload a resume
        response = self.client.post(url, {'resume': resume_file})

        # Check if the response is successful and the expected template is used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume_result.html')

        # Check if the uploaded resume is stored correctly in the database
        uploaded_resume = Resume.objects.last()
        self.assertEqual(uploaded_resume.category, 'Expected category')

        # Clean and preprocess the uploaded resume
        cleaned_resume = clean_resume(resume_file)
        predicted_category = predict_category(cleaned_resume)

        # Check if the predicted category matches the expected result
        self.assertEqual(predicted_category, 'Expected category')
