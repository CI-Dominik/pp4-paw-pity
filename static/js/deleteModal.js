document.addEventListener("DOMContentLoaded", (event) => {

    // Get the delete button elements
    const deleteButtons = document.querySelectorAll('.delete-animal-button');

    // Add click event listener to each delete button
    deleteButtons.forEach(button => {

        button.addEventListener('click', function () {
            // Get the animal ID from the button data attribute
            const animalId = this.dataset.animalId;
            // Show the delete confirmation modal
            const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
            modal.show();
            // Add click event listener to the delete confirmation button
            document.getElementById('deleteConfirm').addEventListener('click', function () {
                // Perform the delete action
                const url = `/animals/delete_animal/${animalId}`;
                window.location.href = url;
                // Hide the modal
                modal.hide();
            });
        });

    });

});