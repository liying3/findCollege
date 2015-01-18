import re

class College():
	def __init__(self):
		self.Name=' '
		
		self.EntranceDifficulty_val=-1
		self.EntranceDifficulty_Des=' '
		
		self.Address=' '
		self.City=' '
		self.State=' '
		self.Zip=' '
		self.Phone=' '
		self.Fax=' '
		self.Email=' '
		
		#-1 for not initialized
		#0 for Not Considered, 3 for very important
		self.Rigor=-1
		self.AcademicGPA=-1
		self.StandardizedTests=-1
		self.ClassRank=-1
		self.Recommendations=-1
		self.Eassy=-1;
		self.Interview=-1
		self.LevelofApplicatsInterest=-1
		self.ExtracurricularActivities=-1
		self.VolunteerWork=-1
		self.ParticularTalentAbility=-1
		self.CharacterPersonalQualities=-1
		self.FirstGeneration2AttendCollege=-1
		self.StateResidency=-1
		self.GeographicResidence=-1
		self.RelationWithAlumnus=-1
		self.ReligiousAffiliationCommitment=-1
		self.Ethnicity=-1
		self.WorkExperience=-1
		
		self.OverallAd_Rate=0 #percentage
		self.OverallAd_Num=0 #abs number
		
		self.women_Rate=0
		self.women_Num=0
		
		self.men_Rate=0
		self.men_Num=0
		
		self.Enrolled_num=0
		self.Enrolled_Rate=0
		self.Enrolled_Admitted=0;
		self.Enrolled_women_num=0
		self.Enrolled_women_rate=0
		self.Enrolled_women_Admitted=0;
		self.Enrolled_men_num=0
		self.Enrolled_men_rate=0
		self.Enrolled_men_Admitted=0;
		
		self.EarlyDecisionAdRate=0
		self.EarlyActionAdRate=0
		self.WaitList=0
		self.StudentAcceptingWaitListPosition=0
		self.StudentAdFromWaitList=0
		
		#self.GradePointAverageofEnrolledFreshmen#4.0 scale
		self.AverageGPA=2.0
		self.AverageGPAAB375=0
		self.AverageGPAAB350=0
		self.AverageGPAAB325=0
		self.AverageGPAAB300=0
		self.AverageGPAAB250=0
		self.AverageGPAAB200=0
		self.AverageGPABL200=0
		
		self.SAT_MATHAverage=600
		self.SAT_MATHMID50=''
		self.SAT_MATHAB700=0
		self.SAT_MATHAB600=0
		self.SAT_MATHAB500=0
		self.SAT_MATHAB400=0
		self.SAT_MATHAB300=0
		self.SAT_MATHAB200=0
		
		self.SAT_ReadingAverage=600
		self.SAT_ReadingMID50=''
		self.SAT_ReadingAB700=0
		self.SAT_ReadingAB600=0
		self.SAT_ReadingAB500=0
		self.SAT_ReadingAB400=0
		self.SAT_ReadingAB300=0
		self.SAT_ReadingAB200=0
		
		self.SAT_WritingAverage=600
		self.SAT_WritingMID50=''
		self.SAT_WritingAB700=0
		self.SAT_WritingAB600=0
		self.SAT_WritingAB500=0
		self.SAT_WritingAB400=0
		self.SAT_WritingAB300=0
		self.SAT_WritingAB200=0
		
		self.ACT_CompositeAvr=0
		self.ACT_CompositeAB30=0
		self.ACT_CompositeAB24=0
		self.ACT_CompositeAB18=0
		self.ACT_CompositeAB12=0
		self.ACT_CompositeAB06=0
		self.ACT_CompositeAB00=0
		
		self.highSchoolClassRank=0
		self.NationalMeritScholar=0
		self.Valedictorian=0
		self.ClassPresident=0
		self.StudentGovernmentOfficer=0
		
		self.CostOfAttendance=0
		self.TuitionFee=0
		self.RoomAndBoard=0
		self.BooksAndSupplies=0
		self.OtherExpenses=0
		#print self
		
	def Extract(self, fileName,outfile):
		f=open(fileName,'r')
		#output=open(outfile,'w')
		for line in f:
			if len(line)>0: #and re.match(r"\s*\S\s*",line)!=None:
				ff=line.split()
				#print(ff)

				if len(ff)>0:
					if ff[0]=='Address':
						self.Address= ' '.join(ff[1:])
						#print self.Address
					elif self.Name=='NEXT_LINE':
						self.Name=' '.join(ff)
						#print(self.Name)
					elif ff[0]=='Save':
						self.Name='NEXT_LINE';
					elif ff[0]=='Phone':
						self.Phone=' '.join(ff[1:])
						#print self.Phone
					elif ff[0]=='Fax':
						self.Fax=' '.join(ff[1:])
						#print self.Fax
					elif ff[0]=='E-mail':
						self.Email=' '.join(ff[1:])
						#print self.Email
					elif len(ff)>2 and ff[0]=='Average' and ff[1]=='GPA':
						#print ' '.join(ff)
						self.AverageGPA=ff[2]
						#print self.AverageGPA
					elif len(ff)>2 and ff[0]=='SAT' and ff[1]=='Math':
						self.SAT_MATHAverage=ff[2]
						#print self.SAT_MATHAverage
					elif len(ff)>2 and ff[0]=='SAT' and ff[1]=='Critical':
						self.SAT_ReadingAverage=ff[3]
						#print self.SAT_ReadingAverage
					elif len(ff)>2 and ff[0]=='SAT' and ff[1]=='Writing':
						self.SAT_WritingAverage=ff[2]
					elif len(ff)>2 and ff[0]=='ACT' and ff[1]=='Composite':
						self.ACT_CompositeAvr=ff[2]
						#print self.ACT_CompositeAvr
					elif len(ff)>3 and ff[0]=='Cost' and ff[2]=='Attendance':
						self.CostOfAttendance=' '.join(ff[3:])						
					elif len(ff)>3 and ff[0]=='Tuition' and ff[2]=='Fees':
						self.TuitionFee=' '.join(ff[3:])
						#print("self###", self.TuitionFee)
					elif len(ff)>3 and ff[0]=='Room' and ff[2]=='Board':
						self.RoomAndBoard=' '.join(ff[3:])
					elif len(ff)>3 and ff[0]=='Books' and ff[2]=='Supplies':
						self.BooksAndSupplies=' '.join(ff[3:])
					elif len(ff)>2 and ff[0]=='Other' and ff[1]=='Expenses':
						self.OtherExpenses=' '.join(ff[2:])
					elif ff[0] == 'City,':
						tmpline=' '.join(ff)
						self.City=' '.join(ff[3:])
						mm=re.search('(?<=(,[A-Z]{2}))\d{5}(-\d{4})*',tmpline)
						if mm!=None:
							#print mm.group(0)
							self.Zip=mm.group(0)
						mm=re.search('[A-Z]{2}(?=(\d{5}(-\d{4})*))',tmpline)
						if mm!=None:
							#print mm.group(0)
							self.State=mm.group(0)
				#output.write(line)
		
		


#for i in range (0, 3335):	
#	attrs=vars(colleges[i])

#	print ''.join("%s: %s\n" % item for item in attrs.items())		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
