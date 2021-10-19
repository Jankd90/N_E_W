<template>
<div>
<h1>Register</h1>

  <div class="md-layout md-gutter">
    <div class="md-layout-item"></div>
    <div class="md-layout-item"></div>
    <div class="md-layout-item"></div>
  </div>



<div class="md-layout-item md-size-15 ">
    <md-field class="md-alignment-center-center">
      <label>Initial Value</label>
      <md-input v-model="email"></md-input>
    </md-field>
</div>


<br>
<input type="password" v-model="password" name="password" placeholder="password"/>
<br>
<button @click="register">Register</button>
</div>
</template>

<script>
import AuthenticationSevice from '@/services/AuthenticationService'
export default({
  data () {
    return {
      email: 'Who you',
      password: 'secret!'
    }
  },
  watch: {
    email (value){
      console.log(value)
    }
  },
  methods: {
    async register () {
      console.log('register')
      const response = await AuthenticationSevice.register({
        email: this.email,
        password: this.password
      })
      console.log(response.data)
    }
  }
})
</script>
<style scoped>
</style>
