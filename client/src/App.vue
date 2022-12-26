<template>
  <div id="app">
    <nav-drawer></nav-drawer>
    <router-view/>
  </div>
</template>

<script>
import NavDrawer from "./components/NavDrawer.vue";

export default {
  name: 'App',
  components: {
        'nav-drawer': NavDrawer
  }
}
</script>


<style>
#app {
  margin-top: 60px
}
</style>
