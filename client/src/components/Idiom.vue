<template>
  <div class="container">
    <div class="row">
      <div>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Resource</button>
        <br><br>
        <!-- 
        <div class="btn-group" role="group">
            <button type="button" class="btn btn-warning btn-sm" v-b-modal.book-update-modal @click="editBook(book)">
                Update
            </button>
            <button type="button" class="btn btn-danger btn-sm" @click="onDeleteBook(book)"> 
                Delete
            </button>
        </div> -->

        <b-table
          id="my-table"
          :items="volt"
          :fields="fields"
          :per-page="perPage"
          :current-page="currentPage"
          small
          style="width:60%; margin: auto;"
        >
        
        </b-table>
<!--         
        <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-table"
        ></b-pagination> -->

      </div>
    </div>
    
    <b-modal ref="addBookModal" id="book-modal" title="Add a new book" hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
            <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
                <b-form-input id="form-title-input" type="text" v-model="addBookForm.title" required placeholder="Enter title">
                </b-form-input>
            </b-form-group>

            <b-form-group id="form-author-group" label="Author:" label-for="form-author-input">
                <b-form-input id="form-author-input" type="text" v-model="addBookForm.author" required placeholder="Enter author">
                </b-form-input>
            </b-form-group>

            <b-form-group id="form-read-group">
                <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
                <b-form-checkbox value="true">Read?</b-form-checkbox>
                </b-form-checkbox-group>
            </b-form-group>

            <b-button-group>
                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
            </b-button-group>
      </b-form>
    </b-modal>

    <b-modal ref="editBookModal" id="book-update-modal" title="Update" hide-footer>
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
            <b-form-group id="form-title-edit-group" label="Title:" label-for="form-title-edit-input">
                <b-form-input id="form-title-edit-input" type="text" v-model="editForm.title" required placeholder="Enter title">
                </b-form-input>
            </b-form-group>
            
            <b-form-group id="form-author-edit-group" label="Author:" label-for="form-author-edit-input">
                <b-form-input id="form-author-edit-input" type="text" v-model="editForm.author" required placeholder="Enter author">
                </b-form-input>
            </b-form-group>

            <b-form-group id="form-read-edit-group">
                <b-form-checkbox-group v-model="editForm.read" id="form-checks">
                <b-form-checkbox value="true">Read?</b-form-checkbox>
                </b-form-checkbox-group>
            </b-form-group>

        <b-button-group>
            <b-button type="submit" variant="primary">Update</b-button>
            <b-button type="reset" variant="danger">Cancel</b-button>
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
      volt: [],
      perPage: 15,
      currentPage: 1,
      fields: [
          { key: 'idiom', label: '숙어'},
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
  methods: {
    editItem(item) { console.log(item); },
    getBooks() {
        const path = 'http://192.168.43.58:5000/word';
        axios.get(path)
            .then((res) => {
                this.volt = JSON.parse(res.data.volt);
            })
            .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
            });
    },
    addBook(payload) {
        const path = 'http://192.168.43.58:5000/word';
        axios.post(path, payload)
            .then(() => {
                this.getBooks();
                this.message = 'Book added!';
                this.showMessage = true;
            })
            .catch((error) => {
                // eslint-disable-next-line
                console.log(error);
                this.getBooks();
            });
    },
    initForm() {
        this.addBookForm.title = '';
        this.addBookForm.author = '';
        this.addBookForm.read = [];
        this.editForm.id = '';
        this.editForm.title = '';
        this.editForm.author = '';
        this.editForm.read = [];
    },
    onSubmit(evt) {
        evt.preventDefault();
        this.$refs.addBookModal.hide();

        let read = false;
        if (this.addBookForm.read[0]) read = true;

        const payload = {
            title: this.addBookForm.title,
            author: this.addBookForm.author,
            read, // property shorthand
        };

        this.addBook(payload);
        this.initForm();
    },
    onReset(evt) {
        evt.preventDefault();
        this.$refs.addBookModal.hide();
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
        const path = `http://192.168.43.58:5000/books/${bookID}`;
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
        const path = `http://192.168.43.58:5000/books/${bookID}`;
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
    this.getBooks();
  },
};
</script>