// clears all data from previously displayed search
function clearDisplay(){
	$("#name").empty();
	$("#location").empty();
	$("#rating").empty();
	$("#image").empty();
	$("#text").empty();
	$("#list").empty();
	$("#type").empty();
}

//function to display the business
function display(returnlist){
	//clear data from previous search (if any)
	clearDisplay();
	
	//creating variables
	var returnlist = returnlist
	var name = $("<div>");
	var location = $("<div>");
	var rating = $("<div>");
	var text = $("<div>");
	var type = $("<div>");
	var image = $("<img src="+returnlist[0]["image"]+">")

	//add attribute to make the image fluid
	$(image).addClass("img-fluid")
	var alt_text = returnlist[0]["name"]+" business";
	
	//add alt text to image
	$(image).attr('alt', alt_text)

	//append name to html site
	$(name).text(returnlist[0]["name"]);
	$("#name").append(name);

	$(location).text("Borough: " +returnlist[0]["location"]);
	$("#location").append(location)

	$(rating).text("Rating: "+returnlist[0]["rating"]+" out of 5 Stars");
	$("#rating").append(rating)

	$(text).text(returnlist[0]["text"]);
	$("#text").append(text)

	$(type).text("Type of Business: "+returnlist[0]["type"]);
	$("#type").append(type)

	$("#image").append(image);
	console.log("flag 1");
	var race_list = returnlist[0]["racelist"];
	//below is just a check for developer
	console.log("start loop");

	//loop to list each minority race that the business is associated with
	$.each(race_list, function(i,value){
		console.log("race:"+value["race"]);
		var item = $("<div>");
		$(item).text("- "+value["race"]);

	$(item).addClass("little_pad")

	$("#list").append(item);
		
	})
	


}


$(document).ready(function(){
	display(returnlist);
})