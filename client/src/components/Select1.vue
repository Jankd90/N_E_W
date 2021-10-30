<template>
<div>
  
     



 <md-field class="md-layout-item">
        <label for="labels">Labels</label>
        <md-select  v-model="selectedLabels" name="labels" id="labels" multiple>
          <md-option value="software">Software</md-option>
          <md-option value="hardware">Hardware</md-option>

        </md-select>
      </md-field>


     
    <md-chips v-model="selectedLabels" md-placeholder="Add your labels..."></md-chips>
  


    
 

  

    </div>

</template>

<script>
import store from '../store'
  export default {
    name: 'MultipleSelect',
    computed: {
      selectedLabels: {
        get () {return store.state.filterval
      },
      set (val, oldVal) {
        store.commit('addFilter', val);
    }
    }}}
</script>
<style scoped>
.md-layout-item{
    display: inline-block;
}
#addLabel{
    margin-top: 6px;
}
</style>