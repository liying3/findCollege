<?php
	$Count = 0;
	
	$SAT = $_POST['sat'];
	$GPA = $_POST['gpa'];
	$TopPercentage = $_POST['percentage'];
	$Locations = $_POST['loc'];
	$Tuition = $_POST['tuition'];
	$Concentration = $_POST['major'];
 
  $GLOBALS['colleges'] = ["The University of Pennsylvania", "Pennsylvania", 60000, 2100, 3.66,5.0,"Stanford University", "California", 70000, 2300, 3.80,4.0,"Drexel University", "Pennsylvania", 50000, 1800, 3.00,3.0];

	echo FindColleges($SAT, $GPA, $TopPercentage, $Locations, $Tuition, $Concentration);
	
	function FindColleges($SAT, $GPA, $TopPercentage, $Locations, $Tuition, $Concentration) {
   // exec("Q:\Python34\python CollegeSearch.py" ." " .$SAT . " ". $GPA. " ".  $TopPercentage. " ".  $Locations. " ".  $Tuition. " ".  $Concentration, $output);
    //var_dump($output);
   // return getString($output);
    return getString($GLOBALS['colleges']);
	}
	
	function getString($out)
	{
		$s = "";
		for ($i = 0; $i < count($out)/6; $i++)
		{
      $s .= $out[$i*6] . "&" . $out[$i*6+1] . "&" . $out[$i*6+2] . "&" . $out[$i*6+3] . "&" . $out[$i*6+4] . "&" . $out[$i*6+5] . ";" ;
		}
		return $s;
	}
?>