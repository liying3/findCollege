<?php
	$Count = 0;
	
/*	$SAT = $_POST['sat'];
	$GPA = $_POST['gpa'];
	$TopPercentage = $_POST['percentage'];
	$Locations = $_POST['loc'];
	$Tuition = $_POST['tuition'];
	$Concentration = $_POST['major'];*/
  
  $SAT = 1500;
	$GPA = 3.8;
	$TopPercentage = 10;
	$Locations = "CA";
	$Tuition = 20000;
	$Concentration = "CS";
  
	$GLOBALS['college1'] = ["University of Pennsylvania", "Philadephia, PA", 60000, 2100, 3.66];
	
	echo FindColleges($SAT, $GPA, $TopPercentage, $Locations, $Tuition, $Concentration);
	
	function FindColleges($SAT, $GPA, $TopPercentage, $Locations, $Tuition, $Concentration) {
    exec("Q:\Python34\python CollegeSearch.py" ." " .$SAT . " ". $GPA. " ".  $TopPercentage. " ".  $Locations. " ".  $Tuition. " ".  $Concentration, $output);
    var_dump($output);
    return getString($output);
    //return getString($GLOBALS['college1']);
	}
	
	function getString($out)
	{
		$s = "";
    echo count($out);
		for ($i = 0; $i < count($out)/6; $i++)
		{
      $s .= $out[$i*6] . "&" . $out[$i*6+1] . "&" . $out[$i*6+2] . "&" . $out[$i*6+3] . "&" . $out[$i*6+4] . "&" . $out[$i*6+5] . ";" ;
		}
		return $s;
	}
?>