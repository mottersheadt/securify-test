<template>
  <div class="mt-5">
    <div class="row">
      <div class="col">
        <h1>Store Data</h1>
        <p>Enter a value in the field below and press "Securely Store" to store as sensitive data and retrieve a reference token.</p>
        <input v-model="secure_data" type="text" class="form-control mb-3" placeholder="Enter Secure Data">
        <button class="btn btn-primary" @click="submit">Securely Submit</button>
        <div v-if="token">
          <div class="bg-light p-3">
            Reference token: {{token}}
          </div>
        </div>
      </div>
      
      <div class="col">
        <h1>Retrieve Data</h1>
        <p>Enter a reference token in the field below and press "Securely Retrieve" to retrieve sensitive data.</p>
        <input v-model="retrieve_token" type="text" class="form-control mb-3" placeholder="Enter Secure Data">
        
        <button class="btn btn-warning mb-3" @click="retrieve">Securely Retrieve</button>
        <div v-if="secure_response" class="bg-light p-3">
          {{secure_response}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        secure_data: null,
        token: null,
        secure_response: null
      }
    },

    methods: {
      async submit(event) {
        console.log(event);
        try {
          let resp = await axios.post(`${this.$config.secureApiUrl}/submit`, {
            secret_data: this.secure_data
          });
          this.token = resp.data
        }
        catch(error)
        {
          this.token = error;
        }
      },

      async retrieve() {
        try {
          console.log(this.token)
          let resp = await axios.get(`${this.$config.apiUrl}/retrieve?token=${this.token}`);
          this.secure_response = resp.data
        }
        catch(error)
        {
          this.secure_response = error;
        }
      }

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
