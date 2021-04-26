<template>
  <div id="animations">
      <b-button v-on:click="toggleEffect('rainbow')">Rainbow</b-button>
      <b-button v-on:click="toggleEffect('pulse')">Pulse</b-button>
      <b-button v-on:click="toggleEffect('heartbeat')">Heartbeat</b-button>
      <b-button v-on:click="toggleEffect('sparkle')">Sparkle</b-button>
      <b-button v-on:click="toggleEffect('knightrider')">Knightrider</b-button>
      <b-button v-on:click="toggleEffect('theatre')">Movie Theatre</b-button>
      <b-button v-on:click="toggleEffect('rainbow_theatre')">Rainbow Theatre</b-button>
  </div>
</template>

<script>
import { serverUrl } from './vars.js'

export default {
    name: 'Animations',
    data () {
        return {
            effect: 'static'
        }
    },
    methods: {
        toggleEffect(effect) {
            this.$axios
                .get(`${serverUrl}/add_animation/${effect}`)
                .then(response => (
                    console.log(response.data))
                )
                .finally(this.effect = effect)
        }
    }
}
</script>

<style scoped>

</style>