<template>

  <div>
    <md-dialog :md-active.sync="showDialog">
      <md-dialog-title>Filter</md-dialog-title>

     
    <div style="padding-left: 5rem; padding-right: 5rem;">
 <selectlabels />
    </div>
         
     

        

 

     
    </md-dialog>

  

<md-button class="md-icon-button" @click="showDialog = true">
        <md-icon>filter_alt</md-icon>
        
      </md-button>
    
  </div>
</template>

<script>
  import Selectlabels from '../components/Select1'  
  export default {
    name: 'DialogPrompt',
    data: () => ({
      showDialog: false
    }),
    components: {
    'selectlabels': Selectlabels,
  }
  }
</script>
<style scoped>
.selectlabels{
  margin: 20rem;
}
</style>