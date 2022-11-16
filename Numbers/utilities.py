from .models import *
import math
from fractions import Fraction

def atsequenceutility(func):
    if atsequence.objects.filter(func=func):
        return atsequence.objects.filter(func=func)
    l=func.replace("^",'**')
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
    try:
        code='from sympy import S\nfrom sympy.calculus.util import continuous_domain\n'
        code+='function='+l
        code+='\na=(continuous_domain(function, _, S.Naturals))'
        exec(code,{'_':_},d)
        val=d['a']
    except:
        val =' Syntax Error'
    ins=atsequence(func=func,solution=val)
    ins.save()
    return atsequence.objects.filter(func=func)

    