from django.http import JsonResponse
from django.views import View

from products.logic.crud import ProductsCRUD


class ProductsView(View):
    def post(self, request):
        action = (request.get_full_path()).split('/')[-1]

        action_functions = {
            'get-for-select': ProductsCRUD.get_products_for_select,
        }

        if action in action_functions:
            return JsonResponse(action_functions[action](request))
        else:
            return JsonResponse({
                'success': False,
                'error': 'endpoint не имеет реализации.'
            })
