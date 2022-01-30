<template>
  <div class="mt-5">
    <h1>Home</h1>
    
    <div class="row">
      <div class="col">
        <input v-model="secure_data" type="text" class="form-control" placeholder="Enter Secure Data">
      </div>
    </div>
    <div class="row mt-3">
      <div class="col">
        <button class="btn btn-primary" @click="submit">Securely Submit</button>
      </div>
    </div>
    <div v-if="token">
      <div class="row mt-3">
        <div class="col">
          <div class="bg-light p-3">
            {{token}}
          </div>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col">
          <button class="btn btn-warning" @click="retrieve">Securely Retrieve</button>
        </div>
      </div>
    </div>

    <div class="row mt-3" v-if="secure_response">
      <div class="col">
        <div class="bg-light p-3">
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
