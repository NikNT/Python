<template>
  <button @click="deleteDrink(drinkId)">Delete</button>
</template>

<script>
import axios from "axios";

export default {
  name: "DeleteDrink",
  props: {
    drinkId: String,
  },
  methods: {
    deleteDrink(drinkId) {
      axios
        .delete(`http://localhost:8000/drinks/${drinkId}`)
        .then((response) => {
          console.log(`Drink with ID ${drinkId} deleted!`);
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>
