# DEPRECATION WARNING

IF YOU ARE INTERESTED IN A MORE RECENT PROJECT ON USING FASTTEXT VECTORS IN RASA, TRY THE FOLLOWING CODE
https://github.com/RasaHQ/rasa-custom-fasttext

Credits to: https://github.com/koaning

THIS CODE BASE IS NOT MAINTAINED FOR OVER 3 YEARS. Life goes on!!


## Loading FastText vectors on Spacy

Tbe requirements are really simple. 

## Requirements

You should have docker

## Download the FastText vector

In order to build with fastText, first download the FastText vector you need in the langauge from here

[FastText Pre-trained vectors](https://github.com/facebookresearch/fastText/blob/master/docs/crawl-vectors.md)

## Load the vectors

Save the downloaded vector file in vector folder.

## Build with docker

Build the docker file as

```sh
docker build -t spacy-fasttext .
```

## Train your first model

Once the image is built, run the following command to build the first model
Go to terminal and reach the present directory first.


```sh
docker run -v $PWD:/app spacy-fasttext python load_fastText.py 
```

This will build the model in the model folder

## Package your model

```sh
docker run -v $PWD:/app spacy-fasttext python -m spacy package model model_package

docker run -it -v $PWWD::/app spacy-fasttext bash
cd model_package/nl_model-0.0.0
python setup.py sdist
```

This will then export a packaged model in .tar.gz, when then you can load for your NLP purposes.
