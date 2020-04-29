from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Post, Category

class IndexView(generic.ListView):
    template_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset

class CategoryView(generic.ListView):
    template_name = 'blog/post_list.html'
    model = Post
    pagenate_by=10

    def get_queryset(self):

        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Post.objects.order_by('-created_at').filter(category=category)

        return queryset
    
class DetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    