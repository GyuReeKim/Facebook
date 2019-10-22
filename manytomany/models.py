from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    # through는 Patient클래스와 Doctor클래스를 연결해주는 클래스를 적어준다.
    # related_name은 Doctor클래스에서도 patients라는 변수를 통해 접근할 수 있도록 한다.
    doctors = models.ManyToManyField(Doctor, related_name="patients") # through='Reservation'
    def __str__(self):
        return self.name

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE) # Not Null = True 값도 줄 수 있다. 빈 칸 허용한다.
#     time = models.CharField(max_length=100)
#     location = models.CharField(max_length=100, default="3층") # default 값 추가
#     def __str__(self):
#         return f"{self.doctor.name}의사 : {self.patient.name}환자"