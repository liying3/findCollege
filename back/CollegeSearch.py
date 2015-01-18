import sys
import os.path
import operator
import Raw2Internal
import time

class PCollege:
    Count = 0
    
    def __init__(self, name="N/A", loc="N/A", tuition=0, aSAT=1, aGPA=1):
        self.name = name
        self.loc = loc
        self.tuition = tuition
        self.aSAT = aSAT
        self.aGPA = aGPA
        self.chance = 0
        PCollege.Count += 1
        
college1 = PCollege("The University of Pennsylvania", "Pennsylvania", 60000, 2100, 3.66)
college2 = PCollege("Stanford University", "California", 70000, 2300, 3.80)
college3 = PCollege("Drexel University", "Pennsylvania", 50000, 1800, 3.00)

pcolleges = [college1, college2, college3];

def ReadCollegeFiles():
    #test=College()		
    for i in range(6,3341):
        try:
            test=Raw2Internal.College()
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
            finalCost = GetCost(str(test.CostOfAttendance), 10000)
            #print(finalSAT)
            #print(finalCost)
            pcolleges.append(PCollege(test.Name, test.State, int(finalCost), finalSAT, aGPA))
        except ValueError:
            #print("Error: Readfile")
            pass

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


def SortCollege(pref1, pref2, pref3):
    try:
        pcolleges.sort(key=operator.attrgetter(pref1))
    except ValueError:
        pass
    return

def FindBestColleges( SAT, GPA, TopPercentage, Locations, Tuition, Concentration ):
    #print("My SAT: ", SAT, "My GPA: ", GPA, "\n");

    for i in range(len(pcolleges)):
        if pcolleges[i].loc in Locations:
            print(pcolleges[i].name)
            print(pcolleges[i].loc)
            print(pcolleges[i].tuition)
            print(pcolleges[i].aGPA)
            print(pcolleges[i].aSAT)
            pcolleges[i].chance = CalculateChance(SAT, GPA, TopPercentage, pcolleges[i].aSAT, pcolleges[i].aGPA)
            print(pcolleges[i].chance)
        
    return


def CalculateChance(SAT, GPA, TopPercentage, aSAT, aGPA):
    try:
        return ( 0.35 * int(SAT)/int(aSAT) + 0.35 * float(GPA)/float(aGPA) + 0.3 * (1-float(TopPercentage))/100) * 100
    except ValueError:
        return 50
    
ReadCollegeFiles()
#SortCollege('chance','123','123')


FindBestColleges(SAT=sys.argv[1], GPA=sys.argv[2], TopPercentage=sys.argv[3], Locations=sys.argv[4], Tuition=sys.argv[5], Concentration=sys.argv[6])


    
