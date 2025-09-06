from rest_framework.pagination import PageNumberPagination


class DefaultProductPaginations(PageNumberPagination):
    page_size = 10
    