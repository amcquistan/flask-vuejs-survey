<!-- components/Header.vue -->
<template>
<nav class="navbar is-light" role="navigation" aria-label="main navigation">
  <div class="navbar-menu">
    <div class="navbar-start">
      <router-link to="/" class="navbar-item">
        Home
      </router-link>
      <router-link v-if="isAuthenticated" to="/surveys" class="navbar-item">
        Create Survey
      </router-link>
      <router-link v-if="!isAuthenticated" to="/login" class="navbar-item">
        Login / Register
      </router-link>
    </div>
  </div>
</nav>
</template>

<script>
export default {
  computed: {
    isAuthenticated () {
      return this.$store.getters.isAuthenticated
    }
  }
}
</script>

<style>

</style>
