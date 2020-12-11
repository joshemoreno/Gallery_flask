window.onload = function(){ 
    changes(form)
}

function validate(form){
    NameValidate(form)
    DescriptionValidate(form)
}

function changes(form){
    document.getElementById('name').addEventListener("change", function(){
        NameValidate(form)
    })
    document.getElementById('description').addEventListener("change", function(){
        DescriptionValidate(form)
    })
}

function NameValidate(form) {
    var nameError = document.getElementById('nameerror');
    if (form.name.value.trim().length == 0) {
        nameError.removeAttribute("hidden");
        nameError.innerHTML = "Debes ingresar nombre para la imagen";
    }else if(form.name.value.trim().length < 5){
        nameError.removeAttribute("hidden");
        nameError.innerHTML = "Tu usuario debe tener al menos 5 caracteres";
    }else if(form.name.value.trim().length > 20){
        nameError.removeAttribute("hidden");
        nameError.innerHTML = "Tu usuario debe tener maximo 15 caracteres";
    }else{
        nameError.setAttribute("hidden","true");
    }
    return false;
}

function DescriptionValidate(form) {
    var descriptionError = document.getElementById('descriptionerror');
    if (form.description.value.trim().length == 0) {
        descriptionError.removeAttribute("hidden");
        descriptionError.innerHTML = "Debes ingresar una descripción";
    }else if(form.name.value.trim().length < 15){
        descriptionError.removeAttribute("hidden");
        descriptionError.innerHTML = "Tu usuario debe tener al menos 15 caracteres";
    }else if(form.name.value.trim().length > 50){
        descriptionError.removeAttribute("hidden");
        descriptionError.innerHTML = "Tu usuario debe tener maximo 50 caracteres";
    }else{
        descriptionError.setAttribute("hidden","true");
    }
    return false;
}

const $select = document.querySelector("#file"),
    $preview = document.querySelector("#preview");
$select.addEventListener("change", () => {
    const files = $select.files;
    if (!files) {
        $preview.src = "../../Assets/Images/newImage.JPG";
        return;
    } else if (files.length) {
        $preview.src = "../../Assets/Images/newImage.JPG";
    }
    const oneFile = files[0];
    const objectURL = URL.createObjectURL(oneFile);
    $preview.src = objectURL;
});

document.getElementById("switch").checked = false;
document.getElementById('switch').addEventListener('change', (e) => {
    let status = $('#statusImag')
    this.checkboxValue = e.target.checked ? status.html('Público') : status.html('Privado');
})

