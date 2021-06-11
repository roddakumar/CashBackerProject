from django.shortcuts import render
from django.shortcuts import render, redirect 
from django import forms
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import os
from django.core.files.storage import FileSystemStorage
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Create your views here.
def index(request):
 
 return render(request,'fileView.html') 


def upload_file(request):
    if request.method == 'POST' :
     myfile = request.FILES['doc']
     print(myfile.name) ## mysheet.xslx
     fs = FileSystemStorage()
     filename = fs.save(myfile.name, myfile)
     fileurl = fs.url(filename)
     ROOT_DIR1 = os.path.dirname(os.path.abspath(myfile.name))
     d = ROOT_DIR1+'\\media\\'+ myfile.name
     xl_file = pd.read_csv(d)
     new_data = xl_file.dropna(axis = 0, how ='any')
     splitt=myfile.name
     print(new_data)
     imageName = splitt.split(".")[0]+'.png'
     plt.plot(xl_file["TARGET_deathRate"], xl_file["incidenceRate"])
     plt.savefig(ROOT_DIR1+'\\media\\'+imageName)
     print(ROOT_DIR1+'\\media\\'+myfile.name+'.png')
    
    return render(request,'DisplayGraph.html',{'userimg': imageName})



