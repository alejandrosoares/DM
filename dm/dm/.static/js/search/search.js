/*
   SEARCH PRODUCTS
   
   variables used:
   minCharsToSearch: minimum characters to display results

*/
import { GLOBAL } from "../globals.js";
import { loadCategoriesSearch, removeStyleSelectedCategory } from "./categories.js";
import { saveSearchInSessionStorage, loadSearchFromSessionStorage } from "./session_storage.js";
import { createProductList } from "../products/products.js";
import requestProduct from "../request_products.js";

const PRODUCTS = GLOBAL.products;
const minCharsToSearch = 2;

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


function addEventToResultItem() {
   const resultItems = document.querySelectorAll('.search-result-item');

   resultItems.forEach(item => {
      item.addEventListener('click', saveSearchInSessionStorage)
   });
}

function clickInSearch(e) {
   SearchOfMatching();
   e.stopPropagation();
}

function writeProductsInSearchResult() {
   /* Write Products in div.search-result-list 
   Add the li elements into searchResultList
   */
   const products = PRODUCTS.getSearchList;
   let search = searchInput.value,
      formatedSearch = normalizeSearchValue(search),
      matching = false;

   searchResultList.innerHTML = "";

   for (const p of products) {
      if (
         p.normalized_name.search(formatedSearch) != -1 ||
         p.id == formatedSearch
      ) {
         if (p.img !== null) {
            // Contains image
            searchResultList.innerHTML =
               searchResultList.innerHTML +
               `<li class="search-result-item">
                  <a href="/products/${p.id}">\
                     <img class="img-search-results" src="${p.img}" alt="Imagen">\
                     <span>${p.name.replace(formatedSearch, '<b>' + formatedSearch + '</b>')}</span>\
                  </a>
               </li>`;
         } else {
            // Without image
            searchResultList.innerHTML =
               searchResultList.innerHTML +
               `<li class="search-result-item">
                  <a href="/products/${p.id}">\
                     <span> ${p.name.replace(formatedSearch, '<b>' + formatedSearch + '</b>')}</span>
                  </a>
               </li>`;
         }
         matching = true;
      }
   }

   return matching;
}

function SearchOfMatching(e) {
   /* Search of matching
   
   e is undefined if SearchOfMatching is called from clickInSearch function

   If e.which not is 13 or e is undefined, then write into searchResultList with matched results
   If e.which is 13, then send request to search by words inserted in searchInput
   
   */
   if (e === undefined || e.which !== 13) {
      const search = searchInput.value;

      if (search.length > minCharsToSearch) {

         const matching = writeProductsInSearchResult();

         if (matching) {
            hideSearchResults(false);
            addEventToResultItem();
         } else {
            hideSearchResults(true);
         }
      } else {
         hideSearchResults(true);
      }
   } else {
      searchByWords();
      hideSearchResults(true);
   }

   if (e !== undefined) {
      e.stopPropagation();
   }
}


function searchByWords() {
   /* Search by words inserted into serch input */
   const url = document.querySelector(
      "#products .products-info .url-products-json-all"
   ).value;

   let query = document.getElementById('searchInput').value;

   if (query !== '') {

      query = encodeURIComponent(query);

      requestProduct(`${url}?query=${query}`, createProductList);

   } else {
      // query is empty
      createProductList(PRODUCTS.getSearchList);
   }
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


function loadSearch() {
   /* Load Search
   Add events to html elements and call to functions for 
   perform operattions
   */

   searchInput.addEventListener('click', clickInSearch);
   searchInput.addEventListener('keyup', SearchOfMatching);
   searchBtn.addEventListener('click', searchByWords);

   loadSearchFromSessionStorage();
   loadCategoriesSearch();
}


document.addEventListener('DOMContentLoaded', loadSearch);
document.addEventListener('click', () => hideSearchResults(true));