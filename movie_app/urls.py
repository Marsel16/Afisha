from django.urls import path
from movie_app.views import DirectorModelViewSet, MovieModelViewSet, ReviewModelViewSet, MovieReviewListAPIView


urlpatterns = [
    path('directors/<int:id>/', DirectorModelViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('directors/', DirectorModelViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('movies/', MovieModelViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('movies/<int:id>/', MovieModelViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('reviews/', ReviewModelViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('reviews/<int:id>/', ReviewModelViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('movies/reviews/', MovieReviewListAPIView.as_view())
]
# movies_view, movie_detail_view, reviews_view, review_detail_view, movies_reviews_view,directors_view, director_detail_view,