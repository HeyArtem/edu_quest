from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# from models_app.models.test.models import Test


class TestListAPIView(APIView):
    def post(self):
        ...

    def get(self, request, *args, **kwargs):
        return Response(
            # ListTestSerializer(Test.objects.all().order_by("-id"), many=True).data,
            status=status.HTTP_200_OK,
        )
