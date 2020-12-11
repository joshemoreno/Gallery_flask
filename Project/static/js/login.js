window.onload = function(){ 
    changes(form)
}

function validate(form){
    UserValidate(form)
    PasswordValidate(form)
}

function changes(form){
    document.getElementById("user").addEventListener("change", function(){
        UserValidate(form)
    })
    document.getElementById("password").addEventListener("change", function(){
        PasswordValidate(form)
    })
}

function UserValidate(form) {
    if (form.user.value.trim().length == 0) {
        var userError = document.getElementById('usererror');
        userError.removeAttribute("hidden");
        userError.innerHTML = "Debes ingresar un usuario";
    }else if(form.user.value.trim().length < 5){
        var userError = document.getElementById('usererror');
        userError.removeAttribute("hidden");
        userError.innerHTML = "Tu usuario debe tener al menos 5 caracteres";
    }else if(form.user.value.trim().length > 15){
        var userError = document.getElementById('usererror');
        userError.removeAttribute("hidden");
        userError.innerHTML = "Tu usuario debe tener maximo 15 caracteres";
    }else{
        var userError = document.getElementById('usererror');
        userError.setAttribute("hidden","true");
    }
    return false;
}

function PasswordValidate(form) {
    if (form.password.value.trim().length < 7 ) {
        var passwordError = document.getElementById('passworderror');
        passwordError.removeAttribute("hidden");
        passwordError.innerHTML = "La contraseña debe tener al menos 7 caracteres";
    }else if (form.password.value.trim().length > 15 ) {
        var passwordError = document.getElementById('passworderror');
        passwordError.removeAttribute("hidden");
        passwordError.innerHTML = "La contraseña debe tener maximo 15 caracteres";
    }else{
        var passwordError = document.getElementById('passworderror');
        passwordError.setAttribute("hidden","true");
    }
    return false;
}
