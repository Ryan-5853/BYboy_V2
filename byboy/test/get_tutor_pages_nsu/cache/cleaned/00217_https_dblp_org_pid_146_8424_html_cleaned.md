> 抓取来源：https://dblp.org/pid/146/8424.html

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

This is just a _disambiguation page_, and is not intended to be the bibliography of an actual person. Any publication listed on this page has not been assigned to an actual author yet. If you know the true author of one of the publications listed below, you are welcome to [contact us.](https://dblp.org/db/about/team.html)

- [Wei-Li Guo](https://dblp.org/pid/174/0321.html)

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Weili+Guo%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F146%2F8424%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Weili+Guo+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F146%2F8424%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Weili+Guo+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F146%2F8424%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Weili+Guo%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F146%2F8424%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Weili+Guo+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F146%2F8424%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Weili+Guo%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F146%2F8424%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Weili+Guo%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F146%2F8424%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F146%2F8424%3E+%7D+.%0A%0A%7D)

_showing all35 records_

2014202552014: 22015: 22016: 12017: 22017: 22018: 52019: 12020: 22020: 22021: 22022: 22023: 72023: 72023: 72024: 62024: 62024: 62025: 32025: 3

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

- ![](https://dblp.org/img/add-mark.12x12.png)Haikun Wei (11)
- ![](https://dblp.org/img/add-mark.12x12.png)Kan-Jian Zhang (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Junsheng Zhao (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Jianfeng Lu 0003 (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Yang Yang 0128 (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Guangyu Li (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Xiangyu Wu (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Jinxia Zhang (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Yang Yang 0074 (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Hailiang Zhang (3)

- _95 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (25)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-5695-8109 (4)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0003-4459-9978 (4)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0001-9759-7074 (2)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Neurocomputing (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Graphs Comb. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Cybern. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Access (2)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Ind. Electron. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)ICDM (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Frontiers Comput. Sci. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IScIDE (1)

- _17 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (23)
- ![](https://dblp.org/img/add-mark.12x12.png)open (12)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[j22\]
[Zhenghang Zhang](https://dblp.org/pid/292/3255.html), [Guifu Su](https://dblp.org/pid/117/7143.html), [Xiaowen Qin](https://dblp.org/pid/411/6694.html), [Junfeng Du](https://dblp.org/pid/163/1331.html), Weili Guo, [Yue Wu](https://dblp.org/pid/41/5979.html):

Several graph properties in terms of the multiplicative version of the first Zagreb index. [Discret. Appl. Math.377](https://dblp.org/db/journals/dam/dam377.html#journals/dam/ZhangSQDGW25): 183-194 (2025)
- ![](https://dblp.org/img/n.png)

\[j21\]
Weili Guo![](https://dblp.org/img/orcid-mark.12x12.png), [Guochun Xiao](https://dblp.org/pid/133/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Laili Wang](https://dblp.org/pid/159/5465.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Noncontact Power Module Current Measurement Based on Bonding Wire Current Sensing Using Hybrid Sensor. [IEEE Trans. Ind. Electron.72(8)](https://dblp.org/db/journals/tie/tie72.html#journals/tie/GuoXW25): 8602-8611 (2025)
- ![](https://dblp.org/img/n.png)

\[c10\]
[Mingxu Feng](https://dblp.org/pid/382/8409.html), [Dian Chao](https://dblp.org/pid/372/7224.html), [Yuxuan Zhang](https://dblp.org/pid/126/5240.html), [Yang Yang](https://dblp.org/pid/48/450-128.html), Weili Guo:

Prompt Learning with Text-Augmented Cues for Out-of-Distribution Detection. [ICDM2025](https://dblp.org/db/conf/icdm/icdm2025.html#conf/icdm/FengCZYG25): 1204-1213
- 2024
- ![](https://dblp.org/img/n.png)

\[j20\]
[Zhaoting Ju](https://dblp.org/pid/373/8110.html), [Guangfeng Jiang](https://dblp.org/pid/200/2732.html), Weili Guo:

Freeness of Signed Graphic Arrangements. [Axioms13(3)](https://dblp.org/db/journals/axioms/axioms13.html#journals/axioms/JuJG24): 208 (2024)
- ![](https://dblp.org/img/n.png)

\[j19\]
Weili Guo![](https://dblp.org/img/orcid-mark.12x12.png), [Guochun Xiao](https://dblp.org/pid/133/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Laili Wang](https://dblp.org/pid/159/5465.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Compact Magnetoresistance-Rogowski Hybrid Sensor for Multichip Online Current Sensing in Press-Pack Power Module. [IEEE Trans. Ind. Electron.71(9)](https://dblp.org/db/journals/tie/tie71.html#journals/tie/GuoXW24): 11529-11539 (2024)
- ![](https://dblp.org/img/n.png)

\[c9\]
[Longfei Huang](https://dblp.org/pid/216/8320.html), [Xiangyu Wu](https://dblp.org/pid/17/343.html), [Jingyuan Wang](https://dblp.org/pid/75/5135.html), Weili Guo, [Yang Yang](https://dblp.org/pid/48/450-74.html):

Refining Visual Perception for Decoration Display: A Self-Enhanced Deep Captioning Model. [ACML2024](https://dblp.org/db/conf/acml/acml2024.html#conf/acml/HuangWWG024): 527-542
- ![](https://dblp.org/img/n.png)

\[c8\]
[Taehoon Kim](https://dblp.org/pid/17/4306.html), [Pyunghwan Ahn](https://dblp.org/pid/193/6530.html), [Sangyun Kim](https://dblp.org/pid/85/6907.html), [Sihaeng Lee](https://dblp.org/pid/160/8476.html), [Mark Marsden](https://dblp.org/pid/182/1926.html), [Alessandra Sala](https://dblp.org/pid/27/4656.html), [Seung Hwan Kim](https://dblp.org/pid/49/1259.html), [Bohyung Han](https://dblp.org/pid/73/4880.html), [Kyoung Mu Lee](https://dblp.org/pid/17/4029.html), [Honglak Lee](https://dblp.org/pid/58/2562.html), [Kyounghoon Bae](https://dblp.org/pid/356/2960.html), [Xiangyu Wu](https://dblp.org/pid/17/343.html), [Yi Gao](https://dblp.org/pid/38/4304.html), [Hailiang Zhang](https://dblp.org/pid/22/9265.html), [Yang Yang](https://dblp.org/pid/48/450-128.html), Weili Guo, [Jianfeng Lu](https://dblp.org/pid/82/6187-3.html), [Youngtaek Oh](https://dblp.org/pid/285/3395.html), [Jae-Won Cho](https://dblp.org/pid/15/2423.html), [Dong-Jin Kim](https://dblp.org/pid/16/9611-3.html), [In So Kweon](https://dblp.org/pid/74/4917.html), [Junmo Kim](https://dblp.org/pid/40/240-2.html), [Wooyoung Kang](https://dblp.org/pid/213/8452.html), [Won Young Jhoo](https://dblp.org/pid/315/5240.html), [Byungseok Roh](https://dblp.org/pid/258/1192.html), [Jonghwan Mun](https://dblp.org/pid/192/2107.html), [Solgil Oh](https://dblp.org/pid/356/2607.html), [Kenan Emir Ak](https://dblp.org/pid/182/2932.html), [Gwang-Gook Lee](https://dblp.org/pid/70/5822.html), [Yan Xu](https://dblp.org/pid/03/4702.html), [Mingwei Shen](https://dblp.org/pid/47/10080-1.html), [Kyomin Hwang](https://dblp.org/pid/356/2620.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wonsik Shin](https://dblp.org/pid/309/1630.html), [Kamin Lee](https://dblp.org/pid/356/2611.html), [Wonhark Park](https://dblp.org/pid/356/2694.html), [Dongkwan Lee](https://dblp.org/pid/184/5455.html), [Nojun Kwak](https://dblp.org/pid/49/2806.html), [Yujin Wang](https://dblp.org/pid/158/5229.html), [Yimu Wang](https://dblp.org/pid/140/7766.html), [Tiancheng Gu](https://dblp.org/pid/354/1392.html), [Xingchang Lv](https://dblp.org/pid/356/2875.html), [Mingmao Sun](https://dblp.org/pid/356/2503.html):

NICE: CVPR 2023 Challenge on Zero-shot Image Captioning. [CVPR Workshops2024](https://dblp.org/db/conf/cvpr/cvprw2024.html#conf/cvpr/KimAKLMSKHLLBWG22): 7356-7365
- ![](https://dblp.org/img/n.png)

\[c7\]
[Guangyu Li](https://dblp.org/pid/131/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Li](https://dblp.org/pid/116/1011-27.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hai Cao](https://dblp.org/pid/58/3172.html), [Houjun Wang](https://dblp.org/pid/91/1352.html), Weili Guo, [Chen Gong](https://dblp.org/pid/21/8587-2.html):

MFF-YOLO: Multi-scale Feature Fusion Network for Small Ship Detection in Night Scenes. [ECAI2024](https://dblp.org/db/conf/ecai/ecai2024.html#conf/ecai/LiCWG024): 475-481
- ![](https://dblp.org/img/n.png)

\[i3\]
[Wenjuan Xi](https://dblp.org/pid/243/5910.html), [Xin Song](https://dblp.org/pid/55/3110.html), Weili Guo, [Yang Yang](https://dblp.org/pid/48/450.html):

Robust Semi-Supervised Learning for Self-learning Open-World Classes. [CoRRabs/2401.07551](https://dblp.org/db/journals/corr/corr2401.html#journals/corr/abs-2401-07551) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j18\]
[Yang Yang](https://dblp.org/pid/48/450-74.html), [Ran Bao](https://dblp.org/pid/145/0730.html), Weili Guo, [De-Chuan Zhan](https://dblp.org/pid/74/498.html), [Yilong Yin](https://dblp.org/pid/94/458.html), [Jian Yang](https://dblp.org/pid/y/JianYang3.html):

Deep visual-linguistic fusion network considering cross-modal inconsistency for rumor detection. [Sci. China Inf. Sci.66(12)](https://dblp.org/db/journals/chinaf/chinaf66.html#journals/chinaf/YangBGZYY23) (2023)
- ![](https://dblp.org/img/n.png)

\[j17\]
[Jinxia Zhang](https://dblp.org/pid/89/1778.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yu Shen](https://dblp.org/pid/48/4462.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiacheng Jiang](https://dblp.org/pid/118/4589.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shixiong Fang](https://dblp.org/pid/205/8118.html), [Liping Chen](https://dblp.org/pid/88/1450.html), [Tingting Yan](https://dblp.org/pid/57/11086.html), [Zuoyong Li](https://dblp.org/pid/16/7695.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kanjian Zhang](https://dblp.org/pid/93/1517.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haikun Wei](https://dblp.org/pid/16/6484.html)![](https://dblp.org/img/orcid-mark.12x12.png), Weili Guo![](https://dblp.org/img/orcid-mark.12x12.png):

Automatic Detection of Defective Solar Cells in Electroluminescence Images via Global Similarity and Concatenated Saliency Guided Network. [IEEE Trans. Ind. Informatics19(6)](https://dblp.org/db/journals/tii/tii19.html#journals/tii/ZhangSJFCYLZWG23): 7335-7345 (2023)
- ![](https://dblp.org/img/n.png)

\[c6\]
[Yang Yang](https://dblp.org/pid/48/450.html), [Yurui Huang](https://dblp.org/pid/343/3113.html), Weili Guo, [Baohua Xu](https://dblp.org/pid/50/5510.html), [Dingyin Xia](https://dblp.org/pid/21/1420.html):

Towards Global Video Scene Segmentation with Context-Aware Transformer. [AAAI2023](https://dblp.org/db/conf/aaai/aaai2023.html#conf/aaai/YangHGXX23): 3206-3213
- ![](https://dblp.org/img/n.png)

\[c5\]
[Wenjuan Xi](https://dblp.org/pid/243/5910.html), [Xin Song](https://dblp.org/pid/55/3110.html), Weili Guo, [Yang Yang](https://dblp.org/pid/48/450-74.html):

Robust Semi-Supervised Learning for Self-learning Open-World Classes. [ICDM2023](https://dblp.org/db/conf/icdm/icdm2023.html#conf/icdm/XiSGY23): 658-667
- ![](https://dblp.org/img/n.png)

\[c4\]
[Jun Li](https://dblp.org/pid/116/1011-27.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guangyu Li](https://dblp.org/pid/131/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haobo Jiang](https://dblp.org/pid/213/7268.html)![](https://dblp.org/img/orcid-mark.12x12.png), Weili Guo, [Chen Gong](https://dblp.org/pid/21/8587-2.html):

An Efficient Enhanced-YOLOv5 Algorithm for Multi-scale Ship Detection. [ICONIP (6)2023](https://dblp.org/db/conf/iconip/iconip2023-6.html#conf/iconip/LiLJGG23): 252-263
- ![](https://dblp.org/img/n.png)

\[i2\]
[Taehoon Kim](https://dblp.org/pid/17/4306.html), [Pyunghwan Ahn](https://dblp.org/pid/193/6530.html), [Sangyun Kim](https://dblp.org/pid/85/6907.html), [Sihaeng Lee](https://dblp.org/pid/160/8476.html), [Mark Marsden](https://dblp.org/pid/182/1926.html), [Alessandra Sala](https://dblp.org/pid/27/4656.html), [Seung Hwan Kim](https://dblp.org/pid/49/1259.html), [Bohyung Han](https://dblp.org/pid/73/4880.html), [Kyoung Mu Lee](https://dblp.org/pid/17/4029.html), [Honglak Lee](https://dblp.org/pid/58/2562.html), [Kyounghoon Bae](https://dblp.org/pid/356/2960.html), [Xiangyu Wu](https://dblp.org/pid/17/343.html), [Yi Gao](https://dblp.org/pid/38/4304.html), [Hailiang Zhang](https://dblp.org/pid/22/9265.html), [Yang Yang](https://dblp.org/pid/48/450-128.html), Weili Guo, [Jianfeng Lu](https://dblp.org/pid/82/6187-3.html), [Youngtaek Oh](https://dblp.org/pid/285/3395.html), [Jae-Won Cho](https://dblp.org/pid/15/2423.html), [Dong-Jin Kim](https://dblp.org/pid/16/9611-3.html), [In So Kweon](https://dblp.org/pid/74/4917.html), [Junmo Kim](https://dblp.org/pid/40/240-2.html), [Woo-Young Kang](https://dblp.org/pid/213/8452.html), [Won Young Jhoo](https://dblp.org/pid/315/5240.html), [Byungseok Roh](https://dblp.org/pid/258/1192.html), [Jonghwan Mun](https://dblp.org/pid/192/2107.html), [Solgil Oh](https://dblp.org/pid/356/2607.html), [Kenan Emir Ak](https://dblp.org/pid/182/2932.html), [Gwang-Gook Lee](https://dblp.org/pid/70/5822.html), [Yan Xu](https://dblp.org/pid/03/4702.html), [Mingwei Shen](https://dblp.org/pid/47/10080-1.html), [Kyomin Hwang](https://dblp.org/pid/356/2620.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wonsik Shin](https://dblp.org/pid/309/1630.html), [Kamin Lee](https://dblp.org/pid/356/2611.html), [Wonhark Park](https://dblp.org/pid/356/2694.html), [Dongkwan Lee](https://dblp.org/pid/184/5455.html), [Nojun Kwak](https://dblp.org/pid/49/2806.html), [Yujin Wang](https://dblp.org/pid/158/5229.html), [Yimu Wang](https://dblp.org/pid/140/7766.html), [Tiancheng Gu](https://dblp.org/pid/354/1392.html), [Xingchang Lv](https://dblp.org/pid/356/2875.html), [Mingmao Sun](https://dblp.org/pid/356/2503.html):

NICE: CVPR 2023 Challenge on Zero-shot Image Captioning. [CoRRabs/2309.01961](https://dblp.org/db/journals/corr/corr2309.html#journals/corr/abs-2309-01961) (2023)
- ![](https://dblp.org/img/n.png)

\[i1\]
[Xiangyu Wu](https://dblp.org/pid/17/343.html), [Yi Gao](https://dblp.org/pid/38/4304.html), [Hailiang Zhang](https://dblp.org/pid/22/9265.html), [Yang Yang](https://dblp.org/pid/48/450-128.html), Weili Guo, [Jianfeng Lu](https://dblp.org/pid/82/6187-3.html):

The Solution for the CVPR2023 NICE Image Captioning Challenge. [CoRRabs/2310.06879](https://dblp.org/db/journals/corr/corr2310.html#journals/corr/abs-2310-06879) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j16\]
Weili Guo![](https://dblp.org/img/orcid-mark.12x12.png), [Guangyu Li](https://dblp.org/pid/131/6213.html), [Jianfeng Lu](https://dblp.org/pid/82/6187-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Fisher Information Matrix and its Application of Bipolar Activation Function Based Multilayer Perceptrons With General Gaussian Input. [IEEE Access10](https://dblp.org/db/journals/access/access10.html#journals/access/GuoLL22): 128250-128262 (2022)
- ![](https://dblp.org/img/n.png)

\[j15\]
[Liping Xie](https://dblp.org/pid/91/7400.html)![](https://dblp.org/img/orcid-mark.12x12.png), Weili Guo, [Haikun Wei](https://dblp.org/pid/16/6484.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuanyan Tang](https://dblp.org/pid/t/YuanYanTang.html), [Dacheng Tao](https://dblp.org/pid/46/3391.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Efficient Unsupervised Dimension Reduction for Streaming Multiview Data. [IEEE Trans. Cybern.52(3)](https://dblp.org/db/journals/tcyb/tcyb52.html#journals/tcyb/XieGWTT22): 1772-1784 (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[j14\]
Weili Guo![](https://dblp.org/img/orcid-mark.12x12.png), [Michele Torielli](https://dblp.org/pid/217/5637.html)![](https://dblp.org/img/orcid-mark.12x12.png):

On the Falk Invariant of Shi and Linial Arrangements. [Discret. Comput. Geom.66(2)](https://dblp.org/db/journals/dcg/dcg66.html#journals/dcg/GuoT21): 751-768 (2021)
- ![](https://dblp.org/img/n.png)

\[j13\]
Weili Guo, [Guangyu Li](https://dblp.org/pid/131/6213.html), [Jianfeng Lu](https://dblp.org/pid/82/6187-3.html), [Jian Yang](https://dblp.org/pid/y/JianYang3.html):

Singular Learning of Deep Multilayer Perceptrons for EEG-Based Emotion Recognition. [Frontiers Comput. Sci.3](https://dblp.org/db/journals/fcomp/fcomp3.html#journals/fcomp/GuoLLY21): 786964 (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[j12\]
Weili Guo, [Michele Torielli](https://dblp.org/pid/217/5637.html):

On the Falk invariant of hyperplane arrangements attached to gain graphs. [Australas. J Comb.77](https://dblp.org/db/journals/ajc/ajc77.html#journals/ajc/GuoT20): 301-317 (2020)
- ![](https://dblp.org/img/n.png)

\[c3\]
Weili Guo, [Liping Xie](https://dblp.org/pid/91/7400.html), [Zhenyong Fu](https://dblp.org/pid/36/8779.html), [Jianhui Guo](https://dblp.org/pid/64/7493.html), [Guochen Pang](https://dblp.org/pid/174/1428.html), [Jian Yang](https://dblp.org/pid/y/JianYang3.html):

Analytical form of Fisher information matrix of bipoloar-activation-function-based multilayer perceptrons. [IJCNN2020](https://dblp.org/db/conf/ijcnn/ijcnn2020.html#conf/ijcnn/GuoXFGPY20): 1-8
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j11\]
Weili Guo![](https://dblp.org/img/orcid-mark.12x12.png), [Yew-Soon Ong](https://dblp.org/pid/64/4136.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yingjiang Zhou](https://dblp.org/pid/174/1464.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jaime Rubio Hervas](https://dblp.org/pid/37/11049.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Aiguo Song](https://dblp.org/pid/21/1796.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haikun Wei](https://dblp.org/pid/16/6484.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Fisher Information Matrix of Unipolar Activation Function-Based Multilayer Perceptrons. [IEEE Trans. Cybern.49(8)](https://dblp.org/db/journals/tcyb/tcyb49.html#journals/tcyb/GuoOZHSW19): 3088-3098 (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[j10\]
Weili Guo![](https://dblp.org/img/orcid-mark.12x12.png), [Yuan Yang](https://dblp.org/pid/25/1439-8.html), [Yingjiang Zhou](https://dblp.org/pid/174/1464.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yushun Tan](https://dblp.org/pid/194/8020.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haikun Wei](https://dblp.org/pid/16/6484.html), [Aiguo Song](https://dblp.org/pid/21/1796.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guochen Pang](https://dblp.org/pid/174/1428.html):

Influence Area of Overlap Singularity in Multilayer Perceptrons. [IEEE Access6](https://dblp.org/db/journals/access/access6.html#journals/access/GuoYZTWSP18): 60214-60223 (2018)
- ![](https://dblp.org/img/n.png)

\[j9\]
Weili Guo![](https://dblp.org/img/orcid-mark.12x12.png), [Michele Torielli](https://dblp.org/pid/217/5637.html)![](https://dblp.org/img/orcid-mark.12x12.png):

On the Falk Invariant of Signed Graphic Arrangements. [Graphs Comb.34(3)](https://dblp.org/db/journals/gc/gc34.html#journals/gc/GuoT18): 477-488 (2018)
- ![](https://dblp.org/img/n.png)

\[j8\]
Weili Guo![](https://dblp.org/img/orcid-mark.12x12.png), [Qiumin Guo](https://dblp.org/pid/200/2568.html), [Guangfeng Jiang](https://dblp.org/pid/200/2732.html):

Falk Invariants of Signed Graphic Arrangements. [Graphs Comb.34(6)](https://dblp.org/db/journals/gc/gc34.html#journals/gc/GuoGJ18): 1247-1258 (2018)
- ![](https://dblp.org/img/n.png)

\[j7\]
Weili Guo, [Junsheng Zhao](https://dblp.org/pid/132/1767.html), [Jinxia Zhang](https://dblp.org/pid/89/1778.html), [Haikun Wei](https://dblp.org/pid/16/6484.html), [Aiguo Song](https://dblp.org/pid/21/1796.html), [Kanjian Zhang](https://dblp.org/pid/93/1517.html):

Stability analysis of opposite singularity in multilayer perceptrons. [Neurocomputing282](https://dblp.org/db/journals/ijon/ijon282.html#journals/ijon/GuoZZWSZ18): 192-201 (2018)
- ![](https://dblp.org/img/n.png)

\[j6\]
Weili Guo, [Haikun Wei](https://dblp.org/pid/16/6484.html), [Yew-Soon Ong](https://dblp.org/pid/64/4136.html), [Jaime Rubio Hervas](https://dblp.org/pid/37/11049.html), [Junsheng Zhao](https://dblp.org/pid/132/1767.html), [Hai Wang](https://dblp.org/pid/59/3767.html), [Kanjian Zhang](https://dblp.org/pid/93/1517.html):

Numerical Analysis near Singularities in RBF Networks. [J. Mach. Learn. Res.19](https://dblp.org/db/journals/jmlr/jmlr19.html#journals/jmlr/GuoWOHZWZ18): 1:1-1:39 (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[j5\]
[Qiumin Guo](https://dblp.org/pid/200/2568.html), Weili Guo![](https://dblp.org/img/orcid-mark.12x12.png), [Wentao Hu](https://dblp.org/pid/200/2542.html), [Guangfeng Jiang](https://dblp.org/pid/200/2732.html):

The Global Invariant of Signed Graphic hyperplane Arrangements. [Graphs Comb.33(3)](https://dblp.org/db/journals/gc/gc33.html#journals/gc/GuoGHJ17): 527-535 (2017)
- ![](https://dblp.org/img/n.png)

\[c2\]
[Jinxia Zhang](https://dblp.org/pid/89/1778.html), [Shixiong Fang](https://dblp.org/pid/205/8118.html), [Krista A. Ehinger](https://dblp.org/pid/13/8654.html), Weili Guo, [Wankou Yang](https://dblp.org/pid/99/3602.html), [Haikun Wei](https://dblp.org/pid/16/6484.html):

Probabilistic Hypergraph Optimization for Salient Object Detection. [IScIDE2017](https://dblp.org/db/conf/iscide/iscide2017.html#conf/iscide/ZhangFEGYW17): 368-378
- 2016
- ![](https://dblp.org/img/n.png)

\[c1\]
[Jiang Zhong](https://dblp.org/pid/76/6486.html), [You Xiong](https://dblp.org/pid/189/8491.html), Weili Guo, [Jingyi Xie](https://dblp.org/pid/156/1408.html):

EDAHT: An Expertise Degree Analysis Model for Mass Comments in the E-Commerce System. [ADMA2016](https://dblp.org/db/conf/adma/adma2016.html#conf/adma/ZhongXGX16): 472-480
- 2015
- ![](https://dblp.org/img/n.png)

\[j4\]
Weili Guo, [Haikun Wei](https://dblp.org/pid/16/6484.html), [Junsheng Zhao](https://dblp.org/pid/132/1767.html), [Kanjian Zhang](https://dblp.org/pid/93/1517.html):

Theoretical and numerical analysis of learning dynamics near singularity in multilayer perceptrons. [Neurocomputing151](https://dblp.org/db/journals/ijon/ijon151.html#journals/ijon/GuoWZZ15): 390-400 (2015)
- ![](https://dblp.org/img/n.png)

\[j3\]
[Junsheng Zhao](https://dblp.org/pid/132/1767.html), [Haikun Wei](https://dblp.org/pid/16/6484.html), [Chi Zhang](https://dblp.org/pid/91/195.html), [Weiling Li](https://dblp.org/pid/93/8839.html), Weili Guo, [Kan-Jian Zhang](https://dblp.org/pid/93/1517.html):

Natural Gradient Learning Algorithms for RBF Networks. [Neural Comput.27(2)](https://dblp.org/db/journals/neco/neco27.html#journals/neco/ZhaoWZLGZ15): 481-505 (2015)
- 2014
- ![](https://dblp.org/img/n.png)

\[j2\]
[Junsheng Zhao](https://dblp.org/pid/132/1767.html), [Haikun Wei](https://dblp.org/pid/16/6484.html), Weili Guo, [Kanjian Zhang](https://dblp.org/pid/93/1517.html):

Singularities in the identification of dynamic systems. [Neurocomputing140](https://dblp.org/db/journals/ijon/ijon140.html#journals/ijon/ZhaoWGZ14): 339-344 (2014)
- ![](https://dblp.org/img/n.png)

\[j1\]
Weili Guo, [Haikun Wei](https://dblp.org/pid/16/6484.html), [Junsheng Zhao](https://dblp.org/pid/132/1767.html), [Kanjian Zhang](https://dblp.org/pid/93/1517.html):

Averaged learning equations of error-function-based multilayer perceptrons. [Neural Comput. Appl.25(3-4)](https://dblp.org/db/journals/nca/nca25.html#journals/nca/GuoWZZ14): 825-832 (2014)
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/146/8424.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Pyunghwan Ahn](https://dblp.org/pid/193/6530.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[2](https://dblp.org/pid/146/8424.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Kenan E. Ak](https://dblp.org/pid/182/2932.html)

aka: Kenan Emir Ak

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[3](https://dblp.org/pid/146/8424.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Kyounghoon Bae](https://dblp.org/pid/356/2960.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[4](https://dblp.org/pid/146/8424.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Ran Bao](https://dblp.org/pid/145/0730.html)

[\[j18\]](https://dblp.org/pid/146/8424.html#j18)

[5](https://dblp.org/pid/146/8424.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Hai Cao](https://dblp.org/pid/58/3172.html)

[\[c7\]](https://dblp.org/pid/146/8424.html#c7)

[6](https://dblp.org/pid/146/8424.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Dian Chao](https://dblp.org/pid/372/7224.html)

[\[c10\]](https://dblp.org/pid/146/8424.html#c10)

[7](https://dblp.org/pid/146/8424.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Liping Chen](https://dblp.org/pid/88/1450.html)

[\[j17\]](https://dblp.org/pid/146/8424.html#j17)

[8](https://dblp.org/pid/146/8424.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jae-Won Cho](https://dblp.org/pid/15/2423.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[9](https://dblp.org/pid/146/8424.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Junfeng Du](https://dblp.org/pid/163/1331.html)

[\[j22\]](https://dblp.org/pid/146/8424.html#j22)

[10](https://dblp.org/pid/146/8424.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Krista A. Ehinger](https://dblp.org/pid/13/8654.html)

[\[c2\]](https://dblp.org/pid/146/8424.html#c2)

[11](https://dblp.org/pid/146/8424.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Shixiong Fang](https://dblp.org/pid/205/8118.html)

[\[j17\]](https://dblp.org/pid/146/8424.html#j17) [\[c2\]](https://dblp.org/pid/146/8424.html#c2)

[12](https://dblp.org/pid/146/8424.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Mingxu Feng](https://dblp.org/pid/382/8409.html)

[\[c10\]](https://dblp.org/pid/146/8424.html#c10)

[13](https://dblp.org/pid/146/8424.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Zhenyong Fu](https://dblp.org/pid/36/8779.html)

[\[c3\]](https://dblp.org/pid/146/8424.html#c3)

[14](https://dblp.org/pid/146/8424.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yi Gao](https://dblp.org/pid/38/4304.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2) [\[i1\]](https://dblp.org/pid/146/8424.html#i1)

[15](https://dblp.org/pid/146/8424.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Chen Gong 0002](https://dblp.org/pid/21/8587-2.html)

[\[c7\]](https://dblp.org/pid/146/8424.html#c7) [\[c4\]](https://dblp.org/pid/146/8424.html#c4)

[16](https://dblp.org/pid/146/8424.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Tiancheng Gu](https://dblp.org/pid/354/1392.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[17](https://dblp.org/pid/146/8424.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jianhui Guo](https://dblp.org/pid/64/7493.html)

[\[c3\]](https://dblp.org/pid/146/8424.html#c3)

[18](https://dblp.org/pid/146/8424.html?view=joint&param=18 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=2)

[Qiumin Guo](https://dblp.org/pid/200/2568.html)

[\[j8\]](https://dblp.org/pid/146/8424.html#j8) [\[j5\]](https://dblp.org/pid/146/8424.html#j5)

[19](https://dblp.org/pid/146/8424.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Bohyung Han](https://dblp.org/pid/73/4880.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[20](https://dblp.org/pid/146/8424.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jaime Rubio Hervas](https://dblp.org/pid/37/11049.html)

[\[j11\]](https://dblp.org/pid/146/8424.html#j11) [\[j6\]](https://dblp.org/pid/146/8424.html#j6)

[21](https://dblp.org/pid/146/8424.html?view=joint&param=21 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=2)

[Wentao Hu](https://dblp.org/pid/200/2542.html)

[\[j5\]](https://dblp.org/pid/146/8424.html#j5)

[22](https://dblp.org/pid/146/8424.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Longfei Huang](https://dblp.org/pid/216/8320.html)

[\[c9\]](https://dblp.org/pid/146/8424.html#c9)

[23](https://dblp.org/pid/146/8424.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yurui Huang](https://dblp.org/pid/343/3113.html)

[\[c6\]](https://dblp.org/pid/146/8424.html#c6)

[24](https://dblp.org/pid/146/8424.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Kyomin Hwang](https://dblp.org/pid/356/2620.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[25](https://dblp.org/pid/146/8424.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Won Young Jhoo](https://dblp.org/pid/315/5240.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[26](https://dblp.org/pid/146/8424.html?view=joint&param=26 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=2)

[Guangfeng Jiang](https://dblp.org/pid/200/2732.html)

[\[j20\]](https://dblp.org/pid/146/8424.html#j20) [\[j8\]](https://dblp.org/pid/146/8424.html#j8) [\[j5\]](https://dblp.org/pid/146/8424.html#j5)

[27](https://dblp.org/pid/146/8424.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Haobo Jiang](https://dblp.org/pid/213/7268.html)

[\[c4\]](https://dblp.org/pid/146/8424.html#c4)

[28](https://dblp.org/pid/146/8424.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jiacheng Jiang](https://dblp.org/pid/118/4589.html)

[\[j17\]](https://dblp.org/pid/146/8424.html#j17)

[29](https://dblp.org/pid/146/8424.html?view=joint&param=29 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=2)

[Zhaoting Ju](https://dblp.org/pid/373/8110.html)

[\[j20\]](https://dblp.org/pid/146/8424.html#j20)

[30](https://dblp.org/pid/146/8424.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Woo-Young Kang](https://dblp.org/pid/213/8452.html)

aka: Wooyoung Kang

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[31](https://dblp.org/pid/146/8424.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Dong-Jin Kim 0003](https://dblp.org/pid/16/9611-3.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[32](https://dblp.org/pid/146/8424.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Junmo Kim 0002](https://dblp.org/pid/40/240-2.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[33](https://dblp.org/pid/146/8424.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Sangyun Kim](https://dblp.org/pid/85/6907.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[34](https://dblp.org/pid/146/8424.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Seung Hwan Kim](https://dblp.org/pid/49/1259.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[35](https://dblp.org/pid/146/8424.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Taehoon Kim](https://dblp.org/pid/17/4306.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[36](https://dblp.org/pid/146/8424.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Nojun Kwak](https://dblp.org/pid/49/2806.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[37](https://dblp.org/pid/146/8424.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[In-So Kweon](https://dblp.org/pid/74/4917.html)

aka: In So Kweon

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[38](https://dblp.org/pid/146/8424.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Dongkwan Lee](https://dblp.org/pid/184/5455.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[39](https://dblp.org/pid/146/8424.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Gwang-Gook Lee](https://dblp.org/pid/70/5822.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[40](https://dblp.org/pid/146/8424.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Honglak Lee](https://dblp.org/pid/58/2562.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[41](https://dblp.org/pid/146/8424.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Kamin Lee](https://dblp.org/pid/356/2611.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[42](https://dblp.org/pid/146/8424.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Kyoung Mu Lee](https://dblp.org/pid/17/4029.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[43](https://dblp.org/pid/146/8424.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Sihaeng Lee](https://dblp.org/pid/160/8476.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[44](https://dblp.org/pid/146/8424.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Guangyu Li](https://dblp.org/pid/131/6213.html)

[\[c7\]](https://dblp.org/pid/146/8424.html#c7) [\[c4\]](https://dblp.org/pid/146/8424.html#c4) [\[j16\]](https://dblp.org/pid/146/8424.html#j16) [\[j13\]](https://dblp.org/pid/146/8424.html#j13)

[45](https://dblp.org/pid/146/8424.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jun Li 0027](https://dblp.org/pid/116/1011-27.html)

[\[c7\]](https://dblp.org/pid/146/8424.html#c7) [\[c4\]](https://dblp.org/pid/146/8424.html#c4)

[46](https://dblp.org/pid/146/8424.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Weiling Li](https://dblp.org/pid/93/8839.html)

[\[j3\]](https://dblp.org/pid/146/8424.html#j3)

[47](https://dblp.org/pid/146/8424.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Zuoyong Li](https://dblp.org/pid/16/7695.html)

[\[j17\]](https://dblp.org/pid/146/8424.html#j17)

[48](https://dblp.org/pid/146/8424.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jianfeng Lu 0003](https://dblp.org/pid/82/6187-3.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2) [\[i1\]](https://dblp.org/pid/146/8424.html#i1) [\[j16\]](https://dblp.org/pid/146/8424.html#j16) [\[j13\]](https://dblp.org/pid/146/8424.html#j13)

[49](https://dblp.org/pid/146/8424.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Xingchang Lv](https://dblp.org/pid/356/2875.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[50](https://dblp.org/pid/146/8424.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Mark Marsden](https://dblp.org/pid/182/1926.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[51](https://dblp.org/pid/146/8424.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jonghwan Mun](https://dblp.org/pid/192/2107.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[52](https://dblp.org/pid/146/8424.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Solgil Oh](https://dblp.org/pid/356/2607.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[53](https://dblp.org/pid/146/8424.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Youngtaek Oh](https://dblp.org/pid/285/3395.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[54](https://dblp.org/pid/146/8424.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yew-Soon Ong](https://dblp.org/pid/64/4136.html)

[\[j11\]](https://dblp.org/pid/146/8424.html#j11) [\[j6\]](https://dblp.org/pid/146/8424.html#j6)

[55](https://dblp.org/pid/146/8424.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Guochen Pang](https://dblp.org/pid/174/1428.html)

[\[c3\]](https://dblp.org/pid/146/8424.html#c3) [\[j10\]](https://dblp.org/pid/146/8424.html#j10)

[56](https://dblp.org/pid/146/8424.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Wonhark Park](https://dblp.org/pid/356/2694.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[57](https://dblp.org/pid/146/8424.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Xiaowen Qin](https://dblp.org/pid/411/6694.html)

[\[j22\]](https://dblp.org/pid/146/8424.html#j22)

[58](https://dblp.org/pid/146/8424.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Byungseok Roh](https://dblp.org/pid/258/1192.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[59](https://dblp.org/pid/146/8424.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Alessandra Sala](https://dblp.org/pid/27/4656.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[60](https://dblp.org/pid/146/8424.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Mingwei Shen 0001](https://dblp.org/pid/47/10080-1.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[61](https://dblp.org/pid/146/8424.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yu Shen](https://dblp.org/pid/48/4462.html)

[\[j17\]](https://dblp.org/pid/146/8424.html#j17)

[62](https://dblp.org/pid/146/8424.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Wonsik Shin](https://dblp.org/pid/309/1630.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[63](https://dblp.org/pid/146/8424.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Aiguo Song](https://dblp.org/pid/21/1796.html)

[\[j11\]](https://dblp.org/pid/146/8424.html#j11) [\[j10\]](https://dblp.org/pid/146/8424.html#j10) [\[j7\]](https://dblp.org/pid/146/8424.html#j7)

[64](https://dblp.org/pid/146/8424.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Xin Song](https://dblp.org/pid/55/3110.html)

[\[i3\]](https://dblp.org/pid/146/8424.html#i3) [\[c5\]](https://dblp.org/pid/146/8424.html#c5)

[65](https://dblp.org/pid/146/8424.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Guifu Su](https://dblp.org/pid/117/7143.html)

[\[j22\]](https://dblp.org/pid/146/8424.html#j22)

[66](https://dblp.org/pid/146/8424.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Mingmao Sun](https://dblp.org/pid/356/2503.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[67](https://dblp.org/pid/146/8424.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yushun Tan](https://dblp.org/pid/194/8020.html)

[\[j10\]](https://dblp.org/pid/146/8424.html#j10)

[68](https://dblp.org/pid/146/8424.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yuan Yan Tang](https://dblp.org/pid/t/YuanYanTang.html)

aka: Yuanyan Tang

[\[j15\]](https://dblp.org/pid/146/8424.html#j15)

[69](https://dblp.org/pid/146/8424.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Dacheng Tao](https://dblp.org/pid/46/3391.html)

[\[j15\]](https://dblp.org/pid/146/8424.html#j15)

[70](https://dblp.org/pid/146/8424.html?view=joint&param=70 "show joint publications")

[Michele Torielli](https://dblp.org/pid/217/5637.html)

[\[j14\]](https://dblp.org/pid/146/8424.html#j14) [\[j12\]](https://dblp.org/pid/146/8424.html#j12) [\[j9\]](https://dblp.org/pid/146/8424.html#j9)

[71](https://dblp.org/pid/146/8424.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Hai Wang](https://dblp.org/pid/59/3767.html)

[\[j6\]](https://dblp.org/pid/146/8424.html#j6)

[72](https://dblp.org/pid/146/8424.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Houjun Wang](https://dblp.org/pid/91/1352.html)

[\[c7\]](https://dblp.org/pid/146/8424.html#c7)

[73](https://dblp.org/pid/146/8424.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jingyuan Wang](https://dblp.org/pid/75/5135.html)

[\[c9\]](https://dblp.org/pid/146/8424.html#c9)

[74](https://dblp.org/pid/146/8424.html?view=joint&param=74 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=3)

[Laili Wang](https://dblp.org/pid/159/5465.html)

[\[j21\]](https://dblp.org/pid/146/8424.html#j21) [\[j19\]](https://dblp.org/pid/146/8424.html#j19)

[75](https://dblp.org/pid/146/8424.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yimu Wang](https://dblp.org/pid/140/7766.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[76](https://dblp.org/pid/146/8424.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yujin Wang](https://dblp.org/pid/158/5229.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[77](https://dblp.org/pid/146/8424.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Haikun Wei](https://dblp.org/pid/16/6484.html)

[\[j17\]](https://dblp.org/pid/146/8424.html#j17) [\[j15\]](https://dblp.org/pid/146/8424.html#j15) [\[j11\]](https://dblp.org/pid/146/8424.html#j11) [\[j10\]](https://dblp.org/pid/146/8424.html#j10) [\[j7\]](https://dblp.org/pid/146/8424.html#j7) [\[j6\]](https://dblp.org/pid/146/8424.html#j6) [\[c2\]](https://dblp.org/pid/146/8424.html#c2) [\[j4\]](https://dblp.org/pid/146/8424.html#j4) [\[j3\]](https://dblp.org/pid/146/8424.html#j3) [\[j2\]](https://dblp.org/pid/146/8424.html#j2) [\[j1\]](https://dblp.org/pid/146/8424.html#j1)

[78](https://dblp.org/pid/146/8424.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Xiangyu Wu](https://dblp.org/pid/17/343.html)

[\[c9\]](https://dblp.org/pid/146/8424.html#c9) [\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2) [\[i1\]](https://dblp.org/pid/146/8424.html#i1)

[79](https://dblp.org/pid/146/8424.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yue Wu](https://dblp.org/pid/41/5979.html)

[\[j22\]](https://dblp.org/pid/146/8424.html#j22)

[80](https://dblp.org/pid/146/8424.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Wenjuan Xi](https://dblp.org/pid/243/5910.html)

[\[i3\]](https://dblp.org/pid/146/8424.html#i3) [\[c5\]](https://dblp.org/pid/146/8424.html#c5)

[81](https://dblp.org/pid/146/8424.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Dingyin Xia](https://dblp.org/pid/21/1420.html)

[\[c6\]](https://dblp.org/pid/146/8424.html#c6)

[82](https://dblp.org/pid/146/8424.html?view=joint&param=82 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=3)

[Guochun Xiao](https://dblp.org/pid/133/7600.html)

[\[j21\]](https://dblp.org/pid/146/8424.html#j21) [\[j19\]](https://dblp.org/pid/146/8424.html#j19)

[83](https://dblp.org/pid/146/8424.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jingyi Xie](https://dblp.org/pid/156/1408.html)

[\[c1\]](https://dblp.org/pid/146/8424.html#c1)

[84](https://dblp.org/pid/146/8424.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Liping Xie](https://dblp.org/pid/91/7400.html)

[\[j15\]](https://dblp.org/pid/146/8424.html#j15) [\[c3\]](https://dblp.org/pid/146/8424.html#c3)

[85](https://dblp.org/pid/146/8424.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[You Xiong](https://dblp.org/pid/189/8491.html)

[\[c1\]](https://dblp.org/pid/146/8424.html#c1)

[86](https://dblp.org/pid/146/8424.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Baohua Xu](https://dblp.org/pid/50/5510.html)

[\[c6\]](https://dblp.org/pid/146/8424.html#c6)

[87](https://dblp.org/pid/146/8424.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yan Xu](https://dblp.org/pid/03/4702.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2)

[88](https://dblp.org/pid/146/8424.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Tingting Yan](https://dblp.org/pid/57/11086.html)

[\[j17\]](https://dblp.org/pid/146/8424.html#j17)

[89](https://dblp.org/pid/146/8424.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jian Yang 0003](https://dblp.org/pid/y/JianYang3.html)

[\[j18\]](https://dblp.org/pid/146/8424.html#j18) [\[j13\]](https://dblp.org/pid/146/8424.html#j13) [\[c3\]](https://dblp.org/pid/146/8424.html#c3)

[90](https://dblp.org/pid/146/8424.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c2\]](https://dblp.org/pid/146/8424.html#c2)

[91](https://dblp.org/pid/146/8424.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yang Yang](https://dblp.org/pid/48/450.html)

[\[i3\]](https://dblp.org/pid/146/8424.html#i3) [\[c6\]](https://dblp.org/pid/146/8424.html#c6)

[92](https://dblp.org/pid/146/8424.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yang Yang 0074](https://dblp.org/pid/48/450-74.html)

[\[c9\]](https://dblp.org/pid/146/8424.html#c9) [\[j18\]](https://dblp.org/pid/146/8424.html#j18) [\[c5\]](https://dblp.org/pid/146/8424.html#c5)

[93](https://dblp.org/pid/146/8424.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yang Yang 0128](https://dblp.org/pid/48/450-128.html)

[\[c10\]](https://dblp.org/pid/146/8424.html#c10) [\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2) [\[i1\]](https://dblp.org/pid/146/8424.html#i1)

[94](https://dblp.org/pid/146/8424.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yuan Yang 0008](https://dblp.org/pid/25/1439-8.html)

[\[j10\]](https://dblp.org/pid/146/8424.html#j10)

[95](https://dblp.org/pid/146/8424.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yilong Yin](https://dblp.org/pid/94/458.html)

[\[j18\]](https://dblp.org/pid/146/8424.html#j18)

[96](https://dblp.org/pid/146/8424.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[De-Chuan Zhan](https://dblp.org/pid/74/498.html)

[\[j18\]](https://dblp.org/pid/146/8424.html#j18)

[97](https://dblp.org/pid/146/8424.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Chi Zhang](https://dblp.org/pid/91/195.html)

[\[j3\]](https://dblp.org/pid/146/8424.html#j3)

[98](https://dblp.org/pid/146/8424.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Hailiang Zhang](https://dblp.org/pid/22/9265.html)

[\[c8\]](https://dblp.org/pid/146/8424.html#c8) [\[i2\]](https://dblp.org/pid/146/8424.html#i2) [\[i1\]](https://dblp.org/pid/146/8424.html#i1)

[99](https://dblp.org/pid/146/8424.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jinxia Zhang](https://dblp.org/pid/89/1778.html)

[\[j17\]](https://dblp.org/pid/146/8424.html#j17) [\[j7\]](https://dblp.org/pid/146/8424.html#j7) [\[c2\]](https://dblp.org/pid/146/8424.html#c2)

[100](https://dblp.org/pid/146/8424.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Kan-Jian Zhang](https://dblp.org/pid/93/1517.html)

aka: Kanjian Zhang

[\[j17\]](https://dblp.org/pid/146/8424.html#j17) [\[j7\]](https://dblp.org/pid/146/8424.html#j7) [\[j6\]](https://dblp.org/pid/146/8424.html#j6) [\[j4\]](https://dblp.org/pid/146/8424.html#j4) [\[j3\]](https://dblp.org/pid/146/8424.html#j3) [\[j2\]](https://dblp.org/pid/146/8424.html#j2) [\[j1\]](https://dblp.org/pid/146/8424.html#j1)

[101](https://dblp.org/pid/146/8424.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yuxuan Zhang](https://dblp.org/pid/126/5240.html)

[\[c10\]](https://dblp.org/pid/146/8424.html#c10)

[102](https://dblp.org/pid/146/8424.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Zhenghang Zhang](https://dblp.org/pid/292/3255.html)

[\[j22\]](https://dblp.org/pid/146/8424.html#j22)

[103](https://dblp.org/pid/146/8424.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Junsheng Zhao](https://dblp.org/pid/132/1767.html)

[\[j7\]](https://dblp.org/pid/146/8424.html#j7) [\[j6\]](https://dblp.org/pid/146/8424.html#j6) [\[j4\]](https://dblp.org/pid/146/8424.html#j4) [\[j3\]](https://dblp.org/pid/146/8424.html#j3) [\[j2\]](https://dblp.org/pid/146/8424.html#j2) [\[j1\]](https://dblp.org/pid/146/8424.html#j1)

[104](https://dblp.org/pid/146/8424.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Jiang Zhong](https://dblp.org/pid/76/6486.html)

[\[c1\]](https://dblp.org/pid/146/8424.html#c1)

[105](https://dblp.org/pid/146/8424.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/146/8424.html?view=group&param=1)

[Yingjiang Zhou](https://dblp.org/pid/174/1464.html)

[\[j11\]](https://dblp.org/pid/146/8424.html#j11) [\[j10\]](https://dblp.org/pid/146/8424.html#j10)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/146/8424.html#) [\[–\]](https://dblp.org/pid/146/8424.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/146/8424.html#) [\[–\]](https://dblp.org/pid/146/8424.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/146/8424.html#) [\[–\]](https://dblp.org/pid/146/8424.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/146/8424.html#) [\[–\]](https://dblp.org/pid/146/8424.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/146/8424.html#) [\[–\]](https://dblp.org/pid/146/8424.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)