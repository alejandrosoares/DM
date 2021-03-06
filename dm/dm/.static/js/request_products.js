import { GLOBAL } from "./globals.js";

const PRODUCTS = GLOBAL.products;

const URL = document.querySelector(
   "#products .products-info .url-products-json-all"
).value;

function requestProduct(url, callback, loadSerchList = false) {
   /* Request Products
   @param: url or null, bool, function
   loadSerchList: is true, then load products in GLOBAL.products.searchList
   url: if this is null, the url base is taken
   */
   if (!url) {
      // url base is taken
      url = URL;
   }

   fetch(url)
      .then(response => {
         if (response.ok) return response.json()
      })
      .then(response => {

         const obj = {
            products: response.products
         };

         if (loadSerchList) {
            PRODUCTS.setSearchList = obj;
         }

         PRODUCTS.setProducts = obj;

         callback(PRODUCTS.getProducts);

      })
      .catch(error => console.error(error));
}


export default requestProduct;