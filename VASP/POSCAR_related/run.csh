#!/bin/csh

while (! -e stoppoll)
    pushd `find . -name wait -printf "%A@ %p\n" |& sed 's+/wait++g' | sort -n -r | tail -n -1 | awk '{print $2}'` >& /dev/null
    rm -f wait
    ../callvasp
    popd >& /dev/null
end