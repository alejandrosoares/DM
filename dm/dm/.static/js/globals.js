/*
   GlOBAL VARIABLES
*/

const GLOBAL = {
   products: {
      list: null,
      set set_products(list) {
         this.list = list;
      },
      get get_products() {
         return this.list;
      }
   }
}


export { GLOBAL };