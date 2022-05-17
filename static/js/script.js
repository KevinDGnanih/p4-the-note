
const heartBtn = document.getElementByClassName("btn-like");

function likeBtn() {
    fetch('BASE_URL', {
        
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(heartBtn),
        })
        .then(response => response.json())
        .then(heartBtn => {
            console.log('Success:', heartBtn);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}
