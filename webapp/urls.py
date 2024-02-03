from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("gallery/", views.gallery, name="gallery"),
    path("login/", views.sign_in, name="login"),
    path("authenticate", views.sign_in_user, name="authenticate_user"),
    path("reservation", views.reservation, name="reservation"),
    # path('register/', views.sign_up, name="register")
    path(
        "dashboard/",
        include(
            [
                path("", views.dashboard, name="dashboard"),
                path(
                    "reservation/",
                    include(
                        [
                            path("", views.reservation_index, name="reservation_index"),
                            path(
                                "show/<int:reservationID>",
                                views.reservation_show,
                                name="reservation_show",
                            ),
                            path(
                                "delete/<int:reservationID>",
                                views.reservation_delete,
                                name="reservation_delete",
                            ),
                            path(
                                "edit/<int:reservationID>",
                                views.reservation_edit,
                                name="reservation_edit",
                            ),
                        ]
                    ),
                ),
                path(
                    "news/",
                    include(
                        [
                            path("", views.new_index, name="new_index"),
                            path(
                                "create",
                                views.new_create,
                                name="new_create",
                            ),
                            path(
                                "show/<int:newsID>",
                                views.new_show,
                                name="new_show",
                            ),
                            path(
                                "delete/<int:newsID>",
                                views.new_delete,
                                name="new_delete",
                            ),
                            
                            # path(
                            #     "delete/<int:reservationID>",
                            #     views.reservation_delete,
                            #     name="reservation_delete",
                            # ),
                            # path(
                            #     "edit/<int:reservationID>",
                            #     views.reservation_edit,
                            #     name="reservation_edit",
                            # ),
                        ]
                    ),
                ),
            ]
        ),
    ),
]
