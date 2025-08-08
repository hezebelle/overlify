const chatBox = document.getElementById('chat-box');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

function appendMessage(content, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${sender}`;
    msgDiv.textContent = content;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

chatForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    const question = userInput.value.trim();
    if (!question) return;
    appendMessage(question, 'user');
    userInput.value = '';
    appendMessage('[Thinking in unnecessarily complex algorithms…]', 'bot');

    // Call backend API
    try {
    const res = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: question })
        });
        const data = await res.json();
        // Remove thinking message
        chatBox.lastChild.remove();
        appendMessage(data.reply, 'bot');
    } catch (err) {
        chatBox.lastChild.remove();
        appendMessage('Error: Could not reach Overexplainer Bot.', 'bot');
    }
});
