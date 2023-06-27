import { loadQuestions } from "./questions.js";


function loadProduct() {
   loadQuestions();
}


document.addEventListener("DOMContentLoaded", loadProduct);