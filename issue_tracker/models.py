from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class Project(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def get_absolute_url(self):
        return reverse('issue_tracker:list_of_issue_by_project', args=[self.slug])

    def __str__(self):
        return self.name


class Issue(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Issue, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('issue_tracker:issue_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    issue = models.ForeignKey(Issue, related_name='Comment', on_delete=models.PROTECT)
    user = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def Approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.user





