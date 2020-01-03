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
        var trivia = document.getElementById("trivia");
        this.setUpTrivia(trivia);

        console.log('Received Event: ' + id);
    },

    setUpTrivia: function(element) {
        var question = document.createElement("textarea");
        question.setAttribute("id", "trivia_question");
        question.setAttribute("class", "trivia_question");
        element.appendChild (question);
    }
};

app.initialize();

