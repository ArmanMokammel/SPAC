from django.db import models

# Create your models here.
class Reg_Student(models.Model):
    ieee_id = models.CharField(blank=True,null=True,max_length=50)
    name = models.CharField(null=True,blank=True,max_length=100)
    email = models.EmailField(null=True,blank=True)
    university = models.CharField(null=True,blank=True,max_length=100)
    department = models.CharField(null=True,blank=True,max_length=100)
    university_id = models.CharField(null=True,blank=True,max_length=100)
    picture_link = models.URLField(null=True, blank=True,max_length=150)
    reference = models.CharField(null=True,blank=True,max_length=50)
    t_shirt_size = models.CharField(null=True,blank=True,max_length=10)
    transaction_id = models.CharField(null=True,blank=True,max_length=50)

    class Meta:
        verbose_name="Registered Student"

    def __str__(self) -> str:
        return str(self.pk)
    
class Reg_Student_Items(models.Model):
    student = models.ForeignKey(Reg_Student,null=False,blank=False,on_delete=models.CASCADE)
    t_shirt = models.BooleanField(null=False,blank=False,default=False)
    goodies = models.BooleanField(null=False,blank=False,default=False)
    certificate = models.BooleanField(null=False,blank=False,default=False)

    class Meta:
        verbose_name="Registered Student Item"

    def __str__(self) -> str:
        return str(self.pk)
    
class Meeting_Session(models.Model):
    session_name = models.CharField(null=False,blank=False,max_length=150)
    speaker_name = models.CharField(null=False,blank=False,max_length=150)

    class Meta:
        verbose_name="Meeting Session"

    def __str__(self) -> str:
        return str(self.pk)
    
class Meeting_Session_FeedBack_Link(models.Model):
    session = models.ForeignKey(Meeting_Session,null=False,blank=False,on_delete=models.CASCADE)
    graphic_link = models.URLField(null=True,blank=True, max_length=300)

    class Meta:
        verbose_name="Session Feedback Link"

    def __str__(self) -> str:
        return str(self.pk)
    
class Meeting_Session_Files(models.Model):
    session = models.ForeignKey(Meeting_Session,null=False,blank=False,on_delete=models.CASCADE)
    title = models.CharField(null=False,blank=False,max_length=100)
    file = models.FileField(upload_to='Meeting Session Files/',null=True,blank=True,default=None)

    class Meta:
        verbose_name="Session Files"

    def __str__(self) -> str:
        return str(self.pk)
    
class Reg_Student_Attendance(models.Model):
    student = models.ForeignKey(Reg_Student,null=False,blank=False,on_delete=models.CASCADE)
    session = models.ForeignKey(Meeting_Session,null=False,blank=False,on_delete=models.CASCADE)
    attendance = models.BooleanField(null=False,blank=False,default=False)

    class Meta:
        verbose_name="Registered Student Attendance"

    def __str__(self) -> str:
        return str(self.pk)