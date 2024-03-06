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
echo $1

cd ..

BUILD_PATH=build/$1
mkdir -p $BUILD_PATH
echo LaTeX build directory of $1 > $BUILD_PATH/README.md
echo >> $BUILD_PATH/README.md
git add $BUILD_PATH/README.md

DATA_PATH=data/$1
mkdir -p $DATA_PATH
echo data folder of $1 > $DATA_PATH/README.md
echo >> $DATA_PATH/README.md
git add $DATA_PATH/README.md

PROJECTS_PATH=projects/$1
mkdir -p $PROJECTS_PATH
echo project folder of $1 > $PROJECTS_PATH/README.md
echo >> $PROJECTS_PATH/README.md
touch $PROJECTS_PATH/exlist.txt
touch $PROJECTS_PATH/rejection_list.txt
git add $PROJECTS_PATH/README.md
git add -f $PROJECTS_PATH/rejection_list.txt

WHISPER_PATH=whisper/$1
mkdir -p $WHISPER_PATH
echo this is the directory path of whisper for $1 project > $WHISPER_PATH/README.md
echo >> $WHISPER_PATH/README.md
echo reference whisper cpp execution be like >> $WHISPER_PATH/README.md
echo \`\`\` >> $WHISPER_PATH/README.md
echo \#!/bin/bash >> $WHISPER_PATH/README.md
echo \`\`\` >> $WHISPER_PATH/README.md
git add $WHISPER_PATH/README.md
echo 4 > $WHISPER_PATH/threadnum.txt

