from functools import wraps

try:
    import django_filters  # noqa

    DJANGO_FILTER_INSTALLED = True
except ImportError:
    DJANGO_FILTER_INSTALLED = False


try:
    import polymorphic  # noqa

    DJANGO_POLYMORPHIC_INSTALLED = True
except ImportError:
    DJANGO_POLYMORPHIC_INSTALLED = False
