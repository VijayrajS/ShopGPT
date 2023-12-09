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
  
 - **Frontend**: <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fpypi.org%2Fproject%2Fgradio%2F&psig=AOvVaw0oWsRaCzjelPeqPCOLH15v&ust=1702165921188000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPiUwquEgYMDFQAAAAAdAAAAABAD"/> 
 - **GPT 3.5 API**: <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.webfx.com%2Fblog%2Fmarketing%2Fwhat-is-openai%2F&psig=AOvVaw1etKLlLvGzQyHICz1mVx92&ust=1702165970241000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLj4rMqEgYMDFQAAAAAdAAAAABAD" height="40" width="120">
 - **Database**: <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.m.wikipedia.org%2Fwiki%2FFile%3AMongoDB_Logo.svg&psig=AOvVaw2pMnsbtBJip9Lvpv-cMmFJ&ust=1702166079596000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOiIxfaEgYMDFQAAAAAdAAAAABAD" height="25" width="100">

 ## 🗄️ Dataset Used and Data Storage


## ✍️ Instructions to Run

## Demo (YouTube)
 [![hurriCARE](https://img.youtube.com/vi/5UYiMiq8xxQ/0.jpg)](https://www.youtube.com/watch?v=5UYiMiq8xxQ)