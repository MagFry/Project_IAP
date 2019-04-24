from django.db import models

# Create your models here.

class Branch_Office(models.Model):
    branch_office_id = models.AutoField(primary_key=True)
    branch_office_name = models.CharField(max_length=200)
    branch_office_location = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Returns url to access a particular instance of Branch_Office"""
        return reverse('branch-office-view', args = [str(self.id)])

    def __str__(self):
        return self.branch_office_name