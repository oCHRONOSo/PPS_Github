const challenges = [
  "Boss Fight: Turn on 2FA and save your backup codes.",
  "Stealth Mission: Add .env to .gitignore before your next commit.",
  "Upgrade Path: Replace old PATs with fine-grained tokens.",
  "Shield Buff: Enable Dependabot security updates.",
  "Trap Check: Review pull requests for suspicious code changes.",
  "Critical Alert: Rotate any leaked secret immediately."
];

const challengeBtn = document.getElementById("challengeBtn");
const challengeText = document.getElementById("challengeText");
const tipsList = document.getElementById("tipsList");

function randomChallenge() {
  const index = Math.floor(Math.random() * challenges.length);
  return challenges[index];
}

challengeBtn.addEventListener("click", () => {
  challengeText.textContent = randomChallenge();
  fetch("/generate-log")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to write log");
      }
      return response.json();
    })
    .then((data) => {
      console.log("Backend logging status:", data.status);
    })
    .catch((error) => {
      console.error("Log endpoint error:", error.message);
    });
});

// Highlight risky keywords in the tips list.
tipsList.querySelectorAll("li").forEach((item) => {
  item.innerHTML = item.innerHTML.replace("Never", '<span class="danger">Never</span>');
});
