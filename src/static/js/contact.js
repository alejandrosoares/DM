import { send, buildPostRequest } from "./helpers/request.js";


const REGEX_EMAIL = /^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$/;
const REGEX_PHONE = /^\+?\d{9,16}$/;
const btnSend = document.querySelector("#contact .contact-form button.send");
const inputName = document.querySelector('#contact input[name="name"]');
const inputEmail = document.querySelector('#contact input[name="email"]');
const textMessage = document.querySelector('#contact textarea[name="message"]');


function showFieldErrorMessageOf(node) {
	const messageNode = node.parentNode.querySelector("p.msg-field");
	messageNode.classList.add("error");
	messageNode.classList.remove("d-none");
}


function removeErrorStyleOfField(e) {
	const node = e.target;
	const messageNode = node.parentNode.querySelector("p.msg-field");
	messageNode.classList.remove("error");
	messageNode.classList.add("d-none");
}


function validateLengthField(field, minLength = 0) {
	return (field.value.length > minLength);
}


function validateName() {
	const isValid = validateLengthField(inputName);
	if (!isValid) {
		showFieldErrorMessageOf(inputName);
	} 
	return isValid;
}


function validateEmail() {
	const isEmail = REGEX_EMAIL.test(inputEmail.value);
	const isPhone = REGEX_PHONE.test(inputEmail.value);
	const isValid = (isEmail || isPhone);
	if (!isValid) {
		showFieldErrorMessageOf(inputEmail);
	}
	return isValid;
}


function validateTextMessage() {
	const isValid = validateLengthField(textMessage);
	if (!isValid) {
		showFieldErrorMessageOf(textMessage);
	}
	return isValid;
}


function validateFields() {
	return validateName() && validateEmail() && validateTextMessage();
}


function resetFormFields() {
	inputName.value = "";
	inputEmail.value = "";
	textMessage.value = "";
}


function showFormMessage(successStyle = true) {
	const messageDiv = document.querySelector("#contact div.msg-form");
	const messageSuccess = messageDiv.querySelector("p.success");
	const messageFail = messageDiv.querySelector("p.fail");

	if (successStyle) {
		messageSuccess.classList.remove("d-none");
		messageFail.classList.add("d-none");
	} else {
		messageSuccess.classList.add("d-none");
		messageFail.classList.remove("d-none");
	}

	messageDiv.classList.remove("d-none");
}


function successfulResponse() {
	const successStatus = true;
	showFormMessage(successStatus);
	resetFormFields();
}


function failedResponse() {
	const successStatus = false;
	showFormMessage(successStatus);
}

function buildFormData() {
	return {
		name: inputName.value,
		email: inputEmail.value,
		message: textMessage.value,
	}
}

function sendContactMessage() {
	if (validateFields()) {
		const data = buildFormData();
		const { url, token } = getContactUrlAndToken();
		const request = buildPostRequest(data, token);
		send(request, url, successfulResponse, failedResponse);
	} else {
		console.warn("Not valid fields in contact form");
	}
}

function getContactUrlAndToken() {
	const divContactData = document.getElementById('contact-data');
	const url = divContactData.querySelector('input.url').value;
	const token = divContactData.querySelector('input[name="csrfmiddlewaretoken"]').value;
	return {
		url,
		token
	}
}


function loadContact() {
	btnSend.addEventListener("click", sendContactMessage);
	inputName.addEventListener("focus", removeErrorStyleOfField);
	inputEmail.addEventListener("focus", removeErrorStyleOfField);
	textMessage.addEventListener("focus", removeErrorStyleOfField);
}


document.addEventListener("DOMContentLoaded", loadContact);
