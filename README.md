# Christian Sermon (Cantonese Speech-To-Text Transcription)

this is a project repository that has the following three functionalities

- grep from youtube cantonese christian sermons from different accessible channels, audio voice files are retrieved;
- from audio voice file an Azure speech recognition engine is used for cantonese sermon transcription (from audio speech file to raw text file)
- generate from cantonese-transcriped sermon text files to a pdf compilation with sorting of preachers, bible book chapter, sermon title, and time of upload (onto youtube)

This project repository relies on a backend engine named [datalab](https://github.com/michaelchanwahyan/datalab) (or ds_workspace, equivalent project with another name) that was also developed by this current project author.

## Usage Guide

#### 1. Start up Docker engine and launch [datalab](https://github.com/michaelchanwahyan/datalab) jupyterlab

```bash
docker run -p 9999:9999 \
           -v /your/path/to/app:/app \
           --name=ds_workspace \
           michaelchanwahyan/ds_workspace:latest \
           /usr/bin/bash /startup.sh
```

Upon successful execution, open localhost:9999 from system browser shall bring you to a jupyterlab interface

(note on the potentially required password. with reference to the [startup script](https://github.com/michaelchanwahyan/datalab/blob/master/startup.sh) of the [datalab platform](https://github.com/michaelchanwahyan/datalab), possibly the password 'dsteam' is already specified in the startup options "--ServerApp.token='dsteam'". try it whenever applicable)

Normal datalab home screen upon startup:
![Alt text](/photos/datalab_home.jpg "datalab home screen")


#### 2. Generate the sermon book table-of-content (toc)

##### a) the index file (a toc-like csv file)
in /app/projects/, run the notebook file [generate_index.ipynb](/projects/generate_index.ipynb) using the launched jupyterlab.
![Alt text](/photos/index_by_preacher.png "table of content")

##### b) download the sermon audio according to index file
inline description in [generate_index.ipynb](/projects/generate_index.ipynb) describe the use of youtube-dl to extraction raw audio from youtube.

#### 3. Convert from audio to text (the cantonese speech-to-text part)
in /app/projects/, the core script is to run the notebook file [generate_content.ipynb](/projects/generate_content.ipynb) (or the [python counterpart](/projects/generate_content.py))
for the host and container systems to run cocurrently, try to look into [cv_runby_host.py](/projects/cv_runby_host.py) and [cv_runby_container](/projects/cv_runby_container.py) for CD/CI

#### 4. Compile the sermon texts into a single book (step 1)
in /app/projects/, run the python script [generate_sermonbook.py](/projects/generate_sermonbook.py) to generate the LaTeX source file under build/ folder

#### 5. Compile the sermon texts into a single book (step 2)
in /app/build/, run the build script [build.sh](/build/build.sh).  the core software package required is XeLaTeX.
