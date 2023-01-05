<template>
    <div style="width:30%; margin: auto;">
        <b-button-group style="margin-bottom:20px;">
            <b-button :pressed="true" variant="success" value="0" v-on:click="changeType(0)" style="margin-right: 15px;"> 단어 </b-button> 
            <b-button :pressed="false" variant="success" value="1" v-on:click="changeType(1)"> 뜻 </b-button>
        </b-button-group>
      
        <div v-show="questionIndex < length">
            <b-card style="max-width: 100%;" class="mb-2">
                <div v-for="(item, index) in allQuestion">
                    <div v-show="index === questionIndex">
                        <h2 style="margin-bottom:15px;">{{ item }}</h2>
                        <input type="text" v-on:input="updateAnswer" placeholder="답을 입력하세요">
                    </div>
                </div>

                <b-button-group style="margin-top: 25px;">
                    <b-button  class="btn btn-warning btn-sm" v-if="questionIndex > 0" variant="primary" v-on:click="prev">
                        이전
                    </b-button>
                    <b-button  class="btn btn-warning btn-sm" v-on:click="next" variant="primary">
                        다음
                    </b-button>
                </b-button-group>
            </b-card>
        </div>

        <div>
            <div v-show="questionIndex === length">
                <h2>
                    테스트가 끝났습니다!
                </h2>
                <p>
                    당신의 점수는 : {{ score() }} / {{length }}
                </p>
                <b-button :pressed="false" variant="success" v-on:click="reset()"> 초기화 </b-button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
        quiz: [],
        answer : [],
        word: [],
        idiom: [],
        allQuestion : [],
        allAnswers : [],
        type : 0,
        length: 0,
        questionIndex: 0,
        userResponses: Array(this.length).fill(false)
    };
  },
  created() {
    this.getExam();
  },
  methods: {
    changeType(e) {
        this.type = parseInt(e);
        this.reset();
    },
    updateAnswer(event) {
        this.userResponses[this.questionIndex] = event.target.value;
    },
    next() {
      this.questionIndex++;
    },
    prev() {
      this.questionIndex--;
    },
    reset(){
        this.allAnswers = [];
        this.allQuestion = [];
        this.questionIndex = 0;
        this.getExam();
    },
    score() {
        var score = 0;
        if (this.questionIndex >= this.length) {
            for (var i in this.allAnswers) {
                if (this.allAnswers[i] == this.userResponses[i]) {
                    score++;
                }
            }
            return score;
        }
        return false;
    },  
    getExam() {
        const path = 'http://127.0.0.1:5000/exam';
        axios.get(path)
        .then((res) => {
            this.word = Object.values(res.data['word']);
            this.idiom = Object.values(res.data['idiom']);
        }).then(()=>{
            this.length = this.word.length + this.idiom.length;
            var queType = this.type ? 'word' : 'mean';
            var ansType = this.type ? 'mean' : 'word';

            for (var i in this.word) {
                this.allQuestion.push(this.word[i][queType]);
                this.allAnswers.push(this.word[i][ansType]);
            }

            for (var i in this.idiom) {
                this.allQuestion.push(this.idiom[i][queType]);
                this.allAnswers.push(this.idiom[i][ansType]);
            }
        }).catch((error) => {
            console.error(error);
        });
        } 
    }
};
</script>