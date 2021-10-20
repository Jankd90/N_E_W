<template>
  <div>
    <md-datepicker v-model="selectedDateStart">
      <label>Select Start</label>
    </md-datepicker>
    <md-datepicker v-model="selectedDateFinish">
      <label>Select Deadline</label>
    </md-datepicker>


    <md-field md-clearable>
      <label>Contact details</label>
      <md-input v-model="contact"></md-input>
    </md-field>

    <div class="md-layout-item md-layout md-gutter">
 
        <md-field class="md-layout-item md-size-30">
      <label>Hours (EC)</label>
      <md-input v-model="initial"></md-input>
    </md-field>

        <md-field class="md-layout-item md-size-30">
      <label>Available slots</label>
      <md-input v-model="slots"></md-input>
    </md-field>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'LabeledDatepicker',
    data: () => ({
      selectedDateFinish: null,
      selectedDateStart: null
    })
  }
</script>
<style scoped>
.md-layout-item{
    display: inline-block;
}
</style>