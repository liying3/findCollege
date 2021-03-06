$( document ).ready(function() {
    $( "#accordion" ).accordion({
      collapsible: true
    });
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

       if(sat > 2400 || sat < 600 || gpa > 4 || gpa <0 || percentage>100 || percentage<0){
        alert("input out of range");
        //return
        sat = 2300;
        gpa = 3.5;
        percentage = 90;
        loc = 2;
        tuition = 1;
        major = 1;
       }
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
              
		     // console.log(data);
		      var cols = data.split(';');
		      console.log(cols.length-1);
			for (var i = 0; i < cols.length-1; i++)
			{
			    var t = cols[i].split('&');
			    var col = { name:t[0], loc:t[1], tuition:t[2], aGPA:t[3], aSAT:t[4], chance:t[5], img:t[6]};
				colleges[i] = col;
				codeAddress(i, colleges[i]['name']);
			}

			fillTable();

     // $('#result-table tr').click(function(){
       // $(this).next().slideToggle(500);
       //$(this).next().animate({down:'250px'});
       // toggle_visibility('sch-content');
     // });
		  },
        });   
	});
	
	function showDetailInfo(i) {
	    $('#cName').text(colleges[i]['name']);
	    $('#cLoc').text(colleges[i]['loc']);
	    $('#cTuition').text(colleges[i]['tuition']);
	    $('#cSAT').text(colleges[i]['aSAT']);
	    $('#cGPA').text(colleges[i]['aGPA']);
	}

	function fillTable() {
       $('#accordion').html('');
	    for (var i = 0; i < colleges.length; i++) {5
        var newTable = '<table><tr><td width="5%">' + String(i+1) +'</td><td width="230px">' + confineLength(colleges[i]['name'],28) +'</td><td width="60px">' + colleges[i]['loc']+'</td><td width="60px">'+ colleges[i]['tuition']+'</td><td width="9%">'+colleges[i]['aGPA']+'</td><td width="80px">'+colleges[i]['aSAT']+'</td><td width="auto">'+ parseFloat(colleges[i]['chance']).toFixed(2) +'%</td></tr></table>';
        var newDetail =  '<p><img src = "pics/'+ colleges[i]['img'] +'.jpg" width = "200px", height = "200px"><br>Name of school: '+ colleges[i]['name'] +'<br>Location: '+ colleges[i]['loc']+'<br>Tuition: '+colleges[i]['tuition']+'<br>SAT: '+colleges[i]['aSAT']+'<br>GPA: '+colleges[i]['aGPA']+'<br></p>';
        var newItem = '<div id = c' + i + '> ' + newTable + '</div><div>' + newDetail + '</div>';
        $('#accordion').append(newItem).accordion('destroy').accordion();
	        //var newRow = '<tr id=c' + i + ' ><td >' + String(i+1) + '</td><td>' + colleges[i]['name'] + '</td><td>' + colleges[i]['loc'] + '</td><td>' + colleges[i]['tuition'] + '</td><td>' + colleges[i]['aGPA'] + '</td><td>' + colleges[i]['aSAT'] + '</td><td>' + colleges[i]['chance'] + '</td></tr>';
	        //$('#result-table').append(newRow);
	    }
       $( "#accordion" ).accordion( "refresh" );
        $( "#accordion" ).accordion({
      collapsible: true
    });
	}

  function confineLength(str,len){
        len = len || 0;
        if(str.length > len){
          var a = str.substring(0,len) + "...";
          return a;
        }
         return str;
  }

   function toggle_visibility(id) {
       var e = document.getElementById(id);
       if(e.style.display == 'block')
          e.style.display = 'none';
       else
          e.style.display = 'block';
    }
	
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
                //showDetailInfo(key);
                $( "#accordion" ).accordion( "option", "active", false);
                $( "#accordion" ).accordion( "option", "active", key);
              }
            }(i));

             google.maps.event.addListener(markers[i], 'mouseover', function(key) {
                  return function() {
                  var mx = event.pageX;
                  var my = event.pageY;
                  $("#img-preview").css("left", mx + "px");
                  $("#img-preview").css("top", my + "px");
                  $("#img-preview").css("display", "block");
                  $('#name-preview').text(colleges[key]['name']);
                  $('#img-preview img').attr({src: "pics/" + colleges[key]['img'] + ".jpg"});
             }
            }(i)); 
      
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