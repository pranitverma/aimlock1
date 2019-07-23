from django.shortcuts import render,HttpResponse,redirect
from myuser.forms import UserRoleForm,SignupForm
from myuser.models import Signup
from miscellaneous.otpgen import otp_sending,time
from django.core.files.storage import FileSystemStorage
from miscellaneous.smtp import smtp
import smtplib
# Create your views here.
def index(request):
    return HttpResponse("<h1> la femme</h1>")
def home(request):
    return render(request,"home.html")
def userindex(request):
    return render(request,"userindex.html")
def addrole(request):
    if request.method=="POST":
        form=UserRoleForm(request.POST)
        f=form.save(commit=False)
        f.rolename=request.POST["userrole"]
        f.save()
        return HttpResponse("<h1> DATA SAVED </h1>")



    return render(request,"addrole.html")
def signup(request):
    if request.method == "POST":

        user_image = None
        if request.FILES:
            myfile = request.FILES['userimage']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            user_image = fs.url(filename)
            user_image = myfile.name
        form = SignupForm(request.POST)
        f = form.save(commit=False)
        f.email = request.POST["email"]
        f.name = request.POST["name"]
        f.city = request.POST["city"]
        f.password = request.POST["password"]
        f.mobile = request.POST["mobile"]
        f.image = user_image
        f.otp=otp_sending()
        otp=otp_sending()
        ti=time()
        f.otpgentime=time()
        token= str(otp)+str(request.POST["email"][0:5])+str(request.POST["mobile"][0:5])
        link="http://127.0.0.1:8000/activeuser/?token="+str(token)+"&email="+request.POST["email"]

        f.token = token
        f.save()
        smtp(f.name, link,f.otpgentime,f.email)



        return HttpResponse("<h1>  verify the existing user, see your email </h1>")



    return render(request, "signup.html")


def fetchdata1(request):
    data = Signup.objects.all()
    return render(request,"fetch.html", {'ud':data})
    return render(request,"fetch.html")
def fetchdata(request):

    if request.method =="POST":
        value = request.POST["email"]
        data = Signup.objects.filter(email=value)
        return render(request,"fetch.html", {'ud':data})

    return render(request,"fetch.html")

def deletedata(request):
    useremail= request.GET["em"]
    data = Signup.objects.get(email=useremail)
    data.delete()
    return redirect("/userindex/fetch/")

def editdata(request):
    email = request.GET["email"]
    data = Signup.objects.get(email=email)
    if request.method == "POST":
        n = request.POST["name"]
        e = request.POST["email"]
        c = request.POST["city"]
        m = request.POST["mobile"]
        p = request.POST["password"]
        update = Signup(
            email=e,
            name=n,
            city=c,
            mobile=m,
            password=p
        )
        update.save(update_fields=["name", "city", "mobile", "password"])
        return redirect("/userindex/fetch1/")

    return render(request,"edit.html", {'ud':data})


def login(request):
    if request.method == "POST":
        un = request.POST["email"]
        up = request.POST["password"]
        try:
            data = Signup.objects.get(email=un)

        except:
            return render(request,"login.html", {'emailerror':True})

        dp = data.password
        active = data.isactive
        if (active==False):
            return render(request, "login.html", {'activeerror':True})

        else:
            if (dp==up):
                request.session['email'] = un
                request.session['Authentication'] = True
                return redirect("/userindex/fetch/")
            else:
                return render(request, "login.html", {'passworderror': True})
    return render(request,"login.html")

def verifyuser(request):
    token = request.GET["token"]
    email = request.GET["email"]
    data = Signup.objects.get(email=email)
    email1=data.token

    if (token==email1):
        update=Signup(
            email=email,
            isactive=True
        )
        update.save(update_fields=["isactive"])

        return HttpResponse("<h1>verified </h1>")

    else:
        return HttpResponse("<h1>not verified </h1>")


def updatepassword(request):

    emailid = request.session['email']

    data = Signup.objects.get(email=emailid)

    value1 = data.name

    otp_msg = otp_sending()
    otp_time = time()
    update = Signup(
        email=emailid,
        otp=otp_msg,
        otpgentime=otp_time
    )
    update.save(update_fields=["otp", "otpgentime"])

    smtp(value1, otp_msg, otp_time, emailid)

    #tokenvalue = data.OTP

    if request.method == "POST":

        dbotp = data.otp
        otpvalue = request.POST["OTP"]

        if dbotp == otpvalue:

            return render(request, "password_update.html", {'updatepassword': True})

        confirmation(request)

        if dbotp != otpvalue:

            return render(request, "password_update.html", {'OTP': True, 'wrongotp': True})

    return render(request, "password_update.html")


def confirmation(request):
    if request.method == "POST":
        emailid = request.session["email"]

        n_p_v = request.POST["np"]
        c_p_v = request.POST["cp"]

        if n_p_v == c_p_v:
            update = Signup(
                    email=emailid,
                    password=c_p_v
                )
            update.save(update_fields=["password"])

            return render(request, "home.html")
        else:
            HttpResponse("<h1> New-Password and Confirm-Password value does not match </h1>")




















