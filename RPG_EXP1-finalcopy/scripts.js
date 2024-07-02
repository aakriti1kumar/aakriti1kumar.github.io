const starterMessage = "I got laid off from my job today...";
let turnCount = 0;
const maxTurns = 6;

document.addEventListener("DOMContentLoaded", () => {
    displayMessage(`Friend: ${starterMessage}`, 'llm');

    const sendButton = document.getElementById('send-button');
    sendButton.addEventListener('click', sendMessage);

    const chatForm = document.getElementById('chat-form');
    chatForm.addEventListener('submit', function(event) {
        event.preventDefault();
    });

    document.getElementById('user-input').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendMessage(event);
        }
    });
});

async function sendMessage(event) {
    if (event) event.preventDefault();  

    const userInput = document.getElementById('user-input');
    if (!userInput) {
        console.error("User input element not found");
        return;
    }

    const message = userInput.value.trim();

    if (message) {
        // Display user's message
        displayMessage(`You: ${message}`, 'user');

        // Increment turn count
        turnCount++;
        

        // Get LLM response
        const response = await getLLMResponse(message);
        displayMessage(`Friend: ${response.rolePlayerResponse}`, 'llm');
        
        // Increment turn count for LLM response
        turnCount++;

        if (turnCount >= maxTurns) {
            endConversation();
            return;
        }

        // Clear the input field
        userInput.value = '';
        
        if (turnCount >= maxTurns) {
            endConversation();
        }
    }
}

function displayMessage(message, sender) {
    const chatMessages = document.getElementById('chat-messages');
    if (!chatMessages) {
        console.error("Chat messages element not found");
        return;
    }

    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = message;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function getLLMResponse(userMessage) {
    try {
        const response = await fetch('http://127.0.0.1:5000/get_llm_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userMessage }),
            credentials: 'include'  
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        return {
            rolePlayerResponse: data.response,
        };
    } catch (error) {
        console.error('Error fetching LLM response:', error);
        return {
            rolePlayerResponse: 'Sorry, there was an error processing your request.',
        };
    }
}

function endConversation() {
    alert("Thank you for trying to make your friend feel better! Please fill out the exit survey.");
    window.location.href = '../templates/exitsurvey.html';
}
