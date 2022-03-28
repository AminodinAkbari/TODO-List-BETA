from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoModel(models.Model):
	STATUS= (
    ('High','High'),
    ('Medium','Medium'),
    ('Low','Low'),
    )
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	task = models.CharField(max_length = 1200)
	date = models.DateTimeField(blank=True , null=True)
	status  = models.CharField(max_length=20,choices=STATUS,default='Low',blank=True,null=True)
	done = models.BooleanField(default=False)


