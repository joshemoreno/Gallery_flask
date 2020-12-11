var exp = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

// document.getElementById('submit').addEventListener("click", function(e){
//     e.preventDefault;
//     MailValidate()
//     UserValidate()
//     PasswordValidate()
//     ConfirmValidate()
// })

function inactiveSubmit(){
    var x = document.getElementById('submitBtn');
    x.removeAttribute('disable');
    console.log(x)
}

window.onload = function(){ 
    // changes()
    inactiveSubmit()
}

// function validate(){
//     // return [MailValidate(),UserValidate(),PasswordValidate(),ConfirmValidate()]
//     // UserValidate()
//     // PasswordValidate()
//     // ConfirmValidate()
//     // return false;
// }

function changes(){
    document.getElementById("user").addEventListener("change", function(){
        return UserValidate()
    })
    document.getElementById("mail").addEventListener("change", function(){
       return MailValidate()
    })
    document.getElementById("password").addEventListener("change", function(){
        return PasswordValidate()
    })
    document.getElementById("confirm").addEventListener("change", function(){
        return ConfirmValidate()
    })
}

function UserValidate(e) {
    var user = document.getElementById('user');
    var salida = true;

    if (user.value.trim().length == 0) {
        var userError = document.getElementById('usererror');
        userError.removeAttribute("hidden");
        userError.innerHTML = "Debes ingresar un usuario";
        salida = false;
    }else if(user.value.trim().length < 5){
        var userError = document.getElementById('usererror');
        userError.removeAttribute("hidden");
        userError.innerHTML = "Tu usuario debe tener al menos 5 caracteres";
        salida = false;
    }else if(user.value.trim().length > 15){
        var userError = document.getElementById('usererror');
        userError.removeAttribute("hidden");
        userError.innerHTML = "Tu usuario debe tener maximo 15 caracteres";
        salida = false;
    }else{
        var userError = document.getElementById('usererror');
        userError.setAttribute("hidden","true");
    }
    return salida;
}

function MailValidate() {
    var mail = document.getElementById('mail');
    var salida = true;

    if (mail.value.trim().length == 0){
        var emailError = document.getElementById('mailerror');
        emailError.removeAttribute("hidden");
        emailError.innerHTML = "Debes ingresar un correo";
        salida = false;
    }else if  (!exp.test(mail.value)) {
        var emailError = document.getElementById('mailerror');
        emailError.removeAttribute("hidden");
        emailError.innerHTML = "Correo invalido";
        inactiveSubmit()
        salida = false;
    }else{
        var emailError = document.getElementById('mailerror');
        emailError.setAttribute("hidden","true");
    }
    console.log(salida)
    return salida;
}

function PasswordValidate() {
    var password = document.getElementById('password');
    var salida = true;
    if (password.value.trim().length < 7 ) {
        var passwordError = document.getElementById('passworderror');
        passwordError.removeAttribute("hidden");
        passwordError.innerHTML = "La contraseña debe tener al menos 7 caracteres";
        salida = false;
    }else if (password.value.trim().length > 15 ) {
        var passwordError = document.getElementById('passworderror');
        passwordError.removeAttribute("hidden");
        passwordError.innerHTML = "La contraseña debe tener maximo 15 caracteres";
        salida = false;
    }else{
        var passwordError = document.getElementById('passworderror');
        passwordError.setAttribute("hidden","true");
    }
    return salida;
}

function ConfirmValidate() {
    var password = document.getElementById('password');
    var confirm = document.getElementById('confirm');
    var salida = true;
    if (password.value.trim() != confirm.value.trim()) {
        var confirmError = document.getElementById('confirmerror');
        confirmError.removeAttribute("hidden");
        confirmError.innerHTML = "No coincide con contraseña";
        salida = false;
    }else{
        var confirmError = document.getElementById('confirmerror');
        confirmError.setAttribute("hidden","true");
    }
    return salida;
}


