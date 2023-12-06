<template>
  <div>
    <h1>Drinks List</h1>
    <ul>
      <li v-for="drink in drinks" :key="drink.id">
        <h2>{{ drink.name }}</h2>
        <p>{{ drink.description }}</p>
      </li>
    </ul>
  </div>
</template>

<script setup>
// export default {
//   data() {
//     return {
//       drinks: [],
//     };
//   },

const { response: drinks } = await useFetch("http://localhost:8000/drinks/");

//   async mounted() {
//     try {
//       const {response : drinks } = await useFetch("http://localhost:8000/drinks/");
//       this.drinks = response.drinks;
//     } catch (error) {
//       console.error("Error fetching drinks:", error);
//     }
//   },
// };
</script>
