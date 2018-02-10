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

            <div
              v-for="(question, idx) in survey.questions"
              v-bind:key="question.id"
              v-show="currentQuestion === idx">

                  <div class="column is-offset-3 is-6">
                    <!-- <h4 class='title'>{{ idx }}) {{ question.text }}</h4> -->
                    <h4 class='title has-text-centered'>{{ question.text }}</h4>
                  </div>
                  <div class="column is-offset-4 is-4">
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

            <div class="column is-offset-one-quarter is-half">
              <nav class="pagination is-centered" role="navigation" aria-label="pagination">
                <a class="pagination-previous" @click.stop="goToPreviousQuestion"><i class="fa fa-chevron-left" aria-hidden="true"></i> &nbsp;&nbsp; Back</a>
                <a class="pagination-next" @click.stop="goToNextQuestion">Next &nbsp;&nbsp; <i class="fa fa-chevron-right" aria-hidden="true"></i></a>
              </nav>
            </div>

            <div class="has-text-centered">
              <a v-show="surveyComplete" class='button is-large is-focused is-primary' @click="handleSubmit">Submit</a>
            </div>

          </div>
        </div>

      </div>
    </section>
  </div>
</template>

<script>
import { fetchSurvey, saveSurveyResponse } from '@/api'
export default {
  data () {
    return {
      survey: {},
      currentQuestion: 0
    }
  },
  beforeMount () {
    return fetchSurvey(parseInt(this.$route.params.id))
      .then((response) => {
        this.survey = response
      })
  },
  methods: {
    goToNextQuestion () {
      if (this.currentQuestion === this.survey.questions.length - 1) {
        this.currentQuestion = 0
      } else {
        this.currentQuestion++
      }
    },
    goToPreviousQuestion () {
      if (this.currentQuestion === 0) {
        this.currentQuestion = this.survey.questions.lenth - 1
      } else {
        this.currentQuestion--
      }
    },
    handleSubmit () {
      saveSurveyResponse(this.survey)
        .then(() => this.$router.push('/'))
    }
  },
  computed: {
    surveyComplete () {
      if (this.survey.questions) {
        const numQuestions = this.survey.questions.length
        const numCompleted = this.survey.questions.filter(q => q.choice).length
        return numQuestions === numCompleted
      }
      return false
    }
  }
}
</script>

<style>
</style>
