function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');

    if (userInput.trim() === "") return;

    // Menampilkan pesan pengguna di kotak obrolan
    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user-message');
    userMessage.textContent = "USER: " + userInput;
    chatBox.appendChild(userMessage);

    // Mengirim pesan ke server
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Menampilkan respons bot di kotak obrolan
        const botMessage = document.createElement('div');
        botMessage.classList.add('message', 'bot-message');
        //botMessage.textContent = "Bot: " + data.response;
        if (data.response.startsWith('<table')) {
            botMessage.innerHTML = data.response; // Respons berupa tabel menu
        } else {
            botMessage.textContent = "Bot: " + data.response; // Respons biasa
        }
        chatBox.appendChild(botMessage);

        // Menghapus input pengguna
        document.getElementById('user-input').value = "";
        
        // Scroll ke bawah untuk melihat pesan terbaru
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error('Error:', error));
}
