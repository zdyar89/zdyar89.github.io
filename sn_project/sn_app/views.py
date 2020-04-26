from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect as redirect
from django.core.files.storage import default_storage
import traceback
import speech_recognition as sr
import mimetypes

# Create your views here.
def login(request):
    return render(request, 'index.html')


def home(request):
    print("in home")
    args={}
    if request.method=='POST':
        if request.POST.get('submitfile'):
            print('pressed submit file button')
            try:
                file = request.FILES['audiofile']
                args["filename"]=file.name
                r = sr.Recognizer()
                with sr.AudioFile(file) as source:
                    audio = r.record(source) #THIS DOESN'T ACTUALLY RECORd
                    text = r.recognize_google(audio)
                    args["stt"]=text
                default_storage.save(file.name,file)
            except Exception as e:
                print(traceback.print_exc())
                args["stt"] = "YOU DIDN'T UPLOAD A FILE"
                return render(request,"base.html",args)
            #TemplateResponse(request,"stt.html",args)
            return render(request,"base.html",args)
        else:
            print("was not pressed")
            return render(request, 'base.html')
    else:
        return render(request, 'editor/base.html')

def test(request):
    return render(request, 'test.html')

def uploadfile(request):
    if request.method=="POST":
        print("posted")
        file = request.FILES['audiofile']
        r = sr.Recognizer()
        with sr.AudioFile(file) as source:
            audio = r.record(source) #THIS DOESN'T ACTUALLY RECORd
            text = r.recognize_google(audio)

    return render(request, 'base.html',{'stt': text})


def stt(request):
    print("in stt")
    # file = request.session['audiofile']
    return render(request,"stt.html")
    # print("posted")
    # audiofile = request.session("audiofile")
    # r = sr.Recognizer()
    # with sr.AudioFile(audiofile) as source:
    #     audio = r.record(source) #THIS DOESN'T ACTUALLY RECORd
    #     text = r.recognize_google(audio)
    #     print(text)

def editor(request):
    if (request.method=="POST"):
        print(request.POST.get)
        args={}
        file = request.FILES['files']
        args["filename"] = file.name
        if file.name.endswith(".txt"):
            args["text"] = file.read().decode("utf-8")
            return render(request,"editor/editor.html",args)
        elif file.name.endswith(".wav"):
            r = sr.Recognizer()
            with sr.AudioFile(file) as source:
                audio = r.record(source) #THIS DOESN'T ACTUALLY RECORd
                text = r.recognize_google(audio)
                args["text"]=text
            return render(request,"editor/editor.html",args)
    else:
        return render(request,"editor/editor.html")

#commit test