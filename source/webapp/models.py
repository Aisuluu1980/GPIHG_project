from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Project')
    image = models.ImageField(upload_to='projects_images', null=True, blank=True, verbose_name='Image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
