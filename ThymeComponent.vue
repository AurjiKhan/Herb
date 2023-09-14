<template>
  <div class="thyme-page">
    <h1>Thyme</h1>
    <img src="@/assets/Thyme.png" alt="Thyme">
    <h2>Description</h2>
    <p>
      Thyme is a fragrant herb with small, greenish-gray leaves and a pleasant, earthy aroma. It is a versatile herb used in cooking and has medicinal properties. Thyme is native to the Mediterranean region and belongs to the mint family.
    </p>

    <h2>Uses</h2>
    <p>
      Thyme is commonly used as a culinary herb to flavor a variety of dishes, including soups, stews, and roasted meats. Medicinally, it has been used to treat respiratory conditions and coughs. Thyme oil is also used in aromatherapy for its calming and soothing effects.
    </p>

    <h2>Origin</h2>
    <p>
      Thyme has a long history of use in Mediterranean cuisine and traditional medicine. It has been cultivated and appreciated for its culinary and therapeutic benefits for centuries.
    </p>
  </div>
</template>

<script>
export default {
  name: 'ThymeComponent'
}
</script>

<style scoped>
.thyme-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  font-size: 32px;
  text-align: center;
  margin-bottom: 20px;
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
