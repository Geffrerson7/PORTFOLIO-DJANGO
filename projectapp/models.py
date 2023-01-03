from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields import CharField, URLField


def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except ValidationError:
        raise ValidationError("Invalid URL for this field")

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
    url_image = URLField(validators=[validate_url])
    url_github = URLField(validators=[validate_url])
    

    def __str__(self) -> str:
        return self.title

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"pk": self.pk})

    

