$(document).ready(function() {
    $('#studentTable').DataTable();
});

function openAddModal() {
    $('#studentId').val('');
    $('#name').val('');
    $('#subject').val('');
    $('#marks').val('');
    $('#studentModal').show();
    $('#overlay').show();
}

function openEditModal(id, name, subject, marks) {
    $('#studentId').val(id);
    $('#name').val(name);
    $('#subject').val(subject);
    $('#marks').val(marks);
    $('#studentModal').show();
    $('#overlay').show();
}

function closeModal() {
    $('#studentModal').hide();
    $('#overlay').hide();
}

function saveStudent() {
    const id = $('#studentId').val();
    const name = $('#name').val();
    const subject = $('#subject').val();
    const marks = $('#marks').val();

    const url = id ? '/edit_ajax/' : '/save_ajax/';
    const payload = id ? {id, name, subject, marks} : {name, subject, marks};

    fetch(url, {
        method: 'POST',
        headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCSRFToken()},
        body: JSON.stringify(payload)
    }).then(() => location.reload());
}

function deleteStudent(id) {
    if (confirm('Are you sure?')) {
        fetch('/delete_ajax/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCSRFToken()},
            body: JSON.stringify({id})
        }).then(() => location.reload());
    }
}

function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken'))
        ?.split('=')[1];
}