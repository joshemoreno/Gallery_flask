// function validateMail(email) {
//     if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/.test(email)) {
//         alert("La dirección de email " + email + " es correcta.");
//        } else {
//         alert("La dirección de email es incorrecta.");
//        }
// }

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

function validateName() {
    var newPassword = document.getElementById('user').value;
    patronNombre = /^([A-Z]{1}[a-z]+[\s]*)+$/;
    compNombre = patronNombre.test(nombre);
    correcto(compNombre);
    document.getElementById('mensaje').value="La dirección de email es incorrecta.";
}