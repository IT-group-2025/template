from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post


class TestPageView(TemplateView):
    template_name = 'example_posts/test_page.html'


class StyleTestPageView(TemplateView):
    template_name = 'example_posts/style_test_page.html'


# class PostListView(ListView):
#     model = Post
#     template_name = 'example_posts/post_list.html'


class PostListView(TemplateView):
    template_name = 'example_posts/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Post.objects.all().order_by('-pub_date')[:10]
        return context
