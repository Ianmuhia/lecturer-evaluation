from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from .models import stars


class barView(DetailView):
    model = stars
    def get_object(self, queryset=None):
        obj, created = self.model.objects.get_or_create(bar="foo bar baz")
        return obj


class SizesView(TemplateView):
    model = stars
    template_name = "sizes.html"

    def get_context_data(self, **kwargs):
        kwargs["sizes"] = {
            size: self.model.objects.get_or_create(bar=str(size))[0]
            for size in range(10, 40)
        }
        return super(SizesView, self).get_context_data(**kwargs)

def ratings(request):
    return render(request, 'pages/ratings.html')