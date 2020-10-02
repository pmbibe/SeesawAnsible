#!/bin/bash
data=$(cat $HOME/.bash_profile)
if [[ $data =~ "*/go/*" ]] ; then
    echo export PATH=$PATH:/usr/local/go/bin >> $HOME/.bash_profile
fi
if [[ $data =~ "GOPATH" ]] ; then
    echo export GOPATH=/usr/local/go/bin >> $HOME/.bash_profile
fi

