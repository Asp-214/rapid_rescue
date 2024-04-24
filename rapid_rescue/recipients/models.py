from django.db import models

# Create your models here.


class Recipients(models.Model):
    recipient_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    recipient_address = models.TextField(blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = True
        db_table = 'Recipients'

    def __str__(self) -> str:
        return f"Recipients - {id} , {self.recipient_name}"
    


class MessageLog(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Falied'),
    )
    accident = models.ForeignKey( 'accidents.Accidents', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='accident_messages')
    recipient = models.ForeignKey('Recipients', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='sent_messages')
    message_content = models.TextField(blank=True, null=True)
    message_status = models.TextField( choices=STATUS_CHOICES, blank=True, null=True)
    class Meta:
        # managed = True
        db_table = 'MessageLog'

    def __str__(self) -> str:
        return f"MessageLog - {self.pk} , {self.accident} , {self.message_status}"