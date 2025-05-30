const button = document.getElementById('start');

button.addEventListener('click', async () => {
    const amount = document.getElementById("amount");
    const gameMode = document.getElementById("picked_mode");
    if(gameMode != "kanji") {
        data = await request_kana(amount.value, gameMode.value);
        handle_kana_data(data, gameMode.value);
    } else {
        data = await request_kana(amount.value);
    }
})

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
    const kanaDisplay = document.getElementById("kana-character");
    const inputField = document.getElementById("user-input");
    const submitButton = document.getElementById("submit-btn");
    const scoreDisplay = document.getElementById("score-display");

    let currentIndex = 0;
    let correctCount = 0;

    function updateScore() {
        scoreDisplay.textContent = `${correctCount} / ${data.length} correct`;
    }

    function showCharacter() {
        if (currentIndex < data.length) {
            kanaDisplay.textContent = data[currentIndex][game_mode];
            inputField.value = "";
            inputField.focus();
            updateScore();
        } else {
            kanaDisplay.textContent = "🎉 Done!";
            submitButton.disabled = true;
            inputField.disabled = true;
            updateScore();
        }
    }

    function animateResult(isCorrect) {
        kanaDisplay.classList.remove("animate-bounce", "animate-shake");

        if (isCorrect) {
            kanaDisplay.classList.add("animate-bounce");
        } else {
            kanaDisplay.classList.add("animate-shake");
        }

        // Remove class after animation ends so it can re-trigger next time
        setTimeout(() => {
            kanaDisplay.classList.remove("animate-bounce", "animate-shake");
        }, 500);
    }

    submitButton.onclick = () => {
        const userAnswer = inputField.value.trim().toLowerCase();
        const correctAnswer = data[currentIndex].romanji.toLowerCase();

        if (userAnswer === correctAnswer) {
            correctCount++;
            animateResult(true);
            currentIndex++;
            setTimeout(showCharacter, 300);
        } else {
            animateResult(false);
            // Optionally show the correct answer for learning
            // inputField.value = ""; // Let user try again
        }
    };

    inputField.addEventListener("keydown", (e) => {
        if (e.key === "Enter") submitButton.click();
    });

    showCharacter();
}
