# Quran Semantic Search [Flask RESTful API]

## Setup

After cloning, refer to this repository folder, and run the following command (_Requires Python3 and the package installer for Python (pip) to run_):

```bash
sh build.sh
```

## How to use 

1. Most Similar Words
```bash
curl --header "Content-Type: application/json" --request POST --data '{"word": "ضيزى"}' http://0.0.0.0:5000/similar-word
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