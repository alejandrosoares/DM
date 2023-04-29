/*
   GlOBAL VARIABLES

   GLOBAL: global object with others objects to share state between sections

   -products.searchList: is a list with all products used in the search,
      when loaded it is no longer modified 
*/

const GLOBAL = {
   products: {
      searchList: null,
      list: null,
      set setProducts(obj) {
         this.list = obj.products;
      },
      get getProducts() {
         return this.list;
      },
      set setSearchList(obj) {
         this.searchList = obj.products;
      },
      get getSearchList() {
         return this.searchList;
      }
   }
}


export { GLOBAL };