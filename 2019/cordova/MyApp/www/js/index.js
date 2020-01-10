/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

var questions = [
    {
        question: "how many times a day do muslims need to pray?",
        wrong:[
            "3",
            "0",
            "8"
        ],
        right: "5"
    },
    {
        question: "which of the following is a companion (sahaba) of the prophet Muhammad SAW?",
        wrong:[
            "Abd-rahma rahgul",
            "salamun al samak",
            "Quasem ibn ruman"
        ],
        right: "Khalid ibn walid"
    },
    {
        question: "which of the following is a daughter of the prophet Muhammad SAW?",
        wrong:[
            "Hadega bint Muhammad",
            "salma bint Muhammad",
            "namah bint Muhammad"
        ],
        right: "Fatimah bint Muhammad"
    }
];

// questions[0]["right_answer"]
// questions[0]["wrong_answers"][]

var app = {
    // Application Constructor
    initialize: function() {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
    },

    // deviceready Event Handler
    //
    // Bind any cordova events here. Common events are:
    // 'pause', 'resume', etc.
    onDeviceReady: function() {
        randQuestionId=Math.floor(Math.random() * questions.length);  // randomly pick a number from 0 - 3
        this.loadQuestion(questions[randQuestionId]);
    },

    loadQuestion: function(question){
        var Q=document.getElementById("trivia_question");
        Q.value=question.question;

        randAnswerId=Math.floor(Math.random() * 4);  // randomly pick a number from 0 - 3

        var A1=document.getElementById("trivia_a1");
        var A2=document.getElementById("trivia_a2");
        var A3=document.getElementById("trivia_a3");
        var A4=document.getElementById("trivia_a4");

        var answerList=[A1,A2,A3,A4];

        var lastUsedAnswer=0;
        for(var i = 0; i < 4; i++)
        (function(i){ 
            // without this function scope the loop index get incremented out of range.
            // causing the onclick event handler to run only once
            if(i==randAnswerId)
            {
                // handle the right answer
                answerList[i].innerText=question.right;
                answerList[i].onclick=function(){
                    window.alert("correct");
                };
            }
            else
            {
                // handle wrong answer
                answerList[i].innerText=question.wrong[lastUsedAnswer];
                answerList[i].onclick=function(){
                    window.alert("incorrect");
                    answerList[i].disabled=true;
                };

                lastUsedAnswer++;
            }
        })(i); // note we are passing i as an argument.
    }
};

app.initialize();

