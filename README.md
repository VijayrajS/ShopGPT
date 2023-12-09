<p align="center">
 <h1 align="center"> 🛍️ ShopGPT 🛍️ </h1>
 <h3 align="center"> An AI-revamped shopping experience </h3>
 <p align="center"> A LLM-assisted Amazon shopping assistant that simplifies reviewing online feedback, helping to analyze product summaries and gain better insight to advise on Amazon purchases. </p>

## 🌐 Motivation

Reviews play a central role in the path to purchase, and many consumers don’t just skim them before purchasing or passing on a product. 53% of users within the age group 18-34 read Amazon review for more than 10 minutes before deciding to buy a product. It is also useful to compare products in terms of user reviews side-by-side to appreciate their strengths, weaknesses and other related issues, as well as, interpret reviews based on personalized requirements.

## 📕 System Architecture

A high-level design for the proposed system is presented below:

![HLD](README_media/HLD.png "High-level System Design")

### Key Components:

Our key components all use the OpenAI API, with GPT3.5-turbo as a base model for AI-driven predictions.

* **Prompt Classifier** : Classifies whether the user wants a summary, comparison or recommendation.
* **Review Summarizer** : Summarizes multiple reviews in JSON format and returns structured product review summaries.
* **Product Comparisons**: Performs structured comparison across pairs of products. 
* **Personalized Product Recommendations**: Given a user input, generates product recommendations by comparison of summaries guided by the user's requirements. 

## 🚀 Technology Stack:
  
 - **Frontend**: <img src="https://pypi-camo.global.ssl.fastly.net/a95ef5913dc4cc84d2155ff690a0fa0d4c33d7e2/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f67726164696f2d6170702f67726164696f2f6d61696e2f726561646d655f66696c65732f67726164696f2e737667" height="25" width="100"> 
 - **GPT 3.5 API**: <img src="https://www.webfx.com/wp-content/uploads/2023/07/what-is-openai.png" height="40" width="80">
 - **Database**: <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/MongoDB_Logo.svg" height="25" width="100">

 ## 🗄️ Dataset Used and Data Storage


## ✍️ Instructions to Run

## Demo (YouTube)
 [![hurriCARE](https://img.youtube.com/vi/5UYiMiq8xxQ/0.jpg)](https://www.youtube.com/watch?v=5UYiMiq8xxQ)