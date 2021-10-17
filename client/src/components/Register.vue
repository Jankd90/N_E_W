<template>
<div>
<h1>Register</h1>
<input type="email" v-model="email" name="email" placeholder="email"/>
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
