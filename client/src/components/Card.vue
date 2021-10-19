<template>
<md-card>
      <md-card-media>
        <img src="@/assets/bangle-leaf.jpg" alt="People">
      </md-card-media>

      <md-card-header>
        <div class="md-title">Smartwatch Engineer</div>
        <div class="md-subhead">Programming, testing</div>
      </md-card-header>

      <md-card-expand>
        <md-card-actions md-alignment="space-between">
          <div>
            
            <md-button>Go to application</md-button>
          </div>

          <md-card-expand-trigger>
            <md-button class="md-icon-button">
              <md-icon>keyboard_arrow_down</md-icon>
            </md-button>
          </md-card-expand-trigger>
        </md-card-actions>

        <md-card-expand-content>
          <md-card-content>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed accusantium quasi non, voluptas eius illo quas, saepe voluptate pariatur in deleniti minus sint. Excepturi.
          </md-card-content>
          
        </md-card-expand-content>
        
      </md-card-expand>
    </md-card> 
</template>

<style scoped>
  .md-app {
    max-height: 400px;
    border: 1px solid rgba(#000, .12);
  }

   // Demo purposes only
  .md-drawer {
    width: 230px;
    max-width: calc(100vw - 125px);
  }
   #add{
    position: absolute;
    right: 1rem;
    bottom: 1rem;
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
  }
</style>