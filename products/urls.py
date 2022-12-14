from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('positive_reviews/<product_id>', views.positive_reviews_view, name='positive_reviews'),
    path('negative_reviews/<product_id>', views.negative_reviews_view, name='negative_reviews'),
    path('add_favorites/<int:product_id>', views.add_favorite, name='add_favorite'),
    path('remove_favorites/<product_id>', views.remove_favorite, name='remove_favorite'),
    path('edit_positive_review/<positive_review_id>', views.edit_positive_review, name='edit_positive_review'),
    path('delete_positive_review/<positive_review_id>', views.delete_positive_review, name='delete_positive_review'),
    path('edit_negative_review/<negative_review_id>', views.edit_negative_review, name='edit_negative_review'),
    path('delete_negative_review/<negative_review_id>', views.delete_negative_review, name='delete_negative_review'),
]
