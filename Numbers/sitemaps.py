from django.contrib.sitemaps import Sitemap
from .urls import urlpatterns
from django.shortcuts import reverse
from datetime import datetime
from django.contrib import admin
from django.urls import path, include 
from .models import *



class percenttToDecimalCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return percenttToDecimalCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    


class decimalToPercentageCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return decimalToPercentageCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    



class moduloCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return moduloCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    


class dividedByWhatCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return dividedByWhatCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    

class negativeDividedCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return negativeDividedCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    

class millionzerosCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return millionzerosCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class billionzerosCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return billionzerosCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    

class crorezerosCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return crorezerosCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified   

class croreinnumberCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return croreinnumberCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified    

class decimaltobinaryCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return decimaltobinaryCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class decimalplacevalueCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return decimalplacevalueCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class addingfractionCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return addingfractionCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class multiplyingfractionCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return multiplyingfractionCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class dividingfractionCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return dividingfractionCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  

class mixedfractionCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return mixedfractionCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  

class threedigitnumberCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return threedigitnumberCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  

class fourdigitnumberCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return fourdigitnumberCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class whatisnextfibonacciCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return whatisnextfibonacciCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 


class howdoyouaddpercenttonumberCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return howdoyouaddpercenttonumberCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class greatestcommondivisorCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return greatestcommondivisorCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class onedecimalplaceCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return onedecimalplaceCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 


class percentofwhatnumberCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return percentofwhatnumberCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 


class rationalnumberCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return rationalnumberCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified


class whattwonumberadduptoCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return whattwonumberadduptoCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  

class sequentialpercentageCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return sequentialpercentageCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified


class fractiondividedbynumberCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return fractiondividedbynumberCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class lakhzerosCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return lakhzerosCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class percentasdecimalCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return percentasdecimalCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  

class whatpercentCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return whatpercentCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  


class xtimesxCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return xtimesxCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  

class squarerootnumberCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return squarerootnumberCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  

class squaremetertofeetCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return squaremetertofeetCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  


class squareinchtofeetCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return squareinchtofeetCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  

class secondpowerCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return secondpowerCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  


class thirdpowerCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return thirdpowerCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class squaredCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return squaredCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  

class minutesofhourpercentCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return minutesofhourpercentCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class percenttopermileCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return percenttopermileCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  


class scientificnotationCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return scientificnotationCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class cubiccentimeterstocubicmetersCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return cubiccentimeterstocubicmetersCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified

class sumofintegerCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return sumofintegerCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class randomnumberbetweenCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return randomnumberbetweenCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class squarerootoffractionCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return squarerootoffractionCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified  

class numberpluspercentCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return numberpluspercentCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class numberminuspercentCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return numberminuspercentCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 

class sumofgeometricsequenceCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return sumofgeometricsequenceCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 


class sumofarithmeticsequenceCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return sumofarithmeticsequenceCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified


class arithmeticsequencetermCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return arithmeticsequencetermCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified

class geometricsequencetermCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return geometricsequencetermCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified


class rectangulardimensionCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return rectangulardimensionCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified


class areaOfTheParallelogramCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return areaOfTheParallelogramCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified


class differentialequationCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return differentialequationCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified


class fractionofadayinhourCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return fractionofadayinhourCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified


class coordinatesh_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return coordinatesh.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 


class remainderofequationCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return remainderofequationCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified 


class HorizontalTangent_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return HorizontalTangent.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified


class equationofarithmeticsequenceCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return equationofarithmeticsequenceCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified

class equationofnthtermCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return equationofnthtermCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified


class findremainderofpowerCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return findremainderofpowerCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified

class independenteventsCalculator_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return independenteventsCalculator.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified
    
class TangentPlane_SiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=5000
    def items(self):
        return TangentPlane.objects.all()
    
    def location(self, obj):
        return obj.slug
    
    def lastmod(self, obj):
        return obj.date_modified



numbers={
     'percent-to-decimal-calculator-sitemap':percenttToDecimalCalculator_SiteMap,
     'decimal-to-percentage-calculator-sitemap':decimalToPercentageCalculator_SiteMap,
     'modulo-calculator-sitemap':moduloCalculator_SiteMap,
     'divided-by-what-calculator-sitemap':dividedByWhatCalculator_SiteMap,
     'negative-divided-calculator-sitemap':negativeDividedCalculator_SiteMap,
     'million-zeros-Calculator-sitemap':millionzerosCalculator_SiteMap,
     'billion-zeros-Calculator-sitemap':billionzerosCalculator_SiteMap,
     'crore-zeros-Calculator-sitemap':crorezerosCalculator_SiteMap,
     'crore-in-number-Calculator-sitemap':croreinnumberCalculator_SiteMap,
     'decimal-to-binary-Calculator-sitemap':decimaltobinaryCalculator_SiteMap,
     'decimal-place-value-Calculator-sitemap':decimalplacevalueCalculator_SiteMap,
     'adding-fraction-Calculator-sitemap':addingfractionCalculator_SiteMap,
     'multiplying-fraction-Calculator-sitemap':multiplyingfractionCalculator_SiteMap,
     'dividing-fraction-Calculator-sitemap':dividingfractionCalculator_SiteMap,
     'mixed-fraction-Calculator-sitemap':mixedfractionCalculator_SiteMap,
     'three-digiti-number-divisible-Calculator-sitemap':threedigitnumberCalculator_SiteMap,
     'four-digiti-number-divisible-Calculator-sitemap':fourdigitnumberCalculator_SiteMap,
     'what-is-next-fibonacci-Calculator-sitemap':whatisnextfibonacciCalculator_SiteMap,
     'how-do-you-add-percent-to-number-Calculator-sitemap':howdoyouaddpercenttonumberCalculator_SiteMap,
     'greatest-common-divisor-Calculator-sitemap':greatestcommondivisorCalculator_SiteMap,
     'one-decimal-place-Calculator-sitemap':onedecimalplaceCalculator_SiteMap,
     'percent-of-what-number-Calculator-sitemap':percentofwhatnumberCalculator_SiteMap,
     'rational-number-Calculator-sitemap':rationalnumberCalculator_SiteMap,
     'numbers-that-add-up-to-Calculator-sitemap':whattwonumberadduptoCalculator_SiteMap,
     'sequential-percentage-Calculator-sitemap':sequentialpercentageCalculator_SiteMap,
     'fraction-divided-by-number-Calculator-sitemap':fractiondividedbynumberCalculator_SiteMap,
     'lakh-zeros-Calculator-sitemap':lakhzerosCalculator_SiteMap,
     'percent-as-decimal-Calculator-sitemap':percentasdecimalCalculator_SiteMap,
     'what-percent-Calculator-sitemap':whatpercentCalculator_SiteMap,
     'x-times-x-Calculator-sitemap':xtimesxCalculator_SiteMap,
     'square-root-of-a-number-squared-Calculator-sitemap':squarerootnumberCalculator_SiteMap,
     'square-meters-to-square-feet-converter-Calculator-sitemap':squaremetertofeetCalculator_SiteMap,
     'square-meters-to-square-feet-converter-Calculator-sitemap':squareinchtofeetCalculator_SiteMap,
     'second-power-Calculator-sitemap':secondpowerCalculator_SiteMap,
     'third-power-Calculator-sitemap':thirdpowerCalculator_SiteMap,
     'squared-Calculator-sitemap':squaredCalculator_SiteMap,
     'minutes-of-an-hour-as-a-percentage-Calculator-sitemap':minutesofhourpercentCalculator_SiteMap,
     'percent-to-permille-converter-Calculator-sitemap':percenttopermileCalculator_SiteMap,
     'scientific-notations-Calculator-sitemap':scientificnotationCalculator_SiteMap,
     'cubic-centimeters-to-cubic-meters-converter-Calculator-sitemap':cubiccentimeterstocubicmetersCalculator_SiteMap,
     'sum-of-integers-Calculator-sitemap':sumofintegerCalculator_SiteMap,
     'cubic-centimeters-to-cubic-meters-Calculator-sitemap':randomnumberbetweenCalculator_SiteMap,
     'square-root-of-a-fraction-Calculator-sitemap':squarerootoffractionCalculator_SiteMap,
     'number-minus-percent-Calculator-sitemap':numberminuspercentCalculator_SiteMap,
     'number-plus-percent-Calculator-sitemap':numberpluspercentCalculator_SiteMap,
     'sum-of-geometric-sequence-Calculator-sitemap':sumofgeometricsequenceCalculator_SiteMap, 
     'sum-of-arithmetic-sequence-Calculator-sitemap':sumofarithmeticsequenceCalculator_SiteMap, 
     'term-of-arithmetic-sequence-Calculator-sitemap':arithmeticsequencetermCalculator_SiteMap,
     'term-of-geometric-sequence-Calculator-sitemap':geometricsequencetermCalculator_SiteMap,
     'dimension-rectangle-of-a-perimeter-Calculator-sitemap':rectangulardimensionCalculator_SiteMap,
     'find-the-area-of-the-parallelogram-with-vertices-Calculator-sitemap':areaOfTheParallelogramCalculator_SiteMap, 
     'differential-equation-of-exponential-Calculator-sitemap':differentialequationCalculator_SiteMap, 
     'fraction-of-a-day-in-hour-calculator-Calculator-sitemap':fractionofadayinhourCalculator_SiteMap,
     'coordinates-shape-calculator-Calculator-sitemap':coordinatesh_SiteMap, 
     'find-remainder-of-equation-Calculator-sitemap':remainderofequationCalculator_SiteMap,
     'horizontal-tangent-points-on-curve-Calculator-sitemap':HorizontalTangent_SiteMap,
     'equation-of-arithmetic-sequence-Calculator-sitemap':equationofarithmeticsequenceCalculator_SiteMap, 
     'equation-of-nth-term-of-arithmetic-sequence-Calculator-sitemap':equationofnthtermCalculator_SiteMap,
     'find-remainder-of-power-Calculator-sitemap':findremainderofpowerCalculator_SiteMap, 
     'independent-events-Calculator-sitemap':independenteventsCalculator_SiteMap, 
     'equation-of-the-tangent-plane-to-the-given-surface-at-the-specified-point-Calculator-sitemap':TangentPlane_SiteMap, 
     
}

