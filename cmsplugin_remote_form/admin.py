from django.contrib import admin
from django.http import HttpResponse

from adminsortable.admin import SortableTabularInline, NonSortableParentAdmin
from cmsplugin_remote_form.models import ExtraField, RemoteForm, ContactRecord

from .actions import export_as_csv_action

class ExtraFieldInline(SortableTabularInline):
    model = ExtraField
    fields = ('name', 'label', 'fieldType', 'placeholder', 'initial', 'css_class', 'required')
    extra = 0


class RemoteFormAdmin(NonSortableParentAdmin):
    model = RemoteForm
    inlines = (ExtraFieldInline, )


class ContactRecordAdmin(admin.ModelAdmin):
    model = ContactRecord
    actions = [export_as_csv_action("CSV Export", 
        fields = ['contact_form', 'date_of_entry', 'date_processed', 'data'],
        header = True,
        json_fields = ['data']), # 
    ]


admin.site.register(ExtraField)

admin.site.register(ContactRecord, ContactRecordAdmin)
admin.site.register(RemoteForm, RemoteFormAdmin)
