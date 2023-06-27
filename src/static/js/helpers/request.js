function send(request, url, success, failed) {
    _send();

    function _send() {
	    fetch(url, request)
            .then( response => {
                if (response.ok) return response.json();
            })
            .then( object => {
                if (object.status === "ok") {
                    success(object);
                } else {
                    failed(object);
                }
            })
            .catch(error => failed(object));
    }
}


async function sendSync(request, url) {
    const response = await fetch(url, request)
            .then( response => {
                if (response.ok) return response.json();
            })
            .then( object => {
                return (object.status === "ok")? object: null;
            })
            .catch(error => console.error(error));
    return response;
}


function buildPostRequest(data, token) {
    const headers = buildHeaders(token);
    return {
        method: 'POST',
        headers: headers,
        body: data? JSON.stringify(data): null
    };
}


function buildGetRequest(token) {
    const headers = buildHeaders(token);
    return {
        method: 'GET',
        headers: headers,
    };
}


function buildHeaders(token = null) {
    const headers = new Headers();
    headers.set("Content-Type", "application/json");
    headers.set("X-CSRFToken", token || getDefaultToken());
    headers.set("Access-Control-Allow-Origin", "same-origin");
    return headers;
}


function getDefaultToken() {
    const divReferences = document.querySelector('div.data-reference');
    const inputToken = divReferences.querySelector('input[name="csrfmiddlewaretoken"]');
    return inputToken.value;
}


export {
    send,
    sendSync,
    buildPostRequest,
    buildGetRequest
};