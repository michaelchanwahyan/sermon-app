#!/bin/bash
set +x

source COMMON_RC

pushd $BUILD_PATH
  echo
  echo sermon TeX build once takes roughly 12 - 15 minutes ...
  echo
  sleep 10
  if [ "$1" == "buildall" ] ; then
  bash build.sh buildall
  elif [ "$1" == "buildlatest" ] ; then
  bash build.sh buildlatest
  elif [ "$1" == "once" ] ; then
  bash build.sh buildall once
  else
  bash build.sh buildall
  fi
popd # back to $CI_PATH
