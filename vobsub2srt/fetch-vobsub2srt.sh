#!/bin/sh

COMMIT=$1
VERSION=1.0
TARGETNAME=vobsub2srt

../get-github-sources.sh ruediger/VobSub2SRT $COMMIT $VERSION $TARGETNAME

