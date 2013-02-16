#!/bin/sh

# $1 repo
# $2 commit
# $3 version
# $4 target-name

COMMIT=$2
SHORTCOMMIT=`echo ${COMMIT:0:7}`
pushd ~/rpmbuild/SOURCES
wget https://github.com/$1/archive/$2/$4-$3-$SHORTCOMMIT.tar.gz
popd
