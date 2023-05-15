import { GLOBAL } from "../globals.js";
import { sendSync, buildGetRequest } from "../request.js";


const productsContainer = document.querySelector(".products-list .row");
const searchNotFound = document.getElementById('search-not-found');
const loader = document.getElementById("products-loader");
const template = document.getElementById("item-product").content;
const fragment = document.createDocumentFragment();


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


function createProductList(products) {
   productsContainer.innerHTML = '';

   if (products.length) {
      products.forEach(p => {
         const card = template.querySelector("div.card");
         const img = template.querySelector("div.product-header img");
         const name = template.querySelector("div.name > p");
         const price = template.querySelector("div.price > span");
         const code = template.querySelector("div.code > span");

         card.setAttribute("data-id", p.id);
         img.src = p.img;
         name.textContent = p.name;
         price.textContent = `$ ${p.price}`;
         code.textContent = `Code: ${p.code}`;

         const clone = document.importNode(template, true);
         fragment.appendChild(clone);
      })

      productsContainer.appendChild(fragment);
      showProductsNotFound(false);
   } else {
      showProductsNotFound(true);
   }

   showLoader(false);
}


function clickProducts(e) {
   if (e.target.matches("#products .product *")) {
      const card = e.target.closest("div.product");
      const productId = card.getAttribute("data-id");
      location.href = `/products/${productId}`;
   }
}


function loadProductsInGlobal(products) {
   GLOBAL.products.setSearchList(products);
   GLOBAL.products.setProducts(products);
}


async function loadProducts() {
   const productsData = document.getElementById('products-data');
   const url = productsData.querySelector('.url-get-products').value;
   const req = buildGetRequest();
   const res = await sendSync(req, url);
   createProductList(res.obj.products);
   loadProductsInGlobal(res.obj.products);
}


document.addEventListener("DOMContentLoaded", loadProducts);
document.addEventListener("click", clickProducts);



export { createProductList };