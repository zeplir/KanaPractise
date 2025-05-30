function request_kana() {
    const url = "http://127.0.0.1:5000/kana";
    const headers = { "Content-Type": "application/json" };
    const body = JSON.stringify({
        "amount": "10",
        "kana_type": "hiragana",
    });
    fetch(url, {
        method: "POST",
        headers: headers,
        body: body
    })
        .then(response => response.json())
        .then(data => console.log("Success:", data))
        .catch(error => console.error("Error: ", error));
}

const button = document.getElementById('sendBtn');

button.addEventListener('click', () => {
    request_kana()
})
