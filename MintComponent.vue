<template>
  <div class="mint-page">
    <h1>Mint</h1>
    <img src="@/assets/Mint.png" alt="mint">
    <h2>Description</h2>
    <p>
      Mint is a fragrant herb known for its refreshing and cooling properties. It has bright green leaves with a distinct, invigorating aroma. Mint is widely used in culinary dishes, beverages, and herbal remedies. It's characterized by its crisp and slightly spicy flavor.
    </p>

    <h2>Uses</h2>
    <p>
      Mint has a variety of uses, including as a flavoring agent in teas, candies, and cocktails. It is also used to soothe digestive discomfort and can be beneficial for promoting fresh breath. Additionally, mint is a popular choice for garnishing and enhancing the flavor of various dishes.
    </p>

    <h2>Origin</h2>
    <p>
      Mint is native to Europe and Asia but is now grown in many parts of the world. It has a long history of cultivation and has been used for centuries in traditional medicine and culinary applications.
    </p>
  </div>
</template>

<script>
export default {
  name: 'MintComponent'
}
</script>

<style scoped>
.mint-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: black;
}

h1 {
  font-size: 32px;
  text-align: center;
  margin-bottom: 20px;
  color:white;
}

h2 {
  font-size: 24px;
  margin-top: 20px;
  color:white;
}

p {
  font-size: 18px;
  line-height: 1.5;
  margin-bottom: 15px;
  color:white;
}
</style>
