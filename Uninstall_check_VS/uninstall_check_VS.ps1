$vs2013="C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\Extensions"
$vs2015="C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE\Extensions"
$vs2017="C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\Common7\IDE\Extensions"

$vs2013_before_penak=ls -name $vs2013
$vs2015_before_penak=ls -name $vs2015
$vs2017_before_penak=ls -name $vs2017
#Compare-object
$vs2013_after_penak=ls -name $vs2013
$vs2015_after_penak=ls -name $vs2015
$vs2017_after_penak=ls -name $vs2017

$pentak_2013= Compare-Object -ReferenceObject $vs2013_before_penak -DifferenceObject $vs2013_after_penak
$pentak_2015= Compare-Object -ReferenceObject $vs2015_before_penak -DifferenceObject $vs2015_after_penak
$pentak_2017= Compare-Object -ReferenceObject $vs2017_before_penak -DifferenceObject $vs2017_after_penak
