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

export default new Vuex.Store({
 state: {a:'b', filterval: [], count: 3, posts: pr, fiteredPosts: pr, selectedLabels: []},
 projects: pr,
 filterval: ['blabla'],
 mutations: {
  addFilter (state, ls) {
      // mutate state
      state.filterval = ls; 
      state.count++;
      if(state.filterval.length == 0){
        state.fiteredPosts = pr;
      }
      else{
      state.fiteredPosts = state.posts.filter((function (currentElement) {
        
        if (getArraysIntersection(currentElement.labels, state.filterval).length > 0) {
          return currentElement
        }}))
      
    }},
    getPosts(state) {
      axios.get('http://127.0.0.1:5000/api/get').then(
        response => {
          state.fiteredPosts = response.data;
        }
      )      
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
        console.log('image upload response > ', response)
      }
    )
    }
    
    
  }
  
})