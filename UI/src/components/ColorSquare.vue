<template>
<div id="color" v-on:click="changeColor();toggleShow()">
    <div :style="filterStyle" :class="{ black_border: show }">
        <div id="square" :style="color"></div>
    </div>
</div>
</template>

<script>
import { serverUrl } from './vars.js'

export default {
  name: 'ColorSquare',
  props: ['color_val', 'type', 'red', 'green', 'blue'],
  methods: {
      toggleShow() {
          this.show = !this.show
      },
      changeColor() {
        const url = `${serverUrl}/change_color?color_type=${this.type}&red=${this.red}&green=${this.green}&blue=${this.blue}`
        console.log(url)
        this.$axios
          .get(`${url}`)
          .then(response => (console.log(response.data)))
      }
  },
  data() {
    return {
      show: false,
      color:{
        backgroundColor:this.color_val
      },
      shad:{
          filter: `drop-shadow(0px 0px 30px ${this.color_val})`
      }
    }
  },
  computed: {
    filterStyle() {
        if (this.show) {
        return {
            filter: `drop-shadow(0px 0px 30px ${this.color_val})`
        };
        } else {
        return '';
        }
    }
  }
}
</script>

<style scoped>
#square {
    /* background-color:rgb(0, 26, 255); */
    height:50px;
    width:50px;
    border-style: solid;
    border-color:rgba(0, 0, 0, 0.322);
    /* filter: drop-shadow(0px 0px 30px color_val); */
}

.black_border {
    border-style: solid;
    border-color:rgb(255, 255, 255);
}
</style>