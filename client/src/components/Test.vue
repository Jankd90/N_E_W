<template>
  <div class="page-container">
    <md-app style="min-height: 100vh;" md-mode="reveal">
      <md-app-toolbar class="md-primary">
      
        <span class="md-title">N_E_W</span>
        
       <div class="md-toolbar-section-end">
        <filter1/>
        <login/>
        
    
          </div>

   
      </md-app-toolbar>
      <md-app-content>
         
  <div id="contain" v-for="index in posts" :key="index">
  
    <card :title="index.title" :subtitle="index.subtitle" :text="index.text" :labels="index.labels"/>
  </div>
         

        
      </md-app-content>
    </md-app>
    <add/>
  </div>
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
    margin-bottom: 1rem;
  }
  .buttonbar{
    right: 0px;
  }
  #contain{
    display: inline-block;
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
import Add from '../components/Add2'
import Filter from '../components/Filter'
import Login from '../components/Login'
//import store from '../store'
import { onMounted } from 'vue'

export default {
  title: 'N_E_W Market',
  ////store,

  computed: {
    count () {
      return this.$store.state.filterval
      // Or return basket.getters.fruitsCount
      // (depends on your design decisions).
    },
    posts () {
      return this.$store.state.fiteredPosts
      // Or return basket.getters.fruitsCount
      // (depends on your design decisions).
    }
  },
  components: {
    'card': Card,
    'filter1': Filter,
    'add': Add,
    'login': Login
  },
  watch: {
    count (newCount, oldCount) {
      console.log(console.log(this.$store.state.fiteredPosts))
    }
  },
  mounted() {             
         this.$store.commit('getPosts');
      }
  
}
</script>