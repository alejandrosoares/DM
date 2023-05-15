const GLOBAL = {
   products: {
      searchList: null,
      list: null,
      setProducts: function(products) {
         this.list = products;
      },
      getProducts: function() {
         return this.list;
      },
      setSearchList: function(products) {
         this.searchList = products;
      },
      getSearchList: function() {
         return this.searchList;
      }
   },
}


export { GLOBAL };