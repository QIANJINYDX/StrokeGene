# RESEARCH ARTICLE Causal associations of particulate matter 2.5 and cardiovascular disease: A two-sample mendelian random iz ation study  

Ye Cao ID , Yi Feng 2 , Nan Xia 2 , Jiancheng Zhang ID 1 \*  

1  Department of Cardiology, Fujian Provincial Hospital, Shengli Clinical Medical College of Fujian Medical University, Fuzhou, Fujian, P. R. China,  2  Department of Cardiology, Renmin Hospital, Hubei University of Medicine, Shiyan, Hubei, P. R. China  

![](images/e1c10853a1df3af4b6d59e4aae60fc5c29a3d38f431531857ed55dc27f57bd95.jpg)  

Citation:  Cao Y, Feng Y, Xia N, Zhang J (2024) Causal associations of particulate matter 2.5 and cardiovascular disease: A two-sample mendelian random iz ation study. PLoS ONE 19(4): e0301823. https://doi.org/10.1371/journal.pone.0301823  

Editor:  Worradorn Phairuang, Kanazawa University, JAPAN  

Received:  October 15, 2023  

Accepted:  March 20, 2024  

Published:  April 5, 2024  

Copyright:  $\copyright$   2024 Cao et al. This is an open access article distributed under the terms of the  Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.  

Data Availability Statement:  All data used in the present study were obtained from genome-wide association study summary statistics which were publicly released by genetic consortia( https://gwas. mrcieu.ac.uk/ ).  

Funding:  This study was supported by the National Natural Science Foundation of China (grant no. 82070341) and the Natural Science Foundation of Fujian Province of China (grant no. 2019J01189). The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.  

\*  fj zhang jian cheng@126.com  

# Abstract  

# Background  

According to epidemiological studies, particulate matter 2.5 (PM2.5) is a significant contributor to cardiovascular disease (CVD). However, making causal inferences is difficult due to the methodological constraints of observational studies. In this study, we used two-sample Mendelian random iz ation (MR) to examine the causal relationship between PM 2.5 and the risk of CVD.  

# Methods  

Genome-wide association study (GWAS) statistics for PM2.5 and CVD were collected from the FinnGen and UK Biobanks. Mendelian random iz ation analyses were applied to explore the causal effects of PM2.5 on CVD by selecting single-nucleotide polymorphisms(SNP) as instrumental variables.  

# Results  

The results revealed that a causal effect was observed between PM2.5 and coronary artery disease(IVW: OR 2.06,  $95\%$   CI 1.35, 3.14), and hypertension(IVW: OR 1.07,  $95\%$   CI 1.03, 1.12). On the contrary, no causal effect was observed between PM2.5 and myocardial infarction(IVW: OR 0.73,  $95\%$   CI 0.44, 1.22), heart failure(IVW: OR 1.54,  $95\%$   CI 0.96,

 2.47), atrial fibrillation(IVW: OR 1.03,   $95\%$   CI 0.71, 1.48), and ischemic stroke (IS)(IVW: OR

 0.98,   $95\%$   CI 0.54, 1.77).  

# Conclusion  

We discovered that there is a causal link between PM2.5 and coronary artery disease and hypertension in the European population, using MR methods. Our discovery may have the significance of public hygiene to improve the understanding of air quality and CVD risk.  

Competing interests:  The authors have declared that no competing interests exist.  

# 1 Introduction  

Air pollution is a complicated combination of particulate matter (PM) and gaseous contaminants. Although the relative hazards associated with air pollution are lower than those associated with more established risk factors (such as hyper lipid emi a and cigarette use), it nevertheless constitutes a danger to public health since it affects billions of people every day without their consent [ 1 ]. PM is the major component of air pollution and is made up of a variety of aerosols with different sizes and compositions, such as metals, carbon dioxide, organic species, and inorganic nitrates and sulfates [ 2 ,  3 ]. There is broad scientific agreement that among size portions, PM2.5 is the most firmly established to have negative health consequences and is responsible for the largest worldwide public health burden [ 4 ].  

Although exposure to PM2.5 has been linked to a variety of health issues, cardiovascular disease(CVD) is the primary cause of PM2.5-related mortality [ 5 ,  6 ]. Moreover, PM2.5 has been identified as a significant risk factor for cardiovascular morbidity and death by health organizations throughout the world, including the American Heart Association and the European Society of Cardiology [ 7 ,  8 ]. The mechanism research validated that exposure to PM2.5 will impact systemic inflammation, oxidative stress, and the autonomic nervous system. The endo the li al, endocrine, and thrombosis pathways will be affected by these consequences, which will cause hypertension, arrhythmia, and artery stiffness, and eventually lead to CVDs [ 9 ]. Numerous epidemiological studies and meta-analyses have established the link between exposure to PM2.5 and an increased risk of CVDs, including coronary artery disease(CAD), myocardial infarction(MI), heart failure(HF), atrial fibrillation(AF), ischemic stroke(IS), and hypertension (HTN) [ 10 ].  

However, the above association is mainly based on epidemiological research. Although the quality and amount of evidence generated in the recent past have improved significantly, observational research is essentially affected by residual confusion and reversal causation. Additionally, no research has yet looked at the combined impact of PM2.5 and genetic polymorphisms on the risk of CVD. Prior research indicates that genetic polymorphism should be taken into account when exploring the effects of pollutants on various physiological and immunological processes in humans, especially in cardiovascular diseases and respiratory diseases [ 11 ,  12 ]. For instance, a panel study revealed that individuals with the glut at hi one Stransfer as e mu 1 genotype are more vulnerable to air pollution [ 12 ].  

Mendelian random iz ation (MR) is a unique method for examining the causal relationship between risk factors and outcomes that employs genetic variations as instrumental variables (IVs), and this approach is extensively utilized in the study of CVD [ 13 ,  14 ]. Because genetic variations are assigned at random before illness starts, MR analysis might eliminate confounding variables and reverse causation, allowing researchers to find more causal drivers of a certain outcome [ 15 ]. In our study, a two-sample MR research was used to explore the potential causality between PM2.5 and CVD risk with the use of extensive genome-wide association study (GWAS) data.  

# 2 Materials and methods  

# 2.1 Study design  

This study adhered to the STROBE-MR (Strengthening the Reporting of Observational Studies in Epidemiology Using Mendelian Random iz ation) guidelines [ 16 ], and the STORBE-MR checklist is provided in  S1 Table . Only when the following MR study assumptions are met may a convincing conclusion be reached. First, the exposure (PM2.5) and the genetic IVs should be highly related. Second, the possible con founders such as body mass index(BMI),  

Table 1. Basic information about the GWAS database of the exposure and outcomes. 
![](images/233682c1bbe64ad2f70b3ad6049cd99ceeadf5581f94487dec902c26bc353af3.jpg)  
https://doi.org/10.1371/journal.pone.0301823.t001  

lipoprotein s (total cholesterol, triglycerides, low-density lipoprotein, high-density lipoprotein), smoking status, diabetes, blood pressure, and others have nothing to do with the genetic IVs. Third, the genetic IVs only affect the outcome (CVD) via PM2.5 [ 17 ,  18 ].  

# 2.2 Data sources  

In this study, summary-level results from GWAS were utilized. GWAS summary statistics for PM2.5 included a total of 423,796 European participants with 9,851,867 SNPs. The outcomes include CAD, MI, HF, AF, IS, and HTN. For the same circumstance, we acquired summarylevel data for the outcome events from the GWAS database. The basic information about the GWAS database of the exposure and outcomes can be seen in  Table 1 .  

# 2.3 Selection and validation of SNPs  

We used three criteria to identify independent SNPs related to PM2.5. First, SNPs with a genome-wide significance threshold of  $\mathsf{p<5x10^{-8}}$    were chosen. Second, paired linkage disequilibrium was employed to assess the independence of the chosen SNPs. SNPs situated at a distance of  $1000\,\mathrm{kb}$   apart were chosen, and those in linkage d is equilibrium (LD)   $(\mathbf{r}^{2}<\!0.001)$  were removed [ 19 ]. Third, the F-statistic was used to confirm the power of every SNP [ 20 ]. When F-statistics were more than 10, SNPs were thought to be effective enough to counteract the effects of possible bias. Furthermore, the Phe no Scanner database was used to rule out the effect of possible con founders [ 21 ].  

# 2.4 Two-sample MR analysis  

We employed three methods(MR egger, weighted median, inverse variance weighted) in this two-sample MR study to obtain causal relationships between PM2.5 and CVD [ 22 ]. In our MR study, the inverse variance weighted (IVW) analysis is the primary method as it produces the most convincing estimates when the IVs absent directional pleiotropy [ 23 ]. To eliminate the horizontal pleiotropy, the other two analytical methods are used. The aforementioned methods of analysis are all centered on various horizontal pleiotropy models. Thus, we may assess the reliability of our results by comparing the consistency of three different methodologies [ 24 ]. Cochran’s Q-test assessed IV heterogeneity, with a  $p<0.05$   result suggesting heterogeneity. We evaluated horizontal pleiotropy using the MR-Egger intercept test [ 25 ,  26 ]. Furthermore,  

we utilized the leave-one-out approach to determine if a single SNP disrupted the causative impact. Two Sample MR (0.5.7) packages were used to do all statistical analyses in R software

 (4.2.3). A value of  $p<0.05$   was regarded as suggestive significance and associations with  $\boldsymbol{p}$   ${<}0.0083$  (Bonferroni correction  $\dot{p}=0.05/6)$  ) were considered statistically significant [ 27 ]. In addition, we assessed the power of this current MR analysis using the "mRnd" tool [ 28 ].  

# 3 Results  

# 3.1 The causal effect of cardiovascular disease  

We got 8 SNPs related to PM2.5 based on the screening criterion. Then, using the Phenoscanner database, we eliminated the rs1537371 related to CAD and rs77205736 related to BMI. We eventually got 6 SNPs. The details of SNPs are shown in  Table 2 .  

The two-sample MR analysis using three methods for the association of PM2.5 with CVD is shown in  Fig 1  and  S1 Fig . The IVW results revealed that causal effect was observed between PM2.5 and CAD(IVW: OR 2.06,  $95\%$   CI 1.35, 3.14), and HTN(IVW: OR 1.07,  $95\%$   CI 1.03, 1.12). After multiple testing corrections, statistical differences persist. Similar results were observed using the weighted median method. On the contrary, no causal effect was observed between PM2.5 and MI(IVW: OR 0.73,  $95\%$   CI 0.44, 1.22), HF(IVW: OR 1.54,  $95\%$   CI 0.96, 2.47), AF(IVW: OR 1.03,  $95\%$   CI 0.71, 1.48), and IS(IVW: OR 0.98,  $95\%$   CI 0.54, 1.77). The MR power of PM2.5 on CAD was 1.0, and the powers of other outcomes were all less than 0.8. The MR powers are shown in  S2 Table .  

# 3.2 Sensitivity analysis validation  

No significant heterogeneity was discovered by Cochran’s Q-test. Consequently, we choose to apply the fixed-effects IVW approach. Then, we used an MR-Egger intercept test and leaveone-out analysis to remove the bias caused by horizontal pleiotropy. The MR-Egger intercept test revealed no directional pleiotropy. The scatter plots of the association between PM2.5 and CVD are shown in  S2 Fig . In the meantime, the leave-one-out analysis revealed the stability of the MR effect estimates, which are shown in  S3 Fig .  

# 4 Discussion  

In this study, we found a causal relationship between PM2.5 and the risk of CAD and HTN by a two-sample MR method, while no causal relationship between PM2.5 and MI, HF, AF, and IS susceptibility.  

Our research results are consistent with some previous epidemiological results. The most recent meta-analysis, published in 2023, found increased exposure to  $\mathrm{PM}\,2.5$   levels is significantly associated with an increased risk of all-cause mortality (HR 1.08,  $95\%$   CI 1.05, 1.11), CVD(HR 1.09,  $95\%$   CI 1.00, 1.18), and CVD mortality(HR 1.12,  $95\%$   CI 1.07, 1.18) [ 29 ].  

Table 2. SNPs of PM2.5 with statistically significant threshold. 
![](images/668a72b5c25e08c4a036cfd0441b3f5bafa6bcfd5a5db0c7e0491d76fe0f64d6.jpg)  
https://doi.org/10.1371/journal.pone.0301823.t002  

![](images/e4318677d8173b6f5ee7014684d291acf59ede4c7b343c1fa68260070436a9a5.jpg)  

https://doi.org/10.1371/journal.pone.0301823.g001  

Another meta-analysis, also published in 2023, found  $\mathrm{PM}\,2.5$   (every   $10\upmu\mathrm{g}/\mathrm{m}^{3}$    rise) increased the risk of hypertension(RR 1.14,  $95\%$   CI 1.09, 1.19), and coronary heart disease (RR 1.21,  $95\%$  CI 1.08, 1.35) [ 30 ]. In addition, the results of the other two meta-analyses did not support the notion that PM2.5 can raise the risk of  $\mathrm{AF}(\mathrm{RR}\:0.89,95\%\:\mathrm{CI}\:0.20,1.57)$  ) and  $\mathrm{HF}(\mathrm{HR}\;1.07,95\%$  CI 0.72, 1.60) [ 31 ,  32 ]. Naturally, there is some prior research that contradicts our findings. In our investigation, there was no evidence of a causal relationship between PM2.5 and MI, AF, or IS. Nevertheless, some research has revealed that exposure to  $\mathrm{PM}\,2.5$   increases the risk of MI [ 33 ,  34 ], AF [ 35 ], and IS [ 30 ,  36 ,  37 ].  

The variations showed that instead of identifying a causal relationship, epidemiology study findings can be constrained by con founders and research design. It is crucial to remember that confounding factors such as different lifestyles, baseline health, socioeconomic status, additional environmental variables, and many other variables could distort this epidemiological research. Obviously, because we used summary-level data in our MR analysis, we cannot completely rule out the potential of a nonlinear causal relationship between PM2.5 and MI, AF, and IS. To investigate potential dose-response causal relationships, further MR research should be carried out using individual-level data and longitudinal designs.  

Based on data from epidemiological research together with animal and to xico logic trials, the mechanism by which  $\operatorname{PM}2.5$   raises the risk of CVD has been partially clarified. PM2.5 may interact with pulmonary and immunological cells, as well as neural receptors, and entering the systemic circulation can set off a chain of events that contribute to the acute and chronic impacts of CVD [ 38 ,  39 ]. PM2.5 may deposit on vascular endothelium, aggravating local oxidative stress and inflammation, leading to at hero sclerotic plaque instability and, eventually, thrombus development [ 40 ]. PM2.5 can cause systemic inflammation and endo the li al  

dysfunction, which can accelerate the progression of atherosclerosis [ 41 ,  42 ]. In addition, PM 2.5 may raise the possibility of acquiring other well-known risk factors for cardiovascular disease including diabetes, hypertension, and hyper lipid emi a [ 43 – 45 ].  

This study presents several benefits. First, this is the first study to use a two-sample MR analysis with data from the GWAS summary-level data to look at the causal link between PM2.5 and CVD. A two-sample method can lower potential con founders and reverse causality in large genomic data summaries. Second, through sensitivity analysis using several MR methods and various model assumptions, the findings were confirmed. All of the analyses indicated that the findings were solid and trustworthy.  

However, this research did have certain restrictions. First, we stress that, due to the relatively small amount of PM2.5 variability that can be explained by real SNPs, our analytical power is somewhat constrained when analyzing the minimal influence of PM2.5 on CVD. Second, it is important to emphasize that our research heavily relied on pre-existing GWAS data. While there are no GWASs for distinct areas of PM2.5, it might be challenging to ascertain how different areas affect the causal relationship between PM2.5 and CVD. Third, in our analysis, the CVD GWAS statistics were limited to European groups to ensure that SNPs are not linked to any confounding factors between PM2.5 and CVD. Thus the results cannot be extrapolated to other populations. Fourth, our investigation may produce false negative results because of its inadequate powers. These results therefore need to be interpreted with caution. This suggests that to provide definitive evidence, larger-scale, specific GWAS data are required. Finally, the MR results only represent the long-term effects of PM2.5 on CVD, not the short-term effects. Therefore, more study is needed to determine the short-term impact of PM2.5 on CVD.  

# 5 Conclusion  

We discovered that there is a causal link between PM2.5 and CAD and HTN in the European population, using MR methods. Our discovery may have the significance of public hygiene to improve the understanding of air quality and CVD risk.  

# Supporting information  

S1 Fig. Forest plots of the association of PM2.5 with CVD.  CAD: coronary artery disease; MI: myocardial infarction; HF: heart failure; AF: atrial fibrillation; IS: ischemic stroke; HTN: hypertension. (TIF)  

S2 Fig. Scatter plots of the association of PM2.5 with CVD.  CAD: coronary artery disease; MI: myocardial infarction; HF: heart failure; AF: atrial fibrillation; IS: ischemic stroke; HTN: hypertension. (TIF)  

S3 Fig. The leave-one-out sensitivity analysis of PM2.5 with CVD.  CAD: coronary artery disease; MI: myocardial infarction; HF: heart failure; AF: atrial fibrillation; IS: ischemic stroke; HTN: hypertension. (TIF)  

S1 Table. STORBE-MR checklist. (DOCX)  

S2 Table. The MR powers of CVD. (DOCX)  

# Acknowledgments  

We sincerely thank the researchers in the MiBioGen, UK Biobank, and other consortiums or studies and all the researchers who worked on the data collection.  

# Author Contributions  

Data curation:  Ye Cao, Yi Feng.  

Funding acquisition:  Jiancheng Zhang.  

Methodology:  Ye Cao, Yi Feng.  

Software:  Ye Cao.  

Validation:  Ye Cao, Jiancheng Zhang.  

Visualization:  Ye Cao, Nan Xia.  

Writing – original draft:  Ye Cao, Yi Feng.  

Writing – review & editing:  Ye Cao, Nan Xia, Jiancheng Zhang.  

# References  

1. Cohen AJ, Ross Anderson H, Ostro B, Pandey KD, Kr zy za now ski M, Ku¨nzli N, et al. The global burden of disease due to outdoor air pollution. Journal of Toxicology and Environmental Health, Part A. 2005; 68(13–14):1301–7.  https://doi.org/10.1080/15287390590936166  PMID:  16024504

 2. Zhang K, Brook RD, Li Y, Raja gopalan S, Kim JB. Air Pollution, Built Environment, and Early Cardiovascular Disease. Circ Res. 2023; 132(12):1707–24. Epub 20230608.  https://doi.org/10.1161/ CIRCRESAHA.123.322002  PMID:  37289906 ; PubMed Central PMCID: PM C 10254077.

 3. Yang L, Zhang Y, Qi W, Zhao T, Zhang L, Zhou L, et al. Adverse effects of PM(2.5) on cardiovascular diseases. Rev Environ Health. 2022; 37(1):71–80. Epub 20210401.  https://doi.org/10.1515/reveh2020-0155  PMID:  33793141 .

 4. Global burden of 87 risk factors in 204 countries and territories, 1990–2019: a systematic analysis for the Global Burden of Disease Study 2019. Lancet. 2020; 396(10258):1223–49.  https://doi.org/10.1016/ S0140-6736(20)30752-2  PMID:  33069327 ; PubMed Central PMCID: PMC7566194.

 5. Cosselman KE, Navas-Acien A, Kaufman JD. Environmental factors in cardiovascular disease. Nature Reviews Cardiology. 2015; 12(11):627–42.  https://doi.org/10.1038/nrcardio.2015.152  PMID:  26461967

 6. Pope CA. Are Adults with Chronic Obstructive Pulmonary Disease Vulnerable to Air Pollution and Cardio vascular Risk? American Journal of Respiratory and Critical Care Medicine. 2021; 204(2):116–8. https://doi.org/10.1164/rccm.202103-0647ED  PMID:  33835901

 7. Brauer M, Casadei B, Harrington RA, Kovacs R, Sliwa K. Taking a stand against air pollution—the impact on cardiovascular disease. Eur Heart J. 2021; 42(15):1460–3.  https://doi.org/10.1093/eurheartj/ ehaa1025  PMID:  33507239 ; PubMed Central PMCID: PMC7953955.

 8. Brook RD, Raja gopalan S, Pope CA 3rd, Brook JR, Bhatnagar A, Diez-Roux AV, et al. Particulate matter air pollution and cardiovascular disease: An update to the scientific statement from the American Heart Association. Circulation. 2010; 121(21):2331–78. Epub 20100510.  https://doi.org/10.1161/CIR. 0b013e3181dbece1  PMID:  20458016 .

 9. de Bont J, Jaganathan S, Dahlquist M, Persson  Å , Stafoggia M, Ljungman P. Ambient air pollution and cardiovascular diseases: An umbrella review of systematic reviews and meta-analyses. J Intern Med. 2022; 291(6):779–800. Epub 20220308.  https://doi.org/10.1111/joim.13467  PMID:  35138681 ; PubMed Central PMCID: PMC9310863.

 10. Dwivedi AK, Vis hwa karma D, Dubey P, Reddy SY. Air Pollution and the Heart: Updated Evidence from Meta-analysis Studies. Curr Cardiol Rep. 2022; 24(12):1811–35. Epub 20221125.  https://doi.org/10. 1007/s11886-022-01819-w  PMID:  36434404 .

 11. Zanobetti A, Baccarelli A, Schwartz J. Gene-air pollution interaction and cardiovascular disease: a review. Prog Cardiovasc Dis. 2011; 53(5):344–52.  https://doi.org/10.1016/j.pcad.2011.01.001  PMID: 21414469 ; PubMed Central PMCID: PMC3073822.

 12. Zeng X, Tian G, Zhu J, Yang F, Zhang R, Li H, et al. Air pollution associated acute respiratory inflammation and modification by GSTM1 and GSTT1 gene polymorphisms: a panel study of healthy undergraduates. Environ Health. 2023; 22(1):14. Epub 20230127.  https://doi.org/10.1186/s12940-022- 00954-9  PMID:  36703205 ; PubMed Central PMCID: PMC9881318.  

13. Wang J, Tan J, Hua L, Sheng Q, Huang X, Liu P. Genetic Predisposition of Both Waist Circumference and Hip Circumference Increased the Risk of Venous Thr ombo embolism. Thromb Haemost. 2023; 123 (3):347–61. Epub 20221116.  https://doi.org/10.1055/a-1980-8852  PMID:  36384228 ; PubMed Central PMCID: PMC9981277.

 14. Wang W, Tan JS, Wang J, Xu W, Bai L, Jin Y, et al. Genetically predicted waist circumference and risk of atrial fibrillation. Chin Med J (Engl). 2024; 137(1):82–6. Epub 20230829.  https://doi.org/10.1097/ CM9.0000000000002775  PMID:  37646132 ; PubMed Central PMCID: PM C 10766313.

 15. Emdin CA, Khera AV, Kathiresan S. Mendelian Random iz ation. Jama. 2017; 318(19):1925–6.  https:// doi.org/10.1001/jama.2017.17219  PMID:  29164242 .

 16. S kr ivan kova VW, Richmond RC, Woolf BA, Yarm olin sky J, Davies NM, Swanson SA, et al. Strengthening the reporting of observational studies in epidemiology using Mendelian random iz ation: the STROBE-MR statement. Jama. 2021; 326(16):1614–21.  https://doi.org/10.1001/jama.2021.18236 PMID:  34698778

 17. Evans DM, Davey Smith G. Mendelian random iz ation: new applications in the coming age of hypothesis-free causality. Annual review of genomics and human genetics. 2015; 16:327–50.  https://doi.org/10. 1146/annurev-genom-090314-050016  PMID:  25939054

 18. Burgess S, Scott RA, Timpson NJ, Davey Smith G, Thompson SG, Consortium E-I. Using published data in Mendelian random iz ation: a blueprint for efficient identification of causal risk factors. European journal of epidemiology. 2015; 30:543–52.  https://doi.org/10.1007/s10654-015-0011-z  PMID: 25773750

 19. Abecasis GR, Altshuler D, Auton A, Brooks LD, Durbin RM, Gibbs RA, et al. A map of human genome variation from population-scale sequencing. Nature. 2010; 467(7319):1061–73.  https://doi.org/10.1038/ nature 09534  PMID:  20981092 ; PubMed Central PMCID: PMC3042601.

 20. Burgess S, Thompson SG, Collaboration CCG. Avoiding bias from weak instruments in Mendelian randomization studies. International journal of epidemiology. 2011; 40(3):755–64.  https://doi.org/10.1093/ ije/dyr036  PMID:  21414999

 21. Kamat MA, Blackshaw JA, Young R, Surendran P, Burgess S, Danesh J, et al. Phe no Scanner V2: an expanded tool for searching human genotype–phenotype associations. Bioinformatics. 2019; 35 (22):4851–3.  https://doi.org/10.1093/bioinformatics/btz469  PMID:  31233103

 22. Pagoni P, Dimou NL, Murphy N, Sterg i a koul i E. Using Mendelian random is ation to assess causality in observational studies. BMJ Ment Health. 2019; 22(2):67–71.  https://doi.org/10.1136/ebmental-2019- 300085  PMID:  30979719

 23. Burgess S, Davey Smith G, Davies NM, Dudbridge F, Gill D, Glymour MM, et al. Guidelines for performing Mendelian random iz ation investigations: update for summer 2023. Wellcome Open Res. 2019; 4:186. Epub 20230804.  https://doi.org/10.12688/wellcome open res.15555.3  PMID:  32760811 ; PubMed Central PMCID: PMC7384151.

 24. Burgess S, Thompson SG. Multivariable Mendelian random iz ation: the use of pleiotropic genetic variants to estimate causal effects. Am J Epidemiol. 2015; 181(4):251–60. Epub 20150127.  https://doi.org/ 10.1093/aje/kwu283  PMID:  25632051 ; PubMed Central PMCID: PMC4325677.

 25. Bowden J, Davey Smith G, Burgess S. Mendelian random iz ation with invalid instruments: effect estimation and bias detection through Egger regression. International journal of epidemiology. 2015; 44 (2):512–25.  https://doi.org/10.1093/ije/dyv080  PMID:  26050253

 26. Greco M FD, Minelli C, Sheehan NA, Thompson JR. Detecting pleiotropy in Mendelian random is ation studies with summary data and a continuous outcome. Statistics in medicine. 2015; 34(21):2926–40. https://doi.org/10.1002/sim.6522  PMID:  25950993

 27. Curtin F, Schulz P. Multiple correlations and Bonferroni’s correction. Biological psychiatry. 1998; 44 (8):775–7.  https://doi.org/10.1016/s0006-3223(98)00043-2  PMID:  9798082

 28. Brion MJ, Shakhbazov K, Visscher PM. Calculating statistical power in Mendelian random iz ation studies. Int J Epidemiol. 2013; 42(5):1497–501.  https://doi.org/10.1093/ije/dyt179  PMID:  24159078 ; PubMed Central PMCID: PMC3807619.

 29. Kr it tana wong C, Qadeer YK, Hayes RB, Wang Z, Virani S, Thurston GD, et al. PM2.5 and Card i ovas cular Health Risks. Curr Probl Cardiol. 2023; 48(6):101670. Epub 20230223.  https://doi.org/10.1016/j. cpcardiol.2023.101670  PMID:  36828043 .

 30. Sun M, Li T, Sun Q, Ren X, Sun Z, Duan J. Associations of long-term particulate matter exposure with car dio metabolic diseases: A systematic review and meta-analysis. Sci Total Environ. 2023; 903:166010. Epub 20230803.  https://doi.org/10.1016/j.scitotenv.2023.166010  PMID:  37541522 .  

31. Shao Q, Liu T, Koran t zo poul os P, Zhang Z, Zhao J, Li G. Association between air pollution and development of atrial fibrillation: A meta-analysis of observational studies. Heart & Lung: The Journal of Cardiopulmonary and Acute Care. 2016; 45(6):557–62.  https://doi.org/10.1016/j.hrtlng.2016.08.001  PMID: 27590407

 32. Pranata R, Vania R, Tondas AE, Setianto B, Santoso A. A time-to-event analysis on air pollutants with the risk of cardiovascular disease and mortality: A systematic review and meta-analysis of 84 cohort studies. Journal of Evidence-Based Medicine. 2020; 13(2):102–15.  https://doi.org/10.1111/jebm.12380 PMID:  32167232

 33. Zhu W, Cai J, Hu Y, Zhang H, Han X, Zheng H, et al. Long-term exposure to fine particulate matter relates with incident myocardial infarction (MI) risks and post-MI mortality: A meta-analysis. Chemosphere. 2021; 267:128903.  https://doi.org/10.1016/j.chemosphere.2020.128903  PMID:  33213879

 34. Luo C, Zhu X, Yao C, Hou L, Zhang J, Cao J, et al. Short-term exposure to particulate air pollution and risk of myocardial infarction: a systematic review and meta-analysis. Environmental Science and Pollution Research. 2015; 22(19):14651–62.  https://doi.org/10.1007/s11356-015-5188  $\times$   PMID:  26298338

 35. Chen M, Zhao J, Zhuo C, Zheng L. The Association Between Ambient Air Pollution and Atrial Fibrillation A Systematic Review and Meta-Analysis. International Heart Journal. 2021; 62(2):290–7.  https://doi. org/10.1536/ihj.20-523

 36. Shah ASV, Lee KK, McAllister DA, Hunter A, Nair H, Whiteley W, et al. Short term exposure to air pollution and stroke: systematic review and meta-analysis. BMJ. 2015; 350:h1295.  https://doi.org/10.1136/ bmj.h1295  PMID:  25810496

 37. Niu Z, Liu F, Yu H, Wu S, Xiang H. Association between exposure to ambient air pollution and hospital admission, incidence, and mortality of stroke: an updated systematic review and meta-analysis of more than 23 million participants. Environmental Health and Preventive Medicine. 2021; 26(1):15.  https://doi. org/10.1186/s12199-021-00937-1  PMID:  33499804

 38. Aryal A, Harmon AC, Dugas TR. Particulate matter air pollutants and cardiovascular disease: Strategies for intervention. Pharmacol Ther. 2021; 223:107890. Epub 20210514.  https://doi.org/10.1016/j. pharmthera.2021.107890  PMID:  33992684 ; PubMed Central PMCID: PMC8216045.

 39. Bhatnagar A. Cardiovascular Effects of Particulate Air Pollution. Annu Rev Med. 2022; 73:393–406. Epub 20211013.  https://doi.org/10.1146/annurev-med-042220-011549  PMID:  34644154 ; PubMed Central PMCID: PM C 10132287.

 40. Kilinc E, Van Oerle R, Borissoff J, Oschatz C, Gerlofs-Nijland M, Janssen N, et al. Factor XII activation is essential to sustain the pro coagulant effects of particulate matter. Journal of Thrombosis and Haemostasis. 2011; 9(7):1359–67.  https://doi.org/10.1111/j.1538-7836.2011.04280.x  PMID:  21481175

 41. Calderon-Garc i due nas L, Villarreal-Calderon R, Valencia-Salazar G, Henriquez-Roldan C, Gutie´rrez- Castrello´n P, Torres-Jardon R, et al. Systemic inflammation, endo the li al dysfunction, and activation in clinically healthy children exposed to air pollutants. Inhalation toxicology. 2008; 20(5):499–506.  https:// doi.org/10.1080/08958370701864797  PMID:  18368620

 42. Sun Q, Wang A, Jin X, Natanzon A, Duquaine D, Brook RD, et al. Long-term air pollution exposure and acceleration of atherosclerosis and vascular inflammation in an animal model. Jama. 2005; 294 (23):3003–10.  https://doi.org/10.1001/jama.294.23.3003  PMID:  16414948

 43. Pearson JF, Bachireddy C, Shy am prasad S, Goldfine AB, Brownstein JS. Association Between Fine Particulate Matter and Diabetes Prevalence in the U.S. Diabetes Care. 2010; 33(10):2196–201.  https:// doi.org/10.2337/dc10-0698  PMID:  20628090

 44. Zhang Z, Guo C, Lau AK, Chan T-C, Chuang YC, Lin C, et al. Long-term exposure to fine particulate matter, blood pressure, and incident hypertension in Taiwanese adults. Environmental health perspectives. 2018; 126(1):017008.  https://doi.org/10.1289/EHP2466  PMID:  29351544

 45. Li J, Yao Y, Xie W, Wang B, Guan T, Han Y, et al. Association of long-term exposure to PM2. 5 with blood lipids in the Chinese population: findings from a longitudinal quasi-experiment. Environment international. 2021; 151:106454.  https://doi.org/10.1016/j.envint.2021.106454  PMID:  33676285  