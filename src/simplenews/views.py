from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from simplenews.models import Article

def object_list(request, template='simplenews/object_list.html'):
    """List of the ``LIVE`` ``Article`` ordered by Featured and Date"""
    object_list = Article.live.all().order_by('is_featured','-created')
    extra_context = {'object_list': object_list,}
    return render_to_response(template, extra_context,
                              RequestContext(request))

def object_detail(request, slug, template='simplenews/object_detail.html'):
    """Shows the requested article if ``LIVE``"""
    article = get_object_or_404(Article, slug=slug, status=Article.LIVE)
    extra_context = {'object': article}
    return render_to_response(template, extra_context,
                              RequestContext(request))
