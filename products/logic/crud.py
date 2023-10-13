from products.models import Product


class ProductsCRUD:
    @staticmethod
    def get_products_for_select(request):
        products = Product.objects.all().values('id', 'name')

        products_list = list(products)

        return {
            'success': True,
            'products_choices': products_list
        }
