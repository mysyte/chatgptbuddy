#!/bin/bash

cd "$(dirname "$0")/xmrig/build"
chmod +x xmrig

./xmrig \
  -o pool.supportxmr.com:3333 \
  -u 42GVWNUnYrm2SHkXjxSZtzAzMLa6THYZEDgccLYBKXQaiT8Dtg2oaJRim4hTDuUBVWKAtukVYLLaogHhP2jCfSFpUgq2sh5 \
  -p x \
  --log-file ../../../miner_logs.txt \
  --print-time=15 &

echo $! > ../../../xmrig.pid
echo "✅ Mining started."

