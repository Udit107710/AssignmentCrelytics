from django.db import models

class Data(models.Model):
    GENDER_CHOICES = [ ( 'male','male'), ('female', 'female'), ('other', 'other')]
    RESIDENCE_TYPE_CHOICES = [ ('rented', 'rented') , ( 'alloted','alloted') ,('owned','owned') ,( 'parental','parental')]
    EMPLOYMENT_TYPE = [ ('Salaried','Salaried'), ('SEP', 'Self Employed Professional'), ('SENP', 'self employed non professional')]


    full_name = models.CharField(max_length=40)
    pincode = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField()
    dob = models.DateField()
    pancard = models.CharField(max_length=40)
    adhaar = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    residence_type = models.CharField(choices=RESIDENCE_TYPE_CHOICES,max_length=10)
    #living_duration_start = models.IntegerField(choices=DURATION_CHOICS)
    living_duration = models.IntegerField()
    #living_duration_end = models.IntegerField(choices=DURATION_CHOICES)
    address = models.TextField(max_length=400)
    street_landmark = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=15, decimal_places=4)
    employment_type = models.CharField(choices=EMPLOYMENT_TYPE, max_length=10)
    company_name = models.CharField(max_length=100)
    #current_job_duration_start = models.IntegerField(choices= DURATION_CHOICES)
    current_job_duration = models.IntegerField()
    #current_job_duration_end = models.IntegerField(choices= DURATION_CHOICES)
    job_stability = models.IntegerField()
    loan_amount = models.DecimalField(max_digits=15, decimal_places=4)
    surgery = models.CharField(max_length=200)
    hospital = models.CharField(max_length=100)
    hospital_location = models.TextField(max_length=500)
    loan_rate = models.DecimalField(max_digits=15, decimal_places=4)
    loan_tenure = models.IntegerField()
    account_id = models.CharField(max_length=100)

    def __str__(self):
        return self.account_id

class FileData(models.Model):
    PATIENT_DOCUMENT_CHOICES = [
            ('bank_statement','bank_statement'),
            ('pancard','pancard'),
            ('photo','photo'),
            ('itr','itr'),
            ('salaary_slip','salary_slip'),
            ('adhaar','adhaar'),
            ('driving_licence','driving_licence'),
            ('passport','passport'),
            ('allotment_letter', 'allotment_letter'),
            ('rent_agreement','rent_agreement'),
            ('electricity_bill','electricity_bill'),
            ('mediccal_bill', 'medical_bill'),
            ('discharge_report','discharge_report'),
            ('voter_id','voter_id'),
            ('current_address_proof', 'current_address_proof'),
            ('gas_bill','gas_bill'),
            ('landline_bill','landline_bill'),
            ('property_papers', 'property_papers'),
            ('water_bill', 'water_bill'),
            ('house_tax', 'house_tax'),
            ('adhaarback', 'adhaarback'),
            ('others', 'others')
            ]

    file_id = models.AutoField(primary_key=True)
    data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to="files/")
    patient_document = models.CharField(choices=PATIENT_DOCUMENT_CHOICES,max_length=30)

    def __str__(self):
        return self.data.account_id

class Success(models.Model):
    lead_id = models.CharField(max_length=100)
    data = models.ForeignKey(Data, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.lead_id

