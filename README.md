# sermon-app
## _A Collection of Christian Sermons From Different Sources_

sermon-app is a collection of christian sermons (typically cantonese) in text or audio format.
texts from audio sources are generated from raw recording using speech-to-text engine, like azure or [whisper](https://github.com/openai/whisper) (whisper indeed performs a lot better than azure)

### Immediately available sermon books
the outcome of this repo compiled from generate LaTeX source are listed below
| sermon book series                                                           | file path in this repo       | link                                                                                                                                        |
|------------------------------------------------------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 建道神學院加拿大建道中心 Alliance Bible Seminary Centre of Canada            | sermon_ABSCC                 | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EdbJ3pBkTdBEh6o6a3SYCZwBCRiDzrt6LzQrITg9xjdhkA?e=pwNtxx) |
| 宣道傳意 講道講章 Alliance Communications Ministry                           | sermon_ACSMHK_2022-24        | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EbF-wP66vEZKgkv0GS0HhMQBxcXod_Xr-abiNQxjE6y2Jg?e=1nDjg7) |
|                                                                              | sermon_ACSMHK_2025-26        | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EfVYTqIf6dlDtA46o5jPEDQB8hPNbiKvnjGfx8IEcUP19Q?e=txo6ah) |
| 漢語聖經協會 講道講章 Chinese Bible International                            | sermon_CBI                   | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EexN9xolxGlBvEegnAAjw4cBLME6Ue52Vj3wkCsqzSSqpg?e=9tFbKT) |
| 中國神學研究院 道講章 China Graduate School of Theology                      | sermon_CGST                  | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/Efm7f5p3N99LvP1cE2UZjIEBGfJj-SkE02GtoasjDnzGkw?e=P8jz2x) |
| 崇基神學院 崇拜講章 Div. Schl of Chung Chi College                           | sermon_DSCCC_2009-present    | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EbVa0FIwrGVFg5NsFWxfS9YBVmiu1LkRfPWCZX26Vi7C6g?e=AtBOgP) |
| 流堂 崇拜講章 Flow Church                                                    | sermon_FLWC_2020-present     | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EVnH4QasLDdJg8KPkJaIMOwBpAS_QTYhRGdUaKJcjoX1eQ?e=5YkTAt) |
| 宣道會錦繡堂 崇拜講章 Christian Missionary Alliance Fairview Church          | sermon_FVC_2017-22           | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EaNzWm1WZKFDmpSA-piTqBgB6GcpXvzCFc9m1EmgkVL27w?e=gGEgOT) |
|                                                                              | sermon_FVC_2023-28           | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EfdU4MLn9ZpEurHV3t0dkvAB7DltkRjxZoejKnwozPubqg?e=COLI19) |
| 宣道會洪恩堂 崇拜講章 Christian Missionary Alliance Graceflow Church         | sermon_GFC_2020-present      | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EW_AhWZ27gdNiXkqlCXQ_7MB_N9u6bg-Y3tUJlMAYMZvow?e=xObMIU) |
| 港九培靈研經會講章 Hong Kong Bible Conference                                | sermon_HKBC_1928-2007        | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EbI8nvf4MMNGkoqGUE2hje8BNrTrkl8T2EQuZQGCJ9IuCg?e=EZmvlp) |
|                                                                              | sermon_HKBC_2008-present     | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EYEdCkwnt-hAqw41PmGxZWkBtmLNoSZCKwP7FvanDchRdQ?e=nfOYhx) |
| JohnsonNg Youtube Channel                                                    | sermon_JNG_2012-18           | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/ETgYxe-drOFNhIZSIbz6AHgBP5ZuLKVsOTOKqrOLBZ5rAg?e=gdbULO) |
|                                                                              | sermon_JNG_2019-20           | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EVqwsOaGDvZApQD2dkAYLkEBCthGc7gR6JtUGLOFqGf6mg?e=GUoOXW) |
|                                                                              | sermon_JNG_2021-22           | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EWUK3pmGjTxKlUylr4f3rTIBo6mOhyFEnIX4AgdKClMOBA?e=mT4P0P) |
|                                                                              | sermon_JNG_2023-24           | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EYILCIGDpgRBusxBprnvmUUBf4zbL0xwTHJEtGmpcAQ6AA?e=kofFQe) |
|                                                                              | sermon_JNG_2025-26           | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EWELovuNELZIozdsaMR1zfgB8OsYK7hoClH1YqbhtekUew?e=jqmphh) |
| 播道會港福堂 崇拜講章 EFCC Kong Fok Church                                   | sermon_KFC_2020-present      | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EXjczoPvWhhNpaHYBJ1V3_cBlZLiHPYE-bc5PWvycw__Aw?e=W0sbp7) |
| The Porch, Dallas, TX 75251                                                  | sermon_PORCH_2014-present    | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EXe-vY7FJWpLm-Sz8N5Z-fgB_6DFwFcxDSbCpxmTdIO9MA?e=FmnW29) |
| 沙田浸信會 Shatin Baptist Church                                             | sermon_STBC_2020-present     | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EU3ibL98TuFCnUT5gRydePUB_egKGhp63F5Vmf66NppPyw?e=eMCZZ7) |
| 葡萄藤教會 The Vine Church                                                   | sermon_VINE_2020-present     | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EYGlZBMMvKlArP3GllgSTr4Bmpc2yjy_Cd-uKXl8CILMpQ?e=scdy1k) |
| 環球聖經公會 講道講章 Worldwide Bible Society                                | sermon_WWBS                  | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/Ec1TxFcHqlhOjjugY5tSPsgB7E2fIPebv9Ze_7EMruHPlA?e=nTBR8n) |
| 播道會恩福堂 崇拜講章 Yan Fook Church & Youth                                | sermon_YFCX_2020-2023        | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/EXQxdBKzl_ZFr3VuxJaiT9UBwzVztGh2eAS22O2xLKdMVg?e=jbENWT) |
|                                                                              | sermon_YFCX_2024-2027        | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/ESO_Cn-5VJFKugJca3A6Uv0Byn11H5RhDwuQALPNXlgr7w?e=NEXCoZ) |
| 中華宣道會友愛堂信培部 Yau Oi School                                         | sermon_YOS                   | [OneDrive link](https://mycuhk-my.sharepoint.com/:b:/g/personal/1155002927_link_cuhk_edu_hk/Eey3JZdDE7pIlWlJEZCLYV8B6YGLDs77gvvYfXWhzZKQjA?e=zGYW9k) |

### Statistics Overview on this project
source | sermon no. (out of 12470) | amount of dev. activity (out of 1929)
----|----|----
ABSCC | 0.0% ( 0 ) | 0.0% ( 0 )
ACSMHK | 10.6% ( 1325 ) | 29.0% ( 560 )
CBI | 0.3% ( 44 ) | 1.8% ( 35 )
CGST | 1.8% ( 222 ) | 0.8% ( 15 )
DSCCC | 5.9% ( 739 ) | 0.6% ( 11 )
FLWC | 2.0% ( 246 ) | 4.7% ( 91 )
FVC | 10.0% ( 1248 ) | 3.1% ( 60 )
GFC | 1.9% ( 238 ) | 3.1% ( 60 )
HKBC | 12.7% ( 1587 ) | 0.1% ( 2 )
JNG | 25.1% ( 3133 ) | 10.7% ( 207 )
KFC | 7.4% ( 923 ) | 9.0% ( 173 )
PORCH | 4.2% ( 520 ) | 2.5% ( 49 )
STBC | 2.3% ( 288 ) | 4.3% ( 83 )
VINE | 3.5% ( 442 ) | 10.2% ( 196 )
WWBS | 0.7% ( 83 ) | 0.5% ( 9 )
YFCX | 11.2% ( 1392 ) | 19.3% ( 372 )
YOS | 0.3% ( 40 ) | 0.3% ( 6 )

### Steps to compile the books from scratch _(painful !)_
#### Pre-requisites
This work containerizes a lot of python packages into one docker image named "[datalab](https://github.com/michaelchanwahyan/datalab)".

You need to play with the following essential elements

- Python3 (already in [datalab](https://github.com/michaelchanwahyan/datalab))
- Jupyter (already in [datalab](https://github.com/michaelchanwahyan/datalab))
- Docker (you shall install it on your host, see Usage-1)
- LaTeX (you shall install it on your host, see Usage-6)

If you are unfamiliar to these basics, please go to [Immediately available sermon books](###Immediately-available-sermon-books) section.

#### Features

- automation-ready: new sermons could be found from destinated youtube channel
- compilation with sorting according preacher, book, etc.
- opening possibility for more channels source
- powered by Docker, Jupyter, and Spark

for sermon-app, the author currently dedicates his effort focusing on cantonese sermon compilation so that the valuable resources could be re-archived, re-distributed, re-presented, and served as reference for future opportunities.

the author uses this project to

- grab from youtube cantonese christian sermons from different accessible channels, audio voice files are retrieved;
- from audio voice file an Azure speech recognition engine is used for cantonese transcription (from audio speech file to raw text file)
- generate from transcriped sermon text a pdf compilation with proper sorting by preachers, bible book chapter, sermon title, and time

as it is written in [NIV Psalm 127](https://www.biblegateway.com/passage/?search=Psalm%20127&version=NIV)

> Unless the Lord builds the house,
> the builders labor in vain.
> Unless the Lord watches over the city,
> the guards stand watch in vain.

This work you see here is truely a blessing from G-d.

## Usage

### 1. Get the [datalab] engine (by host)

#### 1.1 Install Docker

refer to [installation guide](https://docs.docker.com/engine/install/)

#### 1.2 Get datalab container image

```bash
docker pull michaelchanwahyan/datalab
```

### 2. Start and jupyterlab through [datalab] container (by host)

you probably would need [docker-volume](https://docs.docker.com/storage/volumes/)

```bash
docker run -p 9999:9999 \
           -v /your/path/to/app:/app \
           --name=ds_workspace \
           michaelchanwahyan/datalab:latest \
           /usr/bin/bash /startup.sh
```

Upon successful execution, opening localhost:9999 from system browser shall bring you to a jupyterlab interface normally looks like

![Alt text](/photos/datalab_home.jpg "datalab home screen")

(if prompted to password, with reference to the [startup script](https://github.com/michaelchanwahyan/datalab/blob/master/startup.sh) of the [datalab platform](https://github.com/michaelchanwahyan/datalab), possibly the password 'dsteam' is already specified in the startup options "--ServerApp.token='dsteam'". try it whenever it is needed)

### 3. Generate the sermon book table-of-content (toc) (by container)

#### a) the index file (a toc-like csv file)

The code files for JohnsonNg Youtube Channel's sermon content are put under /app/projects/JNG/, so that in /app/projects/JNG, run the notebook file [generate_index.ipynb](/projects/JNG/generate_index.ipynb) using the launched jupyterlab.

![Alt text](/photos/index_by_preacher.png "table of content")

please be reminded that the scripts may involve human-machine interaction so that you are not running [generate_index.ipynb](/projects/JNG/generate_index.ipynb) blindly.
Do take attention to the inline comment in the source file.

#### b) download the sermon audio according to index file

inline description in [generate_index.ipynb](/projects/JNG/generate_index.ipynb) describe the use of yt-dlp to extraction raw audio from youtube.

### 4. Convert from audio to text (speech-to-text part ~~, by container~~)

~~in /app/projects/JNG, the core script is to run the notebook file [generate_content.ipynb](/projects/JNG/generate_content.ipynb) (or the [python counterpart](/projects/JNG/generate_content.py))~~

~~azure speech service is required and the azure subscription info is omitted in this repo~~

~~a pair of ```cv_runby_*.py``` files can be found in the same directory. they serve as cocurrent python script to run the speech2text (by [cv_runby_container.py](/projects/JNG/cv_run_container.py)) and text concatenation (by [cv_runby_host.py](/projects/JNG/cv_run_host.py)) in an on-the-fly manner~~

as from 2023 [OpenAI/whisper model](https://github.com/openai/whisper) became available, speech-to-text could become more effective.

also thanks to [ggerganov/whisper.cpp](https://github.com/ggerganov/whisper.cpp) who contributes on cpp porting for Apple Silicon integration, whisper runs very fast now.

currently whisper model size used is large.  ggerganov's [ggml-large.bin, later renamed to ggml-large-v1.bin](https://huggingface.co/ggerganov/whisper.cpp/blob/main/ggml-large-v1.bin) model file together with other sizes could be found from [ggerganov's HaggingFace page](https://huggingface.co/ggerganov/whisper.cpp/tree/main).

In case transcription runs into error or totally incorrect text output, medium version of the model [ggml-medium.bin](https://huggingface.co/ggerganov/whisper.cpp/blob/main/ggml-medium.bin) could be considered to use.

### 5. Compile the sermon texts into a single book source (by host/container)

in /app/projects/JNG, run the python script [generate_sermonbook.py](/projects/JNG/generate_sermonbook.py) to generate the LaTeX source file under build/ folder

### 6. Compile the sermon texts into a single book pdf (by host, where LaTeX is required)

(LaTeX installation: see [their page](https://www.latex-project.org/get/))

in /app/build/, run the build script [build.sh](/build/build.sh) with input argument detailed below:
```bash
./build.sh JNG # this is to compile JohnsonNg Youtube Channel sermon content
./build.sh HKBC # this is to compile Hong Kong Bible Conference sermon content
```
the core LaTeX software package required is XeLaTeX.

## Editor
contact person : Michael via michaelchan_wahyan@yahoo.com.hk


