<div id="settings" class="space-y-4">
  <div>
    <label for="picked_mode" class="block font-medium text-gray-700 mb-1">Choose what to practice:</label>
    <select id="picked_mode" name="picked_mode" class="...">...</select>
  </div>

  <div>
    <label for="amount" class="block font-medium text-gray-700 mb-1">How many characters?</label>
    <input id="amount" type="number" ... />
  </div>

  <button id="start" class="...">Start</button>
</div>

<button id="play-again"
        class="w-full bg-blue-500 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-600 transition hidden">
  Play Again
</button>

const settings = document.getElementById("settings");
const playAgain = document.getElementById("play-again");

document.getElementById('start').addEventListener('click', async () => {
    // Hide settings
    settings.classList.add("hidden");
    playAgain.classList.add("hidden");

    // Fetch data & start game logic...
});


function showCharacter(data, currentIndex, kanaDisplay, inputField, submitButton, gameMode) {
    if (currentIndex < data.length) {
        kanaDisplay.textContent = data[currentIndex][gameMode];
        inputField.value = "";
        inputField.focus();
    } else {
        kanaDisplay.textContent = "Done! 🎉";
        submitButton.disabled = true;
        inputField.disabled = true;
        playAgain.classList.remove("hidden");
    }
}

playAgain.addEventListener("click", () => {
    location.reload(); // simplest way to reset everything
});
