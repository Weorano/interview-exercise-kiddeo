from django.core.exceptions import ObjectDoesNotExist

from products.models import Product
from ..models import MapMarker


class MapsCRUD:
    @staticmethod
    def get_all_markers(request):
        markers = MapMarker.objects.all()
        markers_list = []

        for marker in markers:
            markers_list.append({
                'id': marker.id,
                'coordinates': marker.coordinates,
                'product_name': marker.product.name,
                'product_address': marker.product.address,
                'product_image': marker.product.image.url if marker.product.image else None,
            })

        return {
            'success': True,
            'markers': markers_list
        }

    @staticmethod
    def add_marker(request):
        coordinates_str = request.POST.getlist('coordinates[]', None)
        product_id = request.POST.get('product_id', None)

        if coordinates_str is None or product_id is None:
            return {
                'success': False,
                'error': 'Ожидалось 2 аргумента.'
            }

        # coordinates = []
        # for coord_str in coordinates_str:
        #     try:
        #         coord_decimal = Decimal(coord_str)
        #         coordinates.append(coord_decimal)
        #     except ValueError:
        #         return {
        #             'success': False,
        #             'error': 'В координатах передаётся что-то не то....'
        #         }

        try:
            marker = MapMarker()
            marker.coordinates = coordinates_str
            marker.product = Product.objects.get(pk=int(product_id))
            marker.save()

            return {'success': True}
        except ObjectDoesNotExist:
            return {
                'success': False,
                'error': 'Не возможно создать маркер, так как '
                'он назначен на несуществующее помещение.'
            }
