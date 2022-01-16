import { GLOBAL } from "../globals.js";

const PRODUCTS = GLOBAL.products;

function showBtnMoreItems(show) {
   /* Show more-items button */

   const divMoreItems = document.getElementById('more-items-container');

   if (show) {
      divMoreItems.classList.remove('d-none');
   } else {
      divMoreItems.classList.add('d-none');
   }
}

function showMoreItems() {
   /*
      Remove .d-none of first 8 items
   */

   const divProducts = document.querySelectorAll('.products-list .product.d-none'),
      divLength = divProducts.length;

   for (let i = 0; i < divLength; i++) {
      if (i < PRODUCTS.toShow) {
         divProducts[i].classList.remove('d-none');
      } else {
         break;
      }
   }

   if (divLength < PRODUCTS.toShow) {
      // Less than 8 products, therefore deactivate more-items button
      showBtnMoreItems(false);
   }

}

export { showBtnMoreItems, showMoreItems };