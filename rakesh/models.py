from django.db import models


# Create your models here.

class Project(models.Model):
    PROJ_FILTER = (
        ('filter-app', 'RA'),
        ('filter-card', 'Autotest'),
        ('filter-web', 'Freelance'),
    )
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, default='def_img1.jpg', )
    proj_filter = models.CharField(choices=PROJ_FILTER, null=True, blank=True, max_length=50)
    client = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=250, null=True)
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class MyResumeModel(models.Model):
    my_name = models.CharField(max_length=100, null=True, blank=True)
    about_headline = models.TextField(null=True, blank=True)
    current_profile = models.CharField(max_length=100, null=True, blank=True)
    current_profile_details = models.TextField(null=True, blank=True)
    my_age = models.CharField(max_length=100, null=True, blank=True)
    my_phone = models.CharField(max_length=100, null=True, blank=True)
    my_current_location = models.CharField(max_length=100, null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    freelance = models.CharField(max_length=100, null=True, blank=True)
    about_myself = models.TextField(null=True, blank=True)
    skills_details = models.TextField(null=True, blank=True)
    skill1 = models.CharField(max_length=100, null=True, blank=True)
    skill1_percentage = models.CharField(max_length=100, null=True, blank=True)
    skill2 = models.CharField(max_length=100, null=True, blank=True)
    skill2_percentage = models.CharField(max_length=100, null=True, blank=True)
    skill3 = models.CharField(max_length=100, null=True, blank=True)
    skill3_percentage = models.CharField(max_length=100, null=True, blank=True)
    skill4 = models.CharField(max_length=100, null=True, blank=True)
    skill4_percentage = models.CharField(max_length=100, null=True, blank=True)
    skill5 = models.CharField(max_length=100, null=True, blank=True)
    skill5_percentage = models.CharField(max_length=100, null=True, blank=True)
    skill6 = models.CharField(max_length=100, null=True, blank=True)
    skill6_percentage = models.CharField(max_length=100, null=True, blank=True)
    resume_summary = models.TextField(null=True, blank=True)
    education1_name = models.CharField(max_length=100, null=True, blank=True)
    education1_year = models.CharField(max_length=100, null=True, blank=True)
    education1_univ_name = models.TextField(null=True, blank=True)
    education1_board = models.CharField(max_length=100, null=True, blank=True)
    education2_name = models.CharField(max_length=100, null=True, blank=True)
    education2_year = models.CharField(max_length=100, null=True, blank=True)
    education2_univ_name = models.TextField(null=True, blank=True)
    education2_board = models.CharField(max_length=100, null=True, blank=True)
    exp1_profile = models.CharField(max_length=100, null=True, blank=True)
    exp1_duration = models.CharField(max_length=100, null=True, blank=True)
    exp1_company = models.CharField(max_length=100, null=True, blank=True)
    exp1_role1 = models.TextField(null=True, blank=True)
    exp1_role2 = models.TextField(null=True, blank=True)
    exp1_role3 = models.TextField(null=True, blank=True)
    exp2_profile = models.CharField(max_length=100, null=True, blank=True)
    exp2_duration = models.CharField(max_length=100, null=True, blank=True)
    exp2_company = models.CharField(max_length=100, null=True, blank=True)
    exp2_role1 = models.TextField(null=True, blank=True)
    exp2_role2 = models.TextField(null=True, blank=True)
    exp2_role3 = models.TextField(null=True, blank=True)
    exp3_profile = models.CharField(max_length=100, null=True, blank=True)
    exp3_duration = models.CharField(max_length=100, null=True, blank=True)
    exp3_company = models.CharField(max_length=100, null=True, blank=True)
    exp3_role1 = models.TextField(null=True, blank=True)
    exp3_role2 = models.TextField(null=True, blank=True)
    exp3_role3 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.my_name
