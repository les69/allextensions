from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Program(models.Model):
    name = models.CharField()
    website = models.URLField(null="true")
    picture = models.ImageField(upload_to="images/program_pictures/", default="images/defaults/default_program.jpg")
    description = models.CharField(max_length=250, default="")

class Extension(models.Model):
    type = models.CharField(max_length=250)
    description = models.CharField(max_length=300, default="")
    program = models.ManyToManyField(Program, related_name="programs")
    icon = models.ImageField(upload_to="images/icon_pictures/", default="images/defaults/default_icon.jpg")

    def _do_stuff(self):
        print 'make me do something'




@receiver(post_save, sender=Extension)
def post_save_do_stuff(sender, **kwargs):
    """ Calls the do_stuff function on the saved instance if it was
        just created
    """
    if kwargs['created']:
        kwargs['instance']._do_stuff()