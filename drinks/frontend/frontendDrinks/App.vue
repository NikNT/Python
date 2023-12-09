<template>
  <GetDrink />
  <PostDrink />
</template>

<script>
import GetDrink from "./components/GetDrink.vue";
import PostDrink from "./components/PostDrink.vue";

export default {
  name: "App",
  components: {
    GetDrink,
    PostDrink,
  },
};
</script>
