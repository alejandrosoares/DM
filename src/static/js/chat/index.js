import { CONTEXT_VARIABLES as CONTEXT, ROLE } from './constants.js';
import { sendSync, buildPostRequest, buildGetRequest } from '../helpers/request.js';


class Chat {
    constructor(sendMessageCb) {
        this._sendFn = sendMessageCb;
        this.showing = false;
        this.chatId = null;
        this.role = ROLE.USER;
        this.elements = {
            chatDiv: document.getElementById('chat'),
            chatBox: document.getElementById('chat-box'),
            messagesDiv: document.querySelector('#chat-box > div'),
            input: document.getElementById('chat-input'),
            sendBtn: document.getElementById('chat-send'),
            showBtn: document.getElementById('show-chat'),
            closeBtn: document.getElementById('close-chat')
        }

        this._loadChat();
    }
    
    _loadChat = async function() {
        this.chatId = await this._getChatId();
        await this._loadPreviousMessages();
        this._loadEvents();
    }
    
    _send = function(sendCb) {
        const data = this._getData();
        sendCb(data);
        this._resetInput();
    }

    _show = function(show = true) {
        if(show && !this.showingChat) {
            this.elements.chatDiv.classList.remove('d-none');
            this.showingChat = true;
            this._updateScroll();
        } else {
            this.elements.chatDiv.classList.add('d-none');
            this.showingChat = false;
        }
    }

    _typing = function(e) {
        const enterCode = 13;
        if (e.keyCode === enterCode) {
            this.elements.sendBtn.click();
        }
    }

    writeMessage = function(content, role) {
        const isAssistant = role == ROLE.ASSISTANT;
        const divMessage = this._createDivMessage(isAssistant);
        const html = `
            <div class="col-8 message ${role}">
                <p>${content}</p>
            </div>`
            ;
        divMessage.innerHTML = html;
        this.elements.messagesDiv.appendChild(divMessage);
        this._updateScroll();
    }

    _createDivMessage = function(addAssistantStyle = false) {
        const divMessage = document.createElement('div');
        divMessage.classList.add('row');
        divMessage.classList.add(addAssistantStyle? 'to-left': 'to-right');
        return divMessage;
    }

    _getData = function() {
        return {
            role: this.role,
            content: this.elements.input.value,
            chatId: this.chatId
        }
    }

    _resetInput = function() {
        this.elements.input.value = '';
    }

    _getChatId = async function() {
        let chatId = localStorage.getItem('chatId');
        if (!chatId) {
            chatId = await this._getNewChatId();
            localStorage.setItem('chatId', chatId);
        }
        return chatId;
    }

    _getNewChatId = async function() {
        const url = CONTEXT.urlNewChat;
        const req = buildPostRequest();
        const res = await sendSync(req, url);
        return res.obj.id;
    }

    _loadEvents = function() {
        this.elements.input.onkeyup = e => this._typing(e);
        this.elements.showBtn.onclick = e => this._show(true);
        this.elements.closeBtn.onclick = e => this._show(false);
        this.elements.sendBtn.onclick = e => this._send(this._sendFn);
    }

    _loadPreviousMessages = async function() {
        const messages = await this._getPreviousMessages();
        messages.forEach(msg => {
            const content = msg.fields.content;
            const role = msg.fields.created_by;
            this.writeMessage(content, role);
        });
    }

    _getPreviousMessages = async function() {
        const req = buildGetRequest();
        const url = `${CONTEXT.urlGetMessages}?chatId=${this.chatId}`;
        const res = await sendSync(req, url);
        return res.obj;
    }

    _updateScroll = function() {
        const height = this.elements.messagesDiv.scrollHeight;
        this.elements.chatBox.scrollTo({
                top: height,
                left: 0,
                behavior: "smooth",
            });
    } 
}


function loadChatScript() {
    const script = document.createElement('script');

    if (CONTEXT.enableAutomaticChatBot) {
        script.setAttribute("src", `/static/js/chat/automaticChat.js`);
    } else {
        script.setAttribute("src", `/static/js/chat/realTimeChat.js`);
    }

    script.setAttribute("type", "module");
    document.body.appendChild(script);
}


export {
    Chat,
    loadChatScript,
}

