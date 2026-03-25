from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Category
from ..forms import InquiryForm

def contact(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Your inquiry has been submitted! Our team will connect you with the right professional within 24 hours.')
            return redirect('contact')
    else:
        preselect = request.GET.get('category', '')
        selected_cat = Category.objects.filter(slug=preselect).first()
        form = InquiryForm(initial={'service_category': selected_cat} if selected_cat else None)

    return render(request, 'professionals/contact.html', {
        'categories': categories,
        'form': form,
    })
