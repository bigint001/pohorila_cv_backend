from django.db import models

class Header(models.Model):
    background = models.ImageField(upload_to="header/")
    avatar = models.ImageField(upload_to="header/")

    def __str__(self):
        return "Header settings"


class PdfCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PdfFile(models.Model):
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        PdfCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='pdfs'
    )

    def __str__(self):
        return self.title


class Summary(models.Model):
    name = models.CharField(max_length=255)
    paragraph_1 = models.TextField(blank=True, null=True)
    paragraph_2 = models.TextField(blank=True, null=True)
    paragraph_3 = models.TextField(blank=True, null=True)
    phone_1 = models.CharField(max_length=20, blank=True, null=True)
    phone_2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    pdfs = models.ManyToManyField(PdfFile, blank=True, related_name='summaries')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # описание
    main_image = models.ImageField(upload_to="projects/main/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="projects/gallery/")

    def __str__(self):
        return f"{self.project.title} - {self.image.name}"

