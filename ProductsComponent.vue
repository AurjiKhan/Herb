<template>
  <div class="product-item">
    <img :src="product.img" alt="Product image" class="product-image" />
    <div class="product-content">
      <div class="product-head">
        <h3 class="product-title">{{ product.name }}</h3>
        <span class="product-owner">By: {{ product.owner }}</span>
      </div>
      <div class="product-footer">
        <div class="product-price">
          <span>Price:</span>
          <span class="product-val">{{ product.val }}</span>
        </div>
        <div class="product-buttons">
          <button class="add-to-cart" @click="addToCart(product)">Add to Cart</button>
          <button class="remove" @click="removeFromCart(product)">Remove</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    product: Object,
  },
  methods: {
    addToCart(product) {
      this.$emit("add-to-cart", product);
    },
    removeFromCart(product) {
      this.$emit("remove-from-cart", product);
    },
  },
};
</script>

<style scoped>
/* Product item styles */
.product-item {
  display: flex;
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 20px;
  border-radius: 5px;
}

.product-image {
  max-width: 100px;
  height: auto;
  margin-right: 20px;
}

.product-content {
  flex: 1;
}

.product-title {
  font-size: 1.2rem;
  margin: 0;
  color: #333;
}

.product-owner {
  font-size: 0.9rem;
  color: #666;
}

.product-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}

.product-price {
  font-weight: bold;
  font-size: 1.1rem;
  color: #333;
}

.product-val {
  font-size: 1rem;
  color: #333;
}

.product-buttons {
  display: flex;
  gap: 10px;
}

.add-to-cart,
.remove {
  padding: 5px 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

.add-to-cart:hover,
.remove:hover {
  background-color: #0056b3;
}
</style>
