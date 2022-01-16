import { GLOBAL } from "./globals.js";

const PRODUCTS = GLOBAL.products;

const URL = document.querySelector(
   "#products .products-info .url-products-json-all"
).value;

function requestProduct(loadSerchList, callback) {

   fetch(URL)
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