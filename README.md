# Quran Semantic Search [Flask RESTful API]

## Setup

After cloning, refer to this repository folder, then run the following command:

```bash
sh build.sh
```
_Requires Python3 and the package installer for Python (pip) to run._

## How to use 

* Most Similar word:

```bash
curl --header "Content-Type: application/json" --request POST --data '{"word": "quran"}' http://0.0.0.0:5000/similar-word
```

Output:

```json
{
    "results": [
        [
            "koran",
            0.7388603687286377
        ],
        [
            "Qur'aan",
            0.7167584300041199
        ],
        [
            "Qur'an",
            0.7027473449707031
        ],
        [
            "Qu'ran",
            0.687604546546936
        ],
        [
            "holy_Qur'an",
            0.6662046909332275
        ],
        [
            "holy_Koran",
            0.6530247926712036
        ],
        [
            "Koran",
            0.6530128717422485
        ],
        [
            "Holy_Qur'an",
            0.6509985327720642
        ],
        [
            "Quran",
            0.6362140774726868
        ],
        [
            "Prophet_PBUH",
            0.6360219120979309
        ]
    ]
}
```
