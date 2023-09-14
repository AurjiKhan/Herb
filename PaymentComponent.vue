<template>
  <div class="payment-form">
    <h2>Payment Details</h2>
    <form @submit.prevent="submitPayment">

      <div class="form-group">
        <input v-model="paymentInfo.first_name" type="text" placeholder="First Name" class="form-input" />
      </div>
      <div class="form-group">
        <input v-model="paymentInfo.last_name" type="text" placeholder="Last Name" class="form-input" />
      </div>
      <div class="form-group">
        <input v-model="paymentInfo.company_name" type="text" placeholder="Company Name (optional)" class="form-input" />
      </div>
      <div class="form-group">
        <input v-model="paymentInfo.address" type="text" placeholder="Address" class="form-input" />
      </div>
      <div class="form-group">
        <input v-model="paymentInfo.city" type="text" placeholder="City" class="form-input" />
      </div>
      <div class="form-group">
        <input v-model="paymentInfo.postal_code" type="text" placeholder="Postal Code" class="form-input" />
      </div>
      <div class="form-group">
        <input v-model="paymentInfo.phone" type="text" placeholder="Phone" class="form-input" />
      </div>
      <button type="submit" class="pay-button" @click="submitPayment">Pay</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {

  name: 'PaymentComponent',
  data() {
    return {
      paymentInfo: {
        first_name: '',
        last_name: '',
        company_name: '',
        address: '',
        city: '',
        postal_code: '',
        phone: '',
      },
    };
  },
  methods: {

   async submitPayment() {
    try {
      await axios.post('/payment', this.paymentInfo);
      // Handle the response as needed
    } catch (error) {
      // Handle errors, e.g., display an error message
      console.error('Error submitting payment:', error);
    }
    },
  },
};
</script>

<style scoped>
.payment-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
}

h2 {
  font-size: 24px;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.pay-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 18px;
  cursor: pointer;
}

.pay-button:hover {
  background-color: #0056b3;
}
</style>
