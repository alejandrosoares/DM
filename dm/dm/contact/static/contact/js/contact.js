/*
    Functions of contact form
    See the url name of contact view en contact.html
    whose values is loaded in URL_CONTACT
*/
const REGEX_PHONE = /^([0-9-()+]{6,19})+$/,
  REGEX_EMAIL =
    /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

const inputName = document.querySelector('#contact input[name="name"]'),
  inputEmail = document.querySelector('#contact input[name="email"]'),
  textMessage = document.querySelector('#contact textarea[name="message"]'),
  URL_CONTACT = document.querySelector("#contact input.url-contact").value;

function insertMessage(node, message) {
  const messageNode = node.parentNode.querySelector("p.msg-field");

  messageNode.textContent = message;
  messageNode.classList.add("error");
  messageNode.classList.remove("d-none");
}
function removeMessage(e) {
  const node = e.target,
    messageNode = node.parentNode.querySelector("p.msg-field");

  messageNode.classList.remove("error");
  messageNode.classList.add("d-none");
}
function validateName() {
  if (inputName.value.length > 0) return true;

  const msg = "Este campo es requerido";

  insertMessage(inputName, msg);

  return false;
}
function validateEmail() {
  const email = inputEmail.value;

  let msg;

  // No valid pattern
  if (REGEX_EMAIL.test(email) || REGEX_PHONE.test(email)) {
    return email;
  }

  // Empty Field
  if (email.length === 0) {
    msg = "Este campo es requerido";
  } else {
    msg = "Ingrese un email o teléfono válido";
  }

  insertMessage(inputEmail, msg);
  return false;
}
function validateMessage() {
  if (textMessage.value.length > 0) return true;

  const msg = "Este campo es requerido";

  insertMessage(textMessage, msg);

  return false;
}
function validateFields() {
  validateName();
  validateEmail();
  validateMessage();

  if (validateName() && validateEmail() && validateMessage()) {
    return true;
  }
  return false;
}
function buildRequest() {
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
    body: JSON.stringify(data),
  };

  return request;
}
function sendMessage() {
  const messageDiv = document.querySelector("#contact div.msg-form"),
    messageNode = messageDiv.querySelector("p");

  const successfulResponse = () => {
    messageDiv.classList.remove("d-none");
    messageNode.innerHTML =
      "Su mensaje ha sido enviado correctamente <br> Nos contactaremos a la brevedad.";
    messageNode.classList.add("text-success");
    messageNode.classList.remove("text-danger");

    // reset inputs
    inputName.value = "";
    inputEmail.value = "";
    textMessage.value = "";
  };
  const failedResponse = () => {
    messageDiv.classList.remove("d-none");
    messageNode.innerHTML =
      "Ha sucedido un error <br> Por favor, espere un momento e intentelo nuevamente.";
    messageNode.classList.add("text-danger");
    messageNode.classList.remove("text-success");
  };
  if (validateFields()) {
    fetch(URL_CONTACT, buildRequest())
      .then((response) => {
        if (response.ok) return response.json();
      })
      .then((object) => {
        if (object.status === "ok") {
          successfulResponse();
        } else {
          failedResponse();
        }
      })
      .catch((error) => failedResponse());
  }
}

document.addEventListener("DOMContentLoaded", (e) => {
  const btnSend = document.querySelector("#contact button.send");

  btnSend.addEventListener("click", sendMessage);

  inputName.addEventListener("focus", removeMessage);
  inputEmail.addEventListener("focus", removeMessage);
  textMessage.addEventListener("focus", removeMessage);
});
