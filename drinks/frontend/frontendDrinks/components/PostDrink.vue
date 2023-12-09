<template>
  <div>
    <form @submit.prevent="createPost">
      <div>
        <label for="name">Drink Name </label>
        <input type="text" name="name" v-model="formData.name" />
      </div>
      <br />
      <div>
        <label for="description">Description </label>
        <input type="text" name="description" v-model="formData.description" />
      </div>
      <br />
      <button>Submit Drink</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "PostDrink",
  data() {
    return {
      formData: {
        name: "",
        description: "",
      },
    };
  },
  methods: {
    createPost() {
      axios
        .post("http://127.0.0.1:8000/drinks/", this.formData)
        .then((response) => {
          console.log(response);
          this.formData = {
            name: "",
            description: "",
          };
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>
