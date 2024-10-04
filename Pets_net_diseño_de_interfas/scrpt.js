// Obtener los elementos necesarios
const searchInput = document.getElementById('searchInput');
const itemsList = document.getElementById('itemsList');

// Función para filtrar los elementos
function filterItems() {
  const searchTerm = searchInput.value.toLowerCase();
  const items = itemsList.getElementsByTagName('li');

  for (let i = 0; i < items.length; i++) {
    const item = items[i];
    const itemName = item.textContent.toLowerCase();

    if (itemName.indexOf(searchTerm) !== -1) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  }
}

// Escuchar el evento de entrada en el campo de búsqueda
searchInput.addEventListener('keyup', filterItems);