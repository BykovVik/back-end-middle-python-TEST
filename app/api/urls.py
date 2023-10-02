from django.urls import path
from .views import UserCreateView, UserRetrieveUpdateDestroyView, UserLoginView, UserRegistrationView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='v1',
      description="API documentation",
   ),
   public=True,
)

urlpatterns = [
   path('register/', UserRegistrationView.as_view(), name='user-registration'),
   path('login/', UserLoginView.as_view(), name='user-login'),
   path("users/", UserCreateView.as_view()),
   path("users/<int:pk>/", UserRetrieveUpdateDestroyView.as_view()),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]