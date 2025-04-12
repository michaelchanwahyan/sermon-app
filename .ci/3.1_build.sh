#!/bin/bash
set +x

source COMMON_RC

pushd $BUILD_PATH
  if [ "$1" != "once" ] ; then
  echo
  echo sermon TeX build once takes roughly 12 - 15 minutes ...
  echo
  sleep 10
  bash build.sh buildall
  else
  echo
  echo sermon TeX build twice takes roughly 25 - 30 minutes ...
  echo
  sleep 10
  bash build.sh buildall once
  fi
popd # back to $CI_PATH
