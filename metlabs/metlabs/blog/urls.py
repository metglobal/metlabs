from django.conf.urls import url, patterns
from metlabs.blog.views import (BlogIndexView, BlogDetailView,
                                        BlogPostsRssFeed, BlogPostsAtomFeed)

urlpatterns = patterns('',

   # blog urls
   url(r'^$', BlogIndexView.as_view(), name="blog"),
   url(r'^(?P<slug>[-\w]+)/$', BlogDetailView.as_view(), name="blog_detail"),

   # rss & atom feed
   url(r'^feed/rss$', BlogPostsRssFeed(), name="blog_rss_feed"),
   url(r'^feed/atom$', BlogPostsAtomFeed(), name="blog_atom_feed"),

)
