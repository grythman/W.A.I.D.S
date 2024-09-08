from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    avatar_thumbnail = ProcessedImageField(upload_to='avatars', processors=[ResizeToFill(150, 150)], format='PNG')
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Role(models.Model):
        role_name = models.CharField(max_length=255)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    

class Category(models.Model):
    category_name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255, blank=True)
    course_summary = models.TextField(blank=True)
    course_information = models.TextField(blank=True)
    course_image = models.ImageField(upload_to="i", blank=True)
    course_thumbnail = ImageSpecField(source='course_image', processors=[ResizeToFill(512, 512)], format='PNG')
    course_instructor_name = models.CharField(max_length=255, blank=True)
    course_instructor_info = models.TextField(blank=True)
    course_instructor_avatar = models.ImageField(upload_to="i", blank=True)
    course_featured = models.BooleanField(blank=False)
    course_status = models.CharField(max_length=255, blank=False)
    course_price = models.IntegerField(blank=True)
    course_video = models.TextField(blank=True)
    archive = models.BooleanField(blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Lecture(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    lecture_name = models.CharField(max_length=255, blank=False)
    lecture_content = models.TextField(blank=True)
    lecture_type = models.CharField(max_length=255, blank=False)
    lecture_video = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Enroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Complete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    grade = models.DecimalField(blank=False, max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Question(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    question_content = models.TextField(blank=False)
    question_type = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_content = models.TextField(blank=False)
    is_correct = models.BooleanField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Solution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class File(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    file_data = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
