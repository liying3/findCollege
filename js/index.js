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
           
        $.ajax({
          type: "POST",
          url: "back/proc.php",
		  data: { sat: sat, gpa: gpa, percentage: percentage, loc:loc, tuition:tuition, major:major},
		  success: function(data, status) {
			var cols = data.split(';');
			for (var i = 0; i < cols.length-1; i++)
			{
				var t = cols[i].split('&');
				var col = { name:t[0], loc:t[1], tuition:t[2], aSAT:t[3], aGPA:t[4] };
				colleges[i] = col;
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
	var marker; 
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
       // var image = 'https://dl.dropboxusercontent.com/u/53181465/graphics/Best7_Texture.png';
        marker = new google.maps.Marker({
            position: myLatlng,
           // title:"Hello World!",
           // icon: image
        });

        // To add the marker to the map, call setMap();
        marker.setMap(map);
       // marker.setMap(null);   // To remove the marker

       google.maps.event.addListener(marker, 'click', function() {
        //infowindow.open(map,marker);
        $("#sch-content").css("display", "block");
		showColInfo(0);
      });

       google.maps.event.addListener(marker, 'mouseover', function() {
            var mx = event.pageX;
            var my = event.pageY;
            $("#img-preview").css("left", mx + "px");
            $("#img-preview").css("top", my + "px");
            $("#img-preview").css("display", "block");
      });   
 

      google.maps.event.addListener(marker, 'mouseout', function() {
            $("#img-preview").css("display", "none");
      });

      }
      function codeAddress() {      
         var address = document.getElementById('address').value;     
         geocoder.geocode( { 'address': address}, function(results, status) {      
           if (status == google.maps.GeocoderStatus.OK) {      
             map.setCenter(results[0].geometry.location);      
             marker.setMap(null);      
             var tmp = new google.maps.Marker({      
                 map: map,     
                 position: results[0].geometry.location      
             });     
             marker = tmp;     
           } else {      
             alert('Geocode was not successful for the following reason: ' + status);      
           }     
         });     
       }  
	   
      google.maps.event.addDomListener(window, 'load', initialize);	  
});