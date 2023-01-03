<template>
  <div class="container">
    <div class="row">
      <div>
        <alert :message="message" v-if="showMessage"></alert>
        
        테스트 
        


      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      word: [],
      idiom: [],
      perPage: 15,
      currentPage: 1,
      fields: [
          { key: 'word', label: '단어'},
          { key: 'mean', label: '뜻'} 
        ],
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
      editForm: {
        id: '',
        title: '',
        author: '',
        read: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  computed:{
    rows() {
        return this.volt.length
    },
    editableFields() {
        return this.fields.filter(field => { return field.editable === true })
    }
  },
  created() {
    this.getExam();
  },
  methods: {
    editItem(item) { console.log(item); },
    getExam() {
        const path = 'http://127.0.0.1:5000/exam';
        axios.get(path)
            .then((res) => {
                this.word = res.data['word'];
                this.idiom = res.data['idiom'];
            })
            .catch((error) => {
                console.error(error);
            });
    }
  }
};
</script>