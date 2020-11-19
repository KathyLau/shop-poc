var displaycards = function(){

	$.ajax({
		type: "POST",
        url: "displaycards",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        success: function(data){
        	console.log("got to success")
        	$("#results").empty();
            var all_data = data["returnlist"]
            returnlist = all_data

            console.log("returnlist len:"+ returnlist.length)
            showcards(returnlist);
           // showcards(returnlist);
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
	})
}

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
        var rating = $("<p class='card-text'>");
        var location = $("<p class='card-text'>");


        $(card).click(function(){
            console.log("row id: " + value["id"])
            var route = "view/"+value["id"];
            //var route = "view"
            window.location.href=route;
            //window.location.href= "{{ url_for('view', id = 'stuff') }}".replace("stuff", id);
            //return false;
        })

        $(name).text(returnlist[i]["name"]);
        //$(name).addClass("red")
        $(location).text(returnlist[i]["location"])
        $(rating).text(returnlist[i]["rating"]+" out of 5 Stars")

        $(card).append(img);
        $(cardbodydiv).append(name);
        $(cardbodydiv).append(location);
        $(cardbodydiv).append(rating);
        $(card).append(cardbodydiv);
        $(card).addClass("row_outline")
        $(row1).append(card);
    })
    $("#results").append(row1);
}

$(document).ready(function(){
	displaycards();
})