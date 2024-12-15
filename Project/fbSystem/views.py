from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()

    return render(request, 'fbSystem/feedback_form.html', {'form': form})

def feedback_success(request):
    return render(request, 'fbSystem/feedback_success.html')
