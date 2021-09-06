from django.contrib import admin
from django.contrib.auth.admin import csrf_protect_m
from django.db import models
from django.contrib.auth import get_user_model

from django.forms import MediaDefiningClass


class FakeModelClass(MediaDefiningClass):
    @property
    def model(cls):
        User = get_user_model()
        attrs = {
            "__module__": cls.__module__,
            "Meta": type(
                "Meta", (), {"proxy": True, "verbose_name": cls.get_verbose_name(), "verbose_name_plural": cls.get_verbose_name()}
            ),
        }
        return type(f"{cls.get_name()}", (User,), attrs)


class NonModelAdmin(admin.ModelAdmin, metaclass=FakeModelClass):
    name = None
    verbose_name = None
    change_list_template = "admin/test.html"

    def get_model_perms(self, request):
        return {"view": True}

    @classmethod
    def get_name(cls):
        return cls.name or cls.__name__.replace("Admin", "")

    @classmethod
    def get_verbose_name(cls):
        return cls.verbose_name or cls.get_name()

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        context = self.get_extra_context(request)
        if extra_context:
            context.update(extra_context)
        return super().changelist_view(request, context)

    def get_extra_context(self, request):
        return {"title": self.get_verbose_name()}

    def get_urls(self):
        return super().get_urls()[:1]  # we only need changelist url

    @classmethod
    def register(cls, site):
        site.register(cls.model, cls)


def register(*models, site=None):
    """
    Register the given model(s) classes and wrapped ModelAdmin class with
    admin site:

    @register(Author)
    class AuthorAdmin(admin.ModelAdmin):
        pass

    NonModelAdmin classes can be registered without models provided.

    @register()
    class DashboardAdmin(NonModelAdmin):
        name = 'dashboard'
        verbose_name = 'My dashboard'
        change_list_template = "my_app/dashboard.html"

    The `site` kwarg is an admin site to use instead of the default admin site.
    """
    from django.contrib.admin import ModelAdmin
    from django.contrib.admin.sites import AdminSite, site as default_site

    def _model_admin_wrapper(admin_class):
        nonlocal models
        if not models:
            if hasattr(admin_class, 'model'):
                models = (admin_class.model,)
            else:
                raise ValueError('At least one model must be passed to register.')

        admin_site = site or default_site

        if not isinstance(admin_site, AdminSite):
            raise ValueError('site must subclass AdminSite')

        if not issubclass(admin_class, ModelAdmin):
            raise ValueError('Wrapped class must subclass ModelAdmin.')

        admin_site.register(models, admin_class=admin_class)

        return admin_class

    return _model_admin_wrapper
