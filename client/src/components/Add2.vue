<template>
  <div>
    <md-dialog :md-active.sync="showDialog">
      <md-dialog-title>Push to market place</md-dialog-title>

      <md-tabs md-dynamic-height>
        <md-tab md-label="General">
          <p>Please provide an consice discription of your project. Check the 
              <md-button style="margin-top:-8px; margin-left: -3px; margin-right:-3px;">market place rules</md-button> if you're not sure! </p>
           
    <md-field>
      <label>Upload image</label>
      <md-file v-model="single" @change="uploadImage($event)"/>

    </md-field>

               <md-field>
      <label>Title</label>
      <md-input v-model="title"></md-input>
    </md-field>

            <md-field>
      <label>Subtitle</label>
      <md-input v-model="subtitle"></md-input>
    </md-field>

    <md-field>
      <label>Textarea</label>
      <md-textarea v-model="text"></md-textarea>
    </md-field>

           </md-tab>
           

        <md-tab md-label="Select Labels">
             <p>Select the topics you think are valueble to describe the project.</p>
        <selectlabels/>
          </md-tab>

        <md-tab md-label="Organization">
          <p>We're almost there! lets fill in some organizational stuff so that the right amound of people can find the project at the right time.</p>
         <organize/>
               <md-dialog-actions>
         <md-button class="md-primary" @click="showDialog = false; uploadProject()">Done</md-button>
      
      </md-dialog-actions>
         </md-tab>
      </md-tabs>


    </md-dialog>

    <md-button id="add"  @click="showDialog = true" class="md-icon-button md-raised md-primary">
        
        <md-icon>add</md-icon>
      </md-button>
 <!-- <md-button id="add2"  @click="getPost" class="md-icon-button md-raised md-primary">
        
        <md-icon>add</md-icon>
      </md-button> -->
  </div>
</template>





<script>
import Organize from '../components/Organize'
import Selectlabels from '../components/Select1'
import axios from 'axios'
import store from '../store'

let IMG_URL,start, finish, hours, slots;
  export default {
    name: 'DialogCustom',
    data: () => ({
      showDialog: false,
      title: '', subtitle : '', text : '', start, finish ,contact : '',hours, slots,
    }),
    components: {
    'selectlabels': Selectlabels,
    'organize': Organize
  },
  watch: {
    title (value) {
      //title = value;
      console.log(value);
    }
  },

  methods: {
    sayHello(){
      alert('aaaaa');
      console.log(single);
    },
    getPost(){
      store.commit('getPosts');
    }
    ,
    uploadProject(){
       let data = new FormData();
       const json = JSON.stringify({ title : this.title, subtitle : this.subtitle, 
       text : this.text, labels : this.$store.state.filterval, 
       start : this.start, finish : this.finish,
       contact : this.contact, hours : this.hours, slots : this.slots });
       data.append('name', 'my-picture');
       data.append('file', this.IMG_URL); 
       data.append('json', json); 
       store.commit('postProject', data);
    }
    ,
    uploadImage(event) {
      this.IMG_URL = event.target.files[0];
   
      
  }
  }
  }
</script>


<style scoped>
  .md-dialog /deep/.md-dialog-container {
    max-width: 268px;
    max-height: 768px;
  }
    #add{
    position: absolute;
    right: 1rem;
    bottom: 1rem;
  }
</style>