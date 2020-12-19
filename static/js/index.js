//displaycards function displays the businesses in the form of Twitter Bootstrap Cards
//does so by calling on showcards function
var displaycards = function(){

	$.ajax({
		type: "POST",
        url: "displaycards",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        success: function(data){
        	$("#results").empty();
            var all_data = data["returnlist"]
            returnlist = all_data

            console.log("returnlist len:"+ returnlist.length)
            showcards(returnlist);
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
	})
}

//showcards function shows appropriate buisness cards given a list of buisnesses
function showcards(returnlist){

	var row1 = $("<div class='card-deck'>")

    $.each(returnlist, function(i,value){
        var card = $("<div class='card'>");
        $(card).attr("id", value["id"]);

        var img = $("<img class='card-img-top' src=" +returnlist[i]["image"]+ ">");
        var alt_text = returnlist[i]["name"]+" taco";
        $(img).attr('alt', alt_text);
        var cardbodydiv = $("<div class='card-body'>");
        var name = $("<h5 class='card_title'>");
        var service = $("<p class='card-text'>");
        var location = $("<p class='card-text'>");


        $(card).click(function(){
            console.log("row id: " + value["id"])
            var route = "view/"+value["id"];
            window.location.href=route;

        })

        $(name).text(returnlist[i]["name"]);
        $(location).text(returnlist[i]["location"])
        $(service).text(returnlist[i]["service"])

        $(card).append(img);
        $(cardbodydiv).append(name);
        $(cardbodydiv).append(location);
        $(cardbodydiv).append(service);
        $(card).append(cardbodydiv);
        $(card).addClass("row_outline")
        $(row1).append(card);
    })
    $("#results").append(row1);
}


$(document).ready(function(){
	displaycards();
})
