function saveSearchInSessionStorage() {
   const searchInput = document.getElementById('searchInput');
   sessionStorage.setItem('search', searchInput.value);
}

function loadSearchFromSessionStorage() {
   const sessionValue = sessionStorage.getItem('search');

   if (sessionValue) {
      const searchInput = document.getElementById('searchInput');
      searchInput.value = sessionStorage.getItem('search');
   }
}

export {
   loadSearchFromSessionStorage,
   saveSearchInSessionStorage
}