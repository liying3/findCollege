$( document ).ready(function() {
	$('.form-inline').on('click', '.submit', function(e){
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
			
		  },
        });   
	});
});