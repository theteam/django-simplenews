from django import template

from simplenews.models import Article

register = template.Library()

@register.inclusion_tag('simplenews/shortlist.html', takes_context=True)
def render_latest_news(context):
    """Renders the latest news"""
    object_list = Article.live.all().order_by('-created')[:5]
    return {'object_list': object_list}
