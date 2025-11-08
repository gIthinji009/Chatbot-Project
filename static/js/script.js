async function sendMessage() {
    const input = document.getElementById('input');
    const chatbox = document.getElementById('chatbox');
    const queryText = input.value.trim();
    
    if (!queryText) {
        chatbox.innerHTML += '<p class="error">Please enter a query.</p>';
        return;
    }
    
    // Display user message
    chatbox.innerHTML += `<p><strong>User:</strong> ${queryText}</p>`;
    
    try {
        const response = await fetch('/query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: 1, query_text: queryText })
        });
        const data = await response.json();
        chatbox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
    } catch (error) {
        chatbox.innerHTML += '<p class="error">Error communicating with the server.</p>';
    }
    
    input.value = '';
    chatbox.scrollTop = chatbox.scrollHeight;
}