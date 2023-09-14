<template>
  <div class="cart">
    <h2 class="cart-title">Cart</h2>
    <div v-if="cart.length === 0" class="empty-cart">
      Your cart is empty.
    </div>
    <div v-else>
      <div v-for="item in cart" :key="item.id" class="cart-item">
        <div class="cart-item-details">
          <div class="item-name">{{ item.name }}</div>
          <div class="item-price">Price: {{ item.val }}</div>
          <div class="item-quantity">Quantity: {{ item.quantity }}</div>
        </div>
        <div class="item-actions">
          <button @click="removeFromCart(item)" class="remove-button">Remove</button>
        </div>
      </div>
      <div class="cart-total">
        Total: {{ calculateTotal() }}
      </div>
    </div>
    <button @click="checkout" class="checkout-button">Checkout</button>
  </div>
</template>

<script>
export default {
  props: {
    cart: Array,
  },
  methods: {
    removeFromCart(item) {
      // Emit the "remove-from-cart" event with the item
      this.$emit("remove-from-cart", item);
    },
    calculateTotal() {
      // Calculate the total cost of items in the cart
      return this.cart.reduce((total, item) => total + item.val * item.quantity, 0);
    },
    checkout() {
      // Assuming you're using Vue Router for navigation
      this.$router.push({ name: 'PaymentComponent' }); // Replace 'payment' with your payment page route name
    },
  },
};
</script>

<style scoped>
/* Cart styles */
.cart {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 5px;
}

.cart-title {
  font-size: 1.5rem;
  margin: 0;
  color: #333;
}

.empty-cart {
  font-size: 1.2rem;
  color: #666;
}

/* Cart item styles */
.cart-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ddd;
  padding: 10px 0;
  margin-bottom: 10px;
}

.cart-item-details {
  flex: 1;
}

.item-name {
  font-size: 1.2rem;
  font-weight: bold;
  color: #333;
}

.item-price,
.item-quantity {
  font-size: 1rem;
  color: #666;
}

.item-actions {
  margin-left: 20px;
}

.remove-button {
  padding: 5px 10px;
  background-color: #ff3d00;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}
.checkout-button{
  padding: 5px 10px;
  background-color: green;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}
.remove-button:hover {
  background-color: #d73000;
}

/* Cart total styles */
.cart-total {
  text-align: right;
  font-size: 1.2rem;
  font-weight: bold;
  margin-top: 20px;
  color: #333;
}
</style>
