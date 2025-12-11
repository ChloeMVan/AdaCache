#!/bin/bash

python reset.py
bash run_sample_image.sh configs/sample.py
sleep 5s
python clean.py
sleep 5s
bash run_sample_video.sh configs/sample_adacache_moreg.py