# ワイヤーフレーム
**ワイヤーフレーム**とは、アプリケーションの画面の代表的なサンプル・テンプレートです。
Vuetify の 公式では、ここに説明があります。[Vuetify - ワイヤーフレーム](https://vuetifyjs.com/ja/getting-started/wireframes/)

## 各ワイヤーフレーム

### Base
[Base](https://vuetifyjs.com/ja/examples/wireframes/base/)

```
<!DOCTYPE html>
<html>
<head>
  <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
  <meta charset="utf-8"/>
  <style>
    [v-cloak] {
      display: none;
    }
  </style>
</head>
<body>
  <div id="app" v-cloak>
    <v-app id="inspire">
      <v-navigation-drawer
        v-model="drawer"
        app
      >
        <!--  -->
      </v-navigation-drawer>

      <v-app-bar app>
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title>Application</v-toolbar-title>
      </v-app-bar>

      <v-main>
        <!--  -->
      </v-main>
    </v-app>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>

  <script>
    new Vue({
      el: '#app',
      vuetify: new Vuetify,
      data: {
        drawer: null
      }
    });
  </script>
</body>
</html>

```

## Extended toolbar

[Extended Toolbar](https://vuetifyjs.com/ja/examples/wireframes/extended-toolbar/)

```
<!DOCTYPE html>
<html>
<head>
  <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
  <meta charset="utf-8"/>
  <style>
    [v-cloak] {
      display: none;
    }
  </style>
</head>
<body>
  <div id="app" v-cloak>
    <v-app id="inspire">
      <v-app-bar
        app
        shrink-on-scroll
      >
        <v-app-bar-nav-icon></v-app-bar-nav-icon>

        <v-toolbar-title>Application</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </v-app-bar>

      <v-main>
        <v-container>
          <v-row>
            <v-col
              v-for="n in 24"
              :key="n"
              cols="4"
            >
              <v-card height="200"></v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>

  <script>
    new Vue({
      el: '#app',
      vuetify: new Vuetify,
      data: {

      }
    });
  </script>
</body>
</html>
```

## System bar

[System Bar](https://vuetifyjs.com/ja/examples/wireframes/system-bar/)

```
<!DOCTYPE html>
<html>
<head>
  <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
  <meta charset="utf-8"/>
  <style>
    [v-cloak] {
      display: none;
    }
  </style>
</head>
<body>
  <div id="app" v-cloak>
    <v-app id="inspire">
      <v-system-bar app>
        <v-spacer></v-spacer>

        <v-icon>mdi-square</v-icon>

        <v-icon>mdi-circle</v-icon>

        <v-icon>mdi-triangle</v-icon>
      </v-system-bar>

      <v-app-bar app>
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title>Application</v-toolbar-title>
      </v-app-bar>

      <v-navigation-drawer
        v-model="drawer"
        fixed
        temporary
      >
        <!--  -->
      </v-navigation-drawer>

      <v-main class="grey lighten-2">
        <v-container>
          <v-row>
            <template v-for="n in 4">
              <v-col
                :key="n"
                class="mt-2"
                cols="12"
              >
                <strong>Category {{ n }}</strong>
              </v-col>

              <v-col
                v-for="j in 6"
                :key="`${n}${j}`"
                cols="6"
                md="2"
              >
                <v-sheet height="150"></v-sheet>
              </v-col>
            </template>
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>

  <script>
    new Vue({
      el: '#app',
      vuetify: new Vuetify,
      data: {
        drawer: null
      }
    });
  </script>
</body>
</html>

```

## Inbox
[Inbox](https://vuetifyjs.com/ja/examples/wireframes/inbox/)

```
<!DOCTYPE html>
<html>
<head>
  <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
  <meta charset="utf-8"/>
  <style>
    [v-cloak] {
      display: none;
    }
  </style>
</head>
<body>
  <div id="app" v-cloak>
    <v-app id="inspire">
      <v-system-bar app>
        <v-spacer></v-spacer>

        <v-icon>mdi-square</v-icon>

        <v-icon>mdi-circle</v-icon>

        <v-icon>mdi-triangle</v-icon>
      </v-system-bar>

      <v-navigation-drawer
        v-model="drawer"
        app
      >
        <v-sheet
          color="grey lighten-4"
          class="pa-4"
        >
          <v-avatar
            class="mb-4"
            color="grey darken-1"
            size="64"
          ></v-avatar>

          <div>john@vuetifyjs.com</div>
        </v-sheet>

        <v-divider></v-divider>

        <v-list>
          <v-list-item
            v-for="[icon, text] in links"
            :key="icon"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main>
        <v-container
          class="py-8 px-6"
          fluid
        >
          <v-row>
            <v-col
              v-for="card in cards"
              :key="card"
              cols="12"
            >
              <v-card>
                <v-subheader>{{ card }}</v-subheader>

                <v-list two-line>
                  <template v-for="n in 6">
                    <v-list-item

                      :key="n"
                    >
                      <v-list-item-avatar color="grey darken-1">
                      </v-list-item-avatar>

                      <v-list-item-content>
                        <v-list-item-title>Message {{ n }}</v-list-item-title>

                        <v-list-item-subtitle>
                          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil repellendus distinctio similique
                        </v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>

                    <v-divider
                      v-if="n !== 6"
                      :key="`divider-${n}`"
                      inset
                    ></v-divider>
                  </template>
                </v-list>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>

  <script>
    new Vue({
      el: '#app',
      vuetify: new Vuetify,
      data: {
        cards: ['Today', 'Yesterday'],
        drawer: null,
        links: [
          ['mdi-inbox-arrow-down', 'Inbox'],
          ['mdi-send', 'Send'],
          ['mdi-delete', 'Trash'],
          ['mdi-alert-octagon', 'Spam'],
          ]
      }
    });
  </script>
</body>
</html>
```

## Constrained
[Constrained](https://vuetifyjs.com/ja/examples/wireframes/constrained/)

```
<!DOCTYPE html>
<html>
<head>
  <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
  <meta charset="utf-8"/>
  <style>
    [v-cloak] {
      display: none;
    }
  </style>
</head>
<body>
  <div id="app" v-cloak>
    <v-app id="inspire">
        <v-app-bar
          app
          color="white"
          flat
        >
          <v-container class="py-0 fill-height">
            <v-avatar
              class="mr-10"
              color="grey darken-1"
              size="32"
            ></v-avatar>

            <v-btn
              v-for="link in links"
              :key="link"
              text
            >
              {{ link }}
            </v-btn>

            <v-spacer></v-spacer>

            <v-responsive max-width="260">
              <v-text-field
                dense
                flat
                hide-details
                rounded
                solo-inverted
              ></v-text-field>
            </v-responsive>
          </v-container>
        </v-app-bar>

        <v-main class="grey lighten-3">
          <v-container>
            <v-row>
              <v-col cols="2">
                <v-sheet rounded="lg">
                  <v-list color="transparent">
                    <v-list-item
                      v-for="n in 5"
                      :key="n"
                      link
                    >
                      <v-list-item-content>
                        <v-list-item-title>
                          List Item {{ n }}
                        </v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>

                    <v-divider class="my-2"></v-divider>

                    <v-list-item
                      link
                      color="grey lighten-4"
                    >
                      <v-list-item-content>
                        <v-list-item-title>
                          Refresh
                        </v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-sheet>
              </v-col>

              <v-col>
                <v-sheet
                  min-height="70vh"
                  rounded="lg"
                >
                  <!--  -->
                </v-sheet>
              </v-col>
            </v-row>
          </v-container>
        </v-main>
      </v-app>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>

  <script>
    new Vue({
      el: '#app',
      vuetify: new Vuetify,
      data: {
        links: [
          'Dashboard',
          'Messages',
          'Profile',
          'Updates',
          ]
        }
    });
  </script>
</body>
</html>

```
## Side navigation

[Side Navigation](https://vuetifyjs.com/ja/examples/wireframes/side-navigation/)

```
<!DOCTYPE html>
<html>
<head>
  <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
  <meta charset="utf-8"/>
  <style>
    [v-cloak] {
      display: none;
    }
  </style>
</head>
<body>
  <div id="app" v-cloak>
    <v-app id="inspire">
      <v-navigation-drawer
        v-model="drawer"
        app
        class="pt-4"
        color="grey lighten-3"
        mini-variant
      >
        <v-avatar
          v-for="n in 6"
          :key="n"
          :color="`grey ${n === 1 ? 'darken' : 'lighten'}-1`"
          :size="n === 1 ? 36 : 20"
          class="d-block text-center mx-auto mb-9"
        ></v-avatar>
      </v-navigation-drawer>

      <v-main>
        <!--  -->
      </v-main>
    </v-app>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>

  <script>
    new Vue({
      el: '#app',
      vuetify: new Vuetify,
      data: {
        drawer: null
      }
    });
  </script>
</body>
</html>
```

## Three column
[Three Column](https://vuetifyjs.com/ja/examples/wireframes/three-column/)

```
<!DOCTYPE html>
<html>
<head>
  <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
  <meta charset="utf-8"/>
  <style>
    [v-cloak] {
      display: none;
    }
  </style>
</head>
<body>
  <div id="app" v-cloak>
    <v-app id="inspire">
      <v-app-bar
        app
        color="white"
        flat
      >
        <v-avatar
          :color="$vuetify.breakpoint.smAndDown ? 'grey darken-1' : 'transparent'"
          size="32"
        ></v-avatar>

        <v-tabs
          centered
          class="ml-n9"
          color="grey darken-1"
        >
          <v-tab
            v-for="link in links"
            :key="link"
          >
            {{ link }}
          </v-tab>
        </v-tabs>

        <v-avatar
          class="hidden-sm-and-down"
          color="grey darken-1 shrink"
          size="32"
        ></v-avatar>
      </v-app-bar>

      <v-main class="grey lighten-3">
        <v-container>
          <v-row>
            <v-col
              cols="12"
              sm="2"
            >
              <v-sheet
                rounded="lg"
                min-height="268"
              >
                <!--  -->
              </v-sheet>
            </v-col>

            <v-col
              cols="12"
              sm="8"
            >
              <v-sheet
                min-height="70vh"
                rounded="lg"
              >
                <!--  -->
              </v-sheet>
            </v-col>

            <v-col
              cols="12"
              sm="2"
            >
              <v-sheet
                rounded="lg"
                min-height="268"
              >
                <!--  -->
              </v-sheet>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>

  <script>
    new Vue({
      el: '#app',
      vuetify: new Vuetify,
      data: {
        links: [
          'Dashboard',
          'Messages',
          'Profile',
          'Updates',
        ],
      }
    });
  </script>
</body>
</html>

```

## Discord
[Discord](https://vuetifyjs.com/ja/examples/wireframes/discord/)

```
<!DOCTYPE html>
<html>
<head>
  <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
  <meta charset="utf-8"/>
  <style>
    [v-cloak] {
      display: none;
    }
  </style>
</head>
<body>
  <div id="app" v-cloak>
    <v-app id="inspire">
      <v-system-bar app>
        <v-spacer></v-spacer>

        <v-icon>mdi-square</v-icon>

        <v-icon>mdi-circle</v-icon>

        <v-icon>mdi-triangle</v-icon>
      </v-system-bar>

      <v-app-bar
        app
        clipped-right
        flat
        height="72"
      >
        <v-spacer></v-spacer>

        <v-responsive max-width="156">
          <v-text-field
            dense
            flat
            hide-details
            rounded
            solo-inverted
          ></v-text-field>
        </v-responsive>
      </v-app-bar>

      <v-navigation-drawer
        v-model="drawer"
        app
        width="300"
      >
        <v-navigation-drawer
          v-model="drawer"
          absolute
          color="grey lighten-3"
          mini-variant
        >
          <v-avatar
            class="d-block text-center mx-auto mt-4"
            color="grey darken-1"
            size="36"
          ></v-avatar>

          <v-divider class="mx-3 my-5"></v-divider>

          <v-avatar
            v-for="n in 6"
            :key="n"
            class="d-block text-center mx-auto mb-9"
            color="grey lighten-1"
            size="28"
          ></v-avatar>
        </v-navigation-drawer>

        <v-sheet
          color="grey lighten-5"
          height="128"
          width="100%"
        ></v-sheet>

        <v-list
          class="pl-14"
          shaped
        >
          <v-list-item
            v-for="n in 5"
            :key="n"
            link
          >
            <v-list-item-content>
              <v-list-item-title>Item {{ n }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-navigation-drawer
        app
        clipped
        right
      >
        <v-list>
          <v-list-item
            v-for="n in 5"
            :key="n"
            link
          >
            <v-list-item-content>
              <v-list-item-title>Item {{ n }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main>
        <!--  -->
      </v-main>

      <v-footer
        app
        color="transparent"
        height="72"
        inset
      >
        <v-text-field
          background-color="grey lighten-1"
          dense
          flat
          hide-details
          rounded
          solo
        ></v-text-field>
      </v-footer>
    </v-app>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>

  <script>
    new Vue({
      el: '#app',
      vuetify: new Vuetify,
      data: {
        drawer: null
      }
    });
  </script>
</body>
</html>

```
