#!/usr/bin/gawk -f

#BEGIN { RS="/[[:digit:]]+[[:space:]]*/" } 
#	  { print "RT=", RS, "rec=", $0 }

#BEGIN { FS=""; RS="/[[:digit:]]+[[:space:]]*/" }
#{if (/[[:digit:]]+$/) {  cc += NF; print $0, "cc=", cc; cc = 0; } else { cc += NF; print $0, "cc=", cc;} }
#{  print $0, "cc=", NF; } 

{if (/[[:digit:]]+[[:space:]]*$/) 
{ len += length($0); str = (str $0); if (len <= 140) { print str } len = 0; str = "" }
else { if (/[[:alnum:]]+/) { len += length($0); str = (str $0); } } }
