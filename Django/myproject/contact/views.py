from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # Replace with saving or emailing later
            return render(request, 'success.html')
    return render(request, 'contact_form.html', {'form': form})