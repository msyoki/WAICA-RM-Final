from django.urls import path
from .views import receiptupdatepage, pdf_view, home, SearchReceipt, PreviewReceipt, advancedsearch, technicalmailupdate, mappedtechnicalmailupdate, paymentadviseupdatepage, updatepaymentadvise, updateremmittance_allocation, updatenonpaired_receipt, remittanceallocationupdatepage, latest_receipts, latest_payment_advices, latest_remittance_allocations


app_name = 'PreviewApp'

urlpatterns = [
    path(
        '',
        home,
        name="home"),
    path(
        'latest/receipts',
        latest_receipts,
        name="latest_receipts"),
    path(
        'latest/remittance_allocation',
        latest_remittance_allocations,
        name="latest_ra"),
    path(
        'latest/payment_advices',
        latest_payment_advices,
        name="latest_pa"),
    path(
        'preview/<slug:foo>',
        PreviewReceipt,
        name="preview"),
    path(
        'pdf_view/<slug:foo>',
        pdf_view,
        name="pdf_view"),
    path(
        'search',
        SearchReceipt,
        name='searchreceipt'),
    path(
        'advanced-search',
        advancedsearch,
        name='advancedsearchreceipt'),
    path(
        'technicalmail/<int:pk>',
        technicalmailupdate,
        name='technicalmail'),
    path(
        'PA/edit/<slug:foo>',
        paymentadviseupdatepage,
        name='paymentadviseupdatepage'),
    path(
        'RA/edit/<slug:foo>',
        remittanceallocationupdatepage,
        name='remittanceallocationupdatepage'),
    path(
        'Receipt/edit/<slug:foo>',
        receiptupdatepage,
        name='receiptupdatepage'),
    path(
        'paymentadvise/<slug:foo>',
        updatepaymentadvise,
        name='paymentadviseupdate'),
    path(
        'remmitance_allocation/<slug:foo>',
        updateremmittance_allocation,
        name='remmitanceallocationupdate'),
    path(
        'receiptupdate/<slug:foo>',
        updatenonpaired_receipt,
        name='receiptupdate'),
    path(
        'mappedtechnicalmail/<int:pk>',
        mappedtechnicalmailupdate,
        name='mappedtechnicalmail'),
]