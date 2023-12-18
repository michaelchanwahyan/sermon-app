#!/bin/bash
set +x
pushd ../build
  if [ "$1" != "once" ] then
  bash build.sh buildall
  else
  bash build.sh buildall once
  fi
popd # back to ./app/.ci
