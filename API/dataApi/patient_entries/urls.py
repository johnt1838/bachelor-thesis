from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patient_entries import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(
    r"patient_entries", views.patient_entryViewSet, basename="patient_entries"

)
router.register(
    r"patient_entries_test", views.patient_entry_testViewSet, basename="patient_entries_test"

)
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
