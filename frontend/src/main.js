const button = document.getElementById('start');
const clueBtn = document.getElementById("clue-btn");
const clueText = document.getElementById("clue-text");
const clueWrapper = document.getElementById("clue-wrapper");
const choseChar = document.getElementById("chose-char");
const choseNum = document.getElementById("chose-num");

button.addEventListener('click', async () => {
    const amount = document.getElementById("amount");
    const gameMode = document.getElementById("picked_mode");
    const mode = gameMode.value.toLowerCase();

    let data = await request(amount.value, mode);
    toggleSettingsData([amount, gameMode, choseChar, choseNum, button], true);

    if (mode !== "kanji") {
        handle_kana_data(data, mode);
    } else {
        const clueBox = document.getElementById("clue-wrapper");
        clueBox.classList.remove("hidden");
        handle_kanji_data(data, mode);
    }
});

// Fetches data for either katakana or kanji
async function request(amount, kana_type) {
    const url = "http://127.0.0.1:5000/" + kana_type;
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

function reset_clue() {
    clueBtn.classList.remove("translate-x-[-4px]");
    clueText.classList.remove("opacity-100", "scale-100");
    clueText.classList.add("hidden", "opacity-0", "scale-95", "pointer-events-none");
    clueText.textContent = "";
}

function handle_kana_data(data, gameMode) {
    const kanaDisplay = document.getElementById("kana-character");
    const inputField = document.getElementById("user-input");
    const submitButton = document.getElementById("submit-btn");
    const scoreDisplay = document.getElementById("score-display");

    let currentIndex = 0;
    let correctCount = 0;

    submitButton.onclick = () => {
        const userAnswer = inputField.value.trim().toLowerCase();
        const correctAnswer = data[currentIndex].romanji.toLowerCase();
        const isCorrect = userAnswer === correctAnswer;

        if (isCorrect) {
            correctCount++;
            currentIndex++;
            reset_clue();
            setTimeout(() => {
                showCharacter(data, currentIndex, kanaDisplay, inputField, submitButton, gameMode);
            }, 300);
            updateScore(scoreDisplay, correctCount, data);
        }
        animateResult(isCorrect, kanaDisplay);
    };

    inputField.addEventListener("keydown", (e) => {
        if (e.key === "Enter") submitButton.click();
    });

    showCharacter(data, currentIndex, kanaDisplay, inputField, submitButton, gameMode);
}

function handle_kanji_data(data, gameMode) {
    const kanaDisplay = document.getElementById("kana-character");
    const inputField = document.getElementById("user-input");
    const submitButton = document.getElementById("submit-btn");
    const scoreDisplay = document.getElementById("score-display");

    let currentIndex = 0;
    let correctCount = 0;

    clueBtn.addEventListener("click", () => {
    clueBtn.classList.add("translate-x-[-4px]");
    clueText.textContent = `Pronunciation: ${data[currentIndex]["kun-readings"]}`;
    clueText.classList.remove("hidden", "opacity-0", "scale-95", "pointer-events-none");
    clueText.classList.add("opacity-100", "scale-100");
    });

    submitButton.onclick = () => {
        const userAnswer = inputField.value.trim().toLowerCase();
        let isCorrect = false;

        // Here we loop through the meaning kanji has, since one
        // kanji can have mulitple meanings and we want to accept all
        data[currentIndex].meaning.forEach((ans) => {
            if(ans === userAnswer) {
                isCorrect = true;
            }
        });

        if (isCorrect) {
            correctCount++;
            currentIndex++;
            setTimeout(() => {
                showCharacter(data, currentIndex, kanaDisplay, inputField, submitButton, gameMode);
            }, 300);
            updateScore(scoreDisplay, correctCount, data);
            reset_clue();
        }
        animateResult(isCorrect, kanaDisplay)
    };

    inputField.addEventListener("keydown", (e) => {
        if (e.key === "Enter") submitButton.click();
    });
    showCharacter(data, currentIndex, kanaDisplay, inputField, submitButton, gameMode);
}

function showCharacter(data, currentIndex, kanaDisplay, inputField, submitButton, gameMode) {
    if (currentIndex < data.length) {
        kanaDisplay.textContent = data[currentIndex][gameMode];
        inputField.value = "";
        inputField.focus();
    } else {
        kanaDisplay.textContent = "Done! 🎉";
        submitButton.disabled = true;
        inputField.disabled = true;
        toggleSettingsData([amount, gameMode, choseChar, choseNum, button], false);
    }
}

function updateScore(scoreDisplay, correctCount, data) {
    scoreDisplay.textContent = `${correctCount} / ${data.length} correct`;
}

function animateResult(isCorrect, kanaDisplay) {
    kanaDisplay.classList.remove("animate-bounce", "animate-shake");

    if (isCorrect) {
        kanaDisplay.classList.add("animate-bounce");
    } else {
        kanaDisplay.classList.add("animate-shake");
    }

    setTimeout(() => {
        kanaDisplay.classList.remove("animate-bounce", "animate-shake");
    }, 500);
}

function toggleSettingsData(domElements, remove_from_dom) {
    if(remove_from_dom) {
        domElements.forEach((el) => {
            el.classList.add('hidden');
        });
    } else {
        domElements.forEach((el) => {
            el.classList.remove('hidden');
        });
    }
}
