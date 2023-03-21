function openLoginPopup() {
  document.getElementById("login-popup").style.display = "block";
}

function closeLoginPopup() {
  document.getElementById("login-popup").style.display = "none";
}

function login() {
  event.preventDefault();
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  if (username === "admin" && password === "studysmart!") {
    alert("Login successful!");
    document.querySelector('.hidden').classList.remove('hidden');
    closeLoginPopup();
    return true;
  } else {
    alert("Invalid username or password.");
    return false;
  }
}
function createNote() {
  var subject = document.getElementById("subject").value;
  var duration = document.getElementById("duration").value;

  var noteContainer = document.createElement("div");
  noteContainer.className = "note-container";

  var note = document.createElement("div");
  note.className = "note";
  note.innerHTML = "<h2>" + subject + "</h2><p>" + duration + "</p>";

  noteContainer.appendChild(note);
  document.body.appendChild(noteContainer);

  document.getElementById("subject").value = "";
  document.getElementById("duration").value = "";
}