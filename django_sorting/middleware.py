def get_field(self):
    try:
        field = self.GET.get('sort', self.POST.get('sort', ''))
    except (KeyError, ValueError, TypeError):
        field = ''
    return (self.direction == 'desc' and '-' or '') + field


def get_direction(self):
    try:
        return self.GET.get('dir', self.POST.get('dir', ''))
    except (KeyError, ValueError, TypeError):
        return 'desc'


class SortingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    """
    Inserts a variable representing the field (with direction of sorting)
    onto the request object if it exists in either **GET** or **POST**
    portions of the request.
    """
    def process_request(self, request):
        request.__class__.field = property(get_field)
        request.__class__.direction = property(get_direction)
