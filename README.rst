Reusable news app

Considerations:
- Templates won't be provided


Usage:
- Add the url files to the mount point, it requres 'simplenews' as a namespace
<pre>
(r'^news/', include('simplenews.urls', namespace='simplenews')),
</pre>
- Add the required templates
<pre>
simplenews/object_detail.html
simplenews/object_list.html
</pre>


Requirements
- Qmanager http://github.com/zacharyvoase/django-qmanager
- django_extensions http://github.com/django-extensions/django-extensions

TODO:
Add requirements file
