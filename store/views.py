from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = [
            {"name": "Echo Dot (4th Gen)", "price": 5980, "image": "https://images-na.ssl-images-amazon.com/images/I/61u48FEsQKL._AC_SL1000_.jpg"},
            {"name": "Fire TV Stick 4K", "price": 6980, "image": "https://images-na.ssl-images-amazon.com/images/I/51CgKGfMelL._AC_SL1000_.jpg"},
            {"name": "Kindle Paperwhite", "price": 13980, "image": "https://images-na.ssl-images-amazon.com/images/I/61n-5L+QFGL._AC_SL1000_.jpg"},
            {"name": "Apple AirPods Pro", "price": 32800, "image": "https://images-na.ssl-images-amazon.com/images/I/71zny7BTRlL._AC_SL1500_.jpg"},
        ]
        return context
