document.addEventListener('DOMContentLoaded', () => {
    const itemForm = document.getElementById('itemForm');
    const itemIdInput = document.getElementById('itemId');
    const itemNameInput = document.getElementById('itemName');
    const submitButton = document.getElementById('submitButton');
    const itemTableBody = document.querySelector('#itemTable tbody');

    // Load items from localStorage, or start with an empty array
    let items = JSON.parse(localStorage.getItem('items')) || [];
    // Determine the next available ID
    let nextId = items.length > 0 ? Math.max(...items.map(item => item.id)) + 1 : 1;

    // Function to render items in the table
    function renderItems() {
        itemTableBody.innerHTML = ''; // Clear existing rows
        if (items.length === 0) {
            const noItemsRow = document.createElement('tr');
            // Adjust colspan to 3 (ID, Name, Actions)
            noItemsRow.innerHTML = '<td colspan="3" style="text-align: center;">No items yet. Add one!</td>';
            itemTableBody.appendChild(noItemsRow);
            return;
        }

        items.forEach(item => {
            const row = itemTableBody.insertRow();
            row.insertCell().textContent = item.id;
            row.insertCell().textContent = item.name;

            const actionsCell = row.insertCell();
            const editButton = document.createElement('button');
            editButton.textContent = 'Edit';
            editButton.classList.add('edit-btn');
            editButton.onclick = () => editItem(item.id);

            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            deleteButton.classList.add('delete-btn');
            deleteButton.onclick = () => deleteItem(item.id);

            actionsCell.appendChild(editButton);
            actionsCell.appendChild(deleteButton);
        });
    }

    // CREATE and UPDATE operation
    itemForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent default form submission

        const id = itemIdInput.value;
        const name = itemNameInput.value.trim();

        if (name === '') {
            alert('Item Name cannot be empty!');
            return;
        }

        if (id) {
            // UPDATE existing item
            const itemIndex = items.findIndex(item => item.id === parseInt(id));
            if (itemIndex !== -1) {
                items[itemIndex].name = name;
            }
            submitButton.textContent = 'Add Item'; // Change button text back
        } else {
            // CREATE new item
            const newItem = {
                id: nextId++,
                name: name
            };
            items.push(newItem);
        }

        // Save updated items to localStorage
        localStorage.setItem('items', JSON.stringify(items));
        itemForm.reset(); // Clear the form
        itemIdInput.value = ''; // Clear hidden ID for next add
        renderItems(); // Re-render the table
    });

    // READ operation (initial load and after every change)
    renderItems();

    // EDIT operation (populate form)
    function editItem(id) {
        const itemToEdit = items.find(item => item.id === id);
        if (itemToEdit) {
            itemIdInput.value = itemToEdit.id;
            itemNameInput.value = itemToEdit.name;
            submitButton.textContent = 'Update Item'; // Change button text
        }
    }

    // DELETE operation
    function deleteItem(id) {
        if (confirm('Are you sure you want to delete this item?')) {
            items = items.filter(item => item.id !== id);
            localStorage.setItem('items', JSON.stringify(items));
            renderItems();
            // If the deleted item was being edited, clear the form
            if (itemIdInput.value === String(id)) {
                itemForm.reset();
                itemIdInput.value = '';
                submitButton.textContent = 'Add Item';
            }
        }
    }
});