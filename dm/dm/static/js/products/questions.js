/* 
   FUNCTIONS FOR SEND QUESTIONS TO SELLER
*/
const questionsContainer = document.querySelector(
   ".main-product .product-questions"
);

let questionVisibility = false;

const listMessages = [{
   numQuestion: 1,
   message: "¿Tenés disponible?",
},
{
   numQuestion: 2,
   message: "¿Me podés enviar?",
},
{
   numQuestion: 3,
   message: "Otra pregunta",
},
];

function showOrHideQuestions(e) {
   /* Show or Hide questionsContainer 
   Trigger when press in  consult button
   */
   if (!questionVisibility) {
      questionsContainer.classList.remove("d-none");
      questionVisibility = true;
   } else {
      questionsContainer.classList.add("d-none");
      questionVisibility = false;
   }

   e.stopPropagation();
}

function getProductCode() {
   /* Get product Code 
   @return: int
   */
   const divCode = document.querySelector(".main-product .product-description .code");
   return parseInt(divCode.getAttribute("data-code"));
}

function getQuestionMessage(messageNumber) {
   /* Get message from listMessage based in the message number */

   let message = null;

   for (const m of listMessages) {
      if (m.numQuestion === messageNumber) {
         message = m.message;
         break;
      }
   }

   return message;
}

function sendQuestion(messageNumber, productCode) {
   /* Send question to seller, set the message to send */

   const questionMessage = getQuestionMessage(messageNumber);
   let message;

   switch (messageNumber) {
      case 1:
         message = `Hola! ${questionMessage}
        
         Producto: ${productCode}`;
         break;
      case 2:
         message = `Hola! ${questionMessage}
        
         Producto: ${productCode}`;
         break;
      case 3:
         message = `Hola!
        
         Producto: ${productCode}`;
         break;
      default:
         message = `Hola!
        
         Producto: ${productCode}`;
         break;
   };
   message = encodeURIComponent(message);
   window.location.href = `
      https://api.whatsapp.com/send?phone=+5493755438460&text=${message}
  `;
}

function performQuestion(e) {
   /* Set the message number and product code */

   const messageNumber = parseInt(
      e.target.getAttribute("data-question")
   ),
      productCode = getProductCode();

   sendQuestion(messageNumber, productCode);
}

function loadQuestions() {
   /* Load events related to questions */

   const btnConsult = document.querySelector(".main-product .product-consult button"),
      questions = document.querySelectorAll(".main-product .product-questions li");

   btnConsult.addEventListener("click", showOrHideQuestions);

   questions.forEach(li => {
      li.addEventListener("click", performQuestion)
   });

   document.addEventListener("click", e => {
      if (!e.target.matches('.main-product .product-consult button *')) {
         if (questionVisibility) {
            document.querySelector(".main-product .product-consult button").click();
         }
      }
   });
}


export default loadQuestions;