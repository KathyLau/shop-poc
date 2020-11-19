
function clearDisplay(){
	$("#name").empty();
	$("#location").empty();
	$("#rating").empty();
	$("#image").empty();
	$("#text").empty();
	$("#list").empty();
}

function display(returnlist){
	clearDisplay();
	console.log("hi");
	var returnlist = returnlist
	var len = $(returnlist).length;
	console.log("what="+len);
	var name = $("<div>");
	var location = $("<div>");
	var rating = $("<div>");
	var text = $("<div>");
	var image = $("<img src="+returnlist[0]["image"]+">")
	$(image).addClass("img-fluid")
	var alt_text = returnlist[0]["name"]+" taco";
	
	//add alt text to image
	$(image).attr('alt', alt_text)

	$(name).text(returnlist[0]["name"]);
	console.log("name:"+ name);
	$("#name").append(name);

	$(location).text("Borough: " +returnlist[0]["location"]);
	$("#location").append(location)

	$(rating).text("Rating: "+returnlist[0]["rating"]+" out of 5 Stars");
	$("#rating").append(rating)

	$(text).text(returnlist[0]["text"]);
	$("#text").append(text)

	$("#image").append(image);
	console.log("flag 1");
	var race_list = returnlist[0]["racelist"];
	console.log("start loop");

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