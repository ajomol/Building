from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import View,ListView,DeleteView
from django.http import HttpResponse
from django.contrib import messages #import messages

from building.forms import BuildingDetailsForm
from building.models import BuildingGroup,BuildingDetails

class NewBuilding(View):
    '''Add new building'''
    template_name = 'building.html'
    form_class = BuildingDetailsForm

    def get(self,request):
        form = self.form_class()
        context={
        'form':form
        }
        return render(request,self.template_name,context)

    def post(self,request):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, "Building details successfully added" )
            # try:
            #     grp_obj = BuildingGroup.objects.get(id=request.POST.get('building_grp'))
            # except BuildingGroup.DoesnotExist:
            #     grp_obj = None
            # try:
            #     build_obj = BuildingDetails.objects.get(build_name=request.POST.get('build_name'),is_active=True)
            # except Exception as e:
            #     build_obj = None

            # print(build_obj)
            # if build_obj is None:
            #     build_obj = BuildingDetails.objects.create(
            #         build_name=request.POST.get('build_name'),
            #         build_address=request.POST.get('build_address'),
            #         building_grp=grp_obj,
            #         region=request.POST.get('region'),
            #         country=request.POST.get('country'),
            #         point_of_contact=request.POST.get('point_of_contact'),
            #         email=request.POST.get('email'),
            #         contact=request.POST.get('contact')
            #     )
            #     messages.success(request, "Building details successfully added" )
            #     form = self.form_class()
            # else:
            #     messages.error(request, "Building with same name already existe!!!" )
        else:
            messages.error(request, "Oops something went wrong" )
        return render(request,self.template_name,{'form':form})

class AllBuildingList(ListView):
    '''To list all building details'''
    template_name = 'all_building.html'
    model = BuildingDetails
    context_object_name = 'all_buildings'

class DeleteBuilding(DeleteView):
    template_name = 'buildingdetails_confirm_delete.html'
    model = BuildingDetails

    def get_success_url(self):
        messages.success(self.request, "deleted successfully")
        return reverse("building:all_building")
    # def get(self,request,pk):
    #   build_obj = BuildingDetails.objects.get(id=pk).delete()
    #   build_obj = BuildingDetails.objects.all()
    #   context = {
    #   'all_buildings':build_obj
    #   }
    #   return render(request,self.template_name,context)