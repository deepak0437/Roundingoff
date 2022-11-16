from django.db import models

# Create your models here.
from datetime import *
from django.db import models
from django.utils.timezone import now


class TableStructure(models.Model):
    inputEnter = models.CharField(max_length=250)
    detailStep = models.TextField()
    finalAnswer = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    solutionTitle = models.CharField(max_length=250)
    date_modified = models.DateTimeField() 
 
    class Meta:
        abstract = True
 
    def __str__(self):
        """A string representation of the model."""
        return self.solutionTitle[:50]

class RoundingoffStructure(models.Model):
    inputEnter = models.CharField(max_length=250)
    detailStep = models.TextField()
    finalAnswer = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    solutionTitle = models.CharField(max_length=250)
    date_modified = models.DateTimeField() 
 
    class Meta:
        abstract = True
 
    def __str__(self):
        """A string representation of the model."""
        return self.solutionTitle[:50]


class percenttToDecimalCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "percenttToDecimalCalculator"


class decimalToPercentageCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "decimalToPercentageCalculator"


class moduloCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "moduloCalculator"


class dividedByWhatCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "dividedByWhatCalculator"        

class negativeDividedCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "negativeDividedCalculator"         

class millionzerosCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "millionzerosCalculator"   

class billionzerosCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "billionzerosCalculator"                

class crorezerosCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "crorezerosCalculator"  

class croreinnumberCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "croreinnumberCalculator"  

class decimaltobinaryCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "decimaltobinaryCalculator"  

class decimalplacevalueCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "decimalplacevalueCalculator" 

class addingfractionCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "addingfractionCalculator" 

class multiplyingfractionCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "multiplyingfractionCalculator" 

class dividingfractionCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "dividingfractionCalculator" 

class mixedfractionCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "mixedfractionCalculator" 

class threedigitnumberCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "threedigitnumberCalculator" 
 
class fourdigitnumberCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "fourdigitnumberCalculator" 

class whatisnextfibonacciCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "whatisnextfibonacciCalculator" 

class howdoyouaddpercenttonumberCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "howdoyouaddpercenttonumberCalculator" 

class greatestcommondivisorCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "greatestcommondivisorCalculator" 

class onedecimalplaceCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "onedecimalplaceCalculator" 

class percentofwhatnumberCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "percentofwhatnumberCalculator" 

class rationalnumberCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "rationalnumberCalculator" 

class whattwonumberadduptoCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "whattwonumberadduptoCalculator"

class sequentialpercentageCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "sequentialpercentageCalculator" 

class fractiondividedbynumberCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "fractiondividedbynumberCalculator"

class lakhzerosCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "lakhzerosCalculator" 

class percentasdecimalCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "percentasdecimalCalculator"

class whatpercentCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "whatpercentCalculator" 

class xtimesxCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "xtimesxCalculator" 

class squarerootnumberCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "squarerootnumberCalculator" 

class squaremetertofeetCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "squaremetertofeetCalculator"

class squareinchtofeetCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "squareinchtofeetCalculator" 

class secondpowerCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "secondpowerCalculator"

class thirdpowerCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "thirdpowerCalculator" 

class squaredCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "squaredCalculator" 

class minutesofhourpercentCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "minutesofhourpercentCalculator" 

class percenttopermileCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "percenttopermileCalculator" 

class scientificnotationCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "scientificnotationCalculator" 

class cubiccentimeterstocubicmetersCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "cubiccentimeterstocubicmetersCalculator" 

class sumofintegerCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "sumofintegerCalculator"

class randomnumberbetweenCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "randomnumberbetweenCalculator" 

class squarerootoffractionCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "squarerootoffractionCalculator" 

class numberpluspercentCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "numberpluspercentCalculator"

class numberminuspercentCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "numberminuspercentCalculator" 

class atsequence(models.Model):
    func=models.CharField(max_length=256)
    solution=models.CharField(max_length=256)


class sumofgeometricsequenceCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "sumofgeometricsequenceCalculator" 


class sumofarithmeticsequenceCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "sumofarithmeticsequenceCalculator" 


class arithmeticsequencetermCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "arithmeticsequencetermCalculator" 

class geometricsequencetermCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "geometricsequencetermCalculator"

class rectangulardimensionCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "rectangulardimensionCalculator" 

class areaOfTheParallelogramCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "areaOfTheParallelogramCalculator" 

class differentialequationCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "differentialequationCalculator"

class fractionofadayinhourCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "fractionofadayinhourCalculator" 

class coordinatesh(RoundingoffStructure): 
        date_modified = models.DateTimeField(default=now) 
        class Meta:
                verbose_name_plural = "coordinatesh"


class remainderofequationCalculator(RoundingoffStructure):
     class Meta:
        verbose_name_plural = "remainderofequationCalculator" 


class HorizontalTangent(RoundingoffStructure):
        eq1 = models.CharField(max_length=300)
        date_modified = models.DateTimeField(default=now) 
        class Meta:
                verbose_name_plural = "HorizontalTangent"