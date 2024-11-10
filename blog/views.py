from django.shortcuts import render
from django.views import generic

from .models import Post


# Create your views here.
class PostList(generic.ListView):
    """Список постов"""
    model = Post
    template_name = 'blog/home.html'
    paginate_by = 5

    def get_queryset(self):
        """
        Выводим только несколько последних постов.

        Их количество определяется в настройках проекта.
        """
        return self.model.objects.order_by('-pub_date')

