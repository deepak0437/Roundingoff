from django.contrib import admin
from django.urls import path
from.views import *

app_name = 'Numbers'

urlpatterns = [
    path('', home,name='home'),
    
    path('percent-to-decimal-calculator/', percenttodecimalcalculator, name='percent-to-decimal-calculator'),
    path('<aa>-percentage-as-a-decimal/',percentagetodecimal_details, name = "percent-to-decimal-calculator-details"),

    path('decimal-as-percentage-calculator/',decimaltopercentagecalculator, name = "decimal-to-percentage"),
    path('<aa>-decimal-as-a-percentage/',decimaltopercentage, name = "decimal-to-percentage-details"),

    path('divided-by-what-equals-calculator/',dividedbywhatcalculator, name = "divided-by-what"),
    path('<aa>-divided-by-what-equals-to-<cc>/',dividedbywhatcalculatordetails, name = "divided-by-what-details"),
 
    path('negative-divided-by-negative-calculator/',negativedividedcalculator, name = "negative-divided-by-negative"),
    path('what-is-negative-<int:aa>-divided-by-negative-<int:cc>/',negativeDividedCalculatorDetails, name = "negative-divided-by-negative-details"),

    path('modulo-calculator/', modulocalculator, name='modulo-calculator'),
    path('what-is-<aa>-mod-<cc>/',modulocalculatordetails, name = "modulo-calculator-details"),

    path('greatest-common-divisor-calculator/',greatestcommondivisorcalculator, name = "greatestcommondivisor"), 
    path('find-gcd-of-<int:aa>-and-<int:bb>/',greatestcommondivisor, name = "greatestcommondivisor1"),

    path('how-many-zeros-in-a-quintillion-calculator/',howmanyzeroesinquintillioncalculator, name = "howmanyzeroesinquintillion"), 
    path('how-many-zeros-in-a-<str:aa>-quintillion/',howmanyzeroesinquintillion, name = "howmanyzeroesinquintillion1"),

    path('how-many-zeros-in-a-googolplex-calculator/',howmanyzeroesingoogolplexcalculator, name = "howmanyzeroesingoogolplex"), 
    path('how-many-zeros-in-a-<str:aa>-googolplex/',howmanyzeroesingoogolplex, name = "howmanyzeroesingoogolplex1"),

    path('how-many-zeros-in-a-million-calculator/',howmanyzeroesinmillioncalculator, name = "howmanyzeroesinmillion"), 
    path('how-many-zeros-in-a-<aa>-million/',howmanyzeroesinmillion, name = "howmanyzeroesinmillion1"),

    path('how-many-zeros-in-a-billion-calculator/',howmanyzeroesinbillioncalculator, name = "howmanyzeroesinbillion"), 
    path('how-many-zeros-in-a-<aa>-billion/',howmanyzeroesinbillion, name = "howmanyzeroesinbillion1"),

    path('how-many-zeros-in-a-crore-calculator/',howmanyzeroesincrorecalculator, name = "howmanyzeroesincrore"), 
    path('how-many-zeros-in-a-<aa>-crore/',howmanyzeroesincrore, name = "howmanyzeroesincrore1"),

    path('crore-in-numbers-calculator/',croreinnumbercalculator, name = "croreinnumber"), 
    path('what-is-<aa>-crore-in-numbers/',croreinnumber, name = "croreinnumber1"),

    path('decimal-to-binary-calculator/',decimaltobinarycalculator, name = "decimaltobinary"), 
    path('how-to-convert-<aa>-to-binary/',decimaltobinary, name = "decimaltobinary1"),

    path('decimal-place-value-calculator/',decimalplacevalueCalculator),

    path('adding-fraction-calculator/',addingfractioncalculator, name = "fraction"), 
    path('what-is-<int:aa>-<int:cc>-plus-<int:bb>-<int:dd>/',addingfraction, name = "fraction1"),

    path('multiplying-fraction-calculator/',multiplyingfractioncalculator, name = "multiplying"), 
    path('what-is-<int:aa>-<int:cc>-times-<int:bb>-<int:dd>/',multiplyingfraction, name = "multiplying1"),

    path('dividing-fraction-calculator/',dividingfractioncalculator, name = "dividings"), 
    path('what-is-<int:aa>-<int:cc>-divided-by-<int:bb>-<int:dd>/',dividingfraction, name = "dividings1"),

    path('mixed-fraction-calculator/',mixedfractioncalculator, name = "mixedfractions"), 
    path('<int:aa>-<int:cc>-as-a-mixed-fraction/',mixedfraction, name = "mixedfraction1"), 

    path('three-digit-number-divisible-calculator/',threedigitnumbercalculator, name = "threedigitnumber"), 
    path('3-digit-number-divisible-by-<int:aa>/',threedigitnumber, name = "threedigitnumber1"),

    path('four-digit-number-divisible-calculator/',fourdigitnumbercalculator, name = "fourdigitnumber"), 
    path('4-digit-number-divisible-by-<int:aa>/',fourdigitnumber, name = "fourdigitnumber1"), 

    path('what-is-next-fibonacci-number-calculator/',whatisnextfibonaccicalculator, name = "whatisnextfibonacci"), 
    path('what-is-the-next-fibonacci-number-in-following-sequence-<aa>/',whatisnextfibonacci, name = "whatisnextfibonacci1"),

    path('how-do-you-add-a-percent-to-number-calculator/',howdoyouaddpercenttonumbercalculator, name = "howdoyouaddpercenttonumber"), 
    path('how-do-you-add-<int:aa>-percent-to-a-number/',howdoyouaddpercenttonumber, name = "howdoyouaddpercenttonumber1"), 
    path('what-is-<bb>-plus-<int:aa>-percent/',howdoyouaddpercenttonumber1, name = "howdoyouaddpercenttonumber2"), 

    path('one-decimal-place-calculator/',onedecimalplacecalculator, name = "onedecimalplace"), 
    path('what-is-<aa>-to-1-decimal-place/',onedecimalplace, name = "onedecimalplace1"),

    path('percent-of-what-number-calculator/',percentofwhatnumbercalculator, name = "percentofwhatnumber"), 
    path('<int:aa>-is-<int:bb>-percent-of-what-number/',percentofwhatnumber, name = "percentofwhatnumber1"),

    path('rational-number-calculator/',rationalnumbercalculator, name = "rationalnumber"), 
    path('is-<aa>-a-rational-number/',rationalnumber, name = "rationalnumber1"),

    path('numbers-that-add-up-to-calculator/',whattwonumberadduptocalculator, name = "whattwonumberaddupto"), 
    path('what-two-numbers-add-up-to-<int:aa>/',whattwonumberaddupto, name = "whattwonumberaddupto1"),

    ##October Months
    path('sequential-percentage-calculator/',sequentialpercentagecalculator, name = "sequentialpercentage"), 
    path('a-number-<nm>-is-<aa_op>-by-<int:aa>%-and-then-<bb_op>-by-<int:bb>%/',sequentialpercentage, name = "sequentialpercentage1"),

    path('fraction-divided-by-number-calculator/',fractiondividedbynumbercalculator, name = "fractiondividedbynumber"), 
    path('what-is-<int:aa>/<int:bb>-divided-by-<int:cc>/',fractiondividedbynumber, name = "fractiondividedbynumber1"),

    path('how-many-zeros-in-a-lakh-calculator/',howmanyzeroesinlakhcalculator, name = "howmanyzeroesinlakh"), 
    path('<aa>-lakh-how-many-zeros/',howmanyzeroesinlakh, name = "howmanyzeroesinlakh1"),

    path('percent-as-a-decimal-calculator/',percentasdecimalcalculator, name='percentasdecimal'),
    path('<aa>-as-a-decimal/',percentasdecimal, name = "percentasdecimal-details"),

    path('what-percent-calculator/',whatpercentcalculator, name='whatpercentl'),
    path('<int:aa>-is-what-percent-of-<int:bb>/',whatpercent, name = "whatpercent2"),

    path('x-times-x-calculator/',xtimesxcalculator, name='xtimesxl'),
    path('what-is-<int:aa>x-times-<int:bb>x/',xtimesx, name = "xtimesx2"),

    path('square-root-of-a-number-squared-calculator/',squarerootnumbercalculator, name='squarerootnumberl'),
    path('square-root-of-<int:aa>-squared/',squarerootnumber, name = "squarerootnumber2"),

    path('square-meters-to-square-feet-converter-calculator/',squaremetertofeetcalculator, name='squaremetertofeetl'),
    path('<aa>-square-meters-to-square-feet/',squaremetertofeet, name = "squaremetertofeet2"),

    path('square-inches-to-square-feet-converter-calculator/',squareinchtofeetcalculator, name='squareinchtofeetl'),
    path('<aa>-square-inches-to-square-feet/',squareinchtofeet, name = "squareinchtofeet2"),

    path('second-power-calculator/',secondpowercalculator, name='secondpowerl'),
    path('what-is-<aa>-to-the-2nd-power/',secondpower, name = "secondpower2"),

    path('third-power-calculator/',thirdpowercalculator, name='thirdpowerl'),
    path('what-is-<aa>-to-the-3rd-power/',thirdpower, name = "thirdpower2"),

    path('squared-calculator/',squaredcalculator, name='squaredl'),
    path('what-is-<aa>-squared/',squared, name = "squared2"),

    path('minutes-of-a-hour-as-a-percentage-calculator/',minutesofhourpercentcalculator, name='minutesofhourpercentl'),
    path('what-percentage-of-a-hour-is-<int:aa>-minutes/',minutesofhourpercent, name = "minutesofhourpercent2"),

    path('percent-to-permille-converter-calculator/',percenttopermilecalculator, name='percenttopermilel'),
    path('<aa>-percent-to-permille/',percenttopermile, name = "percenttopermile2"),

    path('scientific-notation-calculator/',scientificnotationCalculator),

    path('cubic-centimeters-to-cubic-meters-converter-calculator/',cubiccentimeterstocubicmetersconvertercalculator, name = "cubiccentimeterstocubicmetersconverter"), 
    path('convert-<aa>-cm3-to-m3/',cubiccentimeterstocubicmetersconverter, name = "cubiccentimeterstocubicmetersconverter1"),

    path('sum-of-integers-calculator/',sumofintegercalculator, name = "sumofinteger"), 
    path('sum-of-integers-from-<int:aa>-to-<int:bb>/',sumofinteger, name = "sumofinteger1"),

    path('random-number-between-calculator/',randomnumberbetweencalculator, name = "randomnumberbetween"), 
    path('random-number-between-<int:aa>-and-<int:bb>/',randomnumberbetween, name = "randomnumberbetween1"),

    path('square-root-of-a-fraction-calculator/',squarerootoffractioncalculator, name = "squarerootoffraction"), 
    path('square-root-of-<int:aa>-by-<int:bb>/',squarerootoffraction, name = "squarerootoffraction1"),

    path('number-minus-percent-calculator/',numberminuspercentcalculator, name = "numberminuspercent"), 
    path('<aa>-minus-<bb>-percent/',numberminuspercent, name = "numberminuspercent1"),

    path('number-plus-percent-calculator/',numberpluspercentcalculator, name = "numberpluspercent"), 
    path('<aa>-plus-<bb>-percent/',numberpluspercent, name = "numberpluspercent1"),

###################NEW ONE###############################
    path('arithmetic-sequence-domain-calculator/',atsequencedomain,name='atsequencedomain'), ##ERROR  ##SURAJ
    path("given-the-arithmetic-sequence-an-'<str:func>'-what-is-the-domain-for-n/",atsequencedomaintail,name='atsequencedomain'),

    path('sum-of-geometric-sequence-calculator/',sumofgeometricsequencecalculator,name='sumofgeometricsequence'), ##DEEPAK
    path("what-is-the-sum-of-the-geometric-sequence-<aa>-if-there-are-<int:bb>-terms/",sumofgeometricsequence,name='sumofgeometricsequence1'),

    path('sum-of-arithmetic-sequence-calculator/',sumofarithmeticsequencecalculator,name='sumofarithmeticsequence'),##DEEPAK
    path("what-is-the-sum-of-the-arithmetic-sequence-<aa>-if-there-are-<int:bb>-terms/",sumofarithmeticsequence,name='sumofarithmeticsequence1'),

    path('term-of-arithmetic-sequence-calculator/',arithmeticsequencetermcalculator,name='arithmeticsequenceterm'),#NA  ##DEEPAK
    path("what-is-the-<int:aa>-term-of-the-arithmetic-sequence-where-a1-<bb>-and-a<int:yy>-<cc>/",arithmeticsequenceterm,name='arithmeticsequenceterm1'),

    path('term-of-geometric-sequence-calculator/',geometricsequencetermcalculator,name='geometricsequenceterm'),#NA  ##DEEPAK
    path("what-is-the-<int:aa>-term-of-the-geometric-sequence-where-a1-<int:bb>-and-a<int:yy>-<int:cc>/",geometricsequenceterm,name='geometricsequenceterm1'),

    path('fraction-of-a-day-in-hour-calculator/',fractionofadayinhourcalculator,name='fractionofadayinhour'), ##DEEPAK
    path("what-fraction-of-a-day-is-<int:aa>-hours/",fractionofadayinhour,name='fractionofadayinhour1'),

    path('dimension-rectangle-of-a-perimeter-calculator/',rectangulardimensioncalculator, name='dimensionRectangle'), ##SUNIL
    path('find-the-dimensions-of-a-rectangle-with-a-perimeter-<aa>m-whose-area-is-as-large-as-possible/',largestdimension, name = "largestDimension"),

    path('differential-equation-of-exponential-calculator/',differentialequationcalculator, name='differentialEquation'), ##SUNIL
    path("solve-the-given-differential-equation-by-separation-of-variables-dy-dx-e<int:xcof>x<str:operator><int:ycof>y/",generalSolution, name = "generalSolutions"),

    path('find-the-area-of-the-parallelogram-with-vertices-calculator/', areaOfTheParallelogramWithVertices, name='areaOfTheParallelogramWithVertices'), ##MADHAV
    path('area-of-the-parallelogram-with-vertices-a-<x1>-<y1>-b-<x2>-<y2>-c-<x3>-<y3>-and-d-<x4>-<y4>/', areaOfTheParallelogramWithVerticesTail, name='areaOfTheParallelogramWithVerticesTail'),

    path('coordinates-shape-calculator/',coordinatesshapecalculator, name='coordinat'), ##JK
    path('when-the-coordinates-<x1>-<y1>-<x2>-<y2>-<x3>-<y3>-<x4>-<y4>-are-joined-which-shape-is-formed/',coordinatesshapecalculatordetails),

    path('point-on-the-parabola-closest-to-a-point/',pointOnTheParabolaCalculator, name='point on the Parabola'), ##SUNIL
    path("find-the-point-on-the-parabola-y2-<int:xcof>x-that-is-closest-to-the-point-<str:x1>-<str:y1>/",closestPoint, name = "closestPoint"),
    
    path('point-on-the-surface-that-is-closest-to-the-point/',pointOnTheSurfaceCalculator, name='point on the Surface'),  ##SUNIL
    path("find-the-points-on-the-surface-y2-<int:val>-xz-that-are-closest-to-the-origin/",closestOrigin, name = "closestOrigin"),

    path('additive-inverse-of-complex-number-calculator/', additiveInverseOfComplexNumber, name='additiveInverse'),
    path('additive-inverse-of-complex-number-<int:num1>-<int:num2>i/', additiveInverseOfComplexNumberDetails, name='additiveInverseDetail'),
    
    path('find-first-six-term-of-the-sequence/', findFirstSixTermOfSequence, name='first6thTerm'),
    path('find-first-six-term-of-the-sequence-a1=<str:aa>-an=<str:bb>an-1/', findFirstSixTermOfSequenceDetails, name='first6thTermDetails'),

    path('find-remainder-of-equation-calculator/', remainderofequationcalculator, name='remainderofequation'),
    path('find-the-remainder-when-fx-<str:aa>-x3-<str:bb>-x2-<str:cc>-x-<str:dd>-is-divided-by-x-<str:ee>/', remainderofequation, name='remainderofequation1'),

    path("horizontal-tangent-points-on-curve-calculator/",horizontaltangent, name='horizontaltangent'),
    path('find-points-on-the-curve-<equat>-where-the-tangent-is-horizontal/',detailshorizontaltangent),

    path('point-on-the-cone-that-is-closest-to-the-point/',pointOnTheConeCalculator, name='point on the cone'),
    path("find-the-points-on-the-cone-z2-x2-y2-that-are-closest-to-the-point-<int:xval>-<int:yval>-<int:zval>/",closestPoints, name = "closestPoints"),

]
 