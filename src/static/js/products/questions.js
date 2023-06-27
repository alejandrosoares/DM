import { sendSync, buildGetRequest } from '../helpers/request.js';


const questionsDiv = document.querySelector('.product-questions');
const btnShowHideQuestions = document.querySelector('.product-consult button');
const WHATSAPP_URL = 'https://api.whatsapp.com/send?phone=';

let PHONE = null;
let questionsVisible = false;


function showOrHideQuestions(e) {
   if (!questionsVisible) {
      questionsDiv.classList.remove("d-none");
      questionsVisible = true;
   } else {
      questionsDiv.classList.add("d-none");
      questionsVisible = false;
   }
   e.stopPropagation();
}


function getProductCode() {
   const divCode = document.querySelector(".main-product .product-description .code");
   return parseInt(divCode.getAttribute("data-code"));
}


function sendQuestion(message, productCode) {
   const completeMessage = `
      Hello! ${message}
      Code: ${productCode}
      `;
   const encodedMessage = encodeURIComponent(completeMessage);
   window.location.href = `${WHATSAPP_URL}${PHONE}&text=${encodedMessage}`;
}


async function loadQuestions() {
   const productQuestions = await getQuestions();
   writeQuestionsInHtml(productQuestions.questions);
   setPhoneNumber(productQuestions.phone);
   btnShowHideQuestions.onclick = e => showOrHideQuestions(e);
}


async function getQuestions() {
   const divQuestionsData = document.getElementById('questions-data');
	const url = divQuestionsData.querySelector('input.url').value;
   const req = buildGetRequest();
   const res = await sendSync(req, url);
   const questions = res.obj;
   return questions;
}


function setPhoneNumber(phone) {
   PHONE = phone;
}


function writeQuestionsInHtml(questions) {
   const ulContainer = document.querySelector('.product-questions > ul');
   questions.forEach(question => {  
      const li = document.createElement('li');
      li.setAttribute('data-id', question.pk);
      li.innerText = question.fields.content;
      li.onclick = e => makeQuestion(e);
      ulContainer.appendChild(li);
   });
}


function makeQuestion(e) {
   const message = e.target.innerText;
   const productCode = getProductCode();
   sendQuestion(message, productCode);
}


loadQuestions();