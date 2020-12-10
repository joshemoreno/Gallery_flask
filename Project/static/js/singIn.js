window.onload = function() {
    document.getElementById("submitNewAccount").addEventListener("click",function(e){
        e.preventDefault();
        validateUser();
        validateMail();
        validatePassword();
    });
  };
window.onchange = function() {
    document.getElementById("user").addEventListener('change',validateUser());

}

function validateUser() {
    var user = document.getElementById('user').value;
    userPattern = /^[a-z]+$/;
    console.log(userPattern.test(user));
    if (!userPattern.test(user)){
        document.getElementById('userMessage').style.visibility='visible';
        document.getElementById('userMessage').innerText="El usuario debe cumplir con los parametros";
    }
    return false;
}

function validateMail() {
    var email = document.getElementById('email').value;
    //emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/;
    emailPattern = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/;
    console.log(emailPattern.test(email));
    if (!emailPattern.test(email)){
        document.getElementById('emailMessage').style.visibility='visible';
        document.getElementById('emailMessage').innerText="La dirección de email es incorrecta.";
    }
    return false;
}

function validatePassword() {
    var password = document.getElementById('password').value;
    var minNumberofChars = 6;
    var maxNumberofChars = 16;
    if(password.length < minNumberofChars || password.length > maxNumberofChars){
        document.getElementById('passwordMessage').style.visibility='visible';
        document.getElementById('passwordMessage').innerText="La contraseña debe tener al menos 6 caracteres y máximo 16 caracteres.";
        return false;
    }

    passwordPattern = /^[a-zA-Z0-9!@#$%^&*]{6,16}$/;
    console.log(passwordPattern.test(password));
    if (!passwordPattern.test(password)){
        document.getElementById('passwordMessage').style.visibility='visible';
        document.getElementById('passwordMessage').innerText="La contraseña debe contener al menos 1 número y 1 caracter especial.";
    }
    return false;
}