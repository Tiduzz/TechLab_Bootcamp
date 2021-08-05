<template>
  <v-container
    id="gerenciar-cameras"
    fluid
    tag="section"
  >
    <div class="row">
      <div
        v-for="camera in cameras"
        :key="camera.id"
        class="col-4 offset-1"
      >
        <base-material-stats-card
          color="info"
          icon="mdi-webcam"
          :title="camera.name"
          sub-icon="mdi-clock"
          sub-icon-color="blue"
          sub-text="Just Updated"
        />
      </div>
    </div>
  </v-container>
</template>

<script>
  // Components
  import axios from 'axios'

  export default {
    name: 'DashboardDashboard',

    data: () => ({ cameras: [] }),

    created () {
      // GET request using axios with error handling
      axios.get('http://172.17.0.1:7000/api/camera')
        .then(response => {
          console.log(response.data.camera)
          this.cameras = response.data.camera
        })
        .catch(error => {
          this.errorMessage = error.message
          console.error('There was an error!', error)
        })
    },
  }
</script>
