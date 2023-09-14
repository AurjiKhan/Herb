<template>
<div>
    <div class="header">
      <!-- Navigation Bar -->
      <div class="navbar">
        <div class="logo-container">
          <img src="@/assets/logo.png" alt="logo" class="logo-image">
        </div>


        <div class="top-links">
          <router-link to="/loginComponent" class="btn">Login</router-link>
          <router-link to="/SignComponent" class="btn">SignUp</router-link>
          <router-link to="/cart" class="btn">View Cart</router-link>
        </div>
      </div>
      <h1>Welcome To Herb Store</h1>
      <div class="herb-links">
        <router-link to="/BasilComponent" class="btn">Basil</router-link>
        <router-link to="/ThymeComponent" class="btn">Thyme</router-link>
        <router-link to="/ChamomileComponent" class="btn">Chamomile</router-link>
        <router-link to="/MintComponent" class="btn">Mint</router-link>
        <router-link to="/LavenderComponent" class="btn">Lavender</router-link>
      </div>
    </div>
   <section class="image-slider">
      <!-- Image Slider -->
      <div class="slider-container">
        <div
          v-for="product in visibleImages"
          :key="product.id"
          class="herb-image"
          @mouseover="setHoveredProduct(product)"
          @mouseleave="clearHoveredProduct()"
        >
          <img :src="product.img" :alt="product.name" />
          <p>{{ product.name }}</p>
          <button
            v-show="hoveredProduct === product"
            @click="addToCart(product)"
            class="add-to-cart-button"
          >
            Add to Cart
          </button>
        </div>
      </div>
      <div class="prev" @click="scrollPrev">&#10094; Previous</div>
      <div class="next" @click="scrollNext">Next &#10095;</div>
    </section>

    <section class="h1">

    <div class="img1" >
      <h1>Detail About Our Store</h1>
      <img src="@/assets/herbstore.png" alt="il">

      <p>A herb store is a specialized retail establishment that focuses on the sale of a wide variety of herbs, both culinary and medicinal, as well as herbal products and remedies.
        These stores often stock fresh and dried herbs, herbal teas, essential oils, tinctures, capsules, and other herbal supplements.
        Herb stores cater to a diverse clientele, including chefs seeking fresh, high-quality ingredients, individuals interested in natural remedies and alternative medicine, and those looking to explore the aromatic and therapeutic aspects of herbs.
        Many herb stores prioritize organic and sustainably sourced products, and they may also offer expert advice on herb selection, usage, and preparation, making them valuable resources for those interested in incorporating herbs into their daily lives for culinary or health-related purposes.

</p>
      <h1>Why Our Store!</h1>
      <p>People choose our online herb store for a multitude of compelling reasons.
        Firstly, we offer a vast and diverse selection of high-quality herbs, sourced from reputable growers and suppliers worldwide, ensuring freshness and potency.
        Our commitment to sustainability and organic practices resonates with environmentally conscious customers. The convenience of online shopping, coupled with our user-friendly interface and secure payment options, provides a seamless and hassle-free experience.</p>
    </div>
    <div class="img2">
      <h1>Medical Benefits of Herbs</h1>
      <img src="@/assets/medical.png" alt="il">
      <p>Herbs offer a multitude of medical benefits,
        ranging from their natural anti-inflammatory and antioxidant properties to their potential to support various bodily systems.
        Many herbs, such as turmeric and ginger, possess anti-inflammatory effects that can alleviate conditions like arthritis.
        Additionally, herbs like garlic and echinacea are known for their immune-boosting capabilities, aiding the body in warding off infections.
        Moreover, the calming qualities of herbs like chamomile and lavender can promote relaxation and better sleep.
        Herbal remedies have been used for centuries in traditional medicine systems worldwide, offering a holistic approach to health and well-being.

</p>
    </div>
      </section>
  <section>
    <div>
      <div>
        <h1>Here's Our New Arrival of Herbs</h1>
        <div>
          <p>Discover the latest arrivals at our herb store, where nature's bounty meets your well-being needs. Our shelves are now adorned with a vibrant assortment of fresh herbs and botanical treasures harvested from around the world. From fragrant basil and soothing chamomile to exotic spices and medicinal herbs, our new inventory caters to all your culinary and holistic desires. Whether you're a passionate cook seeking to elevate your dishes or an herbal enthusiast in pursuit of natural remedies, these fresh arrivals promise an aromatic and therapeutic journey. With a commitment to quality and sustainability, we ensure that every herb is sourced with care, allowing you to savor the essence of nature in its purest form. Visit our store today to explore these delightful additions and infuse your life with the goodness of herbs.</p>
        </div>
        <div>
          <img src="@/assets/img1.jpg" alt="img1">
          <img src="@/assets/img2.jpg" alt="img1">
          <img src="@/assets/img3.jpg" alt="img1">
          <img src="@/assets/img4.jpg" alt="img1">

        </div>
      </div>
    </div>
  </section>





    <section class="h2">
    <h1>BUY NOW!</h1>
<Product
    v-for="product in products"
    :key="product.id"
    :product="product"
    @add-to-cart="addToCart"
    @remove-from-cart="removeFromCart"/>

  <CartData :cart="cart" @remove-from-cart="removeFromCart" />

    <!-- Confirmation Message -->
    <div class="confirmation-popup" v-if="showConfirmation">
      <div class="confirmation-content">
        {{ confirmationMessage }}
      </div>
    </div>
</section>






  </div>
</template>

<script>


import Product from "@/components/ProductsComponent.vue";
import CartData from "@/components/CartComponent.vue";
export default {
  name: 'HomeComponent',
  components:{
    Product,
    CartData,

  },
  data() {
    return {
      products: [
          {id:1,name:"Basil",val:"1",owner:"Hakeem Luqman",img:require("@/assets/Basil.png")},
          {id:2,name:"Thyme",val:"3",owner:"Hakeem Luqman",img:require("@/assets/Thyme.png")},
          {id:3,name:"Mint",val:"4",owner:"Hakeem Luqman",img:require("@/assets/Mint.png")},
          {id:4,name:"Chamomile",val:"6",owner:"Hakeem Luqman",img:require("@/assets/Chamomile.png")},
          {id:5,name:"Lavender",val:"10",owner:"Hakeem Luqman",img:require("@/assets/Lavender.png")}
      ],
      cart: [],
      showConfirmation: false,
      confirmationMessage: '',
      hoveredProduct: null,
      visibleImages: [],
      firstVisibleIndex: 0,
    };
  },
  methods: {
    addToCart(product) {
      // Check if the product is already in the cart
      const existingProduct = this.cart.find((item) => item.id === product.id);

      if (existingProduct) {
        // If it exists, increase the quantity
        existingProduct.quantity++;
      } else {
        // If it doesn't exist, add it to the cart
        this.cart.push({
          id: product.id,
          name: product.name,
          val: product.val,
          quantity: 1,
        });
      }

      // Set the confirmation message
      this.confirmationMessage = `${product.name} added to cart.`;

      // Show the confirmation message
      this.showConfirmation = true;

      setTimeout(() => {
        this.showConfirmation = false;
      }, 3000);
      // Emit the cart-updated event to notify the parent (HomeRootComponent)
      this.$emit("cart-updated", this.cart);
    },
    removeFromCart(item) {
      const index = this.cart.findIndex((cartItem) => cartItem.id === item.id);

      if (index !== -1) {
        const cartItem = this.cart[index];
        if (cartItem.quantity > 1) {
          cartItem.quantity--;
        } else {
          this.cart.splice(index, 1);
        }
      }

      // Emit the cart-updated event to notify the parent (HomeRootComponent)
      this.$emit("cart-updated", this.cart);
    },
    setHoveredProduct(product) {
      this.hoveredProduct = product;
    },
    clearHoveredProduct() {
      this.hoveredProduct = null;
    },


    updateVisibleImages() {
      const lastVisibleIndex = this.firstVisibleIndex + 2;
      this.visibleImages = this.products.slice(
        this.firstVisibleIndex,
        lastVisibleIndex + 1
      );
    },
    scrollNext() {
      if (this.firstVisibleIndex + 3 < this.products.length) {
        this.firstVisibleIndex += 3;
        this.updateVisibleImages();
      }
    },
    scrollPrev() {
      if (this.firstVisibleIndex >= 3) {
        this.firstVisibleIndex -= 3;
        this.updateVisibleImages();
      }
    },

  },
 created() {
    this.updateVisibleImages();
  },
};
</script>



<style scoped>
.add-to-cart-button {
  position: absolute;
  bottom: 10px; /* Adjust the position as needed */
  left: 50%;
  transform: translateX(-50%);
  padding: 5px 10px;
  background-color: darkgreen;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  opacity: 0; /* Initially hidden */
  transition: opacity 0.3s ease-in-out;
}
.header {
    text-align: center;
    padding: 10px;
    background-color: #d5d3c6;
    color: white;
  }
 .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
.confirmation-popup {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
  z-index: 1000; /* Ensure it's on top of other elements */
  justify-content: center;
  align-items: center;
  display: flex;
}

.confirmation-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
}
.logo-container {
margin-right: 20px;
}

.logo-image {
  max-width: 200px;
  background-color: transparent;
}



.top-links {
  display: flex;

}

.top-links .btn {
   margin-left: 10px;
    padding: 10px 20px;
    background-color: black;
    color: #fff;
    text-decoration: none;
    border-radius: 5px;
    transition: background-color 0.3s ease-in-out;
}

h1 {
  text-align: center;
  margin: 0;
  color:#333;
}



.herb-links .btn {
  flex: 0 0 calc(20% - 10px);
}

.btn {
  padding: 10px 20px;
  background-color: black;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease-in-out;
}

.btn:hover {
  background-color: darkgreen;

}





 .herb-links {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;/* Allow items to wrap to the next row if they don't fit */
}

.herb-links .btn {
  margin: 5px;
}

.herb-links .btn {
  flex: 0 0 calc(20% - 10px);
}


  .top-links .btn:hover {
    background-color: darkgreen;
  }



.h1{
  width: 99%;
    height: 49.5vw;
    position: relative;
    top: 0;
    left: 0;
    z-index: 4;
    margin-top: 0.5vw;
    margin-left: 0.5vw;
    margin-right: 0.5vw;
}


.herb-image {
  flex: 0 0 calc(20% - 10px); /* 20% width with 10px margin */
  text-align: center;
  margin: 10px;
}

.herb-image img {
  max-width: 100px;
  max-height: 100px;
  margin-bottom: 5px;
}
.img1{
      float: left;
    width: 49.75%;
    height: 49vw;
    margin-left: 0;
    margin-right: .25%;
    margin-top: 0;
    margin-right: 0;
    -ms-flex-pack: center;
    justify-content: center;
    opacity: 1;

    box-shadow: 5px 5px 8px -6px rgba(144,143,145,.65);
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    background-position: bottom;
    background-repeat: no-repeat;
    background-size: cover;
}
/* Style for carousel navigation arrows */
.img2{
      float: right;
    width: 50%;
    height: 49vw;
    margin-right: 0;
    margin-left: .25%;
    margin-top: 0;
    margin-left: 0;
    -ms-flex-pack: center;
    justify-content: center;
    opacity: 1;
    box-shadow: 5px 5px 8px -6px rgba(144,143,145,.65);
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    background-position: bottom;
    background-repeat: no-repeat;
    background-size: cover;
}
.h2{
  width: 99%;
    height: 24.5vw;
    position: relative;
    top: 0;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    z-index: 4;
    margin-left: .5%;
}
.image-slider {
            text-align: center;
            padding: 20px;
            position: relative; /* To position buttons */
        }

 .slider-container img {
            max-width: 50%; /* Decrease the image size */
            margin: 0 10px; /* Adjust the margin as needed */
            transition: transform 0.3s ease-in-out;
        }

.herb-image {
  flex: 0 0 calc(33.33% - 10px); /* Three images per row with margin */
  text-align: center;
  margin: 10px;
  display: inline-block;
}

.herb-image img {
  max-width: 100px;
  max-height: 100px;
  margin-bottom: 5px;

}

 .prev, .next {
            background-color: #333;
            color: white;
            padding: 10px;
            cursor: pointer;
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
        }
.prev {
            left: 0;
        }

        .next {
            right: 0;
        }
        .herb-image-container {
  position: relative;
  display: inline-block;
  margin: 10px; /* Adjust the margin as needed */
}
        .herb-image-container:hover .add-to-cart-button {
  opacity: 1;
}
</style>
