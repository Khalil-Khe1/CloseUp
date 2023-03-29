"""CloseUp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from front.src.pages.views import homepage_view, user_create_view, login_view, sign_out, gen_form
from front.src.pages.front_event import dashboard_view, event_create_view, event_view, event_discussion, comment_create_view, comment_view, comment_generate_temp_display, event_discussion_details

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage_view, name="homepage"),
    path("create-user", user_create_view, name="create-user"),
    path("login", login_view, name="login"),
    path("sign-out", sign_out, name="sign-out"),
    path("event-dashboard", dashboard_view, name="event-dashboard"),
    path("event-create", event_create_view, name="event-create"),
    path("comment-create", comment_create_view, name="comment-create"),
    path("temp-comment-create", comment_generate_temp_display, name="comment-temp-display"),
    path("test", event_view, name="test"),
    path("event/id_<int:event_id>/", event_view, name='event-detail'),
    path("event/id_<int:event_id>/discussion/", event_discussion, name='event-discussion'),
    path("event/id_<int:event_id>/discussion/threads/", comment_view, name='comment'),
    path("event/id_<int:event_id>/discussion/threads/post_id<int:post_id>", event_discussion_details, name='discussion-details'),


]
