<template>
  <div class="register-page">
    <div class="register-container">
      <h1>Register Page</h1>
      <form class="register-form" @submit.prevent="register">
        <div class="form-group">
          <input type="text" v-model="username" placeholder="Username" class="form-input" />
        </div>
        <div class="form-group">
          <input type="password" v-model="password" placeholder="Password" class="form-input" />
        </div>
        <button type="submit" class="register-button">Register</button>
      </form>
      <div>
        <p>Already have an account? <router-link to="/loginComponent">Login here</router-link></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegisterComponent',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async register() {
      const user = {
        username: this.username,
        password: this.password
      };

      try {
        const response = await fetch('http://localhost:8000/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(user),
        });

        if (response.ok) {
          // Registration successful, you can handle it as needed
          console.log('Registration successful');
          // Redirect to the login page or another route
          this.$router.push('/loginComponent');
        } else {
          // Registration failed, show an error message
          console.error('Registration failed');
        }
      } catch (error) {
        console.error('An error occurred:', error);
      }
    },
  },
};
</script>

<style scoped>
.register-page {
  background-image: url("@/assets/Lavender.png"); /* Add your background image path */
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Set the height to cover the entire viewport */
}

.register-container {
  max-width: 400px;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.8); /* Add a semi-transparent background color */
  border-radius: 10px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.register-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
  display: block;
}

input[type="text"],
input[type="password"] {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
}

.register-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

.register-button:hover {
  background-color: #0056b3;
}

/* Add additional styling to enhance the form's appearance */
</style>
