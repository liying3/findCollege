<?php
	$Count = 0;
	
	class College{
		var $name;
		var $loc;
        var $tuition;
        var $aSAT;
		var $aGPA;
		
		function College($name="N/A", $loc="N/A", $tuition=0, $aSAT=1, $aGPA=1)
		{
			$this->name = $name;
			$this->loc = $loc;
			$this->tuition = $tuition;
			$this->aSAT = $aSAT;
			$this->aGPA = $aGPA;
		}
	}
	
	$college1 = new College("The University of Pennsylvania", "Pennsylvania", 60000, 2100, 3.66);
	$college2 = new College("Stanford University", "California", 70000, 2300, 3.80);
	$college3 = new College("Drexel University", "Pennsylvania", 50000, 1800, 3.00);
	
	$colleges = [$college1, $college2, $college3];

	echo $Concentration;
/*	+ " " + $GPA +" "+ $TopPercentage + " " + $Locations+"  "+$Tuition+" " + $Concentration;*/
	
	function FindColleges($SAT, $GPA, $TopPercentage, $Locations, $Tuition, $Concentration) {
		/*echo "My SAT: " + $SAT + "My GPA: " + $GPA + "\n";*/
		
		return $colleges;
	}
?>