========================
Django reusable news app
========================

-----
Usage
-----

Add the url files to the mount point, it requres ``simplenews`` as a namespace::

    (r'^news/', include('simplenews.urls', namespace='simplenews')),


Please note that the templates aren't provided::

    simplenews/object_detail.html
    simplenews/object_list.html
    simplenews/shortlist.html


------------
Requirements
------------

* Qmanager http://github.com/zacharyvoase/django-qmanager
* django_extensions http://github.com/django-extensions/django-extensions


Testing the app::

    $ python bootstrap.py
    $ ./bin/buildout
    $ ./bin/test

