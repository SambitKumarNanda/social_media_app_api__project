from django.db import models


# Create your models here.
class CountryModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class StateModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(CountryModel, related_name="StateModel_country", on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CityModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(CountryModel, related_name="CityModel_country", on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(StateModel, related_name="CityModel_state", on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PrimaryEducationAddressModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE,
                                related_name="PrimaryEducationAddressModel_country", null=True)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE, related_name="PrimaryEducationAddressModel_state",
                              null=True)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name="PrimaryEducationAddressModel_city",
                             null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SecondaryEducationAddressModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE,
                                related_name="SecondaryEducationAddressModel_country", blank=True)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE, related_name="SecondaryEducationAddressModel_state",
                              null=True)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name="SecondaryEducationAddressModel_city",
                             null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HigherEducationAddressModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE,
                                related_name="HigherEducationAddressModel_country", blank=True)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE, related_name="HigherEducationAddressModel_state",
                              null=True)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name="HigherEducationAddressModel_city",
                             null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CollegeEducationModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE,
                                related_name="CollegeEducationAddressModel_country", null=True)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE, related_name="CollegeEducationAddressModel_state",
                              null=True)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name="CollegeEducationAddressModel_city",
                             null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class EmploymentModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE,
                                related_name="EmploymentModel_country", null=True)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE, related_name="EmploymentModel_state",
                              null=True)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE, related_name="EmploymentModel_city",
                             null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
