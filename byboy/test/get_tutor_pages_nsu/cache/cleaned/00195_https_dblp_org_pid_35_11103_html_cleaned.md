> 抓取来源：https://dblp.org/pid/35/11103.html

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

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Felix+Juefei-Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F35%2F11103%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Felix+Juefei-Xu+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F35%2F11103%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Felix+Juefei-Xu+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F35%2F11103%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Felix+Juefei-Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F35%2F11103%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Felix+Juefei-Xu+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F35%2F11103%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Felix+Juefei-Xu%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F35%2F11103%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Felix+Juefei-Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F35%2F11103%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F35%2F11103%3E+%7D+.%0A%0A%7D)

_showing all203 records_

20102026302010: 12011: 22012: 22013: 22014: 42014: 42015: 102015: 102016: 72016: 72016: 72017: 22017: 22018: 122018: 122018: 122019: 52019: 52019: 52020: 232020: 232021: 272021: 272022: 172022: 172022: 172023: 172023: 172023: 172024: 372024: 372024: 372025: 322025: 322025: 322026: 32026: 3

**refine by search term**

![](https://dblp.org/img/clear-mark.medium.16x16.png)![filter active](https://dblp.org/img/filter-mark.12x12.png)

**refine by type**

- [ ] Books and Theses(only)
- [ ] Journal Articles(only)
- [ ] Conference and Workshop Papers(only)
- [ ] Informal and Other Publications(only)

- select all \| deselect all

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by coauthor**

- ![](https://dblp.org/img/add-mark.12x12.png)Qing Guo 0005 (92)
- ![](https://dblp.org/img/add-mark.12x12.png)Yang Liu 0003 (80)
- ![](https://dblp.org/img/add-mark.12x12.png)Lei Ma 0003 (65)
- ![](https://dblp.org/img/add-mark.12x12.png)Yihao Huang 0001 (39)
- ![](https://dblp.org/img/add-mark.12x12.png)Xiaofei Xie (37)
- ![](https://dblp.org/img/add-mark.12x12.png)Marios Savvides (35)
- ![](https://dblp.org/img/add-mark.12x12.png)Geguang Pu (29)
- ![](https://dblp.org/img/add-mark.12x12.png)Wei Feng 0005 (26)
- ![](https://dblp.org/img/add-mark.12x12.png)Jianjun Zhao 0001 (24)
- ![](https://dblp.org/img/add-mark.12x12.png)Hongkai Yu (17)

- _657 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (175)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-0857-8611 (28)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (97)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (20)
- ![](https://dblp.org/img/add-mark.12x12.png)MM (8)
- ![](https://dblp.org/img/add-mark.12x12.png)BTAS (6)
- ![](https://dblp.org/img/add-mark.12x12.png)ICIP (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (5)
- ![](https://dblp.org/img/add-mark.12x12.png)ICCV (5)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Multim. (4)
- ![](https://dblp.org/img/add-mark.12x12.png)ECCV (4)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Inf. Forensics Secur. (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Pattern Recognit. (3)

- _36 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)open (118)
- ![](https://dblp.org/img/add-mark.12x12.png)closed (85)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[j30\]
[Xuan Xie](https://dblp.org/pid/22/10184-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiayang Song](https://dblp.org/pid/182/7194.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuheng Huang](https://dblp.org/pid/01/6508-4.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Da Song](https://dblp.org/pid/222/6729.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html):

LeCov: Multi-level testing criteria for large language models. [J. Syst. Softw.235](https://dblp.org/db/journals/jss/jss235.html#journals/jss/XieSHSJM26): 112763 (2026)
- ![](https://dblp.org/img/n.png)

\[j29\]
[Liming Zhai](https://dblp.org/pid/149/3381.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shengchao Qin](https://dblp.org/pid/q/ShengchaoQin.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Adversarial rain attack and defensive deraining for DNN perception. [Neural Networks196](https://dblp.org/db/journals/nn/nn196.html#journals/nn/ZhaiGJXMFQL26): 108376 (2026)
- ![](https://dblp.org/img/n.png)

\[i97\]
[Haochen Zhang](https://dblp.org/pid/133/3401.html), [Animesh Sinha](https://dblp.org/pid/289/7538.html), Felix Juefei-Xu, [Haoyu Ma](https://dblp.org/pid/144/1634.html), [Kunpeng Li](https://dblp.org/pid/38/1577.html), [Zhipeng Fan](https://dblp.org/pid/228/6404.html), [Meng Dong](https://dblp.org/pid/58/2821.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html), [Tingbo Hou](https://dblp.org/pid/35/3986.html), [Peizhao Zhang](https://dblp.org/pid/23/8011.html), [Zecheng He](https://dblp.org/pid/203/5675.html):

Non-Markov Multi-Round Conversational Image Generation with History-Conditioned MLLMs. [CoRRabs/2601.20911](https://dblp.org/db/journals/corr/corr2601.html#journals/corr/abs-2601-20911) (2026)
- 2025
- ![](https://dblp.org/img/n.png)

\[j28\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), [Hua Qi](https://dblp.org/pid/87/4406.html), [Jingyang Sun](https://dblp.org/pid/217/7354.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Di Lin](https://dblp.org/pid/20/3191-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Song Wang](https://dblp.org/pid/62/3151-2.html):

EfficientDeRain+: Learning Uncertainty-Aware Filtering via RainMix Augmentation for High-Efficiency Deraining. [Int. J. Comput. Vis.133(4)](https://dblp.org/db/journals/ijcv/ijcv133.html#journals/ijcv/GuoQSJMLFW25): 2111-2135 (2025)
- ![](https://dblp.org/img/n.png)

\[j27\]
[Yuzhu Cai](https://dblp.org/pid/375/7444.html), [Sheng Yin](https://dblp.org/pid/52/2662.html), [Yuxi Wei](https://dblp.org/pid/323/4932.html), [Chenxin Xu](https://dblp.org/pid/281/7263.html), [Weibo Mao](https://dblp.org/pid/44/4166.html), Felix Juefei-Xu, [Siheng Chen](https://dblp.org/pid/136/4945.html), [Yanfeng Wang](https://dblp.org/pid/55/5407-1.html):

Ethical-Lens: Curbing malicious usages of open-source text-to-image models. [Patterns6(4)](https://dblp.org/db/journals/patterns/patterns6.html#journals/patterns/CaiYWXMJCW25): 101187 (2025)
- ![](https://dblp.org/img/n.png)

\[j26\]
[Yihao Huang](https://dblp.org/pid/255/5085.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Luo](https://dblp.org/pid/53/5106.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaojun Jia](https://dblp.org/pid/57/5656.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weikai Miao](https://dblp.org/pid/94/4256.html), [Geguang Pu](https://dblp.org/pid/33/1678.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Scale-Invariant Adversarial Attack Against Arbitrary-Scale Super-Resolution. [IEEE Trans. Inf. Forensics Secur.20](https://dblp.org/db/journals/tifs/tifs20.html#journals/tifs/HuangLGJJMPL25): 3909-3924 (2025)
- ![](https://dblp.org/img/n.png)

\[j25\]
[Yupeng Cheng](https://dblp.org/pid/148/8300.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Huazhu Fu](https://dblp.org/pid/63/7767.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shangwei Lin](https://dblp.org/pid/55/4730-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weisi Lin](https://dblp.org/pid/14/3737.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Adversarial Exposure Attack on Diabetic Retinopathy Imagery Grading. [IEEE J. Biomed. Health Informatics29(1)](https://dblp.org/db/journals/titb/titb29.html#journals/titb/ChengGJFLL25): 297-309 (2025)
- ![](https://dblp.org/img/n.png)

\[j24\]
[Shuangzhi Li](https://dblp.org/pid/174/9969-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhijie Wang](https://dblp.org/pid/64/5749-14.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xingyu Li](https://dblp.org/pid/45/2385.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Common Corruption Robustness of Point Cloud Detectors: Benchmark and Enhancement. [IEEE Trans. Multim.27](https://dblp.org/db/journals/tmm/tmm27.html#journals/tmm/LiWJGLM25): 848-859 (2025)
- ![](https://dblp.org/img/n.png)

\[j23\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhijie Wang](https://dblp.org/pid/64/5749-14.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lubo Wang](https://dblp.org/pid/352/4271.html), [Haotian Dong](https://dblp.org/pid/314/2870.html), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Di Lin](https://dblp.org/pid/20/3191-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

CarveNet: Carving Point-Block for Complex 3D Shape Completion. [IEEE Trans. Multim.27](https://dblp.org/db/journals/tmm/tmm27.html#journals/tmm/GuoWWDJLMFL25): 1047-1058 (2025)
- ![](https://dblp.org/img/n.png)

\[j22\]
[Yuheng Huang](https://dblp.org/pid/01/6508-4.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiayang Song](https://dblp.org/pid/182/7194.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhijie Wang](https://dblp.org/pid/64/5749-14.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shengming Zhao](https://dblp.org/pid/366/2862.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huaming Chen](https://dblp.org/pid/139/3914.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Look Before You Leap: An Exploratory Study of Uncertainty Analysis for Large Language Models. [IEEE Trans. Software Eng.51(2)](https://dblp.org/db/journals/tse/tse51.html#journals/tse/HuangSWZCJM25): 413-429 (2025)
- ![](https://dblp.org/img/n.png)

\[c75\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), [Chong Wang](https://dblp.org/pid/72/1334-13.html), [Xiaojun Jia](https://dblp.org/pid/57/5656.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Jian Zhang](https://dblp.org/pid/07/314-87.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

Efficient Universal Goal Hijacking with Semantics-guided Prompt Organization. [ACL (1)2025](https://dblp.org/db/conf/acl/acl2025-1.html#conf/acl/0001WJGJZLP25): 5796-5816
- ![](https://dblp.org/img/n.png)

\[c74\]
[Qingcheng Zeng](https://dblp.org/pid/84/1451.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mingyu Jin](https://dblp.org/pid/215/7601.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qinkai Yu](https://dblp.org/pid/350/0275.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenting Wang](https://dblp.org/pid/263/4521.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenyue Hua](https://dblp.org/pid/278/7993.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guangyan Sun](https://dblp.org/pid/67/9556.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanda Meng](https://dblp.org/pid/275/6822.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shiqing Ma](https://dblp.org/pid/172/8745.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qifan Wang](https://dblp.org/pid/33/8610-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Fan Yang](https://dblp.org/pid/29/3081-23.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kaize Ding](https://dblp.org/pid/234/6878.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ruixiang Tang](https://dblp.org/pid/239/1928.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yongfeng Zhang](https://dblp.org/pid/82/7829-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Uncertainty Quantification for Multiple-Choice Questions is Just One-Token Deep. [CIKM2025](https://dblp.org/db/conf/cikm/cikm2025.html#conf/cikm/ZengJYWHSMMWJ0D25): 5474-5478
- ![](https://dblp.org/img/n.png)

\[c73\]
[Hongjie Wang](https://dblp.org/pid/65/7565-2.html), [Chih-Yao Ma](https://dblp.org/pid/198/0963.html), [Yen-Cheng Liu](https://dblp.org/pid/29/7584.html), [Ji Hou](https://dblp.org/pid/152/4311.html), [Tao Xu](https://dblp.org/pid/96/6771.html), [Jialiang Wang](https://dblp.org/pid/27/8578-1.html), Felix Juefei-Xu, [Yaqiao Luo](https://dblp.org/pid/150/6230.html), [Peizhao Zhang](https://dblp.org/pid/23/8011.html), [Tingbo Hou](https://dblp.org/pid/35/3986.html), [Peter Vajda](https://dblp.org/pid/44/5953.html), [Niraj K. Jha](https://dblp.org/pid/j/NirajKJha.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html):

LinGen: Towards High-Resolution Minute-Length Text-to-Video Generation with Linear Computational Complexity. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/0002MLHXWJLZHVJ25): 2578-2588
- ![](https://dblp.org/img/n.png)

\[c72\]
[Feng Liang](https://dblp.org/pid/54/6821.html), [Haoyu Ma](https://dblp.org/pid/144/1634.html), [Zecheng He](https://dblp.org/pid/203/5675.html), [Tingbo Hou](https://dblp.org/pid/35/3986.html), [Ji Hou](https://dblp.org/pid/152/4311.html), [Kunpeng Li](https://dblp.org/pid/38/1577.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html), Felix Juefei-Xu, [Samaneh Azadi](https://dblp.org/pid/145/9932.html), [Animesh Sinha](https://dblp.org/pid/289/7538.html), [Peizhao Zhang](https://dblp.org/pid/23/8011.html), [Peter Vajda](https://dblp.org/pid/44/5953.html), [Diana Marculescu](https://dblp.org/pid/59/2715.html):

Movie Weaver: Tuning-Free Multi-Concept Video Personalization with Anchored Prompts. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/LiangMHHHLDJASZ25): 13146-13156
- ![](https://dblp.org/img/n.png)

\[c71\]
[Zhenting Wang](https://dblp.org/pid/263/4521.html), [Shuming Hu](https://dblp.org/pid/352/2124.html), [Shiyu Zhao](https://dblp.org/pid/120/7474-1.html), [Xiaowen Lin](https://dblp.org/pid/210/0844.html), Felix Juefei-Xu, [Zhuowei Li](https://dblp.org/pid/181/2874-2.html), [Ligong Han](https://dblp.org/pid/187/1675.html), [Harihar Subramanyam](https://dblp.org/pid/166/8374.html), [Li Chen](https://dblp.org/pid/181/2847.html), [Jianfa Chen](https://dblp.org/pid/319/6731.html), [Nan Jiang](https://dblp.org/pid/06/4489.html), [Lingjuan Lyu](https://dblp.org/pid/178/9876.html), [Shiqing Ma](https://dblp.org/pid/172/8745.html), [Dimitris N. Metaxas](https://dblp.org/pid/m/DNMetaxas.html), [Ankit Jain](https://dblp.org/pid/37/7907.html):

MLLM-as-a-Judge for Image Safety without Human Labeling. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/WangHZLJ0HSCCJL25): 14657-14666
- ![](https://dblp.org/img/n.png)

\[c70\]
[Bolin Lai](https://dblp.org/pid/250/6136.html), Felix Juefei-Xu, [Miao Liu](https://dblp.org/pid/60/6348-7.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html), [Nikhil Mehta](https://dblp.org/pid/89/7487-2.html), [Chenguang Zhu](https://dblp.org/pid/48/7536.html), [Zeyi Huang](https://dblp.org/pid/142/5094.html), [James M. Rehg](https://dblp.org/pid/r/JMRehg.html), [Sangmin Lee](https://dblp.org/pid/68/311-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ning Zhang](https://dblp.org/pid/181/2597.html), [Tong Xiao](https://dblp.org/pid/05/5091-3.html):

Unleashing In-context Learning of Autoregressive Models for Few-shot Image Manipulation. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/LaiJ0D0ZHR0ZX25): 18346-18357
- ![](https://dblp.org/img/n.png)

\[c69\]
[Orr Zohar](https://dblp.org/pid/335/1624.html), [Xiaohan Wang](https://dblp.org/pid/73/1307.html), [Yann Dubois](https://dblp.org/pid/198/7527.html), [Nikhil Mehta](https://dblp.org/pid/89/7487-2.html), [Tong Xiao](https://dblp.org/pid/05/5091-3.html), [Philippe Hansen-Estruch](https://dblp.org/pid/289/6990.html), [Licheng Yu](https://dblp.org/pid/32/10805.html), [Xiaofang Wang](https://dblp.org/pid/58/2390.html), Felix Juefei-Xu, [Ning Zhang](https://dblp.org/pid/181/2597.html), [Serena Yeung-Levy](https://dblp.org/pid/147/5023.html), [Xide Xia](https://dblp.org/pid/172/0129.html):

Apollo: An Exploration of Video Understanding in Large Multimodal Models. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/ZoharWD0XHYWJZY25): 18891-18901
- ![](https://dblp.org/img/n.png)

\[c68\]
[Shiyu Zhao](https://dblp.org/pid/120/7474-1.html), [Zhenting Wang](https://dblp.org/pid/263/4521.html), Felix Juefei-Xu, [Xide Xia](https://dblp.org/pid/172/0129.html), [Miao Liu](https://dblp.org/pid/60/6348-7.html), [Xiaofang Wang](https://dblp.org/pid/58/2390.html), [Mingfu Liang](https://dblp.org/pid/241/9790.html), [Ning Zhang](https://dblp.org/pid/181/2597.html), [Dimitris N. Metaxas](https://dblp.org/pid/m/DNMetaxas.html), [Licheng Yu](https://dblp.org/pid/32/10805.html):

Accelerating Multimodal Large Language Models by Searching Optimal Vision Token Reduction. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/ZhaoWJX0WLZMY25): 29869-29879
- ![](https://dblp.org/img/n.png)

\[c67\]
[Weihao Xuan](https://dblp.org/pid/249/5453.html), [Rui Yang](https://dblp.org/pid/92/1942-16.html), [Heli Qi](https://dblp.org/pid/320/4798.html), [Qingcheng Zeng](https://dblp.org/pid/84/1451.html), [Yunze Xiao](https://dblp.org/pid/310/1568.html), [Aosong Feng](https://dblp.org/pid/260/0450.html), [Dairui Liu](https://dblp.org/pid/261/2925.html), [Yun Xing](https://dblp.org/pid/09/9613.html), [Junjue Wang](https://dblp.org/pid/146/0104.html), [Fan Gao](https://dblp.org/pid/51/3982.html), [Jinghui Lu](https://dblp.org/pid/14/983.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuang Jiang](https://dblp.org/pid/249/8012.html), [Huitao Li](https://dblp.org/pid/233/2009.html), [Xin Li](https://dblp.org/pid/09/1365-79.html), [Kunyu Yu](https://dblp.org/pid/381/5302.html), [Ruihai Dong](https://dblp.org/pid/94/11082.html), [Shangding Gu](https://dblp.org/pid/268/8183.html), [Yuekang Li](https://dblp.org/pid/204/3729.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu, [Foutse Khomh](https://dblp.org/pid/32/147.html), [Osamu Yoshie](https://dblp.org/pid/14/5985.html), [Qingyu Chen](https://dblp.org/pid/28/5691-1.html), [Douglas Teodoro](https://dblp.org/pid/01/7332.html), [Nan Liu](https://dblp.org/pid/86/4643-3.html), [Randy Goebel](https://dblp.org/pid/g/RandyGoebel.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Edison Marrese-Taylor](https://dblp.org/pid/137/6899.html), [Shijian Lu](https://dblp.org/pid/42/2718.html), [Yusuke Iwasawa](https://dblp.org/pid/117/7377.html), [Yutaka Matsuo](https://dblp.org/pid/m/YMatsuo.html), [Irene Li](https://dblp.org/pid/44/8976.html):

MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation. [EMNLP2025](https://dblp.org/db/conf/emnlp/emnlp2025.html#conf/emnlp/XuanYQZXFLXWGLJLLYDGLXJ25): 1513-1532
- ![](https://dblp.org/img/n.png)

\[c66\]
[Chao Chen](https://dblp.org/pid/66/3019.html), [Mingzhi Zhu](https://dblp.org/pid/29/8415.html), [Ankush Pratap Singh](https://dblp.org/pid/362/3050.html), [Yu Yan](https://dblp.org/pid/12/778.html), Felix Juefei-Xu, [Chen Feng](https://dblp.org/pid/01/161-2.html):

Human-Inspired Summarization: Cluster Scene Videos into Diverse Frames. [ICCVW2025](https://dblp.org/db/conf/iccv/iccv2025w.html#conf/iccv/ChenZSYJF25): 4872-4882
- ![](https://dblp.org/img/n.png)

\[c65\]
[Xinxi Zhang](https://dblp.org/pid/246/3433.html), [Song Wen](https://dblp.org/pid/119/9492-1.html), [Ligong Han](https://dblp.org/pid/187/1675.html), Felix Juefei-Xu, [Akash Srivastava](https://dblp.org/pid/24/9528.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Vladimir Pavlovic](https://dblp.org/pid/98/2506.html), [Hao Wang](https://dblp.org/pid/w/HaoWang-14.html), [Molei Tao](https://dblp.org/pid/56/9263.html), [Dimitris N. Metaxas](https://dblp.org/pid/m/DNMetaxas.html):

SODA: Spectral Orthogonal Decomposition Adaptation for Diffusion Models. [WACV2025](https://dblp.org/db/conf/wacv/wacv2025.html#conf/wacv/Zhang0HJSH0WTM25): 4665-4682
- ![](https://dblp.org/img/n.png)

\[i96\]
[Zhenting Wang](https://dblp.org/pid/263/4521.html), [Shuming Hu](https://dblp.org/pid/352/2124.html), [Shiyu Zhao](https://dblp.org/pid/120/7474-1.html), [Xiaowen Lin](https://dblp.org/pid/210/0844.html), Felix Juefei-Xu, [Zhuowei Li](https://dblp.org/pid/181/2874-2.html), [Ligong Han](https://dblp.org/pid/187/1675.html), [Harihar Subramanyam](https://dblp.org/pid/166/8374.html), [Li Chen](https://dblp.org/pid/181/2847.html), [Jianfa Chen](https://dblp.org/pid/319/6731.html), [Nan Jiang](https://dblp.org/pid/06/4489.html), [Lingjuan Lyu](https://dblp.org/pid/178/9876.html), [Shiqing Ma](https://dblp.org/pid/172/8745.html), [Dimitris N. Metaxas](https://dblp.org/pid/m/DNMetaxas.html), [Ankit Jain](https://dblp.org/pid/37/7907.html):

MLLM-as-a-Judge for Image Safety without Human Labeling. [CoRRabs/2501.00192](https://dblp.org/db/journals/corr/corr2501.html#journals/corr/abs-2501-00192) (2025)
- ![](https://dblp.org/img/n.png)

\[i95\]
[Feng Liang](https://dblp.org/pid/54/6821.html), [Haoyu Ma](https://dblp.org/pid/144/1634.html), [Zecheng He](https://dblp.org/pid/203/5675.html), [Tingbo Hou](https://dblp.org/pid/35/3986.html), [Ji Hou](https://dblp.org/pid/152/4311.html), [Kunpeng Li](https://dblp.org/pid/38/1577.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html), Felix Juefei-Xu, [Samaneh Azadi](https://dblp.org/pid/145/9932.html), [Animesh Sinha](https://dblp.org/pid/289/7538.html), [Peizhao Zhang](https://dblp.org/pid/23/8011.html), [Peter Vajda](https://dblp.org/pid/44/5953.html), [Diana Marculescu](https://dblp.org/pid/59/2715.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Movie Weaver: Tuning-Free Multi-Concept Video Personalization with Anchored Prompts. [CoRRabs/2502.07802](https://dblp.org/db/journals/corr/corr2502.html#journals/corr/abs-2502-07802) (2025)
- ![](https://dblp.org/img/n.png)

\[i94\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), [Xin Luo](https://dblp.org/pid/53/5106.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Xiaojun Jia](https://dblp.org/pid/57/5656.html), [Weikai Miao](https://dblp.org/pid/94/4256.html), [Geguang Pu](https://dblp.org/pid/33/1678.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

Scale-Invariant Adversarial Attack against Arbitrary-scale Super-resolution. [CoRRabs/2503.04385](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-04385) (2025)
- ![](https://dblp.org/img/n.png)

\[i93\]
[Cong Wei](https://dblp.org/pid/224/8508-1.html), [Bo Sun](https://dblp.org/pid/35/892.html), [Haoyu Ma](https://dblp.org/pid/144/1634.html), [Ji Hou](https://dblp.org/pid/152/4311.html), Felix Juefei-Xu, [Zecheng He](https://dblp.org/pid/203/5675.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html), [Luxin Zhang](https://dblp.org/pid/218/7106.html), [Kunpeng Li](https://dblp.org/pid/38/1577.html), [Tingbo Hou](https://dblp.org/pid/35/3986.html), [Animesh Sinha](https://dblp.org/pid/289/7538.html), [Peter Vajda](https://dblp.org/pid/44/5953.html), [Wenhu Chen](https://dblp.org/pid/136/0957.html):

MoCha: Towards Movie-Grade Talking Character Synthesis. [CoRRabs/2503.23307](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-23307) (2025)
- ![](https://dblp.org/img/n.png)

\[i92\]
[Xichen Pan](https://dblp.org/pid/317/0180.html), [Satya Narayan Shukla](https://dblp.org/pid/161/3356.html), [Aashu Singh](https://dblp.org/pid/394/7460.html), [Zhuokai Zhao](https://dblp.org/pid/348/5348.html), [Shlok Kumar Mishra](https://dblp.org/pid/173/6664.html), [Jialiang Wang](https://dblp.org/pid/27/8578-1.html), [Zhiyang Xu](https://dblp.org/pid/267/2280.html), [Jiuhai Chen](https://dblp.org/pid/263/3943.html), [Kunpeng Li](https://dblp.org/pid/38/1577.html), Felix Juefei-Xu, [Ji Hou](https://dblp.org/pid/152/4311.html), [Saining Xie](https://dblp.org/pid/126/0960.html):

Transfer between Modalities with MetaQueries. [CoRRabs/2504.06256](https://dblp.org/db/journals/corr/corr2504.html#journals/corr/abs-2504-06256) (2025)
- ![](https://dblp.org/img/n.png)

\[i91\]
[Kun Wang](https://dblp.org/pid/05/1958-56.html), [Guibin Zhang](https://dblp.org/pid/227/3812.html), [Zhenhong Zhou](https://dblp.org/pid/295/5709.html), [Jiahao Wu](https://dblp.org/pid/203/9539.html), [Miao Yu](https://dblp.org/pid/49/1749.html), [Shiqian Zhao](https://dblp.org/pid/348/9458.html), [Chenlong Yin](https://dblp.org/pid/384/4116.html), [Jinhu Fu](https://dblp.org/pid/343/9545.html), [Yibo Yan](https://dblp.org/pid/194/2701.html), [Hanjun Luo](https://dblp.org/pid/355/1273.html), [Liang Lin](https://dblp.org/pid/84/7019.html), [Zhihao Xu](https://dblp.org/pid/65/3784.html), [Haolang Lu](https://dblp.org/pid/381/0560.html), [Xinye Cao](https://dblp.org/pid/322/9121.html), [Xinyun Zhou](https://dblp.org/pid/44/7544.html), [Weifei Jin](https://dblp.org/pid/377/6691.html), [Fanci Meng](https://dblp.org/pid/400/2444.html), [Junyuan Mao](https://dblp.org/pid/371/2729.html), [Hao Wu](https://dblp.org/pid/72/4250.html), [Minghe Wang](https://dblp.org/pid/84/3647.html), [Fan Zhang](https://dblp.org/pid/21/3626.html), [Junfeng Fang](https://dblp.org/pid/340/7929.html), [Chengwei Liu](https://dblp.org/pid/163/6525.html), [Yifan Zhang](https://dblp.org/pid/57/4707.html), [Qiankun Li](https://dblp.org/pid/228/7339.html), [Chongye Guo](https://dblp.org/pid/161/6616.html), [Yalan Qin](https://dblp.org/pid/284/8225.html), [Yi Ding](https://dblp.org/pid/89/5503-12.html), [Donghai Hong](https://dblp.org/pid/367/7553.html), [Jiaming Ji](https://dblp.org/pid/313/9356.html), [Xinfeng Li](https://dblp.org/pid/04/8388.html), [Yifan Jiang](https://dblp.org/pid/81/7246.html), [Dongxia Wang](https://dblp.org/pid/52/645.html), [Yihao Huang](https://dblp.org/pid/255/5085.html), [Yufei Guo](https://dblp.org/pid/23/2981.html), [Jen-tse Huang](https://dblp.org/pid/317/7026.html), [Yanwei Yue](https://dblp.org/pid/289/8664.html), [Wenke Huang](https://dblp.org/pid/330/1664-3.html), [Guancheng Wan](https://dblp.org/pid/354/1252.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianlin Li](https://dblp.org/pid/137/8830.html), [Lei Bai](https://dblp.org/pid/119/1223-1.html), [Jie Zhang](https://dblp.org/pid/84/6889-73.html), [Qing Guo](https://dblp.org/pid/25/3038.html), [Jingyi Wang](https://dblp.org/pid/18/3178.html), [Tianlong Chen](https://dblp.org/pid/68/10575-1.html), [Joey Tianyi Zhou](https://dblp.org/pid/123/5110.html), [Xiaojun Jia](https://dblp.org/pid/57/5656.html), [Weisong Sun](https://dblp.org/pid/183/2642.html), [Cong Wu](https://dblp.org/pid/30/10768.html), [Jing Chen](https://dblp.org/pid/27/4364.html), [Xuming Hu](https://dblp.org/pid/262/3664.html), [Yiming Li](https://dblp.org/pid/181/2877.html), [Xiao Wang](https://dblp.org/pid/49/67.html), [Ningyu Zhang](https://dblp.org/pid/139/4181-1.html), [Luu Anh Tuan](https://dblp.org/pid/81/8329.html), [Guowen Xu](https://dblp.org/pid/87/10142.html), [Tianwei Zhang](https://dblp.org/pid/77/7902-4.html), [Xingjun Ma](https://dblp.org/pid/195/8270.html), [Xiang Wang](https://dblp.org/pid/31/2864.html), [Bo An](https://dblp.org/pid/42/6178-1.html), [Jun Sun](https://dblp.org/pid/s/JunSun1.html), [Mohit Bansal](https://dblp.org/pid/32/5243.html), [Shirui Pan](https://dblp.org/pid/91/8171.html), [Yuval Elovici](https://dblp.org/pid/38/4086.html), [Bhavya Kailkhura](https://dblp.org/pid/132/8938.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bo Li](https://dblp.org/pid/50/3402.html), [Yaodong Yang](https://dblp.org/pid/170/1496-1.html), [Hongwei Li](https://dblp.org/pid/39/5544.html), [Wenyuan Xu](https://dblp.org/pid/10/3878.html), [Yizhou Sun](https://dblp.org/pid/37/3868.html), [Wei Wang](https://dblp.org/pid/w/WeiWang.html), [Qing Li](https://dblp.org/pid/181/2689.html), [Ke Tang](https://dblp.org/pid/50/3146.html), [Yu-Gang Jiang](https://dblp.org/pid/24/5818.html), Felix Juefei-Xu, [Hui Xiong](https://dblp.org/pid/262/1686-1.html), [Xiaofeng Wang](https://dblp.org/pid/99/2479.html), [Shuicheng Yan](https://dblp.org/pid/y/ShuichengYan.html), [Dacheng Tao](https://dblp.org/pid/46/3391.html), [Philip S. Yu](https://dblp.org/pid/y/PhilipSYu.html), [Qingsong Wen](https://dblp.org/pid/27/561.html), [Yang Liu](https://dblp.org/pid/51/3710-84.html):

A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training and Deployment. [CoRRabs/2504.15585](https://dblp.org/db/journals/corr/corr2504.html#journals/corr/abs-2504-15585) (2025)
- ![](https://dblp.org/img/n.png)

\[i90\]
[Xu Ma](https://dblp.org/pid/77/9370.html), [Peize Sun](https://dblp.org/pid/249/2345.html), [Haoyu Ma](https://dblp.org/pid/144/1634.html), [Hao Tang](https://dblp.org/pid/07/5751.html), [Chih-Yao Ma](https://dblp.org/pid/198/0963.html), [Jialiang Wang](https://dblp.org/pid/27/8578-1.html), [Kunpeng Li](https://dblp.org/pid/38/1577.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html), [Yujun Shi](https://dblp.org/pid/146/4499.html), [Xuan Ju](https://dblp.org/pid/34/8495.html), [Yushi Hu](https://dblp.org/pid/268/5766.html), [Artsiom Sanakoyeu](https://dblp.org/pid/185/0536.html), Felix Juefei-Xu, [Ji Hou](https://dblp.org/pid/152/4311.html), [Junjiao Tian](https://dblp.org/pid/246/3115.html), [Tao Xu](https://dblp.org/pid/96/6771.html), [Tingbo Hou](https://dblp.org/pid/35/3986.html), [Yen-Cheng Liu](https://dblp.org/pid/29/7584.html), [Zecheng He](https://dblp.org/pid/203/5675.html), [Zijian He](https://dblp.org/pid/60/8884.html), [Matt Feiszli](https://dblp.org/pid/182/8255.html), [Peizhao Zhang](https://dblp.org/pid/23/8011.html), [Peter Vajda](https://dblp.org/pid/44/5953.html), [Sam S. Tsai](https://dblp.org/pid/88/704.html), [Yun Fu](https://dblp.org/pid/00/5815.html):

Token-Shuffle: Towards High-Resolution Image Generation with Autoregressive Models. [CoRRabs/2504.17789](https://dblp.org/db/journals/corr/corr2504.html#journals/corr/abs-2504-17789) (2025)
- ![](https://dblp.org/img/n.png)

\[i89\]
[Zonghao Ying](https://dblp.org/pid/302/7374.html), [Siyang Wu](https://dblp.org/pid/159/5536.html), [Run Hao](https://dblp.org/pid/243/0480.html), [Peng Ying](https://dblp.org/pid/167/4741.html), [Shixuan Sun](https://dblp.org/pid/131/9481.html), [Pengyu Chen](https://dblp.org/pid/142/3636.html), [Junze Chen](https://dblp.org/pid/262/5385.html), [Hao Du](https://dblp.org/pid/13/6441.html), [Kaiwen Shen](https://dblp.org/pid/245/2568.html), [Shangkun Wu](https://dblp.org/pid/410/2403.html), [Jiwei Wei](https://dblp.org/pid/31/2031.html), [Shiyuan He](https://dblp.org/pid/146/2829.html), [Yang Yang](https://dblp.org/pid/48/450.html), [Xiaohai Xu](https://dblp.org/pid/229/1423.html), [Ke Ma](https://dblp.org/pid/98/2014-1.html), [Qianqian Xu](https://dblp.org/pid/07/7627-1.html), [Qingming Huang](https://dblp.org/pid/68/4388.html), [Shi Lin](https://dblp.org/pid/41/7692.html), [Xun Wang](https://dblp.org/pid/82/1331.html), [Changting Lin](https://dblp.org/pid/231/4918.html), [Meng Han](https://dblp.org/pid/91/9124.html), [Yilei Jiang](https://dblp.org/pid/297/8930.html), [Siqi Lai](https://dblp.org/pid/314/0655.html), [Yaozhi Zheng](https://dblp.org/pid/410/2408.html), [Yifei Song](https://dblp.org/pid/284/3356.html), [Xiangyu Yue](https://dblp.org/pid/207/7518.html), [Zonglei Jing](https://dblp.org/pid/384/5611.html), [Tianyuan Zhang](https://dblp.org/pid/145/6286-4.html), [Zhilei Zhu](https://dblp.org/pid/344/7849.html), [Aishan Liu](https://dblp.org/pid/177/5658.html), [Jiakai Wang](https://dblp.org/pid/202/9216.html), [Siyuan Liang](https://dblp.org/pid/205/8767.html), [Xianglong Kong](https://dblp.org/pid/44/2995.html), [Hainan Li](https://dblp.org/pid/256/6812.html), [Junjie Mu](https://dblp.org/pid/283/1108.html), [Haotong Qin](https://dblp.org/pid/262/3626.html), [Yue Yu](https://dblp.org/pid/55/2008.html), [Lei Chen](https://dblp.org/pid/09/3666.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Xinyun Chen](https://dblp.org/pid/03/8495.html), [Yew Soon Ong](https://dblp.org/pid/64/4136.html), [Xianglong Liu](https://dblp.org/pid/55/7901-1.html), [Dawn Song](https://dblp.org/pid/s/DXSong.html), [Alan L. Yuille](https://dblp.org/pid/y/AlanLYuille.html), [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Dacheng Tao](https://dblp.org/pid/46/3391.html):

Pushing the Limits of Safety: A Technical Report on the ATLAS Challenge 2025. [CoRRabs/2506.12430](https://dblp.org/db/journals/corr/corr2506.html#journals/corr/abs-2506-12430) (2025)
- ![](https://dblp.org/img/n.png)

\[i88\]
[Mengyi Shan](https://dblp.org/pid/253/9346.html), [Zecheng He](https://dblp.org/pid/203/5675.html), [Haoyu Ma](https://dblp.org/pid/144/1634.html), Felix Juefei-Xu, [Peizhao Zhang](https://dblp.org/pid/23/8011.html), [Tingbo Hou](https://dblp.org/pid/35/3986.html), [Ching-Yao Chuang](https://dblp.org/pid/190/7522.html):

Populate-A-Scene: Affordance-Aware Human Video Generation. [CoRRabs/2507.00334](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-00334) (2025)
- ![](https://dblp.org/img/n.png)

\[i87\]
[Zeqi Gu](https://dblp.org/pid/230/4614.html), [Markos Georgopoulos](https://dblp.org/pid/197/6876.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html), [Marjan Ghazvininejad](https://dblp.org/pid/50/10813.html), [Chu Wang](https://dblp.org/pid/45/1543.html), Felix Juefei-Xu, [Kunpeng Li](https://dblp.org/pid/38/1577.html), [Yujun Shi](https://dblp.org/pid/146/4499.html), [Zecheng He](https://dblp.org/pid/203/5675.html), [Zijian He](https://dblp.org/pid/60/8884.html), [Jiawei Zhou](https://dblp.org/pid/126/4991.html), [Abe Davis](https://dblp.org/pid/117/4799.html), [Jialiang Wang](https://dblp.org/pid/27/8578-1.html):

Improving Chain-of-Thought Efficiency for Autoregressive Image Generation. [CoRRabs/2510.05593](https://dblp.org/db/journals/corr/corr2510.html#journals/corr/abs-2510-05593) (2025)
- ![](https://dblp.org/img/n.png)

\[i86\]
[Jiayi Zhu](https://dblp.org/pid/53/1649-2.html), [Yihao Huang](https://dblp.org/pid/255/5085.html), [Yue Cao](https://dblp.org/pid/74/5570.html), [Xiaojun Jia](https://dblp.org/pid/57/5656.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Geguang Pu](https://dblp.org/pid/33/1678.html), [Bin Wang](https://dblp.org/pid/13/1898.html):

Beyond Pixels: Semantic-aware Typographic Attack for Geo-Privacy Protection. [CoRRabs/2511.12575](https://dblp.org/db/journals/corr/corr2511.html#journals/corr/abs-2511-12575) (2025)
- ![](https://dblp.org/img/n.png)

\[i85\]
[Long Lian](https://dblp.org/pid/276/0012.html), [Sida Wang](https://dblp.org/pid/153/9609.html), Felix Juefei-Xu, [Tsu-Jui Fu](https://dblp.org/pid/218/5366.html), [Xiuyu Li](https://dblp.org/pid/279/5847.html), [Adam Yala](https://dblp.org/pid/177/9396.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), [Alane Suhr](https://dblp.org/pid/203/9306.html), [Yuandong Tian](https://dblp.org/pid/t/YuandongTian.html), [Xi Victoria Lin](https://dblp.org/pid/215/5264.html):

ThreadWeaver: Adaptive Threading for Efficient Parallel Reasoning in Language Models. [CoRRabs/2512.07843](https://dblp.org/db/journals/corr/corr2512.html#journals/corr/abs-2512-07843) (2025)
- ![](https://dblp.org/img/n.png)

\[i84\]
[Han Lin](https://dblp.org/pid/63/6173.html), [Xichen Pan](https://dblp.org/pid/317/0180.html), [Ziqi Huang](https://dblp.org/pid/159/4681.html), [Ji Hou](https://dblp.org/pid/152/4311.html), [Jialiang Wang](https://dblp.org/pid/27/8578-1.html), [Weifeng Chen](https://dblp.org/pid/74/5429.html), [Zecheng He](https://dblp.org/pid/203/5675.html), Felix Juefei-Xu, [Junzhe Sun](https://dblp.org/pid/389/2226.html), [Zhipeng Fan](https://dblp.org/pid/228/6404.html), [Ali K. Thabet](https://dblp.org/pid/161/1812.html), [Mohit Bansal](https://dblp.org/pid/32/5243.html), [Chu Wang](https://dblp.org/pid/45/1543.html):

Exploring MLLM-Diffusion Information Transfer with MetaCanvas. [CoRRabs/2512.11464](https://dblp.org/db/journals/corr/corr2512.html#journals/corr/abs-2512-11464) (2025)
- ![](https://dblp.org/img/n.png)

\[i83\]
[Yuanhao Cai](https://dblp.org/pid/260/1004.html), [Kunpeng Li](https://dblp.org/pid/38/1577.html), [Menglin Jia](https://dblp.org/pid/228/8465.html), [Jialiang Wang](https://dblp.org/pid/27/8578-1.html), [Junzhe Sun](https://dblp.org/pid/389/2226.html), [Feng Liang](https://dblp.org/pid/54/6821.html), [Weifeng Chen](https://dblp.org/pid/74/5429.html), Felix Juefei-Xu, [Chu Wang](https://dblp.org/pid/45/1543.html), [Ali K. Thabet](https://dblp.org/pid/161/1812.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html), [Xuan Ju](https://dblp.org/pid/34/8495.html), [Alan L. Yuille](https://dblp.org/pid/y/AlanLYuille.html), [Ji Hou](https://dblp.org/pid/152/4311.html):

PhyGDPO: Physics-Aware Groupwise Direct Preference Optimization for Physically Consistent Text-to-Video Generation. [CoRRabs/2512.24551](https://dblp.org/db/journals/corr/corr2512.html#journals/corr/abs-2512-24551) (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j21\]
[Yihao Huang](https://dblp.org/pid/255/5085.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Geguang Pu](https://dblp.org/pid/33/1678.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Dodging DeepFake Detection via Implicit Spatial-Domain Notch Filtering. [IEEE Trans. Circuits Syst. Video Technol.34(8)](https://dblp.org/db/journals/tcsv/tcsv34.html#journals/tcsv/HuangJGLP24): 6949-6962 (2024)
- ![](https://dblp.org/img/n.png)

\[j20\]
[Yihao Huang](https://dblp.org/pid/255/5085.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Ming Hu](https://dblp.org/pid/82/378-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaojun Jia](https://dblp.org/pid/57/5656.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaochun Cao](https://dblp.org/pid/39/3695.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Geguang Pu](https://dblp.org/pid/33/1678.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Texture Re-Scalable Universal Adversarial Perturbation. [IEEE Trans. Inf. Forensics Secur.19](https://dblp.org/db/journals/tifs/tifs19.html#journals/tifs/HuangGJHJCPL24): 8291-8305 (2024)
- ![](https://dblp.org/img/n.png)

\[j19\]
[Qian Zhang](https://dblp.org/pid/04/2024-51.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ruijun Gao](https://dblp.org/pid/247/5683.html), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Hongkai Yu](https://dblp.org/pid/150/6670.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Adversarial Relighting Against Face Recognition. [IEEE Trans. Inf. Forensics Secur.19](https://dblp.org/db/journals/tifs/tifs19.html#journals/tifs/ZhangGGJYF24): 9145-9157 (2024)
- ![](https://dblp.org/img/n.png)

\[j18\]
[Alireza Esmaeilzehi](https://dblp.org/pid/198/7073.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Seyed Matin Tavakoli Afshari](https://dblp.org/pid/407/9056.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

MIPE: Towards Cleaning the Datasets of Autonomous Driving Systems Using Multi-Modal Information Processing and Confident Learning. [IEEE Trans. Intell. Veh.9(9)](https://dblp.org/db/journals/tiv/tiv9.html#journals/tiv/EsmaeilzehiAGJM24): 5361-5376 (2024)
- ![](https://dblp.org/img/n.png)

\[j17\]
[Yihao Huang](https://dblp.org/pid/255/5085.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Geguang Pu](https://dblp.org/pid/33/1678.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Natural & Adversarial Bokeh Rendering via Circle-of-Confusion Predictive Network. [IEEE Trans. Multim.26](https://dblp.org/db/journals/tmm/tmm26.html#journals/tmm/HuangJGPL24): 5729-5740 (2024)
- ![](https://dblp.org/img/n.png)

\[j16\]
[Da Song](https://dblp.org/pid/222/6729.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xuan Xie](https://dblp.org/pid/22/10184-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiayang Song](https://dblp.org/pid/182/7194.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Derui Zhu](https://dblp.org/pid/203/9320.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuheng Huang](https://dblp.org/pid/01/6508-4.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

LUNA: A Model-Based Universal Analysis Framework for Large Language Models. [IEEE Trans. Software Eng.50(7)](https://dblp.org/db/journals/tse/tse50.html#journals/tse/SongXSZHJM24): 1921-1948 (2024)
- ![](https://dblp.org/img/n.png)

\[c64\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Jie Zhang](https://dblp.org/pid/84/6889-2.html), [Yutong Wu](https://dblp.org/pid/312/5805.html), [Ming Hu](https://dblp.org/pid/82/378-3.html), [Tianlin Li](https://dblp.org/pid/137/8830.html), [Geguang Pu](https://dblp.org/pid/33/1678.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Personalization as a Shortcut for Few-Shot Backdoor Attack against Text-to-Image Diffusion Models. [AAAI2024](https://dblp.org/db/conf/aaai/aaai2024.html#conf/aaai/0001JGZ00LPL24): 21169-21178
- ![](https://dblp.org/img/n.png)

\[c63\]
[Jiayi Zhu](https://dblp.org/pid/53/1649-2.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Yihao Huang](https://dblp.org/pid/255/5085.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

Cosalpure: Learning Concept from Group Images for Robust Co-Saliency Detection. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/00020JH0P24): 3669-3678
- ![](https://dblp.org/img/n.png)

\[c62\]
[Jinlong Li](https://dblp.org/pid/34/1296.html), [Baolu Li](https://dblp.org/pid/352/4564.html), [Zhengzhong Tu](https://dblp.org/pid/218/1473.html), [Xinyu Liu](https://dblp.org/pid/98/738-9.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Runsheng Xu](https://dblp.org/pid/214/1446.html), [Hongkai Yu](https://dblp.org/pid/150/6670.html):

Light the Night: A Multi-Condition Diffusion Framework for Unpaired Low-Light Enhancement in Autonomous Driving. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/LiLTL0JXY24): 15205-15215
- ![](https://dblp.org/img/n.png)

\[c61\]
[Di Yang](https://dblp.org/pid/29/5427.html), [Yihao Huang](https://dblp.org/pid/255/5085.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Ming Hu](https://dblp.org/pid/82/378-3.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Geguang Pu](https://dblp.org/pid/33/1678.html):

Architecture-Agnostic Iterative Black-Box Certified Defense Against Adversarial Patches. [ICASSP2024](https://dblp.org/db/conf/icassp/icassp2024.html#conf/icassp/Yang00J0LP24): 5985-5989
- ![](https://dblp.org/img/n.png)

\[c60\]
[Jianlang Chen](https://dblp.org/pid/307/5450.html), [Xuhong Ren](https://dblp.org/pid/138/4258.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Di Lin](https://dblp.org/pid/20/3191-2.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

LRR: Language-Driven Resamplable Continuous Representation against Adversarial Tracking Attacks. [ICLR2024](https://dblp.org/db/conf/iclr/iclr2024.html#conf/iclr/ChenR0J000024)
- ![](https://dblp.org/img/n.png)

\[c59\]
[Jinlong Li](https://dblp.org/pid/34/1296.html), [Baolu Li](https://dblp.org/pid/352/4564.html), [Xinyu Liu](https://dblp.org/pid/98/738-9.html), [Jianwu Fang](https://dblp.org/pid/142/0412.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Hongkai Yu](https://dblp.org/pid/150/6670.html):

AdvGPS: Adversarial GPS for Multi-Agent Perception Attack. [ICRA2024](https://dblp.org/db/conf/icra/icra2024.html#conf/icra/LiLLFJ0Y24): 18421-18427
- ![](https://dblp.org/img/n.png)

\[c58\]
[Lan Fu](https://dblp.org/pid/265/9476.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Hongkai Yu](https://dblp.org/pid/150/6670.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Song Wang](https://dblp.org/pid/62/3151-2.html):

Benchmarking Shadow Removal for Facial Landmark Detection. [CAI2024](https://dblp.org/db/conf/ieeecai/ieeecai2024.html#conf/ieeecai/FuGJYLFW24): 265-271
- ![](https://dblp.org/img/n.png)

\[i82\]
[Jinlong Li](https://dblp.org/pid/34/1296.html), [Baolu Li](https://dblp.org/pid/352/4564.html), [Xinyu Liu](https://dblp.org/pid/98/738-9.html), [Jianwu Fang](https://dblp.org/pid/142/0412.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Hongkai Yu](https://dblp.org/pid/150/6670.html):

AdvGPS: Adversarial GPS for Multi-Agent Perception Attack. [CoRRabs/2401.17499](https://dblp.org/db/journals/corr/corr2401.html#journals/corr/abs-2401-17499) (2024)
- ![](https://dblp.org/img/n.png)

\[i81\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), [Kaiyuan Yu](https://dblp.org/pid/367/9370.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Xiaojun Jia](https://dblp.org/pid/57/5656.html), [Tianlin Li](https://dblp.org/pid/137/8830.html), [Geguang Pu](https://dblp.org/pid/33/1678.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Improving Robustness of LiDAR-Camera Fusion Model against Weather Corruption from Fusion Strategy Perspective. [CoRRabs/2402.02738](https://dblp.org/db/journals/corr/corr2402.html#journals/corr/abs-2402-02738) (2024)
- ![](https://dblp.org/img/n.png)

\[i80\]
[Jiayi Zhu](https://dblp.org/pid/53/1649-2.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Yihao Huang](https://dblp.org/pid/255/5085.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

CosalPure: Learning Concept from Group Images for Robust Co-Saliency Detection. [CoRRabs/2403.18554](https://dblp.org/db/journals/corr/corr2403.html#journals/corr/abs-2403-18554) (2024)
- ![](https://dblp.org/img/n.png)

\[i79\]
[Jinlong Li](https://dblp.org/pid/34/1296.html), [Baolu Li](https://dblp.org/pid/352/4564.html), [Zhengzhong Tu](https://dblp.org/pid/218/1473.html), [Xinyu Liu](https://dblp.org/pid/98/738-9.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Runsheng Xu](https://dblp.org/pid/214/1446.html), [Hongkai Yu](https://dblp.org/pid/150/6670.html):

Light the Night: A Multi-Condition Diffusion Framework for Unpaired Low-Light Enhancement in Autonomous Driving. [CoRRabs/2404.04804](https://dblp.org/db/journals/corr/corr2404.html#journals/corr/abs-2404-04804) (2024)
- ![](https://dblp.org/img/n.png)

\[i78\]
[Jianlang Chen](https://dblp.org/pid/307/5450.html), [Xuhong Ren](https://dblp.org/pid/138/4258.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Di Lin](https://dblp.org/pid/20/3191-2.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

LRR: Language-Driven Resamplable Continuous Representation against Adversarial Tracking Attacks. [CoRRabs/2404.06247](https://dblp.org/db/journals/corr/corr2404.html#journals/corr/abs-2404-06247) (2024)
- ![](https://dblp.org/img/n.png)

\[i77\]
[Yuzhu Cai](https://dblp.org/pid/375/7444.html), [Sheng Yin](https://dblp.org/pid/52/2662.html), [Yuxi Wei](https://dblp.org/pid/323/4932.html), [Chenxin Xu](https://dblp.org/pid/281/7263.html), [Weibo Mao](https://dblp.org/pid/44/4166.html), Felix Juefei-Xu, [Siheng Chen](https://dblp.org/pid/136/4945.html), [Yanfeng Wang](https://dblp.org/pid/55/5407-1.html):

Ethical-Lens: Curbing Malicious Usages of Open-Source Text-to-Image Models. [CoRRabs/2404.12104](https://dblp.org/db/journals/corr/corr2404.html#journals/corr/abs-2404-12104) (2024)
- ![](https://dblp.org/img/n.png)

\[i76\]
[Bertie Vidgen](https://dblp.org/pid/175/1517.html), [Adarsh Agrawal](https://dblp.org/pid/375/6968.html), [Ahmed M. Ahmed](https://dblp.org/pid/294/5028.html), [Victor Akinwande](https://dblp.org/pid/211/6825.html), [Namir Al-Nuaimi](https://dblp.org/pid/375/6416.html), [Najla Alfaraj](https://dblp.org/pid/10/8405.html), [Elie Alhajjar](https://dblp.org/pid/259/6812.html), [Lora Aroyo](https://dblp.org/pid/42/6100.html), [Trupti Bavalatti](https://dblp.org/pid/375/7726.html), [Borhane Blili-Hamelin](https://dblp.org/pid/329/1972.html), [Kurt Bollacker](https://dblp.org/pid/64/4571.html), [Rishi Bomassani](https://dblp.org/pid/375/6407.html), [Marisa Ferrara Boston](https://dblp.org/pid/24/8160.html), [Siméon Campos](https://dblp.org/pid/375/6457.html), [Kal Chakra](https://dblp.org/pid/375/7683.html), [Canyu Chen](https://dblp.org/pid/319/2330.html), [Cody Coleman](https://dblp.org/pid/222/1849.html), [Zacharie Delpierre Coudert](https://dblp.org/pid/375/6531.html), [Leon Derczynski](https://dblp.org/pid/66/8157.html), [Debojyoti Dutta](https://dblp.org/pid/96/2340.html), [Ian Eisenberg](https://dblp.org/pid/324/8716.html), [James Ezick](https://dblp.org/pid/317/2495.html), [Heather Frase](https://dblp.org/pid/348/5691.html), [Brian Fuller](https://dblp.org/pid/50/6951.html), [Ram Gandikota](https://dblp.org/pid/375/6649.html), [Agasthya Gangavarapu](https://dblp.org/pid/337/8985.html), [Ananya Gangavarapu](https://dblp.org/pid/275/3568.html), [James Gealy](https://dblp.org/pid/375/6060.html), [Rajat Ghosh](https://dblp.org/pid/199/6924.html), [James Goel](https://dblp.org/pid/229/5357.html), [Usman Gohar](https://dblp.org/pid/336/1779.html), [Subhra S. Goswami](https://dblp.org/pid/272/0914.html), [Scott A. Hale](https://dblp.org/pid/32/10840.html), [Wiebke Hutiri](https://dblp.org/pid/258/1137.html), [Joseph Marvin Imperial](https://dblp.org/pid/246/4647.html), [Surgan Jandial](https://dblp.org/pid/246/4915.html), [Nick Judd](https://dblp.org/pid/332/0864.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu, [Foutse Khomh](https://dblp.org/pid/32/147.html), [Bhavya Kailkhura](https://dblp.org/pid/132/8938.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hannah Rose Kirk](https://dblp.org/pid/284/9434.html), [Kevin Klyman](https://dblp.org/pid/359/3360.html), [Chris Knotz](https://dblp.org/pid/375/7389.html), [Michael Kuchnik](https://dblp.org/pid/228/8029.html), [Shachi H. Kumar](https://dblp.org/pid/164/7309.html), [Chris Lengerich](https://dblp.org/pid/147/4826.html), [Bo Li](https://dblp.org/pid/50/3402-26.html), [Zeyi Liao](https://dblp.org/pid/254/0197.html), [Eileen Peters Long](https://dblp.org/pid/144/1945.html), [Victor Lu](https://dblp.org/pid/77/8356.html), [Yifan Mai](https://dblp.org/pid/156/8369-1.html), [Priyanka Mary Mammen](https://dblp.org/pid/217/6913.html), [Kelvin N. Manyeki](https://dblp.org/pid/401/7765.html), [Sean McGregor](https://dblp.org/pid/173/7861.html), [Virendra Mehta](https://dblp.org/pid/303/4829.html), [Shafee Mohammed](https://dblp.org/pid/212/4553.html), [Emanuel Moss](https://dblp.org/pid/257/8114.html), [Lama Nachman](https://dblp.org/pid/65/3345.html), [Dinesh Jinenhally Naganna](https://dblp.org/pid/375/6717.html), [Amin Nikanjam](https://dblp.org/pid/42/1656.html), [Besmira Nushi](https://dblp.org/pid/117/4927.html), [Luis Oala](https://dblp.org/pid/261/9215.html), [Iftach Orr](https://dblp.org/pid/375/6721.html), [Alicia Parrish](https://dblp.org/pid/248/7544.html), [Cigdem Patlak](https://dblp.org/pid/375/6217.html), [William Pietri](https://dblp.org/pid/04/1943.html), [Forough Poursabzi-Sangdeh](https://dblp.org/pid/165/0744.html), [Eleonora Presani](https://dblp.org/pid/227/6323.html), [Fabrizio Puletti](https://dblp.org/pid/375/7077.html), [Paul Röttger](https://dblp.org/pid/282/4243.html), [Saurav Sahay](https://dblp.org/pid/18/4070.html), [Tim Santos](https://dblp.org/pid/334/2365.html), [Nino Scherrer](https://dblp.org/pid/295/0198.html), [Alice Schoenauer Sebag](https://dblp.org/pid/164/0807.html), [Patrick Schramowski](https://dblp.org/pid/217/1650.html), [Abolfazl Shahbazi](https://dblp.org/pid/375/6646.html), [Vin Sharma](https://dblp.org/pid/227/2446.html), [Xudong Shen](https://dblp.org/pid/240/0569.html), [Vamsi Sistla](https://dblp.org/pid/375/6335.html), [Leonard Tang](https://dblp.org/pid/306/7940.html), [Davide Testuggine](https://dblp.org/pid/248/8282.html), [Vithursan Thangarasa](https://dblp.org/pid/223/9965.html), [Elizabeth Anne Watkins](https://dblp.org/pid/196/3030.html), [Rebecca Weiss](https://dblp.org/pid/159/0930.html), [Chris Welty](https://dblp.org/pid/w/CAWelty.html), [Tyler Wilbers](https://dblp.org/pid/375/6232.html), [Adina Williams](https://dblp.org/pid/199/2104.html), [Carole-Jean Wu](https://dblp.org/pid/26/9655.html), [Poonam Yadav](https://dblp.org/pid/79/9996.html), [Xianjun Yang](https://dblp.org/pid/37/10237.html), [Yi Zeng](https://dblp.org/pid/75/148-5.html), [Wenhui Zhang](https://dblp.org/pid/82/13.html), [Fedor Zhdanov](https://dblp.org/pid/83/904.html), [Jiacheng Zhu](https://dblp.org/pid/40/10195.html), [Percy Liang](https://dblp.org/pid/04/1701.html), [Peter Mattson](https://dblp.org/pid/47/739.html), [Joaquin Vanschoren](https://dblp.org/pid/85/5045.html):

Introducing v0.5 of the AI Safety Benchmark from MLCommons. [CoRRabs/2404.12241](https://dblp.org/db/journals/corr/corr2404.html#journals/corr/abs-2404-12241) (2024)
- ![](https://dblp.org/img/n.png)

\[i75\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), [Chong Wang](https://dblp.org/pid/72/1334-13.html), [Xiaojun Jia](https://dblp.org/pid/57/5656.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Jian Zhang](https://dblp.org/pid/07/314-87.html), [Geguang Pu](https://dblp.org/pid/33/1678.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Semantic-guided Prompt Organization for Universal Goal Hijacking against LLMs. [CoRRabs/2405.14189](https://dblp.org/db/journals/corr/corr2405.html#journals/corr/abs-2405-14189) (2024)
- ![](https://dblp.org/img/n.png)

\[i74\]
[Di Yang](https://dblp.org/pid/29/5427.html), [Yihao Huang](https://dblp.org/pid/255/5085.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Xiaojun Jia](https://dblp.org/pid/57/5656.html), [Run Wang](https://dblp.org/pid/95/8501-1.html), [Geguang Pu](https://dblp.org/pid/33/1678.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Text Modality Oriented Image Feature Extraction for Detecting Diffusion-based DeepFake. [CoRRabs/2405.18071](https://dblp.org/db/journals/corr/corr2405.html#journals/corr/abs-2405-18071) (2024)
- ![](https://dblp.org/img/n.png)

\[i73\]
[Xinxi Zhang](https://dblp.org/pid/246/3433.html), [Song Wen](https://dblp.org/pid/119/9492-1.html), [Ligong Han](https://dblp.org/pid/187/1675.html), Felix Juefei-Xu, [Akash Srivastava](https://dblp.org/pid/24/9528.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hao Wang](https://dblp.org/pid/w/HaoWang-14.html), [Molei Tao](https://dblp.org/pid/56/9263.html), [Dimitris N. Metaxas](https://dblp.org/pid/m/DNMetaxas.html):

Spectrum-Aware Parameter Efficient Fine-Tuning for Diffusion Models. [CoRRabs/2405.21050](https://dblp.org/db/journals/corr/corr2405.html#journals/corr/abs-2405-21050) (2024)
- ![](https://dblp.org/img/n.png)

\[i72\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Ming Hu](https://dblp.org/pid/82/378-3.html), [Xiaojun Jia](https://dblp.org/pid/57/5656.html), [Xiaochun Cao](https://dblp.org/pid/39/3695.html), [Geguang Pu](https://dblp.org/pid/33/1678.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Texture Re-scalable Universal Adversarial Perturbation. [CoRRabs/2406.06089](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-06089) (2024)
- ![](https://dblp.org/img/n.png)

\[i71\]
[Sanbao Su](https://dblp.org/pid/221/2885.html), [Nuo Chen](https://dblp.org/pid/135/5622-3.html), Felix Juefei-Xu, [Chen Feng](https://dblp.org/pid/01/161-2.html), [Fei Miao](https://dblp.org/pid/143/6002.html):

ɑ-SSC: Uncertainty-Aware Camera-based 3D Semantic Scene Completion. [CoRRabs/2406.11021](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-11021) (2024)
- ![](https://dblp.org/img/n.png)

\[i70\]
[Qingcheng Zeng](https://dblp.org/pid/84/1451.html), [Mingyu Jin](https://dblp.org/pid/215/7601.html), [Qinkai Yu](https://dblp.org/pid/350/0275.html), [Zhenting Wang](https://dblp.org/pid/263/4521.html), [Wenyue Hua](https://dblp.org/pid/278/7993.html), [Zihao Zhou](https://dblp.org/pid/139/5953.html), [Guangyan Sun](https://dblp.org/pid/67/9556.html), [Yanda Meng](https://dblp.org/pid/275/6822.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shiqing Ma](https://dblp.org/pid/172/8745.html), [Qifan Wang](https://dblp.org/pid/33/8610-1.html), Felix Juefei-Xu, [Kaize Ding](https://dblp.org/pid/234/6878.html), [Fan Yang](https://dblp.org/pid/29/3081-23.html), [Ruixiang Tang](https://dblp.org/pid/239/1928.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yongfeng Zhang](https://dblp.org/pid/82/7829-3.html):

Uncertainty is Fragile: Manipulating Uncertainty in Large Language Models. [CoRRabs/2407.11282](https://dblp.org/db/journals/corr/corr2407.html#journals/corr/abs-2407-11282) (2024)
- ![](https://dblp.org/img/n.png)

\[i69\]
[Yuheng Huang](https://dblp.org/pid/01/6508-4.html), [Jiayang Song](https://dblp.org/pid/182/7194.html), [Qiang Hu](https://dblp.org/pid/93/5629.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html):

Active Testing of Large Language Model via Multi-Stage Sampling. [CoRRabs/2408.03573](https://dblp.org/db/journals/corr/corr2408.html#journals/corr/abs-2408-03573) (2024)
- ![](https://dblp.org/img/n.png)

\[i68\]
[Xuan Xie](https://dblp.org/pid/22/10184-1.html), [Jiayang Song](https://dblp.org/pid/182/7194.html), [Yuheng Huang](https://dblp.org/pid/01/6508-4.html), [Da Song](https://dblp.org/pid/222/6729.html), [Fuyuan Zhang](https://dblp.org/pid/08/7637.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html):

LeCov: Multi-level Testing Criteria for Large Language Models. [CoRRabs/2408.10474](https://dblp.org/db/journals/corr/corr2408.html#journals/corr/abs-2408-10474) (2024)
- ![](https://dblp.org/img/n.png)

\[i67\]
[Zecheng He](https://dblp.org/pid/203/5675.html), [Bo Sun](https://dblp.org/pid/35/892.html), Felix Juefei-Xu, [Haoyu Ma](https://dblp.org/pid/144/1634.html), [Ankit Ramchandani](https://dblp.org/pid/257/3893.html), [Vincent Cheung](https://dblp.org/pid/47/5789.html), [Siddharth Shah](https://dblp.org/pid/12/10521.html), [Anmol Kalia](https://dblp.org/pid/337/2585.html), [Harihar Subramanyam](https://dblp.org/pid/166/8374.html), [Alireza Zareian](https://dblp.org/pid/154/6427.html), [Li Chen](https://dblp.org/pid/181/2847.html), [Ankit Jain](https://dblp.org/pid/37/7907.html), [Ning Zhang](https://dblp.org/pid/181/2597.html), [Peizhao Zhang](https://dblp.org/pid/23/8011.html), [Roshan Sumbaly](https://dblp.org/pid/116/5160.html), [Peter Vajda](https://dblp.org/pid/44/5953.html), [Animesh Sinha](https://dblp.org/pid/289/7538.html):

Imagine yourself: Tuning-Free Personalized Image Generation. [CoRRabs/2409.13346](https://dblp.org/db/journals/corr/corr2409.html#journals/corr/abs-2409-13346) (2024)
- ![](https://dblp.org/img/n.png)

\[i66\]
[Christina Zhang](https://dblp.org/pid/41/9457.html), [Simran Motwani](https://dblp.org/pid/358/3864.html), [Matthew Yu](https://dblp.org/pid/262/6275.html), [Ji Hou](https://dblp.org/pid/152/4311.html), Felix Juefei-Xu, [Sam S. Tsai](https://dblp.org/pid/88/704.html), [Peter Vajda](https://dblp.org/pid/44/5953.html), [Zijian He](https://dblp.org/pid/60/8884.html), [Jialiang Wang](https://dblp.org/pid/27/8578-1.html):

Pixel-Space Post-Training of Latent Diffusion Models. [CoRRabs/2409.17565](https://dblp.org/db/journals/corr/corr2409.html#journals/corr/abs-2409-17565) (2024)
- ![](https://dblp.org/img/n.png)

\[i65\]
[Xiaoxiao He](https://dblp.org/pid/22/9737.html), [Ligong Han](https://dblp.org/pid/187/1675.html), [Quan Dao](https://dblp.org/pid/334/7610.html), [Song Wen](https://dblp.org/pid/119/9492-1.html), [Minhao Bai](https://dblp.org/pid/361/3951.html), [Di Liu](https://dblp.org/pid/15/1777-3.html), [Han Zhang](https://dblp.org/pid/26/4189-10.html), [Martin Renqiang Min](https://dblp.org/pid/29/7048.html), Felix Juefei-Xu, [Chaowei Tan](https://dblp.org/pid/155/3101.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Kang Li](https://dblp.org/pid/l/KangLi.html), [Hongdong Li](https://dblp.org/pid/59/4859.html), [Junzhou Huang](https://dblp.org/pid/22/1170.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Faez Ahmed](https://dblp.org/pid/45/10603.html), [Akash Srivastava](https://dblp.org/pid/24/9528.html), [Dimitris N. Metaxas](https://dblp.org/pid/m/DNMetaxas.html):

DICE: Discrete Inversion Enabling Controllable Editing for Multinomial Diffusion and Masked Generative Models. [CoRRabs/2410.08207](https://dblp.org/db/journals/corr/corr2410.html#journals/corr/abs-2410-08207) (2024)
- ![](https://dblp.org/img/n.png)

\[i64\]
[Shiyu Zhao](https://dblp.org/pid/120/7474-1.html), [Zhenting Wang](https://dblp.org/pid/263/4521.html), Felix Juefei-Xu, [Xide Xia](https://dblp.org/pid/172/0129.html), [Miao Liu](https://dblp.org/pid/60/6348-7.html), [Xiaofang Wang](https://dblp.org/pid/58/2390.html), [Mingfu Liang](https://dblp.org/pid/241/9790.html), [Ning Zhang](https://dblp.org/pid/181/2597.html), [Dimitris N. Metaxas](https://dblp.org/pid/m/DNMetaxas.html), [Licheng Yu](https://dblp.org/pid/32/10805.html):

Accelerating Multimodal Large Language Models by Searching Optimal Vision Token Reduction. [CoRRabs/2412.00556](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-00556) (2024)
- ![](https://dblp.org/img/n.png)

\[i63\]
[Bolin Lai](https://dblp.org/pid/250/6136.html), Felix Juefei-Xu, [Miao Liu](https://dblp.org/pid/60/6348-7.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html), [Nikhil Mehta](https://dblp.org/pid/89/7487-2.html), [Chenguang Zhu](https://dblp.org/pid/48/7536.html), [Zeyi Huang](https://dblp.org/pid/142/5094.html), [James M. Rehg](https://dblp.org/pid/r/JMRehg.html), [Sangmin Lee](https://dblp.org/pid/68/311-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ning Zhang](https://dblp.org/pid/181/2597.html), [Tong Xiao](https://dblp.org/pid/05/5091-3.html):

Unleashing In-context Learning of Autoregressive Models for Few-shot Image Manipulation. [CoRRabs/2412.01027](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-01027) (2024)
- ![](https://dblp.org/img/n.png)

\[i62\]
[Hongjie Wang](https://dblp.org/pid/65/7565-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chih-Yao Ma](https://dblp.org/pid/198/0963.html), [Yen-Cheng Liu](https://dblp.org/pid/29/7584.html), [Ji Hou](https://dblp.org/pid/152/4311.html), [Tao Xu](https://dblp.org/pid/96/6771.html), [Jialiang Wang](https://dblp.org/pid/27/8578-1.html), Felix Juefei-Xu, [Yaqiao Luo](https://dblp.org/pid/150/6230.html), [Peizhao Zhang](https://dblp.org/pid/23/8011.html), [Tingbo Hou](https://dblp.org/pid/35/3986.html), [Peter Vajda](https://dblp.org/pid/44/5953.html), [Niraj K. Jha](https://dblp.org/pid/j/NirajKJha.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html):

LinGen: Towards High-Resolution Minute-Length Text-to-Video Generation with Linear Computational Complexity. [CoRRabs/2412.09856](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-09856) (2024)
- ![](https://dblp.org/img/n.png)

\[i61\]
[Orr Zohar](https://dblp.org/pid/335/1624.html), [Xiaohan Wang](https://dblp.org/pid/73/1307.html), [Yann Dubois](https://dblp.org/pid/198/7527.html), [Nikhil Mehta](https://dblp.org/pid/89/7487-2.html), [Tong Xiao](https://dblp.org/pid/05/5091-3.html), [Philippe Hansen-Estruch](https://dblp.org/pid/289/6990.html), [Licheng Yu](https://dblp.org/pid/32/10805.html), [Xiaofang Wang](https://dblp.org/pid/58/2390.html), Felix Juefei-Xu, [Ning Zhang](https://dblp.org/pid/181/2597.html), [Serena Yeung-Levy](https://dblp.org/pid/147/5023.html), [Xide Xia](https://dblp.org/pid/172/0129.html):

Apollo: An Exploration of Video Understanding in Large Multimodal Models. [CoRRabs/2412.10360](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-10360) (2024)
- ![](https://dblp.org/img/n.png)

\[i60\]
[Kunpeng Song](https://dblp.org/pid/194/1391.html), [Tingbo Hou](https://dblp.org/pid/35/3986.html), [Zecheng He](https://dblp.org/pid/203/5675.html), [Haoyu Ma](https://dblp.org/pid/144/1634.html), [Jialiang Wang](https://dblp.org/pid/27/8578-1.html), [Animesh Sinha](https://dblp.org/pid/289/7538.html), [Sam S. Tsai](https://dblp.org/pid/88/704.html), [Yaqiao Luo](https://dblp.org/pid/150/6230.html), [Xiaoliang Dai](https://dblp.org/pid/192/3904.html), [Li Chen](https://dblp.org/pid/181/2847.html), [Xide Xia](https://dblp.org/pid/172/0129.html), [Peizhao Zhang](https://dblp.org/pid/23/8011.html), [Peter Vajda](https://dblp.org/pid/44/5953.html), [Ahmed Elgammal](https://dblp.org/pid/e/AhmedMElgammal.html), Felix Juefei-Xu:

DirectorLLM for Human-Centric Video Generation. [CoRRabs/2412.14484](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-14484) (2024)
- ![](https://dblp.org/img/n.png)

\[i59\]
[Jiayi Zhu](https://dblp.org/pid/53/1649-2.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Yihao Huang](https://dblp.org/pid/255/5085.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

Concept Guided Co-saliency Objection Detection. [CoRRabs/2412.16609](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-16609) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j15\]
[Chuntao Ding](https://dblp.org/pid/150/4003.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhichao Lu](https://dblp.org/pid/144/1417.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yidong Li](https://dblp.org/pid/40/7652.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiannong Cao](https://dblp.org/pid/c/JiannongCao.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Towards Transmission-Friendly and Robust CNN Models over Cloud and Device. [IEEE Trans. Mob. Comput.22(10)](https://dblp.org/db/journals/tmc/tmc22.html#journals/tmc/DingLJBLC23): 6176-6189 (2023)
- ![](https://dblp.org/img/n.png)

\[j14\]
[Hua Qi](https://dblp.org/pid/87/4406.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhijie Wang](https://dblp.org/pid/64/5749-14.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianlang Chen](https://dblp.org/pid/307/5450.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Fuyuan Zhang](https://dblp.org/pid/08/7637.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

_ArchRepair_: Block-Level Architecture-Oriented Repairing for Deep Neural Networks. [ACM Trans. Softw. Eng. Methodol.32(5)](https://dblp.org/db/journals/tosem/tosem32.html#journals/tosem/QiWGCJZMZ23): 129:1-129:31 (2023)
- ![](https://dblp.org/img/n.png)

\[j13\]
[Zhichao Lu](https://dblp.org/pid/144/1417.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chuntao Ding](https://dblp.org/pid/150/4003.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shangguang Wang](https://dblp.org/pid/73/8637.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yun Yang](https://dblp.org/pid/90/3406-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

TFormer: A Transmission-Friendly ViT Model for IoT Devices. [IEEE Trans. Parallel Distributed Syst.34(2)](https://dblp.org/db/journals/tpds/tpds34.html#journals/tpds/LuDJBWY23): 598-610 (2023)
- ![](https://dblp.org/img/n.png)

\[c57\]
[Yiming Li](https://dblp.org/pid/l/YimingLi-3.html), [Qi Fang](https://dblp.org/pid/35/5244.html), [Jiamu Bai](https://dblp.org/pid/331/3706.html), [Siheng Chen](https://dblp.org/pid/136/4945.html), Felix Juefei-Xu, [Chen Feng](https://dblp.org/pid/01/161-2.html):

Among Us: Adversarially Robust Collaborative Perception by Consensus. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/LiFBCJF23): 186-195
- ![](https://dblp.org/img/n.png)

\[c56\]
[Yao Du](https://dblp.org/pid/166/4113-2.html), Felix Juefei-Xu:

Generative AI for Therapy? Opportunities and Barriers for ChatGPT in Speech-Language Therapy. [Tiny Papers @ ICLR2023](https://dblp.org/db/conf/iclr/iclr2023tiny.html#conf/iclr/DuJ23)
- ![](https://dblp.org/img/n.png)

\[c55\]
[Zhichao Lu](https://dblp.org/pid/144/1417.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chuntao Ding](https://dblp.org/pid/150/4003.html), [Shangguang Wang](https://dblp.org/pid/73/8637.html), [Ran Cheng](https://dblp.org/pid/18/4198-4.html), Felix Juefei-Xu, [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html):

Seed Feature Maps-based CNN Models for LEO Satellite Remote Sensing Services. [ICWS2023](https://dblp.org/db/conf/icws/icws2023.html#conf/icws/LuDWCJB23): 415-425
- ![](https://dblp.org/img/n.png)

\[c54\]
[Yi Liu](https://dblp.org/pid/97/4626-69.html), [Yuekang Li](https://dblp.org/pid/204/3729.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Gelei Deng](https://dblp.org/pid/236/9144.html), Felix Juefei-Xu, [Yao Du](https://dblp.org/pid/166/4113-2.html), [Cen Zhang](https://dblp.org/pid/200/7275.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chengwei Liu](https://dblp.org/pid/163/6525.html), [Yeting Li](https://dblp.org/pid/185/7953.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

ASTER: Automatic Speech Recognition System Accessibility Testing for Stutterers. [ASE2023](https://dblp.org/db/conf/kbse/ase2023.html#conf/kbse/LiuLDJDZLLML23): 510-521
- ![](https://dblp.org/img/n.png)

\[c53\]
[Yihao Huang](https://dblp.org/pid/255/5085.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liangru Sun](https://dblp.org/pid/311/4944.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jiayi Zhu](https://dblp.org/pid/53/1649-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jincao Feng](https://dblp.org/pid/255/5597.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Geguang Pu](https://dblp.org/pid/33/1678.html)![](https://dblp.org/img/orcid-mark.12x12.png):

ALA: Naturalness-aware Adversarial Lightness Attack. [ACM Multimedia2023](https://dblp.org/db/conf/mm/mm2023.html#conf/mm/0001S0JZFLP23): 2418-2426
- ![](https://dblp.org/img/n.png)

\[i58\]
[Zhichao Lu](https://dblp.org/pid/144/1417.html), [Chuntao Ding](https://dblp.org/pid/150/4003.html), Felix Juefei-Xu, [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html), [Shangguang Wang](https://dblp.org/pid/73/8637.html), [Yun Yang](https://dblp.org/pid/90/3406-1.html):

TFormer: A Transmission-Friendly ViT Model for IoT Devices. [CoRRabs/2302.07734](https://dblp.org/db/journals/corr/corr2302.html#journals/corr/abs-2302-07734) (2023)
- ![](https://dblp.org/img/n.png)

\[i57\]
[Yiming Li](https://dblp.org/pid/l/YimingLi-3.html), [Qi Fang](https://dblp.org/pid/35/5244.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiamu Bai](https://dblp.org/pid/331/3706.html), [Siheng Chen](https://dblp.org/pid/136/4945.html), Felix Juefei-Xu, [Chen Feng](https://dblp.org/pid/01/161-2.html):

Among Us: Adversarially Robust Collaborative Perception by Consensus. [CoRRabs/2303.09495](https://dblp.org/db/journals/corr/corr2303.html#journals/corr/abs-2303-09495) (2023)
- ![](https://dblp.org/img/n.png)

\[i56\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu:

Zero-Day Backdoor Attack against Text-to-Image Diffusion Models via Personalization. [CoRRabs/2305.10701](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-10701) (2023)
- ![](https://dblp.org/img/n.png)

\[i55\]
[Di Yang](https://dblp.org/pid/29/5427.html), [Yihao Huang](https://dblp.org/pid/255/5085.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Ming Hu](https://dblp.org/pid/82/378-3.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

Architecture-agnostic Iterative Black-box Certified Defense against Adversarial Patches. [CoRRabs/2305.10929](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-10929) (2023)
- ![](https://dblp.org/img/n.png)

\[i54\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), [Yue Cao](https://dblp.org/pid/74/5570.html), [Tianlin Li](https://dblp.org/pid/137/8830.html), Felix Juefei-Xu, [Di Lin](https://dblp.org/pid/20/3191-2.html), [Ivor W. Tsang](https://dblp.org/pid/35/5873.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html):

On the Robustness of Segment Anything. [CoRRabs/2305.16220](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-16220) (2023)
- ![](https://dblp.org/img/n.png)

\[i53\]
[Zhichao Lu](https://dblp.org/pid/144/1417.html), [Chuntao Ding](https://dblp.org/pid/150/4003.html), [Shangguang Wang](https://dblp.org/pid/73/8637.html), [Ran Cheng](https://dblp.org/pid/18/4198-4.html), Felix Juefei-Xu, [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html):

Seed Feature Maps-based CNN Models for LEO Satellite Remote Sensing Services. [CoRRabs/2308.06515](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-06515) (2023)
- ![](https://dblp.org/img/n.png)

\[i52\]
[Yi Liu](https://dblp.org/pid/97/4626-69.html), [Yuekang Li](https://dblp.org/pid/204/3729.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Gelei Deng](https://dblp.org/pid/236/9144.html), Felix Juefei-Xu, [Yao Du](https://dblp.org/pid/166/4113-2.html), [Cen Zhang](https://dblp.org/pid/200/7275.html), [Chengwei Liu](https://dblp.org/pid/163/6525.html), [Yeting Li](https://dblp.org/pid/185/7953.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

ASTER: Automatic Speech Recognition System Accessibility Testing for Stutterers. [CoRRabs/2308.15742](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-15742) (2023)
- ![](https://dblp.org/img/n.png)

\[i51\]
[Da Song](https://dblp.org/pid/222/6729.html), [Xuan Xie](https://dblp.org/pid/22/10184-1.html), [Jiayang Song](https://dblp.org/pid/182/7194.html), [Derui Zhu](https://dblp.org/pid/203/9320.html), [Yuheng Huang](https://dblp.org/pid/01/6508-4.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html):

LUNA: A Model-Based Universal Analysis Framework for Large Language Models. [CoRRabs/2310.14211](https://dblp.org/db/journals/corr/corr2310.html#journals/corr/abs-2310-14211) (2023)
- ![](https://dblp.org/img/n.png)

\[i50\]
[Chao Chen](https://dblp.org/pid/66/3019.html), [Mingzhi Zhu](https://dblp.org/pid/29/8415.html), [Ankush Pratap Singh](https://dblp.org/pid/362/3050.html), [Yu Yan](https://dblp.org/pid/12/778.html), Felix Juefei Xu, [Chen Feng](https://dblp.org/pid/01/161-2.html):

Scene Summarization: Clustering Scene Videos into Spatially Diverse Frames. [CoRRabs/2311.17940](https://dblp.org/db/journals/corr/corr2311.html#journals/corr/abs-2311-17940) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j12\]
Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Run Wang](https://dblp.org/pid/95/8501-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yihao Huang](https://dblp.org/pid/255/5085.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Countering Malicious DeepFakes: Survey, Battleground, and Horizon. [Int. J. Comput. Vis.130(7)](https://dblp.org/db/journals/ijcv/ijcv130.html#journals/ijcv/Juefei-XuWHGML22): 1678-1734 (2022)
- ![](https://dblp.org/img/n.png)

\[j11\]
[Xuhong Ren](https://dblp.org/pid/138/4258.html), [Jianlang Chen](https://dblp.org/pid/307/5450.html), Felix Juefei-Xu, [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html):

DARTSRepair: Core-failure-set guided DARTS for network robustness to common corruptions. [Pattern Recognit.131](https://dblp.org/db/journals/pr/pr131.html#journals/pr/RenCJXGMZC22): 108864 (2022)
- ![](https://dblp.org/img/n.png)

\[j10\]
[Lan Fu](https://dblp.org/pid/265/9476.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongkai Yu](https://dblp.org/pid/150/6670.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jinlong Li](https://dblp.org/pid/34/1296.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Song Wang](https://dblp.org/pid/62/3151-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Let There Be Light: Improved Traffic Surveillance via Detail Preserving Night-to-Day Transfer. [IEEE Trans. Circuits Syst. Video Technol.32(12)](https://dblp.org/db/journals/tcsv/tcsv32.html#journals/tcsv/FuYJLGW22): 8217-8226 (2022)
- ![](https://dblp.org/img/n.png)

\[j9\]
[Yihao Huang](https://dblp.org/pid/255/5085.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Geguang Pu](https://dblp.org/pid/33/1678.html)![](https://dblp.org/img/orcid-mark.12x12.png):

FakeLocator: Robust Localization of GAN-Based Face Manipulations. [IEEE Trans. Inf. Forensics Secur.17](https://dblp.org/db/journals/tifs/tifs17.html#journals/tifs/HuangJGLP22): 2657-2672 (2022)
- ![](https://dblp.org/img/n.png)

\[j8\]
[Yupeng Cheng](https://dblp.org/pid/148/8300.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Shang-Wei Lin](https://dblp.org/pid/55/4730-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weisi Lin](https://dblp.org/pid/14/3737.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Pasadena: Perceptually Aware and Stealthy Adversarial Denoise Attack. [IEEE Trans. Multim.24](https://dblp.org/db/journals/tmm/tmm24.html#journals/tmm/ChengGJLFLL22): 3807-3822 (2022)
- ![](https://dblp.org/img/n.png)

\[j7\]
[Alvin Chan](https://dblp.org/pid/163/6518.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Yew-Soon Ong](https://dblp.org/pid/64/4136.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Minhui Xue](https://dblp.org/pid/166/1912.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Breaking Neural Reasoning Architectures With Metamorphic Relation-Based Adversarial Examples. [IEEE Trans. Neural Networks Learn. Syst.33(11)](https://dblp.org/db/journals/tnn/tnn33.html#journals/tnn/ChanMJOXXL22): 6976-6982 (2022)
- ![](https://dblp.org/img/n.png)

\[j6\]
[Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianlin Li](https://dblp.org/pid/137/8830.html), [Jian Wang](https://dblp.org/pid/39/449-67.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

NPC: Neuron Path Coverage via Characterizing Decision Logic of Deep Neural Networks. [ACM Trans. Softw. Eng. Methodol.31(3)](https://dblp.org/db/journals/tosem/tosem31.html#journals/tosem/XieLWMGJL22): 47:1-47:27 (2022)
- ![](https://dblp.org/img/n.png)

\[j5\]
[Bing Yu](https://dblp.org/pid/47/2129.html), [Hua Qi](https://dblp.org/pid/87/4406.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

DeepRepair: Style-Guided Repairing for Deep Neural Networks in the Real-World Operational Environment. [IEEE Trans. Reliab.71(4)](https://dblp.org/db/journals/tr/tr71.html#journals/tr/YuQGJXMZ22): 1401-1416 (2022)
- ![](https://dblp.org/img/n.png)

\[c52\]
[Ruijun Gao](https://dblp.org/pid/247/5683.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Hongkai Yu](https://dblp.org/pid/150/6670.html), [Huazhu Fu](https://dblp.org/pid/63/7767.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Song Wang](https://dblp.org/pid/62/3151-2.html):

Can You Spot the Chameleon? Adversarially Camouflaging Images from Co-Salient Object Detection. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/Gao0JYFF0W22): 2140-2149
- ![](https://dblp.org/img/n.png)

\[c51\]
[Jiayi Zhu](https://dblp.org/pid/53/1649-2.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Yihao Huang](https://dblp.org/pid/255/5085.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Geguang Pu](https://dblp.org/pid/33/1678.html):

Masked Faces with Faced Masks. [ECCV Workshops (1)2022](https://dblp.org/db/conf/eccv/eccv2022-w1.html#conf/eccv/ZhuGJHLP22): 360-377
- ![](https://dblp.org/img/n.png)

\[i49\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), [Jingyang Sun](https://dblp.org/pid/217/7354.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Di Lin](https://dblp.org/pid/20/3191-2.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Song Wang](https://dblp.org/pid/62/3151-2.html):

Uncertainty-Aware Cascaded Dilation Filtering for High-Efficiency Deraining. [CoRRabs/2201.02366](https://dblp.org/db/journals/corr/corr2201.html#journals/corr/abs-2201-02366) (2022)
- ![](https://dblp.org/img/n.png)

\[i48\]
[Liangru Sun](https://dblp.org/pid/311/4944.html), Felix Juefei-Xu, [Yihao Huang](https://dblp.org/pid/255/5085.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Jiayi Zhu](https://dblp.org/pid/53/1649-2.html), [Jincao Feng](https://dblp.org/pid/255/5597.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

ALA: Adversarial Lightness Attack via Naturalness-aware Regularizations. [CoRRabs/2201.06070](https://dblp.org/db/journals/corr/corr2201.html#journals/corr/abs-2201-06070) (2022)
- ![](https://dblp.org/img/n.png)

\[i47\]
[Jiayi Zhu](https://dblp.org/pid/53/1649-2.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Yihao Huang](https://dblp.org/pid/255/5085.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

Masked Faces with Faced Masks. [CoRRabs/2201.06427](https://dblp.org/db/journals/corr/corr2201.html#journals/corr/abs-2201-06427) (2022)
- ![](https://dblp.org/img/n.png)

\[i46\]
[Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianlin Li](https://dblp.org/pid/137/8830.html), [Jian Wang](https://dblp.org/pid/39/449-67.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Yang Liu](https://dblp.org/pid/51/3710-3.html):

NPC: Neuron Path Coverage via Characterizing Decision Logic of Deep Neural Networks. [CoRRabs/2203.12915](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-12915) (2022)
- ![](https://dblp.org/img/n.png)

\[i45\]
[Chuntao Ding](https://dblp.org/pid/150/4003.html), [Zhichao Lu](https://dblp.org/pid/144/1417.html), Felix Juefei-Xu, [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html), [Yidong Li](https://dblp.org/pid/40/7652.html), [Jiannong Cao](https://dblp.org/pid/c/JiannongCao.html):

Towards Transmission-Friendly and Robust CNN Models over Cloud and Device. [CoRRabs/2207.09616](https://dblp.org/db/journals/corr/corr2207.html#journals/corr/abs-2207-09616) (2022)
- ![](https://dblp.org/img/n.png)

\[i44\]
[Xuhong Ren](https://dblp.org/pid/138/4258.html), [Jianlang Chen](https://dblp.org/pid/307/5450.html), Felix Juefei-Xu, [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html):

DARTSRepair: Core-failure-set Guided DARTS for Network Robustness to Common Corruptions. [CoRRabs/2209.10381](https://dblp.org/db/journals/corr/corr2209.html#journals/corr/abs-2209-10381) (2022)
- ![](https://dblp.org/img/n.png)

\[i43\]
[Shuangzhi Li](https://dblp.org/pid/331/2840.html), [Zhijie Wang](https://dblp.org/pid/64/5749-14.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Xingyu Li](https://dblp.org/pid/45/2385.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html):

Common Corruption Robustness of Point Cloud Detectors: Benchmark and Enhancement. [CoRRabs/2210.05896](https://dblp.org/db/journals/corr/corr2210.html#journals/corr/abs-2210-05896) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[c50\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), [Jingyang Sun](https://dblp.org/pid/217/7354.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

EfficientDeRain: Learning Pixel-wise Dilation Filtering for High-Efficiency Single-Image Deraining. [AAAI2021](https://dblp.org/db/conf/aaai/aaai2021.html#conf/aaai/GuoSJMX00Z21): 1487-1495
- ![](https://dblp.org/img/n.png)

\[c49\]
[Lan Fu](https://dblp.org/pid/265/9476.html), [Changqing Zhou](https://dblp.org/pid/40/6559.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Hongkai Yu](https://dblp.org/pid/150/6670.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Song Wang](https://dblp.org/pid/62/3151-2.html):

Auto-Exposure Fusion for Single-Image Shadow Removal. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/FuZ0JY00021): 10571-10580
- ![](https://dblp.org/img/n.png)

\[c48\]
[Yiming Li](https://dblp.org/pid/l/YimingLi-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Congcong Wen](https://dblp.org/pid/218/4638.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu, [Chen Feng](https://dblp.org/pid/01/161-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Fooling LiDAR Perception via Adversarial Trajectory Perturbation. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/LiWJF21): 7878-7887
- ![](https://dblp.org/img/n.png)

\[c47\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

Learning to Adversarially Blur Visual Object Tracking. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/0005CJ0X0Z21): 10819-10828
- ![](https://dblp.org/img/n.png)

\[c46\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Yu-Chen Chiu](https://dblp.org/pid/199/2494.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Xingping Dong](https://dblp.org/pid/156/3020.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Bilge Günsel](https://dblp.org/pid/47/5125.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Wencheng Han](https://dblp.org/pid/280/3348.html), [Yanyan Huang](https://dblp.org/pid/88/4316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), Felix Juefei-Xu, [J. Yin](https://dblp.org/pid/51/2242.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Jingen Liu](https://dblp.org/pid/10/5849.html), [Li Liu](https://dblp.org/pid/33/4528-36.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Jonathon Luiten](https://dblp.org/pid/211/7992.html), [Jie Ma](https://dblp.org/pid/62/5110.html), [Ziang Ma](https://dblp.org/pid/165/9621.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Yuzhen Niu](https://dblp.org/pid/28/7442.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Aravindh Rajiv](https://dblp.org/pid/307/9144.html), [Muhammad Rana](https://dblp.org/pid/276/0222.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Ling Shao](https://dblp.org/pid/75/1281.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furao Shen](https://dblp.org/pid/80/4685.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Paul Voigtlaender](https://dblp.org/pid/166/6430.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html), [Chenyan Wu](https://dblp.org/pid/76/1190.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang Xu](https://dblp.org/pid/126/2962.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Xiaohan Zhang](https://dblp.org/pid/96/6053.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Ming Zhen](https://dblp.org/pid/307/8430.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html):

The Ninth Visual Object Tracking VOT2021 Challenge Results. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/KristanMLFPKCDZ21): 2711-2738
- ![](https://dblp.org/img/n.png)

\[c45\]
[Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Xuhong Ren](https://dblp.org/pid/138/4258.html), Felix Juefei-Xu, [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

Deepmix: Online Auto Data Augmentation for Robust Visual Object Tracking. [ICME2021](https://dblp.org/db/conf/icmcs/icme2021.html#conf/icmcs/ChengRJX00Z21): 1-6
- ![](https://dblp.org/img/n.png)

\[c44\]
[Binyu Tian](https://dblp.org/pid/274/7389.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Wen Le Chan](https://dblp.org/pid/274/7365.html), [Yupeng Cheng](https://dblp.org/pid/148/8300.html), [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shengchao Qin](https://dblp.org/pid/q/ShengchaoQin.html):

Bias Field Poses a Threat to DNN-Based X-Ray Recognition. [ICME2021](https://dblp.org/db/conf/icmcs/icme2021.html#conf/icmcs/Tian0JCC0XQ21): 1-6
- ![](https://dblp.org/img/n.png)

\[c43\]
[Binyu Tian](https://dblp.org/pid/274/7389.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

AVA: Adversarial Vignetting Attack against Visual Recognition. [IJCAI2021](https://dblp.org/db/conf/ijcai/ijcai2021.html#conf/ijcai/TianJ0XLL21): 1046-1053
- ![](https://dblp.org/img/n.png)

\[c42\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), [Xiaoguang Li](https://dblp.org/pid/46/1349.html), Felix Juefei-Xu, [Hongkai Yu](https://dblp.org/pid/150/6670.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Song Wang](https://dblp.org/pid/62/3151-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

JPGNet: Joint Predictive Filtering and Generative Network for Image Inpainting. [ACM Multimedia2021](https://dblp.org/db/conf/mm/mm2021.html#conf/mm/GuoLJYLW21): 386-394
- ![](https://dblp.org/img/n.png)

\[c41\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Weikai Miao](https://dblp.org/pid/94/4256.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Geguang Pu](https://dblp.org/pid/33/1678.html):

AdvFilter: Predictive Perturbation-aware Filtering against Adversarial Attack via Multi-domain Learning. [ACM Multimedia2021](https://dblp.org/db/conf/mm/mm2021.html#conf/mm/00010JMMLP21): 395-403
- ![](https://dblp.org/img/n.png)

\[c40\]
[Run Wang](https://dblp.org/pid/95/8501-1.html), Felix Juefei-Xu, [Meng Luo](https://dblp.org/pid/16/3121-2.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lina Wang](https://dblp.org/pid/01/1318-1.html):

FakeTagger: Robust Safeguards against DeepFake Dissemination via Provenance Tracking. [ACM Multimedia2021](https://dblp.org/db/conf/mm/mm2021.html#conf/mm/WangJLLW21): 3546-3555
- ![](https://dblp.org/img/n.png)

\[i42\]
Felix Juefei-Xu, [Run Wang](https://dblp.org/pid/95/8501-1.html), [Yihao Huang](https://dblp.org/pid/255/5085.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

Countering Malicious DeepFakes: Survey, Battleground, and Horizon. [CoRRabs/2103.00218](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-00218) (2021)
- ![](https://dblp.org/img/n.png)

\[i41\]
[Lan Fu](https://dblp.org/pid/265/9476.html), [Changqing Zhou](https://dblp.org/pid/40/6559.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Hongkai Yu](https://dblp.org/pid/150/6670.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Song Wang](https://dblp.org/pid/62/3151-2.html):

Auto-Exposure Fusion for Single-Image Shadow Removal. [CoRRabs/2103.01255](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-01255) (2021)
- ![](https://dblp.org/img/n.png)

\[i40\]
[Yiming Li](https://dblp.org/pid/l/YimingLi-3.html), [Congcong Wen](https://dblp.org/pid/218/4638.html), Felix Juefei-Xu, [Chen Feng](https://dblp.org/pid/01/161-2.html):

Fooling LiDAR Perception via Adversarial Trajectory Perturbation. [CoRRabs/2103.15326](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-15326) (2021)
- ![](https://dblp.org/img/n.png)

\[i39\]
[Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Xuhong Ren](https://dblp.org/pid/138/4258.html), Felix Juefei-Xu, [Wanli Xue](https://dblp.org/pid/153/8037.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

DeepMix: Online Auto Data Augmentation for Robust Visual Object Tracking. [CoRRabs/2104.11585](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-11585) (2021)
- ![](https://dblp.org/img/n.png)

\[i38\]
[Ruijun Gao](https://dblp.org/pid/247/5683.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Hongkai Yu](https://dblp.org/pid/150/6670.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html):

AdvHaze: Adversarial Haze Attack. [CoRRabs/2104.13673](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-13673) (2021)
- ![](https://dblp.org/img/n.png)

\[i37\]
[Lan Fu](https://dblp.org/pid/265/9476.html), [Hongkai Yu](https://dblp.org/pid/150/6670.html), Felix Juefei-Xu, [Jinlong Li](https://dblp.org/pid/34/1296.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Song Wang](https://dblp.org/pid/62/3151-2.html):

Let There be Light: Improved Traffic Surveillance via Detail Preserving Night-to-Day Transfer. [CoRRabs/2105.05011](https://dblp.org/db/journals/corr/corr2105.html#journals/corr/abs-2105-05011) (2021)
- ![](https://dblp.org/img/n.png)

\[i36\]
[Binyu Tian](https://dblp.org/pid/274/7389.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

AVA: Adversarial Vignetting Attack against Visual Recognition. [CoRRabs/2105.05558](https://dblp.org/db/journals/corr/corr2105.html#journals/corr/abs-2105-05558) (2021)
- ![](https://dblp.org/img/n.png)

\[i35\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Changqing Zhou](https://dblp.org/pid/40/6559.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Song Wang](https://dblp.org/pid/62/3151-2.html):

Sparta: Spatially Attentive and Adversarially Robust Activation. [CoRRabs/2105.08269](https://dblp.org/db/journals/corr/corr2105.html#journals/corr/abs-2105-08269) (2021)
- ![](https://dblp.org/img/n.png)

\[i34\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), [Xiaoguang Li](https://dblp.org/pid/46/1349.html), Felix Juefei-Xu, [Hongkai Yu](https://dblp.org/pid/150/6670.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Song Wang](https://dblp.org/pid/62/3151-2.html):

JPGNet: Joint Predictive Filtering and Generative Network for Image Inpainting. [CoRRabs/2107.04281](https://dblp.org/db/journals/corr/corr2107.html#journals/corr/abs-2107-04281) (2021)
- ![](https://dblp.org/img/n.png)

\[i33\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Weikai Miao](https://dblp.org/pid/94/4256.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

AdvFilter: Predictive Perturbation-aware Filtering against Adversarial Attack via Multi-domain Learning. [CoRRabs/2107.06501](https://dblp.org/db/journals/corr/corr2107.html#journals/corr/abs-2107-06501) (2021)
- ![](https://dblp.org/img/n.png)

\[i32\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

Learning to Adversarially Blur Visual Object Tracking. [CoRRabs/2107.12085](https://dblp.org/db/journals/corr/corr2107.html#journals/corr/abs-2107-12085) (2021)
- ![](https://dblp.org/img/n.png)

\[i31\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), [Zhijie Wang](https://dblp.org/pid/64/5749-14.html), Felix Juefei-Xu, [Di Lin](https://dblp.org/pid/20/3191-2.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

CarveNet: Carving Point-Block for Complex 3D Shape Completion. [CoRRabs/2107.13452](https://dblp.org/db/journals/corr/corr2107.html#journals/corr/abs-2107-13452) (2021)
- ![](https://dblp.org/img/n.png)

\[i30\]
[Ruijun Gao](https://dblp.org/pid/247/5683.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Qian Zhang](https://dblp.org/pid/04/2024-51.html), Felix Juefei-Xu, [Hongkai Yu](https://dblp.org/pid/150/6670.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html):

Adversarial Relighting against Face Recognition. [CoRRabs/2108.07920](https://dblp.org/db/journals/corr/corr2108.html#journals/corr/abs-2108-07920) (2021)
- ![](https://dblp.org/img/n.png)

\[i29\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Weikai Miao](https://dblp.org/pid/94/4256.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

AdvBokeh: Learning to Adversarially Defocus Blur. [CoRRabs/2111.12971](https://dblp.org/db/journals/corr/corr2111.html#journals/corr/abs-2111-12971) (2021)
- ![](https://dblp.org/img/n.png)

\[i28\]
[Hua Qi](https://dblp.org/pid/87/4406.html), [Zhijie Wang](https://dblp.org/pid/64/5749-14.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Jianlang Chen](https://dblp.org/pid/307/5450.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

ArchRepair: Block-Level Architecture-Oriented Repairing for Deep Neural Networks. [CoRRabs/2111.13330](https://dblp.org/db/journals/corr/corr2111.html#journals/corr/abs-2111-13330) (2021)
- ![](https://dblp.org/img/n.png)

\[i27\]
[Lan Fu](https://dblp.org/pid/265/9476.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Hongkai Yu](https://dblp.org/pid/150/6670.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Song Wang](https://dblp.org/pid/62/3151-2.html):

Benchmarking Shadow Removal for Facial Landmark Detection and Beyond. [CoRRabs/2111.13790](https://dblp.org/db/journals/corr/corr2111.html#journals/corr/abs-2111-13790) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[c39\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhongguo Li](https://dblp.org/pid/49/8374.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

SPARK: Spatial-Aware Online Incremental Attack Against Visual Tracking. [ECCV (25)2020](https://dblp.org/db/conf/eccv/eccv2020-25.html#conf/eccv/GuoXJMLXFL20): 202-219
- ![](https://dblp.org/img/n.png)

\[c38\]
[Xuhong Ren](https://dblp.org/pid/138/4258.html), [Bing Yu](https://dblp.org/pid/47/2129.html), [Hua Qi](https://dblp.org/pid/87/4406.html), Felix Juefei-Xu, [Zhuo Li](https://dblp.org/pid/51/4015-13.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

Few-Shot Guided Mix for DNN Repairing. [ICSME2020](https://dblp.org/db/conf/icsm/icsme2020.html#conf/icsm/RenYQJLXMZ20): 717-721
- ![](https://dblp.org/img/n.png)

\[c37\]
[Run Wang](https://dblp.org/pid/95/8501-1.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Yihao Huang](https://dblp.org/pid/255/5085.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Wang](https://dblp.org/pid/39/449-67.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

FakeSpotter: A Simple yet Robust Baseline for Spotting AI-Synthesized Fake Faces. [IJCAI2020](https://dblp.org/db/conf/ijcai/ijcai2020.html#conf/ijcai/WangJMXHWL20): 3444-3451
- ![](https://dblp.org/img/n.png)

\[c36\]
[Run Wang](https://dblp.org/pid/95/8501-1.html), Felix Juefei-Xu, [Yihao Huang](https://dblp.org/pid/255/5085.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

DeepSonar: Towards Effective and Robust Detection of AI-Synthesized Fake Voices. [ACM Multimedia2020](https://dblp.org/db/conf/mm/mm2020.html#conf/mm/WangJHGXML20): 1207-1216
- ![](https://dblp.org/img/n.png)

\[c35\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), Felix Juefei-Xu, [Run Wang](https://dblp.org/pid/95/8501-1.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianwen Li](https://dblp.org/pid/21/8669.html), [Weikai Miao](https://dblp.org/pid/94/4256.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Geguang Pu](https://dblp.org/pid/33/1678.html):

FakePolisher: Making DeepFakes More Detection-Evasive by Shallow Reconstruction. [ACM Multimedia2020](https://dblp.org/db/conf/mm/mm2020.html#conf/mm/HuangJWGMXLMLP20): 1217-1226
- ![](https://dblp.org/img/n.png)

\[c34\]
[Run Wang](https://dblp.org/pid/95/8501-1.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Yihao Huang](https://dblp.org/pid/255/5085.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Amora: Black-box Adversarial Morphing Attack. [ACM Multimedia2020](https://dblp.org/db/conf/mm/mm2020.html#conf/mm/WangJGHXML20): 1376-1385
- ![](https://dblp.org/img/n.png)

\[c33\]
[Hua Qi](https://dblp.org/pid/87/4406.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

DeepRhythm: Exposing DeepFakes with Attentional Visual Heartbeat Rhythms. [ACM Multimedia2020](https://dblp.org/db/conf/mm/mm2020.html#conf/mm/QiGJXMFLZ20): 4318-4327
- ![](https://dblp.org/img/n.png)

\[c32\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jian Wang](https://dblp.org/pid/39/449-67.html), [Bing Yu](https://dblp.org/pid/47/2129.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

Watch out! Motion is Blurring the Vision of Your Deep Neural Networks. [NeurIPS2020](https://dblp.org/db/conf/nips/neurips2020.html#conf/nips/0005JX0WY0020)
- ![](https://dblp.org/img/n.png)

\[i26\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), Felix Juefei-Xu, [Run Wang](https://dblp.org/pid/95/8501-1.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianwen Li](https://dblp.org/pid/21/8669.html), [Weikai Miao](https://dblp.org/pid/94/4256.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

FakeLocator: Robust Localization of GAN-Based Face Manipulations via Semantic Segmentation Networks with Bells and Whistles. [CoRRabs/2001.09598](https://dblp.org/db/journals/corr/corr2001.html#journals/corr/abs-2001-09598) (2020)
- ![](https://dblp.org/img/n.png)

\[i25\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jian Wang](https://dblp.org/pid/39/449-67.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

ABBA: Saliency-Regularized Motion-Based Adversarial Blur Attack. [CoRRabs/2002.03500](https://dblp.org/db/journals/corr/corr2002.html#journals/corr/abs-2002-03500) (2020)
- ![](https://dblp.org/img/n.png)

\[i24\]
[Run Wang](https://dblp.org/pid/95/8501-1.html), Felix Juefei-Xu, [Yihao Huang](https://dblp.org/pid/255/5085.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

DeepSonar: Towards Effective and Robust Detection of AI-Synthesized Fake Voices. [CoRRabs/2005.13770](https://dblp.org/db/journals/corr/corr2005.html#journals/corr/abs-2005-13770) (2020)
- ![](https://dblp.org/img/n.png)

\[i23\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), Felix Juefei-Xu, [Run Wang](https://dblp.org/pid/95/8501-1.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Jianwen Li](https://dblp.org/pid/21/8669.html), [Weikai Miao](https://dblp.org/pid/94/4256.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

FakePolisher: Making DeepFakes More Detection-Evasive by Shallow Reconstruction. [CoRRabs/2006.07533](https://dblp.org/db/journals/corr/corr2006.html#journals/corr/abs-2006-07533) (2020)
- ![](https://dblp.org/img/n.png)

\[i22\]
[Hua Qi](https://dblp.org/pid/87/4406.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

DeepRhythm: Exposing DeepFakes with Attentional Visual Heartbeat Rhythms. [CoRRabs/2006.07634](https://dblp.org/db/journals/corr/corr2006.html#journals/corr/abs-2006-07634) (2020)
- ![](https://dblp.org/img/n.png)

\[i21\]
[Renzhi Wang](https://dblp.org/pid/152/2466.html), [Tianwei Zhang](https://dblp.org/pid/77/7902-4.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Cong Tian](https://dblp.org/pid/00/5365-1.html), Felix Juefei-Xu, [Yang Liu](https://dblp.org/pid/51/3710-3.html):

Generating Adversarial Examples withControllable Non-transferability. [CoRRabs/2007.01299](https://dblp.org/db/journals/corr/corr2007.html#journals/corr/abs-2007-01299) (2020)
- ![](https://dblp.org/img/n.png)

\[i20\]
[Yupeng Cheng](https://dblp.org/pid/148/8300.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Shang-Wei Lin](https://dblp.org/pid/55/4730-1.html), [Weisi Lin](https://dblp.org/pid/14/3737.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

Pasadena: Perceptually Aware and Stealthy Adversarial Denoise Attack. [CoRRabs/2007.07097](https://dblp.org/db/journals/corr/corr2007.html#journals/corr/abs-2007-07097) (2020)
- ![](https://dblp.org/img/n.png)

\[i19\]
[Liming Zhai](https://dblp.org/pid/149/3381.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Shengchao Qin](https://dblp.org/pid/q/ShengchaoQin.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

It's Raining Cats or Dogs? Adversarial Rain Attack on DNN Perception. [CoRRabs/2009.09205](https://dblp.org/db/journals/corr/corr2009.html#journals/corr/abs-2009-09205) (2020)
- ![](https://dblp.org/img/n.png)

\[i18\]
[Yihao Huang](https://dblp.org/pid/255/5085.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Weikai Miao](https://dblp.org/pid/94/4256.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Geguang Pu](https://dblp.org/pid/33/1678.html):

FakeRetouch: Evading DeepFakes Detection via the Guidance of Deliberate Noise. [CoRRabs/2009.09213](https://dblp.org/db/journals/corr/corr2009.html#journals/corr/abs-2009-09213) (2020)
- ![](https://dblp.org/img/n.png)

\[i17\]
[Yupeng Cheng](https://dblp.org/pid/148/8300.html), Felix Juefei-Xu, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Huazhu Fu](https://dblp.org/pid/63/7767.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Shang-Wei Lin](https://dblp.org/pid/55/4730-1.html), [Weisi Lin](https://dblp.org/pid/14/3737.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

Adversarial Exposure Attack on Diabetic Retinopathy Imagery. [CoRRabs/2009.09231](https://dblp.org/db/journals/corr/corr2009.html#journals/corr/abs-2009-09231) (2020)
- ![](https://dblp.org/img/n.png)

\[i16\]
[Qing Guo](https://dblp.org/pid/25/3038-5.html), [Jingyang Sun](https://dblp.org/pid/217/7354.html), Felix Juefei-Xu, [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

EfficientDeRain: Learning Pixel-wise Dilation Filtering for High-Efficiency Single-Image Deraining. [CoRRabs/2009.09238](https://dblp.org/db/journals/corr/corr2009.html#journals/corr/abs-2009-09238) (2020)
- ![](https://dblp.org/img/n.png)

\[i15\]
[Binyu Tian](https://dblp.org/pid/274/7389.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Wen Le Chan](https://dblp.org/pid/274/7365.html), [Yupeng Cheng](https://dblp.org/pid/148/8300.html), [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Shengchao Qin](https://dblp.org/pid/q/ShengchaoQin.html):

Bias Field Poses a Threat to DNN-based X-Ray Recognition. [CoRRabs/2009.09247](https://dblp.org/db/journals/corr/corr2009.html#journals/corr/abs-2009-09247) (2020)
- ![](https://dblp.org/img/n.png)

\[i14\]
[Ruijun Gao](https://dblp.org/pid/247/5683.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Hongkai Yu](https://dblp.org/pid/150/6670.html), [Xuhong Ren](https://dblp.org/pid/138/4258.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Song Wang](https://dblp.org/pid/62/3151-2.html):

Making Images Undiscoverable from Co-Saliency Detection. [CoRRabs/2009.09258](https://dblp.org/db/journals/corr/corr2009.html#journals/corr/abs-2009-09258) (2020)
- ![](https://dblp.org/img/n.png)

\[i13\]
[Run Wang](https://dblp.org/pid/95/8501-1.html), Felix Juefei-Xu, [Meng Luo](https://dblp.org/pid/16/3121-2.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Lina Wang](https://dblp.org/pid/01/1318-1.html):

FakeTagger: Robust Safeguards against DeepFake Dissemination via Provenance Tracking. [CoRRabs/2009.09869](https://dblp.org/db/journals/corr/corr2009.html#journals/corr/abs-2009-09869) (2020)
- ![](https://dblp.org/img/n.png)

\[i12\]
[Bing Yu](https://dblp.org/pid/47/2129.html), [Hua Qi](https://dblp.org/pid/87/4406.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), Felix Juefei-Xu, [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

DeepRepair: Style-Guided Repairing for DNNs in the Real-world Operational Environment. [CoRRabs/2011.09884](https://dblp.org/db/journals/corr/corr2011.html#journals/corr/abs-2011-09884) (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j4\]
[Ramzi Abiantun](https://dblp.org/pid/72/989.html), Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Utsav Prabhu](https://dblp.org/pid/54/10072.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

SSR2: Sparse signal recovery for single-image super-resolution on faces with extreme low resolutions. [Pattern Recognit.90](https://dblp.org/db/journals/pr/pr90.html#journals/pr/AbiantunJPS19): 308-324 (2019)
- ![](https://dblp.org/img/n.png)

\[c31\]
[Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Ma](https://dblp.org/pid/20/6534-3.html), Felix Juefei-Xu, [Minhui Xue](https://dblp.org/pid/166/1912.html), [Hongxu Chen](https://dblp.org/pid/147/5824-1.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html), [Bo Li](https://dblp.org/pid/50/3402-26.html), [Jianxiong Yin](https://dblp.org/pid/132/8514.html), [Simon See](https://dblp.org/pid/62/6547.html):

DeepHunter: a coverage-guided fuzz testing framework for deep neural networks. [ISSTA2019](https://dblp.org/db/conf/issta/issta2019.html#conf/issta/XieMJXCLZLYS19): 146-157
- ![](https://dblp.org/img/n.png)

\[c30\]
[Lei Ma](https://dblp.org/pid/20/6534-3.html), Felix Juefei-Xu, [Minhui Xue](https://dblp.org/pid/166/1912.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bo Li](https://dblp.org/pid/50/3402-26.html), [Li Li](https://dblp.org/pid/53/2189-29.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html):

DeepCT: Tomographic Combinatorial Testing for Deep Learning Systems. [SANER2019](https://dblp.org/db/conf/wcre/saner2019.html#conf/wcre/MaJXLLLZ19): 614-618
- ![](https://dblp.org/img/n.png)

\[i11\]
[Run Wang](https://dblp.org/pid/95/8501-1.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), Felix Juefei-Xu, [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Jian Wang](https://dblp.org/pid/39/449-67.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

FakeSpotter: A Simple Baseline for Spotting AI-Synthesized Fake Faces. [CoRRabs/1909.06122](https://dblp.org/db/journals/corr/corr1909.html#journals/corr/abs-1909-06122) (2019)
- ![](https://dblp.org/img/n.png)

\[i10\]
[Run Wang](https://dblp.org/pid/95/8501-1.html), Felix Juefei-Xu, [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), [Yihao Huang](https://dblp.org/pid/255/5085.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html):

Amora: Black-box Adversarial Morphing Attack. [CoRRabs/1912.03829](https://dblp.org/db/journals/corr/corr1912.html#journals/corr/abs-1912-03829) (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[b1\]
Felix Juefei-Xu:

Unconstrained Periocular Face Recognition: From Reconstructive Dictionary Learning to Generative Deep Learning and Beyond. Carnegie Mellon University, USA, 2018
- ![](https://dblp.org/img/n.png)

\[c29\]
Felix Juefei-Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Rahul Dey](https://dblp.org/pid/135/8801.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

RankGAN: A Maximum Margin Ranking GAN for Generating Faces. [ACCV (3)2018](https://dblp.org/db/conf/accv/accv2018-3.html#conf/accv/Juefei-XuDBS18): 3-18
- ![](https://dblp.org/img/n.png)

\[c28\]
Felix Juefei-Xu, [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Perturbative Neural Networks. [CVPR2018](https://dblp.org/db/conf/cvpr/cvpr2018.html#conf/cvpr/Juefei-XuBS18): 3310-3318
- ![](https://dblp.org/img/n.png)

\[c27\]
[Lei Ma](https://dblp.org/pid/20/6534-3.html), [Fuyuan Zhang](https://dblp.org/pid/08/7637.html), [Jiyuan Sun](https://dblp.org/pid/160/6224.html), [Minhui Xue](https://dblp.org/pid/166/1912.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bo Li](https://dblp.org/pid/50/3402-26.html), Felix Juefei-Xu, [Chao Xie](https://dblp.org/pid/04/5576.html), [Li Li](https://dblp.org/pid/53/2189-29.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html), [Yadong Wang](https://dblp.org/pid/68/782.html):

DeepMutation: Mutation Testing of Deep Learning Systems. [ISSRE2018](https://dblp.org/db/conf/issre/issre2018.html#conf/issre/MaZSXLJXLLZW18): 100-111
- ![](https://dblp.org/img/n.png)

\[c26\]
[Lei Ma](https://dblp.org/pid/20/6534-3.html), Felix Juefei-Xu, [Fuyuan Zhang](https://dblp.org/pid/08/7637.html), [Jiyuan Sun](https://dblp.org/pid/160/6224.html), [Minhui Xue](https://dblp.org/pid/166/1912.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bo Li](https://dblp.org/pid/50/3402-26.html), [Chunyang Chen](https://dblp.org/pid/180/7246.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ting Su](https://dblp.org/pid/42/6896-1.html), [Li Li](https://dblp.org/pid/53/2189-29.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html), [Yadong Wang](https://dblp.org/pid/68/782.html):

DeepGauge: multi-granularity testing criteria for deep learning systems. [ASE2018](https://dblp.org/db/conf/kbse/ase2018.html#conf/kbse/MaJZSXLCSLLZW18): 120-131
- ![](https://dblp.org/img/n.png)

\[i9\]
[Lei Ma](https://dblp.org/pid/20/6534-3.html), Felix Juefei-Xu, [Jiyuan Sun](https://dblp.org/pid/160/6224.html), [Chunyang Chen](https://dblp.org/pid/180/7246.html), [Ting Su](https://dblp.org/pid/42/6896-1.html), [Fuyuan Zhang](https://dblp.org/pid/08/7637.html), [Minhui Xue](https://dblp.org/pid/166/1912.html), [Bo Li](https://dblp.org/pid/50/3402-26.html), [Li Li](https://dblp.org/pid/53/2189-29.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html), [Yadong Wang](https://dblp.org/pid/68/782.html):

DeepGauge: Comprehensive and Multi-Granularity Testing Criteria for Gauging the Robustness of Deep Learning Systems. [CoRRabs/1803.07519](https://dblp.org/db/journals/corr/corr1803.html#journals/corr/abs-1803-07519) (2018)
- ![](https://dblp.org/img/n.png)

\[i8\]
[Lei Ma](https://dblp.org/pid/20/6534-3.html), [Fuyuan Zhang](https://dblp.org/pid/08/7637.html), [Jiyuan Sun](https://dblp.org/pid/160/6224.html), [Minhui Xue](https://dblp.org/pid/166/1912.html), [Bo Li](https://dblp.org/pid/50/3402-26.html), Felix Juefei-Xu, [Chao Xie](https://dblp.org/pid/04/5576.html), [Li Li](https://dblp.org/pid/53/2189-29.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html), [Yadong Wang](https://dblp.org/pid/68/782.html):

DeepMutation: Mutation Testing of Deep Learning Systems. [CoRRabs/1805.05206](https://dblp.org/db/journals/corr/corr1805.html#journals/corr/abs-1805-05206) (2018)
- ![](https://dblp.org/img/n.png)

\[i7\]
Felix Juefei-Xu, [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Perturbative Neural Networks. [CoRRabs/1806.01817](https://dblp.org/db/journals/corr/corr1806.html#journals/corr/abs-1806-01817) (2018)
- ![](https://dblp.org/img/n.png)

\[i6\]
[Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), Felix Juefei-Xu, [Hongxu Chen](https://dblp.org/pid/147/5824-1.html), [Minhui Xue](https://dblp.org/pid/166/1912.html), [Bo Li](https://dblp.org/pid/50/3402-26.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html), [Jianxiong Yin](https://dblp.org/pid/132/8514.html), [Simon See](https://dblp.org/pid/62/6547.html):

Coverage-Guided Fuzzing for Deep Neural Networks. [CoRRabs/1809.01266](https://dblp.org/db/journals/corr/corr1809.html#journals/corr/abs-1809-01266) (2018)
- ![](https://dblp.org/img/n.png)

\[i5\]
[Alvin Chan](https://dblp.org/pid/163/6518.html), [Lei Ma](https://dblp.org/pid/20/6534-3.html), Felix Juefei-Xu, [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Yew-Soon Ong](https://dblp.org/pid/64/4136.html):

Metamorphic Relation Based Adversarial Attacks on Differentiable Neural Computer. [CoRRabs/1809.02444](https://dblp.org/db/journals/corr/corr1809.html#journals/corr/abs-1809-02444) (2018)
- ![](https://dblp.org/img/n.png)

\[i4\]
[Lei Ma](https://dblp.org/pid/20/6534-3.html), Felix Juefei-Xu, [Minhui Xue](https://dblp.org/pid/166/1912.html), [Qiang Hu](https://dblp.org/pid/93/5629.html), [Sen Chen](https://dblp.org/pid/180/8218-1.html), [Bo Li](https://dblp.org/pid/50/3402-26.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Jianjun Zhao](https://dblp.org/pid/71/6948-1.html), [Jianxiong Yin](https://dblp.org/pid/132/8514.html), [Simon See](https://dblp.org/pid/62/6547.html):

Secure Deep Learning Engineering: A Software Quality Assurance Perspective. [CoRRabs/1810.04538](https://dblp.org/db/journals/corr/corr1810.html#journals/corr/abs-1810-04538) (2018)
- ![](https://dblp.org/img/n.png)

\[i3\]
[Rahul Dey](https://dblp.org/pid/135/8801.html), Felix Juefei-Xu, [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

RankGAN: A Maximum Margin Ranking GAN for Generating Faces. [CoRRabs/1812.08196](https://dblp.org/db/journals/corr/corr1812.html#journals/corr/abs-1812-08196) (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[c25\]
Felix Juefei-Xu, [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Local Binary Convolutional Neural Networks. [CVPR2017](https://dblp.org/db/conf/cvpr/cvpr2017.html#conf/cvpr/Juefei-XuBS17): 4284-4293
- ![](https://dblp.org/img/n.png)

\[i2\]
Felix Juefei-Xu, [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Gang of GANs: Generative Adversarial Networks with Maximum Margin Ranking. [CoRRabs/1704.04865](https://dblp.org/db/journals/corr/corr1704.html#journals/corr/Juefei-XuBS17) (2017)
- 2016
- ![](https://dblp.org/img/n.png)

\[j3\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Multi-class Fukunaga Koontz discriminant analysis for enhanced face recognition. [Pattern Recognit.52](https://dblp.org/db/journals/pr/pr52.html#journals/pr/Juefei-XuS16): 186-205 (2016)
- ![](https://dblp.org/img/n.png)

\[c24\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Learning to Invert Local Binary Patterns. [BMVC2016](https://dblp.org/db/conf/bmvc/bmvc2016.html#conf/bmvc/Juefei-XuS16)
- ![](https://dblp.org/img/n.png)

\[c23\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Fastfood dictionary learning for periocular-based full face hallucination. [BTAS2016](https://dblp.org/db/conf/btas/btas2016.html#conf/btas/Juefei-XuS16): 1-8
- ![](https://dblp.org/img/n.png)

\[c22\]
Felix Juefei-Xu, [Eshan Verma](https://dblp.org/pid/191/9419.html), [Parag Goel](https://dblp.org/pid/191/9354.html), [Anisha Cherodian](https://dblp.org/pid/191/9414.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

DeepGender: Occlusion and Low Resolution Robust Facial Gender Classification via Progressively Trained Convolutional Neural Networks with Attention. [CVPR Workshops2016](https://dblp.org/db/conf/cvpr/cvprw2016.html#conf/cvpr/Juefei-XuVGCS16): 136-145
- ![](https://dblp.org/img/n.png)

\[c21\]
[Dipan K. Pal](https://dblp.org/pid/148/1005.html), Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Discriminative Invariant Kernel Features: A Bells-and-Whistles-Free Approach to Unsupervised Face Recognition and Pose Estimation. [CVPR2016](https://dblp.org/db/conf/cvpr/cvpr2016.html#conf/cvpr/PalJS16): 5590-5599
- ![](https://dblp.org/img/n.png)

\[c20\]
[Paul Buchana](https://dblp.org/pid/191/2612.html), [Irina Cazan](https://dblp.org/pid/169/3406.html), [Manuel Diaz-Granados](https://dblp.org/pid/173/9376.html), Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Simultaneous forgery identification and localization in paintings using advanced correlation filters. [ICIP2016](https://dblp.org/db/conf/icip/icip2016.html#conf/icip/BuchanaCDJS16): 146-150
- ![](https://dblp.org/img/n.png)

\[i1\]
Felix Juefei-Xu, [Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Local Binary Convolutional Neural Networks. [CoRRabs/1608.06049](https://dblp.org/db/journals/corr/corr1608.html#journals/corr/Juefei-XuBS16) (2016)
- 2015
- ![](https://dblp.org/img/n.png)

\[j2\]
Felix Juefei-Xu, [Khoa Luu](https://dblp.org/pid/43/8092.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Spartans: Single-Sample Periocular-Based Alignment-Robust Recognition Technique Applied to Non-Frontal Scenarios. [IEEE Trans. Image Process.24(12)](https://dblp.org/db/journals/tip/tip24.html#journals/tip/Juefei-XuLS15): 4780-4795 (2015)
- ![](https://dblp.org/img/n.png)

\[c19\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Pokerface: Partial order keeping and energy repressing method for extreme face illumination normalization. [BTAS2015](https://dblp.org/db/conf/btas/btas2015.html#conf/btas/Juefei-XuS15): 1-8
- ![](https://dblp.org/img/n.png)

\[c18\]
Felix Juefei-Xu, [Dipan K. Pal](https://dblp.org/pid/148/1005.html), [Karanhaar Singh](https://dblp.org/pid/11/10698.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

A preliminary investigation on the sensitivity of COTS face recognition systems to forensic analyst-style face processing for occlusions. [CVPR Workshops2015](https://dblp.org/db/conf/cvpr/cvprw2015.html#conf/cvpr/Juefei-XuPSS15): 25-33
- ![](https://dblp.org/img/n.png)

\[c17\]
[Keshav Seshadri](https://dblp.org/pid/95/10072.html), Felix Juefei-Xu, [Dipan K. Pal](https://dblp.org/pid/148/1005.html), [Marios Savvides](https://dblp.org/pid/13/3793.html), [Craig P. Thor](https://dblp.org/pid/169/9127.html):

Driver cell phone usage detection on Strategic Highway Research Program (SHRP2) face view videos. [CVPR Workshops2015](https://dblp.org/db/conf/cvpr/cvprw2015.html#conf/cvpr/SeshadriJPST15): 35-43
- ![](https://dblp.org/img/n.png)

\[c16\]
[Shreyas Venugopalan](https://dblp.org/pid/70/9171.html), Felix Juefei-Xu, [Benjamin Cowley](https://dblp.org/pid/36/3345-2.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Electromyograph and keystroke dynamics for spoof-resistant biometric authentication. [CVPR Workshops2015](https://dblp.org/db/conf/cvpr/cvprw2015.html#conf/cvpr/VenugopalanJCS15): 109-118
- ![](https://dblp.org/img/n.png)

\[c15\]
Felix Juefei-Xu, [Dipan K. Pal](https://dblp.org/pid/148/1005.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

NIR-VIS heterogeneous face recognition via cross-spectral joint dictionary learning and reconstruction. [CVPR Workshops2015](https://dblp.org/db/conf/cvpr/cvprw2015.html#conf/cvpr/Juefei-XuPS15): 141-150
- ![](https://dblp.org/img/n.png)

\[c14\]
[Niv Zehngut](https://dblp.org/pid/172/9934.html), Felix Juefei-Xu, [Rishabh Bardia](https://dblp.org/pid/172/9907.html), [Dipan K. Pal](https://dblp.org/pid/148/1005.html), [Chandrasekhar Bhagavatula](https://dblp.org/pid/126/4520.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Investigating the feasibility of image-based nose biometrics. [ICIP2015](https://dblp.org/db/conf/icip/icip2015.html#conf/icip/ZehngutJBPBS15): 522-526
- ![](https://dblp.org/img/n.png)

\[c13\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Pareto-optimal discriminant analysis. [ICIP2015](https://dblp.org/db/conf/icip/icip2015.html#conf/icip/Juefei-XuS15): 611-615
- ![](https://dblp.org/img/n.png)

\[c12\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Single face image super-resolution via solo dictionary learning. [ICIP2015](https://dblp.org/db/conf/icip/icip2015.html#conf/icip/Juefei-XuS15a): 2239-2243
- ![](https://dblp.org/img/n.png)

\[c11\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Encoding and decoding local binary patterns for harsh face illumination normalization. [ICIP2015](https://dblp.org/db/conf/icip/icip2015.html#conf/icip/Juefei-XuS15b): 3220-3224
- 2014
- ![](https://dblp.org/img/n.png)

\[j1\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Subspace-Based Discrete Transform Encoded Local Binary Patterns Representations for Robust Periocular Matching on NIST's Face Recognition Grand Challenge. [IEEE Trans. Image Process.23(8)](https://dblp.org/db/journals/tip/tip23.html#journals/tip/Juefei-XuS14): 3490-3505 (2014)
- ![](https://dblp.org/img/n.png)

\[c10\]
Felix Juefei-Xu, [Dipan K. Pal](https://dblp.org/pid/148/1005.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Hallucinating the Full Face from the Periocular Region via Dimensionally Weighted K-SVD. [CVPR Workshops2014](https://dblp.org/db/conf/cvpr/cvprw2014.html#conf/cvpr/Juefei-XuPS14): 1-8
- ![](https://dblp.org/img/n.png)

\[c9\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Weight-Optimal Local Binary Patterns. [ECCV Workshops (2)2014](https://dblp.org/db/conf/eccv/eccv2014w2.html#conf/eccv/Juefei-XuS14): 148-159
- ![](https://dblp.org/img/n.png)

\[c8\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Facial Ethnic Appearance Synthesis. [ECCV Workshops (2)2014](https://dblp.org/db/conf/eccv/eccv2014w2.html#conf/eccv/Juefei-XuS14a): 825-840
- 2013
- ![](https://dblp.org/img/n.png)

\[c7\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

An image statistics approach towards efficient and robust refinement for landmarks on facial boundary. [BTAS2013](https://dblp.org/db/conf/btas/btas2013.html#conf/btas/Juefei-XuS13): 1-8
- ![](https://dblp.org/img/n.png)

\[c6\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

An Augmented Linear Discriminant Analysis Approach for Identifying Identical Twins with the Aid of Facial Asymmetry Features. [CVPR Workshops2013](https://dblp.org/db/conf/cvpr/cvprw2013.html#conf/cvpr/Juefei-XuS13): 56-63
- 2012
- ![](https://dblp.org/img/n.png)

\[c5\]
Felix Juefei-Xu, [Chandrasekhar Bhagavatula](https://dblp.org/pid/126/4520.html), [Aaron Jaech](https://dblp.org/pid/120/8500.html), [Unni Prasad](https://dblp.org/pid/120/8492.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Gait-ID on the move: Pace independent human identification using cell phone accelerometer dynamics. [BTAS2012](https://dblp.org/db/conf/btas/btas2012.html#conf/btas/Juefei-XuBJPS12): 8-15
- ![](https://dblp.org/img/n.png)

\[c4\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Unconstrained periocular biometric acquisition and recognition using COTS PTZ camera for uncooperative and non-cooperative subjects. [WACV2012](https://dblp.org/db/conf/wacv/wacv2012.html#conf/wacv/Juefei-XuS12): 201-208
- 2011
- ![](https://dblp.org/img/n.png)

\[c3\]
Felix Juefei-Xu, [Khoa Luu](https://dblp.org/pid/43/8092.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), [Ching Y. Suen](https://dblp.org/pid/s/ChingYSuen.html):

Investigating age invariant face recognition based on periocular biometrics. [IJCB2011](https://dblp.org/db/conf/icb/ijcb2011.html#conf/icb/Juefei-XuLSBS11): 1-7
- ![](https://dblp.org/img/n.png)

\[c2\]
Felix Juefei-Xu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Can your eyebrows tell me who you are? [ICSPCS2011](https://dblp.org/db/conf/icspcs/icspcs2011.html#conf/icspcs/Juefei-XuS11): 1-8
- 2010
- ![](https://dblp.org/img/n.png)

\[c1\]
Juefei Xu, [Miriam Cha](https://dblp.org/pid/86/9878.html), [Joseph Heyman](https://dblp.org/pid/49/4607.html), [Shreyas Venugopalan](https://dblp.org/pid/70/9171.html), [Ramzi Abiantun](https://dblp.org/pid/72/989.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Robust local binary pattern feature sets for periocular biometric identification. [BTAS2010](https://dblp.org/db/conf/btas/btas2010.html#conf/btas/XuCHVAS10): 1-8
- _no results_

automatic loading of the coauthor graph disabled due to its size.

**click here to**
**load the graph.**

Note that this feature is _work in progress_ and that it is still far from being perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/35/11103.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[2](https://dblp.org/pid/35/11103.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ramzi Abiantun](https://dblp.org/pid/72/989.html)

[\[j4\]](https://dblp.org/pid/35/11103.html#j4) [\[c1\]](https://dblp.org/pid/35/11103.html#c1)

[3](https://dblp.org/pid/35/11103.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Seyed Matin Tavakoli Afshari](https://dblp.org/pid/407/9056.html)

[\[j18\]](https://dblp.org/pid/35/11103.html#j18)

[4](https://dblp.org/pid/35/11103.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Adarsh Agrawal](https://dblp.org/pid/375/6968.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[5](https://dblp.org/pid/35/11103.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ahmed M. Ahmed 0004](https://dblp.org/pid/294/5028.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[6](https://dblp.org/pid/35/11103.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Faez Ahmed](https://dblp.org/pid/45/10603.html)

[\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[7](https://dblp.org/pid/35/11103.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Victor Akinwande](https://dblp.org/pid/211/6825.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[8](https://dblp.org/pid/35/11103.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Namir Al-Nuaimi](https://dblp.org/pid/375/6416.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[9](https://dblp.org/pid/35/11103.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Najla Alfaraj](https://dblp.org/pid/10/8405.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[10](https://dblp.org/pid/35/11103.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Elie Alhajjar](https://dblp.org/pid/259/6812.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[11](https://dblp.org/pid/35/11103.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bo An 0001](https://dblp.org/pid/42/6178-1.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[12](https://dblp.org/pid/35/11103.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Lora Aroyo](https://dblp.org/pid/42/6100.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[13](https://dblp.org/pid/35/11103.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Samaneh Azadi](https://dblp.org/pid/145/9932.html)

[\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[i95\]](https://dblp.org/pid/35/11103.html#i95)

[14](https://dblp.org/pid/35/11103.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiamu Bai](https://dblp.org/pid/331/3706.html)

[\[c57\]](https://dblp.org/pid/35/11103.html#c57) [\[i57\]](https://dblp.org/pid/35/11103.html#i57)

[15](https://dblp.org/pid/35/11103.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Lei Bai 0001](https://dblp.org/pid/119/1223-1.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[16](https://dblp.org/pid/35/11103.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Minhao Bai](https://dblp.org/pid/361/3951.html)

[\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[17](https://dblp.org/pid/35/11103.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Mohit Bansal](https://dblp.org/pid/32/5243.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91) [\[i84\]](https://dblp.org/pid/35/11103.html#i84)

[18](https://dblp.org/pid/35/11103.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Rishabh Bardia](https://dblp.org/pid/172/9907.html)

[\[c14\]](https://dblp.org/pid/35/11103.html#c14)

[19](https://dblp.org/pid/35/11103.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Trupti Bavalatti](https://dblp.org/pid/375/7726.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[20](https://dblp.org/pid/35/11103.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chandrasekhar Bhagavatula](https://dblp.org/pid/126/4520.html)

[\[c14\]](https://dblp.org/pid/35/11103.html#c14) [\[c5\]](https://dblp.org/pid/35/11103.html#c5)

[21](https://dblp.org/pid/35/11103.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[22](https://dblp.org/pid/35/11103.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Borhane Blili-Hamelin](https://dblp.org/pid/329/1972.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[23](https://dblp.org/pid/35/11103.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Vishnu Naresh Boddeti](https://dblp.org/pid/55/6988.html)

[\[j15\]](https://dblp.org/pid/35/11103.html#j15) [\[j13\]](https://dblp.org/pid/35/11103.html#j13) [\[c55\]](https://dblp.org/pid/35/11103.html#c55) [\[i58\]](https://dblp.org/pid/35/11103.html#i58) [\[i53\]](https://dblp.org/pid/35/11103.html#i53) [\[i45\]](https://dblp.org/pid/35/11103.html#i45) [\[c29\]](https://dblp.org/pid/35/11103.html#c29) [\[c28\]](https://dblp.org/pid/35/11103.html#c28) [\[i7\]](https://dblp.org/pid/35/11103.html#i7) [\[i3\]](https://dblp.org/pid/35/11103.html#i3) [\[c25\]](https://dblp.org/pid/35/11103.html#c25) [\[i2\]](https://dblp.org/pid/35/11103.html#i2) [\[i1\]](https://dblp.org/pid/35/11103.html#i1)

[24](https://dblp.org/pid/35/11103.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kurt Bollacker](https://dblp.org/pid/64/4571.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[25](https://dblp.org/pid/35/11103.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Rishi Bomassani](https://dblp.org/pid/375/6407.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[26](https://dblp.org/pid/35/11103.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Marisa Ferrara Boston](https://dblp.org/pid/24/8160.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[27](https://dblp.org/pid/35/11103.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Paul Buchana](https://dblp.org/pid/191/2612.html)

[\[c20\]](https://dblp.org/pid/35/11103.html#c20)

[28](https://dblp.org/pid/35/11103.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tien D. Bui](https://dblp.org/pid/b/TienDBui.html)

[\[c3\]](https://dblp.org/pid/35/11103.html#c3)

[29](https://dblp.org/pid/35/11103.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yuanhao Cai](https://dblp.org/pid/260/1004.html)

[\[i83\]](https://dblp.org/pid/35/11103.html#i83)

[30](https://dblp.org/pid/35/11103.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yuzhu Cai](https://dblp.org/pid/375/7444.html)

[\[j27\]](https://dblp.org/pid/35/11103.html#j27) [\[i77\]](https://dblp.org/pid/35/11103.html#i77)

[31](https://dblp.org/pid/35/11103.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Siméon Campos](https://dblp.org/pid/375/6457.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[32](https://dblp.org/pid/35/11103.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiannong Cao 0001](https://dblp.org/pid/c/JiannongCao.html)

[\[j15\]](https://dblp.org/pid/35/11103.html#j15) [\[i45\]](https://dblp.org/pid/35/11103.html#i45)

[33](https://dblp.org/pid/35/11103.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaochun Cao](https://dblp.org/pid/39/3695.html)

[\[j20\]](https://dblp.org/pid/35/11103.html#j20) [\[i72\]](https://dblp.org/pid/35/11103.html#i72)

[34](https://dblp.org/pid/35/11103.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xinye Cao](https://dblp.org/pid/322/9121.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[35](https://dblp.org/pid/35/11103.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yue Cao](https://dblp.org/pid/74/5570.html)

[\[i86\]](https://dblp.org/pid/35/11103.html#i86) [\[i54\]](https://dblp.org/pid/35/11103.html#i54)

[36](https://dblp.org/pid/35/11103.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Irina Cazan](https://dblp.org/pid/169/3406.html)

[\[c20\]](https://dblp.org/pid/35/11103.html#c20)

[37](https://dblp.org/pid/35/11103.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[38](https://dblp.org/pid/35/11103.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Llukman Cerkezi](https://dblp.org/pid/208/1312.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[39](https://dblp.org/pid/35/11103.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hakan Çevikalp](https://dblp.org/pid/14/6210.html)

aka: Hakan Cevikalp

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[40](https://dblp.org/pid/35/11103.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Miriam Cha](https://dblp.org/pid/86/9878.html)

[\[c1\]](https://dblp.org/pid/35/11103.html#c1)

[41](https://dblp.org/pid/35/11103.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kal Chakra](https://dblp.org/pid/375/7683.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[42](https://dblp.org/pid/35/11103.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Alvin Chan](https://dblp.org/pid/163/6518.html)

[\[j7\]](https://dblp.org/pid/35/11103.html#j7) [\[i5\]](https://dblp.org/pid/35/11103.html#i5)

[43](https://dblp.org/pid/35/11103.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wen Le Chan](https://dblp.org/pid/274/7365.html)

[\[c44\]](https://dblp.org/pid/35/11103.html#c44) [\[i15\]](https://dblp.org/pid/35/11103.html#i15)

[44](https://dblp.org/pid/35/11103.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[45](https://dblp.org/pid/35/11103.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Canyu Chen](https://dblp.org/pid/319/2330.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[46](https://dblp.org/pid/35/11103.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chao Chen](https://dblp.org/pid/66/3019.html)

[\[c66\]](https://dblp.org/pid/35/11103.html#c66) [\[i50\]](https://dblp.org/pid/35/11103.html#i50)

[47](https://dblp.org/pid/35/11103.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chunyang Chen 0001](https://dblp.org/pid/180/7246.html)

[\[c26\]](https://dblp.org/pid/35/11103.html#c26) [\[i9\]](https://dblp.org/pid/35/11103.html#i9)

[48](https://dblp.org/pid/35/11103.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hongxu Chen 0001](https://dblp.org/pid/147/5824-1.html)

[\[c31\]](https://dblp.org/pid/35/11103.html#c31) [\[i6\]](https://dblp.org/pid/35/11103.html#i6)

[49](https://dblp.org/pid/35/11103.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Huaming Chen](https://dblp.org/pid/139/3914.html)

[\[j22\]](https://dblp.org/pid/35/11103.html#j22)

[50](https://dblp.org/pid/35/11103.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jianfa Chen](https://dblp.org/pid/319/6731.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[i96\]](https://dblp.org/pid/35/11103.html#i96)

[51](https://dblp.org/pid/35/11103.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jianlang Chen](https://dblp.org/pid/307/5450.html)

[\[c60\]](https://dblp.org/pid/35/11103.html#c60) [\[i78\]](https://dblp.org/pid/35/11103.html#i78) [\[j14\]](https://dblp.org/pid/35/11103.html#j14) [\[j11\]](https://dblp.org/pid/35/11103.html#j11) [\[i44\]](https://dblp.org/pid/35/11103.html#i44) [\[i28\]](https://dblp.org/pid/35/11103.html#i28)

[52](https://dblp.org/pid/35/11103.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jing Chen](https://dblp.org/pid/27/4364.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[53](https://dblp.org/pid/35/11103.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiuhai Chen](https://dblp.org/pid/263/3943.html)

[\[i92\]](https://dblp.org/pid/35/11103.html#i92)

[54](https://dblp.org/pid/35/11103.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Junze Chen](https://dblp.org/pid/262/5385.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[55](https://dblp.org/pid/35/11103.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Lei Chen](https://dblp.org/pid/09/3666.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[56](https://dblp.org/pid/35/11103.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Li Chen](https://dblp.org/pid/181/2847.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[i96\]](https://dblp.org/pid/35/11103.html#i96) [\[i67\]](https://dblp.org/pid/35/11103.html#i67) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[57](https://dblp.org/pid/35/11103.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Nuo Chen 0003](https://dblp.org/pid/135/5622-3.html)

[\[i71\]](https://dblp.org/pid/35/11103.html#i71)

[58](https://dblp.org/pid/35/11103.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Pengyu Chen](https://dblp.org/pid/142/3636.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[59](https://dblp.org/pid/35/11103.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qingyu Chen 0001](https://dblp.org/pid/28/5691-1.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[60](https://dblp.org/pid/35/11103.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Sen Chen 0001](https://dblp.org/pid/180/8218-1.html)

[\[i4\]](https://dblp.org/pid/35/11103.html#i4)

[61](https://dblp.org/pid/35/11103.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[j11\]](https://dblp.org/pid/35/11103.html#j11) [\[i44\]](https://dblp.org/pid/35/11103.html#i44) [\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[62](https://dblp.org/pid/35/11103.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Siheng Chen](https://dblp.org/pid/136/4945.html)

[\[j27\]](https://dblp.org/pid/35/11103.html#j27) [\[i77\]](https://dblp.org/pid/35/11103.html#i77) [\[c57\]](https://dblp.org/pid/35/11103.html#c57) [\[i57\]](https://dblp.org/pid/35/11103.html#i57)

[63](https://dblp.org/pid/35/11103.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tianlong Chen 0001](https://dblp.org/pid/68/10575-1.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[64](https://dblp.org/pid/35/11103.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Weifeng Chen](https://dblp.org/pid/74/5429.html)

[\[i84\]](https://dblp.org/pid/35/11103.html#i84) [\[i83\]](https://dblp.org/pid/35/11103.html#i83)

[65](https://dblp.org/pid/35/11103.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wenhu Chen](https://dblp.org/pid/136/0957.html)

[\[i93\]](https://dblp.org/pid/35/11103.html#i93)

[66](https://dblp.org/pid/35/11103.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[67](https://dblp.org/pid/35/11103.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xinyun Chen](https://dblp.org/pid/03/8495.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[68](https://dblp.org/pid/35/11103.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Miao Cheng](https://dblp.org/pid/79/7377.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[69](https://dblp.org/pid/35/11103.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ran Cheng 0004](https://dblp.org/pid/18/4198-4.html)

[\[c55\]](https://dblp.org/pid/35/11103.html#c55) [\[i53\]](https://dblp.org/pid/35/11103.html#i53)

[70](https://dblp.org/pid/35/11103.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yupeng Cheng](https://dblp.org/pid/148/8300.html)

[\[j25\]](https://dblp.org/pid/35/11103.html#j25) [\[j8\]](https://dblp.org/pid/35/11103.html#j8) [\[c44\]](https://dblp.org/pid/35/11103.html#c44) [\[i20\]](https://dblp.org/pid/35/11103.html#i20) [\[i17\]](https://dblp.org/pid/35/11103.html#i17) [\[i15\]](https://dblp.org/pid/35/11103.html#i15)

[71](https://dblp.org/pid/35/11103.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ziyi Cheng](https://dblp.org/pid/290/9342.html)

[\[c47\]](https://dblp.org/pid/35/11103.html#c47) [\[c46\]](https://dblp.org/pid/35/11103.html#c46) [\[c45\]](https://dblp.org/pid/35/11103.html#c45) [\[i39\]](https://dblp.org/pid/35/11103.html#i39) [\[i32\]](https://dblp.org/pid/35/11103.html#i32)

[72](https://dblp.org/pid/35/11103.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Anisha Cherodian](https://dblp.org/pid/191/9414.html)

[\[c22\]](https://dblp.org/pid/35/11103.html#c22)

[73](https://dblp.org/pid/35/11103.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Vincent Cheung](https://dblp.org/pid/47/5789.html)

[\[i67\]](https://dblp.org/pid/35/11103.html#i67)

[74](https://dblp.org/pid/35/11103.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yu-Chen Chiu](https://dblp.org/pid/199/2494.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[75](https://dblp.org/pid/35/11103.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ching-Yao Chuang](https://dblp.org/pid/190/7522.html)

[\[i88\]](https://dblp.org/pid/35/11103.html#i88)

[76](https://dblp.org/pid/35/11103.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ozgun Cirakman](https://dblp.org/pid/86/8843.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[77](https://dblp.org/pid/35/11103.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Cody Coleman](https://dblp.org/pid/222/1849.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[78](https://dblp.org/pid/35/11103.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zacharie Delpierre Coudert](https://dblp.org/pid/375/6531.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[79](https://dblp.org/pid/35/11103.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Benjamin Cowley 0002](https://dblp.org/pid/36/3345-2.html)

[\[c16\]](https://dblp.org/pid/35/11103.html#c16)

[80](https://dblp.org/pid/35/11103.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[81](https://dblp.org/pid/35/11103.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kenan Dai](https://dblp.org/pid/250/4445.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[82](https://dblp.org/pid/35/11103.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaoliang Dai](https://dblp.org/pid/192/3904.html)

[\[i97\]](https://dblp.org/pid/35/11103.html#i97) [\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[c70\]](https://dblp.org/pid/35/11103.html#c70) [\[i95\]](https://dblp.org/pid/35/11103.html#i95) [\[i93\]](https://dblp.org/pid/35/11103.html#i93) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i87\]](https://dblp.org/pid/35/11103.html#i87) [\[i83\]](https://dblp.org/pid/35/11103.html#i83) [\[i63\]](https://dblp.org/pid/35/11103.html#i63) [\[i62\]](https://dblp.org/pid/35/11103.html#i62) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[83](https://dblp.org/pid/35/11103.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[84](https://dblp.org/pid/35/11103.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Quan Dao](https://dblp.org/pid/334/7610.html)

[\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[85](https://dblp.org/pid/35/11103.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html)

[\[i85\]](https://dblp.org/pid/35/11103.html#i85)

[86](https://dblp.org/pid/35/11103.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[87](https://dblp.org/pid/35/11103.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Abe Davis](https://dblp.org/pid/117/4799.html)

[\[i87\]](https://dblp.org/pid/35/11103.html#i87)

[88](https://dblp.org/pid/35/11103.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Gelei Deng](https://dblp.org/pid/236/9144.html)

[\[c54\]](https://dblp.org/pid/35/11103.html#c54) [\[i52\]](https://dblp.org/pid/35/11103.html#i52)

[89](https://dblp.org/pid/35/11103.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[90](https://dblp.org/pid/35/11103.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Leon Derczynski](https://dblp.org/pid/66/8157.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[91](https://dblp.org/pid/35/11103.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Rahul Dey](https://dblp.org/pid/135/8801.html)

[\[c29\]](https://dblp.org/pid/35/11103.html#c29) [\[i3\]](https://dblp.org/pid/35/11103.html#i3)

[92](https://dblp.org/pid/35/11103.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Manuel Diaz-Granados](https://dblp.org/pid/173/9376.html)

[\[c20\]](https://dblp.org/pid/35/11103.html#c20)

[93](https://dblp.org/pid/35/11103.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chuntao Ding](https://dblp.org/pid/150/4003.html)

[\[j15\]](https://dblp.org/pid/35/11103.html#j15) [\[j13\]](https://dblp.org/pid/35/11103.html#j13) [\[c55\]](https://dblp.org/pid/35/11103.html#c55) [\[i58\]](https://dblp.org/pid/35/11103.html#i58) [\[i53\]](https://dblp.org/pid/35/11103.html#i53) [\[i45\]](https://dblp.org/pid/35/11103.html#i45)

[94](https://dblp.org/pid/35/11103.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kaize Ding](https://dblp.org/pid/234/6878.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[95](https://dblp.org/pid/35/11103.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yi Ding 0012](https://dblp.org/pid/89/5503-12.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[96](https://dblp.org/pid/35/11103.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Haotian Dong](https://dblp.org/pid/314/2870.html)

[\[j23\]](https://dblp.org/pid/35/11103.html#j23)

[97](https://dblp.org/pid/35/11103.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Meng Dong](https://dblp.org/pid/58/2821.html)

[\[i97\]](https://dblp.org/pid/35/11103.html#i97)

[98](https://dblp.org/pid/35/11103.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ruihai Dong](https://dblp.org/pid/94/11082.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[99](https://dblp.org/pid/35/11103.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xingping Dong](https://dblp.org/pid/156/3020.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[100](https://dblp.org/pid/35/11103.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[101](https://dblp.org/pid/35/11103.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[102](https://dblp.org/pid/35/11103.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hao Du](https://dblp.org/pid/13/6441.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[103](https://dblp.org/pid/35/11103.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yao Du 0002](https://dblp.org/pid/166/4113-2.html)

[\[c56\]](https://dblp.org/pid/35/11103.html#c56) [\[c54\]](https://dblp.org/pid/35/11103.html#c54) [\[i52\]](https://dblp.org/pid/35/11103.html#i52)

[104](https://dblp.org/pid/35/11103.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yann Dubois](https://dblp.org/pid/198/7527.html)

[\[c69\]](https://dblp.org/pid/35/11103.html#c69) [\[i61\]](https://dblp.org/pid/35/11103.html#i61)

[105](https://dblp.org/pid/35/11103.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[106](https://dblp.org/pid/35/11103.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Debojyoti Dutta](https://dblp.org/pid/96/2340.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[107](https://dblp.org/pid/35/11103.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ian Eisenberg](https://dblp.org/pid/324/8716.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[108](https://dblp.org/pid/35/11103.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ahmed M. Elgammal](https://dblp.org/pid/e/AhmedMElgammal.html)

aka: Ahmed Elgammal

[\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[109](https://dblp.org/pid/35/11103.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yuval Elovici](https://dblp.org/pid/38/4086.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[110](https://dblp.org/pid/35/11103.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Alireza Esmaeilzehi](https://dblp.org/pid/198/7073.html)

[\[j18\]](https://dblp.org/pid/35/11103.html#j18)

[111](https://dblp.org/pid/35/11103.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[James Ezick](https://dblp.org/pid/317/2495.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[112](https://dblp.org/pid/35/11103.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhipeng Fan](https://dblp.org/pid/228/6404.html)

[\[i97\]](https://dblp.org/pid/35/11103.html#i97) [\[i84\]](https://dblp.org/pid/35/11103.html#i84)

[113](https://dblp.org/pid/35/11103.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jianwu Fang](https://dblp.org/pid/142/0412.html)

[\[c59\]](https://dblp.org/pid/35/11103.html#c59) [\[i82\]](https://dblp.org/pid/35/11103.html#i82)

[114](https://dblp.org/pid/35/11103.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Junfeng Fang](https://dblp.org/pid/340/7929.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[115](https://dblp.org/pid/35/11103.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qi Fang](https://dblp.org/pid/35/5244.html)

[\[c57\]](https://dblp.org/pid/35/11103.html#c57) [\[i57\]](https://dblp.org/pid/35/11103.html#i57)

[116](https://dblp.org/pid/35/11103.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Matt Feiszli](https://dblp.org/pid/182/8255.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90)

[117](https://dblp.org/pid/35/11103.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[118](https://dblp.org/pid/35/11103.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Aosong Feng](https://dblp.org/pid/260/0450.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[119](https://dblp.org/pid/35/11103.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chen Feng 0002](https://dblp.org/pid/01/161-2.html)

[\[c66\]](https://dblp.org/pid/35/11103.html#c66) [\[i71\]](https://dblp.org/pid/35/11103.html#i71) [\[c57\]](https://dblp.org/pid/35/11103.html#c57) [\[i57\]](https://dblp.org/pid/35/11103.html#i57) [\[i50\]](https://dblp.org/pid/35/11103.html#i50) [\[c48\]](https://dblp.org/pid/35/11103.html#c48) [\[i40\]](https://dblp.org/pid/35/11103.html#i40)

[120](https://dblp.org/pid/35/11103.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jincao Feng](https://dblp.org/pid/255/5597.html)

[\[c53\]](https://dblp.org/pid/35/11103.html#c53) [\[i48\]](https://dblp.org/pid/35/11103.html#i48)

[121](https://dblp.org/pid/35/11103.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wei Feng 0005](https://dblp.org/pid/17/1152-5.html)

[\[j29\]](https://dblp.org/pid/35/11103.html#j29) [\[j28\]](https://dblp.org/pid/35/11103.html#j28) [\[j23\]](https://dblp.org/pid/35/11103.html#j23) [\[j19\]](https://dblp.org/pid/35/11103.html#j19) [\[c60\]](https://dblp.org/pid/35/11103.html#c60) [\[c58\]](https://dblp.org/pid/35/11103.html#c58) [\[i78\]](https://dblp.org/pid/35/11103.html#i78) [\[j8\]](https://dblp.org/pid/35/11103.html#j8) [\[c52\]](https://dblp.org/pid/35/11103.html#c52) [\[i49\]](https://dblp.org/pid/35/11103.html#i49) [\[c50\]](https://dblp.org/pid/35/11103.html#c50) [\[c49\]](https://dblp.org/pid/35/11103.html#c49) [\[i41\]](https://dblp.org/pid/35/11103.html#i41) [\[i38\]](https://dblp.org/pid/35/11103.html#i38) [\[i31\]](https://dblp.org/pid/35/11103.html#i31) [\[i30\]](https://dblp.org/pid/35/11103.html#i30) [\[i27\]](https://dblp.org/pid/35/11103.html#i27) [\[c39\]](https://dblp.org/pid/35/11103.html#c39) [\[c33\]](https://dblp.org/pid/35/11103.html#c33) [\[c32\]](https://dblp.org/pid/35/11103.html#c32) [\[i25\]](https://dblp.org/pid/35/11103.html#i25) [\[i22\]](https://dblp.org/pid/35/11103.html#i22) [\[i20\]](https://dblp.org/pid/35/11103.html#i20) [\[i19\]](https://dblp.org/pid/35/11103.html#i19) [\[i16\]](https://dblp.org/pid/35/11103.html#i16) [\[i14\]](https://dblp.org/pid/35/11103.html#i14)

[122](https://dblp.org/pid/35/11103.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[123](https://dblp.org/pid/35/11103.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhiyong Feng 0001](https://dblp.org/pid/48/195-1.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[124](https://dblp.org/pid/35/11103.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[125](https://dblp.org/pid/35/11103.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Heather Frase](https://dblp.org/pid/348/5691.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[126](https://dblp.org/pid/35/11103.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Huazhu Fu](https://dblp.org/pid/63/7767.html)

[\[j25\]](https://dblp.org/pid/35/11103.html#j25) [\[c52\]](https://dblp.org/pid/35/11103.html#c52) [\[i17\]](https://dblp.org/pid/35/11103.html#i17)

[127](https://dblp.org/pid/35/11103.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jinhu Fu](https://dblp.org/pid/343/9545.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[128](https://dblp.org/pid/35/11103.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Lan Fu](https://dblp.org/pid/265/9476.html)

[\[c58\]](https://dblp.org/pid/35/11103.html#c58) [\[j10\]](https://dblp.org/pid/35/11103.html#j10) [\[c49\]](https://dblp.org/pid/35/11103.html#c49) [\[i41\]](https://dblp.org/pid/35/11103.html#i41) [\[i37\]](https://dblp.org/pid/35/11103.html#i37) [\[i27\]](https://dblp.org/pid/35/11103.html#i27)

[129](https://dblp.org/pid/35/11103.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tsu-Jui Fu](https://dblp.org/pid/218/5366.html)

[\[i85\]](https://dblp.org/pid/35/11103.html#i85)

[130](https://dblp.org/pid/35/11103.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yun Fu](https://dblp.org/pid/00/5815.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90)

[131](https://dblp.org/pid/35/11103.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[132](https://dblp.org/pid/35/11103.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Brian Fuller](https://dblp.org/pid/50/6951.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[133](https://dblp.org/pid/35/11103.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ram Gandikota](https://dblp.org/pid/375/6649.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[134](https://dblp.org/pid/35/11103.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Agasthya Gangavarapu](https://dblp.org/pid/337/8985.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[135](https://dblp.org/pid/35/11103.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ananya Gangavarapu](https://dblp.org/pid/275/3568.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[136](https://dblp.org/pid/35/11103.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Fan Gao](https://dblp.org/pid/51/3982.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[137](https://dblp.org/pid/35/11103.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ruijun Gao](https://dblp.org/pid/247/5683.html)

[\[j19\]](https://dblp.org/pid/35/11103.html#j19) [\[c52\]](https://dblp.org/pid/35/11103.html#c52) [\[i38\]](https://dblp.org/pid/35/11103.html#i38) [\[i30\]](https://dblp.org/pid/35/11103.html#i30) [\[i14\]](https://dblp.org/pid/35/11103.html#i14)

[138](https://dblp.org/pid/35/11103.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shiming Ge](https://dblp.org/pid/93/8104.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[139](https://dblp.org/pid/35/11103.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[James Gealy](https://dblp.org/pid/375/6060.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[140](https://dblp.org/pid/35/11103.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Markos Georgopoulos](https://dblp.org/pid/197/6876.html)

[\[i87\]](https://dblp.org/pid/35/11103.html#i87)

[141](https://dblp.org/pid/35/11103.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Marjan Ghazvininejad](https://dblp.org/pid/50/10813.html)

[\[i87\]](https://dblp.org/pid/35/11103.html#i87)

[142](https://dblp.org/pid/35/11103.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Rajat Ghosh](https://dblp.org/pid/199/6924.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[143](https://dblp.org/pid/35/11103.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Randy Goebel](https://dblp.org/pid/g/RandyGoebel.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[144](https://dblp.org/pid/35/11103.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[James Goel](https://dblp.org/pid/229/5357.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[145](https://dblp.org/pid/35/11103.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Parag Goel](https://dblp.org/pid/191/9354.html)

[\[c22\]](https://dblp.org/pid/35/11103.html#c22)

[146](https://dblp.org/pid/35/11103.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Usman Gohar](https://dblp.org/pid/336/1779.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[147](https://dblp.org/pid/35/11103.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[148](https://dblp.org/pid/35/11103.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[149](https://dblp.org/pid/35/11103.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Subhra S. Goswami](https://dblp.org/pid/272/0914.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[150](https://dblp.org/pid/35/11103.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shangding Gu](https://dblp.org/pid/268/8183.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[151](https://dblp.org/pid/35/11103.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yuzhang Gu](https://dblp.org/pid/122/3790.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[152](https://dblp.org/pid/35/11103.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zeqi Gu](https://dblp.org/pid/230/4614.html)

[\[i87\]](https://dblp.org/pid/35/11103.html#i87)

[153](https://dblp.org/pid/35/11103.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bilge Günsel](https://dblp.org/pid/47/5125.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[154](https://dblp.org/pid/35/11103.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chongye Guo](https://dblp.org/pid/161/6616.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[155](https://dblp.org/pid/35/11103.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qing Guo](https://dblp.org/pid/25/3038.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[156](https://dblp.org/pid/35/11103.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qing Guo 0003](https://dblp.org/pid/25/3038-3.html)

[\[j29\]](https://dblp.org/pid/35/11103.html#j29)

[157](https://dblp.org/pid/35/11103.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qing Guo 0005](https://dblp.org/pid/25/3038-5.html)

[\[j28\]](https://dblp.org/pid/35/11103.html#j28) [\[j26\]](https://dblp.org/pid/35/11103.html#j26) [\[j25\]](https://dblp.org/pid/35/11103.html#j25) [\[j24\]](https://dblp.org/pid/35/11103.html#j24) [\[j23\]](https://dblp.org/pid/35/11103.html#j23) [\[c75\]](https://dblp.org/pid/35/11103.html#c75) [\[i94\]](https://dblp.org/pid/35/11103.html#i94) [\[i89\]](https://dblp.org/pid/35/11103.html#i89) [\[i86\]](https://dblp.org/pid/35/11103.html#i86) [\[j21\]](https://dblp.org/pid/35/11103.html#j21) [\[j20\]](https://dblp.org/pid/35/11103.html#j20) [\[j19\]](https://dblp.org/pid/35/11103.html#j19) [\[j18\]](https://dblp.org/pid/35/11103.html#j18) [\[j17\]](https://dblp.org/pid/35/11103.html#j17) [\[c64\]](https://dblp.org/pid/35/11103.html#c64) [\[c63\]](https://dblp.org/pid/35/11103.html#c63) [\[c62\]](https://dblp.org/pid/35/11103.html#c62) [\[c61\]](https://dblp.org/pid/35/11103.html#c61) [\[c60\]](https://dblp.org/pid/35/11103.html#c60) [\[c59\]](https://dblp.org/pid/35/11103.html#c59) [\[c58\]](https://dblp.org/pid/35/11103.html#c58) [\[i82\]](https://dblp.org/pid/35/11103.html#i82) [\[i81\]](https://dblp.org/pid/35/11103.html#i81) [\[i80\]](https://dblp.org/pid/35/11103.html#i80) [\[i79\]](https://dblp.org/pid/35/11103.html#i79) [\[i78\]](https://dblp.org/pid/35/11103.html#i78) [\[i75\]](https://dblp.org/pid/35/11103.html#i75) [\[i74\]](https://dblp.org/pid/35/11103.html#i74) [\[i72\]](https://dblp.org/pid/35/11103.html#i72) [\[i59\]](https://dblp.org/pid/35/11103.html#i59) [\[j14\]](https://dblp.org/pid/35/11103.html#j14) [\[c53\]](https://dblp.org/pid/35/11103.html#c53) [\[i56\]](https://dblp.org/pid/35/11103.html#i56) [\[i55\]](https://dblp.org/pid/35/11103.html#i55) [\[i54\]](https://dblp.org/pid/35/11103.html#i54) [\[j12\]](https://dblp.org/pid/35/11103.html#j12) [\[j11\]](https://dblp.org/pid/35/11103.html#j11) [\[j10\]](https://dblp.org/pid/35/11103.html#j10) [\[j9\]](https://dblp.org/pid/35/11103.html#j9) [\[j8\]](https://dblp.org/pid/35/11103.html#j8) [\[j6\]](https://dblp.org/pid/35/11103.html#j6) [\[j5\]](https://dblp.org/pid/35/11103.html#j5) [\[c52\]](https://dblp.org/pid/35/11103.html#c52) [\[c51\]](https://dblp.org/pid/35/11103.html#c51) [\[i49\]](https://dblp.org/pid/35/11103.html#i49) [\[i48\]](https://dblp.org/pid/35/11103.html#i48) [\[i47\]](https://dblp.org/pid/35/11103.html#i47) [\[i46\]](https://dblp.org/pid/35/11103.html#i46) [\[i44\]](https://dblp.org/pid/35/11103.html#i44) [\[i43\]](https://dblp.org/pid/35/11103.html#i43) [\[c50\]](https://dblp.org/pid/35/11103.html#c50) [\[c49\]](https://dblp.org/pid/35/11103.html#c49) [\[c47\]](https://dblp.org/pid/35/11103.html#c47) [\[c46\]](https://dblp.org/pid/35/11103.html#c46) [\[c45\]](https://dblp.org/pid/35/11103.html#c45) [\[c44\]](https://dblp.org/pid/35/11103.html#c44) [\[c43\]](https://dblp.org/pid/35/11103.html#c43) [\[c42\]](https://dblp.org/pid/35/11103.html#c42) [\[c41\]](https://dblp.org/pid/35/11103.html#c41) [\[i42\]](https://dblp.org/pid/35/11103.html#i42) [\[i41\]](https://dblp.org/pid/35/11103.html#i41) [\[i39\]](https://dblp.org/pid/35/11103.html#i39) [\[i38\]](https://dblp.org/pid/35/11103.html#i38) [\[i37\]](https://dblp.org/pid/35/11103.html#i37) [\[i36\]](https://dblp.org/pid/35/11103.html#i36) [\[i35\]](https://dblp.org/pid/35/11103.html#i35) [\[i34\]](https://dblp.org/pid/35/11103.html#i34) [\[i33\]](https://dblp.org/pid/35/11103.html#i33) [\[i32\]](https://dblp.org/pid/35/11103.html#i32) [\[i31\]](https://dblp.org/pid/35/11103.html#i31) [\[i30\]](https://dblp.org/pid/35/11103.html#i30) [\[i29\]](https://dblp.org/pid/35/11103.html#i29) [\[i28\]](https://dblp.org/pid/35/11103.html#i28) [\[i27\]](https://dblp.org/pid/35/11103.html#i27) [\[c39\]](https://dblp.org/pid/35/11103.html#c39) [\[c36\]](https://dblp.org/pid/35/11103.html#c36) [\[c35\]](https://dblp.org/pid/35/11103.html#c35) [\[c34\]](https://dblp.org/pid/35/11103.html#c34) [\[c33\]](https://dblp.org/pid/35/11103.html#c33) [\[c32\]](https://dblp.org/pid/35/11103.html#c32) [\[i25\]](https://dblp.org/pid/35/11103.html#i25) [\[i24\]](https://dblp.org/pid/35/11103.html#i24) [\[i23\]](https://dblp.org/pid/35/11103.html#i23) [\[i22\]](https://dblp.org/pid/35/11103.html#i22) [\[i20\]](https://dblp.org/pid/35/11103.html#i20) [\[i19\]](https://dblp.org/pid/35/11103.html#i19) [\[i18\]](https://dblp.org/pid/35/11103.html#i18) [\[i17\]](https://dblp.org/pid/35/11103.html#i17) [\[i16\]](https://dblp.org/pid/35/11103.html#i16) [\[i15\]](https://dblp.org/pid/35/11103.html#i15) [\[i14\]](https://dblp.org/pid/35/11103.html#i14) [\[i12\]](https://dblp.org/pid/35/11103.html#i12)

[158](https://dblp.org/pid/35/11103.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yufei Guo](https://dblp.org/pid/23/2981.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[159](https://dblp.org/pid/35/11103.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Filiz Gurkan](https://dblp.org/pid/202/7040.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[160](https://dblp.org/pid/35/11103.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Gustav Häger](https://dblp.org/pid/157/3602.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[161](https://dblp.org/pid/35/11103.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Scott A. Hale](https://dblp.org/pid/32/10840.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[162](https://dblp.org/pid/35/11103.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ligong Han](https://dblp.org/pid/187/1675.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[c65\]](https://dblp.org/pid/35/11103.html#c65) [\[i96\]](https://dblp.org/pid/35/11103.html#i96) [\[i73\]](https://dblp.org/pid/35/11103.html#i73) [\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[163](https://dblp.org/pid/35/11103.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Meng Han](https://dblp.org/pid/91/9124.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[164](https://dblp.org/pid/35/11103.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wencheng Han](https://dblp.org/pid/280/3348.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[165](https://dblp.org/pid/35/11103.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Philippe Hansen-Estruch](https://dblp.org/pid/289/6990.html)

[\[c69\]](https://dblp.org/pid/35/11103.html#c69) [\[i61\]](https://dblp.org/pid/35/11103.html#i61)

[166](https://dblp.org/pid/35/11103.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Run Hao](https://dblp.org/pid/243/0480.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[167](https://dblp.org/pid/35/11103.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shiyuan He](https://dblp.org/pid/146/2829.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[168](https://dblp.org/pid/35/11103.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaoxiao He](https://dblp.org/pid/22/9737.html)

[\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[169](https://dblp.org/pid/35/11103.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zecheng He](https://dblp.org/pid/203/5675.html)

[\[i97\]](https://dblp.org/pid/35/11103.html#i97) [\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[i95\]](https://dblp.org/pid/35/11103.html#i95) [\[i93\]](https://dblp.org/pid/35/11103.html#i93) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i88\]](https://dblp.org/pid/35/11103.html#i88) [\[i87\]](https://dblp.org/pid/35/11103.html#i87) [\[i84\]](https://dblp.org/pid/35/11103.html#i84) [\[i67\]](https://dblp.org/pid/35/11103.html#i67) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[170](https://dblp.org/pid/35/11103.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zijian He](https://dblp.org/pid/60/8884.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i87\]](https://dblp.org/pid/35/11103.html#i87) [\[i66\]](https://dblp.org/pid/35/11103.html#i66)

[171](https://dblp.org/pid/35/11103.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Joseph Heyman](https://dblp.org/pid/49/4607.html)

[\[c1\]](https://dblp.org/pid/35/11103.html#c1)

[172](https://dblp.org/pid/35/11103.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Donghai Hong](https://dblp.org/pid/367/7553.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[173](https://dblp.org/pid/35/11103.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ji Hou](https://dblp.org/pid/152/4311.html)

[\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[i95\]](https://dblp.org/pid/35/11103.html#i95) [\[i93\]](https://dblp.org/pid/35/11103.html#i93) [\[i92\]](https://dblp.org/pid/35/11103.html#i92) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i84\]](https://dblp.org/pid/35/11103.html#i84) [\[i83\]](https://dblp.org/pid/35/11103.html#i83) [\[i66\]](https://dblp.org/pid/35/11103.html#i66) [\[i62\]](https://dblp.org/pid/35/11103.html#i62)

[174](https://dblp.org/pid/35/11103.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tingbo Hou](https://dblp.org/pid/35/3986.html)

[\[i97\]](https://dblp.org/pid/35/11103.html#i97) [\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[i95\]](https://dblp.org/pid/35/11103.html#i95) [\[i93\]](https://dblp.org/pid/35/11103.html#i93) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i88\]](https://dblp.org/pid/35/11103.html#i88) [\[i62\]](https://dblp.org/pid/35/11103.html#i62) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[175](https://dblp.org/pid/35/11103.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ming Hu 0003](https://dblp.org/pid/82/378-3.html)

[\[j20\]](https://dblp.org/pid/35/11103.html#j20) [\[c64\]](https://dblp.org/pid/35/11103.html#c64) [\[c61\]](https://dblp.org/pid/35/11103.html#c61) [\[i72\]](https://dblp.org/pid/35/11103.html#i72) [\[i55\]](https://dblp.org/pid/35/11103.html#i55)

[176](https://dblp.org/pid/35/11103.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qiang Hu](https://dblp.org/pid/93/5629.html)

[\[i69\]](https://dblp.org/pid/35/11103.html#i69) [\[i4\]](https://dblp.org/pid/35/11103.html#i4)

[177](https://dblp.org/pid/35/11103.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shuming Hu](https://dblp.org/pid/352/2124.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[i96\]](https://dblp.org/pid/35/11103.html#i96)

[178](https://dblp.org/pid/35/11103.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xuming Hu](https://dblp.org/pid/262/3664.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[179](https://dblp.org/pid/35/11103.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yushi Hu](https://dblp.org/pid/268/5766.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90)

[180](https://dblp.org/pid/35/11103.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wenyue Hua](https://dblp.org/pid/278/7993.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[181](https://dblp.org/pid/35/11103.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jen-tse Huang 0001](https://dblp.org/pid/317/7026.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[182](https://dblp.org/pid/35/11103.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Junzhou Huang](https://dblp.org/pid/22/1170.html)

[\[c65\]](https://dblp.org/pid/35/11103.html#c65) [\[i73\]](https://dblp.org/pid/35/11103.html#i73) [\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[183](https://dblp.org/pid/35/11103.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qingming Huang](https://dblp.org/pid/68/4388.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[184](https://dblp.org/pid/35/11103.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wenke Huang 0003](https://dblp.org/pid/330/1664-3.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[185](https://dblp.org/pid/35/11103.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yanyan Huang](https://dblp.org/pid/88/4316.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[186](https://dblp.org/pid/35/11103.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yihao Huang 0001](https://dblp.org/pid/255/5085.html)

[\[j26\]](https://dblp.org/pid/35/11103.html#j26) [\[c75\]](https://dblp.org/pid/35/11103.html#c75) [\[i94\]](https://dblp.org/pid/35/11103.html#i94) [\[i91\]](https://dblp.org/pid/35/11103.html#i91) [\[i86\]](https://dblp.org/pid/35/11103.html#i86) [\[j21\]](https://dblp.org/pid/35/11103.html#j21) [\[j20\]](https://dblp.org/pid/35/11103.html#j20) [\[j17\]](https://dblp.org/pid/35/11103.html#j17) [\[c64\]](https://dblp.org/pid/35/11103.html#c64) [\[c63\]](https://dblp.org/pid/35/11103.html#c63) [\[c61\]](https://dblp.org/pid/35/11103.html#c61) [\[i81\]](https://dblp.org/pid/35/11103.html#i81) [\[i80\]](https://dblp.org/pid/35/11103.html#i80) [\[i75\]](https://dblp.org/pid/35/11103.html#i75) [\[i74\]](https://dblp.org/pid/35/11103.html#i74) [\[i72\]](https://dblp.org/pid/35/11103.html#i72) [\[i59\]](https://dblp.org/pid/35/11103.html#i59) [\[c53\]](https://dblp.org/pid/35/11103.html#c53) [\[i56\]](https://dblp.org/pid/35/11103.html#i56) [\[i55\]](https://dblp.org/pid/35/11103.html#i55) [\[i54\]](https://dblp.org/pid/35/11103.html#i54) [\[j12\]](https://dblp.org/pid/35/11103.html#j12) [\[j9\]](https://dblp.org/pid/35/11103.html#j9) [\[c51\]](https://dblp.org/pid/35/11103.html#c51) [\[i48\]](https://dblp.org/pid/35/11103.html#i48) [\[i47\]](https://dblp.org/pid/35/11103.html#i47) [\[c41\]](https://dblp.org/pid/35/11103.html#c41) [\[i42\]](https://dblp.org/pid/35/11103.html#i42) [\[i33\]](https://dblp.org/pid/35/11103.html#i33) [\[i29\]](https://dblp.org/pid/35/11103.html#i29) [\[c37\]](https://dblp.org/pid/35/11103.html#c37) [\[c36\]](https://dblp.org/pid/35/11103.html#c36) [\[c35\]](https://dblp.org/pid/35/11103.html#c35) [\[c34\]](https://dblp.org/pid/35/11103.html#c34) [\[i26\]](https://dblp.org/pid/35/11103.html#i26) [\[i24\]](https://dblp.org/pid/35/11103.html#i24) [\[i23\]](https://dblp.org/pid/35/11103.html#i23) [\[i18\]](https://dblp.org/pid/35/11103.html#i18) [\[i10\]](https://dblp.org/pid/35/11103.html#i10)

[187](https://dblp.org/pid/35/11103.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yuheng Huang 0004](https://dblp.org/pid/01/6508-4.html)

[\[j30\]](https://dblp.org/pid/35/11103.html#j30) [\[j22\]](https://dblp.org/pid/35/11103.html#j22) [\[j16\]](https://dblp.org/pid/35/11103.html#j16) [\[i69\]](https://dblp.org/pid/35/11103.html#i69) [\[i68\]](https://dblp.org/pid/35/11103.html#i68) [\[i51\]](https://dblp.org/pid/35/11103.html#i51)

[188](https://dblp.org/pid/35/11103.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zeyi Huang](https://dblp.org/pid/142/5094.html)

[\[c70\]](https://dblp.org/pid/35/11103.html#c70) [\[i63\]](https://dblp.org/pid/35/11103.html#i63)

[189](https://dblp.org/pid/35/11103.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ziqi Huang](https://dblp.org/pid/159/4681.html)

[\[i84\]](https://dblp.org/pid/35/11103.html#i84)

[190](https://dblp.org/pid/35/11103.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wiebke Hutiri](https://dblp.org/pid/258/1137.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[191](https://dblp.org/pid/35/11103.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Joseph Marvin Imperial](https://dblp.org/pid/246/4647.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[192](https://dblp.org/pid/35/11103.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yusuke Iwasawa](https://dblp.org/pid/117/7377.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[193](https://dblp.org/pid/35/11103.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Aaron Jaech](https://dblp.org/pid/120/8500.html)

[\[c5\]](https://dblp.org/pid/35/11103.html#c5)

[194](https://dblp.org/pid/35/11103.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ankit Jain](https://dblp.org/pid/37/7907.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[i96\]](https://dblp.org/pid/35/11103.html#i96) [\[i67\]](https://dblp.org/pid/35/11103.html#i67)

[195](https://dblp.org/pid/35/11103.html?view=joint&param=195 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Surgan Jandial](https://dblp.org/pid/246/4915.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[196](https://dblp.org/pid/35/11103.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Niraj K. Jha](https://dblp.org/pid/j/NirajKJha.html)

[\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[i62\]](https://dblp.org/pid/35/11103.html#i62)

[197](https://dblp.org/pid/35/11103.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[198](https://dblp.org/pid/35/11103.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiaming Ji](https://dblp.org/pid/313/9356.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[199](https://dblp.org/pid/35/11103.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[200](https://dblp.org/pid/35/11103.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Menglin Jia](https://dblp.org/pid/228/8465.html)

[\[i83\]](https://dblp.org/pid/35/11103.html#i83)

[201](https://dblp.org/pid/35/11103.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaojun Jia](https://dblp.org/pid/57/5656.html)

[\[j26\]](https://dblp.org/pid/35/11103.html#j26) [\[c75\]](https://dblp.org/pid/35/11103.html#c75) [\[i94\]](https://dblp.org/pid/35/11103.html#i94) [\[i91\]](https://dblp.org/pid/35/11103.html#i91) [\[i86\]](https://dblp.org/pid/35/11103.html#i86) [\[j20\]](https://dblp.org/pid/35/11103.html#j20) [\[i81\]](https://dblp.org/pid/35/11103.html#i81) [\[i75\]](https://dblp.org/pid/35/11103.html#i75) [\[i74\]](https://dblp.org/pid/35/11103.html#i74) [\[i72\]](https://dblp.org/pid/35/11103.html#i72)

[202](https://dblp.org/pid/35/11103.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[203](https://dblp.org/pid/35/11103.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Nan Jiang](https://dblp.org/pid/06/4489.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[i96\]](https://dblp.org/pid/35/11103.html#i96)

[204](https://dblp.org/pid/35/11103.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yifan Jiang](https://dblp.org/pid/81/7246.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[205](https://dblp.org/pid/35/11103.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yilei Jiang](https://dblp.org/pid/297/8930.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[206](https://dblp.org/pid/35/11103.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[207](https://dblp.org/pid/35/11103.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yu-Gang Jiang 0001](https://dblp.org/pid/24/5818.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[208](https://dblp.org/pid/35/11103.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yuang Jiang](https://dblp.org/pid/249/8012.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[209](https://dblp.org/pid/35/11103.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Mingyu Jin](https://dblp.org/pid/215/7601.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[210](https://dblp.org/pid/35/11103.html?view=joint&param=210 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Weifei Jin](https://dblp.org/pid/377/6691.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[211](https://dblp.org/pid/35/11103.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zonglei Jing](https://dblp.org/pid/384/5611.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[212](https://dblp.org/pid/35/11103.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xuan Ju](https://dblp.org/pid/34/8495.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i83\]](https://dblp.org/pid/35/11103.html#i83)

[213](https://dblp.org/pid/35/11103.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Nick Judd](https://dblp.org/pid/332/0864.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[214](https://dblp.org/pid/35/11103.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bhavya Kailkhura](https://dblp.org/pid/132/8938.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91) [\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[215](https://dblp.org/pid/35/11103.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Anmol Kalia](https://dblp.org/pid/337/2585.html)

[\[i67\]](https://dblp.org/pid/35/11103.html#i67)

[216](https://dblp.org/pid/35/11103.html?view=joint&param=216 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[217](https://dblp.org/pid/35/11103.html?view=joint&param=217 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jani Käpylä](https://dblp.org/pid/244/2529.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[218](https://dblp.org/pid/35/11103.html?view=joint&param=218 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiao Ke](https://dblp.org/pid/78/9040.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[219](https://dblp.org/pid/35/11103.html?view=joint&param=219 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[220](https://dblp.org/pid/35/11103.html?view=joint&param=220 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Foutse Khomh](https://dblp.org/pid/32/147.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67) [\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[221](https://dblp.org/pid/35/11103.html?view=joint&param=221 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Byeong Hak Kim](https://dblp.org/pid/214/8978.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[222](https://dblp.org/pid/35/11103.html?view=joint&param=222 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hannah Kirk](https://dblp.org/pid/284/9434.html)

aka: Hannah Rose Kirk

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[223](https://dblp.org/pid/35/11103.html?view=joint&param=223 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[224](https://dblp.org/pid/35/11103.html?view=joint&param=224 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kevin Klyman](https://dblp.org/pid/359/3360.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[225](https://dblp.org/pid/35/11103.html?view=joint&param=225 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chris Knotz](https://dblp.org/pid/375/7389.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[226](https://dblp.org/pid/35/11103.html?view=joint&param=226 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xianglong Kong](https://dblp.org/pid/44/2995.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[227](https://dblp.org/pid/35/11103.html?view=joint&param=227 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[228](https://dblp.org/pid/35/11103.html?view=joint&param=228 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Michael Kuchnik](https://dblp.org/pid/228/8029.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[229](https://dblp.org/pid/35/11103.html?view=joint&param=229 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shachi H. Kumar](https://dblp.org/pid/164/7309.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[230](https://dblp.org/pid/35/11103.html?view=joint&param=230 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bolin Lai](https://dblp.org/pid/250/6136.html)

[\[c70\]](https://dblp.org/pid/35/11103.html#c70) [\[i63\]](https://dblp.org/pid/35/11103.html#i63)

[231](https://dblp.org/pid/35/11103.html?view=joint&param=231 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Siqi Lai](https://dblp.org/pid/314/0655.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[232](https://dblp.org/pid/35/11103.html?view=joint&param=232 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[233](https://dblp.org/pid/35/11103.html?view=joint&param=233 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[234](https://dblp.org/pid/35/11103.html?view=joint&param=234 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jun Ha Lee](https://dblp.org/pid/260/2774.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[235](https://dblp.org/pid/35/11103.html?view=joint&param=235 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Sangmin Lee 0001](https://dblp.org/pid/68/311-1.html)

[\[c70\]](https://dblp.org/pid/35/11103.html#c70) [\[i63\]](https://dblp.org/pid/35/11103.html#i63)

[236](https://dblp.org/pid/35/11103.html?view=joint&param=236 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[237](https://dblp.org/pid/35/11103.html?view=joint&param=237 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Christopher T. Lengerich](https://dblp.org/pid/147/4826.html)

aka: Chris Lengerich

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[238](https://dblp.org/pid/35/11103.html?view=joint&param=238 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[239](https://dblp.org/pid/35/11103.html?view=joint&param=239 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Baolu Li](https://dblp.org/pid/352/4564.html)

[\[c62\]](https://dblp.org/pid/35/11103.html#c62) [\[c59\]](https://dblp.org/pid/35/11103.html#c59) [\[i82\]](https://dblp.org/pid/35/11103.html#i82) [\[i79\]](https://dblp.org/pid/35/11103.html#i79)

[240](https://dblp.org/pid/35/11103.html?view=joint&param=240 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bo Li](https://dblp.org/pid/50/3402.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[241](https://dblp.org/pid/35/11103.html?view=joint&param=241 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bo Li 0026](https://dblp.org/pid/50/3402-26.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76) [\[c31\]](https://dblp.org/pid/35/11103.html#c31) [\[c30\]](https://dblp.org/pid/35/11103.html#c30) [\[c27\]](https://dblp.org/pid/35/11103.html#c27) [\[c26\]](https://dblp.org/pid/35/11103.html#c26) [\[i9\]](https://dblp.org/pid/35/11103.html#i9) [\[i8\]](https://dblp.org/pid/35/11103.html#i8) [\[i6\]](https://dblp.org/pid/35/11103.html#i6) [\[i4\]](https://dblp.org/pid/35/11103.html#i4)

[242](https://dblp.org/pid/35/11103.html?view=joint&param=242 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hainan Li](https://dblp.org/pid/256/6812.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[243](https://dblp.org/pid/35/11103.html?view=joint&param=243 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hongdong Li](https://dblp.org/pid/59/4859.html)

[\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[244](https://dblp.org/pid/35/11103.html?view=joint&param=244 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hongwei Li](https://dblp.org/pid/39/5544.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[245](https://dblp.org/pid/35/11103.html?view=joint&param=245 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[246](https://dblp.org/pid/35/11103.html?view=joint&param=246 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Huitao Li](https://dblp.org/pid/233/2009.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[247](https://dblp.org/pid/35/11103.html?view=joint&param=247 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Irene Li](https://dblp.org/pid/44/8976.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[248](https://dblp.org/pid/35/11103.html?view=joint&param=248 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jianhua Li](https://dblp.org/pid/93/3389.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[249](https://dblp.org/pid/35/11103.html?view=joint&param=249 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jianwen Li](https://dblp.org/pid/21/8669.html)

[\[c35\]](https://dblp.org/pid/35/11103.html#c35) [\[i26\]](https://dblp.org/pid/35/11103.html#i26) [\[i23\]](https://dblp.org/pid/35/11103.html#i23)

[250](https://dblp.org/pid/35/11103.html?view=joint&param=250 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jinlong Li](https://dblp.org/pid/34/1296.html)

[\[c62\]](https://dblp.org/pid/35/11103.html#c62) [\[c59\]](https://dblp.org/pid/35/11103.html#c59) [\[i82\]](https://dblp.org/pid/35/11103.html#i82) [\[i79\]](https://dblp.org/pid/35/11103.html#i79) [\[j10\]](https://dblp.org/pid/35/11103.html#j10) [\[i37\]](https://dblp.org/pid/35/11103.html#i37)

[251](https://dblp.org/pid/35/11103.html?view=joint&param=251 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kang Li 0004](https://dblp.org/pid/l/KangLi.html)

[\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[252](https://dblp.org/pid/35/11103.html?view=joint&param=252 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kunpeng Li](https://dblp.org/pid/38/1577.html)

[\[i97\]](https://dblp.org/pid/35/11103.html#i97) [\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[i95\]](https://dblp.org/pid/35/11103.html#i95) [\[i93\]](https://dblp.org/pid/35/11103.html#i93) [\[i92\]](https://dblp.org/pid/35/11103.html#i92) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i87\]](https://dblp.org/pid/35/11103.html#i87) [\[i83\]](https://dblp.org/pid/35/11103.html#i83)

[253](https://dblp.org/pid/35/11103.html?view=joint&param=253 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Li Li 0029](https://dblp.org/pid/53/2189-29.html)

[\[c30\]](https://dblp.org/pid/35/11103.html#c30) [\[c27\]](https://dblp.org/pid/35/11103.html#c27) [\[c26\]](https://dblp.org/pid/35/11103.html#c26) [\[i9\]](https://dblp.org/pid/35/11103.html#i9) [\[i8\]](https://dblp.org/pid/35/11103.html#i8)

[254](https://dblp.org/pid/35/11103.html?view=joint&param=254 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qiankun Li](https://dblp.org/pid/228/7339.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[255](https://dblp.org/pid/35/11103.html?view=joint&param=255 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qing Li](https://dblp.org/pid/181/2689.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[256](https://dblp.org/pid/35/11103.html?view=joint&param=256 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shuangzhi Li 0002](https://dblp.org/pid/174/9969-2.html)

[\[j24\]](https://dblp.org/pid/35/11103.html#j24)

[257](https://dblp.org/pid/35/11103.html?view=joint&param=257 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shuangzhi Li 0003](https://dblp.org/pid/331/2840.html)

[\[i43\]](https://dblp.org/pid/35/11103.html#i43)

[258](https://dblp.org/pid/35/11103.html?view=joint&param=258 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tianlin Li](https://dblp.org/pid/137/8830.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91) [\[c64\]](https://dblp.org/pid/35/11103.html#c64) [\[i81\]](https://dblp.org/pid/35/11103.html#i81) [\[i54\]](https://dblp.org/pid/35/11103.html#i54) [\[j6\]](https://dblp.org/pid/35/11103.html#j6) [\[i46\]](https://dblp.org/pid/35/11103.html#i46)

[259](https://dblp.org/pid/35/11103.html?view=joint&param=259 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[260](https://dblp.org/pid/35/11103.html?view=joint&param=260 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaoguang Li](https://dblp.org/pid/46/1349.html)

[\[c42\]](https://dblp.org/pid/35/11103.html#c42) [\[i34\]](https://dblp.org/pid/35/11103.html#i34)

[261](https://dblp.org/pid/35/11103.html?view=joint&param=261 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaohong Li 0001](https://dblp.org/pid/08/2489-1.html)

[\[c44\]](https://dblp.org/pid/35/11103.html#c44) [\[c43\]](https://dblp.org/pid/35/11103.html#c43) [\[i36\]](https://dblp.org/pid/35/11103.html#i36) [\[i15\]](https://dblp.org/pid/35/11103.html#i15)

[262](https://dblp.org/pid/35/11103.html?view=joint&param=262 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xin Li 0079](https://dblp.org/pid/09/1365-79.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[263](https://dblp.org/pid/35/11103.html?view=joint&param=263 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xinfeng Li](https://dblp.org/pid/04/8388.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[264](https://dblp.org/pid/35/11103.html?view=joint&param=264 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xingyu Li](https://dblp.org/pid/45/2385.html)

[\[j24\]](https://dblp.org/pid/35/11103.html#j24) [\[i43\]](https://dblp.org/pid/35/11103.html#i43)

[265](https://dblp.org/pid/35/11103.html?view=joint&param=265 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiuyu Li](https://dblp.org/pid/279/5847.html)

[\[i85\]](https://dblp.org/pid/35/11103.html#i85)

[266](https://dblp.org/pid/35/11103.html?view=joint&param=266 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yeting Li](https://dblp.org/pid/185/7953.html)

[\[c54\]](https://dblp.org/pid/35/11103.html#c54) [\[i52\]](https://dblp.org/pid/35/11103.html#i52)

[267](https://dblp.org/pid/35/11103.html?view=joint&param=267 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yidong Li](https://dblp.org/pid/40/7652.html)

[\[j15\]](https://dblp.org/pid/35/11103.html#j15) [\[i45\]](https://dblp.org/pid/35/11103.html#i45)

[268](https://dblp.org/pid/35/11103.html?view=joint&param=268 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yiming Li](https://dblp.org/pid/181/2877.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[269](https://dblp.org/pid/35/11103.html?view=joint&param=269 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yiming Li 0003](https://dblp.org/pid/l/YimingLi-3.html)

[\[c57\]](https://dblp.org/pid/35/11103.html#c57) [\[i57\]](https://dblp.org/pid/35/11103.html#i57) [\[c48\]](https://dblp.org/pid/35/11103.html#c48) [\[i40\]](https://dblp.org/pid/35/11103.html#i40)

[270](https://dblp.org/pid/35/11103.html?view=joint&param=270 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yuekang Li](https://dblp.org/pid/204/3729.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67) [\[c54\]](https://dblp.org/pid/35/11103.html#c54) [\[i52\]](https://dblp.org/pid/35/11103.html#i52)

[271](https://dblp.org/pid/35/11103.html?view=joint&param=271 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yuezhou Li](https://dblp.org/pid/284/2562.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[272](https://dblp.org/pid/35/11103.html?view=joint&param=272 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhongguo Li](https://dblp.org/pid/49/8374.html)

[\[c39\]](https://dblp.org/pid/35/11103.html#c39)

[273](https://dblp.org/pid/35/11103.html?view=joint&param=273 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhuo Li 0013](https://dblp.org/pid/51/4015-13.html)

[\[c38\]](https://dblp.org/pid/35/11103.html#c38)

[274](https://dblp.org/pid/35/11103.html?view=joint&param=274 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhuowei Li 0002](https://dblp.org/pid/181/2874-2.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[i96\]](https://dblp.org/pid/35/11103.html#i96)

[275](https://dblp.org/pid/35/11103.html?view=joint&param=275 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Long Lian](https://dblp.org/pid/276/0012.html)

[\[i85\]](https://dblp.org/pid/35/11103.html#i85)

[276](https://dblp.org/pid/35/11103.html?view=joint&param=276 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Feng Liang](https://dblp.org/pid/54/6821.html)

[\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[i95\]](https://dblp.org/pid/35/11103.html#i95) [\[i83\]](https://dblp.org/pid/35/11103.html#i83)

[277](https://dblp.org/pid/35/11103.html?view=joint&param=277 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Mingfu Liang](https://dblp.org/pid/241/9790.html)

[\[c68\]](https://dblp.org/pid/35/11103.html#c68) [\[i64\]](https://dblp.org/pid/35/11103.html#i64)

[278](https://dblp.org/pid/35/11103.html?view=joint&param=278 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Percy Liang](https://dblp.org/pid/04/1701.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[279](https://dblp.org/pid/35/11103.html?view=joint&param=279 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Siyuan Liang](https://dblp.org/pid/205/8767.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[280](https://dblp.org/pid/35/11103.html?view=joint&param=280 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zeyi Liao](https://dblp.org/pid/254/0197.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[281](https://dblp.org/pid/35/11103.html?view=joint&param=281 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Changting Lin](https://dblp.org/pid/231/4918.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[282](https://dblp.org/pid/35/11103.html?view=joint&param=282 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Di Lin 0002](https://dblp.org/pid/20/3191-2.html)

[\[j28\]](https://dblp.org/pid/35/11103.html#j28) [\[j23\]](https://dblp.org/pid/35/11103.html#j23) [\[c60\]](https://dblp.org/pid/35/11103.html#c60) [\[i78\]](https://dblp.org/pid/35/11103.html#i78) [\[i54\]](https://dblp.org/pid/35/11103.html#i54) [\[i49\]](https://dblp.org/pid/35/11103.html#i49) [\[i31\]](https://dblp.org/pid/35/11103.html#i31)

[283](https://dblp.org/pid/35/11103.html?view=joint&param=283 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Han Lin](https://dblp.org/pid/63/6173.html)

[\[i84\]](https://dblp.org/pid/35/11103.html#i84)

[284](https://dblp.org/pid/35/11103.html?view=joint&param=284 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Liang Lin](https://dblp.org/pid/84/7019.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[285](https://dblp.org/pid/35/11103.html?view=joint&param=285 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shangwei Lin 0001](https://dblp.org/pid/55/4730-1.html)

aka: Shang-Wei Lin 0001

[\[j25\]](https://dblp.org/pid/35/11103.html#j25) [\[j8\]](https://dblp.org/pid/35/11103.html#j8) [\[i20\]](https://dblp.org/pid/35/11103.html#i20) [\[i17\]](https://dblp.org/pid/35/11103.html#i17)

[286](https://dblp.org/pid/35/11103.html?view=joint&param=286 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shi Lin](https://dblp.org/pid/41/7692.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[287](https://dblp.org/pid/35/11103.html?view=joint&param=287 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Weisi Lin](https://dblp.org/pid/14/3737.html)

[\[j25\]](https://dblp.org/pid/35/11103.html#j25) [\[j8\]](https://dblp.org/pid/35/11103.html#j8) [\[i20\]](https://dblp.org/pid/35/11103.html#i20) [\[i17\]](https://dblp.org/pid/35/11103.html#i17)

[288](https://dblp.org/pid/35/11103.html?view=joint&param=288 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xi Victoria Lin](https://dblp.org/pid/215/5264.html)

[\[i85\]](https://dblp.org/pid/35/11103.html#i85)

[289](https://dblp.org/pid/35/11103.html?view=joint&param=289 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaowen Lin](https://dblp.org/pid/210/0844.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[i96\]](https://dblp.org/pid/35/11103.html#i96)

[290](https://dblp.org/pid/35/11103.html?view=joint&param=290 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Aishan Liu](https://dblp.org/pid/177/5658.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[291](https://dblp.org/pid/35/11103.html?view=joint&param=291 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[i65\]](https://dblp.org/pid/35/11103.html#i65) [\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[292](https://dblp.org/pid/35/11103.html?view=joint&param=292 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[293](https://dblp.org/pid/35/11103.html?view=joint&param=293 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chengwei Liu](https://dblp.org/pid/163/6525.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91) [\[c54\]](https://dblp.org/pid/35/11103.html#c54) [\[i52\]](https://dblp.org/pid/35/11103.html#i52)

[294](https://dblp.org/pid/35/11103.html?view=joint&param=294 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Dairui Liu](https://dblp.org/pid/261/2925.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[295](https://dblp.org/pid/35/11103.html?view=joint&param=295 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Di Liu 0003](https://dblp.org/pid/15/1777-3.html)

[\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[296](https://dblp.org/pid/35/11103.html?view=joint&param=296 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jingen Liu](https://dblp.org/pid/10/5849.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[297](https://dblp.org/pid/35/11103.html?view=joint&param=297 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Li Liu 0036](https://dblp.org/pid/33/4528-36.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[298](https://dblp.org/pid/35/11103.html?view=joint&param=298 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Miao Liu 0007](https://dblp.org/pid/60/6348-7.html)

[\[c70\]](https://dblp.org/pid/35/11103.html#c70) [\[c68\]](https://dblp.org/pid/35/11103.html#c68) [\[i64\]](https://dblp.org/pid/35/11103.html#i64) [\[i63\]](https://dblp.org/pid/35/11103.html#i63)

[299](https://dblp.org/pid/35/11103.html?view=joint&param=299 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Nan Liu 0003](https://dblp.org/pid/86/4643-3.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[300](https://dblp.org/pid/35/11103.html?view=joint&param=300 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qingjie Liu 0001](https://dblp.org/pid/72/10584.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[301](https://dblp.org/pid/35/11103.html?view=joint&param=301 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xianglong Liu 0001](https://dblp.org/pid/55/7901-1.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[302](https://dblp.org/pid/35/11103.html?view=joint&param=302 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xinyu Liu 0009](https://dblp.org/pid/98/738-9.html)

[\[c62\]](https://dblp.org/pid/35/11103.html#c62) [\[c59\]](https://dblp.org/pid/35/11103.html#c59) [\[i82\]](https://dblp.org/pid/35/11103.html#i82) [\[i79\]](https://dblp.org/pid/35/11103.html#i79)

[303](https://dblp.org/pid/35/11103.html?view=joint&param=303 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yang Liu 0003](https://dblp.org/pid/51/3710-3.html)

[\[j29\]](https://dblp.org/pid/35/11103.html#j29) [\[j26\]](https://dblp.org/pid/35/11103.html#j26) [\[j23\]](https://dblp.org/pid/35/11103.html#j23) [\[c75\]](https://dblp.org/pid/35/11103.html#c75) [\[i94\]](https://dblp.org/pid/35/11103.html#i94) [\[j21\]](https://dblp.org/pid/35/11103.html#j21) [\[j20\]](https://dblp.org/pid/35/11103.html#j20) [\[j17\]](https://dblp.org/pid/35/11103.html#j17) [\[c64\]](https://dblp.org/pid/35/11103.html#c64) [\[c63\]](https://dblp.org/pid/35/11103.html#c63) [\[c61\]](https://dblp.org/pid/35/11103.html#c61) [\[c58\]](https://dblp.org/pid/35/11103.html#c58) [\[i81\]](https://dblp.org/pid/35/11103.html#i81) [\[i80\]](https://dblp.org/pid/35/11103.html#i80) [\[i75\]](https://dblp.org/pid/35/11103.html#i75) [\[i74\]](https://dblp.org/pid/35/11103.html#i74) [\[i72\]](https://dblp.org/pid/35/11103.html#i72) [\[i59\]](https://dblp.org/pid/35/11103.html#i59) [\[c54\]](https://dblp.org/pid/35/11103.html#c54) [\[c53\]](https://dblp.org/pid/35/11103.html#c53) [\[i55\]](https://dblp.org/pid/35/11103.html#i55) [\[i54\]](https://dblp.org/pid/35/11103.html#i54) [\[i52\]](https://dblp.org/pid/35/11103.html#i52) [\[j12\]](https://dblp.org/pid/35/11103.html#j12) [\[j9\]](https://dblp.org/pid/35/11103.html#j9) [\[j8\]](https://dblp.org/pid/35/11103.html#j8) [\[j7\]](https://dblp.org/pid/35/11103.html#j7) [\[j6\]](https://dblp.org/pid/35/11103.html#j6) [\[c52\]](https://dblp.org/pid/35/11103.html#c52) [\[c51\]](https://dblp.org/pid/35/11103.html#c51) [\[i48\]](https://dblp.org/pid/35/11103.html#i48) [\[i47\]](https://dblp.org/pid/35/11103.html#i47) [\[i46\]](https://dblp.org/pid/35/11103.html#i46) [\[c50\]](https://dblp.org/pid/35/11103.html#c50) [\[c49\]](https://dblp.org/pid/35/11103.html#c49) [\[c47\]](https://dblp.org/pid/35/11103.html#c47) [\[c43\]](https://dblp.org/pid/35/11103.html#c43) [\[c42\]](https://dblp.org/pid/35/11103.html#c42) [\[c41\]](https://dblp.org/pid/35/11103.html#c41) [\[c40\]](https://dblp.org/pid/35/11103.html#c40) [\[i42\]](https://dblp.org/pid/35/11103.html#i42) [\[i41\]](https://dblp.org/pid/35/11103.html#i41) [\[i36\]](https://dblp.org/pid/35/11103.html#i36) [\[i35\]](https://dblp.org/pid/35/11103.html#i35) [\[i34\]](https://dblp.org/pid/35/11103.html#i34) [\[i33\]](https://dblp.org/pid/35/11103.html#i33) [\[i32\]](https://dblp.org/pid/35/11103.html#i32) [\[i31\]](https://dblp.org/pid/35/11103.html#i31) [\[i29\]](https://dblp.org/pid/35/11103.html#i29) [\[i27\]](https://dblp.org/pid/35/11103.html#i27) [\[c39\]](https://dblp.org/pid/35/11103.html#c39) [\[c37\]](https://dblp.org/pid/35/11103.html#c37) [\[c36\]](https://dblp.org/pid/35/11103.html#c36) [\[c35\]](https://dblp.org/pid/35/11103.html#c35) [\[c34\]](https://dblp.org/pid/35/11103.html#c34) [\[c33\]](https://dblp.org/pid/35/11103.html#c33) [\[c32\]](https://dblp.org/pid/35/11103.html#c32) [\[i26\]](https://dblp.org/pid/35/11103.html#i26) [\[i25\]](https://dblp.org/pid/35/11103.html#i25) [\[i24\]](https://dblp.org/pid/35/11103.html#i24) [\[i23\]](https://dblp.org/pid/35/11103.html#i23) [\[i22\]](https://dblp.org/pid/35/11103.html#i22) [\[i21\]](https://dblp.org/pid/35/11103.html#i21) [\[i20\]](https://dblp.org/pid/35/11103.html#i20) [\[i19\]](https://dblp.org/pid/35/11103.html#i19) [\[i18\]](https://dblp.org/pid/35/11103.html#i18) [\[i17\]](https://dblp.org/pid/35/11103.html#i17) [\[i16\]](https://dblp.org/pid/35/11103.html#i16) [\[i13\]](https://dblp.org/pid/35/11103.html#i13) [\[c31\]](https://dblp.org/pid/35/11103.html#c31) [\[c30\]](https://dblp.org/pid/35/11103.html#c30) [\[i11\]](https://dblp.org/pid/35/11103.html#i11) [\[i10\]](https://dblp.org/pid/35/11103.html#i10) [\[c27\]](https://dblp.org/pid/35/11103.html#c27) [\[c26\]](https://dblp.org/pid/35/11103.html#c26) [\[i9\]](https://dblp.org/pid/35/11103.html#i9) [\[i8\]](https://dblp.org/pid/35/11103.html#i8) [\[i6\]](https://dblp.org/pid/35/11103.html#i6) [\[i5\]](https://dblp.org/pid/35/11103.html#i5) [\[i4\]](https://dblp.org/pid/35/11103.html#i4)

[304](https://dblp.org/pid/35/11103.html?view=joint&param=304 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yang Liu 0084](https://dblp.org/pid/51/3710-84.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[305](https://dblp.org/pid/35/11103.html?view=joint&param=305 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yen-Cheng Liu](https://dblp.org/pid/29/7584.html)

[\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i62\]](https://dblp.org/pid/35/11103.html#i62)

[306](https://dblp.org/pid/35/11103.html?view=joint&param=306 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yi Liu 0069](https://dblp.org/pid/97/4626-69.html)

[\[c54\]](https://dblp.org/pid/35/11103.html#c54) [\[i52\]](https://dblp.org/pid/35/11103.html#i52)

[307](https://dblp.org/pid/35/11103.html?view=joint&param=307 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Eileen Peters Long](https://dblp.org/pid/144/1945.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[308](https://dblp.org/pid/35/11103.html?view=joint&param=308 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Haolang Lu](https://dblp.org/pid/381/0560.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[309](https://dblp.org/pid/35/11103.html?view=joint&param=309 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[310](https://dblp.org/pid/35/11103.html?view=joint&param=310 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jinghui Lu](https://dblp.org/pid/14/983.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[311](https://dblp.org/pid/35/11103.html?view=joint&param=311 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shijian Lu](https://dblp.org/pid/42/2718.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[312](https://dblp.org/pid/35/11103.html?view=joint&param=312 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Victor Lu](https://dblp.org/pid/77/8356.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[313](https://dblp.org/pid/35/11103.html?view=joint&param=313 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wei Lu](https://dblp.org/pid/98/6613.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[314](https://dblp.org/pid/35/11103.html?view=joint&param=314 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhichao Lu](https://dblp.org/pid/144/1417.html)

[\[j15\]](https://dblp.org/pid/35/11103.html#j15) [\[j13\]](https://dblp.org/pid/35/11103.html#j13) [\[c55\]](https://dblp.org/pid/35/11103.html#c55) [\[i58\]](https://dblp.org/pid/35/11103.html#i58) [\[i53\]](https://dblp.org/pid/35/11103.html#i53) [\[i45\]](https://dblp.org/pid/35/11103.html#i45)

[315](https://dblp.org/pid/35/11103.html?view=joint&param=315 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jonathon Luiten](https://dblp.org/pid/211/7992.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[316](https://dblp.org/pid/35/11103.html?view=joint&param=316 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[317](https://dblp.org/pid/35/11103.html?view=joint&param=317 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hanjun Luo](https://dblp.org/pid/355/1273.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[318](https://dblp.org/pid/35/11103.html?view=joint&param=318 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Meng Luo 0002](https://dblp.org/pid/16/3121-2.html)

[\[c40\]](https://dblp.org/pid/35/11103.html#c40) [\[i13\]](https://dblp.org/pid/35/11103.html#i13)

[319](https://dblp.org/pid/35/11103.html?view=joint&param=319 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xin Luo](https://dblp.org/pid/53/5106.html)

[\[j26\]](https://dblp.org/pid/35/11103.html#j26) [\[i94\]](https://dblp.org/pid/35/11103.html#i94)

[320](https://dblp.org/pid/35/11103.html?view=joint&param=320 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yaqiao Luo](https://dblp.org/pid/150/6230.html)

[\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[i62\]](https://dblp.org/pid/35/11103.html#i62) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[321](https://dblp.org/pid/35/11103.html?view=joint&param=321 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Anh Tuan Luu](https://dblp.org/pid/81/8329.html)

aka: Luu Anh Tuan

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[322](https://dblp.org/pid/35/11103.html?view=joint&param=322 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Khoa Luu](https://dblp.org/pid/43/8092.html)

[\[j2\]](https://dblp.org/pid/35/11103.html#j2) [\[c3\]](https://dblp.org/pid/35/11103.html#c3)

[323](https://dblp.org/pid/35/11103.html?view=joint&param=323 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Lingjuan Lyu](https://dblp.org/pid/178/9876.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[i96\]](https://dblp.org/pid/35/11103.html#i96)

[324](https://dblp.org/pid/35/11103.html?view=joint&param=324 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chih-Yao Ma](https://dblp.org/pid/198/0963.html)

[\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i62\]](https://dblp.org/pid/35/11103.html#i62)

[325](https://dblp.org/pid/35/11103.html?view=joint&param=325 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Haoyu Ma](https://dblp.org/pid/144/1634.html)

[\[i97\]](https://dblp.org/pid/35/11103.html#i97) [\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[i95\]](https://dblp.org/pid/35/11103.html#i95) [\[i93\]](https://dblp.org/pid/35/11103.html#i93) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i88\]](https://dblp.org/pid/35/11103.html#i88) [\[i67\]](https://dblp.org/pid/35/11103.html#i67) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[326](https://dblp.org/pid/35/11103.html?view=joint&param=326 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[327](https://dblp.org/pid/35/11103.html?view=joint&param=327 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ke Ma 0001](https://dblp.org/pid/98/2014-1.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[328](https://dblp.org/pid/35/11103.html?view=joint&param=328 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Lei Ma 0003](https://dblp.org/pid/20/6534-3.html)

[\[j30\]](https://dblp.org/pid/35/11103.html#j30) [\[j29\]](https://dblp.org/pid/35/11103.html#j29) [\[j28\]](https://dblp.org/pid/35/11103.html#j28) [\[j24\]](https://dblp.org/pid/35/11103.html#j24) [\[j23\]](https://dblp.org/pid/35/11103.html#j23) [\[j22\]](https://dblp.org/pid/35/11103.html#j22) [\[c67\]](https://dblp.org/pid/35/11103.html#c67) [\[j18\]](https://dblp.org/pid/35/11103.html#j18) [\[j16\]](https://dblp.org/pid/35/11103.html#j16) [\[c60\]](https://dblp.org/pid/35/11103.html#c60) [\[i78\]](https://dblp.org/pid/35/11103.html#i78) [\[i69\]](https://dblp.org/pid/35/11103.html#i69) [\[i68\]](https://dblp.org/pid/35/11103.html#i68) [\[j14\]](https://dblp.org/pid/35/11103.html#j14) [\[c54\]](https://dblp.org/pid/35/11103.html#c54) [\[i52\]](https://dblp.org/pid/35/11103.html#i52) [\[i51\]](https://dblp.org/pid/35/11103.html#i51) [\[j12\]](https://dblp.org/pid/35/11103.html#j12) [\[j11\]](https://dblp.org/pid/35/11103.html#j11) [\[j7\]](https://dblp.org/pid/35/11103.html#j7) [\[j6\]](https://dblp.org/pid/35/11103.html#j6) [\[j5\]](https://dblp.org/pid/35/11103.html#j5) [\[i49\]](https://dblp.org/pid/35/11103.html#i49) [\[i46\]](https://dblp.org/pid/35/11103.html#i46) [\[i44\]](https://dblp.org/pid/35/11103.html#i44) [\[i43\]](https://dblp.org/pid/35/11103.html#i43) [\[c50\]](https://dblp.org/pid/35/11103.html#c50) [\[c47\]](https://dblp.org/pid/35/11103.html#c47) [\[c45\]](https://dblp.org/pid/35/11103.html#c45) [\[c41\]](https://dblp.org/pid/35/11103.html#c41) [\[i42\]](https://dblp.org/pid/35/11103.html#i42) [\[i39\]](https://dblp.org/pid/35/11103.html#i39) [\[i33\]](https://dblp.org/pid/35/11103.html#i33) [\[i32\]](https://dblp.org/pid/35/11103.html#i32) [\[i31\]](https://dblp.org/pid/35/11103.html#i31) [\[i28\]](https://dblp.org/pid/35/11103.html#i28) [\[c39\]](https://dblp.org/pid/35/11103.html#c39) [\[c38\]](https://dblp.org/pid/35/11103.html#c38) [\[c37\]](https://dblp.org/pid/35/11103.html#c37) [\[c36\]](https://dblp.org/pid/35/11103.html#c36) [\[c35\]](https://dblp.org/pid/35/11103.html#c35) [\[c34\]](https://dblp.org/pid/35/11103.html#c34) [\[c33\]](https://dblp.org/pid/35/11103.html#c33) [\[c32\]](https://dblp.org/pid/35/11103.html#c32) [\[i26\]](https://dblp.org/pid/35/11103.html#i26) [\[i25\]](https://dblp.org/pid/35/11103.html#i25) [\[i24\]](https://dblp.org/pid/35/11103.html#i24) [\[i23\]](https://dblp.org/pid/35/11103.html#i23) [\[i22\]](https://dblp.org/pid/35/11103.html#i22) [\[i21\]](https://dblp.org/pid/35/11103.html#i21) [\[i19\]](https://dblp.org/pid/35/11103.html#i19) [\[i18\]](https://dblp.org/pid/35/11103.html#i18) [\[i16\]](https://dblp.org/pid/35/11103.html#i16) [\[i12\]](https://dblp.org/pid/35/11103.html#i12) [\[c31\]](https://dblp.org/pid/35/11103.html#c31) [\[c30\]](https://dblp.org/pid/35/11103.html#c30) [\[i11\]](https://dblp.org/pid/35/11103.html#i11) [\[i10\]](https://dblp.org/pid/35/11103.html#i10) [\[c27\]](https://dblp.org/pid/35/11103.html#c27) [\[c26\]](https://dblp.org/pid/35/11103.html#c26) [\[i9\]](https://dblp.org/pid/35/11103.html#i9) [\[i8\]](https://dblp.org/pid/35/11103.html#i8) [\[i6\]](https://dblp.org/pid/35/11103.html#i6) [\[i5\]](https://dblp.org/pid/35/11103.html#i5) [\[i4\]](https://dblp.org/pid/35/11103.html#i4)

[329](https://dblp.org/pid/35/11103.html?view=joint&param=329 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shiqing Ma](https://dblp.org/pid/172/8745.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[i96\]](https://dblp.org/pid/35/11103.html#i96) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[330](https://dblp.org/pid/35/11103.html?view=joint&param=330 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xingjun Ma](https://dblp.org/pid/195/8270.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[331](https://dblp.org/pid/35/11103.html?view=joint&param=331 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xu Ma](https://dblp.org/pid/77/9370.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90)

[332](https://dblp.org/pid/35/11103.html?view=joint&param=332 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ziang Ma](https://dblp.org/pid/165/9621.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[333](https://dblp.org/pid/35/11103.html?view=joint&param=333 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yifan Mai 0001](https://dblp.org/pid/156/8369-1.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[334](https://dblp.org/pid/35/11103.html?view=joint&param=334 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Priyanka Mary Mammen](https://dblp.org/pid/217/6913.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[335](https://dblp.org/pid/35/11103.html?view=joint&param=335 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kelvin N. Manyeki](https://dblp.org/pid/401/7765.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[336](https://dblp.org/pid/35/11103.html?view=joint&param=336 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Junyuan Mao](https://dblp.org/pid/371/2729.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[337](https://dblp.org/pid/35/11103.html?view=joint&param=337 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Weibo Mao](https://dblp.org/pid/44/4166.html)

[\[j27\]](https://dblp.org/pid/35/11103.html#j27) [\[i77\]](https://dblp.org/pid/35/11103.html#i77)

[338](https://dblp.org/pid/35/11103.html?view=joint&param=338 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Diana Marculescu](https://dblp.org/pid/59/2715.html)

[\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[i95\]](https://dblp.org/pid/35/11103.html#i95)

[339](https://dblp.org/pid/35/11103.html?view=joint&param=339 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Edison Marrese-Taylor](https://dblp.org/pid/137/6899.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[340](https://dblp.org/pid/35/11103.html?view=joint&param=340 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[341](https://dblp.org/pid/35/11103.html?view=joint&param=341 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[342](https://dblp.org/pid/35/11103.html?view=joint&param=342 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yutaka Matsuo](https://dblp.org/pid/m/YMatsuo.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[343](https://dblp.org/pid/35/11103.html?view=joint&param=343 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Peter Mattson](https://dblp.org/pid/47/739.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[344](https://dblp.org/pid/35/11103.html?view=joint&param=344 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[345](https://dblp.org/pid/35/11103.html?view=joint&param=345 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Sean McGregor](https://dblp.org/pid/173/7861.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[346](https://dblp.org/pid/35/11103.html?view=joint&param=346 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Nikhil Mehta 0002](https://dblp.org/pid/89/7487-2.html)

[\[c70\]](https://dblp.org/pid/35/11103.html#c70) [\[c69\]](https://dblp.org/pid/35/11103.html#c69) [\[i63\]](https://dblp.org/pid/35/11103.html#i63) [\[i61\]](https://dblp.org/pid/35/11103.html#i61)

[347](https://dblp.org/pid/35/11103.html?view=joint&param=347 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Virendra Mehta](https://dblp.org/pid/303/4829.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[348](https://dblp.org/pid/35/11103.html?view=joint&param=348 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[349](https://dblp.org/pid/35/11103.html?view=joint&param=349 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Fanci Meng](https://dblp.org/pid/400/2444.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[350](https://dblp.org/pid/35/11103.html?view=joint&param=350 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yanda Meng](https://dblp.org/pid/275/6822.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[351](https://dblp.org/pid/35/11103.html?view=joint&param=351 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Dimitris N. Metaxas](https://dblp.org/pid/m/DNMetaxas.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[c68\]](https://dblp.org/pid/35/11103.html#c68) [\[c65\]](https://dblp.org/pid/35/11103.html#c65) [\[i96\]](https://dblp.org/pid/35/11103.html#i96) [\[i73\]](https://dblp.org/pid/35/11103.html#i73) [\[i65\]](https://dblp.org/pid/35/11103.html#i65) [\[i64\]](https://dblp.org/pid/35/11103.html#i64)

[352](https://dblp.org/pid/35/11103.html?view=joint&param=352 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Fei Miao](https://dblp.org/pid/143/6002.html)

[\[i71\]](https://dblp.org/pid/35/11103.html#i71)

[353](https://dblp.org/pid/35/11103.html?view=joint&param=353 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Weikai Miao](https://dblp.org/pid/94/4256.html)

[\[j26\]](https://dblp.org/pid/35/11103.html#j26) [\[i94\]](https://dblp.org/pid/35/11103.html#i94) [\[c41\]](https://dblp.org/pid/35/11103.html#c41) [\[i33\]](https://dblp.org/pid/35/11103.html#i33) [\[i29\]](https://dblp.org/pid/35/11103.html#i29) [\[c35\]](https://dblp.org/pid/35/11103.html#c35) [\[i26\]](https://dblp.org/pid/35/11103.html#i26) [\[i23\]](https://dblp.org/pid/35/11103.html#i23) [\[i18\]](https://dblp.org/pid/35/11103.html#i18)

[354](https://dblp.org/pid/35/11103.html?view=joint&param=354 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[355](https://dblp.org/pid/35/11103.html?view=joint&param=355 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Martin Renqiang Min](https://dblp.org/pid/29/7048.html)

[\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[356](https://dblp.org/pid/35/11103.html?view=joint&param=356 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shlok Kumar Mishra](https://dblp.org/pid/173/6664.html)

[\[i92\]](https://dblp.org/pid/35/11103.html#i92)

[357](https://dblp.org/pid/35/11103.html?view=joint&param=357 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shafee Mohammed](https://dblp.org/pid/212/4553.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[358](https://dblp.org/pid/35/11103.html?view=joint&param=358 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Emanuel Moss](https://dblp.org/pid/257/8114.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[359](https://dblp.org/pid/35/11103.html?view=joint&param=359 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Simran Motwani](https://dblp.org/pid/358/3864.html)

[\[i66\]](https://dblp.org/pid/35/11103.html#i66)

[360](https://dblp.org/pid/35/11103.html?view=joint&param=360 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Junjie Mu](https://dblp.org/pid/283/1108.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[361](https://dblp.org/pid/35/11103.html?view=joint&param=361 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Lama Nachman](https://dblp.org/pid/65/3345.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[362](https://dblp.org/pid/35/11103.html?view=joint&param=362 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Dinesh Jinenhally Naganna](https://dblp.org/pid/375/6717.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[363](https://dblp.org/pid/35/11103.html?view=joint&param=363 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Amin Nikanjam](https://dblp.org/pid/42/1656.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[364](https://dblp.org/pid/35/11103.html?view=joint&param=364 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yuzhen Niu](https://dblp.org/pid/28/7442.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[365](https://dblp.org/pid/35/11103.html?view=joint&param=365 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Besmira Nushi](https://dblp.org/pid/117/4927.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[366](https://dblp.org/pid/35/11103.html?view=joint&param=366 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Luis Oala](https://dblp.org/pid/261/9215.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[367](https://dblp.org/pid/35/11103.html?view=joint&param=367 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yew-Soon Ong](https://dblp.org/pid/64/4136.html)

aka: Yew Soon Ong

[\[i89\]](https://dblp.org/pid/35/11103.html#i89) [\[j7\]](https://dblp.org/pid/35/11103.html#j7) [\[i5\]](https://dblp.org/pid/35/11103.html#i5)

[368](https://dblp.org/pid/35/11103.html?view=joint&param=368 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Iftach Orr](https://dblp.org/pid/375/6721.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[369](https://dblp.org/pid/35/11103.html?view=joint&param=369 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Dipan K. Pal](https://dblp.org/pid/148/1005.html)

[\[c21\]](https://dblp.org/pid/35/11103.html#c21) [\[c18\]](https://dblp.org/pid/35/11103.html#c18) [\[c17\]](https://dblp.org/pid/35/11103.html#c17) [\[c15\]](https://dblp.org/pid/35/11103.html#c15) [\[c14\]](https://dblp.org/pid/35/11103.html#c14) [\[c10\]](https://dblp.org/pid/35/11103.html#c10)

[370](https://dblp.org/pid/35/11103.html?view=joint&param=370 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shirui Pan](https://dblp.org/pid/91/8171.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[371](https://dblp.org/pid/35/11103.html?view=joint&param=371 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xichen Pan](https://dblp.org/pid/317/0180.html)

[\[i92\]](https://dblp.org/pid/35/11103.html#i92) [\[i84\]](https://dblp.org/pid/35/11103.html#i84)

[372](https://dblp.org/pid/35/11103.html?view=joint&param=372 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Alicia Parrish](https://dblp.org/pid/248/7544.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[373](https://dblp.org/pid/35/11103.html?view=joint&param=373 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Cigdem Patlak](https://dblp.org/pid/375/6217.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[374](https://dblp.org/pid/35/11103.html?view=joint&param=374 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[375](https://dblp.org/pid/35/11103.html?view=joint&param=375 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Vladimir Pavlovic 0001](https://dblp.org/pid/98/2506.html)

[\[c65\]](https://dblp.org/pid/35/11103.html#c65)

[376](https://dblp.org/pid/35/11103.html?view=joint&param=376 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[377](https://dblp.org/pid/35/11103.html?view=joint&param=377 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[378](https://dblp.org/pid/35/11103.html?view=joint&param=378 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[William Pietri](https://dblp.org/pid/04/1943.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[379](https://dblp.org/pid/35/11103.html?view=joint&param=379 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Forough Poursabzi-Sangdeh](https://dblp.org/pid/165/0744.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[380](https://dblp.org/pid/35/11103.html?view=joint&param=380 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Utsav Prabhu](https://dblp.org/pid/54/10072.html)

[\[j4\]](https://dblp.org/pid/35/11103.html#j4)

[381](https://dblp.org/pid/35/11103.html?view=joint&param=381 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Unni Prasad](https://dblp.org/pid/120/8492.html)

[\[c5\]](https://dblp.org/pid/35/11103.html#c5)

[382](https://dblp.org/pid/35/11103.html?view=joint&param=382 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Eleonora Presani](https://dblp.org/pid/227/6323.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[383](https://dblp.org/pid/35/11103.html?view=joint&param=383 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Geguang Pu](https://dblp.org/pid/33/1678.html)

[\[j26\]](https://dblp.org/pid/35/11103.html#j26) [\[c75\]](https://dblp.org/pid/35/11103.html#c75) [\[i94\]](https://dblp.org/pid/35/11103.html#i94) [\[i86\]](https://dblp.org/pid/35/11103.html#i86) [\[j21\]](https://dblp.org/pid/35/11103.html#j21) [\[j20\]](https://dblp.org/pid/35/11103.html#j20) [\[j17\]](https://dblp.org/pid/35/11103.html#j17) [\[c64\]](https://dblp.org/pid/35/11103.html#c64) [\[c63\]](https://dblp.org/pid/35/11103.html#c63) [\[c61\]](https://dblp.org/pid/35/11103.html#c61) [\[i81\]](https://dblp.org/pid/35/11103.html#i81) [\[i80\]](https://dblp.org/pid/35/11103.html#i80) [\[i75\]](https://dblp.org/pid/35/11103.html#i75) [\[i74\]](https://dblp.org/pid/35/11103.html#i74) [\[i72\]](https://dblp.org/pid/35/11103.html#i72) [\[i59\]](https://dblp.org/pid/35/11103.html#i59) [\[c53\]](https://dblp.org/pid/35/11103.html#c53) [\[i55\]](https://dblp.org/pid/35/11103.html#i55) [\[j9\]](https://dblp.org/pid/35/11103.html#j9) [\[c51\]](https://dblp.org/pid/35/11103.html#c51) [\[i48\]](https://dblp.org/pid/35/11103.html#i48) [\[i47\]](https://dblp.org/pid/35/11103.html#i47) [\[c41\]](https://dblp.org/pid/35/11103.html#c41) [\[i33\]](https://dblp.org/pid/35/11103.html#i33) [\[i29\]](https://dblp.org/pid/35/11103.html#i29) [\[c35\]](https://dblp.org/pid/35/11103.html#c35) [\[i26\]](https://dblp.org/pid/35/11103.html#i26) [\[i23\]](https://dblp.org/pid/35/11103.html#i23) [\[i18\]](https://dblp.org/pid/35/11103.html#i18)

[384](https://dblp.org/pid/35/11103.html?view=joint&param=384 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Fabrizio Puletti](https://dblp.org/pid/375/7077.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[385](https://dblp.org/pid/35/11103.html?view=joint&param=385 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Heli Qi](https://dblp.org/pid/320/4798.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[386](https://dblp.org/pid/35/11103.html?view=joint&param=386 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hua Qi](https://dblp.org/pid/87/4406.html)

[\[j28\]](https://dblp.org/pid/35/11103.html#j28) [\[j14\]](https://dblp.org/pid/35/11103.html#j14) [\[j5\]](https://dblp.org/pid/35/11103.html#j5) [\[i28\]](https://dblp.org/pid/35/11103.html#i28) [\[c38\]](https://dblp.org/pid/35/11103.html#c38) [\[c33\]](https://dblp.org/pid/35/11103.html#c33) [\[i22\]](https://dblp.org/pid/35/11103.html#i22) [\[i12\]](https://dblp.org/pid/35/11103.html#i12)

[387](https://dblp.org/pid/35/11103.html?view=joint&param=387 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Haotong Qin](https://dblp.org/pid/262/3626.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[388](https://dblp.org/pid/35/11103.html?view=joint&param=388 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shengchao Qin](https://dblp.org/pid/q/ShengchaoQin.html)

[\[j29\]](https://dblp.org/pid/35/11103.html#j29) [\[c44\]](https://dblp.org/pid/35/11103.html#c44) [\[i19\]](https://dblp.org/pid/35/11103.html#i19) [\[i15\]](https://dblp.org/pid/35/11103.html#i15)

[389](https://dblp.org/pid/35/11103.html?view=joint&param=389 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yalan Qin](https://dblp.org/pid/284/8225.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[390](https://dblp.org/pid/35/11103.html?view=joint&param=390 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shoumeng Qiu](https://dblp.org/pid/284/2537.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[391](https://dblp.org/pid/35/11103.html?view=joint&param=391 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Aravindh Rajiv](https://dblp.org/pid/307/9144.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[392](https://dblp.org/pid/35/11103.html?view=joint&param=392 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ankit Ramchandani](https://dblp.org/pid/257/3893.html)

[\[i67\]](https://dblp.org/pid/35/11103.html#i67)

[393](https://dblp.org/pid/35/11103.html?view=joint&param=393 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Muhammad Rana](https://dblp.org/pid/276/0222.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[394](https://dblp.org/pid/35/11103.html?view=joint&param=394 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[James M. Rehg](https://dblp.org/pid/r/JMRehg.html)

[\[c70\]](https://dblp.org/pid/35/11103.html#c70) [\[i63\]](https://dblp.org/pid/35/11103.html#i63)

[395](https://dblp.org/pid/35/11103.html?view=joint&param=395 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xuhong Ren](https://dblp.org/pid/138/4258.html)

[\[c60\]](https://dblp.org/pid/35/11103.html#c60) [\[i78\]](https://dblp.org/pid/35/11103.html#i78) [\[j11\]](https://dblp.org/pid/35/11103.html#j11) [\[i44\]](https://dblp.org/pid/35/11103.html#i44) [\[c45\]](https://dblp.org/pid/35/11103.html#c45) [\[i39\]](https://dblp.org/pid/35/11103.html#i39) [\[c38\]](https://dblp.org/pid/35/11103.html#c38) [\[i14\]](https://dblp.org/pid/35/11103.html#i14)

[396](https://dblp.org/pid/35/11103.html?view=joint&param=396 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[397](https://dblp.org/pid/35/11103.html?view=joint&param=397 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Paul Röttger](https://dblp.org/pid/282/4243.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[398](https://dblp.org/pid/35/11103.html?view=joint&param=398 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Saurav Sahay](https://dblp.org/pid/18/4070.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[399](https://dblp.org/pid/35/11103.html?view=joint&param=399 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Artsiom Sanakoyeu](https://dblp.org/pid/185/0536.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90)

[400](https://dblp.org/pid/35/11103.html?view=joint&param=400 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tim Santos](https://dblp.org/pid/334/2365.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[401](https://dblp.org/pid/35/11103.html?view=joint&param=401 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hasan Saribas](https://dblp.org/pid/225/3263.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[402](https://dblp.org/pid/35/11103.html?view=joint&param=402 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Marios Savvides](https://dblp.org/pid/13/3793.html)

[\[j4\]](https://dblp.org/pid/35/11103.html#j4) [\[c29\]](https://dblp.org/pid/35/11103.html#c29) [\[c28\]](https://dblp.org/pid/35/11103.html#c28) [\[i7\]](https://dblp.org/pid/35/11103.html#i7) [\[i3\]](https://dblp.org/pid/35/11103.html#i3) [\[c25\]](https://dblp.org/pid/35/11103.html#c25) [\[i2\]](https://dblp.org/pid/35/11103.html#i2) [\[j3\]](https://dblp.org/pid/35/11103.html#j3) [\[c24\]](https://dblp.org/pid/35/11103.html#c24) [\[c23\]](https://dblp.org/pid/35/11103.html#c23) [\[c22\]](https://dblp.org/pid/35/11103.html#c22) [\[c21\]](https://dblp.org/pid/35/11103.html#c21) [\[c20\]](https://dblp.org/pid/35/11103.html#c20) [\[i1\]](https://dblp.org/pid/35/11103.html#i1) [\[j2\]](https://dblp.org/pid/35/11103.html#j2) [\[c19\]](https://dblp.org/pid/35/11103.html#c19) [\[c18\]](https://dblp.org/pid/35/11103.html#c18) [\[c17\]](https://dblp.org/pid/35/11103.html#c17) [\[c16\]](https://dblp.org/pid/35/11103.html#c16) [\[c15\]](https://dblp.org/pid/35/11103.html#c15) [\[c14\]](https://dblp.org/pid/35/11103.html#c14) [\[c13\]](https://dblp.org/pid/35/11103.html#c13) [\[c12\]](https://dblp.org/pid/35/11103.html#c12) [\[c11\]](https://dblp.org/pid/35/11103.html#c11) [\[j1\]](https://dblp.org/pid/35/11103.html#j1) [\[c10\]](https://dblp.org/pid/35/11103.html#c10) [\[c9\]](https://dblp.org/pid/35/11103.html#c9) [\[c8\]](https://dblp.org/pid/35/11103.html#c8) [\[c7\]](https://dblp.org/pid/35/11103.html#c7) [\[c6\]](https://dblp.org/pid/35/11103.html#c6) [\[c5\]](https://dblp.org/pid/35/11103.html#c5) [\[c4\]](https://dblp.org/pid/35/11103.html#c4) [\[c3\]](https://dblp.org/pid/35/11103.html#c3) [\[c2\]](https://dblp.org/pid/35/11103.html#c2) [\[c1\]](https://dblp.org/pid/35/11103.html#c1)

[403](https://dblp.org/pid/35/11103.html?view=joint&param=403 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Nino Scherrer](https://dblp.org/pid/295/0198.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[404](https://dblp.org/pid/35/11103.html?view=joint&param=404 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Patrick Schramowski](https://dblp.org/pid/217/1650.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[405](https://dblp.org/pid/35/11103.html?view=joint&param=405 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Alice Schoenauer Sebag](https://dblp.org/pid/164/0807.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[406](https://dblp.org/pid/35/11103.html?view=joint&param=406 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Simon See](https://dblp.org/pid/62/6547.html)

[\[c31\]](https://dblp.org/pid/35/11103.html#c31) [\[i6\]](https://dblp.org/pid/35/11103.html#i6) [\[i4\]](https://dblp.org/pid/35/11103.html#i4)

[407](https://dblp.org/pid/35/11103.html?view=joint&param=407 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Keshav Seshadri](https://dblp.org/pid/95/10072.html)

[\[c17\]](https://dblp.org/pid/35/11103.html#c17)

[408](https://dblp.org/pid/35/11103.html?view=joint&param=408 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Siddharth Shah](https://dblp.org/pid/12/10521.html)

[\[i67\]](https://dblp.org/pid/35/11103.html#i67)

[409](https://dblp.org/pid/35/11103.html?view=joint&param=409 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Abolfazl Shahbazi](https://dblp.org/pid/375/6646.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[410](https://dblp.org/pid/35/11103.html?view=joint&param=410 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Mengyi Shan](https://dblp.org/pid/253/9346.html)

[\[i88\]](https://dblp.org/pid/35/11103.html#i88)

[411](https://dblp.org/pid/35/11103.html?view=joint&param=411 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[412](https://dblp.org/pid/35/11103.html?view=joint&param=412 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Vin Sharma](https://dblp.org/pid/227/2446.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[413](https://dblp.org/pid/35/11103.html?view=joint&param=413 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Mohamed S. Shehata](https://dblp.org/pid/33/2495.html)

aka: Mohamed Shehata 0001

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[414](https://dblp.org/pid/35/11103.html?view=joint&param=414 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Furao Shen](https://dblp.org/pid/80/4685.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[415](https://dblp.org/pid/35/11103.html?view=joint&param=415 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jianbing Shen](https://dblp.org/pid/38/5435.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[416](https://dblp.org/pid/35/11103.html?view=joint&param=416 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kaiwen Shen](https://dblp.org/pid/245/2568.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[417](https://dblp.org/pid/35/11103.html?view=joint&param=417 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xudong Shen](https://dblp.org/pid/240/0569.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[418](https://dblp.org/pid/35/11103.html?view=joint&param=418 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yujun Shi](https://dblp.org/pid/146/4499.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i87\]](https://dblp.org/pid/35/11103.html#i87)

[419](https://dblp.org/pid/35/11103.html?view=joint&param=419 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Satya Narayan Shukla](https://dblp.org/pid/161/3356.html)

[\[i92\]](https://dblp.org/pid/35/11103.html#i92)

[420](https://dblp.org/pid/35/11103.html?view=joint&param=420 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[421](https://dblp.org/pid/35/11103.html?view=joint&param=421 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Aashu Singh](https://dblp.org/pid/394/7460.html)

[\[i92\]](https://dblp.org/pid/35/11103.html#i92)

[422](https://dblp.org/pid/35/11103.html?view=joint&param=422 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ankush Pratap Singh](https://dblp.org/pid/362/3050.html)

[\[c66\]](https://dblp.org/pid/35/11103.html#c66) [\[i50\]](https://dblp.org/pid/35/11103.html#i50)

[423](https://dblp.org/pid/35/11103.html?view=joint&param=423 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Karanhaar Singh](https://dblp.org/pid/11/10698.html)

[\[c18\]](https://dblp.org/pid/35/11103.html#c18)

[424](https://dblp.org/pid/35/11103.html?view=joint&param=424 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Animesh Sinha](https://dblp.org/pid/289/7538.html)

[\[i97\]](https://dblp.org/pid/35/11103.html#i97) [\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[i95\]](https://dblp.org/pid/35/11103.html#i95) [\[i93\]](https://dblp.org/pid/35/11103.html#i93) [\[i67\]](https://dblp.org/pid/35/11103.html#i67) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[425](https://dblp.org/pid/35/11103.html?view=joint&param=425 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Vamsi Sistla](https://dblp.org/pid/375/6335.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[426](https://dblp.org/pid/35/11103.html?view=joint&param=426 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Da Song](https://dblp.org/pid/222/6729.html)

[\[j30\]](https://dblp.org/pid/35/11103.html#j30) [\[j16\]](https://dblp.org/pid/35/11103.html#j16) [\[i68\]](https://dblp.org/pid/35/11103.html#i68) [\[i51\]](https://dblp.org/pid/35/11103.html#i51)

[427](https://dblp.org/pid/35/11103.html?view=joint&param=427 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Dawn Song](https://dblp.org/pid/s/DXSong.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[428](https://dblp.org/pid/35/11103.html?view=joint&param=428 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiayang Song](https://dblp.org/pid/182/7194.html)

[\[j30\]](https://dblp.org/pid/35/11103.html#j30) [\[j22\]](https://dblp.org/pid/35/11103.html#j22) [\[j16\]](https://dblp.org/pid/35/11103.html#j16) [\[i69\]](https://dblp.org/pid/35/11103.html#i69) [\[i68\]](https://dblp.org/pid/35/11103.html#i68) [\[i51\]](https://dblp.org/pid/35/11103.html#i51)

[429](https://dblp.org/pid/35/11103.html?view=joint&param=429 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kunpeng Song](https://dblp.org/pid/194/1391.html)

[\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[430](https://dblp.org/pid/35/11103.html?view=joint&param=430 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[431](https://dblp.org/pid/35/11103.html?view=joint&param=431 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yifei Song](https://dblp.org/pid/284/3356.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[432](https://dblp.org/pid/35/11103.html?view=joint&param=432 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Akash Srivastava](https://dblp.org/pid/24/9528.html)

[\[c65\]](https://dblp.org/pid/35/11103.html#c65) [\[i73\]](https://dblp.org/pid/35/11103.html#i73) [\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[433](https://dblp.org/pid/35/11103.html?view=joint&param=433 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Sanbao Su](https://dblp.org/pid/221/2885.html)

[\[i71\]](https://dblp.org/pid/35/11103.html#i71)

[434](https://dblp.org/pid/35/11103.html?view=joint&param=434 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ting Su 0001](https://dblp.org/pid/42/6896-1.html)

[\[c26\]](https://dblp.org/pid/35/11103.html#c26) [\[i9\]](https://dblp.org/pid/35/11103.html#i9)

[435](https://dblp.org/pid/35/11103.html?view=joint&param=435 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Harihar Subramanyam](https://dblp.org/pid/166/8374.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[i96\]](https://dblp.org/pid/35/11103.html#i96) [\[i67\]](https://dblp.org/pid/35/11103.html#i67)

[436](https://dblp.org/pid/35/11103.html?view=joint&param=436 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ching Y. Suen](https://dblp.org/pid/s/ChingYSuen.html)

[\[c3\]](https://dblp.org/pid/35/11103.html#c3)

[437](https://dblp.org/pid/35/11103.html?view=joint&param=437 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Alane Suhr](https://dblp.org/pid/203/9306.html)

[\[i85\]](https://dblp.org/pid/35/11103.html#i85)

[438](https://dblp.org/pid/35/11103.html?view=joint&param=438 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Roshan Sumbaly](https://dblp.org/pid/116/5160.html)

[\[i67\]](https://dblp.org/pid/35/11103.html#i67)

[439](https://dblp.org/pid/35/11103.html?view=joint&param=439 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bo Sun](https://dblp.org/pid/35/892.html)

[\[i93\]](https://dblp.org/pid/35/11103.html#i93) [\[i67\]](https://dblp.org/pid/35/11103.html#i67)

[440](https://dblp.org/pid/35/11103.html?view=joint&param=440 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Guangyan Sun](https://dblp.org/pid/67/9556.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[441](https://dblp.org/pid/35/11103.html?view=joint&param=441 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jingyang Sun](https://dblp.org/pid/217/7354.html)

[\[j28\]](https://dblp.org/pid/35/11103.html#j28) [\[i49\]](https://dblp.org/pid/35/11103.html#i49) [\[c50\]](https://dblp.org/pid/35/11103.html#c50) [\[i16\]](https://dblp.org/pid/35/11103.html#i16)

[442](https://dblp.org/pid/35/11103.html?view=joint&param=442 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiyuan Sun](https://dblp.org/pid/160/6224.html)

[\[c27\]](https://dblp.org/pid/35/11103.html#c27) [\[c26\]](https://dblp.org/pid/35/11103.html#c26) [\[i9\]](https://dblp.org/pid/35/11103.html#i9) [\[i8\]](https://dblp.org/pid/35/11103.html#i8)

[443](https://dblp.org/pid/35/11103.html?view=joint&param=443 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jun Sun 0001](https://dblp.org/pid/s/JunSun1.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[444](https://dblp.org/pid/35/11103.html?view=joint&param=444 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Junzhe Sun](https://dblp.org/pid/389/2226.html)

[\[i84\]](https://dblp.org/pid/35/11103.html#i84) [\[i83\]](https://dblp.org/pid/35/11103.html#i83)

[445](https://dblp.org/pid/35/11103.html?view=joint&param=445 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Liangru Sun](https://dblp.org/pid/311/4944.html)

[\[c53\]](https://dblp.org/pid/35/11103.html#c53) [\[i48\]](https://dblp.org/pid/35/11103.html#i48)

[446](https://dblp.org/pid/35/11103.html?view=joint&param=446 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Peize Sun](https://dblp.org/pid/249/2345.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90)

[447](https://dblp.org/pid/35/11103.html?view=joint&param=447 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shixuan Sun](https://dblp.org/pid/131/9481.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[448](https://dblp.org/pid/35/11103.html?view=joint&param=448 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Weisong Sun](https://dblp.org/pid/183/2642.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[449](https://dblp.org/pid/35/11103.html?view=joint&param=449 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yizhou Sun](https://dblp.org/pid/37/3868.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[450](https://dblp.org/pid/35/11103.html?view=joint&param=450 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chaowei Tan](https://dblp.org/pid/155/3101.html)

[\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[451](https://dblp.org/pid/35/11103.html?view=joint&param=451 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hao Tang](https://dblp.org/pid/07/5751.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90)

[452](https://dblp.org/pid/35/11103.html?view=joint&param=452 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ke Tang](https://dblp.org/pid/50/3146.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[453](https://dblp.org/pid/35/11103.html?view=joint&param=453 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Leonard Tang](https://dblp.org/pid/306/7940.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[454](https://dblp.org/pid/35/11103.html?view=joint&param=454 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ruixiang Tang](https://dblp.org/pid/239/1928.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[455](https://dblp.org/pid/35/11103.html?view=joint&param=455 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[456](https://dblp.org/pid/35/11103.html?view=joint&param=456 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Dacheng Tao](https://dblp.org/pid/46/3391.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91) [\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[457](https://dblp.org/pid/35/11103.html?view=joint&param=457 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Molei Tao](https://dblp.org/pid/56/9263.html)

[\[c65\]](https://dblp.org/pid/35/11103.html#c65) [\[i73\]](https://dblp.org/pid/35/11103.html#i73)

[458](https://dblp.org/pid/35/11103.html?view=joint&param=458 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Douglas Teodoro](https://dblp.org/pid/01/7332.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[459](https://dblp.org/pid/35/11103.html?view=joint&param=459 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Davide Testuggine](https://dblp.org/pid/248/8282.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[460](https://dblp.org/pid/35/11103.html?view=joint&param=460 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ali K. Thabet](https://dblp.org/pid/161/1812.html)

[\[i84\]](https://dblp.org/pid/35/11103.html#i84) [\[i83\]](https://dblp.org/pid/35/11103.html#i83)

[461](https://dblp.org/pid/35/11103.html?view=joint&param=461 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Vithursan Thangarasa](https://dblp.org/pid/223/9965.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[462](https://dblp.org/pid/35/11103.html?view=joint&param=462 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Craig P. Thor](https://dblp.org/pid/169/9127.html)

[\[c17\]](https://dblp.org/pid/35/11103.html#c17)

[463](https://dblp.org/pid/35/11103.html?view=joint&param=463 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Binyu Tian](https://dblp.org/pid/274/7389.html)

[\[c44\]](https://dblp.org/pid/35/11103.html#c44) [\[c43\]](https://dblp.org/pid/35/11103.html#c43) [\[i36\]](https://dblp.org/pid/35/11103.html#i36) [\[i15\]](https://dblp.org/pid/35/11103.html#i15)

[464](https://dblp.org/pid/35/11103.html?view=joint&param=464 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Cong Tian 0001](https://dblp.org/pid/00/5365-1.html)

[\[i21\]](https://dblp.org/pid/35/11103.html#i21)

[465](https://dblp.org/pid/35/11103.html?view=joint&param=465 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Junjiao Tian](https://dblp.org/pid/246/3115.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90)

[466](https://dblp.org/pid/35/11103.html?view=joint&param=466 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yuandong Tian](https://dblp.org/pid/t/YuandongTian.html)

[\[i85\]](https://dblp.org/pid/35/11103.html#i85)

[467](https://dblp.org/pid/35/11103.html?view=joint&param=467 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[468](https://dblp.org/pid/35/11103.html?view=joint&param=468 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[i89\]](https://dblp.org/pid/35/11103.html#i89) [\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[469](https://dblp.org/pid/35/11103.html?view=joint&param=469 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[470](https://dblp.org/pid/35/11103.html?view=joint&param=470 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Sam S. Tsai](https://dblp.org/pid/88/704.html)

[\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i66\]](https://dblp.org/pid/35/11103.html#i66) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[471](https://dblp.org/pid/35/11103.html?view=joint&param=471 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ivor W. Tsang](https://dblp.org/pid/35/5873.html)

[\[i54\]](https://dblp.org/pid/35/11103.html#i54)

[472](https://dblp.org/pid/35/11103.html?view=joint&param=472 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhengzhong Tu](https://dblp.org/pid/218/1473.html)

[\[c62\]](https://dblp.org/pid/35/11103.html#c62) [\[i79\]](https://dblp.org/pid/35/11103.html#i79)

[473](https://dblp.org/pid/35/11103.html?view=joint&param=473 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bedirhan Uzun](https://dblp.org/pid/247/8937.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[474](https://dblp.org/pid/35/11103.html?view=joint&param=474 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Peter Vajda](https://dblp.org/pid/44/5953.html)

[\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[i95\]](https://dblp.org/pid/35/11103.html#i95) [\[i93\]](https://dblp.org/pid/35/11103.html#i93) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i67\]](https://dblp.org/pid/35/11103.html#i67) [\[i66\]](https://dblp.org/pid/35/11103.html#i66) [\[i62\]](https://dblp.org/pid/35/11103.html#i62) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[475](https://dblp.org/pid/35/11103.html?view=joint&param=475 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Joaquin Vanschoren](https://dblp.org/pid/85/5045.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[476](https://dblp.org/pid/35/11103.html?view=joint&param=476 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shreyas Venugopalan](https://dblp.org/pid/70/9171.html)

[\[c16\]](https://dblp.org/pid/35/11103.html#c16) [\[c1\]](https://dblp.org/pid/35/11103.html#c1)

[477](https://dblp.org/pid/35/11103.html?view=joint&param=477 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Eshan Verma](https://dblp.org/pid/191/9419.html)

[\[c22\]](https://dblp.org/pid/35/11103.html#c22)

[478](https://dblp.org/pid/35/11103.html?view=joint&param=478 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bertie Vidgen](https://dblp.org/pid/175/1517.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[479](https://dblp.org/pid/35/11103.html?view=joint&param=479 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Paul Voigtlaender](https://dblp.org/pid/166/6430.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[480](https://dblp.org/pid/35/11103.html?view=joint&param=480 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Guancheng Wan](https://dblp.org/pid/354/1252.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[481](https://dblp.org/pid/35/11103.html?view=joint&param=481 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bin Wang](https://dblp.org/pid/13/1898.html)

[\[i86\]](https://dblp.org/pid/35/11103.html#i86)

[482](https://dblp.org/pid/35/11103.html?view=joint&param=482 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chong Wang 0013](https://dblp.org/pid/72/1334-13.html)

[\[c75\]](https://dblp.org/pid/35/11103.html#c75) [\[i75\]](https://dblp.org/pid/35/11103.html#i75)

[483](https://dblp.org/pid/35/11103.html?view=joint&param=483 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chu Wang](https://dblp.org/pid/45/1543.html)

[\[i87\]](https://dblp.org/pid/35/11103.html#i87) [\[i84\]](https://dblp.org/pid/35/11103.html#i84) [\[i83\]](https://dblp.org/pid/35/11103.html#i83)

[484](https://dblp.org/pid/35/11103.html?view=joint&param=484 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[485](https://dblp.org/pid/35/11103.html?view=joint&param=485 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Dongxia Wang](https://dblp.org/pid/52/645.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[486](https://dblp.org/pid/35/11103.html?view=joint&param=486 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Guangting Wang](https://dblp.org/pid/227/7195.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[487](https://dblp.org/pid/35/11103.html?view=joint&param=487 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hao Wang 0014](https://dblp.org/pid/w/HaoWang-14.html)

[\[c65\]](https://dblp.org/pid/35/11103.html#c65) [\[i73\]](https://dblp.org/pid/35/11103.html#i73)

[488](https://dblp.org/pid/35/11103.html?view=joint&param=488 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hongjie Wang 0002](https://dblp.org/pid/65/7565-2.html)

[\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[i62\]](https://dblp.org/pid/35/11103.html#i62)

[489](https://dblp.org/pid/35/11103.html?view=joint&param=489 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiakai Wang](https://dblp.org/pid/202/9216.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[490](https://dblp.org/pid/35/11103.html?view=joint&param=490 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jialiang Wang 0001](https://dblp.org/pid/27/8578-1.html)

[\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[i92\]](https://dblp.org/pid/35/11103.html#i92) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i87\]](https://dblp.org/pid/35/11103.html#i87) [\[i84\]](https://dblp.org/pid/35/11103.html#i84) [\[i83\]](https://dblp.org/pid/35/11103.html#i83) [\[i66\]](https://dblp.org/pid/35/11103.html#i66) [\[i62\]](https://dblp.org/pid/35/11103.html#i62) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[491](https://dblp.org/pid/35/11103.html?view=joint&param=491 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jian Wang 0067](https://dblp.org/pid/39/449-67.html)

[\[j6\]](https://dblp.org/pid/35/11103.html#j6) [\[i46\]](https://dblp.org/pid/35/11103.html#i46) [\[c37\]](https://dblp.org/pid/35/11103.html#c37) [\[c32\]](https://dblp.org/pid/35/11103.html#c32) [\[i25\]](https://dblp.org/pid/35/11103.html#i25) [\[i11\]](https://dblp.org/pid/35/11103.html#i11)

[492](https://dblp.org/pid/35/11103.html?view=joint&param=492 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jingyi Wang](https://dblp.org/pid/18/3178.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[493](https://dblp.org/pid/35/11103.html?view=joint&param=493 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Junjue Wang](https://dblp.org/pid/146/0104.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[494](https://dblp.org/pid/35/11103.html?view=joint&param=494 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kun Wang 0056](https://dblp.org/pid/05/1958-56.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[495](https://dblp.org/pid/35/11103.html?view=joint&param=495 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[496](https://dblp.org/pid/35/11103.html?view=joint&param=496 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[497](https://dblp.org/pid/35/11103.html?view=joint&param=497 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[498](https://dblp.org/pid/35/11103.html?view=joint&param=498 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Lina Wang 0001](https://dblp.org/pid/01/1318-1.html)

[\[c40\]](https://dblp.org/pid/35/11103.html#c40) [\[i13\]](https://dblp.org/pid/35/11103.html#i13)

[499](https://dblp.org/pid/35/11103.html?view=joint&param=499 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Linyuan Wang](https://dblp.org/pid/138/5963.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[500](https://dblp.org/pid/35/11103.html?view=joint&param=500 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Lubo Wang](https://dblp.org/pid/352/4271.html)

[\[j23\]](https://dblp.org/pid/35/11103.html#j23)

[501](https://dblp.org/pid/35/11103.html?view=joint&param=501 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Minghe Wang](https://dblp.org/pid/84/3647.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[502](https://dblp.org/pid/35/11103.html?view=joint&param=502 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qifan Wang 0001](https://dblp.org/pid/33/8610-1.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[503](https://dblp.org/pid/35/11103.html?view=joint&param=503 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Renzhi Wang](https://dblp.org/pid/152/2466.html)

[\[i21\]](https://dblp.org/pid/35/11103.html#i21)

[504](https://dblp.org/pid/35/11103.html?view=joint&param=504 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Run Wang 0001](https://dblp.org/pid/95/8501-1.html)

[\[i74\]](https://dblp.org/pid/35/11103.html#i74) [\[j12\]](https://dblp.org/pid/35/11103.html#j12) [\[c40\]](https://dblp.org/pid/35/11103.html#c40) [\[i42\]](https://dblp.org/pid/35/11103.html#i42) [\[c37\]](https://dblp.org/pid/35/11103.html#c37) [\[c36\]](https://dblp.org/pid/35/11103.html#c36) [\[c35\]](https://dblp.org/pid/35/11103.html#c35) [\[c34\]](https://dblp.org/pid/35/11103.html#c34) [\[i26\]](https://dblp.org/pid/35/11103.html#i26) [\[i24\]](https://dblp.org/pid/35/11103.html#i24) [\[i23\]](https://dblp.org/pid/35/11103.html#i23) [\[i13\]](https://dblp.org/pid/35/11103.html#i13) [\[i11\]](https://dblp.org/pid/35/11103.html#i11) [\[i10\]](https://dblp.org/pid/35/11103.html#i10)

[505](https://dblp.org/pid/35/11103.html?view=joint&param=505 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shangguang Wang](https://dblp.org/pid/73/8637.html)

[\[j13\]](https://dblp.org/pid/35/11103.html#j13) [\[c55\]](https://dblp.org/pid/35/11103.html#c55) [\[i58\]](https://dblp.org/pid/35/11103.html#i58) [\[i53\]](https://dblp.org/pid/35/11103.html#i53)

[506](https://dblp.org/pid/35/11103.html?view=joint&param=506 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Sida I. Wang](https://dblp.org/pid/153/9609.html)

aka: Sida Wang 0001

[\[i85\]](https://dblp.org/pid/35/11103.html#i85)

[507](https://dblp.org/pid/35/11103.html?view=joint&param=507 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Song Wang 0002](https://dblp.org/pid/62/3151-2.html)

[\[j28\]](https://dblp.org/pid/35/11103.html#j28) [\[c58\]](https://dblp.org/pid/35/11103.html#c58) [\[j10\]](https://dblp.org/pid/35/11103.html#j10) [\[c52\]](https://dblp.org/pid/35/11103.html#c52) [\[i49\]](https://dblp.org/pid/35/11103.html#i49) [\[c49\]](https://dblp.org/pid/35/11103.html#c49) [\[c42\]](https://dblp.org/pid/35/11103.html#c42) [\[i41\]](https://dblp.org/pid/35/11103.html#i41) [\[i37\]](https://dblp.org/pid/35/11103.html#i37) [\[i35\]](https://dblp.org/pid/35/11103.html#i35) [\[i34\]](https://dblp.org/pid/35/11103.html#i34) [\[i27\]](https://dblp.org/pid/35/11103.html#i27) [\[i14\]](https://dblp.org/pid/35/11103.html#i14)

[508](https://dblp.org/pid/35/11103.html?view=joint&param=508 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wei Wang 0010](https://dblp.org/pid/w/WeiWang.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[509](https://dblp.org/pid/35/11103.html?view=joint&param=509 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiang Wang](https://dblp.org/pid/31/2864.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[510](https://dblp.org/pid/35/11103.html?view=joint&param=510 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiao Wang](https://dblp.org/pid/49/67.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[511](https://dblp.org/pid/35/11103.html?view=joint&param=511 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaofang Wang](https://dblp.org/pid/58/2390.html)

[\[c69\]](https://dblp.org/pid/35/11103.html#c69) [\[c68\]](https://dblp.org/pid/35/11103.html#c68) [\[i64\]](https://dblp.org/pid/35/11103.html#i64) [\[i61\]](https://dblp.org/pid/35/11103.html#i61)

[512](https://dblp.org/pid/35/11103.html?view=joint&param=512 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaofeng Wang](https://dblp.org/pid/99/2479.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[513](https://dblp.org/pid/35/11103.html?view=joint&param=513 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaohan Wang](https://dblp.org/pid/73/1307.html)

[\[c69\]](https://dblp.org/pid/35/11103.html#c69) [\[i61\]](https://dblp.org/pid/35/11103.html#i61)

[514](https://dblp.org/pid/35/11103.html?view=joint&param=514 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xun Wang](https://dblp.org/pid/82/1331.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[515](https://dblp.org/pid/35/11103.html?view=joint&param=515 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yadong Wang](https://dblp.org/pid/68/782.html)

[\[c27\]](https://dblp.org/pid/35/11103.html#c27) [\[c26\]](https://dblp.org/pid/35/11103.html#c26) [\[i9\]](https://dblp.org/pid/35/11103.html#i9) [\[i8\]](https://dblp.org/pid/35/11103.html#i8)

[516](https://dblp.org/pid/35/11103.html?view=joint&param=516 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yanfeng Wang 0001](https://dblp.org/pid/55/5407-1.html)

[\[j27\]](https://dblp.org/pid/35/11103.html#j27) [\[i77\]](https://dblp.org/pid/35/11103.html#i77)

[517](https://dblp.org/pid/35/11103.html?view=joint&param=517 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[518](https://dblp.org/pid/35/11103.html?view=joint&param=518 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yunhong Wang 0001](https://dblp.org/pid/95/6251.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[519](https://dblp.org/pid/35/11103.html?view=joint&param=519 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhenting Wang](https://dblp.org/pid/263/4521.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[c68\]](https://dblp.org/pid/35/11103.html#c68) [\[i96\]](https://dblp.org/pid/35/11103.html#i96) [\[i70\]](https://dblp.org/pid/35/11103.html#i70) [\[i64\]](https://dblp.org/pid/35/11103.html#i64)

[520](https://dblp.org/pid/35/11103.html?view=joint&param=520 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhijie Wang 0014](https://dblp.org/pid/64/5749-14.html)

[\[j24\]](https://dblp.org/pid/35/11103.html#j24) [\[j23\]](https://dblp.org/pid/35/11103.html#j23) [\[j22\]](https://dblp.org/pid/35/11103.html#j22) [\[j14\]](https://dblp.org/pid/35/11103.html#j14) [\[i43\]](https://dblp.org/pid/35/11103.html#i43) [\[i31\]](https://dblp.org/pid/35/11103.html#i31) [\[i28\]](https://dblp.org/pid/35/11103.html#i28)

[521](https://dblp.org/pid/35/11103.html?view=joint&param=521 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Elizabeth Anne Watkins](https://dblp.org/pid/196/3030.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[522](https://dblp.org/pid/35/11103.html?view=joint&param=522 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Cong Wei 0001](https://dblp.org/pid/224/8508-1.html)

[\[i93\]](https://dblp.org/pid/35/11103.html#i93)

[523](https://dblp.org/pid/35/11103.html?view=joint&param=523 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiwei Wei](https://dblp.org/pid/31/2031.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[524](https://dblp.org/pid/35/11103.html?view=joint&param=524 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yuxi Wei](https://dblp.org/pid/323/4932.html)

[\[j27\]](https://dblp.org/pid/35/11103.html#j27) [\[i77\]](https://dblp.org/pid/35/11103.html#i77)

[525](https://dblp.org/pid/35/11103.html?view=joint&param=525 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Rebecca Weiss](https://dblp.org/pid/159/0930.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[526](https://dblp.org/pid/35/11103.html?view=joint&param=526 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Christopher A. Welty](https://dblp.org/pid/w/CAWelty.html)

aka: Chris Welty

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[527](https://dblp.org/pid/35/11103.html?view=joint&param=527 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Congcong Wen](https://dblp.org/pid/218/4638.html)

[\[c48\]](https://dblp.org/pid/35/11103.html#c48) [\[i40\]](https://dblp.org/pid/35/11103.html#i40)

[528](https://dblp.org/pid/35/11103.html?view=joint&param=528 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qingsong Wen](https://dblp.org/pid/27/561.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[529](https://dblp.org/pid/35/11103.html?view=joint&param=529 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Song Wen 0001](https://dblp.org/pid/119/9492-1.html)

[\[c65\]](https://dblp.org/pid/35/11103.html#c65) [\[i73\]](https://dblp.org/pid/35/11103.html#i73) [\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[530](https://dblp.org/pid/35/11103.html?view=joint&param=530 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tyler Wilbers](https://dblp.org/pid/375/6232.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[531](https://dblp.org/pid/35/11103.html?view=joint&param=531 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Adina Williams](https://dblp.org/pid/199/2104.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[532](https://dblp.org/pid/35/11103.html?view=joint&param=532 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Carole-Jean Wu](https://dblp.org/pid/26/9655.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[533](https://dblp.org/pid/35/11103.html?view=joint&param=533 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chenyan Wu](https://dblp.org/pid/76/1190.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[534](https://dblp.org/pid/35/11103.html?view=joint&param=534 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Cong Wu](https://dblp.org/pid/30/10768.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[535](https://dblp.org/pid/35/11103.html?view=joint&param=535 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[536](https://dblp.org/pid/35/11103.html?view=joint&param=536 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hao Wu](https://dblp.org/pid/72/4250.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[537](https://dblp.org/pid/35/11103.html?view=joint&param=537 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiahao Wu](https://dblp.org/pid/203/9539.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[538](https://dblp.org/pid/35/11103.html?view=joint&param=538 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shangkun Wu](https://dblp.org/pid/410/2403.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[539](https://dblp.org/pid/35/11103.html?view=joint&param=539 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Siyang Wu](https://dblp.org/pid/159/5536.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[540](https://dblp.org/pid/35/11103.html?view=joint&param=540 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[541](https://dblp.org/pid/35/11103.html?view=joint&param=541 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yutong Wu 0009](https://dblp.org/pid/312/5805.html)

[\[c64\]](https://dblp.org/pid/35/11103.html#c64)

[542](https://dblp.org/pid/35/11103.html?view=joint&param=542 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xide Xia](https://dblp.org/pid/172/0129.html)

[\[c69\]](https://dblp.org/pid/35/11103.html#c69) [\[c68\]](https://dblp.org/pid/35/11103.html#c68) [\[i64\]](https://dblp.org/pid/35/11103.html#i64) [\[i61\]](https://dblp.org/pid/35/11103.html#i61) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[543](https://dblp.org/pid/35/11103.html?view=joint&param=543 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tong Xiao 0003](https://dblp.org/pid/05/5091-3.html)

[\[c70\]](https://dblp.org/pid/35/11103.html#c70) [\[c69\]](https://dblp.org/pid/35/11103.html#c69) [\[i63\]](https://dblp.org/pid/35/11103.html#i63) [\[i61\]](https://dblp.org/pid/35/11103.html#i61)

[544](https://dblp.org/pid/35/11103.html?view=joint&param=544 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yunze Xiao](https://dblp.org/pid/310/1568.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[545](https://dblp.org/pid/35/11103.html?view=joint&param=545 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chao Xie](https://dblp.org/pid/04/5576.html)

[\[c27\]](https://dblp.org/pid/35/11103.html#c27) [\[i8\]](https://dblp.org/pid/35/11103.html#i8)

[546](https://dblp.org/pid/35/11103.html?view=joint&param=546 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[547](https://dblp.org/pid/35/11103.html?view=joint&param=547 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Saining Xie](https://dblp.org/pid/126/0960.html)

[\[i92\]](https://dblp.org/pid/35/11103.html#i92)

[548](https://dblp.org/pid/35/11103.html?view=joint&param=548 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaofei Xie](https://dblp.org/pid/127/0713.html)

[\[j29\]](https://dblp.org/pid/35/11103.html#j29) [\[c67\]](https://dblp.org/pid/35/11103.html#c67) [\[j7\]](https://dblp.org/pid/35/11103.html#j7) [\[j6\]](https://dblp.org/pid/35/11103.html#j6) [\[j5\]](https://dblp.org/pid/35/11103.html#j5) [\[i46\]](https://dblp.org/pid/35/11103.html#i46) [\[c50\]](https://dblp.org/pid/35/11103.html#c50) [\[c47\]](https://dblp.org/pid/35/11103.html#c47) [\[c44\]](https://dblp.org/pid/35/11103.html#c44) [\[c43\]](https://dblp.org/pid/35/11103.html#c43) [\[i36\]](https://dblp.org/pid/35/11103.html#i36) [\[i32\]](https://dblp.org/pid/35/11103.html#i32) [\[c39\]](https://dblp.org/pid/35/11103.html#c39) [\[c37\]](https://dblp.org/pid/35/11103.html#c37) [\[c36\]](https://dblp.org/pid/35/11103.html#c36) [\[c35\]](https://dblp.org/pid/35/11103.html#c35) [\[c34\]](https://dblp.org/pid/35/11103.html#c34) [\[c33\]](https://dblp.org/pid/35/11103.html#c33) [\[c32\]](https://dblp.org/pid/35/11103.html#c32) [\[i26\]](https://dblp.org/pid/35/11103.html#i26) [\[i25\]](https://dblp.org/pid/35/11103.html#i25) [\[i24\]](https://dblp.org/pid/35/11103.html#i24) [\[i23\]](https://dblp.org/pid/35/11103.html#i23) [\[i22\]](https://dblp.org/pid/35/11103.html#i22) [\[i21\]](https://dblp.org/pid/35/11103.html#i21) [\[i20\]](https://dblp.org/pid/35/11103.html#i20) [\[i19\]](https://dblp.org/pid/35/11103.html#i19) [\[i18\]](https://dblp.org/pid/35/11103.html#i18) [\[i17\]](https://dblp.org/pid/35/11103.html#i17) [\[i16\]](https://dblp.org/pid/35/11103.html#i16) [\[i15\]](https://dblp.org/pid/35/11103.html#i15) [\[i12\]](https://dblp.org/pid/35/11103.html#i12) [\[c31\]](https://dblp.org/pid/35/11103.html#c31) [\[i11\]](https://dblp.org/pid/35/11103.html#i11) [\[i10\]](https://dblp.org/pid/35/11103.html#i10) [\[i6\]](https://dblp.org/pid/35/11103.html#i6) [\[i5\]](https://dblp.org/pid/35/11103.html#i5)

[549](https://dblp.org/pid/35/11103.html?view=joint&param=549 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xuan Xie 0001](https://dblp.org/pid/22/10184-1.html)

[\[j30\]](https://dblp.org/pid/35/11103.html#j30) [\[j16\]](https://dblp.org/pid/35/11103.html#j16) [\[i68\]](https://dblp.org/pid/35/11103.html#i68) [\[i51\]](https://dblp.org/pid/35/11103.html#i51)

[550](https://dblp.org/pid/35/11103.html?view=joint&param=550 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yun Xing](https://dblp.org/pid/09/9613.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[551](https://dblp.org/pid/35/11103.html?view=joint&param=551 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hui Xiong 0001](https://dblp.org/pid/262/1686-1.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[552](https://dblp.org/pid/35/11103.html?view=joint&param=552 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chenxin Xu](https://dblp.org/pid/281/7263.html)

[\[j27\]](https://dblp.org/pid/35/11103.html#j27) [\[i77\]](https://dblp.org/pid/35/11103.html#i77)

[553](https://dblp.org/pid/35/11103.html?view=joint&param=553 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Guowen Xu](https://dblp.org/pid/87/10142.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[554](https://dblp.org/pid/35/11103.html?view=joint&param=554 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qianqian Xu 0001](https://dblp.org/pid/07/7627-1.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[555](https://dblp.org/pid/35/11103.html?view=joint&param=555 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Runsheng Xu](https://dblp.org/pid/214/1446.html)

[\[c62\]](https://dblp.org/pid/35/11103.html#c62) [\[i79\]](https://dblp.org/pid/35/11103.html#i79)

[556](https://dblp.org/pid/35/11103.html?view=joint&param=556 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tao Xu](https://dblp.org/pid/96/6771.html)

[\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i62\]](https://dblp.org/pid/35/11103.html#i62)

[557](https://dblp.org/pid/35/11103.html?view=joint&param=557 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[558](https://dblp.org/pid/35/11103.html?view=joint&param=558 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wenyuan Xu](https://dblp.org/pid/10/3878.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[559](https://dblp.org/pid/35/11103.html?view=joint&param=559 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiang Xu](https://dblp.org/pid/126/2962.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[560](https://dblp.org/pid/35/11103.html?view=joint&param=560 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaohai Xu](https://dblp.org/pid/229/1423.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[561](https://dblp.org/pid/35/11103.html?view=joint&param=561 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhihao Xu](https://dblp.org/pid/65/3784.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[562](https://dblp.org/pid/35/11103.html?view=joint&param=562 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhiyang Xu](https://dblp.org/pid/267/2280.html)

[\[i92\]](https://dblp.org/pid/35/11103.html#i92)

[563](https://dblp.org/pid/35/11103.html?view=joint&param=563 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Weihao Xuan](https://dblp.org/pid/249/5453.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[564](https://dblp.org/pid/35/11103.html?view=joint&param=564 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Minhui Xue 0001](https://dblp.org/pid/166/1912.html)

[\[j7\]](https://dblp.org/pid/35/11103.html#j7) [\[c31\]](https://dblp.org/pid/35/11103.html#c31) [\[c30\]](https://dblp.org/pid/35/11103.html#c30) [\[c27\]](https://dblp.org/pid/35/11103.html#c27) [\[c26\]](https://dblp.org/pid/35/11103.html#c26) [\[i9\]](https://dblp.org/pid/35/11103.html#i9) [\[i8\]](https://dblp.org/pid/35/11103.html#i8) [\[i6\]](https://dblp.org/pid/35/11103.html#i6) [\[i4\]](https://dblp.org/pid/35/11103.html#i4)

[565](https://dblp.org/pid/35/11103.html?view=joint&param=565 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[j11\]](https://dblp.org/pid/35/11103.html#j11) [\[i44\]](https://dblp.org/pid/35/11103.html#i44) [\[c46\]](https://dblp.org/pid/35/11103.html#c46) [\[c45\]](https://dblp.org/pid/35/11103.html#c45) [\[i39\]](https://dblp.org/pid/35/11103.html#i39) [\[c39\]](https://dblp.org/pid/35/11103.html#c39) [\[c38\]](https://dblp.org/pid/35/11103.html#c38)

[566](https://dblp.org/pid/35/11103.html?view=joint&param=566 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Poonam Yadav](https://dblp.org/pid/79/9996.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[567](https://dblp.org/pid/35/11103.html?view=joint&param=567 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Adam Yala](https://dblp.org/pid/177/9396.html)

[\[i85\]](https://dblp.org/pid/35/11103.html#i85)

[568](https://dblp.org/pid/35/11103.html?view=joint&param=568 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[569](https://dblp.org/pid/35/11103.html?view=joint&param=569 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shuicheng Yan](https://dblp.org/pid/y/ShuichengYan.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[570](https://dblp.org/pid/35/11103.html?view=joint&param=570 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[571](https://dblp.org/pid/35/11103.html?view=joint&param=571 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yibo Yan](https://dblp.org/pid/194/2701.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[572](https://dblp.org/pid/35/11103.html?view=joint&param=572 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yu Yan](https://dblp.org/pid/12/778.html)

[\[c66\]](https://dblp.org/pid/35/11103.html#c66) [\[i50\]](https://dblp.org/pid/35/11103.html#i50)

[573](https://dblp.org/pid/35/11103.html?view=joint&param=573 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Di Yang](https://dblp.org/pid/29/5427.html)

[\[c61\]](https://dblp.org/pid/35/11103.html#c61) [\[i74\]](https://dblp.org/pid/35/11103.html#i74) [\[i55\]](https://dblp.org/pid/35/11103.html#i55)

[574](https://dblp.org/pid/35/11103.html?view=joint&param=574 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Fan Yang 0023](https://dblp.org/pid/29/3081-23.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[575](https://dblp.org/pid/35/11103.html?view=joint&param=575 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[576](https://dblp.org/pid/35/11103.html?view=joint&param=576 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Rui Yang 0016](https://dblp.org/pid/92/1942-16.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[577](https://dblp.org/pid/35/11103.html?view=joint&param=577 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[578](https://dblp.org/pid/35/11103.html?view=joint&param=578 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xianjun Yang](https://dblp.org/pid/37/10237.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[579](https://dblp.org/pid/35/11103.html?view=joint&param=579 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[580](https://dblp.org/pid/35/11103.html?view=joint&param=580 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yang Yang](https://dblp.org/pid/48/450.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[581](https://dblp.org/pid/35/11103.html?view=joint&param=581 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yaodong Yang 0001](https://dblp.org/pid/170/1496-1.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[582](https://dblp.org/pid/35/11103.html?view=joint&param=582 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yun Yang 0001](https://dblp.org/pid/90/3406-1.html)

[\[j13\]](https://dblp.org/pid/35/11103.html#j13) [\[i58\]](https://dblp.org/pid/35/11103.html#i58)

[583](https://dblp.org/pid/35/11103.html?view=joint&param=583 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yu Ye 0004](https://dblp.org/pid/129/0969-4.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[584](https://dblp.org/pid/35/11103.html?view=joint&param=584 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Serena Yeung-Levy](https://dblp.org/pid/147/5023.html)

[\[c69\]](https://dblp.org/pid/35/11103.html#c69) [\[i61\]](https://dblp.org/pid/35/11103.html#i61)

[585](https://dblp.org/pid/35/11103.html?view=joint&param=585 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chenlong Yin](https://dblp.org/pid/384/4116.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[586](https://dblp.org/pid/35/11103.html?view=joint&param=586 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[J. Yin](https://dblp.org/pid/51/2242.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[587](https://dblp.org/pid/35/11103.html?view=joint&param=587 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jianxiong Yin](https://dblp.org/pid/132/8514.html)

[\[c31\]](https://dblp.org/pid/35/11103.html#c31) [\[i6\]](https://dblp.org/pid/35/11103.html#i6) [\[i4\]](https://dblp.org/pid/35/11103.html#i4)

[588](https://dblp.org/pid/35/11103.html?view=joint&param=588 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jun Yin 0003](https://dblp.org/pid/58/5423-3.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[589](https://dblp.org/pid/35/11103.html?view=joint&param=589 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Sheng Yin](https://dblp.org/pid/52/2662.html)

[\[j27\]](https://dblp.org/pid/35/11103.html#j27) [\[i77\]](https://dblp.org/pid/35/11103.html#i77)

[590](https://dblp.org/pid/35/11103.html?view=joint&param=590 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Peng Ying](https://dblp.org/pid/167/4741.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[591](https://dblp.org/pid/35/11103.html?view=joint&param=591 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zonghao Ying](https://dblp.org/pid/302/7374.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[592](https://dblp.org/pid/35/11103.html?view=joint&param=592 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Osamu Yoshie](https://dblp.org/pid/14/5985.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[593](https://dblp.org/pid/35/11103.html?view=joint&param=593 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bing Yu](https://dblp.org/pid/47/2129.html)

[\[j5\]](https://dblp.org/pid/35/11103.html#j5) [\[c38\]](https://dblp.org/pid/35/11103.html#c38) [\[c32\]](https://dblp.org/pid/35/11103.html#c32) [\[i12\]](https://dblp.org/pid/35/11103.html#i12)

[594](https://dblp.org/pid/35/11103.html?view=joint&param=594 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Hongkai Yu](https://dblp.org/pid/150/6670.html)

[\[j19\]](https://dblp.org/pid/35/11103.html#j19) [\[c62\]](https://dblp.org/pid/35/11103.html#c62) [\[c59\]](https://dblp.org/pid/35/11103.html#c59) [\[c58\]](https://dblp.org/pid/35/11103.html#c58) [\[i82\]](https://dblp.org/pid/35/11103.html#i82) [\[i79\]](https://dblp.org/pid/35/11103.html#i79) [\[j10\]](https://dblp.org/pid/35/11103.html#j10) [\[c52\]](https://dblp.org/pid/35/11103.html#c52) [\[c49\]](https://dblp.org/pid/35/11103.html#c49) [\[c42\]](https://dblp.org/pid/35/11103.html#c42) [\[i41\]](https://dblp.org/pid/35/11103.html#i41) [\[i38\]](https://dblp.org/pid/35/11103.html#i38) [\[i37\]](https://dblp.org/pid/35/11103.html#i37) [\[i34\]](https://dblp.org/pid/35/11103.html#i34) [\[i30\]](https://dblp.org/pid/35/11103.html#i30) [\[i27\]](https://dblp.org/pid/35/11103.html#i27) [\[i14\]](https://dblp.org/pid/35/11103.html#i14)

[595](https://dblp.org/pid/35/11103.html?view=joint&param=595 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kaiyuan Yu](https://dblp.org/pid/367/9370.html)

[\[i81\]](https://dblp.org/pid/35/11103.html#i81)

[596](https://dblp.org/pid/35/11103.html?view=joint&param=596 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kunyu Yu](https://dblp.org/pid/381/5302.html)

[\[c67\]](https://dblp.org/pid/35/11103.html#c67)

[597](https://dblp.org/pid/35/11103.html?view=joint&param=597 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Licheng Yu](https://dblp.org/pid/32/10805.html)

[\[c69\]](https://dblp.org/pid/35/11103.html#c69) [\[c68\]](https://dblp.org/pid/35/11103.html#c68) [\[i64\]](https://dblp.org/pid/35/11103.html#i64) [\[i61\]](https://dblp.org/pid/35/11103.html#i61)

[598](https://dblp.org/pid/35/11103.html?view=joint&param=598 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Matthew Yu](https://dblp.org/pid/262/6275.html)

[\[i66\]](https://dblp.org/pid/35/11103.html#i66)

[599](https://dblp.org/pid/35/11103.html?view=joint&param=599 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Miao Yu](https://dblp.org/pid/49/1749.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[600](https://dblp.org/pid/35/11103.html?view=joint&param=600 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Philip S. Yu](https://dblp.org/pid/y/PhilipSYu.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[601](https://dblp.org/pid/35/11103.html?view=joint&param=601 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qinkai Yu](https://dblp.org/pid/350/0275.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[602](https://dblp.org/pid/35/11103.html?view=joint&param=602 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yue Yu](https://dblp.org/pid/55/2008.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[603](https://dblp.org/pid/35/11103.html?view=joint&param=603 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiangyu Yue 0001](https://dblp.org/pid/207/7518.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[604](https://dblp.org/pid/35/11103.html?view=joint&param=604 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yanwei Yue](https://dblp.org/pid/289/8664.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[605](https://dblp.org/pid/35/11103.html?view=joint&param=605 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Alan L. Yuille](https://dblp.org/pid/y/AlanLYuille.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89) [\[i83\]](https://dblp.org/pid/35/11103.html#i83)

[606](https://dblp.org/pid/35/11103.html?view=joint&param=606 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Alireza Zareian](https://dblp.org/pid/154/6427.html)

[\[i67\]](https://dblp.org/pid/35/11103.html#i67)

[607](https://dblp.org/pid/35/11103.html?view=joint&param=607 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Niv Zehngut](https://dblp.org/pid/172/9934.html)

[\[c14\]](https://dblp.org/pid/35/11103.html#c14)

[608](https://dblp.org/pid/35/11103.html?view=joint&param=608 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qingcheng Zeng](https://dblp.org/pid/84/1451.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[c67\]](https://dblp.org/pid/35/11103.html#c67) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[609](https://dblp.org/pid/35/11103.html?view=joint&param=609 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yi Zeng 0005](https://dblp.org/pid/75/148-5.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[610](https://dblp.org/pid/35/11103.html?view=joint&param=610 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Liming Zhai](https://dblp.org/pid/149/3381.html)

[\[j29\]](https://dblp.org/pid/35/11103.html#j29) [\[i19\]](https://dblp.org/pid/35/11103.html#i19)

[611](https://dblp.org/pid/35/11103.html?view=joint&param=611 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Cen Zhang](https://dblp.org/pid/200/7275.html)

[\[c54\]](https://dblp.org/pid/35/11103.html#c54) [\[i52\]](https://dblp.org/pid/35/11103.html#i52)

[612](https://dblp.org/pid/35/11103.html?view=joint&param=612 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[613](https://dblp.org/pid/35/11103.html?view=joint&param=613 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Christina Zhang](https://dblp.org/pid/41/9457.html)

[\[i66\]](https://dblp.org/pid/35/11103.html#i66)

[614](https://dblp.org/pid/35/11103.html?view=joint&param=614 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[615](https://dblp.org/pid/35/11103.html?view=joint&param=615 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Fan Zhang](https://dblp.org/pid/21/3626.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[616](https://dblp.org/pid/35/11103.html?view=joint&param=616 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Fuyuan Zhang](https://dblp.org/pid/08/7637.html)

[\[i68\]](https://dblp.org/pid/35/11103.html#i68) [\[j14\]](https://dblp.org/pid/35/11103.html#j14) [\[c27\]](https://dblp.org/pid/35/11103.html#c27) [\[c26\]](https://dblp.org/pid/35/11103.html#c26) [\[i9\]](https://dblp.org/pid/35/11103.html#i9) [\[i8\]](https://dblp.org/pid/35/11103.html#i8)

[617](https://dblp.org/pid/35/11103.html?view=joint&param=617 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Guibin Zhang](https://dblp.org/pid/227/3812.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[618](https://dblp.org/pid/35/11103.html?view=joint&param=618 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Haitao Zhang](https://dblp.org/pid/19/6669.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[619](https://dblp.org/pid/35/11103.html?view=joint&param=619 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Han Zhang 0010](https://dblp.org/pid/26/4189-10.html)

[\[i65\]](https://dblp.org/pid/35/11103.html#i65)

[620](https://dblp.org/pid/35/11103.html?view=joint&param=620 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Haochen Zhang](https://dblp.org/pid/133/3401.html)

[\[i97\]](https://dblp.org/pid/35/11103.html#i97)

[621](https://dblp.org/pid/35/11103.html?view=joint&param=621 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jian Zhang 0087](https://dblp.org/pid/07/314-87.html)

[\[c75\]](https://dblp.org/pid/35/11103.html#c75) [\[i75\]](https://dblp.org/pid/35/11103.html#i75)

[622](https://dblp.org/pid/35/11103.html?view=joint&param=622 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jie Zhang 0002](https://dblp.org/pid/84/6889-2.html)

[\[c64\]](https://dblp.org/pid/35/11103.html#c64)

[623](https://dblp.org/pid/35/11103.html?view=joint&param=623 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jie Zhang 0073](https://dblp.org/pid/84/6889-73.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[624](https://dblp.org/pid/35/11103.html?view=joint&param=624 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[625](https://dblp.org/pid/35/11103.html?view=joint&param=625 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Kangkai Zhang](https://dblp.org/pid/260/2990.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[626](https://dblp.org/pid/35/11103.html?view=joint&param=626 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Luxin Zhang](https://dblp.org/pid/218/7106.html)

[\[i93\]](https://dblp.org/pid/35/11103.html#i93)

[627](https://dblp.org/pid/35/11103.html?view=joint&param=627 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ning Zhang](https://dblp.org/pid/181/2597.html)

[\[c70\]](https://dblp.org/pid/35/11103.html#c70) [\[c69\]](https://dblp.org/pid/35/11103.html#c69) [\[c68\]](https://dblp.org/pid/35/11103.html#c68) [\[i67\]](https://dblp.org/pid/35/11103.html#i67) [\[i64\]](https://dblp.org/pid/35/11103.html#i64) [\[i63\]](https://dblp.org/pid/35/11103.html#i63) [\[i61\]](https://dblp.org/pid/35/11103.html#i61)

[628](https://dblp.org/pid/35/11103.html?view=joint&param=628 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ningyu Zhang 0001](https://dblp.org/pid/139/4181-1.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[629](https://dblp.org/pid/35/11103.html?view=joint&param=629 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Peizhao Zhang](https://dblp.org/pid/23/8011.html)

[\[i97\]](https://dblp.org/pid/35/11103.html#i97) [\[c73\]](https://dblp.org/pid/35/11103.html#c73) [\[c72\]](https://dblp.org/pid/35/11103.html#c72) [\[i95\]](https://dblp.org/pid/35/11103.html#i95) [\[i90\]](https://dblp.org/pid/35/11103.html#i90) [\[i88\]](https://dblp.org/pid/35/11103.html#i88) [\[i67\]](https://dblp.org/pid/35/11103.html#i67) [\[i62\]](https://dblp.org/pid/35/11103.html#i62) [\[i60\]](https://dblp.org/pid/35/11103.html#i60)

[630](https://dblp.org/pid/35/11103.html?view=joint&param=630 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Qian Zhang 0051](https://dblp.org/pid/04/2024-51.html)

[\[j19\]](https://dblp.org/pid/35/11103.html#j19) [\[i30\]](https://dblp.org/pid/35/11103.html#i30)

[631](https://dblp.org/pid/35/11103.html?view=joint&param=631 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tianwei Zhang 0004](https://dblp.org/pid/77/7902-4.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91) [\[i21\]](https://dblp.org/pid/35/11103.html#i21)

[632](https://dblp.org/pid/35/11103.html?view=joint&param=632 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Tianyuan Zhang 0004](https://dblp.org/pid/145/6286-4.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[633](https://dblp.org/pid/35/11103.html?view=joint&param=633 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Wenhui Zhang](https://dblp.org/pid/82/13.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[634](https://dblp.org/pid/35/11103.html?view=joint&param=634 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaohan Zhang](https://dblp.org/pid/96/6053.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[635](https://dblp.org/pid/35/11103.html?view=joint&param=635 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xiaolin Zhang](https://dblp.org/pid/99/2516.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[636](https://dblp.org/pid/35/11103.html?view=joint&param=636 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xinxi Zhang](https://dblp.org/pid/246/3433.html)

[\[c65\]](https://dblp.org/pid/35/11103.html#c65) [\[i73\]](https://dblp.org/pid/35/11103.html#i73)

[637](https://dblp.org/pid/35/11103.html?view=joint&param=637 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xinyu Zhang 0020](https://dblp.org/pid/58/4582-20.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[638](https://dblp.org/pid/35/11103.html?view=joint&param=638 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yifan Zhang](https://dblp.org/pid/57/4707.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[639](https://dblp.org/pid/35/11103.html?view=joint&param=639 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yongfeng Zhang 0003](https://dblp.org/pid/82/7829-3.html)

[\[c74\]](https://dblp.org/pid/35/11103.html#c74) [\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[640](https://dblp.org/pid/35/11103.html?view=joint&param=640 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[641](https://dblp.org/pid/35/11103.html?view=joint&param=641 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[642](https://dblp.org/pid/35/11103.html?view=joint&param=642 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jianjun Zhao 0001](https://dblp.org/pid/71/6948-1.html)

[\[c60\]](https://dblp.org/pid/35/11103.html#c60) [\[i78\]](https://dblp.org/pid/35/11103.html#i78) [\[j14\]](https://dblp.org/pid/35/11103.html#j14) [\[j11\]](https://dblp.org/pid/35/11103.html#j11) [\[j5\]](https://dblp.org/pid/35/11103.html#j5) [\[i44\]](https://dblp.org/pid/35/11103.html#i44) [\[c50\]](https://dblp.org/pid/35/11103.html#c50) [\[c47\]](https://dblp.org/pid/35/11103.html#c47) [\[c45\]](https://dblp.org/pid/35/11103.html#c45) [\[i39\]](https://dblp.org/pid/35/11103.html#i39) [\[i32\]](https://dblp.org/pid/35/11103.html#i32) [\[i28\]](https://dblp.org/pid/35/11103.html#i28) [\[c38\]](https://dblp.org/pid/35/11103.html#c38) [\[c33\]](https://dblp.org/pid/35/11103.html#c33) [\[i22\]](https://dblp.org/pid/35/11103.html#i22) [\[i12\]](https://dblp.org/pid/35/11103.html#i12) [\[c31\]](https://dblp.org/pid/35/11103.html#c31) [\[c30\]](https://dblp.org/pid/35/11103.html#c30) [\[c27\]](https://dblp.org/pid/35/11103.html#c27) [\[c26\]](https://dblp.org/pid/35/11103.html#c26) [\[i9\]](https://dblp.org/pid/35/11103.html#i9) [\[i8\]](https://dblp.org/pid/35/11103.html#i8) [\[i6\]](https://dblp.org/pid/35/11103.html#i6) [\[i4\]](https://dblp.org/pid/35/11103.html#i4)

[643](https://dblp.org/pid/35/11103.html?view=joint&param=643 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[644](https://dblp.org/pid/35/11103.html?view=joint&param=644 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shengming Zhao](https://dblp.org/pid/366/2862.html)

[\[j22\]](https://dblp.org/pid/35/11103.html#j22)

[645](https://dblp.org/pid/35/11103.html?view=joint&param=645 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shiqian Zhao](https://dblp.org/pid/348/9458.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[646](https://dblp.org/pid/35/11103.html?view=joint&param=646 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Shiyu Zhao 0001](https://dblp.org/pid/120/7474-1.html)

[\[c71\]](https://dblp.org/pid/35/11103.html#c71) [\[c68\]](https://dblp.org/pid/35/11103.html#c68) [\[i96\]](https://dblp.org/pid/35/11103.html#i96) [\[i64\]](https://dblp.org/pid/35/11103.html#i64)

[647](https://dblp.org/pid/35/11103.html?view=joint&param=647 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhuokai Zhao](https://dblp.org/pid/348/5348.html)

[\[i92\]](https://dblp.org/pid/35/11103.html#i92)

[648](https://dblp.org/pid/35/11103.html?view=joint&param=648 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Fedor Zhdanov](https://dblp.org/pid/83/904.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[649](https://dblp.org/pid/35/11103.html?view=joint&param=649 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Ming Zhen](https://dblp.org/pid/307/8430.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[650](https://dblp.org/pid/35/11103.html?view=joint&param=650 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Yaozhi Zheng](https://dblp.org/pid/410/2408.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[651](https://dblp.org/pid/35/11103.html?view=joint&param=651 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[652](https://dblp.org/pid/35/11103.html?view=joint&param=652 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Changqing Zhou](https://dblp.org/pid/40/6559.html)

[\[c49\]](https://dblp.org/pid/35/11103.html#c49) [\[i41\]](https://dblp.org/pid/35/11103.html#i41) [\[i35\]](https://dblp.org/pid/35/11103.html#i35)

[653](https://dblp.org/pid/35/11103.html?view=joint&param=653 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiawei Zhou](https://dblp.org/pid/126/4991.html)

[\[i87\]](https://dblp.org/pid/35/11103.html#i87)

[654](https://dblp.org/pid/35/11103.html?view=joint&param=654 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Joey Tianyi Zhou](https://dblp.org/pid/123/5110.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[655](https://dblp.org/pid/35/11103.html?view=joint&param=655 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xinyun Zhou](https://dblp.org/pid/44/7544.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[656](https://dblp.org/pid/35/11103.html?view=joint&param=656 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhenhong Zhou](https://dblp.org/pid/295/5709.html)

[\[i91\]](https://dblp.org/pid/35/11103.html#i91)

[657](https://dblp.org/pid/35/11103.html?view=joint&param=657 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zihao Zhou](https://dblp.org/pid/139/5953.html)

[\[i70\]](https://dblp.org/pid/35/11103.html#i70)

[658](https://dblp.org/pid/35/11103.html?view=joint&param=658 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Chenguang Zhu](https://dblp.org/pid/48/7536.html)

[\[c70\]](https://dblp.org/pid/35/11103.html#c70) [\[i63\]](https://dblp.org/pid/35/11103.html#i63)

[659](https://dblp.org/pid/35/11103.html?view=joint&param=659 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Derui Zhu](https://dblp.org/pid/203/9320.html)

[\[j16\]](https://dblp.org/pid/35/11103.html#j16) [\[i51\]](https://dblp.org/pid/35/11103.html#i51)

[660](https://dblp.org/pid/35/11103.html?view=joint&param=660 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiacheng Zhu](https://dblp.org/pid/40/10195.html)

[\[i76\]](https://dblp.org/pid/35/11103.html#i76)

[661](https://dblp.org/pid/35/11103.html?view=joint&param=661 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[662](https://dblp.org/pid/35/11103.html?view=joint&param=662 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Jiayi Zhu 0002](https://dblp.org/pid/53/1649-2.html)

[\[i86\]](https://dblp.org/pid/35/11103.html#i86) [\[c63\]](https://dblp.org/pid/35/11103.html#c63) [\[i80\]](https://dblp.org/pid/35/11103.html#i80) [\[i59\]](https://dblp.org/pid/35/11103.html#i59) [\[c53\]](https://dblp.org/pid/35/11103.html#c53) [\[c51\]](https://dblp.org/pid/35/11103.html#c51) [\[i48\]](https://dblp.org/pid/35/11103.html#i48) [\[i47\]](https://dblp.org/pid/35/11103.html#i47)

[663](https://dblp.org/pid/35/11103.html?view=joint&param=663 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Mingzhi Zhu](https://dblp.org/pid/29/8415.html)

[\[c66\]](https://dblp.org/pid/35/11103.html#c66) [\[i50\]](https://dblp.org/pid/35/11103.html#i50)

[664](https://dblp.org/pid/35/11103.html?view=joint&param=664 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c46\]](https://dblp.org/pid/35/11103.html#c46)

[665](https://dblp.org/pid/35/11103.html?view=joint&param=665 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Zhilei Zhu](https://dblp.org/pid/344/7849.html)

[\[i89\]](https://dblp.org/pid/35/11103.html#i89)

[666](https://dblp.org/pid/35/11103.html?view=joint&param=666 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/35/11103.html?view=group&param=1)

[Orr Zohar](https://dblp.org/pid/335/1624.html)

[\[c69\]](https://dblp.org/pid/35/11103.html#c69) [\[i61\]](https://dblp.org/pid/35/11103.html#i61)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/35/11103.html#) [\[–\]](https://dblp.org/pid/35/11103.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/35/11103.html#) [\[–\]](https://dblp.org/pid/35/11103.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/35/11103.html#) [\[–\]](https://dblp.org/pid/35/11103.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/35/11103.html#) [\[–\]](https://dblp.org/pid/35/11103.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/35/11103.html#) [\[–\]](https://dblp.org/pid/35/11103.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)