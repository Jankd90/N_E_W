<template>
  <div>
    <md-dialog-prompt
      :md-active.sync="active"
      v-model="value"
      md-title="What's your name?"
      md-input-maxlength="30"
      md-input-placeholder="Type your name..."
      md-confirm-text="Done" />

  <md-button class="md-icon-button" @click="active = true">
        <md-icon>login</md-icon>
      </md-button>


  </div>
</template>

<script>
  export default {
    name: 'DialogPrompt',
    data: () => ({
      active: false,
      value: null
    })
  }
</script>