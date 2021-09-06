from decouple import config
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.routers import DefaultRouter

from app.views.user import NewUserCreateView
from app.views.login import UserLoginView
from app.views.index import IndexView
from app.views.ask_a_question import AskQuestionView

schema_view = get_schema_view(
    openapi.Info(title="Hasker API", default_version="v1",),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # url=f"",
    authentication_classes=(BasicAuthentication,),
)

router = DefaultRouter()
router.register(r"ask", IndexView, basename="index")
router.register(r"^signup", NewUserCreateView, basename="signup")
router.register(r"^login", UserLoginView, basename="login")
router.register(r"^ask_a_question", AskQuestionView, basename="ask_a_question")


urlpatterns = (
    [
        url("", include(router.urls)),
        path('logout/', views.LogoutView.as_view(next_page='/ask/'), name='logout'),
        url(r"^admin/", admin.site.urls),

        url(
            r"^swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        url(
            r"^redoc/$",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
