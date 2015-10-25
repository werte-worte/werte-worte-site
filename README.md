## What is it (for now)?

A Django-CMS managed site to inform about the idea of the Werte Worte project and to provide a platform for
discussions for it.

### Setup hints
`python-disqus` currently used for Disqus integration is not ready for Python 3 yet, so you need to stick with
Python 2.7 for now.

We adopted the [ordered list of split settings files]
(https://code.djangoproject.com/wiki/SplitSettings#UsingalistofconffilesTransifex) approach. Add a file like
`werteworte/settings/90-local.py` to the project dir (or symlink it) to give confidential information
(passwords, API tokens, password salt, the `SECRET`, ...)

Also we look at the 
`DJANGO_CONFIGURATION` environment variable matching `dev*`, `test` and `prod` to adapt some settings.
