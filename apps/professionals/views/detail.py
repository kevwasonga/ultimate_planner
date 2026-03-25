from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import ReviewForm
from ..selectors import professional_get_detail
from ..services import create_review

def professional_detail(request, pk):
    """
    View to display professional details and handle review submission.
    """
    prof = professional_get_detail(pk)
    # Filter approved reviews using the manager on the professional instance
    # (Django still allows this even if we use selectors for the main object)
    approved_reviews = prof.reviews.filter(is_approved=True)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            create_review(
                professional=prof,
                client_name=form.cleaned_data['client_name'],
                rating=form.cleaned_data['rating'],
                comment=form.cleaned_data['comment'],
                is_approved=False
            )
            messages.success(request, '✅ Your review has been submitted and is awaiting approval. Thank you!')
            return redirect('professional_detail', pk=pk)
    else:
        form = ReviewForm()

    context = {
        'prof': prof,
        'reviews': approved_reviews,
        'form': form,
    }
    return render(request, 'professionals/detail.html', context)
