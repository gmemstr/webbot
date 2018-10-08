(function() {
   //feed to parse
   var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var parser = new DOMParser();
	  var xmlDoc = parser.parseFromString(this.responseText,"text/xml");
	  var items = xmlDoc.getElementsByTagName("item");
	  for (var item of items) {
	  	var el = buildElement(item);
	  	var xmlString = el;
  		var parser = new DOMParser();
    	var doc = parser.parseFromString(xmlString, "text/html");
    	var documento = doc.getElementsByTagName('body')[0].firstChild;
	  	document.getElementById('app').appendChild(documento);
	  }
    }
   };
   xhttp.open("GET", "/rss", true);
   xhttp.send();
})();

var buildElement = (el) => {
	var guid = el.getElementsByTagName("guid").item(0).textContent
	var title = el.getElementsByTagName("title").item(0).textContent
	var link = el.getElementsByTagName("link").item(0) ? el.getElementsByTagName("link").item(0).textContent : "" // sometimes dont sent link
	var description = el.getElementsByTagName("description").item(0).textContent

    var element = "<div id='" + guid + "' class='message'>";
    element += "<h2>" + title + "</h2>";
    if (link != "") {
        element += "<a href='" + link + "'>" + description + "</a>";
    } else {
        element += description;
    }
    element += "</div>";
    return element;
}

function parseHTML(html) {
    var t = document.createElement('template');
    t.innerHTML = html;
    return t.content.cloneNode(true);
}