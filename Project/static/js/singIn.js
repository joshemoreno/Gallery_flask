/* window.onload = function() {
    validateName();
  }; */

window.onclick = function() {
    validateUser();
    validateMail();
}

// function validatePassword() {
//     var newPassword = document.getElementById('changePasswordForm').newPassword.value;
//     var minNumberofChars = 6;
//     var maxNumberofChars = 16;
//     var regularExpression  = /^[a-zA-Z0-9!@#$%^&*]{6,16}$/;
//     alert(newPassword); 
//     if(newPassword.length < minNumberofChars || newPassword.length > maxNumberofChars){
//         return false;
//     }
//     if(!regularExpression.test(newPassword)) {
//         alert("La contraseña debe contener al menos 1 número y 1 caracter especial");
//         return false;
//     }
// }

function validateUser() {
    var user = document.getElementById('user').value;
    userPattern = /^[a-z]+$/;
    console.log(userPattern.test(user));
    if (userPattern.test(user)){
        document.getElementById('userMessage').style.visibility='visible';
        document.getElementById('userMessage').innerText="El usuario cumple con los parametros";
    } else {
        document.getElementById('userMessage').style.visibility='visible';
        document.getElementById('userMessage').innerText="El usuario debe cumplir con los parametros";
    }
}

function validateMail() {
    var email = document.getElementById('email').value;
    //emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/;
    emailPattern = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/;
    console.log(emailPattern.test(email));
    if (emailPattern.test(email)){
        document.getElementById('emailMessage').style.visibility='visible';
        document.getElementById('emailMessage').innerText="La dirección de email " + email + " es correcta.";
    } else {
        document.getElementById('emailMessage').style.visibility='visible';
        document.getElementById('emailMessage').innerText="La dirección de email es incorrecta.";
    }
}
