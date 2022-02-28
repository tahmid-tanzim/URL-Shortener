from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import TinyURL
from .serializers import TinyURLSerializer

from utils.helper import get_milli_shortcode


class TinyURLViewSet(viewsets.ViewSet):
    def create(self, request):
        main_url = request.data["url"]

        try:
            url = TinyURL.objects.get(main_url=main_url)
            serializer = TinyURLSerializer(url, many=False)
            response_body = dict(code=serializer.data['short_code'])
            return Response(response_body, status=status.HTTP_200_OK)
        except TinyURL.DoesNotExist:
            millisecond, short_code = get_milli_shortcode()
            new_data = {
                "millisecond": millisecond,
                "short_code": short_code,
                "main_url": main_url,
            }
            serializer = TinyURLSerializer(data=new_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_body = dict(code=serializer.data['short_code'])
            return Response(response_body, status=status.HTTP_201_CREATED)

    def retrieve(self, request, code=None):
        try:
            url = TinyURL.objects.get(short_code=code)
            serializer = TinyURLSerializer(url, many=False)
            response_body = dict(url=serializer.data['main_url'])
            return Response(response_body, status=status.HTTP_200_OK)
        except TinyURL.DoesNotExist:
            return Response({"message": "Sorry! Invalid Tiny URL Code"}, status=status.HTTP_404_NOT_FOUND)
