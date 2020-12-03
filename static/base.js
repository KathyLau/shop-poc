$(document).ready(function(){

//handles search if user clicks the go button in search bar
    $("#top_submit_button").click(function(){
      //get user input
      var search_input = $("#top_search_input").val()
  
      search_input = search_input.trim();
      console.log("input: "+ search_input)
      if(search_input.length>0){
          var route = "../search/?s="+search_input;
          window.location.href=route;
        }

    })

    //handles search if user hits enter in the searchbar
    $("#top_search_input").keypress(function(e) {
      if (e.keyCode == 13) {
        var search_input = $("#top_search_input").val()
    
        search_input = search_input.trim();
        console.log("input: "+ search_input)
        if(search_input.length>0){
          var route = "../search/?s="+search_input;
          window.location.href=route;
        }
      }

  })

})
