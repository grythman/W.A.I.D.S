from rest_framework import serializers
from .models import Course, Lesson, Lecture, Enroll, Complete, Question, Answer, File, Category, Profile, Role, Solution
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    role = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = ('id', 'user', 'name', 'avatar_thumbnail', 'role', 'stripe_id', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role_name', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class CourseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'user', 'category', 'course_name', 'course_summary', 'course_information', 'course_image', 'course_thumbnail', 'course_instructor_name', 'course_instructor_info', 'course_instructor_avatar', 'course_featured', 'course_status', 'course_price', 'course_video', 'archive', 'created_at', 'updated_at')
        read_only_fields = ('course_image', 'course_thumbnail', 'created_at', 'updated_at')

class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'course', 'lesson_name', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class LectureSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = Lecture
        fields = ('id', 'lesson', 'lecture_name', 'lecture_content', 'lecture_type', 'lecture_video', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class EnrollSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enroll
        fields = ('id', 'user', 'course', 'status', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class CompleteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    lecture = LectureSerializer(read_only=True)

    class Meta:
        model = Complete
        fields = ('id', 'user', 'lecture', 'grade', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class QuestionSerializer(serializers.ModelSerializer):
    lecture = LectureSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'lecture', 'question_content', 'question_type', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer_content', 'is_correct', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class SolutionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = Solution
        fields = ('id', 'user', 'question', 'answer', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

class FileSerializer(serializers.ModelSerializer):
    lecture = LectureSerializer(read_only=True)

    class Meta:
        model = File
        fields = ('id', 'lecture', 'file_data', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
