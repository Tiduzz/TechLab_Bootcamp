<template>
  <v-container
    id="notifications"
    fluid
    tag="section"
  >
    <v-row justify="left">

      <v-col
        cols="12"
        md="8"
      >
        <base-material-card>
          <template v-slot:heading>
            <div class="display-2">
              Notificações
            </div>
          </template>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  // Components
  import axios from 'axios'
  export default {
    name: 'DashboardDashboard',
    data: () => ({ notificações: [] }),
    created () {
      // GET request using axios with error handling
      axios.get('http://172.17.0.1:7000/api/notification')
        .then(response => {
          console.log(response.data.notification)
          this.cameras = response.data.notification
        })
        .catch(error => {
          this.errorMessage = error.message
          console.error('There was an error!', error)
        })
    },
  }
</script>
