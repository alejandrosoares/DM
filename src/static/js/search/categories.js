import { createProductList } from "../products/products.js";
import { sendSync, buildGetRequest } from '../request.js';


const categoriesDiv = document.getElementById('categories');
const categories = categoriesDiv.querySelectorAll(".search-category");


function removeAllSelectedStyle() {
   categories.forEach(category => {
      category.classList.remove("category-activate")
   });
}


function addSelectedStyle(id) {
   const category = categoriesDiv.querySelector(`li[data-id="${id}"]`);
   removeAllSelectedStyle();
   category.classList.add('category-activate');
}


async function searchByCategory(e) {
   const category  = e.target.closest('.search-category');
   const categoryId = category.getAttribute('data-id');
   const res = await getProductsBy(categoryId);
   addSelectedStyle(categoryId);
   createProductList(res.obj.products, res.obj.pagination);
}


async function getProductsBy(categoryId) {
   const divData = document.getElementById('categories-data');
   const url = divData.querySelector('.get-products').value;
   const urlSearchById = `${url}?category=${categoryId}`;
   const req = buildGetRequest();
   const res = await sendSync(req, urlSearchById);
   return res;
}


function loadCategories() {
   categories.forEach(category => {
      category.onclick = e => searchByCategory(e);
   });
}


export {
   loadCategories,
   removeAllSelectedStyle
}