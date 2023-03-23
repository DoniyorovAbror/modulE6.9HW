const submitBtn = document.getElementById('submit_btn');

const onClick = () => {
    const formHtml = new FormData(document.querySelector('form'));

    // for (const [key, value] of formHtml) {
    //     console.log(`${key}: ${value}`);
    // };
     console.log(formHtml)
    const response = fetch('127.0.0.1:8000/auth/users/', {method: 'POST', body: formHtml, headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
            .then(async response => {return await response.json()})
            .then(data => {console.log(data)})
    }

submitBtn.addEventListener('click', onClick);

