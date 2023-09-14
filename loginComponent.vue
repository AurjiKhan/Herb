<template>
  <div class="login-page">
  <div class="login-container">
    <div class="logo">
      <img src="@/assets/login1.png" alt="login1" class="logo-image">
    </div>

    <form class="login-form" @submit.prevent="login">
      <div class="form-group">
        <input type="text" v-model="username" placeholder="Username" class="form-input" />
      </div>
      <div class="form-group">
        <input type="password" v-model="password" placeholder="Password" class="form-input" />
      </div>
      <button type="submit" class="login-button">Login</button>
    </form>
    <div>
      <p>Don't have an account? <router-link to="/SignComponent">Register here</router-link></p>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginComponent',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async login() {
      const user = {
        username: this.username,
        password: this.password
      };

      try {
        const response = await fetch('http://localhost:8000/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(user),
        });

        if (response.ok) {
          const responseData = await response.json();
          const token = responseData.access_token;

          // Store the token in localStorage
          localStorage.setItem('token', token);

          // Redirect to the main page or another route
          this.$router.push('/');
        } else {
          // Authentication failed, show an error message
          console.error('Authentication failed');
          window.alert('Username or password is incorrect. Please try again.'); // Show an alert
        }
      } catch (error) {
        console.error('An error occurred:', error);
      }
    },
  },
};
</script>

<style scoped>
.login-page{
  background-image: url("@/assets/Thyme.png"); /* Add your background image path */
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.login-container {
  max-width: 400px;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.8); /* Add a semi-transparent background color */
  border-radius: 10px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
  text-align: center; /* Position the image at the top */
}

.logo {
  margin-bottom: 20px; /* Add margin below the image */
}

.logo-image {
  width: 200px; /* Adjust the width as needed */
  height: auto; /* Automatically adjust the height to maintain aspect ratio */
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
  color: black;
}

p {
  color: black;
}

.login-form {
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
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

.login-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 18px;
  cursor: pointer;
}

.login-button:hover {
  background-color: #0056b3;
}
</style>
