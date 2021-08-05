<template>
  <v-app>
    <v-content>
      <v-container
        id="login"
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="8"
          >
            <v-card class="elevation-12">
              <v-window v-model="step">
                <v-window-item :value="1">
                  <v-row>
                    <v-col
                      cols="12"
                      md="8"
                    >
                      <v-card-text class="mt-12">
                        <h1
                          class="text-center display-2  black--text text--accent-3"
                        >
                          Bem vindo ao Tecnoria!
                        </h1>
                        <div
                          class="text-center"
                          mt-4
                        />
                        <h4 class="text-center mlt-4">
                          Digite seu e-mail e senha
                        </h4>
                        <v-form>
                          <v-text-field
                            label="E-mail"
                            name="E-mail"
                            prepend-icon=""
                            type="text"
                            color="blue accent-3"
                            required
                          />
                          <v-text-field
                            label="Senha"
                            name="password"
                            prepend-icon=""
                            type="password"
                            color="blue accent-3"
                            required
                          />

                          <div class="text-center mt-3">
                            <v-btn
                              rounded
                              color="blue accent-3"
                              dark
                              type="submit"
                              @click.prevent="login"
                            >
                              Entrar
                            </v-btn>
                          </div>
                        </v-form>
                      </v-card-text>
                    </v-col>
                    <v-col
                      cols="12"
                      md="4"
                      class="blue accent-3"
                    >
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">
                          Caso tenha esquecido a senha é só clicar no botão abaixo!
                        </h1>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn
                          rounded
                          outlined
                          dark
                          @click="step++"
                        >
                          SUPORTE
                        </v-btn>
                      </div>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item :value="2">
                  <v-row class="fill-height">
                    <v-col
                      cols="12"
                      md="4"
                      class="blue"
                    >
                      <v-card-text class="white--text mt-12">
                        <h1 class="text-center display-1">
                          Estamos aqui para ajudar!
                        </h1>
                        <h5 class="text-center">
                          Caso tenha lembrado a senha, tente o login novamente no botão abaixo!
                        </h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn
                          rounded
                          outlined
                          dark
                          @click="step++"
                        >
                          Login
                        </v-btn>
                      </div>
                    </v-col>
                    <v-col
                      cols="12"
                      md="8"
                    >
                      <v-card-text class="mt-12">
                        <h1
                          class="text-center display-2 blue--text text--accent-3"
                        >
                          RECUPERAR A SENHA
                        </h1>
                        <div class="text-center mt-4" />
                        <h4 class="text-center mt-4">
                          Digite seu e-mail para recuperação da senha
                        </h4>
                        <v-form>
                          <v-text-field
                            label="E-mail"
                            name="email"
                            prepend-icon=""
                            type="text"
                            color="yellow accent-3"
                          />
                        </v-form>
                      </v-card-text>
                      <div class="text-center mt-n5">
                        <v-btn
                          rounded
                          color="blue"
                          dark
                        >
                          ENVIAR
                        </v-btn>
                      </div>
                    </v-col>
                  </v-row>
                </v-window-item>
              </v-window>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    datas: () => ({
      step: 1,
    }),
    props: {
      source: String,
    },
    data () {
      return {
        username: '',
        password: '',
      }
    },
    methods: {
      login () {
        this.$router.push('/')
      },
    },
  }
  </script>
