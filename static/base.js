$(document).ready(function(){

//search
    $("#top_submit_button").click(function(){
      //get user input
      var search_input = $("#top_search_input").val()
  
      search_input = search_input.trim();
      console.log("input: "+ search_input)
      if(search_input.length>0){
          var route = "http://127.0.0.1:5000/search/?s="+search_input;
          window.location.href=route;
        }
      //search(search_input);
      //don't forget to catch for caps, mispelling, hitting enter, !!!!!!

    })

    $("#top_search_input").keypress(function(e) {
      if (e.keyCode == 13) {
        var search_input = $("#top_search_input").val()
    
        search_input = search_input.trim();
        console.log("input: "+ search_input)
        if(search_input.length>0){
          var route = "http://127.0.0.1:5000/search/?s="+search_input;
          window.location.href=route;
        }
      }

  })

})