from django.db import models

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50)
    contactInfo = models.TextField()

    def login(self):
        pass  # Implement login logic

    def logout(self):
        pass  # Implement logout logic

class Admin(User):
    adminID = models.AutoField(primary_key=True)

    def manageContent(self):
        pass

class Student(User):
    studentID = models.AutoField(primary_key=True)
    placementInfo = models.TextField()
    journalEntries = models.ManyToManyField('Journal', related_name='students')
    mentorID = models.ForeignKey('Mentor', on_delete=models.SET_NULL, null=True)

class Mentor(User):
    mentorID = models.AutoField(primary_key=True)
    students = models.ManyToManyField(Student, related_name='mentors')

class Session(models.Model):
    sessionID = models.AutoField(primary_key=True)
    sessionName = models.CharField(max_length=150)
    participants = models.ManyToManyField(User)
    sessionStatus = models.CharField(max_length=50)

class Content(models.Model):
    contentID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.ForeignKey(Admin, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)

class Journal(models.Model):
    journalID = models.AutoField(primary_key=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    entries = models.TextField()
    creationDate = models.DateTimeField(auto_now_add=True)

class Monitoring(models.Model):
    monitoringID = models.AutoField(primary_key=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentorID = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)