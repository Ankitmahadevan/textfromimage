# posts/views.py
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .models import Car
from PIL import Image
from pytesseract import image_to_string



# class HomePageView(ListView):
#     model = Car
#     template_name = 'a.html'
    
class BlogDetailView(DetailView):
      model = Car
      template_name = 'detail.html'
      def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
            context = super().get_context_data(**kwargs)
            a=Car.objects.all()
            # Add in a QuerySet of all the books
            context['book_list'] = image_to_string(Image.open(a[0].photo.url[1:]), lang='eng')
            Car.objects.all().delete()
            return context
class BlogCreateView(CreateView):
    model = Car
    template_name = 'new.html'
    fields = ['photo']

