<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">{{ survey.name }}</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">

        <div class="columns">
          <div class="column is-10 is-offset-1">

            <div class="question">

                  <div class="column is-offset-3 is-6">
                    <h4 class='title'>{{ idx }}) {{ question.text }}</h4>
                  </div>
                  <div class="column is-offset-3 is-6">
                    <div class="control">
                      <div v-for="choice in question.choices" v-bind:key="choice.id">
                        <label class="radio">
                        <input type="radio" v-model="question.choice" :value="choice.id">
                        {{ choice.text }}
                      </label>
                      </div>
                    </div>
                  </div>

            </div>

            <div class="column has-text-centered">
              <a v-if="surveyComplete" class='button is-rounded' @click.stop="handleSubmit">Submit</a>
            </div>

            <div class="column is-offset-one-quarter is-half">
              <nav class="pagination is-centered" role="navigation" aria-label="pagination">
                <a class="pagination-previous" @click.stop="previous"><i class="fa fa-chevron-left" aria-hidden="true"></i> &nbsp;&nbsp; Back</a>
                <a class="pagination-next" @click.stop="next">Next &nbsp;&nbsp; <i class="fa fa-chevron-right" aria-hidden="true"></i></a>
                <ul class="pagination-list">
                  <li v-for="(q, idx) in questions" v-bind:key="q.id">
                    <a class="pagination-link" @click.stop="goTo(idx)" aria-label="Goto page 1">{{idx + 1}}</a>
                  </li>
                </ul>
              </nav>
            </div>

          </div>
        </div>

      </div>
    </section>
  </div>
</template>

<script>
  
</script>

<style>
  
</style>


