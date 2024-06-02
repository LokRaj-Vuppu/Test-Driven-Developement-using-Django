from django.db.models import F
from .models import PlatformStatistics


class UserplatformOSIdentifier:

    def __init__(self, get_response):
        self.get_response = get_response

    def stats(self, os_info):
        # Get or create the PlatformStatistics object
        # platform_stats, created = PlatformStatistics.objects.get_or_create(pk=1, defaults={
        #     'windows': 0,
        #     'mac': 0,
        #     'iphone': 0,
        #     'android': 0,
        #     'others': 0
        # })

        if "Windows" in os_info:
            PlatformStatistics.objects.all().update(windows=F("windows") + 1)
        elif "mac" in os_info:
            PlatformStatistics.objects.all().update(mac=F("mac") + 1)
        elif "iPhone" in os_info:
            PlatformStatistics.objects.all().update(iphone=F("iphone") + 1)
        elif "Android" in os_info:
            PlatformStatistics.objects.all().update(android=F("android") + 1)
        else:
            PlatformStatistics.objects.all().update(others=F("others") + 1)

    def __call__(self, request):
        if "admin" not in request.path:
            self.stats(request.META["HTTP_USER_AGENT"])

        response = self.get_response(request)

        return response
