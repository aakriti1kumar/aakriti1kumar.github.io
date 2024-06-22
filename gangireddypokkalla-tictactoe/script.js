// script.js

document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll('[data-cell]');
    const totalCells = cells.length;
    let revealedCount = 0;

    const images = [
        '1h.png', // Replace with actual paths to your images
        '2r.jpeg',
        '1h.png',
        '2r.jpeg',
        '1h.png',
        '2r.jpeg',
        '1h.png',
        '2r.jpeg',
        '1h.png'
    ];

    cells.forEach((cell, index) => {
        cell.addEventListener('click', () => {
            if (cell.classList.contains('revealed')) return;

            const img = document.createElement('img');
            img.src = images[index];
            cell.appendChild(img);
            cell.classList.add('revealed');
            revealedCount++;

            if (revealedCount === totalCells) {
                showPopup();
            }
        });
    });

    function showPopup() {
        const popup = document.createElement('div');
        popup.id = 'popup';
        popup.innerHTML = `
            <p>Oh no! Looks like this was a hoax... Thank God we still have cake!</p>`;
        document.body.appendChild(popup);
        popup.style.display = 'block';
    }

    window.closePopup = function() {
        const popup = document.getElementById('popup');
        popup.style.display = 'none';
    }
});
