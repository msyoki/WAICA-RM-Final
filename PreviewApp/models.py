from django.db import models
from datetime import datetime
# from django.utils import timezone
# Create your models here.


CLASS_CHOICES = (
    ("Non-Paired", "Non-Paired"),
    ("Paired", "Paired"),
)


class PaymentAdvice(models.Model):
    ReceiptNumber = models.TextField(max_length=500, blank=True, null=True)
    BusinessTitle = models.TextField(max_length=500, blank=True, null=True)
    ResponsiblePartner = models.TextField(
        max_length=500, blank=True, null=True)
    BalanceClassofBusiness = models.TextField(
        max_length=500, blank=True, null=True)
    LevelofBusiness = models.TextField(max_length=500, blank=True, null=True)
    TypeofBusiness = models.TextField(max_length=500, blank=True, null=True)
    Currency = models.TextField(max_length=500, blank=True, null=True)
    Amount = models.TextField(max_length=500, blank=True, null=True)
    Claimid = models.CharField(max_length=500, blank=True, null=True)
    Claimname = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.ReceiptNumber}-{self.BusinessTitle} - {self.Amount}  "


class Technical(models.Model):
    ClassName = models.CharField(
        max_length=20,
        choices=CLASS_CHOICES,
        default='Non-Paired',
        blank=True,
        null=True)
    Category = models.CharField(max_length=500, blank=True, null=True)
    PaymentPartner = models.CharField(max_length=500, blank=True, null=True)
    BankID = models.CharField(max_length=500, blank=True, null=True)
    BankName = models.CharField(max_length=500, blank=True, null=True)
    BankAccountNo = models.CharField(max_length=500, blank=True, null=True)
    BankAccountCurrencyCode = models.CharField(
        max_length=500, blank=True, null=True)
    OriginalCurrencyCode = models.CharField(
        max_length=500, blank=True, null=True)
    BalanceOriginal = models.CharField(max_length=500, blank=True, null=True)
    BalanceOutstandingOriginal = models.CharField(
        max_length=500, blank=True, null=True)
    RemittanceDirection = models.CharField(
        max_length=500, blank=True, null=True)
    RemittanceStatus = models.CharField(max_length=500, blank=True, null=True)
    Company = models.CharField(max_length=500, blank=True, null=True)
    ReceiptNumber = models.CharField(max_length=500, blank=True)
    ReceiverEmail = models.CharField(max_length=1000, blank=True, null=True)
    MailSubject = models.CharField(max_length=200, blank=True, null=True)
    MailBody = models.TextField(blank=True, null=True)
    SendStatus = models.BooleanField(blank=True, null=True)
    ValueDate = models.DateField(default=datetime.now, blank=True, null=True)
    IssuedBy = models.CharField(max_length=500, blank=True, null=True)
    MailDate = models.DateField(default=datetime.now, blank=True, null=True)

        
    class Meta: 		
        ordering = ['-ReceiptNumber']

    def __str__(self):
        return f"{self.ReceiptNumber}-{self.PaymentPartner} - {self.ValueDate} "


class MappedTechnical(models.Model):
    ClassName = models.CharField(
        max_length=20,
        choices=CLASS_CHOICES,
        default='Paired',
        blank=True,
        null=True)
    Category = models.CharField(max_length=500, blank=True, null=True)
    Purpose = models.CharField(max_length=500, blank=True, null=True)
    Doclanguage = models.CharField(max_length=500, blank=True, null=True)
    WorkSheetId = models.CharField(max_length=500, blank=True, null=True)
    BusinessPartner = models.CharField(max_length=500, blank=True, null=True)
    ReceiptNumber = models.CharField(max_length=500, blank=True, null=True)
    Currency = models.CharField(max_length=500, blank=True, null=True)
    Amount = models.CharField(max_length=500, blank=True, null=True)
    BalanceUnsettledAmount = models.CharField(
        max_length=500, blank=True, null=True)
    PaymentType = models.CharField(max_length=500, blank=True, null=True)
    Office = models.CharField(max_length=500, blank=True, null=True)
    MailSubject = models.CharField(max_length=200, blank=True, null=True)
    MailBody = models.TextField(blank=True, null=True)
    ReceiverEmail = models.CharField(max_length=1000, blank=True, null=True)
    SendStatus = models.BooleanField(blank=True, null=True)
    IssuedBy = models.CharField(max_length=500, blank=True, null=True)
    ValueDate = models.DateTimeField(
        default=datetime.now, blank=True, null=True)
    MailDate = models.DateField(default=datetime.now, blank=True, null=True)

    
    class Meta: 		
        ordering = ['-ReceiptNumber']


    def __str__(self):
        return f"{self.ReceiptNumber}-{self.BusinessPartner} - {self.ValueDate} "


class CounterModel(models.Model):
    Counter = models.IntegerField()
    Company = models.CharField(max_length=500, blank=True, null=True)
    Counterdate = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.Country


class FrontEndReceipts(models.Model):
    ReceiptName = models.CharField(max_length=500, blank=True, null=True)
    HashedDate = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.ReceiptName


class MailTable(models.Model):
    ReceiptNumber = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.ReceiptNumber