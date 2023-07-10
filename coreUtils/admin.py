from django.contrib import admin
from .models import CityModel, CountryModel, StateModel, PrimaryEducationAddressModel, SecondaryEducationAddressModel, \
    HigherEducationAddressModel, CollegeEducationModel, EmploymentModel

# Register your models here.
admin.site.register(CityModel)
admin.site.register(CountryModel)
admin.site.register(StateModel)
admin.site.register(PrimaryEducationAddressModel)
admin.site.register(SecondaryEducationAddressModel)
admin.site.register(HigherEducationAddressModel)
admin.site.register(CollegeEducationModel)
admin.site.register(EmploymentModel)
