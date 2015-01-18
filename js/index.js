$( document ).ready(function() {
	var colleges = [];
	
    /*---------------------------- form -----------------------------*/
	$('#search-form').submit(function (e) {
	    e.preventDefault()

       var sat = $('#sat').val();
       var gpa = $('#gpa').val();
       var percentage = $('#percentage').val();
       var loc = $('#location').val();
	   var tuition = $('#tuition').val();
	   var major = $('#major').val();

	   console.log(sat);
	   console.log(gpa);
	   console.log(percentage);
	   console.log(loc);
	   console.log(tuition);
	   console.log(major);

	   var tuitionPrio = 1;
	   var majorPrio = 2;
	   var i = 0;
	   $('#sortable').children().each(function () {
	       if ($(this).attr('id') == 'tuition-pri')
	           tuitionPrio = ++i;
	       else if ($(this).attr('id') == 'major-pri')
	           majorPrio = ++i;
	   });
        $.ajax({
          type: "POST",
          url: "back/proc.php",
		  data: { sat: sat, gpa: gpa, percentage: percentage, loc:loc, tuition:tuition, major:major},
		  success: function (data, status) {
		      console.log(data);
			var cols = data.split(';');
			for (var i = 0; i < cols.length-1; i++)
			{
			    var t = cols[i].split('&');
			    var col = { name:t[0], loc:t[1], tuition:t[2], aGPA:t[3], aSAT:t[4], chance:t[5]};
				colleges[i] = col;
				codeAddress(i, colleges[i]['name']);
			}
		  },
        });   
	});
	function showColInfo(i)
	{
		$('#cName').text(colleges[i]['name']);
		$('#cLoc').text(colleges[i]['loc']);
		$('#cTuition').text(colleges[i]['tuition']);
		$('#cSAT').text(colleges[i]['aSAT']);
		$('#cGPA').text(colleges[i]['aGPA']);
	}

    //drag and drop
	$(function () {
	    $("#sortable").sortable();
	    $("#sortable").disableSelection();
	});
	
    //google map

	  var markers = [];
       var map;      
       var geocoder;
      function initialize() {
        var mapCanvas = document.getElementById('map-canvas');
        geocoder = new google.maps.Geocoder();
        var myLatlng = new google.maps.LatLng(-25.363882,131.044922);
        var mapOptions = {
          zoom: 4,
          center: myLatlng
        }
        map = new google.maps.Map(mapCanvas, mapOptions);
      }

      function codeAddress(i, addr) {      
        //var address = document.getElementById('address').value;     
         geocoder.geocode( { 'address': addr}, function(results, status) {      
           if (status == google.maps.GeocoderStatus.OK) {      
            
             map.setCenter(results[0].geometry.location);           
             var tmp = new google.maps.Marker({      
                 map: map,     
                 position: results[0].geometry.location      
             });     
             markers[i] = tmp;

             google.maps.event.addListener(markers[i], 'click', function(key) {
                return function() {
                $("#sch-content").css("display", "block");
                showColInfo(key);
              }
            }(i));

             google.maps.event.addListener(markers[i], 'mouseover', function() {
                  var mx = event.pageX;
                  var my = event.pageY;
                  $("#img-preview").css("left", mx + "px");
                  $("#img-preview").css("top", my + "px");
                  $("#img-preview").css("display", "block");
            });   
      
            google.maps.event.addListener(markers[i], 'mouseout', function() {
                  $("#img-preview").css("display", "none");
            });   


           } else {      
             alert('Geocode was not successful for the following reason: ' + status);      
           }     
         });     
       }  
	   
      google.maps.event.addDomListener(window, 'load', initialize);	  
});