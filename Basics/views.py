from django.shortcuts import render

# Create your views here.
def calculation(request):
    result=""
    if request.method == "POST":
        no1=int(request.POST.get('txtno1'))
        no2=int(request.POST.get('txtno2'))
        btn=request.POST.get('btnsubmit')
        if btn=="+":
            result=no1+no2
        elif btn=="-":
            result=no1-no2
        return render(request,"Basics/Calculator.html",{'res':result})
    else:
        return render(request,"Basics/Calculator.html",{'res':result})

def largest(request):
    if request.method == "POST":
        n1=int(request.POST.get('txtno1'))
        n2=int(request.POST.get('txtno2'))
        n3=int(request.POST.get('txtno3'))
        btn=request.POST.get('btnsubmit')
        if btn=="check":
            if n1>=n2 and n1>=n2:
                r=n1
                return render(request,"Basics/largest.html",{'res1':r})          
            elif  n2>=n3 and n2>=n1:
                r=n2
                return render(request,"Basics/largest.html",{'res1':r})          
            elif  n3>=n1 and n3>=n2:
                r=n3  
                return render(request,"Basics/largest.html",{'res1':r})               
            else:
                return render(request,"Basics/largest.html",{'res1':r})          
        else:
            return render(request,"Basics/largest.html",{'res1':r})          
    else:
        return render(request,"Basics/largest.html",{'res1':r})            

def student(request):
    if request.method == "POST":
        n=request.POST.get('txt_name')
        c=request.POST.get('course')
        m1=int(request.POST.get('m1'))
        m2=int(request.POST.get('m2'))
        m3=int(request.POST.get('m3'))
        m4=int(request.POST.get('m4'))
        m5=int(request.POST.get('m5'))
        m6=int(request.POST.get('m6'))
        avg=(m1+m2+m3+m4+m5+m6)/6
        return render(request,"Basics/student.html",{"name":n,"course":c,"avg1":avg},)
    else:
        return render(request,"Basics/student.html")
        
        
        
        
  
        
             
                                    
            
            
    
 
        

 