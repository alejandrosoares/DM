const inputName = document.querySelector('#contact input[name="name"]'),
  	inputEmail = document.querySelector('#contact input[name="email"]'),
  	textMessage = document.querySelector('#contact textarea[name="message"]');
      
function buildRequest() {
	/* Build the request to send */

	const csrf = document.querySelector(
		'#contact input[name="csrfmiddlewaretoken"]'
	).value;

	const data = {
		name: inputName.value,
		email: inputEmail.value,
		message: textMessage.value,
		};

	const headers = new Headers();
	headers.set("Content-Type", "application/json");
	headers.set("X-CSRFToken", csrf);
	headers.set("Access-Control-Allow-Origin", "same-origin");

	const request = {
		method: "POST",
		headers: headers,
		body: JSON.stringify(data)
	};

	return request;
}

function sendRequest(success, failed) {
    /* Request */

    const urlContact = document.querySelector("#contact input.contact-url").value;
    
    console.log(urlContact);

    fetch(urlContact, buildRequest())
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
        .catch( error => failedResponse());
}

export default sendRequest;

