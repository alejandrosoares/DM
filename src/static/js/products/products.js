import { GLOBAL } from "../globals.js";
import { sendSync, buildGetRequest } from "../request.js";
import Pagination from './pagination.js';

const productDivId = 'products';
const productsContainer = document.querySelector(".products-list .row");
const searchNotFound = document.getElementById('search-not-found');
const loader = document.getElementById("products-loader");
const productsData = document.getElementById('products-data');
const productUrl = productsData.querySelector('.url-get-products').value;
const template = document.getElementById("item-product").content;
const fragment = document.createDocumentFragment();
const paginationObj = new Pagination(createProductList, productUrl, productDivId);


function showLoader(show) {
   if (show) {
      loader.classList.remove("d-none");
   } else {
      loader.classList.add("d-none");
   }
}


function showProductsNotFound(show) {
   if (show) {
      searchNotFound.classList.remove("d-none");
   } else {
      searchNotFound.classList.add("d-none");
   }
}

function setNewPagination(pagination) {
   if(pagination !== null) {
      paginationObj.buildHtml(pagination);
   }
}

function createProductList(products, pagination) {
   setNewPagination(pagination);
   productsContainer.innerHTML = '';

   if (products.length) {
      products.forEach(p => {
         const card = template.querySelector("div.card");
         const img = template.querySelector("div.product-header img");
         const name = template.querySelector("div.name > p");
         const price = template.querySelector("div.price > span");
         const code = template.querySelector("div.code > span");

         card.setAttribute('data-id', p.id);
         card.setAttribute('data-product-link', p.productLink);
         img.src = p.img;
         name.textContent = p.name;
         price.textContent = `$ ${p.price}`;
         code.textContent = `Code: ${p.code}`;
         const clone = document.importNode(template, true);
         fragment.appendChild(clone);
      })

      productsContainer.appendChild(fragment);
      loadEventsInProducts();
      showProductsNotFound(false);
   } else {
      showProductsNotFound(true);
   }

   showLoader(false);
}


function loadEventsInProducts() {
   const productCards = document.querySelectorAll('.products-list .card');
   productCards.forEach(card => card.onclick = e => clickInProductCard(e));
}


function clickInProductCard(e) {
   const card = e.target.closest('.card');
   const productLink = card.getAttribute('data-product-link');
   location.href = productLink;
}


function loadProductsInGlobal(objResponse) {
   GLOBAL.products.setSearchList(objResponse.products);
   GLOBAL.products.setProducts(objResponse.products);
   GLOBAL.pagination.setPagination(objResponse.pagination);
}


async function loadProducts() {
   const url = paginationObj.setParams(productUrl);
   const req = buildGetRequest();
   const res = await sendSync(req, url);

   createProductList(res.obj.products, res.obj.pagination);
   loadProductsInGlobal(res.obj);
}


document.addEventListener("DOMContentLoaded", loadProducts);


export { createProductList };