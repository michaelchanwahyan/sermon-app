#!/bin/bash
if   [ "$1" == "" ] ; then
    echo "NAME                                                                "
    echo "     1.0.new_project.sh - create new project template.              "
    echo "                                                                    "
    echo "SYNOPSIS                                                            "
    echo "     1.0.new_project.sh    [project_name]                           "
    echo "                                                                    "
    echo "DESCRIPTION                                                         "
    echo "     This script create the <project_name> according to sermon      "
    echo "     project purpose. Folders like ./project/<project_name>,        "
    echo "     ./data/<project_name>, ./whisper/<project_name>,               "
    echo "     ./build/<project_name>, etc.                                   "
    exit
fi

set -x

source COMMON_RC

PROJECT_NAME=$1
echo $PROJECT_NAME

cd ..

mkdir -p $BUILD_PATH/$PROJECT_NAME
echo LaTeX build directory of $1 > $BUILD_PATH/$PROJECT_NAME/README.md
echo >> $BUILD_PATH/$PROJECT_NAME/README.md
git add $BUILD_PATH/$PROJECT_NAME/README.md

mkdir -p $DATA_PATH/$PROJECT_NAME
echo data folder of $1 > $DATA_PATH/$PROJECT_NAME/README.md
echo >> $DATA_PATH/$PROJECT_NAME/README.md
git add $DATA_PATH/$PROJECT_NAME/README.md

mkdir -p $PROJECT_PATH/$PROJECT_NAME
echo project folder of $1 > $PROJECT_PATH/$PROJECT_NAME/README.md
echo >> $PROJECT_PATH/$PROJECT_NAME/README.md
touch $PROJECT_PATH/$PROJECT_NAME/exlist.txt
touch $PROJECT_PATH/$PROJECT_NAME/rejection_list.txt
git add $PROJECT_PATH/$PROJECT_NAME/README.md
git add -f $PROJECT_PATH/$PROJECT_NAME/rejection_list.txt

mkdir -p $WHISPER_PATH/$PROJECT_NAME
echo this is the directory path of whisper for $1 project > $WHISPER_PATH/$PROJECT_NAME/README.md
echo >> $WHISPER_PATH/$PROJECT_NAME/README.md
echo reference whisper cpp execution be like >> $WHISPER_PATH/$PROJECT_NAME/README.md
echo \`\`\` >> $WHISPER_PATH/$PROJECT_NAME/README.md
echo \#!/bin/bash >> $WHISPER_PATH/$PROJECT_NAME/README.md
echo \`\`\` >> $WHISPER_PATH/$PROJECT_NAME/README.md
git add $WHISPER_PATH/$PROJECT_NAME/README.md
echo 4 > $WHISPER_PATH/$PROJECT_NAME/threadnum.txt

