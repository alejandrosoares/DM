import { send, buildPostRequest } from '../helpers/request.js';
import { Chat } from './index.js';
import { CONTEXT_VARIABLES as CONTEXT, ROLE } from './constants.js';


let chat = new Chat(sendMessage);


function success(response) {
    const content = response.obj.content;
    const user = ROLE.ASSISTANT;
    chat.writeMessage(content, user);
}


function failed(error) {
    console.error(error);
}


function sendMessage(data) {
    const url = CONTEXT.urlAutomaticChatBot;
    const token = CONTEXT.token;
    const request = buildPostRequest(data, token);
    send(request, url, success, failed);
    writeMessage(data);
}


function writeMessage(data) {
    const content = data.content;
    const role = data.role;
    chat.writeMessage(content, role);
}


chat = new Chat(sendMessage);



