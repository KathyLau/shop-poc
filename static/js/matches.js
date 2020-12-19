//a function to show the cards of buisnesses related to the search term
function showcards(searchlist, searchterm){

    //establishing number of results found
    var n = searchlist.length
    var thenumber = $("<div>")
    $(thenumber).text("Found "+n+" result(s)")
    $(thenumber).addClass("bold")
    $("#numberofresults").append(thenumber)

    //creating card deck
    var row1 = $("<div class='card-deck'>")

    $.each(searchlist, function(i,value){
        var card = $("<div class='card'>");
        $(card).attr("id", value["id"]);

        var img = $("<img class='card-img-top' src=" +searchlist[i]["image"]+ ">");
        var alt_t = searchlist[i]["name"]+" taco"
        console.log(alt_t); //log name to console
        $(img).attr('alt', alt_t);
        var cardbodydiv = $("<div class='card-body'>");
        var name = $("<h5 class='card_title'>");
        var service = $("<p class='card-text'>");
        var location = $("<p class='card-text'>");

        //card click function
        $(card).click(function(){
            console.log("row id: " + value["id"])
            var route = "../view/"+value["id"];
            window.location.href=route;
        })

        $(name).text(searchlist[i]["name"]);

        //set all searchable fields to lowercase to make them easily comparable
        var name_lower = value["name"].toLowerCase()
        var loc_lower = value["location"].toLowerCase()
        var search_lower = searchterm.toLowerCase()

        //highlight the field with search term in it yellow, to make it clear what matched
        if(name_lower.includes(search_lower)){
            $(name).addClass("yellow");
        }
        if(loc_lower.includes(search_lower)){
            $(location).addClass("yellow");
        }

        $(location).text(searchlist[i]["location"])
        $(service).text(searchlist[i]["service"]);


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
	console.log("MATCHES")

    //set up search results row
    var topName = $("<div>")
    $(topName).text("Search Results for '"+ searchterm+ "'")
    $("#name").append(topName)

    //display cards of buisness that match searched term
    if(searchlist.length>0){
        showcards(searchlist, searchterm);
    }
    else{
    //if no cards match searched term, say there are no results
        var message = $("<div>");
        $(message).text("There are 0 results");
        $(message).addClass("red");
        $("#numberofresults").append(message);
    }
    //refocus cursor in searchbox
    $("#top_search_input").val('').focus();

})
