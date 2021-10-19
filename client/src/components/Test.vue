<template>
  <div class="page-container">
    <md-app style="min-height: 100vh;" md-mode="reveal">
      <md-app-toolbar class="md-primary">
      
        <span class="md-title">N_E_W</span>
        
       <div class="md-toolbar-section-end">
        <md-button class="md-icon-button">
        <md-icon>filter_alt</md-icon>
        
      </md-button>
      <md-button class="md-icon-button">
        <md-icon>login</md-icon>
      </md-button>
          </div>

   
      </md-app-toolbar>
      <md-app-content>
         <card/>
         <card/>
         <card/>
         <card/>
         <card/>
         <card/>
         <card/>
         <card/>
      </md-app-content>
    </md-app>
    <md-button id="add" class="md-icon-button md-raised md-primary">
        <md-icon>add</md-icon>
      </md-button>
  </div>
</template>

<style scoped>
  .md-app {
    max-height: 400px;
    border: 1px solid rgba(#000, .12);
  }

   // Demo purposes only
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
  .buttonbar{
    right: 0px;
  }
</style>

<script>
export default {
  name: 'Reveal',
  data: () => ({
    menuVisible: false
  })
}
</script>

<script>
import Card from '../components/Card'

export default {
  components: {
    'card': Card
  }
}
</script>