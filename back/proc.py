import sys

class College:
    Count = 0
    
    def __init__(self, name="N/A", loc="N/A", tuition=0, aSAT=1, aGPA=1):
        self.name = name
        self.loc = loc
        self.tuition = tuition
        self.aSAT = aSAT
        self.aGPA = aGPA
        College.Count += 1


college1 = College("The University of Pennsylvania", "Pennsylvania", 60000, 2100, 3.66)
college2 = College("Stanford University", "California", 70000, 2300, 3.80)
college3 = College("Drexel University", "Pennsylvania", 50000, 1800, 3.00)

colleges = [college1, college2, college3]

def FindBestColleges( SAT, GPA, TopPercentage, Locations, Tuition, Concentration ):
    print("My SAT: ", SAT, "My GPA: ", GPA, "\n");

    for i in range(len(colleges)):
    
        if colleges[i].loc in Locations:
            print("College Name: ", colleges[i].name);
            print("Location: ", colleges[i].loc);
            print("Chance: ", CalculateChance(SAT, GPA, TopPercentage, colleges[i].aSAT, colleges[i].aGPA),"\n");
        
    return 1;

def CalculateChance(SAT, GPA, TopPercentage, aSAT, aGPA):
    return ( 0.35 * int(SAT)/int(aSAT) + 0.35 * float(GPA)/float(aGPA) + 0.3 * (1-float(TopPercentage))/100) * 100;
    

FindBestColleges(SAT=sys.argv[1], GPA=sys.argv[2], TopPercentage=sys.argv[3], Locations=sys.argv[4], Tuition=sys.argv[5], Concentration=sys.argv[6]);

    
