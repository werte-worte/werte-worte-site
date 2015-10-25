INSTALLED_APPS += (
    'connected_accounts',
    'connected_accounts.providers',
    'djangocms_disqus',
)

MIDDLEWARE_CLASSES += (
    'djangocms_disqus.middleware.DisqusMiddleware',
)

# disqus API keys are secret and are hence added in a local settings split file (e.g. 90-local.py)
# setting names: CONNECTED_ACCOUNTS_DISQUS_CONSUMER_KEY, CONNECTED_ACCOUNTS_DISQUS_CONSUMER_SECRET
