<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">{{ name }}</h2>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="tabs is-centered is-fullwidth is-large">
            <ul>
                <li :class="{'is-active': step == 'name'}" @click="step = 'name'">
                    <a>Name</a>
                </li>
                <li :class="{'is-active': step == 'questions'}" @click="step = 'questions'">
                    <a>Questions</a>
                </li>
                <li :class="{'is-active': step == 'review'}" @click="step = 'review'">
                    <a>Review</a>
                </li>
            </ul>
        </div>
        <div class="columns">
          <div class="column is-half is-offset-one-quarter">

            <div class="name" v-show="step === 'name'">
              <div class="field">
                <label class="label  is-large" for="name">Survey name:</label>
                <div class="control">
                  <input type="text" class="input is-large" id="name" v-model="name">
                </div>
              </div>
            </div>

            <div class="questions" v-show="step === 'questions'">
              <new-question v-on:questionComplete="appendQuestion"/>
            </div>

            <div class="review" v-show="step === 'review'">
              <ul>
                <li class="question" v-for="(question, qIdx) in questions" :key="`question-${qIdx}`">
                  <div class="title">
                    {{ question.question }}
                    <span class="icon is-medium is-pulled-right delete-question"
                      @click.stop="removeQuestion(question)">
                      <i class="fa fa-times" aria-hidden="true"></i>
                    </span>
                  </div>
                  <ul>
                    <li v-for="(choice , cIdx) in question.choices" :key="`choice-${cIdx}`">
                      {{ cIdx + 1 }}. {{ choice }}
                    </li>
                  </ul>
                </li>
              </ul>

              <div class="control">
                <a class="button is-large is-primary" @click="submitSurvey">Submit</a>
              </div>

            </div>

          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import NewQuestion from '@/components/NewQuestion'

export default {
  components: { NewQuestion },
  data () {
    return {
      step: 'name',
      name: '',
      questions: []
    }
  },
  methods: {
    appendQuestion (newQuestion) {
      this.questions.push(newQuestion)
    },
    removeQuestion (question) {
      const idx = this.questions.findIndex(q => q.question === question.question)
      this.questions.splice(idx, 1)
    },
    submitSurvey () {
      this.$store.dispatch('submitNewSurvey', {
        name: this.name,
        questions: this.questions
      }).then(() => this.$router.push('/'))
    }
  }
}
</script>

<style>
.question {
  margin: 10px 20px 25px 10px;
}

.delete-question {
  cursor: pointer;
  padding: 10px;
}

.delete-question:hover {
  background-color: lightgray;
  border-radius: 50%;
}
</style>
