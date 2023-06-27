const CONTEXT_VARIABLES = loadContextVariables();
const ROLE = {
    USER: 'user',
    ASSISTANT: 'assistant'
}


function loadContextVariables() {
    const divData = document.getElementById('chat-data');
    const enableAutomaticChatBot = divData.querySelector('.enable-automatic-chatbot').value;
    const urlAutomaticChatBot = divData.querySelector('.url-automatic-chatbot').value;
    const urlNewChat = divData.querySelector('.url-new-chat').value;
    const urlGetMessages = divData.querySelector('.url-get-messages').value;
    const token = divData.querySelector('input[name="csrfmiddlewaretoken"]').value;
    
    return {
        enableAutomaticChatBot: (enableAutomaticChatBot === 'True')? true: false,
        urlAutomaticChatBot,
        urlNewChat,
        urlGetMessages,
        token
    }
}


export { CONTEXT_VARIABLES, ROLE };