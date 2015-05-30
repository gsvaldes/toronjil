from django.contrib.syndication.views import Feed

from .models import Entry

class LatestPosts(Feed):
    title = "Toronjil Blog"
    link = 'blog/feed/'
    description = "Latest posts of Toronjil"
    
    def items(self):
        return Entry.objects.published()[:5]
