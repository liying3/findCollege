$( document ).ready(function() {
	var colleges = [];
	
	$('#search-form').submit(function(e){
       e.preventDefault() 
       
       //lets get our values from the form....
       var sat = $('#sat').val();
       var gpa = $('#gpa').val();
       var percentage = $('#percentage').val();
	   var loc = $('#location').val();
	   var tuition = $('#tuition').val();
	   var major = $('#major').val();
           
       //now lets make our ajax call
        $.ajax({
          type: "POST",
          url: "back/proc.php",
		  data: { sat: sat, gpa: gpa, percentage: percentage, loc:loc, tuition:tuition, major:major},
		  success: function(data, status) {
			var cols = data.split(';');
			for (var i = 0; i < cols.length-1; i++)
			{
				var t = cols[i].split(',');
				var col = { name:t[0], loc:t[1], tuition:t[2], aSAT:t[3], aGPA:t[4] };
				colleges[i] = col;
			}
			alert(colleges[0]['name']);
		  },
        });   
	});
	
	
});