let currentCountry = null;

document
  .getElementById("next-btn")
  .addEventListener("click", () => loadRandomCountry());

function loadRandomCountry() {
  fetch("countries.json")
    .then((res) => res.json())
    .then((countrynames) => {
      const numberOfCountries = countrynames.length;
      const index = Math.floor(Math.random() * numberOfCountries);
      currentCountry = countrynames[index];
      console.log(currentCountry);
      const angle = Math.floor(Math.random() * 360);

      fetch(`countries/${currentCountry}`)
        .then((res) => res.text())
        .then((svg) => {
          const container = document.getElementById("svg-container");
          container.innerHTML = svg;

          const svgElement = container.querySelector("svg");
          if (svgElement) {
            svgElement.style.transform = `rotate(${angle}deg)`;
          }
        });
    });
}

document.getElementById("submit-btn").addEventListener("click", () => {
  const guess = document
    .getElementById("guess-input")
    .value.trim()
    .toLowerCase();
  const feedback = document.getElementById("feedback");
  const filenameWithoutExtension = currentCountry
    .replace(".svg", "")
    .toLowerCase();

  if (guess === filenameWithoutExtension) {
    feedback.textContent = "🎉 Correct!";
    feedback.style.color = "green";
    // setTimeout(() => {
    //   document.getElementById("guess-input").value = "";
    //   feedback.textContent = "";
    //   loadRandomCountry();
    // }, 1500);
  } else {
    feedback.textContent = "❌ Incorrect, try again!";
    feedback.style.color = "red";
  }
});

// Load first country
loadRandomCountry();
