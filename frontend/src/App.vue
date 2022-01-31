<template>
  <div>
    <Navbar></Navbar>
    <div class="container">
      <Home v-if="route == '/' || route == '/index.html' || !route" msg="Welcome to Your Vue.js App"/>
    </div>
  </div>
</template>

<script>
import Home from './components/Home.vue'
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Home,
    Navbar,
  },

  data() {
    return {
      route: window.location.pathname
    }
  },
}
</script>

<style>
</style>
