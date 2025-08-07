from rest_framework import status
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

# from api.serializers.categories.create import CreateCategorySerializer
from api.serializers.categories.list import CategorySerializer
from api.serializers.categories.retrieve import RetrieveCategorySerializer
from models_app.models import Category

"""
        Варианты View
    APIView - базовый класс (по аналогии с View) Var 1
    ListAPIView, CreateAPIView,... (Generic классы, по аналогии с ListView, CreateView...) Var 2
    ViewSet - сложная херь
"""


# class CategoryListCreateAPIView(APIView):
#     """
#         Var 1 View on APIView
#     """
#
#     def get(self, request, *args, **kwargs) -> Response:
#         """
#         Вывод всех категорий + фильтрация по имени
#         """
#         categories = Category.objects.all().order_by('-id')
#         search = (request.query_params.get('search'))
#         if search:
#             categories = categories.filter(title__icontains=search)
#
#         return Response(
#             CategorySerializer(categories, many=True).data,
#             status=status.HTTP_200_OK
#         )
#
#     def post(self, request, *args, **kwargs) -> Response:
#         """ Create categories"""
#         serializer = CreateCategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # return Response(
#             #     serializer.data,
#             #     status=status.HTTP_201_CREATED
#             # )
#             return Response(
#                 CreateCategorySerializer(serializer.instance).data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )


class CategoryListCreateAPIView(ListCreateAPIView):
    """
    Var 2 View on generic (ListAPIView)
    переопределю метод у ListAPIView
    """

    # queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        # categories = Category.objects.all()
        # search = self.request.query_params.get('search')
        # if search:
        #     categories = categories.filter(title__icontains=search)
        # return categories

        # Чтение, фильтрация, создание
        return Category.objects.filter(
            title__icontains=self.request.query_params.get("search", "")
        )


class CategoryTestListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs["id"])

        return Response(
            RetrieveCategorySerializer(category).data, status=status.HTTP_200_OK
        )
