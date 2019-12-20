from django.db import models

"""
Note: When running both the makemigrations and migrate commands, 
we added projects to our command. This tells Django to only look at 
models and migrations in the projects app. Django comes with several 
models already created.

If you run makemigrations and migrate without the projects flag, then 
all migrations for all the default models in your Django projects will be 
created and applied. This is not a problem, but for the purposes of this 
section, they are not needed.
"""

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='/image')