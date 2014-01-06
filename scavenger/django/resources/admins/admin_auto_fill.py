#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created on Jan 6, 2014

"""
Admin for Models.
Snippet for auto-fill field.
"""

from django.contrib import admin

import myapp.models


class MyModelAdmin(admin.ModelAdmin):
    max_num = 1
    list_display = ('__unicode__',
                    'author',
                    )
    list_filter = ('closed',
                   'author')
    search_fields = ('author__first_name',
                     'author__last_name',
                     '__unicode__')

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        return super(MyModelAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

admin.site.register(myapp.models.MyModel, MyModelAdmin)
