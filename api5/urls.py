from django.contrib import admin
from django.urls import path, include
from api5.views import CompanyViewSet, ImageSliderViewSet, QuickLinksViewSet, Objectives_of_Sikkim_UniversityViewSet, Upcoming_Events_ViewSet, School_ViewSet, Department_ViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'imageslider',ImageSliderViewSet)
router.register(r'quicklinks',QuickLinksViewSet)
router.register(r'Objectives_of_Sikkim_University',Objectives_of_Sikkim_UniversityViewSet)
router.register(r'upcoming_events',Upcoming_Events_ViewSet)
router.register(r'school',School_ViewSet)
router.register(r'department',Department_ViewSet)

urlpatterns = [
    path('',include(router.urls))
]
