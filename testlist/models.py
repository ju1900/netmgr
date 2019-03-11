from django.db import models
from django.contrib.auth.models import User 

class Product(models.Model):
    name = models.CharField(max_length=10)

class Chapter(models.Model):
    sequence = models.SmallIntegerField()
    name = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

class Section(models.Model):
    sequence = models.SmallIntegerField() 
    name = models.CharField(max_length=20) 
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True)

class Testplan(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    engineer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Testase(models.Model):
    # priority
    HIGH   = 'H'
    MIDDLE = 'M'
    LOW    = 'L'

    # result
    PASSED     = 'P'
    FAILED     = 'F'
    UNTESTED   = 'U'
    BLOCK_BUG  = 'BB'
    BLOCK_TOOL = 'BT'

    PRIORITY_CHOICES = (
        (HIGH,   'High'), 
        (MIDDLE, 'Middle'), 
        (LOW,    'Low'),
    )

    RESULT_CHOICES = (
        (PASSED,     'Passed'), 
        (FAILED,     'Failed'), 
        (UNTESTED,   'Untested'), 
        (BLOCK_BUG,  'Blocked_by_bug'), 
        (BLOCK_TOOL, 'Blocked_ty_tool'),
    )

    sequence = models.SmallIntegerField()
    title = models.CharField(max_length=300)
    support = models.BooleanField(default=True)
    engineer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    priority = models.CharField(
        max_length=2, 
        choices=PRIORITY_CHOICES, 
        default=MIDDLE, 
    ) 
    result = models.CharField(
        max_length=2, 
        choices=RESULT_CHOICES, 
        default=UNTESTED, 
    )
    version = models.CharField(max_length=50)
    comment = models.TextField() 
    time = models.DateTimeField(auto_now=True)
    testplan = models.ForeignKey(Testplan, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)

class Bug(models.Model):
    # status
    NEW        = 'N'
    VERI_FIXED = 'F' 
    RESO_INVAL = 'I'
    RESO_WONT  = 'W' 

    # priority
    P1 = 'P1'
    P2 = 'P2'
    P3 = 'P3'
    P4 = 'P4'
    P5 = 'P5'

    # severity
    CRITICAL    = 'C'
    MAJOR       = 'M'
    NORMAL      = 'N' 
    ENHANCEMENT = 'E'

    PRIORITY_CHOICES = (
        (P1, 'P1'), 
        (P2, 'P2'), 
        (P3, 'P3'), 
        (P4, 'P4'), 
        (P5, 'P5')
    )

    STATUS_CHOICES = (
        (NEW,        'New'), 
        (VERI_FIXED, 'Verfied_fixed'), 
        (RESO_INVAL, 'Resolved_invalid'), 
        (RESO_WONT,  'Resolved_wontfix'),
    )

    SEVERITY_CHOICES = (
        (CRITICAL,    'Critical'), 
        (MAJOR,       'Major'), 
        (NORMAL,      'Normal'), 
        (ENHANCEMENT, 'Enhancement'), 
    )

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    sequence = models.IntegerField()
    desc = models.CharField(max_length=300)
    status = models.CharField(
        max_length=30, 
        choices=STATUS_CHOICES, 
        default=NEW, 
    )
    priority = models.CharField(
        max_length=2, 
        choices=PRIORITY_CHOICES,
        default=P2, 
    )
    severity = models.CharField(
        max_length=15, 
        choices=SEVERITY_CHOICES, 
        default=MAJOR, 
    )
    open_v = models.CharField(max_length=50) 
    close_v = models.CharField(max_length=50)
    engineer = models.ForeignKey(User, models.SET_NULL, null=True)
    open_t = models.DateTimeField(auto_now_add=True)
    modified_t = models.DateTimeField(auto_now=True)
    testcase = models.ForeignKey(Testase, on_delete=models.SET_NULL, null=True)
