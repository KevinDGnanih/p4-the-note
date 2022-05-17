const likes = document.getElementById('likedata');

document.getElementById("likedata").addEventListener("submit", (e) => {
    e.preventDefault();

    fetch("{% url 'post_like' post.slug %}", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(likes),
    })
    .then(response => response.json())
    .then(likes => {
        console.log('Success:', likes);
    })
    .catch(error => {
        console.error('Error:', error)
    });
})