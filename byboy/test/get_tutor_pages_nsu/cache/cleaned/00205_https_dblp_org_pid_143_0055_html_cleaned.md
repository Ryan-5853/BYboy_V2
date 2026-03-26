> 抓取来源：https://dblp.org/pid/143/0055.html

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

- [Yan-peng Sun](https://dblp.org/pid/142/1543.html)

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Yanpeng+Sun%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F143%2F0055%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Yanpeng+Sun+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F143%2F0055%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Yanpeng+Sun+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F143%2F0055%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Yanpeng+Sun%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F143%2F0055%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Yanpeng+Sun+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F143%2F0055%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Yanpeng+Sun%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F143%2F0055%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Yanpeng+Sun%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F143%2F0055%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F143%2F0055%3E+%7D+.%0A%0A%7D)

_showing all53 records_

20142026102014: 12015: 12016: 12017: 12018: 32018: 32019: 62019: 62021: 32021: 32022: 62022: 62022: 62023: 42023: 42023: 42024: 102024: 102024: 102025: 162025: 162025: 162026: 1

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

- ![](https://dblp.org/img/add-mark.12x12.png)Zechao Li (22)
- ![](https://dblp.org/img/add-mark.12x12.png)Jingdong Wang 0001 (13)
- ![](https://dblp.org/img/add-mark.12x12.png)Qiang Chen 0007 (11)
- ![](https://dblp.org/img/add-mark.12x12.png)Lele Qu (9)
- ![](https://dblp.org/img/add-mark.12x12.png)Shan Zhang 0002 (8)
- ![](https://dblp.org/img/add-mark.12x12.png)Gang Zhang (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Chenzhong Bin (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Tianlong Gu (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Liang Chang 0003 (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Tianhong Yang (6)

- _109 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (46)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0001-6249-5596 (5)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0001-8683-7423 (2)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (22)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Geosci. Remote. Sens. Lett. (5)
- ![](https://dblp.org/img/add-mark.12x12.png)PRICAI (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Pattern Anal. Mach. Intell. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (2)
- ![](https://dblp.org/img/add-mark.12x12.png)IGARSS (2)
- ![](https://dblp.org/img/add-mark.12x12.png)计算机科学 (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ICETT (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Multim. Tools Appl. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Inf. Forensics Secur. (1)

- _15 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)open (27)
- ![](https://dblp.org/img/add-mark.12x12.png)closed (26)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[j19\]
[Peng Xing](https://dblp.org/pid/221/2336.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ning Wang](https://dblp.org/pid/46/2005-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Yanpeng Sun![](https://dblp.org/img/orcid-mark.12x12.png), [Jinhui Tang](https://dblp.org/pid/75/1030.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zechao Li](https://dblp.org/pid/51/8693.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Refine, Control and Distill: A Text-to-Image Framework for Faithful Image Generation. [IEEE Trans. Pattern Anal. Mach. Intell.48(3)](https://dblp.org/db/journals/pami/pami48.html#journals/pami/XingWSTL26): 2296-2311 (2026)
- ![](https://dblp.org/img/n.png)

\[j18\]
[Haiqi Zhang](https://dblp.org/pid/10/6011.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hao Tang](https://dblp.org/pid/07/5751-7.html)![](https://dblp.org/img/orcid-mark.12x12.png), Yanpeng Sun![](https://dblp.org/img/orcid-mark.12x12.png), [Zechao Li](https://dblp.org/pid/51/8693.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Gradient Pruning Interactive Attack for Vision-Language Pre-Training Models. [IEEE Trans. Dependable Secur. Comput.23(2)](https://dblp.org/db/journals/tdsc/tdsc23.html#journals/tdsc/ZhangTSL26): 2198-2214 (2026)
- 2025
- ![](https://dblp.org/img/n.png)

\[j17\]
Yanpeng Sun, [Zechao Li](https://dblp.org/pid/51/8693.html):

SSA: semantic structure aware inference on CNN networks for weakly pixel-wise dense predictions without cost. [Frontiers Comput. Sci.19(2)](https://dblp.org/db/journals/fcsc/fcsc19.html#journals/fcsc/SunL25): 192702 (2025)
- ![](https://dblp.org/img/n.png)

\[j16\]
[Haiqi Zhang](https://dblp.org/pid/10/6011.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hao Tang](https://dblp.org/pid/07/5751-7.html)![](https://dblp.org/img/orcid-mark.12x12.png), Yanpeng Sun![](https://dblp.org/img/orcid-mark.12x12.png), [Shengfeng He](https://dblp.org/pid/38/9555.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zechao Li](https://dblp.org/pid/51/8693.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Modality-Specific Interactive Attack for Vision-Language Pre-Training Models. [IEEE Trans. Inf. Forensics Secur.20](https://dblp.org/db/journals/tifs/tifs20.html#journals/tifs/ZhangTSHL25): 5663-5677 (2025)
- ![](https://dblp.org/img/n.png)

\[j15\]
Yanpeng Sun![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Chen](https://dblp.org/pid/62/2719-7.html), [Jian Wang](https://dblp.org/pid/39/449-66.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html), [Zechao Li](https://dblp.org/pid/51/8693.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Exploring Effective Factors for Improving Visual In-Context Learning. [IEEE Trans. Image Process.34](https://dblp.org/db/journals/tip/tip34.html#journals/tip/SunCWWL25): 2147-2160 (2025)
- ![](https://dblp.org/img/n.png)

\[c13\]
[Ke Zhu](https://dblp.org/pid/32/4014.html), [Yu Wang](https://dblp.org/pid/02/5889.html), Yanpeng Sun, [Qiang Chen](https://dblp.org/pid/62/2719-7.html), [Jiangjiang Liu](https://dblp.org/pid/344/2055.html), [Gang Zhang](https://dblp.org/pid/37/4096.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html):

Continual SFT Matches Multimodal RLHF with Negative Supervision. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/ZhuWS00Z025): 14615-14624
- ![](https://dblp.org/img/n.png)

\[c12\]
[Shan Zhang](https://dblp.org/pid/14/6026-2.html), [Aotian Chen](https://dblp.org/pid/366/0538.html), Yanpeng Sun, [Jindong Gu](https://dblp.org/pid/232/2128.html), [Yi-Yu Zheng](https://dblp.org/pid/397/4097.html), [Piotr Koniusz](https://dblp.org/pid/25/8616.html), [Kai Zou](https://dblp.org/pid/135/5092.html), [Anton van den Hengel](https://dblp.org/pid/v/AntonvandenHengel.html), [Yuan Xue](https://dblp.org/pid/41/5526-2.html):

Primitive Vision: Improving Diagram Understanding in MLLMs. [ICML2025](https://dblp.org/db/conf/icml/icml2025.html#conf/icml/0002CSGZKZHX25)
- ![](https://dblp.org/img/n.png)

\[i22\]
[Shan Zhang](https://dblp.org/pid/14/6026-2.html), [Aotian Chen](https://dblp.org/pid/366/0538.html), Yanpeng Sun, [Jindong Gu](https://dblp.org/pid/232/2128.html), [Yi-Yu Zheng](https://dblp.org/pid/397/4097.html), [Piotr Koniusz](https://dblp.org/pid/25/8616.html), [Kai Zou](https://dblp.org/pid/135/5092.html), [Anton van den Hengel](https://dblp.org/pid/v/AntonvandenHengel.html), [Yuan Xue](https://dblp.org/pid/41/5526-2.html):

Open Eyes, Then Reason: Fine-grained Visual Mathematical Understanding in MLLMs. [CoRRabs/2501.06430](https://dblp.org/db/journals/corr/corr2501.html#journals/corr/abs-2501-06430) (2025)
- ![](https://dblp.org/img/n.png)

\[i21\]
[Wei Tang](https://dblp.org/pid/58/1874-11.html), Yanpeng Sun, [Qinying Gu](https://dblp.org/pid/365/4635.html), [Zechao Li](https://dblp.org/pid/51/8693.html):

Visual Position Prompt for MLLM based Visual Grounding. [CoRRabs/2503.15426](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-15426) (2025)
- ![](https://dblp.org/img/n.png)

\[i20\]
Yanpeng Sun, [Shan Zhang](https://dblp.org/pid/14/6026-2.html), [Wei Tang](https://dblp.org/pid/58/1874-11.html), [Aotian Chen](https://dblp.org/pid/366/0538.html), [Piotr Koniusz](https://dblp.org/pid/25/8616.html), [Kai Zou](https://dblp.org/pid/135/5092.html), [Yuan Xue](https://dblp.org/pid/41/5526-2.html), [Anton van den Hengel](https://dblp.org/pid/v/AntonvandenHengel.html):

MATHGLANCE: Multimodal Large Language Models Do Not Know Where to Look in Mathematical Diagrams. [CoRRabs/2503.20745](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-20745) (2025)
- ![](https://dblp.org/img/n.png)

\[i19\]
[Ming Dai](https://dblp.org/pid/61/6981.html), [Wenxuan Cheng](https://dblp.org/pid/370/2615.html), [Jiang-jiang Liu](https://dblp.org/pid/409/9085.html), [Sen Yang](https://dblp.org/pid/90/4655.html), [Wenxiao Cai](https://dblp.org/pid/348/4892.html), Yanpeng Sun, [Wankou Yang](https://dblp.org/pid/99/3602.html):

DeRIS: Decoupling Perception and Cognition for Enhanced Referring Image Segmentation through Loopback Synergy. [CoRRabs/2507.01738](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-01738) (2025)
- ![](https://dblp.org/img/n.png)

\[i18\]
[Jing Hao](https://dblp.org/pid/21/2724.html), [Yuxuan Fan](https://dblp.org/pid/227/4963.html), Yanpeng Sun, [Kaixin Guo](https://dblp.org/pid/417/5244.html), [Lizhuo Lin](https://dblp.org/pid/412/5549.html), [Jinrong Yang](https://dblp.org/pid/286/5463.html), [Qi Yong H. Ai](https://dblp.org/pid/410/9263.html), [Lun M. Wong](https://dblp.org/pid/417/5514.html), [Hao Tang](https://dblp.org/pid/07/5751-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kuo Feng Hung](https://dblp.org/pid/367/4460.html):

Towards Better Dental AI: A Multimodal Benchmark and Instruction Dataset for Panoramic X-ray Analysis. [CoRRabs/2509.09254](https://dblp.org/db/journals/corr/corr2509.html#journals/corr/abs-2509-09254) (2025)
- ![](https://dblp.org/img/n.png)

\[i17\]
[Weihao Bo](https://dblp.org/pid/327/6215.html), Yanpeng Sun, [Yu Wang](https://dblp.org/pid/02/5889.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-17.html), [Zechao Li](https://dblp.org/pid/51/8693.html):

FedMGP: Personalized Federated Learning with Multi-Group Text-Visual Prompts. [CoRRabs/2511.00480](https://dblp.org/db/journals/corr/corr2511.html#journals/corr/abs-2511-00480) (2025)
- ![](https://dblp.org/img/n.png)

\[i16\]
[Xiaofan Li](https://dblp.org/pid/50/3937.html), Yanpeng Sun, [Chenming Wu](https://dblp.org/pid/190/5879.html), [Fan Duan](https://dblp.org/pid/357/8693.html), [YuAn Wang](https://dblp.org/pid/423/6899.html), [Weihao Bo](https://dblp.org/pid/327/6215.html), [Yumeng Zhang](https://dblp.org/pid/26/4355.html), [Dingkang Liang](https://dblp.org/pid/255/6274.html):

Video4Edit: Viewing Image Editing as a Degenerate Temporal Process. [CoRRabs/2511.18131](https://dblp.org/db/journals/corr/corr2511.html#journals/corr/abs-2511-18131) (2025)
- ![](https://dblp.org/img/n.png)

\[i15\]
[Xiaofan Li](https://dblp.org/pid/50/3937.html), [Chenming Wu](https://dblp.org/pid/190/5879.html), Yanpeng Sun, [Jiaming Zhou](https://dblp.org/pid/250/0527.html), [Delin Qu](https://dblp.org/pid/73/2731.html), [Yansong Qu](https://dblp.org/pid/260/3675.html), [Weihao Bo](https://dblp.org/pid/327/6215.html), [Haibao Yu](https://dblp.org/pid/246/4643.html), [Dingkang Liang](https://dblp.org/pid/255/6274.html):

FVAR: Visual Autoregressive Modeling via Next Focus Prediction. [CoRRabs/2511.18838](https://dblp.org/db/journals/corr/corr2511.html#journals/corr/abs-2511-18838) (2025)
- ![](https://dblp.org/img/n.png)

\[i14\]
[Weihao Bo](https://dblp.org/pid/327/6215.html), [Shan Zhang](https://dblp.org/pid/14/6026-2.html), Yanpeng Sun, [Jingjing Wu](https://dblp.org/pid/27/2384.html), [Qunyi Xie](https://dblp.org/pid/172/9555.html), [Xiao Tan](https://dblp.org/pid/116/7143-1.html), [Kunbin Chen](https://dblp.org/pid/147/4644.html), [Wei He](https://dblp.org/pid/20/6417.html), [Xiaofan Li](https://dblp.org/pid/50/3937.html), [Na Zhao](https://dblp.org/pid/35/3393-4.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html), [Zechao Li](https://dblp.org/pid/51/8693.html):

Agentic Learner with Grow-and-Refine Multimodal Semantic Memory. [CoRRabs/2511.21678](https://dblp.org/db/journals/corr/corr2511.html#journals/corr/abs-2511-21678) (2025)
- ![](https://dblp.org/img/n.png)

\[i13\]
[Jing Hao](https://dblp.org/pid/21/2724.html), [Yuci Liang](https://dblp.org/pid/394/6550.html), [Lizhuo Lin](https://dblp.org/pid/412/5549.html), [Yuxuan Fan](https://dblp.org/pid/227/4963.html), [Wenkai Zhou](https://dblp.org/pid/228/1980.html), [Kaixin Guo](https://dblp.org/pid/417/5244.html), [Zanting Ye](https://dblp.org/pid/356/2713.html), Yanpeng Sun, [Xinyu Zhang](https://dblp.org/pid/58/4582.html), [Yanqi Yang](https://dblp.org/pid/252/1899.html), [Qiankun Li](https://dblp.org/pid/228/7339.html), [Hao Tang](https://dblp.org/pid/07/5751.html), [James Kit-Hon Tsoi](https://dblp.org/pid/423/6078.html), [Linlin Shen](https://dblp.org/pid/88/5607.html), [Kuo Feng Hung](https://dblp.org/pid/367/4460.html):

OralGPT-Omni: A Versatile Dental Multimodal Large Language Model. [CoRRabs/2511.22055](https://dblp.org/db/journals/corr/corr2511.html#journals/corr/abs-2511-22055) (2025)
- ![](https://dblp.org/img/n.png)

\[i12\]
[Wei Tang](https://dblp.org/pid/58/1874-11.html), Yanpeng Sun, [Shan Zhang](https://dblp.org/pid/14/6026-2.html), [Xiaofan Li](https://dblp.org/pid/50/3937.html), [Piotr Koniusz](https://dblp.org/pid/25/8616.html), [Wei Li](https://dblp.org/pid/64/6025.html), [Na Zhao](https://dblp.org/pid/35/3393-4.html), [Zechao Li](https://dblp.org/pid/51/8693.html):

Artemis: Structured Visual Reasoning for Perception Policy Learning. [CoRRabs/2512.01988](https://dblp.org/db/journals/corr/corr2512.html#journals/corr/abs-2512-01988) (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j14\]
[Lele Qu](https://dblp.org/pid/32/9864.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiyue Hu](https://dblp.org/pid/03/9972.html), [Tianhong Yang](https://dblp.org/pid/117/7216.html), [Lili Zhang](https://dblp.org/pid/00/6528.html), Yanpeng Sun:

Clutter Suppression for Through-the-Wall Radar Based on Robust Non-Negative Matrix Factorization in Dual-Domain. [IEEE Geosci. Remote. Sens. Lett.21](https://dblp.org/db/journals/lgrs/lgrs21.html#journals/lgrs/QuHYZS24): 1-5 (2024)
- ![](https://dblp.org/img/n.png)

\[j13\]
[Peng Xing](https://dblp.org/pid/221/2336.html)![](https://dblp.org/img/orcid-mark.12x12.png), Yanpeng Sun![](https://dblp.org/img/orcid-mark.12x12.png), [Dan Zeng](https://dblp.org/pid/06/6575-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zechao Li](https://dblp.org/pid/51/8693.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Normal Image Guided Segmentation Framework for Unsupervised Anomaly Detection. [IEEE Trans. Circuits Syst. Video Technol.34(6)](https://dblp.org/db/journals/tcsv/tcsv34.html#journals/tcsv/XingSZL24): 4639-4652 (2024)
- ![](https://dblp.org/img/n.png)

\[c11\]
Yanpeng Sun, [Jiahui Chen](https://dblp.org/pid/122/5100.html), [Shan Zhang](https://dblp.org/pid/14/6026-2.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-17.html), [Qiang Chen](https://dblp.org/pid/62/2719-7.html), [Gang Zhang](https://dblp.org/pid/37/4096.html), [Errui Ding](https://dblp.org/pid/180/5531.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html), [Zechao Li](https://dblp.org/pid/51/8693.html):

VRP-SAM: SAM with Visual Reference Prompt. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/SunCZZCZDWL24): 23565-23574
- ![](https://dblp.org/img/n.png)

\[c10\]
[Chenguang Zhao](https://dblp.org/pid/67/4612.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qizhi Fang](https://dblp.org/pid/97/1149.html)![](https://dblp.org/img/orcid-mark.12x12.png), Yanpeng Sun![](https://dblp.org/img/orcid-mark.12x12.png):

Research and Design of Blended Learning of EDA Technology Course Based on CDIO. [ICETT2024](https://dblp.org/db/conf/icett/icett2024.html#conf/icett/ZhaoFS24): 16-21
- ![](https://dblp.org/img/n.png)

\[i11\]
Yanpeng Sun, [Jiahui Chen](https://dblp.org/pid/122/5100.html), [Shan Zhang](https://dblp.org/pid/14/6026-2.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-17.html), [Qiang Chen](https://dblp.org/pid/62/2719-7.html), [Gang Zhang](https://dblp.org/pid/37/4096.html), [Errui Ding](https://dblp.org/pid/180/5531.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html), [Zechao Li](https://dblp.org/pid/51/8693.html):

VRP-SAM: SAM with Visual Reference Prompt. [CoRRabs/2402.17726](https://dblp.org/db/journals/corr/corr2402.html#journals/corr/abs-2402-17726) (2024)
- ![](https://dblp.org/img/n.png)

\[i10\]
[Peng Xing](https://dblp.org/pid/221/2336.html), [Haofan Wang](https://dblp.org/pid/234/7841.html), Yanpeng Sun, [Qixun Wang](https://dblp.org/pid/256/6758-1.html), [Xu Bai](https://dblp.org/pid/91/6242.html), [Hao Ai](https://dblp.org/pid/286/5383.html), [Renyuan Huang](https://dblp.org/pid/382/6720.html), [Zechao Li](https://dblp.org/pid/51/8693.html):

CSGO: Content-Style Composition in Text-to-Image Generation. [CoRRabs/2408.16766](https://dblp.org/db/journals/corr/corr2408.html#journals/corr/abs-2408-16766) (2024)
- ![](https://dblp.org/img/n.png)

\[i9\]
[Jing Hao](https://dblp.org/pid/21/2724.html), [Yuxiang Zhao](https://dblp.org/pid/181/2467.html), [Song Chen](https://dblp.org/pid/04/4291.html), Yanpeng Sun, [Qiang Chen](https://dblp.org/pid/62/2719-7.html), [Gang Zhang](https://dblp.org/pid/37/4096.html), [Kun Yao](https://dblp.org/pid/03/6550.html), [Errui Ding](https://dblp.org/pid/180/5531.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html):

FullAnno: A Data Engine for Enhancing Image Comprehension of MLLMs. [CoRRabs/2409.13540](https://dblp.org/db/journals/corr/corr2409.html#journals/corr/abs-2409-13540) (2024)
- ![](https://dblp.org/img/n.png)

\[i8\]
Yanpeng Sun, [Huaxin Zhang](https://dblp.org/pid/72/1833.html), [Qiang Chen](https://dblp.org/pid/62/2719-7.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-17.html), [Nong Sang](https://dblp.org/pid/10/1545.html), [Gang Zhang](https://dblp.org/pid/37/4096.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html), [Zechao Li](https://dblp.org/pid/51/8693.html):

Improving Multi-modal Large Language Model through Boosting Vision Capabilities. [CoRRabs/2410.13733](https://dblp.org/db/journals/corr/corr2410.html#journals/corr/abs-2410-13733) (2024)
- ![](https://dblp.org/img/n.png)

\[i7\]
[Ke Zhu](https://dblp.org/pid/32/4014.html), [Yu Wang](https://dblp.org/pid/02/5889.html), Yanpeng Sun, [Qiang Chen](https://dblp.org/pid/62/2719-7.html), [Jiangjiang Liu](https://dblp.org/pid/344/2055.html), [Gang Zhang](https://dblp.org/pid/37/4096.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html):

Continual SFT Matches Multimodal RLHF with Negative Supervision. [CoRRabs/2411.14797](https://dblp.org/db/journals/corr/corr2411.html#journals/corr/abs-2411-14797) (2024)
- ![](https://dblp.org/img/n.png)

\[i6\]
Yanpeng Sun, [Jing Hao](https://dblp.org/pid/21/2724.html), [Ke Zhu](https://dblp.org/pid/32/4014.html), [Jiangjiang Liu](https://dblp.org/pid/344/2055.html), [Yuxiang Zhao](https://dblp.org/pid/181/2467.html), [Xiaofan Li](https://dblp.org/pid/50/3937.html), [Gang Zhang](https://dblp.org/pid/37/4096.html), [Zechao Li](https://dblp.org/pid/51/8693.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html):

Descriptive Caption Enhancement with Visual Specialists for Multimodal Perception. [CoRRabs/2412.14233](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-14233) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j12\]
[Yuqing Ding](https://dblp.org/pid/236/6555.html), Yanpeng Sun, [Zechao Li](https://dblp.org/pid/51/8693.html):

Who is partner: A new perspective on data association of multi-object tracking. [Image Vis. Comput.136](https://dblp.org/db/journals/ivc/ivc136.html#journals/ivc/DingSL23): 104737 (2023)
- ![](https://dblp.org/img/n.png)

\[c9\]
[Jinhao Du](https://dblp.org/pid/312/4875.html), [Shan Zhang](https://dblp.org/pid/14/6026-2.html), [Qiang Chen](https://dblp.org/pid/62/2719-7.html), [Haifeng Le](https://dblp.org/pid/366/3250.html), Yanpeng Sun, [Yao Ni](https://dblp.org/pid/222/7928.html), [Jian Wang](https://dblp.org/pid/39/449-66.html), [Bin He](https://dblp.org/pid/78/4523.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html):

σ-Adaptive Decoupled Prototype for Few-Shot Object Detection. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/DuZCLSNWH023): 18904-18914
- ![](https://dblp.org/img/n.png)

\[c8\]
Yanpeng Sun![](https://dblp.org/img/orcid-mark.12x12.png), [Jinhai Miao](https://dblp.org/pid/360/5915.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Research on Unmanned Aerial Vehicle Flight Attitude Control Method Based on Sparrow Search Algorithm and PID Optimization. [UAVM2023](https://dblp.org/db/conf/uavm/uavm2023.html#conf/uavm/SunM23): 73-77
- ![](https://dblp.org/img/n.png)

\[i5\]
Yanpeng Sun, [Qiang Chen](https://dblp.org/pid/62/2719-7.html), [Jian Wang](https://dblp.org/pid/39/449-66.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html), [Zechao Li](https://dblp.org/pid/51/8693.html):

Exploring Effective Factors for Improving Visual In-Context Learning. [CoRRabs/2304.04748](https://dblp.org/db/journals/corr/corr2304.html#journals/corr/abs-2304-04748) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j11\]
[Yiqin Luo](https://dblp.org/pid/227/6695.html), Yanpeng Sun, [Liang Chang](https://dblp.org/pid/72/6746-3.html), [Tianlong Gu](https://dblp.org/pid/42/5786.html), [Chenzhong Bin](https://dblp.org/pid/210/0267.html), [Long Li](https://dblp.org/pid/56/4380-5.html):

Considering Fine-Grained and Coarse-Grained Information for Context-Aware Recommendations. [Comput. J.65(3)](https://dblp.org/db/journals/cj/cj65.html#journals/cj/LuoSCGBL22): 679-688 (2022)
- ![](https://dblp.org/img/n.png)

\[j10\]
[Lele Qu](https://dblp.org/pid/32/9864.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changan Wang](https://dblp.org/pid/228/8302.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianhong Yang](https://dblp.org/pid/117/7216.html), [Lili Zhang](https://dblp.org/pid/00/6528-5.html), Yanpeng Sun:

Enhanced Through-the-Wall Radar Imaging Based on Deep Layer Aggregation. [IEEE Geosci. Remote. Sens. Lett.19](https://dblp.org/db/journals/lgrs/lgrs19.html#journals/lgrs/QuWYZS22): 1-5 (2022)
- ![](https://dblp.org/img/n.png)

\[j9\]
[Zechao Li](https://dblp.org/pid/51/8693.html)![](https://dblp.org/img/orcid-mark.12x12.png), Yanpeng Sun![](https://dblp.org/img/orcid-mark.12x12.png), [Liyan Zhang](https://dblp.org/pid/54/4596-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jinhui Tang](https://dblp.org/pid/75/1030.html)![](https://dblp.org/img/orcid-mark.12x12.png):

CTNet: Context-Based Tandem Network for Semantic Segmentation. [IEEE Trans. Pattern Anal. Mach. Intell.44(12)](https://dblp.org/db/journals/pami/pami44.html#journals/pami/LiSZT22): 9904-9917 (2022)
- ![](https://dblp.org/img/n.png)

\[c7\]
Yanpeng Sun, [Qiang Chen](https://dblp.org/pid/62/2719-7.html), [Xiangyu He](https://dblp.org/pid/173/4661.html), [Jian Wang](https://dblp.org/pid/39/449-66.html), [Haocheng Feng](https://dblp.org/pid/151/7248.html), [Junyu Han](https://dblp.org/pid/62/10697.html), [Errui Ding](https://dblp.org/pid/180/5531.html), [Jian Cheng](https://dblp.org/pid/14/6145-1.html), [Zechao Li](https://dblp.org/pid/51/8693.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html):

Singular Value Fine-tuning: Few-shot Segmentation requires Few-parameters Fine-tuning. [NeurIPS2022](https://dblp.org/db/conf/nips/neurips2022.html#conf/nips/SunCH0FHD0L022)
- ![](https://dblp.org/img/n.png)

\[i4\]
Yanpeng Sun, [Qiang Chen](https://dblp.org/pid/62/2719-7.html), [Xiangyu He](https://dblp.org/pid/173/4661.html), [Jian Wang](https://dblp.org/pid/39/449-66.html), [Haocheng Feng](https://dblp.org/pid/151/7248.html), [Junyu Han](https://dblp.org/pid/62/10697.html), [Errui Ding](https://dblp.org/pid/180/5531.html), [Jian Cheng](https://dblp.org/pid/14/6145-1.html), [Zechao Li](https://dblp.org/pid/51/8693.html), [Jingdong Wang](https://dblp.org/pid/49/3441.html):

Singular Value Fine-tuning: Few-shot Segmentation requires Few-parameters Fine-tuning. [CoRRabs/2206.06122](https://dblp.org/db/journals/corr/corr2206.html#journals/corr/abs-2206-06122) (2022)
- ![](https://dblp.org/img/n.png)

\[i3\]
[Peng Xing](https://dblp.org/pid/221/2336.html), Yanpeng Sun, [Zechao Li](https://dblp.org/pid/51/8693.html):

Self-Supervised Guided Segmentation Framework for Unsupervised Anomaly Detection. [CoRRabs/2209.12440](https://dblp.org/db/journals/corr/corr2209.html#journals/corr/abs-2209-12440) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[c6\]
[Lele Qu](https://dblp.org/pid/32/9864.html), [Yutong Wang](https://dblp.org/pid/90/3631.html), [Tianhong Yang](https://dblp.org/pid/117/7216.html), [Lili Zhang](https://dblp.org/pid/00/6528-5.html), Yanpeng Sun:

WGAN-GP-Based Synthetic Radar Spectrogram Augmentation in Human Activity Recognition. [IGARSS2021](https://dblp.org/db/conf/igarss/igarss2021.html#conf/igarss/QuWYZS21): 2532-2535
- ![](https://dblp.org/img/n.png)

\[i2\]
[Zechao Li](https://dblp.org/pid/51/8693.html), Yanpeng Sun, [Jinhui Tang](https://dblp.org/pid/75/1030.html):

CTNet: Context-based Tandem Network for Semantic Segmentation. [CoRRabs/2104.09805](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-09805) (2021)
- ![](https://dblp.org/img/n.png)

\[i1\]
Yanpeng Sun, [Zechao Li](https://dblp.org/pid/51/8693.html):

SSA: Semantic Structure Aware Inference for Weakly Pixel-Wise Dense Predictions without Cost. [CoRRabs/2111.03392](https://dblp.org/db/journals/corr/corr2111.html#journals/corr/abs-2111-03392) (2021)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j8\]
Yanpeng Sun, [Li Chen](https://dblp.org/pid/181/2847.html), [Lele Qu](https://dblp.org/pid/32/9864.html):

Through-the-wall radar imaging algorithm for moving target under wall parameter uncertainties. [IET Image Process.13(11)](https://dblp.org/db/journals/iet-ipr/iet-ipr13.html#journals/iet-ipr/SunCQ19): 1903-1908 (2019)
- ![](https://dblp.org/img/n.png)

\[j7\]
[Wenping Sun](https://dblp.org/pid/223/8405.html), [Liang Chang](https://dblp.org/pid/72/6746-3.html), [Chenzhong Bin](https://dblp.org/pid/210/0267.html), [Tianlong Gu](https://dblp.org/pid/42/5786.html), Yanpeng Sun:

基于知识图谱和频繁序列挖掘的旅游路线推荐 (Travel Route Recommendation Based on Knowledge Graph and Frequent Sequence Mining). [计算机科学46(2)](https://dblp.org/db/journals/jsjkx/jsjkx46.html#journals/jsjkx/SunCBGS19): 56-61 (2019)
- ![](https://dblp.org/img/n.png)

\[j6\]
[Chenzhong Bin](https://dblp.org/pid/210/0267.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianlong Gu](https://dblp.org/pid/42/5786.html), Yanpeng Sun, [Liang Chang](https://dblp.org/pid/72/6746-3.html):

A personalized POI route recommendation system based on heterogeneous tourism data and sequential pattern mining. [Multim. Tools Appl.78(24)](https://dblp.org/db/journals/mta/mta78.html#journals/mta/BinGSC19): 35135-35156 (2019)
- ![](https://dblp.org/img/n.png)

\[j5\]
[Chenzhong Bin](https://dblp.org/pid/210/0267.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianlong Gu](https://dblp.org/pid/42/5786.html), Yanpeng Sun, [Liang Chang](https://dblp.org/pid/72/6746-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Sun](https://dblp.org/pid/02/2264.html):

A Travel Route Recommendation System Based on Smart Phones and IoT Environment. [Wirel. Commun. Mob. Comput.2019](https://dblp.org/db/journals/wicomm/wicomm2019.html#journals/wicomm/BinGSCS19): 7038259:1-7038259:16 (2019)
- ![](https://dblp.org/img/n.png)

\[c5\]
[Lele Qu](https://dblp.org/pid/32/9864.html), [Zhongli Fang](https://dblp.org/pid/253/3619.html), [Tianhong Yang](https://dblp.org/pid/117/7216.html), Yanpeng Sun, [Lili Zhang](https://dblp.org/pid/00/6528-5.html):

Sparse Recovery Method for Estimation of Wall Parameters in Through-the-Wall Radar. [IGARSS2019](https://dblp.org/db/conf/igarss/igarss2019.html#conf/igarss/QuFYSZ19): 3558-3561
- ![](https://dblp.org/img/n.png)

\[c4\]
[Guiming Zhu](https://dblp.org/pid/74/10734.html), [Chenzhong Bin](https://dblp.org/pid/210/0267.html), [Tianlong Gu](https://dblp.org/pid/42/5786.html), [Liang Chang](https://dblp.org/pid/72/6746-3.html), Yanpeng Sun, [Wei Chen](https://dblp.org/pid/181/2832-105.html), [Zhonghao Jia](https://dblp.org/pid/247/6264.html):

A Neural User Preference Modeling Framework for Recommendation Based on Knowledge Graph. [PRICAI (1)2019](https://dblp.org/db/conf/pricai/pricai2019-1.html#conf/pricai/ZhuBGCS0J19): 176-189
- 2018
- ![](https://dblp.org/img/n.png)

\[j4\]
Yanpeng Sun, [Shi Zhang](https://dblp.org/pid/84/4135.html), [Zhao Cui](https://dblp.org/pid/215/3035.html):

Group sparsity based imaging algorithm for TWRI under wall parameter uncertainties. [Trans. Inst. Meas. Control40(1)](https://dblp.org/db/journals/tinstmc/tinstmc40.html#journals/tinstmc/SunZC18): 251-260 (2018)
- ![](https://dblp.org/img/n.png)

\[c3\]
[Chenzhong Bin](https://dblp.org/pid/210/0267.html), [Tianlong Gu](https://dblp.org/pid/42/5786.html), Yanpeng Sun, [Liang Chang](https://dblp.org/pid/72/6746-3.html), [Wenping Sun](https://dblp.org/pid/223/8405.html), [Lei Sun](https://dblp.org/pid/02/2264.html):

Personalized POIs Travel Route Recommendation System Based on Tourism Big Data. [PRICAI2018](https://dblp.org/db/conf/pricai/pricai2018b.html#conf/pricai/BinGSCSS18): 290-299
- ![](https://dblp.org/img/n.png)

\[c2\]
Yanpeng Sun, [Tianlong Gu](https://dblp.org/pid/42/5786.html), [Chenzhong Bin](https://dblp.org/pid/210/0267.html), [Liang Chang](https://dblp.org/pid/72/6746-3.html), [Haili Kuang](https://dblp.org/pid/223/8097.html), [Zhaowei Huang](https://dblp.org/pid/79/9654.html), [Lei Sun](https://dblp.org/pid/02/2264.html):

A Multi-latent Semantics Representation Model for Mining Tourist Trajectory. [PRICAI (1)2018](https://dblp.org/db/conf/pricai/pricai2018a.html#conf/pricai/SunGBCKHS18): 463-476
- 2017
- ![](https://dblp.org/img/n.png)

\[c1\]
[Lele Qu](https://dblp.org/pid/32/9864.html), [Shimiao An](https://dblp.org/pid/221/8893.html), [Tianhong Yang](https://dblp.org/pid/117/7216.html), Yanpeng Sun:

Full polarimetric ground penetrating radar imaging using multiple measurement vectors model. [ICNC-FSKD2017](https://dblp.org/db/conf/icnc/icnc2017.html#conf/icnc/QuAYS17): 2662-2667
- 2016
- ![](https://dblp.org/img/n.png)

\[j3\]
Yanpeng Sun, [Lele Qu](https://dblp.org/pid/32/9864.html), [Shi Zhang](https://dblp.org/pid/84/4135.html), [Yuqing Yin](https://dblp.org/pid/166/9147.html):

MT-BCS-Based Two-Dimensional Diffraction Tomographic GPR Imaging Algorithm With Multiview-Multistatic Configuration. [IEEE Geosci. Remote. Sens. Lett.13(6)](https://dblp.org/db/journals/lgrs/lgrs13.html#journals/lgrs/SunQZY16): 831-835 (2016)
- 2015
- ![](https://dblp.org/img/n.png)

\[j2\]
[Lele Qu](https://dblp.org/pid/32/9864.html), [Yuqing Yin](https://dblp.org/pid/166/9147.html), Yanpeng Sun, [Lili Zhang](https://dblp.org/pid/00/6528-5.html):

Diffraction Tomographic Ground-Penetrating Radar Multibistatic Imaging Algorithm With Compressive Frequency Measurements. [IEEE Geosci. Remote. Sens. Lett.12(10)](https://dblp.org/db/journals/lgrs/lgrs12.html#journals/lgrs/QuYSZ15): 2011-2015 (2015)
- 2014
- ![](https://dblp.org/img/n.png)

\[j1\]
[Lele Qu](https://dblp.org/pid/32/9864.html), [Qiang Sun](https://dblp.org/pid/73/2066.html), [Tianhong Yang](https://dblp.org/pid/117/7216.html), [Lili Zhang](https://dblp.org/pid/00/6528-5.html), Yanpeng Sun:

Time-Delay Estimation for Ground Penetrating Radar Using ESPRIT With Improved Spatial Smoothing Technique. [IEEE Geosci. Remote. Sens. Lett.11(8)](https://dblp.org/db/journals/lgrs/lgrs11.html#journals/lgrs/QuSYZS14): 1315-1319 (2014)
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/143/0055.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Hao Ai](https://dblp.org/pid/286/5383.html)

[\[i10\]](https://dblp.org/pid/143/0055.html#i10)

[2](https://dblp.org/pid/143/0055.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Qi Yong H. Ai](https://dblp.org/pid/410/9263.html)

[\[i18\]](https://dblp.org/pid/143/0055.html#i18)

[3](https://dblp.org/pid/143/0055.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Shimiao An](https://dblp.org/pid/221/8893.html)

[\[c1\]](https://dblp.org/pid/143/0055.html#c1)

[4](https://dblp.org/pid/143/0055.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Xu Bai](https://dblp.org/pid/91/6242.html)

[\[i10\]](https://dblp.org/pid/143/0055.html#i10)

[5](https://dblp.org/pid/143/0055.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Chenzhong Bin](https://dblp.org/pid/210/0267.html)

[\[j11\]](https://dblp.org/pid/143/0055.html#j11) [\[j7\]](https://dblp.org/pid/143/0055.html#j7) [\[j6\]](https://dblp.org/pid/143/0055.html#j6) [\[j5\]](https://dblp.org/pid/143/0055.html#j5) [\[c4\]](https://dblp.org/pid/143/0055.html#c4) [\[c3\]](https://dblp.org/pid/143/0055.html#c3) [\[c2\]](https://dblp.org/pid/143/0055.html#c2)

[6](https://dblp.org/pid/143/0055.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Weihao Bo](https://dblp.org/pid/327/6215.html)

[\[i17\]](https://dblp.org/pid/143/0055.html#i17) [\[i16\]](https://dblp.org/pid/143/0055.html#i16) [\[i15\]](https://dblp.org/pid/143/0055.html#i15) [\[i14\]](https://dblp.org/pid/143/0055.html#i14)

[7](https://dblp.org/pid/143/0055.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Wenxiao Cai](https://dblp.org/pid/348/4892.html)

[\[i19\]](https://dblp.org/pid/143/0055.html#i19)

[8](https://dblp.org/pid/143/0055.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Liang Chang 0003](https://dblp.org/pid/72/6746-3.html)

[\[j11\]](https://dblp.org/pid/143/0055.html#j11) [\[j7\]](https://dblp.org/pid/143/0055.html#j7) [\[j6\]](https://dblp.org/pid/143/0055.html#j6) [\[j5\]](https://dblp.org/pid/143/0055.html#j5) [\[c4\]](https://dblp.org/pid/143/0055.html#c4) [\[c3\]](https://dblp.org/pid/143/0055.html#c3) [\[c2\]](https://dblp.org/pid/143/0055.html#c2)

[9](https://dblp.org/pid/143/0055.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Aotian Chen](https://dblp.org/pid/366/0538.html)

[\[c12\]](https://dblp.org/pid/143/0055.html#c12) [\[i22\]](https://dblp.org/pid/143/0055.html#i22) [\[i20\]](https://dblp.org/pid/143/0055.html#i20)

[10](https://dblp.org/pid/143/0055.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jiahui Chen](https://dblp.org/pid/122/5100.html)

[\[c11\]](https://dblp.org/pid/143/0055.html#c11) [\[i11\]](https://dblp.org/pid/143/0055.html#i11)

[11](https://dblp.org/pid/143/0055.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Kunbin Chen](https://dblp.org/pid/147/4644.html)

[\[i14\]](https://dblp.org/pid/143/0055.html#i14)

[12](https://dblp.org/pid/143/0055.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Li Chen](https://dblp.org/pid/181/2847.html)

[\[j8\]](https://dblp.org/pid/143/0055.html#j8)

[13](https://dblp.org/pid/143/0055.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Qiang Chen 0007](https://dblp.org/pid/62/2719-7.html)

[\[j15\]](https://dblp.org/pid/143/0055.html#j15) [\[c13\]](https://dblp.org/pid/143/0055.html#c13) [\[c11\]](https://dblp.org/pid/143/0055.html#c11) [\[i11\]](https://dblp.org/pid/143/0055.html#i11) [\[i9\]](https://dblp.org/pid/143/0055.html#i9) [\[i8\]](https://dblp.org/pid/143/0055.html#i8) [\[i7\]](https://dblp.org/pid/143/0055.html#i7) [\[c9\]](https://dblp.org/pid/143/0055.html#c9) [\[i5\]](https://dblp.org/pid/143/0055.html#i5) [\[c7\]](https://dblp.org/pid/143/0055.html#c7) [\[i4\]](https://dblp.org/pid/143/0055.html#i4)

[14](https://dblp.org/pid/143/0055.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Song Chen](https://dblp.org/pid/04/4291.html)

[\[i9\]](https://dblp.org/pid/143/0055.html#i9)

[15](https://dblp.org/pid/143/0055.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Wei Chen 0105](https://dblp.org/pid/181/2832-105.html)

[\[c4\]](https://dblp.org/pid/143/0055.html#c4)

[16](https://dblp.org/pid/143/0055.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jian Cheng 0001](https://dblp.org/pid/14/6145-1.html)

[\[c7\]](https://dblp.org/pid/143/0055.html#c7) [\[i4\]](https://dblp.org/pid/143/0055.html#i4)

[17](https://dblp.org/pid/143/0055.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Wenxuan Cheng](https://dblp.org/pid/370/2615.html)

[\[i19\]](https://dblp.org/pid/143/0055.html#i19)

[18](https://dblp.org/pid/143/0055.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Zhao Cui](https://dblp.org/pid/215/3035.html)

[\[j4\]](https://dblp.org/pid/143/0055.html#j4)

[19](https://dblp.org/pid/143/0055.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Ming Dai](https://dblp.org/pid/61/6981.html)

[\[i19\]](https://dblp.org/pid/143/0055.html#i19)

[20](https://dblp.org/pid/143/0055.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Errui Ding](https://dblp.org/pid/180/5531.html)

[\[c11\]](https://dblp.org/pid/143/0055.html#c11) [\[i11\]](https://dblp.org/pid/143/0055.html#i11) [\[i9\]](https://dblp.org/pid/143/0055.html#i9) [\[c7\]](https://dblp.org/pid/143/0055.html#c7) [\[i4\]](https://dblp.org/pid/143/0055.html#i4)

[21](https://dblp.org/pid/143/0055.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yuqing Ding](https://dblp.org/pid/236/6555.html)

[\[j12\]](https://dblp.org/pid/143/0055.html#j12)

[22](https://dblp.org/pid/143/0055.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jinhao Du](https://dblp.org/pid/312/4875.html)

[\[c9\]](https://dblp.org/pid/143/0055.html#c9)

[23](https://dblp.org/pid/143/0055.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Fan Duan](https://dblp.org/pid/357/8693.html)

[\[i16\]](https://dblp.org/pid/143/0055.html#i16)

[24](https://dblp.org/pid/143/0055.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yuxuan Fan](https://dblp.org/pid/227/4963.html)

[\[i18\]](https://dblp.org/pid/143/0055.html#i18) [\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[25](https://dblp.org/pid/143/0055.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Qizhi Fang](https://dblp.org/pid/97/1149.html)

[\[c10\]](https://dblp.org/pid/143/0055.html#c10)

[26](https://dblp.org/pid/143/0055.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Zhongli Fang](https://dblp.org/pid/253/3619.html)

[\[c5\]](https://dblp.org/pid/143/0055.html#c5)

[27](https://dblp.org/pid/143/0055.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Haocheng Feng](https://dblp.org/pid/151/7248.html)

[\[c7\]](https://dblp.org/pid/143/0055.html#c7) [\[i4\]](https://dblp.org/pid/143/0055.html#i4)

[28](https://dblp.org/pid/143/0055.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jindong Gu](https://dblp.org/pid/232/2128.html)

[\[c12\]](https://dblp.org/pid/143/0055.html#c12) [\[i22\]](https://dblp.org/pid/143/0055.html#i22)

[29](https://dblp.org/pid/143/0055.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Qinying Gu](https://dblp.org/pid/365/4635.html)

[\[i21\]](https://dblp.org/pid/143/0055.html#i21)

[30](https://dblp.org/pid/143/0055.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Tianlong Gu](https://dblp.org/pid/42/5786.html)

[\[j11\]](https://dblp.org/pid/143/0055.html#j11) [\[j7\]](https://dblp.org/pid/143/0055.html#j7) [\[j6\]](https://dblp.org/pid/143/0055.html#j6) [\[j5\]](https://dblp.org/pid/143/0055.html#j5) [\[c4\]](https://dblp.org/pid/143/0055.html#c4) [\[c3\]](https://dblp.org/pid/143/0055.html#c3) [\[c2\]](https://dblp.org/pid/143/0055.html#c2)

[31](https://dblp.org/pid/143/0055.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Kaixin Guo](https://dblp.org/pid/417/5244.html)

[\[i18\]](https://dblp.org/pid/143/0055.html#i18) [\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[32](https://dblp.org/pid/143/0055.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Junyu Han](https://dblp.org/pid/62/10697.html)

[\[c7\]](https://dblp.org/pid/143/0055.html#c7) [\[i4\]](https://dblp.org/pid/143/0055.html#i4)

[33](https://dblp.org/pid/143/0055.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jing Hao](https://dblp.org/pid/21/2724.html)

[\[i18\]](https://dblp.org/pid/143/0055.html#i18) [\[i13\]](https://dblp.org/pid/143/0055.html#i13) [\[i9\]](https://dblp.org/pid/143/0055.html#i9) [\[i6\]](https://dblp.org/pid/143/0055.html#i6)

[34](https://dblp.org/pid/143/0055.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Bin He](https://dblp.org/pid/78/4523.html)

[\[c9\]](https://dblp.org/pid/143/0055.html#c9)

[35](https://dblp.org/pid/143/0055.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Shengfeng He](https://dblp.org/pid/38/9555.html)

[\[j16\]](https://dblp.org/pid/143/0055.html#j16)

[36](https://dblp.org/pid/143/0055.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Wei He](https://dblp.org/pid/20/6417.html)

[\[i14\]](https://dblp.org/pid/143/0055.html#i14)

[37](https://dblp.org/pid/143/0055.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Xiangyu He](https://dblp.org/pid/173/4661.html)

[\[c7\]](https://dblp.org/pid/143/0055.html#c7) [\[i4\]](https://dblp.org/pid/143/0055.html#i4)

[38](https://dblp.org/pid/143/0055.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Anton van den Hengel](https://dblp.org/pid/v/AntonvandenHengel.html)

[\[c12\]](https://dblp.org/pid/143/0055.html#c12) [\[i22\]](https://dblp.org/pid/143/0055.html#i22) [\[i20\]](https://dblp.org/pid/143/0055.html#i20)

[39](https://dblp.org/pid/143/0055.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Qiyue Hu](https://dblp.org/pid/03/9972.html)

[\[j14\]](https://dblp.org/pid/143/0055.html#j14)

[40](https://dblp.org/pid/143/0055.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Renyuan Huang](https://dblp.org/pid/382/6720.html)

[\[i10\]](https://dblp.org/pid/143/0055.html#i10)

[41](https://dblp.org/pid/143/0055.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Zhaowei Huang](https://dblp.org/pid/79/9654.html)

[\[c2\]](https://dblp.org/pid/143/0055.html#c2)

[42](https://dblp.org/pid/143/0055.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Kuo Feng Hung](https://dblp.org/pid/367/4460.html)

[\[i18\]](https://dblp.org/pid/143/0055.html#i18) [\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[43](https://dblp.org/pid/143/0055.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Zhonghao Jia](https://dblp.org/pid/247/6264.html)

[\[c4\]](https://dblp.org/pid/143/0055.html#c4)

[44](https://dblp.org/pid/143/0055.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Piotr Koniusz](https://dblp.org/pid/25/8616.html)

[\[c12\]](https://dblp.org/pid/143/0055.html#c12) [\[i22\]](https://dblp.org/pid/143/0055.html#i22) [\[i20\]](https://dblp.org/pid/143/0055.html#i20) [\[i12\]](https://dblp.org/pid/143/0055.html#i12)

[45](https://dblp.org/pid/143/0055.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Haili Kuang](https://dblp.org/pid/223/8097.html)

[\[c2\]](https://dblp.org/pid/143/0055.html#c2)

[46](https://dblp.org/pid/143/0055.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Haifeng Le](https://dblp.org/pid/366/3250.html)

[\[c9\]](https://dblp.org/pid/143/0055.html#c9)

[47](https://dblp.org/pid/143/0055.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Long Li 0005](https://dblp.org/pid/56/4380-5.html)

[\[j11\]](https://dblp.org/pid/143/0055.html#j11)

[48](https://dblp.org/pid/143/0055.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Qiankun Li](https://dblp.org/pid/228/7339.html)

[\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[49](https://dblp.org/pid/143/0055.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Wei Li](https://dblp.org/pid/64/6025.html)

[\[i12\]](https://dblp.org/pid/143/0055.html#i12)

[50](https://dblp.org/pid/143/0055.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Xiaofan Li](https://dblp.org/pid/50/3937.html)

[\[i16\]](https://dblp.org/pid/143/0055.html#i16) [\[i15\]](https://dblp.org/pid/143/0055.html#i15) [\[i14\]](https://dblp.org/pid/143/0055.html#i14) [\[i12\]](https://dblp.org/pid/143/0055.html#i12) [\[i6\]](https://dblp.org/pid/143/0055.html#i6)

[51](https://dblp.org/pid/143/0055.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Zechao Li](https://dblp.org/pid/51/8693.html)

[\[j19\]](https://dblp.org/pid/143/0055.html#j19) [\[j18\]](https://dblp.org/pid/143/0055.html#j18) [\[j17\]](https://dblp.org/pid/143/0055.html#j17) [\[j16\]](https://dblp.org/pid/143/0055.html#j16) [\[j15\]](https://dblp.org/pid/143/0055.html#j15) [\[i21\]](https://dblp.org/pid/143/0055.html#i21) [\[i17\]](https://dblp.org/pid/143/0055.html#i17) [\[i14\]](https://dblp.org/pid/143/0055.html#i14) [\[i12\]](https://dblp.org/pid/143/0055.html#i12) [\[j13\]](https://dblp.org/pid/143/0055.html#j13) [\[c11\]](https://dblp.org/pid/143/0055.html#c11) [\[i11\]](https://dblp.org/pid/143/0055.html#i11) [\[i10\]](https://dblp.org/pid/143/0055.html#i10) [\[i8\]](https://dblp.org/pid/143/0055.html#i8) [\[i6\]](https://dblp.org/pid/143/0055.html#i6) [\[j12\]](https://dblp.org/pid/143/0055.html#j12) [\[i5\]](https://dblp.org/pid/143/0055.html#i5) [\[j9\]](https://dblp.org/pid/143/0055.html#j9) [\[c7\]](https://dblp.org/pid/143/0055.html#c7) [\[i4\]](https://dblp.org/pid/143/0055.html#i4) [\[i3\]](https://dblp.org/pid/143/0055.html#i3) [\[i2\]](https://dblp.org/pid/143/0055.html#i2) [\[i1\]](https://dblp.org/pid/143/0055.html#i1)

[52](https://dblp.org/pid/143/0055.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Dingkang Liang](https://dblp.org/pid/255/6274.html)

[\[i16\]](https://dblp.org/pid/143/0055.html#i16) [\[i15\]](https://dblp.org/pid/143/0055.html#i15)

[53](https://dblp.org/pid/143/0055.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yuci Liang](https://dblp.org/pid/394/6550.html)

[\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[54](https://dblp.org/pid/143/0055.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Lizhuo Lin](https://dblp.org/pid/412/5549.html)

[\[i18\]](https://dblp.org/pid/143/0055.html#i18) [\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[55](https://dblp.org/pid/143/0055.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jiang-jiang Liu](https://dblp.org/pid/409/9085.html)

[\[i19\]](https://dblp.org/pid/143/0055.html#i19)

[56](https://dblp.org/pid/143/0055.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jiangjiang Liu 0006](https://dblp.org/pid/344/2055.html)

[\[c13\]](https://dblp.org/pid/143/0055.html#c13) [\[i7\]](https://dblp.org/pid/143/0055.html#i7) [\[i6\]](https://dblp.org/pid/143/0055.html#i6)

[57](https://dblp.org/pid/143/0055.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yiqin Luo](https://dblp.org/pid/227/6695.html)

[\[j11\]](https://dblp.org/pid/143/0055.html#j11)

[58](https://dblp.org/pid/143/0055.html?view=joint&param=58 "show joint publications")

[Jinhai Miao](https://dblp.org/pid/360/5915.html)

[\[c8\]](https://dblp.org/pid/143/0055.html#c8)

[59](https://dblp.org/pid/143/0055.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yao Ni](https://dblp.org/pid/222/7928.html)

[\[c9\]](https://dblp.org/pid/143/0055.html#c9)

[60](https://dblp.org/pid/143/0055.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Delin Qu](https://dblp.org/pid/73/2731.html)

[\[i15\]](https://dblp.org/pid/143/0055.html#i15)

[61](https://dblp.org/pid/143/0055.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Lele Qu](https://dblp.org/pid/32/9864.html)

[\[j14\]](https://dblp.org/pid/143/0055.html#j14) [\[j10\]](https://dblp.org/pid/143/0055.html#j10) [\[c6\]](https://dblp.org/pid/143/0055.html#c6) [\[j8\]](https://dblp.org/pid/143/0055.html#j8) [\[c5\]](https://dblp.org/pid/143/0055.html#c5) [\[c1\]](https://dblp.org/pid/143/0055.html#c1) [\[j3\]](https://dblp.org/pid/143/0055.html#j3) [\[j2\]](https://dblp.org/pid/143/0055.html#j2) [\[j1\]](https://dblp.org/pid/143/0055.html#j1)

[62](https://dblp.org/pid/143/0055.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yansong Qu](https://dblp.org/pid/260/3675.html)

[\[i15\]](https://dblp.org/pid/143/0055.html#i15)

[63](https://dblp.org/pid/143/0055.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Nong Sang](https://dblp.org/pid/10/1545.html)

[\[i8\]](https://dblp.org/pid/143/0055.html#i8)

[64](https://dblp.org/pid/143/0055.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[LinLin Shen](https://dblp.org/pid/88/5607.html)

aka: Linlin Shen

[\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[65](https://dblp.org/pid/143/0055.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Lei Sun](https://dblp.org/pid/02/2264.html)

[\[j5\]](https://dblp.org/pid/143/0055.html#j5) [\[c3\]](https://dblp.org/pid/143/0055.html#c3) [\[c2\]](https://dblp.org/pid/143/0055.html#c2)

[66](https://dblp.org/pid/143/0055.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Qiang Sun](https://dblp.org/pid/73/2066.html)

[\[j1\]](https://dblp.org/pid/143/0055.html#j1)

[67](https://dblp.org/pid/143/0055.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Wenping Sun](https://dblp.org/pid/223/8405.html)

[\[j7\]](https://dblp.org/pid/143/0055.html#j7) [\[c3\]](https://dblp.org/pid/143/0055.html#c3)

[68](https://dblp.org/pid/143/0055.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Xiao Tan 0001](https://dblp.org/pid/116/7143-1.html)

[\[i14\]](https://dblp.org/pid/143/0055.html#i14)

[69](https://dblp.org/pid/143/0055.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Hao Tang](https://dblp.org/pid/07/5751.html)

[\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[70](https://dblp.org/pid/143/0055.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Hao Tang 0005](https://dblp.org/pid/07/5751-5.html)

[\[i18\]](https://dblp.org/pid/143/0055.html#i18)

[71](https://dblp.org/pid/143/0055.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Hao Tang 0007](https://dblp.org/pid/07/5751-7.html)

[\[j18\]](https://dblp.org/pid/143/0055.html#j18) [\[j16\]](https://dblp.org/pid/143/0055.html#j16)

[72](https://dblp.org/pid/143/0055.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jinhui Tang 0001](https://dblp.org/pid/75/1030.html)

[\[j19\]](https://dblp.org/pid/143/0055.html#j19) [\[j9\]](https://dblp.org/pid/143/0055.html#j9) [\[i2\]](https://dblp.org/pid/143/0055.html#i2)

[73](https://dblp.org/pid/143/0055.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Wei Tang 0011](https://dblp.org/pid/58/1874-11.html)

[\[i21\]](https://dblp.org/pid/143/0055.html#i21) [\[i20\]](https://dblp.org/pid/143/0055.html#i20) [\[i12\]](https://dblp.org/pid/143/0055.html#i12)

[74](https://dblp.org/pid/143/0055.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[James Kit-Hon Tsoi](https://dblp.org/pid/423/6078.html)

[\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[75](https://dblp.org/pid/143/0055.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Changan Wang](https://dblp.org/pid/228/8302.html)

[\[j10\]](https://dblp.org/pid/143/0055.html#j10)

[76](https://dblp.org/pid/143/0055.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Haofan Wang](https://dblp.org/pid/234/7841.html)

[\[i10\]](https://dblp.org/pid/143/0055.html#i10)

[77](https://dblp.org/pid/143/0055.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jian Wang 0066](https://dblp.org/pid/39/449-66.html)

[\[j15\]](https://dblp.org/pid/143/0055.html#j15) [\[c9\]](https://dblp.org/pid/143/0055.html#c9) [\[i5\]](https://dblp.org/pid/143/0055.html#i5) [\[c7\]](https://dblp.org/pid/143/0055.html#c7) [\[i4\]](https://dblp.org/pid/143/0055.html#i4)

[78](https://dblp.org/pid/143/0055.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jingdong Wang 0001](https://dblp.org/pid/49/3441.html)

[\[j15\]](https://dblp.org/pid/143/0055.html#j15) [\[c13\]](https://dblp.org/pid/143/0055.html#c13) [\[i14\]](https://dblp.org/pid/143/0055.html#i14) [\[c11\]](https://dblp.org/pid/143/0055.html#c11) [\[i11\]](https://dblp.org/pid/143/0055.html#i11) [\[i9\]](https://dblp.org/pid/143/0055.html#i9) [\[i8\]](https://dblp.org/pid/143/0055.html#i8) [\[i7\]](https://dblp.org/pid/143/0055.html#i7) [\[i6\]](https://dblp.org/pid/143/0055.html#i6) [\[c9\]](https://dblp.org/pid/143/0055.html#c9) [\[i5\]](https://dblp.org/pid/143/0055.html#i5) [\[c7\]](https://dblp.org/pid/143/0055.html#c7) [\[i4\]](https://dblp.org/pid/143/0055.html#i4)

[79](https://dblp.org/pid/143/0055.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Ning Wang 0020](https://dblp.org/pid/46/2005-20.html)

[\[j19\]](https://dblp.org/pid/143/0055.html#j19)

[80](https://dblp.org/pid/143/0055.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Qixun Wang 0001](https://dblp.org/pid/256/6758-1.html)

[\[i10\]](https://dblp.org/pid/143/0055.html#i10)

[81](https://dblp.org/pid/143/0055.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yu Wang](https://dblp.org/pid/02/5889.html)

[\[c13\]](https://dblp.org/pid/143/0055.html#c13) [\[i17\]](https://dblp.org/pid/143/0055.html#i17) [\[i7\]](https://dblp.org/pid/143/0055.html#i7)

[82](https://dblp.org/pid/143/0055.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[YuAn Wang](https://dblp.org/pid/423/6899.html)

[\[i16\]](https://dblp.org/pid/143/0055.html#i16)

[83](https://dblp.org/pid/143/0055.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yutong Wang](https://dblp.org/pid/90/3631.html)

[\[c6\]](https://dblp.org/pid/143/0055.html#c6)

[84](https://dblp.org/pid/143/0055.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Lun M. Wong](https://dblp.org/pid/417/5514.html)

[\[i18\]](https://dblp.org/pid/143/0055.html#i18)

[85](https://dblp.org/pid/143/0055.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Chenming Wu](https://dblp.org/pid/190/5879.html)

[\[i16\]](https://dblp.org/pid/143/0055.html#i16) [\[i15\]](https://dblp.org/pid/143/0055.html#i15)

[86](https://dblp.org/pid/143/0055.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jingjing Wu](https://dblp.org/pid/27/2384.html)

[\[i14\]](https://dblp.org/pid/143/0055.html#i14)

[87](https://dblp.org/pid/143/0055.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Qunyi Xie](https://dblp.org/pid/172/9555.html)

[\[i14\]](https://dblp.org/pid/143/0055.html#i14)

[88](https://dblp.org/pid/143/0055.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Peng Xing](https://dblp.org/pid/221/2336.html)

[\[j19\]](https://dblp.org/pid/143/0055.html#j19) [\[j13\]](https://dblp.org/pid/143/0055.html#j13) [\[i10\]](https://dblp.org/pid/143/0055.html#i10) [\[i3\]](https://dblp.org/pid/143/0055.html#i3)

[89](https://dblp.org/pid/143/0055.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yuan Xue 0002](https://dblp.org/pid/41/5526-2.html)

[\[c12\]](https://dblp.org/pid/143/0055.html#c12) [\[i22\]](https://dblp.org/pid/143/0055.html#i22) [\[i20\]](https://dblp.org/pid/143/0055.html#i20)

[90](https://dblp.org/pid/143/0055.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jinrong Yang](https://dblp.org/pid/286/5463.html)

[\[i18\]](https://dblp.org/pid/143/0055.html#i18)

[91](https://dblp.org/pid/143/0055.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Sen Yang](https://dblp.org/pid/90/4655.html)

[\[i19\]](https://dblp.org/pid/143/0055.html#i19)

[92](https://dblp.org/pid/143/0055.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Tianhong Yang](https://dblp.org/pid/117/7216.html)

[\[j14\]](https://dblp.org/pid/143/0055.html#j14) [\[j10\]](https://dblp.org/pid/143/0055.html#j10) [\[c6\]](https://dblp.org/pid/143/0055.html#c6) [\[c5\]](https://dblp.org/pid/143/0055.html#c5) [\[c1\]](https://dblp.org/pid/143/0055.html#c1) [\[j1\]](https://dblp.org/pid/143/0055.html#j1)

[93](https://dblp.org/pid/143/0055.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[i19\]](https://dblp.org/pid/143/0055.html#i19)

[94](https://dblp.org/pid/143/0055.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yanqi Yang](https://dblp.org/pid/252/1899.html)

[\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[95](https://dblp.org/pid/143/0055.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Kun Yao](https://dblp.org/pid/03/6550.html)

[\[i9\]](https://dblp.org/pid/143/0055.html#i9)

[96](https://dblp.org/pid/143/0055.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Zanting Ye](https://dblp.org/pid/356/2713.html)

[\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[97](https://dblp.org/pid/143/0055.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yuqing Yin](https://dblp.org/pid/166/9147.html)

[\[j3\]](https://dblp.org/pid/143/0055.html#j3) [\[j2\]](https://dblp.org/pid/143/0055.html#j2)

[98](https://dblp.org/pid/143/0055.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Haibao Yu](https://dblp.org/pid/246/4643.html)

[\[i15\]](https://dblp.org/pid/143/0055.html#i15)

[99](https://dblp.org/pid/143/0055.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Dan Zeng 0001](https://dblp.org/pid/06/6575-1.html)

[\[j13\]](https://dblp.org/pid/143/0055.html#j13)

[100](https://dblp.org/pid/143/0055.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Gang Zhang](https://dblp.org/pid/37/4096.html)

[\[c13\]](https://dblp.org/pid/143/0055.html#c13) [\[c11\]](https://dblp.org/pid/143/0055.html#c11) [\[i11\]](https://dblp.org/pid/143/0055.html#i11) [\[i9\]](https://dblp.org/pid/143/0055.html#i9) [\[i8\]](https://dblp.org/pid/143/0055.html#i8) [\[i7\]](https://dblp.org/pid/143/0055.html#i7) [\[i6\]](https://dblp.org/pid/143/0055.html#i6)

[101](https://dblp.org/pid/143/0055.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Haiqi Zhang](https://dblp.org/pid/10/6011.html)

[\[j18\]](https://dblp.org/pid/143/0055.html#j18) [\[j16\]](https://dblp.org/pid/143/0055.html#j16)

[102](https://dblp.org/pid/143/0055.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Huaxin Zhang](https://dblp.org/pid/72/1833.html)

[\[i8\]](https://dblp.org/pid/143/0055.html#i8)

[103](https://dblp.org/pid/143/0055.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Lili Zhang](https://dblp.org/pid/00/6528.html)

[\[j14\]](https://dblp.org/pid/143/0055.html#j14)

[104](https://dblp.org/pid/143/0055.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Lili Zhang 0005](https://dblp.org/pid/00/6528-5.html)

[\[j10\]](https://dblp.org/pid/143/0055.html#j10) [\[c6\]](https://dblp.org/pid/143/0055.html#c6) [\[c5\]](https://dblp.org/pid/143/0055.html#c5) [\[j2\]](https://dblp.org/pid/143/0055.html#j2) [\[j1\]](https://dblp.org/pid/143/0055.html#j1)

[105](https://dblp.org/pid/143/0055.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Liyan Zhang 0001](https://dblp.org/pid/54/4596-1.html)

[\[j9\]](https://dblp.org/pid/143/0055.html#j9)

[106](https://dblp.org/pid/143/0055.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Shan Zhang 0002](https://dblp.org/pid/14/6026-2.html)

[\[c12\]](https://dblp.org/pid/143/0055.html#c12) [\[i22\]](https://dblp.org/pid/143/0055.html#i22) [\[i20\]](https://dblp.org/pid/143/0055.html#i20) [\[i14\]](https://dblp.org/pid/143/0055.html#i14) [\[i12\]](https://dblp.org/pid/143/0055.html#i12) [\[c11\]](https://dblp.org/pid/143/0055.html#c11) [\[i11\]](https://dblp.org/pid/143/0055.html#i11) [\[c9\]](https://dblp.org/pid/143/0055.html#c9)

[107](https://dblp.org/pid/143/0055.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Shi Zhang](https://dblp.org/pid/84/4135.html)

[\[j4\]](https://dblp.org/pid/143/0055.html#j4) [\[j3\]](https://dblp.org/pid/143/0055.html#j3)

[108](https://dblp.org/pid/143/0055.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Xinyu Zhang](https://dblp.org/pid/58/4582.html)

[\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[109](https://dblp.org/pid/143/0055.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Xinyu Zhang 0017](https://dblp.org/pid/58/4582-17.html)

[\[i17\]](https://dblp.org/pid/143/0055.html#i17) [\[c11\]](https://dblp.org/pid/143/0055.html#c11) [\[i11\]](https://dblp.org/pid/143/0055.html#i11) [\[i8\]](https://dblp.org/pid/143/0055.html#i8)

[110](https://dblp.org/pid/143/0055.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yumeng Zhang](https://dblp.org/pid/26/4355.html)

[\[i16\]](https://dblp.org/pid/143/0055.html#i16)

[111](https://dblp.org/pid/143/0055.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Chenguang Zhao](https://dblp.org/pid/67/4612.html)

[\[c10\]](https://dblp.org/pid/143/0055.html#c10)

[112](https://dblp.org/pid/143/0055.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Na Zhao 0004](https://dblp.org/pid/35/3393-4.html)

[\[i14\]](https://dblp.org/pid/143/0055.html#i14) [\[i12\]](https://dblp.org/pid/143/0055.html#i12)

[113](https://dblp.org/pid/143/0055.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yuxiang Zhao](https://dblp.org/pid/181/2467.html)

[\[i9\]](https://dblp.org/pid/143/0055.html#i9) [\[i6\]](https://dblp.org/pid/143/0055.html#i6)

[114](https://dblp.org/pid/143/0055.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Yi-Yu Zheng](https://dblp.org/pid/397/4097.html)

[\[c12\]](https://dblp.org/pid/143/0055.html#c12) [\[i22\]](https://dblp.org/pid/143/0055.html#i22)

[115](https://dblp.org/pid/143/0055.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Jiaming Zhou](https://dblp.org/pid/250/0527.html)

[\[i15\]](https://dblp.org/pid/143/0055.html#i15)

[116](https://dblp.org/pid/143/0055.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Wenkai Zhou](https://dblp.org/pid/228/1980.html)

[\[i13\]](https://dblp.org/pid/143/0055.html#i13)

[117](https://dblp.org/pid/143/0055.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Guiming Zhu](https://dblp.org/pid/74/10734.html)

[\[c4\]](https://dblp.org/pid/143/0055.html#c4)

[118](https://dblp.org/pid/143/0055.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Ke Zhu](https://dblp.org/pid/32/4014.html)

[\[c13\]](https://dblp.org/pid/143/0055.html#c13) [\[i7\]](https://dblp.org/pid/143/0055.html#i7) [\[i6\]](https://dblp.org/pid/143/0055.html#i6)

[119](https://dblp.org/pid/143/0055.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/143/0055.html?view=group&param=1)

[Kai Zou](https://dblp.org/pid/135/5092.html)

[\[c12\]](https://dblp.org/pid/143/0055.html#c12) [\[i22\]](https://dblp.org/pid/143/0055.html#i22) [\[i20\]](https://dblp.org/pid/143/0055.html#i20)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/143/0055.html#) [\[–\]](https://dblp.org/pid/143/0055.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/143/0055.html#) [\[–\]](https://dblp.org/pid/143/0055.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/143/0055.html#) [\[–\]](https://dblp.org/pid/143/0055.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/143/0055.html#) [\[–\]](https://dblp.org/pid/143/0055.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/143/0055.html#) [\[–\]](https://dblp.org/pid/143/0055.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)