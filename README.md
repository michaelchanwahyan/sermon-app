# sermon-app
## _A Collection of Christian Sermons From Different Sources_

sermon-app is a collection of christian sermons (typically cantonese) in text or audio format.
texts from audio sources are generated from raw recording using speech-to-text engine, like azure or [whisper](https://github.com/openai/whisper) (whisper indeed performs a lot better than azure)

### Immediately available sermon books
the outcome of this repo compiled from generate LaTeX source are listed below
| sermon book series                                                           | file path in this repo       | link                                                                                                                                        |
|------------------------------------------------------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 建道神學院加拿大建道中心 Alliance Bible Seminary Centre of Canada            | sermon_ABSCC                 | [Dropbox link](https://www.dropbox.com/scl/fi/19vx8vaclognefpbo71wk/sermon_ABSCC.pdf?rlkey=v6lc4fi6s3mywoas8qodh07tz&st=aaunegub&dl=0              ) |
| 宣道傳意 講道講章 Alliance Communications Ministry                           | sermon_ACSMHK_2022-24        | [Dropbox link](https://www.dropbox.com/scl/fi/8ryvn7ulfd0rr3u4aauzg/sermon_ACSMHK_2022-24.pdf?rlkey=1i4h6ipgk6e58vxmi62eq7yt7&st=mi40c76p&dl=0     ) |
|                                                                              | sermon_ACSMHK_2025-26        | [Dropbox link](https://www.dropbox.com/scl/fi/aa0mw6xitqeg9i085erty/sermon_ACSMHK_2025-26.pdf?rlkey=l8rsna372paovl8nr5yb8t1hr&st=7rwji54f&dl=0     ) |
| 漢語聖經協會 講道講章 Chinese Bible International                            | sermon_CBI                   | [Dropbox link](https://www.dropbox.com/scl/fi/kri87524l6odxord50oz6/sermon_CBI.pdf?rlkey=uc49459whnh3jubwl6okukia0&st=nz04gybw&dl=0                ) |
| 中國神學研究院 道講章 China Graduate School of Theology                      | sermon_CGST                  | [Dropbox link](https://www.dropbox.com/scl/fi/ime14zaa9on3cmx3if0ea/sermon_CGST.pdf?rlkey=pdg3pse45b8vqnhgkawk3bk7n&st=ra559fvd&dl=0               ) |
| 崇基神學院 崇拜講章 Div. Schl of Chung Chi College                           | sermon_DSCCC_2009-present    | [Dropbox link](https://www.dropbox.com/scl/fi/i3zi3taibm4x3c4cypjtz/sermon_DSCCC_2009-present.pdf?rlkey=ndybxo4pxxaj8xk9ix6c9diq4&st=f2o5p1xx&dl=0 ) |
| 流堂 崇拜講章 Flow Church                                                    | sermon_FLWC_2020-present     | [Dropbox link](https://www.dropbox.com/scl/fi/hlm0r2vn6jfd99rxwosfr/sermon_FLWC_2020-present.pdf?rlkey=35e5f6pqnab08yqbh6skcyxy0&st=7ea7hw55&dl=0  ) |
| 宣道會錦繡堂 崇拜講章 Christian Missionary Alliance Fairview Church          | sermon_FVC_2017-22           | [Dropbox link](https://www.dropbox.com/scl/fi/i5jlzacawmlwskwz20w6g/sermon_FVC_2017-22.pdf?rlkey=8da9p796i2px78p7yg6bm34vb&st=1rwj409f&dl=0        ) |
|                                                                              | sermon_FVC_2023-28           | [Dropbox link](https://www.dropbox.com/scl/fi/1r0cx106e0087r2lstiy3/sermon_FVC_2023-28.pdf?rlkey=ehlycvpqx5lbq3rrk112tpbra&st=i7cqqm6p&dl=0        ) |
| 宣道會洪恩堂 崇拜講章 Christian Missionary Alliance Graceflow Church         | sermon_GFC_2020-present      | [Dropbox link](https://www.dropbox.com/scl/fi/buzgzqtooe8r2fgy6ciik/sermon_GFC_2020-present.pdf?rlkey=66egk46fhlcee4dt1egd9eqcb&st=b2dzp6c1&dl=0   ) |
| 港九培靈研經會講章 Hong Kong Bible Conference                                | sermon_HKBC_1928-2007        | [Dropbox link](https://www.dropbox.com/scl/fi/gy475ozahgyswvp6da9lg/sermon_HKBC_1928-2007.pdf?rlkey=mngdp4lfb4amsaj0erk0ys6ia&st=n71s4znf&dl=0     ) |
|                                                                              | sermon_HKBC_2008-present     | [Dropbox link](https://www.dropbox.com/scl/fi/c5y2wziiriiilbn1vqlcz/sermon_HKBC_2008-present.pdf?rlkey=bueyeempd66zne60k0sanaety&st=43dmwv8u&dl=0  ) |
| JohnsonNg Youtube Channel                                                    | sermon_JNG_2012-18           | [Dropbox link](https://www.dropbox.com/scl/fi/b5iv5kqzy9oqtt508cfjw/sermon_JNG_2012-18.pdf?rlkey=rj0dgeougqdjeezjz15ristcw&st=802aufjj&dl=0        ) |
|                                                                              | sermon_JNG_2019-20           | [Dropbox link](https://www.dropbox.com/scl/fi/vmxmnmz4c7z47uyyvji7o/sermon_JNG_2019-20.pdf?rlkey=a5b1gcijqr0fk7blqyk8nahdp&st=t5f6c0uz&dl=0        ) |
|                                                                              | sermon_JNG_2021-22           | [Dropbox link](https://www.dropbox.com/scl/fi/ag0cu3xuxtamh69eq9qve/sermon_JNG_2021-22.pdf?rlkey=4lmvq2e8n4ef0maf9bepqi7px&st=3ilpzsyq&dl=0        ) |
|                                                                              | sermon_JNG_2023-24           | [Dropbox link](https://www.dropbox.com/scl/fi/6aiod4iwos9kchxa8s9bz/sermon_JNG_2023-24.pdf?rlkey=see55hvomd7uaqqquqssuifg8&st=ach9kxbk&dl=0        ) |
|                                                                              | sermon_JNG_2025-26           | [Dropbox link](https://www.dropbox.com/scl/fi/gcuby99drfulyf4s5fvcz/sermon_JNG_2025-26.pdf?rlkey=mypcf3fv3gvedkhqf8caeexhm&st=z3y8uutx&dl=0        ) |
| 播道會港福堂 崇拜講章 EFCC Kong Fok Church                                   | sermon_KFC_2020-present      | [Dropbox link](https://www.dropbox.com/scl/fi/56w19qca9z33psnmg5wnr/sermon_KFC_2020-present.pdf?rlkey=7uv3hoqb6ne3n7dsthrv1onbd&st=7artfn9s&dl=0   ) |
| 旺角浸信會 崇拜講章 Mongkok Baptist Church                                   | sermon_MKBC_2020-present     | [Dropbox link](https://www.dropbox.com/scl/fi/kijr8c7k741j5gnd928o7/sermon_MKBC_2020-present.pdf?rlkey=bi0aamjejvf75oiymdf7enqx8&st=q4fivytf&dl=0  ) |
| The Porch, Dallas, TX 75251                                                  | sermon_PORCH_2014-present    | [Dropbox link](https://www.dropbox.com/scl/fi/0u87t49t4null5zdnzr4z/sermon_PORCH_2014-present.pdf?rlkey=iyt02hpvq8i1yryh5waag83bh&st=u41vufkv&dl=0 ) |
| 沙田浸信會 Shatin Baptist Church                                             | sermon_STBC_2020-present     | [Dropbox link](https://www.dropbox.com/scl/fi/pg6c7h8sj9dajz9l9283q/sermon_STBC_2020-present.pdf?rlkey=u83166iscihnh9gjy138cgyb5&st=zq516qem&dl=0  ) |
| 葡萄藤教會 The Vine Church                                                   | sermon_VINE_2020-present     | [Dropbox link](https://www.dropbox.com/scl/fi/5y14d6av5m8cy5m9s3qdq/sermon_VINE_2020-present.pdf?rlkey=apmi1j2ozeouuikhunykt06jz&st=kz6zlj13&dl=0  ) |
| 環球聖經公會 講道講章 Worldwide Bible Society                                | sermon_WWBS                  | [Dropbox link](https://www.dropbox.com/scl/fi/pjwwfgjhdropdlyar3i89/sermon_WWBS.pdf?rlkey=rowv5dtpix7wwkhmavhnzwls2&st=n4yvpr3s&dl=0               ) |
| 播道會恩福堂 崇拜講章 Yan Fook Church & Youth                                | sermon_YFCX_2020-2023        | [Dropbox link](https://www.dropbox.com/scl/fi/jmb7ddpbzoafvr92aecvj/sermon_YFCX_2020-23.pdf?rlkey=vuqpv0ddtmk19cqps45hoak6a&st=5xve5yah&dl=0       ) |
|                                                                              | sermon_YFCX_2024-2027        | [Dropbox link](https://www.dropbox.com/scl/fi/6n81qydnxu8jniaqqh59n/sermon_YFCX_2024-27.pdf?rlkey=mc0enlv3zbwv8xffv5q4jt36c&st=6w1b922y&dl=0       ) |
| 中華宣道會友愛堂信培部 Yau Oi School                                         | sermon_YOS                   | [Dropbox link](https://www.dropbox.com/scl/fi/0gssb757sah0luha38jlv/sermon_YOS.pdf?rlkey=cvcisn4hq0g7ybv8jcmfm55lt&st=f1ozdavh&dl=0                ) |
                                                                                                               
### Statistics Overview on this project
source | sermon no. (out of 13147) | amount of dev. activity (out of 3199)
----|----|----
ABSCC | 0.2% ( 32 ) | 3.8% ( 122 )
ACSMHK | 11.2% ( 1485 ) | 17.4% ( 553 )
CBI | 0.4% ( 53 ) | 2.3% ( 72 )
CGST | 1.7% ( 222 ) | 0.8% ( 26 )
DSCCC | 5.7% ( 753 ) | 0.8% ( 26 )
FLWC | 2.0% ( 263 ) | 3.3% ( 104 )
FVC | 9.5% ( 1260 ) | 2.9% ( 92 )
GFC | 1.9% ( 251 ) | 2.5% ( 81 )
HKBC | 11.9% ( 1587 ) | 0.4% ( 13 )
JNG | 24.1% ( 3203 ) | 8.4% ( 266 )
KFC | 7.4% ( 985 ) | 7.1% ( 225 )
MKBC | 1.7% ( 226 ) | 23.3% ( 740 )
PORCH | 4.0% ( 534 ) | 2.6% ( 83 )
STBC | 2.4% ( 314 ) | 3.8% ( 121 )
VINE | 3.8% ( 499 ) | 6.4% ( 203 )
WWBS | 0.6% ( 83 ) | 0.8% ( 24 )
YFCX | 11.3% ( 1509 ) | 12.9% ( 409 )
YOS | 0.3% ( 40 ) | 0.6% ( 19 )

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


