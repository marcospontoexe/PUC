const messagesContainer = document.getElementById('chatMessages');
const chatForm = document.getElementById('chatForm');
const messageInput = document.getElementById('messageInput');
const btnSend = document.getElementById('btnSend');
const btnReset = document.getElementById('btnReset');
const quickActions = document.getElementById('quickActions');

const sessionId = crypto.randomUUID ? crypto.randomUUID() : Date.now().toString();
let isIdentified = false;

function getCurrentTime() {
    return new Date().toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
}

function formatMessage(text) {
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    text = text.replace(/`(.*?)`/g, '<code>$1</code>');
    return text;
}

function addMessage(content, isUser = false) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.innerHTML = formatMessage(content);

    const timeSpan = document.createElement('span');
    timeSpan.className = 'message-time';
    timeSpan.textContent = getCurrentTime();

    msgDiv.appendChild(contentDiv);
    msgDiv.appendChild(timeSpan);
    messagesContainer.appendChild(msgDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function showTyping() {
    const typing = document.createElement('div');
    typing.className = 'typing-indicator';
    typing.id = 'typingIndicator';
    typing.innerHTML = '<span></span><span></span><span></span>';
    messagesContainer.appendChild(typing);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function removeTyping() {
    const typing = document.getElementById('typingIndicator');
    if (typing) typing.remove();
}

async function sendMessage(text) {
    if (!text.trim()) return;

    addMessage(text, true);
    messageInput.value = '';
    btnSend.disabled = true;
    showTyping();

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text, session_id: sessionId }),
        });

        const data = await response.json();
        removeTyping();

        const delay = Math.min(500 + data.response.length * 3, 1500);
        await new Promise(resolve => setTimeout(resolve, delay));

        addMessage(data.response);

        if (data.identified && !isIdentified) {
            isIdentified = true;
            quickActions.style.display = 'flex';
        }

        if (data.state === 'INICIO' && isIdentified) {
            isIdentified = false;
            quickActions.style.display = 'none';
        }
    } catch (err) {
        removeTyping();
        addMessage('Desculpe, ocorreu um erro de conexão. Tente novamente em alguns instantes.');
    }

    btnSend.disabled = false;
    messageInput.focus();
}

chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    sendMessage(messageInput.value);
});

btnReset.addEventListener('click', async () => {
    try {
        await fetch('/api/reset', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ session_id: sessionId }),
        });
    } catch (_) {}

    messagesContainer.innerHTML = '';
    isIdentified = false;
    quickActions.style.display = 'none';
    addMessage(
        'Conversa reiniciada! 👋\n\n' +
        'Olá! Bem-vindo à **TeleConecta Brasil**!\n' +
        'Sou o **AtendeBot**, seu assistente virtual.\n\n' +
        'Para começar, por favor me informe seu **CPF**.\n\n' +
        '💡 CPFs de teste: 123.456.789-01 | 987.654.321-00 | 111.222.333-44'
    );
});

document.querySelectorAll('.quick-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        sendMessage(btn.dataset.message);
    });
});

const firstTimeEl = document.querySelector('.message-time');
if (firstTimeEl) firstTimeEl.textContent = getCurrentTime();
