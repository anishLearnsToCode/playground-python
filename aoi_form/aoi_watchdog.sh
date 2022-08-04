#!/bin/bash

#mailto="ERP-procurement@cern.ch"
mailto="fap-dep-bc-team-pss2@cern.ch"

$ORACLE_HOME/bin/sqlplus @/usr/cern/sql/aoi_watchdog.sql

if cat /tmp/aoi_watchdog.lst|egrep -i '0' >/dev/null; then
    exit;
else
    (
     echo
     cat /tmp/aoi_watchdog.lst
     echo
     echo
     )|/bin/mail -s "AOI form problems" $mailto
fi
