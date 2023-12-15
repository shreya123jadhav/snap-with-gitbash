from django.db import models

# Create your models here.

class Admin(models.Model):
    adminemailid = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=10, blank=True, null=True)
    phoneno = models.CharField(max_length=10, blank=True, null=True)
    Objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'admin'


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    emailid = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    Objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'user'


class Event(models.Model):
    eventname = models.CharField(primary_key=True, max_length=50)
    adminemailid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminemailid', max_length=50)
    artist = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    ticket_avail = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    photo1 = models.CharField(max_length=50, blank=True, null=True)
    photo2 = models.CharField(max_length=50, blank=True, null=True)
    photo3 = models.CharField(max_length=50, blank=True, null=True)
    likecount = models.CharField(max_length=50, blank=True, null=True)
    Objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'event'


class Ticket(models.Model):
    ticketid = models.CharField(primary_key=True, max_length=50)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userid', blank=True, null=True)
    eventname = models.ForeignKey(Event, models.DO_NOTHING, db_column='eventname', blank=True, null=True)
    transactionid = models.CharField(max_length=20, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    Objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'ticket'

class User_Event_Organiser(models.Model):
    eventname = models.CharField(primary_key=True, max_length=50)
    adminemailid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminemailid', max_length=50)
    artist = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    ticket_avail = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='pics')
    likecount = models.CharField(max_length=50, blank=True, null=True)
    Objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'usereventorganiser'