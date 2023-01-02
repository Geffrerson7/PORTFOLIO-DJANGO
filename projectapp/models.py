from django.db import models
from django.urls  import reverse
from django.db import models
from django.db.models.fields import CharField, URLField


class Project(models.Model):
    class tagsOption(models.TextChoices):
        PYTHON = 'python', 
        DJANGO = 'django',
        FLASK = 'flask',         

    tags = models.CharField(
        max_length=10,
        choices=tagsOption.choices,
        default=tagsOption.PYTHON,
    )
    title = CharField(max_length=200)
    description = models.TextField()
    url_image = URLField(blank=True)
    url_github = URLField(blank=True)
    

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    

