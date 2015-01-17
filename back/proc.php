<?php
	$Count = 0;
	
	$SAT = $_POST['sat'];
	$GPA = $_POST['gpa'];
	$TopPercentage = $_POST['percentage'];
	$Locations = $_POST['loc'];
	$Tuition = $_POST['tuition'];
	$Concentration = $_POST['major'];
	
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
	
	$college1 = new College("University of Pennsylvania", "Philadephia, PA", 60000, 2100, 3.66);
	$college2 = new College("Stanford University", "Stanford, CA", 70000, 2300, 3.80);
	$college3 = new College("University of Califorlia Los Angeles", "Los Angeles, CA", 50000, 1800, 3.00);
	
	$GLOBALS['colleges'] = [$college1, $college2, $college3];
	
	echo FindColleges($SAT, $GPA, $TopPercentage, $Locations, $Tuition, $Concentration);
	
	function FindColleges($SAT, $GPA, $TopPercentage, $Locations, $Tuition, $Concentration) {
		/*echo "My SAT: " + $SAT + "My GPA: " + $GPA + "\n";*/
		return getString($GLOBALS['colleges']);
	}
	
	function getString($colleges)
	{
		$s = "";
		foreach ($colleges as $college)
		{
			$s .= $college->name . "&" . $college->loc . "&" . $college->tuition . "&" . $college->aSAT . "&" . $college->aGPA . ";";
		}
		return $s;
	}
?>