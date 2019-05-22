from django.db import models
from django.cors.validators import MaxValueValidator, MinValueValidator

class Data(models.Model):
    GENDER_CHOICES = [ ( 'male','male'), ('female', 'female'), ('other', 'other')]
    RESIDENCE_TYPE_CHOICES = [ ('rented', 'rented') , ( 'alloted','alloted') ,('owned','owned') ,( 'parental','parental')]
    DURATION_CHOICES = [ ('1','january'),('2','february') ,('3','march') ,('4', 'april') ,('5','may') ,('6','june') ,('7','july') ,('8','august') ,( '9', 'september') ,( '10', 'october') ,('11', 'november') , ( '12','december') ] 
    EMPLOYMENT_TYPE = ['Salaried','Salaried', 'SEP', 'Self Employed Professional', 'SENP', 'self employed non professional']


    full_name = models.CharField()
    pincode = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField()
    dob = models.DateField()
    pancard = models.CharField()
    adhaar = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES)
    residence_type = models.CharField(choices=RESIDENCE_TYPE_CHOICES)
    #living_duration_start = models.IntegerField(choices=DURATION_CHOICS)
    living_duration = models.IntegerField(validators=[MivValueValidator(0), MaxValueValidator(12)])
    #living_duration_end = models.IntegerField(choices=DURATION_CHOICES)
    address = models.CharField()
    street_landmark = models.CharField()
    salary = models.DecimalField(max_digits=15, max_places=4)
    employment_type = models.CharField(choices=EMPLOYMENT_TYPE)
    company_name = models.CharField()
    #current_job_duration_start = models.IntegerField(choices= DURATION_CHOICES)
    current_job_duration = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(12)])
    #current_job_duration_end = models.IntegerField(choices= DURATION_CHOICES)
    job_stability = models.IntegerField()
    loan_amount = models.DecimalField(max_digits=15, max_places=4)
    surgery = models.CharField()
    hospital = models.CharField()
    hospital_location = models.CharField()
    loan_rate = models.DoubleField(max_digits=15, max_places=4)
    loan_tenure = models.IntegerField()
    lead_id = models.AutoField(primary_key=True)
    patient_documents = 
    document_type = 
    account_id = models.CharField()

class FileData(models.Model):
    PATIENT_DOCUMENT_CHOICES = [
            ('bank_statement', )
            ]

    file_id = models.AutoField(primary_key=True)
    data = models.ForeignKey(Data)
    file = models.FileField()
    patient_document = models.CharField()

