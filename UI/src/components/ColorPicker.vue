<template>
    <div id="color_picker">
        <div style="background:green;margin:auto;width:85%;font-size:25px;" v-on:click="togglePicker()">Color Picker</div>
        <v-color-picker
            dot-size="37"
            swatches-max-height="100"
            dark
            v-bind:style='{"display" : (isActive? "none" : "" )}'
            style="margin:auto"
        ></v-color-picker>
    </div>
</template>

<script>
export default {
    name: 'ColorPicker',
    data () {
        return {
            isActive: true
        }
    },
    methods: {
        togglePicker() {
            this.isActive = !this.isActive
        }
    }
}
</script>

<style scoped>

</style>