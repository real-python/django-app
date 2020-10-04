from django.utils.deprecation import MiddlewareMixin


class Demomiddleware(MiddlewareMixin):
    def process_request(self, request):
        # print(request.META)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print("Your Ip is : ", ip)

        ip_list = ['172.10.123.1', '172.10.123.2', '172.10.123.3', '127.0.0.1']

        if ip in ip_list:
            print("Your Are Welcome")
        else:
            print("!!!!!!!!!!!!!!!!!!!")


