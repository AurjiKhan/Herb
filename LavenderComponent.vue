<template>
  <div class="lavender-page">
    <h1>Lavender<span class="horizontal-bar"></span></h1>
    <img src="@/assets/Lavender.png" alt="Lavender Image">
    <h2>Description</h2>
    <p>
      Lavender is a fragrant herb known for its beautiful purple flowers and soothing aroma. It's commonly used in aromatherapy, herbal remedies, and as a culinary herb. Lavender is known for its calming and relaxing properties, making it a popular choice for essential oils, sachets, and teas.
    </p>

    <h2>Uses</h2>
    <p>
      In addition to its pleasant fragrance, Lavender has several potential health benefits, including stress relief, sleep improvement, and skincare properties. It's a versatile herb that can be used in various ways to promote well-being.
    </p>

    <h2>Origin</h2>
    <p>
      Lavender is native to the Mediterranean region but is now grown in various parts of the world. It has a long history of use in ancient civilizations and continues to be cherished for its many applications.
    </p>
  </div>
</template>

<script>
export default {
  name: 'LavenderComponent'
}
</script>

<style scoped>
.lavender-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background-color: #1e1e1e;
  color: #fff;
  text-align: center;
}

h1 {
  font-size: 32px;
  margin-bottom: 20px;
  position: relative;
}

.horizontal-bar {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
  background-color: dodgerblue;
}

h2 {
  font-size: 24px;
  margin-top: 20px;
}

p {
  font-size: 18px;
  line-height: 1.5;
  margin-bottom: 15px;
}
</style>
