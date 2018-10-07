$(document).ready(function() {
	//feed to parse
	var feed = "/rss";

	$.ajax(feed, {
		accepts:{
			xml:"application/rss+xml"
		},
		dataType:"xml",
		success:function(data) {
			//Credit: http://stackoverflow.com/questions/10943544/how-to-parse-an-rss-feed-using-javascript
			$(data).find("item").each(function () { // or "item" or whatever suits your feed
				var el = buildElement($(this))
				$("#app").append(el);
			});


		}
	});
});

var buildElement = (el) => {
    var element = "<div id='"+el.find("guid").text()+"' class='message'>";
    element += "<h2>" + el.find("title").text() + "</h2>";
    if (el.find("link").text() != "") {
        element += "<a href='" + el.find("link").text() + "'>" + el.find("description").text() + "</a>";
    } else {
        element += el.find("description").text();
    }
    element += "</div>";
    return element;
}