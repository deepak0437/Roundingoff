from django.contrib import admin
from django.urls import path,include
from django.contrib.sitemaps.views import sitemap
from Numbers.sitemaps import *

from django.contrib.sitemaps.views import sitemap,index

sitemaps = { 
    'four-digit-number-divisible-calculator':fourdigitnumberCalculator_SiteMap,
    'three-digit-number-divisible-calculator':threedigitnumberCalculator_SiteMap, 
    'what-is-next-fibonacci-number-calculator':whatisnextfibonacciCalculator_SiteMap,
    'mixed-fraction-calculator':mixedfractionCalculator_SiteMap, 
    'decimal-place-value-calculator':decimalplacevalueCalculator_SiteMap,
    'crore-in-number-Calculator':croreinnumberCalculator_SiteMap,
    'decimal-to-binary-Calculator':decimaltobinaryCalculator_SiteMap,
    'how-many-zeros-in-a-million-calculator':millionzerosCalculator_SiteMap,
    'how-many-zeros-in-a-billion-calculator':billionzerosCalculator_SiteMap,
    'how-many-zeros-in-a-crore-calculator':crorezerosCalculator_SiteMap,
    'how-do-you-add-a-percent-to-number-calculator':howdoyouaddpercenttonumberCalculator_SiteMap,
    'greatest-common-divisor-calculator':greatestcommondivisorCalculator_SiteMap,
    'one-decimal-place-calculator':onedecimalplaceCalculator_SiteMap,
    'percent-of-what-number-calculator':percentofwhatnumberCalculator_SiteMap,
    'rational-number-calculator':rationalnumberCalculator_SiteMap,
    'numbers-that-add-up-to-calculator':whattwonumberadduptoCalculator_SiteMap,
    'sequential-percentage-calculator':sequentialpercentageCalculator_SiteMap,
    'fraction-divided-by-number-calculator':fractiondividedbynumberCalculator_SiteMap,
    'how-many-zeros-in-a-lakh-calculator':lakhzerosCalculator_SiteMap,
    'percent-as-a-decimal-calculator':percentasdecimalCalculator_SiteMap,
    'what-percent-calculator':whatpercentCalculator_SiteMap,
    'x-times-x-calculator':xtimesxCalculator_SiteMap,
    'square-root-of-a-number-squared-calculator':squarerootnumberCalculator_SiteMap,
    'square-meters-to-square-feet-converter-calculator':squaremetertofeetCalculator_SiteMap,
    'square-meters-to-square-feet-converter-calculator':squareinchtofeetCalculator_SiteMap,
    'second-power-calculator':secondpowerCalculator_SiteMap,
    'third-power-calculator':thirdpowerCalculator_SiteMap,
    'squared-calculator':squaredCalculator_SiteMap,
    'minutes-of-an-hour-as-a-percentage-calculator':minutesofhourpercentCalculator_SiteMap,
    'percent-to-permille-converter-calculator':percenttopermileCalculator_SiteMap,
    'scientific-notation-calculator':percenttopermileCalculator_SiteMap,
    'cubic-centimeters-to-cubic-meters-converter-calculator':cubiccentimeterstocubicmetersCalculator_SiteMap,
    'sum-of-integers-calculator':sumofintegerCalculator_SiteMap,
    'random-number-between-calculator':randomnumberbetweenCalculator_SiteMap,
    'square-root-of-a-fraction-calculator':squarerootoffractionCalculator_SiteMap,
    'number-minus-percent-calculator':numberminuspercentCalculator_SiteMap,
    'sum-of-geometric-sequence-calculator':sumofgeometricsequenceCalculator_SiteMap,
    'sum-of-arithmetic-sequence-calculator':sumofarithmeticsequenceCalculator_SiteMap,
    'term-of-arithmetic-sequence-calculator':arithmeticsequencetermCalculator_SiteMap,
    'term-of-geometric-sequence-calculator':geometricsequencetermCalculator_SiteMap,
    'dimension-rectangle-of-a-perimeter-calculator':rectangulardimensionCalculator_SiteMap,
    'find-the-area-of-the-parallelogram-with-vertices-calculator':areaOfTheParallelogramCalculator_SiteMap,
    'differential-equation-of-exponential-calculator':differentialequationCalculator_SiteMap,
    'fraction-of-a-day-in-hour-calculator-calculator':fractionofadayinhourCalculator_SiteMap,
    'coordinates-shape-calculator':coordinatesh_SiteMap,
    'find-remainder-of-equation-calculator':remainderofequationCalculator_SiteMap,
    'horizontal-tangent-points-on-curve-calculator':HorizontalTangent_SiteMap,
    'equation-of-arithmetic-sequence-calculator':equationofarithmeticsequenceCalculator_SiteMap,
    'equation-of-nth-term-of-arithmetic-sequence-calculator':equationofnthtermCalculator_SiteMap,
    'find-remainder-of-power-calculator':findremainderofpowerCalculator_SiteMap,
    'independent-events-calculator':independenteventsCalculator_SiteMap,
    'equation-of-the-tangent-plane-to-the-given-surface-at-the-specified-point-calculator':TangentPlane_SiteMap,

}

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include('Numbers.urls')),
    
    path('sitemap.xml', index, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.index'),    
    path('<section>.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

"""path(
        'sitemap.xml',sitemap, {'sitemaps':sitemap}, name='django.contrib.sitemaps.views.sitemap'
    )"""

