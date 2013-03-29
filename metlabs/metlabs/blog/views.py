from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from metlabs.events.models import Event
from metlabs.blog.models import Post


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return {
            "future_events": Event.objects.future(),
            "latest_posts": Post.published_objects.all()[:5]
        }


class BlogIndexView(ListView):
    template_name = "blog/index.html"
    queryset = Post.published_objects.all()
    context_object_name = "posts"
    paginate_by = 30


class BlogDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post
    context_object_name = "post"


class BlogPostsRssFeed(Feed):
    title = settings.BLOG_FEED_TITLE
    link = settings.BLOG_URL
    description = settings.BLOG_FEED_DESCRIPTION

    def items(self):
        return Post.objects.all()[:20]

    def item_description(self, post):
        return post.content

    def item_pubdate(self, post):
        return post.date_created

    def item_categories(self, post):
        return [tag.name for tag in post.tags.all()]


class BlogPostsAtomFeed(BlogPostsRssFeed):
    feed_type = Atom1Feed
    subtitle = settings.BLOG_FEED_DESCRIPTION
