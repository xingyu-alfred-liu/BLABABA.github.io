---
permalink: /project/
title: "Project"
excerpt: "My projects"
---

## Feature Reduction for CIFAR-100 (Python, Tensorflow, Scikit-Learn)  

![Image of CIFAR project](https://BLABABA.github.io/images/mpb_pipeline.png)  

The project pipeline is shown in the figure above, the CIFAR-100 images was first fed into a CNN for image classification. Then the corresponding image representations were extracted from three layers: input layer, flatten layer, and the fully connected layer. Then dimensionality reduction were performed with these extracted features to further reduce the dimensionality to a 2-dimensional feature space. To confirm the best hyperparameters settings, and to compare the performance of PCA, t-SNE, and isomap, logistic regression was applied to these reduced features to train a classification model. With the quantitative classification accuracy, the optimum hyperparameter set was confirmed. 

Logistic regression was applied to generate quantitative comparisons among the three dimensionality reduction methods PCA, t-SNE, and isomap. The metric which yielded the highest classification accuracy from logistic regression is confirmed as the most suitable feature reduction for CIFAR-100 dataset. Three layers, the input image, flattened layer after the convolutional processing, and the fully connected layer before output were chosen because we would like to compare the improvement of the feature extraction after different treatment. This improvement among CNN layers can be detected by visualization of the reduced features and the logistic regression model performances.

![Image of CIFAR project2](https://BLABABA.github.io/images/pca_tsne_isomap.png)  

Among the three metrics, t-SNE gives the best performance. For the input CIFAR-100 images, PCA, t-SNE, and isomap showed almost the same effect as the classification accuracy are almost identical. After the convolutional image processing, t-SNE showed better performance than PCA and isomap. The difference between PCA and isomap at this layer is still merely observable. For the FC layer, the t-SNE showed much better results than PCA and isomap. In this layer, isomap starts to generate more representable features than PCA, but not comparable to t-SNE. 

The visualizations of the reduced FC features with PCA, t-SNE, and isomap are shown in Figure \ref{fig:pca_tsne_isomap}. Results of PCA showed that different classes are still mingled together. A bit better than that of PCA, isomap tends to separate different classes, but not very obvious. t-SNE clearly clustered some classes, such as the light yellow, red, and purple point in the figure. This also explains why t-SNE showed the highest accuracy. 


## Enhance the Band Gap Classifier for Organic Molecular Crystals with Batch Mode Active Learning  

Machine learning techniques routinely demand large amount of annotated data points to formulate a decent model. However, data annotation such as density functional theory (DFT) calculation, a physics framework computing the bandgap of atomic systems using atomic element and coordinate information as input, requires extensive computer time. In order to maximize the efficiency of obtaining a classifier with decent performance with less demanded computing resources, active learning (AL) is designed to select the next batch of unlabeled data points. Classical AL strategies request single annotation in each iteration, however, this could be inefficient for DFT calculations where high-throughput computing with thousands of CPUs running in parallel can be performed. Considering both the budget of computing resources and expected improvement of classifier performance, we want to study if the batch mode AL (BMAL) could maximize the efficiency of information gain for bandgap classification problem.

AL, as an effective tool with great potential, has been widely studied and applied into various areas in the past two decades. Multiple practical challenges about active learning have been listed, such as how to prevent erroneous annotation from being added to training data, and how to consider the various labeling costs. Limited by available data, we will only discuss different methods about query in batch. Different general ideas were proposed about BMAL. Xu et al. indicates the approach where the next batch is constructed such that unlabeled data are selected from high-density region. In the mean time, the diversity among the next batch is maintained at an user-specified level. On the other hand, Hoi et al. utilizes Fisher information matrix to quantify the uncertainty of the classification model. Acquiring the next batch of unlabeled structures simply asks the next batch yielding the maximized reduction of Fisher information matrix.

Studying the optimal BMAL strategy for bandgap classification could grant us an efficient path searching for replacements of the light-absorbing materials in organic solar cell devices, which usually demands tests run by large amount of manual labors and chemical samples. With a better performed bandgap classifier, clear energy could be delivered with less cost and time. Although statistical techniques have been gradually implemented into materials research, to the best knowledge of the authors, no band gap classifier has been studied specifically for organic molecular crystals. Here, we compare three BMAL query methods for a set of molecular materials.

![Image of SF process](https://BLABABA.github.io/images/bmal.png)  

The comparison between _Relevance, Density and Diversity_ and _Fisher Information Matrix Reduction_ shows that _Fisher Information Matrix Reduction_ is more informative given the same initial structure set and unlabeled structure pool. However, this advantage of using Fisher Information matrix only exists when the labeled structure set is relatively small. When the classification accuracy is close to final converged optimum, the model performance generated by these two strategies start to behave similarly.


## Phenylated and Pyrene-Fused Acenes Derivatives as Singlet Fission Candidate   

Singlet fission (SF) is a photophysical process considered as a possible scheme to bypass the Shockley–Queisser limit by generating two triplet-state excitons from one high-energy photon. Polyacene crystals, such as tetracene and pentacene, have shown outstanding SF performance both theoretically and experimentally. However, their instability prevents them from being utilized in SF-based photovoltaic devices. Several strategies were attepmted to stabilize this family of compounds. One approach is attaching side groups, such as phenyl side groups. The other approach was proposed recently by fusing pyrene terminals. In search of practical SF candidates, a series of phenylated acenes and pyrene-fused acenes were studied using many-body perturbation theory within the GW approximation and Bethe–Salpeter equation.  

![Image of phenylated_acene](https://BLABABA.github.io/images/phenylated_acene_struct.png)  

Various packing motif were generated and hence lead to various electronic properties, such as different frontier-orbital induced band dispersion. Details can be found in this [paper](https://pubs.acs.org/doi/abs/10.1021/acs.jpcc.8b12549). 

![Image of pfa](https://BLABABA.github.io/images/pfa_struct.png)  

Pyrene-fused acenes were observed with different packings as well.  
One issue pointed out in this [paper](https://iopscience.iop.org/article/10.1088/1361-648X/ab699e/meta) was about the convergence of exciton wave-functions with respect to fine k-point grid when generating mean-field wave-functions. A threshold was proposed to confirm the convergence. 

![Image of exciton_wfn](https://BLABABA.github.io/images/pfa_exciton_wfn_convergence.png)  

## Fully-Printable Perovskite Solar Cell   
The organic–inorganic hybrid lead halide perovskite materials has been widely implemented into solar cells as the perovskite light absorbers. The highest power cponversion efficiency of this type of device has reached 22.7%, far exceeding that of the other emerging photovoltaic technologies such as dye-sensitized solar cells (DSSCs). Most perovskite solar cell devices still need Au or Ag as their counter electrodes, which are commonly deposited by thermal evaporation. However, the usage of noble metals is not favorable for commercialization. In this regard, carbon-based perovskite solar cell, which employs carbon as the counter electrode, has been introduced. Additionally, the carbon-based solar cell device can be fabricated via fully-printing procedure, which is propitious for massive production.  

![Image of SF process](https://BLABABA.github.io/images/hysterisis.png)  

The hysteretic phenomenon commonly exists in the J–V curves of perovskite solar cells with different structures, especially for carbon-based mesoscopic perovskite solar cells without hole-conductor. By adding moderate amounts of methylammonium chloride (MACl) into MAPbI3 perovskite precursor, we found the J–V hysteresis of carbon-based perovskite solar cells could be significantly alleviated and the crystallinity of MAPbI3 perovskite could also be influenced. As shown in the figure above, the J-V curve for MACl-added perovskite solar cell shows almost no hysteresis and presents significantly higher power conversion efficiency. 

Click [here](https://pubs.rsc.org/ko/content/articlehtml/2018/ra/c8ra04347g) for the full paper.  