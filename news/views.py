# Create your views here.
from django.conf.urls.defaults import *
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from news.models import Article


class NewsApp(object):
    app_name = "news"
    namespace = "news"

    def _get_patterns(self):
        return patterns('',
            url("^$", self.index, name="index"),
            url("^article/(?P<slug>[\w-]+)/$", self.article, name="article"),
        )

    @property
    def urls(self):
        return self._get_patterns(), self.app_name, self.namespace

    model = Article

    def index(self, request):
        ctx = RequestContext(request)
        ctx.current_app = self.namespace
        ctx["news"] = self.model.objects.all()
        return render_to_response("news/index.html", context_instance=ctx)

    def article(self, request, slug):
        ctx = RequestContext(request)
        ctx.current_app = self.namespace
        ctx["article"] = get_object_or_404(self.model, slug=slug)
        return render_to_response("news/article.html", context_instance=ctx)
