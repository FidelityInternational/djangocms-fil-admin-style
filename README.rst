*************************
django CMS FilAdminStyle
*************************

This overrides the djangocms_admin_style with global admin template modifications

============
Installation
============

Ensure that it is installed before djangocms_admin_style


Requirements
============

django CMS FilAdminStyle requires that you have a django CMS 3.5.0 (or higher) project already running and set up.


To install
==========

Run::

    pip install git+git://github.com/divio/djangocms-fil_admin_style@master#egg=djangocms-fil_admin_style

Add the following to your project's ``INSTALLED_APPS``:

  - ``'djangocms_fil_admin_style'``

Add following line in project level urls.py after 'url(r'^admin/', include(admin.site.urls)),'

- ``url(r'^djangocms_fil_admin_style/', include('djangocms_fil_admin_style.urls')),``

Run::

    python manage.py migrate djangocms_fil_admin_style

to perform the application's database migrations (there aren't any currently)
