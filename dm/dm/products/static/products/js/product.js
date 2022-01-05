const questionsContainer = document.querySelector(
  ".product .product-questions"
);

let questionVisibility = false;

const consult = {
  clickConsultBtn: 0,
  refs: [
    {
      numberQuestion: 1,
      message: "¿Tenés disponible?",
    },
    {
      numberQuestion: 2,
      message: "¿Me podés enviar?",
    },
    {
      numberQuestion: 3,
      message: "Otra pregunta",
    },
  ],
};

function consultProduct() {
  if (!questionVisibility) {
    questionsContainer.classList.remove("d-none");
    questionVisibility = true;
  } else {
    questionsContainer.classList.add("d-none");
    questionVisibility = false;
  }
}

function getProductCode() {
  const divCode = document.querySelector(".product .product-description .code");

  return parseInt(divCode.getAttribute("data-code"));
}

function queryFromQuestion(e) {
    const messageNumber = parseInt(
        e.target.getAttribute("data-question")
    ),
    productCode = getProductCode();
    
    sendConsult(messageNumber, productCode);
}

function getQuestionMessage(messageNumber) {
  const listMessages = consult.refs;
  let message = null;

  for (const m of listMessages) {
    if (m.numberQuestion === messageNumber) {
      message = m.message;
    }
  }

  return message;
}

function sendConsult(messageNumber, productCode) {
  const questionMessage = getQuestionMessage(messageNumber);

  switch (messageNumber) {
    case 0:
      message = `
                Hola! ${questionMessage}
                Producto: ${productCode}
                `;
      alert(message);
      break;
    case 1:
        message = `
            Hola! ${questionMessage}
            Producto: ${productCode}
        `;
        alert(message);
      break;
    case 2:
        message = `
            Hola! ${questionMessage}
            Producto: ${productCode}
        `;
        alert(message);
      break;
    case 3:
        message = `
            Hola!
            Producto: ${productCode}
        `;
        alert(message);
      break;
    default:
        message = `
            Hola!
            Producto: ${productCode}
        `;
        alert(message);
        break;
  }
  message = encodeURIComponent(message);
  window.location.href = `
    https://api.whatsapp.com/send?phone=+543755445423&text=${message}
  `;
}

function consultProductFunctions() {
  const btnConsult = document.querySelector(".product .product-consult button"),
    questions = document.querySelectorAll(".product .product-questions li");

  btnConsult.addEventListener("click", consultProduct);
  questions.forEach((li) => li.addEventListener("click", queryFromQuestion));
}
document.addEventListener("DOMContentLoaded", (e) => {
  consultProductFunctions();
});
