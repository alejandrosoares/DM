import { GLOBAL } from "../globals.js";

const PRODUCTS = GLOBAL.products;
const url = document.querySelector(
         "#products .products-info .url-products-json-all"
      ).value;

let START = 0,
   END = 10;

const productsContainer = document.querySelector(".products-list .row"),
   loader = document.querySelector("#products .loader"),
   template = document.getElementById("item-product").content,
   fragment = document.createDocumentFragment();


function showLoader(show) {
   /* Show Loader if show parameter is True, if is False hide loader */

   (show) ?
   loader.classList.remove("d-none"): loader.classList.add("d-none");
}

function createProductList(products) {
   /* Create Product List
   Insert inside .products-list .row with the html elements

   @param: list
   */
   
   productsContainer.innerHTML = "";

   if (products.length) {
      products.forEach(p => {
         const card = template.querySelector("div.card"),
            img = template.querySelector("div.product-header img"),
            name = template.querySelector("div.name > p"),
            price = template.querySelector("div.price > span"),
            code = template.querySelector("div.in-stock > span");
   
         card.setAttribute("data-id", p.id);
         img.src = p.img;
         name.textContent = p.name;
         price.textContent = `$ ${p.price}`;
         code.textContent = `Cód: ${p.code}`;
   
         const clone = document.importNode(template, true);
   
         fragment.appendChild(clone);
      })
   
      productsContainer.appendChild(fragment);
      
   } else {
      productsContainer.innerHTML = `
            <div class="search-not-found">
               <p>No encontramos resultados coincidentes.</p>
            </div>`;
   }

   showLoader(false);
}


function clickProducts(e) {
   /* Go to product description
   Trigger when make click in div.card.product 
   */
   if (e.target.matches("#products .product *")) {
      const card = e.target.closest("div.product"),
         product_id = card.getAttribute("data-id");

      location.href = `/products/${product_id}`;
   }
}


function loadProductsInGlobal() {
   /* Load products in the global variable */

   const url = document.querySelector(
      "#products .products-info .url-products-json-all"
   ).value;

   fetch(url)
      .then(response => {
         if (response.ok) return response.json()
      })
      .then(products => {
         PRODUCTS.setProducts = products;
         PRODUCTS.setSearchList = products;
         createProductList(PRODUCTS.setProducts);
      })
      .catch(error => console.error(error));
}

function loadProducts() {
   const searchBtn = document.getElementById('searchBtn');

   loadProductsInGlobal();
}

document.addEventListener("DOMContentLoaded", loadProducts);
document.addEventListener("click", clickProducts);

export { createProductList };