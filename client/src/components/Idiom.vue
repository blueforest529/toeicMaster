<template>
  <div class="container">
        <div>
            <alert :message="message" v-if="showMessage"></alert>
            <button type="button" class="btn btn-success btn-sm" v-b-modal.idiom-add-modal>숙어 추가</button>
            <div style="width:400px; margin: auto; margin-bottom: 40px;">
                <b-form-group label="검색" label-for="filter-input" label-cols-sm="3"
                    label-align-sm="right" label-size="sm" class="mb-0">
                    <b-input-group size="sm">
                        <b-form-input id="filter-input" v-model="filter" type="search" ></b-form-input>
                    </b-input-group>
                </b-form-group>
            </div>
            <b-table id="my-table" :items="idioms" :fields="fields" :filter="filter"
                :per-page="perPage" :current-page="currentPage" 
                small style="width:60%; margin: auto;">
                <template #cell(actions)="row">
                    <button type="button" class="btn btn-warning btn-sm" @click="onEditSetting(row.item)" 
                    v-b-modal.idiom-edit-modal style="margin-right : 15px;">
                        수정
                    </button>
                    <b-button class="btn btn-warning btn-sm" @click="deleteIdiom(row.item)">
                        삭제
                    </b-button>
                </template>
            </b-table>
            <div style="width:400px; margin: auto; margin-top: 40px; margin-bottom: 40px;">
                <b-pagination v-model="currentPage" :total-rows="totalRows" 
                :per-page="perPage" align="fill" size="sm" class="my-0"></b-pagination>
            </div>        
        </div>

        <b-modal ref="addIdiomModal" id="idiom-add-modal" title="숙어 추가" hide-footer>
            <b-form @submit="onAddSubmit" @reset="onAddReset" class="w-100">
                <b-form-group id="form-idiom-group" label="숙어 :" label-for="form-idiom-input"> 
                    <b-form-input id="form-idiom-input" type="text" v-model="addIdiomForm.idiom" required>
                    </b-form-input>
                </b-form-group>

                <b-form-group id="form-mean-group" label="뜻 :" label-for="form-mean-input" style="margin-top: 15px;">
                    <b-form-input id="form-mean-input" type="text" v-model="addIdiomForm.mean" required>
                    </b-form-input>
                </b-form-group>

                <b-button-group style="margin-top: 25px;">
                    <b-button type="submit" variant="primary">저장</b-button>
                    <b-button type="reset" variant="danger">취소</b-button>
                </b-button-group>
            </b-form>
        </b-modal>

        <b-modal ref="editIdiomModal" id="idiom-edit-modal" title="숙어 수정" hide-footer>
            <b-form @submit="onEditSubmit" @reset="onEditReset" class="w-100">
                <b-form-group id="form-idiom-group" label="숙어 :" label-for="form-idiom-input"> 
                    <b-form-input id="form-idiom-input" type="text" v-model="editIdiomForm.idiom" placeholder=""  required>
                    </b-form-input>
                </b-form-group>

                <b-form-group id="form-mean-group" label="뜻 :" label-for="form-mean-input" style="margin-top: 15px;">
                    <b-form-input id="form-mean-input" type="text" v-model="editIdiomForm.mean" required>
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
        idioms: [],
        totalRows: 1,
        currentPage: 1,
        perPage: 10,
        filter: null,
        fields: [
            { key: 'idiom', label: '단어'},
            { key: 'mean', label: '뜻'},
            { key: 'actions', label: 'Actions' }
          ],
        addIdiomForm: {
          idiom: '',
          mean: ''
        },
        editIdiomForm: {
          seq : 0,
          idiom: '',
          mean: ''
        }, 
        message: '',
        showMessage: false
    };
  },
  components: {
    alert: Alert,
  },
  created() {
    this.getIdioms();
  },
  methods: {
    getIdioms() {
        const path = 'http://127.0.0.1:5000/idiom';
        axios.get(path)
            .then((res) => {
                this.idioms = res.data;
                this.totalRows = res.data.length;
            })
            .catch((error) => {
                console.error(error);
            });
    },
    initForm() {
        this.addIdiomForm.idiom = '';
        this.addIdiomForm.mean = '';
        this.editIdiomForm.idiom = '';
        this.editIdiomForm.mean = '';
        this.editIdiomForm.seq = 0;
    },
    onAddSubmit(evt) {
        evt.preventDefault();
        this.$refs.addIdiomModal.hide();
        var addData = new Object() ;
        addData.idiom = (this.addIdiomForm.idiom).toString(),
        addData.mean = (this.addIdiomForm.mean).toString()
        this.addIdioms(JSON.stringify(addData));
        this.initForm();
    },
    onAddReset(evt) {
        evt.preventDefault();
        this.$refs.addIdiomModal.hide();
        this.initForm();
    },
    addIdioms(addData) {
        const path = 'http://127.0.0.1:5000/idiom';
        axios.post(path, addData)
            .then(() => {
                this.getIdioms();
                this.messageShow('단어가 추가 되었습니다.');
            })
            .catch((error) => {
                console.log(error);
                this.getIdioms();
            });
    },
    onEditReset(evt) {
        evt.preventDefault();
        this.$refs.editIdiomModal.hide();
        this.initForm();
    },
    onEditSetting(item, index, evt) {
        this.editIdiomForm.idiom = item.idiom;
        this.editIdiomForm.mean = item.mean;
        this.editIdiomForm.seq = item.seq;
    },
    onEditSubmit(evt) {
        evt.preventDefault();
        this.$refs.editIdiomModal.hide();
        var editData = new Object() ;
        editData.idiom = (this.editIdiomForm.idiom).toString(),
        editData.mean  = (this.editIdiomForm.mean).toString()
        this.editIdioms(JSON.stringify(editData));
        this.initForm();
    },
    editIdioms(editData) {
        const path = 'http://127.0.0.1:5000/idiom/'+this.editIdiomForm.seq;
        axios.put(path, editData)
            .then(() => {
                this.getIdioms();
                this.messageShow('단어가 수정 되었습니다.');
            })
            .catch((error) => {
                console.log(error);
                this.getIdioms();
            });
    },
    deleteIdiom(item) {
        const path = 'http://127.0.0.1:5000/idiom/'+item.seq;
        axios.delete(path)
            .then(() => {
                this.messageShow('단어가 삭제 되었습니다.');  
                this.getIdioms();
            })
            .catch((error) => {
                console.error(error);
                this.getIdioms();
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