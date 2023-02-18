from django.db import models

# Create your models here.
heading = models.ForeignKey(ForumSections, on_delete=models.CASCADE)
