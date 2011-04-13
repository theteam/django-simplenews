from django.core.urlresolvers import reverse
from django.test import TestCase

from simplenews.models import Article

class SimpleNewsTest(TestCase):

    def setUp(self):
        """Actions to be performed at the begining of every test"""
        pass

    def tearDown(self):
        """Actions to be performed at the end of every test"""
        Article.objects.all().delete()

    def create_article(self, title, extra_data=None):
        data = {'title': title,
                'body': 'Body of: %s' % title,
                'summary': 'Summary of: %s' % title,}
        if extra_data:
            data.update(extra_data)
        return Article.objects.create(**data)

    def test_article_creation(self):
        """Test an article creation"""
        article = self.create_article('Lorem ipsum')
        assert article, "Failed to create Article"
        extra_data = {'status': Article.HIDDEN}
        self.create_article('DRAFT Lorem ipsum', extra_data)
        total_article = Article.live.all().count()
        self.assertEqual(total_article, 1)

    def test_article_list(self):
        """Test article listing"""
        # Populate with articles
        self.test_article_creation()
        response = self.client.get('/')
        context = response.context
        self.assertEqual(len(context['object_list']), 1)

    def test_non_live_article(self):
        """Test non live article"""
        extra_data = {'status': Article.HIDDEN}
        article = self.create_article('DRAFT Lorem ipsum', extra_data)
        url = reverse('news_detail', args=[article.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_live_article(self):
        """Test a live article"""
        title = 'Lorem ipsum'
        article = self.create_article(title)
        url = reverse('news_detail', args=[article.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        context_article = response.context['object']
        self.assertEqual(context_article.title, title)

    # TODO: test the template tag