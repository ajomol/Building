from django.contrib import admin
from django.urls import path,include
from building.views import NewBuilding,AllBuildingList,DeleteBuilding
app_name ="building"

urlpatterns = [
	path('building/',NewBuilding.as_view(),name='add_building'),
	path('allbuilding/',AllBuildingList.as_view(),name='all_building'),
	path('delete/<int:pk>/',DeleteBuilding.as_view(),name='build_delete'),

]
