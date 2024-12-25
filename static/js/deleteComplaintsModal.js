document.addEventListener('DOMContentLoaded', function () {
    const deleteCommentModal = document.getElementById('delete-comment-modal');
    const deleteComplaintModal = document.getElementById('delete-complaint-modal');
    const deleteCommentButtons = document.querySelectorAll('[data-bs-toggle="modal"][data-bs-target="#delete-comment-modal"]');
    const deleteComplaintButtons = document.querySelectorAll('[data-bs-toggle="modal"][data-bs-target="#delete-complaint-modal"]');

    deleteCommentButtons.forEach(button => {
        button.addEventListener('click', function () {
            const commentId = button.getAttribute('data-comment-id');
            const form = deleteCommentModal.querySelector('#delete-comment-form');
            form.action = `/complaints/remove_comment/${commentId}/`;
        });
    });

    deleteComplaintButtons.forEach(button => {
        button.addEventListener('click', function () {
            const complaintId = button.getAttribute('data-complaint-id');
            const form = deleteComplaintModal.querySelector('#delete-complaint-form');
            form.action = `/complaints/delete_complaint/${complaintId}/`;
        });
    });
});