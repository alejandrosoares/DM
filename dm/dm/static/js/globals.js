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