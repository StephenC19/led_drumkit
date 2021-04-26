<template>
  <div id="app">
    <div id="header" style="font-weight:bold;font-size:45px;" class="p-3">DRUM LED CONTROL</div>
    <drum-color-control/>
  </div>
</template>

<script>
import DrumColorControl from './components/DrumColorControl.vue'

export default {
  name: 'App',
  components: {
    DrumColorControl
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0px;
  background-color: #181933;
}
#header {
  background-image: radial-gradient(rgb(17, 83, 5), black);
  font-family: Avenir;
  color:white;
  letter-spacing: 7px;
}
</style>
