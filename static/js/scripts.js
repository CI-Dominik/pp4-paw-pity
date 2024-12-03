// Adjusted function learned from Code institute

document.addEventListener("DOMContentLoaded", (event) => {

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let animalId = e.target.getAttribute("animal_id");
            deleteConfirm.href = `delete_animal/${animalId}`;
            deleteModal.show();
        });
    }

});