from django.urls import path
from . import views
from shop import views


urlpatterns = [
    path("",views.index,name="Shop Home"),
    path("about/",views.about,name="about us"),
    path("contact/",views.contact,name="contact us"),
    # path("test/",views.Contact.as_view(), name="test"),
    path("tracker/",views.tracker,name="tracking status"),
    path("search/",views.search,name="search"),
    path("products/<int:myid>",views.productview,name="productview"),
    path("checkout/",views.checkout,name="checkout"),

]
