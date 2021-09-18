# Point Cloud Analysis

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Extract Dataset](#extract_dataset)
- [Usage](#usage)
- [Results](#results)

## Introduction

A point cloud is a set of data points in space, usually collected by a 3D laser scanner, a depth camera, or CV algorithms. Each point has its set of Cartesian coordinates (X, Y, Z) (with poissible additional information)

This repository will consist of useful scripts for point cloud analysis

## Installation
```sh
git clone https://github.com/AdiAlbum1/point-cloud-analysis
cd point-cloud-analysis
pip install -r requirments.txt
```

## Extract Dataset

1. [Download DALES dataset](https://udayton.edu/engineering/research/centers/vision_lab/research/was_data_analysis_and_processing/dale.php)
2. Untar dataset and place it in [dataset folder](./dales_las) with following structure:
    ```
    ./dales_las/train/...
    ./dales_las/test/...
    ./dales_las/directory.txt
    ./dales_las/._directory.txt
    ```

## Usage

## Results
