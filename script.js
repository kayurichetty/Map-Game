let currentCountry = null;

document
  .getElementById("next-btn")
  .addEventListener("click", () => loadRandomCountry());

function loadRandomCountry() {
  const nextbtn = document.getElementById("next-btn");
  nextbtn.style.visibility = "hidden";
  const angletext = document.getElementById("angletext");
  // angle.style.visibility = "hidden";

  const name = document.getElementById("countryname");
  fetch("countries.json")
    .then((res) => res.json())
    .then((countrynames) => {
      const numberOfCountries = countrynames.length;
      const index = Math.floor(Math.random() * numberOfCountries);
      currentCountry = countrynames[index];
      console.log(currentCountry);
      name.textContent = currentCountry;
      const angle = Math.floor(Math.random() * 360);
      angletext.textContent = angle;

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
  const nextbtn = document.getElementById("next-btn");
  const angle = document.getElementById("angletext");

  if (guess === filenameWithoutExtension) {
    feedback.textContent = "🎉 Correct!";
    feedback.style.color = "green";
    nextbtn.style.visibility = "visible";
    angle.style.visibility = "visible";
  } else {
    feedback.textContent = "❌ Incorrect, try again!";
    feedback.style.color = "red";
  }
});

// Load first country
loadRandomCountry();
