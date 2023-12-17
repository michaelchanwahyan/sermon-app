#!/bin/bash
set +x
pushd ../build
  bash build.sh buildall
popd # back to ./app/.ci
