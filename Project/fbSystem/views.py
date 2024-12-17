import logging
from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from .forms import FeedbackForm
from .models import Feedback


logger = logging.getLogger(__name__)

def feedback_view(request):
    try:
        if request.method == 'POST':
            form = FeedbackForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('feedback_success')
                except Exception as e:
                    logger.error(f"Error saving feedback form: {e}")
                    return render(request, 'fbSystem/feedback_form.html', {
                        'form': form,
                        'error_message': 'An error occurred while saving your feedback. Please try again later.'
                    })
            else:
                return render(request, 'fbSystem/feedback_form.html', {
                    'form': form,
                    'error_message': 'Please correct the errors below.'
                })
        else:
            form = FeedbackForm()
        return render(request, 'fbSystem/feedback_form.html', {'form': form})

    except Exception as e:
        logger.error(f"Error processing feedback form: {e}")
        return HttpResponseServerError("Something went wrong. Please try again later.")

def feedback_success(request):
    try:
        return render(request, 'fbSystem/feedback_success.html')
    except Exception as e:
        logger.error(f"Error rendering success page: {e}")
        return HttpResponseServerError("Something went wrong while displaying the success page.")
