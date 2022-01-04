/*
    CONTACT SECTION:
    See the url name of contact view en contact.html
    whose values is loaded in URL_CONTACT
*/

import sendRequest from "./request.js";

const REGEX_PHONE = /^([0-9-()+]{6,19})+$/,
	REGEX_EMAIL = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

const inputName = document.querySelector('#contact input[name="name"]'),
  	inputEmail = document.querySelector('#contact input[name="email"]'),
  	textMessage = document.querySelector('#contact textarea[name="message"]');

	  
function insertMessage(node, message) {
	/* Insert error message in fiels of form */

  	const messageNode = node.parentNode.querySelector("p.msg-field");

  	messageNode.textContent = message;
  	messageNode.classList.add("error");
  	messageNode.classList.remove("d-none");
}

function removeMessage(e) {
	/* Remove error message in fiels of form */

  	const node = e.target,
    	messageNode = node.parentNode.querySelector("p.msg-field");

  	messageNode.classList.remove("error");
  	messageNode.classList.add("d-none");
}

function validateLengthField(field) {
	if (field.value.length > 0) return true;

	insertMessage(field, "Este campo es requerido.");

	return false;
}

function validateName() {
	return validateLengthField(inputName);
}

function validateEmail() {
	const email = inputEmail.value;

	let msg;

	// Validating patterns
	if (REGEX_EMAIL.test(email) || REGEX_PHONE.test(email)) {
		return email;
	}

	if (validateLengthField(inputEmail)) {
		// If is not empty, then it does not check the pattern
		msg = "Ingrese un email o teléfono válido";
		insertMessage(inputEmail, msg);
	}

	return false;
}

function validateMessage() {
	return validateLengthField(textMessage);
}

function validateFields() {
 	
	console.log(validateName());
  	console.log(validateEmail());
  	console.log(validateMessage());

  	if (validateName() && validateEmail() && validateMessage()) {
    	return true;
  	}

  	return false;
}


function successfulResponse() {
	const messageDiv = document.querySelector("#contact div.msg-form"),
    	messageNode = messageDiv.querySelector("p");

	messageDiv.classList.remove("d-none");
	messageNode.innerHTML =` Su mensaje ha sido enviado correctamente 
							<br> Nos contactaremos a la brevedad.`;
	messageNode.classList.add("text-muted");
	messageNode.classList.remove("text-danger");

	// reset inputs
	inputName.value = "";
	inputEmail.value = "";
	textMessage.value = "";
}

function failedResponse() {
	const messageDiv = document.querySelector("#contact div.msg-form"),
    	messageNode = messageDiv.querySelector("p");

	messageDiv.classList.remove("d-none");
	messageNode.innerHTML = `Ha sucedido un error 
							<br> Por favor, espere un momento e intentelo nuevamente.`;
	messageNode.classList.add("text-danger");
	messageNode.classList.remove("text-muted");
}

function sendMessage(e) {
	
	console.log("Send message");

	if (validateFields()) {
		console.log("valid fields");
		sendRequest(successfulResponse, failedResponse);
	} else {
		console.log("not valid fields");
	}
}

document.addEventListener("DOMContentLoaded", e => {
	const btnSend = document.querySelector("#contact button.send");

	btnSend.addEventListener("click", sendMessage);
	inputName.addEventListener("focus", removeMessage);
	inputEmail.addEventListener("focus", removeMessage);
	textMessage.addEventListener("focus", removeMessage);
});
