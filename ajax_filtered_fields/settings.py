from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required

# Set AJAX_FILTERED_FIELDS_AUTH_DECORATOR = None
# in your project settings if you want to give public
# access to the views.json_index view.
# Otherwise set it as a auth decorator callable
# (eg: django.contrib.auth.decorators.login_required).
# Default is django.contrib.admin.views.decorators.staff_member_required.

AUTH_DECORATOR = getattr(settings, 
    "AJAX_FILTERED_FIELDS_AUTH_DECORATOR", 
    staff_member_required)

JQUERY_URL = getattr(settings,
    "AJAX_FILTERED_FIELDS_JQUERY_URL", None)

JAVASCRIPT_URL = getattr(settings,
    "AJAX_FILTERED_FIELDS_JAVASCRIPT_URL", None)

CSS_URL = getattr(settings,
    "AJAX_FILTERED_FIELDS_CSS_URL", None)

if not JAVASCRIPT_URL or not CSS_URL or not JQUERY_URL:
    from django.core.exceptions import ImproperlyConfigured
    
    raise ImproperlyConfigured(
        "The settings AJAX_FILTERED_FIELDS_JQUERY_URL, AJAX_FILTERED_FIELDS_JAVASCRIPT_URL, "
        "and AJAX_FILTERED_FIELDS_CSS_URL must both be set. "
        "They should be set to the urls to ajax_filtered_fields.js and ajax_filtered_fields.css, "
        "packaged with the ajax_filtered_fields app.")
