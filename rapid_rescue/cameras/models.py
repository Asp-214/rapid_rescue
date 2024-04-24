from django.db import models



# Create your models here.


class CameraProtocols(models.Model):
    protocol = models.CharField(primary_key=True, max_length=100)

    class Meta:
        # managed = True
        db_table = 'CameraProtocols'

    def __str__(self) -> str:
        return self.protocol



class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    class Meta:
        # managed = True
        db_table = 'Locations'

    def __str__(self) -> str:
        return f"Location - {self.latitude} , {self.longitude}"



class Cameras(models.Model):
    camera_name = models.CharField(max_length=100, blank=False, null=False)
    protocol = models.ForeignKey( CameraProtocols , models.DO_NOTHING, db_column='protocol', blank=False, null=False, related_name='list_cameras')
    camera_ip = models.CharField(max_length=100, blank=False, null=False)
    camera_auth = models.BooleanField(blank=False, null=False)
    camera_username = models.CharField(max_length=100, blank=True, null=True)
    camera_password = models.CharField(max_length=100, blank=True, null=True)
    camera_stream_path = models.CharField(max_length=255, blank=True, null=True)
    camera_port_no = models.IntegerField(blank=True, null=True)
    recipient = models.ForeignKey('recipients.Recipients', on_delete=models.DO_NOTHING, blank=True, null=True , related_name='recipient_camera')
    location = models.ForeignKey('Locations' , on_delete=models.DO_NOTHING, blank=False, null=False, related_name='list_cameras')
    is_active = models.BooleanField(blank=True, null=True, default=True)
    is_exist = models.BooleanField(blank=True, null=True, default=True)
    added_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = True
        db_table = 'Cameras'

    def __str__(self) -> str:
        return f" Camera - {self.pk} , {self.camera_name} , {self.camera_ip}"