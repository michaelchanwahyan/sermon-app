# sermon-app
## _A Collection of Christian Sermons From Different Sources_

sermon-app is a collection of christian sermons (typically cantonese) in text or audio format.
texts from audio sources are generated from raw recording using speech-to-text engine, like azure or [whisper](https://github.com/openai/whisper) (whisper indeed performs a lot better than azure)

### Immediately available sermon books
the outcome of this repo compiled from generate LaTeX source are listed below
| sermon book series                                                           | file path in this repo                    | link                                                                                                             |
|------------------------------------------------------------------------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| 建道神學院加拿大建道中心 Alliance Bible Seminary Centre of Canada            |                                           |                                                                                                                  |
| 宣道傳意 講道講章 Alliance Communications Ministry                           | ./pdf/sermon_ACSMHK_2022-24.pdf           | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_ACSMHK_2022-24.pdf)                 |
| 漢語聖經協會 講道講章 Chinese Bible International                            | ./pdf/sermon_CBI.pdf                      | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_CBI.pdf)                            |
| 中國神學研究院 道講章 China Graduate School of Theology                      | ./pdf/sermon_CGST.pdf                     | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_CGST.pdf)                           |
| 崇基神學院 崇拜講章 Div. Schl of Chung Chi College                           | ./pdf/sermon_DSCCC_2009-present.pdf       | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_DSCCC_2009-present.pdf)             |
| 流堂 崇拜講章 Flow Church                                                    | ./pdf/sermon_FLWC_2020-present.pdf        | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_FLWC_2020-present.pdf)              |
| 宣道會錦繡堂 崇拜講章 Christian Missionary Alliance Fairview Church          | ./pdf/sermon_FVC_2017-22.pdf              | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_FVC_2017-22.pdf)                    |
|                                                                              | ./pdf/sermon_FVC_2023-28.pdf              | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_FVC_2023-28.pdf)                    |
| 宣道會洪恩堂 崇拜講章 Christian Missionary Alliance Graceflow Church         | ./pdf/sermon_GFC_2020-present.pdf         | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_GFC_2020-present.pdf)               |
| 港九培靈研經會講章 Hong Kong Bible Conference                                | ./pdf/sermon_HKBC_1928-2007.pdf           | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_HKBC_1928-2007.pdf)                 |
|                                                                              | ./pdf/sermon_HKBC_2008-present.pdf        | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_HKBC_2008-present.pdf)              |
| JohnsonNg Youtube Channel                                                    | ./pdf/sermon_JNG_2012-18.pdf              | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_JNG_2012-18.pdf)                    |
|                                                                              | ./pdf/sermon_JNG_2019-20.pdf              | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_JNG_2019-20.pdf)                    |
|                                                                              | ./pdf/sermon_JNG_2021-22.pdf              | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_JNG_2021-22.pdf)                    |
|                                                                              | ./pdf/sermon_JNG_2023-24.pdf              | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_JNG_2023-24.pdf)                    |
| 播道會港福堂 崇拜講章 EFCC Kong Fok Church                                   | ./pdf/sermon_KFC_2020-present.pdf         | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_KFC_2020-present.pdf)               |
| The Porch, Dallas, TX 75251                                                  | ./pdf/sermon_PORCH_2014-present.pdf       | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_PORCH_2014-present.pdf)             |
| 沙田浸信會 Shatin Baptist Church                                             | ./pdf/sermon_STBC_2020-present.pdf        | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_STBC_2020-present.pdf)              |
| 葡萄藤教會 The Vine Church                                                   | ./pdf/sermon_VINE_2020-present.pdf        | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_VINE_2020-present.pdf)              |
| 環球聖經公會 講道講章 Worldwide Bible Society                                | ./pdf/sermon_WWBS.pdf                     | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_WWBS.pdf)                           |
| 播道會恩福堂 崇拜講章 Yan Fook Church & Youth                                | ./pdf/sermon_YFCX_2020-2023.pdf           | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_YFCX_2020-2023.pdf)                 |
|                                                                              | ./pdf/sermon_YFCX_2024-2027.pdf           | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_YFCX_2024-2027.pdf)                 |
| 中華宣道會友愛堂信培部 Yau Oi School                                         | ./pdf/sermon_YOS.pdf                      | [link](https://github.com/michaelchanwahyan/sermon-app/raw/master/pdf/sermon_YOS.pdf)                            |

### Statistics Overview on this project
sermon source | transcript total count | recent development activity
----|----|----
ABSCC | 0.0% ( 0 / 11718) | 0.2% ( 8 / 3221)
ACSMHK | 9.4% ( 1101 / 11718) | 18.2% ( 585 / 3221)
CBI | 0.3% ( 34 / 11718) | 1.6% ( 52 / 3221)
CGST | 1.9% ( 222 / 11718) | 1.1% ( 35 / 3221)
DSCCC | 6.2% ( 723 / 11718) | 2.2% ( 71 / 3221)
FLWC | 1.9% ( 226 / 11718) | 3.2% ( 104 / 3221)
FVC | 10.6% ( 1237 / 11718) | 1.9% ( 61 / 3221)
GFC | 1.9% ( 221 / 11718) | 23.3% ( 752 / 3221)
HKBC | 13.3% ( 1559 / 11718) | 0.1% ( 2 / 3221)
JNG | 26.1% ( 3060 / 11718) | 8.2% ( 266 / 3221)
KFC | 7.4% ( 864 / 11718) | 11.2% ( 362 / 3221)
PORCH | 4.3% ( 507 / 11718) | 2.4% ( 77 / 3221)
STBC | 2.2% ( 258 / 11718) | 4.2% ( 136 / 3221)
VINE | 3.0% ( 349 / 11718) | 7.5% ( 240 / 3221)
WWBS | 0.7% ( 81 / 11718) | 2.4% ( 76 / 3221)
YFCX | 10.5% ( 1236 / 11718) | 11.2% ( 362 / 3221)
YOS | 0.3% ( 40 / 11718) | 1.0% ( 32 / 3221)

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


