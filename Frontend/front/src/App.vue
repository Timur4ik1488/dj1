<template>
  <div>
    <h1>YO</h1>
    <ul>
      <li v-for="item in items" :key="item.id">
        Число: {{ item.a }}
      </li>
    </ul>
    <button @click="addItem">Добавить число</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: [],
    };
  },
  methods: {
    fetchItems() { 
      axios.get('http://localhost:8000/api/yo/')
        .then(response => {
          this.items = response.data;
        })
        .catch(error => {
          console.error('Ошибка загрузки данных:', error);
        });
    },
    addItem() {
      const newItem = {
        a: Math.floor(Math.random() * 100) 
      };
      axios.post('http://localhost:8000/api/yo/', newItem)
        .then(() => {
          this.fetchItems(); 
        })
        .catch(error => {
          console.error('Ошибка добавления данных:', error);
        });
    },
  },
  mounted() {
    this.fetchItems(); 
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 10px 0;
  padding: 10px;
  background: #000000;
  border-radius: 4px;
}
button {
  padding: 10px 15px;
  background: #42b983;
  color: rgb(0, 0, 0);
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background: #369f6b;
}
</style>