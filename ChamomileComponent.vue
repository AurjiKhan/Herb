<template>
  <div class="chamomile-page">
    <h1>Chamomile</h1>
    <img src="@/assets/Chamomile.png" alt="Chamomile">
    <h2>Description</h2>
    <p>
      Chamomile is a daisy-like herb with small, white flowers and a sweet, apple-like scent. It is known for its calming and soothing properties and is often used in herbal teas and aromatherapy. Chamomile is native to Europe and Asia and is part of the daisy family.
    </p>

    <h2>Uses</h2>
    <p>
      Chamomile has a wide range of uses, primarily as a natural remedy for relaxation and stress reduction. It is commonly consumed as a tea to aid with sleep and digestion. Chamomile oil is used in aromatherapy for its calming effects. Additionally, it can be applied topically to soothe skin irritations.
    </p>

    <h2>Origin</h2>
    <p>
      Chamomile has a rich history of traditional use in both European and Asian cultures. It has been cultivated and utilized for its therapeutic benefits for centuries.
    </p>
  </div>
</template>

<script>
export default {
  name: 'ChamomileComponent'
}
</script>

<style scoped>
.chamomile-page {
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
