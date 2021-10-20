<template>
  <div class="md-size-66">
    <md-dialog  :md-active.sync="showDialog">

<div class="md-layout-item ">
      <md-field>
        <label for="movies">Movies</label>
        <md-select v-model="selectedMovies" name="movies" id="movies" multiple>
          <md-option value="fight-club">Fight Club</md-option>
          <md-option value="godfather">Godfather</md-option>
          <md-option value="godfather-ii">Godfather II</md-option>
          <md-option value="godfather-iii">Godfather III</md-option>
          <md-option value="godfellas">Godfellas</md-option>
          <md-option value="pulp-fiction">Pulp Fiction</md-option>
          <md-option value="scarface">Scarface</md-option>
        </md-select>
      </md-field>

      <div>
        <strong>Selected movies:</strong>
        {{ selectedMovies }}
      </div>
    </div>

         <md-dialog-actions>
        <md-button class="md-primary" @click="showDialog = false">Close</md-button>
        <md-button class="md-primary" @click="showDialog = false">Save</md-button>
      </md-dialog-actions>
    </md-dialog>


<md-button id="add"  @click="showDialog = true" class="md-icon-button md-raised md-primary">
        <md-icon>add</md-icon>
      </md-button>
    
  </div>
</template>

<script>
  export default {
    name: 'DialogCustom',
    data: () => ({
      showDialog: false
    })
  }
</script>
<style scoped>
  #add{
    position: absolute;
    right: 1rem;
    bottom: 1rem;
  }
  .md-dialog /deep/.md-dialog-container {
    width: 900px;
  }
</style>