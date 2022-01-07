/*
   variables used:
   listWordsSearch
*/

const searchResultContainer = document.querySelector("#search .search-result-list"),
   searchResultList = searchResultContainer.querySelector("ul"),
   searchInput = document.getElementById("searchInput"),
   searchBtn = document.getElementById("searchBtn");

function ClearSearchInput() {
   searchInput.value = "";
}

function normalizeSearchValue(text) {
   /* Normalize the search value 
   Replace accent mark and convert to upper case

   @param: str
   @return: str
   */
   text = text
      .replace("á", "a")
      .replace("é", "e")
      .replace("í", "i")
      .replace("ó", "o")
      .replace("ú", "u");

   text = text
      .replace("Á", "A")
      .replace("É", "E")
      .replace("Í", "I")
      .replace("Ó", "O")
      .replace("Ú", "U");

   return text.toUpperCase();
}




function SearchWords() {
   let search = searchInput.value,
      formatedSearch = normalizeSearchValue(search),
      matching = false;

   if (search.length > 2) {

      searchResultList.innerHTML = "";

      for (const p of PRODS) {
         if (
            p.normalized_name.search(formatedSearch) != -1 ||
            p.id == formatedSearch
         ) { 
            console.log('existe coincidencia')
            if (p.img !== null) {
               // Contains image

               /* Cambiar li, solo debe contener id */
               searchResultList.innerHTML =
               searchResultList.innerHTML +
                  `<li onclick="saveSearchInSessionStorage()">
                     <a href="/products/${p.id}">\
                        <img class="img-search-results" src="${p.img}" alt="Imagen">\
                        <span>${p.name.replace(formatedSearch, '<b>' + formatedSearch + '</b>')}</span>\
                     </a>
                  </li>`;
            } else {
               // Without image
               searchResultList.innerHTML =
               searchResultList.innerHTML +
                  `<li>
                     <a href="/products/${p.id}">\
                        <span> ${p.name.replace(formatedSearch, '<b>' + formatedSearch + '</b>')}</span>
                     </a>
                  </li>`;
            }
            matching = true;
         }
      }
      
      console.log(matching);

      if (matching) {
         hideSearchResults(false);
      } else {
         hideSearchResults(true);
      }
   } else {
      hideSearchResults(true);
   }
}

function Search() {
   // Funcion para buscar lo que se escribe en el input de busqueda
   var value = document.getElementById("searchInput").value;
   let request;

   request = RequestConstruction();

   if (request) {
      request.onreadystatechange = function () {
         if (request.readyState == 4 && request.status == 200) {
            document.getElementById("productsContainer").innerHTML =
               request.responseText;
            RemoveStyleCategories();
            window.setTimeout(function () {
               // Temporizando para que ocurra el evento keyup y luego oculte el cuadro de busquedas
               hideSearchResults(true);
            }, 1000);
         }
      };
      request.open("GET", urlSearch + "?q=" + value, true);
      request.send();
   }
}

function SearchById(type, i, id) {
   // Actua cuando se realiza click en algun resultado de busqueda coincidente con el input de busqueda
   // Los argumentos de la funcion son:
   // *type que indica el tipo de consulta, si es un producto o marca (para buscar en la bases de datos)
   // *i que es el incide de lo clickeado dentro de la lista listWordsSearch, se utiliza para escribir lo clickeado en el input
   // *id de la consulta, puede ser el id de una marca o de un producto
   let request;

   searchInput.value = listWordsSearch[i][0];

   request = RequestConstruction();

   if (request) {
      request.onreadystatechange = function () {
         if (request.readyState == 4 && request.status == 200) {
            document.getElementById("productsContainer").innerHTML =
               request.responseText;
            RemoveStyleCategories(); //Remueve los estilos de las categorias, por si tiene alguna etiqueta seleccionada
         }
      };
      request.open("GET", urlSearchById + `?q=${id}&t=${type}`, true);
      request.send();
   }
}

function SearchByCategory(id) {
   let request;
   request = RequestConstruction();
   if (request) {
      request.onreadystatechange = function () {
         if (request.readyState == 4 && request.status == 200) {
            document.getElementById("productsContainer").innerHTML =
               request.responseText;
            ChangeStyleCategory(id);
            ClearSearchInput();
         }
      };
      request.open("GET", urlSearchByCategory + "?q=" + id, true);
      request.send();
   }
}

function keyPressInSearchInput(e) {
   if (e.which === 13) {
      Search();
   }
   e.stopPropagation();
}

function ShowResults(e) {
   if (searchResultList.style.display == "none") {
      SearchWords();
   }
   e.stopPropagation();
}

function hideSearchResults(hide) {
   /* Show or Hide div.search-result-list 
   If hide is true, hide the div and change borders of input and button to search
   */

   if (hide) {
      searchResultContainer.classList.add('d-none');
      searchInput.classList.remove("input-box-result-active");
      searchBtn.classList.remove("btn-box-result-active");
   } else {
      searchResultContainer.classList.remove('d-none');
      searchInput.classList.add("input-box-result-active");
      searchBtn.classList.add("btn-box-result-active");
   }
}

function ChangeStyleCategory(id) {
   const categories = document.getElementsByClassName("categories"),
      lCategories = categories.length;

   for (var i = 0; i < lCategories; i++) {
      if (categories[i].getAttribute("idvalue") === id) {
         categories[i].classList.add("category-activate");
      } else {
         categories[i].classList.remove("category-activate");
      }
   }
}

function RemoveStyleCategories() {
   const categories = document.getElementsByClassName("categories"),
      lCategories = categories.length;
   for (var i = 0; i < lCategories; i++) {
      categories[i].classList.remove("category-activate");
   }
}


document.addEventListener("click", function () {hideSearchResults(true)});

let PRODS = null;

function getListProducts() {
   const url = document.querySelector('#search .info .products-url').value;
  
   fetch(url)
      .then(response => {
         if (response.ok) return response.json()
      })
      .then(products => {
         PRODS = products;
      })
      .catch(error => {
         console.log('error')
         console.error(error)
      });
}

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

function loadSearch() {

   searchInput.addEventListener('keyup', keyPressInSearchInput);

   getListProducts();
   SearchWords();
   loadSearchFromSessionStorage();
}


document.addEventListener('DOMContentLoaded', loadSearch);