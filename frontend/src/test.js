// Fetches data for either katakana or kanji
async function request_kana(amount, kana_type) {
    const url = "http://127.0.0.1:5000/kana";
    const headers = { "Content-Type": "application/json" };
    const body = JSON.stringify({
        "amount": amount,
        "kana_type": kana_type,
    });

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: headers,
            body: body
        });
        const data = await response.json();
        console.log("Success:", data);
        return data;
    } catch (error) {
        console.error("Error:", error);
    }
}

// Works like request_kana, but seperated for debugging and
// readablitys sake
async function request_kanji(amount) {
    const url = "http://127.0.0.1:5000/kanji";
    const headers = { "Content-Type": "application/json" };
    const body = JSON.stringify({"amount": amount});

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: headers,
            body: body
        });
        const data = await response.json();
        console.log("Success:", data);
        return data;
    } catch (error) {
        console.error("Error:", error);
    }
}

function handle_kana_data(data, game_mode) {
    const test = document.getElementById("test");
    test.innerHTML = data[0][game_mode]
}

const button = document.getElementById('start');

button.addEventListener('click', async () => {
    const amount = document.getElementById("amount");
    const game_mode = document.getElementById("picked_mode");
    if(game_mode != "kanji") {
        data = await request_kana(amount.value, game_mode.value);
        handle_kana_data(data, game_mode.value);
    } else {
        data = await request_kana(amount.value);
    }
})
