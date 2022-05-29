# Quran Semantic Search [Flask RESTful API]

## Overview 

This Flask REST API allows you to search (extract predictions) from a word embeddings model pre-trained on an Arabic Islamic Corpus (+237 Million words).

You can obtain:
* The top 10 most similar words and scores for a given word.
* The top 10 most similar verses for a given query.

## Setup

1. Clone the repository and head to main folder.
2. Download [`ksucca_full_cbow`](https://drive.google.com/u/0/uc?id=1rZiOKy71Z_WycxnOG9bwrNoAc4ziGo_n) and place it in the `data` folder.
3. Head/Refer again to this main folder, and run the following command:
```bash
sh build.sh
```
<details> <summary>Helpful notes</summary>

* The bash file will require Python3 and the package installer for Python (pip) to run.

* Refering/Heading means to `cd` into the folder on your terminal.
</details>

## How to use 

### Without Docker

1. Head to main folder.
2. Run `python3 app.py` to open locally.
3. To call the API use `curl` on your terminal or test on [POSTMAN](https://www.postman.com/).

#### Examples of using `curl`

1. To get the most similar words by a word
```bash
curl --header "Content-Type: application/json" --request GET --data http://0.0.0.0:5000/similar-word/ضيزى
```
```json
{
  "results": [
    [
      "جائره", 
      0.7013014554977417
    ], 
    [
      "ضيزي", 
      0.638590395450592
    ], 
    [
      "خاسره", 
      0.5436197519302368
    ], 
    [
      "جائره", 
      0.5415328145027161
    ], 
    [
      "قسمه", 
      0.527427077293396
    ], 
    [
      "الكم", 
      0.4947861433029175
    ], 
    [
      "ضيزي", 
      0.46748870611190796
    ], 
    [
      "عوجاء", 
      0.46708834171295166
    ], 
    [
      "العلي", 
      0.4437080919742584
    ], 
    [
      "والليل", 
      0.4276253581047058
    ]
  ]
}
```

2. To get the most similar verses by a query
```bash
curl --header "Content-Type: application/json" --request GET http://0.0.0.0:5000/similar-verse/شجاعة
```
```json
{
  "results": [
    "إنه فكر وقدر", 
    "خاشعة أبصارهم ترهقهم ذلة ذلك اليوم الذي كانوا يوعدون", 
    "خاشعة أبصارهم ترهقهم ذلة وقد كانوا يدعون إلى السجود وهم سالمون", 
    "علمه شديد القوى", 
    "إذ جعل الذين كفروا في قلوبهم الحمية حمية الجاهلية فأنزل الله سكينته على رسوله وعلى المؤمنين وألزمهم كلمة التقوى وكانوا أحق بها وأهلها وكان الله بكل شيء عليما", 
    "فاصبر كما صبر أولو العزم من الرسل ولا تستعجل لهم كأنهم يوم يرون ما يوعدون لم يلبثوا إلا ساعة من نهار بلاغ فهل يهلك إلا القوم الفاسقون", 
    "وآتيناهم من الآيات ما فيه بلاء مبين", 
    "ولا تستوي الحسنة ولا السيئة ادفع بالتي هي أحسن فإذا الذي بينك وبينه عداوة كأنه ولي حميم", 
    "قل من كان في الضلالة فليمدد له الرحمن مدا حتى إذا رأوا ما يوعدون إما العذاب وإما الساعة فسيعلمون من هو شر مكانا وأضعف جندا", 
    "وإذ قال موسى لقومه اذكروا نعمة الله عليكم إذ أنجاكم من آل فرعون يسومونكم سوء العذاب ويذبحون أبناءكم ويستحيون نساءكم وفي ذلكم بلاء من ربكم عظيم"
  ]
}
```

### With Docker

1. Head to main folder.
2. Install [Docker](https://docs.docker.com/get-docker/): `sudo snap install docker`
3. Run `docker build -t semantic-api .` to build a container called `semantic-api` from the instructions set in the current Dockerfile.
4. Run `docker run -p 5000:5000 semantic-api` to open the container locally, forwarding the request from port 5000 on the host (your computer) to port 5000 in the container.
5. To call the API use `curl` on your terminal like the previous examples or test on [POSTMAN](https://www.postman.com/).

## Sources
* [Arabic Islamic Corpus for training the Word2Vec Model](https://github.com/EyadMShokry/SearchQuranByTopic#word2vec-model)
* [Tanzil Quran text](https://tanzil.net/download/)