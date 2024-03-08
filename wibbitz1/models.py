from django.db import models

COMPANY_SIZE_CHOICES = [
    ("1", "1-10"),
    ("2", "11-50"),
    ("3", "51-200"),
    ("4", "200-500"),
]

INDUSTRY_CHOICES = [
    ("1", "Agriculture"),
    ("2", "Banking, Finance"),
    ("3", "Business Services & Software")
]

JOB_ROLE_CHOICES = [
    ("1", "C-Sute"),
    ("2", "VP")
]

COUNTRY_CHOICES = [
    ("us", "United States"),
    ("albania", "Albania")
]

class Customer(models.Model):
    image = models.FileField(upload_to="media/")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.image)


class Subscribe(models.Model):
    email = models.EmailField(unique=False, primary_key=True)

    def __str__(self):
        return self.email


class Featured(models.Model):
    image = models.ImageField(upload_to="media/")
    icon_logo = models.FileField(upload_to="media/")
    icon_background = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    testimonial_description = models.TextField(max_length=255)
    testimonial_author = models.CharField(max_length=255)
    author_description = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to="media/")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title


class Videoblog(models.Model):
    logo_admin = models.FileField(upload_to="videoblog_admin/")
    image = models.ImageField(upload_to="video/")
    title = models.CharField(max_length=100)
    logo = models.FileField(upload_to="videoblog/")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonial/")
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    p_designation = models.CharField(max_length=200)
    company_name = models.CharField(max_length=50)
    is_featured = models.BooleanField()
    logo = models.FileField(upload_to="testi/")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Marketing(models.Model):
    image = models.FileField(upload_to="markating/")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    a_description = models.TextField(blank=True, max_length=30)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title


class Business(models.Model):
    business_background = models.FileField(upload_to="background/")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="business/")
    background = models.CharField(max_length=10)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title


class Videoresources(models.Model):
    image = models.ImageField(upload_to="video/")
    heding = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    spana = models.CharField(max_length=255)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.heding


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    company_size_choices = models.CharField(max_length=128, choices=COMPANY_SIZE_CHOICES)
    industry_choices = models.CharField(max_length=128, choices=INDUSTRY_CHOICES)
    job_role_choices = models.CharField(max_length=128, choices=JOB_ROLE_CHOICES)
    country_choices = models.CharField(max_length=128, choices=COUNTRY_CHOICES)
    user = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.first_name



class Img (models.Model):
    image = models.FileField(upload_to="afe/", blank=True)
    h1 = models.CharField(max_length=100)


class  Latest_customer (models.Model):
    image = models.FileField(upload_to="media10/")