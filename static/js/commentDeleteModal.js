// commentDeleteModal.js
document.addEventListener('DOMContentLoaded', function() {
    const deleteModal = document.getElementById('delete-modal');
    const deleteLink = document.getElementById('delete-link');
  
    // Ensure we correctly set the href when a delete button is clicked
    deleteModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;  // Button that triggered the modal
        const commentId = button.getAttribute('data-comment-id');
        const animalId = button.getAttribute('data-animal-id');
        
        // Construct the URL for deleting the comment based on the animal_id and comment_id
        deleteLink.href = `/reports/${animalId}/comments/${commentId}/delete/`;
    });
});
