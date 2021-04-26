<template>
    <div id="power_switch">
        <b-button block variant="danger" size="lg" v-on:click="togglePower()">
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-power" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M5.578 4.437a5 5 0 1 0 4.922.044l.5-.866a6 6 0 1 1-5.908-.053l.486.875z"/>
                <path fill-rule="evenodd" d="M7.5 8V1h1v7h-1z"/>
            </svg>
            Power
        </b-button>
    </div>
</template>

<script>
import { serverUrl } from './vars.js'

export default {
    name: 'PowerSwitch',
    data () {
        return {
            power: 'off'
        }
    },
    methods: {
        togglePower() {
            if (this.power == 'off') {
                this.power = 'on'
            } else {
                this.power = 'off'
            }
            this.$axios
                .get(`${serverUrl}/start_app`)
                .then(response => (
                    console.log(response.data)
                ))
        }
    }
}
</script>

<style scoped>

</style>
