function checkEmpty(name,location,web,service,img,type){
	var lowered_location = location.toLowerCase()

	var pass = 1;

	if(name.length == 0){
		console.log("missing entry for name")
		pass = 0
		var msg = $("<div>")
		$(msg).text("missing entry")
		$("#name_warn").append(msg);
	}

	if(location.length == 0){
		console.log("location is empty")
		pass = 0
		var msg = $("<div>")
		$(msg).text("missing entry")
		$(msg).removeClass("red_mini")
		$(msg).removeClass("red_location")
		$(msg).addClass("red_mini")
		$("#location_warn").append(msg);
	}
	else if(lowered_location == "brooklyn"){
		pass = 1;
		location = "Brooklyn"
	}
	else if(lowered_location == "manhattan"){
		pass= 1;
		location = "Manhattan"
	}
	else if(lowered_location == "queens"){
		pass = 1;
		location = "Queens"
	}
	else if(lowered_location == "the bronx"){
		pass = 1;
		location = "the Bronx"
	}
	else if(lowered_location == "bronx"){
		pass = 1;
		location = "the Bronx"
	}
	else if(lowered_location == "staten island"){
		pass = 1;
		location = "Staten Island"
	}
	else{
		pass = 0;
		var msg = $("<div>")
		$(msg).text("Invalid Entry. The borough must be one of the following 5: Manhattan, Brooklyn, the Bronx, Queens, or Staten Island")
		$(msg).removeClass("red_mini")
		$(msg).removeClass("red_location")
		$(msg).addClass("red_location")
		$("#location_warn").append(msg);
	}


	if(web.length == 0){
		pass = 0;
		var msg = $("<div>")
		$(msg).text("missing entry")
		$("#web_warn").append(msg);
	}

	if(service.length == 0){
		pass = 0;
		var msg = $("<div>")
		$(msg).text("missing entry")
		$("#service_warn").append(msg);
	}

	if (img.length == 0){
		pass = 0;
		var msg = $("<div>")
		$(msg).text("missing jpeg for image")
		$("#img_warn").append(msg);
	}

	if (type.length == 0){
		pass = 0;
		var msg = $("<div>")
		$(msg).text("missing entry")
		$("#type_warn").append(msg);
	}

	if(pass == 1){
		console.log("passed all checks")
		submit(name, location, web, service, img, type);
	}
	else{
		var warn  = $("<div>")
		$(warn).addClass("red_warn")
		$(warn).text("There is an error in one or more of the fields");
		$("#top_warn").append(warn);
	}

}


function clearAll(){
	$("#name_entry").val('');
	$("#location_entry").val('');
	$("#web_entry").val('');
	$("#service_entry").val('');
	$("#img_entry").val('');
	$("#type_entry").val('');
}

var submit = function(name, location, web, service, img, type){
	var name = name
	var location = location
	var web = web
	var service = service
	var img = img
	var type = type

//NOTE: Here we name the variable web to text as server stores website address under "text"
    var submit_input = {
    	'name': name,
    	'location': location,
    	'text': web,
    	'service': service,
    	'image': img,
    	'type': type
    }
    

    $.ajax({
        type: "POST",
        url: "add",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(submit_input),
        success: function(result){
	        var success_msg = $("<div>");
	        $(success_msg).text("New item successfully created.");
	        $(success_msg).addClass("blue_success");
	        $("#top_warn").append(success_msg);
	        clearAll();
	        $("#name_entry").focus();

	       
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


$(document).ready(function(){
	console.log("create page");
	
	$("#submit_button").click(function(){
		console.log("you hit submit");
		$("#top_warn").empty();
		$("#name_warn").empty();
		$("#location_warn").empty();
		$("#web_warn").empty();
		$("#service_warn").empty();
		$("#img_warn").empty();
		$("#type_warn").empty();

		var name = $("#name_entry").val();
		name = name.trim();

		var location = $("#location_entry").val();
		location = location.trim();

		var web = $("#web_entry").val();
		web = web.trim();

		var service= $("#service_entry").val();
		service = service.trim();

		var img = $("#img_entry").val();
		img = img.trim();

		var type= $("#type_entry").val();
		type = type.trim();

		checkEmpty(name,location,web,service,img,type);

	})
	
})