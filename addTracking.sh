#!/bin/bash
for file in ./*.html; 
do
   x="$(tail -n 2 $file | wc -c)"
   truncate --size=-$x $file
   cat ./statcounter >> $file
   echo -e '\n</body>\n</html>' >> $file
done
