
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv('TOKEN')
USERNAME = getenv('USERNAME')
PIXELA_URL = "https://pixe.la/"

r = requests.post(PIXELA_URL + "v1/users", json={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
})
print(r.text)


Dear Scientific Visual Team,

My name is Stanislav Muravyev, I finished 42Lausanne about a month ago, and upon one of my recent visits to the school I saw your announcement for the Junior Python Developer position. Having asked around - apparently the notice has been up for about a week - so I truly hope you are still accepting applications.

Since you haven't mentioned whether you'd prefer a motivation letter, CV, or a more traditional application, I'll keep things simple: here's a quick introduction, my CV, and links to some of my projects.

Over the past 7 years on the job market, I've explored a variety of roles before finding my passion in development. A few fortunate events led me to becoming a Teaching Assistant for an introductory Python course at EHL Hospitality Business School - essentially opening the gates into programming. Fast-forward about 3 years later: I discovered, applied to, and finished 42 - which gave me the necessary computer science knowledge to quickly adapt and learn new tools. 

This journey hasn't been only Python - it's been fueled some newly found passions. I was always been a video game enthusiast, I wanted to learn hands-on how games are made - I participated in GameJams and explored game engines such as Godot and Unreal, including dipping my toes for a second into Blender.

In my current role of LMS Coordinator, I've been using Python for over a year now to collect data from our Learning Management System (LMS) and analyze it to get insights into different activities the university's faculty and students engage with the most, which allowed me to integrate a programming to a job which is not originally a development role. (I am not at liberty to show those projects as they contain confidential student data - and cannot be shared, I'll be glad to talk about the tools and methods I used though!)

Here are some links where you'll find some of my work:

    Github - most projects are on display here - if it is specifically Python you are interested in, you should check out python100days challenge that I am currently undergoing - it is being committed to every day, it may seem basic - but I took it up as an exploration / dedication challenge.
    Plant-o-mancer: Godot Game Engine, GameJam42 2024, 3rd place
    Speed-o-flyght: Godot Game Engine, GameJam42 2025, 1st place

Fun fact about me: There is something weirdly satisfying in Object Oriented Programming - I feel like it helps me structure my ideas and make them scalable from the get go - creating intricately thought-out classes over procedural programs brings a whole new level of fulfillment.

Looking at what Scientific Visual does and the role requirements - really inspired me to apply and to hope that I could become a part of your team. Fingers crossed, my existing experience would be a sufficient stepping stone to learn much more from your team and to contribute as effectively as possible to your projects.

I appreciate your time and attention brought to my application, I'm available for an interview at any time and I'll happily go into more detail about anything of the above. You will find my CV attached to this e-mail.

Best regards,

Stanislav Muravyev