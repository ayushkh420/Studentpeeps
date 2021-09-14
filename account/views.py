from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.template import Context
from django.contrib.auth.models import User
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator


# Create your views here.
def register(request):
    if request.method=='POST':
        Email = request.POST['email']
        Password = request.POST['password']
        if Registers.objects.filter(username=Email).exists() or User.objects.filter(username=Email).exists():
            messages.error(request, "Looks like you're already a Peep, click on Log in below and enjoy life🙃")
            return redirect('register')
        elif Registers.objects.filter(email=Email).exists() or User.objects.filter(email=Email).exists():
            messages.error(request, 'Email is already Taken')
            return redirect('register')
        else:
            signup = Signup(email=Email, password=Password)
            signup.save()
            request.session['email'] = Email
            request.session['password'] = Password
            return redirect('yourdetail')
    return render(request, 'signup.html')

def yourdetail(request):
    if request.method=='POST':
        FirstName= request.POST['fname']
        LastName = request.POST['lname']
        Gender = request.POST['Gender']
        Date = request.POST['date']
        Month = request.POST['month']
        Year = request.POST['year']

        yourdetail = Yourdetail(firstname=FirstName,lastname=LastName,gender=Gender,date=Date,month=Month,year=Year)
        yourdetail.save()

        request.session['fname'] = FirstName
        request.session['lname'] = LastName
        request.session['gender'] = Gender
        request.session['date'] = Date
        request.session['month'] = Month
        request.session['year'] = Year
        value = {
            'FirstName' : FirstName,
            'LastName' : LastName,
            'Date' : Date,
            'Month' : Month,
            'Year' : Year,
        }
        
        return redirect('signup')
        data = {
                'values' : value
            }
        return render(request, 'signup2.html', data)
    return render(request, 'signup2.html')

    return render(request, 'signup2.html')

def signup(request):
    Institution = {
    	'Aayojan- School of Architecture (All campus)':['ayojan.edu.in','aayojan.edu.in'],
	    'Abeda Inamdar Senior College (AISC)':['azamcampus.org','abedainamdarcollege.org.in'],
		'Academy of Maritime Education and Training (AMET)': ['ametuniv.ac.in', ],
		'Accman Institute of Management':['accmanbusinessschool.in','accmanbusinessschool.edu','accmanbusinessschool.ac.in'],
		'Accurate Institute of Management and Technology (AIMT)':['accurate.in','accurate.edu','accurate.ac.in'],
    	'Adamas University':'stu.adamasuniversity.ac.in',
    	'AIHM Chandigarh':'ihmchandigarh.org',
	    'Aissms Institute of Management (AISSMS)': 'aissmsiom.org',
    	'Aligarh Muslim University':['amu.ac.in','myamu.ac.in'],
	    'All India Shri Shivaji Memorial Society (AISSMS) College of Hotel Management & Catering Technology': 'aissmschmct.in',
    	'Alliance University':['alliance.edu.in','bus.alliance.edu.in','ced.alliance.edu.in','law.alliance.edu.in'],
    	'Amity University':['amity.edu','amitystudent.com','amityopenuniversity.com','amityonline.com'],
    	'Amity University Chhattisgarh':['rpr.amity.edu','s.amity.edu'],
    	'Amity University Gwalior (Madhya Pradesh)':'gwa.amity.edu',
    	'Amity University Mumbai':'mum.amity.edu',
    	'Amity university, Noida':'s.amity.edu',
    	'Anna University, Chennai':'annauniv.edu',
		'Apeejay Institute of Technology, School Of Architecture & Planning (AIT SAP)':'apeejay.edu',
	    'Armed Forces Medical College ( AFMC)': ['afmcnic.in','afmc.nic.in'],
		'Army Institute Of Management & Technology (AIMT)':['aimt.ac.in','aimt.edu','aimt.edu.in'],
	    'Army Institute of Technology (AIT)': ['aitpune.edu.in','aitpune.in'],
    	'Aryabhatta College, University Of Delhi':'aryabhattacollege.ac.in',
    	'Ashoka University':'ashoka.edu.in',
		'Asian Academy Of Film And Television (AAFT)':['aaft.com','aaft.edu.in','aaft.ac.in'],
		'Asian College Of Journalism (ACJ)':['asianmedia.org.in','asianmedia.edu','asianmedia.ac.in','asianmedia.edu.in'],
	    'ASMs College of Commerce, Science & Information Technology': ['asmedu.org','csit.edu.in'],
	    'ASMs Institute of Business Management and Research (IBMR)': ['ibmrpune.in','asmibmr.edu.in'],
		'B.S. Abdur Rahman Crescent Institute Of Science & Technology (BSAU)':['crescent.education','crescent.education.edu','crescent.education.ac.in'],
	    'Balaji Institute of International Business - (BIIB)':['sribalajisocietypune.org','biibpune.com','balajisociety.org'],
	    'Balaji Institute of Management and Human Resource Development (BIMHRD)':['sribalajisocietypune.org','bimhrdpune.com','bimhrdpune.edu.in'],
	    'Balaji Institute of Modern Management (BIMM)':['balajisociety.org','bimmpune.edu.in'],
	    'Balaji Institute of Telecom and Management (BITM)':['sribalajisocietypune.org','bitmpune.com'],
    	'Banasthali Vidyapith':'banasthali.in',
    	'Bangalore University':['bangaloreuniversity.ac.in','bub.ernet.in'],
		'BBS Institute Of Pharmaceutical And Allied Sciences - (BBSIPAS)':['bbsipas.ac.in','bbsip.edu'],
    	'Bennett university':'bennett.edu.in',
		'Bharath Institute Of Higher Education And Research (BIHER)':['bharathuniv.ac.in','bharathuniv.edu'],
	    'Bharati ViDYapeeth Deemed University, Medical College School of Optometry':'bharatividyapeeth.edu',
	    'Bharati ViDYapeeth Dental College and Hospital (BVDCH)':'bharatividyapeeth.edu',
	    'Bharati ViDYapeeth New Law College (NLC)':['bharatividyapeeth.edu','bvpnlcpune.org'],
	    'Bharati ViDYapeeth University, Pune':['bharatividyapeeth.edu','bvcoa.in','bvuniversity.edu.in'],
	    'Bharatiya Jain Sanghatana Arts, Science and Commerce College - (BJS)':'bjs.edu.in',
	    'Bharatiya Kala Prasarini Sabha College of Architecture (BKPS)':'bkps.edu',
    	'Bhartiya Vidyapeeth College of Engineering , Pune':'deccansociety.org',
		'Birla Institute of Management Technology (BIMTECH)':['bimtech.ac.in','bimtech.edu'],
    	'Birla Institute of Technology - Mesra':['student.biticrak.ae','bitmesra.ac.in'],    	
    	'Birla Institute of Technology and Science (BITS)':['bits-pilani.ac.in','dubai.bits-pilani.ac.in','goa.bits-pilani.ac.in','hyderabad.bits-pilani.ac.in','pilani.bits-pilani.ac.in','wilp.bits-pilani.ac.in','bits.pilani.wilp.ac.in','bitspilaniwilp.ac.in'],
    	'BITS Pilani, Goa Campus':'bits-goa.ac.in',
    	'Biyani College':'biyanicolleges.org',
    	'BMS College of Engineering':['bmsce.edu.in','bmsce.ac.in'],
    	'BMS college of Law':['bmscl.edu.in','bmscl.ac.in'],
    	'BMS Institute of Technology and Management':['bmsit.edu.in','bmsit.in','bmsit.ac.in'],
    	'BMS School of Architecture':['bmssa.edu.in','bmsca.org','bmssa.ac.in'],
    	'BMSCCM - BMS College of Commerce and Management':['bmsccm.edu.in','bmsccm.ac.in','bmsccm.in'],
	    'Brihan Maharashtra College of Commerce (BMCC)': ['despune.org','bmcc.ac.in'],
	    'Byramjee Jeejeebhoy Government Medical College':['bjmcpune.org','bjmcpune.edu'],
    	'Calcutta University, Kolkata':'caluniv.ac.in',
    	'Chandigarh university':'cumail.in',
		'Chennai Business School (CBS)':['cbs.org.in','cbs.edu','cbs.ac.in'],
		'Chennai Institute of Technology (CIT)':['citchennai.net','citchennai.edu','citchennai.ac.in','citchennai.edu.in'],
    	'Chitkara University':'chitkara.edu.in',
	    'Christ College':['christcollegepune.org','cccug.org'],
    	'Christ University, Bangalore':['soc.christuniversity.in','science.christuniversity.in','psy.christuniversity.in','pme.christuniversity.in','phl.christuniversity.in','mtech.christuniversity.in','mcom.christuniversity.in','mca.christuniversity.in','mba.christuniversity.in','maths.christuniversity.in','law.christuniversity.in','it.christuniversity.in','eng.christuniversity.in','cse.christuniversity.in','cs.christuniversity.in','commerce.christuniversity.in','christuniversity.in','btech.christuniversity.in','bba.christuniversity.in','barch.christuniversity.in','arts.christuniversity.in',],
    	'Christ University, Ghaziabad':['soc.christuniversity.in','science.christuniversity.in','psy.christuniversity.in','pme.christuniversity.in','phl.christuniversity.in','mtech.christuniversity.in','mcom.christuniversity.in','mca.christuniversity.in','mba.christuniversity.in','maths.christuniversity.in','law.christuniversity.in','it.christuniversity.in','eng.christuniversity.in','cse.christuniversity.in','cs.christuniversity.in','commerce.christuniversity.in','christuniversity.in','btech.christuniversity.in','bba.christuniversity.in','barch.christuniversity.in','arts.christuniversity.in',],
    	'Christ University, Lavasa ':['soc.christuniversity.in','science.christuniversity.in','psy.christuniversity.in','pme.christuniversity.in','phl.christuniversity.in','mtech.christuniversity.in','mcom.christuniversity.in','mca.christuniversity.in','mba.christuniversity.in','maths.christuniversity.in','law.christuniversity.in','it.christuniversity.in','eng.christuniversity.in','cse.christuniversity.in','cs.christuniversity.in','commerce.christuniversity.in','christuniversity.in','btech.christuniversity.in','bba.christuniversity.in','barch.christuniversity.in','arts.christuniversity.in',],
		'Cl Baid Metha College Of Pharmacy':['clbaidmethacollege.com','clbaidmethacollege.edu','clbaidmethacollege.ac.in'],
	    'College of Agricultural Biotechnology':['pravara.in','agribiotechpravara.in','themgmgroup.com'],
	    'College of Agriculture':'',
	    'College of Computer Sciences':'ccspune.in',
	    'College of Engineering (COEP)': ['coep.ac.in','coep.org.in','coep.edu.in'],
		'College Of Engineering, Guindy (CEG)':['annauniv.edu','annauniv.ac.in'],
    	'College of Vocational Studies, University of Delhi':'cvs.edu.in',
		'CSI Bishop Newbigin College Of Education':['bishopnewbigin.edu.in','bishopnewbigin.ac.in'],
	    'D.E.S Shri. Navalmal Firodia Law College (DES SNFLC)':['despune.org','deslaw.edu.in'],
    	'Daulat Ram College':'dr.du.ac.in',
	    'Defense Institute of Advanced Technology':'diat.ac.in',
		'Delhi Technical Campus (DTC)':['delhitechnicalcampus.ac.in','delhitechnicalcampus.edu'],
    	'Delhi Technological University':['cumsdtu.in','dtu.co.in','dtu.ac.in','dce.edu'],
	    'Department of Management Sciences, Pune University (PUMBA)':'pumba.in',
    	'Deshbandu College':['deshbandhucollege.ac.in','du.ac.in'],
    	'DKTE Societys Textile & Engineering Institute':['dktes.com','dkte.in','dkte.ac.in'],
		'DMI College Of Engineering':['dmice.ac.in','dmice.edu',],
    	'Dr Akhilesh Das Gupta Institute of Technology & Management':'adgitmdelhi.ac.in',
	    'Dr DY Patil College of Pharmacy Akurdi':['dyppharmaakurdi.ac.in','dypakurdi.onmicrosoft.com','dyptc.edu.in'],
	    'Dr DY Patil Dental College & Hospital (DYPDCH)':'dpu.edu.in',
	    'Dr DY Patil Institute of Management & Research (DYPIMR) Pimpri':['dypvp.edu.in','imrdypvp.edu.in'],
		'Dr. A.P.J. Abdul Kalam Technical University':['aktu.ac.in','aktu.edu'],
	    'Dr. DY Patil Arts, Science and Commerce College Pimpri':['dypvp.edu.in','acsdypvp.edu.in'],
	    'Dr. DY Patil Institute of Engineering, Management and Research (DYPIEMR)':['dypagribusiness.ac.in','dypiemr.ac.in'],
	    'Dr. DY Patil Institute of Management Studies (DYPIMS)':'dypims.com',
	    'Dr. DY Patil ViDYapeeth':['dpu.edu.in','dypatil.edu'],
	    'Dr. DY Patil Institute of Hotel Management & Catering Technology (DYPIHMCT)':['dypvp.edu.in','hmct.dypvp.edu.in'],
		'Dr. M.G.R. Educational And Research Institute':['drmgrdu.ac.in','drmgrdu.edu'],
		'Dronacharya Group of Institutions (DGI)':['gnindia.dronacharya.info','dronacharya.info''dronacharya.info.edu','dronacharya.info.ac.in'],
		'Dwaraka Doss Goverdhan Doss Vaishnav College (DDGDVC)':'dgvaishnavcollege.edu.in',
	    'DY Patil Medical College':'dpu.edu.in',
		'Easwari Engineering College (EEC)':['eec.srmrmp.edu.in','eec.srmrmp.ac.in','eec.srmrmp.ac.in'],
	    'Ecole Hoteliere Lavasa':['ecolehotelierelavasa.com','ecolelavasa.com'],
		'Ethiraj College For Women':['ethirajcollege.edu.in','ethirajcollege.ac.in'],
    	'Faculty of Management, Delhi (FMS)':'fms.edu',
	    'Fergusson College':'fergusson.edu',
    	'Flame University':'flame.edu.in',
		'Galgotias College of Engineering & Technology (GCET)':['galgotiacollege.edu','galgotiacollege.ac.in','galgotiasuniversity.edu.in'],
    	'Galgotias University':'galgotiasuniversity.edu.in',
    	'Gandhi Institute of Technology and Management University (GITAM)':['gitam.in','gitam.edu'],
    	'Gargi College (University of Delhi)':['gargi.du.ac.in','gargicollege.in'],
		'Gautam Buddha University':['gbu.ac.in','gbu.edu'],
    	'GD Goenka University Gurgaon':['gdgu.org','gdgoenka.ac.in'],
		'GL Bajaj Institute of Technology and Management':['glbitm.ac.in','glbitm.org','glbitm.edu.in'],
		'GNIOT Group of Institutions':['gniot.net.in','gniot.edu','gniot.ac.in'],
		'GNIOT Institute of Management Studies (GIMS)':['gims.net.in','gims.edu','gims.ac.in'],
	    'Gramonnati Mandals Arts, Commerce & Science College - (ACSC) Narayangaon':'collegeacs.org',
		'Great Lakes Institute Of Management':['greatlakes.edu.in','greatlakes.ac.in'],
		'Greater Noida Institute Of Business Management (GNIBM)':['gnibm.in','gnibm.edu','gnibm.ac.in','gnibm.edu.in'],
		'Greater Noida Institute Of Technology - IPU ( GNIT IPU)':['gnitipu.in','gnitipu.edu'],
		'Greater Noida Institute of Technology (GNIT)':['GNIOT.NET.IN','gniot.edu','gniot.ac.in'],
		'Greater Noida Institute of Technology MBA Institute':['gniot.net.in','gniot.net.in','gniot.ac.in'],
    	'Guru Gobind Singh Indraprastha University':'ipu.ac.in',
		'Guru Nanak College':['gurunanakcollege.edu.in','gurunanakcollege.ac.in'],
    	'Guru Nanak Dev University, Amritsar. (GNDU)':'gndu.ac.in',
    	'Hansraj College':['hansrajcollege.du.ac.in','hansrajcollege.ac.in','hrc.du.ac.in'],
		'Harlal Institute of Management and Technology (HIMT)':['himt.ac.in','himt.edu'],
    	'Hindu College, Delhi University':['hinducollege.co.in','hinducollege.ac.in'],
		'HINDUSTAN Institute Of Technology And Science (HITS)':['hindustanuniv.ac.in','student.hindustanuniv.ac.in'],
    	'Hindustan University':'hindustanuniv.ac.in',
    	'HR College of Economics':'hrcollege.edu',
		'I Business Institute (IBI)':['ibusinessinstitute.org','ibusinessinstitute.edu','ibusinessinstitute.ac.in'],
    	'ICT College of Vocational Studies':'ict.edu.rs', 
		'IEC Group of Institutions':['iec.edu.in','ieccollege.com','iec.ac.in'],
	    'Iiebm Indus Business School':'iiebm.com',
    	'IIIT - Indian Institute of Information Technology, Kota':'iiitkota.ac.in',
		'IIIT Sonipat':'iiitsonepat.ac.in',
		'IIKM Business School':['iikm.in','iikm.ac.in','iikm.edu','iikm.edu.in'],
		'IILM Academy of Higher Learning':['iilm.edu','iilm.ac.in'],
		'IILM College of Engineering and Technology (IILM CET)':['iilmcet.ac.in','iilmcet.edu'],
		'IILM Graduate School of Management (IILM GSM)':['iilm.edu','iilmgsm.ac.in'],
    	'IIM Ahmedabad':'iima.ac.in',
    	'IIM Amritsar':'iimamritsar.ac.in',
    	'IIM Bangalore':'iimb.ac.in',
    	'IIM Bodh Gaya':'iimbg.ac.in',
    	'IIM Calcutta':['iimcal.ac.in','email.iimcal.ac.in'],
    	'IIM Indore':'iimidr.ac.in',
    	'IIM Kozhikode':['iimk.ac.in','iimk.edu.in'],
    	'IIM Lucknow':'iiml.ac.in',
    	'IIM Ranchi':'iimranchi.ac.in',
    	'IIM Rohtak':'iimrohtak.ac.in',
    	'IIM Sambalpur':'iimsambalpur.ac.in',
    	'IIM Shillong':'iimshillong.ac.in',
    	'IIM Sirmaur':'iimsirmaur.ac.in',
    	'IIM Udaipur':'iimu.ac.in',
		'IIMT College of Engineering':['iimtindia.net','iimtindia.edu','iimtindia.ac.in'],
		'IIMT College of Management':['iimtindia.net','iimtindia.edu','iimtindia.ac.in'],
		'IIMT Group of Colleges':['iimtindia.net','iimtindia.ac.in','iimtindia.edu'],
    	'IIS University, Jaipur ':'iisuniv.ac.in',
    	'IIT (ISM) Dhanbad':['agl.ism.ac.in','agp.iitism.ac.in','agp.ism.ac.in','am.iitism.ac.in','am.ism.ac.in','ap.iitism.ac.in','ap.ism.ac.in','ce.iitism.ac.in','ce.ism.ac.in','cse.iitism.ac.in','cse.ism.ac.in','cve.iitism.ac.in','cve.ism.ac.in','ece.iitism.ac.in','ece.ism.ac.in','ee.iitism.ac.in','ee.ism.ac.in','ese.iitism.ac.in','fme.iitism.ac.in','fme.ism.ac.in','ismu.ac.in','mc.iitism.ac.in','me.iitism.ac.in','me.ism.ac.in','mech.iitism.ac.in','mech.ism.ac.in','mme.iitism.ac.in','mme.ism.ac.in','pe.iitism.ac.in','pe.ism.ac.in'],
    	'IIT Bhilai':'iitbhilai.ac.in',
    	'IIT Bhubaneswar':'iitbbs.ac.in',
    	'IIT Bombay':['aero.iitb.ac.in','cse.iitb.ac.in','iitbombay.org','sjmsom.in','ee.iitb.ac.in','chem.iitb.ac.in','iitb.ac.in'],
    	'IIT Delhi':['student.iitd.ac.in','physics.iitd.ac.in','mech.iitd.ac.in','maths.iitd.ernet.in','maths.iitd.ac.in','iitd.ac.in','dms.iitd.ernet.in','ee.iitd.ac.in','dbeb.iitd.ac.in','cse.iitd.ernet.in','cse.iitd.ac.in','chemical.iitd.ac.in','care.iitd.ernet.in','am.iitd.ac.in','textile.iitd.ac.in'],
    	'IIT Dharwad':'iitdh.ac.in',
    	'IIT Gandinagar':'iitgn.ac.in',
    	'IIT Goa':'iitgoa.ac.in',
    	'IIT Guwahati':'iitg.ac.in',
    	'IIT Hyderabad':'ee.iith.ac.in',
    	'IIT Indore':'iitdh.ac.in',
    	'IIT Jammu':'iitjammu.ac.in',
    	'IIT Jodhpur':'iitj.ac.in',
    	'IIT Kanpur':'iitk.ac.in',
    	'IIT Kharagpur (IITK)':['sit.iitkgp.ernet.in','metal.iitkgp.ernet.in','mech.iitkgp.ernet.in','iitkgp.ac.in','gg.iitkgp.ernet.in','ee.iitkgp.ernet.in','cse.iitkgp.ernet.in','ece.iitkgp.ernet.in','cse.iitkgp.ac.in'],
    	'IIT Mandi (IITM)':'students.iitmandi.ac.in',
    	'IIT Palakkad':'smail.iitpkd.ac.in',
    	'IIT Patna':'iitp.ac.in',
    	'IIT Ropar':'iitrpr.ac.in',
    	'IIT Rorkee':'ar.iitr.ac.in',
    	'IIT Tirupati':'iittp.ac.in',
    	'IITM - Indian Institute of Technology Madras':['smail.iitm.ac.in','student.onlinedegree.iitm.ac.in','onlinedegree.iitm.ac.in','imail.iitm.ac.in','iitm.ac.in','htic.iitm.ac.in','ee.iitm.ac.in','cse.iitm.ac.in'],
		'Indian Institute of Finance (IIF)':'iif.edu',
    	'Indian Institute of Foreign Trade (IIFT)':'iift.edu',
		'Indian Institute Of Information Technology, Design,And Manufacturing (IIITDM Kancheepuram)':['iiitdm.ac.in','iiitdm.edu'],
		'Indian Institute Of Information Technology, Pune (IIIT-P)':['iiip.ac.in','ece.iiitp.ac.in','cse.iiitp.ac.in','alumni.iiitp.ac.in'],
    	'Indian Institute of Science, Bangalore':['ug.iisc.in','ssl.serc.iisc.in','serc.iisc.in','mecheng.iisc.ernet.in','mbu.iisc.ernet.in','math.iisc.ernet.in','iisc.ac.in','grads.cds.iisc.ac.in','ece.iisc.ernet.in','csa.iisc.ernet.in','ces.iisc.ernet.in'],
    	'Indian Institute of Technology Varanasi (BHU)':['itbhu.ac.in','tbhu.ac.in','iitbhu.ac.in','bhu.ac.in'],
	    'Indian Law Societys Law College': ['ilslaw.in','ilslaw.edu','ilslaw.edu.in'],
		'Indian Maritime University (IMU)':['imu.ac.in','imu.edu','imu.edu.in'],
    	'Indian School of Business (ISB)':['tep.isb.edu','pgppro.isb.edu','pgp.isb.edu','isb.edu','cba.isb.edu'],
    	'Indian Statistical Institute':['isical.ac.in','isibang.ac.in'],
	    'Indira Institute of Management, Pune':['indiraedu.com','indiraiimp.edu.in'],
    	'Indraprastha Institute of Information Technology, Delhi':'iiitd.ac.in',
		'Indus Business Academy (IBA)':['ibagreaternoida.org','ibagreaternoida.ac.in'],
		'Institute Of Advanced Study In Education':['asetamilnadu.ac.in','iasetamilnadu.ac.in','asetamilnadu.edu','iasetamilnadu.edu'],
	    'Institute of Management and Entrepreneurship Development (IMED)':['bharatividyapeeth.edu','imed.bharatividyapeeth.edu'],
    	'Institute of Management Studies Noida (IMS Noida)':'imsnoida.com',
    	'Integral University':'student.iul.ac.in',
    	'International Institute of Information Technology - IIIT Hyderabad':['students.iiit.ac.in','research.iiit.ac.in','iiit.ac.in'],
	    'International Institute of Management Studies (IIMS)':'iimspune.edu.in',
	    'International School of Business and Media (ISB&M)':['isbm.ac.in','isbm.edu.in'],
    	'ISBF - Indian School of Business & Finance':'isbf.edu.in',
		'Ishan Institute of Management and Technology':['ishan.ac','ishan.edu','ishan.ac.in','law.ishan.ac','iimt.ishan.ac','ishanayurved.com','pharmacy.ishan.ac'],
		'ITM Group of Institutions (All campus)':['itm.edu','itm.ac.in','itm.edu.in'],
		'ITS Dental College (ITSDC)':['itsdentalcollege.edu.in','its.edu.in','itsdentalcollege.ac.in'],
		'ITS Engineering College':['its.edu.in','its.ac.in'],
    	'Jagan Institute of Management Studies':'jimsindia.org',
    	'Jai Hind College':'jaihindcollege.edu.in',
    	'Jain (Deemed-to-be University), Bangalore':['jainuniversity.ac.in','cms.ac.in'],
    	'Jaipuria Institute of Management':'jaipuria.ac.in',
    	'Jamia Millia Islamia - A Central University':['st.jmi.ac.in','jmi.ac.in'],
		'Janhit Group of Institutions (JGI)':['jgi.edu','jgi.ac.in',],
    	'Jawaharlal Nehru University':['jnu.ac.in','mail.jnu.ac.in'],
    	'JECRC University':['jecrcmail.com','jecrcu.edu.in'],
		'Jeppiaar Engineering College':['jeppiaarcollege.org','jeppiaarcollege.edu','jeppiaarcollege.ac.in','jeppiaarinstitute.org'],
		'Jeppiaar Institute of Technology':['jeppiaarinstitute.org','jeppiaarinstitute.edu','jeppiaarinstitute.ac.in'],
    	'Jesus And Mary College , Delhi University':['jmc.ac.in','jmc.du.ac.in'],
		'JIIT - Jaypee Institute of Information Technology':['jiit.ac.in','mail.jiit.ac.in','jiit.edu'],
    	'JIIT - Jaypee Institute of Information Technology, Noida':'mail.jiit.ac.in',
		'JIMS Engineering Management Technical Campus (JEMTEC)':['jagannath.org','jagannath.org','jagannath.edu','jagannath.ac.in'],
		'JSS Academy of Technical Education':['jssaten.ac.in','jssaten.edu'],
    	'Justice Basheer Ahmed Sayeed College For Women (JBAS)':['jbascollege.edu.in','jbascollege.ac.in'],
		'JK Lakshmipat University':'jklu.edu.in',
    	'Kalinga Institute of Industrial Technology, (KIIT)':['kiitbiotech.ac.in','kiit.ac.in'],
    	'KIIT University (Kalinga Institute of Industrial Technology)':['kiitbiotech.ac.in','kiit.ac.in','biotech.kiit.ac.in'],
		'KCC Institute Of Legal & Higher Education':['kccitm.edu.in','kccitm.ac.in',],
		'KCC Institute of Technology and Management (KCC ITM)':['kccitm.edu.in','kccitm.ac.in'],
		'KCG College of Technology':['kcgcollege.com','hindustanuniv.ac.in','kcgcollege.edu','kcgcollege.ac.in'],
	    'Kirloskar Institute of Advanced Management Studies (KIAMS)':['kiams.ac.in','kiams.edu.ac.in'],
    	'Kirori Mal College, University of Delhi':['kmc.du.ac.in','kmcollege.ac.in'],
	    'Kohinoor International Management Institute (KIMI)':['kohinoor.ac.in','kimi.kohinoor.ac.in'],
    	'Lady Shri Ram College for Women':['lsrcollege.org','lsr.du.ac.in','lsr.edu.in'],
    	'Lakshmi Bai College (Delhi University, DU)':['lb.du.ac.in','lakshmibaicollege.in'],
	    'Lexicon Management Institute of Leadership and Excellence (Lexon Mile)':['mile.education','lexiconmile.com'],
    	'Lloyd Law College':['lloydbusinessschool.edu.in','lloydlawcollege.edu.in'],
	    'Lotus Business School (LBS)':'lotuscentre.ac.in',
    	'Lovely Professional University (LPU)':['lpu.co.in','lpu.in'],
		'Loyola College':['loyolacollege.edu','loyolacollege.ac.in'],
		'Loyola Institute Of Business Administration (LIBA)':'liba.edu',
    	'Loyola Law School':'lls.edu',
	    'M.E.S. Abasaheb Garware College':['mespune.edu.in','mespune.in'],
		'Madras Christian College':['mcc.edu.in','mcc.ac.in'],
		'Madras Christian College (MCC)':['mcc.edu.in','mcc.ac.in'],
		'Madras Institute Of Fashion Technology (MFT)':['mftindia.com','mftindia.edu','mftindia.ac.in'],
		'Madras Institute of Technology (MIT)':['mitindia.edu','mitindia.ac.in'],
		'Madras School Of Economics (MSE)':['mse.ac.in','mse.edu'],
		'Madras School Of Social Work (MSSW)':['mssw.in','mssw.edu','mssw.ac.in'],
	    'Maharashtra Institute of Medical Education and Research (MIMER)':'mitmimer.com',
	    'Mahatma Phule Krishi ViDYapeeth (MPKV)':'mpkv.ac.in',
		'Mangalmay Institute of Engineering and Technology (MIET)':['mangalmay.org','mangalmay.edu','mangalmay.ac.in'],
		'Mangalmay Institute of Management and Technology (MIMT)':['mangalmay.org','mangalmay.edu','mangalmay.ac.in'],
    	'Manipal Institute of Technology (Manipal Academy of Higher Education)' :['manipal.edu','learners.manipal.edu'],
    	'Manipal University ':['manipal.edu','muj.manipal.edu','datascience.manipal.edu'],
	    'Marathwada Mitra Mandals College of Commerce (MMCC)':'mmcc.edu.in',
	    'Marathwada Mitramandals College of Architecture':'mmcoa.edu.in',
    	'Mata Sundri College for Women(University Of Delhi)':'ms.du.ac.in',
    	'Maulana Azad National Institute of Technology (MANIT) Bhopal':['manitacin.onmicrosoft.com','manit.ac.in'],
	    'MCE Societys Allana College of Architecture':['azamcampus.org','allanaarchitecture.org'],
		'Measi Academy Of Architecture':['measiarch.net','measiarch.in','measiarch.edu'],
		'Measi Institute Of Management (MIM)':['measimba.ac.in','measimba.edu'],
		'Meenakshi College for Women':['meenakshicollege.com','meenakshicollege.edu','meenakshicollege.ac.in','meenakshicollege.edu.in'],
    	'Miranda House, University College for Women':'mirandahouse.ac.in',
	    'MIT College of Management (MITCOM) Kothrud':['mituniversity.edu.in','mitpune.edu.in','mitwpu.ac.in','mitwpu.edu.in','thescriptgroup.in'],
	    'Mit International School of Broadcasting and Journalism (MITISBJ)':['mitisbjmituniversity.edu.in','mituniversity.edu.in'],
	    'MIT World Peace University (MITWPU)':['mitwpu.edu.in','mitpune.edu.in','mitwpu.ac.in','thescriptgroup.in'],
	    'Mitsom College':['mitsomcollege.edu.in','mitsomcollege.com',],
	    'Mkssss Cummins College of Engineering For Women, Pune':'cumminscollege.in',
    	'MNIT Allahabad':['mnnit.ac.in','ecellmnnit.in'],
    	'MNIT Jaipur':'mnit.ac.in',
	    'Modern College of Arts, Science & Commerce':['moderncollegepune.edu.in','moderncollegegk.org'],
	    'Modern College of Pharmacy':'mcop.org.in',
		'Mohamed Sathak A.J. College Of Engineering':['msajce-edu.in','msajce-ac.in'],
		'Mohamed Sathak College Of Arts And Science':['mscartsandscience-edu.in','mscartsandscience-ac.in'],
		'MOP Vaishnav College For Women':['mopvc.edu.in','mopvc.ac.in','mopvcfw.in'],
    	'Mount Caramel College, Bangalore':'mccblr.edu.in',
    	'Narsee Monjee Institute of Management Studies (NMIMS)':['nmims.edu','nmims.edu.in'],
    	'N. L. Dalmia Institute of Management Studies and Research':['www.nldalmia.ac.in','www.nldalmia.edu.in','nldalmia.in'],
	    'National Institute of Construction Management & Research (NICMAR)':'nicmar.ac.in',
		'National Institute Of Fashion Technology (NIFT) All Campus':['nift.ac.in','nift.edu','nift.edu.in'],
    	'National Rail and Transportation Institute':'nrti.edu.in',
	    'Neville Wadia Institute of Management Studies and Research (NWIMSR)':'nevillewadia.com',
    	'Nirma University':'nirmauni.ac.in',
    	'NIT Agartala':'nita.ac.in',
    	'NIT Andhra P':'nitandhra.ac.in',
    	'NIT Arunachal Pradesh':['nitap.in','nitap.ac.in'],
	    'NIT Calicut':'nitc.ac.in',
    	'NIT Delhi':'nitdelhi.ac.in',
    	'NIT Durgapura':['phd.nitdgp.ac.in','mtech.nitdgp.ac.in','mca.nitdgp.ac.in','btech.nitdgp.ac.in'],
    	'NIT Goa':'nitgoa.ac.in',
    	'NIT Hamirpur':'nith.ac.in',
    	'NIT Jalandhar':'nitj.ac.in',
    	'NIT Jamshedpur':'nitjsr.ac.in',
    	'NIT Karnataka':['nitk.ac.in','nitk.edu.in'],
    	'NIT Kurukshetra':['nitkkr.edu.in','nitkkr.ac.in'],
    	'NIT Manipur':['nitmanipur.edu.in','nitmanipur.ac.in'],
    	'NIT Meghalaya':['nitm.edu.in','nitm.ac.in'],
    	'NIT Mizoram':['nitmz.edu.in','nitmz.ac.in'],
    	'NIT Nagaland':['nitnagaland.edu.in','nitnagaland.ac.in'],
    	'NIT Patna':['nitp.edu.in','nitp.ac.in'],
    	'NIT Raipur':['nitrr.edu.in','nitrr.ac.in'],
    	'NIT Roukela':['nitrkl.edu.in','nitrkl.ac.in'],
    	'NIT Sikkim':['nitsikkim.edu.in','nitsikkim.ac.in'],
    	'NIT Silchar':['nits.edu.in','nits.ac.in'],
    	'NIT Srinagar':['nitsri.edu.in','nitsri.ac.in'],
    	'NIT Surat':['svnit.edu.in','svnit.ac.in'],
    	'NIT Surathkal':['nitk.edu.in','nitk.ac.in'],
    	'NIT Tiruchirapalli':'nitt.edu',
    	'NIT Uttarakhand':['nituk.edu.in','nituk.ac.in'],
    	'NLU, Lucknow':['rmlnlu.edu.in','rmlnlu.ac.in'],
		'Noida Institute of Engineering and Technology (NIET)':['niet.co.in','niet.ac.in','niet.edu'],
		'Noida International University':['niu.edu.in','niu.ac.in'],
    	'NSUT - Netaji Subhas Institute of Technology':['nsut.ac.in','nsit.net.in','aiactr.ac.in'],
    	'O.P. Jindal Global University':['opju.ac.in','jgu.edu.in'],
    	'Pandit Deendayal Energy University (PDEU) (Formerly PDPU)':['spt.pdpu.ac.in','spm.pdpu.ac.in','sot.pdpu.ac.in','sls.pdpu.ac.in'],
		'Panimalar Engineering College':['panimalar.ac.in','panimalarengg.onmicrosoft.com','panimalar.edu'],
	    'Pimpri Chinchwad College of Engineering (PCCOE)':'pccoepune.com',
	    'Poona College of Pharmacy (PCP)':['pcp.bharatividyapeeth.edu','bharatividyapeeth.edu'],
    	'Poornima Institute of Engineering & Technology':['poornima.org','poornima.edu.in'],
    	'Poornima University':['poornima.edu.in','poornima.ac.in'],
		'Presidency College':['presidencycollegechennai.ac.in','presidencycollegechennai.edu','presidencycollege.ac.in'],
    	'Presidency University, Bangalore':'presidency.edu.in',
		'Prince Institute of Innovative Technology (PIIT)':['piitindia.edu.in','piitindia.ac.in'],
	    'Pune Institute of Business Management (PIBM)':['pibm.ac.in','pibm.edu.in','pibm.in'],
		'Quaide-E-Millath Government College For Women (Autonomous)':['qmgcw.edu.in','qmgcw.ac.in'],
		'Rajalakshmi Engineering College (REC)':['rajalakshmi.edu.in','rajalakshmi.ac.in',''],
	    'Rajgad Dnyanpeeths College of Pharmacy (RDCOP)':'rdcopbhor.com',
		'Rakshpal Bahadur Management Institute (RBMI)':['rbmi.in','rbmi.edu','rbmi.ac.in'],
    	'Ramaiah Institute of Technology':'msrit.edu',
		'Ramakrishna Mission Vivekananda College':['rkmvc.ac.in','rkmvc.edu'],
    	'Ramanujan College, University of Delhi':'ramanujan.du.ac.in',
    	'Ramjas College':'ramjas.du.ac.in',
		'RIG Institute of Hospitality and Management':['riginstitute.com','riginstitute.edu','riginstitute.ac.in'],
    	'RV College of Engineering (RVCE)':'rvce.edu.in',
	    'S. P. Jain Institute of Management and Research':'spjimr.org',
    	'S.A. Engineering College':['saec.ac.in','saec.edu'],
		'Sagunthala R&D Institute of Science and Technology (Vel Tech)':['veltech.edu.in','veltechengg.com','veltechuniv.edu.in'],
		'Sathyabama Institute Of Science And Technology':['sathyabama.ac.in','sathyabamauniversity.ac.in','somca.ssn.edu.in'],
		'Satyawati College (Delhi University, DU)':['satyawati.du.ac.in','satyawati.edu.ac.in','satyawatie.du.ac.in','satyawatievedu.ac.in'],
		'Saveetha Dental College & Hospital':['saveethamedicalcollege.com','saveethadental.com'],
		'Saveetha Engineering College (SEC)':'saveetha.ac.in',
		'Saveetha Medical College':['saveetha.com','saveetha.edu','saveetha.ac.in'],
		'Saveetha School Of Engineering (SSE)':['saveetha.com','saveetha.ac.in','saveetha.edu'],
		'Saveetha School Of Law':['saveetha.com','sslsaveetha.com',],
	    'Savitribai Phule Pune University (SPPU)':['pun.unipune.ac.in','unipune.ac.in','cs.unipune.ac.in','scms.unipune.ac.in','unipune.ac.in','uopca.unipune.ac.in'],
		'SDN Bhatt Vaishnav College For Women':['sdnbvc.edu.in','sdnbvc.ac.in'],
    	'Shaheed Bhagat Singh College':'sbsc.in ',
    	'Shaheed Sukhdev College of Business Studies':'sscbs.du.ac.in',
    	'Sharda University':['ug.sharda.ac.in','sharda.ac.in','sgei.org','pg.sharda.ac.in'],
    	'Shiv Nadar University':'snu.edu.in',
    	'Shivaji College, University of Delhi':'shivaji.du.ac.in',
		'Shrimathi Devkunvar Nanalal Bhatt Vaishnav College For Women':['sdnbvc.edu.in','sdnbvc.ac.in'],
    	'Shri Ram College of Commerce (SRCC)':'srcc.du.ac.in',
    	'Sikkim Manipal University':['smude.edu.in','smims.smu.edu.in'],
	    'Sinhgad Business School (SBS)':'sinhgad.edu',
	    'Sinhgad College of Architecture (SCOA)':['sinhgad.edu','scoasinhgad.edu'],
	    'Sinhgad College of Art, Commerce and Science':'sinhgad.edu',
	    'Sinhgad College of Science (SCOS)':['sinhgad.edu','scossinhgad.edu'],
	    'Sinhgad Dental College and Hospital (SDCH)':'sinhgad.edu',
	    'Sinhgad Institute of Hotel Management & Catering Technology (SIHMCT)':['sihmctsinhgad.edu','sinhgad.edu'],
	    'Sinhgad Institute of Management (SIOM)':['sinhgad.edu','siomsinhgad.edu'],
	    'Sinhgad Law College':'sinhgad.edu',
		'Skyline Institute Of Engineering And Technology (SIET)':['skylineinstitute.com','skylineinstitute.ac.in','skylineinstitute.edu'],
	    'Smt Kashibai Navale Medical College and General Hospital (SKNMCGH)':'sknmcgh.org',
    	'Sophia College for Women, Mumbai':['sophiacollegemumbai.com','sophiacollege.edu.in'],
		'Sree Balaji Medical College And Hospital (SBMCH)':['sbmc_hyahoo.com','sbmc_hyahoo.edu','sbmch.ac.in','bharathuniv.ac.in'],
    	'Sri Aurobindo College, University of Delhi':'aurobindoe.du.ac.in',
		'Sri Ramachandra Institute Of Higher Education And Research (SRIHER)':['sriramachandra.edu.in','sriramachandra.ac.in'],
		'Sri Ramachandra Medical College':['sriramachandra.edu.in','sriramachandra.ac.in'],
		'Sri Sairam Engineering College (SSEC)':['sairam.edu.in','sairam.ac.in','sims.sairam.edu.in','sairamgroup.in','sairamce.edu.in','sairamit.edu.in','saimedical.com','sairamsiddha.edu.in','sairamayur.edu.in','sairamhomoeo.edu.in','sairamgroup.in'],
		'Sri Sairam Institute Of Technology (SSIT)':['sairamit.edu.in','sairamgroup.in'],
    	'Sri Venkateswara College, Delhi University':'svc.edu.du.ac.in',
    	'Sri Venkateswara College, Delhi University':['svc.edu.in','svc.ac.in','svc.du.ac.in'],
    	'Sri Venkateswara University':'svuniversity.edu.in',
    	'SRM University':'srmist.edu.in',
    	'SRM University, Amaravati, AP':'srmap.edu.in',
		'SSN College Of Engineering (SSNCE)':['ssn.edu.in','bme.ssn.edu.in','chemical.ssn.edu.in','cse.ssn.edu.in','mech.ssn.edu.in','somca.ssn.edu.in'],
    	'St. Joseph’s College of Commerce':'sjcc.edu.in',
	    'St. Miras College For Girls':'stmirascollegepune.edu.in',
    	'St. Xavier University':['sxu.edu','mymail.sxu.edu'],
    	'St. Xaviers College (Autonomous), Kolkata':'sxccal.edu',
    	'St. Xaviers College, Mumbai':'xaviers.edu.in',
    	'Suresh Gyan Vihar University':'mygyanvihar.com',
	    'Suryadatta College of Hospitality Management and Travel Tourism (SCHMTT)':['suryadatta.edu.in','suryadatta.org','simmc.org'],
	    'Suryadatta Institute of Fashion Technology (SIFT)':['suryadatta.edu.in','sgisift.org'],
	    'Suryadatta Institute of Management and Mass Communication (SIMMC)':['simmc.org','suryadatta.edu.in'],
    	'Sushant University ( Previously Ansal University)':['ansaluniversity.edu.in','sushantuniversity.edu.in'],
    	'Symbiosis Center for Distance Learning':'student.scdl.net',
	    'Symbiosis Centre For Information Technology (SCIT)':['scit.edu','associates.scit.edu'],
	    'Symbiosis Centre For Management and Human Resource Development (SCMHRD)':'scmhrd.edu',
	    'Symbiosis College of Arts and Commerce':'sicsr.ac.in',
    	'Symbiosis Institute of Business Management, Pune':['sibmpune.edu.in','associates.sibmpune.edu.in'],
    	'Symbiosis Institute of Computer Studies and Research (SICSR)':'sicsr.ac.in',
        'Symbiosis Institute of Design':'sid.edu.in',
	    'Symbiosis Institute of Digital and Telecom Management (SIDTM)':'sidtm.edu.in',
    	'Symbiosis Institute of International Business':'siib.ac.in',
    	'Symbiosis Institute of Management Studies, Noida':['symlaw.edu.in','scmsnoida.ac.in'],
	    'Symbiosis Institute of Management Studies, Pune':'sims.edu',
    	'Symbiosis Institute of Media and Communication (SIMC)':'simc.edu',
	    'Symbiosis Institute of Media and Communication (SIMC)':'simc.edu',
    	'Symbiosis Institute of Technology':'sitpune.edu.in',
    	'Symbiosis International University ':'siu.edu.in',
    	'Symbiosis Law School':['symlaw.ac.in','symlaw.edu.in','student.slsh.edu.in','slsh.edu.in'],
	    'Symbiosis Law School':['symlaw.ac.in','student.slsh.edu.in','slsh.edu.in','symlaw.ac.in'],
    	'Symbiosis School for Liberal Arts':'ssla.edu.in',
    	'Symbiosis School of Economics':'sse.ac.in',
    	'Symbiosis Skills and Professional University':['student.sspu.ac.in','student.ssou.ac.in'],
    	'Symbiosis Statistical Institute':'ssi.edu.in',
    	'Symbiosis University, Nagpur':'slsnagpur.edu.in',
		'Tamil Nadu Dr. Ambedkar Law University':['tndalu.ac.in','tndalu.edu'],
		'Tamil Nadu Teachers Education University':['tnteu.ac.in','tnteu.edu'],
		'Tamil Nadu Veterinary And Animal Sciences University (TANUVAS)':['tanuvas.ac.in','tanuvas.edu'],
		'Tamil Nadu Veterinary And Animal Sciences University (TANUVAS)':['tanuvas.ac.in','tanuvas.edu',],
    	'Thapar University ':'thapar.edu',
	    'The National Institute of Bank Management (NIBM)':'nibmindia.org',
    	'The Northcap University':'ncuindia.edu',
		'The Queen Mary’s College of Tamil Nadu':['queenmaryscollege.edu.in','queenmaryscollege.ac.in'],
		'United Group of Institutions':['united.ac.in','united.ac.in','united.edu'],
    	'University of Delhi (Delhi University, DU)':['svc.edu.du.ac.in','ss.du.ac.in','sol.du.ac.in','sol-du.ac.in','shivaji.du.ac.in','sgndkc.du.ac.in','rla.du.ac.in','ramanujan.du.ac.in','pg.du.ac.in','one.ducic.ac.in','lc2.du.ac.in','lb.du.ac.in','kmcollege.ac.in','kmc.du.ac.in','keshav.du.ac.in','kalindi.du.ac.in','ihe.du.ac.in','fms.edu','dbe-du.org','cs.du.ac.in','clc.du.ac.in','bcas.du.ac.in','aurobindoe.du.ac.in','arsd.edu.du.ac.in','arsd.du.ac.in','andc.du.ac.in'],
    	'University of Petroleum and Energy Studies - UPES':['stu.upes.ac.in','ddn.upes.ac.in'],
	    'Vaikunth Mehta National Institute of Cooperative Management':'vamnicom.gov.in',
		'Vel Tech High Tech Dr. Rangarajan Dr. Sakunthala Engineering College (Vel Tech High Tech)':['velhightech.com','velhightech.edu','velhightech.ac.in','veltechmultitech.org','veltechmultitech.edu','veltechmultitech.ac.in'],
		'Vel Tech Multi Tech Dr Rangarajan Dr Sakunthala Engineering College (Vel Tech Multi Tech)':['veltechmultitech.org','veltechmultitech.edu','veltechmultitech.ac.in','velhightech.com','velhightech.edu','velhightech.ac.in'],
		'Velammal Engineering College (VEC)':'velammal.edu.in',
    	'Vellore Institute of Technology (VIT)':['vit.ac.in','vitstudent.ac.in','vitalum.ac.in'],
    	'Vellore Institute of Technology (VIT)':['vit.ac.in','vitstudent.ac.in'],
		'Vels Institute Of Science, Technology And Advanced Studies (VISTAS)':['velsuniv.ac.in','velsuniv.edu'],
		'Veterinary College And Research Institute (VCRI)':'email.gov.in',
		'Vishveshwarya Group Of Institutions - (VGI)':['vgi.ac.in','vgi.edu'],
	    'Vishwakarma Institute of Information Technology (VIIT)':'viit.ac.in',
    	'VIT Bhopal University (Vellore Institute of Technology Bhopal':'vitbhopal.ac.in',
		'Women’s Christian College (WCC)':['wcc.edu.in','wcc.ac.in','wcconline.wcc.edu.in'],
		'Xavier Institute Of Management And Entrepreneurship [XIME]':['xime.org','xime.ac.in','xime.edu'],
    	'Xavier School of Management (XLRI)':['xlri.ac.in','astra.xlri.ac.in'],
	}

    if request.method == 'POST':
        institution = request.POST['institution']
        Email = request.POST['institution_email']
        graduation_year = request.POST['graduation_year']
        request.session['institution_name'] = institution
        request.session['institution_email'] = Email
        request.session['graduation_year'] = graduation_year
        domains = Institution.get(institution)
        if domains is None:
            messages.error(request,"Ohh! Looks like your college email doesn't match with your institution database. If you think it's a mistake, please shoot us a mail at verify@studentpeeps.club")
            return render(request, 'signup3.html', {'Institution': Institution})
        afterSlice = Email.split("@")
        sliceValue = afterSlice[1]
        i=0
        for i in domains:
            dom = i
            if(dom==sliceValue):
                domains=sliceValue
                break

        if Registers.objects.filter(email=Email).exists() or User.objects.filter(email=Email).exists():
            messages.error(request, 'Email is already Taken')
            return redirect('signup')
			
        if(sliceValue==domains):
            username = request.session.get('email')
            firstname = request.session.get('fname')
            lastname = request.session.get('lname')
            Password = request.session.get('password')
            user = User.objects.create_user(username=username, password=Password, email=Email, first_name=firstname)
            user.is_active = False
            user.save()
            a = request.user
            request.session['user'] = user.email

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})

            activate_url = 'https://' + domain + link

            message = render_to_string('mail_body.html', {'fname': firstname,'lname' : lastname ,'activate_url': activate_url})
            msg = EmailMessage(
                "you're just one step away...",
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
            )
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send(fail_silently=False)
            gender = request.session.get('gender')
            date = request.session.get('date')
            month = request.session.get('month')
            year = request.session.get('year')
            unverified = UnVerified(username=username,password=Password,email=username,firstname=firstname,lastname=lastname,gender=gender,
                            date=date,month=month,year=year,institution=institution,institution_email=Email,graduation_year=graduation_year)
            unverified.save()
            return redirect('Verificationmsg')
        else:
            messages.error(request, "Ohh! Looks like your college email doesn't match with your institution database. If you think it's a mistake, please shoot us a mail at verify@studentpeeps.club")
            return render(request,'signup3.html', {'Institution':Institution})

    return render(request,'signup3.html', {'Institution':Institution})

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Looks like you haven't signed up yet or you've entered the wrong password.")
            return redirect('login')
    else:
        return render(request, 'login.html')

def upload(request):
    if request.method == "POST":
        images = request.FILES['image']
        username = request.session.get('email')
        password = request.session.get('password')
        email = request.session.get('email')
        fname = request.session.get('fname')
        lname = request.session.get('lname')
        gender = request.session.get('gender')
        date = request.session.get('date')
        month = request.session.get('month')
        year = request.session.get('year')
        
        user = User.objects.create_user(username=username, password=password, email=email, first_name=fname)
        user.is_active = False
        user.save()
        register = Upload(username=username, password=password, email=email, firstname=fname, lastname=lname,
                             gender=gender,date=date, month=month, year=year,image=images)
        register.save()
        return redirect('Uploadmsg')
    return render(request,'signup4.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

class VerificationView(View):
    def get(self, request, uidb64, token):
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        user.is_active = True
        if UnVerified.objects.filter(username=user.username).exists():
            profile = UnVerified.objects.get(username=user.username)
            register = Registers(username=profile.username,password=profile.password,email=profile.email,firstname=profile.firstname,lastname=profile.lastname,gender=profile.gender,
                            date=profile.date,month=profile.month,year=profile.year,institution=profile.institution,institution_email=profile.institution_email,graduation_year=profile.graduation_year)
            register.save()
            user.save()
            emailname =  profile.firstname
            pemail = profile.email
            UnVerified.objects.filter(username=profile.username).delete()
            Signup.objects.filter(email=pemail).delete()
            Yourdetail.objects.filter(firstname=emailname).delete()
            user = auth.authenticate(username=profile.username, password=profile.password)
            

            if user is not None:
                auth.login(request, user)
                message = render_to_string('mail_body2.html', {'fname' : emailname})
                msg = EmailMessage(
                "You're in!!",
                message,
                settings.EMAIL_HOST_USER,
                [pemail],
                )
                msg.content_subtype = "html"  # Main content is now text/html
                msg.send(fail_silently=False)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('login')
        return redirect('login')

def myaccount(request):
    users = request.user.username
    if Registers.objects.filter(username=users).exists():

        profile = Registers.objects.get(username=users)
        if request.method == "POST":
            FirstName = request.POST['fname']
            LastName = request.POST['lname']
            Gender = request.POST['Gender']
            Date = request.POST['date']
            Month = request.POST['month']
            Year = request.POST['year']
            images = request.FILES['image']
            profile.firstname=FirstName
            profile.lastname=LastName
            profile.gender=Gender
            profile.date=Date
            profile.month=Month
            profile.year=Year
            profile.profile_image=images
            profile.save()
        return render(request, 'edit_profile.html',{'profile':profile})
    else:
        profile = Upload.objects.get(username=users)
        if request.method == "POST":
            FirstName = request.POST['fname']
            LastName = request.POST['lname']
            Gender = request.POST['Gender']
            Date = request.POST['date']
            Month = request.POST['month']
            Year = request.POST['year']
            images = request.FILES['image']
            profile.firstname = FirstName
            profile.lastname = LastName
            profile.gender = Gender
            profile.date = Date
            profile.month = Month
            profile.year = Year
            profile.profile_image = images
            profile.save()
        return render(request, 'edit_profile.html',{'profile':profile})

def error_404_view(request, exception):
     return render(request, '404.html')

def uploademail(request):
    messages = None
    if request.method == "POST":
        email = request.POST['email']
        message = render_to_string('uploadverification.html')
        msg = EmailMessage(
                "You're in!!",
                message,
                settings.EMAIL_HOST_USER,
                [email],
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send(fail_silently=False)
        messages = "Mail Sent!!"   
        
        return render(request, 'uploademail.html',{'message' : messages})
    return render(request, 'uploademail.html')