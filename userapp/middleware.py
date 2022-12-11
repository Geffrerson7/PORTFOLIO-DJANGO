from ipware import get_client_ip

from .models import IpUsers

class IPIsValid:
    """
    __init__ : sirve como constructor
    __call__ : se ejecuta antes de mostrar la vista
    """

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        print("ip", ip)
        IpUsers.objects.create(ip_user=str(ip))
        response = self.get_response(request)
        return response