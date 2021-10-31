import Vue from "vue";
import Vuex from "vuex";
import Api from '@/services/Api'
import axios from "axios";
Vue.use(Vuex);

let pr = [
  {UUID: 1, title: 'Data analyses',subtitle: 'Open source smart watch', text: 'come join the team!', labels: ['software']},
  {UUID: 2, title: 'Feature engineering',subtitle: 'Open source smart watch', text: 'come join the team!', labels: ['hardware']},
  {UUID: 3, title: 'Data communication',subtitle: 'Open source smart watch', text: 'come join the team!', labels: ['software','hardware']},
  {UUID: 4, title: 'Localization',subtitle: 'Open source smart watch', text: 'come join the team!', labels: ['software']},
  {UUID: 5, title: 'Embedded ML',subtitle: 'Open source smart watch', text: 'come join the team!', labels: ['hardware', 'test']},
  {UUID: 6, title: 'Test',subtitle: 'Open source smart watch', text: 'come join the team!', labels: ['test']}

]

function getArraysIntersection(a1,a2){
  return  a1.filter(function(n) { return a2.indexOf(n) !== -1;});
}

function getposts(state) {
  axios.get('http://127.0.0.1:5000/api/get').then(
    response => {
      state.posts = response.data;
      state.fiteredPosts = response.data;
    }
  )      
}



export default new Vuex.Store({
 state: {a:'b', filterval: [], count: 3, posts: [], fiteredPosts: [], selectedLabels: []},
 projects: pr,
 filterval: ['blabla'],
 mutations: {
  addFilter (state, ls) {
      // mutate state
      state.filterval = ls; 
      console.log(ls);
      console.log(state.posts);
      if(state.filterval.length == 0){
        state.fiteredPosts = state.posts;
      }
      else{
      state.fiteredPosts = state.posts.filter((function (currentElement) {
        
        if (getArraysIntersection(currentElement.labels, state.filterval).length > 0) {
          return currentElement
        }}))
      
    }},
    getPosts(state) {
      getposts(state);    
    },
    postProject(state, data) {
    const URL = 'http://127.0.0.1:5000/api/upload'; 
    let config = {
      header : {
        'Content-Type' : 'image/png'
      }
    }
    axios.post(
      URL, 
      data,
      config
    ).then(
      response => {
        console.log('image upload response > ', response);
        //setInterval(function() {getposts(state)},3000);
        setTimeout(function(){
          getposts(state); 
       }, 1000);
      }
    )
    }
    
    
  }
  
})