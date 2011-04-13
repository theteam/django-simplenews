Django reusable news app

Usage

Add the url files to the mount point, it requres ``simplenews`` as a namespace
<pre>
(r'^news/', include('simplenews.urls', namespace='simplenews')),
</pre>

Please note that the templates aren't provided.

<pre>
simplenews/object_detail.html
simplenews/object_list.html
simplenews/shortlist.html
</pre>


Requirements:

- Qmanager http://github.com/zacharyvoase/django-qmanager
- django_extensions http://github.com/django-extensions/django-extensions


Testing the app:

<pre>
$ python bootstrap.py
$ ./bin/buildout
$ ./bin/test
</pre>
