<template>
<md-card>
      <md-card-media>
        <img src="@/assets/bangle-leaf.jpg" alt="People">
      </md-card-media>

      <md-card-header>
        <div class="md-title">{{title}}</div>
        <div class="md-subhead">{{subtitle}}</div>
      </md-card-header>

      <md-card-expand>
        <md-card-actions md-alignment="space-between">
          <div>
            
            <md-button class="md-raised md-primary">Go to application</md-button>
          </div>

          <md-card-expand-trigger>
            <md-button class="md-icon-button">
              <md-icon>keyboard_arrow_down</md-icon>
            </md-button>
          </md-card-expand-trigger>
        </md-card-actions>

        <md-card-expand-content>
          <md-card-content>
            {{text}}
            <br><br>
            <div id="contain" v-for="index in labels" :key="index">
            <chip :label="index"/>
            
            </div>
          </md-card-content>
          
        </md-card-expand-content>
        
      </md-card-expand>
    </md-card> 
</template>

<style scoped>
  .md-app {
    max-height: 400px;
    border: 1px solid rgba(#000, .12);
  }


  .md-drawer {
    width: 230px;
    max-width: calc(100vw - 125px);
  }
   #add{
    position: absolute;
    right: 1rem;
    bottom: 1rem;
  }
 .md-content{
   height: 100vh;

 }
 #app{
   height: 100vh;
      overflow-x: hidden;
  overflow-y: auto;
  
 }

  .md-card {
    width: 320px;
    margin: 4px;
    display: inline-block;
    vertical-align: top;
  }
  #contain{
    display: inline-block;
  }
</style>

<script>

import Chip from '../components/Chip'

export default {
  components: {
    'chip': Chip,
  },
  name: 'card',
  props:{
    UUID: String,
    title: String,
    subtitle:String,
    text: String,
    IMG_URL: String,
    labels: Array,
    contact: String,
  }
}
//UUID, Title, Subtitle, Text, IMG_URL, Labels, Contact, Start, Finish, Hours, Slots
</script>