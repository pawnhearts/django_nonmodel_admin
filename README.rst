=====================
Django NonModel Admin
=====================



Allows to add sections to django admin which are not tied to any model. They can render some template for example.

=====
Usage
=====

In admins.py::

    from django_nonmodel_admin import NonModelAdmin, register

    @register()
    class DashboardAdmin(NonModelAdmin):
        name = 'dashboard'
        verbose_name = 'My dashboard'
        change_list_template = "my_app/dashboard.html"

register decorator can be used with regular ModelAdmin's too.

Template example::

    {% extends "admin/change_list.html" %}
    {% block content %}
    <div id="content-main">
    ,,, your stuff
    </div>
    {% endblock %}

Extra context can be defined via overwriting get_extra_context method of NonModelAdmin.

It can be extended like regular ModelAdmin, for example you can define own get_urls method.

You DON'T have to add anything to INSTALLED_APPS.

* Free software: MIT license


