#!/bin/bash

python reset.py
bash run_sample_image.sh configs/sample.py
python clean.py
bash run_sample_video.sh configs/sample_adacache_moreg.py