import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') 

import django 
django.setup() 

from myapp.models import Lesson 

lessons = {
    "Introduction": {
        "index": 1,
        "vid": "0AM35Nu5McY"
    },
    "Student Presentations I": {
        "index": 2,
        "vid": "jTtm1tgK3Vg"
    },
    "Feedback on Presentations I": {
        "index": 3,
        "vid": "osbozn9iV3g"
    },
    "Stage Manners": {
        "index": 4,
        "vid": "Cj2M-T5HTsE"
    },
    "Tempo of Speech": {
        "index": 5,
        "vid": "czYtzi833js"
    },
    "Some Reasons for Mishearing": {
        "index": 6,
        "vid": "6NKAmR6TmuA"
    },
    "Topics for Presentations II": {
        "index": 7,
        "vid": "PvZBWHpYCEg"
    },
    "Message": {
        "index": 8,
        "vid": "ieEaXXy8R5A"
    },
    "Tables, Charts, Graphs": {
        "index": 9,
        "vid": "xVWKPSIBDIQ"
    },
    "Power Point Slides": {
        "index": 10,
        "vid": "1GZ3OeOcaVA"
    },
    "Criteria for Evaluation": {
        "index": 11,
        "vid": "iQcxtBnT34A"
    },
    "Student Presentations II": {
        "index": 12,
        "vid": "OO1tWM23xZ8"
    },
    "Feedback on Presentation II": {
        "index": 13,
        "vid": "KLhNMF1-yLc"
    },
    "Topics for Presentation III": {
        "index": 14,
        "vid": "z-ueNH7RFfM"
    },
    "Mod-01 Lec-15 On \"Saying 'Please!' \"": {
        "index": 15,
        "vid": "Za1ZFQq8Lag"
    },
    "English Rhythm I": {
        "index": 16,
        "vid": "Ce0eHcyST3k"
    },
    "English Rhythm II": {
        "index": 17,
        "vid": "qa_wmCE_gYc"
    },
    "Mod-01 Lec-18 Phrasal Pause in English I": {
        "index": 18,
        "vid": "0esjrK4qbT4"
    },
    "Phrasal Pause in English II": {
        "index": 19,
        "vid": "ZR7mJyZVIVU"
    },
    "Units of Time, Weight, Distance": {
        "index": 20,
        "vid": "QKMim7dEECQ"
    },
    "Stress in English I": {
        "index": 21,
        "vid": "_KHtfvob4j4"
    },
    "Stress in English II": {
        "index": 22,
        "vid": "rEzux4C-hX8"
    },
    "Stress in English III": {
        "index": 23,
        "vid": "rtAOMpCPpi0"
    },
    "Stress in English IV": {
        "index": 24,
        "vid": "DfPbxuDBhXg"
    },
    "Mod-01 Lec-25 Stress in English V": {
        "index": 25,
        "vid": "81L2IialxHo"
    },
    "Mod-01 Lec-26 Stress in English VI": {
        "index": 26,
        "vid": "lgBau4CxA0Y"
    },
    "Mod-01 Lec-27 Student Presentations III": {
        "index": 27,
        "vid": "dMQTLsq_wrk"
    },
    "Mod-01 Lec-28 Student Presentations III": {
        "index": 28,
        "vid": "J1F5-Taa-Gw"
    },
    "Mod-01 Lec-29 Student Presentations III": {
        "index": 29,
        "vid": "oALZfbtz980"
    },
    "Mod-01 Lec-30 Student Presentations III": {
        "index": 30,
        "vid": "hwXku1CjVdQ"
    },
    "Mod-01 Lec-31 Some Different Sounds": {
        "index": 31,
        "vid": "sJgEn9om8dM"
    },
    "Mod-01 Lec-32 Some \"Difficult\" Sounds in English": {
        "index": 32,
        "vid": "6XUSa5HWDmo"
    },
    "Mod-01 Lec-34 Some \"Consonants\" in English": {
        "index": 33,
        "vid": "XspcekJ9GaQ"
    },
    "Mod-01 Lec-35 Student Presentations IV": {
        "index": 34,
        "vid": "NCTqriJNAe8"
    },
    "Mod-01 Lec-36 Student Presentation IV": {
        "index": 35,
        "vid": "N-JVzsXUtZ8"
    },
    "Mod-01 Lec-37 Feedback on Student Presentation IV": {
        "index": 36,
        "vid": "Pn277N5gxCI"
    },
    "Mod-01 Lec-38 Final Tips": {
        "index": 37,
        "vid": "ntSNdQtBZh4"
    },
    "Aiming For Excellence: Developing Potential And Self-Actualisation": {
        "index": 38,
        "vid": "W7QgPtO7NRE"
    },
    "Human Perceptions: Understanding People": {
        "index": 39,
        "vid": "z6uFihRyvW4"
    }
}

def populate():

    for title, value in lessons.items():
        Lesson.objects.create(title=title, video_id=value['vid'])


if __name__ == "__main__":
    print('Populating...')
    populate()
    print('Complete!')                                