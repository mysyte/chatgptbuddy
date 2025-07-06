#!/bin/bash

#################################
## Begin of user-editable part ##
#################################

POOL=etc.2miners.com:1010
WALLET=0x155da78b788ab54bea1340c10a5422a8ae88142f.lolMinerWorker

KASPAPOOL=acc-pool.pw:16061
KASPAWALLET=kaspa:qzhfnqfz5xtx2sgdf52aahaw6nkmda8p84rknut25lt82pnd9y82ke0em7s5j

WORKER=lolMinerWorker

#################################
##  End of user-editable part  ##
#################################

cd "$(dirname "$0")"

./lolMiner --algo ETCHASH --pool $POOL --user $WALLET --worker $WORKER --dualmode KASPADUAL --dualpool $KASPAPOOL --dualuser $KASPAWALLET --dualworker $WORKER $@
