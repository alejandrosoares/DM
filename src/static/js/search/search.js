import { GLOBAL } from "../globals.js";
import { loadCategories, removeAllSelectedStyle as removeSelectedCategoryStyle } from "./categories.js";
import { saveSearchInSessionStorage, loadSearchFromSessionStorage } from "./session_storage.js";
import { createProductList } from "../products/products.js";
import { normalizeText } from '../helpers/normalize.js';
import { buildGetRequest, sendSync } from "../request.js";


const PRODUCTS = GLOBAL.products;
const searchDiv = document.getElementById('search');
const searchResultContainer = searchDiv.querySelector(".search-result-list");
const searchResultList = searchResultContainer.querySelector("ul");
const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");


function addEventToResultItem() {
   const resultItems = document.querySelectorAll('.search-result-item');
   resultItems.forEach(item => {
      item.addEventListener('click', saveSearchInSessionStorage)
   });
}


function clickInInputSearch(e) {
   searchForMatching();
   e.stopPropagation();
}


function typingInInputSearch(e) {
   const enterCode = 13;
   if (e.keyCode === enterCode) {
      searchByWords();
      showSearchResults(false);
   } else {
      searchForMatching();
   }
}


function writeMatches() {
   const products = PRODUCTS.getSearchList();
   const toSearch = searchInput.value;
   const normalizedSearch = normalizeText(toSearch);
   let match = false;
   searchResultList.innerHTML = "";

   for (const p of products) {
      const hasMatching = (
         p.normalized_name.search(normalizedSearch) !== -1 
         || p.id === normalizedSearch
      );

      if (hasMatching) {
         if (p.img !== null) {
            searchResultList.innerHTML += getHtmlOfResultWithImg(p, normalizedSearch);
         } else {
            searchResultList.innerHTML += getHtmlOfResultWithOutImg(p, normalizedSearch);
         }
         match = true;
      }
   }

   return match;
}


function getHtmlOfResultWithImg(p, normalizedSearch) {
   return `<li class="search-result-item">
            <a href="/products/${p.id}">\
               <img class="img-search-results" src="${p.img}" alt="Image">\
               <span>${p.name.replace(normalizedSearch, '<b>' + normalizedSearch + '</b>')}</span>\
            </a>
         </li>`;
}


function getHtmlOfResultWithOutImg(p, normalizedSearch) {
   return `<li class="search-result-item">
            <a href="/products/${p.id}">\
               <span> ${p.name.replace(normalizedSearch, '<b>' + normalizedSearch + '</b>')}</span>
            </a>
         </li>`;
}


function searchForMatching() {
   const minCharsToSearch = 3;
   const isValid = searchInput.value.length >= minCharsToSearch;
   const hasMatches = writeMatches();
   if (isValid && hasMatches) {
      showSearchResults(true);
      addEventToResultItem(); 
      return; 
   }
   showSearchResults(false); 
}


async function searchByWords() {
   const url = document.querySelector("#products-data .url-get-products").value;
   const toSearch = searchInput.value;
  
   if (toSearch !== '') {
      const urlSearchByWords = `${url}?query=${encodeURIComponent(toSearch)}`;
      const req = buildGetRequest();
      const res = await sendSync(req, urlSearchByWords);
      createProductList(res.obj.products);
   } else {
      createProductList(PRODUCTS.getSearchList());
   }

   removeSelectedCategoryStyle();
}


function showSearchResults(show) {
   if (show) {
      searchResultContainer.classList.remove('d-none');
      searchInput.classList.add("input-box-result-active");
      searchBtn.classList.add("btn-box-result-active"); 
   } else {
      searchResultContainer.classList.add('d-none');
      searchInput.classList.remove("input-box-result-active");
      searchBtn.classList.remove("btn-box-result-active");
   }
}


function loadSearch() {
   searchInput.addEventListener('click', clickInInputSearch);
   searchInput.addEventListener('keyup', typingInInputSearch);
   searchBtn.addEventListener('click', searchByWords);
   loadSearchFromSessionStorage();
   loadCategories();
}


document.addEventListener('DOMContentLoaded', loadSearch);
document.addEventListener('click', () => showSearchResults(false));