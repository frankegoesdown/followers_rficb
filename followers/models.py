from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Man(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=32)
    follow = models.ManyToManyField('self', symmetrical=False, related_name='pursued')

    class Meta:
        managed = True

    def __str__(self):
        return "%s, id=%s" % (self.name, self.id)


class Follow(models.Model):
    '''Describes follow relation between Man instances: who follows whom'''
    from_man = models.ForeignKey('Man', related_name='from_man')
    to_man = models.ForeignKey('Man', related_name='to_man')

    class Meta:
        db_table = 'followers_man_follow'
        unique_together = ('from_man', 'to_man')
