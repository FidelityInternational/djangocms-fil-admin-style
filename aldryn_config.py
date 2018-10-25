from aldryn_client import forms


class Form(forms.BaseForm):
    def to_settings(self, data, settings):
        for app_name in ('djangocms_admin_style', 'django.contrib.admin'):
            try:
                index = settings['INSTALLED_APPS'].index(app_name)
                break
            except ValueError:
                pass
        else:
            index = 0
        settings['INSTALLED_APPS'].insert(index, 'djangocms_fil_admin_style')
        return settings
