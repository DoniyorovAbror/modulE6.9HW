
const recordBtn = document.querySelector('form');

const user = document.getElementById('user_id')

recordBtn.addEventListener('submit', (e) => {
    e.preventDefault();
    // let text = document.querySelector('input')
    let form = new FormData(recordBtn)
    form.set('id', form.get('id'));
    form.set('author', user.textContent);
    const redirect_url = 'http://127.0.0.1:8000/chat_room/'
    
    const response = fetch('http://127.0.0.1:8000/api/v1/rooms/', {
        method: 'POST',
        body: form,
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
        window.location.href = redirect_url + data.id
    }).catch(err => {
        console.log(err);
    })
})

