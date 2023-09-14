<template>
  <div>
    <h2>View Cart</h2>
    <CartData :cart="cart" @remove-from-cart="removeFromCart" />
  </div>
</template>

<script>
import CartData from "@/components/CartComponent.vue";

export default {
  name: 'ViewCart',
  components: {
    CartData
  },
  data() {
    return {
      cart: [] // Initialize the cart data
    };
  },
  methods: {
    removeFromCart(item) {
      // Handle the removal of items from the cart (same as in HomeComponent)
      const index = this.cart.findIndex((cartItem) => cartItem.id === item.id);

      if (index !== -1) {
        const cartItem = this.cart[index];
        if (cartItem.quantity > 1) {
          cartItem.quantity--;
        } else {
          this.cart.splice(index, 1);
        }
      }
    }
  }
};
</script>
