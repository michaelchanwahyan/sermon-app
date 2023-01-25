# sermon-app
## _A Collection of Christian Sermons From Voice To Text_

sermon-app is a collection of christian sermons (typically cantonese) generated from their raw recording using speech-to-text technology

this work requires the following essential elements

- Python3 (already in [datalab](https://github.com/michaelchanwahyan/datalab))
- Jupyter (already in [datalab](https://github.com/michaelchanwahyan/datalab))
- Docker (user shall install it on host, see Usage-1)
- LaTeX (user shall install it on host, see Usage-6)

users shall be familiar with their basics in order to play around this repo on their own

## Features

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

in /app/projects/, run the notebook file [generate_index.ipynb](/projects/generate_index.ipynb) using the launched jupyterlab.

![Alt text](/photos/index_by_preacher.png "table of content")

please be reminded that the scripts may involve human-machine interaction so that you are not running [generate_index.ipynb](/projects/generate_index.ipynb) blindly.  do take attention to the inline comment in the source file.

#### b) download the sermon audio according to index file

inline description in [generate_index.ipynb](/projects/generate_index.ipynb) describe the use of youtube-dl to extraction raw audio from youtube.

### 4. Convert from audio to text (speech-to-text part, by container)

in /app/projects/, the core script is to run the notebook file [generate_content.ipynb](/projects/generate_content.ipynb) (or the [python counterpart](/projects/generate_content.py))

azure speech service is required and the azure subscription info is omitted in this repo

a pair of ```cv_runby_*.py``` files can be found in the same directory. they serve as cocurrent python script to run the speech2text (by [cv_runby_container.py](/projects/cv_run_container.py)) and text concatenation (by [cv_runby_host.py](/projects/cv_run_host.py)) in an on-the-fly manner

### 5. Compile the sermon texts into a single book source (by host/container)

in /app/projects/, run the python script [generate_sermonbook.py](/projects/generate_sermonbook.py) to generate the LaTeX source file under build/ folder

### 6. Compile the sermon texts into a single book pdf (by host, where LaTeX is required)

(LaTeX installation: see [their page](https://www.latex-project.org/get/))

in /app/build/, run the build script [build.sh](/build/build.sh).  the core LaTeX software package required is XeLaTeX.
