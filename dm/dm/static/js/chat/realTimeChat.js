import Chat from "./chat.js";


let chat = new Chat(sendMessage);
let chatSocket = loadSocketConnection();


chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const content = data.message.content;
    const role = data.message.role;
    chat.writeMessage(content, role);
};


chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};


function sendMessage(data) {
    chatSocket.send(JSON.stringify(data));
}


function loadSocketConnection() {
    const chatId = chat.chatId;
    const urlChat = `ws://${window.location.host}/ws/chat/${chatId}/`;
    return new WebSocket(urlChat);
}

