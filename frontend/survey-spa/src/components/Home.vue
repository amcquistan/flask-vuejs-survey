<template>
<div>
  <section class="hero is-primary">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="title">Check out recent surveys</h2>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
<div class="card" v-for="survey in surveys" v-bind:key="survey.id">
  <div class="card-content">
    <p class="title">{{ survey.name}}</p>
    <p class='subtitle'>{{survey.created_at}}</p>
  </div>
  <div class="card-foooter">
    <router-link :to="`surveys/${survey.id}`" class="card-footer-item">Take Survey</router-link>
  </div>
</div>
    </div>
  </section>
</div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  computed: mapState({
    surveys: state => state.surveys
  }),
  beforeMount () {
    this.$store.dispatch('loadSurveys')
  }
}
</script>

<style>

</style>
