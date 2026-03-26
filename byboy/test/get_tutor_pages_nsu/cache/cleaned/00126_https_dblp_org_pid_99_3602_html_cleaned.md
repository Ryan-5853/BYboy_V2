> 抓取来源：https://dblp.org/pid/99/3602.html

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

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Wankou+Yang%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F99%2F3602%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Wankou+Yang+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F99%2F3602%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Wankou+Yang+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F99%2F3602%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Wankou+Yang%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F99%2F3602%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Wankou+Yang+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F99%2F3602%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Wankou+Yang%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F99%2F3602%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Wankou+Yang%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F99%2F3602%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F99%2F3602%3E+%7D+.%0A%0A%7D)

_showing all283 records_

20052026302005: 12006: 12008: 52008: 52009: 32009: 32010: 42010: 42011: 112011: 112012: 112012: 112013: 92013: 92013: 92014: 52014: 52015: 182015: 182016: 172016: 172016: 172017: 172017: 172017: 172018: 122018: 122018: 122019: 152019: 152019: 152020: 162020: 162020: 162021: 232021: 232021: 232022: 172022: 172022: 172023: 332023: 332023: 332024: 292024: 292024: 292025: 272025: 272025: 272026: 9

**refine by search term**

![](https://dblp.org/img/clear-mark.medium.16x16.png)![filter active](https://dblp.org/img/filter-mark.12x12.png)

**refine by type**

- [ ] Journal Articles(only)
- [ ] Conference and Workshop Papers(only)
- [ ] Editorship(only)
- [ ] Informal and Other Publications(only)

- select all \| deselect all

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by coauthor**

- ![](https://dblp.org/img/add-mark.12x12.png)Changyin Sun 0001 (64)
- ![](https://dblp.org/img/add-mark.12x12.png)Jifeng Shen (36)
- ![](https://dblp.org/img/add-mark.12x12.png)Jun Li 0033 (26)
- ![](https://dblp.org/img/add-mark.12x12.png)Xin Zuo (24)
- ![](https://dblp.org/img/add-mark.12x12.png)Sen Yang (23)
- ![](https://dblp.org/img/add-mark.12x12.png)Baochang Zhang 0001 (16)
- ![](https://dblp.org/img/add-mark.12x12.png)Ming Dai (16)
- ![](https://dblp.org/img/add-mark.12x12.png)Fei Xie (14)
- ![](https://dblp.org/img/add-mark.12x12.png)Jing-Yu Yang 0001 (14)
- ![](https://dblp.org/img/add-mark.12x12.png)Zhenhua Feng 0001 (13)

- _590 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (239)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-6385-6776 (44)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (47)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (39)
- ![](https://dblp.org/img/add-mark.12x12.png)Neurocomputing (27)
- ![](https://dblp.org/img/add-mark.12x12.png)Pattern Recognit. (24)
- ![](https://dblp.org/img/add-mark.12x12.png)IScIDE (18)
- ![](https://dblp.org/img/add-mark.12x12.png)J. Vis. Commun. Image Represent. (9)
- ![](https://dblp.org/img/add-mark.12x12.png)CCBR (8)
- ![](https://dblp.org/img/add-mark.12x12.png)CCIS (8)
- ![](https://dblp.org/img/add-mark.12x12.png)ICCV (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Neural Comput. Appl. (6)
- ![](https://dblp.org/img/add-mark.12x12.png)ICPR (6)

- _67 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (220)
- ![](https://dblp.org/img/add-mark.12x12.png)open (61)
- ![](https://dblp.org/img/add-mark.12x12.png)unavailable (1)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[j149\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), [Haibo Zhan](https://dblp.org/pid/413/3286.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shaohua Dong](https://dblp.org/pid/188/4523.html), [Xin Zuo](https://dblp.org/pid/15/2278.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Haibin Ling](https://dblp.org/pid/93/3488.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Multispectral state-space feature fusion: Bridging shared and cross-parametric interactions for object detection. [Inf. Fusion127](https://dblp.org/db/journals/inffus/inffus127.html#journals/inffus/ShenZDZYL26): 103895 (2026)
- ![](https://dblp.org/img/n.png)

\[j148\]
[Wenkang Zhang](https://dblp.org/pid/340/0966.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Fei Xie](https://dblp.org/pid/51/1316.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jinhui Wu](https://dblp.org/pid/36/6077.html), Wankou Yang:

TATrack: Target-oriented adaptive vision transformer for UAV tracking. [Neural Networks193](https://dblp.org/db/journals/nn/nn193.html#journals/nn/ZhangXXWY26): 108067 (2026)
- ![](https://dblp.org/img/n.png)

\[j147\]
[Yunfei Ma](https://dblp.org/pid/80/7673.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Li](https://dblp.org/pid/17/2703-40.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lingfeng Yang](https://dblp.org/pid/45/7593.html), [Yifei Su](https://dblp.org/pid/237/4153.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yingpeng Li](https://dblp.org/pid/388/6664.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Shadow-DETR: Alleviating matching conflicts through shadow queries. [Neural Networks197](https://dblp.org/db/journals/nn/nn197.html#journals/nn/MaLYSLY26): 108524 (2026)
- ![](https://dblp.org/img/n.png)

\[j146\]
[Ming Dai](https://dblp.org/pid/61/6981.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenxuan Cheng](https://dblp.org/pid/370/2615.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiang-Jiang Liu](https://dblp.org/pid/18/2542-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lingfeng Yang](https://dblp.org/pid/45/7593.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Jingdong Wang](https://dblp.org/pid/49/3441.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Improving Generalized Visual Grounding With Instance-Aware Joint Learning. [IEEE Trans. Pattern Anal. Mach. Intell.48(1)](https://dblp.org/db/journals/pami/pami48.html#journals/pami/DaiCLYFYW26): 448-465 (2026)
- ![](https://dblp.org/img/n.png)

\[j145\]
[Yihao Xu](https://dblp.org/pid/254/1616.html), [Ming Dai](https://dblp.org/pid/61/6981.html), [Xiang Li](https://dblp.org/pid/40/1491-41.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuncong Yao](https://dblp.org/pid/17/5361.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

DTSI: Towards faster convergence of query-based detectors for rotated dense aerial images. [Pattern Recognit.172](https://dblp.org/db/journals/pr/pr172.html#journals/pr/XuDLYY26): 112729 (2026)
- ![](https://dblp.org/img/n.png)

\[j144\]
[Wenxiao Cai](https://dblp.org/pid/348/4892.html), [Dongting Hu](https://dblp.org/pid/159/6788.html), [Ruoyan Yin](https://dblp.org/pid/395/6967.html), [Jiankang Deng](https://dblp.org/pid/156/7808.html), [Huan Fu](https://dblp.org/pid/139/8082.html), Wankou Yang, [Mingming Gong](https://dblp.org/pid/98/8479.html):

Probabilistic modeling of disparity uncertainty for robust and efficient stereo matching. [Pattern Recognit.175](https://dblp.org/db/journals/pr/pr175.html#journals/pr/CaiHYDFYG26): 113102 (2026)
- ![](https://dblp.org/img/n.png)

\[j143\]
[Ze Feng](https://dblp.org/pid/12/5914.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Jiang-Jiang Liu](https://dblp.org/pid/18/2542-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

PoseAdapter: Efficiently transferring 2D human pose estimator to 3D whole-body task via adapter. [Pattern Recognit.175](https://dblp.org/db/journals/pr/pr175.html#journals/pr/FengYLY26): 113154 (2026)
- ![](https://dblp.org/img/n.png)

\[j142\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), [Haibo Zhan](https://dblp.org/pid/413/3286.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Zuo](https://dblp.org/pid/15/2278.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaohui Yuan](https://dblp.org/pid/61/623-1.html), [Jun Li](https://dblp.org/pid/116/1011-33.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

IRDFusion: Iterative relation-map difference guided feature fusion for multispectral object detection. [Pattern Recognit.176](https://dblp.org/db/journals/pr/pr176.html#journals/pr/ShenZZFYLY26): 113189 (2026)
- ![](https://dblp.org/img/n.png)

\[j141\]
[Ming Dai](https://dblp.org/pid/61/6981.html), [Enhui Zheng](https://dblp.org/pid/138/8144.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenxuan Cheng](https://dblp.org/pid/370/2615.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiahao Chen](https://dblp.org/pid/149/2661.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

DRL: An efficient heterogeneous spatial feature interaction framework for UAV self-localization. [Pattern Recognit.177](https://dblp.org/db/journals/pr/pr177.html#journals/pr/DaiZCCFY26): 113330 (2026)
- 2025
- ![](https://dblp.org/img/n.png)

\[j140\]
[Jingren Liu](https://dblp.org/pid/269/7845.html), [Ke Sun](https://dblp.org/pid/69/476.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zheng Zhang](https://dblp.org/pid/181/2621-6.html), [Yang Long](https://dblp.org/pid/82/10183-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Yunyang Yan](https://dblp.org/pid/11/4039.html), [Haofeng Zhang](https://dblp.org/pid/17/4297.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Synthesizing Spreading-out features for generative zero-shot image classification. [Eng. Appl. Artif. Intell.144](https://dblp.org/db/journals/eaai/eaai144.html#journals/eaai/LiuSZLYYZ25): 110151 (2025)
- ![](https://dblp.org/img/n.png)

\[j139\]
[Yixin Xu](https://dblp.org/pid/04/5753.html), Wankou Yang:

Efficient template-separable hierarchical transformer tracking for edge computing. [Eng. Appl. Artif. Intell.162](https://dblp.org/db/journals/eaai/eaai162.html#journals/eaai/XuY25a): 112784 (2025)
- ![](https://dblp.org/img/n.png)

\[j138\]
[Wenxiao Cai](https://dblp.org/pid/348/4892.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ke Jin](https://dblp.org/pid/94/2193.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jinyan Hou](https://dblp.org/pid/348/4547.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Cong Guo](https://dblp.org/pid/117/1754.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Letian Wu](https://dblp.org/pid/322/6967.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

VDD: Varied Drone Dataset for semantic segmentation. [J. Vis. Commun. Image Represent.109](https://dblp.org/db/journals/jvcir/jvcir109.html#journals/jvcir/CaiJHGWY25): 104429 (2025)
- ![](https://dblp.org/img/n.png)

\[j137\]
[Jinhui Wu](https://dblp.org/pid/36/6077.html), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Exploring efficient appearance prompts for light-weight object tracking. [J. Vis. Commun. Image Represent.113](https://dblp.org/db/journals/jvcir/jvcir113.html#journals/jvcir/WuZY25): 104608 (2025)
- ![](https://dblp.org/img/n.png)

\[j136\]
[Xin Zuo](https://dblp.org/pid/15/2278.html), [Jiaran Jiang](https://dblp.org/pid/402/5383.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html), Wankou Yang:

Improving underwater semantic segmentation with underwater image quality attention and muti-scale aggregation attention. [Pattern Anal. Appl.28(2)](https://dblp.org/db/journals/paa/paa28.html#journals/paa/ZuoJSY25): 80 (2025)
- ![](https://dblp.org/img/n.png)

\[j135\]
[Letian Wu](https://dblp.org/pid/322/6967.html), [Shen Zhang](https://dblp.org/pid/62/6204.html), [Chuankai Zhang](https://dblp.org/pid/244/6871.html), [Zhenyu Zhao](https://dblp.org/pid/26/7695.html), [Jiajun Liang](https://dblp.org/pid/184/6428.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang:

Enhancing knowledge distillation for semantic segmentation through text-assisted modular plugins. [Pattern Recognit.161](https://dblp.org/db/journals/pr/pr161.html#journals/pr/WuZZZLY25): 111329 (2025)
- ![](https://dblp.org/img/n.png)

\[j134\]
[Lingyu Xiao](https://dblp.org/pid/355/3184.html), [Jinhui Wu](https://dblp.org/pid/36/6077.html), [Junjie Hu](https://dblp.org/pid/123/0773-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ziyu Li](https://dblp.org/pid/177/3057.html), Wankou Yang:

Domain adaptive depth completion via spatial-error consistency. [Pattern Recognit.166](https://dblp.org/db/journals/pr/pr166.html#journals/pr/XiaoWHLY25): 111645 (2025)
- ![](https://dblp.org/img/n.png)

\[j133\]
[Yunfei Ma](https://dblp.org/pid/80/7673.html), [Zinan Cheng](https://dblp.org/pid/358/1002.html), [Letian Wu](https://dblp.org/pid/322/6967.html), [Lei Qi](https://dblp.org/pid/15/2464-1.html), Wankou Yang:

Global-local information sensitivity adjustment factor. [Pattern Recognit. Lett.192](https://dblp.org/db/journals/prl/prl192.html#journals/prl/MaCWQY25): 122-128 (2025)
- ![](https://dblp.org/img/n.png)

\[j132\]
[Qingxiao Zou](https://dblp.org/pid/400/4769.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Kong](https://dblp.org/pid/94/1836-1.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

REACTER: Perception-Informed Adaptive Tracker in Cluttered Environments. [IEEE Robotics Autom. Lett.10(9)](https://dblp.org/db/journals/ral/ral10.html#journals/ral/ZouKY25): 9422-9429 (2025)
- ![](https://dblp.org/img/n.png)

\[j131\]
[Xin Zuo](https://dblp.org/pid/15/2278.html), [Chenyu Qu](https://dblp.org/pid/421/1237.html), [Haibo Zhan](https://dblp.org/pid/413/3286.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

SFFR: Spatial-Frequency Feature Reconstruction for Multispectral Aerial Object Detection. [IEEE Trans. Geosci. Remote. Sens.63](https://dblp.org/db/journals/tgrs/tgrs63.html#journals/tgrs/ZuoQZSY25): 1-11 (2025)
- ![](https://dblp.org/img/n.png)

\[c86\]
[Wenxiao Cai](https://dblp.org/pid/348/4892.html), Wankou Yang:

Object-level Geometric Structure Preserving for Natural Image Stitching. [AAAI2025](https://dblp.org/db/conf/aaai/aaai2025.html#conf/aaai/CaiY25): 1926-1934
- ![](https://dblp.org/img/n.png)

\[c85\]
[Ming Dai](https://dblp.org/pid/61/6981.html), [Jian Li](https://dblp.org/pid/33/5448.html), [Jiedong Zhuang](https://dblp.org/pid/305/1138.html), [Xian Zhang](https://dblp.org/pid/56/5624.html), Wankou Yang:

Multi-task Visual Grounding with Coarse-to-Fine Consistency Constraints. [AAAI2025](https://dblp.org/db/conf/aaai/aaai2025.html#conf/aaai/DaiLZZY25): 2618-2626
- ![](https://dblp.org/img/n.png)

\[c84\]
[Lingyu Xiao](https://dblp.org/pid/355/3184.html), [Jiang-Jiang Liu](https://dblp.org/pid/18/2542-1.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Xiaofan Li](https://dblp.org/pid/50/3937.html), [Xiaoqing Ye](https://dblp.org/pid/177/0181.html), Wankou Yang, [Jingdong Wang](https://dblp.org/pid/49/3441.html):

Learning Multiple Probabilistic Decisions from Latent World Model in Autonomous Driving. [ICRA2025](https://dblp.org/db/conf/icra/icra2025.html#conf/icra/XiaoLYLYYW25): 1279-1285
- ![](https://dblp.org/img/n.png)

\[c83\]
[Wenxiao Cai](https://dblp.org/pid/348/4892.html), [Iaroslav Ponomarenko](https://dblp.org/pid/372/4375.html), [Jianhao Yuan](https://dblp.org/pid/336/7530.html), [Xiaoqi Li](https://dblp.org/pid/357/1937.html), Wankou Yang, [Hao Dong](https://dblp.org/pid/14/1525-3.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html):

SpatialBot: Precise Spatial Understanding with Vision Language Models. [ICRA2025](https://dblp.org/db/conf/icra/icra2025.html#conf/icra/CaiPYLYDZ25): 9490-9498
- ![](https://dblp.org/img/n.png)

\[c82\]
[Yuanze Xu](https://dblp.org/pid/400/0032.html), [Ming Dai](https://dblp.org/pid/61/6981.html), Wankou Yang:

Precise GPS-Denied UAV Self-positioning via Context-Enhanced Cross-View Geo-Localization. [PRCV (15)2025](https://dblp.org/db/conf/prcv/prcv2025-15.html#conf/prcv/XuDY25): 374-388
- ![](https://dblp.org/img/n.png)

\[i47\]
[Ming Dai](https://dblp.org/pid/61/6981.html), [Jian Li](https://dblp.org/pid/33/5448.html), [Jiedong Zhuang](https://dblp.org/pid/305/1138.html), [Xian Zhang](https://dblp.org/pid/56/5624.html), Wankou Yang:

Multi-task Visual Grounding with Coarse-to-Fine Consistency Constraints. [CoRRabs/2501.06710](https://dblp.org/db/journals/corr/corr2501.html#journals/corr/abs-2501-06710) (2025)
- ![](https://dblp.org/img/n.png)

\[i46\]
[Yuanze Xu](https://dblp.org/pid/400/0032.html), [Ming Dai](https://dblp.org/pid/61/6981.html), [Wenxiao Cai](https://dblp.org/pid/348/4892.html), Wankou Yang:

Precise GPS-Denied UAV Self-Positioning via Context-Enhanced Cross-View Geo-Localization. [CoRRabs/2502.11408](https://dblp.org/db/journals/corr/corr2502.html#journals/corr/abs-2502-11408) (2025)
- ![](https://dblp.org/img/n.png)

\[i45\]
[Xin Zuo](https://dblp.org/pid/15/2278.html), [Jiaran Jiang](https://dblp.org/pid/402/5383.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html), Wankou Yang:

Improving underwater semantic segmentation with underwater image quality attention and muti-scale aggregation attention. [CoRRabs/2503.23422](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-23422) (2025)
- ![](https://dblp.org/img/n.png)

\[i44\]
[Ze Feng](https://dblp.org/pid/12/5914.html), [Jiang-Jiang Liu](https://dblp.org/pid/18/2542-1.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Lingyu Xiao](https://dblp.org/pid/355/3184.html), [Xiaofan Li](https://dblp.org/pid/50/3937.html), Wankou Yang, [Jingdong Wang](https://dblp.org/pid/49/3441.html):

Vision Remember: Alleviating Visual Forgetting in Efficient MLLM with Vision Feature Resample. [CoRRabs/2506.03928](https://dblp.org/db/journals/corr/corr2506.html#journals/corr/abs-2506-03928) (2025)
- ![](https://dblp.org/img/n.png)

\[i43\]
[Ming Dai](https://dblp.org/pid/61/6981.html), [Wenxuan Cheng](https://dblp.org/pid/370/2615.html), [Jiang-jiang Liu](https://dblp.org/pid/409/9085.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Wenxiao Cai](https://dblp.org/pid/348/4892.html), [Yanpeng Sun](https://dblp.org/pid/143/0055.html), Wankou Yang:

DeRIS: Decoupling Perception and Cognition for Enhanced Referring Image Segmentation through Loopback Synergy. [CoRRabs/2507.01738](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-01738) (2025)
- ![](https://dblp.org/img/n.png)

\[i42\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), [Haibo Zhan](https://dblp.org/pid/413/3286.html), [Shaohua Dong](https://dblp.org/pid/188/4523.html), [Xin Zuo](https://dblp.org/pid/15/2278.html), Wankou Yang, [Haibin Ling](https://dblp.org/pid/93/3488.html):

Multispectral State-Space Feature Fusion: Bridging Shared and Cross-Parametric Interactions for Object Detection. [CoRRabs/2507.14643](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-14643) (2025)
- ![](https://dblp.org/img/n.png)

\[i41\]
[Ming Dai](https://dblp.org/pid/61/6981.html), [Wenxuan Cheng](https://dblp.org/pid/370/2615.html), [Jiedong Zhuang](https://dblp.org/pid/305/1138.html), [Jiang-jiang Liu](https://dblp.org/pid/409/9085.html), [Hongshen Zhao](https://dblp.org/pid/373/4477.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), Wankou Yang:

PropVG: End-to-End Proposal-Driven Visual Grounding with Multi-Granularity Discrimination. [CoRRabs/2509.04833](https://dblp.org/db/journals/corr/corr2509.html#journals/corr/abs-2509-04833) (2025)
- ![](https://dblp.org/img/n.png)

\[i40\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), [Haibo Zhan](https://dblp.org/pid/413/3286.html), [Xin Zuo](https://dblp.org/pid/15/2278.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Xiaohui Yuan](https://dblp.org/pid/61/623-1.html), [Jun Li](https://dblp.org/pid/116/1011-33.html), Wankou Yang:

IRDFusion: Iterative Relation-Map Difference guided Feature Fusion for Multispectral Object Detection. [CoRRabs/2509.09085](https://dblp.org/db/journals/corr/corr2509.html#journals/corr/abs-2509-09085) (2025)
- ![](https://dblp.org/img/n.png)

\[i39\]
[Ming Dai](https://dblp.org/pid/61/6981.html), [Wenxuan Cheng](https://dblp.org/pid/370/2615.html), [Jiang-jiang Liu](https://dblp.org/pid/409/9085.html), [Lingfeng Yang](https://dblp.org/pid/45/7593.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), Wankou Yang, [Jingdong Wang](https://dblp.org/pid/49/3441.html):

Improving Generalized Visual Grounding with Instance-aware Joint Learning. [CoRRabs/2509.13747](https://dblp.org/db/journals/corr/corr2509.html#journals/corr/abs-2509-13747) (2025)
- ![](https://dblp.org/img/n.png)

\[i38\]
[Ming Dai](https://dblp.org/pid/61/6981.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Boqiang Duan](https://dblp.org/pid/309/8582.html), Wankou Yang, [Jingdong Wang](https://dblp.org/pid/49/3441.html):

MomentSeg: Moment-Centric Sampling for Enhanced Video Pixel Understanding. [CoRRabs/2510.09274](https://dblp.org/db/journals/corr/corr2510.html#journals/corr/abs-2510-09274) (2025)
- ![](https://dblp.org/img/n.png)

\[i37\]
[Xin Zuo](https://dblp.org/pid/15/2278.html), [Yuchen Qu](https://dblp.org/pid/422/1178.html), [Haibo Zhan](https://dblp.org/pid/413/3286.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html), Wankou Yang:

SFFR: Spatial-Frequency Feature Reconstruction for Multispectral Aerial Object Detection. [CoRRabs/2511.06298](https://dblp.org/db/journals/corr/corr2511.html#journals/corr/abs-2511-06298) (2025)
- ![](https://dblp.org/img/n.png)

\[i36\]
[Ze Feng](https://dblp.org/pid/12/5914.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Boqiang Duan](https://dblp.org/pid/309/8582.html), Wankou Yang, [Jingdong Wang](https://dblp.org/pid/49/3441.html):

EM-KD: Distilling Efficient Multimodal Large Language Model with Unbalanced Vision Tokens. [CoRRabs/2511.21106](https://dblp.org/db/journals/corr/corr2511.html#journals/corr/abs-2511-21106) (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j130\]
[Xin Zuo](https://dblp.org/pid/15/2278.html), [Chenhui Qi](https://dblp.org/pid/384/4642.html), [Yifei Chen](https://dblp.org/pid/75/5017.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Heng Fan](https://dblp.org/pid/20/10120-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Learnable Cross-Scale Sparse Attention Guided Feature Fusion for UAV Object Detection. [IEEE Access12](https://dblp.org/db/journals/access/access12.html#journals/access/ZuoQCSFY24): 114212-114226 (2024)
- ![](https://dblp.org/img/n.png)

\[j129\]
[Suyi Li](https://dblp.org/pid/98/7732-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chenyi Jiang](https://dblp.org/pid/132/7866.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiaolin Ye](https://dblp.org/pid/44/7694.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shidong Wang](https://dblp.org/pid/82/8629.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Haofeng Zhang](https://dblp.org/pid/17/4297.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Fusing spatial and frequency features for compositional zero-shot image classification. [Expert Syst. Appl.258](https://dblp.org/db/journals/eswa/eswa258.html#journals/eswa/LiJYWYZ24): 125230 (2024)
- ![](https://dblp.org/img/n.png)

\[j128\]
[Dexin Ren](https://dblp.org/pid/214/2519.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shidong Wang](https://dblp.org/pid/82/8629.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zheng Zhang](https://dblp.org/pid/181/2621-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Mingwu Ren](https://dblp.org/pid/84/5438.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haofeng Zhang](https://dblp.org/pid/17/4297.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Unsupervised cross domain semantic segmentation with mutual refinement and information distillation. [Neurocomputing586](https://dblp.org/db/journals/ijon/ijon586.html#journals/ijon/RenWZYRZ24): 127641 (2024)
- ![](https://dblp.org/img/n.png)

\[j127\]
[Jiang Zhai](https://dblp.org/pid/291/9340.html), [Zinan Cheng](https://dblp.org/pid/358/1002.html), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), [Dejun Zhu](https://dblp.org/pid/64/9048.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Efficient object tracking on edge devices with MobileTrack. [J. Vis. Commun. Image Represent.100](https://dblp.org/db/journals/jvcir/jvcir100.html#journals/jvcir/ZhaiCZZY24): 104126 (2024)
- ![](https://dblp.org/img/n.png)

\[j126\]
[Siyao Duan](https://dblp.org/pid/331/7006.html), [Ting Wang](https://dblp.org/pid/12/2633.html), [Tao Li](https://dblp.org/pid/75/4601.html), Wankou Yang:

M-YOLOv8s: An improved small target detection algorithm for UAV aerial photography. [J. Vis. Commun. Image Represent.104](https://dblp.org/db/journals/jvcir/jvcir104.html#journals/jvcir/DuanWLY24): 104289 (2024)
- ![](https://dblp.org/img/n.png)

\[j125\]
[Yihao Xu](https://dblp.org/pid/254/1616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ming Dai](https://dblp.org/pid/61/6981.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dejun Zhu](https://dblp.org/pid/64/9048.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Adaptive Angle Module and Radian Regression Method for Rotated Object Detection. [IEEE Geosci. Remote. Sens. Lett.21](https://dblp.org/db/journals/lgrs/lgrs21.html#journals/lgrs/XuDZY24): 1-5 (2024)
- ![](https://dblp.org/img/n.png)

\[j124\]
[Fei Xie](https://dblp.org/pid/51/1316.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Chunyu Wang](https://dblp.org/pid/63/7235-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Chu](https://dblp.org/pid/168/2875.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yue Cao](https://dblp.org/pid/74/5570-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chao Ma](https://dblp.org/pid/79/1552-4.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenjun Zeng](https://dblp.org/pid/57/145.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Correlation-Embedded Transformer Tracking: A Single-Branch Framework. [IEEE Trans. Pattern Anal. Mach. Intell.46(12)](https://dblp.org/db/journals/pami/pami46.html#journals/pami/XieYWCCMZ24): 10681-10696 (2024)
- ![](https://dblp.org/img/n.png)

\[j123\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yifei Chen](https://dblp.org/pid/75/5017.html), [Yue Liu](https://dblp.org/pid/74/1932.html), [Xin Zuo](https://dblp.org/pid/15/2278.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang:

ICAFusion: Iterative cross-attention guided feature fusion for multispectral object detection. [Pattern Recognit.145](https://dblp.org/db/journals/pr/pr145.html#journals/pr/ShenCLZFY24): 109913 (2024)
- ![](https://dblp.org/img/n.png)

\[j122\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Teng Guo](https://dblp.org/pid/94/11139-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Zuo](https://dblp.org/pid/15/2278.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang:

SSPNet: Scale and spatial priors guided generalizable and interpretable pedestrian attribute recognition. [Pattern Recognit.148](https://dblp.org/db/journals/pr/pr148.html#journals/pr/ShenGZFY24): 110194 (2024)
- ![](https://dblp.org/img/n.png)

\[j121\]
[Xian Zhang](https://dblp.org/pid/56/5624.html), [Zhibin Quan](https://dblp.org/pid/141/2189.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Li](https://dblp.org/pid/72/872-24.html), [Dejun Zhu](https://dblp.org/pid/64/9048.html), Wankou Yang:

SED: Searching Enhanced Decoder with switchable skip connection for semantic segmentation. [Pattern Recognit.149](https://dblp.org/db/journals/pr/pr149.html#journals/pr/ZhangQLZY24): 110196 (2024)
- ![](https://dblp.org/img/n.png)

\[j120\]
[Yihao Xu](https://dblp.org/pid/254/1616.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ming Dai](https://dblp.org/pid/61/6981.html), Wankou Yang:

PARDet: Dynamic point set alignment for rotated object detection. [Pattern Recognit.153](https://dblp.org/db/journals/pr/pr153.html#journals/pr/XuSDY24): 110534 (2024)
- ![](https://dblp.org/img/n.png)

\[j119\]
[Wenkang Zhang](https://dblp.org/pid/340/0966.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Jiang Zhai](https://dblp.org/pid/291/9340.html), Wankou Yang:

CRTrack: Learning Correlation-Refine network for visual object tracking. [Pattern Recognit.154](https://dblp.org/db/journals/pr/pr154.html#journals/pr/ZhangXXZY24): 110582 (2024)
- ![](https://dblp.org/img/n.png)

\[j118\]
[Zhibin Quan](https://dblp.org/pid/141/2189.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Man Vong](https://dblp.org/pid/68/5768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weili Zeng](https://dblp.org/pid/86/11483.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

The MorPhEMe Machine: An Addressable Neural Memory for Learning Knowledge-Regularized Deep Contextualized Chinese Embedding. [IEEE ACM Trans. Audio Speech Lang. Process.32](https://dblp.org/db/journals/taslp/taslp32.html#journals/taslp/QuanVZY24): 1673-1686 (2024)
- ![](https://dblp.org/img/n.png)

\[j117\]
[Hanjin Zhang](https://dblp.org/pid/214/5921.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bin Li](https://dblp.org/pid/89/6764-85.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shun-Feng Su](https://dblp.org/pid/42/598.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Liping Xie](https://dblp.org/pid/91/7400.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Novel Hybrid Transformer-Based Framework for Solar Irradiance Forecasting Under Incomplete Data Scenarios. [IEEE Trans. Ind. Informatics20(6)](https://dblp.org/db/journals/tii/tii20.html#journals/tii/ZhangLSYX24): 8605-8615 (2024)
- ![](https://dblp.org/img/n.png)

\[j116\]
[Ming Dai](https://dblp.org/pid/61/6981.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Enhui Zheng](https://dblp.org/pid/138/8144.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Qi](https://dblp.org/pid/15/2464-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiedong Zhuang](https://dblp.org/pid/305/1138.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Vision-Based UAV Self-Positioning in Low-Altitude Urban Environments. [IEEE Trans. Image Process.33](https://dblp.org/db/journals/tip/tip33.html#journals/tip/DaiZFQZY24): 493-508 (2024)
- ![](https://dblp.org/img/n.png)

\[j115\]
[Lineng Chen](https://dblp.org/pid/230/6597.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Kong](https://dblp.org/pid/94/1836-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huan Wang](https://dblp.org/pid/70/6155-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Lou](https://dblp.org/pid/54/9756.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fenglei Xu](https://dblp.org/pid/230/6532.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mingwu Ren](https://dblp.org/pid/84/5438.html)![](https://dblp.org/img/orcid-mark.12x12.png):

HVP-Net: A Hybrid Voxel- and Point-Wise Network for Place Recognition. [IEEE Trans. Intell. Veh.9(1)](https://dblp.org/db/journals/tiv/tiv9.html#journals/tiv/ChenKWYLXR24): 395-406 (2024)
- ![](https://dblp.org/img/n.png)

\[j114\]
[Ziyu Li](https://dblp.org/pid/177/3057.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuncong Yao](https://dblp.org/pid/17/5361.html), [Zhibin Quan](https://dblp.org/pid/141/2189.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Qi](https://dblp.org/pid/15/2464-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Adaptation via Proxy: Building Instance-Aware Proxy for Unsupervised Domain Adaptive 3D Object Detection. [IEEE Trans. Intell. Veh.9(2)](https://dblp.org/db/journals/tiv/tiv9.html#journals/tiv/LiYQQFY24): 3478-3492 (2024)
- ![](https://dblp.org/img/n.png)

\[j113\]
Wankou Yang, [Jiren Mai](https://dblp.org/pid/342/1505.html), [Fei Zhang](https://dblp.org/pid/16/5105.html), [Tongliang Liu](https://dblp.org/pid/150/6667.html), [Bo Han](https://dblp.org/pid/241/0472-3.html):

Exploit CAM by itself: Complementary Learning System for Weakly Supervised Semantic Segmentation. [Trans. Mach. Learn. Res.2024](https://dblp.org/db/journals/tmlr/tmlr2024.html#journals/tmlr/YangMZL024) (2024)
- ![](https://dblp.org/img/n.png)

\[j112\]
[Haoran Wang](https://dblp.org/pid/28/3021-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yajie Wang](https://dblp.org/pid/10/821.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Baosheng Yu](https://dblp.org/pid/178/8725.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yibing Zhan](https://dblp.org/pid/142/8486.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chunfeng Yuan](https://dblp.org/pid/47/2506.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Attentional Composition Networks for Long-Tailed Human Action Recognition. [ACM Trans. Multim. Comput. Commun. Appl.20(1)](https://dblp.org/db/journals/tomccap/tomccap20.html#journals/tomccap/WangWYZYY24): 8:1-8:18 (2024)
- ![](https://dblp.org/img/n.png)

\[c81\]
[Yixin Xu](https://dblp.org/pid/04/5753.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), [Jinhui Wu](https://dblp.org/pid/36/6077.html), [Zinan Cheng](https://dblp.org/pid/358/1002.html), Wankou Yang:

Efficient Transformer-Based Visual Tracking for Edge Computing Devices. [ISAIR (2)2024](https://dblp.org/db/conf/isair/isair2024-2.html#conf/isair/XuXZWCY24): 223-232
- ![](https://dblp.org/img/n.png)

\[c80\]
[Chenghao Xu](https://dblp.org/pid/254/6051.html), [Qingxiao Zou](https://dblp.org/pid/400/4769.html), Wankou Yang:

PD-SLAM: A Visual SLAM for Dynamic Environments. [ISAIR (1)2024](https://dblp.org/db/conf/isair/isair2024-1.html#conf/isair/XuZY24): 250-257
- ![](https://dblp.org/img/n.png)

\[c79\]
[Ming Dai](https://dblp.org/pid/61/6981.html), [Lingfeng Yang](https://dblp.org/pid/45/7593.html), [Yihao Xu](https://dblp.org/pid/254/1616.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), Wankou Yang:

SimVG: A Simple Framework for Visual Grounding with Decoupled Multi-modal Fusion. [NeurIPS2024](https://dblp.org/db/conf/nips/neurips2024.html#conf/nips/DaiYX0Y24)
- ![](https://dblp.org/img/n.png)

\[i35\]
[Fei Xie](https://dblp.org/pid/51/1316.html), Wankou Yang, [Chunyu Wang](https://dblp.org/pid/63/7235-1.html), [Lei Chu](https://dblp.org/pid/168/2875.html), [Yue Cao](https://dblp.org/pid/74/5570-1.html), [Chao Ma](https://dblp.org/pid/79/1552-4.html), [Wenjun Zeng](https://dblp.org/pid/57/145.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Correlation-Embedded Transformer Tracking: A Single-Branch Framework. [CoRRabs/2401.12743](https://dblp.org/db/journals/corr/corr2401.html#journals/corr/abs-2401-12743) (2024)
- ![](https://dblp.org/img/n.png)

\[i34\]
[Wenxiao Cai](https://dblp.org/pid/348/4892.html), Wankou Yang:

Object-level Geometric Structure Preserving for Natural Image Stitching. [CoRRabs/2402.12677](https://dblp.org/db/journals/corr/corr2402.html#journals/corr/abs-2402-12677) (2024)
- ![](https://dblp.org/img/n.png)

\[i33\]
[Wenxiao Cai](https://dblp.org/pid/348/4892.html), [Yaroslav Ponomarenko](https://dblp.org/pid/380/2248.html), [Jianhao Yuan](https://dblp.org/pid/336/7530.html), [Xiaoqi Li](https://dblp.org/pid/357/1937.html), Wankou Yang, [Hao Dong](https://dblp.org/pid/14/1525-3.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html):

SpatialBot: Precise Spatial Understanding with Vision Language Models. [CoRRabs/2406.13642](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-13642) (2024)
- ![](https://dblp.org/img/n.png)

\[i32\]
[Lingyu Xiao](https://dblp.org/pid/355/3184.html), [Jiang-Jiang Liu](https://dblp.org/pid/18/2542-1.html), [Xiaoqing Ye](https://dblp.org/pid/177/0181.html), Wankou Yang, [Jingdong Wang](https://dblp.org/pid/49/3441.html):

EasyChauffeur: A Baseline Advancing Simplicity and Efficiency on Waymax. [CoRRabs/2408.16375](https://dblp.org/db/journals/corr/corr2408.html#journals/corr/abs-2408-16375) (2024)
- ![](https://dblp.org/img/n.png)

\[i31\]
[Lingyu Xiao](https://dblp.org/pid/355/3184.html), [Jiang-Jiang Liu](https://dblp.org/pid/18/2542-1.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Xiaofan Li](https://dblp.org/pid/50/3937.html), [Xiaoqing Ye](https://dblp.org/pid/177/0181.html), Wankou Yang, [Jingdong Wang](https://dblp.org/pid/49/3441.html):

Learning Multiple Probabilistic Decisions from Latent World Model in Autonomous Driving. [CoRRabs/2409.15730](https://dblp.org/db/journals/corr/corr2409.html#journals/corr/abs-2409-15730) (2024)
- ![](https://dblp.org/img/n.png)

\[i30\]
[Ming Dai](https://dblp.org/pid/61/6981.html), [Lingfeng Yang](https://dblp.org/pid/45/7593.html), [Yihao Xu](https://dblp.org/pid/254/1616.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), Wankou Yang:

SimVG: A Simple Framework for Visual Grounding with Decoupled Multi-modal Fusion. [CoRRabs/2409.17531](https://dblp.org/db/journals/corr/corr2409.html#journals/corr/abs-2409-17531) (2024)
- ![](https://dblp.org/img/n.png)

\[i29\]
[Wenxiao Cai](https://dblp.org/pid/348/4892.html), [Dongting Hu](https://dblp.org/pid/159/6788.html), [Ruoyan Yin](https://dblp.org/pid/395/6967.html), [Jiankang Deng](https://dblp.org/pid/156/7808.html), [Huan Fu](https://dblp.org/pid/139/8082.html), Wankou Yang, [Mingming Gong](https://dblp.org/pid/98/8479.html):

Uncertainty Quantification in Stereo Matching. [CoRRabs/2412.18703](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-18703) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j111\]
[Mu Nie](https://dblp.org/pid/210/3225.html), [Zhibin Quan](https://dblp.org/pid/141/2189.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weiping Ding](https://dblp.org/pid/133/0292-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang:

Enhancing motion visual cues for self-supervised video representation learning. [Eng. Appl. Artif. Intell.123(Part A)](https://dblp.org/db/journals/eaai/eaai123.html#journals/eaai/NieQ0Y23): 106203 (2023)
- ![](https://dblp.org/img/n.png)

\[j110\]
[Lei Shi](https://dblp.org/pid/29/563.html), [Yimin Zhou](https://dblp.org/pid/63/2223-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Juan Wang](https://dblp.org/pid/74/3634-17.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zuli Wang](https://dblp.org/pid/187/9462.html), [Ding Chen](https://dblp.org/pid/78/3806.html), [Haifeng Zhao](https://dblp.org/pid/17/5245.html), Wankou Yang, [Edward Szczerbicki](https://dblp.org/pid/25/345.html):

Compact global association based adaptive routing framework for personnel behavior understanding. [Future Gener. Comput. Syst.141](https://dblp.org/db/journals/fgcs/fgcs141.html#journals/fgcs/ShiZWWCZYS23): 514-525 (2023)
- ![](https://dblp.org/img/n.png)

\[j109\]
[Xin Zuo](https://dblp.org/pid/15/2278.html), [Zhi Wang](https://dblp.org/pid/95/6543.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang:

Improving multispectral pedestrian detection with scale-aware permutation attention and adjacent feature aggregation. [IET Comput. Vis.17(7)](https://dblp.org/db/journals/iet-cvi/iet-cvi17.html#journals/iet-cvi/ZuoWSY23): 726-738 (2023)
- ![](https://dblp.org/img/n.png)

\[j108\]
[Qiang Wang](https://dblp.org/pid/64/5630-23.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), Wankou Yang, [Chunyan Xu](https://dblp.org/pid/70/8453.html), [Zhen Cui](https://dblp.org/pid/59/8491-1.html):

Prototype-guided Instance matching for multiple pedestrian tracking. [Neurocomputing538](https://dblp.org/db/journals/ijon/ijon538.html#journals/ijon/WangZYXC23): 126207 (2023)
- ![](https://dblp.org/img/n.png)

\[j107\]
[Junlong Tong](https://dblp.org/pid/332/1196.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liping Xie](https://dblp.org/pid/91/7400.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Kanjian Zhang](https://dblp.org/pid/93/1517.html), [Junsheng Zhao](https://dblp.org/pid/132/1767.html):

Enhancing time series forecasting: A hierarchical transformer with probabilistic decomposition representation. [Inf. Sci.647](https://dblp.org/db/journals/isci/isci647.html#journals/isci/TongXYZZ23): 119410 (2023)
- ![](https://dblp.org/img/n.png)

\[j106\]
[Qiang Wang](https://dblp.org/pid/64/5630-23.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ziyu Li](https://dblp.org/pid/177/3057.html), [Dejun Zhu](https://dblp.org/pid/64/9048.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

LiDAR-only 3D object detection based on spatial context. [J. Vis. Commun. Image Represent.93](https://dblp.org/db/journals/jvcir/jvcir93.html#journals/jvcir/WangLZY23): 103805 (2023)
- ![](https://dblp.org/img/n.png)

\[j105\]
[Wenxiao Cai](https://dblp.org/pid/348/4892.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Songlin Du](https://dblp.org/pid/154/7687.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

UAV image stitching by estimating orthograph with RGB cameras. [J. Vis. Commun. Image Represent.94](https://dblp.org/db/journals/jvcir/jvcir94.html#journals/jvcir/CaiDY23): 103835 (2023)
- ![](https://dblp.org/img/n.png)

\[j104\]
[Letian Wu](https://dblp.org/pid/322/6967.html), [Xian Zhang](https://dblp.org/pid/56/5624.html), [Dejun Zhu](https://dblp.org/pid/64/9048.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

BFANet: Effective segmentation network for low altitude high-resolution urban scene image. [J. Vis. Commun. Image Represent.94](https://dblp.org/db/journals/jvcir/jvcir94.html#journals/jvcir/WuZZY23): 103847 (2023)
- ![](https://dblp.org/img/n.png)

\[j103\]
[Mu Nie](https://dblp.org/pid/210/3225.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Zhenhua Wang](https://dblp.org/pid/33/4679.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Huimin Lu](https://dblp.org/pid/64/2633-1.html), Wankou Yang:

Multi-receptive field spatiotemporal network for action recognition. [Int. J. Mach. Learn. Cybern.14(7)](https://dblp.org/db/journals/mlc/mlc14.html#journals/mlc/NieYWZLY23): 2439-2453 (2023)
- ![](https://dblp.org/img/n.png)

\[j102\]
[Guangtao Wang](https://dblp.org/pid/26/11029.html), [Jun Li](https://dblp.org/pid/116/1011-33.html), [Zhijian Wu](https://dblp.org/pid/23/3616.html), [Jianhua Xu](https://dblp.org/pid/57/6846.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html), Wankou Yang:

EfficientFace: an efficient deep network with feature enhancement for accurate face detection. [Multim. Syst.29(5)](https://dblp.org/db/journals/mms/mms29.html#journals/mms/WangLWXSY23): 2825-2839 (2023)
- ![](https://dblp.org/img/n.png)

\[j101\]
[Siyu Wang](https://dblp.org/pid/168/9309.html), [Changhui Hu](https://dblp.org/pid/31/7616-1.html), [Weilin Yi](https://dblp.org/pid/253/6460.html), [Ziyun Cai](https://dblp.org/pid/179/6081.html), [Mingliang Zhai](https://dblp.org/pid/221/3748.html), Wankou Yang:

Flow Learning Based Dual Networks for Low-Light Image Enhancement. [Neural Process. Lett.55(6)](https://dblp.org/db/journals/npl/npl55.html#journals/npl/WangHYCZY23): 8115-8130 (2023)
- ![](https://dblp.org/img/n.png)

\[j100\]
[Xian Zhang](https://dblp.org/pid/56/5624.html), [Qiang Li](https://dblp.org/pid/72/872-24.html), [Zhibin Quan](https://dblp.org/pid/141/2189.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang:

Pyramid Geometric Consistency Learning For Semantic Segmentation. [Pattern Recognit.133](https://dblp.org/db/journals/pr/pr133.html#journals/pr/ZhangLQY23): 109020 (2023)
- ![](https://dblp.org/img/n.png)

\[j99\]
[Sen Yang](https://dblp.org/pid/90/4655.html), [Ze Feng](https://dblp.org/pid/12/5914.html), [Zhicheng Wang](https://dblp.org/pid/78/1664-1.html), [Yanjie Li](https://dblp.org/pid/70/4538.html), [Shoukui Zhang](https://dblp.org/pid/289/7121.html), [Zhibin Quan](https://dblp.org/pid/141/2189.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shutao Xia](https://dblp.org/pid/34/3173.html), Wankou Yang:

Detecting and grouping keypoints for multi-person pose estimation using instance-aware attention. [Pattern Recognit.136](https://dblp.org/db/journals/pr/pr136.html#journals/pr/YangFWLZQXY23): 109232 (2023)
- ![](https://dblp.org/img/n.png)

\[j98\]
[Lei Ju](https://dblp.org/pid/97/3791-5.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Muhammad Awais Rana](https://dblp.org/pid/347/3707.html), Wankou Yang, [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Keep an eye on faces: Robust face detection with heatmap-Assisted spatial attention and scale-Aware layer attention. [Pattern Recognit.140](https://dblp.org/db/journals/pr/pr140.html#journals/pr/JuKRYF23): 109553 (2023)
- ![](https://dblp.org/img/n.png)

\[j97\]
[Lineng Chen](https://dblp.org/pid/230/6597.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huan Wang](https://dblp.org/pid/70/6155-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Kong](https://dblp.org/pid/94/1836-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Mingwu Ren](https://dblp.org/pid/84/5438.html)![](https://dblp.org/img/orcid-mark.12x12.png):

PTC-Net: Point-Wise Transformer With Sparse Convolution Network for Place Recognition. [IEEE Robotics Autom. Lett.8(6)](https://dblp.org/db/journals/ral/ral8.html#journals/ral/ChenWKYR23): 3414-3421 (2023)
- ![](https://dblp.org/img/n.png)

\[j96\]
[Chang-Hui Hu](https://dblp.org/pid/31/7616-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yu Liu](https://dblp.org/pid/97/2274.html), [Lin-Tao Xu](https://dblp.org/pid/354/1298.html), [Xiao-Yuan Jing](https://dblp.org/pid/59/1365.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaobo Lu](https://dblp.org/pid/93/8545.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Pan Liu](https://dblp.org/pid/68/5616-13.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Joint Image-to-Image Translation for Traffic Monitoring Driver Face Image Enhancement. [IEEE Trans. Intell. Transp. Syst.24(8)](https://dblp.org/db/journals/tits/tits24.html#journals/tits/HuLXJLYL23): 7961-7973 (2023)
- ![](https://dblp.org/img/n.png)

\[c78\]
[Mu Nie](https://dblp.org/pid/210/3225.html), [Wen Jiang](https://dblp.org/pid/37/6235.html), Wankou Yang, [Senling Wang](https://dblp.org/pid/123/8631.html), [Xiaoqing Wen](https://dblp.org/pid/38/3836.html), [Tianming Ni](https://dblp.org/pid/193/1937.html):

Enhancing Defect Diagnosis and Localization in Wafer Map Testing Through Weakly Supervised Learning. [ATS2023](https://dblp.org/db/conf/ats/ats2023.html#conf/ats/NieJYWWN23): 1-6
- ![](https://dblp.org/img/n.png)

\[c77\]
[Ziyu Li](https://dblp.org/pid/177/3057.html), [Jingming Guo](https://dblp.org/pid/174/3127.html), [Tongtong Cao](https://dblp.org/pid/229/5950.html), [Bingbing Liu](https://dblp.org/pid/34/3868.html), Wankou Yang:

GPA-3D: Geometry-aware Prototype Alignment for Unsupervised Domain Adaptive 3D Object Detection from Point Clouds. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/LiGCLY23): 6371-6380
- ![](https://dblp.org/img/n.png)

\[c76\]
[Lingyu Xiao](https://dblp.org/pid/355/3184.html), [Xiang Li](https://dblp.org/pid/40/1491-41.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sen Yang](https://dblp.org/pid/90/4655.html), Wankou Yang:

ADNet: Lane Shape Prediction via Anchor Decomposition. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/XiaoLYY23): 6381-6390
- ![](https://dblp.org/img/n.png)

\[c75\]
[Hao Wang](https://dblp.org/pid/181/2812-144.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaolou Sun](https://dblp.org/pid/329/0397.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wang](https://dblp.org/pid/64/5630-23.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning Efficient Transformer Representation for Siamese Tracker to UAV. [ICIAI2023](https://dblp.org/db/conf/iciai/iciai2023.html#conf/iciai/WangSY023): 135-140
- ![](https://dblp.org/img/n.png)

\[c74\]
[Ziwei Chen](https://dblp.org/pid/219/9605.html), [Qiang Li](https://dblp.org/pid/72/872-24.html), [Xiaofeng Wang](https://dblp.org/pid/99/2479.html), Wankou Yang:

LiftedCL: Lifting Contrastive Learning for Human-Centric Perception. [ICLR2023](https://dblp.org/db/conf/iclr/iclr2023.html#conf/iclr/ChenLWY23)
- ![](https://dblp.org/img/n.png)

\[c73\]
[Sen Yang](https://dblp.org/pid/90/4655.html), [Wen Heng](https://dblp.org/pid/201/7460.html), [Gang Liu](https://dblp.org/pid/37/2109.html), [Guozhong Luo](https://dblp.org/pid/228/8540.html), Wankou Yang, [Gang Yu](https://dblp.org/pid/75/1683-2.html):

Capturing the Motion of Every Joint: 3D Human Pose and Shape Estimation with Independent Tokens. [ICLR2023](https://dblp.org/db/conf/iclr/iclr2023.html#conf/iclr/YangHLLYY23)
- ![](https://dblp.org/img/n.png)

\[c72\]
[Ke Jin](https://dblp.org/pid/94/2193.html), Wankou Yang:

CLIP for Lightweight Semantic Segmentation. [PRCV (10)2023](https://dblp.org/db/conf/prcv/prcv2023-10.html#conf/prcv/JinY23): 323-333
- ![](https://dblp.org/img/n.png)

\[i28\]
[Guangtao Wang](https://dblp.org/pid/26/11029.html), [Jun Li](https://dblp.org/pid/116/1011-33.html), [Zhijian Wu](https://dblp.org/pid/23/3616.html), [Jianhua Xu](https://dblp.org/pid/57/6846.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html), Wankou Yang:

EfficientFace: An Efficient Deep Network with Feature Enhancement for Accurate Face Detection. [CoRRabs/2302.11816](https://dblp.org/db/journals/corr/corr2302.html#journals/corr/abs-2302-11816) (2023)
- ![](https://dblp.org/img/n.png)

\[i27\]
[Sen Yang](https://dblp.org/pid/90/4655.html), [Wen Heng](https://dblp.org/pid/201/7460.html), [Gang Liu](https://dblp.org/pid/37/2109.html), [Guozhong Luo](https://dblp.org/pid/228/8540.html), Wankou Yang, [Gang Yu](https://dblp.org/pid/75/1683-2.html):

Capturing the motion of every joint: 3D human pose and shape estimation with independent tokens. [CoRRabs/2303.00298](https://dblp.org/db/journals/corr/corr2303.html#journals/corr/abs-2303-00298) (2023)
- ![](https://dblp.org/img/n.png)

\[i26\]
[Jiren Mai](https://dblp.org/pid/342/1505.html), [Fei Zhang](https://dblp.org/pid/16/5105.html), [Junjie Ye](https://dblp.org/pid/19/8588-2.html), [Marcus Kalander](https://dblp.org/pid/256/9291.html), [Xian Zhang](https://dblp.org/pid/56/5624.html), Wankou Yang, [Tongliang Liu](https://dblp.org/pid/150/6667.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bo Han](https://dblp.org/pid/241/0472-3.html):

Exploit CAM by itself: Complementary Learning System for Weakly Supervised Semantic Segmentation. [CoRRabs/2303.02449](https://dblp.org/db/journals/corr/corr2303.html#journals/corr/abs-2303-02449) (2023)
- ![](https://dblp.org/img/n.png)

\[i25\]
[Letian Wu](https://dblp.org/pid/322/6967.html), [Wenyao Zhang](https://dblp.org/pid/86/2144.html), [Tengping Jiang](https://dblp.org/pid/270/8012.html), Wankou Yang, [Xin Jin](https://dblp.org/pid/68/3340-14.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenjun Zeng](https://dblp.org/pid/57/145.html)![](https://dblp.org/img/orcid-mark.12x12.png):

\[CLS\] Token is All You Need for Zero-Shot Semantic Segmentation. [CoRRabs/2304.06212](https://dblp.org/db/journals/corr/corr2304.html#journals/corr/abs-2304-06212) (2023)
- ![](https://dblp.org/img/n.png)

\[i24\]
[Wenxiao Cai](https://dblp.org/pid/348/4892.html), [Ke Jin](https://dblp.org/pid/94/2193.html), [Jinyan Hou](https://dblp.org/pid/348/4547.html), [Cong Guo](https://dblp.org/pid/117/1754.html), [Letian Wu](https://dblp.org/pid/322/6967.html), Wankou Yang:

VDD: Varied Drone Dataset for Semantic Segmentation. [CoRRabs/2305.13608](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-13608) (2023)
- ![](https://dblp.org/img/n.png)

\[i23\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), [Yifei Chen](https://dblp.org/pid/75/5017.html), [Yue Liu](https://dblp.org/pid/74/1932.html), [Xin Zuo](https://dblp.org/pid/15/2278.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), Wankou Yang:

ICAFusion: Iterative Cross-Attention Guided Feature Fusion for Multispectral Object Detection. [CoRRabs/2308.07504](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-07504) (2023)
- ![](https://dblp.org/img/n.png)

\[i22\]
[Ziyu Li](https://dblp.org/pid/177/3057.html), [Jingming Guo](https://dblp.org/pid/174/3127.html), [Tongtong Cao](https://dblp.org/pid/229/5950.html), [Bingbing Liu](https://dblp.org/pid/34/3868.html), Wankou Yang:

GPA-3D: Geometry-aware Prototype Alignment for Unsupervised Domain Adaptive 3D Object Detection from Point Clouds. [CoRRabs/2308.08140](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-08140) (2023)
- ![](https://dblp.org/img/n.png)

\[i21\]
[Lingyu Xiao](https://dblp.org/pid/355/3184.html), [Xiang Li](https://dblp.org/pid/40/1491-41.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sen Yang](https://dblp.org/pid/90/4655.html), Wankou Yang:

ADNet: Lane Shape Prediction via Anchor Decomposition. [CoRRabs/2308.10481](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-10481) (2023)
- ![](https://dblp.org/img/n.png)

\[i20\]
[Ke Jin](https://dblp.org/pid/94/2193.html), Wankou Yang:

CLIP for Lightweight Semantic Segmentation. [CoRRabs/2310.07394](https://dblp.org/db/journals/corr/corr2310.html#journals/corr/abs-2310-07394) (2023)
- ![](https://dblp.org/img/n.png)

\[i19\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), [Teng Guo](https://dblp.org/pid/94/11139-3.html), [Xin Zuo](https://dblp.org/pid/15/2278.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), Wankou Yang:

SSPNet: Scale and Spatial Priors Guided Generalizable and Interpretable Pedestrian Attribute Recognition. [CoRRabs/2312.06049](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-06049) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j95\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yue Liu](https://dblp.org/pid/74/1932.html), [Yifei Chen](https://dblp.org/pid/75/5017.html), [Xin Zuo](https://dblp.org/pid/15/2278.html), [Jun Li](https://dblp.org/pid/116/1011-33.html), Wankou Yang:

Mask-guided explicit feature modulation for multispectral pedestrian detection. [Comput. Electr. Eng.103](https://dblp.org/db/journals/cee/cee103.html#journals/cee/ShenLCZLY22): 108385 (2022)
- ![](https://dblp.org/img/n.png)

\[j94\]
[Zhijian Wu](https://dblp.org/pid/23/3616.html), [Jun Li](https://dblp.org/pid/116/1011-33.html), [Jianhua Xu](https://dblp.org/pid/57/6846.html), Wankou Yang:

Subspace-based self-weighted multiview fusion for instance retrieval. [Inf. Sci.592](https://dblp.org/db/journals/isci/isci592.html#journals/isci/Wu0XY22): 261-276 (2022)
- ![](https://dblp.org/img/n.png)

\[j93\]
[Xiao Shen](https://dblp.org/pid/166/6158.html), [Haofeng Zhang](https://dblp.org/pid/17/4297.html), [Lunbo Li](https://dblp.org/pid/188/6062.html), Wankou Yang, [Li Liu](https://dblp.org/pid/33/4528-4.html):

Semi-supervised cross-modal hashing with multi-view graph representation. [Inf. Sci.604](https://dblp.org/db/journals/isci/isci604.html#journals/isci/ShenZLYL22): 45-60 (2022)
- ![](https://dblp.org/img/n.png)

\[j92\]
[Zhikang Fu](https://dblp.org/pid/169/4639.html), [Leibo Zheng](https://dblp.org/pid/239/7320.html), [Jun Li](https://dblp.org/pid/116/1011-33.html), [Guoqing Chen](https://dblp.org/pid/87/4902.html), [Tianbao Yu](https://dblp.org/pid/331/0776.html), [Tiansheng Deng](https://dblp.org/pid/391/3535.html), Wankou Yang:

DMvLNet: deep multiview learning network for blindly accessing image quality. [J. Electronic Imaging31(5)](https://dblp.org/db/journals/jei/jei31.html#journals/jei/FuZ0CYDY22) (2022)
- ![](https://dblp.org/img/n.png)

\[j91\]
[Wen Shi](https://dblp.org/pid/02/3628-7.html), [Yongming Huang](https://dblp.org/pid/385/3909-2.html), [Guobao Zhang](https://dblp.org/pid/25/2971.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang:

A data-driven degradation prognostics approach for rolling element bearings. [J. Intell. Fuzzy Syst.43(5)](https://dblp.org/db/journals/jifs/jifs43.html#journals/jifs/ShiHZY22): 6061-6076 (2022)
- ![](https://dblp.org/img/n.png)

\[j90\]
[Xiaolou Sun](https://dblp.org/pid/329/0397.html), [Qi Wang](https://dblp.org/pid/19/1924.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Zhibin Quan](https://dblp.org/pid/141/2189.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Wang](https://dblp.org/pid/35/7092.html), [Hao Wang](https://dblp.org/pid/181/2812-144.html), [Yuncong Yao](https://dblp.org/pid/17/5361.html), Wankou Yang, [Satoshi Suzuki](https://dblp.org/pid/30/181.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Siamese Transformer Network: Building an autonomous real-time target tracking system for UAV. [J. Syst. Archit.130](https://dblp.org/db/journals/jsa/jsa130.html#journals/jsa/SunWXQWWYYS22): 102675 (2022)
- ![](https://dblp.org/img/n.png)

\[j89\]
[Jingren Liu](https://dblp.org/pid/269/7845.html), [Liyong Fu](https://dblp.org/pid/155/9293.html), [Haofeng Zhang](https://dblp.org/pid/17/4297.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiaolin Ye](https://dblp.org/pid/44/7694.html), Wankou Yang, [Li Liu](https://dblp.org/pid/33/4528-4.html):

Learning discriminative and representative feature with cascade GAN for generalized zero-shot learning. [Knowl. Based Syst.236](https://dblp.org/db/journals/kbs/kbs236.html#journals/kbs/LiuFZYYL22): 107780 (2022)
- ![](https://dblp.org/img/n.png)

\[j88\]
[Qipeng Chen](https://dblp.org/pid/134/5036.html), [Haofeng Zhang](https://dblp.org/pid/17/4297.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiaolin Ye](https://dblp.org/pid/44/7694.html), [Zheng Zhang](https://dblp.org/pid/181/2621-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang:

Learning discriminative feature via a generic auxiliary distribution for unsupervised domain adaptation. [Int. J. Mach. Learn. Cybern.13(1)](https://dblp.org/db/journals/mlc/mlc13.html#journals/mlc/ChenZYZY22): 175-185 (2022)
- ![](https://dblp.org/img/n.png)

\[j87\]
[Sen Yang](https://dblp.org/pid/90/4655.html), Wankou Yang, [Zhen Cui](https://dblp.org/pid/59/8491-1.html):

Searching part-specific neural fabrics for human pose estimation. [Pattern Recognit.128](https://dblp.org/db/journals/pr/pr128.html#journals/pr/YangYC22): 108652 (2022)
- ![](https://dblp.org/img/n.png)

\[j86\]
[Ziyu Li](https://dblp.org/pid/177/3057.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuncong Yao](https://dblp.org/pid/17/5361.html), [Zhibin Quan](https://dblp.org/pid/141/2189.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jin Xie](https://dblp.org/pid/80/1949.html), Wankou Yang:

Spatial information enhancement network for 3D object detection from point cloud. [Pattern Recognit.128](https://dblp.org/db/journals/pr/pr128.html#journals/pr/LiYQXY22): 108684 (2022)
- ![](https://dblp.org/img/n.png)

\[j85\]
[Qiaolin Ye](https://dblp.org/pid/44/7694.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peng Huang](https://dblp.org/pid/29/1726.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhao Zhang](https://dblp.org/pid/87/6853-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuhui Zheng](https://dblp.org/pid/155/0258.html), [Liyong Fu](https://dblp.org/pid/155/9293.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Multiview Learning With Robust Double-Sided Twin SVM. [IEEE Trans. Cybern.52(12)](https://dblp.org/db/journals/tcyb/tcyb52.html#journals/tcyb/YeHZZFY22): 12745-12758 (2022)
- ![](https://dblp.org/img/n.png)

\[j84\]
[Liyong Fu](https://dblp.org/pid/155/9293.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zechao Li](https://dblp.org/pid/51/8693.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiaolin Ye](https://dblp.org/pid/44/7694.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hang Yin](https://dblp.org/pid/81/7626.html), [Qingwang Liu](https://dblp.org/pid/189/3601.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaobo Chen](https://dblp.org/pid/21/4778-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xijian Fan](https://dblp.org/pid/166/8478.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Guowei Yang](https://dblp.org/pid/43/3366-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning Robust Discriminant Subspace Based on Joint L₂, ₚ- and L₂, ₛ-Norm Distance Metrics. [IEEE Trans. Neural Networks Learn. Syst.33(1)](https://dblp.org/db/journals/tnn/tnn33.html#journals/tnn/FuLYYLCFYY22): 130-144 (2022)
- ![](https://dblp.org/img/n.png)

\[c71\]
[Fei Xie](https://dblp.org/pid/51/1316.html), [Chunyu Wang](https://dblp.org/pid/63/7235-1.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Yue Cao](https://dblp.org/pid/74/5570-1.html), Wankou Yang, [Wenjun Zeng](https://dblp.org/pid/57/145.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Correlation-Aware Deep Tracking. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/XieWWCYZ22): 8741-8750
- ![](https://dblp.org/img/n.png)

\[c70\]
[Yanjie Li](https://dblp.org/pid/70/4538.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Peidong Liu](https://dblp.org/pid/07/11190-3.html), [Shoukui Zhang](https://dblp.org/pid/289/7121.html), [Yunxiao Wang](https://dblp.org/pid/11/3450.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhicheng Wang](https://dblp.org/pid/78/1664-1.html), Wankou Yang, [Shu-Tao Xia](https://dblp.org/pid/34/3173.html):

SimCC: A Simple Coordinate Classification Perspective for Human Pose Estimation. [ECCV (6)2022](https://dblp.org/db/conf/eccv/eccv2022-6.html#conf/eccv/LiYLZWWYX22): 89-106
- ![](https://dblp.org/img/n.png)

\[c69\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Wenyan Yang](https://dblp.org/pid/119/2426.html), [Dingding Cai](https://dblp.org/pid/198/1127.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Kang Ben](https://dblp.org/pid/340/0959.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Hong Chang](https://dblp.org/pid/02/2689-1.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Jiaye Chen](https://dblp.org/pid/116/2901.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xilin Chen](https://dblp.org/pid/c/XilinChen.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Xiuyi Chen](https://dblp.org/pid/218/7190.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu-Hsi Chen](https://dblp.org/pid/127/3933.html), [Zhixing Chen](https://dblp.org/pid/62/3074.html), [Yangming Cheng](https://dblp.org/pid/340/1285.html), [Angelo Ciaramella](https://dblp.org/pid/37/6845.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Benjamin Dzubur](https://dblp.org/pid/340/1520.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Debajyoti Dhar](https://dblp.org/pid/128/3182.html), [Shangzhe Di](https://dblp.org/pid/304/1344.html), [Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shang Gao](https://dblp.org/pid/28/435-12.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Eric Granger](https://dblp.org/pid/86/2306.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Q. H. Gu](https://dblp.org/pid/340/1209.html), [Himanshu Gupta](https://dblp.org/pid/330/0760-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianfeng He](https://dblp.org/pid/93/8352.html), [Keji He](https://dblp.org/pid/319/4518.html), [Yan Huang](https://dblp.org/pid/75/6434-8.html), [Deepak Jangid](https://dblp.org/pid/340/1460.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Ze Kang](https://dblp.org/pid/340/1063.html), [Madhu Kiran](https://dblp.org/pid/39/10281.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Simiao Lai](https://dblp.org/pid/282/1954.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Dongwook Lee](https://dblp.org/pid/25/6543.html), [Hyunjeong Lee](https://dblp.org/pid/00/3423.html), [Seohyung Lee](https://dblp.org/pid/210/4662.html), [Hui Li](https://dblp.org/pid/66/3387-37.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ming Li](https://dblp.org/pid/l/MingLi10.html), [Wangkai Li](https://dblp.org/pid/340/1456.html), [Xi Li](https://dblp.org/pid/46/2311-1.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Xiao Li](https://dblp.org/pid/66/2069.html), [Zhe Li](https://dblp.org/pid/11/751-8.html), [Liting Lin](https://dblp.org/pid/227/2204.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Si Liu](https://dblp.org/pid/60/7642.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html), [Bingpeng Ma](https://dblp.org/pid/62/1822.html), [Chao Ma](https://dblp.org/pid/79/1552-4.html), [Jie Ma](https://dblp.org/pid/62/5110.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yinchao Ma](https://dblp.org/pid/189/1326.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Payman Moallem](https://dblp.org/pid/63/5378.html), [Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html), [Siyang Pan](https://dblp.org/pid/250/5753.html), [ChangBeom Park](https://dblp.org/pid/340/0926.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Litu Rout](https://dblp.org/pid/206/6445.html), [Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Tianhui Song](https://dblp.org/pid/181/8738.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Chao Sun](https://dblp.org/pid/54/3957.html), [Jingna Sun](https://dblp.org/pid/255/0702.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Om Prakash Verma](https://dblp.org/pid/61/8145.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Qiang Wang](https://dblp.org/pid/64/5630-23.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Jinlin Wu](https://dblp.org/pid/123/7200.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Xu](https://dblp.org/pid/32/1213-17.html), [Yong Xu](https://dblp.org/pid/07/4630-7.html), [Yuanyou Xu](https://dblp.org/pid/248/7663.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zizheng Xun](https://dblp.org/pid/340/1441.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Dawei Yang](https://dblp.org/pid/22/1038.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), Wankou Yang, [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Yichun Yang](https://dblp.org/pid/249/9678.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Botao Ye](https://dblp.org/pid/227/4610.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Qianjin Yu](https://dblp.org/pid/53/10179.html), [Weichen Yu](https://dblp.org/pid/325/1209.html), [Kang Ze](https://dblp.org/pid/340/1107.html), [Jiang Zhai](https://dblp.org/pid/291/9340.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhu Zhang](https://dblp.org/pid/292/0953.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Haixia Zheng](https://dblp.org/pid/119/1585.html), [Min Zheng](https://dblp.org/pid/23/328.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html):

The Tenth Visual Object Tracking VOT2022 Challenge Results. [ECCV Workshops (8)2022](https://dblp.org/db/conf/eccv/eccv2022-w8.html#conf/eccv/KristanLMFPKCDZLDBZZYYCMFBBCCCCCCCCCCC22): 431-460
- ![](https://dblp.org/img/n.png)

\[i18\]
[Fei Xie](https://dblp.org/pid/51/1316.html), [Chunyu Wang](https://dblp.org/pid/63/7235-1.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Yue Cao](https://dblp.org/pid/74/5570-1.html), Wankou Yang, [Wenjun Zeng](https://dblp.org/pid/57/145.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Correlation-Aware Deep Tracking. [CoRRabs/2203.01666](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-01666) (2022)
- ![](https://dblp.org/img/n.png)

\[i17\]
[Junlong Tong](https://dblp.org/pid/332/1196.html), [Liping Xie](https://dblp.org/pid/91/7400.html), Wankou Yang, [Kanjian Zhang](https://dblp.org/pid/93/1517.html):

Probabilistic Decomposition Transformer for Time Series Forecasting. [CoRRabs/2210.17393](https://dblp.org/db/journals/corr/corr2210.html#journals/corr/abs-2210-17393) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[j83\]
[Hong Li](https://dblp.org/pid/93/6234.html), [Qiang Wang](https://dblp.org/pid/64/5630-23.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huan Wang](https://dblp.org/pid/70/6155-13.html), Wankou Yang:

Infrared small target detection using tensor based least mean square. [Comput. Electr. Eng.91](https://dblp.org/db/journals/cee/cee91.html#journals/cee/LiWWY21): 106994 (2021)
- ![](https://dblp.org/img/n.png)

\[j82\]
[Yun-Hao Yuan](https://dblp.org/pid/51/7436.html), [Jin Li](https://dblp.org/pid/48/1097-28.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yun Li](https://dblp.org/pid/87/6284-10.html), [Jipeng Qiang](https://dblp.org/pid/138/2494.html), [Bin Li](https://dblp.org/pid/89/6764-6.html), Wankou Yang, [Furong Peng](https://dblp.org/pid/138/8117.html):

OPLS-SR: A novel face super-resolution learning method using orthonormalized coherent features. [Inf. Sci.561](https://dblp.org/db/journals/isci/isci561.html#journals/isci/YuanLLQLYP21): 52-69 (2021)
- ![](https://dblp.org/img/n.png)

\[j81\]
[Zhijian Wu](https://dblp.org/pid/23/3616.html), [Jun Li](https://dblp.org/pid/116/1011-33.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianhua Xu](https://dblp.org/pid/57/6846.html), Wankou Yang:

Beyond ITQ: Efficient binary multi-view subspace learning for instance retrieval. [J. Vis. Commun. Image Represent.79](https://dblp.org/db/journals/jvcir/jvcir79.html#journals/jvcir/WuLXY21): 103234 (2021)
- ![](https://dblp.org/img/n.png)

\[j80\]
[Qiang Wang](https://dblp.org/pid/64/5630-23.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lukuan Zhou](https://dblp.org/pid/247/4747.html), [Yuncong Yao](https://dblp.org/pid/17/5361.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Jun Li](https://dblp.org/pid/116/1011-33.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang:

An Interconnected Feature Pyramid Networks for object detection. [J. Vis. Commun. Image Represent.79](https://dblp.org/db/journals/jvcir/jvcir79.html#journals/jvcir/WangZYWLY21): 103260 (2021)
- ![](https://dblp.org/img/n.png)

\[j79\]
[Jian Dong](https://dblp.org/pid/58/3444.html), Wankou Yang, [Yazhou Yao](https://dblp.org/pid/173/6775.html), [Fatih Porikli](https://dblp.org/pid/p/FatihMuratPorikli.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Knowledge memorization and generation for action recognition in still images. [Pattern Recognit.120](https://dblp.org/db/journals/pr/pr120.html#journals/pr/DongYYP21): 108188 (2021)
- ![](https://dblp.org/img/n.png)

\[j78\]
[Lingxiang Yao](https://dblp.org/pid/207/9512.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Worapan Kusakunniran](https://dblp.org/pid/05/7576.html), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenmin Tang](https://dblp.org/pid/13/6728.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Robust gait recognition using hybrid descriptors based on Skeleton Gait Energy Image. [Pattern Recognit. Lett.150](https://dblp.org/db/journals/prl/prl150.html#journals/prl/YaoKWZTY21): 289-296 (2021)
- ![](https://dblp.org/img/n.png)

\[j77\]
[Bingwen Hu](https://dblp.org/pid/215/8072.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhedong Zheng](https://dblp.org/pid/190/7710.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ping Liu](https://dblp.org/pid/34/188-4.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Mingwu Ren](https://dblp.org/pid/84/5438.html):

Unsupervised Eyeglasses Removal in the Wild. [IEEE Trans. Cybern.51(9)](https://dblp.org/db/journals/tcyb/tcyb51.html#journals/tcyb/HuZLYR21): 4373-4385 (2021)
- ![](https://dblp.org/img/n.png)

\[j76\]
[Jun Li](https://dblp.org/pid/116/1011-33.html), [Bo Yang](https://dblp.org/pid/46/999-19.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Jianhua Xu](https://dblp.org/pid/57/6846.html):

Subspace-based multi-view fusion for instance-level image retrieval. [Vis. Comput.37(3)](https://dblp.org/db/journals/vc/vc37.html#journals/vc/LiYYSX21): 619-633 (2021)
- ![](https://dblp.org/img/n.png)

\[c68\]
[Ziwei Chen](https://dblp.org/pid/219/9605.html), [Yiye Wang](https://dblp.org/pid/298/5387.html), Wankou Yang:

Video Based Fall Detection Using Human Poses. [Big Data (CCF)2021](https://dblp.org/db/conf/bdccf/bdccf2021.html#conf/bdccf/ChenWY21): 283-296
- ![](https://dblp.org/img/n.png)

\[c67\]
[Shuangping Jin](https://dblp.org/pid/283/5840.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), Wankou Yang, [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html):

Separable Batch Normalization for Robust Facial Landmark Localization. [BMVC2021](https://dblp.org/db/conf/bmvc/bmvc2021.html#conf/bmvc/JinFYK21): Article 367
- ![](https://dblp.org/img/n.png)

\[c66\]
[Shuangping Jin](https://dblp.org/pid/283/5840.html), [Qiang Wang](https://dblp.org/pid/64/5630-23.html), Wankou Yang:

Explicit Attention Network for Face Alignment. [ICCPR2021](https://dblp.org/db/conf/iccpr/iccpr2021.html#conf/iccpr/JinWY21): 199-203
- ![](https://dblp.org/img/n.png)

\[c65\]
[Yanjie Li](https://dblp.org/pid/70/4538.html), [Shoukui Zhang](https://dblp.org/pid/289/7121.html), [Zhicheng Wang](https://dblp.org/pid/78/1664-1.html), [Sen Yang](https://dblp.org/pid/90/4655.html), Wankou Yang, [Shu-Tao Xia](https://dblp.org/pid/34/3173.html), [Erjin Zhou](https://dblp.org/pid/150/4019.html):

TokenPose: Learning Keypoint Tokens for Human Pose Estimation. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/LiZWYYXZ21): 11293-11302
- ![](https://dblp.org/img/n.png)

\[c64\]
[Sen Yang](https://dblp.org/pid/90/4655.html), [Zhibin Quan](https://dblp.org/pid/141/2189.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mu Nie](https://dblp.org/pid/210/3225.html), Wankou Yang:

TransPose: Keypoint Localization via Transformer. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/YangQNY21): 11782-11792
- ![](https://dblp.org/img/n.png)

\[c63\]
[Fei Xie](https://dblp.org/pid/51/1316.html), Wankou Yang, [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Wangmeng Zuo](https://dblp.org/pid/93/2671.html):

Learning Spatio-Appearance Memory Network for High-Performance Visual Tracking. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/XieYZLWZ21): 2678-2687
- ![](https://dblp.org/img/n.png)

\[c62\]
[Fei Xie](https://dblp.org/pid/51/1316.html), [Chunyu Wang](https://dblp.org/pid/63/7235-1.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), Wankou Yang, [Wenjun Zeng](https://dblp.org/pid/57/145.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning Tracking Representations via Dual-Branch Fully Transformer Networks. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/XieWWYZ21): 2688-2697
- ![](https://dblp.org/img/n.png)

\[c61\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Yu-Chen Chiu](https://dblp.org/pid/199/2494.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Xingping Dong](https://dblp.org/pid/156/3020.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Bilge Günsel](https://dblp.org/pid/47/5125.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Wencheng Han](https://dblp.org/pid/280/3348.html), [Yanyan Huang](https://dblp.org/pid/88/4316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [J. Yin](https://dblp.org/pid/51/2242.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Jingen Liu](https://dblp.org/pid/10/5849.html), [Li Liu](https://dblp.org/pid/33/4528-36.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Jonathon Luiten](https://dblp.org/pid/211/7992.html), [Jie Ma](https://dblp.org/pid/62/5110.html), [Ziang Ma](https://dblp.org/pid/165/9621.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Yuzhen Niu](https://dblp.org/pid/28/7442.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Aravindh Rajiv](https://dblp.org/pid/307/9144.html), [Muhammad Rana](https://dblp.org/pid/276/0222.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Ling Shao](https://dblp.org/pid/75/1281.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furao Shen](https://dblp.org/pid/80/4685.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Paul Voigtlaender](https://dblp.org/pid/166/6430.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html), [Chenyan Wu](https://dblp.org/pid/76/1190.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang Xu](https://dblp.org/pid/126/2962.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), Wankou Yang, [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Xiaohan Zhang](https://dblp.org/pid/96/6053.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Ming Zhen](https://dblp.org/pid/307/8430.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html):

The Ninth Visual Object Tracking VOT2021 Challenge Results. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/KristanMLFPKCDZ21): 2711-2738
- ![](https://dblp.org/img/n.png)

\[i16\]
[Shuangping Jin](https://dblp.org/pid/283/5840.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), Wankou Yang, [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html):

Separable Batch Normalization for Robust Facial Landmark Localization with Cross-protocol Network Training. [CoRRabs/2101.06663](https://dblp.org/db/journals/corr/corr2101.html#journals/corr/abs-2101-06663) (2021)
- ![](https://dblp.org/img/n.png)

\[i15\]
[Ziyu Li](https://dblp.org/pid/177/3057.html), [Yuncong Yao](https://dblp.org/pid/17/5361.html), [Zhibin Quan](https://dblp.org/pid/141/2189.html), Wankou Yang, [Jin Xie](https://dblp.org/pid/80/1949.html):

SIENet: Spatial Information Enhancement Network for 3D Object Detection from Point Cloud. [CoRRabs/2103.15396](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-15396) (2021)
- ![](https://dblp.org/img/n.png)

\[i14\]
[Yanjie Li](https://dblp.org/pid/70/4538.html), [Shoukui Zhang](https://dblp.org/pid/289/7121.html), [Zhicheng Wang](https://dblp.org/pid/78/1664-1.html), [Sen Yang](https://dblp.org/pid/90/4655.html), Wankou Yang, [Shu-Tao Xia](https://dblp.org/pid/34/3173.html), [Erjin Zhou](https://dblp.org/pid/150/4019.html):

TokenPose: Learning Keypoint Tokens for Human Pose Estimation. [CoRRabs/2104.03516](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-03516) (2021)
- ![](https://dblp.org/img/n.png)

\[i13\]
[Yanjie Li](https://dblp.org/pid/70/4538.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Shoukui Zhang](https://dblp.org/pid/289/7121.html), [Zhicheng Wang](https://dblp.org/pid/78/1664-1.html), Wankou Yang, [Shu-Tao Xia](https://dblp.org/pid/34/3173.html), [Erjin Zhou](https://dblp.org/pid/150/4019.html):

Is 2D Heatmap Representation Even Necessary for Human Pose Estimation? [CoRRabs/2107.03332](https://dblp.org/db/journals/corr/corr2107.html#journals/corr/abs-2107-03332) (2021)
- ![](https://dblp.org/img/n.png)

\[i12\]
[Ziwei Chen](https://dblp.org/pid/219/9605.html), [Yiye Wang](https://dblp.org/pid/298/5387.html), Wankou Yang:

Video Based Fall Detection Using Human Poses. [CoRRabs/2107.14633](https://dblp.org/db/journals/corr/corr2107.html#journals/corr/abs-2107-14633) (2021)
- ![](https://dblp.org/img/n.png)

\[i11\]
[Sen Yang](https://dblp.org/pid/90/4655.html), [Zhicheng Wang](https://dblp.org/pid/78/1664-1.html), [Ze Chen](https://dblp.org/pid/15/4184.html), [Yanjie Li](https://dblp.org/pid/70/4538.html), [Shoukui Zhang](https://dblp.org/pid/289/7121.html), [Zhibin Quan](https://dblp.org/pid/141/2189.html), [Shu-Tao Xia](https://dblp.org/pid/34/3173.html), [Yiping Bao](https://dblp.org/pid/235/2626.html), [Erjin Zhou](https://dblp.org/pid/150/4019.html), Wankou Yang:

Attend to Who You Are: Supervising Self-Attention for Keypoint Detection and Instance-Aware Association. [CoRRabs/2111.12892](https://dblp.org/db/journals/corr/corr2111.html#journals/corr/abs-2111-12892) (2021)
- ![](https://dblp.org/img/n.png)

\[i10\]
[Fei Xie](https://dblp.org/pid/51/1316.html), [Chunyu Wang](https://dblp.org/pid/63/7235-1.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), Wankou Yang, [Wenjun Zeng](https://dblp.org/pid/57/145.html):

Learning Tracking Representations via Dual-Branch Fully Transformer Networks. [CoRRabs/2112.02571](https://dblp.org/db/journals/corr/corr2112.html#journals/corr/abs-2112-02571) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[j75\]
Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Ziyu Li](https://dblp.org/pid/177/3057.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chao Wang](https://dblp.org/pid/188/7759.html), [Jun Li](https://dblp.org/pid/116/1011-33.html):

A multi-task Faster R-CNN method for 3D vehicle detection based on a single image. [Appl. Soft Comput.95](https://dblp.org/db/journals/asc/asc95.html#journals/asc/YangLWL20): 106533 (2020)
- ![](https://dblp.org/img/n.png)

\[j74\]
Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Xian Zhang](https://dblp.org/pid/56/5624.html), [Jun Li](https://dblp.org/pid/l/JunLi11.html):

A local multiple patterns feature descriptor for face recognition. [Neurocomputing373](https://dblp.org/db/journals/ijon/ijon373.html#journals/ijon/YangZL20): 109-122 (2020)
- ![](https://dblp.org/img/n.png)

\[j73\]
[Biyun Sheng](https://dblp.org/pid/158/1357.html), [Jun Li](https://dblp.org/pid/116/1011.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Multilayer deep features with multiple kernel learning for action recognition. [Neurocomputing399](https://dblp.org/db/journals/ijon/ijon399.html#journals/ijon/ShengLXY20): 65-74 (2020)
- ![](https://dblp.org/img/n.png)

\[j72\]
[Guangwei Gao](https://dblp.org/pid/118/3484.html), [Dong Zhu](https://dblp.org/pid/57/5560.html), [Meng Yang](https://dblp.org/pid/44/2761-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huimin Lu](https://dblp.org/pid/64/2633-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Hao Gao](https://dblp.org/pid/69/8912-5.html):

Face image super-resolution with pose via nuclear norm regularized structural orthogonal Procrustes regression. [Neural Comput. Appl.32(9)](https://dblp.org/db/journals/nca/nca32.html#journals/nca/GaoZYLYG20): 4361-4371 (2020)
- ![](https://dblp.org/img/n.png)

\[j71\]
[Feng Liu](https://dblp.org/pid/77/1318-36.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tao Xiang](https://dblp.org/pid/22/4460-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Timothy M. Hospedales](https://dblp.org/pid/32/3545.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Changyin Sun](https://dblp.org/pid/64/221.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Inverse Visual Question Answering: A New Benchmark and VQA Diagnosis Tool. [IEEE Trans. Pattern Anal. Mach. Intell.42(2)](https://dblp.org/db/journals/pami/pami42.html#journals/pami/LiuXHYS20): 460-474 (2020)
- ![](https://dblp.org/img/n.png)

\[j70\]
[Pourya Shamsolmoali](https://dblp.org/pid/154/8477.html), [Abdul Hamid Sadka](https://dblp.org/pid/89/5742.html), [Huiyu Zhou](https://dblp.org/pid/36/1648.html), Wankou Yang:

Advanced deep learning for image super-resolution. [Signal Process. Image Commun.82](https://dblp.org/db/journals/spic/spic82.html#journals/spic/ShamsolmoaliSZY20): 115732 (2020)
- ![](https://dblp.org/img/n.png)

\[j69\]
[Biyun Sheng](https://dblp.org/pid/158/1357.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Li](https://dblp.org/pid/116/1011-33.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qun Li](https://dblp.org/pid/42/6066-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Junwei Han](https://dblp.org/pid/00/3003.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Discriminative Multi-View Subspace Feature Learning for Action Recognition. [IEEE Trans. Circuits Syst. Video Technol.30(12)](https://dblp.org/db/journals/tcsv/tcsv30.html#journals/tcsv/ShengLXLYH20): 4591-4600 (2020)
- ![](https://dblp.org/img/n.png)

\[j68\]
[Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Ze Wang](https://dblp.org/pid/35/6674-8.html), [Lian Zhuo](https://dblp.org/pid/218/5220.html), [Jungong Han](https://dblp.org/pid/98/6127.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiantong Zhen](https://dblp.org/pid/78/10651.html):

The Structure Transfer Machine Theory and Applications. [IEEE Trans. Image Process.29](https://dblp.org/db/journals/tip/tip29.html#journals/tip/ZhangYWZHZ20): 2889-2902 (2020)
- ![](https://dblp.org/img/n.png)

\[j67\]
[Jun Li](https://dblp.org/pid/116/1011-33.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chang Xu](https://dblp.org/pid/97/2966-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Changyin Sun](https://dblp.org/pid/64/221.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianhua Xu](https://dblp.org/pid/57/6846.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hong Zhang](https://dblp.org/pid/24/6914-13.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Discriminative Multi-View Privileged Information Learning for Image Re-Ranking. [IEEE Trans. Image Process.29](https://dblp.org/db/journals/tip/tip29.html#journals/tip/LiXYSXZ20): 3490-3505 (2020)
- ![](https://dblp.org/img/n.png)

\[j66\]
[Zhibin Quan](https://dblp.org/pid/141/2189.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weili Zeng](https://dblp.org/pid/86/11483.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xuelian Li](https://dblp.org/pid/85/7695.html), [Yandong Liu](https://dblp.org/pid/83/605.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yunxiu Yu](https://dblp.org/pid/211/9450.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png):

Recurrent Neural Networks With External Addressable Long-Term and Working Memory for Learning Long-Term Dependences. [IEEE Trans. Neural Networks Learn. Syst.31(3)](https://dblp.org/db/journals/tnn/tnn31.html#journals/tnn/QuanZLLYY20): 813-826 (2020)
- ![](https://dblp.org/img/n.png)

\[j65\]
[Haofeng Zhang](https://dblp.org/pid/17/4297.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huaqi Mao](https://dblp.org/pid/263/3026.html), [Yang Long](https://dblp.org/pid/82/10183-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Probabilistic Zero-Shot Learning Method via Latent Nonnegative Prototype Synthesis of Unseen Classes. [IEEE Trans. Neural Networks Learn. Syst.31(7)](https://dblp.org/db/journals/tnn/tnn31.html#journals/tnn/ZhangM0Y020): 2361-2375 (2020)
- ![](https://dblp.org/img/n.png)

\[c60\]
[Jiemi Bai](https://dblp.org/pid/276/3622.html), [Yazhou Yao](https://dblp.org/pid/173/6775.html), [Qiong Wang](https://dblp.org/pid/65/3144-3.html), [Yichao Zhou](https://dblp.org/pid/146/9862.html), Wankou Yang, [Fumin Shen](https://dblp.org/pid/92/10934.html):

Multi-model Network for Fine-Grained Cross-Media Retrieval. [PRCV (2)2020](https://dblp.org/db/conf/prcv/prcv2020-2.html#conf/prcv/BaiYWZYS20): 187-199
- ![](https://dblp.org/img/n.png)

\[c59\]
[Duyao Fan](https://dblp.org/pid/276/3634.html), [Yazhou Yao](https://dblp.org/pid/173/6775.html), [Yunfei Cai](https://dblp.org/pid/172/2636.html), [Xiangbo Shu](https://dblp.org/pid/169/3410.html), [Pu Huang](https://dblp.org/pid/51/3775.html), Wankou Yang:

A Novel CNN Architecture for Real-Time Point Cloud Recognition in Road Environment. [PRCV (1)2020](https://dblp.org/db/conf/prcv/prcv2020-1.html#conf/prcv/FanYCSHY20): 206-218
- ![](https://dblp.org/img/n.png)

\[c58\]
[Fei Xie](https://dblp.org/pid/51/1316.html), [Ning Wang](https://dblp.org/pid/46/2005-20.html), [Yuncong Yao](https://dblp.org/pid/17/5361.html), Wankou Yang, [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html):

Hierarchical Representations with Discriminative Meta-filters in Dual Path Network for Tracking. [PRCV (2)2020](https://dblp.org/db/conf/prcv/prcv2020-2.html#conf/prcv/XieWYYZL20): 303-315
- ![](https://dblp.org/img/n.png)

\[i9\]
[Fei Xie](https://dblp.org/pid/51/1316.html), Wankou Yang, [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Wangmeng Zuo](https://dblp.org/pid/93/2671.html):

Discriminative Segmentation Tracking Using Dual Memory Banks. [CoRRabs/2009.09669](https://dblp.org/db/journals/corr/corr2009.html#journals/corr/abs-2009-09669) (2020)
- ![](https://dblp.org/img/n.png)

\[i8\]
[Sen Yang](https://dblp.org/pid/90/4655.html), [Zhibin Quan](https://dblp.org/pid/141/2189.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mu Nie](https://dblp.org/pid/210/3225.html), Wankou Yang:

TransPose: Towards Explainable Human Pose Estimation by Transformer. [CoRRabs/2012.14214](https://dblp.org/db/journals/corr/corr2012.html#journals/corr/abs-2012-14214) (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j64\]
[Yifan Gu](https://dblp.org/pid/167/3881.html), [Shidong Wang](https://dblp.org/pid/82/8629.html), [Haofeng Zhang](https://dblp.org/pid/17/4297.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yazhou Yao](https://dblp.org/pid/173/6775.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Li Liu](https://dblp.org/pid/33/4528-4.html):

Clustering-driven unsupervised deep hashing for image retrieval. [Neurocomputing368](https://dblp.org/db/journals/ijon/ijon368.html#journals/ijon/GuWZYY019): 114-123 (2019)
- ![](https://dblp.org/img/n.png)

\[j63\]
[Haofeng Zhang](https://dblp.org/pid/17/4297.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Long](https://dblp.org/pid/82/10183-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Dual-verification network for zero-shot learning. [Inf. Sci.470](https://dblp.org/db/journals/isci/isci470.html#journals/isci/ZhangLYS19): 43-57 (2019)
- ![](https://dblp.org/img/n.png)

\[j62\]
[Qiming Sun](https://dblp.org/pid/65/7929.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Changyin Sun](https://dblp.org/pid/64/221.html), Wankou Yang:

Exploiting aggregate channel features for urine sediment detection. [Multim. Tools Appl.78(17)](https://dblp.org/db/journals/mta/mta78.html#journals/mta/SunYSY19): 23883-23895 (2019)
- ![](https://dblp.org/img/n.png)

\[j61\]
Wankou Yang, [Lukuan Zhou](https://dblp.org/pid/247/4747.html), [Tianhuang Li](https://dblp.org/pid/247/4712.html), [Haoran Wang](https://dblp.org/pid/28/3021-1.html):

A Face Detection Method Based on Cascade Convolutional Neural Network. [Multim. Tools Appl.78(17)](https://dblp.org/db/journals/mta/mta78.html#journals/mta/YangZLW19): 24373-24390 (2019)
- ![](https://dblp.org/img/n.png)

\[j60\]
[Yazhou Yao](https://dblp.org/pid/173/6775.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Pu Huang](https://dblp.org/pid/51/3775.html), [Qiong Wang](https://dblp.org/pid/65/3144-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yunfei Cai](https://dblp.org/pid/172/2636.html), [Zhenmin Tang](https://dblp.org/pid/13/6728.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Exploiting textual and visual features for image categorization. [Pattern Recognit. Lett.117](https://dblp.org/db/journals/prl/prl117.html#journals/prl/YaoYHWCT19): 140-145 (2019)
- ![](https://dblp.org/img/n.png)

\[j59\]
Wankou Yang, [Su-Jing Wang](https://dblp.org/pid/209/7218.html), [Pritee Khanna](https://dblp.org/pid/75/3036.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiong Li](https://dblp.org/pid/63/6031-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Pattern Recognition Techniques for Non Verbal Human Behavior (NVHB). [Pattern Recognit. Lett.125](https://dblp.org/db/journals/prl/prl125.html#journals/prl/YangWKL19): 684-686 (2019)
- ![](https://dblp.org/img/n.png)

\[j58\]
[Hongren Wang](https://dblp.org/pid/227/4893-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ce Li](https://dblp.org/pid/58/411-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiantong Zhen](https://dblp.org/pid/78/10651.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Gaussian Transfer Convolutional Neural Networks. [IEEE Trans. Emerg. Top. Comput. Intell.3(5)](https://dblp.org/db/journals/tetci/tetci3.html#journals/tetci/WangLZYZ19): 360-368 (2019)
- ![](https://dblp.org/img/n.png)

\[j57\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Zuo](https://dblp.org/pid/15/2278.html), [Lei Zhu](https://dblp.org/pid/99/549-10.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Li](https://dblp.org/pid/116/1011-33.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Haibin Ling](https://dblp.org/pid/93/3488.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Pedestrian Proposal and Refining Based on the Shared Pixel Differential Feature. [IEEE Trans. Intell. Transp. Syst.20(6)](https://dblp.org/db/journals/tits/tits20.html#journals/tits/ShenZZLYL19): 2085-2095 (2019)
- ![](https://dblp.org/img/n.png)

\[j56\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Zuo](https://dblp.org/pid/15/2278.html), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Danil V. Prokhorov](https://dblp.org/pid/74/5147.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xue Mei](https://dblp.org/pid/29/4521.html), [Haibin Ling](https://dblp.org/pid/93/3488.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Differential Features for Pedestrian Detection: A Taylor Series Perspective. [IEEE Trans. Intell. Transp. Syst.20(8)](https://dblp.org/db/journals/tits/tits20.html#journals/tits/ShenZYPML19): 2913-2922 (2019)
- ![](https://dblp.org/img/n.png)

\[j55\]
[Jun Li](https://dblp.org/pid/116/1011-33.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chang Xu](https://dblp.org/pid/97/2966-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Ramamohanarao Kotagiri](https://dblp.org/pid/r/KRamamohanarao.html), [Dacheng Tao](https://dblp.org/pid/46/3391.html)![](https://dblp.org/img/orcid-mark.12x12.png):

ROMIR: Robust Multi-View Image Re-Ranking. [IEEE Trans. Knowl. Data Eng.31(12)](https://dblp.org/db/journals/tkde/tkde31.html#journals/tkde/LiXYSKT19): 2393-2406 (2019)
- ![](https://dblp.org/img/n.png)

\[j54\]
[Wenming Zheng](https://dblp.org/pid/64/2253.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Cheng Lu](https://dblp.org/pid/91/1482-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhouchen Lin](https://dblp.org/pid/l/ZhouchenLin.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tong Zhang](https://dblp.org/pid/07/4227-21.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhen Cui](https://dblp.org/pid/59/8491-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang:

ℓ1-Norm Heteroscedastic Discriminant Analysis Under Mixture of Gaussian Distributions. [IEEE Trans. Neural Networks Learn. Syst.30(10)](https://dblp.org/db/journals/tnn/tnn30.html#journals/tnn/ZhengLL0CY19): 2898-2915 (2019)
- ![](https://dblp.org/img/n.png)

\[j53\]
[Qiaolin Ye](https://dblp.org/pid/44/7694.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zechao Li](https://dblp.org/pid/51/8693.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liyong Fu](https://dblp.org/pid/155/9293.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhao Zhang](https://dblp.org/pid/87/6853-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Guowei Yang](https://dblp.org/pid/43/3366-2.html):

Nonpeaked Discriminant Analysis for Data Representation. [IEEE Trans. Neural Networks Learn. Syst.30(12)](https://dblp.org/db/journals/tnn/tnn30.html#journals/tnn/YeLFZYY19): 3818-3832 (2019)
- ![](https://dblp.org/img/n.png)

\[c57\]
[Xian Zhang](https://dblp.org/pid/56/5624.html), [Xinjie Tong](https://dblp.org/pid/244/0818.html), [Ziyu Li](https://dblp.org/pid/177/3057.html), Wankou Yang:

A Robust Facial Landmark Detector with Mixed Loss. [IScIDE (1)2019](https://dblp.org/db/conf/iscide/iscide2019-1.html#conf/iscide/ZhangTLY19): 249-261
- ![](https://dblp.org/img/n.png)

\[c56\]
[Yonggui He](https://dblp.org/pid/187/6203.html), [Yaoye Song](https://dblp.org/pid/254/0543.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html), Wankou Yang:

Visual Saliency Guided Deep Fabric Defect Classification. [IScIDE (1)2019](https://dblp.org/db/conf/iscide/iscide2019-1.html#conf/iscide/HeSSY19): 435-446
- ![](https://dblp.org/img/n.png)

\[i7\]
[Sen Yang](https://dblp.org/pid/90/4655.html), Wankou Yang, [Zhen Cui](https://dblp.org/pid/59/8491-1.html):

Pose Neural Fabrics Search. [CoRRabs/1909.07068](https://dblp.org/db/journals/corr/corr1909.html#journals/corr/abs-1909-07068) (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[j52\]
Wankou Yang![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Li](https://dblp.org/pid/116/1011-33.html), [Hao Zheng](https://dblp.org/pid/31/6916.html), [Richard Yi Da Xu](https://dblp.org/pid/38/3064.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Nuclear Norm Based Matrix Regression Based Projections Method for Feature Extraction. [IEEE Access6](https://dblp.org/db/journals/access/access6.html#journals/access/YangLZX18): 7445-7451 (2018)
- ![](https://dblp.org/img/n.png)

\[j51\]
[Jinxia Zhang](https://dblp.org/pid/89/1778.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shixiong Fang](https://dblp.org/pid/205/8118.html), [Krista A. Ehinger](https://dblp.org/pid/13/8654.html), [Haikun Wei](https://dblp.org/pid/16/6484.html), Wankou Yang, [Kanjian Zhang](https://dblp.org/pid/93/1517.html), [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

Hypergraph Optimization for Salient Region Detection Based on Foreground and Background Queries. [IEEE Access6](https://dblp.org/db/journals/access/access6.html#journals/access/ZhangFEWYZY18): 26729-26741 (2018)
- ![](https://dblp.org/img/n.png)

\[j50\]
[Jiasong Wu](https://dblp.org/pid/63/8859.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shijie Qiu](https://dblp.org/pid/177/9019.html), [Youyong Kong](https://dblp.org/pid/154/7641.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Longyu Jiang](https://dblp.org/pid/69/10291.html), [Yang Chen](https://dblp.org/pid/48/4792-8.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Lotfi Senhadji](https://dblp.org/pid/58/670.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huazhong Shu](https://dblp.org/pid/56/121.html):

PCANet: An energy perspective. [Neurocomputing313](https://dblp.org/db/journals/ijon/ijon313.html#journals/ijon/WuQKJCYSS18): 271-287 (2018)
- ![](https://dblp.org/img/n.png)

\[j49\]
[Haoran Wang](https://dblp.org/pid/28/3021-1.html), [Chunfeng Yuan](https://dblp.org/pid/47/2506.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html), Wankou Yang, [Haibin Ling](https://dblp.org/pid/93/3488.html):

Action unit detection and key frame selection for human activity prediction. [Neurocomputing318](https://dblp.org/db/journals/ijon/ijon318.html#journals/ijon/WangYSYL18): 109-119 (2018)
- ![](https://dblp.org/img/n.png)

\[j48\]
[Biyun Sheng](https://dblp.org/pid/158/1357.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chunhua Shen](https://dblp.org/pid/56/1673.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guosheng Lin](https://dblp.org/pid/126/4778.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Li](https://dblp.org/pid/116/1011-33.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Crowd Counting via Weighted VLAD on a Dense Attribute Feature Map. [IEEE Trans. Circuits Syst. Video Technol.28(8)](https://dblp.org/db/journals/tcsv/tcsv28.html#journals/tcsv/ShengSLLYS18): 1788-1797 (2018)
- ![](https://dblp.org/img/n.png)

\[c55\]
[Yazhou Yao](https://dblp.org/pid/173/6775.html), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fumin Shen](https://dblp.org/pid/92/10934.html), Wankou Yang, [Pu Huang](https://dblp.org/pid/51/3775.html), [Zhenmin Tang](https://dblp.org/pid/13/6728.html):

Discovering and Distinguishing Multiple Visual Senses for Polysemous Words. [AAAI2018](https://dblp.org/db/conf/aaai/aaai2018.html#conf/aaai/YaoZSYHT18): 523-530
- ![](https://dblp.org/img/n.png)

\[c54\]
[Feng Liu](https://dblp.org/pid/77/1318-36.html), [Tao Xiang](https://dblp.org/pid/22/4460-2.html), [Timothy M. Hospedales](https://dblp.org/pid/32/3545.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

IVQA: Inverse Visual Question Answering. [CVPR2018](https://dblp.org/db/conf/cvpr/cvpr2018.html#conf/cvpr/LiuXHYS18): 8611-8619
- ![](https://dblp.org/img/n.png)

\[c53\]
[Yazhou Yao](https://dblp.org/pid/173/6775.html), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fumin Shen](https://dblp.org/pid/92/10934.html), Wankou Yang, [Xian-Sheng Hua](https://dblp.org/pid/56/5807-1.html), [Zhenmin Tang](https://dblp.org/pid/13/6728.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Extracting Privileged Information from Untagged Corpora for Classifier Learning. [IJCAI2018](https://dblp.org/db/conf/ijcai/ijcai2018.html#conf/ijcai/YaoZSYHT18): 1085-1091
- ![](https://dblp.org/img/n.png)

\[c52\]
[Jun Li](https://dblp.org/pid/116/1011-33.html), [Bo Yang](https://dblp.org/pid/46/999-19.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Hong Zhang](https://dblp.org/pid/24/6914-13.html):

When Deep Meets Shallow: Subspace-Based Multi-View Fusion for Instance-Level Image Retrieval. [ROBIO2018](https://dblp.org/db/conf/robio/robio2018.html#conf/robio/LiYYSZ18): 486-492
- ![](https://dblp.org/img/n.png)

\[c51\]
[Shangzhen Luan](https://dblp.org/pid/182/1956.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Siyue Zhou](https://dblp.org/pid/218/9477.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), [Jungong Han](https://dblp.org/pid/98/6127.html), Wankou Yang, [Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html):

Gabor Convolutional Networks. [WACV2018](https://dblp.org/db/conf/wacv/wacv2018.html#conf/wacv/LuanZZ0HYL18): 1254-1262
- ![](https://dblp.org/img/n.png)

\[i6\]
[Feng Liu](https://dblp.org/pid/77/1318-36.html), [Tao Xiang](https://dblp.org/pid/22/4460-2.html), [Timothy M. Hospedales](https://dblp.org/pid/32/3545.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Inverse Visual Question Answering: A New Benchmark and VQA Diagnosis Tool. [CoRRabs/1803.06936](https://dblp.org/db/journals/corr/corr1803.html#journals/corr/abs-1803-06936) (2018)
- ![](https://dblp.org/img/n.png)

\[i5\]
[Jun Li](https://dblp.org/pid/116/1011-33.html), [Chang Xu](https://dblp.org/pid/97/2966-2.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Dacheng Tao](https://dblp.org/pid/46/3391.html), [Hong Zhang](https://dblp.org/pid/24/6914-13.html):

Discriminative multi-view Privileged Information learning for image re-ranking. [CoRRabs/1808.04437](https://dblp.org/db/journals/corr/corr1808.html#journals/corr/abs-1808-04437) (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[j47\]
[Haoran Wang](https://dblp.org/pid/28/3021-1.html), Wankou Yang, [Chunfeng Yuan](https://dblp.org/pid/47/2506.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Weiming Hu](https://dblp.org/pid/41/6824-4.html):

Human activity prediction using temporally-weighted generalized time warping. [Neurocomputing225](https://dblp.org/db/journals/ijon/ijon225.html#journals/ijon/WangYYLH17): 139-147 (2017)
- ![](https://dblp.org/img/n.png)

\[j46\]
[Biyun Sheng](https://dblp.org/pid/158/1357.html), [Qichang Hu](https://dblp.org/pid/169/9980.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Li](https://dblp.org/pid/116/1011-33.html), Wankou Yang, [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Filtered shallow-deep feature channels for pedestrian detection. [Neurocomputing249](https://dblp.org/db/journals/ijon/ijon249.html#journals/ijon/ShengHLYZS17): 19-27 (2017)
- ![](https://dblp.org/img/n.png)

\[j45\]
[Jun Li](https://dblp.org/pid/116/1011-33.html), [Chang Xu](https://dblp.org/pid/97/2966-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

SPA: Spatially Pooled Attributes for image retrieval. [Neurocomputing257](https://dblp.org/db/journals/ijon/ijon257.html#journals/ijon/LiXYS17): 47-58 (2017)
- ![](https://dblp.org/img/n.png)

\[j44\]
Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Wenming Zheng](https://dblp.org/pid/64/2253.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Karl Ricanek](https://dblp.org/pid/39/609.html):

Gender classification using 3D statistical models. [Multim. Tools Appl.76(3)](https://dblp.org/db/journals/mta/mta76.html#journals/mta/YangSZR17): 4491-4503 (2017)
- ![](https://dblp.org/img/n.png)

\[j43\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), [Xin Zuo](https://dblp.org/pid/15/2278.html), [Hui Liu](https://dblp.org/pid/93/4010.html), [Haoran Wang](https://dblp.org/pid/28/3021-1.html), Wankou Yang, [Chengshan Qian](https://dblp.org/pid/133/3243.html):

Supervised Local High-Order Differential Channel Feature Learning for Pedestrian Detection. [Neural Process. Lett.45(3)](https://dblp.org/db/journals/npl/npl45.html#journals/npl/ShenZLWYQ17): 1025-1037 (2017)
- ![](https://dblp.org/img/n.png)

\[j42\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Zuo](https://dblp.org/pid/15/2278.html), [Jun Li](https://dblp.org/pid/116/1011-33.html), Wankou Yang, [Haibin Ling](https://dblp.org/pid/93/3488.html):

A novel pixel neighborhood differential statistic feature for pedestrian and face detection. [Pattern Recognit.63](https://dblp.org/db/journals/pr/pr63.html#journals/pr/ShenZLYL17): 127-138 (2017)
- ![](https://dblp.org/img/n.png)

\[j41\]
[Guangwei Gao](https://dblp.org/pid/118/3484.html), [Jian Yang](https://dblp.org/pid/y/JianYang3.html), [Xiao-Yuan Jing](https://dblp.org/pid/59/1365.html), [Fumin Shen](https://dblp.org/pid/92/10934.html), Wankou Yang, [Dong Yue](https://dblp.org/pid/72/4106-1.html):

Learning robust and discriminative low-rank representations for face recognition with occlusion. [Pattern Recognit.66](https://dblp.org/db/journals/pr/pr66.html#journals/pr/GaoYJSYY17): 129-143 (2017)
- ![](https://dblp.org/img/n.png)

\[j40\]
[Jun Li](https://dblp.org/pid/116/1011-33.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chang Xu](https://dblp.org/pid/97/2966-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Dacheng Tao](https://dblp.org/pid/46/3391.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Discriminative Multi-View Interactive Image Re-Ranking. [IEEE Trans. Image Process.26(7)](https://dblp.org/db/journals/tip/tip26.html#journals/tip/LiXYST17): 3113-3127 (2017)
- ![](https://dblp.org/img/n.png)

\[c50\]
[Guangwei Gao](https://dblp.org/pid/118/3484.html), [Pu Huang](https://dblp.org/pid/51/3775.html), [Dong Yue](https://dblp.org/pid/72/4106-1.html), Wankou Yang:

Locality-Constrained Structral Orthogonal Procrustes Regression for Low-Resolution Face Recognition with Pose Variations. [ACPR2017](https://dblp.org/db/conf/acpr/acpr2017.html#conf/acpr/GaoHYY17): 554-558
- ![](https://dblp.org/img/n.png)

\[c49\]
[Jing Lou](https://dblp.org/pid/54/9756.html), [Fenglei Xu](https://dblp.org/pid/230/6532.html), [Qingyuan Xia](https://dblp.org/pid/198/1080.html), Wankou Yang, [Mingwu Ren](https://dblp.org/pid/84/5438.html):

Hierarchical Co-salient Object Detection via Color Names. [ACPR2017](https://dblp.org/db/conf/acpr/acpr2017.html#conf/acpr/LouXXYR17): 718-724
- ![](https://dblp.org/img/n.png)

\[c48\]
[Feng Liu](https://dblp.org/pid/77/1318-36.html), [Tao Xiang](https://dblp.org/pid/22/4460-2.html), [Timothy M. Hospedales](https://dblp.org/pid/32/3545.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Semantic Regularisation for Recurrent Image Annotation. [CVPR2017](https://dblp.org/db/conf/cvpr/cvpr2017.html#conf/cvpr/LiuXHYS17): 4160-4168
- ![](https://dblp.org/img/n.png)

\[c47\]
[Lu Dong](https://dblp.org/pid/40/2448-2.html), [Jun Li](https://dblp.org/pid/116/1011-33.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Robust optimal control for time-delay systems with dynamic uncertainties via ADP. [IJCNN2017](https://dblp.org/db/conf/ijcnn/ijcnn2017.html#conf/ijcnn/DongLYS17): 4229-4235
- ![](https://dblp.org/img/n.png)

\[c46\]
[Shuihua Wang](https://dblp.org/pid/18/8544.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Zhengchao Dong](https://dblp.org/pid/61/9409.html), [Preetha Phillips](https://dblp.org/pid/145/9806.html), [Yudong Zhang](https://dblp.org/pid/39/2699-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Facial Emotion Recognition via Discrete Wavelet Transform, Principal Component Analysis, and Cat Swarm Optimization. [IScIDE2017](https://dblp.org/db/conf/iscide/iscide2017.html#conf/iscide/WangYDPZ17): 203-214
- ![](https://dblp.org/img/n.png)

\[c45\]
[Kai Zang](https://dblp.org/pid/205/8078.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html), Wankou Yang:

Using LFDA to Learn Subset-Haar-Like Intermediate Feature Weights for Pedestrian Detection. [IScIDE2017](https://dblp.org/db/conf/iscide/iscide2017.html#conf/iscide/ZangSY17): 215-230
- ![](https://dblp.org/img/n.png)

\[c44\]
[Jinxia Zhang](https://dblp.org/pid/89/1778.html), [Shixiong Fang](https://dblp.org/pid/205/8118.html), [Krista A. Ehinger](https://dblp.org/pid/13/8654.html), [Weili Guo](https://dblp.org/pid/146/8424.html), Wankou Yang, [Haikun Wei](https://dblp.org/pid/16/6484.html):

Probabilistic Hypergraph Optimization for Salient Object Detection. [IScIDE2017](https://dblp.org/db/conf/iscide/iscide2017.html#conf/iscide/ZhangFEGYW17): 368-378
- ![](https://dblp.org/img/n.png)

\[i4\]
[Yazhou Yao](https://dblp.org/pid/173/6775.html), [Jian Zhang](https://dblp.org/pid/07/314-2.html), [Fumin Shen](https://dblp.org/pid/92/10934.html), [Xian-Sheng Hua](https://dblp.org/pid/56/5807-1.html), Wankou Yang, [Zhenmin Tang](https://dblp.org/pid/13/6728.html):

Refining Image Categorization by Exploiting Web Images and General Corpus. [CoRRabs/1703.05451](https://dblp.org/db/journals/corr/corr1703.html#journals/corr/YaoZSHYT17) (2017)
- ![](https://dblp.org/img/n.png)

\[i3\]
[Feng Liu](https://dblp.org/pid/77/1318-36.html), [Tao Xiang](https://dblp.org/pid/22/4460-2.html), [Timothy M. Hospedales](https://dblp.org/pid/32/3545.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

iVQA: Inverse Visual Question Answering. [CoRRabs/1710.03370](https://dblp.org/db/journals/corr/corr1710.html#journals/corr/abs-1710-03370) (2017)
- 2016
- ![](https://dblp.org/img/n.png)

\[j39\]
[Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Suli Ji](https://dblp.org/pid/150/4045.html), [Li Li](https://dblp.org/pid/53/2189.html), [Shengping Zhang](https://dblp.org/pid/60/1866.html), Wankou Yang:

Sparsity analysis versus sparse representation classifier. [Neurocomputing171](https://dblp.org/db/journals/ijon/ijon171.html#journals/ijon/ZhangJLZY16): 387-393 (2016)
- ![](https://dblp.org/img/n.png)

\[j38\]
[Hoangvu Nguyen](https://dblp.org/pid/160/2774.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Biyun Sheng](https://dblp.org/pid/158/1357.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Discriminative low-rank dictionary learning for face recognition. [Neurocomputing173](https://dblp.org/db/journals/ijon/ijon173.html#journals/ijon/NguyenYSS16): 541-551 (2016)
- ![](https://dblp.org/img/n.png)

\[j37\]
Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Wenming Zheng](https://dblp.org/pid/64/2253.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A regularized least square based discriminative projections for feature extraction. [Neurocomputing175](https://dblp.org/db/journals/ijon/ijon175.html#journals/ijon/YangSZ16): 198-205 (2016)
- ![](https://dblp.org/img/n.png)

\[j36\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), [Xin Zuo](https://dblp.org/pid/15/2278.html), Wankou Yang, [Hualong Yu](https://dblp.org/pid/13/4009.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guohai Liu](https://dblp.org/pid/34/1121.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning discriminative shape statistics distribution features for pedestrian detection. [Neurocomputing184](https://dblp.org/db/journals/ijon/ijon184.html#journals/ijon/ShenZYYL16): 66-77 (2016)
- ![](https://dblp.org/img/n.png)

\[j35\]
[Jun Li](https://dblp.org/pid/116/1011-33.html), [Chang Xu](https://dblp.org/pid/97/2966-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mingming Gong](https://dblp.org/pid/98/8479.html), [Junliang Xing](https://dblp.org/pid/43/7659.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

SERVE: Soft and Equalized Residual VEctors for image retrieval. [Neurocomputing207](https://dblp.org/db/journals/ijon/ijon207.html#journals/ijon/LiXGXYS16): 202-212 (2016)
- ![](https://dblp.org/img/n.png)

\[j34\]
Wankou Yang, [Zhenyu Wang](https://dblp.org/pid/22/1486.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html):

Face recognition using adaptive local ternary patterns method. [Neurocomputing213](https://dblp.org/db/journals/ijon/ijon213.html#journals/ijon/YangWZ16): 183-190 (2016)
- ![](https://dblp.org/img/n.png)

\[j33\]
[Hualong Yu](https://dblp.org/pid/13/4009.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changyin Sun](https://dblp.org/pid/64/221.html), [Xibei Yang](https://dblp.org/pid/53/779.html), Wankou Yang, [Jifeng Shen](https://dblp.org/pid/23/8615.html), [Yunsong Qi](https://dblp.org/pid/48/1306.html):

ODOC-ELM: Optimal decision outputs compensation-based extreme learning machine for classifying imbalanced data. [Knowl. Based Syst.92](https://dblp.org/db/journals/kbs/kbs92.html#journals/kbs/YuSYYSQ16): 55-70 (2016)
- ![](https://dblp.org/img/n.png)

\[j32\]
[Fumin Shen](https://dblp.org/pid/92/10934.html), Wankou Yang, [Hanxi Li](https://dblp.org/pid/21/5003.html), [Hanwang Zhang](https://dblp.org/pid/79/8116.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Heng Tao Shen](https://dblp.org/pid/s/HTShen.html):

Robust regression based face recognition with fast outlier removal. [Multim. Tools Appl.75(20)](https://dblp.org/db/journals/mta/mta75.html#journals/mta/ShenYLZS16): 12535-12546 (2016)
- ![](https://dblp.org/img/n.png)

\[j31\]
[Zhenyu Wang](https://dblp.org/pid/22/1486.html), Wankou Yang, [Fumin Shen](https://dblp.org/pid/92/10934.html):

Face Recognition Using A Low Rank Representation Based Projections Method. [Neural Process. Lett.43(3)](https://dblp.org/db/journals/npl/npl43.html#journals/npl/WangYS16): 823-835 (2016)
- ![](https://dblp.org/img/n.png)

\[j30\]
[Shigang Liu](https://dblp.org/pid/88/2562.html), [Yali Peng](https://dblp.org/pid/13/11029.html), [Xianye Ben](https://dblp.org/pid/96/10791.html), Wankou Yang, [Guoyong Qiu](https://dblp.org/pid/10/10778.html):

A novel label learning algorithm for face recognition. [Signal Process.124](https://dblp.org/db/journals/sigpro/sigpro124.html#journals/sigpro/LiuPBYQ16): 141-146 (2016)
- ![](https://dblp.org/img/n.png)

\[j29\]
[Xiaoyong Yan](https://dblp.org/pid/70/8665.html), [Zhong Yang](https://dblp.org/pid/46/2248.html), [Aiguo Song](https://dblp.org/pid/21/1796.html), Wankou Yang, [Yu Liu](https://dblp.org/pid/97/2274.html), [Ronghui Zhu](https://dblp.org/pid/175/5685.html):

A Novel Multihop Range-Free Localization Based on Kernel Learning Approach for the Internet of Things. [Wirel. Pers. Commun.87(1)](https://dblp.org/db/journals/wpc/wpc87.html#journals/wpc/YanYSYLZ16): 269-292 (2016)
- ![](https://dblp.org/img/n.png)

\[c43\]
[Yucong Peng](https://dblp.org/pid/187/1548.html), [Peng Zhou](https://dblp.org/pid/23/5823.html), [Hao Zheng](https://dblp.org/pid/31/6916.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Wankou Yang:

Multilinear Local Fisher Discriminant Analysis for Face Recognition. [CCBR2016](https://dblp.org/db/conf/ccbr/ccbr2016.html#conf/ccbr/PengZZZY16): 130-138
- ![](https://dblp.org/img/n.png)

\[c42\]
[Peng Zhou](https://dblp.org/pid/23/5823.html), [Yucong Peng](https://dblp.org/pid/187/1548.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Wankou Yang:

Local Dual-Cross Ternary Pattern for Feature Representation. [CCBR2016](https://dblp.org/db/conf/ccbr/ccbr2016.html#conf/ccbr/ZhouPSZY16): 600-608
- ![](https://dblp.org/img/n.png)

\[c41\]
[Lei Ju](https://dblp.org/pid/97/3791-5.html), [Ke Xie](https://dblp.org/pid/44/2171-4.html), [Hao Zheng](https://dblp.org/pid/31/6916.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Wankou Yang:

GPCA-SIFT: A New Local Feature Descriptor for Scene Image Classification. [CCPR (2)2016](https://dblp.org/db/conf/ccpr/ccpr2016-2.html#conf/ccpr/JuXZZY16): 286-295
- ![](https://dblp.org/img/n.png)

\[c40\]
[Shiwei Shi](https://dblp.org/pid/187/9158.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html), [Xin Zuo](https://dblp.org/pid/15/2278.html), Wankou Yang:

A Novel Discriminative Weighted Pooling Feature for Multi-view Face Detection. [CCPR (1)2016](https://dblp.org/db/conf/ccpr/ccpr2016-1.html#conf/ccpr/ShiSZY16): 437-448
- ![](https://dblp.org/img/n.png)

\[i2\]
[Biyun Sheng](https://dblp.org/pid/158/1357.html), [Chunhua Shen](https://dblp.org/pid/56/1673.html), [Guosheng Lin](https://dblp.org/pid/126/4778.html), [Jun Li](https://dblp.org/pid/116/1011-33.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Crowd Counting via Weighted VLAD on Dense Attribute Feature Maps. [CoRRabs/1604.08660](https://dblp.org/db/journals/corr/corr1604.html#journals/corr/ShengSLLYS16) (2016)
- ![](https://dblp.org/img/n.png)

\[i1\]
[Feng Liu](https://dblp.org/pid/77/1318-36.html), [Tao Xiang](https://dblp.org/pid/22/4460-2.html), [Timothy M. Hospedales](https://dblp.org/pid/32/3545.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Semantic Regularisation for Recurrent Image Annotation. [CoRRabs/1611.05490](https://dblp.org/db/journals/corr/corr1611.html#journals/corr/LiuXHYS16) (2016)
- 2015
- ![](https://dblp.org/img/n.png)

\[j28\]
[Xiaoyong Yan](https://dblp.org/pid/70/8665.html), [Aiguo Song](https://dblp.org/pid/21/1796.html), [Zhong Yang](https://dblp.org/pid/46/2248.html), Wankou Yang:

An improved multihop-based localization algorithm for wireless sensor network using learning approach. [Comput. Electr. Eng.48](https://dblp.org/db/journals/cee/cee48.html#journals/cee/YanSYY15): 247-257 (2015)
- ![](https://dblp.org/img/n.png)

\[j27\]
[Hoangvu Nguyen](https://dblp.org/pid/160/2774.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Fumin Shen](https://dblp.org/pid/92/10934.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Kernel Low-Rank Representation for face recognition. [Neurocomputing155](https://dblp.org/db/journals/ijon/ijon155.html#journals/ijon/NguyenYSS15): 32-42 (2015)
- ![](https://dblp.org/img/n.png)

\[j26\]
[Biyun Sheng](https://dblp.org/pid/158/1357.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Action recognition using direction-dependent feature pairs and non-negative low rank sparse model. [Neurocomputing158](https://dblp.org/db/journals/ijon/ijon158.html#journals/ijon/ShengYS15): 73-80 (2015)
- ![](https://dblp.org/img/n.png)

\[j25\]
[Jian Dong](https://dblp.org/pid/58/3444.html), [Changyin Sun](https://dblp.org/pid/64/221.html), Wankou Yang:

A supervised dictionary learning and discriminative weighting model for action recognition. [Neurocomputing158](https://dblp.org/db/journals/ijon/ijon158.html#journals/ijon/DongSY15): 246-256 (2015)
- ![](https://dblp.org/img/n.png)

\[j24\]
[Hualong Yu](https://dblp.org/pid/13/4009.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changyin Sun](https://dblp.org/pid/64/221.html), Wankou Yang, [Xibei Yang](https://dblp.org/pid/53/779.html), [Xin Zuo](https://dblp.org/pid/15/2278.html):

AL-ELM: One uncertainty-based active learning algorithm using extreme learning machine. [Neurocomputing166](https://dblp.org/db/journals/ijon/ijon166.html#journals/ijon/YuSYYZ15): 140-150 (2015)
- ![](https://dblp.org/img/n.png)

\[j23\]
[Hualong Yu](https://dblp.org/pid/13/4009.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chaoxu Mu](https://dblp.org/pid/11/6606.html), [Changyin Sun](https://dblp.org/pid/64/221.html), Wankou Yang, [Xibei Yang](https://dblp.org/pid/53/779.html), [Xin Zuo](https://dblp.org/pid/15/2278.html):

Support vector machine-based optimized decision threshold adjustment strategy for classifying imbalanced data. [Knowl. Based Syst.76](https://dblp.org/db/journals/kbs/kbs76.html#journals/kbs/YuMSYYZ15): 67-78 (2015)
- ![](https://dblp.org/img/n.png)

\[j22\]
[Zhenyu Wang](https://dblp.org/pid/22/1486.html), Wankou Yang, [Xianye Ben](https://dblp.org/pid/96/10791.html):

Low-resolution degradation face recognition over long distance based on CCA. [Neural Comput. Appl.26(7)](https://dblp.org/db/journals/nca/nca26.html#journals/nca/WangYB15): 1645-1652 (2015)
- ![](https://dblp.org/img/n.png)

\[j21\]
Wankou Yang, [Zhenyu Wang](https://dblp.org/pid/22/1486.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

A collaborative representation based projections method for feature extraction. [Pattern Recognit.48(1)](https://dblp.org/db/journals/pr/pr48.html#journals/pr/YangWS15): 20-27 (2015)
- ![](https://dblp.org/img/n.png)

\[c39\]
[Hoangvu Nguyen](https://dblp.org/pid/160/2774.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Transposed discriminative low-rank representation for face recognition. [ACPR2015](https://dblp.org/db/conf/acpr/acpr2015.html#conf/acpr/NguyenYS15): 191-195
- ![](https://dblp.org/img/n.png)

\[c38\]
[Yun Yang](https://dblp.org/pid/90/3406.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Linlin Yang](https://dblp.org/pid/84/6484.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), Wankou Yang:

Action recognition using completed local binary patterns and multiple-class boosting classifier. [ACPR2015](https://dblp.org/db/conf/acpr/acpr2015.html#conf/acpr/YangZYCY15): 336-340
- ![](https://dblp.org/img/n.png)

\[c37\]
[Chen Chen](https://dblp.org/pid/65/4423-1.html), [Junjun Jiang](https://dblp.org/pid/119/0230.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Wankou Yang, [Jianzhong Guo](https://dblp.org/pid/99/4475.html):

Hyperspectral image classification using Gradient Local Auto-Correlations. [ACPR2015](https://dblp.org/db/conf/acpr/acpr2015.html#conf/acpr/ChenJZYG15): 454-458
- ![](https://dblp.org/img/n.png)

\[c36\]
[Linlin Yang](https://dblp.org/pid/84/6484.html), [Dandan Du](https://dblp.org/pid/150/4075.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Wankou Yang:

A Panoramic Video System Based on Exposure Adjustment and Non-linear Fusion. [CCBR2015](https://dblp.org/db/conf/ccbr/ccbr2015.html#conf/ccbr/YangDZY15): 499-507
- ![](https://dblp.org/img/n.png)

\[c35\]
[Lei Wang](https://dblp.org/pid/w/LeiWang18.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Wankou Yang:

Boosting-Like Deep Convolutional Network for Pedestrian Detection. [CCBR2015](https://dblp.org/db/conf/ccbr/ccbr2015.html#conf/ccbr/WangZY15): 581-588
- ![](https://dblp.org/img/n.png)

\[c34\]
[Feng Liu](https://dblp.org/pid/77/1318-36.html), [Yongzhen Huang](https://dblp.org/pid/11/753.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

High-level spatial modeling in convolutional neural network with application to pedestrian detection. [CCECE2015](https://dblp.org/db/conf/ccece/ccece2015.html#conf/ccece/LiuHYS15): 778-783
- ![](https://dblp.org/img/n.png)

\[c33\]
[Jiayu Sheng](https://dblp.org/pid/169/4623.html), [Biyun Sheng](https://dblp.org/pid/158/1357.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Assigning PLS Based Descriptors by SVM in Action Recognition. [IScIDE (1)2015](https://dblp.org/db/conf/iscide/iscide2015-1.html#conf/iscide/ShengSYS15): 145-153
- ![](https://dblp.org/img/n.png)

\[c32\]
[Jinhua Liu](https://dblp.org/pid/09/7129.html), [Hualong Yu](https://dblp.org/pid/13/4009.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Combining Active Learning and Semi-Supervised Learning Based on Extreme Learning Machine for Multi-class Image Classification. [IScIDE (1)2015](https://dblp.org/db/conf/iscide/iscide2015-1.html#conf/iscide/LiuYYS15): 163-175
- ![](https://dblp.org/img/n.png)

\[c31\]
[Dandan Zhao](https://dblp.org/pid/72/7814.html), [Changyin Sun](https://dblp.org/pid/64/221.html), [Qingling Wang](https://dblp.org/pid/61/4797.html)![](https://dblp.org/img/orcid-mark.12x12.png), Wankou Yang:

Neural Network Based PID Control for Quadrotor Aircraft. [IScIDE (2)2015](https://dblp.org/db/conf/iscide/iscide2015-2.html#conf/iscide/ZhaoSWY15): 287-297
- ![](https://dblp.org/img/n.png)

\[c30\]
[Mingxing Zhang](https://dblp.org/pid/153/5382.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fumin Shen](https://dblp.org/pid/92/10934.html), [Hanwang Zhang](https://dblp.org/pid/79/8116.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ning Xie](https://dblp.org/pid/55/4104-3.html), Wankou Yang:

Hashing with Inductive Supervised Learning. [PCM (2)2015](https://dblp.org/db/conf/pcm/pcm2015-2.html#conf/pcm/ZhangSZXY15): 447-455
- 2014
- ![](https://dblp.org/img/n.png)

\[j20\]
[Feng Liu](https://dblp.org/pid/77/1318-36.html), [Yongzhen Huang](https://dblp.org/pid/11/753.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Spatial modeling via feature co-pooling and SG grafting. [Neurocomputing139](https://dblp.org/db/journals/ijon/ijon139.html#journals/ijon/LiuHWYS14): 415-422 (2014)
- ![](https://dblp.org/img/n.png)

\[j19\]
Wankou Yang, [Karl Ricanek](https://dblp.org/pid/39/609.html), [Fumin Shen](https://dblp.org/pid/92/10934.html):

Image classification using local linear regression. [Neural Comput. Appl.25(7-8)](https://dblp.org/db/journals/nca/nca25.html#journals/nca/YangRS14): 1913-1920 (2014)
- ![](https://dblp.org/img/n.png)

\[j18\]
[Haoran Wang](https://dblp.org/pid/28/3021-1.html), [Chunfeng Yuan](https://dblp.org/pid/47/2506.html), [Weiming Hu](https://dblp.org/pid/41/6824-4.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Action Recognition Using Nonnegative Action Component Representation and Sparse Basis Selection. [IEEE Trans. Image Process.23(2)](https://dblp.org/db/journals/tip/tip23.html#journals/tip/WangYHLYS14): 570-581 (2014)
- ![](https://dblp.org/img/n.png)

\[c29\]
[Biyun Sheng](https://dblp.org/pid/158/1357.html), Wankou Yang, [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

A Non-negative Low Rank and Sparse Model for Action Recognition. [CCPR (2)2014](https://dblp.org/db/conf/ccpr/ccpr2014-2.html#conf/ccpr/ShengYZS14): 266-275
- ![](https://dblp.org/img/n.png)

\[c28\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), [Xin Zuo](https://dblp.org/pid/15/2278.html), Wankou Yang, [Guohai Liu](https://dblp.org/pid/34/1121.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Real-Time Human Detection Based on Optimized Integrated Channel Features. [CCPR (2)2014](https://dblp.org/db/conf/ccpr/ccpr2014-2.html#conf/ccpr/ShenZYL14): 286-295
- 2013
- ![](https://dblp.org/img/n.png)

\[j17\]
Wankou Yang, [Zhenyu Wang](https://dblp.org/pid/22/1486.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Changyin Sun](https://dblp.org/pid/64/221.html), [Karl Ricanek](https://dblp.org/pid/39/609.html):

Image classification using kernel collaborative representation with regularized least square. [Appl. Math. Comput.222](https://dblp.org/db/journals/amc/amc222.html#journals/amc/YangWYSR13): 13-28 (2013)
- ![](https://dblp.org/img/n.png)

\[j16\]
[Jianguo Wang](https://dblp.org/pid/64/1071-2.html), Wankou Yang, [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

Face recognition using fuzzy maximum scatter discriminant analysis. [Neural Comput. Appl.23(3-4)](https://dblp.org/db/journals/nca/nca23.html#journals/nca/WangYY13): 957-964 (2013)
- ![](https://dblp.org/img/n.png)

\[j15\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Real-time human detection based on gentle MILBoost with variable granularity HOG-CSLBP. [Neural Comput. Appl.23(7-8)](https://dblp.org/db/journals/nca/nca23.html#journals/nca/ShenYS13): 1937-1948 (2013)
- ![](https://dblp.org/img/n.png)

\[c27\]
[Rong Huang](https://dblp.org/pid/92/6101-9.html), [Lian Zhu](https://dblp.org/pid/95/7051.html), Wankou Yang, [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

An Improved Adaptive Weighted LTP Algorithm for Face Recognition Based on Single Training Sample. [CCBR2013](https://dblp.org/db/conf/ccbr/ccbr2013.html#conf/ccbr/HuangZYZS13): 9-15
- ![](https://dblp.org/img/n.png)

\[c26\]
[Zhenyu Wang](https://dblp.org/pid/22/1486.html), Wankou Yang, [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Kernel Collaborative Representation with Regularized Least Square for Face Recognition. [CCBR2013](https://dblp.org/db/conf/ccbr/ccbr2013.html#conf/ccbr/WangYYS13): 130-137
- ![](https://dblp.org/img/n.png)

\[c25\]
[Lian Zhu](https://dblp.org/pid/95/7051.html), [Rong Huang](https://dblp.org/pid/92/6101-9.html), [Xinfu Ye](https://dblp.org/pid/138/2054.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

GPCA on Gabor Tensor for Face Recognition. [IScIDE2013](https://dblp.org/db/conf/iscide/iscide2013.html#conf/iscide/ZhuHYYS13): 344-350
- ![](https://dblp.org/img/n.png)

\[c24\]
[Feng Liu](https://dblp.org/pid/77/1318-36.html), [Yongzhen Huang](https://dblp.org/pid/11/753.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), Wankou Yang:

Boosting Deformable Part Model by Sample Sharing and Outlier Ablation. [IScIDE2013](https://dblp.org/db/conf/iscide/iscide2013.html#conf/iscide/LiuHWY13): 418-426
- ![](https://dblp.org/img/n.png)

\[c23\]
[Jian Dong](https://dblp.org/pid/58/3444.html), [Changyin Sun](https://dblp.org/pid/64/221.html), Wankou Yang:

An Improved Method for Oriented Chamfer Matching. [IScIDE2013](https://dblp.org/db/conf/iscide/iscide2013.html#conf/iscide/DongSY13): 875-879
- ![](https://dblp.org/img/n.png)

\[e1\]
[Changyin Sun](https://dblp.org/pid/64/221.html), [Fang Fang](https://dblp.org/pid/74/3719.html), [Zhi-Hua Zhou](https://dblp.org/pid/z/ZhiHuaZhou.html), Wankou Yang, [Zhiyong Liu](https://dblp.org/pid/16/5205.html):

Intelligence Science and Big Data Engineering - 4th International Conference, IScIDE 2013, Beijing, China, July 31 - August 2, 2013, Revised Selected Papers. [Lecture Notes in Computer Science](https://dblp.org/db/series/lncs/index.html) 8261, Springer2013, ISBN 978-3-642-42056-6 [\[contents\]](https://dblp.org/db/conf/iscide/iscide2013.html)
- 2012
- ![](https://dblp.org/img/n.png)

\[j14\]
[Jun Yin](https://dblp.org/pid/58/5423-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhonghua Liu](https://dblp.org/pid/42/876.html), [Zhong Jin](https://dblp.org/pid/24/5268.html), Wankou Yang:

Kernel sparse representation based classification. [Neurocomputing77(1)](https://dblp.org/db/journals/ijon/ijon77.html#journals/ijon/YinLJY12): 120-128 (2012)
- ![](https://dblp.org/img/n.png)

\[j13\]
Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Karl Ricanek](https://dblp.org/pid/39/609.html):

Sequential Row-Column 2DPCA for face recognition. [Neural Comput. Appl.21(7)](https://dblp.org/db/journals/nca/nca21.html#journals/nca/YangSR12): 1729-1735 (2012)
- ![](https://dblp.org/img/n.png)

\[j12\]
[Zhongxi Sun](https://dblp.org/pid/39/9614.html), [Changyin Sun](https://dblp.org/pid/64/221.html), Wankou Yang, [Jifeng Shen](https://dblp.org/pid/23/8615.html):

Feature extraction using 2DIFDA with fuzzy membership. [Soft Comput.16(10)](https://dblp.org/db/journals/soco/soco16.html#journals/soco/SunSYS12): 1783-1793 (2012)
- ![](https://dblp.org/img/n.png)

\[c22\]
Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Qingshan Liu](https://dblp.org/pid/181/2731-2.html), [Karl Ricanek](https://dblp.org/pid/39/609.html):

Collaborative Representation Based Projections for Face Recognition. [CCPR2012](https://dblp.org/db/conf/ccpr/ccpr2012.html#conf/ccpr/YangSLR12): 276-283
- ![](https://dblp.org/img/n.png)

\[c21\]
[Xiaobo Chen](https://dblp.org/pid/21/4778-1.html), [Jian Yang](https://dblp.org/pid/y/JianYang3.html), Wankou Yang:

Large margin null space discriminant analysis with applications to face recognition. [ICPR2012](https://dblp.org/db/conf/icpr/icpr2012.html#conf/icpr/ChenYY12): 1679-1682
- ![](https://dblp.org/img/n.png)

\[c20\]
[Karl Ricanek](https://dblp.org/pid/39/609.html), [Amrutha Sethuram](https://dblp.org/pid/72/233.html), Wankou Yang:

Face Registration: Evaluating Generative Models for Automatic Dense Landmarking of the Face. [IScIDE2012](https://dblp.org/db/conf/iscide/iscide2012.html#conf/iscide/RicanekSY12): 206-215
- ![](https://dblp.org/img/n.png)

\[c19\]
[Lian Zhu](https://dblp.org/pid/95/7051.html), [Yan Zhang](https://dblp.org/pid/04/3348.html), [Changyin Sun](https://dblp.org/pid/64/221.html), Wankou Yang:

Face Recognition with Multi-scale Block Local Ternary Patterns. [IScIDE2012](https://dblp.org/db/conf/iscide/iscide2012.html#conf/iscide/ZhuZSY12): 216-222
- ![](https://dblp.org/img/n.png)

\[c18\]
[Qiuping Pan](https://dblp.org/pid/125/5176.html), [Jifeng Shen](https://dblp.org/pid/23/8615.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Ensemble Haar and MB-LBP Features for License Plate Detection. [IScIDE2012](https://dblp.org/db/conf/iscide/iscide2012.html#conf/iscide/PanSYS12): 223-230
- ![](https://dblp.org/img/n.png)

\[c17\]
[Ting Zhao](https://dblp.org/pid/34/528.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

A Fast Vanishing Point Detection Method in Structured Road. [IScIDE2012](https://dblp.org/db/conf/iscide/iscide2012.html#conf/iscide/ZhaoYS12): 372-379
- ![](https://dblp.org/img/n.png)

\[c16\]
[Xianye Ben](https://dblp.org/pid/96/10791.html), Wankou Yang, [Hongyuan Wang](https://dblp.org/pid/17/203.html), [Shengdi Wang](https://dblp.org/pid/125/5067.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Performance Analysis of Matrix Gait Recognition under Linear Interpolation Framework. [IScIDE2012](https://dblp.org/db/conf/iscide/iscide2012.html#conf/iscide/BenYWW12): 711-718
- ![](https://dblp.org/img/n.png)

\[c15\]
[Zhe Chen](https://dblp.org/pid/06/4240.html), [Yan Zhang](https://dblp.org/pid/04/3348.html), [Changyin Sun](https://dblp.org/pid/64/221.html), Wankou Yang:

Fusing Discrete Cosine Transform and Multi-level Center-Symmetric Local Binary Pattern Features for Periocular Recognition. [IScIDE2012](https://dblp.org/db/conf/iscide/iscide2012.html#conf/iscide/ChenZSY12): 810-816
- 2011
- ![](https://dblp.org/img/n.png)

\[j11\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), [Changyin Sun](https://dblp.org/pid/64/221.html), Wankou Yang, [Zhenyu Wang](https://dblp.org/pid/22/1486.html), [Zhongxi Sun](https://dblp.org/pid/39/9614.html):

A novel distribution-based feature for rapid object detection. [Neurocomputing74(17)](https://dblp.org/db/journals/ijon/ijon74.html#journals/ijon/ShenSYWS11): 2767-2779 (2011)
- ![](https://dblp.org/img/n.png)

\[j10\]
Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Helen S. Du](https://dblp.org/pid/65/5702.html), [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

Feature Extraction Using Laplacian Maximum Margin Criterion. [Neural Process. Lett.33(1)](https://dblp.org/db/journals/npl/npl33.html#journals/npl/YangSDY11): 99-110 (2011)
- ![](https://dblp.org/img/n.png)

\[j9\]
Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Jingyu Yang](https://dblp.org/pid/65/2850-1.html), [Helen S. Du](https://dblp.org/pid/65/5702.html), [Karl Ricanek](https://dblp.org/pid/39/609.html):

Face Recognition Using Kernel UDP. [Neural Process. Lett.34(2)](https://dblp.org/db/journals/npl/npl34.html#journals/npl/YangSYDR11): 177-192 (2011)
- ![](https://dblp.org/img/n.png)

\[j8\]
Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Lei Zhang](https://dblp.org/pid/64/5666-6.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A multi-manifold discriminant analysis method for image feature extraction. [Pattern Recognit.44(8)](https://dblp.org/db/journals/pr/pr44.html#journals/pr/YangSZ11): 1649-1657 (2011)
- ![](https://dblp.org/img/n.png)

\[c14\]
[Cuixian Chen](https://dblp.org/pid/06/9606.html), Wankou Yang, [Yishi Wang](https://dblp.org/pid/15/9606.html), [Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Karl Ricanek](https://dblp.org/pid/39/609.html):

Learning Gabor Features for Facial Age Estimation. [CCBR2011](https://dblp.org/db/conf/ccbr/ccbr2011.html#conf/ccbr/ChenYWSR11): 204-213
- ![](https://dblp.org/img/n.png)

\[c13\]
Wankou Yang, [Cuixian Chen](https://dblp.org/pid/06/9606.html), [Karl Ricanek](https://dblp.org/pid/39/609.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Gender Classification via Global-Local Features Fusion. [CCBR2011](https://dblp.org/db/conf/ccbr/ccbr2011.html#conf/ccbr/YangCRS11): 214-220
- ![](https://dblp.org/img/n.png)

\[c12\]
[Cuixian Chen](https://dblp.org/pid/06/9606.html), Wankou Yang, [Yishi Wang](https://dblp.org/pid/15/9606.html), [Karl Ricanek](https://dblp.org/pid/39/609.html), [Khoa Luu](https://dblp.org/pid/43/8092.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Facial feature fusion and model selection for age estimation. [FG2011](https://dblp.org/db/conf/fgr/fg2011.html#conf/fgr/ChenYWRL11): 200-205
- ![](https://dblp.org/img/n.png)

\[c11\]
Wankou Yang, [Cuixian Chen](https://dblp.org/pid/06/9606.html), [Karl Ricanek](https://dblp.org/pid/39/609.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Ensemble of Global and Local Features for Face Age Estimation. [ISNN (2)2011](https://dblp.org/db/conf/isnn/isnn2011-2.html#conf/isnn/YangCRS11): 251-259
- ![](https://dblp.org/img/n.png)

\[c10\]
[Ming Xiong](https://dblp.org/pid/x/MingXiong.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Finger-Knuckle-Print Recognition Using LGBP. [ISNN (2)2011](https://dblp.org/db/conf/isnn/isnn2011-2.html#conf/isnn/XiongYS11): 270-277
- ![](https://dblp.org/img/n.png)

\[c9\]
Wankou Yang, [Amrutha Sethuram](https://dblp.org/pid/72/233.html), [Eric Patterson](https://dblp.org/pid/79/1282.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Karl Ricanek](https://dblp.org/pid/39/609.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Gender Classification Using the Profile. [ISNN (2)2011](https://dblp.org/db/conf/isnn/isnn2011-2.html#conf/isnn/YangSPRS11): 288-295
- ![](https://dblp.org/img/n.png)

\[c8\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), [Changyin Sun](https://dblp.org/pid/64/221.html), Wankou Yang, [Zhongxi Sun](https://dblp.org/pid/39/9614.html):

Fast Human Detection Based on Enhanced Variable Size HOG Features. [ISNN (2)2011](https://dblp.org/db/conf/isnn/isnn2011-2.html#conf/isnn/ShenSYS11): 342-349
- 2010
- ![](https://dblp.org/img/n.png)

\[j7\]
Wankou Yang, [Xiaoyong Yan](https://dblp.org/pid/70/8665.html), [Lei Zhang](https://dblp.org/pid/64/5666-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changyin Sun](https://dblp.org/pid/64/221.html):

Feature extraction based on fuzzy 2DLDA. [Neurocomputing73(10-12)](https://dblp.org/db/journals/ijon/ijon73.html#journals/ijon/YangYZS10): 1556-1561 (2010)
- ![](https://dblp.org/img/n.png)

\[j6\]
Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Lei Zhang](https://dblp.org/pid/64/5666-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Karl Ricanek](https://dblp.org/pid/39/609.html):

Laplacian bidirectional PCA for face recognition. [Neurocomputing74(1-3)](https://dblp.org/db/journals/ijon/ijon74.html#journals/ijon/YangSZR10): 487-493 (2010)
- ![](https://dblp.org/img/n.png)

\[c7\]
Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html), [Lei Zhang](https://dblp.org/pid/64/5666-6.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Face Recognition Using a Multi-manifold Discriminant Analysis Method. [ICPR2010](https://dblp.org/db/conf/icpr/icpr2010.html#conf/icpr/YangSZ10): 527-530
- ![](https://dblp.org/img/n.png)

\[c6\]
[Jifeng Shen](https://dblp.org/pid/23/8615.html), Wankou Yang, [Changyin Sun](https://dblp.org/pid/64/221.html):

Learning Discriminative Features Based on Distribution. [ICPR2010](https://dblp.org/db/conf/icpr/icpr2010.html#conf/icpr/ShenYS10): 1401-1404
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2009
- ![](https://dblp.org/img/n.png)

\[j5\]
Wankou Yang, [Jianguo Wang](https://dblp.org/pid/64/1071-2.html), [Mingwu Ren](https://dblp.org/pid/84/5438.html), [Lei Zhang](https://dblp.org/pid/64/5666-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

Feature extraction using fuzzy inverse FDA. [Neurocomputing72(13-15)](https://dblp.org/db/journals/ijon/ijon72.html#journals/ijon/YangWRZY09): 3384-3390 (2009)
- ![](https://dblp.org/img/n.png)

\[j4\]
Wankou Yang, [Jianguo Wang](https://dblp.org/pid/64/1071-2.html), [Mingwu Ren](https://dblp.org/pid/84/5438.html), [Jingyu Yang](https://dblp.org/pid/65/2850-1.html), [Lei Zhang](https://dblp.org/pid/64/5666-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guanghai Liu](https://dblp.org/pid/41/7381.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Feature extraction based on Laplacian bidirectional maximum margin criterion. [Pattern Recognit.42(11)](https://dblp.org/db/journals/pr/pr42.html#journals/pr/YangWRYZL09): 2327-2334 (2009)
- ![](https://dblp.org/img/n.png)

\[c5\]
[Hui Yan](https://dblp.org/pid/95/4747.html), Wankou Yang, [Jian Yang](https://dblp.org/pid/y/JianYang3.html), [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

Discriminant feature extraction based on center distance. [ICIP2009](https://dblp.org/db/conf/icip/icip2009.html#conf/icip/YanYYY09): 1249-1252
- 2008
- ![](https://dblp.org/img/n.png)

\[j3\]
[Jianguo Wang](https://dblp.org/pid/64/1071-2.html), Wankou Yang, [Yusheng Lin](https://dblp.org/pid/87/4635.html), [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

Two-directional maximum scatter difference discriminant analysis for face recognition. [Neurocomputing72(1-3)](https://dblp.org/db/journals/ijon/ijon72.html#journals/ijon/WangYLY08): 352-358 (2008)
- ![](https://dblp.org/img/n.png)

\[j2\]
[Jianguo Wang](https://dblp.org/pid/64/1071-2.html), [Yusheng Lin](https://dblp.org/pid/87/4635.html), Wankou Yang, [Jing-yu Yang](https://dblp.org/pid/65/2850-1.html):

Kernel maximum scatter difference based feature extraction and its application to face recognition. [Pattern Recognit. Lett.29(13)](https://dblp.org/db/journals/prl/prl29.html#journals/prl/WangLYY08): 1832-1835 (2008)
- ![](https://dblp.org/img/n.png)

\[c4\]
[Jianguo Wang](https://dblp.org/pid/64/1071-2.html), Wankou Yang, [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

Fuzzy maximum scatter discriminant analysis and its application to face recognition. [ICPR2008](https://dblp.org/db/conf/icpr/icpr2008.html#conf/icpr/WangYY08): 1-4
- ![](https://dblp.org/img/n.png)

\[c3\]
Wankou Yang, [Jianguo Wang](https://dblp.org/pid/64/1071-2.html), [Mingwu Ren](https://dblp.org/pid/84/5438.html), [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

Feature Extraction base on Local Maximum Margin Criterion. [ICPR2008](https://dblp.org/db/conf/icpr/icpr2008.html#conf/icpr/YangWRY08): 1-4
- ![](https://dblp.org/img/n.png)

\[c2\]
Wankou Yang, [Hui Yan](https://dblp.org/pid/95/4747.html), [Jianguo Wang](https://dblp.org/pid/64/1071-2.html), [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

Face recognition using Complete Fuzzy LDA. [ICPR2008](https://dblp.org/db/conf/icpr/icpr2008.html#conf/icpr/YangYWY08): 1-4
- 2006
- ![](https://dblp.org/img/n.png)

\[c1\]
[Qiong Wang](https://dblp.org/pid/65/3144-3.html), Wankou Yang, [Huan Wang](https://dblp.org/pid/70/6155-13.html), [Jing-Yu Yang](https://dblp.org/pid/65/2850-1.html), [Yu-Jie Zheng](https://dblp.org/pid/49/5016.html):

Face Detection Using Binary Template Matching and SVM. [PRICAI2006](https://dblp.org/db/conf/pricai/pricai2006.html#conf/pricai/WangYWYZ06): 1237-1241
- 2005
- ![](https://dblp.org/img/n.png)

\[j1\]
[Mingwu Ren](https://dblp.org/pid/84/5438.html), Wankou Yang, [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

A new and fast contour-filling algorithm. [Pattern Recognit.38(12)](https://dblp.org/db/journals/pr/pr38.html#journals/pr/RenYY05): 2564-2577 (2005)
- _no results_

automatic loading of the coauthor graph disabled due to its size.

**click here to**
**load the graph.**

Note that this feature is _work in progress_ and that it is still far from being perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/99/3602.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[2](https://dblp.org/pid/99/3602.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiemi Bai](https://dblp.org/pid/276/3622.html)

[\[c60\]](https://dblp.org/pid/99/3602.html#c60)

[3](https://dblp.org/pid/99/3602.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yiping Bao](https://dblp.org/pid/235/2626.html)

[\[i11\]](https://dblp.org/pid/99/3602.html#i11)

[4](https://dblp.org/pid/99/3602.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Kang Ben](https://dblp.org/pid/340/0959.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[5](https://dblp.org/pid/99/3602.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xianye Ben](https://dblp.org/pid/96/10791.html)

[\[j30\]](https://dblp.org/pid/99/3602.html#j30) [\[j22\]](https://dblp.org/pid/99/3602.html#j22) [\[c16\]](https://dblp.org/pid/99/3602.html#c16)

[6](https://dblp.org/pid/99/3602.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[7](https://dblp.org/pid/99/3602.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Johanna Björklund](https://dblp.org/pid/75/5525.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[8](https://dblp.org/pid/99/3602.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dingding Cai](https://dblp.org/pid/198/1127.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[9](https://dblp.org/pid/99/3602.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wenxiao Cai](https://dblp.org/pid/348/4892.html)

[\[j144\]](https://dblp.org/pid/99/3602.html#j144) [\[j138\]](https://dblp.org/pid/99/3602.html#j138) [\[c86\]](https://dblp.org/pid/99/3602.html#c86) [\[c83\]](https://dblp.org/pid/99/3602.html#c83) [\[i46\]](https://dblp.org/pid/99/3602.html#i46) [\[i43\]](https://dblp.org/pid/99/3602.html#i43) [\[i34\]](https://dblp.org/pid/99/3602.html#i34) [\[i33\]](https://dblp.org/pid/99/3602.html#i33) [\[i29\]](https://dblp.org/pid/99/3602.html#i29) [\[j105\]](https://dblp.org/pid/99/3602.html#j105) [\[i24\]](https://dblp.org/pid/99/3602.html#i24)

[10](https://dblp.org/pid/99/3602.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yunfei Cai](https://dblp.org/pid/172/2636.html)

[\[c59\]](https://dblp.org/pid/99/3602.html#c59) [\[j60\]](https://dblp.org/pid/99/3602.html#j60)

[11](https://dblp.org/pid/99/3602.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ziyun Cai](https://dblp.org/pid/179/6081.html)

[\[j101\]](https://dblp.org/pid/99/3602.html#j101)

[12](https://dblp.org/pid/99/3602.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tongtong Cao](https://dblp.org/pid/229/5950.html)

[\[c77\]](https://dblp.org/pid/99/3602.html#c77) [\[i22\]](https://dblp.org/pid/99/3602.html#i22)

[13](https://dblp.org/pid/99/3602.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yue Cao 0001](https://dblp.org/pid/74/5570-1.html)

[\[j124\]](https://dblp.org/pid/99/3602.html#j124) [\[i35\]](https://dblp.org/pid/99/3602.html#i35) [\[c71\]](https://dblp.org/pid/99/3602.html#c71) [\[i18\]](https://dblp.org/pid/99/3602.html#i18)

[14](https://dblp.org/pid/99/3602.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[15](https://dblp.org/pid/99/3602.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Llukman Cerkezi](https://dblp.org/pid/208/1312.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[16](https://dblp.org/pid/99/3602.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hakan Çevikalp](https://dblp.org/pid/14/6210.html)

aka: Hakan Cevikalp

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[17](https://dblp.org/pid/99/3602.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hong Chang 0001](https://dblp.org/pid/02/2689-1.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[18](https://dblp.org/pid/99/3602.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[19](https://dblp.org/pid/99/3602.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chen Chen 0001](https://dblp.org/pid/65/4423-1.html)

[\[c51\]](https://dblp.org/pid/99/3602.html#c51) [\[c38\]](https://dblp.org/pid/99/3602.html#c38) [\[c37\]](https://dblp.org/pid/99/3602.html#c37)

[20](https://dblp.org/pid/99/3602.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Cuixian Chen](https://dblp.org/pid/06/9606.html)

[\[c14\]](https://dblp.org/pid/99/3602.html#c14) [\[c13\]](https://dblp.org/pid/99/3602.html#c13) [\[c12\]](https://dblp.org/pid/99/3602.html#c12) [\[c11\]](https://dblp.org/pid/99/3602.html#c11)

[21](https://dblp.org/pid/99/3602.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ding Chen](https://dblp.org/pid/78/3806.html)

[\[j110\]](https://dblp.org/pid/99/3602.html#j110)

[22](https://dblp.org/pid/99/3602.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guangqi Chen](https://dblp.org/pid/178/8116.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[23](https://dblp.org/pid/99/3602.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guoqing Chen](https://dblp.org/pid/87/4902.html)

[\[j92\]](https://dblp.org/pid/99/3602.html#j92)

[24](https://dblp.org/pid/99/3602.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiahao Chen](https://dblp.org/pid/149/2661.html)

[\[j141\]](https://dblp.org/pid/99/3602.html#j141)

[25](https://dblp.org/pid/99/3602.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiaye Chen](https://dblp.org/pid/116/2901.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[26](https://dblp.org/pid/99/3602.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lineng Chen](https://dblp.org/pid/230/6597.html)

[\[j115\]](https://dblp.org/pid/99/3602.html#j115) [\[j97\]](https://dblp.org/pid/99/3602.html#j97)

[27](https://dblp.org/pid/99/3602.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qipeng Chen](https://dblp.org/pid/134/5036.html)

[\[j88\]](https://dblp.org/pid/99/3602.html#j88)

[28](https://dblp.org/pid/99/3602.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[29](https://dblp.org/pid/99/3602.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaobo Chen 0001](https://dblp.org/pid/21/4778-1.html)

[\[j84\]](https://dblp.org/pid/99/3602.html#j84) [\[c21\]](https://dblp.org/pid/99/3602.html#c21)

[30](https://dblp.org/pid/99/3602.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xilin Chen 0001](https://dblp.org/pid/c/XilinChen.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[31](https://dblp.org/pid/99/3602.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[32](https://dblp.org/pid/99/3602.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiuyi Chen](https://dblp.org/pid/218/7190.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[33](https://dblp.org/pid/99/3602.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yang Chen 0008](https://dblp.org/pid/48/4792-8.html)

[\[j50\]](https://dblp.org/pid/99/3602.html#j50)

[34](https://dblp.org/pid/99/3602.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yifei Chen](https://dblp.org/pid/75/5017.html)

[\[j130\]](https://dblp.org/pid/99/3602.html#j130) [\[j123\]](https://dblp.org/pid/99/3602.html#j123) [\[i23\]](https://dblp.org/pid/99/3602.html#i23) [\[j95\]](https://dblp.org/pid/99/3602.html#j95)

[35](https://dblp.org/pid/99/3602.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yiwei Chen](https://dblp.org/pid/28/2965.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[36](https://dblp.org/pid/99/3602.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yu-Hsi Chen](https://dblp.org/pid/127/3933.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[37](https://dblp.org/pid/99/3602.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ze Chen](https://dblp.org/pid/15/4184.html)

[\[i11\]](https://dblp.org/pid/99/3602.html#i11)

[38](https://dblp.org/pid/99/3602.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhe Chen](https://dblp.org/pid/06/4240.html)

[\[c15\]](https://dblp.org/pid/99/3602.html#c15)

[39](https://dblp.org/pid/99/3602.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhixing Chen](https://dblp.org/pid/62/3074.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[40](https://dblp.org/pid/99/3602.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ziwei Chen](https://dblp.org/pid/219/9605.html)

[\[c74\]](https://dblp.org/pid/99/3602.html#c74) [\[c68\]](https://dblp.org/pid/99/3602.html#c68) [\[i12\]](https://dblp.org/pid/99/3602.html#i12)

[41](https://dblp.org/pid/99/3602.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Miao Cheng](https://dblp.org/pid/79/7377.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[42](https://dblp.org/pid/99/3602.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wenxuan Cheng](https://dblp.org/pid/370/2615.html)

[\[j146\]](https://dblp.org/pid/99/3602.html#j146) [\[j141\]](https://dblp.org/pid/99/3602.html#j141) [\[i43\]](https://dblp.org/pid/99/3602.html#i43) [\[i41\]](https://dblp.org/pid/99/3602.html#i41) [\[i39\]](https://dblp.org/pid/99/3602.html#i39)

[43](https://dblp.org/pid/99/3602.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yangming Cheng](https://dblp.org/pid/340/1285.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[44](https://dblp.org/pid/99/3602.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zinan Cheng](https://dblp.org/pid/358/1002.html)

[\[j133\]](https://dblp.org/pid/99/3602.html#j133) [\[j127\]](https://dblp.org/pid/99/3602.html#j127) [\[c81\]](https://dblp.org/pid/99/3602.html#c81)

[45](https://dblp.org/pid/99/3602.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ziyi Cheng](https://dblp.org/pid/290/9342.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[46](https://dblp.org/pid/99/3602.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yu-Chen Chiu](https://dblp.org/pid/199/2494.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[47](https://dblp.org/pid/99/3602.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lei Chu](https://dblp.org/pid/168/2875.html)

[\[j124\]](https://dblp.org/pid/99/3602.html#j124) [\[i35\]](https://dblp.org/pid/99/3602.html#i35)

[48](https://dblp.org/pid/99/3602.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Angelo Ciaramella](https://dblp.org/pid/37/6845.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[49](https://dblp.org/pid/99/3602.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ozgun Cirakman](https://dblp.org/pid/86/8843.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[50](https://dblp.org/pid/99/3602.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[51](https://dblp.org/pid/99/3602.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[52](https://dblp.org/pid/99/3602.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhen Cui 0001](https://dblp.org/pid/59/8491-1.html)

[\[j108\]](https://dblp.org/pid/99/3602.html#j108) [\[j87\]](https://dblp.org/pid/99/3602.html#j87) [\[j54\]](https://dblp.org/pid/99/3602.html#j54) [\[i7\]](https://dblp.org/pid/99/3602.html#i7)

[53](https://dblp.org/pid/99/3602.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Kenan Dai](https://dblp.org/pid/250/4445.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[54](https://dblp.org/pid/99/3602.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ming Dai](https://dblp.org/pid/61/6981.html)

[\[j146\]](https://dblp.org/pid/99/3602.html#j146) [\[j145\]](https://dblp.org/pid/99/3602.html#j145) [\[j141\]](https://dblp.org/pid/99/3602.html#j141) [\[c85\]](https://dblp.org/pid/99/3602.html#c85) [\[c82\]](https://dblp.org/pid/99/3602.html#c82) [\[i47\]](https://dblp.org/pid/99/3602.html#i47) [\[i46\]](https://dblp.org/pid/99/3602.html#i46) [\[i43\]](https://dblp.org/pid/99/3602.html#i43) [\[i41\]](https://dblp.org/pid/99/3602.html#i41) [\[i39\]](https://dblp.org/pid/99/3602.html#i39) [\[i38\]](https://dblp.org/pid/99/3602.html#i38) [\[j125\]](https://dblp.org/pid/99/3602.html#j125) [\[j120\]](https://dblp.org/pid/99/3602.html#j120) [\[j116\]](https://dblp.org/pid/99/3602.html#j116) [\[c79\]](https://dblp.org/pid/99/3602.html#c79) [\[i30\]](https://dblp.org/pid/99/3602.html#i30)

[55](https://dblp.org/pid/99/3602.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[56](https://dblp.org/pid/99/3602.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[57](https://dblp.org/pid/99/3602.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiankang Deng](https://dblp.org/pid/156/7808.html)

[\[j144\]](https://dblp.org/pid/99/3602.html#j144) [\[i29\]](https://dblp.org/pid/99/3602.html#i29)

[58](https://dblp.org/pid/99/3602.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[59](https://dblp.org/pid/99/3602.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tiansheng Deng](https://dblp.org/pid/391/3535.html)

[\[j92\]](https://dblp.org/pid/99/3602.html#j92)

[60](https://dblp.org/pid/99/3602.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Debajyoti Dhar](https://dblp.org/pid/128/3182.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[61](https://dblp.org/pid/99/3602.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shangzhe Di](https://dblp.org/pid/304/1344.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[62](https://dblp.org/pid/99/3602.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Weiping Ding 0001](https://dblp.org/pid/133/0292-1.html)

[\[j111\]](https://dblp.org/pid/99/3602.html#j111)

[63](https://dblp.org/pid/99/3602.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hao Dong 0003](https://dblp.org/pid/14/1525-3.html)

[\[c83\]](https://dblp.org/pid/99/3602.html#c83) [\[i33\]](https://dblp.org/pid/99/3602.html#i33)

[64](https://dblp.org/pid/99/3602.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jian Dong](https://dblp.org/pid/58/3444.html)

[\[j79\]](https://dblp.org/pid/99/3602.html#j79) [\[j25\]](https://dblp.org/pid/99/3602.html#j25) [\[c23\]](https://dblp.org/pid/99/3602.html#c23)

[65](https://dblp.org/pid/99/3602.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lu Dong 0002](https://dblp.org/pid/40/2448-2.html)

[\[c47\]](https://dblp.org/pid/99/3602.html#c47)

[66](https://dblp.org/pid/99/3602.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shaohua Dong](https://dblp.org/pid/188/4523.html)

[\[j149\]](https://dblp.org/pid/99/3602.html#j149) [\[i42\]](https://dblp.org/pid/99/3602.html#i42)

[67](https://dblp.org/pid/99/3602.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xingping Dong](https://dblp.org/pid/156/3020.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[68](https://dblp.org/pid/99/3602.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhengchao Dong](https://dblp.org/pid/61/9409.html)

[\[c46\]](https://dblp.org/pid/99/3602.html#c46)

[69](https://dblp.org/pid/99/3602.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[70](https://dblp.org/pid/99/3602.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dandan Du](https://dblp.org/pid/150/4075.html)

[\[c36\]](https://dblp.org/pid/99/3602.html#c36)

[71](https://dblp.org/pid/99/3602.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[72](https://dblp.org/pid/99/3602.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Helen S. Du](https://dblp.org/pid/65/5702.html)

[\[j10\]](https://dblp.org/pid/99/3602.html#j10) [\[j9\]](https://dblp.org/pid/99/3602.html#j9)

[73](https://dblp.org/pid/99/3602.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Songlin Du](https://dblp.org/pid/154/7687.html)

[\[j105\]](https://dblp.org/pid/99/3602.html#j105)

[74](https://dblp.org/pid/99/3602.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Boqiang Duan](https://dblp.org/pid/309/8582.html)

[\[i38\]](https://dblp.org/pid/99/3602.html#i38) [\[i36\]](https://dblp.org/pid/99/3602.html#i36)

[75](https://dblp.org/pid/99/3602.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Siyao Duan](https://dblp.org/pid/331/7006.html)

[\[j126\]](https://dblp.org/pid/99/3602.html#j126)

[76](https://dblp.org/pid/99/3602.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[77](https://dblp.org/pid/99/3602.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Benjamin Dzubur](https://dblp.org/pid/340/1520.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[78](https://dblp.org/pid/99/3602.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Krista A. Ehinger](https://dblp.org/pid/13/8654.html)

[\[j51\]](https://dblp.org/pid/99/3602.html#j51) [\[c44\]](https://dblp.org/pid/99/3602.html#c44)

[79](https://dblp.org/pid/99/3602.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Duyao Fan](https://dblp.org/pid/276/3634.html)

[\[c59\]](https://dblp.org/pid/99/3602.html#c59)

[80](https://dblp.org/pid/99/3602.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Heng Fan 0001](https://dblp.org/pid/20/10120-1.html)

[\[j142\]](https://dblp.org/pid/99/3602.html#j142) [\[i40\]](https://dblp.org/pid/99/3602.html#i40) [\[j130\]](https://dblp.org/pid/99/3602.html#j130) [\[j123\]](https://dblp.org/pid/99/3602.html#j123) [\[j122\]](https://dblp.org/pid/99/3602.html#j122) [\[i23\]](https://dblp.org/pid/99/3602.html#i23) [\[i19\]](https://dblp.org/pid/99/3602.html#i19) [\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[81](https://dblp.org/pid/99/3602.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xijian Fan](https://dblp.org/pid/166/8478.html)

[\[j84\]](https://dblp.org/pid/99/3602.html#j84)

[82](https://dblp.org/pid/99/3602.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Fang Fang](https://dblp.org/pid/74/3719.html)

[\[e1\]](https://dblp.org/pid/99/3602.html#e1)

[83](https://dblp.org/pid/99/3602.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shixiong Fang](https://dblp.org/pid/205/8118.html)

[\[j51\]](https://dblp.org/pid/99/3602.html#j51) [\[c44\]](https://dblp.org/pid/99/3602.html#c44)

[84](https://dblp.org/pid/99/3602.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[85](https://dblp.org/pid/99/3602.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ze Feng](https://dblp.org/pid/12/5914.html)

[\[j143\]](https://dblp.org/pid/99/3602.html#j143) [\[i44\]](https://dblp.org/pid/99/3602.html#i44) [\[i36\]](https://dblp.org/pid/99/3602.html#i36) [\[j99\]](https://dblp.org/pid/99/3602.html#j99)

[86](https://dblp.org/pid/99/3602.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[j146\]](https://dblp.org/pid/99/3602.html#j146) [\[j141\]](https://dblp.org/pid/99/3602.html#j141) [\[i41\]](https://dblp.org/pid/99/3602.html#i41) [\[i39\]](https://dblp.org/pid/99/3602.html#i39) [\[j116\]](https://dblp.org/pid/99/3602.html#j116) [\[j114\]](https://dblp.org/pid/99/3602.html#j114) [\[c79\]](https://dblp.org/pid/99/3602.html#c79) [\[i30\]](https://dblp.org/pid/99/3602.html#i30) [\[j98\]](https://dblp.org/pid/99/3602.html#j98) [\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c67\]](https://dblp.org/pid/99/3602.html#c67) [\[c61\]](https://dblp.org/pid/99/3602.html#c61) [\[i16\]](https://dblp.org/pid/99/3602.html#i16)

[87](https://dblp.org/pid/99/3602.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhiyong Feng 0001](https://dblp.org/pid/48/195-1.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[88](https://dblp.org/pid/99/3602.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[89](https://dblp.org/pid/99/3602.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Huan Fu](https://dblp.org/pid/139/8082.html)

[\[j144\]](https://dblp.org/pid/99/3602.html#j144) [\[i29\]](https://dblp.org/pid/99/3602.html#i29)

[90](https://dblp.org/pid/99/3602.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Liyong Fu](https://dblp.org/pid/155/9293.html)

[\[j89\]](https://dblp.org/pid/99/3602.html#j89) [\[j85\]](https://dblp.org/pid/99/3602.html#j85) [\[j84\]](https://dblp.org/pid/99/3602.html#j84) [\[j53\]](https://dblp.org/pid/99/3602.html#j53)

[91](https://dblp.org/pid/99/3602.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[92](https://dblp.org/pid/99/3602.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhikang Fu](https://dblp.org/pid/169/4639.html)

[\[j92\]](https://dblp.org/pid/99/3602.html#j92)

[93](https://dblp.org/pid/99/3602.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guangwei Gao](https://dblp.org/pid/118/3484.html)

[\[j72\]](https://dblp.org/pid/99/3602.html#j72) [\[j41\]](https://dblp.org/pid/99/3602.html#j41) [\[c50\]](https://dblp.org/pid/99/3602.html#c50)

[94](https://dblp.org/pid/99/3602.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hao Gao 0005](https://dblp.org/pid/69/8912-5.html)

[\[j72\]](https://dblp.org/pid/99/3602.html#j72)

[95](https://dblp.org/pid/99/3602.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shang Gao 0012](https://dblp.org/pid/28/435-12.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[96](https://dblp.org/pid/99/3602.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shiming Ge](https://dblp.org/pid/93/8104.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[97](https://dblp.org/pid/99/3602.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Mingming Gong](https://dblp.org/pid/98/8479.html)

[\[j144\]](https://dblp.org/pid/99/3602.html#j144) [\[i29\]](https://dblp.org/pid/99/3602.html#i29) [\[j35\]](https://dblp.org/pid/99/3602.html#j35)

[98](https://dblp.org/pid/99/3602.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[99](https://dblp.org/pid/99/3602.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[100](https://dblp.org/pid/99/3602.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Eric Granger](https://dblp.org/pid/86/2306.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[101](https://dblp.org/pid/99/3602.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Q. H. Gu](https://dblp.org/pid/340/1209.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[102](https://dblp.org/pid/99/3602.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yifan Gu](https://dblp.org/pid/167/3881.html)

[\[j64\]](https://dblp.org/pid/99/3602.html#j64)

[103](https://dblp.org/pid/99/3602.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yuzhang Gu](https://dblp.org/pid/122/3790.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[104](https://dblp.org/pid/99/3602.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bilge Günsel](https://dblp.org/pid/47/5125.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[105](https://dblp.org/pid/99/3602.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Cong Guo](https://dblp.org/pid/117/1754.html)

[\[j138\]](https://dblp.org/pid/99/3602.html#j138) [\[i24\]](https://dblp.org/pid/99/3602.html#i24)

[106](https://dblp.org/pid/99/3602.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jianzhong Guo](https://dblp.org/pid/99/4475.html)

[\[c37\]](https://dblp.org/pid/99/3602.html#c37)

[107](https://dblp.org/pid/99/3602.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jingming Guo](https://dblp.org/pid/174/3127.html)

[\[c77\]](https://dblp.org/pid/99/3602.html#c77) [\[i22\]](https://dblp.org/pid/99/3602.html#i22)

[108](https://dblp.org/pid/99/3602.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qing Guo 0005](https://dblp.org/pid/25/3038-5.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[109](https://dblp.org/pid/99/3602.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Teng Guo 0003](https://dblp.org/pid/94/11139-3.html)

[\[j122\]](https://dblp.org/pid/99/3602.html#j122) [\[i19\]](https://dblp.org/pid/99/3602.html#i19)

[110](https://dblp.org/pid/99/3602.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Weili Guo](https://dblp.org/pid/146/8424.html)

[\[c44\]](https://dblp.org/pid/99/3602.html#c44)

[111](https://dblp.org/pid/99/3602.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Himanshu Gupta 0003](https://dblp.org/pid/330/0760-3.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[112](https://dblp.org/pid/99/3602.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Filiz Gurkan](https://dblp.org/pid/202/7040.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[113](https://dblp.org/pid/99/3602.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Gustav Häger](https://dblp.org/pid/157/3602.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[114](https://dblp.org/pid/99/3602.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bo Han 0003](https://dblp.org/pid/241/0472-3.html)

[\[j113\]](https://dblp.org/pid/99/3602.html#j113) [\[i26\]](https://dblp.org/pid/99/3602.html#i26)

[115](https://dblp.org/pid/99/3602.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jungong Han](https://dblp.org/pid/98/6127.html)

[\[j68\]](https://dblp.org/pid/99/3602.html#j68) [\[c51\]](https://dblp.org/pid/99/3602.html#c51)

[116](https://dblp.org/pid/99/3602.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Junwei Han 0001](https://dblp.org/pid/00/3003.html)

[\[j69\]](https://dblp.org/pid/99/3602.html#j69)

[117](https://dblp.org/pid/99/3602.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wencheng Han](https://dblp.org/pid/280/3348.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[118](https://dblp.org/pid/99/3602.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jianfeng He](https://dblp.org/pid/93/8352.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[119](https://dblp.org/pid/99/3602.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Keji He](https://dblp.org/pid/319/4518.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[120](https://dblp.org/pid/99/3602.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yonggui He](https://dblp.org/pid/187/6203.html)

[\[c56\]](https://dblp.org/pid/99/3602.html#c56)

[121](https://dblp.org/pid/99/3602.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wen Heng](https://dblp.org/pid/201/7460.html)

[\[c73\]](https://dblp.org/pid/99/3602.html#c73) [\[i27\]](https://dblp.org/pid/99/3602.html#i27)

[122](https://dblp.org/pid/99/3602.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Timothy M. Hospedales](https://dblp.org/pid/32/3545.html)

[\[j71\]](https://dblp.org/pid/99/3602.html#j71) [\[c54\]](https://dblp.org/pid/99/3602.html#c54) [\[i6\]](https://dblp.org/pid/99/3602.html#i6) [\[c48\]](https://dblp.org/pid/99/3602.html#c48) [\[i3\]](https://dblp.org/pid/99/3602.html#i3) [\[i1\]](https://dblp.org/pid/99/3602.html#i1)

[123](https://dblp.org/pid/99/3602.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jinyan Hou](https://dblp.org/pid/348/4547.html)

[\[j138\]](https://dblp.org/pid/99/3602.html#j138) [\[i24\]](https://dblp.org/pid/99/3602.html#i24)

[124](https://dblp.org/pid/99/3602.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bingwen Hu](https://dblp.org/pid/215/8072.html)

[\[j77\]](https://dblp.org/pid/99/3602.html#j77)

[125](https://dblp.org/pid/99/3602.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Changhui Hu 0001](https://dblp.org/pid/31/7616-1.html)

aka: Chang-Hui Hu 0001

[\[j101\]](https://dblp.org/pid/99/3602.html#j101) [\[j96\]](https://dblp.org/pid/99/3602.html#j96)

[126](https://dblp.org/pid/99/3602.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dongting Hu](https://dblp.org/pid/159/6788.html)

[\[j144\]](https://dblp.org/pid/99/3602.html#j144) [\[i29\]](https://dblp.org/pid/99/3602.html#i29)

[127](https://dblp.org/pid/99/3602.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Junjie Hu 0003](https://dblp.org/pid/123/0773-3.html)

[\[j134\]](https://dblp.org/pid/99/3602.html#j134)

[128](https://dblp.org/pid/99/3602.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qichang Hu](https://dblp.org/pid/169/9980.html)

[\[j46\]](https://dblp.org/pid/99/3602.html#j46)

[129](https://dblp.org/pid/99/3602.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Weiming Hu 0004](https://dblp.org/pid/41/6824-4.html)

[\[j47\]](https://dblp.org/pid/99/3602.html#j47) [\[j18\]](https://dblp.org/pid/99/3602.html#j18)

[130](https://dblp.org/pid/99/3602.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xian-Sheng Hua 0001](https://dblp.org/pid/56/5807-1.html)

[\[c53\]](https://dblp.org/pid/99/3602.html#c53) [\[i4\]](https://dblp.org/pid/99/3602.html#i4)

[131](https://dblp.org/pid/99/3602.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Peng Huang](https://dblp.org/pid/29/1726.html)

[\[j85\]](https://dblp.org/pid/99/3602.html#j85)

[132](https://dblp.org/pid/99/3602.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Pu Huang](https://dblp.org/pid/51/3775.html)

[\[c59\]](https://dblp.org/pid/99/3602.html#c59) [\[j60\]](https://dblp.org/pid/99/3602.html#j60) [\[c55\]](https://dblp.org/pid/99/3602.html#c55) [\[c50\]](https://dblp.org/pid/99/3602.html#c50)

[133](https://dblp.org/pid/99/3602.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Rong Huang 0009](https://dblp.org/pid/92/6101-9.html)

[\[c27\]](https://dblp.org/pid/99/3602.html#c27) [\[c25\]](https://dblp.org/pid/99/3602.html#c25)

[134](https://dblp.org/pid/99/3602.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yan Huang 0008](https://dblp.org/pid/75/6434-8.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[135](https://dblp.org/pid/99/3602.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yanyan Huang](https://dblp.org/pid/88/4316.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[136](https://dblp.org/pid/99/3602.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yongming Huang 0002](https://dblp.org/pid/385/3909-2.html)

[\[j91\]](https://dblp.org/pid/99/3602.html#j91)

[137](https://dblp.org/pid/99/3602.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yongzhen Huang](https://dblp.org/pid/11/753.html)

[\[c34\]](https://dblp.org/pid/99/3602.html#c34) [\[j20\]](https://dblp.org/pid/99/3602.html#j20) [\[c24\]](https://dblp.org/pid/99/3602.html#c24)

[138](https://dblp.org/pid/99/3602.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Deepak Jangid](https://dblp.org/pid/340/1460.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[139](https://dblp.org/pid/99/3602.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[140](https://dblp.org/pid/99/3602.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[141](https://dblp.org/pid/99/3602.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Suli Ji](https://dblp.org/pid/150/4045.html)

[\[j39\]](https://dblp.org/pid/99/3602.html#j39)

[142](https://dblp.org/pid/99/3602.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[143](https://dblp.org/pid/99/3602.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chenyi Jiang](https://dblp.org/pid/132/7866.html)

[\[j129\]](https://dblp.org/pid/99/3602.html#j129)

[144](https://dblp.org/pid/99/3602.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiaran Jiang](https://dblp.org/pid/402/5383.html)

[\[j136\]](https://dblp.org/pid/99/3602.html#j136) [\[i45\]](https://dblp.org/pid/99/3602.html#i45)

[145](https://dblp.org/pid/99/3602.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Junjun Jiang](https://dblp.org/pid/119/0230.html)

[\[c37\]](https://dblp.org/pid/99/3602.html#c37)

[146](https://dblp.org/pid/99/3602.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Longyu Jiang](https://dblp.org/pid/69/10291.html)

[\[j50\]](https://dblp.org/pid/99/3602.html#j50)

[147](https://dblp.org/pid/99/3602.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tengping Jiang](https://dblp.org/pid/270/8012.html)

[\[i25\]](https://dblp.org/pid/99/3602.html#i25)

[148](https://dblp.org/pid/99/3602.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wen Jiang](https://dblp.org/pid/37/6235.html)

[\[c78\]](https://dblp.org/pid/99/3602.html#c78)

[149](https://dblp.org/pid/99/3602.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[150](https://dblp.org/pid/99/3602.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ke Jin](https://dblp.org/pid/94/2193.html)

[\[j138\]](https://dblp.org/pid/99/3602.html#j138) [\[c72\]](https://dblp.org/pid/99/3602.html#c72) [\[i24\]](https://dblp.org/pid/99/3602.html#i24) [\[i20\]](https://dblp.org/pid/99/3602.html#i20)

[151](https://dblp.org/pid/99/3602.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shuangping Jin](https://dblp.org/pid/283/5840.html)

[\[c67\]](https://dblp.org/pid/99/3602.html#c67) [\[c66\]](https://dblp.org/pid/99/3602.html#c66) [\[i16\]](https://dblp.org/pid/99/3602.html#i16)

[152](https://dblp.org/pid/99/3602.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xin Jin 0014](https://dblp.org/pid/68/3340-14.html)

[\[i25\]](https://dblp.org/pid/99/3602.html#i25)

[153](https://dblp.org/pid/99/3602.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhong Jin](https://dblp.org/pid/24/5268.html)

[\[j14\]](https://dblp.org/pid/99/3602.html#j14)

[154](https://dblp.org/pid/99/3602.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaoyuan Jing](https://dblp.org/pid/59/1365.html)

aka: Xiao-Yuan Jing

[\[j96\]](https://dblp.org/pid/99/3602.html#j96) [\[j41\]](https://dblp.org/pid/99/3602.html#j41)

[155](https://dblp.org/pid/99/3602.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lei Ju 0005](https://dblp.org/pid/97/3791-5.html)

[\[j98\]](https://dblp.org/pid/99/3602.html#j98) [\[c41\]](https://dblp.org/pid/99/3602.html#c41)

[156](https://dblp.org/pid/99/3602.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[157](https://dblp.org/pid/99/3602.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Marcus Kalander](https://dblp.org/pid/256/9291.html)

[\[i26\]](https://dblp.org/pid/99/3602.html#i26)

[158](https://dblp.org/pid/99/3602.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[159](https://dblp.org/pid/99/3602.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ze Kang](https://dblp.org/pid/340/1063.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[160](https://dblp.org/pid/99/3602.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jani Käpylä](https://dblp.org/pid/244/2529.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[161](https://dblp.org/pid/99/3602.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiao Ke](https://dblp.org/pid/78/9040.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[162](https://dblp.org/pid/99/3602.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[163](https://dblp.org/pid/99/3602.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Pritee Khanna](https://dblp.org/pid/75/3036.html)

[\[j59\]](https://dblp.org/pid/99/3602.html#j59)

[164](https://dblp.org/pid/99/3602.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Byeong Hak Kim](https://dblp.org/pid/214/8978.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[165](https://dblp.org/pid/99/3602.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Madhu Kiran](https://dblp.org/pid/39/10281.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[166](https://dblp.org/pid/99/3602.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[j98\]](https://dblp.org/pid/99/3602.html#j98) [\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c67\]](https://dblp.org/pid/99/3602.html#c67) [\[c61\]](https://dblp.org/pid/99/3602.html#c61) [\[i16\]](https://dblp.org/pid/99/3602.html#i16)

[167](https://dblp.org/pid/99/3602.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hui Kong 0001](https://dblp.org/pid/94/1836-1.html)

[\[j132\]](https://dblp.org/pid/99/3602.html#j132) [\[j115\]](https://dblp.org/pid/99/3602.html#j115) [\[j97\]](https://dblp.org/pid/99/3602.html#j97)

[168](https://dblp.org/pid/99/3602.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Youyong Kong](https://dblp.org/pid/154/7641.html)

[\[j50\]](https://dblp.org/pid/99/3602.html#j50)

[169](https://dblp.org/pid/99/3602.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[170](https://dblp.org/pid/99/3602.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Worapan Kusakunniran](https://dblp.org/pid/05/7576.html)

[\[j78\]](https://dblp.org/pid/99/3602.html#j78)

[171](https://dblp.org/pid/99/3602.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Simiao Lai](https://dblp.org/pid/282/1954.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[172](https://dblp.org/pid/99/3602.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[173](https://dblp.org/pid/99/3602.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[174](https://dblp.org/pid/99/3602.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dongwook Lee](https://dblp.org/pid/25/6543.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[175](https://dblp.org/pid/99/3602.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hyunjeong Lee](https://dblp.org/pid/00/3423.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[176](https://dblp.org/pid/99/3602.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jun Ha Lee](https://dblp.org/pid/260/2774.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[177](https://dblp.org/pid/99/3602.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Seohyung Lee](https://dblp.org/pid/210/4662.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[178](https://dblp.org/pid/99/3602.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[179](https://dblp.org/pid/99/3602.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[180](https://dblp.org/pid/99/3602.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bin Li 0006](https://dblp.org/pid/89/6764-6.html)

[\[j82\]](https://dblp.org/pid/99/3602.html#j82)

[181](https://dblp.org/pid/99/3602.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bin Li 0085](https://dblp.org/pid/89/6764-85.html)

[\[j117\]](https://dblp.org/pid/99/3602.html#j117)

[182](https://dblp.org/pid/99/3602.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ce Li 0002](https://dblp.org/pid/58/411-2.html)

[\[j58\]](https://dblp.org/pid/99/3602.html#j58)

[183](https://dblp.org/pid/99/3602.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hanxi Li](https://dblp.org/pid/21/5003.html)

[\[j32\]](https://dblp.org/pid/99/3602.html#j32)

[184](https://dblp.org/pid/99/3602.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hong Li](https://dblp.org/pid/93/6234.html)

[\[j83\]](https://dblp.org/pid/99/3602.html#j83)

[185](https://dblp.org/pid/99/3602.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[186](https://dblp.org/pid/99/3602.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jian Li](https://dblp.org/pid/33/5448.html)

[\[c85\]](https://dblp.org/pid/99/3602.html#c85) [\[i47\]](https://dblp.org/pid/99/3602.html#i47)

[187](https://dblp.org/pid/99/3602.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jianhua Li](https://dblp.org/pid/93/3389.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[188](https://dblp.org/pid/99/3602.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jie Li 0040](https://dblp.org/pid/17/2703-40.html)

[\[j147\]](https://dblp.org/pid/99/3602.html#j147)

[189](https://dblp.org/pid/99/3602.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jin Li 0028](https://dblp.org/pid/48/1097-28.html)

[\[j82\]](https://dblp.org/pid/99/3602.html#j82)

[190](https://dblp.org/pid/99/3602.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jun Li](https://dblp.org/pid/116/1011.html)

[\[j73\]](https://dblp.org/pid/99/3602.html#j73)

[191](https://dblp.org/pid/99/3602.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jun Li 0011](https://dblp.org/pid/l/JunLi11.html)

[\[j74\]](https://dblp.org/pid/99/3602.html#j74)

[192](https://dblp.org/pid/99/3602.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jun Li 0033](https://dblp.org/pid/116/1011-33.html)

[\[j142\]](https://dblp.org/pid/99/3602.html#j142) [\[i40\]](https://dblp.org/pid/99/3602.html#i40) [\[j102\]](https://dblp.org/pid/99/3602.html#j102) [\[i28\]](https://dblp.org/pid/99/3602.html#i28) [\[j95\]](https://dblp.org/pid/99/3602.html#j95) [\[j94\]](https://dblp.org/pid/99/3602.html#j94) [\[j92\]](https://dblp.org/pid/99/3602.html#j92) [\[j81\]](https://dblp.org/pid/99/3602.html#j81) [\[j80\]](https://dblp.org/pid/99/3602.html#j80) [\[j76\]](https://dblp.org/pid/99/3602.html#j76) [\[j75\]](https://dblp.org/pid/99/3602.html#j75) [\[j69\]](https://dblp.org/pid/99/3602.html#j69) [\[j67\]](https://dblp.org/pid/99/3602.html#j67) [\[j57\]](https://dblp.org/pid/99/3602.html#j57) [\[j55\]](https://dblp.org/pid/99/3602.html#j55) [\[j52\]](https://dblp.org/pid/99/3602.html#j52) [\[j48\]](https://dblp.org/pid/99/3602.html#j48) [\[c52\]](https://dblp.org/pid/99/3602.html#c52) [\[i5\]](https://dblp.org/pid/99/3602.html#i5) [\[j46\]](https://dblp.org/pid/99/3602.html#j46) [\[j45\]](https://dblp.org/pid/99/3602.html#j45) [\[j42\]](https://dblp.org/pid/99/3602.html#j42) [\[j40\]](https://dblp.org/pid/99/3602.html#j40) [\[c47\]](https://dblp.org/pid/99/3602.html#c47) [\[j35\]](https://dblp.org/pid/99/3602.html#j35) [\[i2\]](https://dblp.org/pid/99/3602.html#i2)

[193](https://dblp.org/pid/99/3602.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Li Li](https://dblp.org/pid/53/2189.html)

[\[j39\]](https://dblp.org/pid/99/3602.html#j39)

[194](https://dblp.org/pid/99/3602.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lunbo Li](https://dblp.org/pid/188/6062.html)

[\[j93\]](https://dblp.org/pid/99/3602.html#j93)

[195](https://dblp.org/pid/99/3602.html?view=joint&param=195 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ming Li 0010](https://dblp.org/pid/l/MingLi10.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[196](https://dblp.org/pid/99/3602.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qiang Li 0024](https://dblp.org/pid/72/872-24.html)

[\[j121\]](https://dblp.org/pid/99/3602.html#j121) [\[j100\]](https://dblp.org/pid/99/3602.html#j100) [\[c74\]](https://dblp.org/pid/99/3602.html#c74)

[197](https://dblp.org/pid/99/3602.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qun Li 0002](https://dblp.org/pid/42/6066-2.html)

[\[j69\]](https://dblp.org/pid/99/3602.html#j69)

[198](https://dblp.org/pid/99/3602.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Suyi Li 0005](https://dblp.org/pid/98/7732-5.html)

[\[j129\]](https://dblp.org/pid/99/3602.html#j129)

[199](https://dblp.org/pid/99/3602.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tao Li](https://dblp.org/pid/75/4601.html)

[\[j126\]](https://dblp.org/pid/99/3602.html#j126)

[200](https://dblp.org/pid/99/3602.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tianhuang Li](https://dblp.org/pid/247/4712.html)

[\[j61\]](https://dblp.org/pid/99/3602.html#j61)

[201](https://dblp.org/pid/99/3602.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wangkai Li](https://dblp.org/pid/340/1456.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[202](https://dblp.org/pid/99/3602.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xi Li 0001](https://dblp.org/pid/46/2311-1.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[203](https://dblp.org/pid/99/3602.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiang Li 0041](https://dblp.org/pid/40/1491-41.html)

[\[j145\]](https://dblp.org/pid/99/3602.html#j145) [\[c76\]](https://dblp.org/pid/99/3602.html#c76) [\[i21\]](https://dblp.org/pid/99/3602.html#i21)

[204](https://dblp.org/pid/99/3602.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[205](https://dblp.org/pid/99/3602.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiao Li](https://dblp.org/pid/66/2069.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[206](https://dblp.org/pid/99/3602.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaofan Li](https://dblp.org/pid/50/3937.html)

[\[c84\]](https://dblp.org/pid/99/3602.html#c84) [\[i44\]](https://dblp.org/pid/99/3602.html#i44) [\[i31\]](https://dblp.org/pid/99/3602.html#i31)

[207](https://dblp.org/pid/99/3602.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaoqi Li 0020](https://dblp.org/pid/357/1937.html)

[\[c83\]](https://dblp.org/pid/99/3602.html#c83) [\[i33\]](https://dblp.org/pid/99/3602.html#i33)

[208](https://dblp.org/pid/99/3602.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiong Li 0002](https://dblp.org/pid/63/6031-2.html)

[\[j59\]](https://dblp.org/pid/99/3602.html#j59)

[209](https://dblp.org/pid/99/3602.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xuelian Li](https://dblp.org/pid/85/7695.html)

[\[j66\]](https://dblp.org/pid/99/3602.html#j66)

[210](https://dblp.org/pid/99/3602.html?view=joint&param=210 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yanjie Li](https://dblp.org/pid/70/4538.html)

[\[j99\]](https://dblp.org/pid/99/3602.html#j99) [\[c70\]](https://dblp.org/pid/99/3602.html#c70) [\[c65\]](https://dblp.org/pid/99/3602.html#c65) [\[i14\]](https://dblp.org/pid/99/3602.html#i14) [\[i13\]](https://dblp.org/pid/99/3602.html#i13) [\[i11\]](https://dblp.org/pid/99/3602.html#i11)

[211](https://dblp.org/pid/99/3602.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yingpeng Li](https://dblp.org/pid/388/6664.html)

[\[j147\]](https://dblp.org/pid/99/3602.html#j147)

[212](https://dblp.org/pid/99/3602.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yuezhou Li](https://dblp.org/pid/284/2562.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[213](https://dblp.org/pid/99/3602.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yun Li 0010](https://dblp.org/pid/87/6284-10.html)

[\[j82\]](https://dblp.org/pid/99/3602.html#j82)

[214](https://dblp.org/pid/99/3602.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zechao Li](https://dblp.org/pid/51/8693.html)

[\[j84\]](https://dblp.org/pid/99/3602.html#j84) [\[j53\]](https://dblp.org/pid/99/3602.html#j53)

[215](https://dblp.org/pid/99/3602.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhe Li 0008](https://dblp.org/pid/11/751-8.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[216](https://dblp.org/pid/99/3602.html?view=joint&param=216 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ziyu Li](https://dblp.org/pid/177/3057.html)

[\[j134\]](https://dblp.org/pid/99/3602.html#j134) [\[j114\]](https://dblp.org/pid/99/3602.html#j114) [\[j106\]](https://dblp.org/pid/99/3602.html#j106) [\[c77\]](https://dblp.org/pid/99/3602.html#c77) [\[i22\]](https://dblp.org/pid/99/3602.html#i22) [\[j86\]](https://dblp.org/pid/99/3602.html#j86) [\[i15\]](https://dblp.org/pid/99/3602.html#i15) [\[j75\]](https://dblp.org/pid/99/3602.html#j75) [\[c57\]](https://dblp.org/pid/99/3602.html#c57)

[217](https://dblp.org/pid/99/3602.html?view=joint&param=217 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiajun Liang](https://dblp.org/pid/184/6428.html)

[\[j135\]](https://dblp.org/pid/99/3602.html#j135)

[218](https://dblp.org/pid/99/3602.html?view=joint&param=218 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guosheng Lin](https://dblp.org/pid/126/4778.html)

[\[j48\]](https://dblp.org/pid/99/3602.html#j48) [\[i2\]](https://dblp.org/pid/99/3602.html#i2)

[219](https://dblp.org/pid/99/3602.html?view=joint&param=219 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Liting Lin](https://dblp.org/pid/227/2204.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[220](https://dblp.org/pid/99/3602.html?view=joint&param=220 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yusheng Lin](https://dblp.org/pid/87/4635.html)

[\[j3\]](https://dblp.org/pid/99/3602.html#j3) [\[j2\]](https://dblp.org/pid/99/3602.html#j2)

[221](https://dblp.org/pid/99/3602.html?view=joint&param=221 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhouchen Lin](https://dblp.org/pid/l/ZhouchenLin.html)

[\[j54\]](https://dblp.org/pid/99/3602.html#j54)

[222](https://dblp.org/pid/99/3602.html?view=joint&param=222 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Haibin Ling](https://dblp.org/pid/93/3488.html)

[\[j149\]](https://dblp.org/pid/99/3602.html#j149) [\[i42\]](https://dblp.org/pid/99/3602.html#i42) [\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[j57\]](https://dblp.org/pid/99/3602.html#j57) [\[j56\]](https://dblp.org/pid/99/3602.html#j56) [\[j49\]](https://dblp.org/pid/99/3602.html#j49) [\[j47\]](https://dblp.org/pid/99/3602.html#j47) [\[j42\]](https://dblp.org/pid/99/3602.html#j42) [\[j18\]](https://dblp.org/pid/99/3602.html#j18)

[223](https://dblp.org/pid/99/3602.html?view=joint&param=223 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bingbing Liu](https://dblp.org/pid/34/3868.html)

[\[c77\]](https://dblp.org/pid/99/3602.html#c77) [\[i22\]](https://dblp.org/pid/99/3602.html#i22)

[224](https://dblp.org/pid/99/3602.html?view=joint&param=224 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c63\]](https://dblp.org/pid/99/3602.html#c63) [\[c61\]](https://dblp.org/pid/99/3602.html#c61) [\[c58\]](https://dblp.org/pid/99/3602.html#c58) [\[i9\]](https://dblp.org/pid/99/3602.html#i9)

[225](https://dblp.org/pid/99/3602.html?view=joint&param=225 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[226](https://dblp.org/pid/99/3602.html?view=joint&param=226 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Feng Liu 0036](https://dblp.org/pid/77/1318-36.html)

[\[j71\]](https://dblp.org/pid/99/3602.html#j71) [\[c54\]](https://dblp.org/pid/99/3602.html#c54) [\[i6\]](https://dblp.org/pid/99/3602.html#i6) [\[c48\]](https://dblp.org/pid/99/3602.html#c48) [\[i3\]](https://dblp.org/pid/99/3602.html#i3) [\[i1\]](https://dblp.org/pid/99/3602.html#i1) [\[c34\]](https://dblp.org/pid/99/3602.html#c34) [\[j20\]](https://dblp.org/pid/99/3602.html#j20) [\[c24\]](https://dblp.org/pid/99/3602.html#c24)

[227](https://dblp.org/pid/99/3602.html?view=joint&param=227 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Gang Liu](https://dblp.org/pid/37/2109.html)

[\[c73\]](https://dblp.org/pid/99/3602.html#c73) [\[i27\]](https://dblp.org/pid/99/3602.html#i27)

[228](https://dblp.org/pid/99/3602.html?view=joint&param=228 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guanghai Liu 0001](https://dblp.org/pid/41/7381.html)

[\[j4\]](https://dblp.org/pid/99/3602.html#j4)

[229](https://dblp.org/pid/99/3602.html?view=joint&param=229 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guohai Liu](https://dblp.org/pid/34/1121.html)

[\[j36\]](https://dblp.org/pid/99/3602.html#j36) [\[c28\]](https://dblp.org/pid/99/3602.html#c28)

[230](https://dblp.org/pid/99/3602.html?view=joint&param=230 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hui Liu](https://dblp.org/pid/93/4010.html)

[\[j43\]](https://dblp.org/pid/99/3602.html#j43)

[231](https://dblp.org/pid/99/3602.html?view=joint&param=231 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiang-jiang Liu](https://dblp.org/pid/409/9085.html)

[\[i43\]](https://dblp.org/pid/99/3602.html#i43) [\[i41\]](https://dblp.org/pid/99/3602.html#i41) [\[i39\]](https://dblp.org/pid/99/3602.html#i39)

[232](https://dblp.org/pid/99/3602.html?view=joint&param=232 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiang-Jiang Liu 0001](https://dblp.org/pid/18/2542-1.html)

[\[j146\]](https://dblp.org/pid/99/3602.html#j146) [\[j143\]](https://dblp.org/pid/99/3602.html#j143) [\[c84\]](https://dblp.org/pid/99/3602.html#c84) [\[i44\]](https://dblp.org/pid/99/3602.html#i44) [\[i32\]](https://dblp.org/pid/99/3602.html#i32) [\[i31\]](https://dblp.org/pid/99/3602.html#i31)

[233](https://dblp.org/pid/99/3602.html?view=joint&param=233 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html)

[\[c51\]](https://dblp.org/pid/99/3602.html#c51)

[234](https://dblp.org/pid/99/3602.html?view=joint&param=234 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jingen Liu](https://dblp.org/pid/10/5849.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[235](https://dblp.org/pid/99/3602.html?view=joint&param=235 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jingren Liu](https://dblp.org/pid/269/7845.html)

[\[j140\]](https://dblp.org/pid/99/3602.html#j140) [\[j89\]](https://dblp.org/pid/99/3602.html#j89)

[236](https://dblp.org/pid/99/3602.html?view=joint&param=236 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jinhua Liu](https://dblp.org/pid/09/7129.html)

[\[c32\]](https://dblp.org/pid/99/3602.html#c32)

[237](https://dblp.org/pid/99/3602.html?view=joint&param=237 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Li Liu 0004](https://dblp.org/pid/33/4528-4.html)

[\[j93\]](https://dblp.org/pid/99/3602.html#j93) [\[j89\]](https://dblp.org/pid/99/3602.html#j89) [\[j64\]](https://dblp.org/pid/99/3602.html#j64)

[238](https://dblp.org/pid/99/3602.html?view=joint&param=238 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Li Liu 0036](https://dblp.org/pid/33/4528-36.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[239](https://dblp.org/pid/99/3602.html?view=joint&param=239 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Pan Liu 0013](https://dblp.org/pid/68/5616-13.html)

[\[j96\]](https://dblp.org/pid/99/3602.html#j96)

[240](https://dblp.org/pid/99/3602.html?view=joint&param=240 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Peidong Liu 0003](https://dblp.org/pid/07/11190-3.html)

[\[c70\]](https://dblp.org/pid/99/3602.html#c70)

[241](https://dblp.org/pid/99/3602.html?view=joint&param=241 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ping Liu 0004](https://dblp.org/pid/34/188-4.html)

[\[j77\]](https://dblp.org/pid/99/3602.html#j77)

[242](https://dblp.org/pid/99/3602.html?view=joint&param=242 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qingjie Liu 0001](https://dblp.org/pid/72/10584.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[243](https://dblp.org/pid/99/3602.html?view=joint&param=243 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qingshan Liu 0002](https://dblp.org/pid/181/2731-2.html)

[\[c22\]](https://dblp.org/pid/99/3602.html#c22)

[244](https://dblp.org/pid/99/3602.html?view=joint&param=244 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qingwang Liu](https://dblp.org/pid/189/3601.html)

[\[j84\]](https://dblp.org/pid/99/3602.html#j84)

[245](https://dblp.org/pid/99/3602.html?view=joint&param=245 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shigang Liu](https://dblp.org/pid/88/2562.html)

[\[j30\]](https://dblp.org/pid/99/3602.html#j30)

[246](https://dblp.org/pid/99/3602.html?view=joint&param=246 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Si Liu 0001](https://dblp.org/pid/60/7642.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[247](https://dblp.org/pid/99/3602.html?view=joint&param=247 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tongliang Liu](https://dblp.org/pid/150/6667.html)

[\[j113\]](https://dblp.org/pid/99/3602.html#j113) [\[i26\]](https://dblp.org/pid/99/3602.html#i26)

[248](https://dblp.org/pid/99/3602.html?view=joint&param=248 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yandong Liu](https://dblp.org/pid/83/605.html)

[\[j66\]](https://dblp.org/pid/99/3602.html#j66)

[249](https://dblp.org/pid/99/3602.html?view=joint&param=249 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yu Liu](https://dblp.org/pid/97/2274.html)

[\[j96\]](https://dblp.org/pid/99/3602.html#j96) [\[j29\]](https://dblp.org/pid/99/3602.html#j29)

[250](https://dblp.org/pid/99/3602.html?view=joint&param=250 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yue Liu](https://dblp.org/pid/74/1932.html)

[\[j123\]](https://dblp.org/pid/99/3602.html#j123) [\[i23\]](https://dblp.org/pid/99/3602.html#i23) [\[j95\]](https://dblp.org/pid/99/3602.html#j95)

[251](https://dblp.org/pid/99/3602.html?view=joint&param=251 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhiyong Liu](https://dblp.org/pid/16/5205.html)

[\[e1\]](https://dblp.org/pid/99/3602.html#e1)

[252](https://dblp.org/pid/99/3602.html?view=joint&param=252 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhonghua Liu](https://dblp.org/pid/42/876.html)

[\[j14\]](https://dblp.org/pid/99/3602.html#j14)

[253](https://dblp.org/pid/99/3602.html?view=joint&param=253 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yang Long 0001](https://dblp.org/pid/82/10183-1.html)

[\[j140\]](https://dblp.org/pid/99/3602.html#j140) [\[j65\]](https://dblp.org/pid/99/3602.html#j65) [\[j63\]](https://dblp.org/pid/99/3602.html#j63)

[254](https://dblp.org/pid/99/3602.html?view=joint&param=254 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jing Lou](https://dblp.org/pid/54/9756.html)

[\[j115\]](https://dblp.org/pid/99/3602.html#j115) [\[c49\]](https://dblp.org/pid/99/3602.html#c49)

[255](https://dblp.org/pid/99/3602.html?view=joint&param=255 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Cheng Lu 0005](https://dblp.org/pid/91/1482-5.html)

[\[j54\]](https://dblp.org/pid/99/3602.html#j54)

[256](https://dblp.org/pid/99/3602.html?view=joint&param=256 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[257](https://dblp.org/pid/99/3602.html?view=joint&param=257 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Huimin Lu 0001](https://dblp.org/pid/64/2633-1.html)

[\[j103\]](https://dblp.org/pid/99/3602.html#j103) [\[j72\]](https://dblp.org/pid/99/3602.html#j72)

[258](https://dblp.org/pid/99/3602.html?view=joint&param=258 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wei Lu](https://dblp.org/pid/98/6613.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[259](https://dblp.org/pid/99/3602.html?view=joint&param=259 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaobo Lu](https://dblp.org/pid/93/8545.html)

[\[j96\]](https://dblp.org/pid/99/3602.html#j96)

[260](https://dblp.org/pid/99/3602.html?view=joint&param=260 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shangzhen Luan](https://dblp.org/pid/182/1956.html)

[\[c51\]](https://dblp.org/pid/99/3602.html#c51)

[261](https://dblp.org/pid/99/3602.html?view=joint&param=261 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jonathon Luiten](https://dblp.org/pid/211/7992.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[262](https://dblp.org/pid/99/3602.html?view=joint&param=262 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[263](https://dblp.org/pid/99/3602.html?view=joint&param=263 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guozhong Luo](https://dblp.org/pid/228/8540.html)

[\[c73\]](https://dblp.org/pid/99/3602.html#c73) [\[i27\]](https://dblp.org/pid/99/3602.html#i27)

[264](https://dblp.org/pid/99/3602.html?view=joint&param=264 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Khoa Luu](https://dblp.org/pid/43/8092.html)

[\[c12\]](https://dblp.org/pid/99/3602.html#c12)

[265](https://dblp.org/pid/99/3602.html?view=joint&param=265 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bingpeng Ma](https://dblp.org/pid/62/1822.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[266](https://dblp.org/pid/99/3602.html?view=joint&param=266 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chao Ma 0004](https://dblp.org/pid/79/1552-4.html)

[\[j124\]](https://dblp.org/pid/99/3602.html#j124) [\[i35\]](https://dblp.org/pid/99/3602.html#i35) [\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[267](https://dblp.org/pid/99/3602.html?view=joint&param=267 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[268](https://dblp.org/pid/99/3602.html?view=joint&param=268 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yinchao Ma](https://dblp.org/pid/189/1326.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[269](https://dblp.org/pid/99/3602.html?view=joint&param=269 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yunfei Ma](https://dblp.org/pid/80/7673.html)

[\[j147\]](https://dblp.org/pid/99/3602.html#j147) [\[j133\]](https://dblp.org/pid/99/3602.html#j133)

[270](https://dblp.org/pid/99/3602.html?view=joint&param=270 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ziang Ma](https://dblp.org/pid/165/9621.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[271](https://dblp.org/pid/99/3602.html?view=joint&param=271 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiren Mai](https://dblp.org/pid/342/1505.html)

[\[j113\]](https://dblp.org/pid/99/3602.html#j113) [\[i26\]](https://dblp.org/pid/99/3602.html#i26)

[272](https://dblp.org/pid/99/3602.html?view=joint&param=272 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Huaqi Mao](https://dblp.org/pid/263/3026.html)

[\[j65\]](https://dblp.org/pid/99/3602.html#j65)

[273](https://dblp.org/pid/99/3602.html?view=joint&param=273 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[274](https://dblp.org/pid/99/3602.html?view=joint&param=274 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[275](https://dblp.org/pid/99/3602.html?view=joint&param=275 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[276](https://dblp.org/pid/99/3602.html?view=joint&param=276 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xue Mei](https://dblp.org/pid/29/4521.html)

[\[j56\]](https://dblp.org/pid/99/3602.html#j56)

[277](https://dblp.org/pid/99/3602.html?view=joint&param=277 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[278](https://dblp.org/pid/99/3602.html?view=joint&param=278 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[279](https://dblp.org/pid/99/3602.html?view=joint&param=279 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Payman Moallem](https://dblp.org/pid/63/5378.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[280](https://dblp.org/pid/99/3602.html?view=joint&param=280 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chaoxu Mu](https://dblp.org/pid/11/6606.html)

[\[j23\]](https://dblp.org/pid/99/3602.html#j23)

[281](https://dblp.org/pid/99/3602.html?view=joint&param=281 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[282](https://dblp.org/pid/99/3602.html?view=joint&param=282 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hoangvu Nguyen](https://dblp.org/pid/160/2774.html)

[\[j38\]](https://dblp.org/pid/99/3602.html#j38) [\[j27\]](https://dblp.org/pid/99/3602.html#j27) [\[c39\]](https://dblp.org/pid/99/3602.html#c39)

[283](https://dblp.org/pid/99/3602.html?view=joint&param=283 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[284](https://dblp.org/pid/99/3602.html?view=joint&param=284 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tianming Ni](https://dblp.org/pid/193/1937.html)

[\[c78\]](https://dblp.org/pid/99/3602.html#c78)

[285](https://dblp.org/pid/99/3602.html?view=joint&param=285 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Mu Nie](https://dblp.org/pid/210/3225.html)

[\[j111\]](https://dblp.org/pid/99/3602.html#j111) [\[j103\]](https://dblp.org/pid/99/3602.html#j103) [\[c78\]](https://dblp.org/pid/99/3602.html#c78) [\[c64\]](https://dblp.org/pid/99/3602.html#c64) [\[i8\]](https://dblp.org/pid/99/3602.html#i8)

[286](https://dblp.org/pid/99/3602.html?view=joint&param=286 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yuzhen Niu](https://dblp.org/pid/28/7442.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[287](https://dblp.org/pid/99/3602.html?view=joint&param=287 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qiuping Pan](https://dblp.org/pid/125/5176.html)

[\[c18\]](https://dblp.org/pid/99/3602.html#c18)

[288](https://dblp.org/pid/99/3602.html?view=joint&param=288 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Siyang Pan](https://dblp.org/pid/250/5753.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[289](https://dblp.org/pid/99/3602.html?view=joint&param=289 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[ChangBeom Park](https://dblp.org/pid/340/0926.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[290](https://dblp.org/pid/99/3602.html?view=joint&param=290 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Eric Patterson](https://dblp.org/pid/79/1282.html)

[\[c9\]](https://dblp.org/pid/99/3602.html#c9)

[291](https://dblp.org/pid/99/3602.html?view=joint&param=291 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[292](https://dblp.org/pid/99/3602.html?view=joint&param=292 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Matthieu Paul](https://dblp.org/pid/255/6113.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[293](https://dblp.org/pid/99/3602.html?view=joint&param=293 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Furong Peng](https://dblp.org/pid/138/8117.html)

[\[j82\]](https://dblp.org/pid/99/3602.html#j82)

[294](https://dblp.org/pid/99/3602.html?view=joint&param=294 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[295](https://dblp.org/pid/99/3602.html?view=joint&param=295 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yali Peng](https://dblp.org/pid/13/11029.html)

[\[j30\]](https://dblp.org/pid/99/3602.html#j30)

[296](https://dblp.org/pid/99/3602.html?view=joint&param=296 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yucong Peng](https://dblp.org/pid/187/1548.html)

[\[c43\]](https://dblp.org/pid/99/3602.html#c43) [\[c42\]](https://dblp.org/pid/99/3602.html#c42)

[297](https://dblp.org/pid/99/3602.html?view=joint&param=297 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[298](https://dblp.org/pid/99/3602.html?view=joint&param=298 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Preetha Phillips](https://dblp.org/pid/145/9806.html)

[\[c46\]](https://dblp.org/pid/99/3602.html#c46)

[299](https://dblp.org/pid/99/3602.html?view=joint&param=299 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Iaroslav Ponomarenko](https://dblp.org/pid/372/4375.html)

[\[c83\]](https://dblp.org/pid/99/3602.html#c83)

[300](https://dblp.org/pid/99/3602.html?view=joint&param=300 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yaroslav Ponomarenko](https://dblp.org/pid/380/2248.html)

[\[i33\]](https://dblp.org/pid/99/3602.html#i33)

[301](https://dblp.org/pid/99/3602.html?view=joint&param=301 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Fatih Porikli](https://dblp.org/pid/p/FatihMuratPorikli.html)

[\[j79\]](https://dblp.org/pid/99/3602.html#j79)

[302](https://dblp.org/pid/99/3602.html?view=joint&param=302 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Danil V. Prokhorov](https://dblp.org/pid/74/5147.html)

[\[j56\]](https://dblp.org/pid/99/3602.html#j56)

[303](https://dblp.org/pid/99/3602.html?view=joint&param=303 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chenhui Qi](https://dblp.org/pid/384/4642.html)

[\[j130\]](https://dblp.org/pid/99/3602.html#j130)

[304](https://dblp.org/pid/99/3602.html?view=joint&param=304 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lei Qi 0001](https://dblp.org/pid/15/2464-1.html)

[\[j133\]](https://dblp.org/pid/99/3602.html#j133) [\[j116\]](https://dblp.org/pid/99/3602.html#j116) [\[j114\]](https://dblp.org/pid/99/3602.html#j114)

[305](https://dblp.org/pid/99/3602.html?view=joint&param=305 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yunsong Qi](https://dblp.org/pid/48/1306.html)

[\[j33\]](https://dblp.org/pid/99/3602.html#j33)

[306](https://dblp.org/pid/99/3602.html?view=joint&param=306 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chengshan Qian](https://dblp.org/pid/133/3243.html)

[\[j43\]](https://dblp.org/pid/99/3602.html#j43)

[307](https://dblp.org/pid/99/3602.html?view=joint&param=307 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jipeng Qiang](https://dblp.org/pid/138/2494.html)

[\[j82\]](https://dblp.org/pid/99/3602.html#j82)

[308](https://dblp.org/pid/99/3602.html?view=joint&param=308 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guoyong Qiu](https://dblp.org/pid/10/10778.html)

[\[j30\]](https://dblp.org/pid/99/3602.html#j30)

[309](https://dblp.org/pid/99/3602.html?view=joint&param=309 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shijie Qiu](https://dblp.org/pid/177/9019.html)

[\[j50\]](https://dblp.org/pid/99/3602.html#j50)

[310](https://dblp.org/pid/99/3602.html?view=joint&param=310 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shoumeng Qiu](https://dblp.org/pid/284/2537.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[311](https://dblp.org/pid/99/3602.html?view=joint&param=311 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chenyu Qu](https://dblp.org/pid/421/1237.html)

[\[j131\]](https://dblp.org/pid/99/3602.html#j131)

[312](https://dblp.org/pid/99/3602.html?view=joint&param=312 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yuchen Qu](https://dblp.org/pid/422/1178.html)

[\[i37\]](https://dblp.org/pid/99/3602.html#i37)

[313](https://dblp.org/pid/99/3602.html?view=joint&param=313 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhibin Quan](https://dblp.org/pid/141/2189.html)

[\[j121\]](https://dblp.org/pid/99/3602.html#j121) [\[j118\]](https://dblp.org/pid/99/3602.html#j118) [\[j114\]](https://dblp.org/pid/99/3602.html#j114) [\[j111\]](https://dblp.org/pid/99/3602.html#j111) [\[j100\]](https://dblp.org/pid/99/3602.html#j100) [\[j99\]](https://dblp.org/pid/99/3602.html#j99) [\[j90\]](https://dblp.org/pid/99/3602.html#j90) [\[j86\]](https://dblp.org/pid/99/3602.html#j86) [\[c64\]](https://dblp.org/pid/99/3602.html#c64) [\[i15\]](https://dblp.org/pid/99/3602.html#i15) [\[i11\]](https://dblp.org/pid/99/3602.html#i11) [\[j66\]](https://dblp.org/pid/99/3602.html#j66) [\[i8\]](https://dblp.org/pid/99/3602.html#i8)

[314](https://dblp.org/pid/99/3602.html?view=joint&param=314 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Aravindh Rajiv](https://dblp.org/pid/307/9144.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[315](https://dblp.org/pid/99/3602.html?view=joint&param=315 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Kotagiri Ramamohanarao](https://dblp.org/pid/r/KRamamohanarao.html)

aka: Ramamohanarao Kotagiri

[\[j55\]](https://dblp.org/pid/99/3602.html#j55)

[316](https://dblp.org/pid/99/3602.html?view=joint&param=316 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Muhammad Rana](https://dblp.org/pid/276/0222.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[317](https://dblp.org/pid/99/3602.html?view=joint&param=317 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Muhammad Awais Rana](https://dblp.org/pid/347/3707.html)

[\[j98\]](https://dblp.org/pid/99/3602.html#j98)

[318](https://dblp.org/pid/99/3602.html?view=joint&param=318 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dexin Ren](https://dblp.org/pid/214/2519.html)

[\[j128\]](https://dblp.org/pid/99/3602.html#j128)

[319](https://dblp.org/pid/99/3602.html?view=joint&param=319 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Mingwu Ren](https://dblp.org/pid/84/5438.html)

[\[j128\]](https://dblp.org/pid/99/3602.html#j128) [\[j115\]](https://dblp.org/pid/99/3602.html#j115) [\[j97\]](https://dblp.org/pid/99/3602.html#j97) [\[j77\]](https://dblp.org/pid/99/3602.html#j77) [\[c49\]](https://dblp.org/pid/99/3602.html#c49) [\[j5\]](https://dblp.org/pid/99/3602.html#j5) [\[j4\]](https://dblp.org/pid/99/3602.html#j4) [\[c3\]](https://dblp.org/pid/99/3602.html#c3) [\[j1\]](https://dblp.org/pid/99/3602.html#j1)

[320](https://dblp.org/pid/99/3602.html?view=joint&param=320 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Karl Ricanek](https://dblp.org/pid/39/609.html)

[\[j44\]](https://dblp.org/pid/99/3602.html#j44) [\[j19\]](https://dblp.org/pid/99/3602.html#j19) [\[j17\]](https://dblp.org/pid/99/3602.html#j17) [\[j13\]](https://dblp.org/pid/99/3602.html#j13) [\[c22\]](https://dblp.org/pid/99/3602.html#c22) [\[c20\]](https://dblp.org/pid/99/3602.html#c20) [\[j9\]](https://dblp.org/pid/99/3602.html#j9) [\[c14\]](https://dblp.org/pid/99/3602.html#c14) [\[c13\]](https://dblp.org/pid/99/3602.html#c13) [\[c12\]](https://dblp.org/pid/99/3602.html#c12) [\[c11\]](https://dblp.org/pid/99/3602.html#c11) [\[c9\]](https://dblp.org/pid/99/3602.html#c9) [\[j6\]](https://dblp.org/pid/99/3602.html#j6)

[321](https://dblp.org/pid/99/3602.html?view=joint&param=321 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[322](https://dblp.org/pid/99/3602.html?view=joint&param=322 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Litu Rout](https://dblp.org/pid/206/6445.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[323](https://dblp.org/pid/99/3602.html?view=joint&param=323 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Abdul Hamid Sadka](https://dblp.org/pid/89/5742.html)

[\[j70\]](https://dblp.org/pid/99/3602.html#j70)

[324](https://dblp.org/pid/99/3602.html?view=joint&param=324 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hasan Saribas](https://dblp.org/pid/225/3263.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[325](https://dblp.org/pid/99/3602.html?view=joint&param=325 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lotfi Senhadji](https://dblp.org/pid/58/670.html)

[\[j50\]](https://dblp.org/pid/99/3602.html#j50)

[326](https://dblp.org/pid/99/3602.html?view=joint&param=326 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Amrutha Sethuram](https://dblp.org/pid/72/233.html)

[\[c20\]](https://dblp.org/pid/99/3602.html#c20) [\[c9\]](https://dblp.org/pid/99/3602.html#c9)

[327](https://dblp.org/pid/99/3602.html?view=joint&param=327 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Pourya Shamsolmoali](https://dblp.org/pid/154/8477.html)

[\[j70\]](https://dblp.org/pid/99/3602.html#j70)

[328](https://dblp.org/pid/99/3602.html?view=joint&param=328 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c14\]](https://dblp.org/pid/99/3602.html#c14)

[329](https://dblp.org/pid/99/3602.html?view=joint&param=329 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61) [\[j65\]](https://dblp.org/pid/99/3602.html#j65) [\[j63\]](https://dblp.org/pid/99/3602.html#j63)

[330](https://dblp.org/pid/99/3602.html?view=joint&param=330 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Mohamed S. Shehata](https://dblp.org/pid/33/2495.html)

aka: Mohamed Shehata 0001

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[331](https://dblp.org/pid/99/3602.html?view=joint&param=331 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chunhua Shen](https://dblp.org/pid/56/1673.html)

[\[j48\]](https://dblp.org/pid/99/3602.html#j48) [\[i2\]](https://dblp.org/pid/99/3602.html#i2)

[332](https://dblp.org/pid/99/3602.html?view=joint&param=332 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Fumin Shen](https://dblp.org/pid/92/10934.html)

[\[c60\]](https://dblp.org/pid/99/3602.html#c60) [\[c55\]](https://dblp.org/pid/99/3602.html#c55) [\[c53\]](https://dblp.org/pid/99/3602.html#c53) [\[j41\]](https://dblp.org/pid/99/3602.html#j41) [\[i4\]](https://dblp.org/pid/99/3602.html#i4) [\[j32\]](https://dblp.org/pid/99/3602.html#j32) [\[j31\]](https://dblp.org/pid/99/3602.html#j31) [\[j27\]](https://dblp.org/pid/99/3602.html#j27) [\[c30\]](https://dblp.org/pid/99/3602.html#c30) [\[j19\]](https://dblp.org/pid/99/3602.html#j19)

[333](https://dblp.org/pid/99/3602.html?view=joint&param=333 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Furao Shen](https://dblp.org/pid/80/4685.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[334](https://dblp.org/pid/99/3602.html?view=joint&param=334 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Heng Tao Shen](https://dblp.org/pid/s/HTShen.html)

[\[j32\]](https://dblp.org/pid/99/3602.html#j32)

[335](https://dblp.org/pid/99/3602.html?view=joint&param=335 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jianbing Shen](https://dblp.org/pid/38/5435.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[336](https://dblp.org/pid/99/3602.html?view=joint&param=336 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jifeng Shen](https://dblp.org/pid/23/8615.html)

[\[j149\]](https://dblp.org/pid/99/3602.html#j149) [\[j142\]](https://dblp.org/pid/99/3602.html#j142) [\[j136\]](https://dblp.org/pid/99/3602.html#j136) [\[j131\]](https://dblp.org/pid/99/3602.html#j131) [\[i45\]](https://dblp.org/pid/99/3602.html#i45) [\[i42\]](https://dblp.org/pid/99/3602.html#i42) [\[i40\]](https://dblp.org/pid/99/3602.html#i40) [\[i37\]](https://dblp.org/pid/99/3602.html#i37) [\[j130\]](https://dblp.org/pid/99/3602.html#j130) [\[j123\]](https://dblp.org/pid/99/3602.html#j123) [\[j122\]](https://dblp.org/pid/99/3602.html#j122) [\[j120\]](https://dblp.org/pid/99/3602.html#j120) [\[j109\]](https://dblp.org/pid/99/3602.html#j109) [\[j102\]](https://dblp.org/pid/99/3602.html#j102) [\[i28\]](https://dblp.org/pid/99/3602.html#i28) [\[i23\]](https://dblp.org/pid/99/3602.html#i23) [\[i19\]](https://dblp.org/pid/99/3602.html#i19) [\[j95\]](https://dblp.org/pid/99/3602.html#j95) [\[j57\]](https://dblp.org/pid/99/3602.html#j57) [\[j56\]](https://dblp.org/pid/99/3602.html#j56) [\[c56\]](https://dblp.org/pid/99/3602.html#c56) [\[j49\]](https://dblp.org/pid/99/3602.html#j49) [\[j43\]](https://dblp.org/pid/99/3602.html#j43) [\[j42\]](https://dblp.org/pid/99/3602.html#j42) [\[c45\]](https://dblp.org/pid/99/3602.html#c45) [\[j36\]](https://dblp.org/pid/99/3602.html#j36) [\[j33\]](https://dblp.org/pid/99/3602.html#j33) [\[c42\]](https://dblp.org/pid/99/3602.html#c42) [\[c40\]](https://dblp.org/pid/99/3602.html#c40) [\[c28\]](https://dblp.org/pid/99/3602.html#c28) [\[j15\]](https://dblp.org/pid/99/3602.html#j15) [\[j12\]](https://dblp.org/pid/99/3602.html#j12) [\[c18\]](https://dblp.org/pid/99/3602.html#c18) [\[j11\]](https://dblp.org/pid/99/3602.html#j11) [\[c8\]](https://dblp.org/pid/99/3602.html#c8) [\[c6\]](https://dblp.org/pid/99/3602.html#c6)

[337](https://dblp.org/pid/99/3602.html?view=joint&param=337 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiao Shen](https://dblp.org/pid/166/6158.html)

[\[j93\]](https://dblp.org/pid/99/3602.html#j93)

[338](https://dblp.org/pid/99/3602.html?view=joint&param=338 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Biyun Sheng](https://dblp.org/pid/158/1357.html)

[\[j73\]](https://dblp.org/pid/99/3602.html#j73) [\[j69\]](https://dblp.org/pid/99/3602.html#j69) [\[j48\]](https://dblp.org/pid/99/3602.html#j48) [\[j46\]](https://dblp.org/pid/99/3602.html#j46) [\[j38\]](https://dblp.org/pid/99/3602.html#j38) [\[i2\]](https://dblp.org/pid/99/3602.html#i2) [\[j26\]](https://dblp.org/pid/99/3602.html#j26) [\[c33\]](https://dblp.org/pid/99/3602.html#c33) [\[c29\]](https://dblp.org/pid/99/3602.html#c29)

[339](https://dblp.org/pid/99/3602.html?view=joint&param=339 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiayu Sheng](https://dblp.org/pid/169/4623.html)

[\[c33\]](https://dblp.org/pid/99/3602.html#c33)

[340](https://dblp.org/pid/99/3602.html?view=joint&param=340 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lei Shi](https://dblp.org/pid/29/563.html)

[\[j110\]](https://dblp.org/pid/99/3602.html#j110)

[341](https://dblp.org/pid/99/3602.html?view=joint&param=341 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shiwei Shi](https://dblp.org/pid/187/9158.html)

[\[c40\]](https://dblp.org/pid/99/3602.html#c40)

[342](https://dblp.org/pid/99/3602.html?view=joint&param=342 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wen Shi 0007](https://dblp.org/pid/02/3628-7.html)

[\[j91\]](https://dblp.org/pid/99/3602.html#j91)

[343](https://dblp.org/pid/99/3602.html?view=joint&param=343 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Huazhong Shu](https://dblp.org/pid/56/121.html)

[\[j50\]](https://dblp.org/pid/99/3602.html#j50)

[344](https://dblp.org/pid/99/3602.html?view=joint&param=344 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiangbo Shu](https://dblp.org/pid/169/3410.html)

[\[c59\]](https://dblp.org/pid/99/3602.html#c59)

[345](https://dblp.org/pid/99/3602.html?view=joint&param=345 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[346](https://dblp.org/pid/99/3602.html?view=joint&param=346 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Aiguo Song](https://dblp.org/pid/21/1796.html)

[\[j29\]](https://dblp.org/pid/99/3602.html#j29) [\[j28\]](https://dblp.org/pid/99/3602.html#j28)

[347](https://dblp.org/pid/99/3602.html?view=joint&param=347 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tianhui Song](https://dblp.org/pid/181/8738.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[348](https://dblp.org/pid/99/3602.html?view=joint&param=348 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[349](https://dblp.org/pid/99/3602.html?view=joint&param=349 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yaoye Song](https://dblp.org/pid/254/0543.html)

[\[c56\]](https://dblp.org/pid/99/3602.html#c56)

[350](https://dblp.org/pid/99/3602.html?view=joint&param=350 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shun-Feng Su](https://dblp.org/pid/42/598.html)

[\[j117\]](https://dblp.org/pid/99/3602.html#j117)

[351](https://dblp.org/pid/99/3602.html?view=joint&param=351 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yifei Su](https://dblp.org/pid/237/4153.html)

[\[j147\]](https://dblp.org/pid/99/3602.html#j147)

[352](https://dblp.org/pid/99/3602.html?view=joint&param=352 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Changyin Sun 0001](https://dblp.org/pid/64/221.html)

[\[j76\]](https://dblp.org/pid/99/3602.html#j76) [\[j71\]](https://dblp.org/pid/99/3602.html#j71) [\[j67\]](https://dblp.org/pid/99/3602.html#j67) [\[j62\]](https://dblp.org/pid/99/3602.html#j62) [\[j55\]](https://dblp.org/pid/99/3602.html#j55) [\[j48\]](https://dblp.org/pid/99/3602.html#j48) [\[c54\]](https://dblp.org/pid/99/3602.html#c54) [\[c52\]](https://dblp.org/pid/99/3602.html#c52) [\[i6\]](https://dblp.org/pid/99/3602.html#i6) [\[i5\]](https://dblp.org/pid/99/3602.html#i5) [\[j46\]](https://dblp.org/pid/99/3602.html#j46) [\[j45\]](https://dblp.org/pid/99/3602.html#j45) [\[j44\]](https://dblp.org/pid/99/3602.html#j44) [\[j40\]](https://dblp.org/pid/99/3602.html#j40) [\[c48\]](https://dblp.org/pid/99/3602.html#c48) [\[c47\]](https://dblp.org/pid/99/3602.html#c47) [\[i3\]](https://dblp.org/pid/99/3602.html#i3) [\[j38\]](https://dblp.org/pid/99/3602.html#j38) [\[j37\]](https://dblp.org/pid/99/3602.html#j37) [\[j35\]](https://dblp.org/pid/99/3602.html#j35) [\[j33\]](https://dblp.org/pid/99/3602.html#j33) [\[i2\]](https://dblp.org/pid/99/3602.html#i2) [\[i1\]](https://dblp.org/pid/99/3602.html#i1) [\[j27\]](https://dblp.org/pid/99/3602.html#j27) [\[j26\]](https://dblp.org/pid/99/3602.html#j26) [\[j25\]](https://dblp.org/pid/99/3602.html#j25) [\[j24\]](https://dblp.org/pid/99/3602.html#j24) [\[j23\]](https://dblp.org/pid/99/3602.html#j23) [\[j21\]](https://dblp.org/pid/99/3602.html#j21) [\[c39\]](https://dblp.org/pid/99/3602.html#c39) [\[c34\]](https://dblp.org/pid/99/3602.html#c34) [\[c33\]](https://dblp.org/pid/99/3602.html#c33) [\[c32\]](https://dblp.org/pid/99/3602.html#c32) [\[c31\]](https://dblp.org/pid/99/3602.html#c31) [\[j20\]](https://dblp.org/pid/99/3602.html#j20) [\[j18\]](https://dblp.org/pid/99/3602.html#j18) [\[c29\]](https://dblp.org/pid/99/3602.html#c29) [\[j17\]](https://dblp.org/pid/99/3602.html#j17) [\[j15\]](https://dblp.org/pid/99/3602.html#j15) [\[c27\]](https://dblp.org/pid/99/3602.html#c27) [\[c26\]](https://dblp.org/pid/99/3602.html#c26) [\[c25\]](https://dblp.org/pid/99/3602.html#c25) [\[c23\]](https://dblp.org/pid/99/3602.html#c23) [\[e1\]](https://dblp.org/pid/99/3602.html#e1) [\[j13\]](https://dblp.org/pid/99/3602.html#j13) [\[j12\]](https://dblp.org/pid/99/3602.html#j12) [\[c22\]](https://dblp.org/pid/99/3602.html#c22) [\[c19\]](https://dblp.org/pid/99/3602.html#c19) [\[c18\]](https://dblp.org/pid/99/3602.html#c18) [\[c17\]](https://dblp.org/pid/99/3602.html#c17) [\[c15\]](https://dblp.org/pid/99/3602.html#c15) [\[j11\]](https://dblp.org/pid/99/3602.html#j11) [\[j10\]](https://dblp.org/pid/99/3602.html#j10) [\[j9\]](https://dblp.org/pid/99/3602.html#j9) [\[j8\]](https://dblp.org/pid/99/3602.html#j8) [\[c13\]](https://dblp.org/pid/99/3602.html#c13) [\[c11\]](https://dblp.org/pid/99/3602.html#c11) [\[c10\]](https://dblp.org/pid/99/3602.html#c10) [\[c9\]](https://dblp.org/pid/99/3602.html#c9) [\[c8\]](https://dblp.org/pid/99/3602.html#c8) [\[j7\]](https://dblp.org/pid/99/3602.html#j7) [\[j6\]](https://dblp.org/pid/99/3602.html#j6) [\[c7\]](https://dblp.org/pid/99/3602.html#c7) [\[c6\]](https://dblp.org/pid/99/3602.html#c6)

[353](https://dblp.org/pid/99/3602.html?view=joint&param=353 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chao Sun](https://dblp.org/pid/54/3957.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[354](https://dblp.org/pid/99/3602.html?view=joint&param=354 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jingna Sun](https://dblp.org/pid/255/0702.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[355](https://dblp.org/pid/99/3602.html?view=joint&param=355 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ke Sun](https://dblp.org/pid/69/476.html)

[\[j140\]](https://dblp.org/pid/99/3602.html#j140)

[356](https://dblp.org/pid/99/3602.html?view=joint&param=356 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qiming Sun](https://dblp.org/pid/65/7929.html)

[\[j62\]](https://dblp.org/pid/99/3602.html#j62)

[357](https://dblp.org/pid/99/3602.html?view=joint&param=357 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaolou Sun](https://dblp.org/pid/329/0397.html)

[\[c75\]](https://dblp.org/pid/99/3602.html#c75) [\[j90\]](https://dblp.org/pid/99/3602.html#j90)

[358](https://dblp.org/pid/99/3602.html?view=joint&param=358 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yanpeng Sun](https://dblp.org/pid/143/0055.html)

[\[i43\]](https://dblp.org/pid/99/3602.html#i43)

[359](https://dblp.org/pid/99/3602.html?view=joint&param=359 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhongxi Sun](https://dblp.org/pid/39/9614.html)

[\[j12\]](https://dblp.org/pid/99/3602.html#j12) [\[j11\]](https://dblp.org/pid/99/3602.html#j11) [\[c8\]](https://dblp.org/pid/99/3602.html#c8)

[360](https://dblp.org/pid/99/3602.html?view=joint&param=360 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Satoshi Suzuki](https://dblp.org/pid/30/181.html)

[\[j90\]](https://dblp.org/pid/99/3602.html#j90)

[361](https://dblp.org/pid/99/3602.html?view=joint&param=361 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Edward Szczerbicki](https://dblp.org/pid/25/345.html)

[\[j110\]](https://dblp.org/pid/99/3602.html#j110)

[362](https://dblp.org/pid/99/3602.html?view=joint&param=362 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[363](https://dblp.org/pid/99/3602.html?view=joint&param=363 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhenmin Tang](https://dblp.org/pid/13/6728.html)

[\[j78\]](https://dblp.org/pid/99/3602.html#j78) [\[j60\]](https://dblp.org/pid/99/3602.html#j60) [\[c55\]](https://dblp.org/pid/99/3602.html#c55) [\[c53\]](https://dblp.org/pid/99/3602.html#c53) [\[i4\]](https://dblp.org/pid/99/3602.html#i4)

[364](https://dblp.org/pid/99/3602.html?view=joint&param=364 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dacheng Tao](https://dblp.org/pid/46/3391.html)

[\[j55\]](https://dblp.org/pid/99/3602.html#j55) [\[i5\]](https://dblp.org/pid/99/3602.html#i5) [\[j40\]](https://dblp.org/pid/99/3602.html#j40)

[365](https://dblp.org/pid/99/3602.html?view=joint&param=365 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[366](https://dblp.org/pid/99/3602.html?view=joint&param=366 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Junlong Tong](https://dblp.org/pid/332/1196.html)

[\[j107\]](https://dblp.org/pid/99/3602.html#j107) [\[i17\]](https://dblp.org/pid/99/3602.html#i17)

[367](https://dblp.org/pid/99/3602.html?view=joint&param=367 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xinjie Tong](https://dblp.org/pid/244/0818.html)

[\[c57\]](https://dblp.org/pid/99/3602.html#c57)

[368](https://dblp.org/pid/99/3602.html?view=joint&param=368 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[369](https://dblp.org/pid/99/3602.html?view=joint&param=369 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[370](https://dblp.org/pid/99/3602.html?view=joint&param=370 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bedirhan Uzun](https://dblp.org/pid/247/8937.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[371](https://dblp.org/pid/99/3602.html?view=joint&param=371 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Om Prakash Verma](https://dblp.org/pid/61/8145.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[372](https://dblp.org/pid/99/3602.html?view=joint&param=372 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Paul Voigtlaender](https://dblp.org/pid/166/6430.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[373](https://dblp.org/pid/99/3602.html?view=joint&param=373 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chi-Man Vong](https://dblp.org/pid/68/5768.html)

[\[j118\]](https://dblp.org/pid/99/3602.html#j118)

[374](https://dblp.org/pid/99/3602.html?view=joint&param=374 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chao Wang](https://dblp.org/pid/188/7759.html)

[\[j75\]](https://dblp.org/pid/99/3602.html#j75)

[375](https://dblp.org/pid/99/3602.html?view=joint&param=375 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chunyu Wang 0001](https://dblp.org/pid/63/7235-1.html)

[\[j124\]](https://dblp.org/pid/99/3602.html#j124) [\[i35\]](https://dblp.org/pid/99/3602.html#i35) [\[c71\]](https://dblp.org/pid/99/3602.html#c71) [\[i18\]](https://dblp.org/pid/99/3602.html#i18) [\[c62\]](https://dblp.org/pid/99/3602.html#c62) [\[i10\]](https://dblp.org/pid/99/3602.html#i10)

[376](https://dblp.org/pid/99/3602.html?view=joint&param=376 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[377](https://dblp.org/pid/99/3602.html?view=joint&param=377 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Fei Wang 0032](https://dblp.org/pid/52/3194-32.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[378](https://dblp.org/pid/99/3602.html?view=joint&param=378 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guangtao Wang](https://dblp.org/pid/26/11029.html)

[\[j102\]](https://dblp.org/pid/99/3602.html#j102) [\[i28\]](https://dblp.org/pid/99/3602.html#i28)

[379](https://dblp.org/pid/99/3602.html?view=joint&param=379 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guangting Wang](https://dblp.org/pid/227/7195.html)

[\[c71\]](https://dblp.org/pid/99/3602.html#c71) [\[i18\]](https://dblp.org/pid/99/3602.html#i18) [\[c63\]](https://dblp.org/pid/99/3602.html#c63) [\[c62\]](https://dblp.org/pid/99/3602.html#c62) [\[c61\]](https://dblp.org/pid/99/3602.html#c61) [\[i10\]](https://dblp.org/pid/99/3602.html#i10)

[380](https://dblp.org/pid/99/3602.html?view=joint&param=380 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hao Wang 0144](https://dblp.org/pid/181/2812-144.html)

[\[c75\]](https://dblp.org/pid/99/3602.html#c75) [\[j90\]](https://dblp.org/pid/99/3602.html#j90)

[381](https://dblp.org/pid/99/3602.html?view=joint&param=381 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Haoran Wang 0001](https://dblp.org/pid/28/3021-1.html)

[\[j112\]](https://dblp.org/pid/99/3602.html#j112) [\[j61\]](https://dblp.org/pid/99/3602.html#j61) [\[j49\]](https://dblp.org/pid/99/3602.html#j49) [\[j47\]](https://dblp.org/pid/99/3602.html#j47) [\[j43\]](https://dblp.org/pid/99/3602.html#j43) [\[j18\]](https://dblp.org/pid/99/3602.html#j18)

[382](https://dblp.org/pid/99/3602.html?view=joint&param=382 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hongren Wang 0001](https://dblp.org/pid/227/4893-1.html)

[\[j58\]](https://dblp.org/pid/99/3602.html#j58)

[383](https://dblp.org/pid/99/3602.html?view=joint&param=383 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hongyuan Wang](https://dblp.org/pid/17/203.html)

[\[c16\]](https://dblp.org/pid/99/3602.html#c16)

[384](https://dblp.org/pid/99/3602.html?view=joint&param=384 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Huan Wang 0013](https://dblp.org/pid/70/6155-13.html)

[\[j115\]](https://dblp.org/pid/99/3602.html#j115) [\[j97\]](https://dblp.org/pid/99/3602.html#j97) [\[j83\]](https://dblp.org/pid/99/3602.html#j83) [\[c1\]](https://dblp.org/pid/99/3602.html#c1)

[385](https://dblp.org/pid/99/3602.html?view=joint&param=385 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jianguo Wang 0002](https://dblp.org/pid/64/1071-2.html)

[\[j16\]](https://dblp.org/pid/99/3602.html#j16) [\[j5\]](https://dblp.org/pid/99/3602.html#j5) [\[j4\]](https://dblp.org/pid/99/3602.html#j4) [\[j3\]](https://dblp.org/pid/99/3602.html#j3) [\[j2\]](https://dblp.org/pid/99/3602.html#j2) [\[c4\]](https://dblp.org/pid/99/3602.html#c4) [\[c3\]](https://dblp.org/pid/99/3602.html#c3) [\[c2\]](https://dblp.org/pid/99/3602.html#c2)

[386](https://dblp.org/pid/99/3602.html?view=joint&param=386 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jingdong Wang 0001](https://dblp.org/pid/49/3441.html)

[\[j146\]](https://dblp.org/pid/99/3602.html#j146) [\[c84\]](https://dblp.org/pid/99/3602.html#c84) [\[i44\]](https://dblp.org/pid/99/3602.html#i44) [\[i39\]](https://dblp.org/pid/99/3602.html#i39) [\[i38\]](https://dblp.org/pid/99/3602.html#i38) [\[i36\]](https://dblp.org/pid/99/3602.html#i36) [\[i32\]](https://dblp.org/pid/99/3602.html#i32) [\[i31\]](https://dblp.org/pid/99/3602.html#i31)

[387](https://dblp.org/pid/99/3602.html?view=joint&param=387 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Juan Wang 0017](https://dblp.org/pid/74/3634-17.html)

[\[j110\]](https://dblp.org/pid/99/3602.html#j110)

[388](https://dblp.org/pid/99/3602.html?view=joint&param=388 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lei Wang 0018](https://dblp.org/pid/w/LeiWang18.html)

[\[c35\]](https://dblp.org/pid/99/3602.html#c35)

[389](https://dblp.org/pid/99/3602.html?view=joint&param=389 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Liang Wang 0001](https://dblp.org/pid/56/4499-1.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[j20\]](https://dblp.org/pid/99/3602.html#j20) [\[c24\]](https://dblp.org/pid/99/3602.html#c24)

[390](https://dblp.org/pid/99/3602.html?view=joint&param=390 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[391](https://dblp.org/pid/99/3602.html?view=joint&param=391 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[392](https://dblp.org/pid/99/3602.html?view=joint&param=392 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[393](https://dblp.org/pid/99/3602.html?view=joint&param=393 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Linyuan Wang](https://dblp.org/pid/138/5963.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[394](https://dblp.org/pid/99/3602.html?view=joint&param=394 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ning Wang 0020](https://dblp.org/pid/46/2005-20.html)

[\[c58\]](https://dblp.org/pid/99/3602.html#c58)

[395](https://dblp.org/pid/99/3602.html?view=joint&param=395 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qi Wang](https://dblp.org/pid/19/1924.html)

[\[j90\]](https://dblp.org/pid/99/3602.html#j90)

[396](https://dblp.org/pid/99/3602.html?view=joint&param=396 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qiang Wang 0023](https://dblp.org/pid/64/5630-23.html)

[\[j108\]](https://dblp.org/pid/99/3602.html#j108) [\[j106\]](https://dblp.org/pid/99/3602.html#j106) [\[c75\]](https://dblp.org/pid/99/3602.html#c75) [\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[j83\]](https://dblp.org/pid/99/3602.html#j83) [\[j80\]](https://dblp.org/pid/99/3602.html#j80) [\[c66\]](https://dblp.org/pid/99/3602.html#c66)

[397](https://dblp.org/pid/99/3602.html?view=joint&param=397 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qingling Wang](https://dblp.org/pid/61/4797.html)

[\[c31\]](https://dblp.org/pid/99/3602.html#c31)

[398](https://dblp.org/pid/99/3602.html?view=joint&param=398 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qiong Wang 0003](https://dblp.org/pid/65/3144-3.html)

[\[c60\]](https://dblp.org/pid/99/3602.html#c60) [\[j60\]](https://dblp.org/pid/99/3602.html#j60) [\[c1\]](https://dblp.org/pid/99/3602.html#c1)

[399](https://dblp.org/pid/99/3602.html?view=joint&param=399 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Senling Wang](https://dblp.org/pid/123/8631.html)

[\[c78\]](https://dblp.org/pid/99/3602.html#c78)

[400](https://dblp.org/pid/99/3602.html?view=joint&param=400 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shengdi Wang](https://dblp.org/pid/125/5067.html)

[\[c16\]](https://dblp.org/pid/99/3602.html#c16)

[401](https://dblp.org/pid/99/3602.html?view=joint&param=401 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shidong Wang](https://dblp.org/pid/82/8629.html)

[\[j129\]](https://dblp.org/pid/99/3602.html#j129) [\[j128\]](https://dblp.org/pid/99/3602.html#j128) [\[j64\]](https://dblp.org/pid/99/3602.html#j64)

[402](https://dblp.org/pid/99/3602.html?view=joint&param=402 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shuihua Wang](https://dblp.org/pid/18/8544.html)

[\[c46\]](https://dblp.org/pid/99/3602.html#c46)

[403](https://dblp.org/pid/99/3602.html?view=joint&param=403 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Siyu Wang](https://dblp.org/pid/168/9309.html)

[\[j101\]](https://dblp.org/pid/99/3602.html#j101)

[404](https://dblp.org/pid/99/3602.html?view=joint&param=404 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Su-Jing Wang](https://dblp.org/pid/209/7218.html)

[\[j59\]](https://dblp.org/pid/99/3602.html#j59)

[405](https://dblp.org/pid/99/3602.html?view=joint&param=405 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ting Wang](https://dblp.org/pid/12/2633.html)

[\[j126\]](https://dblp.org/pid/99/3602.html#j126)

[406](https://dblp.org/pid/99/3602.html?view=joint&param=406 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wei Wang](https://dblp.org/pid/35/7092.html)

[\[j90\]](https://dblp.org/pid/99/3602.html#j90)

[407](https://dblp.org/pid/99/3602.html?view=joint&param=407 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaofeng Wang](https://dblp.org/pid/99/2479.html)

[\[c74\]](https://dblp.org/pid/99/3602.html#c74)

[408](https://dblp.org/pid/99/3602.html?view=joint&param=408 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yajie Wang](https://dblp.org/pid/10/821.html)

[\[j112\]](https://dblp.org/pid/99/3602.html#j112)

[409](https://dblp.org/pid/99/3602.html?view=joint&param=409 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yishi Wang](https://dblp.org/pid/15/9606.html)

[\[c14\]](https://dblp.org/pid/99/3602.html#c14) [\[c12\]](https://dblp.org/pid/99/3602.html#c12)

[410](https://dblp.org/pid/99/3602.html?view=joint&param=410 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yiye Wang](https://dblp.org/pid/298/5387.html)

[\[c68\]](https://dblp.org/pid/99/3602.html#c68) [\[i12\]](https://dblp.org/pid/99/3602.html#i12)

[411](https://dblp.org/pid/99/3602.html?view=joint&param=411 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[j80\]](https://dblp.org/pid/99/3602.html#j80) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[412](https://dblp.org/pid/99/3602.html?view=joint&param=412 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yunhong Wang 0001](https://dblp.org/pid/95/6251.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[413](https://dblp.org/pid/99/3602.html?view=joint&param=413 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yunxiao Wang](https://dblp.org/pid/11/3450.html)

[\[c70\]](https://dblp.org/pid/99/3602.html#c70)

[414](https://dblp.org/pid/99/3602.html?view=joint&param=414 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ze Wang 0008](https://dblp.org/pid/35/6674-8.html)

[\[j68\]](https://dblp.org/pid/99/3602.html#j68)

[415](https://dblp.org/pid/99/3602.html?view=joint&param=415 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhenhua Wang](https://dblp.org/pid/33/4679.html)

[\[j103\]](https://dblp.org/pid/99/3602.html#j103)

[416](https://dblp.org/pid/99/3602.html?view=joint&param=416 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhenyu Wang](https://dblp.org/pid/22/1486.html)

[\[j34\]](https://dblp.org/pid/99/3602.html#j34) [\[j31\]](https://dblp.org/pid/99/3602.html#j31) [\[j22\]](https://dblp.org/pid/99/3602.html#j22) [\[j21\]](https://dblp.org/pid/99/3602.html#j21) [\[j17\]](https://dblp.org/pid/99/3602.html#j17) [\[c26\]](https://dblp.org/pid/99/3602.html#c26) [\[j11\]](https://dblp.org/pid/99/3602.html#j11)

[417](https://dblp.org/pid/99/3602.html?view=joint&param=417 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhi Wang](https://dblp.org/pid/95/6543.html)

[\[j109\]](https://dblp.org/pid/99/3602.html#j109)

[418](https://dblp.org/pid/99/3602.html?view=joint&param=418 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhicheng Wang 0001](https://dblp.org/pid/78/1664-1.html)

[\[j99\]](https://dblp.org/pid/99/3602.html#j99) [\[c70\]](https://dblp.org/pid/99/3602.html#c70) [\[c65\]](https://dblp.org/pid/99/3602.html#c65) [\[i14\]](https://dblp.org/pid/99/3602.html#i14) [\[i13\]](https://dblp.org/pid/99/3602.html#i13) [\[i11\]](https://dblp.org/pid/99/3602.html#i11)

[419](https://dblp.org/pid/99/3602.html?view=joint&param=419 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zuli Wang 0001](https://dblp.org/pid/187/9462.html)

[\[j110\]](https://dblp.org/pid/99/3602.html#j110)

[420](https://dblp.org/pid/99/3602.html?view=joint&param=420 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Haikun Wei](https://dblp.org/pid/16/6484.html)

[\[j51\]](https://dblp.org/pid/99/3602.html#j51) [\[c44\]](https://dblp.org/pid/99/3602.html#c44)

[421](https://dblp.org/pid/99/3602.html?view=joint&param=421 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaoqing Wen](https://dblp.org/pid/38/3836.html)

[\[c78\]](https://dblp.org/pid/99/3602.html#c78)

[422](https://dblp.org/pid/99/3602.html?view=joint&param=422 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chenyan Wu](https://dblp.org/pid/76/1190.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[423](https://dblp.org/pid/99/3602.html?view=joint&param=423 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[424](https://dblp.org/pid/99/3602.html?view=joint&param=424 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiasong Wu](https://dblp.org/pid/63/8859.html)

[\[j50\]](https://dblp.org/pid/99/3602.html#j50)

[425](https://dblp.org/pid/99/3602.html?view=joint&param=425 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jinhui Wu](https://dblp.org/pid/36/6077.html)

[\[j148\]](https://dblp.org/pid/99/3602.html#j148) [\[j137\]](https://dblp.org/pid/99/3602.html#j137) [\[j134\]](https://dblp.org/pid/99/3602.html#j134) [\[c81\]](https://dblp.org/pid/99/3602.html#c81)

[426](https://dblp.org/pid/99/3602.html?view=joint&param=426 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jinlin Wu](https://dblp.org/pid/123/7200.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[427](https://dblp.org/pid/99/3602.html?view=joint&param=427 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Letian Wu](https://dblp.org/pid/322/6967.html)

[\[j138\]](https://dblp.org/pid/99/3602.html#j138) [\[j135\]](https://dblp.org/pid/99/3602.html#j135) [\[j133\]](https://dblp.org/pid/99/3602.html#j133) [\[j104\]](https://dblp.org/pid/99/3602.html#j104) [\[i25\]](https://dblp.org/pid/99/3602.html#i25) [\[i24\]](https://dblp.org/pid/99/3602.html#i24)

[428](https://dblp.org/pid/99/3602.html?view=joint&param=428 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qiang Wu 0001](https://dblp.org/pid/87/2533-1.html)

[\[j78\]](https://dblp.org/pid/99/3602.html#j78)

[429](https://dblp.org/pid/99/3602.html?view=joint&param=429 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[430](https://dblp.org/pid/99/3602.html?view=joint&param=430 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhijian Wu](https://dblp.org/pid/23/3616.html)

[\[j102\]](https://dblp.org/pid/99/3602.html#j102) [\[i28\]](https://dblp.org/pid/99/3602.html#i28) [\[j94\]](https://dblp.org/pid/99/3602.html#j94) [\[j81\]](https://dblp.org/pid/99/3602.html#j81)

[431](https://dblp.org/pid/99/3602.html?view=joint&param=431 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qingyuan Xia](https://dblp.org/pid/198/1080.html)

[\[c49\]](https://dblp.org/pid/99/3602.html#c49)

[432](https://dblp.org/pid/99/3602.html?view=joint&param=432 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shutao Xia](https://dblp.org/pid/34/3173.html)

aka: Shu-Tao Xia

[\[j99\]](https://dblp.org/pid/99/3602.html#j99) [\[c70\]](https://dblp.org/pid/99/3602.html#c70) [\[c65\]](https://dblp.org/pid/99/3602.html#c65) [\[i14\]](https://dblp.org/pid/99/3602.html#i14) [\[i13\]](https://dblp.org/pid/99/3602.html#i13) [\[i11\]](https://dblp.org/pid/99/3602.html#i11)

[433](https://dblp.org/pid/99/3602.html?view=joint&param=433 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tao Xiang 0002](https://dblp.org/pid/22/4460-2.html)

[\[j71\]](https://dblp.org/pid/99/3602.html#j71) [\[c54\]](https://dblp.org/pid/99/3602.html#c54) [\[i6\]](https://dblp.org/pid/99/3602.html#i6) [\[c48\]](https://dblp.org/pid/99/3602.html#c48) [\[i3\]](https://dblp.org/pid/99/3602.html#i3) [\[i1\]](https://dblp.org/pid/99/3602.html#i1)

[434](https://dblp.org/pid/99/3602.html?view=joint&param=434 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Fu Xiao 0001](https://dblp.org/pid/91/8079-1.html)

[\[j73\]](https://dblp.org/pid/99/3602.html#j73) [\[j69\]](https://dblp.org/pid/99/3602.html#j69)

[435](https://dblp.org/pid/99/3602.html?view=joint&param=435 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lingyu Xiao](https://dblp.org/pid/355/3184.html)

[\[j134\]](https://dblp.org/pid/99/3602.html#j134) [\[c84\]](https://dblp.org/pid/99/3602.html#c84) [\[i44\]](https://dblp.org/pid/99/3602.html#i44) [\[i32\]](https://dblp.org/pid/99/3602.html#i32) [\[i31\]](https://dblp.org/pid/99/3602.html#i31) [\[c76\]](https://dblp.org/pid/99/3602.html#c76) [\[i21\]](https://dblp.org/pid/99/3602.html#i21)

[436](https://dblp.org/pid/99/3602.html?view=joint&param=436 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[j148\]](https://dblp.org/pid/99/3602.html#j148) [\[j124\]](https://dblp.org/pid/99/3602.html#j124) [\[j119\]](https://dblp.org/pid/99/3602.html#j119) [\[i35\]](https://dblp.org/pid/99/3602.html#i35) [\[j90\]](https://dblp.org/pid/99/3602.html#j90) [\[c71\]](https://dblp.org/pid/99/3602.html#c71) [\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[i18\]](https://dblp.org/pid/99/3602.html#i18) [\[c63\]](https://dblp.org/pid/99/3602.html#c63) [\[c62\]](https://dblp.org/pid/99/3602.html#c62) [\[c61\]](https://dblp.org/pid/99/3602.html#c61) [\[i10\]](https://dblp.org/pid/99/3602.html#i10) [\[c58\]](https://dblp.org/pid/99/3602.html#c58) [\[i9\]](https://dblp.org/pid/99/3602.html#i9)

[437](https://dblp.org/pid/99/3602.html?view=joint&param=437 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jin Xie](https://dblp.org/pid/80/1949.html)

[\[j86\]](https://dblp.org/pid/99/3602.html#j86) [\[i15\]](https://dblp.org/pid/99/3602.html#i15)

[438](https://dblp.org/pid/99/3602.html?view=joint&param=438 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ke Xie 0004](https://dblp.org/pid/44/2171-4.html)

[\[c41\]](https://dblp.org/pid/99/3602.html#c41)

[439](https://dblp.org/pid/99/3602.html?view=joint&param=439 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Liping Xie](https://dblp.org/pid/91/7400.html)

[\[j117\]](https://dblp.org/pid/99/3602.html#j117) [\[j107\]](https://dblp.org/pid/99/3602.html#j107) [\[i17\]](https://dblp.org/pid/99/3602.html#i17)

[440](https://dblp.org/pid/99/3602.html?view=joint&param=440 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ning Xie 0003](https://dblp.org/pid/55/4104-3.html)

[\[c30\]](https://dblp.org/pid/99/3602.html#c30)

[441](https://dblp.org/pid/99/3602.html?view=joint&param=441 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Junliang Xing](https://dblp.org/pid/43/7659.html)

[\[j35\]](https://dblp.org/pid/99/3602.html#j35)

[442](https://dblp.org/pid/99/3602.html?view=joint&param=442 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ming Xiong](https://dblp.org/pid/x/MingXiong.html)

[\[c10\]](https://dblp.org/pid/99/3602.html#c10)

[443](https://dblp.org/pid/99/3602.html?view=joint&param=443 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chang Xu 0002](https://dblp.org/pid/97/2966-2.html)

[\[j67\]](https://dblp.org/pid/99/3602.html#j67) [\[j55\]](https://dblp.org/pid/99/3602.html#j55) [\[i5\]](https://dblp.org/pid/99/3602.html#i5) [\[j45\]](https://dblp.org/pid/99/3602.html#j45) [\[j40\]](https://dblp.org/pid/99/3602.html#j40) [\[j35\]](https://dblp.org/pid/99/3602.html#j35)

[444](https://dblp.org/pid/99/3602.html?view=joint&param=444 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chenghao Xu](https://dblp.org/pid/254/6051.html)

[\[c80\]](https://dblp.org/pid/99/3602.html#c80)

[445](https://dblp.org/pid/99/3602.html?view=joint&param=445 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chunyan Xu](https://dblp.org/pid/70/8453.html)

[\[j108\]](https://dblp.org/pid/99/3602.html#j108)

[446](https://dblp.org/pid/99/3602.html?view=joint&param=446 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Fenglei Xu](https://dblp.org/pid/230/6532.html)

[\[j115\]](https://dblp.org/pid/99/3602.html#j115) [\[c49\]](https://dblp.org/pid/99/3602.html#c49)

[447](https://dblp.org/pid/99/3602.html?view=joint&param=447 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jianhua Xu](https://dblp.org/pid/57/6846.html)

[\[j102\]](https://dblp.org/pid/99/3602.html#j102) [\[i28\]](https://dblp.org/pid/99/3602.html#i28) [\[j94\]](https://dblp.org/pid/99/3602.html#j94) [\[j81\]](https://dblp.org/pid/99/3602.html#j81) [\[j76\]](https://dblp.org/pid/99/3602.html#j76) [\[j67\]](https://dblp.org/pid/99/3602.html#j67)

[448](https://dblp.org/pid/99/3602.html?view=joint&param=448 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lin-Tao Xu](https://dblp.org/pid/354/1298.html)

[\[j96\]](https://dblp.org/pid/99/3602.html#j96)

[449](https://dblp.org/pid/99/3602.html?view=joint&param=449 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Richard Y. D. Xu](https://dblp.org/pid/38/3064.html)

aka: Richard Yi Da Xu

[\[j52\]](https://dblp.org/pid/99/3602.html#j52)

[450](https://dblp.org/pid/99/3602.html?view=joint&param=450 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[j148\]](https://dblp.org/pid/99/3602.html#j148) [\[j119\]](https://dblp.org/pid/99/3602.html#j119) [\[c81\]](https://dblp.org/pid/99/3602.html#c81) [\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[451](https://dblp.org/pid/99/3602.html?view=joint&param=451 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wei Xu 0017](https://dblp.org/pid/32/1213-17.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[452](https://dblp.org/pid/99/3602.html?view=joint&param=452 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiang Xu](https://dblp.org/pid/126/2962.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[453](https://dblp.org/pid/99/3602.html?view=joint&param=453 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yihao Xu](https://dblp.org/pid/254/1616.html)

[\[j145\]](https://dblp.org/pid/99/3602.html#j145) [\[j125\]](https://dblp.org/pid/99/3602.html#j125) [\[j120\]](https://dblp.org/pid/99/3602.html#j120) [\[c79\]](https://dblp.org/pid/99/3602.html#c79) [\[i30\]](https://dblp.org/pid/99/3602.html#i30)

[454](https://dblp.org/pid/99/3602.html?view=joint&param=454 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yixin Xu](https://dblp.org/pid/04/5753.html)

[\[j139\]](https://dblp.org/pid/99/3602.html#j139) [\[c81\]](https://dblp.org/pid/99/3602.html#c81)

[455](https://dblp.org/pid/99/3602.html?view=joint&param=455 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yong Xu 0007](https://dblp.org/pid/07/4630-7.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[456](https://dblp.org/pid/99/3602.html?view=joint&param=456 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yuanyou Xu](https://dblp.org/pid/248/7663.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[457](https://dblp.org/pid/99/3602.html?view=joint&param=457 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yuanze Xu](https://dblp.org/pid/400/0032.html)

[\[c82\]](https://dblp.org/pid/99/3602.html#c82) [\[i46\]](https://dblp.org/pid/99/3602.html#i46)

[458](https://dblp.org/pid/99/3602.html?view=joint&param=458 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61) [\[i9\]](https://dblp.org/pid/99/3602.html#i9)

[459](https://dblp.org/pid/99/3602.html?view=joint&param=459 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zizheng Xun](https://dblp.org/pid/340/1441.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[460](https://dblp.org/pid/99/3602.html?view=joint&param=460 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[461](https://dblp.org/pid/99/3602.html?view=joint&param=461 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hui Yan](https://dblp.org/pid/95/4747.html)

[\[c5\]](https://dblp.org/pid/99/3602.html#c5) [\[c2\]](https://dblp.org/pid/99/3602.html#c2)

[462](https://dblp.org/pid/99/3602.html?view=joint&param=462 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[463](https://dblp.org/pid/99/3602.html?view=joint&param=463 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaoyong Yan](https://dblp.org/pid/70/8665.html)

[\[j29\]](https://dblp.org/pid/99/3602.html#j29) [\[j28\]](https://dblp.org/pid/99/3602.html#j28) [\[j7\]](https://dblp.org/pid/99/3602.html#j7)

[464](https://dblp.org/pid/99/3602.html?view=joint&param=464 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yunyang Yan](https://dblp.org/pid/11/4039.html)

[\[j140\]](https://dblp.org/pid/99/3602.html#j140)

[465](https://dblp.org/pid/99/3602.html?view=joint&param=465 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bo Yang 0019](https://dblp.org/pid/46/999-19.html)

[\[j76\]](https://dblp.org/pid/99/3602.html#j76) [\[c52\]](https://dblp.org/pid/99/3602.html#c52)

[466](https://dblp.org/pid/99/3602.html?view=joint&param=466 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dawei Yang](https://dblp.org/pid/22/1038.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[467](https://dblp.org/pid/99/3602.html?view=joint&param=467 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guowei Yang 0002](https://dblp.org/pid/43/3366-2.html)

[\[j84\]](https://dblp.org/pid/99/3602.html#j84) [\[j53\]](https://dblp.org/pid/99/3602.html#j53)

[468](https://dblp.org/pid/99/3602.html?view=joint&param=468 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jian Yang 0003](https://dblp.org/pid/y/JianYang3.html)

[\[j41\]](https://dblp.org/pid/99/3602.html#j41) [\[c21\]](https://dblp.org/pid/99/3602.html#c21) [\[c5\]](https://dblp.org/pid/99/3602.html#c5)

[469](https://dblp.org/pid/99/3602.html?view=joint&param=469 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jing-Yu Yang 0001](https://dblp.org/pid/65/2850-1.html)

aka: Jingyu Yang 0001

aka: Jing-yu Yang 0001

[\[j51\]](https://dblp.org/pid/99/3602.html#j51) [\[j16\]](https://dblp.org/pid/99/3602.html#j16) [\[j10\]](https://dblp.org/pid/99/3602.html#j10) [\[j9\]](https://dblp.org/pid/99/3602.html#j9) [\[j5\]](https://dblp.org/pid/99/3602.html#j5) [\[j4\]](https://dblp.org/pid/99/3602.html#j4) [\[c5\]](https://dblp.org/pid/99/3602.html#c5) [\[j3\]](https://dblp.org/pid/99/3602.html#j3) [\[j2\]](https://dblp.org/pid/99/3602.html#j2) [\[c4\]](https://dblp.org/pid/99/3602.html#c4) [\[c3\]](https://dblp.org/pid/99/3602.html#c3) [\[c2\]](https://dblp.org/pid/99/3602.html#c2) [\[c1\]](https://dblp.org/pid/99/3602.html#c1) [\[j1\]](https://dblp.org/pid/99/3602.html#j1)

[470](https://dblp.org/pid/99/3602.html?view=joint&param=470 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[471](https://dblp.org/pid/99/3602.html?view=joint&param=471 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lingfeng Yang](https://dblp.org/pid/45/7593.html)

[\[j147\]](https://dblp.org/pid/99/3602.html#j147) [\[j146\]](https://dblp.org/pid/99/3602.html#j146) [\[i39\]](https://dblp.org/pid/99/3602.html#i39) [\[c79\]](https://dblp.org/pid/99/3602.html#c79) [\[i30\]](https://dblp.org/pid/99/3602.html#i30)

[472](https://dblp.org/pid/99/3602.html?view=joint&param=472 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Linlin Yang](https://dblp.org/pid/84/6484.html)

[\[c38\]](https://dblp.org/pid/99/3602.html#c38) [\[c36\]](https://dblp.org/pid/99/3602.html#c36)

[473](https://dblp.org/pid/99/3602.html?view=joint&param=473 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Meng Yang 0001](https://dblp.org/pid/44/2761-1.html)

[\[j72\]](https://dblp.org/pid/99/3602.html#j72)

[474](https://dblp.org/pid/99/3602.html?view=joint&param=474 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Sen Yang](https://dblp.org/pid/90/4655.html)

[\[j143\]](https://dblp.org/pid/99/3602.html#j143) [\[c84\]](https://dblp.org/pid/99/3602.html#c84) [\[i44\]](https://dblp.org/pid/99/3602.html#i44) [\[i43\]](https://dblp.org/pid/99/3602.html#i43) [\[i38\]](https://dblp.org/pid/99/3602.html#i38) [\[i36\]](https://dblp.org/pid/99/3602.html#i36) [\[i31\]](https://dblp.org/pid/99/3602.html#i31) [\[j103\]](https://dblp.org/pid/99/3602.html#j103) [\[j99\]](https://dblp.org/pid/99/3602.html#j99) [\[c76\]](https://dblp.org/pid/99/3602.html#c76) [\[c73\]](https://dblp.org/pid/99/3602.html#c73) [\[i27\]](https://dblp.org/pid/99/3602.html#i27) [\[i21\]](https://dblp.org/pid/99/3602.html#i21) [\[j87\]](https://dblp.org/pid/99/3602.html#j87) [\[c70\]](https://dblp.org/pid/99/3602.html#c70) [\[c65\]](https://dblp.org/pid/99/3602.html#c65) [\[c64\]](https://dblp.org/pid/99/3602.html#c64) [\[i14\]](https://dblp.org/pid/99/3602.html#i14) [\[i13\]](https://dblp.org/pid/99/3602.html#i13) [\[i11\]](https://dblp.org/pid/99/3602.html#i11) [\[i8\]](https://dblp.org/pid/99/3602.html#i8) [\[j62\]](https://dblp.org/pid/99/3602.html#j62) [\[i7\]](https://dblp.org/pid/99/3602.html#i7)

[475](https://dblp.org/pid/99/3602.html?view=joint&param=475 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wenyan Yang](https://dblp.org/pid/119/2426.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[476](https://dblp.org/pid/99/3602.html?view=joint&param=476 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[477](https://dblp.org/pid/99/3602.html?view=joint&param=477 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xibei Yang](https://dblp.org/pid/53/779.html)

[\[j33\]](https://dblp.org/pid/99/3602.html#j33) [\[j24\]](https://dblp.org/pid/99/3602.html#j24) [\[j23\]](https://dblp.org/pid/99/3602.html#j23)

[478](https://dblp.org/pid/99/3602.html?view=joint&param=478 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yi Yang 0001](https://dblp.org/pid/33/4854-1.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[479](https://dblp.org/pid/99/3602.html?view=joint&param=479 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yichun Yang](https://dblp.org/pid/249/9678.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[480](https://dblp.org/pid/99/3602.html?view=joint&param=480 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yun Yang](https://dblp.org/pid/90/3406.html)

[\[c38\]](https://dblp.org/pid/99/3602.html#c38)

[481](https://dblp.org/pid/99/3602.html?view=joint&param=481 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhong Yang](https://dblp.org/pid/46/2248.html)

[\[j29\]](https://dblp.org/pid/99/3602.html#j29) [\[j28\]](https://dblp.org/pid/99/3602.html#j28)

[482](https://dblp.org/pid/99/3602.html?view=joint&param=482 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zongxin Yang](https://dblp.org/pid/249/5456.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[483](https://dblp.org/pid/99/3602.html?view=joint&param=483 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lingxiang Yao](https://dblp.org/pid/207/9512.html)

[\[j78\]](https://dblp.org/pid/99/3602.html#j78)

[484](https://dblp.org/pid/99/3602.html?view=joint&param=484 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yazhou Yao](https://dblp.org/pid/173/6775.html)

[\[j79\]](https://dblp.org/pid/99/3602.html#j79) [\[c60\]](https://dblp.org/pid/99/3602.html#c60) [\[c59\]](https://dblp.org/pid/99/3602.html#c59) [\[j64\]](https://dblp.org/pid/99/3602.html#j64) [\[j60\]](https://dblp.org/pid/99/3602.html#j60) [\[c55\]](https://dblp.org/pid/99/3602.html#c55) [\[c53\]](https://dblp.org/pid/99/3602.html#c53) [\[i4\]](https://dblp.org/pid/99/3602.html#i4)

[485](https://dblp.org/pid/99/3602.html?view=joint&param=485 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yuncong Yao](https://dblp.org/pid/17/5361.html)

[\[j145\]](https://dblp.org/pid/99/3602.html#j145) [\[j114\]](https://dblp.org/pid/99/3602.html#j114) [\[j90\]](https://dblp.org/pid/99/3602.html#j90) [\[j86\]](https://dblp.org/pid/99/3602.html#j86) [\[j80\]](https://dblp.org/pid/99/3602.html#j80) [\[i15\]](https://dblp.org/pid/99/3602.html#i15) [\[c58\]](https://dblp.org/pid/99/3602.html#c58)

[486](https://dblp.org/pid/99/3602.html?view=joint&param=486 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Botao Ye](https://dblp.org/pid/227/4610.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[487](https://dblp.org/pid/99/3602.html?view=joint&param=487 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Junjie Ye 0002](https://dblp.org/pid/19/8588-2.html)

[\[i26\]](https://dblp.org/pid/99/3602.html#i26)

[488](https://dblp.org/pid/99/3602.html?view=joint&param=488 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qiaolin Ye](https://dblp.org/pid/44/7694.html)

[\[j129\]](https://dblp.org/pid/99/3602.html#j129) [\[j89\]](https://dblp.org/pid/99/3602.html#j89) [\[j88\]](https://dblp.org/pid/99/3602.html#j88) [\[j85\]](https://dblp.org/pid/99/3602.html#j85) [\[j84\]](https://dblp.org/pid/99/3602.html#j84) [\[j53\]](https://dblp.org/pid/99/3602.html#j53)

[489](https://dblp.org/pid/99/3602.html?view=joint&param=489 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaoqing Ye](https://dblp.org/pid/177/0181.html)

[\[c84\]](https://dblp.org/pid/99/3602.html#c84) [\[i32\]](https://dblp.org/pid/99/3602.html#i32) [\[i31\]](https://dblp.org/pid/99/3602.html#i31)

[490](https://dblp.org/pid/99/3602.html?view=joint&param=490 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xinfu Ye](https://dblp.org/pid/138/2054.html)

[\[c25\]](https://dblp.org/pid/99/3602.html#c25)

[491](https://dblp.org/pid/99/3602.html?view=joint&param=491 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yu Ye 0004](https://dblp.org/pid/129/0969-4.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[492](https://dblp.org/pid/99/3602.html?view=joint&param=492 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Weilin Yi](https://dblp.org/pid/253/6460.html)

[\[j101\]](https://dblp.org/pid/99/3602.html#j101)

[493](https://dblp.org/pid/99/3602.html?view=joint&param=493 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hang Yin](https://dblp.org/pid/81/7626.html)

[\[j84\]](https://dblp.org/pid/99/3602.html#j84)

[494](https://dblp.org/pid/99/3602.html?view=joint&param=494 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[J. Yin](https://dblp.org/pid/51/2242.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[495](https://dblp.org/pid/99/3602.html?view=joint&param=495 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jun Yin 0003](https://dblp.org/pid/58/5423-3.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61) [\[j17\]](https://dblp.org/pid/99/3602.html#j17) [\[c26\]](https://dblp.org/pid/99/3602.html#c26) [\[j14\]](https://dblp.org/pid/99/3602.html#j14)

[496](https://dblp.org/pid/99/3602.html?view=joint&param=496 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ruoyan Yin](https://dblp.org/pid/395/6967.html)

[\[j144\]](https://dblp.org/pid/99/3602.html#j144) [\[i29\]](https://dblp.org/pid/99/3602.html#i29)

[497](https://dblp.org/pid/99/3602.html?view=joint&param=497 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Baosheng Yu](https://dblp.org/pid/178/8725.html)

[\[j112\]](https://dblp.org/pid/99/3602.html#j112)

[498](https://dblp.org/pid/99/3602.html?view=joint&param=498 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Fisher Yu 0001](https://dblp.org/pid/117/6314.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[499](https://dblp.org/pid/99/3602.html?view=joint&param=499 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Gang Yu 0002](https://dblp.org/pid/75/1683-2.html)

[\[c73\]](https://dblp.org/pid/99/3602.html#c73) [\[i27\]](https://dblp.org/pid/99/3602.html#i27)

[500](https://dblp.org/pid/99/3602.html?view=joint&param=500 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hongyuan Yu](https://dblp.org/pid/232/2265.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[501](https://dblp.org/pid/99/3602.html?view=joint&param=501 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hualong Yu](https://dblp.org/pid/13/4009.html)

[\[j36\]](https://dblp.org/pid/99/3602.html#j36) [\[j33\]](https://dblp.org/pid/99/3602.html#j33) [\[j24\]](https://dblp.org/pid/99/3602.html#j24) [\[j23\]](https://dblp.org/pid/99/3602.html#j23) [\[c32\]](https://dblp.org/pid/99/3602.html#c32)

[502](https://dblp.org/pid/99/3602.html?view=joint&param=502 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiaqian Yu](https://dblp.org/pid/164/7325.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[503](https://dblp.org/pid/99/3602.html?view=joint&param=503 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qianjin Yu](https://dblp.org/pid/53/10179.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[504](https://dblp.org/pid/99/3602.html?view=joint&param=504 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tianbao Yu](https://dblp.org/pid/331/0776.html)

[\[j92\]](https://dblp.org/pid/99/3602.html#j92)

[505](https://dblp.org/pid/99/3602.html?view=joint&param=505 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Weichen Yu](https://dblp.org/pid/325/1209.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[506](https://dblp.org/pid/99/3602.html?view=joint&param=506 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yunxiu Yu](https://dblp.org/pid/211/9450.html)

[\[j66\]](https://dblp.org/pid/99/3602.html#j66)

[507](https://dblp.org/pid/99/3602.html?view=joint&param=507 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chunfeng Yuan](https://dblp.org/pid/47/2506.html)

[\[j112\]](https://dblp.org/pid/99/3602.html#j112) [\[j49\]](https://dblp.org/pid/99/3602.html#j49) [\[j47\]](https://dblp.org/pid/99/3602.html#j47) [\[j18\]](https://dblp.org/pid/99/3602.html#j18)

[508](https://dblp.org/pid/99/3602.html?view=joint&param=508 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jianhao Yuan](https://dblp.org/pid/336/7530.html)

[\[c83\]](https://dblp.org/pid/99/3602.html#c83) [\[i33\]](https://dblp.org/pid/99/3602.html#i33)

[509](https://dblp.org/pid/99/3602.html?view=joint&param=509 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaohui Yuan 0001](https://dblp.org/pid/61/623-1.html)

[\[j142\]](https://dblp.org/pid/99/3602.html#j142) [\[i40\]](https://dblp.org/pid/99/3602.html#i40)

[510](https://dblp.org/pid/99/3602.html?view=joint&param=510 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yun-Hao Yuan 0001](https://dblp.org/pid/51/7436.html)

[\[j82\]](https://dblp.org/pid/99/3602.html#j82)

[511](https://dblp.org/pid/99/3602.html?view=joint&param=511 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dong Yue 0001](https://dblp.org/pid/72/4106-1.html)

[\[j41\]](https://dblp.org/pid/99/3602.html#j41) [\[c50\]](https://dblp.org/pid/99/3602.html#c50)

[512](https://dblp.org/pid/99/3602.html?view=joint&param=512 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Kai Zang](https://dblp.org/pid/205/8078.html)

[\[c45\]](https://dblp.org/pid/99/3602.html#c45)

[513](https://dblp.org/pid/99/3602.html?view=joint&param=513 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Kang Ze](https://dblp.org/pid/340/1107.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[514](https://dblp.org/pid/99/3602.html?view=joint&param=514 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Weili Zeng](https://dblp.org/pid/86/11483.html)

[\[j118\]](https://dblp.org/pid/99/3602.html#j118) [\[j66\]](https://dblp.org/pid/99/3602.html#j66)

[515](https://dblp.org/pid/99/3602.html?view=joint&param=515 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wenjun Zeng 0001](https://dblp.org/pid/57/145.html)

[\[j124\]](https://dblp.org/pid/99/3602.html#j124) [\[i35\]](https://dblp.org/pid/99/3602.html#i35) [\[i25\]](https://dblp.org/pid/99/3602.html#i25) [\[c71\]](https://dblp.org/pid/99/3602.html#c71) [\[i18\]](https://dblp.org/pid/99/3602.html#i18) [\[c62\]](https://dblp.org/pid/99/3602.html#c62) [\[i10\]](https://dblp.org/pid/99/3602.html#i10)

[516](https://dblp.org/pid/99/3602.html?view=joint&param=516 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiang Zhai](https://dblp.org/pid/291/9340.html)

[\[j127\]](https://dblp.org/pid/99/3602.html#j127) [\[j119\]](https://dblp.org/pid/99/3602.html#j119) [\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[517](https://dblp.org/pid/99/3602.html?view=joint&param=517 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Mingliang Zhai](https://dblp.org/pid/221/3748.html)

[\[j101\]](https://dblp.org/pid/99/3602.html#j101)

[518](https://dblp.org/pid/99/3602.html?view=joint&param=518 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Haibo Zhan](https://dblp.org/pid/413/3286.html)

[\[j149\]](https://dblp.org/pid/99/3602.html#j149) [\[j142\]](https://dblp.org/pid/99/3602.html#j142) [\[j131\]](https://dblp.org/pid/99/3602.html#j131) [\[i42\]](https://dblp.org/pid/99/3602.html#i42) [\[i40\]](https://dblp.org/pid/99/3602.html#i40) [\[i37\]](https://dblp.org/pid/99/3602.html#i37)

[519](https://dblp.org/pid/99/3602.html?view=joint&param=519 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yibing Zhan](https://dblp.org/pid/142/8486.html)

[\[j112\]](https://dblp.org/pid/99/3602.html#j112)

[520](https://dblp.org/pid/99/3602.html?view=joint&param=520 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Baochang Zhang 0001](https://dblp.org/pid/80/3887-1.html)

[\[j103\]](https://dblp.org/pid/99/3602.html#j103) [\[j68\]](https://dblp.org/pid/99/3602.html#j68) [\[j58\]](https://dblp.org/pid/99/3602.html#j58) [\[c51\]](https://dblp.org/pid/99/3602.html#c51) [\[j46\]](https://dblp.org/pid/99/3602.html#j46) [\[j39\]](https://dblp.org/pid/99/3602.html#j39) [\[j34\]](https://dblp.org/pid/99/3602.html#j34) [\[c43\]](https://dblp.org/pid/99/3602.html#c43) [\[c42\]](https://dblp.org/pid/99/3602.html#c42) [\[c41\]](https://dblp.org/pid/99/3602.html#c41) [\[c38\]](https://dblp.org/pid/99/3602.html#c38) [\[c37\]](https://dblp.org/pid/99/3602.html#c37) [\[c36\]](https://dblp.org/pid/99/3602.html#c36) [\[c35\]](https://dblp.org/pid/99/3602.html#c35) [\[c29\]](https://dblp.org/pid/99/3602.html#c29) [\[c27\]](https://dblp.org/pid/99/3602.html#c27)

[521](https://dblp.org/pid/99/3602.html?view=joint&param=521 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[522](https://dblp.org/pid/99/3602.html?view=joint&param=522 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chuankai Zhang](https://dblp.org/pid/244/6871.html)

[\[j135\]](https://dblp.org/pid/99/3602.html#j135)

[523](https://dblp.org/pid/99/3602.html?view=joint&param=523 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chunhu Zhang](https://dblp.org/pid/292/0953.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[524](https://dblp.org/pid/99/3602.html?view=joint&param=524 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[525](https://dblp.org/pid/99/3602.html?view=joint&param=525 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Fei Zhang](https://dblp.org/pid/16/5105.html)

[\[j113\]](https://dblp.org/pid/99/3602.html#j113) [\[i26\]](https://dblp.org/pid/99/3602.html#i26)

[526](https://dblp.org/pid/99/3602.html?view=joint&param=526 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Guobao Zhang](https://dblp.org/pid/25/2971.html)

[\[j91\]](https://dblp.org/pid/99/3602.html#j91)

[527](https://dblp.org/pid/99/3602.html?view=joint&param=527 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Haitao Zhang](https://dblp.org/pid/19/6669.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[528](https://dblp.org/pid/99/3602.html?view=joint&param=528 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hanjin Zhang](https://dblp.org/pid/214/5921.html)

[\[j117\]](https://dblp.org/pid/99/3602.html#j117)

[529](https://dblp.org/pid/99/3602.html?view=joint&param=529 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hanwang Zhang](https://dblp.org/pid/79/8116.html)

[\[j32\]](https://dblp.org/pid/99/3602.html#j32) [\[c30\]](https://dblp.org/pid/99/3602.html#c30)

[530](https://dblp.org/pid/99/3602.html?view=joint&param=530 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Haofeng Zhang 0001](https://dblp.org/pid/17/4297.html)

[\[j140\]](https://dblp.org/pid/99/3602.html#j140) [\[j129\]](https://dblp.org/pid/99/3602.html#j129) [\[j128\]](https://dblp.org/pid/99/3602.html#j128) [\[j93\]](https://dblp.org/pid/99/3602.html#j93) [\[j89\]](https://dblp.org/pid/99/3602.html#j89) [\[j88\]](https://dblp.org/pid/99/3602.html#j88) [\[j65\]](https://dblp.org/pid/99/3602.html#j65) [\[j64\]](https://dblp.org/pid/99/3602.html#j64) [\[j63\]](https://dblp.org/pid/99/3602.html#j63)

[531](https://dblp.org/pid/99/3602.html?view=joint&param=531 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hong Zhang 0013](https://dblp.org/pid/24/6914-13.html)

[\[j67\]](https://dblp.org/pid/99/3602.html#j67) [\[c52\]](https://dblp.org/pid/99/3602.html#c52) [\[i5\]](https://dblp.org/pid/99/3602.html#i5)

[532](https://dblp.org/pid/99/3602.html?view=joint&param=532 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jian Zhang 0002](https://dblp.org/pid/07/314-2.html)

[\[j78\]](https://dblp.org/pid/99/3602.html#j78) [\[c55\]](https://dblp.org/pid/99/3602.html#c55) [\[c53\]](https://dblp.org/pid/99/3602.html#c53) [\[i4\]](https://dblp.org/pid/99/3602.html#i4)

[533](https://dblp.org/pid/99/3602.html?view=joint&param=533 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jinxia Zhang](https://dblp.org/pid/89/1778.html)

[\[j51\]](https://dblp.org/pid/99/3602.html#j51) [\[c44\]](https://dblp.org/pid/99/3602.html#c44)

[534](https://dblp.org/pid/99/3602.html?view=joint&param=534 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c63\]](https://dblp.org/pid/99/3602.html#c63) [\[c61\]](https://dblp.org/pid/99/3602.html#c61) [\[c58\]](https://dblp.org/pid/99/3602.html#c58) [\[i9\]](https://dblp.org/pid/99/3602.html#i9)

[535](https://dblp.org/pid/99/3602.html?view=joint&param=535 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Kan-Jian Zhang](https://dblp.org/pid/93/1517.html)

aka: Kanjian Zhang

[\[j107\]](https://dblp.org/pid/99/3602.html#j107) [\[i17\]](https://dblp.org/pid/99/3602.html#i17) [\[j51\]](https://dblp.org/pid/99/3602.html#j51)

[536](https://dblp.org/pid/99/3602.html?view=joint&param=536 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Kangkai Zhang](https://dblp.org/pid/260/2990.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[537](https://dblp.org/pid/99/3602.html?view=joint&param=537 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lei Zhang 0006](https://dblp.org/pid/64/5666-6.html)

[\[j8\]](https://dblp.org/pid/99/3602.html#j8) [\[j7\]](https://dblp.org/pid/99/3602.html#j7) [\[j6\]](https://dblp.org/pid/99/3602.html#j6) [\[c7\]](https://dblp.org/pid/99/3602.html#c7) [\[j5\]](https://dblp.org/pid/99/3602.html#j5) [\[j4\]](https://dblp.org/pid/99/3602.html#j4)

[538](https://dblp.org/pid/99/3602.html?view=joint&param=538 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Mingxing Zhang](https://dblp.org/pid/153/5382.html)

[\[c30\]](https://dblp.org/pid/99/3602.html#c30)

[539](https://dblp.org/pid/99/3602.html?view=joint&param=539 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shen Zhang](https://dblp.org/pid/62/6204.html)

[\[j135\]](https://dblp.org/pid/99/3602.html#j135)

[540](https://dblp.org/pid/99/3602.html?view=joint&param=540 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shengping Zhang](https://dblp.org/pid/60/1866.html)

[\[j39\]](https://dblp.org/pid/99/3602.html#j39)

[541](https://dblp.org/pid/99/3602.html?view=joint&param=541 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shoukui Zhang](https://dblp.org/pid/289/7121.html)

[\[j99\]](https://dblp.org/pid/99/3602.html#j99) [\[c70\]](https://dblp.org/pid/99/3602.html#c70) [\[c65\]](https://dblp.org/pid/99/3602.html#c65) [\[i14\]](https://dblp.org/pid/99/3602.html#i14) [\[i13\]](https://dblp.org/pid/99/3602.html#i13) [\[i11\]](https://dblp.org/pid/99/3602.html#i11)

[542](https://dblp.org/pid/99/3602.html?view=joint&param=542 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tianzhu Zhang 0001](https://dblp.org/pid/15/7643-1.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[543](https://dblp.org/pid/99/3602.html?view=joint&param=543 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Tong Zhang 0021](https://dblp.org/pid/07/4227-21.html)

[\[j54\]](https://dblp.org/pid/99/3602.html#j54)

[544](https://dblp.org/pid/99/3602.html?view=joint&param=544 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wenkang Zhang](https://dblp.org/pid/340/0966.html)

[\[j148\]](https://dblp.org/pid/99/3602.html#j148) [\[j137\]](https://dblp.org/pid/99/3602.html#j137) [\[j127\]](https://dblp.org/pid/99/3602.html#j127) [\[j119\]](https://dblp.org/pid/99/3602.html#j119) [\[c81\]](https://dblp.org/pid/99/3602.html#c81) [\[j108\]](https://dblp.org/pid/99/3602.html#j108) [\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[545](https://dblp.org/pid/99/3602.html?view=joint&param=545 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wenyao Zhang](https://dblp.org/pid/86/2144.html)

[\[i25\]](https://dblp.org/pid/99/3602.html#i25)

[546](https://dblp.org/pid/99/3602.html?view=joint&param=546 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xian Zhang](https://dblp.org/pid/56/5624.html)

[\[c85\]](https://dblp.org/pid/99/3602.html#c85) [\[i47\]](https://dblp.org/pid/99/3602.html#i47) [\[j121\]](https://dblp.org/pid/99/3602.html#j121) [\[j104\]](https://dblp.org/pid/99/3602.html#j104) [\[j100\]](https://dblp.org/pid/99/3602.html#j100) [\[i26\]](https://dblp.org/pid/99/3602.html#i26) [\[j74\]](https://dblp.org/pid/99/3602.html#j74) [\[c57\]](https://dblp.org/pid/99/3602.html#c57)

[547](https://dblp.org/pid/99/3602.html?view=joint&param=547 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaohan Zhang](https://dblp.org/pid/96/6053.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[548](https://dblp.org/pid/99/3602.html?view=joint&param=548 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiaolin Zhang](https://dblp.org/pid/99/2516.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[549](https://dblp.org/pid/99/3602.html?view=joint&param=549 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xinyu Zhang 0020](https://dblp.org/pid/58/4582-20.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[550](https://dblp.org/pid/99/3602.html?view=joint&param=550 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yan Zhang](https://dblp.org/pid/04/3348.html)

[\[c19\]](https://dblp.org/pid/99/3602.html#c19) [\[c15\]](https://dblp.org/pid/99/3602.html#c15)

[551](https://dblp.org/pid/99/3602.html?view=joint&param=551 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yudong Zhang 0001](https://dblp.org/pid/39/2699-1.html)

[\[c46\]](https://dblp.org/pid/99/3602.html#c46)

[552](https://dblp.org/pid/99/3602.html?view=joint&param=552 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yushan Zhang](https://dblp.org/pid/50/10702.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[553](https://dblp.org/pid/99/3602.html?view=joint&param=553 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhao Zhang 0001](https://dblp.org/pid/87/6853-1.html)

[\[j85\]](https://dblp.org/pid/99/3602.html#j85) [\[j53\]](https://dblp.org/pid/99/3602.html#j53)

[554](https://dblp.org/pid/99/3602.html?view=joint&param=554 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zheng Zhang 0006](https://dblp.org/pid/181/2621-6.html)

[\[j140\]](https://dblp.org/pid/99/3602.html#j140) [\[j128\]](https://dblp.org/pid/99/3602.html#j128) [\[j88\]](https://dblp.org/pid/99/3602.html#j88)

[555](https://dblp.org/pid/99/3602.html?view=joint&param=555 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[556](https://dblp.org/pid/99/3602.html?view=joint&param=556 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhipeng Zhang](https://dblp.org/pid/49/4941.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[557](https://dblp.org/pid/99/3602.html?view=joint&param=557 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[558](https://dblp.org/pid/99/3602.html?view=joint&param=558 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bo Zhao 0037](https://dblp.org/pid/94/4810-37.html)

[\[c83\]](https://dblp.org/pid/99/3602.html#c83) [\[i33\]](https://dblp.org/pid/99/3602.html#i33)

[559](https://dblp.org/pid/99/3602.html?view=joint&param=559 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dandan Zhao](https://dblp.org/pid/72/7814.html)

[\[c31\]](https://dblp.org/pid/99/3602.html#c31)

[560](https://dblp.org/pid/99/3602.html?view=joint&param=560 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Haifeng Zhao](https://dblp.org/pid/17/5245.html)

[\[j110\]](https://dblp.org/pid/99/3602.html#j110)

[561](https://dblp.org/pid/99/3602.html?view=joint&param=561 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hongshen Zhao](https://dblp.org/pid/373/4477.html)

[\[i41\]](https://dblp.org/pid/99/3602.html#i41)

[562](https://dblp.org/pid/99/3602.html?view=joint&param=562 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jie Zhao 0014](https://dblp.org/pid/23/3168-14.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[563](https://dblp.org/pid/99/3602.html?view=joint&param=563 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Junsheng Zhao](https://dblp.org/pid/132/1767.html)

[\[j107\]](https://dblp.org/pid/99/3602.html#j107)

[564](https://dblp.org/pid/99/3602.html?view=joint&param=564 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[565](https://dblp.org/pid/99/3602.html?view=joint&param=565 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ting Zhao](https://dblp.org/pid/34/528.html)

[\[c17\]](https://dblp.org/pid/99/3602.html#c17)

[566](https://dblp.org/pid/99/3602.html?view=joint&param=566 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhenyu Zhao](https://dblp.org/pid/26/7695.html)

[\[j135\]](https://dblp.org/pid/99/3602.html#j135)

[567](https://dblp.org/pid/99/3602.html?view=joint&param=567 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ming Zhen](https://dblp.org/pid/307/8430.html)

[\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[568](https://dblp.org/pid/99/3602.html?view=joint&param=568 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xiantong Zhen](https://dblp.org/pid/78/10651.html)

[\[j68\]](https://dblp.org/pid/99/3602.html#j68) [\[j58\]](https://dblp.org/pid/99/3602.html#j58)

[569](https://dblp.org/pid/99/3602.html?view=joint&param=569 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Enhui Zheng](https://dblp.org/pid/138/8144.html)

[\[j141\]](https://dblp.org/pid/99/3602.html#j141) [\[j116\]](https://dblp.org/pid/99/3602.html#j116)

[570](https://dblp.org/pid/99/3602.html?view=joint&param=570 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Feng Zheng 0001](https://dblp.org/pid/39/800-1.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[571](https://dblp.org/pid/99/3602.html?view=joint&param=571 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Haixia Zheng](https://dblp.org/pid/119/1585.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[572](https://dblp.org/pid/99/3602.html?view=joint&param=572 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Hao Zheng](https://dblp.org/pid/31/6916.html)

[\[j52\]](https://dblp.org/pid/99/3602.html#j52) [\[c43\]](https://dblp.org/pid/99/3602.html#c43) [\[c41\]](https://dblp.org/pid/99/3602.html#c41)

[573](https://dblp.org/pid/99/3602.html?view=joint&param=573 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Leibo Zheng](https://dblp.org/pid/239/7320.html)

[\[j92\]](https://dblp.org/pid/99/3602.html#j92)

[574](https://dblp.org/pid/99/3602.html?view=joint&param=574 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Min Zheng](https://dblp.org/pid/23/328.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[575](https://dblp.org/pid/99/3602.html?view=joint&param=575 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wenming Zheng](https://dblp.org/pid/64/2253.html)

[\[j54\]](https://dblp.org/pid/99/3602.html#j54) [\[j44\]](https://dblp.org/pid/99/3602.html#j44) [\[j37\]](https://dblp.org/pid/99/3602.html#j37)

[576](https://dblp.org/pid/99/3602.html?view=joint&param=576 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yu-Jie Zheng](https://dblp.org/pid/49/5016.html)

[\[c1\]](https://dblp.org/pid/99/3602.html#c1)

[577](https://dblp.org/pid/99/3602.html?view=joint&param=577 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yuhui Zheng](https://dblp.org/pid/155/0258.html)

[\[j85\]](https://dblp.org/pid/99/3602.html#j85)

[578](https://dblp.org/pid/99/3602.html?view=joint&param=578 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhedong Zheng](https://dblp.org/pid/190/7710.html)

[\[j77\]](https://dblp.org/pid/99/3602.html#j77)

[579](https://dblp.org/pid/99/3602.html?view=joint&param=579 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[580](https://dblp.org/pid/99/3602.html?view=joint&param=580 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Erjin Zhou](https://dblp.org/pid/150/4019.html)

[\[c65\]](https://dblp.org/pid/99/3602.html#c65) [\[i14\]](https://dblp.org/pid/99/3602.html#i14) [\[i13\]](https://dblp.org/pid/99/3602.html#i13) [\[i11\]](https://dblp.org/pid/99/3602.html#i11)

[581](https://dblp.org/pid/99/3602.html?view=joint&param=581 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Huiyu Zhou 0001](https://dblp.org/pid/36/1648.html)

[\[j70\]](https://dblp.org/pid/99/3602.html#j70)

[582](https://dblp.org/pid/99/3602.html?view=joint&param=582 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lukuan Zhou](https://dblp.org/pid/247/4747.html)

[\[j80\]](https://dblp.org/pid/99/3602.html#j80) [\[j61\]](https://dblp.org/pid/99/3602.html#j61)

[583](https://dblp.org/pid/99/3602.html?view=joint&param=583 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Peng Zhou](https://dblp.org/pid/23/5823.html)

[\[c43\]](https://dblp.org/pid/99/3602.html#c43) [\[c42\]](https://dblp.org/pid/99/3602.html#c42)

[584](https://dblp.org/pid/99/3602.html?view=joint&param=584 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Siyue Zhou](https://dblp.org/pid/218/9477.html)

[\[c51\]](https://dblp.org/pid/99/3602.html#c51)

[585](https://dblp.org/pid/99/3602.html?view=joint&param=585 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yichao Zhou](https://dblp.org/pid/146/9862.html)

[\[c60\]](https://dblp.org/pid/99/3602.html#c60)

[586](https://dblp.org/pid/99/3602.html?view=joint&param=586 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yimin Zhou 0002](https://dblp.org/pid/63/2223-2.html)

[\[j110\]](https://dblp.org/pid/99/3602.html#j110)

[587](https://dblp.org/pid/99/3602.html?view=joint&param=587 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Zhi-Hua Zhou](https://dblp.org/pid/z/ZhiHuaZhou.html)

[\[e1\]](https://dblp.org/pid/99/3602.html#e1)

[588](https://dblp.org/pid/99/3602.html?view=joint&param=588 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dejun Zhu](https://dblp.org/pid/64/9048.html)

[\[j127\]](https://dblp.org/pid/99/3602.html#j127) [\[j125\]](https://dblp.org/pid/99/3602.html#j125) [\[j121\]](https://dblp.org/pid/99/3602.html#j121) [\[j106\]](https://dblp.org/pid/99/3602.html#j106) [\[j104\]](https://dblp.org/pid/99/3602.html#j104)

[589](https://dblp.org/pid/99/3602.html?view=joint&param=589 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Dong Zhu](https://dblp.org/pid/57/5560.html)

[\[j72\]](https://dblp.org/pid/99/3602.html#j72)

[590](https://dblp.org/pid/99/3602.html?view=joint&param=590 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[591](https://dblp.org/pid/99/3602.html?view=joint&param=591 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lei Zhu 0010](https://dblp.org/pid/99/549-10.html)

[\[j57\]](https://dblp.org/pid/99/3602.html#j57)

[592](https://dblp.org/pid/99/3602.html?view=joint&param=592 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lian Zhu](https://dblp.org/pid/95/7051.html)

[\[c27\]](https://dblp.org/pid/99/3602.html#c27) [\[c25\]](https://dblp.org/pid/99/3602.html#c25) [\[c19\]](https://dblp.org/pid/99/3602.html#c19)

[593](https://dblp.org/pid/99/3602.html?view=joint&param=593 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Ronghui Zhu](https://dblp.org/pid/175/5685.html)

[\[j29\]](https://dblp.org/pid/99/3602.html#j29)

[594](https://dblp.org/pid/99/3602.html?view=joint&param=594 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69) [\[c61\]](https://dblp.org/pid/99/3602.html#c61)

[595](https://dblp.org/pid/99/3602.html?view=joint&param=595 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Jiedong Zhuang](https://dblp.org/pid/305/1138.html)

[\[c85\]](https://dblp.org/pid/99/3602.html#c85) [\[i47\]](https://dblp.org/pid/99/3602.html#i47) [\[i41\]](https://dblp.org/pid/99/3602.html#i41) [\[j116\]](https://dblp.org/pid/99/3602.html#j116)

[596](https://dblp.org/pid/99/3602.html?view=joint&param=596 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Yueting Zhuang](https://dblp.org/pid/218/7793.html)

[\[c69\]](https://dblp.org/pid/99/3602.html#c69)

[597](https://dblp.org/pid/99/3602.html?view=joint&param=597 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Lian Zhuo](https://dblp.org/pid/218/5220.html)

[\[j68\]](https://dblp.org/pid/99/3602.html#j68)

[598](https://dblp.org/pid/99/3602.html?view=joint&param=598 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Qingxiao Zou](https://dblp.org/pid/400/4769.html)

[\[j132\]](https://dblp.org/pid/99/3602.html#j132) [\[c80\]](https://dblp.org/pid/99/3602.html#c80)

[599](https://dblp.org/pid/99/3602.html?view=joint&param=599 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Wangmeng Zuo](https://dblp.org/pid/93/2671.html)

[\[c63\]](https://dblp.org/pid/99/3602.html#c63) [\[i9\]](https://dblp.org/pid/99/3602.html#i9)

[600](https://dblp.org/pid/99/3602.html?view=joint&param=600 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/99/3602.html?view=group&param=1)

[Xin Zuo](https://dblp.org/pid/15/2278.html)

[\[j149\]](https://dblp.org/pid/99/3602.html#j149) [\[j142\]](https://dblp.org/pid/99/3602.html#j142) [\[j136\]](https://dblp.org/pid/99/3602.html#j136) [\[j131\]](https://dblp.org/pid/99/3602.html#j131) [\[i45\]](https://dblp.org/pid/99/3602.html#i45) [\[i42\]](https://dblp.org/pid/99/3602.html#i42) [\[i40\]](https://dblp.org/pid/99/3602.html#i40) [\[i37\]](https://dblp.org/pid/99/3602.html#i37) [\[j130\]](https://dblp.org/pid/99/3602.html#j130) [\[j123\]](https://dblp.org/pid/99/3602.html#j123) [\[j122\]](https://dblp.org/pid/99/3602.html#j122) [\[j109\]](https://dblp.org/pid/99/3602.html#j109) [\[i23\]](https://dblp.org/pid/99/3602.html#i23) [\[i19\]](https://dblp.org/pid/99/3602.html#i19) [\[j95\]](https://dblp.org/pid/99/3602.html#j95) [\[j57\]](https://dblp.org/pid/99/3602.html#j57) [\[j56\]](https://dblp.org/pid/99/3602.html#j56) [\[j43\]](https://dblp.org/pid/99/3602.html#j43) [\[j42\]](https://dblp.org/pid/99/3602.html#j42) [\[j36\]](https://dblp.org/pid/99/3602.html#j36) [\[c40\]](https://dblp.org/pid/99/3602.html#c40) [\[j24\]](https://dblp.org/pid/99/3602.html#j24) [\[j23\]](https://dblp.org/pid/99/3602.html#j23) [\[c28\]](https://dblp.org/pid/99/3602.html#c28)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/99/3602.html#) [\[–\]](https://dblp.org/pid/99/3602.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/99/3602.html#) [\[–\]](https://dblp.org/pid/99/3602.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/99/3602.html#) [\[–\]](https://dblp.org/pid/99/3602.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/99/3602.html#) [\[–\]](https://dblp.org/pid/99/3602.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/99/3602.html#) [\[–\]](https://dblp.org/pid/99/3602.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)