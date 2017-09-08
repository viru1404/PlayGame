from __future__ import unicode_literals
from datetime import datetime  
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Questions(models.Model):
    ques = models.ImageField(upload_to = 'pic_folder/')
    ans1 = models.ImageField(upload_to = 'pic_folder/')
    ans2 = models.ImageField(upload_to = 'pic_folder/')
    ans3 = models.ImageField(upload_to = 'pic_folder/')
    ans4 = models.ImageField(upload_to = 'pic_folder/')
    ans5 = models.ImageField(upload_to = 'pic_folder/')


class Activeusers(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	qid1 = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='qid1' , null=True)
	qid2 = models.ForeignKey(Questions, related_name='qid2', null=True)
	qid3 = models.ForeignKey(Questions, related_name='qid3', null=True)
	qid4 = models.ForeignKey(Questions, related_name='qid4', null=True)
	qid5 = models.ForeignKey(Questions, related_name='qid5', null=True)
	answer1 = models.IntegerField(default=0)
	answer2 = models.IntegerField(default=0)
	answer3 = models.IntegerField(default=0)
	answer4 = models.IntegerField(default=0)
	answer5 = models.IntegerField(default=0)
	timetill = models.DateTimeField(default=datetime.now, blank=True)
	isfinished = models.IntegerField(default=0)
	score =models.IntegerField(default=0)
class checkfun(models.Model):
    id1 = models.IntegerField(default=0)
    id2 = models.IntegerField(default=0)

class timer(models.Model):
	id1 = models.IntegerField(default=0)
	id2=models.IntegerField(default=0)
	timetill = models.DateTimeField(default=datetime.now, blank=True)

 