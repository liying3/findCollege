import sys
import os.path
from operator import itemgetter, attrgetter, methodcaller
import Raw2Internal
import time

class PCollege:
    Count = 0
    
    def __init__(self, name=" ", loc=" ", tuition=0, aSAT=1, aGPA=1, fn=" ", chance=0, overall=0):
        self.name = name
        self.loc = loc
        self.tuition = tuition
        self.aSAT = aSAT
        self.aGPA = aGPA
        self.chance = chance
        self.filename = fn
        self.overall = overall
        PCollege.Count += 1
        
pcolleges = [];
pcolleges2 = []
def ReadCollegeFiles(SAT, GPA, TopPercentage, Locations, Tuition, Concentration ):
    #test=College()		
    for i in range(6,3341):
        try:
            test=Raw2Internal.College()
            fn = 'school'+str(i)
            test.Extract('../extracted/school'+str(i)+'.txt',  '../extracted/school'+str(i)+'.txt')
            #if test.Name=='':
            #    break
            aGPA = 2.0
            if 'N' in str(test.AverageGPA):
                aGPA = 2.0
            else:
                aGPA = float(test.AverageGPA)
                
            #print(test.Name)
            #print(test.State)
            #print("Phone: ",test.Phone)
            #print("Tuition: ", test.TuitionFee)
            #print("Cost: ",test.CostOfAttendance)            
            #print(aGPA)
                
            satMath = str(test.SAT_MATHAverage)[:3]
            satReading = str(test.SAT_ReadingAverage)[:3]
            satWriting = str(test.SAT_WritingAverage)[:3]

            finalSAT = GetScore(satMath, 600) + GetScore(satReading, 600) + GetScore(satWriting, 600)
            finalCost = GetCost(str(test.CostOfAttendance), 25000)
            chance = CalculateChance(SAT, GPA, TopPercentage, finalSAT, aGPA)
            rank = 999
            if Concentration == 'Business':
                rank = test.BusinessRank
            elif Concentration == 'Education':
                rank = test.EducationRank
            elif Concentration == 'Engineering':
                rank = test.EngineeringRank
            elif Concentration == 'Health':
                rank = test.HealthRank
                
            overall = CalculateOverall(chance, finalCost, rank)

            pcolleges.append(PCollege(test.Name, test.State, int(finalCost), finalSAT, aGPA, fn, chance, overall))
            
        except ValueError:
            #print("Error: Readfile")
            pass
        
    pcolleges.sort( key=attrgetter('overall'), reverse=True)

    return

def GetScore(s, val):
    if 'N' in s:
        return val
    else:
        return int(s)

def GetCost(s, val):
    if 'N' in s or '0' in s or 'n' in s:
        return val
    else:
        s1 = s[1:]
        s2 = s1.split(',',1)
        s3 = s2[0] + s2[1]
        return int(s3)



def FindBestColleges( SAT, GPA, TopPercentage, Locations, Tuition, Concentration ):
    #print("My SAT: ", SAT, "My GPA: ", GPA, "\n");
    for i in range(len(pcolleges)):
        if  len(str(Locations))==2:
            if pcolleges[i].tuition>=Tuition and pcolleges[i].tuition<=Tuition+10000 and pcolleges[i].loc == str(Locations) or int(Tuition) == 0 and pcolleges[i].loc == str(Locations):
                print(pcolleges[i].name)
                print(pcolleges[i].loc)
                print(pcolleges[i].tuition)
                print(pcolleges[i].aGPA)
                print(pcolleges[i].aSAT)
                print(pcolleges[i].chance)
                print(pcolleges[i].filename)

        elif len(str(Locations))==3:
            if pcolleges[i].tuition>=int(Tuition) and pcolleges[i].tuition<=int(Tuition)+10000 or int(Tuition) == 0:
                print(pcolleges[i].name)
                print(pcolleges[i].loc)
                print(pcolleges[i].tuition)
                print(pcolleges[i].aGPA)
                print(pcolleges[i].aSAT)
                print(pcolleges[i].chance)
                print(pcolleges[i].filename)
    return

def CalculateOverall(chance, tuition, rank):
    return (chance + ((500-rank)/250))/2

def CalculateChance(SAT, GPA, TopPercentage, aSAT, aGPA):
    try:
        return (0.7*((aSAT/2400.0) * (2400.0 - abs(int(SAT)-aSAT))/2400) ** 2 +  0.2*((aGPA/4.0) * (4.0-abs(float(GPA)-aGPA))/4.0) ** 2 +  0.1*((100-float(TopPercentage))/100)**2)* 100
    except ValueError:
        return 0
    
ReadCollegeFiles(SAT=int(sys.argv[1]), GPA=float(sys.argv[2]), TopPercentage=int(sys.argv[3]), Locations=str(sys.argv[4]), Tuition=int(sys.argv[5]), Concentration=str(sys.argv[6]))
FindBestColleges(SAT=int(sys.argv[1]), GPA=float(sys.argv[2]), TopPercentage=int(sys.argv[3]), Locations=str(sys.argv[4]), Tuition=int(sys.argv[5]), Concentration=str(sys.argv[6]))
#ReadCollegeFiles(SAT=1800, GPA=3.0, TopPercentage=20, Locations='MA', Tuition=10000, Concentration='Business')
#FindBestColleges(SAT=1800, GPA=3.0, TopPercentage=20, Locations='MA', Tuition=10000, Concentration='Business')


    
