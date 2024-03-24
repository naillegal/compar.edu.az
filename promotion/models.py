from tabnanny import verbose
from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Ad, Soyad')
    contact = models.CharField(max_length=100, null=False, blank=False, verbose_name='Email və ya Telefon')
    subject = models.CharField(max_length=100, null=False, blank=False, verbose_name='Mövzu')
    message = models.TextField(null=False, blank=False, verbose_name='Mesaj')
    viewed = models.BooleanField(default=False, verbose_name='Baxdım')
    created = models.DateField(auto_now_add=True, verbose_name='Göndərilmə Tarixi')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Müraciət'
        verbose_name_plural = 'Müraciətlər'

    def __str__(self):
        return self.name + ' müraciət'
    
    
class Slider(models.Model):
    headline = models.CharField(max_length=100, null=False, blank=False, verbose_name='Başlıq')
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Başlıq')
    description = models.TextField(null=False, blank=False, verbose_name='Mətn')
    image = models.ImageField(upload_to='slider/', null=False, blank=False, verbose_name='Şəkil')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliderlər'

    def __str__(self):
        return self.title + ' slider'


class StudentReview(models.Model):
    profile_picture = models.ImageField(upload_to='student/', null=False, blank=False, verbose_name='Profil Şəkli')
    full_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Ad, Soyad')
    job_title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Vəzifə')
    comment = models.TextField(null=False, blank=False, verbose_name='Rəy')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Tələbə Rəyi'
        verbose_name_plural = 'Tələbə Rəyləri'
        
    def __str__(self):
        return self.full_name + ' rəyi'


class Alumni(models.Model):
    profile_picture = models.ImageField(upload_to='alumni/', null=False, blank=False, verbose_name='Profil Şəkli')
    full_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Ad, Soyad')
    job_title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Vəzifə')
    linkedin_url = models.URLField(max_length=200, null=False, blank=False, verbose_name='Linkedin URL')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Alumni'
        verbose_name_plural = 'Alumni'
        
    def __str__(self):
        return self.full_name + ' Alumni'
    
    
class Faq(models.Model):
    question = models.TextField(null=False, blank=False, verbose_name='Sual')
    answer = models.TextField(null=False, blank=False, verbose_name='Cavab')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
        
    def __str__(self):
        return self.question + ' sualı'
    
    
class AboutStatictic(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Başlıq')
    count = models.IntegerField(default=0, verbose_name='Say')
    description = models.TextField()
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Haqqımızda Statistika'
        verbose_name_plural = 'Haqqımızda Statistikalar'
        
    def __str__(self):
        return self.title + ' statistikası'
    
class StudentProjectTag(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Başlıq')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Tələbə Layihəsi Teq'
        verbose_name_plural = 'Tələbə Layihəsi Teqləri'
        
    def __str__(self):
        return self.title + ' tag'
        
        
class StudentProject(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Başlıq')
    description = models.TextField(null=False, blank=False, verbose_name='Mətn')
    image = models.ImageField(upload_to='student/project/', null=False, blank=False, verbose_name='Şəkil')
    project_url = models.URLField(max_length=200, null=False, blank=False, verbose_name='Layihə URL')
    tags = models.ManyToManyField(StudentProjectTag, verbose_name='Teqlər')
    updated = models.DateField(auto_now=True, verbose_name='Yenilənmə Tarixi')
    created = models.DateField(auto_now_add=True, verbose_name='Yaradılma Tarixi')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Tələbə Layihəsi'
        verbose_name_plural = 'Tələbə Layihələri'
        
    def __str__(self):
        return self.title + ' layihəsi'
    
