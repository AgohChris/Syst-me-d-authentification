const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});


// Exemple de validation côté client
document.getElementById('activationForm').addEventListener('submit', function(event) {
  const email = document.getElementById('email').value;
  const activationCode = document.getElementById('activation_code').value;
  const messageDiv = document.getElementById('message')
  // Réinitialiser les messages
  messageDiv.innerHTML = ''
  if (!email || !activationCode) {
      event.preventDefault();
      messageDiv.innerHTML = '<p class="error">Tous les champs sont obligatoires.</p>';
  } else if (activationCode.length !== 6 || isNaN(activationCode)) {
      event.preventDefault();
      messageDiv.innerHTML = '<p class="error">Le code d\'activation doit contenir exactement 6 chiffres.</p>';
  }
  });