document.addEventListener('DOMContentLoaded', function () {

    // Get the delete comment and delete complaint modals
    const deleteCommentModal = document.getElementById('delete-comment-modal');
    const deleteComplaintModal = document.getElementById('delete-complaint-modal');
    const deleteCommentButtons = document.querySelectorAll('[data-bs-toggle="modal"][data-bs-target="#delete-comment-modal"]');
    const deleteComplaintButtons = document.querySelectorAll('[data-bs-toggle="modal"][data-bs-target="#delete-complaint-modal"]');

    // Add click event listener to each delete comment button
    deleteCommentButtons.forEach(button => {
        button.addEventListener('click', function () {
            const commentId = button.getAttribute('data-comment-id');
            const form = deleteCommentModal.querySelector('#delete-comment-form');
            form.action = `/complaints/remove_comment/${commentId}/`;
        });
    });

    // Add click event listener to each delete complaint button
    deleteComplaintButtons.forEach(button => {
        button.addEventListener('click', function () {
            const complaintId = button.getAttribute('data-complaint-id');
            const form = deleteComplaintModal.querySelector('#delete-complaint-form');
            form.action = `/complaints/delete_complaint/${complaintId}/`;
        });
    });
});