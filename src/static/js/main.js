import loadCloseMessage from "./messages.js";
import loadNavBar from "./navbar.js";


function loadMain() {
   loadCloseMessage();
   loadNavBar();
}


document.addEventListener('DOMContentLoaded', loadMain);