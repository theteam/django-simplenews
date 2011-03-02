from django.template import RequestContext
from django.shortcuts import render_to_response

from simplenews.models import Article

def object_list(request, template='simplenews/object_list.html'):
    """List of the latest ``Article`` ordered by Featured and Date"""
    object_list = Article.live.all().order_by('is_featured','-created')
    extra_context = {'object_list': object_list,}
    return render_to_response(template, extra_context,
                              RequestContext(request))
