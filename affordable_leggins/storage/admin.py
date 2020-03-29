from django.contrib import admin
from affordable_leggins.storage.models import Leggin, Size


class LegginAdmin(admin.ModelAdmin):
    list_filter = ("sizes", "price", "date", "external_id")
    list_display = ("name", "price", "date", "url", "created_at")
    search_fields = ("name",)


admin.site.register(Leggin, LegginAdmin)
admin.site.register(Size)
