/*
   SEARCH PRODUCTS
   
   variables used:
   listWordsSearch
*/
import { GLOBAL } from "../globals.js";
import { loadCategoriesSearch, removeStyleSelectedCategory} from "./categories.js";
import { saveSearchInSessionStorage, loadSearchFromSessionStorage } from "./session_storage.js";

const PRODUCTS = GLOBAL.products;

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

function clickInSearch(e) {
   SearchWords();
   e.stopPropagation();
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
      
      console.log("matching ", matching);

      if (matching) {
         hideSearchResults(false);
      } else {
         hideSearchResults(true);
      }
   } else {
      hideSearchResults(true);
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
               removeStyleSelectedCategory(); //Remueve los estilos de las categorias, por si tiene alguna etiqueta seleccionada
         }
      };
      request.open("GET", urlSearchById + `?q=${id}&t=${type}`, true);
      request.send();
   }
}



function keyPressInSearchInput(e) {
   if (e.which === 13) {
      Search();
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

function getListProducts() {
   const url = document.querySelector('#search .info .products-url').value;
  
   fetch(url)
      .then(response => {
         if (response.ok) return response.json()
      })
      .then(products => PRODUCTS.set_products = products)
      .catch(error => console.error(error));
}


function loadSearch() {
   /* Load Search
   Add events to html elements and call to functions for 
   perform operattions
   */

   searchInput.addEventListener('click', clickInSearch);
   searchInput.addEventListener('keypress', keyPressInSearchInput);
   searchInput.addEventListener('keypress', SearchWords);

   getListProducts();
   loadSearchFromSessionStorage(); 
   loadCategoriesSearch();  
}


document.addEventListener('DOMContentLoaded', loadSearch);


document.addEventListener('click', () => hideSearchResults(true));