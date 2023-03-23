const room_id = document.getElementById('room_id');

const redirect_url = 'http://127.0.0.1:8000/chat_rooms/';
const api_url = `http://127.0.0.1:8000/api/v1/rooms/${room_id.textContent}/`;
const del_btn = document.getElementById('delete_room');
let request_data;
const input_room_name = document.getElementById('id_name');

window.onload = async () => {
   await fetch(api_url, {

}).then(async (response) => {
    return await response.json();
}).then((data) => {
    console.log(data);
    request_data = data;
    input_room_name.value = data.name;
})};

const btn = document.getElementById('edit_room');

btn.addEventListener('click', async (e) => {
    e.preventDefault();
    let params;
    params = {
        'id': request_data.id,
        'name': input_room_name.value,
        'author': request_data.author,
    };
    await fetch(api_url, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(params),
    }).then(async (response) => {
        return await response.json();
    }).then((data) => {
        console.log(data);
        window.location.href = redirect_url;
    }).catch((err) => {
        console.log(err);
    });
});



del_btn.addEventListener('click', (e) => {
    e.preventDefault();
    fetch(api_url, {
        method: 'DELETE',
    }).then( (response) => {
        response.json()
    }).then((data) => {
        console.log(data);
        window.location.href = redirect_url;
    }).catch((err) => {
        console.log(err);
    });
});