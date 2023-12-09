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

Our key components all use the OpenAI API, with **GPT3.5-turbo** as a base model for AI-driven predictions.

* **Prompt Classifier** : Classifies whether the user wants a summary, comparison or recommendation. Internal backend component.
* **Review Summarizer** : Summarizes multiple reviews in JSON format and returns structured product review summaries. An example is shown below:
  
  [![summarization-gif.gif](https://i.postimg.cc/DyfKb6HC/summarization-gif.gif)](https://postimg.cc/8sYY2R1W)
  
* **Product Comparisons**: Performs structured comparison across pairs of products. An example is shown below:
  
  [![comparison.gif](https://i.postimg.cc/JnQ2rVrR/comparison.gif)](https://postimg.cc/HcV2zN8N)
  
* **Personalized Product Recommendations**: Given a user input, generates product recommendations by comparison of summaries guided by the user's requirements. An example is shown below:
  
  [![reco.gif](https://i.postimg.cc/nrgYZ0DH/reco.gif)](https://postimg.cc/8fdrmd43)

* **Keyword Extraction**: Extract keywords from the summarized reviews and allow to filter the summary according to a keyword. An example is shown below:

  [![keywords.gif](https://i.postimg.cc/xj5CXttC/keywords.gif)](https://postimg.cc/t71yft0Q)

## 🚀 Technology Stack:
  
 - **Frontend**: <img src="https://pypi-camo.global.ssl.fastly.net/a95ef5913dc4cc84d2155ff690a0fa0d4c33d7e2/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f67726164696f2d6170702f67726164696f2f6d61696e2f726561646d655f66696c65732f67726164696f2e737667" height="25" width="100"> 
 - **GPT 3.5 API**: <img src="https://www.webfx.com/wp-content/uploads/2023/07/what-is-openai.png" height="50" width="80">
 - **Database**: <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/MongoDB_Logo.svg" height="30" width="100">

 ## 🗄️ Dataset Used and Data Storage

We use the [Amazon Review Dataset](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/) Provided by UCSD (2018) with 233.1 million reviews. The dataset contains reviews in the range May 1996 - Oct 2018. We host a subset of this dataset in JSON format, along with associated metadata on MongoDB Atlas. 

## ✍️ Instructions to Run

- **Clone the repository**: `git clone https://github.com/VijayrajS/ShopGPT`
- **Create a Python virtual environment:** Follow instructions from [virtualenv Documentation](https://docs.python.org/3/library/venv.html)
- **Install necessary Python packages**: `pip install -r requirements.txt`
- **Set up your own OpenAI API key**: Follow instructions from [OpenAI API docs](https://platform.openai.com/docs/quickstart?context=python)
- **Download the dataset** from [UCSD Amazon Reviews Dataset](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/)
- **Host your Database**: Host the downloaded dataset on MongoDB Atlas.
- **Run the App Locally**: Run `python UI_v0.py`

## Demo (YouTube)
 [![hurriCARE](https://img.youtube.com/vi/5UYiMiq8xxQ/0.jpg)](https://www.youtube.com/watch?v=5UYiMiq8xxQ)
