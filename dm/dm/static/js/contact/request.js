function sendRequest(data, success, failed) {
	const urlContact = document.querySelector("#contact input.contact-url").value;

	fetch(urlContact, buildRequest(data))
		.then( response => {
			if (response.ok) return response.json();
		})
		.then( object => {
			if (object.status === "ok") {
				success();
			} else {
				failed();
			}
		})
		.catch( error => { 
			console.error(error);
			failed();
		});
}


function buildRequest(data) {
	const headers = buildHeaders();
	const request = {
		method: "POST",
		headers: headers,
		body: JSON.stringify(data)
	};

	return request;
}


function buildHeaders() {
	const headers = new Headers();
	const token = getTokenValue();
	headers.set("Content-Type", "application/json");
	headers.set("X-CSRFToken", token);
	headers.set("Access-Control-Allow-Origin", "same-origin");
	return headers;
}


function getTokenValue() {
	const csrfNode = document.querySelector(
		'#contact input[name="csrfmiddlewaretoken"]');
	return csrfNode.value;
}


export default sendRequest;

