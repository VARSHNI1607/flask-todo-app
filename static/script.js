function openEditModal(taskId) {
  fetch(`/get_task/${taskId}`)
  .then(response => response.json())
  .then(task => {
      document.getElementById('editTitle').value = task.title;
      document.getElementById('editCategory').value = task.category;
      document.getElementById('editDeadline').value = task.deadline;
      document.getElementById('editPriority').value = task.priority;
      document.getElementById('editForm').action = `/edit/${task.id}`;
      document.getElementById('editModal').style.display = 'block';
  });
}

function closeEditModal() {
  document.getElementById('editModal').style.display = 'none';
}

// Close modal if user clicks outside
window.onclick = function(event) {
  if (event.target == document.getElementById('editModal')) {
      closeEditModal();
  }
}
