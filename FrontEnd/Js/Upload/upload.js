const $select = document.querySelector("#file"),
    $preview = document.querySelector("#preview");
$select.addEventListener("change", () => {
    const files = $select.files;
    if (!files) {
        $preview.src = "../../Assets/Images/newImage.JPG";
        return;
    }else if(files.length){
        $preview.src = "../../Assets/Images/newImage.JPG";
    }
    const oneFile = files[0];
    const objectURL = URL.createObjectURL(oneFile);
    $preview.src = objectURL;
});

document.getElementById('switch').addEventListener('change', (e) => {
    let status = $('#statusImag')
    this.checkboxValue = e.target.checked ? status.html('Público') : status.html('Privado');
  })