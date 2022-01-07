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
      set setProducts(list) {
         this.list = list;
      },
      get getProducts() {
         return this.list;
      },
      set setSearchList(list) {
         this.searchList = list;
      },
      get getSearchList() {
         return this.searchList;
      }
   }
}


export { GLOBAL };