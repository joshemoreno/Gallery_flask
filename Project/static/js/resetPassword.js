window.onload = function(){ 
    changes(form)
}

function validate(form){
    PasswordValidate(form)
    ConfirmValidate(form)
}

function changes(form){
    document.getElementById("password").addEventListener("change", function(){
        PasswordValidate(form)
    })
    document.getElementById("confirm").addEventListener("change", function(){
        ConfirmValidate(form)
    })
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

function ConfirmValidate(form) {
    if (form.password.value.trim() != form.confirm.value.trim()) {
        var confirmError = document.getElementById('confirmerror');
        confirmError.removeAttribute("hidden");
        confirmError.innerHTML = "No coincide con contraseña";
    }else{
        var confirmError = document.getElementById('confirmerror');
        confirmError.setAttribute("hidden","true");
    }
    return false;
}