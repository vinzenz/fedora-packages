#!/bin/sh

COMMIT=$1
VERSION=0.12.1
TARGETNAME=fcppt

../get-github-sources.sh freundlich/fcppt $COMMIT $VERSION $TARGETNAME

