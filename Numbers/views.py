from dataclasses import replace
from django.shortcuts import render,redirect
import math
import random
from  random import randint
from math import ceil, floor
from .models import *
import datetime
from datetime import datetime
from num2words import num2words
from email import message
from django.contrib import messages
from math import ceil, floor
from sympy import *
from sympy import N
from .models import *
from .utilities import *

#Function for getting the random numbers with n digits
def random_with_N_digits(range_start,range_end):
    l1=[]
    present=dict()
    for i in range(0,5):
       temp=randint(range_start, range_end)
       if temp not in present.keys():
            l1.append(temp)
            present[temp]=1
            
    return l1 

def random_with_N_digits1(range_start,range_end,n):
    l1=[]
    present=dict()
    for i in range(0,5):
       temp=round(random.uniform(range_start, range_end), int(n))
       if temp not in present.keys():
            l1.append(temp)
            present[temp]=1
            
    return l1   

def random_with_single_digits(range_start,range_end):
    l1=[]
    present=dict()
    for i in range(0,1):
       temp=randint(range_start, range_end)
       if temp not in present.keys():
            l1.append(temp)
            present[temp]=1
            
    return l1  

def random_with_single_digits1(range_start,range_end,n):
    l1=[]
    present=dict()
    for i in range(0,1):
       temp=round(random.uniform(range_start, range_end), int(n))
       if temp not in present.keys():
            l1.append(temp)
            present[temp]=1
            
    return l1 

# Create your views here.
def home(request):
         return render(request,'base/math-calculator.html')


def percenttodecimalcalculator(request):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/{aa}-percentage-as-a-decimal/')

    else:
         return render(request,'Mathcue/percent-to-decimal-calculator.html')

def percentagetodecimal_details(request,aa):
  if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/{aa}-percentage-as-a-decimal/')
  else:    
    
    x = round(float(aa)/100,4)
    z = int(float(aa))
    
    query=percenttToDecimalCalculator.objects.filter(inputEnter=str(aa))
    if len(query)==0:
        solutionTitle="Percent to Decimal  Calculator | Free Calculator to find Percent to Decimal"
        detailStep=f'''<p>What is {aa} percent as a decimal? Get the answer for the question using the percent to decimal conversion. {aa} percent to a decimal is {x}</p><p>The given number is : {aa} </p><p>Divide a percent by 100 and remove the percent sign to convert from a percent to a decimal. Another way is to move the decimal two places left. </p><p>The formula to convert percent to decimal is <b>d = p÷ 100</b> </p>p>Let us convert {aa} percent as a decimal number with detailed explanation. </p> <ol><li>First write the percent in the form of fraction.<br> {aa}% = {aa}/100</li>  <br><li>Now divide {aa} by 100 to write in the decimal form.<br>  {aa} ÷ 100 = {x}</li></ol><p>So, {aa}% as a decimal is equal to {x}</p>'''
        finalAnswer=str(x)
        obj=percenttToDecimalCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug="",date_modified=datetime.datetime.now())
        obj.save()

    list1 = []
    lst1 = []
    sum1 = z
    while sum1 < z+0.33:
        sum1 = round(sum1 +0.01,2)
        list1.append(sum1)
        per1 = round(sum1/100,4)
        lst1.append(per1)

    dict1 = dict(zip(list1, lst1))
    
    list2 = []
    lst2 = []
    sum2 = z + 0.33
    while sum2 < z+0.66:
        sum2 = round(sum2 +0.01,2)
        list2.append(sum2)
        per2 = round(sum2/100,4)
        lst2.append(per2)
    dict2 = dict(zip(list2, lst2))

    list3 = []
    lst3 = []
    sum3 = z + 0.66
    while sum3 < z+0.99:
        sum3 = round(sum3 +0.01,2)
        list3.append(sum3)
        per3 = round(sum3/100,4)
        lst3.append(per3)
    dict3 = dict(zip(list3, lst3))
    r1=int(floor(float(aa)))
    randList1=random_with_N_digits(r1+1,r1+100)
    context = {
        'dict1':dict1,
        'dict2':dict2,
        'dict3':dict3,
        'list1':list1,
        'list2':list2,
        'list3':list3,
        'lst1':lst1,
        'lst2':lst2,
        'lst3':lst3,
        'x':x,
        'aa':aa,
        'check':True,
        'id':1,
        'randList1':randList1
    }
    return render(request,'Mathcue/percent-to-decimal-calculator-details.html',context)



def decimaltopercentagecalculator(request):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/{aa}-decimal-as-a-percentage/')

    else:
        return render(request,"Mathcue/decimal_percentage.html")


def decimaltopercentage(request,aa):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/{aa}-decimal-as-a-percentage/')
    else:
        
        x = int(float(aa)*100)
        r1=int(floor(float(aa)))
        randList1=random_with_N_digits(r1+1,r1+100)
        query=decimalToPercentageCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="Decimal to percent  Calculator makes it easy for you to find Decimal to percent "
            detailStep=f'''<p>The given number is : {aa} </p> <p>Multiply a decimal by 100 and add the percent sign to convert from a decimal to a percent. </p> <p>The formula to convert Decimal to percent is <b>p = d x 100</b> </p> <p>Let us convert {aa} decimal as a percent number with detailed explanation. </p> <ul style="list-style: none;"> <li>Express the decimal number {aa} as a percent.</li> <li>To convert the decimal {aa} into a percentage you have to multiply {aa} by 100.</li> <li>{aa} × 100 = {x}</li> <li>Now add the % symbol to the obtained result.</li> <li>Thus {aa} as a percent is {x}%</li> </ul>'''
            finalAnswer=str(x)
            obj=decimalToPercentageCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug="",date_modified=datetime.datetime.now())
            obj.save()

        list1 = []
        lst1 = []
        for i in range(1, 34):      
            z = str(aa)+str(i)
            #print(z)
            list1.append(z)
            zz = round(float(z)*100, 4)
            lst1.append(zz)
        dict1 = dict(zip(list1, lst1))


        list2 = []
        lst2 = []
        for i in range(34, 67):
            z = (str(aa)+str(i))
            list2.append(z)
            zz = round(float(z)*100, 4)
            lst2.append(zz)
        dict2 = dict(zip(list2, lst2))

        list3 = []
        lst3 = []
        for i in range(67, 100):
            z = (str(aa)+str(i))
            list3.append(z)
            zz = round(float(z)*100, 4)
            lst3.append(zz)
        dict3 = dict(zip(list3, lst3))

        
        context = {
            #'randomlist':randomlist,
            'x':x,
            'aa':aa,
            'dict1':dict1,
            'dict2':dict2,
            'dict3':dict3,
            'list1':list1,
            'list2':list2,
            'list3':list3,
            'lst1':lst1,
            'lst2':lst2,
            'lst3':lst3,
            
            'check':True,
            'id':1,
            'randList':randList1
                }
        return render(request,"Mathcue/decimaltopercentage_details.html", context) 



def dividedbywhatcalculator(request): 
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None
        return redirect(f'/{aa}-divided-by-what-equals-to-{cc}/')    

    else:
        return render(request,"Mathcue/dividedbywhat.html")

def dividedbywhatcalculatordetails(request,aa,cc):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None
        return redirect(f'/{aa}-divided-by-what-equals-to-{cc}/')    

    else:
        x = round(float(float(aa)/float(cc)) ,3)
        inputEnter=f"{aa},{cc}"

        query=dividedByWhatCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:  
                solutionTitle="Divided by what equals  Calculatorr | Divided by what equals"
                finalAnswer=f"{x}"
                detailStep=f'''<p>The process to find out Divided by What Equals is given below. They are along the lines </p> <ol> <li>The first and foremost step is to identify the given inputs and unknown values to be found.</li> <li>Then, plug in the inputs in the formula divided by what equals i.e. Z/X = Y.</li> <li>Using the cross multiplication technique rewrite the equation.</li> <li>Solve for the unknown value easily.</li> </ol>'''
                obj=dividedByWhatCalculator(inputEnter=inputEnter,finalAnswer=finalAnswer,detailStep=detailStep,solutionTitle=solutionTitle,slug="",date_modified=datetime.datetime.now())
                obj.save()
        r1=int(floor(float(aa)))
        r2=int(floor(float(cc)))
        randList1=random_with_N_digits(r1+1,r1+100)
        randList2=random_with_N_digits(r2+1,r2+100)
            
        context = {
            'aa':aa,
            'cc':cc,
            'x':x,
            'check':True,
            'id':1,
            'randList1':randList1,
            'randList2':randList2
        }
        return render(request,"Mathcue/dividedbywhat-details.html", context)




def negativedividedcalculator(request): 
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if cc == None:
            cc = 1
        return redirect(f'/what-is-negative-{aa}-divided-by-negative-{cc}/')    
 
    else:
        return render(request,"Mathcue/negative-divided-by-negative.html")


def negativeDividedCalculatorDetails(request,aa,cc):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if cc == None:
            cc = 1
        return redirect(f'/what-is-negative-{aa}-divided-by-negative-{cc}/')    
 
    else:
        x = round(aa/cc,4)    
       
        inputEnter=f"{aa},{cc}"
        query=negativeDividedCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:  
                solutionTitle="Negative Divided By Negative Calculator | Free Calculator to find Negative Divided By Negative"
                finalAnswer=f"{x}"
                detailStep=f'''p>See how to find the division of negative numbers - {aa} and - {cc} below</p> <p>-{aa} ÷ -{cc}</p> <p>Divide as if they are normal numbers</p> <p>= <span class="frac"><span>{aa}</span><span class="symbol">/</span><span class="bottom">{cc}</span></span></p> <p>= {x}</p> <p>The sign will be positive as both numbers have the same sign.</p> <br> <p>Therefore, - {aa} ÷ - {cc} is {x}.</p>'''
                obj=negativeDividedCalculator(inputEnter=inputEnter,finalAnswer=finalAnswer,detailStep=detailStep,solutionTitle=solutionTitle,slug="",date_modified=datetime.datetime.now())
                obj.save()

        r1=int(floor(float(aa)))
        r2=int(floor(float(cc)))
        randList1=random_with_N_digits(r1+1,r1+100)
        randList2=random_with_N_digits(r2+1,r2+100)   

        context = {
            'aa':aa,
            'cc':cc,
            'x':x,
            'check':True,
            'id':1,
            'randList1':randList1,
            'randList2':randList2,
        }
        return render(request,"Mathcue/negative-divided-by-negative-details.html", context)
        



def modulocalculator(request):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        return redirect(f'/what-is-{aa}-mod-{cc}/')
    else:
         return render(request,'Mathcue/modulo-calculator.html')


def modulocalculatordetails(request,aa,cc):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        return redirect(f'/what-is-{aa}-mod-{cc}/')
    
    else:
        x = int(float(aa)%float(cc))
        r =int(float(aa)//float(cc)) 
        inputEnter=f"{aa},{cc}"

        query=moduloCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:  
                solutionTitle="Modulo Calculator | Free Calculator to find Modulo"
                finalAnswer=f"{x},{r}"
                detailStep=f'''<p>Solve the given problem what is {aa} mod {cc} by using the modulo calculation. a mod b means we have to divide <span class="frac"><span>a</span><span class="symbol">/</span><span class="bottom">b</span></span></p> <p>In mathematics, the modulo is the remainder or the number that’s left after a number is divided by another value. Modulo is also referred to as ‘mod.’</p> <p>Let us discuss {aa} mod {cc} in detail here.</p> <p><b>Solution:</b></p> <p>If you needed to find {aa} mod {cc}, divide {aa} by {cc}.</p> <ul> <li><p>{aa} mod {cc} = ?</p></li> <li><p>{aa} ÷ {cc} = {r} with a remainder of {x}</p></li> <li><p>{aa} mod {cc} = {x}</p></li> </ul>'''
                obj=moduloCalculator(inputEnter=inputEnter,finalAnswer=finalAnswer,detailStep=detailStep,solutionTitle=solutionTitle,slug="",date_modified=datetime.datetime.now())
                obj.save()
        randList1=random_with_N_digits(int(aa)-100,int(aa)+100)
        randList2=random_with_N_digits(int(cc)-100,int(cc)+100)
        
        context = {
            'aa':aa,
            'cc':cc,
            'x':x,
            'r':r,
            'check':True,
            'id':1,
            'randList1':randList1,
            'randList2':randList2
        }
        return render(request,'Mathcue/modulo-calculator-details.html',context)



def greatestcommondivisorcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        return redirect(f'/find-gcd-of-{aa}-and-{bb}/')    #/dividing-fractions-calculator/ /what-is-2-3-plus-2-5/dividing

    else:
        return render(request,"Deepak/greatest-common-divisor-calculator.html")

def greatestcommondivisor(request,bb,aa):

    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        return redirect(f'/find-gcd-of-{aa}-and-{bb}/')
    
    else:
        lst1 = []
        c = 2
        x = aa
        while(x > 1):
            if(x % c == 0):
                lst1.append(c)
                x = x / c
            else:
                c = c + 1

        lst2 = []
        c = 2
        y = bb
        while(y > 1):
            if(y % c == 0):
                lst2.append(c)
                y = y / c
            else:
                c = c + 1

        ans = math.gcd(aa,bb)
        lcm1 = (aa*bb)//ans

        ab = aa*bb
        #print(ab,lcm1)

        lst5 = []
        for i in range(1,aa+1):
            if (aa%i == 0):
                lst5.append(i)

        lst6 = []
        for i in range(1,bb+1):
            if (aa%i == 0):
                lst6.append(i)
        # print(lst5)
        # print(lst6)

        inputEnter=f"{aa},{bb}"
        query=greatestcommondivisorCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:  
                solutionTitle="Greatest Common divisior Calculator | Free Calculator to find Greatest Common divisior"
                finalAnswer=str(ans)
                detailStep=f'''<p>Solve the given problem to find-gcd-of-{aa}-and-{bb} by using the Greatest Common divisior calculation. By Using the prime factorization method, Given, GCD({aa},{bb}). Prime factors of {aa} = {lst1} and Prime factors of {bb} = {lst2}. The Greatest common divisor, GCD({aa},{bb}) = {ans}</p></li> </ul>'''
                obj=greatestcommondivisorCalculator(inputEnter=inputEnter,finalAnswer=finalAnswer,detailStep=detailStep,solutionTitle=solutionTitle,slug=f'/find-gcd-of-{aa}-and-{bb}/',date_modified=datetime.datetime.now())
                obj.save()

        randList1=random_with_N_digits(1,70)
        randList2=random_with_N_digits(50,110)
        
  

        
        context = {
            'ans':ans,
            'ab':ab,
            'lcm1':lcm1,
            'lst1':lst1,
            'lst2':lst2,
            'lst5':lst5,
            'lst6':lst6,
            'aa':aa,
            'bb':bb,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            #'randomlist2':randomlist2,
            #'randomlist3':randomlist3,
            'id':1,
                }
        return render(request,"Deepak/greatest-common-divisor-calculator-details.html", context)


def howmanyzeroesinquintillioncalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        return redirect(f'/how-many-zeros-in-a-{aa}-quintillion/')    

    else:
        return render(request,"Deepak/how-many-zeroes-in-quintillion-calculator-calculator.html")


def howmanyzeroesinquintillion(request,aa):
    aa = str(aa)

    #x = aa[len(aa)::-1]
    ans = 18
    r = int(float(aa)*(10**18))
    print(r)
    l = str(r)
    ans = 0
    for x in l[:]:
        if x == "0":
            ans = ans+1

    context = {
        'ans':ans,
        'aa':aa,
        'check':True,
        
        'id':1,
            }
    return render(request,"Deepak/how-many-zeroes-in-quintillion-calculator-details.html", context)


def howmanyzeroesingoogolplexcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        return redirect(f'/how-many-zeros-in-a-{aa}-googolplex/')    #/dividing-fractions-calculator/ /what-is-2-3-plus-2-5/dividing

    else:
        return render(request,"Deepak/how-many-zeroes-in-googolplex-calculator-calculator.html")


def howmanyzeroesingoogolplex(request,aa):

    
    aa = str(aa)
    x = aa[len(aa)::-1]
    ans = 18
    for i in x:
        if i == "0":
            ans= ans+1
        else:
            break
    context = {
        'ans':ans,
        'aa':aa,
        'check':True,
       
        'id':1,
            }
    return render(request,"Deepak/how-many-zeroes-in-googolplex-calculator-details.html", context)



def howmanyzeroesinmillioncalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        

        return redirect(f'/how-many-zeros-in-a-{aa}-million/')    

    else:
        return render(request,"Deepak/how-many-zeroes-in-million-calculator.html")


def howmanyzeroesinmillion(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
            
        return redirect(f'/how-many-zeros-in-a-{aa}-million/') 
    else:

        
        
        aa = str(aa)
        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)

        ten = int(float(aa)*100000)
        hun = round(float(float(aa)*10000),1)
        th = round(float(float(aa)*1000),2)
        tt = round(float(float(aa)*100),3)
        ht = round(float(float(aa)*10),4)

        cr = round(float(float(aa)*0.1),6)
        bl = round(float(float(aa)*0.001),8)
        tr = round(float(float(aa)*0.000001),11)

        r = int(float(aa)*(10**6))

        l = str(r)
        ans = 0
        for x in l[:]:
            if x == "0":
                ans = ans+1

        z = int(float(aa))

        list1 = []
        lst1 = []
        sum1 = z
        while sum1 < z+0.25:
            sum1 = round(sum1 +0.01,2)
            list1.append(sum1)
            dd = round(sum1*1000000)
            l = str(dd)
            per1 = 0
            for x in l[:]:
                if x == "0":
                    per1 = per1+1
            lst1.append(per1)

        dict1 = dict(zip(list1, lst1))

        list2 = []
        lst2 = []
        sum2 = z + 0.25
        while sum2 < z+0.50:
            sum2 = round(sum2 +0.01,2)
            list2.append(sum2)
            dd1 = round(sum2*1000000)
            l = str(dd1)
            per2 = 0
            for x in l[:]:
                if x == "0":
                    per2 = per2+1
            lst2.append(per2)
        dict2 = dict(zip(list2, lst2))

        query=millionzerosCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="How Many Zeros in a Million  Calculator makes it easy for you to find How Many Zeros in a Million "
            detailStep=f'''<p>The given number is : {aa} </p> <p>Million is thousand times thousand. In scientific notation we can express million as 1 × 106. In simple terms million is a number that has 6 zeros. . </p> <p>We know 1 Million = 1,000, 000 </p> <p>Let us count how many zeros in {aa} million with detailed explanation. </p> <p>So for {aa} million = {r}. Therefore, {aa} Million have {ans} zeros</p>'''
            finalAnswer=str(ans)
            obj=millionzerosCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/how-many-zeros-in-a-{aa}-million/',date_modified=datetime.datetime.now())
            obj.save()

        words = num2words(r)
        words = words.replace(" and", "")
        words = words.replace(",", "")

        context = {
            'words':words,
            'dict1':dict1,
            'list1':list1,
            'lst1':lst1,
            'dict2':dict2,
            'list2':list2,
            'lst2':lst2,
            'r':r,
            'ans':ans,
            'ten':ten,
            'hun':hun,
            'th':th,
            'tt':tt,
            'ht':ht,
            'cr':cr,
            'bl':bl,
            'tr':tr,
            'aa':aa,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/how-many-zeroes-in-million-calculator-details.html", context)


def howmanyzeroesinbillioncalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/how-many-zeros-in-a-{aa}-billion/')    

    else:
        return render(request,"Deepak/how-many-zeroes-in-billion-calculator.html")


def howmanyzeroesinbillion(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/how-many-zeros-in-a-{aa}-billion/') 
    else:

        

        aa = str(aa)
        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)

        ten = int(float(aa)*100000000)
        hun = round(float(float(aa)*10000000),1)
        th =  round(float(float(aa)*1000000),2)
        tt =  round(float(float(aa)*100000),3)
        ht =  round(float(float(aa)*10000),4)
        mi =  round(float(float(aa)*1000),5)

        cr = round(float(float(aa)*100),6)
        #ml = round(float(float(aa)*1000),8)
        tr = round(float(float(aa)*0.001),7)

        r = int(float(aa)*(10**9))

        l = str(r)
        ans = 0
        for x in l[:]:
            if x == "0":
                ans = ans+1

        z = int(float(aa))

        list1 = []
        lst1 = []
        sum1 = z
        while sum1 < z+0.25:
            sum1 = round(sum1 +0.01,2)
            list1.append(sum1)
            dd = round(sum1*1000000000)
            l = str(dd)
            per1 = 0
            for x in l[:]:
                if x == "0":
                    per1 = per1+1
            lst1.append(per1)

        dict1 = dict(zip(list1, lst1))

        list2 = []
        lst2 = []
        sum2 = z + 0.25
        while sum2 < z+0.50:
            sum2 = round(sum2 +0.01,2)
            list2.append(sum2)
            dd1 = round(sum2*1000000000)
            l = str(dd1)
            per2 = 0
            for x in l[:]:
                if x == "0":
                    per2 = per2+1
            lst2.append(per2)
        dict2 = dict(zip(list2, lst2))

        query=billionzerosCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="How Many Zeros in a Billion  Calculator makes it easy for you to find How Many Zeros in a Billion "
            detailStep=f'''<p>The given number is : {aa} </p> <p>Billion . In scientific notation we can express Billion as 1 × 10^9. In simple terms Billion is a number that has 9 zeros. . </p> <p>We know 1 Billion = 1,000,000,000 </p> <p>Let us count how many zeros in {aa} Billion with detailed explanation. </p> <p>So for {aa} Billion = {r}. Therefore, {aa} Billion have {ans} zeros</p>'''
            finalAnswer=str(ans)
            obj=billionzerosCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/how-many-zeros-in-a-{aa}-billion/' ,date_modified=datetime.datetime.now())
            obj.save()

        words = num2words(r)
        words = words.replace(" and", "")
        words = words.replace(",", "")

        context = {
            'words':words,
            'dict1':dict1,
            'list1':list1,
            'lst1':lst1,
            'dict2':dict2,
            'list2':list2,
            'lst2':lst2,
            'r':r,
            'ans':ans,
            'ten':ten,
            'hun':hun,
            'th':th,
            'tt':tt,
            'ht':ht,
            'mi':mi,
            'aa':aa,
            'cr':cr,
            #'ml':ml,
            'tr':tr,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/how-many-zeroes-in-billion-calculator-details.html", context)



def howmanyzeroesincrorecalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/how-many-zeros-in-a-{aa}-crore/')    

    else:
        return render(request,"Deepak/how-many-zeroes-in-crore-calculator.html")


def howmanyzeroesincrore(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/how-many-zeros-in-a-{aa}-crore/') 
    else:

        aa = str(aa)
        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)

        ten = int(float(aa)*1000000)
        hun =round(float(float(aa)*100000),1)
        th = round(float(float(aa)*10000),3)
        tt = round(float(float(aa)*1000),4)
        ht = round(float(float(aa)*100),5)
        tl = round(float(float(aa)*1),6)
        ml = round(float(float(aa)*10),6)

        bl = round(float(float(aa)*0.01),7)
        tr = round(float(float(aa)*0.00001),11)



        r = int(float(aa)*(10**7))

        l = str(r)
        ans = 0
        for x in l[:]:
            if x == "0":
                ans = ans+1

        z = int(float(aa))

        list1 = []
        lst1 = []
        sum1 = z
        while sum1 < z+0.25:
            sum1 = round(sum1 +0.01,2)
            list1.append(sum1)
            dd = round(sum1*10000000)
            l = str(dd)
            per1 = 0
            for x in l[:]:
                if x == "0":
                    per1 = per1+1
            lst1.append(per1)

        dict1 = dict(zip(list1, lst1))

        list2 = []
        lst2 = []
        sum2 = z + 0.25
        while sum2 < z+0.50:
            sum2 = round(sum2 +0.01,2)
            list2.append(sum2)
            dd1 = round(sum2*10000000)
            l = str(dd1)
            per2 = 0
            for x in l[:]:
                if x == "0":
                    per2 = per2+1
            lst2.append(per2)
        dict2 = dict(zip(list2, lst2))

        query=crorezerosCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="How Many Zeros in a Crore  Calculator makes it easy for you to find How Many Zeros in a Crore "
            detailStep=f'''<p>The given number is : {aa} </p> <p>Crore. In scientific notation we can express Crore as 1 × 10^7. In simple terms Crore is a number that has 7 zeros. . </p> <p>We know 1 Crore = 10,000, 000 </p> <p>Let us count how many zeros in {aa} Crore with detailed explanation. </p> <p>So for {aa} Crore = {r}. Therefore, {aa} Crore have {ans} zeros</p>'''
            finalAnswer=str(ans)
            obj=crorezerosCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/how-many-zeros-in-a-{aa}-crore/',date_modified=datetime.datetime.now())
            obj.save()

        words = num2words(r)
        words = words.replace(" and", "")
        words = words.replace(",", "")


        context = {
            'words':words,
            'dict1':dict1,
            'list1':list1,
            'lst1':lst1,
            'dict2':dict2,
            'list2':list2,
            'lst2':lst2,
            'r':r,
            'ans':ans,
            'ten':ten,
            'hun':hun,
            'th':th,
            'tt':tt,
            'ht':ht,
            'tl':tl,
            'ml':ml,
            'bl':bl,
            'tr':tr,
            'aa':aa,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/how-many-zeroes-in-crore-calculator-details.html", context)


def croreinnumbercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/what-is-{aa}-crore-in-numbers/')    

    else:
        return render(request,"Deepak/crore-in-number-calculator.html")


def croreinnumber(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/what-is-{aa}-crore-in-numbers/') 
    else:

        itr = int(aa)/100

        aa = str(aa)
        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)

        ml = round(float(float(aa)*10),6)
        r = int(float(aa)*(10**7))

        l = str(r)
        ans = 0
        for x in l[:]:
            if x == "0":
                ans = ans+1

        words = num2words(aa)
        words = words.replace(" and", "")
        words = words.replace(",", "")

        query=croreinnumberCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="Crore in number  Calculator makes it easy for you to find how to write number in crore "
            detailStep=f'''<p>The given number is : {aa} Crore</p> <p>We know 1 crore = 10000000 . We represent {aa} crore in the above format as {aa} x 10000000 , So, {aa} crore in words =  {words} crore</p>'''
            finalAnswer=f'''{words} crore'''
            obj=croreinnumberCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-is-{aa}-crore-in-numbers/',date_modified=datetime.datetime.now())
            obj.save()

       


        context = {
            'itr':itr,
            'words':words,
            'r':r,
            'ans':ans,
            'ml':ml,
            'aa':aa,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/crore-in-number-calculator-details.html", context)



def decimaltobinarycalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/how-to-convert-{aa}-to-binary/')    

    else:
        return render(request,"Deepak/decimal-to-binary-calculator.html")


def decimaltobinary(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/how-to-convert-{aa}-to-binary/') 
    else:

        aa = str(aa)
        randList1=random_with_N_digits(10,51)
        randList2=random_with_N_digits(51,110)
        ans = ""

        lst = []
        lst1 = []
        dec = int(aa)
        while dec >0:
            x = dec//2
            z = dec%2
            dec = x
            lst.append(x)
            lst1.append(z)

        y = [int(aa)]+lst[:-1]
        print(y)

        mapped = list(zip(y,lst,lst1))

        lst1.reverse()
        new = lst1
        ans = ""
        for x in new:
            ans = ans+str(x)

        #print(new)
        #print(lst)
        #print(frst)



        query=decimaltobinaryCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="How to convert decimal to binary  Calculator makes it easy for you to find how to convert decimal to binary "
            detailStep=f'''<p>The given number is : {aa} base 10 </p> <p>. Divide the given decimal number by 2 and make a note of the remainder. Again divide the quotient by 2 and note the remainder.Repeat the above steps until you get 0 as the quotient. so {aa} base 10 to binary number is {ans}</p>'''
            finalAnswer=str(ans)
            obj=decimaltobinaryCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/how-to-convert-{aa}-to-binary/',date_modified=datetime.datetime.now())
            obj.save()

        context = {
            'mapped':mapped,
            'y':y,
            'lst':lst,
            'new':new,
            'ans':ans,
            'aa':aa,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/decimal-to-binary-calculator-details.html", context)


def decimalplacevalueCalculator(request):

    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        
        if aa:
            aa1 = float(aa)
            result = math.modf(aa1)
            one = str(int(result[1]))
            two = str(round(result[0],8))
            two = two[2:]
            ans = ["Ones Place", "Tens Place", "Hundreds Place", "Thousands Place",
            "Ten Thousands Place", "Hundred Thousands Place", "Millions Place",
            "Ten Millions Place","Hundred Millions Place","Billions Place"]

            lst1 = []
            if len(one) == 1:
                lst = [ans[0]]
                lst1.append(lst)
            elif len(one) == 2:
                lst = ans[1::-1]
                lst1.append(lst)
            elif len(one) == 3:
                lst = ans[2::-1]
                lst1.append(lst)
            elif len(one) == 4:
                lst = ans[3::-1]
                lst1.append(lst)
            elif len(one) == 5:
                lst = ans[4::-1]
                lst1.append(lst)
            elif len(one) == 6:
                lst = ans[5::-1]
                lst1.append(lst)
            elif len(one) == 7:
                lst = ans[6::-1]
                lst1.append(lst)
            elif len(one) == 8:
                lst = ans[7::-1]
                lst1.append(lst)
            elif len(one) == 9:
                lst = ans[8::-1]
                lst1.append(lst)
            elif len(one) == 10:
                lst = ans[9::-1]
                lst1.append(lst)

            num_list = []
            for x in one[:]:
                num_list.append(int(x))
            num_list.append("●") 
            frst_list = [element for innerList in lst1 for element in innerList] + ["Decimal Point"]

            ans1 = ["Tenths Place", "Hundredths Place", "Thousandths Place", "Ten Thousandths Place",
            "Hundred Thousandths Place", "Millionths Place", "Ten Millionths Place",
            "Hundred Millionths Place"]

            lst2 = []
            if len(two) == 1:
                lst = [ans1[0]]
                lst2.append(lst)
            elif len(two) == 2:
                lst = ans1[0:2]
                lst2.append(lst)
            elif len(two) == 3:
                lst = ans1[0:3]
                lst2.append(lst)
            elif len(two) == 4:
                lst = ans1[0:4]
                lst2.append(lst)
            elif len(two) == 5:
                lst = ans1[0:5]
                lst2.append(lst)
            elif len(two) == 6:
                lst = ans1[0:6]
                lst2.append(lst)
            elif len(two) == 7:
                lst = ans1[0:7]
                lst2.append(lst)
            elif len(two) == 8:
                lst = ans1[0:8]
                lst2.append(lst)


            num_list1 = []
            for x in two[:]:
                num_list1.append(int(x))
            frst_list1 = [element for innerList in lst2 for element in innerList] 

            final_list1 = num_list + num_list1
            final_list2 = frst_list + frst_list1

            mapped = list(zip(final_list1,final_list2))
            #print(mapped)


            context = {
                'mapped':mapped,
                'aa':aa,
                'aa1':aa1,
                'id':1
            }
            return render(request,"Deepak/decimal-place-value-calculator.html", context)
        elif bb:
            bb1 = float(bb)
            result = math.modf(bb1)
            one = str(int(result[1]))
            two = str(round(result[0],8))
            two = two[2:]
            ans = ["1,000,000,000", "100,000,000", "10,000,000", "1,000,000",
                "100,000", "10,000", "1000", "100","10","1"]
            ans = ans[-1::-1]
            lst1 = []
            if len(one) == 1:
                lst = [ans[0]]
                lst1.append(lst)
            elif len(one) == 2:
                lst = ans[1::-1]
                lst1.append(lst)
            elif len(one) == 3:
                lst = ans[2::-1]
                lst1.append(lst)
            elif len(one) == 4:
                lst = ans[3::-1]
                lst1.append(lst)
            elif len(one) == 5:
                lst = ans[4::-1]
                lst1.append(lst)
            elif len(one) == 6:
                lst = ans[5::-1]
                lst1.append(lst)
            elif len(one) == 7:
                lst = ans[6::-1]
                lst1.append(lst)
            elif len(one) == 8:
                lst = ans[7::-1]
                lst1.append(lst)
            elif len(one) == 9:
                lst = ans[8::-1]
                lst1.append(lst)
            elif len(one) == 10:
                lst = ans[9::-1]
                lst1.append(lst)

            num_list = []
            for x in one[:]:
                num_list.append(int(x))
            num_list.append("●") 
            frst_list = [element for innerList in lst1 for element in innerList] + ["Decimal Point"]

            ans1 = ["0.1", "0.01", "0.001", "0.0001",
            "0.00001", "0.000001", "0.0000001", "0.00000001"]

            lst2 = []
            if len(two) == 1:
                lst = [ans1[0]]
                lst2.append(lst)
            elif len(two) == 2:
                lst = ans1[0:2]
                lst2.append(lst)
            elif len(two) == 3:
                lst = ans1[0:3]
                lst2.append(lst)
            elif len(two) == 4:
                lst = ans1[0:4]
                lst2.append(lst)
            elif len(two) == 5:
                lst = ans1[0:5]
                lst2.append(lst)
            elif len(two) == 6:
                lst = ans1[0:6]
                lst2.append(lst)
            elif len(two) == 7:
                lst = ans1[0:7]
                lst2.append(lst)
            elif len(two) == 8:
                lst = ans1[0:8]
                lst2.append(lst)


            num_list1 = []
            for x in two[:]:
                num_list1.append(int(x))
            frst_list1 = [element for innerList in lst2 for element in innerList] 

            final_list1 = num_list + num_list1
            final_list2 = frst_list + frst_list1

            mapped = list(zip(final_list1,final_list2))
            #print(mapped)

            context = {
                'mapped':mapped,
                'bb':bb,
                'bb1':bb1,
                'id2':2
            }
            return render(request,"Deepak/decimal-place-value-calculator.html", context)
        elif cc:
            cc1 = float(cc)
            result = math.modf(cc1)
            one = str(int(result[1]))
            two = str(round(result[0],8))
            two = two[2:]
            ans = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
            lst1 = []
            new = []
            if len(one) == 1:
                lst = [ans[0]]
                lst1.append(lst)
            elif len(one) == 2:
                lst = ans[1::-1]
                lst1.append(lst)
            elif len(one) == 3:
                lst = ans[2::-1]
                lst1.append(lst)
            elif len(one) == 4:
                lst = ans[3::-1]
                lst1.append(lst)
            elif len(one) == 5:
                lst = ans[4::-1]
                lst1.append(lst)
            elif len(one) == 6:
                lst = ans[5::-1]
                lst1.append(lst)
            elif len(one) == 7:
                lst = ans[6::-1]
                lst1.append(lst)
            elif len(one) == 8:
                lst = ans[7::-1]
                lst1.append(lst)
            elif len(one) == 9:
                lst = ans[8::-1]
                lst1.append(lst)
            elif len(one) == 10:
                lst = ans[9::-1]
                lst1.append(lst)
            
            num_list = []
            for x in one[:]:
                num_list.append(int(x))
            dup_lst1 = [element for innerList in lst1 for element in innerList]

            lst3 = []
            for i in range(0, len(dup_lst1)):
                lst3.append(dup_lst1[i] * num_list[i])
            
            last_lst = lst3+["Decimal Point (●)"]
            num_list.append("●") 
            frst_list = [element for innerList in lst1 for element in innerList] + ["Decimal Point"]

            ans1 = [0.1, 0.01, 0.001, 0.0001,
            0.00001, 0.000001, 0.0000001, 0.00000001]

            lst2 = []
            if len(two) == 1:
                lst = [ans1[0]]
                lst2.append(lst)
            elif len(two) == 2:
                lst = ans1[0:2]
                lst2.append(lst)
            elif len(two) == 3:
                lst = ans1[0:3]
                lst2.append(lst)
            elif len(two) == 4:
                lst = ans1[0:4]
                lst2.append(lst)
            elif len(two) == 5:
                lst = ans1[0:5]
                lst2.append(lst)
            elif len(two) == 6:
                lst = ans1[0:6]
                lst2.append(lst)
            elif len(two) == 7:
                lst = ans1[0:7]
                lst2.append(lst)
            elif len(two) == 8:
                lst = ans1[0:8]
                lst2.append(lst)


            num_list1 = []
            for x in two[:]:
                num_list1.append(int(x))
            frst_list1 = [element for innerList in lst2 for element in innerList]

            lst4 = []
            for i in range(0, len(frst_list1)):
                lst4.append(round(frst_list1[i] * num_list1[i],9))
                        

            final_list1 = num_list + num_list1
            final_list2 = frst_list + frst_list1
            final_list3 = last_lst + lst4            

            mapped = list(zip(final_list1,final_list2,final_list3))

            context = {
                'mapped':mapped,
                'cc':cc,
                'cc1':cc1,
                'id3':3
            }
            return render(request,"Deepak/decimal-place-value-calculator.html", context)

        query=decimalplacevalueCalculator.objects.filter(inputEnter=str(cc))
        if len(query)==0:
            solutionTitle="Decimal Place Value Calculator makes it easy for you to find how to find Decimal Place Value."
            detailStep=f'''<p>The given number is : {cc} </p> <p>The total value of each digit in the number is each digit multiplied by its decimal place value. {final_list3}</p>'''
            finalAnswer={final_list3}
            obj=decimalplacevalueCalculator(inputEnter=str(cc),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f"/decimal-place-value-calculator/",date_modified=datetime.datetime.now())
            obj.save()        

        
        context = {
            'aa':aa,
            'bb':bb,
            'cc':cc,
           
            
            }

        return render(request,"Deepak/decimal-place-value-calculator.html", context)
    
    else:
        return render(request,"Deepak/decimal-place-value-calculator.html")



def addingfractioncalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('dd')!=None and request.POST.get('dd')!='' :
            inp=str(request.POST.get('dd'))
            if inp.isdigit(): 
                dd=int(request.POST.get('dd'))
            else:
                dd=float(request.POST.get('dd'))
        else:
            dd=None

        if dd == None:
            dd = 1

        return redirect(f'/what-is-{aa}-{cc}-plus-{bb}-{dd}/')    

    else:
        return render(request,"Deepak/adding-fractions-calculator.html")


def addingfraction(request,aa,bb,cc,dd):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('dd')!=None and request.POST.get('dd')!='' :
            inp=str(request.POST.get('dd'))
            if inp.isdigit(): 
                dd=int(request.POST.get('dd'))
            else:
                dd=float(request.POST.get('dd'))
        else:
            dd=None

        if dd == None:
            dd = 1
        return redirect(f'/what-is-{aa}-{cc}-plus-{bb}-{dd}/') 
    else:


        lc = math.lcm(cc,dd)
        #print(lc)
        f = int(lc/cc)
        f1 = int(lc/dd)

        m = aa*f 
        m1 = bb*f1

        x = m+m1

        from math import gcd
    
        d = gcd(x, lc);

        p = x // d;
        q = lc // d;
        

        print(p,q)

        ans = 0
        randList1=random_with_N_digits(1,30)
        randList2=random_with_N_digits(30,60) 
        randList5=random_with_N_digits(10,50)
        randList6=random_with_N_digits(50,100)   
        list1 = list(zip(randList1,randList2,randList5,randList6)) 

        randList3=random_with_N_digits(10,50)
        randList4=random_with_N_digits(1,30)
        randList7=random_with_N_digits(50,100)
        randList8=random_with_N_digits(35,90)   
        list2 = list(zip(randList3,randList4,randList7,randList8))    

        query=addingfractionCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="what is {aa} crore in number  Calculator makes it easy for you to find how to write number in crore "
            detailStep=f'''<p>The given number is : {aa} </p> <p>Crore. We know that 1 crore = 100 lakhs and 1 lakh = 1,00,000. So, 1 crore = . Thus, the number of zeros in a {aa} crore is {ans}</p>'''
            finalAnswer=str(ans)
            obj=addingfractionCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug="crore-in-numbers-calculator",date_modified=datetime.datetime.now())
            obj.save()

       
        context = {
            'p':p,
            'q':q,
            #'y':y,
            'f':f,
            'f1':f1,
            'm1':m1,
            'm':m,
            'aa':aa,
            'bb':bb,
            'cc':cc,
            'dd':dd,
            'lc':lc,
            'x':x,
            'check':True,
            'id':1,
            'list1':list1,
            'list2':list2,
            'id':1,
                }
        return render(request,"Deepak/adding-fractions-calculator-details.html", context)


def multiplyingfractioncalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('dd')!=None and request.POST.get('dd')!='' :
            inp=str(request.POST.get('dd'))
            if inp.isdigit(): 
                dd=int(request.POST.get('dd'))
            else:
                dd=float(request.POST.get('dd'))
        else:
            dd=None

        if dd == None:
            dd = 1

        return redirect(f'/what-is-{aa}-{cc}-times-{bb}-{dd}/')    

    else:
        return render(request,"Deepak/multiplying-fractions-calculator.html")


def multiplyingfraction(request,aa,bb,cc,dd):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('dd')!=None and request.POST.get('dd')!='' :
            inp=str(request.POST.get('dd'))
            if inp.isdigit(): 
                dd=int(request.POST.get('dd'))
            else:
                dd=float(request.POST.get('dd'))
        else:
            dd=None

        if dd == None:
            dd = 1
        return redirect(f'/what-is-{aa}-{cc}-times-{bb}-{dd}/') 
    else:

        x = aa*bb
        y = cc*dd

        from math import gcd
    
        d = gcd(x, y);

        p = x // d;
        q = y // d;

        ans = 0
        randList1=random_with_N_digits(1,30)
        randList2=random_with_N_digits(30,60) 
        randList5=random_with_N_digits(10,50)
        randList6=random_with_N_digits(50,100)   
        list1 = list(zip(randList1,randList2,randList5,randList6)) 

        randList3=random_with_N_digits(10,50)
        randList4=random_with_N_digits(1,30)
        randList7=random_with_N_digits(50,100)
        randList8=random_with_N_digits(35,90)   
        list2 = list(zip(randList3,randList4,randList7,randList8))        

        query=multiplyingfractionCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="what is {aa} crore in number  Calculator makes it easy for you to find how to write number in crore "
            detailStep=f'''<p>The given number is : {aa} </p> <p>Crore. We know that 1 crore = 100 lakhs and 1 lakh = 1,00,000. So, 1 crore = . Thus, the number of zeros in a {aa} crore is {ans}</p>'''
            finalAnswer=str(ans)
            obj=multiplyingfractionCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug="crore-in-numbers-calculator",date_modified=datetime.datetime.now())
            obj.save()


        context = {
            'aa':aa,
            'bb':bb,
            'cc':cc,
            'dd':dd,
            'x':x,
            'y':y,
            'p':p,
            'q':q,
            'check':True,
            'id':1,
            'list1':list1,
            'list2':list2,
            'id':1,
                }
        return render(request,"Deepak/multiplying-fractions-calculator-details.html", context)


def dividingfractioncalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('dd')!=None and request.POST.get('dd')!='' :
            inp=str(request.POST.get('dd'))
            if inp.isdigit(): 
                dd=int(request.POST.get('dd'))
            else:
                dd=float(request.POST.get('dd'))
        else:
            dd=None

        if dd == None:
            dd = 1

        return redirect(f'/what-is-{aa}-{cc}-divided-by-{bb}-{dd}/')    

    else:
        return render(request,"Deepak/dividing-fractions-calculator.html")


def dividingfraction(request,aa,bb,cc,dd):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('dd')!=None and request.POST.get('dd')!='' :
            inp=str(request.POST.get('dd'))
            if inp.isdigit(): 
                dd=int(request.POST.get('dd'))
            else:
                dd=float(request.POST.get('dd'))
        else:
            dd=None

        if dd == None:
            dd = 1
        return redirect(f'/what-is-{aa}-{cc}-divided-by-{bb}-{dd}/') 
    else:

        x = (aa*dd)
        y = (cc*bb)

        from math import gcd
    
        d = gcd(x, y);

        p = x // d;
        q = y // d;

        z = round(p/q,4)

        ans = 0
        randList1=random_with_N_digits(1,30)
        randList2=random_with_N_digits(30,60) 
        randList5=random_with_N_digits(10,50)
        randList6=random_with_N_digits(50,100)   
        list1 = list(zip(randList1,randList2,randList5,randList6)) 

        randList3=random_with_N_digits(10,50)
        randList4=random_with_N_digits(1,30)
        randList7=random_with_N_digits(50,100)
        randList8=random_with_N_digits(35,90)   
        list2 = list(zip(randList3,randList4,randList7,randList8))  

        query=dividingfractionCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="what is {aa} crore in number  Calculator makes it easy for you to find how to write number in crore "
            detailStep=f'''<p>The given number is : {aa} </p> <p>Crore. We know that 1 crore = 100 lakhs and 1 lakh = 1,00,000. So, 1 crore = . Thus, the number of zeros in a {aa} crore is {ans}</p>'''
            finalAnswer=str(ans)
            obj=dividingfractionCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug="crore-in-numbers-calculator",date_modified=datetime.datetime.now())
            obj.save()


        context = {
            'z':z,
            'aa':aa,
            'bb':bb,
            'cc':cc,
            'dd':dd,
            'x':x,
            'y':y,
            'p':p,
            'q':q,
            'check':True,
            'id':1,
            'list1':list1,
            'list2':list2,
            'id':1,
                }
        return render(request,"Deepak/dividing-fractions-calculator-details.html", context)


def mixedfractioncalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None


        return redirect(f'/{aa}-{cc}-as-a-mixed-fraction/')    

    else:
        return render(request,"Deepak/mixed-fractions-calculator.html")


def mixedfraction(request,aa,cc):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        return redirect(f'/{aa}-{cc}-as-a-mixed-fraction/') 
    else:

        q = (int(aa))// (int(cc))
        r = (int(aa) )% (int(cc))

        ans = 0
        randList1=random_with_N_digits(10,70)
        randList2=random_with_N_digits(5,100)    
        list1 = list(zip(randList1,randList2)) 

        randList3=random_with_N_digits(5,50)
        randList4=random_with_N_digits(10,100)
         
        list2 = list(zip(randList3,randList4))  

        inputEnter=f"{aa} and {cc}"
        query=mixedfractionCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="Mixed fraction Calculator makes it easy for you to find how to write Mixed fraction "
            detailStep=f'''<p>The given number is : {aa} by {cc} </p> <p>Divide the numerator by the denominator. Write down the quotient as the whole number. Write down the remainder as the numerator and the divisor as the denominator. Therefor, {aa} by {cc} written as mixed fraction in {q} x {r} by {cc}.</p>'''
            finalAnswer=f'''{q} x {r} by {cc}'''
            obj=mixedfractionCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f"/{aa}-{cc}-as-a-mixed-fraction/",date_modified=datetime.datetime.now())
            obj.save()


        context = {
            'aa':aa,
            'cc':cc,
            'q':q,
            'r':r,
            'check':True,
            'id':1,
            'list1':list1,
            'list2':list2,
            'id':1,
                }
        return render(request,"Deepak/mixed-fractions-calculator-details.html", context)


def threedigitnumbercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/3-digit-number-divisible-by-{aa}/')    

    else:
        return render(request,"Deepak/three-digit-number-divisible-calculator.html")


def threedigitnumber(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/3-digit-number-divisible-by-{aa}/') 
    else:

        lst1 = []
        for i in range(100,1000):
            if i%aa==0:
                lst1.append(i)

        c = len(lst1)
        one = lst1[0]
        length = len(lst1)
        two = 0
        if len(lst1)>1:
            two = two+lst1[1]
        else:
            two = 0
        l = lst1[-1]

        sum = 0
        for x in lst1:
            sum = sum+x
        ans = 0

        randList1=random_with_N_digits(10,51)
        randList2=random_with_N_digits(51,110)

        query=threedigitnumberCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="Three digit number divisible by Calculator makes it easy for you to find Three digit number divisible by"
            detailStep=f'''<p>The given number is : {aa}  </p> <p>List the three-digit numbers range i.e 100 to 999.Then, using the number divisibility rule, find the first 3-digit number divisible by the given number.Simply add the given number to the first number to get the second number. The 3-digit numbers divisible by {aa} is {lst1}.</p>'''
            finalAnswer=(lst1)
            obj=threedigitnumberCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f"/3-digit-number-divisible-by-{aa}/",date_modified=datetime.datetime.now())
            obj.save()


        context = {
            'length':length,
            'aa':aa,
            'lst1':lst1,
            'one':one,
            'l':l,
            'two':two,
            'sum':sum,
            'c':c,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/three-digit-number-divisible-calculator-details.html", context)


def fourdigitnumbercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/4-digit-number-divisible-by-{aa}/')    

    else:
        return render(request,"Deepak/four-digit-number-divisible-calculator.html")


def fourdigitnumber(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/4-digit-number-divisible-by-{aa}/') 
    else:

        lst1 = []
        for i in range(1000,10000):
            if i%aa==0:
                lst1.append(i)

        c = len(lst1)
        length = len(lst1)
        one = lst1[0]
        two = 0
        if len(lst1)>1:
            two = two+lst1[1]
        else:
            two = 0
        
        l = lst1[-1]

        sum = 0
        for x in lst1:
            sum = sum+x
        ans = 0

        randList1=random_with_N_digits(10,51)
        randList2=random_with_N_digits(51,110)

        query=fourdigitnumberCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="Four Digit Numbers Divisible By Calculator makes it easy for you to find Four Digit Numbers Divisible By"
            detailStep=f'''<p>The given number is : {aa}  </p> <p> List out the 4-digit numbers ranging from 1000 to 9999. From all the four-digit whole numbers, get the lowest number that is divisible by the given number. Then add the given number to the lowest number to get the second number.The 4-digit numbers divisible by {aa} is {lst1}.</p>'''
            finalAnswer=(lst1)
            obj=fourdigitnumberCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f"/4-digit-number-divisible-by-{aa}/",date_modified=datetime.datetime.now())
            obj.save()


        context = {
            'length':length,
            'aa':aa,
            'lst1':lst1,
            'one':one,
            'l':l,
            'two':two,
            'sum':sum,
            'c':c,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/four-digit-number-divisible-calculator-details.html", context)


def whatisnextfibonaccicalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            aa=request.POST.get('aa')
            
        else:
            aa=None

        try:
        #lst = aa.split(",")
            lst = [int(i) for i in aa.split(",")]
            #print(lst, "New list")
            
        except:
            context = {
            'aa':aa,
            'messages': "Invalid Input",
            }
            return render(request,'Deepak/what-is-nextfibonacci-series-number-calculator.html', context)

        out1 = []

        for i in lst:
            phi=0.5+0.5*math.sqrt(5.0)
            a=phi*i
            out =[ i == 0 or abs(round(a) - a) < 1.0 / i];
            out1.append(out)
        
        for x in out1:
            if x == [False]:
                context = {
                'aa':aa,
                'messages': "Please enter valid Fibonacci Number",
                }
                return render(request,'Deepak/what-is-nextfibonacci-series-number-calculator.html', context)
        return redirect(f'/what-is-the-next-fibonacci-number-in-following-sequence-{aa}/')   

    else:
        return render(request,"Deepak/what-is-nextfibonacci-series-number-calculator.html")


def whatisnextfibonacci(request,aa):
    
    # try:
    #     lst = [int(i) for i in aa.split(",")]            
    # except:
    #     context = {
    #     'aa':aa,
    #     'messages': "Invalid Input",
    #     }
    #     return render(request,'Deepak/what-is-nextfibonacci-series-number-calculator.html', context)

    # lst = [int(i) for i in aa.split(",")]
    # out1 = []
    # for i in lst:
    #     phi=0.5+0.5*math.sqrt(5.0)
    #     a=phi*i
    #     out =[ i == 0 or abs(round(a) - a) < 1.0 / i];
    #     out1.append(out)
    
    # for x in out1:
    #     if x == [False]:
    #         context = {
    #         'aa':aa,
    #         'messages': "Please enter valid Fibonacci Number",
    #         }
    #         return render(request,'Deepak/what-is-nextfibonacci-series-number-calculator.html', context)

    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            aa=request.POST.get('aa')
            
        else:
            aa=None
        
        

        try:
            lst = [int(i) for i in aa.split(",")]   
        except:
            context = {
            'aa':aa,
            'messages': "Invalid Input",
            }
            #print(context)
            return render(request,'Deepak/what-is-nextfibonacci-series-number-calculator.html', context)
       
        return redirect(f'/what-is-the-next-fibonacci-number-in-following-sequence-{aa}/')
    else:
        
        lst = [int(i) for i in aa.split(",")]
        ls = lst[-1]
        ss = lst[-2]

        ans = ls+ss

        l1 = lst[2:]
        l2 = lst[1:len(lst)-1]
        l3 = lst[0:len(lst)-2]

        mapped = list(zip(l1,l2,l3))
        #ans = 0

        randList1=random_with_N_digits(10,51)
        randList2=random_with_N_digits(51,110)

        query=whatisnextfibonacciCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is the next Fibonacci series number. Calculator makes it easy for you to find What is the next Fibonacci series number."
            detailStep=f'''<p>The given number is : {aa} .</p> <p>. The Fibonacci Sequence is a set of numbers such that each number in the sequence is the sum of the two numbers that immediatly preceed it.F0 = 0, F1 = F2 = 1 and Fn = Fn-1 + Fn-2. Now, Let us find the next Fibonacci Number {aa}, i.e. the next Fibonacci number in the following sequence is {ans}</p>'''
            finalAnswer=str(ans)
            obj=whatisnextfibonacciCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f"/what-is-the-next-fibonacci-number-in-following-sequence-{aa}/",date_modified=datetime.datetime.now())
            obj.save()


        context = {
            'ls':ls,
            'ss':ss,
            'aa':aa,
            'l1':l1,
            'l2':l2,
            'l3':l3,
            'lst':lst,
            'ans':ans,
            'mapped':mapped,       
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/what-is-nextfibonacci-series-number-calculator-details.html", context)




def howdoyouaddpercenttonumbercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        # if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
        #     inp=str(request.POST.get('bb'))
        #     if inp.isdigit(): 
        #         bb=int(request.POST.get('bb'))
        #     else:
        #         bb=float(request.POST.get('bb'))
        # else:
        #     bb=None
        
        # if aa:
        #     return redirect(f'/how-do-you-add-{aa}-percent-to-a-number/') 
        # else:
        #     return redirect(f'/what-is-{bb}-plus-{aa}-percent/') 

        return redirect(f'/how-do-you-add-{aa}-percent-to-a-number/')

    else:
        return render(request,"Deepak/how-do-you-add-percent-to-number-calculator.html")


def howdoyouaddpercenttonumber(request,aa):
    aa = aa
    if request.method == 'POST':
        print(request.method )
        # if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
        #     inp=str(request.POST.get('aa'))
        #     if inp.isdigit(): 
        #         aa=int(request.POST.get('aa'))
        #     else:
        #         aa=float(request.POST.get('aa'))
        # else:
        #     aa=None
       
        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        print(aa)
        

        # if aa:
        #     return redirect(f'/how-do-you-add-{aa}-percent-to-a-number/') 
        # else:
        print(f'/what-is-{bb}-plus-{aa}-percent/')
        return redirect(f'/what-is-{bb}-plus-{aa}-percent/') 
    else:
  
        ans = 0
        xy = round(aa/100,4)
        xy1 = round(xy + 1,4)
        xy2 = round(xy1*150,4)
        xy3 = round(54.3*xy1,5)
        xy4 = round(54.3+(xy*54.3),5)

        randList1=random_with_N_digits(10,51)
        randList2=random_with_N_digits(51,110)

        

        query=howdoyouaddpercenttonumberCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            bb = 0
            solutionTitle="How do You add percent to number Calculator makes it easy for you to find How do You add percent to number"
            detailStep=f'''<p>The given number is : {aa} percent and {bb} number.  </p> <p>If you want to add a y % to an x number, then the formula to find it is given as ,Total = x + (( y / 100) * x ). Where, X = Given number. Y = Given percent value. {aa} by 100 + 1 = {xy1}.  </p>'''
            finalAnswer=(xy1)
            obj=howdoyouaddpercenttonumberCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/how-do-you-add-{aa}-percent-to-a-number/',date_modified=datetime.datetime.now())
            obj.save()

        
        context = {
            'xy':xy,
            'xy1':xy1,
            'xy2':xy2,
            'xy3':xy3,
            'xy4':xy4,
            'aa':aa,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/how-do-you-add-percent-to-number-calculator-details.html", context)


def howdoyouaddpercenttonumber1(request,aa,bb):
    
    # print("aa",aa)
    # print("bb",bb)
    if request.method == 'POST':
        
        #aa == aa

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        #print(aa)

        return redirect(f'/what-is-{bb}-plus-{aa}-percent/') 
    else:

        ab = int(float(aa) * float(bb))
        ba = ab / 100
        ans = round((float(bb) + float(ba)),4)

        if "." not in bb:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in bb:
            n = len(str(bb).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)

        # randList1=random_with_N_digits(10,51)
        # randList2=random_with_N_digits(51,110)
        #ans = 0
        num = round((int(aa)/100) * float(bb), 4)

        list1 = []
        lst1 = []
        for x in range(1,51):
            list1.append(x)
            dif = round(float(bb) * round(((x/100)+1),5),4)
            lst1.append(dif)
            #print(x,dif)
        dict1 = dict(zip(lst1, list1))
       
        #####
        list2 = []
        lst2 = []
        for x in range(51,101):
            list2.append(x)
            dif = round(float(bb) * round(((x/100)+1),5),4)
            lst2.append(dif)
        dict2 = dict(zip(lst2, list2))


        context = {
            'ab':ab,
            'ba':ba,
            'ans':ans,
            'aa':aa,
            'bb':bb,
            'num':num,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'dict1':dict1,
            'dict2':dict2,
            'id':1,
                }
        #print(context)
        return render(request,"Deepak/how-do-you-add-percent-to-number-calculator-details-1.html", context)



def onedecimalplacecalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/what-is-{aa}-to-1-decimal-place/')    

    else:
        return render(request,"Deepak/one-decimal-place-calculator.html")


def onedecimalplace(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/what-is-{aa}-to-1-decimal-place/') 
    else:

        aa1 = float(aa)
        ans = round(float(aa), 1)
        # n = len(str(aa1).split(".")[1])
        # print("Hello",n)

        # def random_with_N_digits2(range_start,range_end):
        #     l1=[]
        #     present=dict()
        #     for i in range(0,5):
        #         temp=round(random.uniform(range_start, range_end), int(n))
        #         if temp not in present.keys():
        #                 l1.append(temp)
        #                 present[temp]=1
                    
        #     return l1   

        # randList1=random_with_N_digits2(10,51)
        # randList2=random_with_N_digits2(51,110)

        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)

        query=onedecimalplaceCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="One decimal place value Calculator makes it easy for you to find One decimal place value"
            detailStep=f'''<p>The given number is : {aa}  </p> <p>What is {aa} to 1 decimal place value. To round to one decimal place we will look at the hundredths place digit. Therefore, {aa} rounded to 1 decimal place is {ans}</p>'''
            finalAnswer=(ans)
            obj=onedecimalplaceCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-is-{aa}-to-1-decimal-place/',date_modified=datetime.datetime.now())
            obj.save()

        context = {
            'ans':ans,
            'aa':aa,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/one-decimal-place-calculator-details.html", context)


def percentofwhatnumbercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        return redirect(f'/{aa}-is-{bb}-percent-of-what-number/')    

    else:
        return render(request,"Deepak/percent-of-what-number-calculator.html")


def percentofwhatnumber(request,aa,bb):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        return redirect(f'/{aa}-is-{bb}-percent-of-what-number/') 
    else:

        ans = round((aa*100)/bb,4)
        xy = round(bb/100  ,2)
        randList=random_with_N_digits(10,100)
        randList1=random_with_N_digits(10,50)
        dict1 = list(zip(randList,randList1))

        randList3=random_with_N_digits(50,151)
        randList2=random_with_N_digits(51,110)
        dict2 = list(zip(randList3,randList2))

        list1 = []
        lst1 = []
        for x in range(1,51):
            list1.append(x)
            dif = round(aa/(x/100),2)
            lst1.append(dif)
            #print(x,dif)
        new1 = dict(zip(lst1, list1))
       
        #####
        list2 = []
        lst2 = []
        for x in range(51,101):
            list2.append(x)
            dif = round(aa/(x/100),2)
            lst2.append(dif)
        new2 = dict(zip(lst2, list2))

        inputEnter = f'{aa} and {bb}'
        query=percentofwhatnumberCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="Percent of what number Calculator makes it easy for you to find Percent of what number"
            detailStep=f'''<p>The given number is : {aa} and {bb} percent.  </p> <p>To calculate percent of what number simplified formula to find the % of what number concept: X = (Number x 100) / Percent. {aa} is the result of {bb} percent of a number (x), i.e., {bb}% of x = {aa}. Hence, the {bb}% of {ans} is {aa}.</p>'''
            finalAnswer=(ans)
            obj=percentofwhatnumberCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/{aa}-is-{bb}-percent-of-what-number/',date_modified=datetime.datetime.now())
            obj.save()

        context = {
            'ans':ans,
            'aa':aa,
            'bb':bb,
            'xy':xy,
            'check':True,
            'dict1':dict1,
            'dict2':dict2,
            'new1':new1,
            'new2':new2,
            'id':1,
                }
        return render(request,"Deepak/percent-of-what-number-calculator-details.html", context)


def rationalnumbercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/is-{aa}-a-rational-number/')    

    else:
        return render(request,"Deepak/rational-number-calculator.html")


def rationalnumber(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/is-{aa}-a-rational-number/') 
    else:
        aa1 = float(aa)
        n = len(str(aa1).split(".")[1])
        x = int("1"+"0"*n)
        
        xy = int(aa1*x)
        ans = "Yes"

        if "." not in aa:
            randList=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)

        # randList=random_with_N_digits1(10,100)
        # randList2=random_with_N_digits1(10,151)
       

        query=rationalnumberCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="Rational number Calculator makes it easy for you to find Rational number"
            detailStep=f'''<p>The given number is : {aa} .  </p> <p>We know that the number expressed in a fractional form ie p/q. is a rational number. Here {aa} is similar to {aa} over 1.ie. {aa}/1. ({aa1} x {x}) / (1 x {x}) = {xy} / {x}. So Yes it is rational Number.</p>'''
            finalAnswer=(ans)
            obj=rationalnumberCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/is-{aa}-a-rational-number/',date_modified=datetime.datetime.now())
            obj.save()

        context = {
            'ans':ans,
            'aa':aa,
            'aa1':aa1,
            'x':x,
            'xy':xy,
            'check':True,
            'randList':randList,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/rational-number-calculator-details.html", context)


def whattwonumberadduptocalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/what-two-numbers-add-up-to-{aa}/')    

    else:
        return render(request,"Deepak/numbers-that-add-up-to-calculator.html")


def whattwonumberaddupto(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/what-two-numbers-add-up-to-{aa}/') 
    else:
        nlst1 = [-1,-2,-3,-4,-5]
        nlst2 = [-6,-7,-8,-9,-10]
        lst1 = []
        for x in range(1,6):
            y = x+aa
            lst1.append(y)
        lst2 = []
        for x in range(6,11):
            y = x+aa
            lst2.append(y)
        dict1 = list(zip(nlst1, lst1))
        dict2 = list(zip(nlst2, lst2))

        slst1 = [2,3,4,5,6]
        flst1 = []
        for x in range(aa,(aa*6),aa):
            flst1.append(x)
        slst2 = [7,8,9,10,11]
        flst2 = []
        for x in range((aa*6),(aa*11),aa):
            flst2.append(x)
        dict3 = list(zip(flst1, slst1))
        dict4 = list(zip(flst2, slst2))

        dlst1 = [1.25, 2.50, 3.75, 5.00, 6.25]
        mlst1 = [(aa-1.25), (aa-2.50), (aa-3.75), (aa-5.00), (aa-6.25)]
        dlst2 = [7.50, 8.75, 10.00, 11.25, 12.50]
        mlst2 = [(aa-7.50), (aa-8.75), (aa-10.00), (aa-11.25), (aa-12.50)]
        dict5 = list(zip(dlst1, mlst1))
        dict6 = list(zip(dlst2, mlst2))

        alst1 = []
        slst1 = []
        p = aa
        for x in range(1,11):
            alst1.append(x)
            p = p-1
            slst1.append(p)
        alst2 = []
        slst2 = []
        p = aa-10
        for x in range(11,21):
            alst2.append(x)
            p = p-1
            slst2.append(p)
        dict7 = list(zip(alst1, slst1))
        dict8 = list(zip(alst2, slst2))
        
        xy = aa-10
        fl = aa//2
        sm = aa-6

        randList=random_with_N_digits(10,100)
        randList2=random_with_N_digits(10,151)
        ans = 0

        query=whattwonumberadduptoCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="Rational number Calculator makes it easy for you to find Rational number"
            detailStep=f'''<p>The given number is : {aa} .  </p> <p> </p>'''
            finalAnswer=(ans)
            obj=whattwonumberadduptoCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-two-numbers-add-up-to-{aa}/',date_modified=datetime.datetime.now())
            obj.save()

        context = {
            'dict1':dict1,
            'dict2':dict2,
            'dict3':dict3,
            'dict4':dict4,
            'dict6':dict6,
            'dict5':dict5,
            'dict7':dict7,
            'dict8':dict8,
            'ans':ans,
            'aa':aa,
            'sm':sm,
            'fl':fl,
            'xy':xy,
            'check':True,
            'randList':randList,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/numbers-that-add-up-to-calculator-details.html", context)




def sequentialpercentagecalculator(request):
     
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if request.POST.get('nm')!=None and request.POST.get('nm')!='' :
            inp=str(request.POST.get('nm'))
            if inp.isdigit(): 
                nm=int(request.POST.get('nm'))
            else:
                nm=float(request.POST.get('nm'))
        else:
            nm=None

        aa_op=request.POST.get('aa_op')
        bb_op=request.POST.get('bb_op')
        
        return redirect(f'/a-number-{nm}-is-{aa_op}-by-{aa}%-and-then-{bb_op}-by-{bb}%/') 

    else:
        return render(request,"Deepak/sequential-percentage-calculator.html")


def sequentialpercentage(request,aa,bb,nm,aa_op,bb_op):
    aa_op=aa_op
    bb_op=bb_op
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if request.POST.get('nm')!=None and request.POST.get('nm')!='' :
            inp=str(request.POST.get('nm'))
            if inp.isdigit(): 
                nm=int(request.POST.get('nm'))
            else:
                nm=float(request.POST.get('nm'))
        else:
            nm=None

        aa_op=request.POST.get('aa_op')
        bb_op=request.POST.get('bb_op')

        return redirect(f'/a-number-{nm}-is-{aa_op}-by-{aa}%-and-then-{bb_op}-by-{bb}%/')         

    else:
        xy = ""
        p1 = ""
        if aa_op == "increased":
            a1 = +aa
            p1 = round((aa/100)*float(nm),2)
            xy = round(float(nm)+(p1),2)
        else:
            a1 = -aa
            p1 = round((aa/100)*float(nm),2)
            xy = round(float(nm)-(p1),2)

        yx = ""
        p2 = ""
        if bb_op == "increased":
            b1 = +bb
            p2 = round((bb/100)*float(xy),2)
            yx = round(float(xy)+(p2),2)
        else:
            b1 = -bb
            p2 = round((bb/100)*float(xy),2)
            yx = round(float(xy)-(p2),2)
        ans = a1+b1
        x1 = int(float(nm) - float(yx))
        
        add = ""
        if x1 < 0:
            add = "Profit"
        else:
            add = "Loss"

        x2 = abs(x1)
        ad = round((x2/float(nm))*100,2)   
        inputEnter = f"number = {nm}, {aa_op} by {aa}% and then {bb_op} by {bb}%"
        query=sequentialpercentageCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="what is Sequential Percentage  Calculator makes it easy for you to find how to write Sequential Percentage "
            detailStep=f'''<p>The given number is : {inputEnter} .</p> <p>A number {nm} is {aa_op} by {aa}% and then {bb_op} by {bb}%.. So, {nm} is {aa_op} by {aa}% i.e, {xy} and then {xy} {bb_op} by {bb}% is {yx} </p>'''
            finalAnswer=str(ans)
            obj=sequentialpercentageCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/a-number-{nm}-is-{aa_op}-by-{aa}%-and-then-{bb_op}-by-{bb}%/',date_modified=datetime.datetime.now())
            obj.save()


        randList1 = []
        for i in range(aa+1,aa+7):
            randList1.append(i)
        if "." not in nm:
            randList2=random_with_N_digits(100,500)
        if "." in nm:
            n = len(str(nm).split(".")[1])
            randList2=random_with_N_digits1(100,500,n)
        dict1 = list(zip(randList2,randList1))

        randList5 = []
        for i in range(bb+1,bb+7):
            randList5.append(i)
        if "." not in nm:
            randList4=random_with_N_digits(100,500)
        if "." in nm:
            n = len(str(nm).split(".")[1])
            randList4=random_with_N_digits1(100,500,n)
        dict2 = list(zip(randList4,randList5))


        lst1 = []
        lst2 = []
        lst3 = []
        if aa_op == "increased":
            for x in range(1,51):
                lst1.append(x)
                p1 = round(float(nm)+(x/100)*float(nm),2)
                lst2.append(p1)
                if bb_op == "increased":
                    p2 = round(float(p1)+(bb/100)*float(p1),2)
                    lst3.append(p2)
                else:
                    p2 = round(float(p1)-(bb/100)*float(p1),2)
                    lst3.append(p2)
           
        else:
            for x in range(1,51):
                lst1.append(x)
                p1 = round(float(nm)-(x/100)*float(nm),2)
                lst2.append(p1)
                if bb_op == "increased":
                    p2 = round(float(p1)+(bb/100)*float(p1),2)
                    lst3.append(p2)
                else:
                    p2 = round(float(p1)-(bb/100)*float(p1),2)
                    lst3.append(p2)
            

        lst4 = []
        lst5 = []
        lst6 = []
        if aa_op == "increased":
            for x in range(51,101):
                lst4.append(x)
                p1 = round(float(nm)+(x/100)*float(nm),2)
                lst5.append(p1)
                if bb_op == "increased":
                    p2 = round(float(p1)+(bb/100)*float(p1),2)
                    lst6.append(p2)
                else:
                    p2 = round(float(p1)-(bb/100)*float(p1),2)
                    lst6.append(p2)
           
        else:
            for x in range(51,101):
                lst4.append(x)
                p1 = round(float(nm)-(x/100)*float(nm),2)
                lst5.append(p1)
                if bb_op == "increased":
                    p2 = round(float(p1)+(bb/100)*float(p1),2)
                    lst6.append(p2)
                else:
                    p2 = round(float(p1)-(bb/100)*float(p1),2)
                    lst6.append(p2)

        new1 = list(zip(lst1,lst2,lst3))
        new2 = list(zip(lst4,lst5,lst6))


        
        context = {
            'add':add,
            'ans':ans,
            'ad':ad,
            'aa':aa,
            'bb':bb,
            'nm':nm,
            'a1':a1,
            'b1':b1,
            'p1':p1,
            'p2':p2,
            'ans':ans,
            '1':1,
            'xy':xy,
            'yx':yx,
            'x1':x1,
            'x2':x2,
            'aa_op':aa_op,
            'bb_op':bb_op,
            'dict1':dict1,
            'dict2':dict2,
            'new1':new1,
            'new2':new2,
            'check':True,
            'id':1,
            
            'id':1,
                }
        return render(request,"Deepak/sequential-percentage-calculator-details.html", context)


def fractiondividedbynumbercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        return redirect(f'/what-is-{aa}/{bb}-divided-by-{cc}/')    

    else:
        return render(request,"Deepak/fraction-divided-by-number-calculator.html")


def fractiondividedbynumber(request,aa,bb,cc):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        return redirect(f'/what-is-{aa}/{bb}-divided-by-{cc}/') 
    else:
        xy = bb*cc
        from math import gcd
        d = gcd(aa, xy);

        p = aa // d; 
        q = xy // d;
        
        yx = round(p/q,4)

        ans = yx

        randList1=random_with_N_digits(50,100)
        randList2=random_with_N_digits(10,75)
        randList3=random_with_N_digits(50,300)
        dict1 = list(zip(randList1,randList2,randList3))

        randList4=random_with_N_digits(10,75)
        randList5=random_with_N_digits(50,100)
        randList6=random_with_N_digits(50,300)
        dict2 = list(zip(randList4,randList5,randList6))
       
        inputEnter = f"fraction = {aa}/{bb} and whole number = {cc}"
        query=fractiondividedbynumberCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="fraction divided by number Calculator makes it easy for you to find fraction divided by number"
            detailStep=f'''<p>The given number is : {aa} .  </p> <p>Given fraction number is {aa}/{bb} and divided by {cc}. For getting answer we have to multiply denominator with the whole number {cc}. and then we got a simplest form as {p}/{q} and in decimal form is {xy}</p>'''
            finalAnswer=(ans)
            obj=fractiondividedbynumberCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-is-{aa}/{bb}-divided-by-{cc}/',date_modified=datetime.datetime.now())
            obj.save()

        context = {
            'ans':ans,
            'aa':aa,
            'bb':bb,
            'cc':cc,
            'xy':xy,
            'yx':yx,
            'p':p,
            'q':q,
            'check':True,
            'dict1':dict1,
            'dict2':dict2,
            'id':1,
                }
        return render(request,"Deepak/fraction-divided-by-number-calculator-details.html", context)



def howmanyzeroesinlakhcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        

        return redirect(f'/{aa}-lakh-how-many-zeros/')    

    else:
        return render(request,"Deepak/how-many-zeroes-in-lakh-calculator.html")


def howmanyzeroesinlakh(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
            
        return redirect(f'/{aa}-lakh-how-many-zeros/') 
    else:
        
        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)
        
        

        ten = int(float(aa)*10000)
        hun = round(float(float(aa)*1000),1)
        th = round(float(float(aa)*100),2)
        tt = round(float(float(aa)*10),3)
        ht = round(float(float(aa)*1),4)

        cr = round(float(float(aa)*0.01),6)
        ml = round(float(float(aa)*0.1),6)
        bl = round(float(float(aa)*0.0001),8)
        tr = round(float(float(aa)*0.000001),9)

        
        r = int(float(aa)*(10**5))

        l = str(r)
        ans = 0
        for x in l[:]:
            if x == "0":
                ans = ans+1

        z = int(float(aa))

        list1 = []
        lst1 = []
        sum1 = z
        while sum1 < z+0.25:
            sum1 = round(sum1 +0.01,2)
            list1.append(sum1)
            dd = round(sum1*100000)
            l = str(dd)
            per1 = 0
            for x in l[:]:
                if x == "0":
                    per1 = per1+1
            lst1.append(per1)

        dict1 = dict(zip(list1, lst1))

        list2 = []
        lst2 = []
        sum2 = z + 0.25
        while sum2 < z+0.50:
            sum2 = round(sum2 +0.01,2)
            list2.append(sum2)
            dd1 = round(sum2*100000)
            l = str(dd1)
            per2 = 0
            for x in l[:]:
                if x == "0":
                    per2 = per2+1
            lst2.append(per2)
        dict2 = dict(zip(list2, lst2))

        query=lakhzerosCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="How Many Zeros in a lakh  Calculator makes it easy for you to find How Many Zeros in a lakh "
            detailStep=f'''<p>The given number is : {aa} </p> <p>Lakh is thousand times thousand. In scientific notation we can express Lakh as 1 × 105. In simple terms Lakh is a number that has 5 zeros. . </p> <p>We know 1 Lakh = 1,000, 000 </p> <p>Let us count how many zeros in {aa} Lakh with detailed explanation. </p> <p>So for {aa} Lakh = {r}. Therefore, {aa} Lakh have {ans} zeros</p>'''
            finalAnswer=str(ans)
            obj=lakhzerosCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/{aa}-lakh-how-many-zeros/',date_modified=datetime.datetime.now())
            obj.save()

        words = num2words(r)
        words = words.replace(" and", "")
        words = words.replace(",", "")

        context = {
            'words':words,
            'dict1':dict1,
            'list1':list1,
            'lst1':lst1,
            'dict2':dict2,
            'list2':list2,
            'lst2':lst2,
            'r':r,
            'ans':ans,
            'ten':ten,
            'hun':hun,
            'th':th,
            'tt':tt,
            'ht':ht,
            'cr':cr,
            'ml':ml,
            'bl':bl,
            'tr':tr,
            'aa':aa,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/how-many-zeroes-in-lakh-calculator-details.html", context)



def percentasdecimalcalculator(request):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/{aa}-as-a-decimal/')

    else:
         return render(request,'LCMGCF/percent-as-decimal-calculator.html')

def percentasdecimal(request,aa):
    if request.method == 'POST':
            if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
                inp=str(request.POST.get('aa'))
                if inp.isdigit(): 
                    aa=int(request.POST.get('aa'))
                else:
                    aa=float(request.POST.get('aa'))
            else:
                aa=None
            return redirect(f'/{aa}-as-a-decimal/')
    else:    
        
        x = round(float(aa)/100,4)
        z = int(float(aa))
        
        query=percentasdecimalCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="Percent as Decimal  Calculator | Free Calculator to find Percent as Decimal"
            detailStep=f'''<p>What is {aa} percent as a decimal? Get the answer for the question using the percent as decimal conversion. {aa} percent to a decimal is {x}</p><p>The given number is : {aa} </p><p>Divide a percent by 100 and remove the percent sign to convert from a percent to a decimal. Another way is to move the decimal two places left. </p><p>The formula to convert percent to decimal is <b>d = p÷ 100</b> </p>p>Let us convert {aa} percent as a decimal number with detailed explanation. </p> <ol><li>First write the percent in the form of fraction.<br> {aa}% = {aa}/100</li>  <br><li>Now divide {aa} by 100 to write in the decimal form.<br>  {aa} ÷ 100 = {x}</li></ol><p>So, {aa}% as a decimal is equal to {x}</p>'''
            finalAnswer=str(x)
            obj=percentasdecimalCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/{aa}-as-a-decimal/',date_modified=datetime.datetime.now())
            obj.save()

        list1 = []
        lst1 = []
        sum1 = z
        while sum1 < z+0.33:
            sum1 = round(sum1 +0.01,2)
            list1.append(sum1)
            per1 = round(sum1/100,4)
            lst1.append(per1)

        dict1 = dict(zip(list1, lst1))
        
        list2 = []
        lst2 = []
        sum2 = z + 0.33
        while sum2 < z+0.66:
            sum2 = round(sum2 +0.01,2)
            list2.append(sum2)
            per2 = round(sum2/100,4)
            lst2.append(per2)
        dict2 = dict(zip(list2, lst2))

        list3 = []
        lst3 = []
        sum3 = z + 0.66
        while sum3 < z+0.99:
            sum3 = round(sum3 +0.01,2)
            list3.append(sum3)
            per3 = round(sum3/100,4)
            lst3.append(per3)
        dict3 = dict(zip(list3, lst3))
        r1=int(floor(float(aa)))

        if "." not in aa:
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList2=random_with_N_digits1(20,150,n)
        context = {
            'dict1':dict1,
            'dict2':dict2,
            'dict3':dict3,
            'list1':list1,
            'list2':list2,
            'list3':list3,
            'lst1':lst1,
            'lst2':lst2,
            'lst3':lst3,
            'x':x,
            'aa':aa,
            'check':True,
            'id':1,
            'randList2':randList2
        }
        return render(request,'LCMGCF/percent-as-decimal-calculator-details.html',context)



def whatpercentcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        

        return redirect(f'/{aa}-is-what-percent-of-{bb}/')    

    else:
        return render(request,"Deepak/what-percent-calculator.html")

def whatpercent(request,aa,bb):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
            
        return redirect(f'/{aa}-is-what-percent-of-{bb}/') 
    else:
        
        # if "." not in aa:
        #     randList1=random_with_N_digits(10,51)
        #     randList2=random_with_N_digits(51,110)
        # if "." in aa:
        #     n = len(str(aa).split(".")[1])
        #     randList1=random_with_N_digits1(10,70,n)
        #     randList2=random_with_N_digits1(40,110,n)
        randList1 = []
        for x in range(aa+1, aa+6):
            randList1.append(x)

        randList2 = []
        for x in range(bb+1, bb+6):
            randList2.append(x)

        ans = round((aa*100)/bb,6)

        lst1 = []
        lst2 = []
        for x in range(aa+1, aa+51):
            lst1.append(x)
            lst2.append(round((x*100)/bb,2))
        dict1 = list(zip(lst1,lst2))

        lst3 = []
        lst4 = []
        for x in range(aa+51, aa+101):
            lst3.append(x)
            lst4.append(round((x*100)/bb,2))
        dict2 = list(zip(lst3,lst4))

        inputEnter = f"{aa} and {bb}"
        query=whatpercentCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="What percent  Calculator makes it easy for you to find What percent "
            detailStep=f'''<p>The given number is : {aa} and {bb} </p> <p></p>'''
            finalAnswer=str(ans)
            obj=whatpercentCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/{aa}-is-what-percent-of-{bb}/',date_modified=datetime.datetime.now())
            obj.save()

        
        context = {
            'ans':ans,
            
            'aa':aa,
            'bb':bb,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'dict1':dict1,
            'dict2':dict2,
            'id':1,
                }
        return render(request,"Deepak/what-percent-calculator-details.html", context)



def xtimesxcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        

        return redirect(f'/what-is-{aa}x-times-{bb}x/')    

    else:
        return render(request,"Deepak/what-is-x-times-x-calculator.html")

def xtimesx(request,aa,bb):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
            
        return redirect(f'/what-is-{aa}x-times-{bb}x/') 
    else:
        
        # if "." not in aa:
        #     randList1=random_with_N_digits(10,51)
        #     randList2=random_with_N_digits(51,110)
        # if "." in aa:
        #     n = len(str(aa).split(".")[1])
        #     randList1=random_with_N_digits1(10,70,n)
        #     randList2=random_with_N_digits1(40,110,n)
        randList1 = []
        for x in range(aa+1, aa+6):
            randList1.append(x)

        randList2 = []
        for x in range(bb+1, bb+6):
            randList2.append(x)

        ab = aa*bb

        ans = aa*bb

        lst1 = []
        lst2 = []
        for x in range(1,51):
            lst1.append(x)
            lst2.append(round((x*100)/bb,2))
        dict1 = list(zip(lst1,lst2))

        lst3 = []
        lst4 = []
        for x in range(51,101):
            lst3.append(x)
            lst4.append(round((x*100)/bb,2))
        dict2 = list(zip(lst3,lst4))

        inputEnter = f"{aa} and {bb}"
        query=xtimesxCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="What is x times x  Calculator makes it easy for you to find What is x times x "
            detailStep=f'''<p>The given number is : {aa} and {bb} </p> <p></p>'''
            finalAnswer=str(ans)
            obj=xtimesxCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-is-{aa}x-times-{bb}x/',date_modified=datetime.datetime.now())
            obj.save()

      
        context = {
            'ans':ans,
            'ab':ab,
            'aa':aa,
            'bb':bb,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'dict1':dict1,
            'dict2':dict2,
            'id':1,
                }
        return render(request,"Deepak/what-is-x-times-x-calculator-details.html", context)





def squarerootnumbercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        

        return redirect(f'/square-root-of-{aa}-squared/')    

    else:
        return render(request,"Deepak/square-root-of-number-calculator.html")

def squarerootnumber(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
            
        return redirect(f'/square-root-of-{aa}-squared/') 
    else:
        
        # if "." not in aa:
        #     randList1=random_with_N_digits(10,51)
        #     randList2=random_with_N_digits(51,110)
        # if "." in aa:
        #     n = len(str(aa).split(".")[1])
        #     randList1=random_with_N_digits1(10,70,n)
        #     randList2=random_with_N_digits1(40,110,n)
        randList1 = []
        for x in range(aa+1, aa+6):
            randList1.append(x)
        randList2 = []
        for x in range(aa+7, aa+12):
            randList2.append(x)

        ans = round(math.sqrt(aa),4)
        ab = (aa**2)

        query=squarerootnumberCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is square root of number  Calculator makes it easy for you to find What is square root of number "
            detailStep=f'''<p>The given number is : {aa}  </p> <p></p>'''
            finalAnswer=str(ans)
            obj=squarerootnumberCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/square-root-of-{aa}-squared/',date_modified=datetime.datetime.now())
            obj.save()

      
        context = {
            'ans':ans,
            'ab':ab,
            'aa':aa,
            #'bb':bb,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            # 'dict1':dict1,
            # 'dict2':dict2,
            'id':1,
                }
        return render(request,"Deepak/square-root-of-number-calculator-details.html", context)


def squaremetertofeetcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        return redirect(f'/{aa}-square-meters-to-square-feet/')    

    else:
        return render(request,"Deepak/square-meters-to-square-feet-calculator.html")

def squaremetertofeet(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
            
        return redirect(f'/{aa}-square-meters-to-square-feet/') 
    else:
        
        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)
        # randList1 = []
        # for x in range(aa+1, aa+6):
        #     randList1.append(x)
        # randList2 = []
        # for x in range(aa+7, aa+12):
        #     randList2.append(x)

        ans = round(float(aa)*10.76391041671,4)

        query=squaremetertofeetCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is square meter to square feet  Calculator makes it easy for you to find What is square meter to square feet "
            detailStep=f'''<p>The given number is : {aa}  </p> <p></p>'''
            finalAnswer=str(ans)
            obj=squaremetertofeetCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/{aa}-square-meters-to-square-feet/',date_modified=datetime.datetime.now())
            obj.save()

      
        context = {
            'ans':ans,
            'aa':aa,
            #'bb':bb,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            # 'dict1':dict1,
            # 'dict2':dict2,
            'id':1,
                }
        return render(request,"Deepak/square-meters-to-square-feet-calculator-details.html", context)


def squareinchtofeetcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        return redirect(f'/{aa}-square-inches-to-square-feet/')    

    else:
        return render(request,"Deepak/square-inches-to-square-feet-calculator.html")

def squareinchtofeet(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
            
        return redirect(f'/{aa}-square-inches-to-square-feet/') 
    else:
        
        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)
        # randList1 = []
        # for x in range(aa+1, aa+6):
        #     randList1.append(x)
        # randList2 = []
        # for x in range(aa+7, aa+12):
        #     randList2.append(x)

        ans = round(float(aa)/144,6)

        query=squareinchtofeetCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is square inch to square feet  Calculator makes it easy for you to find What is square inch to square feet "
            detailStep=f'''<p>The given number is : {aa}  </p> <p></p>'''
            finalAnswer=str(ans)
            obj=squareinchtofeetCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/{aa}-square-inches-to-square-feet/',date_modified=datetime.datetime.now())
            obj.save()

      
        context = {
            'ans':ans,
            'aa':aa,
            #'bb':bb,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            # 'dict1':dict1,
            # 'dict2':dict2,
            'id':1,
                }
        return render(request,"Deepak/square-inches-to-square-feet-calculator-details.html", context)


def secondpowercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        return redirect(f'/what-is-{aa}-to-the-2nd-power/')    

    else:
        return render(request,"LCMGCF/second-power-calculator.html")

def secondpower(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
            
        return redirect(f'/what-is-{aa}-to-the-2nd-power/') 
    else:
        
        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)
        # randList1 = []
        # for x in range(aa+1, aa+6):
        #     randList1.append(x)
        # randList2 = []
        # for x in range(aa+7, aa+12):
        #     randList2.append(x)

        ans = round(float(aa)**2,4)
        ans1 = round(1/ans,4)

        query=secondpowerCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is Second Power  Calculator makes it easy for you to find What is Second Power "
            detailStep=f'''<p>The given number is : {aa}  </p> <p></p>'''
            finalAnswer=str(ans)
            obj=secondpowerCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-is-{aa}-to-the-2nd-power/',date_modified=datetime.datetime.now())
            obj.save()
        
        words = num2words(float(aa))
        words = words.replace(" and", "")
        words = words.replace(",", "")

        ab = int(float(aa))
        lst1 = []
        lst2 = []
        for x in range(ab+1, ab+26):
            lst1.append(x)
            lst2.append((x**2))
        dict1 = list(zip(lst1,lst2))

        lst3 = []
        lst4 = []
        for x in range(ab+26, ab+51):
            lst3.append(x)
            lst4.append((x**2))
        dict2 = list(zip(lst3,lst4))

        lst5 = []
        lst6 = []
        for x in range(ab+51, ab+76):
            lst5.append(x)
            lst6.append((x**2))
        dict3 = list(zip(lst5,lst6))

      
        context = {
            'ans':ans,
            'ans1':ans1,
            'words':words,
            'aa':aa,
            #'bb':bb,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'dict1':dict1,
            'dict2':dict2,
            'dict3':dict3,
            'id':1,
                }
        return render(request,"LCMGCF/second-power-calculator-details.html", context)



def thirdpowercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        return redirect(f'/what-is-{aa}-to-the-3rd-power/')    

    else:
        return render(request,"LCMGCF/third-power-calculator.html")

def thirdpower(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
            
        return redirect(f'/what-is-{aa}-to-the-3rd-power/') 
    else:
        
        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)
        # randList1 = []
        # for x in range(aa+1, aa+6):
        #     randList1.append(x)
        # randList2 = []
        # for x in range(aa+7, aa+12):
        #     randList2.append(x)

        ans = round(float(aa)**3,4)
        ans1 = round(1/ans,6)

        query=thirdpowerCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is third Power  Calculator makes it easy for you to find What is third Power "
            detailStep=f'''<p>The given number is : {aa}  </p> <p></p>'''
            finalAnswer=str(ans)
            obj=thirdpowerCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-is-{aa}-to-the-3rd-power/',date_modified=datetime.datetime.now())
            obj.save()
        
        words = num2words(aa)
        words = words.replace(" and", "")
        words = words.replace(",", "")

        ab = int(float(aa))
        lst1 = []
        lst2 = []
        for x in range(ab+1, ab+26):
            lst1.append(x)
            lst2.append((x**3))
        dict1 = list(zip(lst1,lst2))

        lst3 = []
        lst4 = []
        for x in range(ab+26, ab+51):
            lst3.append(x)
            lst4.append((x**3))
        dict2 = list(zip(lst3,lst4))

        lst5 = []
        lst6 = []
        for x in range(ab+51, ab+76):
            lst5.append(x)
            lst6.append((x**3))
        dict3 = list(zip(lst5,lst6))

      
        context = {
            'ans':ans,
            'ans1':ans1,
            'words':words,
            'aa':aa,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'dict1':dict1,
            'dict2':dict2,
            'dict3':dict3,
            'id':1,
                }
        return render(request,"LCMGCF/third-power-calculator-details.html", context)


def squaredcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        return redirect(f'/what-is-{aa}-squared/')    

    else:
        return render(request,"LCMGCF/squared-calculator.html")

def squared(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
            
        return redirect(f'/what-is-{aa}-squared/') 
    else:
        
        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)
        # randList1 = []
        # for x in range(aa+1, aa+6):
        #     randList1.append(x)
        # randList2 = []
        # for x in range(aa+7, aa+12):
        #     randList2.append(x)

        ans = round(float(aa)**2,4)
        ans1 = round(math.sqrt(float(aa)),4)

        query=squaredCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is Squared  Calculator makes it easy for you to find What is Squared "
            detailStep=f'''<p>The given number is : {aa}  </p> <p></p>'''
            finalAnswer=str(ans)
            obj=squaredCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-is-{aa}-squared/',date_modified=datetime.datetime.now())
            obj.save()
        
        words = num2words(float(aa))
        words = words.replace(" and", "")
        words = words.replace(",", "")

        ab = int(float(aa))
        lst1 = []
        lst2 = []
        for x in range(ab+1, ab+26):
            lst1.append(x)
            lst2.append((x**2))
        dict1 = list(zip(lst1,lst2))

        lst3 = []
        lst4 = []
        for x in range(ab+26, ab+51):
            lst3.append(x)
            lst4.append((x**2))
        dict2 = list(zip(lst3,lst4))

        lst5 = []
        lst6 = []
        for x in range(ab+51, ab+76):
            lst5.append(x)
            lst6.append((x**2))
        dict3 = list(zip(lst5,lst6))

      
        context = {
            'ans':ans,
            'ans1':ans1,
            'words':words,
            'aa':aa,
            #'bb':bb,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'dict1':dict1,
            'dict2':dict2,
            'dict3':dict3,
            'id':1,
                }
        return render(request,"LCMGCF/squared-calculator-details.html", context)




def minutesofhourpercentcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        return redirect(f'/what-percentage-of-a-hour-is-{aa}-minutes/')    

    else:
        return render(request,"Deepak/minutes-of-an-hour-as-a-percentage-calculator.html")

def minutesofhourpercent(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
            
        return redirect(f'/what-percentage-of-a-hour-is-{aa}-minutes/') 
    else:
        
        # if "." not in aa:
        #     randList1=random_with_N_digits(10,51)
        #     randList2=random_with_N_digits(51,110)
        # if "." in aa:
        #     n = len(str(aa).split(".")[1])
        #     randList1=random_with_N_digits1(10,70,n)
        #     randList2=random_with_N_digits1(40,110,n)
        # # randList1 = []
        # for x in range(aa+1, aa+6):
        #     randList1.append(x)
        # randList2 = []
        # for x in range(aa+7, aa+12):
        #     randList2.append(x)

        randList1=random_with_N_digits(10,60)
        randList2=random_with_N_digits(1,30)
        ab = (100*aa)
        print(ab)

        ans = round(ab/60,2)
        xy = round(aa/60,4)
        ans1 =round(100-ans,2)

        query=minutesofhourpercentCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is Minutes of an Hour as a Percentage  Calculator makes it easy for you to find What is Minutes of an Hour as a Percentage "
            detailStep=f'''<p>The given number is : {aa}  </p> <p></p>'''
            finalAnswer=str(ans)
            obj=minutesofhourpercentCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-percentage-of-a-hour-is-{aa}-minutes/',date_modified=datetime.datetime.now())
            obj.save()
        
        
        lst1 = []
        lst2 = []
        for x in range(1, 21):
            lst1.append(x)
            lst2.append((round((100*x)/60,2)))
        dict1 = list(zip(lst1,lst2))

        lst3 = []
        lst4 = []
        for x in range(21, 41):
            lst3.append(x)
            lst4.append((round((100*x)/60,2)))
        dict2 = list(zip(lst3,lst4))

        lst5 = []
        lst6 = []
        for x in range(41, 61):
            lst5.append(x)
            lst6.append((round((100*x)/60,2)))
        dict3 = list(zip(lst5,lst6))

        


      
        context = {
            'ans':ans,
            'xy':xy,
            'aa':aa,
            'ab':ab,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'dict1':dict1,
            'dict2':dict2,
            'dict3':dict3,
            'id':1,
                }
        return render(request,"Deepak/minutes-of-an-hour-as-a-percentage-calculator-details.html", context)



def percenttopermilecalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        return redirect(f'/{aa}-percent-to-permille/')    

    else:
        return render(request,"Deepak/percent-to-permille-converter-calculator.html")

def percenttopermile(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
            
        return redirect(f'/{aa}-percent-to-permille/') 
    else:
        
        if "." not in aa:
            randList1=random_with_N_digits(10,80)
            randList2=random_with_N_digits(5,101)
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,80,n)
            randList2=random_with_N_digits1(5,101,n)
        # randList1 = []
        # for x in range(aa+1, aa+6):
        #     randList1.append(x)
        # randList2 = []
        # for x in range(aa+7, aa+12):
        #     randList2.append(x)

        ans = round(float(aa)*10,4)
        

        query=percenttopermileCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is Percent to Permille Converter  Calculator makes it easy for you to find What is Percent to Permille Converter "
            detailStep=f'''<p>The given number is : {aa}  </p> <p></p>'''
            finalAnswer=str(ans)
            obj=percenttopermileCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/{aa}-percent-to-permille/',date_modified=datetime.datetime.now())
            obj.save()
        
        

      
        context = {
            'ans':ans,
            'aa':aa,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            
            'id':1,
                }
        return render(request,"Deepak/percent-to-permille-converter-calculator-details.html", context)



def scientificnotationCalculator(request):

    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------

        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('dd')!=None and request.POST.get('dd')!='' :
            inp=str(request.POST.get('dd'))
            if inp.isdigit(): 
                dd=int(request.POST.get('dd'))
            else:
                dd=float(request.POST.get('dd'))
        else:
            dd=None

        
        if aa:
            ans = 0
            if cc == 0:
                ans = "{:.0e}".format(aa)
            elif cc == 1:
                ans = "{:.1e}".format(aa)
            elif cc == 2:
                ans = "{:.2e}".format(aa)
            elif cc == 3:
                ans = "{:.3e}".format(aa)
            elif cc == 4:
                ans = "{:.4e}".format(aa)
            elif cc == 5:
                ans = "{:.5e}".format(aa)
            elif cc == 6:
                ans = "{:.6e}".format(aa)
            elif cc == 7:
                ans = "{:.7e}".format(aa)
            elif cc == 8:
                ans = "{:.8e}".format(aa)
            elif cc == 9:
                ans = "{:.9e}".format(aa)
            elif cc == 10:
                ans = "{:.10e}".format(aa)
            elif cc == 11:
                ans = "{:.11e}".format(aa)
            elif cc == 12:
                ans = "{:.12e}".format(aa)
            elif cc == 13:
                ans = "{:.13e}".format(aa)
            elif cc == 14:
                ans = "{:.14e}".format(aa)
            elif cc == 15:
                ans = "{:.15e}".format(aa)
            elif cc == 16:
                ans = "{:.16e}".format(aa)
            elif cc == 17:
                ans = "{:.17e}".format(aa)
            elif cc == 18:
                ans = "{:.18e}".format(aa)
            elif cc == 19:
                ans = "{:.19e}".format(aa)
            elif cc == 20:
                ans = "{:.20e}".format(aa)

            context = {
                'ans':ans,
                'aa':aa,
                'cc':cc,
                'id':1
            }
            return render(request,"Deepak/scientific-notation-calculator.html", context)
        elif bb:
            n = ((len(str(dd))-1)+len(str(bb).split(".")[1]))
            xy = (10**dd)
            ans = round(bb*xy,n)
            context = {
                'xy':xy,
                'ans':ans,
                'bb':bb,
                'dd':dd,
                'id2':2
            }
            return render(request,"Deepak/scientific-notation-calculator.html", context)
        ans = 0
        query=scientificnotationCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="Scientific Notation Calculator makes it easy for you to find how to find Scientific Notation."
            detailStep=f'''<p>The given number is : {aa} </p> <p></p>'''
            finalAnswer={ans}
            obj=scientificnotationCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f"/scientific-notation-calculator/",date_modified=datetime.datetime.now())
            obj.save()        

        
        context = {
            'aa':aa,
            'bb':bb,
            'dd':dd,
            'cc':cc,
           
            }

        return render(request,"Deepak/scientific-notation-calculator.html", context)
    
    else:
        return render(request,"Deepak/scientific-notation-calculator.html")

def cubiccentimeterstocubicmetersconvertercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        return redirect(f'/convert-{aa}-cm3-to-m3/')    

    else:
        return render(request,"Deepak/cubic-centimeters-to-cubic-meters-converter-calculator.html")


def cubiccentimeterstocubicmetersconverter(request,aa):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        
        return redirect(f'/convert-{aa}-cm3-to-m3/') 
    else:
        ans=round(float(aa)*0.000001,10)

        if "." not in aa:
            randList1=random_with_N_digits(10,51)
            randList2=random_with_N_digits(51,110)
            
        if "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(10,70,n)
            randList2=random_with_N_digits1(40,110,n)
            

        query=cubiccentimeterstocubicmetersCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is cubic centemeter to cubic meter Calculator makes it easy for you to find cubic centemeter to cubic meter"
            detailStep=f'''<p>The given number is : {aa}   </p> <p></p>'''
            finalAnswer=(ans)
            obj=cubiccentimeterstocubicmetersCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/convert-{aa}-cm3-to-m3/',date_modified=datetime.datetime.now())
            obj.save()

        context = {
            'ans':ans,
            'aa':aa,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/cubic-centimeters-to-cubic-meters-converter-calculator-details.html", context)



def sumofintegercalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        if aa>bb:
            xy = aa
            aa = bb
            bb = xy
        else:
            aa = aa
            bb = bb

        return redirect(f'/sum-of-integers-from-{aa}-to-{bb}/')    

    else:
        return render(request,"Deepak/sum-of-integers-calculator.html")


def sumofinteger(request,aa,bb):
    if aa>bb:
        xy = aa
        aa = bb
        bb = xy
    else:
        aa = aa
        bb = bb
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        
        return redirect(f'/sum-of-integers-from-{aa}-to-{bb}/') 
    else:
        # ans=round(float(aa)*0.000001,10)

        # if "." not in aa:
        #     randList1=random_with_N_digits(10,51)
        #     randList2=random_with_N_digits(51,110)
            
        # if "." in aa:
        #     n = len(str(aa).split(".")[1])
        #     randList1=random_with_N_digits1(10,70,n)
        #     randList2=random_with_N_digits1(40,110,n)

        randList1=random_with_N_digits(50,170)
        randList2=random_with_N_digits(170,250)
        dict1 = list(zip(randList1,randList2))

        randList3=random_with_N_digits(10,100)
        randList4=random_with_N_digits(110,250)
        dict2 = list(zip(randList3,randList4))


        lst1 = []
        xyz = 0
        if bb-aa>250:
            xyz = xyz+9
            for x in range(aa,aa+251):
                lst1.append(x)
        else:
            for x in range(aa,bb+1):
                lst1.append(x)
        ans = 0
        lst2 = []
        for x in range(aa,bb+1):
            ans = ans+x
            lst2.append(x)
        
        ans1 = 0
        for x in range(aa,bb+1):
            if x%2 == 0:
                ans1 = ans1+x
                
        ab = aa+bb
        cc = bb-aa+1
        bc = ab*cc
        #ans = round(bc/2,2)
        
        inputEnter = f'{aa} and {bb}'
        query=sumofintegerCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="What is Sum of integers Calculator makes it easy for you to find Sum of integers"
            detailStep=f'''<p>The given number is : {aa}   </p> <p></p>'''
            finalAnswer=(ans)
            obj=sumofintegerCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/sum-of-integers-from-{aa}-to-{bb}/',date_modified=datetime.datetime.now())
            obj.save()

        context = {
            'ab':ab,
            'cc':cc,
            'bc':bc,
            'ans':ans,
            'ans1':ans1,
            'bb':bb,
            'aa':aa,
            'check':True,
            'lst1':lst1,
            'dict1':dict1,
            'dict2':dict2,
            'id':1,
            'xyz':xyz,
                }
        return render(request,"Deepak/sum-of-integers-calculator-details.html", context)



def randomnumberbetweencalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        if aa>bb:
            xy = aa
            aa = bb
            bb = xy
        else:
            aa = aa
            bb = bb

        return redirect(f'/random-number-between-{aa}-and-{bb}/')    

    else:
        return render(request,"Deepak/random-number-between-calculator.html")


def randomnumberbetween(request,aa,bb):
    if aa>bb:
        xy = aa
        aa = bb
        bb = xy
    else:
        aa = aa
        bb = bb
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        return redirect(f'/random-number-between-{aa}-and-{bb}/') 
    else:
        ans=randint(aa,bb+1)

        randList1=random_with_N_digits(50,170)
        randList2=random_with_N_digits(170,250)
        dict1 = list(zip(randList1,randList2))

        randList3=random_with_N_digits(10,100)
        randList4=random_with_N_digits(110,250)
        dict2 = list(zip(randList3,randList4))
            
        inputEnter = f'{aa} and {bb}'
        query=randomnumberbetweenCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="What is random Number Between Calculator makes it easy for you to find random Number Between"
            detailStep=f'''<p>The given number is : {aa}   </p> <p></p>'''
            finalAnswer=(ans)
            obj=randomnumberbetweenCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/random-number-between-{aa}-and-{bb}/',date_modified=datetime.datetime.now())
            obj.save()

        context = {
            'ans':ans,
            'bb':bb,
            'aa':aa,
            'check':True,
            'dict1':dict1,
            'dict2':dict2,
            'id':1,
                }
        return render(request,"Deepak/random-number-between-calculator-details.html", context)


def squarerootoffractioncalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        return redirect(f'/square-root-of-{aa}-by-{bb}/')    

    else:
        return render(request,"Deepak/square-root-of-a-fraction-calculator.html")


def squarerootoffraction(request,aa,bb):
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        return redirect(f'/square-root-of-{aa}-by-{bb}/') 
    else:
        ans=randint(aa,bb+1)

        randList1=random_with_N_digits(50,170)
        randList2=random_with_N_digits(170,250)
        dict1 = list(zip(randList1,randList2))

        randList3=random_with_N_digits(10,100)
        randList4=random_with_N_digits(110,250)
        dict2 = list(zip(randList3,randList4))

        sr1 = round(math.sqrt(aa),4)
        sr2 = round(math.sqrt(bb),4)
        ans = round(sr1/sr2,4)
        ab = round(aa/bb,4)
            

        query=squarerootoffractionCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is random Number Between Calculator makes it easy for you to find random Number Between"
            detailStep=f'''<p>The given number is : {aa}   </p> <p></p>'''
            finalAnswer=(ans)
            obj=squarerootoffractionCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/square-root-of-{aa}-by-{bb}/',date_modified=datetime.datetime.now())
            obj.save()

        context = {
            'ans':ans,
            'sr1':sr1,
            'sr2':sr2,
            'bb':bb,
            'aa':aa,
            'ab':ab,
            'check':True,
            'dict1':dict1,
            'dict2':dict2,
            'id':1,
                }
        return render(request,"Deepak/square-root-of-a-fraction-calculator-details.html", context)


##########----------------------LCMGCF TEMPLATE ----->  (5071 to 5308) --------------------###########
def numberminuspercentcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        return redirect(f'/{aa}-minus-{bb}-percent/')    

    else:
        return render(request,"LCMGCF/number-minus-percent-calculator.html")


def numberminuspercent(request,aa,bb):
    
    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        
        return redirect(f'/{aa}-minus-{bb}-percent/') 
    else:
        p = float(aa)
        q = float(bb)
        ab = p*q
        xy = round(ab/100,4)
        ans = round(p-xy,4)

        if "." not in aa:
            randList1=random_with_N_digits(100,500)
        elif "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(100,500,n)

        if "." not in bb:
            randList2=random_with_N_digits(10,50)
        elif "." in bb:
            n = len(str(bb).split(".")[1])
            randList2=random_with_N_digits1(10,50,n)     
        dict1 = list(zip(randList1,randList2))


        if "." not in aa:
            randList3=random_with_N_digits(100,500)
        elif "." in aa:
            n = len(str(aa).split(".")[1])
            randList3=random_with_N_digits1(100,500,n)

        if "." not in bb:
            randList4=random_with_N_digits(10,50)
        elif "." in bb:
            n = len(str(bb).split(".")[1])
            randList4=random_with_N_digits1(10,50,n)     
        dict2 = list(zip(randList3,randList4))

        
        inputEnter = f'{aa} and {bb}'
        query=numberminuspercentCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="What is Number minus percent Calculator makes it easy for you to find Number minus percent"
            detailStep=f'''<p>The given number is : {aa} and {bb}   </p> <p></p>'''
            finalAnswer=(ans)
            obj=numberminuspercentCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/{aa}-minus-{bb}-percent/',date_modified=datetime.datetime.now())
            obj.save()

        lst1 = []
        lst2 = []
        for x in range(int(float(bb))+1, int(float(bb))+51):
            lst1.append(x)
            m = round((p*x)/100,4)
            lst2.append(round(p-m,4))
        dict3 = list(zip(lst1,lst2))

        lst3 = []
        lst4 = []
        for x in range(int(float(aa))+1, int(float(aa))+51):
            lst3.append(x)
            m = round((q*x)/100,4)
            lst4.append(round(x-m,4))
        dict4 = list(zip(lst3,lst4))

        context = {
            'ab':ab,
            'xy':xy,
            #'bc':bc,
            'ans':ans,
            #'ans1':ans1,
            'bb':bb,
            'aa':aa,
            'check':True,
            #'lst1':lst1,
            'dict1':dict1,
            'dict2':dict2,
            'dict3':dict3,
            'dict4':dict4,
            'id':1,
                }
        return render(request,"LCMGCF/number-minus-percent-calculator-details.html", context)

def numberpluspercentcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
    
        return redirect(f'/{aa}-plus-{bb}-percent/')    

    else:
        return render(request,"LCMGCF/number-plus-percent-calculator.html")

def numberpluspercent(request,aa,bb):

    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        return redirect(f'/{aa}-plus-{bb}-percent/') 
    else:
        p = float(aa)
        q = float(bb)
        ab = p*q
        xy = round(ab/100,4)
        ans = p+xy
        ans1 = round(float(bb)/100,4)

        if "." not in aa:
            randList1=random_with_N_digits(100,500)
        elif "." in aa:
            n = len(str(aa).split(".")[1])
            randList1=random_with_N_digits1(100,500,n)

        if "." not in bb:
            randList2=random_with_N_digits(10,50)
        elif "." in bb:
            n = len(str(bb).split(".")[1])
            randList2=random_with_N_digits1(10,50,n)     
        dict1 = list(zip(randList1,randList2))


        if "." not in aa:
            randList3=random_with_N_digits(100,500)
        elif "." in aa:
            n = len(str(aa).split(".")[1])
            randList3=random_with_N_digits1(100,500,n)

        if "." not in bb:
            randList4=random_with_N_digits(10,50)
        elif "." in bb:
            n = len(str(bb).split(".")[1])
            randList4=random_with_N_digits1(10,50,n)     
        dict2 = list(zip(randList3,randList4))
            
        inputEnter = f'{aa} and {bb}'
        query=numberpluspercentCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="What is Number plus Percent Calculator makes it easy for you to find Number plus Percent"
            detailStep=f'''<p>The given number is : {aa}   </p> <p></p>'''
            finalAnswer=(ans)
            obj=numberpluspercentCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/{aa}-plus-{bb}-percent/',date_modified=datetime.datetime.now())
            obj.save()
        
        lst1 = []
        lst2 = []
        for x in range(int(float(bb))+1, int(float(bb))+51):
            lst1.append(x)
            m = round((p*x)/100,4)
            lst2.append(round(p+m,4))
        dict3 = list(zip(lst1,lst2))

        lst3 = []
        lst4 = []
        for x in range(int(float(aa))+1, int(float(aa))+51):
            lst3.append(x)
            m = round((q*x)/100,4)
            lst4.append(round(x+m,4))
        dict4 = list(zip(lst3,lst4))

        context = {
            'ans':ans,
            'ans1':ans1,
            'bb':bb,
            'aa':aa,
            'ab':ab,
            'xy':xy,
            'check':True,
            'dict1':dict1,
            'dict2':dict2,
            'dict3':dict3,
            'dict4':dict4,
            'id':1,
                }
        return render(request,"LCMGCF/number-plus-percent-calculator-details.html", context)

##########----------------------LCMGCF TEMPLATE ENDS--------------------###########
#############------------START NEW WORK##########################################
def atsequencedomain(request):
    if request.method=='POST':
        func=str(request.POST['func'])
        if '/' in func:
            func=func.replace('/','÷')
        return redirect("/given-the-arithmetic-sequence-an-'{}'-what-is-the-domain-for-n".format(func))    
    else:
        content={
            'question':'1+2*(n-1)',
            'display':'none'
        }
        return render(request,'Deepak/atsequence-calculator.html',content)
def atsequencedomaintail(request,func):

    val=atsequenceutility(func)
    if val[0].solution=='Syntax Error':
        content={
            'question':func,
            'display':'block'
        }
        return render(request,'Deepak/atsequence-calculator.html',content)
    else:
        linka=[]
        for i in range(5):
            a=random.randint(1,9)
            b=random.randint(1,9)
            c=random.randint(1,9)
            s=str(a)+'+'+str(b)+'*'+'(n-'+str(c)+')'
            linka.append(s)
        linkb=[]
        for i in range(5):
            a=random.randint(1,9)
            b=random.randint(1,9)
            c=random.randint(1,9)
            s=str(a)+'+'+str(b)+'*'+'(n-'+str(c)+')'
            linkb.append(s)
        content={
        'res':val,
        'question':val[0].func,
        'linksa':linka,
        'linksb':linkb
        }
        return render(request,'Deepak/atsequence-calculator-details.html',content)
        #########__________________________________________FUNCTION

##DEEPAK
def checkIsAP(arr, n):
 
    # Base Case
    if (n == 1):
        return True
 
    # Sort array
    arr.sort();
 
   
    d = arr[1] - arr[0]
 
 
    for i in range(2, n):
        if (arr[i] - arr[i - 1] != d):
            return False
 
    return True
 
# Returns true if arr[0..n-1]
# can form GP
def checkIsGP(arr, n):
 
    if (n == 1):
        return True 
    arr.sort()
    r = arr[1] / arr[0]
    for i in range(2, n):
        if (arr[i] / arr[i - 1] != r):
            return False
 
    return True
#########__________________________________________FUNCTION


def sumofgeometricsequencecalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            aa=request.POST.get('aa')
        try:
            lst = [int(i) for i in aa.split(",")]
            
            #print(len(lst))
            
        except:
            messages.error(request, 'Syntax Error.')
            context = {
            'aa':aa,
            }
            return render(request,'Deepak/sum-of-geometric-sequence-calculator.html', context)

        flag = 0

        if (checkIsGP(lst, len(lst))):
            flag = 1
            if len(lst)>=4:
                print()
            elif len(lst)<4:
                messages.error(request, 'Enter atleast upto 4 terms.')
                context = {
                    'aa':aa,
                    }
                return render(request,'Deepak/sum-of-geometric-sequence-calculator.html', context)

        
        elif (flag == 0):
            messages.error(request, 'The given array is not in geometric sequence.')
            context = {
                'aa':aa,
                }
            return render(request,'Deepak/sum-of-geometric-sequence-calculator.html', context)

        # print("LIST LENGTH",len(lst))
        # if len(lst)>=4:
        #     x = 0
        # elif len(lst)<4:
        #     messages.error(request, 'Enter atleast upto 4 terms.')
        #     context = {
        #         'aa':aa,
        #         }
        #     return render(request,'Deepak/sum-of-geometric-sequence-calculator.html', context)
        # cc = str(lst).replace(',', '-')
        # print(cc)
        #print("LENGTH",len(aa))
        #lst = [int(i) for i in aa.split(",")]
        return redirect(f'/what-is-the-sum-of-the-geometric-sequence-{aa}-if-there-are-{bb}-terms/')
    else:
        return render(request,"Deepak/sum-of-geometric-sequence-calculator.html")


def sumofgeometricsequence(request,aa,bb):
    if request.method == 'POST':

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            aa=request.POST.get('aa')
        try:
            lst = [int(i) for i in aa.split(",")]

        except:
            messages.error(request, 'Syntax Error.')
            # context = {
            # 'aa':aa,
            # }
            #return render(request,'Deepak/sum-of-geometric-sequence-calculator.html', context)
            return redirect(f'/sum-of-geometric-sequence-calculator/')

        flag = 0

        if (checkIsGP(lst, len(lst))):
            flag = 1
            if len(lst)>=4:
                print()
            elif len(lst)<4:
                messages.error(request, 'Enter atleast upto 4 terms.')
                return redirect(f'/sum-of-geometric-sequence-calculator/')
        
        elif (flag == 0):
            messages.error(request, 'The given array is not in geometric sequence.')
            # context = {
            #     'aa':aa,
            #     }
            return redirect(f'/sum-of-geometric-sequence-calculator/')

        return redirect(f'/what-is-the-sum-of-the-geometric-sequence-{aa}-if-there-are-{bb}-terms/') 
    else:
        lst = [int(i) for i in aa.split(",")]
        # aa = 9
        # ans=randint(aa,bb+1)
        x1 = lst[0]
        x2 = lst[1]
        x3 = lst[2]
        x4 = lst[3]
        xy = int(x4/x3)
        z = 0
        xb = (int(xy)**bb)
        xb1 = (int(xy)-1)
        xx = int(x1) * (xb-1)
        xx1 = int(xx/xb1)
        if xy >= 1:
            z = 9
        else:
            z = 0
        
        ab = (int(xy)**bb)
        ab1 = 1+int(xy)
        ac = int(x1) * (1-ab)
        ac1 = int(ac/ab1)
        randList1=random_with_N_digits(1,40)
        randList2=random_with_N_digits(1,50)
        

        #x1,y1 = (-3, 18, -108) , 9
        ans = ac1
        query=sumofgeometricsequenceCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is the sum of the geometric sequence {aa}, ... if there are {bb} terms?"
            detailStep=f'''<p>The given geometric sequence is : {aa}  and sum of {bb} term is {ans}</p> <p></p>'''
            finalAnswer=(ans)
            obj=sumofgeometricsequenceCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-is-the-sum-of-the-geometric-sequence-{aa}-if-there-are-{bb}-terms/',date_modified=datetime.now())
            obj.save()

        context = {
            'ans':ans,
            'ac1':ac1,
            'ac':ac,
            'ab1':ab1,
            'ab':ab,
            'xx1':xx1,
            'xx':xx,
            'xb1':xb1,
            'xb':xb,
            'xy':xy,
            'x2':x2,
            'x1':x1,
            'bb':bb,
            'aa':aa,
            'x3':x3,
            'x4':x4,
            'z':z,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/sum-of-geometric-sequence-calculator-details.html", context)




def sumofarithmeticsequencecalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            aa=request.POST.get('aa')
        try:
            lst = [int(i) for i in aa.split(",")]
            
            #print(len(lst))
            
        except:
            messages.error(request, 'Syntax Error.')
            context = {
            'aa':aa,
            }
            return render(request,'Deepak/sum-of-arithmetic-sequence-calculator.html', context)

        flag = 0

        if (checkIsAP(lst, len(lst))):
            flag = 1
            if len(lst)>=4:
                print()
            elif len(lst)<4:
                messages.error(request, 'Enter atleast upto 4 terms.')
                context = {
                    'aa':aa,
                    }
                return render(request,'Deepak/sum-of-arithmetic-sequence-calculator.html', context)

        
        elif (flag == 0):
            messages.error(request, 'The given array is not in arithmetic sequence.')
            context = {
                'aa':aa,
                }
            return render(request,'Deepak/sum-of-arithmetic-sequence-calculator.html', context)

        
        return redirect(f'/what-is-the-sum-of-the-arithmetic-sequence-{aa}-if-there-are-{bb}-terms/')
    else:
        return render(request,"Deepak/sum-of-arithmetic-sequence-calculator.html")


def sumofarithmeticsequence(request,aa,bb):
    if request.method == 'POST':

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            aa=request.POST.get('aa')
        try:
            lst = [int(i) for i in aa.split(",")]

        except:
            messages.error(request, 'Syntax Error.')
            
            return redirect(f'/sum-of-arithmetic-sequence-calculator/')

        flag = 0

        if (checkIsAP(lst, len(lst))):
            flag = 1
            if len(lst)>=4:
                print()
            elif len(lst)<4:
                messages.error(request, 'Enter atleast upto 4 terms.')
                return redirect(f'/sum-of-arithmetic-sequence-calculator/')
        
        elif (flag == 0):
            messages.error(request, 'The given array is not in arithmetic sequence.')
            
            return redirect(f'/sum-of-arithmetic-sequence-calculator/')

        return redirect(f'/what-is-the-sum-of-the-arithmetic-sequence-{aa}-if-there-are-{bb}-terms/') 
    else:
        lst = [int(i) for i in aa.split(",")]
        # aa = 9
        # ans=randint(aa,bb+1)
        x1 = lst[0]
        x2 = lst[1]
        x3 = lst[2]
        x4 = lst[3]
        xy = int(x2-x1)
        
        xb = bb-1
        xb1 = xb*xy
        xx = x1+xb1    


        ab = bb*(x1+xx)
        ab1 = round(ab/2,2)

        randList1=random_with_N_digits(1,40)
        randList2=random_with_N_digits(1,50)
        

        #x1,y1 = (-3, 18, -108) , 9
        ans = ab1
        query=sumofarithmeticsequenceCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is the sum of the arithmetic sequence {aa}, ... if there are {bb} terms?"
            detailStep=f'''<p>The given arithmetic sequence are : {aa} and the sum of {bb} term of the given arithmetic sequence is {ans}   </p> <p></p>'''
            finalAnswer=(ans)
            obj=sumofarithmeticsequenceCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-is-the-sum-of-the-arithmetic-sequence-{aa}-if-there-are-{bb}-terms/',date_modified=datetime.now())
            obj.save()

        context = {
            'ans':ans,
           
            'ab1':ab1,
            'ab':ab,
            'xx':xx,
            'xb1':xb1,
            'xb':xb,
            'xy':xy,
            'x2':x2,
            'x1':x1,
            'bb':bb,
            'aa':aa,
            'x3':x3,
            'x4':x4,
            #'z':z,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
                }
        return render(request,"Deepak/sum-of-arithmetic-sequence-calculator-details.html", context)



def arithmeticsequencetermcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('yy')!=None and request.POST.get('yy')!='' :
            inp=str(request.POST.get('yy'))
            if inp.isdigit(): 
                yy=int(request.POST.get('yy'))
            else:
                yy=float(request.POST.get('yy'))
        else:
            yy=None
            
        return redirect(f'/what-is-the-{aa}-term-of-the-arithmetic-sequence-where-a1-{bb}-and-a{yy}-{cc}/')
        
    else:
        return render(request,"Deepak/term-of-arithmetic-sequence-calculator.html")


def arithmeticsequenceterm(request,aa,bb,cc,yy):

    if request.method == 'POST':

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('yy')!=None and request.POST.get('yy')!='' :
            inp=str(request.POST.get('yy'))
            if inp.isdigit(): 
                yy=int(request.POST.get('yy'))
            else:
                yy=float(request.POST.get('yy'))
        else:
            yy=None
        
        
        
        return redirect(f'/what-is-the-{aa}-term-of-the-arithmetic-sequence-where-a1-{bb}-and-a{yy}-{cc}/') 
    else:
        

        x1 = round(float(cc)-float(bb),2)
        x2 = yy-1
        x3 = round(x1/x2,2)

        ab = aa-1
        ba = round(ab*x3,4)
        ans = round(float(bb)+ba,2)
        #print(ans)
        randList1=random_with_N_digits(10,100)
        randList2=random_with_N_digits(10,500)
        randList3=random_with_N_digits(2,90)
        randList4=random_with_N_digits(100,500)
        dict2 = list(zip(randList1,randList2,randList3,randList4))

        #x1,y1 = (-3, 18, -108) , 9
        query=arithmeticsequencetermCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is the sum of the arithmetic sequence {aa}, ... if there are {bb} terms?"
            detailStep=f'''<p>The given number is : {aa}   </p> <p></p>'''
            finalAnswer=(ans)
            obj=arithmeticsequencetermCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-is-the-{aa}-term-of-the-arithmetic-sequence-where-a1-{bb}-and-a{yy}-{cc}/',date_modified=datetime.now())
            obj.save()

        # from math import exp, log
        # x = 8
        # n = 3
        # exp(log(x)/n)

        context = {
            'ans':ans,
           
            'ba':ba,
            'ab':ab,
            'ans':ans,
            # 'xb1':xb1,
            # 'xb':xb,
            # 'xy':xy,
            'x2':x2,
            'cc':cc,
            'bb':bb,
            'aa':aa,
            'x1':x1,
            'yy':yy,
            'x3':x3,
            'check':True,
            #'n':n,
            'dict2':dict2,
            'id':1,
                }
        return render(request,"Deepak/term-of-arithmetic-sequence-calculator-details.html", context)



def geometricsequencetermcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('yy')!=None and request.POST.get('yy')!='' :
            inp=str(request.POST.get('yy'))
            if inp.isdigit(): 
                yy=int(request.POST.get('yy'))
            else:
                yy=float(request.POST.get('yy'))
        else:
            yy=None
            
        return redirect(f'/what-is-the-{aa}-term-of-the-geometric-sequence-where-a1-{bb}-and-a{yy}-{cc}/')
        
    else:
        return render(request,"Deepak/term-of-geometric-sequence-calculator.html")


def geometricsequenceterm(request,aa,bb,cc,yy):

    if request.method == 'POST':

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('cc')!=None and request.POST.get('cc')!='' :
            inp=str(request.POST.get('cc'))
            if inp.isdigit(): 
                cc=int(request.POST.get('cc'))
            else:
                cc=float(request.POST.get('cc'))
        else:
            cc=None

        if request.POST.get('yy')!=None and request.POST.get('yy')!='' :
            inp=str(request.POST.get('yy'))
            if inp.isdigit(): 
                yy=int(request.POST.get('yy'))
            else:
                yy=float(request.POST.get('yy'))
        else:
            yy=None
        
        
        
        return redirect(f'/what-is-the-{aa}-term-of-the-geometric-sequence-where-a1-{bb}-and-a{yy}-{cc}/') 
    else:
        n = yy-1
        n1 = aa-1
        print(n)
        from math import gcd
        from math import exp, log
        d = gcd(bb, cc);
        p = bb // d;
        q = cc // d;
        fin = int(exp(log(p)/n))
        fin1 = int(exp(log(q)/n))


        x1 = fin1**n1
        x2 = fin**n1
        d1 = gcd(x1, x2);
        p1 = x1 // d1;
        q1 = x2 // d1;


        y1 = bb*p1
        d2 = gcd(y1, q1);
        p2 = y1 // d2;
        q2 = q1 // d2;

        
        ans = round(p2/q2,8)
        #print(ans)
        randList1=random_with_N_digits(10,100)
        randList2=random_with_N_digits(10,500)
        randList3=random_with_N_digits(2,90)
        randList4=random_with_N_digits(100,500)
        dict2 = list(zip(randList1,randList2,randList3,randList4))

        #x1,y1 = (-3, 18, -108) , 9
        query=geometricsequencetermCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is the sum of the geometric sequence {aa}, ... if there are {bb} terms?"
            detailStep=f'''<p>The given number is : {aa}   </p> <p></p>'''
            finalAnswer=(ans)
            obj=geometricsequencetermCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-is-the-{aa}-term-of-the-geometric-sequence-where-a1-{bb}-and-a{yy}-{cc}/',date_modified=datetime.now())
            obj.save()

        context = {
            'ans':ans,
           
            'p2':p2,
            'q2':q2,
            'ans':ans,
            'fin1':fin1,
            'fin':fin,
            'n1':n1,
            'q1':q1,
            'cc':cc,
            'bb':bb,
            'aa':aa,
            'p1':p1,
            'yy':yy,
            #'x3':x3,
            'check':True,
            'n':n,
            'dict2':dict2,
            'id':1,
                }
        return render(request,"Deepak/term-of-geometric-sequence-calculator-details.html", context)


def fractionofadayinhourcalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
            
        return redirect(f'/what-fraction-of-a-day-is-{aa}-hours/')
        
    else:
        return render(request,"Deepak/fraction-of-a-day-in-hour-calculator.html")


def fractionofadayinhour(request,aa):

    if request.method == 'POST':
        
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        
        return redirect(f'/what-fraction-of-a-day-is-{aa}-hours/') 
    else:
        from math import gcd
        d = gcd(aa, 24);
        p1 = aa // d;
        q1 = 24 // d;


        d1 = gcd(aa, 60);
        p2 = aa // d1;
        q2 = 60 // d1;

        y = q2*24
        d2 = gcd(p2, y);
        p3 = p2 // d2;
        q3 = y // d2;
        
        randList1=random_with_N_digits(10,100)
        randList2=random_with_N_digits(10,100)
        
        ans = round(p1/q1,3)
        #x1,y1 = (-3, 18, -108) , 9
        query=fractionofadayinhourCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is the fraction of a day in hours calculator?"
            detailStep=f'''<p>The given number is : {aa} hours. </p> <p> We know that The total number of hours in 1 day = 24 hours. Number of days in 1 hour = 1/24 hrs. so number of day in given {aa} hrs is {ans} day(s).   </p>'''
            finalAnswer=(ans)
            obj=fractionofadayinhourCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/what-fraction-of-a-day-is-{aa}-hours/',date_modified=datetime.now())
            obj.save()

        # from math import exp, log
        # x = 8
        # n = 3
        # exp(log(x)/n)

        context = {
            'ans':ans,
           
            'p1':p1,
            'q1':q1,
            'p2':p2,
            'q2':q2,
            'p3':p3,
            'q3':q3,
            # 'ans':ans,
            # # 'xb1':xb1,
            # # 'xb':xb,
            # # 'xy':xy,
            # 'x2':x2,
            # 'cc':cc,
            # 'bb':bb,
            'aa':aa,
            # 'x1':x1,
            # 'yy':yy,
            # 'x3':x3,
            'check':True,
            #'n':n,
            'randList1':randList1,
            'randList2':randList2,
            
            'id':1,
                }
        return render(request,"Deepak/fraction-of-a-day-in-hour-calculator-details.html", context)




def remainderofequationcalculator(request):
     
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        aa = request.POST['aa']
        bb = request.POST['bb']
        cc = request.POST['cc']
        dd = request.POST['dd']
        ee = request.POST['ee']

        #print("MAIN",aa)
        return redirect(f'/find-the-remainder-when-fx-{aa}-x3-{bb}-x2-{cc}-x-{dd}-is-divided-by-x-{ee}/') 

    else:
        return render(request,"Deepak/find-the-remainder-equation-calculator.html")


def remainderofequation(request,aa,bb,cc,dd,ee):
    
    #try:
        
        
        a,b,c,d,e = '','','','',''
        if aa[-1] == '-':
            aa = int(aa.rstrip('-'))
            a = 'minus'
        else:
            aa = int(aa)
            a = 'plus'

        if '-' in bb:
            bb = bb.strip('-')
            b = 'minus'
        else:
            b = 'plus'

        if '-' in cc:
            cc = cc.strip('-')
            c = 'minus'
        else:
            c = 'plus'

        if '-' in dd:
            dd = dd.strip('-')
            d = 'minus'
        else:
            d = 'plus'

        if '-' in ee:
            ee = ee.strip('-')
            e = 'minus'
        else:
            e = 'plus'

        ###########################
        x1,x2,x3,x4,x5,xe = 0,0,0,0,0,0
        if a == 'minus':
            aa = int('-'+ aa)
            x1 = abs(aa)
        else:
            aa = int(aa)
            
        if b == 'minus':
            bb = int('-'+ bb)
            x2 = abs(bb)
        else:
            bb = int(bb)
            

        if c == 'minus':
            cc = int('-'+ cc)
            x3 = abs(cc)
        else:
            cc = int(cc)

        if d == 'minus':
            dd = int('-'+ dd)
            x4 = abs(dd)
        else:
            dd = int(dd)

        a1,a2,p1,p2 = 0,0,0,0
        if e == 'minus':
            ee = int('-'+ ee)
            x5 = abs(ee)
            a1 = (x5**3)
            a2 = (x5**2)
            p1 = (cc*x5)
            
        else:
            ee = int(ee)
            xe = int('-'+ str(ee))
            a1 = (xe**3)
            a2 = (xe**2)
            p2 = (cc*xe)

        a3 = aa*a1
        a4 = bb*a2
        z = ''
        z1 = 0
        if a4 >= 0:
            z = 'plus'
        else:
            z = 'minus'
            z1 = abs(a4)        
        ans = 0
        if p1 == 0:
            ans = a3+a4+dd+p2
        elif p2 == 0:
            ans = a3+a4+dd+p1

        inputEnter = f"number = {aa}x3, {bb}x2  {cc}x and {dd} divided by x + {ee}"
        query=remainderofequationCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="what is remainder when f(x) = {aa}x3 + {bb}x2 + {cc}x + {dd} is divided by x - {ee}"
            detailStep=f'''<p>The given number is : {inputEnter} .</p> <p>A number </p>'''
            finalAnswer=str(ans)
            obj=remainderofequationCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/find-the-remainder-when-fx-{aa}-x3-{bb}-x2-{cc}-x-{dd}-is-divided-by-x-{ee}/',date_modified=datetime.now())
            obj.save()

        randList1=random_with_single_digits(1,20)
        randList2=random_with_single_digits(20,40)
        randList5=random_with_single_digits(10,50)
        randList6=random_with_single_digits(20,90)
        randList7=random_with_single_digits(1,10)
        dict1 = list(zip(randList1,randList2,randList5,randList6,randList7))

        randList3=random_with_single_digits(10,50)
        randList4=random_with_single_digits(20,40)
        randList8=random_with_single_digits(1,50)
        randList9=random_with_single_digits(20,90)
        randList=random_with_single_digits(1,10)
        dict2 = list(zip(randList3,randList4,randList8,randList9,randList))  
        
        
        context = {
            'aa':aa,
            'bb':bb,
            'cc':cc,
            'dd':dd,
            'ee':ee,
            'a':a,
            'b':b,
            'c':c,
            'd':d,
            'e':e,
            'z':z,
            # 'p':p,
            'p1':p1,
            'p2':p2,
            'z1':z1,
            'a1':a1,
            'a2':a2,
            'a3':a3,
            'a4':a4,
            # 'a5':a5,
            'x1':x1,
            'x2':x2,
            'x3':x3,
            'x4':x4,
            'x5':x5,
            'xe':xe,
            'ans':ans,
            # 'add':add,
            # 'ans':ans,
            # 'ad':ad,
            # 'aa':aa,
            # 'bb':bb,
            # 'nm':nm,
            # 'a1':a1,
            # 'b1':b1,
            # 'p1':p1,
            # 'p2':p2,
            # 'ans':ans,
            # '1':1,
            # 'xy':xy,
            # 'yx':yx,
            # 'x1':x1,
            # 'x2':x2,
            # 'aa_op':aa_op,
            # 'bb_op':bb_op,
            'dict1':dict1,
            'dict2':dict2,
            # 'new1':new1,
            # 'new2':new2,
            'check':True,
            'id':1,
            
                }
        return render(request,"Deepak/find-the-remainder-equation-calculator-details.html", context)
    # except:
    #     messages.error(request,'Invalid Inputs.') 
    #     return redirect('/find-remainder-of-equation-calculator/')




##-------------------------------SUNIL---------------------------------
def rectangulardimensioncalculator(request): 
    if request.method == 'POST':
        
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        

        return redirect(f'/find-the-dimensions-of-a-rectangle-with-a-perimeter-{aa}m-whose-area-is-as-large-as-possible/')    

    else:
        return render(request,"Deepak/dimension_rectangl_calculator.html")

def largestdimension(request,aa):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None
        return redirect(f'/find-the-dimensions-of-a-rectangle-with-a-perimeter-{aa}m-whose-area-is-as-large-as-possible/')    
    else:
        randList1 = []
        for x in range(int(float(aa))+1, int(float(aa))+6):
            randList1.append(x)
        randList2 = []
        for x in range(int(float(aa))+7, int(float(aa))+12):
            randList2.append(x)

        ans = round(float(aa)/4,3)
        #ab = (aa/4)

        query=rectangulardimensionCalculator.objects.filter(inputEnter=str(aa))
        if len(query)==0:
            solutionTitle="What is the Largest dimension of a Rectangle Calculator?"
            detailStep=f'''<p>The given number is : {aa}m and    </p> <p>To find the dimension of a rectangle with given perimeter whose area is as large as possible, can be found by using a formula can be written as x = Perimeter/4</p>'''
            finalAnswer=(ans)
            obj=rectangulardimensionCalculator(inputEnter=str(aa),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/find-the-dimensions-of-a-rectangle-with-a-perimeter-{aa}m-whose-area-is-as-large-as-possible/',date_modified=datetime.now())
            obj.save()


        context = {
            'ans':ans,
            'aa':aa,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
        }
        return render(request,"Deepak/dimension_rectangle_calculator-details.html", context)

def differentialequationcalculator(request): 
    if request.method=='POST':
        xcof= int(request.POST["xcof"])
        ycof = int(request.POST["ycof"])
        operator = request.POST['operator']
        return redirect(f"/solve-the-given-differential-equation-by-separation-of-variables-dy-dx-e{xcof}x{operator}{ycof}y/")   

    else:
        return render(request,"Deepak/differential_equation_calculator.html")

def generalSolution(request,xcof,operator,ycof):
        if request.method=='POST':
            m=xcof= int(request.POST["xcof"])
            n=ycof = int(request.POST["ycof"])
            operator = request.POST['operator']
            #solve-the-given-differential-equation-by-separation-of-variables-dy-dx-e{xcof}xoperator{ycof}y
            return redirect(f"/solve-the-given-differential-equation-by-separation-of-variables-dy-dx-e{xcof}x{operator}{ycof}y/")   
        m=xcof
        valy=n= ycof
        if operator == "+":
            valy = -n
        ans = "(e<sup>{0}y</sup>/{0}) = (e<sup>{1}x</sup>/{1})+c".format(valy,m)
        randList1 = []
        for x in range(1,6):
            pair = (m+x,n+x)
            val = str(pair[0])+"x{}".format(operator)+str(pair[1])+"y"
            randList1.append(val)
        #print(randList1)
        randList2 = []
        for x in range(7,12):
            pair = (m+x,n+x)
            val = str(pair[0])+"x{}".format(operator)+str(pair[1])+"y"
            randList2.append(val)

        inputEnter = f'/{xcof}x {operator} {ycof}y'
        query=differentialequationCalculator.objects.filter(inputEnter=inputEnter)
        if len(query)==0:
            solutionTitle="What is the differential equation of exponential?"
            detailStep=f'''<p>The given number is : e{xcof}x  {operator} {ycof}yand    </p> <p>General Solutions of a differential equation, that are used in our daily life. A differential equation in exponential form can be written as dy/dx= e(ax+by). We know that the formula of ∫e(ax)dx = (e(ax) /a) + c, where c is the integration constant. We know that the formula of ∫e(ax)dx = (e(ax) /a) + c, where c is the integration constant.</p>'''
            finalAnswer=(ans)
            obj=differentialequationCalculator(inputEnter=inputEnter,solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/solve-the-given-differential-equation-by-separation-of-variables-dy-dx-e{xcof}x{operator}{ycof}y/',date_modified=datetime.now())
            obj.save()

        context = {
            'ans':ans, 
            'xcof':m,
            'ycof':n,
            'valy':valy,
            'operator':operator,
            'check':True,
            'randList1':randList1,
            'randList2':randList2,
            'id':1,
        }
        return render(request,"Deepak/differential-equation-calculator-details.html", context)



def pointOnTheParabolaCalculator(request):
    if request.method=='POST':
        xcof= int(request.POST["xcof"])
        x1 = int(request.POST["x1"])
        y1 = int(request.POST["y1"])
        return redirect("/find-the-point-on-the-parabola-y2-{0}x-that-is-closest-to-the-point-{1}-{2}/".format(xcof,x1,y1))   
    else:
        id = 0
        return render(request,"Deepak/point-on-the-parabola-calculator.html",{"id":id})

def closestPoint(request,xcof,x1,y1):
    if request.method=='POST':
        xcof= int(request.POST["xcof"])
        x1 = int(request.POST["x1"])
        y1 = int(request.POST["y1"])
        return redirect("/find-the-point-on-the-parabola-y2-{0}x-that-is-closest-to-the-point-{1}-{2}/".format(xcof,str(x1),str(y1)))
    
    y1 = int(y1)
    x1 = int(x1)
    y = (xcof*y1)**(1/3)
    x = y**2/xcof

    randList1 = []
    for i in range(1,6):
        xi = x1+i
        yi = y1+i
        pair = str(xi)+"-"+str(yi)
        randList1.append(pair)
    randList2 = []
    for i in range(7,12):
        xi = x1+i
        yi = y1+i
        pair = str(xi)+"-"+str(yi)
        randList2.append(pair)
    context= {
        "y":round(y,2),
        "x":round(x,2),
        "x1":x1,
        "y1":y1,
        "xcof":xcof,
        "id":1,
        "randList1":randList1,
        "randList2":randList2
        
    }
    return render(request,"Deepak/point-on-the-parabola-calculator.html",context)


def pointOnTheSurfaceCalculator(request):
    if request.method=='POST':
        val= int(request.POST["value"])
        return redirect("/find-the-points-on-the-surface-y2-{}-xz-that-are-closest-to-the-origin/".format(val))   
    else:
        id = 0
        return render(request,"Deepak/find-the-point-on-the-surface-calculator.html")

def closestOrigin(request,val):
    if request.method=='POST':
        val= int(request.POST["value"])
        return redirect("/find-the-points-on-the-surface-y2-{}-xz-that-are-closest-to-the-origin/".format(val)) 
    value = int(val)
    y = math.sqrt(value)
    randList1 = []
    for i in range(1,6):
        val = value+i
        randList1.append(val)
    randList2 = []
    for i in range(7,12):
        val = value+i
        randList2.append(val)
    context= {
        "value":value,
        "y":round(y,2),
        "id":1,
        "randList1":randList1,
        "randList2":randList2
    }
    return render(request,"Deepak/find-the-point-on-the-surface-calculator-details.html",context)


def pointOnTheConeCalculator(request):
    if request.method=='POST':
        xval= int(request.POST["xval"])
        yval = int(request.POST["yval"])
        zval = int(request.POST["zval"])
        return redirect("/find-the-points-on-the-cone-z2-x2-y2-that-are-closest-to-the-point-{}-{}-{}/".format(xval,yval,zval))
    else:
        id = 0
        return render(request,"Deepak/find-the-point-on-the-cone-calculator.html")

def closestPoints(request,xval,yval,zval):
    if request.method=='POST':
        xval= int(request.POST["xval"])
        yval = int(request.POST["yval"])
        zval = int(request.POST["zval"])
        return redirect("/find-the-points-on-the-cone-z2-x2-y2-that-are-closest-to-the-point-{}-{}-{}/".format(xval,yval,zval))

    xval = int(xval) 
    yval = int(yval)
    zval = int(zval)
    txval = 2*xval
    tyval = 2*yval
    x = round(txval / 4)
    y = round(tyval/4)
    zv =z = x**2 + y**2
    
    if (type(math.sqrt(z))==int):
        z =  "±"+str(math.sqrt(z))
    else:
        z = "±√"+str(x**2 + y**2)

    randList1 = []
    for i in range(1,6):
        val = [xval+i,yval+i,zval]
        randList1.append(val)
    randList2 = []
    for i in range(7,12):
        val = [xval+i,yval+i,zval]
        randList2.append(val)
    context= {
        "xval":xval,
        "yval":yval,
        "zval":zval,
        "x":x,
        "y":y,
        "z":z,
        "zv":zv,
        "txval":txval,
        "tyval":tyval,
        "id":1,
        "randList1":randList1,
        "randList2":randList2
    }
    return render(request,"Deepak/find-the-point-on-the-cone-calculator-details.html",context)


##-------------------------------MADHAV-------------------------------
# areaOfTheParallelogramWithVertices
def randomGen(start,end):
    arr1=[]
    for i in range(0,15):
        temp=randint(start, end)
        if temp not in arr1:
            arr1.append(temp)
            if len(arr1)>=5:
                break
    return arr1

def areaOfTheParallelogramWithVertices(request):
    if request.method=='POST':
        try:
            x1 = request.POST.get('x1')
            y1 = request.POST.get('y1')
            x2 = request.POST.get('x2')
            y2 = request.POST.get('y2')
            x3 = request.POST.get('x3')
            y3 = request.POST.get('y3')
            x4 = request.POST.get('x4')
            y4 = request.POST.get('y4')

            return redirect(f'/area-of-the-parallelogram-with-vertices-a-{x1}-{y1}-b-{x2}-{y2}-c-{x3}-{y3}-and-d-{x4}-{y4}')          

        except Exception as e:
            # print(e)
            return render(request, 'Deepak/areaOfTheParallelogramWithVertices.html')

    return render(request, 'Deepak/areaOfTheParallelogramWithVertices.html')

def negVals(n):
    #print('n is: ',str(n)[0])
    if str(n)[0]=='-':
        print('in')
        return f'({n})' 
    else:
        return n

def areaOfTheParallelogramWithVerticesTail(request, **data):
      
    if request.method=='POST':
        try:
            x1 = request.POST.get('x1')
            y1 = request.POST.get('y1')
            x2 = request.POST.get('x2')
            y2 = request.POST.get('y2')
            x3 = request.POST.get('x3')
            y3 = request.POST.get('y3')
            x4 = request.POST.get('x4')
            y4 = request.POST.get('y4')
            print("MAINPAGE",x1)
            return redirect(f'/area-of-the-parallelogram-with-vertices-a-{x1}-{y1}-b-{x2}-{y2}-c-{x3}-{y3}-and-d-{x4}-{y4}')        
        except Exception as e:
            print(e)
            return render(request, 'Deepak/areaOfTheParallelogramWithVertices.html')
     
    else:
        # code for balancing -ve sign
        
        ct=0
        for i in data:
            if ct==1:
                data[i] = '-'+data[i]
                ct=0
            if data[i][len(data[i])-1] == '-':
                ct=1
                data[i] = data[i][:-1]

        #print("DETAILS",data['x1'])
        for i in data:
            data[i] = float(data[i])
            data[i] = float("{:.2f}".format(data[i])) if '.0' not in "{:.2f}".format(data[i]) else int("{:.0f}".format(data[i])) 
        
        step1 = f'''{negVals(data['x1'])}*({negVals(data['y2'])}-{negVals(data['y3'])}) + {negVals(data['x2'])}*({negVals(data['y3'])}-{negVals(data['y1'])}) + {negVals(data['x3'])}*({negVals(data['y1'])}-{negVals(data['y2'])})'''

        temp1 = data['y2']-data['y3']
        temp2 = data['y3']-data['y1']
        temp3 = data['y1']-data['y2']
        
        temp1 = data['x1']*temp1
        temp2 = data['x2']*temp2
        temp3 = data['x3']*temp3
       
        step2 = f'''[{negVals(temp1)} + {negVals(temp2)} + {negVals(temp3)}]'''

        sumAll = temp1 + temp2 + temp3
        step3 = negVals(sumAll)

        ans1 = abs(1/2*sumAll)
        ans1 = float("{:.2f}".format(ans1)) if '.0' not in "{:.2f}".format(ans1) else int("{:.0f}".format(ans1))
        step4 = ans1

        # triangle 2 acd
        step5 = f'''[{negVals(data['x1'])}*({negVals(data['y3'])}-{negVals(data['y4'])}) + {negVals(data['x3'])}*({negVals(data['y4'])}-{negVals(data['y1'])}) + {negVals(data['x4'])}*({negVals(data['y1'])}-{negVals(data['y3'])})]'''

        temp1 = data['y3']-data['y4']
        temp2 = data['y4']-data['y1']
        temp3 = data['y1']-data['y3']        

        temp1 = data['x1']*temp1
        temp2 = data['x3']*temp2
        temp3 = data['x4']*temp3
        step6 = f'''[{negVals(temp1)} + {negVals(temp2)} + {negVals(temp3)}]'''

        sumAll = temp1 + temp2 + temp3
        step7 = negVals(sumAll)

        ans2 = abs(1/2*sumAll)
        ans2 = float("{:.2f}".format(ans2)) if '.0' not in "{:.2f}".format(ans2) else int("{:.0f}".format(ans2))
        step8 = ans2
        
        ans = ans1 + ans2
        ans = float("{:.2f}".format(ans)) if '.0' not in "{:.2f}".format(ans) else int("{:.0f}".format(ans))

        point1 = randomGen(0,10)
        point2 = randomGen(10,20)
        point3 = randomGen(20,30)
        point4 = randomGen(30,40)
        relatedP1 = zip(point1,point2,point3,point4)

        point5 = randomGen(40,50)
        point6 = randomGen(50,60)
        point7 = randomGen(60,70)
        point8 = randomGen(70,80)
        relatedP2 = zip(point1,point2,point3,point4,point5,point6,point7,point8)

        data['step1'] = step1
        data['step2'] = step2
        data['step3'] = step3
        data['step4'] = step4
        data['step5'] = step5
        data['step6'] = step6
        data['step7'] = step7
        data['step8'] = step8
        data['id'] = 1
        data['ans'] = ans
        data['relatedP1'] = relatedP1
        data['relatedP2'] = relatedP2

        # input1 = data
        # print(data)
        x1 = data['x1']
        y1 = data['y1']
        x2 = data['x2']
        y2 = data['y2']
        x3 = data['x3']
        y3 = data['y3']
        x4 = data['x4']
        y4 = data['y4']
        print(x1)
        query=areaOfTheParallelogramCalculator.objects.filter(inputEnter=str(data))
        if len(query)==0:
            solutionTitle="What is the Area of the Parallelogram with Vertices Calculator?"
            detailStep=f'''<p>The vertices of a parallelogram are a(data['x1'], data['y1']), b(data['x2'],data['y2']), c(data['x3'],data['y3']), d(data['x4'],data['y4']) and Area of triangle S=[x1(y2−y3)+x2(y3−y1)+x3(y1−y2)]/2. So, Area of parallelogram = {ans} sq units.</p>'''
            finalAnswer=(ans)
            obj=areaOfTheParallelogramCalculator(inputEnter=str(data),solutionTitle=solutionTitle,detailStep=detailStep,finalAnswer=finalAnswer,slug=f'/area-of-the-parallelogram-with-vertices-a-{x1}-{y1}-b-{x2}-{y2}-c-{x3}-{y3}-and-d-{x4}-{y4}/',date_modified=datetime.now())
            obj.save()

    return render(request, 'Deepak/areaOfTheParallelogramWithVerticesTail.html', data)
 





##-------------------------------JJJJJJJJJJJJJKKKKKKK-------------------------------


def coordinatesshapecalculator(request):
    print(request.POST)
    if request.POST:
        x1 = request.POST['x1']
        y1 = request.POST['y1']
        x2 = request.POST['x2']
        y2 = request.POST['y2']
        x3 = request.POST['x3']
        y3 = request.POST['y3']
        x4 = request.POST['x4']
        y4 = request.POST['y4']

        # return redirect(f'/square-root-of-{aa}-by-{bb}/') 
        # messages.error(request,"I am a message")
        return redirect(f'/when-the-coordinates-{x1}-{y1}-{x2}-{y2}-{x3}-{y3}-{x4}-{y4}-are-joined-which-shape-is-formed/') 
    return render(request,'Deepak/coordinatesshapecalculator.html')    

        # # importing the required module
        # import matplotlib.pyplot as plt

        # # x axis values
        # x = [0,6,10,4,0]

        # # corresponding y axis values
        # y = [14,16,4,2,14]

        # # dist = math.hypot(x2 - x1, y2 - y1)

        # print(math.hypot(x[1] - x[0], y[1] - y[0]))
        # print(math.hypot(x[2] - x[1], y[2] - y[1]))
        # print(math.hypot(x[3] - x[2], y[3] - y[2]))
        # print(math.hypot(x[4] - x[3], y[4] - y[3]))

        # # import math

        # def dot(vA, vB):
        #     return vA[0]*vB[0]+vA[1]*vB[1]

        
        
        
        # def ang(lineA, lineB):
        #     # Get nicer vector form
        #     vA = [(lineA[0][0]-lineA[1][0]), (lineA[0][1]-lineA[1][1])]
        #     vB = [(lineB[0][0]-lineB[1][0]), (lineB[0][1]-lineB[1][1])]
        #     # Get dot prod
        #     dot_prod = dot(vA, vB)
        #     # Get magnitudes
        #     magA = dot(vA, vA)**0.5
        #     magB = dot(vB, vB)**0.5
        #     # Get cosine value
        #     cos_ = dot_prod/magA/magB
        #     # Get angle in radians and then convert to degrees
        #     angle = math.acos(dot_prod/magB/magA)
        #     # Basically doing angle <- angle mod 360
        #     ang_deg = math.degrees(angle)%360

        #     if ang_deg-180>=0:
        #         # As in if statement
        #         return 360 - ang_deg
        #     else: 
        #         return ang_deg

        
        # print(ang(((-3, 5), (3, 7)), ((3, 7), (6, -2))))
        
        # plt.plot(x, y, color='green', linewidth = 3,
        # marker='o', markerfacecolor='blue', markersize=12)
        # plt.xlabel('x - axis')
        # plt.ylabel('y - axis')
        # plt.title('My first graph!')
        # plt.show()



        # return render(request,'coordinatesshapecalculator.html')
    



def coordinatesshapecalculatordetails(request,x1,y1,x2,y2,x3,y3,x4,y4):
    try:
        print(request)
        # print(messages.error)
        
        
            

        print(f'{x1=},{y1=},{x2=},{y2=},{x3=},{y3=},{x4=},{y4=}')

        if x1[-1] == '-':
            # print("i am x-1")
            x1 = float(x1.rstrip('-'))
            a = 'minus'
        else:
            x1 = float(x1)
            a = 'plus'

        if '-' in y1:
            y1 = y1.strip('-')
            b = 'minus'
        else:
            b = 'plus'

        if '-' in x2:
            x2 = x2.strip('-')
            c = 'minus'
        else:
            c = 'plus'

        if '-' in y2:
            y2 = y2.strip('-')
            d = 'minus'
        else:
            d = 'plus'

        if '-' in x3:
            x3 = x3.strip('-')
            e = 'minus'
        else:
            e = 'plus'

        if '-' in y3:
            y3 = y3.strip('-')
            f = 'minus'
        else:
            f = 'plus'

        if '-' in x4:
            x4 = x4.strip('-')
            g = 'minus'
        else:
            g = 'plus'

        # if '-' in y4:
        #     y4 = y4.strip('-')
        #     h = 'minus'
        # else:
        #     h = 'plus'

        print(f'{x1=},{y1=},{x2=},{y2=},{x3=},{y3=},{x4=},{y4=}')
        print(f'{a=},{b=},{c=},{d=},{e=},{f=},{g=}')
        if a == 'minus':
            y1 = float('-'+ y1)
        else:
            y1 = float(y1)

        if b == 'minus':
            x2 = float('-'+ x2)
        else:
            x2 = float(x2)

        if c == 'minus':
            y2 = float('-'+ y2)
        else:
            y2 = float(y2)

        if d == 'minus':
            x3 = float('-'+ x3)
        else:
            x3 = float(x3)

        if e == 'minus':
            y3 = float('-'+ y3)
        else:
            y3 = float(y3)

        if f == 'minus':
            x4 = float('-'+ x4)
        else:
            x4 = float(x4)

        if g == 'minus':
            y4 = float('-'+ y4)
        else:
            y4 = float(y4)

        if x1 == int(x1):x1 = int(x1)
        if y1 == int(y1):y1 = int(y1)
        if x2 == int(x2):x2 = int(x2)
        if y2 == int(y2):y2 = int(y2)
        if x3 == int(x3):x3 = int(x3)
        if y3 == int(y3):y3 = int(y3)
        if x4 == int(x4):x4 = int(x4)
        if y4 == int(y4):y4 = int(y4)

        print(f'{x1=},{y1=},{x2=},{y2=},{x3=},{y3=},{x4=},{y4=}')

        query=coordinatesh.objects.filter(inputEnter=f'{x1},{y1},{x2},{y2},{x3},{y3},{x4},{y4}')
        if len(query)!=0:
            context={
                'x1':x1,
                'y1':y1,
                'x2':x2,
                'y2':y2,
                'x3':x3,
                'y3':y3,
                'x4':x4,
                'y4':y4,
                'detailsteps':query[0].detailStep,
                'shape':query[0].finalAnswer,
                        
                }
            print("I am Database Database Database")
            return render(request,'Deepak/coordinatesshapecalculatordetails.html',context)

            

        a,b,c,d = (x1,y1),(x2,y2),(x3,y3),(x4,y4)


        #for Square  #for Square  #for Square  #for Square  #for Square  #for Square
        def vertices(h,f):
            return math.sqrt((f[0]-h[0])**2 + (f[1]-h[1])**2)

        # Vertices
        ab = vertices(a,b)
        bc = vertices(b,c)
        cd = vertices(c,d)
        ad = vertices(a,d)
        print(f'{ab=},{bc=},{cd=},{ad=}')

        # Diagonals
        ac = vertices(a,c)
        bd = vertices(b,d)  
        print(f'{ac=},{bd=}')

        if ab == bc and bc == cd and cd == ad and ac == bd:

            detailsteps = f''' <p>Given coordinates are A({x1}, {y1}), B({x2}, {y2}), C({x3}, {y3}), and D({x4}, {y4})</p>

            <p>d = √(x<sub>2</sub>-x<sub>1</sub>)<sup>2</sup>+(y<sub>2</sub>-y<sub>1</sub>)<sup>2</sup></p>

            
            <p><strong>Vertices</strong></p>
            <p>AB = √({x2}-{x1})<sup>2</sup>+({y2}-{y1})<sup>2</sup> = √{(x2-x1)**2+(y2-y1)**2}</p>
            <p>BC = √({x3}-{x2})<sup>2</sup>+({y3}-{y2})<sup>2</sup> = √{(x3-x2)**2+(y3-y2)**2}</p>
            <p>CD = √({x4}-{x3})<sup>2</sup>+({y4}-{y3})<sup>2</sup> = √{(x4-x3)**2+(y4-y3)**2}</p>
            <p>AD = √({x4}-{x1})<sup>2</sup>+({y4}-{y1})<sup>2</sup> = √{(x4-x1)**2+(y4-y1)**2}</p>

            <p><strong>Diagonals</strong></p>
            <p>AC = √({x3}-{x1})<sup>2</sup>+({y3}-{y1})<sup>2</sup> = √{(x3-x1)**2+(y3-y1)**2}</p>
            <p>BD = √({x4}-{x2})<sup>2</sup>+({y4}-{y2})<sup>2</sup> = √{(x4-x2)**2+(y4-y2)**2}</p>

            <p style="color:green"><strong>Since lenghts of sides are same and lengths of diagonals are same, they form a square.</strong></p>

            '''
            obj=coordinatesh(inputEnter=f'{x1},{y1},{x2},{y2},{x3},{y3},{x4},{y4}',finalAnswer="square",detailStep=detailsteps,slug=f"/when-the-coordinates-{x1}-{y1}-{x2}-{y2}-{x3}-{y3}-{x4}-{y4}-are-joined-which-shape-is-formed/",solutionTitle='title')
            obj.save()

            context = {
                'x1':x1,
                'y1':y1,
                'x2':x2,
                'y2':y2,
                'x3':x3,
                'y3':y3,
                'x4':x4,
                'y4':y4,
                "detailsteps":detailsteps,
                'shape':'square',
            }
            print("I am square")
            return render(request,'Deepak/coordinatesshapecalculatordetails.html',context)
        
        #for rectangle AB2 + AD2 = BD2
        if ab == cd and bc == ad and (ab**2) + (ad**2) == bd**2:
        # if (ab**2) + (ad**2) == bd**2:
            print("I am a rectangle")

            print("(ab**2) + (ad**2) = ",(ab**2) + (ad**2))
            print("bd**2 = ",bd**2)


            detailsteps = f''' <p>Given coordinates are A({x1}, {y1}), B({x2}, {y2}), C({x3}, {y3}), and D({x4}, {y4})</p>

            <p>d = √(x<sub>2</sub>-x<sub>1</sub>)<sup>2</sup>+(y<sub>2</sub>-y<sub>1</sub>)<sup>2</sup></p>

            
            <p><strong>Vertices</strong></p>
            <p>AB = √({x2}-{x1})<sup>2</sup>+({y2}-{y1})<sup>2</sup> = √{(x2-x1)**2+(y2-y1)**2}</p>
            <p>BC = √({x3}-{x2})<sup>2</sup>+({y3}-{y2})<sup>2</sup> = √{(x3-x2)**2+(y3-y2)**2}</p>
            <p>CD = √({x4}-{x3})<sup>2</sup>+({y4}-{y3})<sup>2</sup> = √{(x4-x3)**2+(y4-y3)**2}</p>
            <p>AD = √({x4}-{x1})<sup>2</sup>+({y4}-{y1})<sup>2</sup> = √{(x4-x1)**2+(y4-y1)**2}</p>


            <p><strong>Consider ΔABD</strong></p>
            
            <p>BD = √({x4}-{x2})<sup>2</sup>+({y4}-{y2})<sup>2</sup> = √{(x4-x2)**2+(y4-y2)**2}</p>
            <p>BD = √{(x4-x2)**2+(y4-y2)**2}</p>
            <p>BD<sup>2</sup> = {(x4-x2)**2+(y4-y2)**2}</p>

            <p>AB<sup>2</sup> = {(x2-x1)**2+(y2-y1)**2}</p>

            <p>AD<sup>2</sup> = {(x4-x1)**2+(y4-y1)**2}</p>

            <p>{(x2-x1)**2+(y2-y1)**2} + {(x4-x1)**2+(y4-y1)**2} = {(x4-x2)**2+(y4-y2)**2} </p>

            <p>AB<sup>2</sup> + AD<sup>2</sup> = BD<sup>2</sup></p>


            <p style="color:green"><strong>From the above workings, AB = CD and AD = BC.<br>ΔABD above satisfies Pythagorean Theorem, hence ΔABD is a right triangle with ∠A = 90°.<br>Opposite sides are equal and it is proved that one of the vertices has right angle.<br>So, the given four points form a rectangle.  </strong></p>

            '''
            obj=coordinatesh(inputEnter=f'{x1},{y1},{x2},{y2},{x3},{y3},{x4},{y4}',finalAnswer="rectangle",detailStep=detailsteps,slug=f"/when-the-coordinates-{x1}-{y1}-{x2}-{y2}-{x3}-{y3}-{x4}-{y4}-are-joined-which-shape-is-formed/",solutionTitle='title')
            obj.save()

            context = {
                'x1':x1,
                'y1':y1,
                'x2':x2,
                'y2':y2,
                'x3':x3,
                'y3':y3,
                'x4':x4,
                'y4':y4,
                "detailsteps":detailsteps,
                'shape':'rectangle',
            }
            print("I am rectangle")
            return render(request,'Deepak/coordinatesshapecalculatordetails.html',context)



        #for Parallelogram
        midpointAC = (x1+x3)/2,(y1+y3)/2
        midpointBD = (x2+x4)/2,(y2+y4)/2
        print(type(midpointBD))
        print(f'{midpointAC = },{midpointBD = }')
        if ab == cd and bc == ad and midpointAC[0] == midpointBD[0] and midpointAC[1] == midpointBD[1]:
            print("I am a parallelogram")

            detailsteps = f''' <p>Given coordinates are A({x1}, {y1}), B({x2}, {y2}), C({x3}, {y3}), and D({x4}, {y4})</p>

            <p>d = √(x<sub>2</sub>-x<sub>1</sub>)<sup>2</sup>+(y<sub>2</sub>-y<sub>1</sub>)<sup>2</sup></p>

            
            <p><strong>Vertices</strong></p>
            <p>AB = √({x2}-{x1})<sup>2</sup>+({y2}-{y1})<sup>2</sup> = √{(x2-x1)**2+(y2-y1)**2}</p>
            <p>BC = √({x3}-{x2})<sup>2</sup>+({y3}-{y2})<sup>2</sup> = √{(x3-x2)**2+(y3-y2)**2}</p>
            <p>CD = √({x4}-{x3})<sup>2</sup>+({y4}-{y3})<sup>2</sup> = √{(x4-x3)**2+(y4-y3)**2}</p>
            <p>AD = √({x4}-{x1})<sup>2</sup>+({y4}-{y1})<sup>2</sup> = √{(x4-x1)**2+(y4-y1)**2}</p>


            <p><strong>Midpoint of diagonals: =  (x<sub>1</sub> + x<sub>2</sub>)/2, (y<sub>1</sub> + y<sub>2</sub>)/2</strong></p>

            <p>Midpoint of diagonal AC :</p>
            <p>({x1}+{x3}/2),({y1}+{y3}/2)</p>
            <p>({x1+x3}/2),({y1+y3}/2)</p>
            <p>({(x1+x3)/2},{(y1+y3)/2})</p>

            <p>Midpoint of diagonal BD :</p>
            <p>({x2}+{x4}/2),({y2}+{y4}/2)</p>
            <p>({x2+x4}/2),({y2+y4}/2)</p>
            <p>({(x2+x4)/2},{(y2+y4)/2})</p>
            


            <p style="color:green"><strong>Since the midpoint of diagonals are equal, the given points form a parallelogram.<br>Length of opposite sides are equal. So the given vertices forms a parallelogram.</strong></p>

            '''
            obj=coordinatesh(inputEnter=f'{x1},{y1},{x2},{y2},{x3},{y3},{x4},{y4}',finalAnswer="parallelogram",detailStep=detailsteps,slug=f"/when-the-coordinates-{x1}-{y1}-{x2}-{y2}-{x3}-{y3}-{x4}-{y4}-are-joined-which-shape-is-formed/",solutionTitle='title')
            obj.save()

            context = {
                'x1':x1,
                'y1':y1,
                'x2':x2,
                'y2':y2,
                'x3':x3,
                'y3':y3,
                'x4':x4,
                'y4':y4,
                "detailsteps":detailsteps,
                'shape':'parallelogram',
            }
            print("I am parallelogram")
            return render(request,'Deepak/coordinatesshapecalculatordetails.html',context)
        print("I am the end")  
        messages.error(request,'Given coordinates do not form a square, rectangle or parallelogram.') 
        # messages.add_message(request, messages.INFO, 'There has been an error...')
        return redirect('/coordinates-shape-calculator/')
        # return redirect(f'/coordinates-shape-calculator/')
    except:
        messages.error(request,'Invalid Inputs.') 
        return redirect('/coordinates-shape-calculator/')

    

def horizontaltangent(request):
    print(request.POST)
    if request.POST:
        equat = request.POST['equat']

        return redirect(f'/find-points-on-the-curve-{equat}-where-the-tangent-is-horizontal/')
    return render(request,'Deepak/horizontaltangent.html') 




def detailshorizontaltangent(request, equat):
    try:
        x, y = symbols('x y')
        query=HorizontalTangent.objects.filter(inputEnter=equat)
        if len(query)!=0:
            # obj=HorizontalTangent(inputEnter=equat, finalAnswer=result1,detailStep=detailsteps,slug=f"/find-points-on-the-curve-{equat}-where-the-tangent-is-horizontal/",solutionTitle=result2,eq1=eq1)
            context={
                    'eq1':query[0].eq1,
                    'result1':query[0].finalAnswer,
                    'result2':query[0].solutionTitle,
                    'detailsteps':query[0].detailStep,
                    'equat':query[0].inputEnter,
                    "exp1":latex(sympify(16*(x**-1)-x**2)),
                    "exp2":latex(sympify(sin(x)))
                            
                    }

            
            print("I am Database Database Database")
            return render(request,'Deepak/detailshorizontaltangent.html',context)

        # x, y = symbols('x y')
        print(f'{equat=}')

        #converting input string into expression
        expr = sympify(equat)
        print("Expression : {} ".format(expr))

        #creating latex of the expression
        eq1 = latex(expr)
        print(f'{eq1=}')

        
        #Derivative of expression with respect to x
        expr_diff = Derivative(expr, x) 
        print("Derivative of expression with respect to x : {}".format(expr_diff)) 

        #Value of the derivative
        print("Value of the derivative : {} ".format(expr_diff.doit()))

        #creating latex
        eq2 =  latex(expr_diff.doit(),0)   
        print(f'{eq2=}')

        
        #solving equation
        xvalues = solve(Eq(expr_diff.doit(),0))
        print(f'{xvalues=}')
    

        print(expr)
        # print(str(expr).replace('x',str(xvalues[0])))
        eq3 = latex(str(expr).replace('x',str(xvalues[0])))
        print(f'{eq3=}')
        print(latex(sympify(equat.replace('x',str(xvalues[0])))))

    
        #substituting value of x in equation        
        a,b = expr.subs(x,str(xvalues[0])), expr.subs(x,str(xvalues[1]))
        print(a)
        print(b)
        result1 = f'{xvalues[0]},{a}'
        result2 = f'{xvalues[1]},{b}'


        detailsteps = f'''<p>Given curve is y=\({eq1}\)</p>

                <p>Let us first start by understanding that the slope can be found by finding the first differential of the equation of the curve.</p>

                <p>dy/dx = \({eq2}\)</p>

                <p>Therefore, the slope is equal to \({eq2}\). If the tangent is horizontal, then the slope of the tangent will be 0</p>
                
                <p>\({eq2}\)= 0</p>

                <p>Now, solve this equation to find x, which are the roots.</p>

                <p>\({eq2}\)= 0</p>



                <p>So, the two roots are as follows.</p>


                <p>x = {xvalues[0]}</p>


                <p>x = {xvalues[1]}</p>


                <p>Then, it is time to find the y coordinates of the points. To do so, we have to plug the x values that we just found into the equation of the curve and find y.</p>


                <p>y=\({eq1}\)</p>


                <p>If x = {xvalues[0]}, then the y value can be found like this.</p>


                <p>y = {a}</p>


                <p>Therefore, the coordinates of the first point are ({xvalues[0]}, {a}).</p>


                <p>If x = {xvalues[1]}, then the y value can be found like this.</p>


                <p>y = {b}</p>


                <p>Thus, the coordinates of the second point are ({xvalues[1]}, {b}).</p>


                <p>In conclusion, the two points on the curve y=\({eq1}\) where the tangent is horizontal, are ({xvalues[0]}, {a}) and ({xvalues[1]}, {b}).</p>


                <p></p>'''


        obj=HorizontalTangent(inputEnter=equat, finalAnswer=result1,detailStep=detailsteps,slug=f"/find-points-on-the-curve-{equat}-where-the-tangent-is-horizontal/",solutionTitle=result2,eq1=eq1)
        obj.save()

        context = {
                "eq1":eq1,
                "result1":result1,
                "result2":result2,
                "detailsteps":detailsteps,
                "equat":equat,
                "exp1":latex(sympify(16*(x**-1)-x**2)),
                "exp2":latex(sympify(sin(x)))

            }

            
        return render(request,'Deepak/detailshorizontaltangent.html',context)
    except:
        messages.error(request,'Invalid Inputs') 
        return redirect('/horizontal-tangent-points-on-curve-calculator/')

        



##-------------------------------ABHINANDAN-------------------------------
# Additive inverse
def additiveInverseOfComplexNumberDetails(request, num1, num2):
    if request.method == 'POST':
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        return redirect(f'/additive-inverse-of-complex-number-{aa}-{bb}i/')
    
    randList1=random_with_single_digits(1,20)
    randList2=random_with_single_digits(20,70)
    all1 = list(zip(randList1,randList2))

    randList3=random_with_single_digits(10,50)
    randList4=random_with_single_digits(50,100)
    all2 = list(zip(randList3,randList4)) 
    
    
    
    context = {
            'ans':0,
            'ans1':0,
            'bb':num2,
            'aa':num1,
            'ab':2,
            'xy':2,
            'check':True,
            'dict1':dict(),
            'dict2':dict(),
            'dict3':dict(),
            'dict4':dict(),
            'all1':all1,
            'all2':all2,
            'id':1,
        }
    return render(request, 'Deepak/additive-inverse-of-complex-number-details.html', context)


def additiveInverseOfComplexNumber(request):
    
    if request.method == 'POST':
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp.isdigit(): 
                aa=int(request.POST.get('aa'))
            else:
                aa=float(request.POST.get('aa'))
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp.isdigit(): 
                bb=int(request.POST.get('bb'))
            else:
                bb=float(request.POST.get('bb'))
        else:
            bb=None

        return redirect(f'/additive-inverse-of-complex-number-{aa}-{bb}i/') 
      
    
    return render(request, 'Deepak/additive-inverse-of-complex-number.html')

def findFirstSixTermOfSequence(request):
    if request.method == 'POST':
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            
            if inp[0] == '-':
                aa = int(inp[1:])*-1
            elif inp[0] == '+':
                aa = int(inp[1:])
            else:
                aa=int(inp)
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp[0] == '-':
                bb = int(inp[1:])*-1
            elif inp[0] == '+':
                bb = int(inp[1:])
            else:
                bb=int(inp)
        else:
            bb=None

        return redirect(f'/find-first-six-term-of-the-sequence-a1={aa}-an={bb}an-1/')
    
    return render(request, 'Deepak/find-first-six-term-of-the-sequence.html')

def findFirstSixTermOfSequenceDetails(request, aa, bb):
    if request.method == 'POST':
        #VALUE FOR THE no--------------------------------------------------
        if request.POST.get('aa')!=None and request.POST.get('aa')!='' :
            inp=str(request.POST.get('aa'))
            if inp[0] == '-':
                aa = int(inp[1:])*-1
            elif inp[0] == '+':
                aa = int(inp[1:])
            else:
                aa=int(inp)
        else:
            aa=None

        if request.POST.get('bb')!=None and request.POST.get('bb')!='' :
            inp=str(request.POST.get('bb'))
            if inp[0] == '-':
                bb = int(inp[1:])*-1
            elif inp[0] == '+':
                bb = int(inp[1:])
            else:
                bb=int(inp)
        else:
            bb=None

        return redirect(f'/find-first-six-term-of-the-sequence-a1={aa}-an={bb}an-1/')

    else:
    
        if aa[0] == '-':
            aa = int(aa[1:])*-1
        elif aa[0] == '+':
            aa = int(aa[1:])
        else:
            aa=int(aa)
        
        if bb[0] == '-':
            bb = int(bb[1:])*-1
        elif bb[0] == '+':
            bb = int(bb[1:])
        else:
            bb=int(bb)
        
        firstSixTerm = [aa]
        for i in range(6):
            firstSixTerm.append(firstSixTerm[i]*bb)
        

        randList1=random_with_single_digits(1,20)
        randList2=random_with_single_digits(20,70)
        all1 = list(zip(randList1,randList2))

        randList3=random_with_single_digits(10,50)
        randList4=random_with_single_digits(50,100)
        all2 = list(zip(randList3,randList4))    
        
    
    
    context = {
            'ans':{'a1':firstSixTerm[0], 'a2':firstSixTerm[1], 'a3':firstSixTerm[2], 'a4':firstSixTerm[3], 'a5':firstSixTerm[4], 'a6':firstSixTerm[5], 'a7':firstSixTerm[6]},
            'ans1':0,
            'bb':bb,
            'aa':aa,
            'ab':2,
            'xy':2,
            'check':True,
            'dict1':dict(),
            'dict2':dict(),
            'dict3':dict(),
            'dict4':dict(),
            'all1':all1,
            'all2':all2,
            'id':1,
        }
    
    return render(request, 'Deepak/find-first-six-term-of-the-sequence-details.html', context)


