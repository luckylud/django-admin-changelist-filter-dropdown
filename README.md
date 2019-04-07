# django-admin-changelist-filter-dropdown

A django admin add-on to make changelist-filter div collapsable with nice dropdown filters display.

 - [Installation](#installation)
 - [License](#license)


## Installation

Enable in `settings.py`:

```py

INSTALLED_APPS = (
    'django_admin_changelist_filter_dropdown',
    'django.contrib.admin',
    ...
)

```

*django_admin_changelist_filter_dropdown must be install before django.contrib.admin


Install css:

```sh
django-admin/manage.py collectstatic
```

## License

django-admin-changelist-filter-dropdown is under MIT License. See the
[LICENSE](LICENSE) file for the exact license text.


[1]: https://github.com/luckylud/django-admin-changelist-filter-dropdown
