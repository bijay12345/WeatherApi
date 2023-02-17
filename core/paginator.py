from rest_framework.pagination import PageNumberPagination

# I AM USING THE PAGE NUMBER PAGINATION PROVIDED BY THE DRF TO PAGINATE THE QUERYSETS AND SETTING PAGE_SIZE = 10 TO DISPLAY ON 10 ITEMS PER PAGE.

class WeatherPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100