<template>
  <div class="drum_control">
    <b-container class="mt-4">
      <b-row class="mb-3">
        <b-col cols="4"><h1>Pad Color:</h1></b-col>
        <b-col><color-choice type="pad"/></b-col>
      </b-row>
      <b-row class="mb-3">
        <b-col cols="4"><h1>Snare Color:</h1></b-col>
        <b-col><color-choice type="snare"/></b-col>
      </b-row>
      <b-row class="mb-3">
        <b-col cols="4"><h1>Cymbal Color:</h1></b-col>
        <b-col><color-choice type="cymbal"/></b-col>
      </b-row>
      <b-row class="mb-3">
        <b-col cols="4"><h1>Kick Color:</h1></b-col>
        <b-col><color-choice type="kick"/></b-col>
      </b-row>
      <b-row class="mb-3">
        <b-col cols="4"><h1>Accent 1 Color:</h1></b-col>
        <b-col><color-choice type="accent_hit_1"/></b-col>
      </b-row>
      <b-row class="mb-3">
        <b-col cols="4"><h1>Accent 2 Color:</h1></b-col>
        <b-col><color-choice type="accent_hit_2"/></b-col>
      </b-row>
    </b-container>
    <Power/>
    <br/>
    <Animations/>
    <!-- <color-picker/> -->
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
  </div>
</template>

<script>
import ColorChoice from './ColorChoice.vue'
import Animations from './Animations.vue'
import Power from './Power'
// import ColorPicker from './ColorPicker.vue';

export default {
  components: {
    ColorChoice,
    // ColorPicker,
    Animations,
    Power
  },
  name: 'DrumControl',
  props: {
    msg: String
  },
  methods: {
    togglePower() {
      this.$axios
          .get("http://192.168.0.79:5000/start_app")
          .then(response => (
            console.log(response.data)
          ))
        }
    }
}
</script>

<style scoped>
  h1 {
    color: white;
    text-align: right;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }

  #thing {
    margin: 10px;
  }
</style>
