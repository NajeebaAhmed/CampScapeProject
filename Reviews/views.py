
from Reviews.forms import ReviewForm
from django.views.generic import ListView, CreateView
from django.shortcuts import redirect, render
from .models import Review
from .forms import ReviewForm
from django.urls import reverse_lazy


# Create your views here.

    # model = Review
    # #Go to models.py and use the name of the model you created here.
    # #I have created the model as Post, hence using that here.
    # template_name = 'add_review.html'


def home(request):
    return render(request, 'home.html', {})

def reviewlist(request):
      review = Review.objects.all()
      rating_range = range(1, 6)  # Generate the range
      return render(request, 'reviewlist.html', {'reviews' : review})  

def add_review(request):
     review_add = Review.objects.all()
     return render(request, 'add_review.html', {'reviews' : review_add} )

class all_reviews(ListView):
    model = Review
    template_name = 'reviewlist.html'
     
def save_rating(request, review_id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review = Review.objects.get(id=review_id)
        review.rating = rating
        review.save()
    return redirect('reviewlist.html')


class ReviewDetails(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'add_review.html'

    def get_success_url(self):
        return reverse_lazy('reviewlist') 

