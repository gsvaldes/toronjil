from django.views import generic

from . import models

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/blog_index.html"
    paginate_by = 2
    
    
class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "blog/post.html"
