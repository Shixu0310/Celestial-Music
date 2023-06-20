<h1 align="center">
  <img src="static\picture\logo.svg" alt="JAVClub" width="200">
</h1>

❗ | **This project is used for a python major assignment, personal work during freshman year, and may have some usefulness for other projects (will be explained clearly in the board afterwards) If there is any infringement, please contact me to remove it.**
:---: | :---
⚠️ | Because it is an assignment, so this project to show and record mainly, this is my first attempt to develop front-end, basically for learning as we go, the project omission must be a lot of places, welcome to correct! Once again (only for learning, if it involves copyright and other issues, the author immediately delete the warehouse to run away!)

## Introduction
The project is a **song preference analysis system** that crawls a specific user's Netflix data, performs the relevant processing and then visualises the data on a web page. It also includes recommending artists and song lists to users based on their preferences, as well as analysing the artist's listener user profile. There is a lot of private stuff in the project, ~~please use caution~~
![](static\picture\keainie.gif)

## Technology Included

Design language：Python + CSV + HTML + CSS + JS

Data crawlers：NeteaseCloudMusicApi + Requset + etree + json 

Data Cleaning：re + replace + join + spilt

Visualisation：Flask + Echarts + WordCloud + Html

Text Analysis：jieba2

Data storage：CSV


## Features

- Support login with NetCloud user id
- Support for querying user information for open data
- Support for visualisation of logged-in users' favourite artists
- Support for displaying the top 100 favourite songs of users
- Support for displaying user listening preference tag statistics
- Support displaying the word cloud in users' comment section and related hot review information
- Support for searching any author by author id
- Support displaying statistics on the gender and place of residence of the author's fan base
- Support to display author's creation preferences
- Support for displaying the author's top songs and top comments
- Support for suggesting songs and song lists for logged in users
- ~~There are all kinds of private stuff in the page, find it yourself~~

## TODO
- [ ] Song search page
- [ ] Song-based user group analysis
- [ ] ~~more private stuff~~
  
## DEMO
> I don't have the URL to show the online demo, so I'll download it and deploy it, Meow~( ｡ớ ₃ờ)ھ
> The following will show some basic information about the page, with simple gif to show the miles~
> (P.S. Please contact [here](mailto:bican700066@163.com) for questions/sponsorship) ~~but I don't always reply~~

<details>

  <summary>Page display (click to expand)</summary>

  ![](img\gif\login.gif)

  ![](img\gif\user.gif)

  ![](img\gif\animation_user.gif)

  ![](img\gif\artist.gif)

  ![](img\gif\animation_artist.gif)

  ![](img\gif\recommend.gif)

  ![](img\gif\logout.gif)

</details>

## Deployment

The information below may be tedious and boring, and may even contain errors, so I hope you will forgive me.~~Easy peace for dalao!╮(๑•́ ₃•̀๑)╭~~
+ The content of the deployment is divided into two sections, please read them carefully.
  
### Music 163 api deployment
The project uses the NetEase cloud api as part of the crawler, ensuring the stability of the real-time crawler while reducing the stage of user configuration of the crawler.
> For a detailed configuration process please [see here](https://github.com/Binaryify/NeteaseCloudMusicApi)

Please ensure you have/complete the following capabilities/things before deploying:
- Node.js / JavaScript Fundamentals
- Basic error reading skills
- ~~To put it bluntly, it's really just a matter of configuring the node environment (😓)~~

<details>

  <summary>Brief deployment process (click to expand)</summary>

  #### Install
```
$ git clone git@github.com:Binaryify/NeteaseCloudMusicApi.git
$ cd NeteaseCloudMusicApi
$ npm install
```

  #### Running
```shell
$ node app.js
```

The default port for server startup is **3000**, if you do not want to use port **3000**, you can use the following command : **Mac/Linux**

```shell
$ PORT=4000 node app.js
```

On **windows**, use a terminal such as **git-bash** or **cmder** to execute the following command .

```shell
$ set PORT=4000 && node app.js
```

The default host for server startup is **localhost**, if you need to change it, you can use the following command : **Mac/Linux**

```shell
$ HOST=127.0.0.1 node app.js
```

On **windows**, use a terminal such as **git-bash** or **cmder** to execute the following command .

```shell
$ set HOST=127.0.0.1 && node app.js
```
</details>

### Celestial Music Deployment

The project is using **python 3.10** and I don't know if a lower version will have any problems. A virtual environment for **py 3.10** can be created with the following statement

```shell
conda create -n music_work python=3.10
```

All are very common libraries that can be installed via pip. However, it is recommended to use a virtual environment~
> pip list
```shell
pip install pandas flask bs4 html5lib Jinja2 lxml requests jieba 
pip install wordcloud imageio matplotlib numpy
```
If there is anything you haven't covered, just pip when you get an error

## Start-up process

1. Firstly, referring to what we saw in Deployment 1, we cd to the NeteaseCloudMusicApi directory and run the following:
```shell
node app.js
```
A successful run is indicated when the following appears:
```powershell
server running @ http://localhost:3000
```

2. Open a new terminal, cd to the project folder, open the virtual environment and run the following:
```shell
python app.py
```
A successful run is indicated when the following appears:
```shell
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:5000
Press CTRL+C to quit
```
Visit [here](http://localhost:5000) in your browser (click here again once it has run successfully!!!)

## Tutorials for using the website

1. **Entering the initial login screen users can log in using their NetEase cloud id:**
   - If the user id entered is normal you can enter the user interface, **Note** because the data are crawled on site so you need to wait a while, you can check the crawling process on the **app.py** terminal.
   - Please be patient during the crawling phase ~~it's not a bug that hasn't been solved yet~~
   - If you enter the wrong user id you will be redirected to the **42** error URL ~~here's the egg~~
   - If the crawl fails, it will go to the **25252** error screen

![](img\login.png)

2. **On entering the user interface, the user can view basic operational information:**
    <details>
      <summary>Viewable information (click to expand)</summary>
      user：

      - Top 10 Listening Tags
             
      - User Avatar
        
      - Basic Information

      - Top100 Hot Music

      - Top100 My Hot Music

      - Favourite Singers Top8

      - Hotword Cloud Chart

      - Popular Reviews

    </details>


3. **Next Steps:**
   - You can select the board you want to view on the Dash Menu
   - Dash Menu can be tucked away in the top left corner
   - Top right corner has a message alert panel, a logout button and a help button
   - The gear in the bottom right corner allows you to change the colour scheme of the UI
   - Click on a singer's name under Favourite Singers Top8 to jump directly to the corresponding singer's screen
   - ~~Follow Tuffy Meow~~That's right, this is an advertisement, I'm not a 雏草姬!

![](img\user.png)

4. **Search Artist board:**
   - The search board allows you to search for an author based on their id
     - If the id is incorrect, you will be taken to the **42** error page.
     - If the crawler fails to run it will go to the **25252** error page, you can check the progress of the crawler in the terminal
     - The Favourite Singers Top8 section provides recommended authors to choose from

![](img\search.png)

5. **Recommend To You board:**
   - Recommended Songs 1~4 suggest four songs that the current user may like, based on the recommendation system of NetEase Cloud. It is based on NetEase's recommendation system. It is obtained by searching through the tag and related categories of the music the user often listens to.
   - Recommended Songs 5~8 Same as above
   - Singer Hit Song Hot Reviews recommends 10 songs and shows the tags of the songs.
  
![](img\recommend.png)

6. **Artist board introduction (accessed via singer search):**
   <details>
      <summary>Viewable information (click to expand)</summary>
      artist：

      - Basic Information
             
      - Quantitative Table Of Creative Directions
        
      - Singer Production Label Statistics

      - Singer Fan Gender Statistics Review

      - Heat Map

      - Singer Hit Song Hot Reviews

    </details>

![](img\artist.png)

## Reference notes and acknowledgements

The project has been implemented with reference to the following:

BiliBili： [基础python+Flask+爬虫 ](https://www.bilibili.com/video/BV12E411A7ZQ?from=search&seid=17327553224685529336) Through this course, I learned the basics of crawling and learned about building websites (negative basic tutorial, the teacher was very detailed, I was skipping through the course, still very recommended)

Github： [guanchazhe_spider](https://github.com/hunter-lee1/guanchazhe_spider) Although there is no reference to the code of this project, the lesson above was recommended on this project, so I will put this project up as well ~~I didn't get through this one.(•ิ_•ิ)~~

Github： [NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi) This project references some of the functionality of this project, in order to ensure the stability of the real-time crawler crawl, while reducing the burden of filling in cookies and useragent for the user

HTML： [站长之家](https://aspx.sc.chinaz.com/) This project uses web templates from this website, all of which are free resources. The actual design of this project has been heavily redacted from the original sample website and is largely original except for the framework.

README:  [JAVClub](https://github.com/JAVClub/core) The README for this project is written with reference to some of the README content of the project, sorry for the author's first time writing a README. ~~Don't care about why it's this one!~~

Echarts： [Echarts](https://echarts.apache.org/zh/index.html) Most of the visualisation solutions within this project are provided by echarts, and two JS files, echarts.js and bmap.js, are referenced in the project.

miHoYo： [miHoYo](https://www.mihoyo.com/) The interface of this project contains some graphics from three games of MihaYu, especially the virtual image of "Silver Wolf", which will be removed immediately if there is any infringement. ~~dddd~~

Music_163： [Music_163](https://music.163.com/) This project crawls all the content in NetEase Cloud Music, and the data are all sourced from NetEase Cloud Music.



## Follow-up

Thanks in advance for reading this long winded document, there are many things that may not be clear, if you have any questions please feel free to bombard me with IS

Normally the whole system should be working now, if not please check again if you have missed any steps.
