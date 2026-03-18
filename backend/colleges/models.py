from django.db import models

class College(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    established_year = models.IntegerField()
    website = models.URLField()
    image = models.ImageField(upload_to='college_images/', blank=True, null=True)
    
    # Placement Details
    placement_description = models.TextField(blank=True, null=True, help_text="Details about placement statistics and companies.")
    average_package = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Average package in LPA")
    highest_package = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Highest package in LPA")
    
    def __str__(self):
        return self.name

class Course(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50) # e.g., "4 Years"
    
    def __str__(self):
        return f"{self.name} at {self.college.name}"

class Facility(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='facilities')
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Icon name from frontend library")
    
    def __str__(self):
        return f"{self.name} - {self.college.name}"

class GalleryMedia(models.Model):
    CATEGORY_CHOICES = (
        ('classroom', 'Classroom'),
        ('campus', 'Campus'),
        ('library', 'Library'),
        ('hostel', 'Hostel'),
        ('canteen', 'Canteen'),
        ('seminar_hall', 'Seminar Hall'),
        ('ground', 'Ground'),
        ('laboratory', 'Laboratory'),
        ('other', 'Other'),
    )
    MEDIA_TYPE_CHOICES = (
        ('photo', 'Photo'),
        ('video', 'Video'),
    )

    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='gallery_media')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to='gallery/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='photo')
    title = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.college.name}"
