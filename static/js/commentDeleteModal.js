document.addEventListener('DOMContentLoaded', function() {

    // Get the delete modal and the delete link
    const deleteModal = document.getElementById('delete-modal');
    const deleteLink = document.getElementById('delete-link');
  
    // Ensure we correctly set the href when a delete button is clicked
    deleteModal.addEventListener('show.bs.modal', function (event) {

        // Get the button that triggered the modal
        const button = event.relatedTarget;

        // Get the comment_id and animal_id from the button data attributes
        const commentId = button.getAttribute('data-comment-id');
        const animalId = button.getAttribute('data-animal-id');
        
        // Construct the URL for deleting the comment based on the animal_id and comment_id
        deleteLink.href = `/reports/${animalId}/comments/${commentId}/delete/`;
    });
    
});
