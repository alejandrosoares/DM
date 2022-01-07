/*
   CATEGORIES FOR SEARCH 
*/
import { GLOBAL } from "../globals.js";
import { createProductList } from "../products/products.js";

const PRODUCTS = GLOBAL.products;

function removeStyleSelectedCategory() {
   /* Remove style of selected category */

   const categories = document.querySelectorAll(".search-categories li");

   categories.forEach(category => {
      category.classList.remove("category-activate")
   });
}

function changeStyleCategory(id) {
   /* Add style to selected category */

   const category =  document.querySelector(`.search-categories li[data-id="${id}"]`);
   
   removeStyleSelectedCategory();

   category.classList.add('category-activate');
}


function SearchByCategory(e) {
   /* Send request for search by category 
   @param: li.search-category
   */
  
   let url = document.querySelector('#search .info .products-url').value,
      liCategory = e.target.closest('.search-category'),
         id = liCategory.getAttribute('data-id');

   fetch(`${url}?category=${id}`)
      .then(response => {
         if (response.ok) return response.json()
      })
      .then(products => {
         PRODUCTS.setProducts = products;
         createProductList();
         changeStyleCategory(id);
      })
      .catch(error => console.error(error));
}


function loadCategoriesSearch() {
   /* Load events and run functions related to categories */

   const categories = document.querySelectorAll(".search-categories .search-category");

   categories.forEach(category => {
      category.addEventListener('click', SearchByCategory);
   });
}

export { 
   loadCategoriesSearch,
   removeStyleSelectedCategory
}