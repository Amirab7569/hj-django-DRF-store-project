from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')
router.register('categories', views.CategoryViewSet, basename='category')
router.register('carts', views.CartViewSet, basename='cart')
router.register('customers', views.CustomerViewSet, basename='customer')
router.register('orders', views.OrderViewSet, basename='order')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('comments', views.CommentViewSet, basename='product-comment')

cart_items_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_items_router.register('items', views.CartItemViewSet, basename='cart-items')


urlpatterns = router.urls + products_router.urls + cart_items_router.urls


# urlpatterns = [
#     path('', include(router.urls))
# ]


# urlpatterns = [
#     path('products/', views.ProductListView.as_view()),
#     path('products/<int:pk>/', views.ProductDetailView.as_view()),
#     path('categories/', views.CategoryListView.as_view(), name='category-detail'),
#     path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
# ]
