<template>
  <v-container
    id="estatisticas"
    tag="section"
  >
    <v-row>
      <v-col
        cols="12"
        sm="6"
        md="4"
      >
        <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="false"
          :return-value.sync="date"
          transition="scale-transition"
          offset-y
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="date"
              label="Data Inicial"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date"
            no-title
            scrollable
          >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="menu = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.menu.save(date)"
            >
              OK
            </v-btn>
          </v-date-picker>
        </v-menu>
      </v-col>
      <v-spacer></v-spacer>

      <v-col
        cols="12"
        sm="6"
        md="4"
      >
        <v-menu
          ref="menu2"
          v-model="menu2"
          :close-on-content-click="false"
          :return-value.sync="date2"
          transition="scale-transition"
          offset-y
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="date2"
              label="Data Final"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date2"
            no-title
            scrollable
          >
            <v-spacer></v-spacer>
            <v-btn
              text
              color="primary"
              @click="menu2 = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.menu2.save(date2)"
            >
              OK
            </v-btn>
          </v-date-picker>
        </v-menu>
      </v-col>
      <v-spacer></v-spacer>
      <!--Fim de Date Field -->
      <div class="row">
        <container
          fluid
        >
          <v-checkbox
            v-model="checkbox"
            :label="'Relatório Diário'"
          >
            <v-radio-group
              v-model="radioGroup"
            >
              <v-radio
                v-for="n in 3"
                :key="n"
                :label="'Radio ${n}'"
                :value="n"
              >
              </v-radio>
            </v-radio-group>
            <v-switch
              v-model="switch1"
              :label="'Switch 1: ${switch1.toString()}'"
            >
            </v-switch>
          </v-checkbox>
          <v-checkbox
            v-model="checkbox2"
            :label="'Relatório Semanal'"
          >
            <v-radio-group
              v-model="radioGroup"
            >
              <v-radio
                v-for="n in 3"
                :key="n"
                :label="'Radio ${n}'"
                :value="n"
              >
              </v-radio>
            </v-radio-group>
            <v-switch
              v-model="switch2"
              :label="'Switch 2: ${switch1.toString()}'"
            >
            </v-switch>
          </v-checkbox>
          <v-checkbox
            v-model="checkbox3"
            :label="'Relatório Mensal'"
          >
            <v-radio-group
              v-model="radioGroup"
            >
              <v-radio
                v-for="n in 3"
                :key="n"
                :label="'Radio ${n}'"
                :value="n"
              >
              </v-radio>
            </v-radio-group>
            <v-switch
              v-model="switch3"
              :label="'Switch 3: ${switch1.toString()}'"
            >
            </v-switch>
          </v-checkbox>
        </container>
      </div>
      <v-spacer></v-spacer>
      <!--Fim de Checkbox -->
      <v-col
        cols="10"
      >
        <v-select
          :items="items"
          :menu-props="{ top: true, offsetY: true }"
          label="Selecione o tipo de relatório desejado"
        >
        </v-select>
      </v-col>
      <!--Fim de Menu Select -->
      <v-col
        cols="12"
        md="10"
      >
        <base-material-chart-card
          :data="pieChart.data"
          hover-reveal
          color="indigo"
          type="Pie"
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
            Pessoas sem Máscara por Sala
          </h3>

          <p class="d-inline-flex font-weight-light ml-2 mt-1">
            Não há pessoas sem máscara na sala 3
          </p>

          <template v-slot:actions>
            <v-icon
              class="mr-1"
              small
            >
              mdi-clock-outline
            </v-icon>
            <span class="caption grey--text font-weight-light">updated 5 minutes ago</span>
          </template>
        </base-material-chart-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<!-- Fim do Gráfico -->
<script>
  // Components

  export default {
    name: 'DashboardDashboard',
    data () {
      return {
        pieChart: {
          data: {
            labels: ['40.6%', '50.4%', '8.0%'],
            series: [10, 7, 5],
          },
        },
        date: new Date().toISOString().substr(0, 10),
        date2: new Date().toISOString().substr(0, 10),
        menu: false,
        menu2: false,
        text: 'center',
        icon: 'justify',
        items: ['Locais de Aglomeração', 'Pessoas sem Máscara', 'Contagem de Pessoas'],
      }
    },
  }

</script>
