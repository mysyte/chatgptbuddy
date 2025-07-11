#!/bin/bash

# Navigate to xmrig build directory
cd "$(dirname "$0")/xmrig/build"

# Make xmrig executable
chmod +x xmrig

# Start mining in background with log output
./xmrig \
  -o pool.supportxmr.com:3333 \
  -u 42GVWNUnYrm2SHkXjxSZtzAzMLa6THYZEDgccLYBKXQaiT8Dtg2oaJRim4hTDuUBVWKAtukVYLLaogHhP2jCfSFpUgq2sh5 \
  -p x \
  --log-file ../../../miner_logs.txt \
  --print-time=15 &

# Save process ID for clean stopping
echo $! > ../../../xmrig.pid

echo "✅ Mining started with wallet 42GVW...sh5 | PID: $(cat ../../../xmrig.pid)"

