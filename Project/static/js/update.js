window.onload = function(){ 
    changes()
}
function inactiveSubmit(){
    document.getElementById('submitBtn').disabled=true;
}
function activeSubmit(){
    document.getElementById('submitBtn').disabled=false;
}

function changes(){
    document.getElementById('name').addEventListener("change", function(){
        NameValidate()
    })
    document.getElementById('description').addEventListener("change", function(){
        DescriptionValidate()
    })
}

function NameValidate() {
    var name = document.getElementById('name');
    var nameError = document.getElementById('nameerror');
    if (name.value.trim().length == 0) {
        nameError.removeAttribute("hidden");
        nameError.innerHTML = "Debes ingresar un nombre para la imagen";
        inactiveSubmit();
    }else if(name.value.trim().length < 5){
        nameError.removeAttribute("hidden");
        nameError.innerHTML = "El nombre de la imagen debe tener al menos 5 caracteres";
        inactiveSubmit();
    }else if(name.value.trim().length > 20){
        nameError.removeAttribute("hidden");
        nameError.innerHTML = "El nombre de la imagen debe tener máximo 20 caracteres";
        inactiveSubmit();
    }else{
        nameError.setAttribute("hidden","true");
        activeSubmit();
    }
    return false;
}

function DescriptionValidate() {
    var description = document.getElementById('description');
    var descriptionError = document.getElementById('descriptionerror');
    if (description.value.trim().length == 0) {
        descriptionError.removeAttribute("hidden");
        descriptionError.innerHTML = "Debes ingresar una descripción para la imagen";
        inactiveSubmit();
    }else if(description.value.trim().length < 15){
        descriptionError.removeAttribute("hidden");
        descriptionError.innerHTML = "La descripción de la imagen debe tener al menos 15 caracteres";
        inactiveSubmit();
    }else if(description.value.trim().length > 250){
        descriptionError.removeAttribute("hidden");
        descriptionError.innerHTML = "La descripción de la imagen debe tener máximo 250 caracteres";
        inactiveSubmit();
    }else{
        descriptionError.setAttribute("hidden","true");
        activeSubmit();
    }
    return false;
}

document.getElementById("switch").checked = false;
document.getElementById('switch').addEventListener('change', (e) => {
    let status = $('#statusImag')
    this.checkboxValue = e.target.checked ? status.html('Público') : status.html('Privado');
})