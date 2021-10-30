<template>
  <div>
    <md-chip class="md-primary">{{label}}</md-chip>
  </div>
</template>

<script>
export default {
  name: 'SingleChip',
  props:{
    label: String
  }
}
</script>
<style scoped>
.md-chip{
    margin: 0.2rem;
}
</style>