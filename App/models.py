from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone = models.CharField(max_length=10)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=7)
    userimage = models.ImageField(upload_to='UserImage/')

    def __str__(self):
        return self.phone


class Blog(models.Model):
    heading = models.CharField(max_length=30)
    content = models.TextField()
    tag = models.CharField(max_length=20)
    image = models.ImageField(upload_to='Blog/')
    user = models.ForeignKey(
        UserDetails,
        on_delete=models.CASCADE,
        related_name="post_owner",
        blank=True,
        null=True
        )

    def __str__(self):
        return self.heading
    

class Feedback(models.Model):
    message = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    status = models.BooleanField(default=True)



# Many To Many
# class Course(models.Model):
#     name = models.TextField()
#     year = models.IntegerField()
    
#     def __str__(self):
#         return self.name
    

# class Person(models.Model):
#     last_name = models.TextField()
#     first_name = models.TextField()
#     courses = models.ManyToManyField("Course")

#     def __str(self):
#         return self.first_name

# One To One
# class UserDetails(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     phone = models.CharField(max_length=10, blank=True, null=True)
#     pan_no = models.CharField(max_length=15, unique=True)
    
#     def __str__(self):
#         return self.phone
    
#     class Meta:
#         db_table = "UserDetails"
#         ordering = ['phone']


# ForeignKey
# class Batch(models.Model):
#     batch_id = models.CharField(max_length=10)
#     batch_name = models.CharField(max_length=50)
    

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     batch = models.ForeignKey(
#             Batch,
#             on_delete=models.CASCADE,
#             related_name="batch_allocating",
#             blank=True,
#             null=True
#         )


# class Emp(models.Model):
#     # id = auto()
#     fn = models.CharField(max_length=10)
#     ln = models.CharField(max_length=10)
#     salary = models.FloatField()

#     def __str__(self):
#         return self.fn


# class Stu(models.Model):
#     # id = auto()
#     fn = models.CharField(max_length=10)
#     ln = models.CharField(max_length=10)
#     email = models.EmailField()
#     course = models.CharField(max_length=20)

#     def __str__(self):
#         return self.email
    
