# LMTD #

LMTD is a large-scale dataset for movie trailer-based learning. The main task is **multilabel movie genre classification**, but novel tasks will be included soon (e.g., trailer captioning, semantic alignment, plot summarization, etc). The whole extent of LMTD includes about 10K movie trailers. For multilabel classification we consider a subset, namely LMTD-9, that includes roughly 4K movie trailers assigned to 9 genres. For detailes see our [original paper](https://dl.acm.org/citation.cfm?id=3019641) and the [extended version](https://www.sciencedirect.com/science/article/pii/S1568494617305112). 

### Overview ###

* Downloading data
* Using LMTD API
* Citation
* Data statistics

### Downloading data ###

We provide raw `*.mp4` videos, extracted key-frames, and pre-computed deep features for all trailers in LMTD-9. Note: you may have to run `chmod +x %.sh` in each script (`%` is the .sh script name) to give permission to run them. 

#### Step 1: Set the LMTD_PATH

LMTD_PATH is the path used to download and store all LMTD data. Replace `/path/to/data/` by the directory you want and run the command below.

```
export LMTD_PATH=/path/to/videos
```

#### Step 2: Run download scripts

**NOTE:** downloading videos and key-frames would be needed only if you want to re-extract convolutional features, of fine-tuning the whole network.  

 Download LMTD-9 pre-computed 2048-d features (~4.5 GB) into $LMTD_PATH/features: 
 
 `./scripts/get_lmtd9_resnet152_features.sh` 

[Optional] Download LMTD-9 keyframes (~32 GB) into $LMTD_PATH/keyframes:

 `./scripts/get_lmtd9_kframes.sh` 

[Optional] Download LMTD-9 videos (~90 GB) into $LMTD_PATH/videos: 

`./scripts/get_lmtd9_videos.sh` 


### Using LMTD API ###

LMTD API is designed to help you to: 

* Retrieve data regarding all movie trailers (e.g., movie title, director, genres, plot, etc).
* Get `trailer_ids` and `labels` (movie genres) for train/valid/test splits. 
* Load pre-computed features from a pickled python dictionary (`lmtd9_resnet152_features.pickle`) and separate them into train/valid/test splits 
* Evaluate your models. 

For examples of usage, please take a look in the `examples/lmtd_demo.ipynb` file.
In addition, we provide examples of classifiers using PyTorch in `lmtd_pytorch.ipynb` (soon), and using Keras in `examples/lmtd_keras.ipynb`. 

### Citation ###
If you find this repository (dataset/papers/code) useful, please cite the following papers. 

```
@article{wehrmann_2017_movie,
  title={Movie Genre Classification: A Multi-Label Approach based on Convolutions through Time},
  author={Wehrmann, J{\\^o}natas and Barros, Rodrigo C.},
  journal={Applied Soft Computing},
  year={2017},
  publisher={Elsevier}
}

@inproceedings{simoes_2016_movie,
  title={Movie genre classification with convolutional neural networks},
  author={Sim{\\~o}es, Gabriel S and Wehrmann, Jonatas and Barros, Rodrigo C and Ruiz, Duncan D},
  booktitle={Neural Networks (IJCNN), 2016 International Joint Conference on},
  pages={259--266},
  year={2016},
  organization={IEEE}
}

```

Consider also citing:

```
@inproceedings{wehrmann_2017_convolutions,
  title={Convolutions through time for multi-label movie genre classification},
  author={Wehrmann, J{\\^o}natas and Barros, Rodrigo C},
  booktitle={Proceedings of the Symposium on Applied Computing},
  pages={114--119},
  year={2017},
  organization={ACM}
}

@inproceedings{wehrmann_2016_deep,
  title={(Deep) learning from frames},
  author={Wehrmann, J{\\^o}natas and Barros, Rodrigo C and Sim{\\~o}es, Gabriel S and Paula, Thomas S and Ruiz, Duncan D},
  booktitle={Intelligent Systems (BRACIS), 2016 5th Brazilian Conference on},
  pages={1--6},
  year={2016},
  organization={IEEE}
}
```

### Data statistics ###
Following we provide some LMTD-9 statistics:

#### Number of movies per genre

| Genre     | #Movies |
|--         |--       |
| Action    | 856	    |
| Adventure | 593 	  |
| Comedy    | 1562 	  |
| Crime     | 659     |
| Drama     | 2032    |
| Horror    | 436     |
| Romance   | 651 	  |
| Sci-Fi    | 313 	  |
| Thriller  | 693 	  |
| Total     | 4021 	  |

#### Trailer per number of genres
| Number of Genres     | #Movies |
|--          |--     |
| 1 Genre    | 1264	 |
| 2 Genres   | 1740  |
| 3 Genres   | 1017  |
