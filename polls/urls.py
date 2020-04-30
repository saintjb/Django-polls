from django.urls import path
from . import views
from .views import IndexView, DetailView, ResultsView

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:pk>/', DetailView.as_view()),
    path('<int:pk>/results/', ResultsView.as_view()),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]