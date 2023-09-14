// store/index.js

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    cart: []
  },
  mutations: {
    addToCart(state, product) {
      const existingProduct = state.cart.find((item) => item.id === product.id);

      if (existingProduct) {
        existingProduct.quantity++;
      } else {
        state.cart.push({
          id: product.id,
          name: product.name,
          val: product.val,
          quantity: 1,
        });
      }
    },
    removeFromCart(state, item) {
      const index = state.cart.findIndex((cartItem) => cartItem.id === item.id);

      if (index !== -1) {
        const cartItem = state.cart[index];
        if (cartItem.quantity > 1) {
          cartItem.quantity--;
        } else {
          state.cart.splice(index, 1);
        }
      }
    }
  },
  actions: {
    // Optionally, you can define actions to perform async operations
  }
})
