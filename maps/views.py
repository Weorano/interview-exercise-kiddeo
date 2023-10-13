from django.http import JsonResponse
from django.views import View

from maps.logic.crud import MapsCRUD


class AdminMapsView(View):
    def post(self, request):
        action = (request.get_full_path()).split('/')[-1]
        crud = MapsCRUD()

        action_functions = {
            '': crud.get_all_markers,
            'add-marker': crud.add_marker,
        }

        if action in action_functions:
            return JsonResponse(action_functions[action](request))
        else:
            return JsonResponse({
                'success': False,
                'error': 'endpoint не имеет реализации.'
            })
