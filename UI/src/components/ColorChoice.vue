<template>
    <div id="color_choser">
      <b-container>
        <b-row>
          <ColorSquare color_val="#FF0000" style="margin:auto" :type="type" :red='255' :green='0' :blue='0'/>
          <ColorSquare color_val="#00FF00" style="margin:auto" :type="type" :red='0' :green='255' :blue='0'/>
          <ColorSquare color_val="#0000FF" style="margin:auto" :type="type" :red='0' :green='0' :blue='255'/>
          <ColorSquare color_val="#FFFF00" style="margin:auto" :type="type" :red='255' :green='255' :blue='0'/>
          <ColorSquare color_val="#FF8C00" style="margin:auto" :type="type" :red='255' :green='140' :blue='0'/>
          <ColorSquare color_val="#00FFFF" style="margin:auto" :type="type" :red='0' :green='255' :blue='255'/>
          <ColorSquare color_val="#9400D3" style="margin:auto" :type="type" :red='148' :green='0' :blue='211'/>
          <ColorSquare color_val="#FF00FF" style="margin:auto" :type="type" :red='255' :green='0' :blue='255'/>
          <ColorSquare color_val="#FFFFFF" style="margin:auto" :type="type" :red='255' :green='255' :blue='255'/>
        </b-row>
      </b-container>

    </div>
</template>

    <script>
        import ColorSquare from './ColorSquare.vue';

        export default {
            name: "BedroomLight",
            props: ['type'],
            components: {
                ColorSquare
            }
        }
    </script>
    <style scoped>

    </style>