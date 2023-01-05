<template>
  <div class="container">
        <div>
            <alert :message="message" v-if="showMessage"></alert>
            <button type="button" class="btn btn-success btn-sm" v-b-modal.word-add-modal>단어 추가</button>
            <div style="width:400px; margin: auto; margin-bottom: 40px;">
                <b-form-group label="검색" label-for="filter-input" label-cols-sm="3"
                    label-align-sm="right" label-size="sm" class="mb-0">
                    <b-input-group size="sm">
                        <b-form-input id="filter-input" v-model="filter" type="search" ></b-form-input>
                    </b-input-group>
                </b-form-group>
            </div>

            <b-table id="my-table" :items="words" :fields="fields" :filter="filter"
                :per-page="perPage" :current-page="currentPage" 
                small style="width:60%; margin: auto;">
                <template #cell(actions)="row">
                    <button type="button" class="btn btn-warning btn-sm" @click="onEditSetting(row.item)" 
                    v-b-modal.word-edit-modal style="margin-right : 15px;">
                        수정
                    </button>
                    <b-button class="btn btn-warning btn-sm" @click="deleteWord(row.item)">
                        삭제
                    </b-button>
                </template>
            </b-table>

            <div style="width:400px; margin: auto; margin-top: 40px; margin-bottom: 40px;">
                <b-pagination v-model="currentPage" :total-rows="totalRows" 
                :per-page="perPage" align="fill" size="sm" class="my-0"></b-pagination>
            </div>
        </div>

        <b-modal ref="addWordModal" id="word-add-modal" title="단어 추가" hide-footer>
            <b-form @submit="onAddSubmit" @reset="onAddReset" class="w-100">
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
                    <b-button type="submit" variant="primary">저장</b-button>
                    <b-button type="reset" variant="danger">취소</b-button>
                </b-button-group>
            </b-form>
        </b-modal>

        <b-modal ref="editWordModal" id="word-edit-modal" title="단어 수정" hide-footer>
            <b-form @submit="onEditSubmit" @reset="onEditReset" class="w-100">
                <b-form-group id="form-word-group" label="단어 :" label-for="form-word-input"> 
                    <b-form-input id="form-word-input" type="text" v-model="editWordForm.word" placeholder=""  required>
                    </b-form-input>
                </b-form-group>

                <b-form-group id="form-parts-group" label="품사 :" label-for="form-parts-input" style="margin-top: 15px;">
                    <b-form-input id="form-parts-input" type="text" v-model="editWordForm.parts" required>
                    </b-form-input>
                </b-form-group>

                <b-form-group id="form-mean-group" label="뜻 :" label-for="form-mean-input" style="margin-top: 15px;">
                    <b-form-input id="form-mean-input" type="text" v-model="editWordForm.mean" required>
                    </b-form-input>
                </b-form-group>

                <b-button-group style="margin-top: 25px;">
                    <b-button type="submit" variant="primary">저장</b-button>
                    <b-button type="reset" variant="danger">취소</b-button>
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
        totalRows: 1,
        currentPage: 1,
        perPage: 10,
        filter: null,
        fields: [
            { key: 'word', label: '단어'},
            { key: 'parts', label: '품사'},
            { key: 'mean', label: '뜻'},
            { key: 'actions', label: 'Actions' }
          ],
        addWordForm: {
          word: '',
          parts: '',
          mean: ''
        },
        editWordForm: {
          seq : 0,
          word: '',
          parts: '',
          mean: ''
        }, 
        message: '',
        showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  created() {
    this.getWords();
  },
  methods: {
    getWords() {
        const path = 'http://127.0.0.1:5000/word';
        axios.get(path)
            .then((res) => {
                this.words = res.data;
                this.totalRows = res.data.length;
            })
            .catch((error) => {
                console.error(error);
            });
    },
    initForm() {
        this.addWordForm.word = '';
        this.addWordForm.parts = '';
        this.addWordForm.mean = '';
        this.editWordForm.word = '';
        this.editWordForm.parts = '';
        this.editWordForm.mean = '';
        this.editWordForm.seq = 0;
    },
    onAddSubmit(evt) {
        evt.preventDefault();
        this.$refs.addWordModal.hide();
        var addData = new Object() ;
        addData.word = (this.addWordForm.word).toString(),
        addData.parts = (this.addWordForm.parts).toString(),
        addData.mean = (this.addWordForm.mean).toString()
        this.addWords(JSON.stringify(addData));
        this.initForm();
    },
    onAddReset(evt) {
        evt.preventDefault();
        this.$refs.addWordModal.hide();
        this.initForm();
    },
    addWords(addData) {
        const path = 'http://127.0.0.1:5000/word';
        axios.post(path, addData)
            .then(() => {
                this.getWords();
                this.messageShow('단어가 추가 되었습니다.');
            })
            .catch((error) => {
                console.log(error);
                this.getWords();
            });
    },
    onEditReset(evt) {
        evt.preventDefault();
        this.$refs.editWordModal.hide();
        this.initForm();
    },
    onEditSetting(item, index, evt) {
        this.editWordForm.word = item.word;
        this.editWordForm.parts = item.parts;
        this.editWordForm.mean = item.mean;
        this.editWordForm.seq = item.seq;
    },
    onEditSubmit(evt) {
        evt.preventDefault();
        this.$refs.editWordModal.hide();
        var editData = new Object() ;
        editData.word = (this.editWordForm.word).toString(),
        editData.parts = (this.editWordForm.parts).toString(),
        editData.mean = (this.editWordForm.mean).toString()
        this.editWords(JSON.stringify(editData));
        this.initForm();
    },
    editWords(editData) {
        const path = 'http://127.0.0.1:5000/word/'+this.editWordForm.seq;
        axios.put(path, editData)
            .then(() => {
                this.getWords();
                this.messageShow('단어가 수정 되었습니다.');
            })
            .catch((error) => {
                console.log(error);
                this.getWords();
            });
    },
    deleteWord(item) {
        const path = 'http://127.0.0.1:5000/word/'+item.seq;
        axios.delete(path)
            .then(() => {
                this.getWords();
                this.messageShow('단어가 삭제 되었습니다.');
            })
            .catch((error) => {
                console.error(error);
                this.getWords();
            });
    },
    messageShow(msg) {
        this.message = msg;
        this.showMessage = true;
        
        sleep(3000).then(() => {
            this.message = '';
            this.showMessage = false;
        });
    }}
};

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}
</script>