import json

from django.contrib import admin

from maps.models import MapMarker


@admin.register(MapMarker)
class ProductAdmin(admin.ModelAdmin):
    actions = None
    model = MapMarker
    list_display = ('coordinates', 'product')
    change_list_template = 'admin/maps.html'

    def changelist_view(
        self,
        request,
        extra_context=None
    ):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            queryset = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        place_marks_json = json.dumps([{
            'coordinates': mark.coordinates,
            'product_name': mark.product.name,
            'product_address': mark.product.address,
            'product_image': mark.product.image.url
        } for mark in queryset])

        response.context_data['place_marks'] = place_marks_json
        return response

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
