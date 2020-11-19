function showcards(searchlist, searchterm){

    var n = searchlist.length
    var thenumber = $("<div>")
    $(thenumber).text("Found "+n+" result(s)")
    $(thenumber).addClass("bold")
    $("#numberofresults").append(thenumber)

    var row1 = $("<div class='card-deck'>")

    $.each(searchlist, function(i,value){
        var card = $("<div class='card'>");
        $(card).attr("id", value["id"]);
        
        var img = $("<img class='card-img-top' src=" +searchlist[i]["image"]+ ">");
        var alt_t = searchlist[i]["name"]+" taco"
        console.log(alt_t);
        $(img).attr('alt', alt_t);
        var cardbodydiv = $("<div class='card-body'>");
        var name = $("<h5 class='card_title'>");
        var rating = $("<p class='card-text'>");
        var location = $("<p class='card-text'>");


        $(card).click(function(){
            console.log("row id: " + value["id"])
            var route = "http://127.0.0.1:5000/view/"+value["id"];
            //var route = "view"
            window.location.href=route;
            //window.location.href= "{{ url_for('view', id = 'stuff') }}".replace("stuff", id);
            //return false;
        })

        $(name).text(searchlist[i]["name"]);

        
        var name_lower = value["name"].toLowerCase()
        var loc_lower = value["location"].toLowerCase()
        var search_lower = searchterm.toLowerCase()
        if(name_lower.includes(search_lower)){
            $(name).addClass("yellow");
        }
        if(loc_lower.includes(search_lower)){
            $(location).addClass("yellow");
        }
        //$(name).addClass("red")
        $(location).text(searchlist[i]["location"])
        $(rating).text(searchlist[i]["rating"]+" out of 5 Stars");

        //var star = $("<span class='glyphicon glyphicon-star-empty'>")


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

    var topName = $("<div>")
    $(topName).text("Search Results for '"+ searchterm+ "'")
    $("#name").append(topName)

    if(searchlist.length>0){
        showcards(searchlist, searchterm);
        //displayResultBanner();
        //displayResults(searchlist);
    }
    else{
        var message = $("<div>");
        $(message).text("There are 0 results");
        $(message).addClass("red");
        $("#numberofresults").append(message);
    }
    $("#top_search_input").val('').focus();
    
})