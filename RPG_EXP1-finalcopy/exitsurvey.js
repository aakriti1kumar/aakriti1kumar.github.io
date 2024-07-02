document.addEventListener("DOMContentLoaded", () => {
    const endButton = document.getElementById('end-button');
    endButton.addEventListener('click', async (event) => {
        event.preventDefault();

        const empathyRating = document.querySelector('input[name="empathy"]:checked').value;
        const feedback = document.getElementById('feedback').value.trim();

        const response = await submitSurvey({ empathy_rating: empathyRating, feedback: feedback });

        if (response.message === "Survey response saved successfully") {
            // Redirect to the exit page
            window.location.href = '/templates/exit.html';
        } else {
            alert("There was an issue submitting your survey response. Please try again.");
        }
    });
});

async function submitSurvey(surveyData) {
    try {
        const response = await fetch('http://127.0.0.1:5000/submit_survey', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(surveyData),
            credentials: 'include'
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error submitting survey response:', error);
        return { message: 'Error submitting survey response' };
    }
}
