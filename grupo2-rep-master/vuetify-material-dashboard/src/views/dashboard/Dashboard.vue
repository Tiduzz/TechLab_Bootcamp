<!-- Olá! Doug droppando os comentários :) -->
<template>
  <v-container
    id="dashboard"
    tag="section"
  >
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <base-material-chart-card
          :data="barChart.data"
          hover-reveal
          color="indigo"
          type="Bar"
        >
          <template v-slot:reveal-actions>
            <v-tooltip bottom>
              <template v-slot:activator="{ attrs, on }">
                <v-btn
                  v-bind="attrs"
                  color="info"
                  icon
                  v-on="on"
                >
                  <v-icon
                    color="info"
                  >
                    mdi-refresh
                  </v-icon>
                </v-btn>
              </template>

              <span>Refresh</span>
            </v-tooltip>

            <v-tooltip bottom>
              <template v-slot:activator="{ attrs, on }">
                <v-btn
                  v-bind="attrs"
                  light
                  icon
                  v-on="on"
                >
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
              </template>
              <span>Change Date</span>
            </v-tooltip>
          </template>

          <h3 class="card-title font-weight-light mt-2 ml-2">
            Pessoas sem máscara nas Salas
          </h3>

          <template v-slot:actions>
            <v-icon
              class="mr-1"
              small
            >
            </v-icon>
            <span class="caption grey--text font-weight-light"></span>
          </template>
        </base-material-chart-card>
      </v-col>

      <v-col
        cols="12"
        md="6"
      >
        <base-material-chart-card
          :data="dailySalesChart.data"
          :options="dailySalesChart.options"
          color="success"
          hover-reveal
          type="Line"
        >
          <template v-slot:reveal-actions>
            <v-tooltip bottom>
              <template v-slot:activator="{ attrs, on }">
                <v-btn
                  v-bind="attrs"
                  color="info"
                  icon
                  v-on="on"
                >
                  <v-icon
                    color="info"
                  >
                    mdi-refresh
                  </v-icon>
                </v-btn>
              </template>

              <span>Refresh</span>
            </v-tooltip>

            <v-tooltip bottom>
              <template v-slot:activator="{ attrs, on }">
                <v-btn
                  v-bind="attrs"
                  light
                  icon
                  v-on="on"
                >
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
              </template>

              <span>Change Date</span>
            </v-tooltip>
          </template>

          <h3 class="card-title font-weight-light mt-2 ml-2">
            Pessoas sem Máscara por Dia
          </h3>

          <template v-slot:actions>
            <v-icon
              class="mr-1"
              small
            >
            </v-icon>
          </template>
        </base-material-chart-card>
      </v-col>
      <div class = "row">
        <v-col
          cols="12"
          sm="6"
          lg="3"
        >
          <base-material-stats-card
            color="green"
            icon="mdi-chair-rolling"
            title="Sala 1"
            value="2"
            sub-icon="mdi-clock"
            sub-icon-color="green"
            sub-text="Incidência de Aglomeração: Baixa"
          />
        </v-col>

        <v-col
          cols="12"
          sm="6"
          lg="3"
        >
          <base-material-stats-card
            color="red"
            icon="mdi-chair-rolling"
            title="Sala 2"
            value="99"
            text-color="black"
            sub-icon="mdi-clock"
            sub-icon-color="red"
            sub-text="Incidência de Aglomeração: Alta!"
          />
        </v-col>

        <v-col
          cols="12"
          sm="6"
          lg="3"
        >
          <base-material-stats-card
            color="grey"
            icon="mdi-chair-rolling"
            title="Sala 3"
            value="0"
            sub-icon="mdi-clock"
            sub-icon-color="light-grey"
            sub-text="Sala Disponível"
          />
        </v-col>

        <v-col
          cols="12"
          sm="6"
          lg="3"
        >
          <base-material-stats-card
            color="yellow"
            icon="mdi-chair-rolling"
            title="Sala 4"
            value="4"
            sub-icon="mdi-clock"
            sub-icon-color="yellow"
            sub-text="Incidência de Aglomeração: Média"
          />
        </v-col>
      </div>
      <v-col
        cols="18"
        lg="12"
      >
        <base-material-chart-card
          :data="dataCompletedTasksChart.data"
          :options="dataCompletedTasksChart.options"
          hover-reveal
          color="info"
          type="Line"
        >
          <template v-slot:reveal-actions>
            <v-tooltip bottom>
              <template v-slot:activator="{ attrs, on }">
                <v-btn
                  v-bind="attrs"
                  color="info"
                  icon
                  v-on="on"
                >
                  <v-icon
                    color="info"
                  >
                    mdi-refresh
                  </v-icon>
                </v-btn>
              </template>

              <span>Refresh</span>
            </v-tooltip>

            <v-tooltip bottom>
              <template v-slot:activator="{ attrs, on }">
                <v-btn
                  v-bind="attrs"
                  light
                  icon
                  v-on="on"
                >
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
              </template>

              <span>Change Date</span>
            </v-tooltip>
          </template>

          <h3 class="card-title font-weight-light mt-2 ml-2">
            Pessoas sem Máscara nas Últimas Horas
          </h3>
          <template v-slot:actions>
        </template>
        </base-material-chart-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'DashboardDashboard',
    data () {
      return {
        barChart: {
          data: {
            labels: ['Sala 1', 'Sala 2', 'Sala 3', 'Sala 4'],
            series: [
              [13, 20, 10, 12],
            ],
          },
        },
        dailySalesChart: {
          data: {
            labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom'],
            series: [
              [1, 20, 1, 25, 40, 1, 5],
            ],
          },
          options: {
            lineSmooth: this.$chartist.Interpolation.cardinal({
              tension: 0,
            }),
            low: 0,
            high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
            chartPadding: {
              top: 0,
              right: 0,
              bottom: 0,
              left: 0,
            },
          },
        },
        dataCompletedTasksChart: {
          data: {
            labels: ['06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00', '00:00'],
            series: [
              [230, 750, 450, 300, 280, 240, 200, 190, 0, 0],
            ],
          },
          options: {
            lineSmooth: this.$chartist.Interpolation.cardinal({
              tension: 0,
            }),
            low: 0,
            high: 1000, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
            chartPadding: {
              top: 0,
              right: 0,
              bottom: 0,
              left: 0,
            },
          },
        },
        emailsSubscriptionChart: {
          data: {
            labels: ['Ja', 'Fe', 'Ma', 'Ap', 'Mai', 'Ju', 'Jul', 'Au', 'Se', 'Oc', 'No', 'De'],
            series: [
              [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895],
            ],
          },
          options: {
            axisX: {
              showGrid: false,
            },
            low: 0,
            high: 1000,
            chartPadding: {
              top: 0,
              right: 5,
              bottom: 0,
              left: 0,
            },
          },
          responsiveOptions: [
            ['screen and (max-width: 640px)', {
              seriesBarDistance: 5,
              axisX: {
                labelInterpolationFnc: function (value) {
                  return value[0]
                },
              },
            }],
          ],
        },
      }
    },
    created () {
      // GET request using axios with error handling
      axios.get('http://172.17.0.1:7000/api/facereports')
        .then(response => {
          console.log(response.data.data)
          this.barChart.data = response.data.data
        })
        .catch(error => {
          this.errorMessage = error.message
          console.error('There was an error!', error)
        })
    },
    methods: {
      complete (index) {
        this.list[index] = !this.list[index]
      },
    },
  }

</script>
