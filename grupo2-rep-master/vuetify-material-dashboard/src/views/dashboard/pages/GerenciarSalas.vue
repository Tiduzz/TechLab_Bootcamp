<template>
  <v-container
    id="gerenciar-salas"
    fluid
    tag="section"
  >
    <div class="row">
      <div
        v-for="room in rooms"
        :key="room.id"
        class="col-4 offset-1"
      >
        <base-material-stats-card
          color="purple"
          icon="mdi-chair-rolling"
          :title="room.name"
          sub-icon="mdi-clock"
          sub-icon-color="purple"
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

    data: () => ({ rooms: [] }),

    created () {
      // GET request using axios with error handling
      axios.get('http://172.17.0.1:7000/api/room')
        .then(response => {
          console.log(response.data.room)
          this.rooms = response.data.room
        })
        .catch(error => {
          this.errorMessage = error.message
          console.error('There was an error!', error)
        })
    },
  }
</script>
