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
    <div v-if="response">
      <div class="row mt-3">
        <div class="col">
          <div class="bg-light p-3">
            {{response}}
          </div>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col">
          <button class="btn btn-secondary" @click="reset">Reset</button>
        </div>
      </div>
    </div>

    <ul class="mt-5">
      <li v-for="company in companies" :key="company.id">
        {{ company.name }}
      </li>
    </ul>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        secure_data: null
      }
    },

    methods: {
      async submit(event) {
        console.log(event);
        try {
          let resp = await axios.post(`${this.$config.apiUrl}/submit`, {
            data: this.secure_data
          });
          console.log(resp)
          this.response = resp.data
        }
        catch(error)
        {
          this.response = error;
        }
      },

      reset() {
        this.response = null
      }

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
