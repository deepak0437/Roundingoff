from .models import *
import math
from fractions import Fraction


def atsequenceutility(func):
    if atsequence.objects.filter(func=func):
        return atsequence.objects.filter(func=func)
    l=func.replace("^",'**')
    l=func.replace("÷",'/')

    _=''
    for i in l:
        if i.isalpha() and i not in _:
            _+=i+','
    _=_[0:-1]
    from sympy import S
    _=S(_)
    try:
        for i in range(0,len(_)):
            if str(_[i]) in l:
                l=l.replace(str(_[i]),'_['+str(i)+']')   
    except:
         if str(_) in l:
                l=l.replace(str(_),'_')
    d={}
    print(l)
    try:
        code='from sympy import S\nfrom sympy.calculus.util import continuous_domain\n'
        code+='function='+l
        code+='\na=(continuous_domain(function, _, S.Naturals))'
        exec(code,{'_':_},d)
        val=d['a']
        print(val)
    except:
        val ='Syntax Error'
    ins=atsequence(func=func,solution=val)
    ins.save()
    return atsequence.objects.filter(func=func)

def distancebtweenpoints(point1,point2):
    point1=point1.replace(' ','').replace('(','').replace(')','')
    point2=point2.replace(' ','').replace('(','').replace(')','')
    point1l=list(point1.split(','))
    point2l=list(point2.split(','))
    d=str(((int(point2l[0])-int(point1l[0]))**2)+((int(point2l[1])-int(point1l[1]))**2))
    steps='<p>Here, x<sub>1</sub> = '+point1l[0]+', y<sub>1</sub> = '+point1l[1]+'; x<sub>2</sub> = '+point2l[0]+'; y<sub>2</sub> = '+point2l[1]+'</p>'
    steps+='<p>d = √('+point2l[0]+') - ('+point1l[0]+'))<sup>2</sup> + ('+point2l[1]+' - '+point1l[1]+')<sup>2</sup></p>'
    steps+='<p>d = √'+str(int(point2l[0])-int(point1l[0]))+'<sup>2</sup>  + '+str(int(point2l[1])-int(point1l[1]))+'<sup>2</sup></p>'
    steps+='<p>d = √'+str((int(point2l[0])-int(point1l[0]))**2)+' + '+str((int(point2l[1])-int(point1l[1]))**2)+'</p>'
    steps+='<p>d = √'+d+'units</p>'
    point1='('+point1+')'
    point2='('+point2+')'
    ins=distanceBetweenPoints(point1=point1,point2=point2,d=d,steps=steps)
    ins.save()



from sympy import *
def intercept(eqn):
    if interceptForm.objects.filter(eqn= eqn):
        return interceptForm.objects.filter(eqn= eqn) 

    print(eqn)
    smpl=list(eqn.split('='))
    smpl=smpl[0]+'-('+smpl[1]+')'
    from latex2sympy2 import latex2sympy, latex2latex
    smpl=latex2sympy(smpl)
    print(smpl)
    x = symbols('x')
    y = symbols('y')
    smpl=expand(smpl,evaluate=False)
    smpl = simplify(smpl)

    cox=smpl.coeff('x')
    cox*=(-1)
    coy=smpl.coeff('y')
    cons= smpl.func(*[term for term in smpl.args if not term.free_symbols])
    cons*=(-1)
    slope=round((cox/coy),4)
    result='y=('+str(slope)+'x'+str(cons)+'/'+str(coy)
    ins=interceptForm(eqn=eqn,cox=cox,coy=coy,cons=cons,slope=slope,result=result)       
    ins.save()
    return interceptForm.objects.filter(eqn= eqn)

def area_of_triangle(a,b,c):
    if aot.objects.filter(a= a,b=b,c=c):
        return aot.objects.filter(a=a,b=b,c=c)
    l=list(a.split(','))
    l.extend(list(b.split(',')))
    l.extend(list(c.split(',')))
    for i in range(len(l)):
        if int(l[i])>=0:
            l[i]=' '+l[i]
    steps='<p>1/2|'+l[0]+l[1]+' 1|</p>'
    steps+='<p>   |'+l[2]+l[3]+' 1|</p>'
    steps+='<p>   |'+l[4]+l[5]+' 1|</p>'
    steps+='<p>'+'=1/2[('+l[0]+')*(('+l[3]+')-('+l[5]+'))-('+l[2]+')*(('+l[1]+')-('+l[5]+')+('+l[4]+')*(('+l[1]+')-('+l[3]+'))]'+'</p>'
    steps+='<p>'+'=1/2[('+l[0]+')*('+str(float(l[3])-float(l[5]))+')-('+l[2]+')*('+str(float(l[1])-float(l[5]))+')+('+l[4]+')*('+str(float(l[1])-float(l[3]))+')]'+'</p>'
    steps+='<p>'+'=1/2[('+str(float(l[0])*float(str(float(l[3])-float(l[5]))))+')-('+str(float(l[2])*float(str(float(l[1])-float(l[5]))))+')+('+str(float(l[4])*float(str(float(l[1])-float(l[3]))))+')]'+'</p>'
    steps+='<p>'+'=1/2['+str(float(str(float(l[0])*float(str(float(l[3])-float(l[5])))))-float(str(float(l[2])*float(str(float(l[1])-float(l[5])))))+float(str(float(l[4])*float(str(float(l[1])-float(l[3]))))))+']'+'</p>'
    steps+='<p>='+str(float(str(float(str(float(l[0])*float(str(float(l[3])-float(l[5])))))-float(str(float(l[2])*float(str(float(l[1])-float(l[5])))))+float(str(float(l[4])*float(str(float(l[1])-float(l[3])))))))*0.5)+'sq units</p>'
    result=abs(float(str(float(str(float(l[0])*float(str(float(l[3])-float(l[5])))))-float(str(float(l[2])*float(str(float(l[1])-float(l[5])))))+float(str(float(l[4])*float(str(float(l[1])-float(l[3])))))))*0.5)
    ins=aot(a=a,b=b,c=c,steps=steps,result=result)       
    ins.save()
    return aot.objects.filter(a=a,b=b,c=c)

def max_area_rectangle(perim):
    perim=float(perim)
    if maxAreaRectangle.objects.filter(perim=perim):
        return maxAreaRectangle.objects.filter(perim=perim)
    hp=perim/2
    qp=hp/2
    ar=qp**2
    ins=maxAreaRectangle(perim=perim,halfperim=hp,quatperim=qp,area=ar)       
    ins.save()
    return maxAreaRectangle.objects.filter(perim=perim)

def sqr_sim(und_root):
    und_root = int(und_root)
    und_root0 = round(und_root)
    rt_fc = []
    coef = 1
    if und_root < 0:
        return None
    elif und_root == 0:
        return 0
    else:
        for i in range(2, und_root0):
            if und_root%(i**2) == 0:
                rt_fc.append(i)
                und_root /= i**2

                for i0 in range(2, und_root0):
                    if und_root%(i0**2) == 0:
                        rt_fc.append(i0)
                        und_root /= i0**2

        for ele in rt_fc:
            coef *= ele
        return(str(coef)+'√'+str(und_root))

def distancebtweenpointsdeci(point1,point2):
    point1=point1.replace(' ','').replace('(','').replace(')','')
    point2=point2.replace(' ','').replace('(','').replace(')','')
    point1l=list(point1.split(','))
    point2l=list(point2.split(','))
    d=str(round(((float(point2l[0])-float(point1l[0]))**2)+((float(point2l[1])-float(point1l[1]))**2),4))
    steps='<p>Here, x<sub>1</sub> = '+point1l[0]+', y<sub>1</sub> = '+point1l[1]+'; x<sub>2</sub> = '+point2l[0]+'; y<sub>2</sub> = '+point2l[1]+'</p>'
    steps+='<p>d = √('+point2l[0]+') - ('+point1l[0]+'))<sup>2</sup> + ('+point2l[1]+' - '+point1l[1]+')<sup>2</sup></p>'
    steps+='<p>d = √'+str(float(point2l[0])-float(point1l[0]))+'<sup>2</sup>  + '+str(float(point2l[1])-float(point1l[1]))+'<sup>2</sup></p>'
    steps+='<p>d = √'+str((float(point2l[0])-float(point1l[0]))**2)+' + '+str((float(point2l[1])-float(point1l[1]))**2)+'</p>'
    steps+='<p>d = √'+d+'units</p>'
    point1='('+point1+')'
    point2='('+point2+')'
    ins=distanceBetweenPoints(point1=point1,point2=point2,d=d,steps=steps)
    ins.save()



