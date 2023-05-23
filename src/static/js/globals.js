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
   pagination: {
      pagination: null,
      setPagination: function(pagination) {
         this.list = pagination;
      },
      getPagination: function() {
         return this.pagination;
      }
   }
}


export { GLOBAL };