from django.db import models


# Create your models here.

class Severity(models.Model):
    severity_id = models.AutoField(primary_key=True)
    severity_level = models.IntegerField(blank=True, null=True)
    severity_description = models.TextField(blank=True, null=True)
    class Meta:
        # managed = True
        db_table = 'Severity'

    def __str__(self) -> str:
        return self.severity_level
    


class Accidents(models.Model):
    accident_date = models.DateField(blank=True, null=True)
    accident_time = models.TimeField(blank=True, null=True)
    camera = models.ForeignKey( 'cameras.Cameras', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='nearby_accidents' )
    severity = models.ForeignKey( Severity , on_delete=models.DO_NOTHING, blank=True, null=True,related_name='listed_accidents') 
    location = models.ForeignKey( 'cameras.Locations' , models.DO_NOTHING, blank=True, null=True)
    video_clip = models.BinaryField(blank=True, null=True)

    class Meta:
        # managed = True
        db_table = 'Accidents'
