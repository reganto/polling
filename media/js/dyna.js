function manage(url) {
    var xhrObject = new XMLHttpRequest();
    xhrObject.open('POST', url, true);
    xhrObject.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
    xhrObject.onreadystatechange = function() {
        if(xhrObject.readyState == 1) {
            console.log("readystate is 1");
        } else if(xhrObject.readyState == 2) {
            console.log("readystate is 2");
        } else if (xhrObject.readyState == 3) {
            console.log("readystate is 3");
        } else if (xhrObject.readyState == 4) {
            console.log("readystate is 4");
            updatePage(xhrObject.responseText);
        } else {
            console.log("other");
        }
    }
    xhrObject.send(getQueryString());
}

function getQueryString() {
    var form = document.forms['reg'];
    var username = form.username.value;
    qstr = "username="+username;
    return qstr;
}

function updatePage(response) {
    document.getElementById("demo").innerHTML = response;
}

