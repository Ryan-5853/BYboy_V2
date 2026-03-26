> 抓取来源：https://dblp.org/pid/290/9342.html

[![Schloss Dagstuhl - Leibniz Center for Informatics](https://dblp.org/img/lzi-logo.82x57.png)](https://www.dagstuhl.de/en)

![](https://dblp.org/img/logo.320x120.png)

![search dblp](https://dblp.org/img/search.dark.16x16.png)

![search dblp](https://dblp.org/img/search.dark.16x16.png)

**default search action**

- combined dblp search
- author search
- venue search
- publication search

**Authors:**

- _no matches_

- ![waiting...](https://dblp.org/img/waiting.anim.gif)

**Venues:**

- _no matches_

- ![waiting...](https://dblp.org/img/waiting.anim.gif)

**Publications:**

- _no matches_

- ![waiting...](https://dblp.org/img/waiting.anim.gif)

![clear](https://dblp.org/img/clear-mark.medium.16x16.png)

[![ask others](https://dblp.org/img/search-external.dark.hollow.16x16.png)](https://google.com/search)

**ask others**

- [![](https://dblp.org/img/google.dark.16x16.png)Google](https://google.com/search)
- [![](https://dblp.org/img/google-scholar.dark.16x16.png)Google Scholar](https://scholar.google.com/scholar)
- [![](https://dblp.org/img/semscholar.dark.16x16.png)Semantic Scholar](https://www.semanticscholar.org/search)
- [![](https://dblp.org/img/internetarchive.dark.16x16.png)Internet Archive Scholar](https://scholar.archive.org/search)
- [![](https://dblp.org/img/citeseer.dark.16x16.png)CiteSeerX](https://citeseerx.ist.psu.edu/search_result?query=)
- [![](https://dblp.org/img/orcid.dark.16x16.png)ORCID](https://orcid.org/orcid-search/search)

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Ziyi+Cheng%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F290%2F9342%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Ziyi+Cheng+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F290%2F9342%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Ziyi+Cheng+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F290%2F9342%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Ziyi+Cheng%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F290%2F9342%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Ziyi+Cheng+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F290%2F9342%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Ziyi+Cheng%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F290%2F9342%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Ziyi+Cheng%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F290%2F9342%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F290%2F9342%3E+%7D+.%0A%0A%7D)

_showing all13 records_

2016202652021: 62021: 62023: 22023: 22024: 42025: 1

**refine by search term**

![](https://dblp.org/img/clear-mark.medium.16x16.png)![filter active](https://dblp.org/img/filter-mark.12x12.png)

**refine by type**

- [ ] Journal Articles(only)
- [ ] Conference and Workshop Papers(only)
- [ ] Informal and Other Publications(only)

- select all \| deselect all

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by coauthor**

- ![](https://dblp.org/img/add-mark.12x12.png)Felix Juefei-Xu (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Qing Guo 0005 (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Jianjun Zhao 0001 (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Lei Ma 0003 (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Wanli Xue (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Jundong Zhang (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Xuhong Ren (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Yang Liu 0003 (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Xiaofei Xie (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Kristian Simonato (1)

- _153 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (12)
- ![](https://dblp.org/img/add-mark.12x12.png)0009-0009-2897-1400 (1)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)ICCV (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)J. Big Data (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Access (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Reliab. Eng. Syst. Saf. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ISPRS Int. J. Geo Inf. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)PRCV (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Pattern Recognit. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ICAIIS (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ICME (1)

- _1 more option_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (8)
- ![](https://dblp.org/img/add-mark.12x12.png)open (5)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[j6\]
[Yu Guo](https://dblp.org/pid/53/382-12.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiangyu Li](https://dblp.org/pid/87/9032.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jundong Zhang](https://dblp.org/pid/66/7763.html)![](https://dblp.org/img/orcid-mark.12x12.png), Ziyi Cheng:

SDCGAN: A CycleGAN-based single-domain generalization method for mechanical fault diagnosis. [Reliab. Eng. Syst. Saf.258](https://dblp.org/db/journals/ress/ress258.html#journals/ress/GuoLZC25): 110854 (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j5\]
Ziyi Cheng![](https://dblp.org/img/orcid-mark.12x12.png):

EICNet: An End-to-End Efficient Learning-Based Image Compression Network. [IEEE Access12](https://dblp.org/db/journals/access/access12.html#journals/access/Cheng24a): 142668-142676 (2024)
- ![](https://dblp.org/img/n.png)

\[j4\]
[Yinkong Wei](https://dblp.org/pid/377/1797.html), [Mucong Wu](https://dblp.org/pid/377/1272.html), [Wei Wei](https://dblp.org/pid/24/4105.html), [Paulo R. F. Rocha](https://dblp.org/pid/28/9666.html), Ziyi Cheng, [Weifang Yao](https://dblp.org/pid/377/1218.html):

Research on Total Electric Field Prediction Method of Ultra-High Voltage Direct Current Transmission Line Based on Stacking Algorithm. [Comput. Syst. Sci. Eng.48(3)](https://dblp.org/db/journals/csse/csse48.html#journals/csse/WeiWWRCY24): 723-738 (2024)
- ![](https://dblp.org/img/n.png)

\[j3\]
[Jing Zhao](https://dblp.org/pid/69/5882.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Faziawati Abdul Aziz](https://dblp.org/pid/403/8228.html), Ziyi Cheng, [Norsidah Ujang](https://dblp.org/pid/403/8506.html), [Hui Zhang](https://dblp.org/pid/181/2846.html), [Jiajun Xu](https://dblp.org/pid/151/4980.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Xiao](https://dblp.org/pid/61/6921.html), [Lin Shi](https://dblp.org/pid/15/5412.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Post-Occupancy Evaluation of the Improved Old Residential Neighborhood Satisfaction Using Principal Component Analysis: The Case of Wuxi, China. [ISPRS Int. J. Geo Inf.13(9)](https://dblp.org/db/journals/ijgi/ijgi13.html#journals/ijgi/ZhaoACUZXXS24): 318 (2024)
- ![](https://dblp.org/img/n.png)

\[j2\]
[Yu Guo](https://dblp.org/pid/53/382.html), Ziyi Cheng, [Jundong Zhang](https://dblp.org/pid/66/7763.html), [Bin Sun](https://dblp.org/pid/01/5401.html), [YongKang Wang](https://dblp.org/pid/389/3287.html):

A review on adversarial-based deep transfer learning mechanical fault diagnosis. [J. Big Data11(1)](https://dblp.org/db/journals/jbd/jbd11.html#journals/jbd/GuoCZSW24): 151 (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j1\]
Ziyi Cheng, [Baoyuan Wu](https://dblp.org/pid/73/7781.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenya Zhang](https://dblp.org/pid/98/4896.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

TAT: Targeted backdoor attacks against visual object tracking. [Pattern Recognit.142](https://dblp.org/db/journals/pr/pr142.html#journals/pr/ChengWZZ23): 109629 (2023)
- ![](https://dblp.org/img/n.png)

\[c5\]
Ziyi Cheng, [Chen Chen](https://dblp.org/pid/65/4423-36.html), [Yichao Zhou](https://dblp.org/pid/146/9862.html), [Xiyuan Hu](https://dblp.org/pid/83/7614.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Mining Temporal Inconsistency with 3D Face Model for Deepfake Video Detection. [PRCV (7)2023](https://dblp.org/db/conf/prcv/prcv2023-7.html#conf/prcv/ChengCZH23): 231-243
- 2021
- ![](https://dblp.org/img/n.png)

\[c4\]
[Tianai Yue](https://dblp.org/pid/304/9450.html), Ziyi Cheng, [Runlin Liu](https://dblp.org/pid/304/9660.html), [Fengrong Han](https://dblp.org/pid/266/6897.html):

The Choice of Best Summer Job Based on Improved Fuzzy Comprehensive Evaluation. [ICAIIS2021](https://dblp.org/db/conf/icaiis/icaiis2021.html#conf/icaiis/YueCLH21): 300:1-300:5
- ![](https://dblp.org/img/n.png)

\[c3\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), Ziyi Cheng, [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

Learning to Adversarially Blur Visual Object Tracking. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/0005CJ0X0Z21): 10819-10828
- ![](https://dblp.org/img/n.png)

\[c2\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), Ziyi Cheng, [Yu-Chen Chiu](https://dblp.org/pid/199/2494.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Xingping Dong](https://dblp.org/pid/156/3020.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Bilge Günsel](https://dblp.org/pid/47/5125.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Wencheng Han](https://dblp.org/pid/280/3348.html), [Yanyan Huang](https://dblp.org/pid/88/4316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [J. Yin](https://dblp.org/pid/51/2242.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Jingen Liu](https://dblp.org/pid/10/5849.html), [Li Liu](https://dblp.org/pid/33/4528-36.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Jonathon Luiten](https://dblp.org/pid/211/7992.html), [Jie Ma](https://dblp.org/pid/62/5110.html), [Ziang Ma](https://dblp.org/pid/165/9621.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Yuzhen Niu](https://dblp.org/pid/28/7442.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Aravindh Rajiv](https://dblp.org/pid/307/9144.html), [Muhammad Rana](https://dblp.org/pid/276/0222.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Ling Shao](https://dblp.org/pid/75/1281.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furao Shen](https://dblp.org/pid/80/4685.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Paul Voigtlaender](https://dblp.org/pid/166/6430.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html), [Chenyan Wu](https://dblp.org/pid/76/1190.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang Xu](https://dblp.org/pid/126/2962.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Xiaohan Zhang](https://dblp.org/pid/96/6053.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Ming Zhen](https://dblp.org/pid/307/8430.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html):

The Ninth Visual Object Tracking VOT2021 Challenge Results. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/KristanMLFPKCDZ21): 2711-2738
- ![](https://dblp.org/img/n.png)

\[c1\]
Ziyi Cheng, [Xuhong Ren](https://dblp.org/pid/138/4258.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

Deepmix: Online Auto Data Augmentation for Robust Visual Object Tracking. [ICME2021](https://dblp.org/db/conf/icmcs/icme2021.html#conf/icmcs/ChengRJX00Z21): 1-6
- ![](https://dblp.org/img/n.png)

\[i2\]
Ziyi Cheng, [Xuhong Ren](https://dblp.org/pid/138/4258.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

DeepMix: Online Auto Data Augmentation for Robust Visual Object Tracking. [CoRRabs/2104.11585](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-11585) (2021)
- ![](https://dblp.org/img/n.png)

\[i1\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), Ziyi Cheng, [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

Learning to Adversarially Blur Visual Object Tracking. [CoRRabs/2107.12085](https://dblp.org/db/journals/corr/corr2107.html#journals/corr/abs-2107-12085) (2021)
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/290/9342.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[2](https://dblp.org/pid/290/9342.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Faziawati Abdul Aziz](https://dblp.org/pid/403/8228.html)

[\[j3\]](https://dblp.org/pid/290/9342.html#j3)

[3](https://dblp.org/pid/290/9342.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[4](https://dblp.org/pid/290/9342.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[5](https://dblp.org/pid/290/9342.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Llukman Cerkezi](https://dblp.org/pid/208/1312.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[6](https://dblp.org/pid/290/9342.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Hakan Çevikalp](https://dblp.org/pid/14/6210.html)

aka: Hakan Cevikalp

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[7](https://dblp.org/pid/290/9342.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[8](https://dblp.org/pid/290/9342.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Chen Chen 0036](https://dblp.org/pid/65/4423-36.html)

[\[c5\]](https://dblp.org/pid/290/9342.html#c5)

[9](https://dblp.org/pid/290/9342.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[10](https://dblp.org/pid/290/9342.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[11](https://dblp.org/pid/290/9342.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Miao Cheng](https://dblp.org/pid/79/7377.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[12](https://dblp.org/pid/290/9342.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yu-Chen Chiu](https://dblp.org/pid/199/2494.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[13](https://dblp.org/pid/290/9342.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Ozgun Cirakman](https://dblp.org/pid/86/8843.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[14](https://dblp.org/pid/290/9342.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[15](https://dblp.org/pid/290/9342.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Kenan Dai](https://dblp.org/pid/250/4445.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[16](https://dblp.org/pid/290/9342.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[17](https://dblp.org/pid/290/9342.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[18](https://dblp.org/pid/290/9342.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[19](https://dblp.org/pid/290/9342.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xingping Dong](https://dblp.org/pid/156/3020.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[20](https://dblp.org/pid/290/9342.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[21](https://dblp.org/pid/290/9342.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[22](https://dblp.org/pid/290/9342.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[23](https://dblp.org/pid/290/9342.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[24](https://dblp.org/pid/290/9342.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[25](https://dblp.org/pid/290/9342.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Zhiyong Feng 0001](https://dblp.org/pid/48/195-1.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[26](https://dblp.org/pid/290/9342.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[27](https://dblp.org/pid/290/9342.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[28](https://dblp.org/pid/290/9342.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Shiming Ge](https://dblp.org/pid/93/8104.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[29](https://dblp.org/pid/290/9342.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[30](https://dblp.org/pid/290/9342.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[31](https://dblp.org/pid/290/9342.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yuzhang Gu](https://dblp.org/pid/122/3790.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[32](https://dblp.org/pid/290/9342.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Bilge Günsel](https://dblp.org/pid/47/5125.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[33](https://dblp.org/pid/290/9342.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Qing Guo 0005](https://dblp.org/pid/25/3038-5.html)

[\[c3\]](https://dblp.org/pid/290/9342.html#c3) [\[c2\]](https://dblp.org/pid/290/9342.html#c2) [\[c1\]](https://dblp.org/pid/290/9342.html#c1) [\[i2\]](https://dblp.org/pid/290/9342.html#i2) [\[i1\]](https://dblp.org/pid/290/9342.html#i1)

[34](https://dblp.org/pid/290/9342.html?view=joint&param=34 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=2)

[Yu Guo](https://dblp.org/pid/53/382.html)

[\[j2\]](https://dblp.org/pid/290/9342.html#j2)

[35](https://dblp.org/pid/290/9342.html?view=joint&param=35 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=2)

[Yu Guo 0012](https://dblp.org/pid/53/382-12.html)

[\[j6\]](https://dblp.org/pid/290/9342.html#j6)

[36](https://dblp.org/pid/290/9342.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Filiz Gurkan](https://dblp.org/pid/202/7040.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[37](https://dblp.org/pid/290/9342.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Gustav Häger](https://dblp.org/pid/157/3602.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[38](https://dblp.org/pid/290/9342.html?view=joint&param=38 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=3)

[Fengrong Han](https://dblp.org/pid/266/6897.html)

[\[c4\]](https://dblp.org/pid/290/9342.html#c4)

[39](https://dblp.org/pid/290/9342.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Wencheng Han](https://dblp.org/pid/280/3348.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[40](https://dblp.org/pid/290/9342.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xiyuan Hu](https://dblp.org/pid/83/7614.html)

[\[c5\]](https://dblp.org/pid/290/9342.html#c5)

[41](https://dblp.org/pid/290/9342.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yanyan Huang](https://dblp.org/pid/88/4316.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[42](https://dblp.org/pid/290/9342.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[43](https://dblp.org/pid/290/9342.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[44](https://dblp.org/pid/290/9342.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[45](https://dblp.org/pid/290/9342.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[46](https://dblp.org/pid/290/9342.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html)

[\[c3\]](https://dblp.org/pid/290/9342.html#c3) [\[c2\]](https://dblp.org/pid/290/9342.html#c2) [\[c1\]](https://dblp.org/pid/290/9342.html#c1) [\[i2\]](https://dblp.org/pid/290/9342.html#i2) [\[i1\]](https://dblp.org/pid/290/9342.html#i1)

[47](https://dblp.org/pid/290/9342.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[48](https://dblp.org/pid/290/9342.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jani Käpylä](https://dblp.org/pid/244/2529.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[49](https://dblp.org/pid/290/9342.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xiao Ke](https://dblp.org/pid/78/9040.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[50](https://dblp.org/pid/290/9342.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[51](https://dblp.org/pid/290/9342.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Byeong Hak Kim](https://dblp.org/pid/214/8978.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[52](https://dblp.org/pid/290/9342.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[53](https://dblp.org/pid/290/9342.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[54](https://dblp.org/pid/290/9342.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[55](https://dblp.org/pid/290/9342.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[56](https://dblp.org/pid/290/9342.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jun Ha Lee](https://dblp.org/pid/260/2774.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[57](https://dblp.org/pid/290/9342.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[58](https://dblp.org/pid/290/9342.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[59](https://dblp.org/pid/290/9342.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[60](https://dblp.org/pid/290/9342.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jianhua Li](https://dblp.org/pid/93/3389.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[61](https://dblp.org/pid/290/9342.html?view=joint&param=61 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=2)

[Xiangyu Li](https://dblp.org/pid/87/9032.html)

[\[j6\]](https://dblp.org/pid/290/9342.html#j6)

[62](https://dblp.org/pid/290/9342.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[63](https://dblp.org/pid/290/9342.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yuezhou Li](https://dblp.org/pid/284/2562.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[64](https://dblp.org/pid/290/9342.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[65](https://dblp.org/pid/290/9342.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[66](https://dblp.org/pid/290/9342.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jingen Liu](https://dblp.org/pid/10/5849.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[67](https://dblp.org/pid/290/9342.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Li Liu 0036](https://dblp.org/pid/33/4528-36.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[68](https://dblp.org/pid/290/9342.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Qingjie Liu 0001](https://dblp.org/pid/72/10584.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[69](https://dblp.org/pid/290/9342.html?view=joint&param=69 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=3)

[Runlin Liu](https://dblp.org/pid/304/9660.html)

[\[c4\]](https://dblp.org/pid/290/9342.html#c4)

[70](https://dblp.org/pid/290/9342.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yang Liu 0003](https://dblp.org/pid/51/3710-3.html)

[\[c3\]](https://dblp.org/pid/290/9342.html#c3) [\[i1\]](https://dblp.org/pid/290/9342.html#i1)

[71](https://dblp.org/pid/290/9342.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[72](https://dblp.org/pid/290/9342.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Wei Lu](https://dblp.org/pid/98/6613.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[73](https://dblp.org/pid/290/9342.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jonathon Luiten](https://dblp.org/pid/211/7992.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[74](https://dblp.org/pid/290/9342.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[75](https://dblp.org/pid/290/9342.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[76](https://dblp.org/pid/290/9342.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Lei Ma 0003](https://dblp.org/pid/20/6534-3.html)

[\[c3\]](https://dblp.org/pid/290/9342.html#c3) [\[c1\]](https://dblp.org/pid/290/9342.html#c1) [\[i2\]](https://dblp.org/pid/290/9342.html#i2) [\[i1\]](https://dblp.org/pid/290/9342.html#i1)

[77](https://dblp.org/pid/290/9342.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Ziang Ma](https://dblp.org/pid/165/9621.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[78](https://dblp.org/pid/290/9342.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[79](https://dblp.org/pid/290/9342.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[80](https://dblp.org/pid/290/9342.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[81](https://dblp.org/pid/290/9342.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[82](https://dblp.org/pid/290/9342.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[83](https://dblp.org/pid/290/9342.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yuzhen Niu](https://dblp.org/pid/28/7442.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[84](https://dblp.org/pid/290/9342.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[85](https://dblp.org/pid/290/9342.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[86](https://dblp.org/pid/290/9342.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[87](https://dblp.org/pid/290/9342.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Shoumeng Qiu](https://dblp.org/pid/284/2537.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[88](https://dblp.org/pid/290/9342.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Aravindh Rajiv](https://dblp.org/pid/307/9144.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[89](https://dblp.org/pid/290/9342.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Muhammad Rana](https://dblp.org/pid/276/0222.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[90](https://dblp.org/pid/290/9342.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xuhong Ren](https://dblp.org/pid/138/4258.html)

[\[c1\]](https://dblp.org/pid/290/9342.html#c1) [\[i2\]](https://dblp.org/pid/290/9342.html#i2)

[91](https://dblp.org/pid/290/9342.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[92](https://dblp.org/pid/290/9342.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Paulo R. F. Rocha](https://dblp.org/pid/28/9666.html)

[\[j4\]](https://dblp.org/pid/290/9342.html#j4)

[93](https://dblp.org/pid/290/9342.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Hasan Saribas](https://dblp.org/pid/225/3263.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[94](https://dblp.org/pid/290/9342.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[95](https://dblp.org/pid/290/9342.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Mohamed S. Shehata](https://dblp.org/pid/33/2495.html)

aka: Mohamed Shehata 0001

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[96](https://dblp.org/pid/290/9342.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Furao Shen](https://dblp.org/pid/80/4685.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[97](https://dblp.org/pid/290/9342.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jianbing Shen](https://dblp.org/pid/38/5435.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[98](https://dblp.org/pid/290/9342.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Lin Shi](https://dblp.org/pid/15/5412.html)

[\[j3\]](https://dblp.org/pid/290/9342.html#j3)

[99](https://dblp.org/pid/290/9342.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[100](https://dblp.org/pid/290/9342.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[101](https://dblp.org/pid/290/9342.html?view=joint&param=101 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=2)

[Bin Sun](https://dblp.org/pid/01/5401.html)

[\[j2\]](https://dblp.org/pid/290/9342.html#j2)

[102](https://dblp.org/pid/290/9342.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[103](https://dblp.org/pid/290/9342.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[104](https://dblp.org/pid/290/9342.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[105](https://dblp.org/pid/290/9342.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[106](https://dblp.org/pid/290/9342.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Norsidah Ujang](https://dblp.org/pid/403/8506.html)

[\[j3\]](https://dblp.org/pid/290/9342.html#j3)

[107](https://dblp.org/pid/290/9342.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Bedirhan Uzun](https://dblp.org/pid/247/8937.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[108](https://dblp.org/pid/290/9342.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Paul Voigtlaender](https://dblp.org/pid/166/6430.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[109](https://dblp.org/pid/290/9342.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[110](https://dblp.org/pid/290/9342.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Guangting Wang](https://dblp.org/pid/227/7195.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[111](https://dblp.org/pid/290/9342.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[112](https://dblp.org/pid/290/9342.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[113](https://dblp.org/pid/290/9342.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[114](https://dblp.org/pid/290/9342.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Linyuan Wang](https://dblp.org/pid/138/5963.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[115](https://dblp.org/pid/290/9342.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[116](https://dblp.org/pid/290/9342.html?view=joint&param=116 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=2)

[YongKang Wang](https://dblp.org/pid/389/3287.html)

[\[j2\]](https://dblp.org/pid/290/9342.html#j2)

[117](https://dblp.org/pid/290/9342.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yunhong Wang 0001](https://dblp.org/pid/95/6251.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[118](https://dblp.org/pid/290/9342.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Wei Wei](https://dblp.org/pid/24/4105.html)

[\[j4\]](https://dblp.org/pid/290/9342.html#j4)

[119](https://dblp.org/pid/290/9342.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yinkong Wei](https://dblp.org/pid/377/1797.html)

[\[j4\]](https://dblp.org/pid/290/9342.html#j4)

[120](https://dblp.org/pid/290/9342.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Baoyuan Wu](https://dblp.org/pid/73/7781.html)

[\[j1\]](https://dblp.org/pid/290/9342.html#j1)

[121](https://dblp.org/pid/290/9342.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Chenyan Wu](https://dblp.org/pid/76/1190.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[122](https://dblp.org/pid/290/9342.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[123](https://dblp.org/pid/290/9342.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Mucong Wu](https://dblp.org/pid/377/1272.html)

[\[j4\]](https://dblp.org/pid/290/9342.html#j4)

[124](https://dblp.org/pid/290/9342.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[125](https://dblp.org/pid/290/9342.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yi Xiao](https://dblp.org/pid/61/6921.html)

[\[j3\]](https://dblp.org/pid/290/9342.html#j3)

[126](https://dblp.org/pid/290/9342.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[127](https://dblp.org/pid/290/9342.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xiaofei Xie](https://dblp.org/pid/127/0713.html)

[\[c3\]](https://dblp.org/pid/290/9342.html#c3) [\[i1\]](https://dblp.org/pid/290/9342.html#i1)

[128](https://dblp.org/pid/290/9342.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jiajun Xu](https://dblp.org/pid/151/4980.html)

[\[j3\]](https://dblp.org/pid/290/9342.html#j3)

[129](https://dblp.org/pid/290/9342.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[130](https://dblp.org/pid/290/9342.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xiang Xu](https://dblp.org/pid/126/2962.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[131](https://dblp.org/pid/290/9342.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2) [\[c1\]](https://dblp.org/pid/290/9342.html#c1) [\[i2\]](https://dblp.org/pid/290/9342.html#i2)

[132](https://dblp.org/pid/290/9342.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[133](https://dblp.org/pid/290/9342.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[134](https://dblp.org/pid/290/9342.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[135](https://dblp.org/pid/290/9342.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[136](https://dblp.org/pid/290/9342.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[137](https://dblp.org/pid/290/9342.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Weifang Yao](https://dblp.org/pid/377/1218.html)

[\[j4\]](https://dblp.org/pid/290/9342.html#j4)

[138](https://dblp.org/pid/290/9342.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yu Ye 0004](https://dblp.org/pid/129/0969-4.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[139](https://dblp.org/pid/290/9342.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[J. Yin](https://dblp.org/pid/51/2242.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[140](https://dblp.org/pid/290/9342.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jun Yin 0003](https://dblp.org/pid/58/5423-3.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[141](https://dblp.org/pid/290/9342.html?view=joint&param=141 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=3)

[Tianai Yue](https://dblp.org/pid/304/9450.html)

[\[c4\]](https://dblp.org/pid/290/9342.html#c4)

[142](https://dblp.org/pid/290/9342.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[143](https://dblp.org/pid/290/9342.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[144](https://dblp.org/pid/290/9342.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Haitao Zhang](https://dblp.org/pid/19/6669.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[145](https://dblp.org/pid/290/9342.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Hui Zhang](https://dblp.org/pid/181/2846.html)

[\[j3\]](https://dblp.org/pid/290/9342.html#j3)

[146](https://dblp.org/pid/290/9342.html?view=joint&param=146 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=2)

[Jundong Zhang](https://dblp.org/pid/66/7763.html)

[\[j6\]](https://dblp.org/pid/290/9342.html#j6) [\[j2\]](https://dblp.org/pid/290/9342.html#j2)

[147](https://dblp.org/pid/290/9342.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[148](https://dblp.org/pid/290/9342.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Kangkai Zhang](https://dblp.org/pid/260/2990.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[149](https://dblp.org/pid/290/9342.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xiaohan Zhang](https://dblp.org/pid/96/6053.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[150](https://dblp.org/pid/290/9342.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xiaolin Zhang](https://dblp.org/pid/99/2516.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[151](https://dblp.org/pid/290/9342.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xinyu Zhang 0020](https://dblp.org/pid/58/4582-20.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[152](https://dblp.org/pid/290/9342.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Zhenya Zhang](https://dblp.org/pid/98/4896.html)

[\[j1\]](https://dblp.org/pid/290/9342.html#j1)

[153](https://dblp.org/pid/290/9342.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[154](https://dblp.org/pid/290/9342.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[155](https://dblp.org/pid/290/9342.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jianjun Zhao 0001](https://dblp.org/pid/71/6948-1.html)

[\[j1\]](https://dblp.org/pid/290/9342.html#j1) [\[c3\]](https://dblp.org/pid/290/9342.html#c3) [\[c1\]](https://dblp.org/pid/290/9342.html#c1) [\[i2\]](https://dblp.org/pid/290/9342.html#i2) [\[i1\]](https://dblp.org/pid/290/9342.html#i1)

[156](https://dblp.org/pid/290/9342.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jing Zhao](https://dblp.org/pid/69/5882.html)

[\[j3\]](https://dblp.org/pid/290/9342.html#j3)

[157](https://dblp.org/pid/290/9342.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[158](https://dblp.org/pid/290/9342.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Ming Zhen](https://dblp.org/pid/307/8430.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[159](https://dblp.org/pid/290/9342.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[160](https://dblp.org/pid/290/9342.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Yichao Zhou](https://dblp.org/pid/146/9862.html)

[\[c5\]](https://dblp.org/pid/290/9342.html#c5)

[161](https://dblp.org/pid/290/9342.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

[162](https://dblp.org/pid/290/9342.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/290/9342.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c2\]](https://dblp.org/pid/290/9342.html#c2)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/290/9342.html#) [\[–\]](https://dblp.org/pid/290/9342.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/290/9342.html#) [\[–\]](https://dblp.org/pid/290/9342.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/290/9342.html#) [\[–\]](https://dblp.org/pid/290/9342.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/290/9342.html#) [\[–\]](https://dblp.org/pid/290/9342.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/290/9342.html#) [\[–\]](https://dblp.org/pid/290/9342.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)