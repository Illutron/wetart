$(document).ready(function(){

    $.getJSON("http://api.flickr.com/services/feeds/photos_public.gne?tags=wetart2011&format=json&jsoncallback=?", function(data){
      $.each(data.items, function(i,item){
        $("<img/>").attr("src", item.media.m).appendTo("#flickrfeed")
          .wrap("<a href='" + item.link + "'></a>");
      });
    });




   // $.getJSON("http://search.twitter.com/search.json?q=%23wetart&jsoncallback=?", function(data){
   //   $.each(data.items, function(i,item){
   //     $("<div>").attr("src", item.media.m).appendTo("#twitterfeed")
   //       .wrap("<a href='" + item.link + "'></a>");
   //   });
   // });

    //$.getJSON("http://search.twitter.com/search.json?q=illutron&jsoncallback=?", function(data){
    //    $.each(data, function(i,item){
      //     ct = item.text;
        //   ct = ct.replace(/http:\/\/\S+/g, "<a href='$&' target='_blank'>$&</a>");
         ///  ct = ct.replace(/\s(@)(\w+)/g, " @<a target='_blank'>$2</a>");
   //        ct = ct.replace(/\s(#)(\w+)/g, " #<a href='http://search.twitter.com/search?q=%23$2' target='_blank'>$2</a>");
   //        $("#twitterfeed").append('<div>'+ct +'</div>');
   //     });
   // });

    $("#twitterfeed").tweet({
        query: "#wetart OR #platform4dk OR #illutron OR from:platform4dk OR from:illutron",
        avatar_size: 32,
        count: 20,
        loading_text: "loading tweets..."
    });
    

});

