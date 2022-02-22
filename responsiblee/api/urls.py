from .views import EmissionListView, EmissionAddView
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Responsiblee API",
      default_version='0.0.1',
      description="Test",
   ),
   public=True,
)

urlpatterns = [
    path('emissions/view', EmissionListView.as_view()),
    path('emissions/add', EmissionAddView.as_view()),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
