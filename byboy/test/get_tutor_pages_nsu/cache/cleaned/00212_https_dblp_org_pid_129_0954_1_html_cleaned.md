> 抓取来源：https://dblp.org/pid/129/0954-1.html

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

- _affiliation:_ Tianjin University, College of Intelligence and Computing, China
- _affiliation:_ Dalian Maritime University, College of Information Science and Technology, China

- [Chengwei Zhang](https://dblp.org/pid/129/0954.html)(aka: Cheng-wei Zhang) — _disambiguation page_
- [Chengwei Zhang 0002](https://dblp.org/pid/129/0954-2.html)![[0000-0002-1921-9032]](https://dblp.org/img/orcid-mark.12x12.png) — Huazhong University of Science and Technology, School of Electronic Information and Communications, Wuhan, China
- [Chengwei Zhang 0003](https://dblp.org/pid/129/0954-3.html)![[0000-0002-1738-2450]](https://dblp.org/img/orcid-mark.12x12.png) — Shanghai Jiao Tong University, China

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Chengwei+Zhang+0001%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F129%2F0954-1%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Chengwei+Zhang+0001+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F129%2F0954-1%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Chengwei+Zhang+0001+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F129%2F0954-1%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Chengwei+Zhang+0001%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F129%2F0954-1%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Chengwei+Zhang+0001+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F129%2F0954-1%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Chengwei+Zhang+0001%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F129%2F0954-1%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Chengwei+Zhang+0001%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F129%2F0954-1%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F129%2F0954-1%3E+%7D+.%0A%0A%7D)

_showing all36 records_

2014202652014: 12016: 22017: 22017: 22018: 62018: 62018: 62019: 12021: 72021: 72021: 72022: 72022: 72023: 22025: 62025: 62026: 2

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

- ![](https://dblp.org/img/add-mark.12x12.png)Wanli Xue (18)
- ![](https://dblp.org/img/add-mark.12x12.png)Xiaohong Li 0001 (13)
- ![](https://dblp.org/img/add-mark.12x12.png)Rong Chen 0003 (11)
- ![](https://dblp.org/img/add-mark.12x12.png)Jianye Hao (11)
- ![](https://dblp.org/img/add-mark.12x12.png)Zhiyong Feng 0002 (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Wanting Liu (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Dou An (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Furui Zhan (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Shengyong Chen (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Siqi Chen 0001 (5)

- _265 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (23)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-9157-6050 (13)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (4)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Intell. Transp. Syst. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Int. J. Mach. Learn. Cybern. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans Autom. Sci. Eng. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)DAI (2)
- ![](https://dblp.org/img/add-mark.12x12.png)AAMAS (2)
- ![](https://dblp.org/img/add-mark.12x12.png)J. Appl. Math. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)NeurIPS (1)
- ![](https://dblp.org/img/add-mark.12x12.png)J. King Saud Univ. Comput. Inf. Sci. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Sensors (1)

- _17 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (23)
- ![](https://dblp.org/img/add-mark.12x12.png)open (13)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[j19\]
[Yihong Li](https://dblp.org/pid/81/5405.html), Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Furui Zhan](https://dblp.org/pid/196/4796.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wanting Liu](https://dblp.org/pid/157/6844.html), [Kailing Zhou](https://dblp.org/pid/382/4660.html), [Longji Zheng](https://dblp.org/pid/401/9939.html):

Enhancing traffic signal control through model-based reinforcement learning and policy reuse. [Expert Syst. Appl.298](https://dblp.org/db/journals/eswa/eswa298.html#journals/eswa/LiZZLZZ26): 129755 (2026)
- ![](https://dblp.org/img/n.png)

\[j18\]
[Yuanbo Li](https://dblp.org/pid/198/2381.html)![](https://dblp.org/img/orcid-mark.12x12.png), Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Wanting Liu](https://dblp.org/pid/157/6844.html), [Chao Li](https://dblp.org/pid/66/190.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dou An](https://dblp.org/pid/142/1098.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qi Wang](https://dblp.org/pid/19/1924-44.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Two-Stage Framework Based on RL for Truck-Drone Collaborative Delivery Problem. [IEEE Internet Things J.13(5)](https://dblp.org/db/journals/iotj/iotj13.html#journals/iotj/LiZLLAW26): 8777-8788 (2026)
- 2025
- ![](https://dblp.org/img/n.png)

\[j17\]
[Kun Tang](https://dblp.org/pid/93/1223.html), Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Wanting Liu](https://dblp.org/pid/157/6844.html), [Xue Li](https://dblp.org/pid/181/2710.html), [Qi Wang](https://dblp.org/pid/19/1924-44.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dou An](https://dblp.org/pid/142/1098.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furui Zhan](https://dblp.org/pid/196/4796.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Safe Refined Oil Dispatching via Constrained Multiagent Reinforcement Learning With Hierarchical Action Spaces. [IEEE Trans Autom. Sci. Eng.22](https://dblp.org/db/journals/tase/tase22.html#journals/tase/TangZLLWAZ25): 23164-23176 (2025)
- ![](https://dblp.org/img/n.png)

\[j16\]
[Wanting Liu](https://dblp.org/pid/157/6844.html), Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Wanqing Fang](https://dblp.org/pid/310/8973.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kailing Zhou](https://dblp.org/pid/382/4660.html), [Yihong Li](https://dblp.org/pid/81/5405.html), [Furui Zhan](https://dblp.org/pid/196/4796.html), [Qi Wang](https://dblp.org/pid/19/1924-44.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rong Chen](https://dblp.org/pid/22/6904-3.html):

Vehicle-Level Fairness-Oriented Constrained Multi-Agent Reinforcement Learning for Adaptive Traffic Signal Control. [IEEE Trans. Intell. Transp. Syst.26(4)](https://dblp.org/db/journals/tits/tits26.html#journals/tits/LiuZFZLZWXC25): 4878-4890 (2025)
- ![](https://dblp.org/img/n.png)

\[j15\]
[Wanting Liu](https://dblp.org/pid/157/6844.html), Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Kailing Zhou](https://dblp.org/pid/382/4660.html), [Yihong Li](https://dblp.org/pid/81/5405.html), [Furui Zhan](https://dblp.org/pid/196/4796.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rong Chen](https://dblp.org/pid/22/6904-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Sequential Decision MARL for Adaptive Traffic Signal Control With Different Intersections Priorities. [IEEE Trans. Intell. Transp. Syst.26(7)](https://dblp.org/db/journals/tits/tits26.html#journals/tits/LiuZZLZXC25): 9799-9811 (2025)
- ![](https://dblp.org/img/n.png)

\[j14\]
[Zhibin Zhang](https://dblp.org/pid/85/1218.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bo Liu](https://dblp.org/pid/58/2670-5.html), Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Jingen Liu](https://dblp.org/pid/10/5849.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shengyong Chen](https://dblp.org/pid/93/2479.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning Self-Corrective Network via Adaptive Self-Labeling and Dynamic NMS for High-Performance Long-Term Tracking. [IEEE Trans. Neural Networks Learn. Syst.36(1)](https://dblp.org/db/journals/tnn/tnn36.html#journals/tnn/ZhangXZLZLC25): 653-664 (2025)
- ![](https://dblp.org/img/n.png)

\[i5\]
[Kailing Zhou](https://dblp.org/pid/382/4660.html), Chengwei Zhang, [Furui Zhan](https://dblp.org/pid/196/4796.html), [Wanting Liu](https://dblp.org/pid/157/6844.html), [Yihong Li](https://dblp.org/pid/81/5405.html):

Using a single actor to output personalized policy for different intersections. [CoRRabs/2503.07678](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-07678) (2025)
- ![](https://dblp.org/img/n.png)

\[i4\]
[Yihong Li](https://dblp.org/pid/81/5405.html), Chengwei Zhang, [Furui Zhan](https://dblp.org/pid/196/4796.html), [Wanting Liu](https://dblp.org/pid/157/6844.html), [Kailing Zhou](https://dblp.org/pid/382/4660.html), [Longji Zheng](https://dblp.org/pid/401/9939.html):

Enhancing Traffic Signal Control through Model-based Reinforcement Learning and Policy Reuse. [CoRRabs/2503.08728](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-08728) (2025)
- 2023
- ![](https://dblp.org/img/n.png)

\[j13\]
[Qi Wang](https://dblp.org/pid/19/1924-44.html)![](https://dblp.org/img/orcid-mark.12x12.png), Chengwei Zhang, [Chunlei Tang](https://dblp.org/pid/211/4125.html):

Discovering Lin-Kernighan-Helsgaun heuristic for routing optimization using self-supervised reinforcement learning. [J. King Saud Univ. Comput. Inf. Sci.35(8)](https://dblp.org/db/journals/jksucis/jksucis35.html#journals/jksucis/WangZT23): 101723 (2023)
- ![](https://dblp.org/img/n.png)

\[j12\]
Chengwei Zhang, [Dina Fang](https://dblp.org/pid/341/4050.html), [Sandip Sen](https://dblp.org/pid/19/1004.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaohong Li](https://dblp.org/pid/08/2489-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhiyong Feng](https://dblp.org/pid/48/195-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dou An](https://dblp.org/pid/142/1098.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xintian Zhao](https://dblp.org/pid/318/6762.html), [Rong Chen](https://dblp.org/pid/22/6904-3.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Opinion Dynamics in Gossiper-Media Networks Based on Multiagent Reinforcement Learning. [IEEE Trans. Netw. Sci. Eng.10(2)](https://dblp.org/db/journals/tnse/tnse10.html#journals/tnse/ZhangFSLFXAZC23): 1143-1156 (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j11\]
Chengwei Zhang, [Kangjie Zheng](https://dblp.org/pid/249/2602.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yu Tian](https://dblp.org/pid/15/4658.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianpei Yang](https://dblp.org/pid/184/8221.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dou An](https://dblp.org/pid/142/1098.html), [Yongqi Pi](https://dblp.org/pid/318/4583.html), [Rong Chen](https://dblp.org/pid/22/6904-3.html):

Advertising Impression Resource Allocation Strategy with Multi-Level Budget Constraint DQN in Real-Time Bidding. [Neurocomputing488](https://dblp.org/db/journals/ijon/ijon488.html#journals/ijon/ZhangZTXYAPC22): 647-656 (2022)
- ![](https://dblp.org/img/n.png)

\[j10\]
Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Zhuobing Han](https://dblp.org/pid/156/4630.html), [Bingfu Liu](https://dblp.org/pid/251/7589.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianye Hao](https://dblp.org/pid/21/7664.html), [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Dou An](https://dblp.org/pid/142/1098.html), [Rong Chen](https://dblp.org/pid/22/6904-3.html):

SCC-rFMQ: a multiagent reinforcement learning method in cooperative Markov games with continuous actions. [Int. J. Mach. Learn. Cybern.13(7)](https://dblp.org/db/journals/mlc/mlc13.html#journals/mlc/ZhangHLXHLAC22): 1927-1944 (2022)
- ![](https://dblp.org/img/n.png)

\[j9\]
[Dou An](https://dblp.org/pid/142/1098.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Feiye Zhang](https://dblp.org/pid/73/1183.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qingyu Yang](https://dblp.org/pid/01/2404-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png):

Data Integrity Attack in Dynamic State Estimation of Smart Grid: Attack Model and Countermeasures. [IEEE Trans Autom. Sci. Eng.19(3)](https://dblp.org/db/journals/tase/tase19.html#journals/tase/AnZY022): 1631-1644 (2022)
- ![](https://dblp.org/img/n.png)

\[j8\]
[Zhe Zhang](https://dblp.org/pid/87/5809-39.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xuhong Ren](https://dblp.org/pid/138/4258.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Object-Aware Ghost Identification and Elimination for Dynamic Scene Mosaic. [IEEE Trans. Circuits Syst. Video Technol.32(4)](https://dblp.org/db/journals/tcsv/tcsv32.html#journals/tcsv/ZhangRXZGC22): 2025-2034 (2022)
- ![](https://dblp.org/img/n.png)

\[j7\]
Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Yu Tian](https://dblp.org/pid/15/4658.html), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianpei Yang](https://dblp.org/pid/184/8221.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Ge](https://dblp.org/pid/90/3741.html), [Rong Chen](https://dblp.org/pid/22/6904-3.html):

Neighborhood Cooperative Multiagent Reinforcement Learning for Adaptive Traffic Signal Control in Epidemic Regions. [IEEE Trans. Intell. Transp. Syst.23(12)](https://dblp.org/db/journals/tits/tits23.html#journals/tits/ZhangTZXXYGC22): 25157-25168 (2022)
- ![](https://dblp.org/img/n.png)

\[c12\]
[Yu Tian](https://dblp.org/pid/15/4658.html), Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Kangjie Zheng](https://dblp.org/pid/249/2602.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wanqing Fang](https://dblp.org/pid/310/8973.html), [Xintian Zhao](https://dblp.org/pid/318/6762.html), [Shiqi Zhang](https://dblp.org/pid/03/9964.html):

Optimistic Exploration Based on Categorical-DQN for Cooperative Markov Games. [DAI2022](https://dblp.org/db/conf/dai2/dai2022.html#conf/dai2/TianZGZFZZ22): 60-73
- ![](https://dblp.org/img/n.png)

\[c11\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Wenyan Yang](https://dblp.org/pid/119/2426.html), [Dingding Cai](https://dblp.org/pid/198/1127.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Kang Ben](https://dblp.org/pid/340/0959.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Hong Chang](https://dblp.org/pid/02/2689-1.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Jiaye Chen](https://dblp.org/pid/116/2901.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xilin Chen](https://dblp.org/pid/c/XilinChen.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Xiuyi Chen](https://dblp.org/pid/218/7190.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu-Hsi Chen](https://dblp.org/pid/127/3933.html), [Zhixing Chen](https://dblp.org/pid/62/3074.html), [Yangming Cheng](https://dblp.org/pid/340/1285.html), [Angelo Ciaramella](https://dblp.org/pid/37/6845.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Benjamin Dzubur](https://dblp.org/pid/340/1520.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Debajyoti Dhar](https://dblp.org/pid/128/3182.html), [Shangzhe Di](https://dblp.org/pid/304/1344.html), [Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shang Gao](https://dblp.org/pid/28/435-12.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Eric Granger](https://dblp.org/pid/86/2306.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Q. H. Gu](https://dblp.org/pid/340/1209.html), [Himanshu Gupta](https://dblp.org/pid/330/0760-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianfeng He](https://dblp.org/pid/93/8352.html), [Keji He](https://dblp.org/pid/319/4518.html), [Yan Huang](https://dblp.org/pid/75/6434-8.html), [Deepak Jangid](https://dblp.org/pid/340/1460.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Ze Kang](https://dblp.org/pid/340/1063.html), [Madhu Kiran](https://dblp.org/pid/39/10281.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Simiao Lai](https://dblp.org/pid/282/1954.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Dongwook Lee](https://dblp.org/pid/25/6543.html), [Hyunjeong Lee](https://dblp.org/pid/00/3423.html), [Seohyung Lee](https://dblp.org/pid/210/4662.html), [Hui Li](https://dblp.org/pid/66/3387-37.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ming Li](https://dblp.org/pid/l/MingLi10.html), [Wangkai Li](https://dblp.org/pid/340/1456.html), [Xi Li](https://dblp.org/pid/46/2311-1.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Xiao Li](https://dblp.org/pid/66/2069.html), [Zhe Li](https://dblp.org/pid/11/751-8.html), [Liting Lin](https://dblp.org/pid/227/2204.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Si Liu](https://dblp.org/pid/60/7642.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html), [Bingpeng Ma](https://dblp.org/pid/62/1822.html), [Chao Ma](https://dblp.org/pid/79/1552-4.html), [Jie Ma](https://dblp.org/pid/62/5110.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yinchao Ma](https://dblp.org/pid/189/1326.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Payman Moallem](https://dblp.org/pid/63/5378.html), [Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html), [Siyang Pan](https://dblp.org/pid/250/5753.html), [ChangBeom Park](https://dblp.org/pid/340/0926.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Litu Rout](https://dblp.org/pid/206/6445.html), [Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Tianhui Song](https://dblp.org/pid/181/8738.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Chao Sun](https://dblp.org/pid/54/3957.html), [Jingna Sun](https://dblp.org/pid/255/0702.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Om Prakash Verma](https://dblp.org/pid/61/8145.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Qiang Wang](https://dblp.org/pid/64/5630-23.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Jinlin Wu](https://dblp.org/pid/123/7200.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Xu](https://dblp.org/pid/32/1213-17.html), [Yong Xu](https://dblp.org/pid/07/4630-7.html), [Yuanyou Xu](https://dblp.org/pid/248/7663.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zizheng Xun](https://dblp.org/pid/340/1441.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Dawei Yang](https://dblp.org/pid/22/1038.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Yichun Yang](https://dblp.org/pid/249/9678.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Botao Ye](https://dblp.org/pid/227/4610.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Qianjin Yu](https://dblp.org/pid/53/10179.html), [Weichen Yu](https://dblp.org/pid/325/1209.html), [Kang Ze](https://dblp.org/pid/340/1107.html), [Jiang Zhai](https://dblp.org/pid/291/9340.html), Chengwei Zhang, [Chunhu Zhang](https://dblp.org/pid/292/0953.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Haixia Zheng](https://dblp.org/pid/119/1585.html), [Min Zheng](https://dblp.org/pid/23/328.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html):

The Tenth Visual Object Tracking VOT2022 Challenge Results. [ECCV Workshops (8)2022](https://dblp.org/db/conf/eccv/eccv2022-w8.html#conf/eccv/KristanLMFPKCDZLDBZZYYCMFBBCCCCCCCCCCC22): 431-460
- 2021
- ![](https://dblp.org/img/n.png)

\[j6\]
[Zhifeng Zhou](https://dblp.org/pid/231/4770.html), [Rong Chen](https://dblp.org/pid/22/6904-3.html), [Can Wang](https://dblp.org/pid/71/4716.html), Chengwei Zhang:

Dynamic pricing in profit-driven task assignment: a domain-of-influence based approach. [Int. J. Mach. Learn. Cybern.12(4)](https://dblp.org/db/journals/mlc/mlc12.html#journals/mlc/ZhouCWZ21): 1015-1030 (2021)
- ![](https://dblp.org/img/n.png)

\[j5\]
Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Shan Jin](https://dblp.org/pid/10/2477.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaofei Xie](https://dblp.org/pid/127/0713.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shengyong Chen](https://dblp.org/pid/93/2479.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rong Chen](https://dblp.org/pid/22/6904-3.html):

Independent Reinforcement Learning for Weakly Cooperative Multiagent Traffic Control Problem. [IEEE Trans. Veh. Technol.70(8)](https://dblp.org/db/journals/tvt/tvt70.html#journals/tvt/ZhangJXXCC21): 7426-7436 (2021)
- ![](https://dblp.org/img/n.png)

\[c10\]
[Yang Zhang](https://dblp.org/pid/06/6785-97.html), [Qingyu Yang](https://dblp.org/pid/01/2404-3.html), [Dou An](https://dblp.org/pid/142/1098.html), Chengwei Zhang:

Coordination Between Individual Agents in Multi-Agent Reinforcement Learning. [AAAI2021](https://dblp.org/db/conf/aaai/aaai2021.html#conf/aaai/ZhangYAZ21): 11387-11394
- ![](https://dblp.org/img/n.png)

\[c9\]
[Liguang Luan](https://dblp.org/pid/310/7942.html), [Yu Tian](https://dblp.org/pid/15/4658.html), [Wanqing Fang](https://dblp.org/pid/310/8973.html), Chengwei Zhang, [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rong Chen](https://dblp.org/pid/22/6904-3.html), [Chen Sang](https://dblp.org/pid/231/1051.html):

MARL for Traffic Signal Control in Scenarios with Different Intersection Importance. [DAI2021](https://dblp.org/db/conf/dai2/dai2021.html#conf/dai2/LuanTFZXCS21): 93-106
- ![](https://dblp.org/img/n.png)

\[c8\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Yu-Chen Chiu](https://dblp.org/pid/199/2494.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Xingping Dong](https://dblp.org/pid/156/3020.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Bilge Günsel](https://dblp.org/pid/47/5125.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Wencheng Han](https://dblp.org/pid/280/3348.html), [Yanyan Huang](https://dblp.org/pid/88/4316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [J. Yin](https://dblp.org/pid/51/2242.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Jingen Liu](https://dblp.org/pid/10/5849.html), [Li Liu](https://dblp.org/pid/33/4528-36.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Jonathon Luiten](https://dblp.org/pid/211/7992.html), [Jie Ma](https://dblp.org/pid/62/5110.html), [Ziang Ma](https://dblp.org/pid/165/9621.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Yuzhen Niu](https://dblp.org/pid/28/7442.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Aravindh Rajiv](https://dblp.org/pid/307/9144.html), [Muhammad Rana](https://dblp.org/pid/276/0222.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Ling Shao](https://dblp.org/pid/75/1281.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furao Shen](https://dblp.org/pid/80/4685.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Paul Voigtlaender](https://dblp.org/pid/166/6430.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html), [Chenyan Wu](https://dblp.org/pid/76/1190.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang Xu](https://dblp.org/pid/126/2962.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), Chengwei Zhang, [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Xiaohan Zhang](https://dblp.org/pid/96/6053.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Ming Zhen](https://dblp.org/pid/307/8430.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html):

The Ninth Visual Object Tracking VOT2021 Challenge Results. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/KristanMLFPKCDZ21): 2711-2738
- ![](https://dblp.org/img/n.png)

\[c7\]
[Tianpei Yang](https://dblp.org/pid/184/8221.html), [Weixun Wang](https://dblp.org/pid/84/998.html), [Hongyao Tang](https://dblp.org/pid/220/4275.html), [Jianye Hao](https://dblp.org/pid/21/7664.html), [Zhaopeng Meng](https://dblp.org/pid/67/8175.html), [Hangyu Mao](https://dblp.org/pid/191/6097.html), [Dong Li](https://dblp.org/pid/47/4826-16.html), [Wulong Liu](https://dblp.org/pid/36/9257.html), [Yingfeng Chen](https://dblp.org/pid/37/1835.html), [Yujing Hu](https://dblp.org/pid/160/1923.html), [Changjie Fan](https://dblp.org/pid/71/882.html), Chengwei Zhang:

An Efficient Transfer Learning Framework for Multiagent Reinforcement Learning. [NeurIPS2021](https://dblp.org/db/conf/nips/neurips2021.html#conf/nips/YangWTHMMLLCHFZ21): 17037-17048
- ![](https://dblp.org/img/n.png)

\[i3\]
Chengwei Zhang, [Shan Jin](https://dblp.org/pid/10/2477.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Xiaofei Xie](https://dblp.org/pid/127/0713.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Rong Chen](https://dblp.org/pid/22/6904-3.html):

Independent Reinforcement Learning for Weakly Cooperative Multiagent Traffic Control Problem. [CoRRabs/2104.10917](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-10917) (2021)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j4\]
Chengwei Zhang![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Jianye Hao](https://dblp.org/pid/21/7664.html), [Siqi Chen](https://dblp.org/pid/05/8743-1.html), [Karl Tuyls](https://dblp.org/pid/t/KTuyls.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhiyong Feng](https://dblp.org/pid/48/195-2.html):

SA-IGA: a multiagent reinforcement learning method towards socially optimal outcomes. [Auton. Agents Multi Agent Syst.33(4)](https://dblp.org/db/journals/aamas/aamas33.html#journals/aamas/ZhangLHCTXF19): 403-429 (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[j3\]
[Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhiyong Feng](https://dblp.org/pid/48/195-2.html), [Chao Xu](https://dblp.org/pid/79/1442-3.html), [Zhaopeng Meng](https://dblp.org/pid/67/8175.html), Chengwei Zhang:

Adaptive Object Tracking via Multi-Angle Analysis Collaboration. [Sensors18(11)](https://dblp.org/db/journals/sensors/sensors18.html#journals/sensors/XueFXMZ18): 3606 (2018)
- ![](https://dblp.org/img/n.png)

\[c6\]
Chengwei Zhang, [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Jianye Hao](https://dblp.org/pid/21/7664.html), [Sandip Sen](https://dblp.org/pid/19/1004.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Zhiyong Feng](https://dblp.org/pid/48/195-2.html):

The Dynamics of Opinion Evolution in Gossiper-Media Model with WoLS-CALA Learning. [AAMAS2018](https://dblp.org/db/conf/atal/aamas2018.html#conf/atal/ZhangLHSXF18): 2159-2161
- ![](https://dblp.org/img/n.png)

\[c5\]
Chengwei Zhang, [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Jianye Hao](https://dblp.org/pid/21/7664.html), [Siqi Chen](https://dblp.org/pid/05/8743-1.html), [Karl Tuyls](https://dblp.org/pid/t/KTuyls.html), [Zhiyong Feng](https://dblp.org/pid/48/195-2.html):

SCC-rFMQ Learning in Cooperative Markov Games with Continuous Actions. [AAMAS2018](https://dblp.org/db/conf/atal/aamas2018.html#conf/atal/ZhangLHCTF18): 2162-2164
- ![](https://dblp.org/img/n.png)

\[c4\]
[Wanshu Liu](https://dblp.org/pid/223/7969.html), Chengwei Zhang, [Tianpei Yang](https://dblp.org/pid/184/8221.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianye Hao](https://dblp.org/pid/21/7664.html), [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Zhijie Bao](https://dblp.org/pid/195/7876.html):

Achieving Multiagent Coordination Through CALA-rFMQ Learning in Continuous Action Space. [PRICAI2018](https://dblp.org/db/conf/pricai/pricai2018b.html#conf/pricai/LiuZYHLB18): 132-139
- ![](https://dblp.org/img/n.png)

\[i2\]
Chengwei Zhang, [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Jianye Hao](https://dblp.org/pid/21/7664.html), [Siqi Chen](https://dblp.org/pid/05/8743-1.html), [Karl Tuyls](https://dblp.org/pid/t/KTuyls.html), [Wanli Xue](https://dblp.org/pid/153/8037.html):

SA-IGA: A Multiagent Reinforcement Learning Method Towards Socially Optimal Outcomes. [CoRRabs/1803.03021](https://dblp.org/db/journals/corr/corr1803.html#journals/corr/abs-1803-03021) (2018)
- ![](https://dblp.org/img/n.png)

\[i1\]
Chengwei Zhang, [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Jianye Hao](https://dblp.org/pid/21/7664.html), [Siqi Chen](https://dblp.org/pid/05/8743-1.html), [Karl Tuyls](https://dblp.org/pid/t/KTuyls.html), [Zhiyong Feng](https://dblp.org/pid/48/195-2.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Rong Chen](https://dblp.org/pid/22/6904-3.html):

SCC-rFMQ Learning in Cooperative Markov Games with Continuous Actions. [CoRRabs/1809.06625](https://dblp.org/db/journals/corr/corr1809.html#journals/corr/abs-1809-06625) (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[j2\]
Chengwei Zhang, [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Shuxin Li](https://dblp.org/pid/84/4388-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-2.html):

Dynamically analyzing cell interactions in biological environments using multiagent social learning framework. [J. Biomed. Semant.8-S(1)](https://dblp.org/db/journals/biomedsem/biomedsem8S.html#journals/biomedsem/ZhangLLF17): 43-52 (2017)
- ![](https://dblp.org/img/n.png)

\[c3\]
[Shuxin Li](https://dblp.org/pid/84/4388-1.html), [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Jianye Hao](https://dblp.org/pid/21/7664.html), [Bo An](https://dblp.org/pid/42/6178-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-2.html), [Kangjie Chen](https://dblp.org/pid/204/3003.html), Chengwei Zhang:

Defending Against Man-In-The-Middle Attack in Repeated Games. [IJCAI2017](https://dblp.org/db/conf/ijcai/ijcai2017.html#conf/ijcai/LiLHAFCZ17): 3742-3748
- 2016
- ![](https://dblp.org/img/n.png)

\[c2\]
Chengwei Zhang, [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Shuxin Li](https://dblp.org/pid/84/4388-1.html), [Jianye Hao](https://dblp.org/pid/21/7664.html):

Dynamic analysis of cell interactions in biological environments under multiagent social learning framework. [BIBM2016](https://dblp.org/db/conf/bibm/bibm2016.html#conf/bibm/ZhangLLH16): 1673-1678
- ![](https://dblp.org/img/n.png)

\[c1\]
[Xiaohong Li](https://dblp.org/pid/08/2489-1.html), Chengwei Zhang, [Jianye Hao](https://dblp.org/pid/21/7664.html), [Karl Tuyls](https://dblp.org/pid/t/KTuyls.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Siqi Chen](https://dblp.org/pid/05/8743-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-2.html):

Socially-Aware Multiagent Learning: Towards Socially Optimal Outcomes. [ECAI2016](https://dblp.org/db/conf/ecai/ecai2016.html#conf/ecai/LiZHTCF16): 533-541
- 2014
- ![](https://dblp.org/img/n.png)

\[j1\]
Chengwei Zhang, [Xiaohong Li](https://dblp.org/pid/08/2489-1.html), [Jing Hu](https://dblp.org/pid/95/6046-7.html), [Zhiyong Feng](https://dblp.org/pid/48/195-2.html), [Jiaojiao Song](https://dblp.org/pid/146/9110.html):

Formal Modeling and Analysis of Fairness Characterization of E-Commerce Protocols. [J. Appl. Math.2014](https://dblp.org/db/journals/jam/jam2014.html#journals/jam/ZhangLHFS14): 138370:1-138370:10 (2014)
- _no results_

automatic loading of the coauthor graph disabled due to its size.

**click here to**
**load the graph.**

Note that this feature is _work in progress_ and that it is still far from being perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/129/0954-1.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[2](https://dblp.org/pid/129/0954-1.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Bo An 0001](https://dblp.org/pid/42/6178-1.html)

[\[c3\]](https://dblp.org/pid/129/0954-1.html#c3)

[3](https://dblp.org/pid/129/0954-1.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Dou An](https://dblp.org/pid/142/1098.html)

[\[j18\]](https://dblp.org/pid/129/0954-1.html#j18) [\[j17\]](https://dblp.org/pid/129/0954-1.html#j17) [\[j12\]](https://dblp.org/pid/129/0954-1.html#j12) [\[j11\]](https://dblp.org/pid/129/0954-1.html#j11) [\[j10\]](https://dblp.org/pid/129/0954-1.html#j10) [\[j9\]](https://dblp.org/pid/129/0954-1.html#j9) [\[c10\]](https://dblp.org/pid/129/0954-1.html#c10)

[4](https://dblp.org/pid/129/0954-1.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhijie Bao](https://dblp.org/pid/195/7876.html)

[\[c4\]](https://dblp.org/pid/129/0954-1.html#c4)

[5](https://dblp.org/pid/129/0954-1.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Kang Ben](https://dblp.org/pid/340/0959.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[6](https://dblp.org/pid/129/0954-1.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[7](https://dblp.org/pid/129/0954-1.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Johanna Björklund](https://dblp.org/pid/75/5525.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[8](https://dblp.org/pid/129/0954-1.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Dingding Cai](https://dblp.org/pid/198/1127.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[9](https://dblp.org/pid/129/0954-1.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[10](https://dblp.org/pid/129/0954-1.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Llukman Cerkezi](https://dblp.org/pid/208/1312.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[11](https://dblp.org/pid/129/0954-1.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Hakan Çevikalp](https://dblp.org/pid/14/6210.html)

aka: Hakan Cevikalp

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[12](https://dblp.org/pid/129/0954-1.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Hong Chang 0001](https://dblp.org/pid/02/2689-1.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[13](https://dblp.org/pid/129/0954-1.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[14](https://dblp.org/pid/129/0954-1.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Guangqi Chen](https://dblp.org/pid/178/8116.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[15](https://dblp.org/pid/129/0954-1.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jiaye Chen](https://dblp.org/pid/116/2901.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[16](https://dblp.org/pid/129/0954-1.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Kangjie Chen](https://dblp.org/pid/204/3003.html)

[\[c3\]](https://dblp.org/pid/129/0954-1.html#c3)

[17](https://dblp.org/pid/129/0954-1.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Rong Chen 0003](https://dblp.org/pid/22/6904-3.html)

[\[j16\]](https://dblp.org/pid/129/0954-1.html#j16) [\[j15\]](https://dblp.org/pid/129/0954-1.html#j15) [\[j12\]](https://dblp.org/pid/129/0954-1.html#j12) [\[j11\]](https://dblp.org/pid/129/0954-1.html#j11) [\[j10\]](https://dblp.org/pid/129/0954-1.html#j10) [\[j7\]](https://dblp.org/pid/129/0954-1.html#j7) [\[j6\]](https://dblp.org/pid/129/0954-1.html#j6) [\[j5\]](https://dblp.org/pid/129/0954-1.html#j5) [\[c9\]](https://dblp.org/pid/129/0954-1.html#c9) [\[i3\]](https://dblp.org/pid/129/0954-1.html#i3) [\[i1\]](https://dblp.org/pid/129/0954-1.html#i1)

[18](https://dblp.org/pid/129/0954-1.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[j14\]](https://dblp.org/pid/129/0954-1.html#j14) [\[j8\]](https://dblp.org/pid/129/0954-1.html#j8) [\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[j5\]](https://dblp.org/pid/129/0954-1.html#j5) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8) [\[i3\]](https://dblp.org/pid/129/0954-1.html#i3)

[19](https://dblp.org/pid/129/0954-1.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Siqi Chen 0001](https://dblp.org/pid/05/8743-1.html)

[\[j4\]](https://dblp.org/pid/129/0954-1.html#j4) [\[c5\]](https://dblp.org/pid/129/0954-1.html#c5) [\[i2\]](https://dblp.org/pid/129/0954-1.html#i2) [\[i1\]](https://dblp.org/pid/129/0954-1.html#i1) [\[c1\]](https://dblp.org/pid/129/0954-1.html#c1)

[20](https://dblp.org/pid/129/0954-1.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xilin Chen 0001](https://dblp.org/pid/c/XilinChen.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[21](https://dblp.org/pid/129/0954-1.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[22](https://dblp.org/pid/129/0954-1.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiuyi Chen](https://dblp.org/pid/218/7190.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[23](https://dblp.org/pid/129/0954-1.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yingfeng Chen](https://dblp.org/pid/37/1835.html)

[\[c7\]](https://dblp.org/pid/129/0954-1.html#c7)

[24](https://dblp.org/pid/129/0954-1.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yiwei Chen](https://dblp.org/pid/28/2965.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[25](https://dblp.org/pid/129/0954-1.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yu-Hsi Chen](https://dblp.org/pid/127/3933.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[26](https://dblp.org/pid/129/0954-1.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhixing Chen](https://dblp.org/pid/62/3074.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[27](https://dblp.org/pid/129/0954-1.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Miao Cheng](https://dblp.org/pid/79/7377.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[28](https://dblp.org/pid/129/0954-1.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yangming Cheng](https://dblp.org/pid/340/1285.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[29](https://dblp.org/pid/129/0954-1.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Ziyi Cheng](https://dblp.org/pid/290/9342.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[30](https://dblp.org/pid/129/0954-1.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yu-Chen Chiu](https://dblp.org/pid/199/2494.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[31](https://dblp.org/pid/129/0954-1.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Angelo Ciaramella](https://dblp.org/pid/37/6845.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[32](https://dblp.org/pid/129/0954-1.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Ozgun Cirakman](https://dblp.org/pid/86/8843.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[33](https://dblp.org/pid/129/0954-1.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[34](https://dblp.org/pid/129/0954-1.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[35](https://dblp.org/pid/129/0954-1.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Kenan Dai](https://dblp.org/pid/250/4445.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[36](https://dblp.org/pid/129/0954-1.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[37](https://dblp.org/pid/129/0954-1.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[38](https://dblp.org/pid/129/0954-1.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[39](https://dblp.org/pid/129/0954-1.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Debajyoti Dhar](https://dblp.org/pid/128/3182.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[40](https://dblp.org/pid/129/0954-1.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Shangzhe Di](https://dblp.org/pid/304/1344.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[41](https://dblp.org/pid/129/0954-1.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xingping Dong](https://dblp.org/pid/156/3020.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[42](https://dblp.org/pid/129/0954-1.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[43](https://dblp.org/pid/129/0954-1.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[44](https://dblp.org/pid/129/0954-1.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[45](https://dblp.org/pid/129/0954-1.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Benjamin Dzubur](https://dblp.org/pid/340/1520.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[46](https://dblp.org/pid/129/0954-1.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Changjie Fan](https://dblp.org/pid/71/882.html)

[\[c7\]](https://dblp.org/pid/129/0954-1.html#c7)

[47](https://dblp.org/pid/129/0954-1.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Heng Fan 0001](https://dblp.org/pid/20/10120-1.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[48](https://dblp.org/pid/129/0954-1.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Dina Fang](https://dblp.org/pid/341/4050.html)

[\[j12\]](https://dblp.org/pid/129/0954-1.html#j12)

[49](https://dblp.org/pid/129/0954-1.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wanqing Fang](https://dblp.org/pid/310/8973.html)

[\[j16\]](https://dblp.org/pid/129/0954-1.html#j16) [\[c12\]](https://dblp.org/pid/129/0954-1.html#c12) [\[c9\]](https://dblp.org/pid/129/0954-1.html#c9)

[50](https://dblp.org/pid/129/0954-1.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[51](https://dblp.org/pid/129/0954-1.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[52](https://dblp.org/pid/129/0954-1.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhiyong Feng 0001](https://dblp.org/pid/48/195-1.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[53](https://dblp.org/pid/129/0954-1.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhiyong Feng 0002](https://dblp.org/pid/48/195-2.html)

[\[j12\]](https://dblp.org/pid/129/0954-1.html#j12) [\[j4\]](https://dblp.org/pid/129/0954-1.html#j4) [\[j3\]](https://dblp.org/pid/129/0954-1.html#j3) [\[c6\]](https://dblp.org/pid/129/0954-1.html#c6) [\[c5\]](https://dblp.org/pid/129/0954-1.html#c5) [\[i1\]](https://dblp.org/pid/129/0954-1.html#i1) [\[j2\]](https://dblp.org/pid/129/0954-1.html#j2) [\[c3\]](https://dblp.org/pid/129/0954-1.html#c3) [\[c1\]](https://dblp.org/pid/129/0954-1.html#c1) [\[j1\]](https://dblp.org/pid/129/0954-1.html#j1)

[54](https://dblp.org/pid/129/0954-1.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[55](https://dblp.org/pid/129/0954-1.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[56](https://dblp.org/pid/129/0954-1.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Shang Gao 0012](https://dblp.org/pid/28/435-12.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[57](https://dblp.org/pid/129/0954-1.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Shiming Ge](https://dblp.org/pid/93/8104.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[58](https://dblp.org/pid/129/0954-1.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xin Ge](https://dblp.org/pid/90/3741.html)

[\[j7\]](https://dblp.org/pid/129/0954-1.html#j7)

[59](https://dblp.org/pid/129/0954-1.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[60](https://dblp.org/pid/129/0954-1.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[61](https://dblp.org/pid/129/0954-1.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Eric Granger](https://dblp.org/pid/86/2306.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[62](https://dblp.org/pid/129/0954-1.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Q. H. Gu](https://dblp.org/pid/340/1209.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[63](https://dblp.org/pid/129/0954-1.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yuzhang Gu](https://dblp.org/pid/122/3790.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[64](https://dblp.org/pid/129/0954-1.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Bilge Günsel](https://dblp.org/pid/47/5125.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[65](https://dblp.org/pid/129/0954-1.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Qing Guo 0005](https://dblp.org/pid/25/3038-5.html)

[\[j8\]](https://dblp.org/pid/129/0954-1.html#j8) [\[c12\]](https://dblp.org/pid/129/0954-1.html#c12) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[66](https://dblp.org/pid/129/0954-1.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Himanshu Gupta 0003](https://dblp.org/pid/330/0760-3.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[67](https://dblp.org/pid/129/0954-1.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Filiz Gurkan](https://dblp.org/pid/202/7040.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[68](https://dblp.org/pid/129/0954-1.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Gustav Häger](https://dblp.org/pid/157/3602.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[69](https://dblp.org/pid/129/0954-1.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wencheng Han](https://dblp.org/pid/280/3348.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[70](https://dblp.org/pid/129/0954-1.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhuobing Han](https://dblp.org/pid/156/4630.html)

[\[j10\]](https://dblp.org/pid/129/0954-1.html#j10)

[71](https://dblp.org/pid/129/0954-1.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jianye Hao](https://dblp.org/pid/21/7664.html)

[\[j10\]](https://dblp.org/pid/129/0954-1.html#j10) [\[c7\]](https://dblp.org/pid/129/0954-1.html#c7) [\[j4\]](https://dblp.org/pid/129/0954-1.html#j4) [\[c6\]](https://dblp.org/pid/129/0954-1.html#c6) [\[c5\]](https://dblp.org/pid/129/0954-1.html#c5) [\[c4\]](https://dblp.org/pid/129/0954-1.html#c4) [\[i2\]](https://dblp.org/pid/129/0954-1.html#i2) [\[i1\]](https://dblp.org/pid/129/0954-1.html#i1) [\[c3\]](https://dblp.org/pid/129/0954-1.html#c3) [\[c2\]](https://dblp.org/pid/129/0954-1.html#c2) [\[c1\]](https://dblp.org/pid/129/0954-1.html#c1)

[72](https://dblp.org/pid/129/0954-1.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jianfeng He](https://dblp.org/pid/93/8352.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[73](https://dblp.org/pid/129/0954-1.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Keji He](https://dblp.org/pid/319/4518.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[74](https://dblp.org/pid/129/0954-1.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jing Hu 0007](https://dblp.org/pid/95/6046-7.html)

[\[j1\]](https://dblp.org/pid/129/0954-1.html#j1)

[75](https://dblp.org/pid/129/0954-1.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yujing Hu](https://dblp.org/pid/160/1923.html)

[\[c7\]](https://dblp.org/pid/129/0954-1.html#c7)

[76](https://dblp.org/pid/129/0954-1.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yan Huang 0008](https://dblp.org/pid/75/6434-8.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[77](https://dblp.org/pid/129/0954-1.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yanyan Huang](https://dblp.org/pid/88/4316.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[78](https://dblp.org/pid/129/0954-1.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Deepak Jangid](https://dblp.org/pid/340/1460.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[79](https://dblp.org/pid/129/0954-1.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[80](https://dblp.org/pid/129/0954-1.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[81](https://dblp.org/pid/129/0954-1.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[82](https://dblp.org/pid/129/0954-1.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[83](https://dblp.org/pid/129/0954-1.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Shan Jin](https://dblp.org/pid/10/2477.html)

[\[j5\]](https://dblp.org/pid/129/0954-1.html#j5) [\[i3\]](https://dblp.org/pid/129/0954-1.html#i3)

[84](https://dblp.org/pid/129/0954-1.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[85](https://dblp.org/pid/129/0954-1.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[86](https://dblp.org/pid/129/0954-1.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Ze Kang](https://dblp.org/pid/340/1063.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[87](https://dblp.org/pid/129/0954-1.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jani Käpylä](https://dblp.org/pid/244/2529.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[88](https://dblp.org/pid/129/0954-1.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiao Ke](https://dblp.org/pid/78/9040.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[89](https://dblp.org/pid/129/0954-1.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[90](https://dblp.org/pid/129/0954-1.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Byeong Hak Kim](https://dblp.org/pid/214/8978.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[91](https://dblp.org/pid/129/0954-1.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Madhu Kiran](https://dblp.org/pid/39/10281.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[92](https://dblp.org/pid/129/0954-1.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[93](https://dblp.org/pid/129/0954-1.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[94](https://dblp.org/pid/129/0954-1.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Simiao Lai](https://dblp.org/pid/282/1954.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[95](https://dblp.org/pid/129/0954-1.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[96](https://dblp.org/pid/129/0954-1.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[97](https://dblp.org/pid/129/0954-1.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Dongwook Lee](https://dblp.org/pid/25/6543.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[98](https://dblp.org/pid/129/0954-1.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Hyunjeong Lee](https://dblp.org/pid/00/3423.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[99](https://dblp.org/pid/129/0954-1.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jun Ha Lee](https://dblp.org/pid/260/2774.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[100](https://dblp.org/pid/129/0954-1.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Seohyung Lee](https://dblp.org/pid/210/4662.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[101](https://dblp.org/pid/129/0954-1.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[102](https://dblp.org/pid/129/0954-1.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[103](https://dblp.org/pid/129/0954-1.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Chao Li](https://dblp.org/pid/66/190.html)

[\[j18\]](https://dblp.org/pid/129/0954-1.html#j18)

[104](https://dblp.org/pid/129/0954-1.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Dong Li 0016](https://dblp.org/pid/47/4826-16.html)

[\[c7\]](https://dblp.org/pid/129/0954-1.html#c7)

[105](https://dblp.org/pid/129/0954-1.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[106](https://dblp.org/pid/129/0954-1.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jianhua Li](https://dblp.org/pid/93/3389.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[107](https://dblp.org/pid/129/0954-1.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Ming Li 0010](https://dblp.org/pid/l/MingLi10.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[108](https://dblp.org/pid/129/0954-1.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Shuxin Li 0001](https://dblp.org/pid/84/4388-1.html)

[\[j2\]](https://dblp.org/pid/129/0954-1.html#j2) [\[c3\]](https://dblp.org/pid/129/0954-1.html#c3) [\[c2\]](https://dblp.org/pid/129/0954-1.html#c2)

[109](https://dblp.org/pid/129/0954-1.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wangkai Li](https://dblp.org/pid/340/1456.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[110](https://dblp.org/pid/129/0954-1.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xi Li 0001](https://dblp.org/pid/46/2311-1.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[111](https://dblp.org/pid/129/0954-1.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[112](https://dblp.org/pid/129/0954-1.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiao Li](https://dblp.org/pid/66/2069.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[113](https://dblp.org/pid/129/0954-1.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiaohong Li 0001](https://dblp.org/pid/08/2489-1.html)

[\[j12\]](https://dblp.org/pid/129/0954-1.html#j12) [\[j10\]](https://dblp.org/pid/129/0954-1.html#j10) [\[j4\]](https://dblp.org/pid/129/0954-1.html#j4) [\[c6\]](https://dblp.org/pid/129/0954-1.html#c6) [\[c5\]](https://dblp.org/pid/129/0954-1.html#c5) [\[c4\]](https://dblp.org/pid/129/0954-1.html#c4) [\[i2\]](https://dblp.org/pid/129/0954-1.html#i2) [\[i1\]](https://dblp.org/pid/129/0954-1.html#i1) [\[j2\]](https://dblp.org/pid/129/0954-1.html#j2) [\[c3\]](https://dblp.org/pid/129/0954-1.html#c3) [\[c2\]](https://dblp.org/pid/129/0954-1.html#c2) [\[c1\]](https://dblp.org/pid/129/0954-1.html#c1) [\[j1\]](https://dblp.org/pid/129/0954-1.html#j1)

[114](https://dblp.org/pid/129/0954-1.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xue Li](https://dblp.org/pid/181/2710.html)

[\[j17\]](https://dblp.org/pid/129/0954-1.html#j17)

[115](https://dblp.org/pid/129/0954-1.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yihong Li](https://dblp.org/pid/81/5405.html)

[\[j19\]](https://dblp.org/pid/129/0954-1.html#j19) [\[j16\]](https://dblp.org/pid/129/0954-1.html#j16) [\[j15\]](https://dblp.org/pid/129/0954-1.html#j15) [\[i5\]](https://dblp.org/pid/129/0954-1.html#i5) [\[i4\]](https://dblp.org/pid/129/0954-1.html#i4)

[116](https://dblp.org/pid/129/0954-1.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yuanbo Li](https://dblp.org/pid/198/2381.html)

[\[j18\]](https://dblp.org/pid/129/0954-1.html#j18)

[117](https://dblp.org/pid/129/0954-1.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yuezhou Li](https://dblp.org/pid/284/2562.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[118](https://dblp.org/pid/129/0954-1.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhe Li 0008](https://dblp.org/pid/11/751-8.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[119](https://dblp.org/pid/129/0954-1.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Liting Lin](https://dblp.org/pid/227/2204.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[120](https://dblp.org/pid/129/0954-1.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Haibin Ling](https://dblp.org/pid/93/3488.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[121](https://dblp.org/pid/129/0954-1.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Bingfu Liu](https://dblp.org/pid/251/7589.html)

[\[j10\]](https://dblp.org/pid/129/0954-1.html#j10)

[122](https://dblp.org/pid/129/0954-1.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[j14\]](https://dblp.org/pid/129/0954-1.html#j14) [\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[123](https://dblp.org/pid/129/0954-1.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[124](https://dblp.org/pid/129/0954-1.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jingen Liu](https://dblp.org/pid/10/5849.html)

[\[j14\]](https://dblp.org/pid/129/0954-1.html#j14) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[125](https://dblp.org/pid/129/0954-1.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Li Liu 0036](https://dblp.org/pid/33/4528-36.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[126](https://dblp.org/pid/129/0954-1.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Qingjie Liu 0001](https://dblp.org/pid/72/10584.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[127](https://dblp.org/pid/129/0954-1.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Si Liu 0001](https://dblp.org/pid/60/7642.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[128](https://dblp.org/pid/129/0954-1.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wanshu Liu](https://dblp.org/pid/223/7969.html)

[\[c4\]](https://dblp.org/pid/129/0954-1.html#c4)

[129](https://dblp.org/pid/129/0954-1.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wanting Liu](https://dblp.org/pid/157/6844.html)

[\[j19\]](https://dblp.org/pid/129/0954-1.html#j19) [\[j18\]](https://dblp.org/pid/129/0954-1.html#j18) [\[j17\]](https://dblp.org/pid/129/0954-1.html#j17) [\[j16\]](https://dblp.org/pid/129/0954-1.html#j16) [\[j15\]](https://dblp.org/pid/129/0954-1.html#j15) [\[i5\]](https://dblp.org/pid/129/0954-1.html#i5) [\[i4\]](https://dblp.org/pid/129/0954-1.html#i4)

[130](https://dblp.org/pid/129/0954-1.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wulong Liu](https://dblp.org/pid/36/9257.html)

[\[c7\]](https://dblp.org/pid/129/0954-1.html#c7)

[131](https://dblp.org/pid/129/0954-1.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[132](https://dblp.org/pid/129/0954-1.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wei Lu](https://dblp.org/pid/98/6613.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[133](https://dblp.org/pid/129/0954-1.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Liguang Luan](https://dblp.org/pid/310/7942.html)

[\[c9\]](https://dblp.org/pid/129/0954-1.html#c9)

[134](https://dblp.org/pid/129/0954-1.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jonathon Luiten](https://dblp.org/pid/211/7992.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[135](https://dblp.org/pid/129/0954-1.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[136](https://dblp.org/pid/129/0954-1.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Bingpeng Ma](https://dblp.org/pid/62/1822.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[137](https://dblp.org/pid/129/0954-1.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Chao Ma 0004](https://dblp.org/pid/79/1552-4.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[138](https://dblp.org/pid/129/0954-1.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[139](https://dblp.org/pid/129/0954-1.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yinchao Ma](https://dblp.org/pid/189/1326.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[140](https://dblp.org/pid/129/0954-1.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Ziang Ma](https://dblp.org/pid/165/9621.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[141](https://dblp.org/pid/129/0954-1.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Hangyu Mao](https://dblp.org/pid/191/6097.html)

[\[c7\]](https://dblp.org/pid/129/0954-1.html#c7)

[142](https://dblp.org/pid/129/0954-1.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[143](https://dblp.org/pid/129/0954-1.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[144](https://dblp.org/pid/129/0954-1.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[145](https://dblp.org/pid/129/0954-1.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[146](https://dblp.org/pid/129/0954-1.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhaopeng Meng](https://dblp.org/pid/67/8175.html)

[\[c7\]](https://dblp.org/pid/129/0954-1.html#c7) [\[j3\]](https://dblp.org/pid/129/0954-1.html#j3)

[147](https://dblp.org/pid/129/0954-1.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[148](https://dblp.org/pid/129/0954-1.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Payman Moallem](https://dblp.org/pid/63/5378.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[149](https://dblp.org/pid/129/0954-1.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[150](https://dblp.org/pid/129/0954-1.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[151](https://dblp.org/pid/129/0954-1.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yuzhen Niu](https://dblp.org/pid/28/7442.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[152](https://dblp.org/pid/129/0954-1.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Siyang Pan](https://dblp.org/pid/250/5753.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[153](https://dblp.org/pid/129/0954-1.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[ChangBeom Park](https://dblp.org/pid/340/0926.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[154](https://dblp.org/pid/129/0954-1.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[155](https://dblp.org/pid/129/0954-1.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Matthieu Paul](https://dblp.org/pid/255/6113.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[156](https://dblp.org/pid/129/0954-1.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[157](https://dblp.org/pid/129/0954-1.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[158](https://dblp.org/pid/129/0954-1.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yongqi Pi](https://dblp.org/pid/318/4583.html)

[\[j11\]](https://dblp.org/pid/129/0954-1.html#j11)

[159](https://dblp.org/pid/129/0954-1.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Shoumeng Qiu](https://dblp.org/pid/284/2537.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[160](https://dblp.org/pid/129/0954-1.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Aravindh Rajiv](https://dblp.org/pid/307/9144.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[161](https://dblp.org/pid/129/0954-1.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Muhammad Rana](https://dblp.org/pid/276/0222.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[162](https://dblp.org/pid/129/0954-1.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xuhong Ren](https://dblp.org/pid/138/4258.html)

[\[j8\]](https://dblp.org/pid/129/0954-1.html#j8)

[163](https://dblp.org/pid/129/0954-1.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[164](https://dblp.org/pid/129/0954-1.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Litu Rout](https://dblp.org/pid/206/6445.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[165](https://dblp.org/pid/129/0954-1.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Chen Sang](https://dblp.org/pid/231/1051.html)

[\[c9\]](https://dblp.org/pid/129/0954-1.html#c9)

[166](https://dblp.org/pid/129/0954-1.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Hasan Saribas](https://dblp.org/pid/225/3263.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[167](https://dblp.org/pid/129/0954-1.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Sandip Sen](https://dblp.org/pid/19/1004.html)

[\[j12\]](https://dblp.org/pid/129/0954-1.html#j12) [\[c6\]](https://dblp.org/pid/129/0954-1.html#c6)

[168](https://dblp.org/pid/129/0954-1.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[169](https://dblp.org/pid/129/0954-1.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[170](https://dblp.org/pid/129/0954-1.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Mohamed S. Shehata](https://dblp.org/pid/33/2495.html)

aka: Mohamed Shehata 0001

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[171](https://dblp.org/pid/129/0954-1.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Furao Shen](https://dblp.org/pid/80/4685.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[172](https://dblp.org/pid/129/0954-1.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jianbing Shen](https://dblp.org/pid/38/5435.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[173](https://dblp.org/pid/129/0954-1.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[174](https://dblp.org/pid/129/0954-1.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jiaojiao Song](https://dblp.org/pid/146/9110.html)

[\[j1\]](https://dblp.org/pid/129/0954-1.html#j1)

[175](https://dblp.org/pid/129/0954-1.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Tianhui Song](https://dblp.org/pid/181/8738.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[176](https://dblp.org/pid/129/0954-1.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[177](https://dblp.org/pid/129/0954-1.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Chao Sun](https://dblp.org/pid/54/3957.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[178](https://dblp.org/pid/129/0954-1.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jingna Sun](https://dblp.org/pid/255/0702.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[179](https://dblp.org/pid/129/0954-1.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Chunlei Tang](https://dblp.org/pid/211/4125.html)

[\[j13\]](https://dblp.org/pid/129/0954-1.html#j13)

[180](https://dblp.org/pid/129/0954-1.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Hongyao Tang](https://dblp.org/pid/220/4275.html)

[\[c7\]](https://dblp.org/pid/129/0954-1.html#c7)

[181](https://dblp.org/pid/129/0954-1.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Kun Tang](https://dblp.org/pid/93/1223.html)

[\[j17\]](https://dblp.org/pid/129/0954-1.html#j17)

[182](https://dblp.org/pid/129/0954-1.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[183](https://dblp.org/pid/129/0954-1.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yu Tian](https://dblp.org/pid/15/4658.html)

[\[j11\]](https://dblp.org/pid/129/0954-1.html#j11) [\[j7\]](https://dblp.org/pid/129/0954-1.html#j7) [\[c12\]](https://dblp.org/pid/129/0954-1.html#c12) [\[c9\]](https://dblp.org/pid/129/0954-1.html#c9)

[184](https://dblp.org/pid/129/0954-1.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[185](https://dblp.org/pid/129/0954-1.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[186](https://dblp.org/pid/129/0954-1.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[187](https://dblp.org/pid/129/0954-1.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Karl Tuyls](https://dblp.org/pid/t/KTuyls.html)

[\[j4\]](https://dblp.org/pid/129/0954-1.html#j4) [\[c5\]](https://dblp.org/pid/129/0954-1.html#c5) [\[i2\]](https://dblp.org/pid/129/0954-1.html#i2) [\[i1\]](https://dblp.org/pid/129/0954-1.html#i1) [\[c1\]](https://dblp.org/pid/129/0954-1.html#c1)

[188](https://dblp.org/pid/129/0954-1.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Bedirhan Uzun](https://dblp.org/pid/247/8937.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[189](https://dblp.org/pid/129/0954-1.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Om Prakash Verma](https://dblp.org/pid/61/8145.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[190](https://dblp.org/pid/129/0954-1.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Paul Voigtlaender](https://dblp.org/pid/166/6430.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[191](https://dblp.org/pid/129/0954-1.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Can Wang](https://dblp.org/pid/71/4716.html)

[\[j6\]](https://dblp.org/pid/129/0954-1.html#j6)

[192](https://dblp.org/pid/129/0954-1.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[193](https://dblp.org/pid/129/0954-1.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Fei Wang 0032](https://dblp.org/pid/52/3194-32.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[194](https://dblp.org/pid/129/0954-1.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Guangting Wang](https://dblp.org/pid/227/7195.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[195](https://dblp.org/pid/129/0954-1.html?view=joint&param=195 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Liang Wang 0001](https://dblp.org/pid/56/4499-1.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[196](https://dblp.org/pid/129/0954-1.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[197](https://dblp.org/pid/129/0954-1.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[198](https://dblp.org/pid/129/0954-1.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[199](https://dblp.org/pid/129/0954-1.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Linyuan Wang](https://dblp.org/pid/138/5963.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[200](https://dblp.org/pid/129/0954-1.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Qi Wang 0044](https://dblp.org/pid/19/1924-44.html)

[\[j18\]](https://dblp.org/pid/129/0954-1.html#j18) [\[j17\]](https://dblp.org/pid/129/0954-1.html#j17) [\[j16\]](https://dblp.org/pid/129/0954-1.html#j16) [\[j13\]](https://dblp.org/pid/129/0954-1.html#j13)

[201](https://dblp.org/pid/129/0954-1.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Qiang Wang 0023](https://dblp.org/pid/64/5630-23.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[202](https://dblp.org/pid/129/0954-1.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Weixun Wang](https://dblp.org/pid/84/998.html)

[\[c7\]](https://dblp.org/pid/129/0954-1.html#c7)

[203](https://dblp.org/pid/129/0954-1.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[204](https://dblp.org/pid/129/0954-1.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yunhong Wang 0001](https://dblp.org/pid/95/6251.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[205](https://dblp.org/pid/129/0954-1.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Chenyan Wu](https://dblp.org/pid/76/1190.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[206](https://dblp.org/pid/129/0954-1.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[207](https://dblp.org/pid/129/0954-1.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jinlin Wu](https://dblp.org/pid/123/7200.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[208](https://dblp.org/pid/129/0954-1.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[209](https://dblp.org/pid/129/0954-1.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[210](https://dblp.org/pid/129/0954-1.html?view=joint&param=210 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiaofei Xie](https://dblp.org/pid/127/0713.html)

[\[j7\]](https://dblp.org/pid/129/0954-1.html#j7) [\[j5\]](https://dblp.org/pid/129/0954-1.html#j5) [\[i3\]](https://dblp.org/pid/129/0954-1.html#i3)

[211](https://dblp.org/pid/129/0954-1.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Chao Xu 0003](https://dblp.org/pid/79/1442-3.html)

[\[j3\]](https://dblp.org/pid/129/0954-1.html#j3)

[212](https://dblp.org/pid/129/0954-1.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[213](https://dblp.org/pid/129/0954-1.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wei Xu 0017](https://dblp.org/pid/32/1213-17.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[214](https://dblp.org/pid/129/0954-1.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiang Xu](https://dblp.org/pid/126/2962.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[215](https://dblp.org/pid/129/0954-1.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yong Xu 0007](https://dblp.org/pid/07/4630-7.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[216](https://dblp.org/pid/129/0954-1.html?view=joint&param=216 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yuanyou Xu](https://dblp.org/pid/248/7663.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[217](https://dblp.org/pid/129/0954-1.html?view=joint&param=217 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[j16\]](https://dblp.org/pid/129/0954-1.html#j16) [\[j15\]](https://dblp.org/pid/129/0954-1.html#j15) [\[j14\]](https://dblp.org/pid/129/0954-1.html#j14) [\[j12\]](https://dblp.org/pid/129/0954-1.html#j12) [\[j11\]](https://dblp.org/pid/129/0954-1.html#j11) [\[j10\]](https://dblp.org/pid/129/0954-1.html#j10) [\[j8\]](https://dblp.org/pid/129/0954-1.html#j8) [\[j7\]](https://dblp.org/pid/129/0954-1.html#j7) [\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[j5\]](https://dblp.org/pid/129/0954-1.html#j5) [\[c9\]](https://dblp.org/pid/129/0954-1.html#c9) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8) [\[i3\]](https://dblp.org/pid/129/0954-1.html#i3) [\[j4\]](https://dblp.org/pid/129/0954-1.html#j4) [\[j3\]](https://dblp.org/pid/129/0954-1.html#j3) [\[c6\]](https://dblp.org/pid/129/0954-1.html#c6) [\[i2\]](https://dblp.org/pid/129/0954-1.html#i2) [\[i1\]](https://dblp.org/pid/129/0954-1.html#i1)

[218](https://dblp.org/pid/129/0954-1.html?view=joint&param=218 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zizheng Xun](https://dblp.org/pid/340/1441.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[219](https://dblp.org/pid/129/0954-1.html?view=joint&param=219 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[220](https://dblp.org/pid/129/0954-1.html?view=joint&param=220 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[221](https://dblp.org/pid/129/0954-1.html?view=joint&param=221 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Dawei Yang](https://dblp.org/pid/22/1038.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[222](https://dblp.org/pid/129/0954-1.html?view=joint&param=222 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[223](https://dblp.org/pid/129/0954-1.html?view=joint&param=223 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Qingyu Yang 0003](https://dblp.org/pid/01/2404-3.html)

[\[j9\]](https://dblp.org/pid/129/0954-1.html#j9) [\[c10\]](https://dblp.org/pid/129/0954-1.html#c10)

[224](https://dblp.org/pid/129/0954-1.html?view=joint&param=224 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Tianpei Yang](https://dblp.org/pid/184/8221.html)

[\[j11\]](https://dblp.org/pid/129/0954-1.html#j11) [\[j7\]](https://dblp.org/pid/129/0954-1.html#j7) [\[c7\]](https://dblp.org/pid/129/0954-1.html#c7) [\[c4\]](https://dblp.org/pid/129/0954-1.html#c4)

[225](https://dblp.org/pid/129/0954-1.html?view=joint&param=225 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[226](https://dblp.org/pid/129/0954-1.html?view=joint&param=226 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wenyan Yang](https://dblp.org/pid/119/2426.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[227](https://dblp.org/pid/129/0954-1.html?view=joint&param=227 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[228](https://dblp.org/pid/129/0954-1.html?view=joint&param=228 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yi Yang 0001](https://dblp.org/pid/33/4854-1.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[229](https://dblp.org/pid/129/0954-1.html?view=joint&param=229 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yichun Yang](https://dblp.org/pid/249/9678.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[230](https://dblp.org/pid/129/0954-1.html?view=joint&param=230 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zongxin Yang](https://dblp.org/pid/249/5456.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[231](https://dblp.org/pid/129/0954-1.html?view=joint&param=231 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Botao Ye](https://dblp.org/pid/227/4610.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[232](https://dblp.org/pid/129/0954-1.html?view=joint&param=232 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yu Ye 0004](https://dblp.org/pid/129/0969-4.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[233](https://dblp.org/pid/129/0954-1.html?view=joint&param=233 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[J. Yin](https://dblp.org/pid/51/2242.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[234](https://dblp.org/pid/129/0954-1.html?view=joint&param=234 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jun Yin 0003](https://dblp.org/pid/58/5423-3.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[235](https://dblp.org/pid/129/0954-1.html?view=joint&param=235 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Fisher Yu 0001](https://dblp.org/pid/117/6314.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[236](https://dblp.org/pid/129/0954-1.html?view=joint&param=236 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Hongyuan Yu](https://dblp.org/pid/232/2265.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[237](https://dblp.org/pid/129/0954-1.html?view=joint&param=237 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jiaqian Yu](https://dblp.org/pid/164/7325.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[238](https://dblp.org/pid/129/0954-1.html?view=joint&param=238 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Qianjin Yu](https://dblp.org/pid/53/10179.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[239](https://dblp.org/pid/129/0954-1.html?view=joint&param=239 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Weichen Yu](https://dblp.org/pid/325/1209.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[240](https://dblp.org/pid/129/0954-1.html?view=joint&param=240 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Kang Ze](https://dblp.org/pid/340/1107.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[241](https://dblp.org/pid/129/0954-1.html?view=joint&param=241 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jiang Zhai](https://dblp.org/pid/291/9340.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[242](https://dblp.org/pid/129/0954-1.html?view=joint&param=242 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Furui Zhan](https://dblp.org/pid/196/4796.html)

[\[j19\]](https://dblp.org/pid/129/0954-1.html#j19) [\[j17\]](https://dblp.org/pid/129/0954-1.html#j17) [\[j16\]](https://dblp.org/pid/129/0954-1.html#j16) [\[j15\]](https://dblp.org/pid/129/0954-1.html#j15) [\[i5\]](https://dblp.org/pid/129/0954-1.html#i5) [\[i4\]](https://dblp.org/pid/129/0954-1.html#i4)

[243](https://dblp.org/pid/129/0954-1.html?view=joint&param=243 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Chunhu Zhang](https://dblp.org/pid/292/0953.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[244](https://dblp.org/pid/129/0954-1.html?view=joint&param=244 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[245](https://dblp.org/pid/129/0954-1.html?view=joint&param=245 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Feiye Zhang](https://dblp.org/pid/73/1183.html)

[\[j9\]](https://dblp.org/pid/129/0954-1.html#j9)

[246](https://dblp.org/pid/129/0954-1.html?view=joint&param=246 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Haitao Zhang](https://dblp.org/pid/19/6669.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[247](https://dblp.org/pid/129/0954-1.html?view=joint&param=247 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[j14\]](https://dblp.org/pid/129/0954-1.html#j14) [\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[248](https://dblp.org/pid/129/0954-1.html?view=joint&param=248 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Kangkai Zhang](https://dblp.org/pid/260/2990.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[249](https://dblp.org/pid/129/0954-1.html?view=joint&param=249 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Shiqi Zhang](https://dblp.org/pid/03/9964.html)

[\[c12\]](https://dblp.org/pid/129/0954-1.html#c12)

[250](https://dblp.org/pid/129/0954-1.html?view=joint&param=250 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Tianzhu Zhang 0001](https://dblp.org/pid/15/7643-1.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[251](https://dblp.org/pid/129/0954-1.html?view=joint&param=251 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Wenkang Zhang](https://dblp.org/pid/340/0966.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[252](https://dblp.org/pid/129/0954-1.html?view=joint&param=252 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiaohan Zhang](https://dblp.org/pid/96/6053.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[253](https://dblp.org/pid/129/0954-1.html?view=joint&param=253 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xiaolin Zhang](https://dblp.org/pid/99/2516.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[254](https://dblp.org/pid/129/0954-1.html?view=joint&param=254 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xinyu Zhang 0020](https://dblp.org/pid/58/4582-20.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[255](https://dblp.org/pid/129/0954-1.html?view=joint&param=255 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yang Zhang 0097](https://dblp.org/pid/06/6785-97.html)

[\[c10\]](https://dblp.org/pid/129/0954-1.html#c10)

[256](https://dblp.org/pid/129/0954-1.html?view=joint&param=256 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yushan Zhang](https://dblp.org/pid/50/10702.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[257](https://dblp.org/pid/129/0954-1.html?view=joint&param=257 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhe Zhang 0039](https://dblp.org/pid/87/5809-39.html)

[\[j8\]](https://dblp.org/pid/129/0954-1.html#j8)

[258](https://dblp.org/pid/129/0954-1.html?view=joint&param=258 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[j14\]](https://dblp.org/pid/129/0954-1.html#j14) [\[j7\]](https://dblp.org/pid/129/0954-1.html#j7) [\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[259](https://dblp.org/pid/129/0954-1.html?view=joint&param=259 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhipeng Zhang](https://dblp.org/pid/49/4941.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[260](https://dblp.org/pid/129/0954-1.html?view=joint&param=260 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[261](https://dblp.org/pid/129/0954-1.html?view=joint&param=261 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jie Zhao 0014](https://dblp.org/pid/23/3168-14.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[262](https://dblp.org/pid/129/0954-1.html?view=joint&param=262 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[263](https://dblp.org/pid/129/0954-1.html?view=joint&param=263 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xintian Zhao](https://dblp.org/pid/318/6762.html)

[\[j12\]](https://dblp.org/pid/129/0954-1.html#j12) [\[c12\]](https://dblp.org/pid/129/0954-1.html#c12)

[264](https://dblp.org/pid/129/0954-1.html?view=joint&param=264 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Ming Zhen](https://dblp.org/pid/307/8430.html)

[\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[265](https://dblp.org/pid/129/0954-1.html?view=joint&param=265 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Feng Zheng 0001](https://dblp.org/pid/39/800-1.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[266](https://dblp.org/pid/129/0954-1.html?view=joint&param=266 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Haixia Zheng](https://dblp.org/pid/119/1585.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[267](https://dblp.org/pid/129/0954-1.html?view=joint&param=267 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Kangjie Zheng](https://dblp.org/pid/249/2602.html)

[\[j11\]](https://dblp.org/pid/129/0954-1.html#j11) [\[c12\]](https://dblp.org/pid/129/0954-1.html#c12)

[268](https://dblp.org/pid/129/0954-1.html?view=joint&param=268 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Longji Zheng](https://dblp.org/pid/401/9939.html)

[\[j19\]](https://dblp.org/pid/129/0954-1.html#j19) [\[i4\]](https://dblp.org/pid/129/0954-1.html#i4)

[269](https://dblp.org/pid/129/0954-1.html?view=joint&param=269 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Min Zheng](https://dblp.org/pid/23/328.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

[270](https://dblp.org/pid/129/0954-1.html?view=joint&param=270 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[271](https://dblp.org/pid/129/0954-1.html?view=joint&param=271 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Kailing Zhou](https://dblp.org/pid/382/4660.html)

[\[j19\]](https://dblp.org/pid/129/0954-1.html#j19) [\[j16\]](https://dblp.org/pid/129/0954-1.html#j16) [\[j15\]](https://dblp.org/pid/129/0954-1.html#j15) [\[i5\]](https://dblp.org/pid/129/0954-1.html#i5) [\[i4\]](https://dblp.org/pid/129/0954-1.html#i4)

[272](https://dblp.org/pid/129/0954-1.html?view=joint&param=272 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Zhifeng Zhou](https://dblp.org/pid/231/4770.html)

[\[j6\]](https://dblp.org/pid/129/0954-1.html#j6)

[273](https://dblp.org/pid/129/0954-1.html?view=joint&param=273 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[274](https://dblp.org/pid/129/0954-1.html?view=joint&param=274 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11) [\[c8\]](https://dblp.org/pid/129/0954-1.html#c8)

[275](https://dblp.org/pid/129/0954-1.html?view=joint&param=275 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/129/0954-1.html?view=group&param=1)

[Yueting Zhuang](https://dblp.org/pid/218/7793.html)

[\[c11\]](https://dblp.org/pid/129/0954-1.html#c11)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/129/0954-1.html#) [\[–\]](https://dblp.org/pid/129/0954-1.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/129/0954-1.html#) [\[–\]](https://dblp.org/pid/129/0954-1.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/129/0954-1.html#) [\[–\]](https://dblp.org/pid/129/0954-1.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/129/0954-1.html#) [\[–\]](https://dblp.org/pid/129/0954-1.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/129/0954-1.html#) [\[–\]](https://dblp.org/pid/129/0954-1.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)