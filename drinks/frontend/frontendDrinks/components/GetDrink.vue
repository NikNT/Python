<template>
  <div>
    <button @click="getDrinks">Load Posts</button>
    <div v-for="drink in drinks" :key="drink.id">
      <h3>{{ drink.name }}</h3>
      <h4>{{ drink.description }}</h4>
      <DeleteDrink :drinkId="drink.id" />
    </div>
    <hr />
  </div>
</template>

<script>
import axios from "axios";
import DeleteDrink from "./DeleteDrink.vue";
export default {
  name: "GetDrink",
  components: {
    DeleteDrink,
  },
  data() {
    return {
      drinks: [],
    };
  },
  methods: {
    getDrinks() {
      axios
        .get("http://localhost:8000/drinks/")
        .then((response) => {
          this.drinks = response.data.drinks;
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>
