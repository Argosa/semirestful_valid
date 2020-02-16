from __future__ import unicode_literals
from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData["show_name"]) < 2:
            errors["show_name"] = 'Show name should be 2 characters or more'
        if len(postData["show_release"]) < 8:
            errors["show_release"] = 'Show release date needs to be entered'
        if len(postData["show_desc"]) < 10:
            errors["show_desc"] = 'Show description requires 10 characters or more'
        return errors
    
    def edit_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData["new_title"]) < 2:
            errors["new_title"] = 'Show name should be 2 characters or more'
        if len(postData["new_release_date"]) < 8:
            errors["new_release_date"] = 'Show release date needs to be entered'
        if len(postData["new_description"]) < 10:
            errors["new_description"] = 'Show description requires 10 characters or more'
        return errors

class Network(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.name} {self.created_at} {self.updated_at}"

class Show(models.Model):
    name = models.CharField(max_length=255)
    network = models.ForeignKey(Network, related_name= "networks", on_delete = models.CASCADE)
    release_date = models.DateField()
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"{self.name} {self.network} {self.release_date} {self.desc} {self.created_at} {self.updated_at}"

