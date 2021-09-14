
from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = " login to Student Peeps"
admin.site.site_title = "Dashboard"
admin.site.index_title = "Welcome to Student Peeps Dashboard"

urlpatterns = [
    path('',views.home,name="Home"),
    path('about/',views.about,name="About"),
    path('verification-message/',views.verificationmsg,name="Verificationmsg"),
    path('upload-message/',views.uploadmsg,name="Uploadmsg"),
    path('contactus/',views.contactus,name="ContactUs"),
    path('faq/',views.faq,name="Faq"),
    path('privacypolicy/',views.privacy,name="PrivacyPolicy"),
    path('request-your-fav-brand/',views.Favroiute,name="Favroiute"),
    path('course-application/',views.Course,name="Course"),
    path('resource/',views.Tools,name="Resource"),

    path('whole-truth-food/',views.wtf,name='Wtf'),
    path('student-discount-whole-truth-food/',views.codewtf,name='CodeWtf'),

    path('avni-by-giva/',views.avni,name='Avni'),
    path('student-discount-avni/',views.codeavni,name='CodeAvni'),

    path('naagin/',views.naagin,name='Naagin'),
    path('student-discount-naagin/',views.codenaagin,name='CodeNaagin'),

    path('pee-safe/',views.peesafe,name='PEESAFE'),
    path('student-discount-pee-safe/',views.codepeesafe,name='CodePEESAFE'),

    path('propshop/',views.propshop,name='Propshop'),
    path('student-discount-propshop/',views.codepropshop,name='CodePropshop'),

    path('trib/',views.trib,name='TRIB'),
    path('student-discount-trib/',views.codetrib,name='CodeTRIB'),

    path('to-be-honest/',views.tbh,name='TBH'),
    path('student-discount-to-be-honest/',views.codetbh,name='CodeTBH'),

    path('unlu-class/',views.unlu,name='Unlu'),
    path('student-discount-unlu-class/',views.codeunlu,name='CodeUnlu'),

    path('unlu-shoutout/',views.unlu2,name='Unlu2'),
    path('student-discount-unlu-shoutout/',views.codeunlu2,name='CodeUnlu2'),

    path('yes-done/',views.yesdone,name='YesDone'),
    path('student-discount-yes-done/',views.codeyesdone,name='CodeYesDone'),

    path('skoosh/',views.skoosh,name='skoosh'),
    path('student-discount-skoosh/',views.codeskoosh,name='Codeskoosh'),

    path('bitclass/',views.bitclass,name='bitclass'),
    path('student-discount-bitclass/',views.codebitclass,name='Codebitclass'),
    
    path('chaaryaar/',views.chaaryaar,name='Chaaryaar'),
    path('student-discount-chaaryaar/',views.codechaaryaar,name='Codechaaryaar'),
    
    path('mypaperclip/',views.mypaperclip,name='MyPaperClip'),
    path('student-discount-mypaperclip/',views.codemypaperclip,name='CodeMyPaperClip'),
    
    path('mittihub/',views.mittihub,name='Mittihub'),
    path('student-discount-mittihub/',views.codemittihub,name='CodeMittihub'),
    
    path('sattviko/',views.sattviko,name='Sattviko'),
    path('student-discount-sattviko/',views.codesattviko,name='CodeSattviko'),
    
    path('rapido/',views.rapido,name='Rapido'),
    path('student-discount-rapido/',views.coderapido,name='StudentDiscountRapido'),
    
    path('the-womans-company/',views.TWC,name='TWC'),
    path('student-discount-the-womans-company/',views.codeTWC,name='StudentDiscountTWC'),
    
    path('ptal/',views.ptal,name='Ptal'),
    path('student-discount-ptal/',views.codeptal,name='StudentDiscountPtal'),
    
    path('bookchor/',views.bookchor,name='Bookchor'),
    path('student-discount-bookchor/',views.codebookchor,name='StudentDiscountBookchor'),
    
]
