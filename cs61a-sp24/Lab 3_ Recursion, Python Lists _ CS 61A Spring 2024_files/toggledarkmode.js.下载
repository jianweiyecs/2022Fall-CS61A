function onDarkModeToggleClick() {
  let checked = $("#toggle-mode-cb").is(":checked");
  try {
    localStorage.setItem("dark-mode-enabled", checked);
  } catch(error) {
    console.error(error);
  }

  let body = document.getElementById("index");
  body.classList.toggle("dark-mode-active");
  if (checked) {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
  }
}

function checkForDarkMode() {
  $("#toggle-mode-cb").on("click", onDarkModeToggleClick);
  let checked = "true" == localStorage.getItem("dark-mode-enabled");
  let body = document.getElementById("index");
  if (checked) {
    body.classList.add('dark-mode-active');
  }
  $("#toggle-mode-cb").prop('checked', checked);
}

$(document).ready(checkForDarkMode);

let checked = "true" == localStorage.getItem("dark-mode-enabled");
if (checked) {
  document.documentElement.setAttribute('data-theme', 'dark');
}