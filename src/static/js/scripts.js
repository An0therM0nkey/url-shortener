document.getElementById('add_form').addEventListener('submit', submitForm);

function submitForm(e) {
    e.preventDefault();

    let formData = new FormData(e.target);

    let obj = {};
    formData.forEach((value, key) => obj[key] = value);

    let request = new Request(e.target.action, {
        method: 'POST',
        body: JSON.stringify(obj),
        headers: {
            'Content-Type': 'application/json',
        },
    });

    fetch(request)
        .then((resp) => {
            if (resp.status == 400)
                return resp.json()
            location.reload()
        })
        .then((json) => alert(json.message))
}


let del_forms = document.getElementsByClassName('js-delete-form');

for (let df of del_forms)
    df.addEventListener('submit', deleteForm);

function deleteForm(e) {
    e.preventDefault();

    let formData = new FormData(e.target);

    let obj = {};
    formData.forEach((value, key) => obj[key] = value);

    let request = new Request(e.target.action, {
        method: 'DELETE',
    });

    fetch(request).then(
        function(response) {
            location.reload()
        },
        function(error) {
            console.error(error);
        }
    );
}