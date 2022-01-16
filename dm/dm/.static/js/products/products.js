import { GLOBAL } from "../globals.js";
import requestProduct from "../request_products.js";
import { showBtnMoreItems, showMoreItems } from "./more_items.js";

const productsContainer = document.querySelector(".products-list .row"),
   loader = document.querySelector("#products .loader"),
   template = document.getElementById("item-product").content,
   fragment = document.createDocumentFragment();


const productsToShow = GLOBAL.products.toShow;

function showLoader(show) {
   /* Show Loader if show parameter is True, if is False hide loader */

   (show) ?
      loader.classList.remove("d-none") : loader.classList.add("d-none");
}

function createProductList(products) {
   /* Create Product List
   Insert inside .products-list .row with the html elements

   @param: Object, bool (is add new items or empty productsContainer)
   */

   const productsLength = products.length;

   productsContainer.innerHTML = '';

   if (productsLength > productsToShow) {
      showBtnMoreItems(true);
   } else {
      showBtnMoreItems(false);
   }

   console.log('length counter ', productsLength);

   if (productsLength) {

      let counter = 0;

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

         console.log(counter, productsToShow, counter >= productsToShow);

         if (counter >= productsToShow) {
            card.classList.add('d-none');
         }
         counter += 1;

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

   requestProduct(true, createProductList);
}


function loadProducts() {
   /* El orden de las llamadas importa */
   const btnMoreItems = document.getElementById('btn-more-items');

   btnMoreItems.addEventListener('click', showMoreItems);

   loadProductsInGlobal();
}

document.addEventListener("DOMContentLoaded", loadProducts);
document.addEventListener("click", clickProducts);

export { createProductList };