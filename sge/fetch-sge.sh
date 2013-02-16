#!/bin/sh

COMMIT=$1
VERSION=0.1
TARGETNAME=spacegameengine

../get-github-sources.sh freundlich/spacegameengine $COMMIT $VERSION $TARGETNAME

