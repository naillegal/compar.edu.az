from django.db import models
from shared.urlutils import get_slug
from django.urls import reverse
# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Ad')
    updated = models.DateField(auto_now = True, verbose_name='Dəyişdirildi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradıldı')

    class Meta:
        ordering = ['-updated']
        verbose_name = 'Teq'
        verbose_name_plural = 'Teqlər'

    def __str__(self):
        return self.title
    
class Course(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Başlıq')
    slug = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=False, blank=False, verbose_name='Mətn')
    image = models.ImageField(upload_to='course/', null=False, blank=False, verbose_name='Şəkil')
    tags = models.ManyToManyField(Tag, verbose_name='Teqlər')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'

    def __str__(self):
        return self.title + ' kurs'
    
    def save(self, *args, **kwargs):
        self.slug = get_slug(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("course-detail", kwargs={"pk": self.pk, 'slug': self.slug})
    
class Lesson(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Dərs adı')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')
    class Meta:
        ordering = ['-updated']
        verbose_name = 'Dərs'
        verbose_name_plural = 'Dərslər'

    def __str__(self):
        return self.name
    
    
class CourseOpportunity(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Başlıq')
    description = models.TextField(null=False, blank=False, verbose_name='Mətn')
    image = models.ImageField(upload_to='course/opportunity/', null=False, blank=False, verbose_name='Şəkil')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Kurs')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')


    class Meta:
        ordering = ['-created']
        verbose_name = 'Kurs Fürsəti'
        verbose_name_plural = 'Kurs Fürsətləri'

    def __str__(self):
        return self.title + ' fürsət'
    
    
class CourseSyllabus(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Başlıq')
    description = models.TextField(null=False, blank=False, verbose_name='Proqram açıqlaması')
    duration = models.CharField(max_length=100, null=False, blank=False, verbose_name='Müddət')
    lesson = models.ManyToManyField('Lesson', verbose_name='Dərs adları')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Kurs')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Kurs Proqramı'
        verbose_name_plural = 'Kurs Proqramları'

    def __str__(self):
        return self.title + ' proqram'
    
    
    
class CourseTeacher(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Ad, Soyad')
    job_title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Vəzifə')
    description = models.TextField(null=False, blank=False, verbose_name='Mətn')
    image = models.ImageField(upload_to='teacher/', null=False, blank=False, verbose_name='Şəkil')
    courses = models.ManyToManyField(Course, related_name='teachers', verbose_name='Kurslar')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Müəllim'
        verbose_name_plural = 'Müəllimlər'
        
    def __str__(self):
        return self.full_name + ' müəllim'