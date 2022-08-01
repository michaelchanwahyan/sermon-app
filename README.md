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



#### 2. Generate the sermon book index (a table-of-content-like csv file) within jupyterlab
in /app/projects/, run the notebook file [generate_index.ipynb](https://github.com/michaelchanwahyan/sermon-app/blob/master/projects/generate_index.ipynb) using the launched jupyterlab.  note and follow the inline instructions on the method of extraction raw audio from youtube.

#### 3. Download the sermon audio and Generate the sermon textual content (the cantonese speech-to-text part)
in /app/projects/, the core script is to run the notebook file [generate_content.ipynb](https://github.com/michaelchanwahyan/sermon-app/blob/master/projects/generate_content.ipynb) (or the [python counterpart](https://github.com/michaelchanwahyan/sermon-app/blob/master/projects/generate_content.py))
for the host and container systems to run cocurrently, try to look into [cv_runby_host.py](https://github.com/michaelchanwahyan/sermon-app/blob/master/projects/cv_runby_host.py) and [cv_runby_container](https://github.com/michaelchanwahyan/sermon-app/blob/master/projects/cv_runby_container.py) for CD/CI

#### 4. Compile the sermon texts into a single book (step 1)
in /app/projects/, run the python script [generate_sermonbook.py](https://github.com/michaelchanwahyan/sermon-app/blob/master/projects/generate_sermonbook.py) to generate the LaTeX source file under build/ folder

#### 5. Compile the sermon texts into a single book (step 2)
in /app/build/, run the build script [build.sh](https://github.com/michaelchanwahyan/sermon-app/blob/master/build/build.sh).  the core software package required is XeLaTeX.