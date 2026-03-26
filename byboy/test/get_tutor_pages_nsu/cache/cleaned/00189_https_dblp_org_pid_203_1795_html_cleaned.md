> 抓取来源：https://dblp.org/pid/203/1795.html

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

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Zhihong+Fu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F203%2F1795%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Zhihong+Fu+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F203%2F1795%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Zhihong+Fu+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F203%2F1795%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Zhihong+Fu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F203%2F1795%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Zhihong+Fu+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F203%2F1795%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Zhihong+Fu%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F203%2F1795%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Zhihong+Fu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F203%2F1795%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F203%2F1795%3E+%7D+.%0A%0A%7D)

_showing all25 records_

2016202652017: 12019: 62019: 62020: 22021: 32021: 32022: 62022: 62022: 62023: 42024: 22025: 1

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

- ![](https://dblp.org/img/add-mark.12x12.png)Zhengyu Xu (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Xian Liao (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Yunhong Wang 0001 (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Yao Wang (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Qingjie Liu 0001 (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Longhuan Liu (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Nengyi Fu (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Zehua Fu (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Haowen Wang (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Daniel K. Du (3)

- _253 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (17)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-5567-8893 (4)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-7593-9886 (4)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Sensors (9)
- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Geosci. Remote. Sens. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)ECCV (2)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Access (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)IJCAI (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Geosci. Remote. Sens. Lett. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)SmartGridComm (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Ind. Electron. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Instrum. Meas. (1)

- _3 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)open (17)
- ![](https://dblp.org/img/add-mark.12x12.png)closed (8)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[j17\]
[Kun Jiang](https://dblp.org/pid/03/4406.html)![](https://dblp.org/img/orcid-mark.12x12.png), Zhihong Fu![](https://dblp.org/img/orcid-mark.12x12.png):

Backward Signal Propagation: A Symmetry-Based Training Method for Neural Networks. [Algorithms18(10)](https://dblp.org/db/journals/algorithms/algorithms18.html#journals/algorithms/JiangF25): 594 (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j16\]
[Xizhe Zhang](https://dblp.org/pid/79/1033.html), [Ben Yu](https://dblp.org/pid/251/6353.html), [Longhuan Liu](https://dblp.org/pid/248/4753.html)![](https://dblp.org/img/orcid-mark.12x12.png), Zhihong Fu![](https://dblp.org/img/orcid-mark.12x12.png), [Jinshan Yu](https://dblp.org/pid/49/5055.html), [Xin Cheng](https://dblp.org/pid/96/4269.html):

Accumulative Imaging Method of Grounding Grid Topological Features Based on Combined Sources. [IEEE Access12](https://dblp.org/db/journals/access/access12.html#journals/access/ZhangYLFYC24): 60876-60882 (2024)
- ![](https://dblp.org/img/n.png)

\[j15\]
[Xian Liao](https://dblp.org/pid/164/0940.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhengyu Xu](https://dblp.org/pid/74/7387.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Liu](https://dblp.org/pid/49/3283-196.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xuquan Hu](https://dblp.org/pid/364/3667.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Zhou](https://dblp.org/pid/00/5012.html)![](https://dblp.org/img/orcid-mark.12x12.png), Zhihong Fu![](https://dblp.org/img/orcid-mark.12x12.png):

Influence of Parasitic Capacitance on Turn-Off Current and Its Optimization Method for Transient Electromagnetic System. [IEEE Trans. Instrum. Meas.73](https://dblp.org/db/journals/tim/tim73.html#journals/tim/LiaoXLHZF24): 1-11 (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j14\]
[Yuning Hu](https://dblp.org/pid/208/0834.html), [Wei Wang](https://dblp.org/pid/35/7092.html), [Wei Liu](https://dblp.org/pid/49/3283.html), [Zihan Chen](https://dblp.org/pid/139/3503.html), [Jie Zhou](https://dblp.org/pid/00/5012.html), Zhihong Fu:

A Portable Tunnel Electromagnetic Impulse Shock Source. [Sensors23(9)](https://dblp.org/db/journals/sensors/sensors23.html#journals/sensors/HuWLCZF23): 4213 (2023)
- ![](https://dblp.org/img/n.png)

\[j13\]
[Bo Li](https://dblp.org/pid/50/3402.html), [Yanping He](https://dblp.org/pid/99/1365.html), [Lei Wang](https://dblp.org/pid/181/2817.html), [Min Cao](https://dblp.org/pid/92/5343.html), Zhihong Fu, [Huiyuan Zhang](https://dblp.org/pid/34/9800.html):

Calibration Method of a Wideband AC Resistance Voltage Divider Based on an Equivalent Model. [Sensors23(16)](https://dblp.org/db/journals/sensors/sensors23.html#journals/sensors/LiHWCFZ23): 7181 (2023)
- ![](https://dblp.org/img/n.png)

\[j12\]
[Xian Liao](https://dblp.org/pid/164/0940.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhengyu Xu](https://dblp.org/pid/74/7387.html), [Wei Liu](https://dblp.org/pid/49/3283.html), [Heng-Ming Tai](https://dblp.org/pid/40/2487.html), [Jie Zhou](https://dblp.org/pid/00/5012.html), [Xiao Ma](https://dblp.org/pid/35/573.html), Zhihong Fu![](https://dblp.org/img/orcid-mark.12x12.png):

Electromagnetic Detection System with Magnetic Dipole Source for Near-Surface Detection. [Sensors23(24)](https://dblp.org/db/journals/sensors/sensors23.html#journals/sensors/LiaoXLTZMF23): 9771 (2023)
- ![](https://dblp.org/img/n.png)

\[j11\]
[Zhengyu Xu](https://dblp.org/pid/74/7387.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xian Liao](https://dblp.org/pid/164/0940.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Longhuan Liu](https://dblp.org/pid/248/4753.html), [Nengyi Fu](https://dblp.org/pid/238/4096.html), Zhihong Fu![](https://dblp.org/img/orcid-mark.12x12.png):

Research on Small-Loop Transient Electromagnetic Method Forward and Nonlinear Optimization Inversion Method. [IEEE Trans. Geosci. Remote. Sens.61](https://dblp.org/db/journals/tgrs/tgrs61.html#journals/tgrs/XuLLFF23): 1-13 (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j10\]
[Haowen Wang](https://dblp.org/pid/158/7000.html), [Jiangbo Huang](https://dblp.org/pid/153/1891.html), [Longhuan Liu](https://dblp.org/pid/248/4753.html), [Shanqiang Qin](https://dblp.org/pid/248/4817.html), Zhihong Fu:

A Novel Pulsed Eddy Current Criterion for Non-Ferromagnetic Metal Thickness Quantifications under Large Liftoff. [Sensors22(2)](https://dblp.org/db/journals/sensors/sensors22.html#journals/sensors/WangHLQF22): 614 (2022)
- ![](https://dblp.org/img/n.png)

\[j9\]
[Zhengyu Xu](https://dblp.org/pid/74/7387.html)![](https://dblp.org/img/orcid-mark.12x12.png), Zhihong Fu![](https://dblp.org/img/orcid-mark.12x12.png), [Nengyi Fu](https://dblp.org/pid/238/4096.html):

Firefly Algorithm for Transient Electromagnetic Inversion. [IEEE Trans. Geosci. Remote. Sens.60](https://dblp.org/db/journals/tgrs/tgrs60.html#journals/tgrs/XuFF22): 1-12 (2022)
- ![](https://dblp.org/img/n.png)

\[c6\]
[Wei Xu](https://dblp.org/pid/32/1213-17.html), Zhihong Fu, [Zhixing Chen](https://dblp.org/pid/62/3074.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Mingtao Fu](https://dblp.org/pid/254/1780.html), [Xijin Zhang](https://dblp.org/pid/242/9085.html), [Yuan Gao](https://dblp.org/pid/76/2452.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Min Zheng](https://dblp.org/pid/23/328.html):

HiFace: Hybrid Task Learning for Face Reconstruction from Single Image. [ECCV Workshops (5)2022](https://dblp.org/db/conf/eccv/eccv2022-w5.html#conf/eccv/XuFCDFZGDZ22): 382-391
- ![](https://dblp.org/img/n.png)

\[c5\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Wenyan Yang](https://dblp.org/pid/119/2426.html), [Dingding Cai](https://dblp.org/pid/198/1127.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Kang Ben](https://dblp.org/pid/340/0959.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Hong Chang](https://dblp.org/pid/02/2689-1.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Jiaye Chen](https://dblp.org/pid/116/2901.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xilin Chen](https://dblp.org/pid/c/XilinChen.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Xiuyi Chen](https://dblp.org/pid/218/7190.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu-Hsi Chen](https://dblp.org/pid/127/3933.html), [Zhixing Chen](https://dblp.org/pid/62/3074.html), [Yangming Cheng](https://dblp.org/pid/340/1285.html), [Angelo Ciaramella](https://dblp.org/pid/37/6845.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Benjamin Dzubur](https://dblp.org/pid/340/1520.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Debajyoti Dhar](https://dblp.org/pid/128/3182.html), [Shangzhe Di](https://dblp.org/pid/304/1344.html), [Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), Zhihong Fu, [Shang Gao](https://dblp.org/pid/28/435-12.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Eric Granger](https://dblp.org/pid/86/2306.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Q. H. Gu](https://dblp.org/pid/340/1209.html), [Himanshu Gupta](https://dblp.org/pid/330/0760-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianfeng He](https://dblp.org/pid/93/8352.html), [Keji He](https://dblp.org/pid/319/4518.html), [Yan Huang](https://dblp.org/pid/75/6434-8.html), [Deepak Jangid](https://dblp.org/pid/340/1460.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Ze Kang](https://dblp.org/pid/340/1063.html), [Madhu Kiran](https://dblp.org/pid/39/10281.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Simiao Lai](https://dblp.org/pid/282/1954.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Dongwook Lee](https://dblp.org/pid/25/6543.html), [Hyunjeong Lee](https://dblp.org/pid/00/3423.html), [Seohyung Lee](https://dblp.org/pid/210/4662.html), [Hui Li](https://dblp.org/pid/66/3387-37.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ming Li](https://dblp.org/pid/l/MingLi10.html), [Wangkai Li](https://dblp.org/pid/340/1456.html), [Xi Li](https://dblp.org/pid/46/2311-1.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Xiao Li](https://dblp.org/pid/66/2069.html), [Zhe Li](https://dblp.org/pid/11/751-8.html), [Liting Lin](https://dblp.org/pid/227/2204.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Si Liu](https://dblp.org/pid/60/7642.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html), [Bingpeng Ma](https://dblp.org/pid/62/1822.html), [Chao Ma](https://dblp.org/pid/79/1552-4.html), [Jie Ma](https://dblp.org/pid/62/5110.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yinchao Ma](https://dblp.org/pid/189/1326.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Payman Moallem](https://dblp.org/pid/63/5378.html), [Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html), [Siyang Pan](https://dblp.org/pid/250/5753.html), [ChangBeom Park](https://dblp.org/pid/340/0926.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Litu Rout](https://dblp.org/pid/206/6445.html), [Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Tianhui Song](https://dblp.org/pid/181/8738.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Chao Sun](https://dblp.org/pid/54/3957.html), [Jingna Sun](https://dblp.org/pid/255/0702.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Om Prakash Verma](https://dblp.org/pid/61/8145.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Qiang Wang](https://dblp.org/pid/64/5630-23.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Jinlin Wu](https://dblp.org/pid/123/7200.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Xu](https://dblp.org/pid/32/1213-17.html), [Yong Xu](https://dblp.org/pid/07/4630-7.html), [Yuanyou Xu](https://dblp.org/pid/248/7663.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zizheng Xun](https://dblp.org/pid/340/1441.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Dawei Yang](https://dblp.org/pid/22/1038.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Yichun Yang](https://dblp.org/pid/249/9678.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Botao Ye](https://dblp.org/pid/227/4610.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Qianjin Yu](https://dblp.org/pid/53/10179.html), [Weichen Yu](https://dblp.org/pid/325/1209.html), [Kang Ze](https://dblp.org/pid/340/1107.html), [Jiang Zhai](https://dblp.org/pid/291/9340.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhu Zhang](https://dblp.org/pid/292/0953.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Haixia Zheng](https://dblp.org/pid/119/1585.html), [Min Zheng](https://dblp.org/pid/23/328.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html):

The Tenth Visual Object Tracking VOT2022 Challenge Results. [ECCV Workshops (8)2022](https://dblp.org/db/conf/eccv/eccv2022-w8.html#conf/eccv/KristanLMFPKCDZLDBZZYYCMFBBCCCCCCCCCCC22): 431-460
- ![](https://dblp.org/img/n.png)

\[c4\]
Zhihong Fu, [Zehua Fu](https://dblp.org/pid/137/6488.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Wenrui Cai](https://dblp.org/pid/320/0398.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html):

SparseTT: Visual Tracking with Sparse Transformers. [IJCAI2022](https://dblp.org/db/conf/ijcai/ijcai2022.html#conf/ijcai/FuFLCW22): 905-912
- ![](https://dblp.org/img/n.png)

\[i2\]
Zhihong Fu, [Zehua Fu](https://dblp.org/pid/137/6488.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Wenrui Cai](https://dblp.org/pid/320/0398.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html):

SparseTT: Visual Tracking with Sparse Transformers. [CoRRabs/2205.03776](https://dblp.org/db/journals/corr/corr2205.html#journals/corr/abs-2205-03776) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[c3\]
Zhihong Fu, [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Zehua Fu](https://dblp.org/pid/137/6488.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html):

STMTrack: Template-Free Visual Tracking With Space-Time Memory Networks. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/FuLFW21): 13774-13783
- ![](https://dblp.org/img/n.png)

\[c2\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Yu-Chen Chiu](https://dblp.org/pid/199/2494.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Xingping Dong](https://dblp.org/pid/156/3020.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-1.html), Zhihong Fu, [Shiming Ge](https://dblp.org/pid/93/8104.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Bilge Günsel](https://dblp.org/pid/47/5125.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Wencheng Han](https://dblp.org/pid/280/3348.html), [Yanyan Huang](https://dblp.org/pid/88/4316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [J. Yin](https://dblp.org/pid/51/2242.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Jingen Liu](https://dblp.org/pid/10/5849.html), [Li Liu](https://dblp.org/pid/33/4528-36.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Jonathon Luiten](https://dblp.org/pid/211/7992.html), [Jie Ma](https://dblp.org/pid/62/5110.html), [Ziang Ma](https://dblp.org/pid/165/9621.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Yuzhen Niu](https://dblp.org/pid/28/7442.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Aravindh Rajiv](https://dblp.org/pid/307/9144.html), [Muhammad Rana](https://dblp.org/pid/276/0222.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Ling Shao](https://dblp.org/pid/75/1281.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furao Shen](https://dblp.org/pid/80/4685.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Paul Voigtlaender](https://dblp.org/pid/166/6430.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html), [Chenyan Wu](https://dblp.org/pid/76/1190.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang Xu](https://dblp.org/pid/126/2962.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Xiaohan Zhang](https://dblp.org/pid/96/6053.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Ming Zhen](https://dblp.org/pid/307/8430.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html):

The Ninth Visual Object Tracking VOT2021 Challenge Results. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/KristanMLFPKCDZ21): 2711-2738
- ![](https://dblp.org/img/n.png)

\[i1\]
Zhihong Fu, [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Zehua Fu](https://dblp.org/pid/137/6488.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html):

STMTrack: Template-free Visual Tracking with Space-time Memory Networks. [CoRRabs/2104.00324](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-00324) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[j8\]
[Zhengyu Xu](https://dblp.org/pid/74/7387.html)![](https://dblp.org/img/orcid-mark.12x12.png), Zhihong Fu![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Zhang](https://dblp.org/pid/05/3499.html):

Research and Application of the Transient Electromagnetic Method Inversion Technique Based on Particle Swarm Optimization Algorithm. [IEEE Access8](https://dblp.org/db/journals/access/access8.html#journals/access/XuFZ20): 198307-198316 (2020)
- ![](https://dblp.org/img/n.png)

\[j7\]
[Jiangbo Huang](https://dblp.org/pid/153/1891.html), [Haowen Wang](https://dblp.org/pid/158/7000.html), Zhihong Fu, [Wei Fu](https://dblp.org/pid/26/4472.html):

Analysis of Primary Field Shielding Stability for the Weak Coupling Coil Designs. [Sensors20(2)](https://dblp.org/db/journals/sensors/sensors20.html#journals/sensors/HuangWFF20): 519 (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j6\]
[Shanqiang Qin](https://dblp.org/pid/248/4817.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yao Wang](https://dblp.org/pid/72/628.html), [Zhengyu Xu](https://dblp.org/pid/74/7387.html), [Xian Liao](https://dblp.org/pid/164/0940.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Longhuan Liu](https://dblp.org/pid/248/4753.html), Zhihong Fu![](https://dblp.org/img/orcid-mark.12x12.png):

Fast Resistivity Imaging of Transient Electromagnetic Using ANN. [IEEE Geosci. Remote. Sens. Lett.16(9)](https://dblp.org/db/journals/lgrs/lgrs16.html#journals/lgrs/QinWXLLF19): 1373-1377 (2019)
- ![](https://dblp.org/img/n.png)

\[j5\]
[Yao Wang](https://dblp.org/pid/72/628.html), [Nengyi Fu](https://dblp.org/pid/238/4096.html), [Xinglin Lu](https://dblp.org/pid/234/5139.html), Zhihong Fu:

Application of a New Geophone and Geometry in Tunnel Seismic Detection. [Sensors19(5)](https://dblp.org/db/journals/sensors/sensors19.html#journals/sensors/WangFLF19): 1246 (2019)
- ![](https://dblp.org/img/n.png)

\[j4\]
[Xiujuan Wang](https://dblp.org/pid/85/5016.html), Zhihong Fu, [Yao Wang](https://dblp.org/pid/72/628.html), [Renkuan Liu](https://dblp.org/pid/242/5662.html), [Lin Chen](https://dblp.org/pid/13/3479.html):

A Non-Destructive Testing Method for Fault Detection of Substation Grounding Grids. [Sensors19(9)](https://dblp.org/db/journals/sensors/sensors19.html#journals/sensors/WangFWLC19): 2046 (2019)
- ![](https://dblp.org/img/n.png)

\[j3\]
[Jiangbo Huang](https://dblp.org/pid/153/1891.html), [Haowen Wang](https://dblp.org/pid/158/7000.html), Zhihong Fu, [Wei Fu](https://dblp.org/pid/26/4472.html):

Modeling and Solution of Signal Oscillation Mechanism of the Multi-Coil Sensor. [Sensors19(16)](https://dblp.org/db/journals/sensors/sensors19.html#journals/sensors/HuangWFF19): 3563 (2019)
- ![](https://dblp.org/img/n.png)

\[j2\]
[Yao Wang](https://dblp.org/pid/72/628.html), [Nengyi Fu](https://dblp.org/pid/238/4096.html), Zhihong Fu, [Xinglin Lu](https://dblp.org/pid/234/5139.html), [Xian Liao](https://dblp.org/pid/164/0940.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haowen Wang](https://dblp.org/pid/158/7000.html), [Shanqiang Qin](https://dblp.org/pid/248/4817.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Semi-Automatic Coupling Geophone for Tunnel Seismic Detection. [Sensors19(17)](https://dblp.org/db/journals/sensors/sensors19.html#journals/sensors/WangFFLLWQ19): 3734 (2019)
- ![](https://dblp.org/img/n.png)

\[c1\]
[Wenli Chen](https://dblp.org/pid/16/1207.html), [Kaitao Peng](https://dblp.org/pid/254/6141.html), [Chao Yang](https://dblp.org/pid/00/5867.html), [Yao Wang](https://dblp.org/pid/72/628.html), Zhihong Fu:

Traction substation power signal characteristics and transient power quality evaluation method. [SmartGridComm2019](https://dblp.org/db/conf/smartgridcomm/smartgridcomm2019.html#conf/smartgridcomm/ChenPYWF19): 1-7
- 2017
- ![](https://dblp.org/img/n.png)

\[j1\]
[Cigong Yu](https://dblp.org/pid/203/1605.html), Zhihong Fu, [Gaolin Wu](https://dblp.org/pid/143/0139.html), [Liuyuan Zhou](https://dblp.org/pid/203/1936.html), [Xuegui Zhu](https://dblp.org/pid/46/1439.html), [Minghui Bao](https://dblp.org/pid/203/1850.html):

Configuration Detection of Substation Grounding Grid Using Transient Electromagnetic Method. [IEEE Trans. Ind. Electron.64(8)](https://dblp.org/db/journals/tie/tie64.html#journals/tie/YuFWZZB17): 6475-6483 (2017)
- _no results_

automatic loading of the coauthor graph disabled due to its size.

**click here to**
**load the graph.**

Note that this feature is _work in progress_ and that it is still far from being perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/203/1795.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[2](https://dblp.org/pid/203/1795.html?view=joint&param=2 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=2)

[Minghui Bao](https://dblp.org/pid/203/1850.html)

[\[j1\]](https://dblp.org/pid/203/1795.html#j1)

[3](https://dblp.org/pid/203/1795.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Kang Ben](https://dblp.org/pid/340/0959.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[4](https://dblp.org/pid/203/1795.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[5](https://dblp.org/pid/203/1795.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Johanna Björklund](https://dblp.org/pid/75/5525.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[6](https://dblp.org/pid/203/1795.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Dingding Cai](https://dblp.org/pid/198/1127.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[7](https://dblp.org/pid/203/1795.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wenrui Cai](https://dblp.org/pid/320/0398.html)

[\[c4\]](https://dblp.org/pid/203/1795.html#c4) [\[i2\]](https://dblp.org/pid/203/1795.html#i2)

[8](https://dblp.org/pid/203/1795.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Min Cao](https://dblp.org/pid/92/5343.html)

[\[j13\]](https://dblp.org/pid/203/1795.html#j13)

[9](https://dblp.org/pid/203/1795.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[10](https://dblp.org/pid/203/1795.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Llukman Cerkezi](https://dblp.org/pid/208/1312.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[11](https://dblp.org/pid/203/1795.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Hakan Çevikalp](https://dblp.org/pid/14/6210.html)

aka: Hakan Cevikalp

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[12](https://dblp.org/pid/203/1795.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Hong Chang 0001](https://dblp.org/pid/02/2689-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[13](https://dblp.org/pid/203/1795.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[14](https://dblp.org/pid/203/1795.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Guangqi Chen](https://dblp.org/pid/178/8116.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[15](https://dblp.org/pid/203/1795.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jiaye Chen](https://dblp.org/pid/116/2901.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[16](https://dblp.org/pid/203/1795.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Lin Chen](https://dblp.org/pid/13/3479.html)

[\[j4\]](https://dblp.org/pid/203/1795.html#j4)

[17](https://dblp.org/pid/203/1795.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[18](https://dblp.org/pid/203/1795.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wenli Chen](https://dblp.org/pid/16/1207.html)

[\[c1\]](https://dblp.org/pid/203/1795.html#c1)

[19](https://dblp.org/pid/203/1795.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xilin Chen 0001](https://dblp.org/pid/c/XilinChen.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[20](https://dblp.org/pid/203/1795.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[21](https://dblp.org/pid/203/1795.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiuyi Chen](https://dblp.org/pid/218/7190.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[22](https://dblp.org/pid/203/1795.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yiwei Chen](https://dblp.org/pid/28/2965.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[23](https://dblp.org/pid/203/1795.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yu-Hsi Chen](https://dblp.org/pid/127/3933.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[24](https://dblp.org/pid/203/1795.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zhixing Chen](https://dblp.org/pid/62/3074.html)

[\[c6\]](https://dblp.org/pid/203/1795.html#c6) [\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[25](https://dblp.org/pid/203/1795.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zihan Chen](https://dblp.org/pid/139/3503.html)

[\[j14\]](https://dblp.org/pid/203/1795.html#j14)

[26](https://dblp.org/pid/203/1795.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Miao Cheng](https://dblp.org/pid/79/7377.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[27](https://dblp.org/pid/203/1795.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xin Cheng](https://dblp.org/pid/96/4269.html)

[\[j16\]](https://dblp.org/pid/203/1795.html#j16)

[28](https://dblp.org/pid/203/1795.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yangming Cheng](https://dblp.org/pid/340/1285.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[29](https://dblp.org/pid/203/1795.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Ziyi Cheng](https://dblp.org/pid/290/9342.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[30](https://dblp.org/pid/203/1795.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yu-Chen Chiu](https://dblp.org/pid/199/2494.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[31](https://dblp.org/pid/203/1795.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Angelo Ciaramella](https://dblp.org/pid/37/6845.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[32](https://dblp.org/pid/203/1795.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Ozgun Cirakman](https://dblp.org/pid/86/8843.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[33](https://dblp.org/pid/203/1795.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[34](https://dblp.org/pid/203/1795.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[35](https://dblp.org/pid/203/1795.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Kenan Dai](https://dblp.org/pid/250/4445.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[36](https://dblp.org/pid/203/1795.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[37](https://dblp.org/pid/203/1795.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[38](https://dblp.org/pid/203/1795.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c6\]](https://dblp.org/pid/203/1795.html#c6) [\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[39](https://dblp.org/pid/203/1795.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Debajyoti Dhar](https://dblp.org/pid/128/3182.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[40](https://dblp.org/pid/203/1795.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Shangzhe Di](https://dblp.org/pid/304/1344.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[41](https://dblp.org/pid/203/1795.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xingping Dong](https://dblp.org/pid/156/3020.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[42](https://dblp.org/pid/203/1795.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[43](https://dblp.org/pid/203/1795.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c6\]](https://dblp.org/pid/203/1795.html#c6) [\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[44](https://dblp.org/pid/203/1795.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[45](https://dblp.org/pid/203/1795.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Benjamin Dzubur](https://dblp.org/pid/340/1520.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[46](https://dblp.org/pid/203/1795.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Heng Fan 0001](https://dblp.org/pid/20/10120-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[47](https://dblp.org/pid/203/1795.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[48](https://dblp.org/pid/203/1795.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[49](https://dblp.org/pid/203/1795.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zhiyong Feng 0001](https://dblp.org/pid/48/195-1.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[50](https://dblp.org/pid/203/1795.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[51](https://dblp.org/pid/203/1795.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Mingtao Fu](https://dblp.org/pid/254/1780.html)

[\[c6\]](https://dblp.org/pid/203/1795.html#c6)

[52](https://dblp.org/pid/203/1795.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Nengyi Fu](https://dblp.org/pid/238/4096.html)

[\[j11\]](https://dblp.org/pid/203/1795.html#j11) [\[j9\]](https://dblp.org/pid/203/1795.html#j9) [\[j5\]](https://dblp.org/pid/203/1795.html#j5) [\[j2\]](https://dblp.org/pid/203/1795.html#j2)

[53](https://dblp.org/pid/203/1795.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wei Fu](https://dblp.org/pid/26/4472.html)

[\[j7\]](https://dblp.org/pid/203/1795.html#j7) [\[j3\]](https://dblp.org/pid/203/1795.html#j3)

[54](https://dblp.org/pid/203/1795.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zehua Fu](https://dblp.org/pid/137/6488.html)

[\[c4\]](https://dblp.org/pid/203/1795.html#c4) [\[i2\]](https://dblp.org/pid/203/1795.html#i2) [\[c3\]](https://dblp.org/pid/203/1795.html#c3) [\[i1\]](https://dblp.org/pid/203/1795.html#i1)

[55](https://dblp.org/pid/203/1795.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Shang Gao 0012](https://dblp.org/pid/28/435-12.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[56](https://dblp.org/pid/203/1795.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yuan Gao](https://dblp.org/pid/76/2452.html)

[\[c6\]](https://dblp.org/pid/203/1795.html#c6)

[57](https://dblp.org/pid/203/1795.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Shiming Ge](https://dblp.org/pid/93/8104.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[58](https://dblp.org/pid/203/1795.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[59](https://dblp.org/pid/203/1795.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[60](https://dblp.org/pid/203/1795.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Eric Granger](https://dblp.org/pid/86/2306.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[61](https://dblp.org/pid/203/1795.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Q. H. Gu](https://dblp.org/pid/340/1209.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[62](https://dblp.org/pid/203/1795.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yuzhang Gu](https://dblp.org/pid/122/3790.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[63](https://dblp.org/pid/203/1795.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Bilge Günsel](https://dblp.org/pid/47/5125.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[64](https://dblp.org/pid/203/1795.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Qing Guo 0005](https://dblp.org/pid/25/3038-5.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[65](https://dblp.org/pid/203/1795.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Himanshu Gupta 0003](https://dblp.org/pid/330/0760-3.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[66](https://dblp.org/pid/203/1795.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Filiz Gurkan](https://dblp.org/pid/202/7040.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[67](https://dblp.org/pid/203/1795.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Gustav Häger](https://dblp.org/pid/157/3602.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[68](https://dblp.org/pid/203/1795.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wencheng Han](https://dblp.org/pid/280/3348.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[69](https://dblp.org/pid/203/1795.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jianfeng He](https://dblp.org/pid/93/8352.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[70](https://dblp.org/pid/203/1795.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Keji He](https://dblp.org/pid/319/4518.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[71](https://dblp.org/pid/203/1795.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yanping He](https://dblp.org/pid/99/1365.html)

[\[j13\]](https://dblp.org/pid/203/1795.html#j13)

[72](https://dblp.org/pid/203/1795.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xuquan Hu](https://dblp.org/pid/364/3667.html)

[\[j15\]](https://dblp.org/pid/203/1795.html#j15)

[73](https://dblp.org/pid/203/1795.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yuning Hu](https://dblp.org/pid/208/0834.html)

[\[j14\]](https://dblp.org/pid/203/1795.html#j14)

[74](https://dblp.org/pid/203/1795.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jiangbo Huang](https://dblp.org/pid/153/1891.html)

[\[j10\]](https://dblp.org/pid/203/1795.html#j10) [\[j7\]](https://dblp.org/pid/203/1795.html#j7) [\[j3\]](https://dblp.org/pid/203/1795.html#j3)

[75](https://dblp.org/pid/203/1795.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yan Huang 0008](https://dblp.org/pid/75/6434-8.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[76](https://dblp.org/pid/203/1795.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yanyan Huang](https://dblp.org/pid/88/4316.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[77](https://dblp.org/pid/203/1795.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Deepak Jangid](https://dblp.org/pid/340/1460.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[78](https://dblp.org/pid/203/1795.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[79](https://dblp.org/pid/203/1795.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[80](https://dblp.org/pid/203/1795.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[81](https://dblp.org/pid/203/1795.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Kun Jiang](https://dblp.org/pid/03/4406.html)

[\[j17\]](https://dblp.org/pid/203/1795.html#j17)

[82](https://dblp.org/pid/203/1795.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[83](https://dblp.org/pid/203/1795.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[84](https://dblp.org/pid/203/1795.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[85](https://dblp.org/pid/203/1795.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Ze Kang](https://dblp.org/pid/340/1063.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[86](https://dblp.org/pid/203/1795.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jani Käpylä](https://dblp.org/pid/244/2529.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[87](https://dblp.org/pid/203/1795.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiao Ke](https://dblp.org/pid/78/9040.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[88](https://dblp.org/pid/203/1795.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[89](https://dblp.org/pid/203/1795.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Byeong Hak Kim](https://dblp.org/pid/214/8978.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[90](https://dblp.org/pid/203/1795.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Madhu Kiran](https://dblp.org/pid/39/10281.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[91](https://dblp.org/pid/203/1795.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[92](https://dblp.org/pid/203/1795.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[93](https://dblp.org/pid/203/1795.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Simiao Lai](https://dblp.org/pid/282/1954.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[94](https://dblp.org/pid/203/1795.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[95](https://dblp.org/pid/203/1795.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[96](https://dblp.org/pid/203/1795.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Dongwook Lee](https://dblp.org/pid/25/6543.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[97](https://dblp.org/pid/203/1795.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Hyunjeong Lee](https://dblp.org/pid/00/3423.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[98](https://dblp.org/pid/203/1795.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jun Ha Lee](https://dblp.org/pid/260/2774.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[99](https://dblp.org/pid/203/1795.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Seohyung Lee](https://dblp.org/pid/210/4662.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[100](https://dblp.org/pid/203/1795.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[101](https://dblp.org/pid/203/1795.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[102](https://dblp.org/pid/203/1795.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Bo Li](https://dblp.org/pid/50/3402.html)

[\[j13\]](https://dblp.org/pid/203/1795.html#j13)

[103](https://dblp.org/pid/203/1795.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[104](https://dblp.org/pid/203/1795.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jianhua Li](https://dblp.org/pid/93/3389.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[105](https://dblp.org/pid/203/1795.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Ming Li 0010](https://dblp.org/pid/l/MingLi10.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[106](https://dblp.org/pid/203/1795.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wangkai Li](https://dblp.org/pid/340/1456.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[107](https://dblp.org/pid/203/1795.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xi Li 0001](https://dblp.org/pid/46/2311-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[108](https://dblp.org/pid/203/1795.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[109](https://dblp.org/pid/203/1795.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiao Li](https://dblp.org/pid/66/2069.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[110](https://dblp.org/pid/203/1795.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yuezhou Li](https://dblp.org/pid/284/2562.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[111](https://dblp.org/pid/203/1795.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zhe Li 0008](https://dblp.org/pid/11/751-8.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[112](https://dblp.org/pid/203/1795.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xian Liao](https://dblp.org/pid/164/0940.html)

[\[j15\]](https://dblp.org/pid/203/1795.html#j15) [\[j12\]](https://dblp.org/pid/203/1795.html#j12) [\[j11\]](https://dblp.org/pid/203/1795.html#j11) [\[j6\]](https://dblp.org/pid/203/1795.html#j6) [\[j2\]](https://dblp.org/pid/203/1795.html#j2)

[113](https://dblp.org/pid/203/1795.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Liting Lin](https://dblp.org/pid/227/2204.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[114](https://dblp.org/pid/203/1795.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Haibin Ling](https://dblp.org/pid/93/3488.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[115](https://dblp.org/pid/203/1795.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[116](https://dblp.org/pid/203/1795.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[117](https://dblp.org/pid/203/1795.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jingen Liu](https://dblp.org/pid/10/5849.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[118](https://dblp.org/pid/203/1795.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Li Liu 0036](https://dblp.org/pid/33/4528-36.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[119](https://dblp.org/pid/203/1795.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Longhuan Liu](https://dblp.org/pid/248/4753.html)

[\[j16\]](https://dblp.org/pid/203/1795.html#j16) [\[j11\]](https://dblp.org/pid/203/1795.html#j11) [\[j10\]](https://dblp.org/pid/203/1795.html#j10) [\[j6\]](https://dblp.org/pid/203/1795.html#j6)

[120](https://dblp.org/pid/203/1795.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Qingjie Liu 0001](https://dblp.org/pid/72/10584.html)

[\[c4\]](https://dblp.org/pid/203/1795.html#c4) [\[i2\]](https://dblp.org/pid/203/1795.html#i2) [\[c3\]](https://dblp.org/pid/203/1795.html#c3) [\[c2\]](https://dblp.org/pid/203/1795.html#c2) [\[i1\]](https://dblp.org/pid/203/1795.html#i1)

[121](https://dblp.org/pid/203/1795.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Renkuan Liu](https://dblp.org/pid/242/5662.html)

[\[j4\]](https://dblp.org/pid/203/1795.html#j4)

[122](https://dblp.org/pid/203/1795.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Si Liu 0001](https://dblp.org/pid/60/7642.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[123](https://dblp.org/pid/203/1795.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wei Liu](https://dblp.org/pid/49/3283.html)

[\[j14\]](https://dblp.org/pid/203/1795.html#j14) [\[j12\]](https://dblp.org/pid/203/1795.html#j12)

[124](https://dblp.org/pid/203/1795.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wei Liu 0196](https://dblp.org/pid/49/3283-196.html)

[\[j15\]](https://dblp.org/pid/203/1795.html#j15)

[125](https://dblp.org/pid/203/1795.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[126](https://dblp.org/pid/203/1795.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wei Lu](https://dblp.org/pid/98/6613.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[127](https://dblp.org/pid/203/1795.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xinglin Lu](https://dblp.org/pid/234/5139.html)

[\[j5\]](https://dblp.org/pid/203/1795.html#j5) [\[j2\]](https://dblp.org/pid/203/1795.html#j2)

[128](https://dblp.org/pid/203/1795.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jonathon Luiten](https://dblp.org/pid/211/7992.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[129](https://dblp.org/pid/203/1795.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[130](https://dblp.org/pid/203/1795.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Bingpeng Ma](https://dblp.org/pid/62/1822.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[131](https://dblp.org/pid/203/1795.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Chao Ma 0004](https://dblp.org/pid/79/1552-4.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[132](https://dblp.org/pid/203/1795.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[133](https://dblp.org/pid/203/1795.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiao Ma](https://dblp.org/pid/35/573.html)

[\[j12\]](https://dblp.org/pid/203/1795.html#j12)

[134](https://dblp.org/pid/203/1795.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yinchao Ma](https://dblp.org/pid/189/1326.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[135](https://dblp.org/pid/203/1795.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Ziang Ma](https://dblp.org/pid/165/9621.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[136](https://dblp.org/pid/203/1795.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[137](https://dblp.org/pid/203/1795.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[138](https://dblp.org/pid/203/1795.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[139](https://dblp.org/pid/203/1795.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[140](https://dblp.org/pid/203/1795.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[141](https://dblp.org/pid/203/1795.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Payman Moallem](https://dblp.org/pid/63/5378.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[142](https://dblp.org/pid/203/1795.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[143](https://dblp.org/pid/203/1795.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[144](https://dblp.org/pid/203/1795.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yuzhen Niu](https://dblp.org/pid/28/7442.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[145](https://dblp.org/pid/203/1795.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Siyang Pan](https://dblp.org/pid/250/5753.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[146](https://dblp.org/pid/203/1795.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[ChangBeom Park](https://dblp.org/pid/340/0926.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[147](https://dblp.org/pid/203/1795.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[148](https://dblp.org/pid/203/1795.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Matthieu Paul](https://dblp.org/pid/255/6113.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[149](https://dblp.org/pid/203/1795.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[150](https://dblp.org/pid/203/1795.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Kaitao Peng](https://dblp.org/pid/254/6141.html)

[\[c1\]](https://dblp.org/pid/203/1795.html#c1)

[151](https://dblp.org/pid/203/1795.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[152](https://dblp.org/pid/203/1795.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Shanqiang Qin](https://dblp.org/pid/248/4817.html)

[\[j10\]](https://dblp.org/pid/203/1795.html#j10) [\[j6\]](https://dblp.org/pid/203/1795.html#j6) [\[j2\]](https://dblp.org/pid/203/1795.html#j2)

[153](https://dblp.org/pid/203/1795.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Shoumeng Qiu](https://dblp.org/pid/284/2537.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[154](https://dblp.org/pid/203/1795.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Aravindh Rajiv](https://dblp.org/pid/307/9144.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[155](https://dblp.org/pid/203/1795.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Muhammad Rana](https://dblp.org/pid/276/0222.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[156](https://dblp.org/pid/203/1795.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[157](https://dblp.org/pid/203/1795.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Litu Rout](https://dblp.org/pid/206/6445.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[158](https://dblp.org/pid/203/1795.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Hasan Saribas](https://dblp.org/pid/225/3263.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[159](https://dblp.org/pid/203/1795.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[160](https://dblp.org/pid/203/1795.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[161](https://dblp.org/pid/203/1795.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Mohamed S. Shehata](https://dblp.org/pid/33/2495.html)

aka: Mohamed Shehata 0001

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[162](https://dblp.org/pid/203/1795.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Furao Shen](https://dblp.org/pid/80/4685.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[163](https://dblp.org/pid/203/1795.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jianbing Shen](https://dblp.org/pid/38/5435.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[164](https://dblp.org/pid/203/1795.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[165](https://dblp.org/pid/203/1795.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Tianhui Song](https://dblp.org/pid/181/8738.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[166](https://dblp.org/pid/203/1795.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[167](https://dblp.org/pid/203/1795.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Chao Sun](https://dblp.org/pid/54/3957.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[168](https://dblp.org/pid/203/1795.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jingna Sun](https://dblp.org/pid/255/0702.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[169](https://dblp.org/pid/203/1795.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Heng-Ming Tai](https://dblp.org/pid/40/2487.html)

[\[j12\]](https://dblp.org/pid/203/1795.html#j12)

[170](https://dblp.org/pid/203/1795.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[171](https://dblp.org/pid/203/1795.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[172](https://dblp.org/pid/203/1795.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[173](https://dblp.org/pid/203/1795.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[174](https://dblp.org/pid/203/1795.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Bedirhan Uzun](https://dblp.org/pid/247/8937.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[175](https://dblp.org/pid/203/1795.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Om Prakash Verma](https://dblp.org/pid/61/8145.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[176](https://dblp.org/pid/203/1795.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Paul Voigtlaender](https://dblp.org/pid/166/6430.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[177](https://dblp.org/pid/203/1795.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[178](https://dblp.org/pid/203/1795.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Fei Wang 0032](https://dblp.org/pid/52/3194-32.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[179](https://dblp.org/pid/203/1795.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Guangting Wang](https://dblp.org/pid/227/7195.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[180](https://dblp.org/pid/203/1795.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Haowen Wang](https://dblp.org/pid/158/7000.html)

[\[j10\]](https://dblp.org/pid/203/1795.html#j10) [\[j7\]](https://dblp.org/pid/203/1795.html#j7) [\[j3\]](https://dblp.org/pid/203/1795.html#j3) [\[j2\]](https://dblp.org/pid/203/1795.html#j2)

[181](https://dblp.org/pid/203/1795.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Lei Wang](https://dblp.org/pid/181/2817.html)

[\[j13\]](https://dblp.org/pid/203/1795.html#j13)

[182](https://dblp.org/pid/203/1795.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Liang Wang 0001](https://dblp.org/pid/56/4499-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[183](https://dblp.org/pid/203/1795.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[184](https://dblp.org/pid/203/1795.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[185](https://dblp.org/pid/203/1795.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[186](https://dblp.org/pid/203/1795.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Linyuan Wang](https://dblp.org/pid/138/5963.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[187](https://dblp.org/pid/203/1795.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Qiang Wang 0023](https://dblp.org/pid/64/5630-23.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[188](https://dblp.org/pid/203/1795.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wei Wang](https://dblp.org/pid/35/7092.html)

[\[j14\]](https://dblp.org/pid/203/1795.html#j14)

[189](https://dblp.org/pid/203/1795.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiujuan Wang](https://dblp.org/pid/85/5016.html)

[\[j4\]](https://dblp.org/pid/203/1795.html#j4)

[190](https://dblp.org/pid/203/1795.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yao Wang](https://dblp.org/pid/72/628.html)

[\[j6\]](https://dblp.org/pid/203/1795.html#j6) [\[j5\]](https://dblp.org/pid/203/1795.html#j5) [\[j4\]](https://dblp.org/pid/203/1795.html#j4) [\[j2\]](https://dblp.org/pid/203/1795.html#j2) [\[c1\]](https://dblp.org/pid/203/1795.html#c1)

[191](https://dblp.org/pid/203/1795.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[192](https://dblp.org/pid/203/1795.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yunhong Wang 0001](https://dblp.org/pid/95/6251.html)

[\[c4\]](https://dblp.org/pid/203/1795.html#c4) [\[i2\]](https://dblp.org/pid/203/1795.html#i2) [\[c3\]](https://dblp.org/pid/203/1795.html#c3) [\[c2\]](https://dblp.org/pid/203/1795.html#c2) [\[i1\]](https://dblp.org/pid/203/1795.html#i1)

[193](https://dblp.org/pid/203/1795.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Chenyan Wu](https://dblp.org/pid/76/1190.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[194](https://dblp.org/pid/203/1795.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[195](https://dblp.org/pid/203/1795.html?view=joint&param=195 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=2)

[Gaolin Wu](https://dblp.org/pid/143/0139.html)

[\[j1\]](https://dblp.org/pid/203/1795.html#j1)

[196](https://dblp.org/pid/203/1795.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jinlin Wu](https://dblp.org/pid/123/7200.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[197](https://dblp.org/pid/203/1795.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[198](https://dblp.org/pid/203/1795.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[199](https://dblp.org/pid/203/1795.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[200](https://dblp.org/pid/203/1795.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wei Xu 0017](https://dblp.org/pid/32/1213-17.html)

[\[c6\]](https://dblp.org/pid/203/1795.html#c6) [\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[201](https://dblp.org/pid/203/1795.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiang Xu](https://dblp.org/pid/126/2962.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[202](https://dblp.org/pid/203/1795.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yong Xu 0007](https://dblp.org/pid/07/4630-7.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[203](https://dblp.org/pid/203/1795.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yuanyou Xu](https://dblp.org/pid/248/7663.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[204](https://dblp.org/pid/203/1795.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zhengyu Xu](https://dblp.org/pid/74/7387.html)

[\[j15\]](https://dblp.org/pid/203/1795.html#j15) [\[j12\]](https://dblp.org/pid/203/1795.html#j12) [\[j11\]](https://dblp.org/pid/203/1795.html#j11) [\[j9\]](https://dblp.org/pid/203/1795.html#j9) [\[j8\]](https://dblp.org/pid/203/1795.html#j8) [\[j6\]](https://dblp.org/pid/203/1795.html#j6)

[205](https://dblp.org/pid/203/1795.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[206](https://dblp.org/pid/203/1795.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zizheng Xun](https://dblp.org/pid/340/1441.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[207](https://dblp.org/pid/203/1795.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[208](https://dblp.org/pid/203/1795.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[209](https://dblp.org/pid/203/1795.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Chao Yang](https://dblp.org/pid/00/5867.html)

[\[c1\]](https://dblp.org/pid/203/1795.html#c1)

[210](https://dblp.org/pid/203/1795.html?view=joint&param=210 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Dawei Yang](https://dblp.org/pid/22/1038.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[211](https://dblp.org/pid/203/1795.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[212](https://dblp.org/pid/203/1795.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[213](https://dblp.org/pid/203/1795.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wenyan Yang](https://dblp.org/pid/119/2426.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[214](https://dblp.org/pid/203/1795.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[215](https://dblp.org/pid/203/1795.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yi Yang 0001](https://dblp.org/pid/33/4854-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[216](https://dblp.org/pid/203/1795.html?view=joint&param=216 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yichun Yang](https://dblp.org/pid/249/9678.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[217](https://dblp.org/pid/203/1795.html?view=joint&param=217 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zongxin Yang](https://dblp.org/pid/249/5456.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[218](https://dblp.org/pid/203/1795.html?view=joint&param=218 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Botao Ye](https://dblp.org/pid/227/4610.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[219](https://dblp.org/pid/203/1795.html?view=joint&param=219 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yu Ye 0004](https://dblp.org/pid/129/0969-4.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[220](https://dblp.org/pid/203/1795.html?view=joint&param=220 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[J. Yin](https://dblp.org/pid/51/2242.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[221](https://dblp.org/pid/203/1795.html?view=joint&param=221 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jun Yin 0003](https://dblp.org/pid/58/5423-3.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[222](https://dblp.org/pid/203/1795.html?view=joint&param=222 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Ben Yu](https://dblp.org/pid/251/6353.html)

[\[j16\]](https://dblp.org/pid/203/1795.html#j16)

[223](https://dblp.org/pid/203/1795.html?view=joint&param=223 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=2)

[Cigong Yu](https://dblp.org/pid/203/1605.html)

[\[j1\]](https://dblp.org/pid/203/1795.html#j1)

[224](https://dblp.org/pid/203/1795.html?view=joint&param=224 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Fisher Yu 0001](https://dblp.org/pid/117/6314.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[225](https://dblp.org/pid/203/1795.html?view=joint&param=225 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Hongyuan Yu](https://dblp.org/pid/232/2265.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[226](https://dblp.org/pid/203/1795.html?view=joint&param=226 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jiaqian Yu](https://dblp.org/pid/164/7325.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[227](https://dblp.org/pid/203/1795.html?view=joint&param=227 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jinshan Yu](https://dblp.org/pid/49/5055.html)

[\[j16\]](https://dblp.org/pid/203/1795.html#j16)

[228](https://dblp.org/pid/203/1795.html?view=joint&param=228 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Qianjin Yu](https://dblp.org/pid/53/10179.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[229](https://dblp.org/pid/203/1795.html?view=joint&param=229 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Weichen Yu](https://dblp.org/pid/325/1209.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[230](https://dblp.org/pid/203/1795.html?view=joint&param=230 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Kang Ze](https://dblp.org/pid/340/1107.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[231](https://dblp.org/pid/203/1795.html?view=joint&param=231 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jiang Zhai](https://dblp.org/pid/291/9340.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[232](https://dblp.org/pid/203/1795.html?view=joint&param=232 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[233](https://dblp.org/pid/203/1795.html?view=joint&param=233 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Chunhu Zhang](https://dblp.org/pid/292/0953.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[234](https://dblp.org/pid/203/1795.html?view=joint&param=234 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[235](https://dblp.org/pid/203/1795.html?view=joint&param=235 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Haitao Zhang](https://dblp.org/pid/19/6669.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[236](https://dblp.org/pid/203/1795.html?view=joint&param=236 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Huiyuan Zhang](https://dblp.org/pid/34/9800.html)

[\[j13\]](https://dblp.org/pid/203/1795.html#j13)

[237](https://dblp.org/pid/203/1795.html?view=joint&param=237 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jing Zhang](https://dblp.org/pid/05/3499.html)

[\[j8\]](https://dblp.org/pid/203/1795.html#j8)

[238](https://dblp.org/pid/203/1795.html?view=joint&param=238 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[239](https://dblp.org/pid/203/1795.html?view=joint&param=239 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Kangkai Zhang](https://dblp.org/pid/260/2990.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[240](https://dblp.org/pid/203/1795.html?view=joint&param=240 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Tianzhu Zhang 0001](https://dblp.org/pid/15/7643-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[241](https://dblp.org/pid/203/1795.html?view=joint&param=241 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Wenkang Zhang](https://dblp.org/pid/340/0966.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[242](https://dblp.org/pid/203/1795.html?view=joint&param=242 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiaohan Zhang](https://dblp.org/pid/96/6053.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[243](https://dblp.org/pid/203/1795.html?view=joint&param=243 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xiaolin Zhang](https://dblp.org/pid/99/2516.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[244](https://dblp.org/pid/203/1795.html?view=joint&param=244 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xijin Zhang](https://dblp.org/pid/242/9085.html)

[\[c6\]](https://dblp.org/pid/203/1795.html#c6)

[245](https://dblp.org/pid/203/1795.html?view=joint&param=245 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xinyu Zhang 0020](https://dblp.org/pid/58/4582-20.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[246](https://dblp.org/pid/203/1795.html?view=joint&param=246 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xizhe Zhang](https://dblp.org/pid/79/1033.html)

[\[j16\]](https://dblp.org/pid/203/1795.html#j16)

[247](https://dblp.org/pid/203/1795.html?view=joint&param=247 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yushan Zhang](https://dblp.org/pid/50/10702.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[248](https://dblp.org/pid/203/1795.html?view=joint&param=248 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[249](https://dblp.org/pid/203/1795.html?view=joint&param=249 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zhipeng Zhang](https://dblp.org/pid/49/4941.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[250](https://dblp.org/pid/203/1795.html?view=joint&param=250 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[251](https://dblp.org/pid/203/1795.html?view=joint&param=251 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jie Zhao 0014](https://dblp.org/pid/23/3168-14.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[252](https://dblp.org/pid/203/1795.html?view=joint&param=252 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[253](https://dblp.org/pid/203/1795.html?view=joint&param=253 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Ming Zhen](https://dblp.org/pid/307/8430.html)

[\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[254](https://dblp.org/pid/203/1795.html?view=joint&param=254 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Feng Zheng 0001](https://dblp.org/pid/39/800-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[255](https://dblp.org/pid/203/1795.html?view=joint&param=255 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Haixia Zheng](https://dblp.org/pid/119/1585.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[256](https://dblp.org/pid/203/1795.html?view=joint&param=256 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Min Zheng](https://dblp.org/pid/23/328.html)

[\[c6\]](https://dblp.org/pid/203/1795.html#c6) [\[c5\]](https://dblp.org/pid/203/1795.html#c5)

[257](https://dblp.org/pid/203/1795.html?view=joint&param=257 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[258](https://dblp.org/pid/203/1795.html?view=joint&param=258 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jie Zhou](https://dblp.org/pid/00/5012.html)

[\[j15\]](https://dblp.org/pid/203/1795.html#j15) [\[j14\]](https://dblp.org/pid/203/1795.html#j14) [\[j12\]](https://dblp.org/pid/203/1795.html#j12)

[259](https://dblp.org/pid/203/1795.html?view=joint&param=259 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=2)

[Liuyuan Zhou](https://dblp.org/pid/203/1936.html)

[\[j1\]](https://dblp.org/pid/203/1795.html#j1)

[260](https://dblp.org/pid/203/1795.html?view=joint&param=260 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[261](https://dblp.org/pid/203/1795.html?view=joint&param=261 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5) [\[c2\]](https://dblp.org/pid/203/1795.html#c2)

[262](https://dblp.org/pid/203/1795.html?view=joint&param=262 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=2)

[Xuegui Zhu](https://dblp.org/pid/46/1439.html)

[\[j1\]](https://dblp.org/pid/203/1795.html#j1)

[263](https://dblp.org/pid/203/1795.html?view=joint&param=263 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/203/1795.html?view=group&param=1)

[Yueting Zhuang](https://dblp.org/pid/218/7793.html)

[\[c5\]](https://dblp.org/pid/203/1795.html#c5)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/203/1795.html#) [\[–\]](https://dblp.org/pid/203/1795.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/203/1795.html#) [\[–\]](https://dblp.org/pid/203/1795.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/203/1795.html#) [\[–\]](https://dblp.org/pid/203/1795.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/203/1795.html#) [\[–\]](https://dblp.org/pid/203/1795.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/203/1795.html#) [\[–\]](https://dblp.org/pid/203/1795.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)