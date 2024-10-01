from django.views.generic import ListView

from shop.models import Product


class MainPageView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        print(self.model)
        return self.model.objects.all().order_by('-id')[:8]
