<template>
  <div class="container">
        <b-row>
            <!-- <b-col lg="6" class="my-1">
                    <b-form-group
                    label="Filter"
                    label-for="filter-input"
                    label-cols-sm="3"
                    label-align-sm="right"
                    label-size="sm"
                    class="mb-0"
                    >
                    <b-input-group size="sm">
                        <b-form-input
                        id="filter-input"
                        v-model="filter"
                        type="search"
                        placeholder="Type to Search"
                        ></b-form-input>

                        <b-input-group-append>
                        <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
                        </b-input-group-append>
                    </b-input-group>
                </b-form-group>
            </b-col> -->
<!-- 
            <b-col sm="5" md="6" class="my-1">
                
                <b-form-group
                label="Per page"
                label-for="per-page-select"
                label-cols-sm="6"
                label-cols-md="4"
                label-cols-lg="3"
                label-align-sm="right"
                label-size="sm"
                class="mb-0"
                >
                <b-form-select
                    id="per-page-select"
                    v-model="perPage"
                    :options="pageOptions"
                    size="sm"
                ></b-form-select>
                </b-form-group>
            </b-col>

            <b-col sm="7" md="6" class="my-1">
                <b-pagination
                v-model="currentPage"
                :total-rows="totalRows"
                :per-page="perPage"
                size="sm"
                class="my-0"
                ></b-pagination>
            </b-col> -->
        </b-row>

        <div>
            <alert :message="message" v-if="showMessage"></alert>
            <button type="button" class="btn btn-success btn-sm" v-b-modal.word-modal>단어 추가</button>
            <b-table id="my-table" :items="words" :fields="fields" :per-page="perPage" :current-page="currentPage" small style="width:60%; margin: auto;">
            </b-table>
        </div>


        <b-modal ref="addWordModal" id="word-modal" title="단어 추가" hide-footer>
            <b-form @submit="onSubmit" @reset="onReset" class="w-100">
                <b-form-group id="form-word-group" label="단어 :" label-for="form-word-input"> 
                    <b-form-input id="form-word-input" type="text" v-model="addWordForm.word" required>
                    </b-form-input>
                </b-form-group>

                <b-form-group id="form-parts-group" label="품사 :" label-for="form-parts-input" style="margin-top: 15px;">
                    <b-form-input id="form-parts-input" type="text" v-model="addWordForm.parts" required>
                    </b-form-input>
                </b-form-group>

                <b-form-group id="form-mean-group" label="뜻 :" label-for="form-mean-input" style="margin-top: 15px;">
                    <b-form-input id="form-mean-input" type="text" v-model="addWordForm.mean" required>
                    </b-form-input>
                </b-form-group>

                <b-button-group style="margin-top: 25px;">
                    <b-button type="submit" variant="primary">Submit</b-button>
                    <b-button type="reset" variant="danger">Reset</b-button>
                </b-button-group>
            </b-form>
        </b-modal>

    </div>
</template>
<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
        words: [],
        perPage: 15,
        currentPage: 1,
        totalRows: 1,
        currentPage: 1,
        perPage: 5,
        pageOptions: [5, 10, 15, { value: 100, text: "Show a lot" }],
        fields: [
            { key: 'word', label: '단어'},
            { key: 'parts', label: '품사'},
            { key: 'mean', label: '뜻'} 
          ],
        addWordForm: {
          word: '',
          parts: '',
          mean: '',
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
        return this.words.length
    }
  },
  methods: {
    getWords() {
        const path = 'http://127.0.0.1:5000/word';
        axios.get(path)
            .then((res) => {
                this.words = res.data;
                console.log(this.words)
            })
            .catch((error) => {
                console.error(error);
            });
    },
    addWords(addData) {
        const path = 'http://127.0.0.1:5000/word';
        axios.post(path, addData)
            .then(() => {
                this.getWords();
                this.message = '단어가 추가 되었습니다.';
                this.showMessage = true;
            })
            .catch((error) => {
                console.log(error);
                this.getWords();
            });
    },
    initForm() {
        this.addWordForm.word = '';
        this.addWordForm.parts = '';
        this.addWordForm.mean = '';
        // this.editForm.id = '';
        // this.editForm.title = '';
        // this.editForm.author = '';
        // this.editForm.read = [];
    },
    onSubmit(evt) {
        evt.preventDefault();
        this.$refs.addWordModal.hide();
        var addData = new Object() ;
        addData.word = (this.addWordForm.word).toString(),
        addData.parts = (this.addWordForm.parts).toString(),
        addData.mean = (this.addWordForm.mean).toString()
        this.addWords(JSON.stringify(addData));
        this.initForm();
    },
    onReset(evt) {
        evt.preventDefault();
        this.$refs.addWordModal.hide();
        this.initForm();
      },
    editBook(book) {
        this.editForm = book;
    },
    onSubmitUpdate(evt) {
        evt.preventDefault();
        this.$refs.editBookModal.hide();
        let read = false;
        if (this.editForm.read[0]) read = true;
        const payload = {
            title: this.editForm.title,
            author: this.editForm.author,
            read,
        };

        this.updateBook(payload, this.editForm.id);
    },
    updateBook(payload, bookID) {
        const path = `http://127.0.0.1:5000/books/${bookID}`;
        axios.put(path, payload)
            .then(() => {
                this.getBooks();
                this.message = 'Book updated!';
                this.showMessage = true;
            })
            .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                this.getBooks();
            });
      },
    onResetUpdate(evt) {
        evt.preventDefault();
        this.$refs.editBookModal.hide();
        this.initForm();
        this.getBooks(); // why?
    },
    removeBook(bookID) {
        const path = `http://127.0.0.1:5000/books/${bookID}`;
        axios.delete(path)
            .then(() => {
                this.getBooks();
                this.message = 'Book removed!';
                this.showMessage = true;
            })
            .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                this.getBooks();
            });
    },
    onDeleteBook(book) {
        this.removeBook(book.id);
    },
  },
  created() {
    this.getWords();
  },
};
</script>