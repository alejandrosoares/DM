import loadCloseMessage from "./messages.js";
import loadNavBar from "./navbar.js";
import { loadChatScript } from "./chat/index.js";

function loadMain() {
   loadCloseMessage();
   loadNavBar();
   loadChatScript();
}


document.addEventListener('DOMContentLoaded', loadMain);