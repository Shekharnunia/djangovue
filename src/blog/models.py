from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """This class will going to contain the blog database table data."""

    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Blog."""

        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        """Unicode representation of Blog."""
        return self.title