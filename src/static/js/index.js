import loadCloseMessage from "./messages.js";
import loadNavBar from "./navbar.js";
import { loadChatScript } from "./chat/index.js";
import loadServiceWorkers from "./service-workers/index.js";


(function () {
   console.log('main');
   loadCloseMessage();
   loadNavBar();
   loadChatScript();
   loadServiceWorkers();
}())

