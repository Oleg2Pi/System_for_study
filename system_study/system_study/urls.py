from django.contrib import admin
from django.urls import path, include
from school.views import ProductAPIView, LessonsAPIView, ProductAPIListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product_list/', ProductAPIView.as_view()),
    path('api/product_detail_list/', ProductAPIListView.as_view()),
    path('api/lessons_list/', LessonsAPIView.as_view()),
]
