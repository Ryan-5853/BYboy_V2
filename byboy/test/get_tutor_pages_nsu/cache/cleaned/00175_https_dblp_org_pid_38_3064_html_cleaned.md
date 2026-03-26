> 抓取来源：https://dblp.org/pid/38/3064.html

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

- [Richard Li Xu](https://dblp.org/pid/388/1885.html)
- [Richard Xu-Rong](https://dblp.org/pid/174/9468.html)

🛈 Please note that only 69% of the items listed on this page have a DOI stored with their dblp record. Therefore, DOI-based queries can only provide partial results.

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Richard+Y.+D.+Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F38%2F3064%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Richard+Y.+D.+Xu+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F38%2F3064%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Richard+Y.+D.+Xu+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F38%2F3064%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Richard+Y.+D.+Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F38%2F3064%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Richard+Y.+D.+Xu+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F38%2F3064%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Richard+Y.+D.+Xu%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F38%2F3064%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Richard+Y.+D.+Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F38%2F3064%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F38%2F3064%3E+%7D+.%0A%0A%7D)

_showing all151 records_

20022025202002: 12003: 22005: 72006: 32007: 32007: 32008: 32009: 32009: 32010: 42010: 42011: 32012: 12013: 52013: 52014: 22015: 92015: 92015: 92016: 72016: 72017: 82017: 82018: 112018: 112018: 112019: 122019: 122019: 122020: 202020: 202020: 202021: 162021: 162021: 162022: 172022: 172022: 172023: 82023: 82023: 82024: 22025: 42025: 4

**refine by search term**

![](https://dblp.org/img/clear-mark.medium.16x16.png)![filter active](https://dblp.org/img/filter-mark.12x12.png)

**refine by type**

- [ ] Journal Articles(only)
- [ ] Conference and Workshop Papers(only)
- [ ] Parts in Books or Collections(only)
- [ ] Informal and Other Publications(only)

- select all \| deselect all

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by coauthor**

- ![](https://dblp.org/img/add-mark.12x12.png)Jesse S. Jin (15)
- ![](https://dblp.org/img/add-mark.12x12.png)Shuai Jiang (15)
- ![](https://dblp.org/img/add-mark.12x12.png)Massimo Piccardi (12)
- ![](https://dblp.org/img/add-mark.12x12.png)Wei Huang 0034 (11)
- ![](https://dblp.org/img/add-mark.12x12.png)Ziyue Zhang (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Congzhentao Huang (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Xiangfeng Luo (9)
- ![](https://dblp.org/img/add-mark.12x12.png)Xuhui Fan 0001 (9)
- ![](https://dblp.org/img/add-mark.12x12.png)Jian (Andrew) Zhang (8)
- ![](https://dblp.org/img/add-mark.12x12.png)Junyu Xuan (7)

- _206 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)0000-0003-2080-4762 (92)
- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (59)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (34)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Pattern Recognit. Lett. (7)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Neural Networks Learn. Syst. (5)
- ![](https://dblp.org/img/add-mark.12x12.png)AAAI (5)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Knowl. Data Eng. (4)
- ![](https://dblp.org/img/add-mark.12x12.png)ICIP (4)
- ![](https://dblp.org/img/add-mark.12x12.png)PMLR (4)
- ![](https://dblp.org/img/add-mark.12x12.png)VIP (3)
- ![](https://dblp.org/img/add-mark.12x12.png)ICPR (3)
- ![](https://dblp.org/img/add-mark.12x12.png)ACML (3)

- _67 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (85)
- ![](https://dblp.org/img/add-mark.12x12.png)open (63)
- ![](https://dblp.org/img/add-mark.12x12.png)unavailable (3)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[j49\]
[Haotian Li](https://dblp.org/pid/135/9708.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bin Yu](https://dblp.org/pid/27/116.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuliang Wei](https://dblp.org/pid/173/9369.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kai Wang](https://dblp.org/pid/78/2022-14.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Bailing Wang](https://dblp.org/pid/31/7938.html)![](https://dblp.org/img/orcid-mark.12x12.png):

KERMIT: Knowledge graph completion of enhanced relation modeling with inverse transformation. [Knowl. Based Syst.324](https://dblp.org/db/journals/kbs/kbs324.html#journals/kbs/LiYWWXW25): 113500 (2025)
- ![](https://dblp.org/img/n.png)

\[c67\]
[Shuai Niu](https://dblp.org/pid/31/5390.html), [Jing Ma](https://dblp.org/pid/96/6129-4.html), [Hongzhan Lin](https://dblp.org/pid/292/1751-1.html), [Liang Bai](https://dblp.org/pid/91/6504-1.html), [Zhihua Wang](https://dblp.org/pid/66/6802-8.html), [Wei Bi](https://dblp.org/pid/38/1163.html), Richard Yi Da Xu, [Guo Li](https://dblp.org/pid/35/1964-2.html), [Xian Yang](https://dblp.org/pid/25/10624-1.html):

ProMedTS: A Self-Supervised, Prompt-Guided Multimodal Approach for Integrating Medical Text and Time Series. [ACL (Findings)2025](https://dblp.org/db/conf/acl/acl2025f.html#conf/acl/Niu00B0BX0025): 5915-5928
- ![](https://dblp.org/img/n.png)

\[c66\]
[Shuai Niu](https://dblp.org/pid/31/5390.html), [Jing Ma](https://dblp.org/pid/96/6129-4.html), [Hongzhan Lin](https://dblp.org/pid/292/1751-1.html), [Liang Bai](https://dblp.org/pid/91/6504-1.html), [Zhihua Wang](https://dblp.org/pid/66/6802-8.html), Richard Yi Da Xu, [Yunya Song](https://dblp.org/pid/165/3067.html), [Xian Yang](https://dblp.org/pid/25/10624-1.html):

Knowledge-Augmented Multimodal Clinical Rationale Generation for Disease Diagnosis with Small Language Models. [ACL (1)2025](https://dblp.org/db/conf/acl/acl2025-1.html#conf/acl/Niu00B0XS025): 11011-11024
- ![](https://dblp.org/img/n.png)

\[c65\]
[Miaoge Li](https://dblp.org/pid/330/3622.html), [Jingcai Guo](https://dblp.org/pid/192/7270.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Dongsheng Wang](https://dblp.org/pid/21/841.html), [Xiaofeng Cao](https://dblp.org/pid/117/3982-2.html), [Zhijie Rao](https://dblp.org/pid/351/0660.html), [Song Guo](https://dblp.org/pid/01/267-1.html):

TsCA: On the Semantic Consistency Alignment via Conditional Transport for Compositional Zero-Shot Learning. [IJCAI2025](https://dblp.org/db/conf/ijcai/ijcai2025.html#conf/ijcai/LiGXWCR025): 5607-5615
- 2024
- ![](https://dblp.org/img/n.png)

\[i34\]
[Miaoge Li](https://dblp.org/pid/330/3622.html), [Jingcai Guo](https://dblp.org/pid/192/7270.html), Richard Yi Da Xu, [Dongsheng Wang](https://dblp.org/pid/21/841.html), [Xiaofeng Cao](https://dblp.org/pid/117/3982-2.html), [Song Guo](https://dblp.org/pid/01/267-1.html):

TsCA: On the Semantic Consistency Alignment via Conditional Transport for Compositional Zero-Shot Learning. [CoRRabs/2408.08703](https://dblp.org/db/journals/corr/corr2408.html#journals/corr/abs-2408-08703) (2024)
- ![](https://dblp.org/img/n.png)

\[i33\]
[Haotian Li](https://dblp.org/pid/135/9708.html), [Rui Zhang](https://dblp.org/pid/60/2536-50.html), [Lingzhi Wang](https://dblp.org/pid/66/8430.html), [Bin Yu](https://dblp.org/pid/27/116.html), [Youwei Wang](https://dblp.org/pid/73/4416.html), [Yuliang Wei](https://dblp.org/pid/173/9369.html), [Kai Wang](https://dblp.org/pid/78/2022-14.html), Richard Yi Da Xu, [Bailing Wang](https://dblp.org/pid/31/7938.html):

Deep Sparse Latent Feature Models for Knowledge Graph Completion. [CoRRabs/2411.15694](https://dblp.org/db/journals/corr/corr2411.html#journals/corr/abs-2411-15694) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j48\]
[Can Zhang](https://dblp.org/pid/35/1714.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xu Zhang](https://dblp.org/pid/98/5660.html), [Wanming Huang](https://dblp.org/pid/92/7710.html):

Capture and control content discrepancies via normalised flow transfer. [Pattern Recognit. Lett.165](https://dblp.org/db/journals/prl/prl165.html#journals/prl/ZhangXZH23): 161-167 (2023)
- ![](https://dblp.org/img/n.png)

\[j47\]
[Yi Huang](https://dblp.org/pid/15/6040-23.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ying Li](https://dblp.org/pid/22/1805-39.html), [Guillaume Jourjon](https://dblp.org/pid/51/2666.html), [Suranga Seneviratne](https://dblp.org/pid/126/2555.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kanchana Thilakarathna](https://dblp.org/pid/92/10700.html), [Adriel Cheng](https://dblp.org/pid/24/6615.html), [Darren Webb](https://dblp.org/pid/36/4297.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Calibrated reconstruction based adversarial autoencoder model for novelty detection. [Pattern Recognit. Lett.169](https://dblp.org/db/journals/prl/prl169.html#journals/prl/HuangLJSTCWX23): 50-57 (2023)
- ![](https://dblp.org/img/n.png)

\[j46\]
[Wei Huang](https://dblp.org/pid/81/6685-34.html), [Chunrui Liu](https://dblp.org/pid/266/7209.html), [Yilan Chen](https://dblp.org/pid/167/6638-2.html), Richard Yi Da Xu, [Miao Zhang](https://dblp.org/pid/60/7041-22.html), [Tsui-Wei Weng](https://dblp.org/pid/177/9197.html):

Analyzing Deep PAC-Bayesian Learning with Neural Tangent Kernel: Convergence, Analytic Generalization Bound, and Efficient Hyperparameter Selection. [Trans. Mach. Learn. Res.2023](https://dblp.org/db/journals/tmlr/tmlr2023.html#journals/tmlr/0034L0XZW23) (2023)
- ![](https://dblp.org/img/n.png)

\[c64\]
[Sen Pei](https://dblp.org/pid/129/1503.html), [Jiaxi Sun](https://dblp.org/pid/289/6842.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Shiming Xiang](https://dblp.org/pid/81/6575.html), [Gaofeng Meng](https://dblp.org/pid/78/6915.html):

Domain Decorrelation with Potential Energy Ranking. [AAAI2023](https://dblp.org/db/conf/aaai/aaai2023.html#conf/aaai/PeiSXXM23): 2020-2028
- ![](https://dblp.org/img/n.png)

\[c63\]
[Shengchao Zhou](https://dblp.org/pid/194/4326.html), [Gaofeng Meng](https://dblp.org/pid/78/6915.html), [Zhaoxiang Zhang](https://dblp.org/pid/55/2285-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Shiming Xiang](https://dblp.org/pid/81/6575.html):

Robust Feature Rectification of Pretrained Vision Models for Object Recognition. [AAAI2023](https://dblp.org/db/conf/aaai/aaai2023.html#conf/aaai/ZhouMZXX23): 3796-3804
- ![](https://dblp.org/img/n.png)

\[c62\]
[Qimeng Cao](https://dblp.org/pid/356/9490.html), [Qing Yin](https://dblp.org/pid/55/10035.html), [Yunya Song](https://dblp.org/pid/165/3067.html), [Zhihua Wang](https://dblp.org/pid/66/6802-8.html), [Yujun Chen](https://dblp.org/pid/57/6294.html), Richard Yi Da Xu, [Xian Yang](https://dblp.org/pid/25/10624-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

RTANet: Recommendation Target-Aware Network Embedding. [ICWSM2023](https://dblp.org/db/conf/icwsm/icwsm2023.html#conf/icwsm/CaoYS0CX023): 84-94
- ![](https://dblp.org/img/n.png)

\[i32\]
[Hong-Bo Xie](https://dblp.org/pid/54/7839.html), [Caoyuan Li](https://dblp.org/pid/157/8323.html), [Shuliang Wang](https://dblp.org/pid/36/4791-1.html), Richard Yi Da Xu, [Kerrie L. Mengersen](https://dblp.org/pid/64/3136.html):

A variational autoencoder-based nonnegative matrix factorisation model for deep dictionary learning. [CoRRabs/2301.07272](https://dblp.org/db/journals/corr/corr2301.html#journals/corr/abs-2301-07272) (2023)
- ![](https://dblp.org/img/n.png)

\[i31\]
[Haotian Li](https://dblp.org/pid/135/9708.html), [Lingzhi Wang](https://dblp.org/pid/66/8430.html), [Yuliang Wei](https://dblp.org/pid/173/9369.html), Richard Yi Da Xu, [Bailing Wang](https://dblp.org/pid/31/7938.html):

KERMIT: Knowledge Graph Completion of Enhanced Relation Modeling with Inverse Transformation. [CoRRabs/2309.14770](https://dblp.org/db/journals/corr/corr2309.html#journals/corr/abs-2309-14770) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j45\]
[Helen Huiru Lou](https://dblp.org/pid/421/7522.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Fang](https://dblp.org/pid/29/3425.html), [Huilong Gai](https://dblp.org/pid/321/7744.html), Richard Xu, [Sidney Lin](https://dblp.org/pid/321/7255.html):

A novel zone-based machine learning approach for the prediction of the performance of industrial flares. [Comput. Chem. Eng.162](https://dblp.org/db/journals/cce/cce162.html#journals/cce/LouFGXL22): 107795 (2022)
- ![](https://dblp.org/img/n.png)

\[j44\]
[Ying Li](https://dblp.org/pid/22/1805-39.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Huang](https://dblp.org/pid/15/6040-23.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Suranga Seneviratne](https://dblp.org/pid/126/2555.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kanchana Thilakarathna](https://dblp.org/pid/92/10700.html), [Adriel Cheng](https://dblp.org/pid/24/6615.html), [Guillaume Jourjon](https://dblp.org/pid/51/2666.html), [Darren Webb](https://dblp.org/pid/36/4297.html), [David B. Smith](https://dblp.org/pid/47/3219.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

From traffic classes to content: A hierarchical approach for encrypted traffic classification. [Comput. Networks212](https://dblp.org/db/journals/cn/cn212.html#journals/cn/LiHSTCJWSX22): 109017 (2022)
- ![](https://dblp.org/img/n.png)

\[j43\]
[Chenghao Zhang](https://dblp.org/pid/186/0078-3.html), [Gaofeng Meng](https://dblp.org/pid/78/6915.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Shiming Xiang](https://dblp.org/pid/81/6575.html), [Chunhong Pan](https://dblp.org/pid/26/3810.html):

Learning adversarial point-wise domain alignment for stereo matching. [Neurocomputing491](https://dblp.org/db/journals/ijon/ijon491.html#journals/ijon/ZhangMXXP22): 564-574 (2022)
- ![](https://dblp.org/img/n.png)

\[j42\]
[Zhenguo Shi](https://dblp.org/pid/89/4115.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qingqing Cheng](https://dblp.org/pid/58/7703.html)![](https://dblp.org/img/orcid-mark.12x12.png), [J. Andrew Zhang](https://dblp.org/pid/07/314-a.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yida Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Environment-Robust WiFi-Based Human Activity Recognition Using Enhanced CSI and Deep Learning. [IEEE Internet Things J.9(24)](https://dblp.org/db/journals/iotj/iotj9.html#journals/iotj/ShiCZX22): 24643-24654 (2022)
- ![](https://dblp.org/img/n.png)

\[j41\]
[Steven Y. K. Wong](https://dblp.org/pid/260/0739.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jennifer S. K. Chan](https://dblp.org/pid/09/4557.html), [Lamiae Azizi](https://dblp.org/pid/155/3944.html), Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Time-varying neural network for stock return prediction. [Intell. Syst. Account. Finance Manag.29(1)](https://dblp.org/db/journals/isafm/isafm29.html#journals/isafm/WongCAX22): 3-18 (2022)
- ![](https://dblp.org/img/n.png)

\[j40\]
[Xian Yang](https://dblp.org/pid/25/10624-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shuo Wang](https://dblp.org/pid/63/1591-11.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuting Xing](https://dblp.org/pid/212/0136.html), [Ling Li](https://dblp.org/pid/92/5001-10.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Karl J. Friston](https://dblp.org/pid/92/848.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yike Guo](https://dblp.org/pid/g/YikeGuo.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Bayesian data assimilation for estimating instantaneous reproduction numbers during epidemics: Applications to COVID-19. [PLoS Comput. Biol.18(2)](https://dblp.org/db/journals/ploscb/ploscb18.html#journals/ploscb/YangWXLXFG22) (2022)
- ![](https://dblp.org/img/n.png)

\[j39\]
[Yi Huang](https://dblp.org/pid/15/6040-23.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ying Li](https://dblp.org/pid/22/1805-39.html), [Timothy Heyes](https://dblp.org/pid/323/2133.html), [Guillaume Jourjon](https://dblp.org/pid/51/2666.html), [Adriel Cheng](https://dblp.org/pid/24/6615.html), [Suranga Seneviratne](https://dblp.org/pid/126/2555.html), [Kanchana Thilakarathna](https://dblp.org/pid/92/10700.html), [Darren Webb](https://dblp.org/pid/36/4297.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Task adaptive siamese neural networks for open-set recognition of encrypted network traffic with bidirectional dropout. [Pattern Recognit. Lett.159](https://dblp.org/db/journals/prl/prl159.html#journals/prl/HuangLHJCSTWX22): 132-139 (2022)
- ![](https://dblp.org/img/n.png)

\[j38\]
[Andre Pearce](https://dblp.org/pid/282/9349.html)![](https://dblp.org/img/orcid-mark.12x12.png), [J. Andrew Zhang](https://dblp.org/pid/07/314-a.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Xu![](https://dblp.org/img/orcid-mark.12x12.png):

A Combined mmWave Tracking and Classification Framework Using a Camera for Labeling and Supervised Learning. [Sensors22(22)](https://dblp.org/db/journals/sensors/sensors22.html#journals/sensors/PearceZX22): 8859 (2022)
- ![](https://dblp.org/img/n.png)

\[j37\]
[Ziyue Zhang](https://dblp.org/pid/202/8855.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shuai Jiang](https://dblp.org/pid/45/5080.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Congzhentao Huang](https://dblp.org/pid/258/0557.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Unsupervised Clothing Change Adaptive Person ReID. [IEEE Signal Process. Lett.29](https://dblp.org/db/journals/spl/spl29.html#journals/spl/ZhangJHX22): 304-308 (2022)
- ![](https://dblp.org/img/n.png)

\[j36\]
[Shuai Jiang](https://dblp.org/pid/45/5080.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kan Li](https://dblp.org/pid/21/2083-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Magnitude Bounded Matrix Factorisation for Recommender Systems. [IEEE Trans. Knowl. Data Eng.34(4)](https://dblp.org/db/journals/tkde/tkde34.html#journals/tkde/JiangLX22): 1856-1869 (2022)
- ![](https://dblp.org/img/n.png)

\[j35\]
[Zhenguo Shi](https://dblp.org/pid/89/4115.html)![](https://dblp.org/img/orcid-mark.12x12.png), [J. Andrew Zhang](https://dblp.org/pid/07/314-a.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yida Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Qingqing Cheng](https://dblp.org/pid/58/7703.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Environment-Robust Device-Free Human Activity Recognition With Channel-State-Information Enhancement and One-Shot Learning. [IEEE Trans. Mob. Comput.21(2)](https://dblp.org/db/journals/tmc/tmc21.html#journals/tmc/ShiZXC22): 540-554 (2022)
- ![](https://dblp.org/img/n.png)

\[c61\]
[Qing Yin](https://dblp.org/pid/55/10035.html), [Zhihua Wang](https://dblp.org/pid/66/6802-8.html), [Yunya Song](https://dblp.org/pid/165/3067.html), Richard Yida Xu, [Shuai Niu](https://dblp.org/pid/31/5390.html), [Liang Bai](https://dblp.org/pid/91/6504-1.html), [Yike Guo](https://dblp.org/pid/g/YikeGuo.html), [Xian Yang](https://dblp.org/pid/25/10624-1.html):

Improving Deep Embedded Clustering via Learning Cluster-level Representations. [COLING2022](https://dblp.org/db/conf/coling/coling2022.html#conf/coling/YinWSXNBG022): 2226-2236
- ![](https://dblp.org/img/n.png)

\[c60\]
[Wei Huang](https://dblp.org/pid/81/6685-34.html), [Yayong Li](https://dblp.org/pid/187/5915.html), [Weitao Du](https://dblp.org/pid/17/10015.html), Richard Y. D. Xu, [Jie Yin](https://dblp.org/pid/97/3358-1.html), [Ling Chen](https://dblp.org/pid/17/1237-6.html), [Miao Zhang](https://dblp.org/pid/60/7041-22.html):

Towards Deepening Graph Neural Networks: A GNTK-based Optimization Perspective. [ICLR2022](https://dblp.org/db/conf/iclr/iclr2022.html#conf/iclr/HuangLDXYCZ22)
- ![](https://dblp.org/img/n.png)

\[c59\]
[Lu Mi](https://dblp.org/pid/185/3258.html), Richard Xu, [Sridhama Prakhya](https://dblp.org/pid/242/9030.html), [Albert Lin](https://dblp.org/pid/32/3460.html), [Nir Shavit](https://dblp.org/pid/s/NirShavit.html), [Aravinthan D. T. Samuel](https://dblp.org/pid/275/6920.html), [Srinivas C. Turaga](https://dblp.org/pid/91/747.html):

Connectome-constrained Latent Variable Model of Whole-Brain Neural Activity. [ICLR2022](https://dblp.org/db/conf/iclr/iclr2022.html#conf/iclr/MiXPLSST22)
- ![](https://dblp.org/img/n.png)

\[i30\]
[Wei Huang](https://dblp.org/pid/81/6685-34.html), [Chunrui Liu](https://dblp.org/pid/266/7209.html), [Yilan Chen](https://dblp.org/pid/167/6638-2.html), [Tianyu Liu](https://dblp.org/pid/134/1099.html), Richard Yi Da Xu:

Demystify Optimization and Generalization of Over-parameterized PAC-Bayesian Learning. [CoRRabs/2202.01958](https://dblp.org/db/journals/corr/corr2202.html#journals/corr/abs-2202-01958) (2022)
- ![](https://dblp.org/img/n.png)

\[i29\]
[Leijie Wu](https://dblp.org/pid/303/7332.html), [Song Guo](https://dblp.org/pid/01/267-1.html), [Yaohong Ding](https://dblp.org/pid/313/1192.html), [Junxiao Wang](https://dblp.org/pid/221/1246.html), [Wenchao Xu](https://dblp.org/pid/96/8862-1.html), Richard Yida Xu, [Jie Zhang](https://dblp.org/pid/84/6889-76.html):

Demystify Self-Attention in Vision Transformers from a Semantic Perspective: Analysis and Application. [CoRRabs/2211.08543](https://dblp.org/db/journals/corr/corr2211.html#journals/corr/abs-2211-08543) (2022)
- ![](https://dblp.org/img/n.png)

\[i28\]
[Yingchun Wang](https://dblp.org/pid/15/6511.html), [Song Guo](https://dblp.org/pid/01/267-1.html), [Jingcai Guo](https://dblp.org/pid/192/7270.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weizhan Zhang](https://dblp.org/pid/17/6858.html), Richard Yida Xu, [Jie Zhang](https://dblp.org/pid/84/6889-76.html), [Yi Liu](https://dblp.org/pid/97/4626-57.html):

Efficient Stein Variational Inference for Reliable Distribution-lossless Network Pruning. [CoRRabs/2212.03537](https://dblp.org/db/journals/corr/corr2212.html#journals/corr/abs-2212-03537) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[j34\]
[Ziyue Zhang](https://dblp.org/pid/202/8855.html), [Shuai Jiang](https://dblp.org/pid/45/5080.html), [Congzhentao Huang](https://dblp.org/pid/258/0557.html), [Yang Li](https://dblp.org/pid/37/4190-82.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

RGB-IR cross-modality person ReID based on teacher-student GAN model. [Pattern Recognit. Lett.150](https://dblp.org/db/journals/prl/prl150.html#journals/prl/ZhangJHLX21): 155-161 (2021)
- ![](https://dblp.org/img/n.png)

\[j33\]
[Wei Huang](https://dblp.org/pid/81/6685-34.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Gaussian process latent variable model factorization for context-aware recommender systems. [Pattern Recognit. Lett.151](https://dblp.org/db/journals/prl/prl151.html#journals/prl/HuangX21): 281-287 (2021)
- ![](https://dblp.org/img/n.png)

\[j32\]
[Caoyuan Li](https://dblp.org/pid/157/8323.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hong-Bo Xie](https://dblp.org/pid/54/7839.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xuhui Fan](https://dblp.org/pid/117/4874.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Sabine Van Huffel](https://dblp.org/pid/60/5071.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kerrie L. Mengersen](https://dblp.org/pid/64/3136.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Kernelized Sparse Bayesian Matrix Factorization. [IEEE Trans. Neural Networks Learn. Syst.32(1)](https://dblp.org/db/journals/tnn/tnn32.html#journals/tnn/LiXFXHM21): 391-404 (2021)
- ![](https://dblp.org/img/n.png)

\[c58\]
[Christos Markos](https://dblp.org/pid/197/6658.html), [James J. Q. Yu](https://dblp.org/pid/55/10087.html), Richard Yi Da Xu:

Capturing Uncertainty in Unsupervised GPS Trajectory Segmentation Using Bayesian Deep Learning. [AAAI2021](https://dblp.org/db/conf/aaai/aaai2021.html#conf/aaai/MarkosYX21): 390-398
- ![](https://dblp.org/img/n.png)

\[c57\]
[Chapman Siu](https://dblp.org/pid/222/3167.html), [Jason Traish](https://dblp.org/pid/302/4716.html), Richard Yi Da Xu:

Dynamic Coordination Graph for Cooperative Multi-Agent Reinforcement Learning. [ACML2021](https://dblp.org/db/conf/acml/acml2021.html#conf/acml/SiuTX21): 438-453
- ![](https://dblp.org/img/n.png)

\[c56\]
[Steven Y. K. Wong](https://dblp.org/pid/260/0739.html), [Jennifer S. K. Chan](https://dblp.org/pid/09/4557.html), [Lamiae Azizi](https://dblp.org/pid/155/3944.html), Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Supervised Temporal Autoencoder for Stock Return Time-series Forecasting. [COMPSAC2021](https://dblp.org/db/conf/compsac/compsac2021.html#conf/compsac/WongCAX21): 1735-1741
- ![](https://dblp.org/img/n.png)

\[c55\]
[Ziyue Zhang](https://dblp.org/pid/202/8855.html), [Shuai Jiang](https://dblp.org/pid/45/5080.html), [Congzhentao Huang](https://dblp.org/pid/258/0557.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Resolution-Invariant Person Reid Based On Feature Transformation And Self-Weighted Attention. [ICIP2021](https://dblp.org/db/conf/icip/icip2021.html#conf/icip/ZhangJHX21): 1134-1138
- ![](https://dblp.org/img/n.png)

\[c54\]
[Wei Huang](https://dblp.org/pid/81/6685-34.html), [Weitao Du](https://dblp.org/pid/17/10015.html), Richard Yi Da Xu:

On the Neural Tangent Kernel of Deep Networks with Orthogonal Initialization. [IJCAI2021](https://dblp.org/db/conf/ijcai/ijcai2021.html#conf/ijcai/HuangDX21): 2577-2583
- ![](https://dblp.org/img/n.png)

\[i27\]
[Ziyue Zhang](https://dblp.org/pid/202/8855.html), [Shuai Jiang](https://dblp.org/pid/45/5080.html), [Congzhentao Huang](https://dblp.org/pid/258/0557.html), Richard Yi Da Xu:

Resolution-invariant Person ReID Based on Feature Transformation and Self-weighted Attention. [CoRRabs/2101.04544](https://dblp.org/db/journals/corr/corr2101.html#journals/corr/abs-2101-04544) (2021)
- ![](https://dblp.org/img/n.png)

\[i26\]
[Wei Huang](https://dblp.org/pid/81/6685-34.html), [Yayong Li](https://dblp.org/pid/187/5915.html), [Weitao Du](https://dblp.org/pid/17/10015.html), Richard Yi Da Xu, [Jie Yin](https://dblp.org/pid/97/3358-1.html), [Ling Chen](https://dblp.org/pid/17/1237-6.html):

Wide Graph Neural Networks: Aggregation Provably Leads to Exponentially Trainability Loss. [CoRRabs/2103.03113](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-03113) (2021)
- ![](https://dblp.org/img/n.png)

\[i25\]
[Sen Pei](https://dblp.org/pid/129/1503.html), Richard Yi Da Xu, [Shiming Xiang](https://dblp.org/pid/81/6575.html), [Gaofeng Meng](https://dblp.org/pid/78/6915.html):

Alleviating Mode Collapse in GAN via Diversity Penalty Module. [CoRRabs/2108.02353](https://dblp.org/db/journals/corr/corr2108.html#journals/corr/abs-2108-02353) (2021)
- ![](https://dblp.org/img/n.png)

\[i24\]
[Ziyue Zhang](https://dblp.org/pid/202/8855.html), [Shuai Jiang](https://dblp.org/pid/45/5080.html), [Congzhentao Huang](https://dblp.org/pid/258/0557.html), Richard Yida Xu:

Unsupervised clothing change adaptive person ReID. [CoRRabs/2109.03702](https://dblp.org/db/journals/corr/corr2109.html#journals/corr/abs-2109-03702) (2021)
- ![](https://dblp.org/img/n.png)

\[i23\]
[Chapman Siu](https://dblp.org/pid/222/3167.html), [Jason M. Traish](https://dblp.org/pid/61/2861.html), Richard Yi Da Xu:

Greedy UnMixing for Q-Learning in Multi-Agent Reinforcement Learning. [CoRRabs/2109.09034](https://dblp.org/db/journals/corr/corr2109.html#journals/corr/abs-2109-09034) (2021)
- ![](https://dblp.org/img/n.png)

\[i22\]
[Chapman Siu](https://dblp.org/pid/222/3167.html), [Jason M. Traish](https://dblp.org/pid/61/2861.html), Richard Yi Da Xu:

Dual Behavior Regularized Reinforcement Learning. [CoRRabs/2109.09037](https://dblp.org/db/journals/corr/corr2109.html#journals/corr/abs-2109-09037) (2021)
- ![](https://dblp.org/img/n.png)

\[i21\]
[Chapman Siu](https://dblp.org/pid/222/3167.html), [Jason Traish](https://dblp.org/pid/302/4716.html), Richard Yi Da Xu:

Regularize! Don't Mix: Multi-Agent Reinforcement Learning without Explicit Centralized Structures. [CoRRabs/2109.09038](https://dblp.org/db/journals/corr/corr2109.html#journals/corr/abs-2109-09038) (2021)
- ![](https://dblp.org/img/n.png)

\[i20\]
[Sen Pei](https://dblp.org/pid/129/1503.html), [Xin Zhang](https://dblp.org/pid/76/1584-93.html), Richard Yida Xu, [Gaofeng Meng](https://dblp.org/pid/78/6915.html):

GAN Based Boundary Aware Classifier for Detecting Out-of-distribution Samples. [CoRRabs/2112.11648](https://dblp.org/db/journals/corr/corr2112.html#journals/corr/abs-2112-11648) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[j31\]
[Kael Dai](https://dblp.org/pid/269/0476.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sergey L. Gratiy](https://dblp.org/pid/155/7888.html), [Yazan N. Billeh](https://dblp.org/pid/166/8634.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Xu, [Binghuang Cai](https://dblp.org/pid/31/1412.html), [Nicholas Cain](https://dblp.org/pid/124/5187.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Atle E. Rimehaug](https://dblp.org/pid/311/9849.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alexander J. Stasik](https://dblp.org/pid/269/1161.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Gaute T. Einevoll](https://dblp.org/pid/70/3700.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Stefan Mihalas](https://dblp.org/pid/90/7228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christof Koch](https://dblp.org/pid/71/4603.html), [Anton Arkhipov](https://dblp.org/pid/155/3493.html):

Brain Modeling ToolKit: An open source software suite for multiscale modeling of brain circuits. [PLoS Comput. Biol.16(11)](https://dblp.org/db/journals/ploscb/ploscb16.html#journals/ploscb/DaiGBXCCRSEMKA20) (2020)
- ![](https://dblp.org/img/n.png)

\[j30\]
[Yang Li](https://dblp.org/pid/37/4190-82.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kan Li](https://dblp.org/pid/21/2083-1.html), [Xinxin Wang](https://dblp.org/pid/24/3969.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Exploring temporal consistency for human pose estimation in videos. [Pattern Recognit.103](https://dblp.org/db/journals/pr/pr103.html#journals/pr/LiLWX20): 107258 (2020)
- ![](https://dblp.org/img/n.png)

\[j29\]
[Minqi Li](https://dblp.org/pid/159/1126.html), Richard Yida Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Xin](https://dblp.org/pid/81/1853.html), [Kaibing Zhang](https://dblp.org/pid/91/10256.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Junfeng Jing](https://dblp.org/pid/115/5261.html):

Fast non-rigid points registration with cluster correspondences projection. [Signal Process.170](https://dblp.org/db/journals/sigpro/sigpro170.html#journals/sigpro/LiXXZJ20): 107425 (2020)
- ![](https://dblp.org/img/n.png)

\[j28\]
[Caoyuan Li](https://dblp.org/pid/157/8323.html), [Hong-Bo Xie](https://dblp.org/pid/54/7839.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kerrie L. Mengersen](https://dblp.org/pid/64/3136.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xuhui Fan](https://dblp.org/pid/117/4874.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Scott A. Sisson](https://dblp.org/pid/46/8608.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sabine Van Huffel](https://dblp.org/pid/60/5071.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Bayesian Nonnegative Matrix Factorization With Dirichlet Process Mixtures. [IEEE Trans. Signal Process.68](https://dblp.org/db/journals/tsp/tsp68.html#journals/tsp/LiXMFXSH20): 3860-3870 (2020)
- ![](https://dblp.org/img/n.png)

\[c53\]
[Yang Li](https://dblp.org/pid/37/4190-82.html), [Kan Li](https://dblp.org/pid/21/2083-1.html), [Shuai Jiang](https://dblp.org/pid/45/5080.html), [Ziyue Zhang](https://dblp.org/pid/202/8855.html), [Congzhentao Huang](https://dblp.org/pid/258/0557.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Geometry-Driven Self-Supervised Method for 3D Human Pose Estimation. [AAAI2020](https://dblp.org/db/conf/aaai/aaai2020.html#conf/aaai/LiLJZHX20): 11442-11449
- ![](https://dblp.org/img/n.png)

\[c52\]
[Wei Huang](https://dblp.org/pid/81/6685-34.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Weitao Du](https://dblp.org/pid/17/10015.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yutian Zeng](https://dblp.org/pid/255/5747.html), [Yunce Zhao](https://dblp.org/pid/255/5947.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Mean Field Theory for Deep Dropout Networks: Digging up Gradient Backpropagation Deeply. [ECAI2020](https://dblp.org/db/conf/ecai/ecai2020.html#conf/ecai/HuangXDZZ20): 1215-1222
- ![](https://dblp.org/img/n.png)

\[c51\]
[Congzhentao Huang](https://dblp.org/pid/258/0557.html), [Shuai Jiang](https://dblp.org/pid/45/5080.html), [Yang Li](https://dblp.org/pid/37/4190-82.html), [Ziyue Zhang](https://dblp.org/pid/202/8855.html), [Jason M. Traish](https://dblp.org/pid/61/2861.html), [Chen Deng](https://dblp.org/pid/22/9348.html), [Sam Ferguson](https://dblp.org/pid/228/5939.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

End-to-end Dynamic Matching Network for Multi-view Multi-person 3D Pose Estimation. [ECCV (28)2020](https://dblp.org/db/conf/eccv/eccv2020-28.html#conf/eccv/HuangJLZTDFX20): 477-493
- ![](https://dblp.org/img/n.png)

\[c50\]
[Zhenguo Shi](https://dblp.org/pid/89/4115.html)![](https://dblp.org/img/orcid-mark.12x12.png), [J. Andrew Zhang](https://dblp.org/pid/07/314-a.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Qingqing Cheng](https://dblp.org/pid/58/7703.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Andre Pearce](https://dblp.org/pid/282/9349.html):

Towards Environment-independent Human Activity Recognition using Deep Learning and Enhanced CSI. [GLOBECOM2020](https://dblp.org/db/conf/globecom/globecom2020.html#conf/globecom/ShiZXCP20): 1-6
- ![](https://dblp.org/img/n.png)

\[c49\]
[Zhenguo Shi](https://dblp.org/pid/89/4115.html)![](https://dblp.org/img/orcid-mark.12x12.png), [J. Andrew Zhang](https://dblp.org/pid/07/314-a.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yida Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Qingqing Cheng](https://dblp.org/pid/58/7703.html)![](https://dblp.org/img/orcid-mark.12x12.png):

WiFi-Based Activity Recognition using Activity Filter and Enhanced Correlation with Deep Learning. [ICC Workshops2020](https://dblp.org/db/conf/icc/icc2020w.html#conf/icc/ShiZXC20): 1-6
- ![](https://dblp.org/img/n.png)

\[c48\]
[Ziyue Zhang](https://dblp.org/pid/202/8855.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Shuai Jiang](https://dblp.org/pid/45/5080.html), [Yang Li](https://dblp.org/pid/37/4190-82.html), [Congzhentao Huang](https://dblp.org/pid/258/0557.html), [Chen Deng](https://dblp.org/pid/22/9348.html):

Illumination Adaptive Person Reid Based on Teacher-Student Model and Adversarial Training. [ICIP2020](https://dblp.org/db/conf/icip/icip2020.html#conf/icip/ZhangXJ0HD20): 2321-2325
- ![](https://dblp.org/img/n.png)

\[c47\]
[Siqi Zhang](https://dblp.org/pid/55/287.html), [Ling Luo](https://dblp.org/pid/00/1811-2.html), [Zhidong Li](https://dblp.org/pid/10/6710.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Wang](https://dblp.org/pid/w/YangWang2.html), [Fang Chen](https://dblp.org/pid/52/488-1.html), Richard Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Simultaneous Customer Segmentation and Behavior Discovery. [ICONIP (4)2020](https://dblp.org/db/conf/iconip/iconip2020-4.html#conf/iconip/ZhangLL00X20): 122-130
- ![](https://dblp.org/img/n.png)

\[c46\]
[Wanming Huang](https://dblp.org/pid/92/7710.html), Richard Yida Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Shuai Jiang](https://dblp.org/pid/45/5080.html), [Xuan Liang](https://dblp.org/pid/119/7993.html), [Ian J. Oppermann](https://dblp.org/pid/132/8466.html)![](https://dblp.org/img/orcid-mark.12x12.png):

GAN-based Gaussian Mixture Model Responsibility Learning. [ICPR2020](https://dblp.org/db/conf/icpr/icpr2020.html#conf/icpr/HuangXJLO20): 3467-3474
- ![](https://dblp.org/img/n.png)

\[c45\]
[Jingwei Liu](https://dblp.org/pid/29/4366.html), [J. Andrew Zhang](https://dblp.org/pid/07/314-a.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Andre Pearce](https://dblp.org/pid/282/9349.html), [Wei Ni](https://dblp.org/pid/31/2597-1.html), [Mark Hedley](https://dblp.org/pid/14/4985.html):

Gaussian Mixture Model based Convolutional Sparse Coding for Radar Heartbeat Detection. [ICSPCS2020](https://dblp.org/db/conf/icspcs/icspcs2020.html#conf/icspcs/LiuZXPNH20): 1-6
- ![](https://dblp.org/img/n.png)

\[c44\]
[Hong-Bo Xie](https://dblp.org/pid/54/7839.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Caoyuan Li](https://dblp.org/pid/157/8323.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kerrie L. Mengersen](https://dblp.org/pid/64/3136.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shuliang Wang](https://dblp.org/pid/36/4791-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Nonparametric Bayesian Nonnegative Matrix Factorization. [MDAI2020](https://dblp.org/db/conf/mdai/mdai2020.html#conf/mdai/XieLMWX20): 132-141
- ![](https://dblp.org/img/n.png)

\[c43\]
[Luke Marsh](https://dblp.org/pid/178/8796.html), [Madeleine Cochrane](https://dblp.org/pid/226/6263.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Riley Lodge](https://dblp.org/pid/245/5887.html), [Brendan Sims](https://dblp.org/pid/224/1067.html), [Jason M. Traish](https://dblp.org/pid/61/2861.html), Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Autonomous Target Allocation Recommendations. [SSCI2020](https://dblp.org/db/conf/ssci/ssci2020.html#conf/ssci/MarshCLSTX20): 1403-1410
- ![](https://dblp.org/img/n.png)

\[i19\]
[Ziyue Zhang](https://dblp.org/pid/202/8855.html), Richard Y. D. Xu, [Shuai Jiang](https://dblp.org/pid/45/5080.html), [Yang Li](https://dblp.org/pid/37/4190-82.html), [Congzhentao Huang](https://dblp.org/pid/258/0557.html), [Chen Deng](https://dblp.org/pid/22/9348.html):

Illumination adaptive person reid based on teacher-student model and adversarial training. [CoRRabs/2002.01625](https://dblp.org/db/journals/corr/corr2002.html#journals/corr/abs-2002-01625) (2020)
- ![](https://dblp.org/img/n.png)

\[i18\]
[Steven Y. K. Wong](https://dblp.org/pid/260/0739.html), [Jennifer S. K. Chan](https://dblp.org/pid/09/4557.html), [Lamiae Azizi](https://dblp.org/pid/155/3944.html), Richard Y. D. Xu:

Non-stationary neural network for stock return prediction. [CoRRabs/2003.02515](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-02515) (2020)
- ![](https://dblp.org/img/n.png)

\[i17\]
[Wei Huang](https://dblp.org/pid/81/6685-34.html), [Weitao Du](https://dblp.org/pid/17/10015.html), Richard Yi Da Xu:

On the Neural Tangent Kernel of Deep Networks with Orthogonal Initialization. [CoRRabs/2004.05867](https://dblp.org/db/journals/corr/corr2004.html#journals/corr/abs-2004-05867) (2020)
- ![](https://dblp.org/img/n.png)

\[i16\]
[Ziyue Zhang](https://dblp.org/pid/202/8855.html), [Shuai Jiang](https://dblp.org/pid/45/5080.html), [Congzhentao Huang](https://dblp.org/pid/258/0557.html), [Yang Li](https://dblp.org/pid/37/4190-82.html), Richard Yi Da Xu:

RGB-IR Cross-modality Person ReID based on Teacher-Student GAN Model. [CoRRabs/2007.07452](https://dblp.org/db/journals/corr/corr2007.html#journals/corr/abs-2007-07452) (2020)
- ![](https://dblp.org/img/n.png)

\[i15\]
[Wei Huang](https://dblp.org/pid/81/6685-34.html), [Weitao Du](https://dblp.org/pid/17/10015.html), Richard Yi Da Xu, [Chunrui Liu](https://dblp.org/pid/266/7209.html):

Implicit bias of deep linear networks in the large learning rate phase. [CoRRabs/2011.12547](https://dblp.org/db/journals/corr/corr2011.html#journals/corr/abs-2011-12547) (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j27\]
[Caoyuan Li](https://dblp.org/pid/157/8323.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hong-Bo Xie](https://dblp.org/pid/54/7839.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xuhui Fan](https://dblp.org/pid/117/4874.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Sabine Van Huffel](https://dblp.org/pid/60/5071.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Scott A. Sisson](https://dblp.org/pid/46/8608.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kerrie L. Mengersen](https://dblp.org/pid/64/3136.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Image Denoising Based on Nonlocal Bayesian Singular Value Thresholding and Stein's Unbiased Risk Estimator. [IEEE Trans. Image Process.28(10)](https://dblp.org/db/journals/tip/tip28.html#journals/tip/LiXFXHSM19): 4899-4911 (2019)
- ![](https://dblp.org/img/n.png)

\[j26\]
[Shuai Jiang](https://dblp.org/pid/45/5080.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kan Li](https://dblp.org/pid/21/2083-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Relative Pairwise Relationship Constrained Non-Negative Matrix Factorisation. [IEEE Trans. Knowl. Data Eng.31(8)](https://dblp.org/db/journals/tkde/tkde31.html#journals/tkde/JiangLX19): 1595-1609 (2019)
- ![](https://dblp.org/img/n.png)

\[j25\]
[Wei He](https://dblp.org/pid/20/6417-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changyin Sun](https://dblp.org/pid/64/221.html), [Donald C. Wunsch](https://dblp.org/pid/w/DCWunsch.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Guest Editorial Special Issue on Intelligent Control Through Neural Learning and Optimization for Human-Machine Hybrid Systems. [IEEE Trans. Neural Networks Learn. Syst.30(12)](https://dblp.org/db/journals/tnn/tnn30.html#journals/tnn/HeSWX19): 3530-3533 (2019)
- ![](https://dblp.org/img/n.png)

\[c42\]
[Wanming Huang](https://dblp.org/pid/92/7710.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Ian J. Oppermann](https://dblp.org/pid/132/8466.html):

Realistic Image Generation using Region-phrase Attention. [ACML2019](https://dblp.org/db/conf/acml/acml2019.html#conf/acml/HuangXO19): 284-299
- ![](https://dblp.org/img/n.png)

\[c41\]
[Wanming Huang](https://dblp.org/pid/92/7710.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Ian J. Oppermann](https://dblp.org/pid/132/8466.html):

Efficient Diversified Mini-Batch Selection using Variable High-layer Features. [ACML2019](https://dblp.org/db/conf/acml/acml2019.html#conf/acml/HuangXO19a): 300-315
- ![](https://dblp.org/img/n.png)

\[c40\]
[Zhenguo Shi](https://dblp.org/pid/89/4115.html)![](https://dblp.org/img/orcid-mark.12x12.png), [J. Andrew Zhang](https://dblp.org/pid/07/314-a.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Qingqing Cheng](https://dblp.org/pid/58/7703.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Deep Learning Networks for Human Activity Recognition with CSI Correlation Feature Extraction. [ICC2019](https://dblp.org/db/conf/icc/icc2019.html#conf/icc/ShiZXC19): 1-6
- ![](https://dblp.org/img/n.png)

\[c39\]
[Kai Zhou](https://dblp.org/pid/82/1512.html), [Xiangfeng Luo](https://dblp.org/pid/63/4996.html), [Hao Wang](https://dblp.org/pid/181/2812-97.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Multi-task Learning for Relation Extraction. [ICTAI2019](https://dblp.org/db/conf/ictai/ictai2019.html#conf/ictai/ZhouLWX19): 1480-1487
- ![](https://dblp.org/img/n.png)

\[c38\]
[Qiongxing Tao](https://dblp.org/pid/255/5561.html), [Xiangfeng Luo](https://dblp.org/pid/63/4996.html), [Hao Wang](https://dblp.org/pid/181/2812-97.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Enhancing Relation Extraction Using Syntactic Indicators and Sentential Contexts. [ICTAI2019](https://dblp.org/db/conf/ictai/ictai2019.html#conf/ictai/TaoLWX19): 1574-1580
- ![](https://dblp.org/img/n.png)

\[c37\]
[Hong-Bo Xie](https://dblp.org/pid/54/7839.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Caoyuan Li](https://dblp.org/pid/157/8323.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Kerrie L. Mengersen](https://dblp.org/pid/64/3136.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Robust Kernelized Bayesian Matrix Factorization for Video Background/Foreground Separation. [LOD2019](https://dblp.org/db/conf/mod/lod2019.html#conf/mod/XieLXM19): 484-495
- ![](https://dblp.org/img/n.png)

\[i14\]
[Maoying Qiao](https://dblp.org/pid/62/9638.html), [Wei Bian](https://dblp.org/pid/77/3270.html), Richard Yida Xu, [Dacheng Tao](https://dblp.org/pid/46/3391.html):

Diversified Hidden Markov Models for Sequential Labeling. [CoRRabs/1904.03170](https://dblp.org/db/journals/corr/corr1904.html#journals/corr/abs-1904-03170) (2019)
- ![](https://dblp.org/img/n.png)

\[i13\]
[Wei Huang](https://dblp.org/pid/81/6685-34.html), Richard Yi Da Xu, [Weitao Du](https://dblp.org/pid/17/10015.html), [Yutian Zeng](https://dblp.org/pid/255/5747.html), [Yunce Zhao](https://dblp.org/pid/255/5947.html):

Mean field theory for deep dropout networks: digging up gradient backpropagation deeply. [CoRRabs/1912.09132](https://dblp.org/db/journals/corr/corr1912.html#journals/corr/abs-1912-09132) (2019)
- ![](https://dblp.org/img/n.png)

\[i12\]
[Wei Huang](https://dblp.org/pid/81/6685-34.html), Richard Yi Da Xu:

Gaussian Process Latent Variable Model Factorization for Context-aware Recommender Systems. [CoRRabs/1912.09593](https://dblp.org/db/journals/corr/corr1912.html#journals/corr/abs-1912-09593) (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[j24\]
[Wankou Yang](https://dblp.org/pid/99/3602.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Li](https://dblp.org/pid/116/1011-33.html), [Hao Zheng](https://dblp.org/pid/31/6916.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

A Nuclear Norm Based Matrix Regression Based Projections Method for Feature Extraction. [IEEE Access6](https://dblp.org/db/journals/access/access6.html#journals/access/YangLZX18): 7445-7451 (2018)
- ![](https://dblp.org/img/n.png)

\[j23\]
[Xiang Feng](https://dblp.org/pid/19/3734.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wanggen Wan](https://dblp.org/pid/83/7086.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Stuart W. Perry](https://dblp.org/pid/50/6281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pengfei Li](https://dblp.org/pid/10/1749.html), [Song Zhu](https://dblp.org/pid/00/4449.html):

A novel spatial pooling method for 3D mesh quality assessment based on percentile weighting strategy. [Comput. Graph.74](https://dblp.org/db/journals/cg/cg74.html#journals/cg/FengWXPLZ18): 12-22 (2018)
- ![](https://dblp.org/img/n.png)

\[j22\]
[Xiang Feng](https://dblp.org/pid/19/3734.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wanggen Wan](https://dblp.org/pid/83/7086.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Stuart W. Perry](https://dblp.org/pid/50/6281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Song Zhu](https://dblp.org/pid/00/4449.html), [Zexin Liu](https://dblp.org/pid/45/9879.html):

A new mesh visual quality metric using saliency weighting-based pooling strategy. [Graph. Model.99](https://dblp.org/db/journals/cvgip/cvgip99.html#journals/cvgip/FengWXPZL18): 1-12 (2018)
- ![](https://dblp.org/img/n.png)

\[j21\]
[Xiang Feng](https://dblp.org/pid/19/3734.html), [Wanggen Wan](https://dblp.org/pid/83/7086.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Haoyu Chen](https://dblp.org/pid/146/8170.html), [Pengfei Li](https://dblp.org/pid/10/1749.html), [J. Alfredo Sánchez](https://dblp.org/pid/s/JASanchez.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A perceptual quality metric for 3D triangle meshes based on spatial pooling. [Frontiers Comput. Sci.12(4)](https://dblp.org/db/journals/fcsc/fcsc12.html#journals/fcsc/FengWXCLS18): 798-812 (2018)
- ![](https://dblp.org/img/n.png)

\[j20\]
[Junyu Xuan](https://dblp.org/pid/08/10768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Lu](https://dblp.org/pid/39/2936-1.html), [Guangquan Zhang](https://dblp.org/pid/37/628-1.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xiangfeng Luo](https://dblp.org/pid/63/4996.html):

Doubly Nonparametric Sparse Nonnegative Matrix Factorization Based on Dependent Indian Buffet Processes. [IEEE Trans. Neural Networks Learn. Syst.29(5)](https://dblp.org/db/journals/tnn/tnn29.html#journals/tnn/XuanLZXL18): 1835-1849 (2018)
- ![](https://dblp.org/img/n.png)

\[j19\]
[Ava Bargi](https://dblp.org/pid/64/9659.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

AdOn HDP-HMM: An Adaptive Online Model for Segmentation and Classification of Sequential Data. [IEEE Trans. Neural Networks Learn. Syst.29(9)](https://dblp.org/db/journals/tnn/tnn29.html#journals/tnn/BargiXP18): 3953-3968 (2018)
- ![](https://dblp.org/img/n.png)

\[c36\]
[Zhenguo Shi](https://dblp.org/pid/89/4115.html)![](https://dblp.org/img/orcid-mark.12x12.png), [J. Andrew Zhang](https://dblp.org/pid/07/314-a.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Gengfa Fang](https://dblp.org/pid/50/6377.html):

Human Activity Recognition Using Deep Learning Networks with Enhanced Channel State Information. [GLOBECOM Workshops2018](https://dblp.org/db/conf/globecom/globecom2018w.html#conf/globecom/ShiZXF18): 1-6
- ![](https://dblp.org/img/n.png)

\[c35\]
[Ying Li](https://dblp.org/pid/22/1805-39.html), [Yi Huang](https://dblp.org/pid/15/6040-23.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Suranga Seneviratne](https://dblp.org/pid/126/2555.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kanchana Thilakarathna](https://dblp.org/pid/92/10700.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Adriel Cheng](https://dblp.org/pid/24/6615.html), [Darren Webb](https://dblp.org/pid/36/4297.html), [Guillaume Jourjon](https://dblp.org/pid/51/2666.html):

Deep Content: Unveiling Video Streaming Content from Encrypted WiFi Traffic. [NCA2018](https://dblp.org/db/conf/nca/nca2018.html#conf/nca/LiHXSTCWJ18): 1-8
- ![](https://dblp.org/img/n.png)

\[i11\]
[Shuai Jiang](https://dblp.org/pid/45/5080.html), [Kan Li](https://dblp.org/pid/21/2083-1.html), Richard Yida Xu:

Relative Pairwise Relationship Constrained Non-negative Matrix Factorisation. [CoRRabs/1803.02218](https://dblp.org/db/journals/corr/corr1803.html#journals/corr/abs-1803-02218) (2018)
- ![](https://dblp.org/img/n.png)

\[i10\]
[Chapman Siu](https://dblp.org/pid/222/3167.html), Richard Yi Da Xu:

Diverse Online Feature Selection. [CoRRabs/1806.04308](https://dblp.org/db/journals/corr/corr1806.html#journals/corr/abs-1806-04308) (2018)
- ![](https://dblp.org/img/n.png)

\[i9\]
[Shuai Jiang](https://dblp.org/pid/45/5080.html), [Kan Li](https://dblp.org/pid/21/2083-1.html), Richard Yi Da Xu:

Magnitude Bounded Matrix Factorisation for Recommender Systems. [CoRRabs/1807.05515](https://dblp.org/db/journals/corr/corr1807.html#journals/corr/abs-1807-05515) (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[j18\]
[Weidong Liu](https://dblp.org/pid/92/9611-8.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiangfeng Luo](https://dblp.org/pid/63/4996.html), [Jun Zhang](https://dblp.org/pid/29/4190-38.html), [Ruirong Xue](https://dblp.org/pid/203/4373.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Semantic summary automatic generation in news event. [Concurr. Comput. Pract. Exp.29(24)](https://dblp.org/db/journals/concurrency/concurrency29.html#journals/concurrency/LiuLZXX17) (2017)
- ![](https://dblp.org/img/n.png)

\[j17\]
[Yufei Chen](https://dblp.org/pid/79/4489-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaodong Yue](https://dblp.org/pid/36/4716-2.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Hamido Fujita](https://dblp.org/pid/49/6628.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Region scalable active contour model with global constraint. [Knowl. Based Syst.120](https://dblp.org/db/journals/kbs/kbs120.html#journals/kbs/ChenYXF17): 57-73 (2017)
- ![](https://dblp.org/img/n.png)

\[j16\]
[Junyu Xuan](https://dblp.org/pid/08/10768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Lu](https://dblp.org/pid/39/2936-1.html), [Guangquan Zhang](https://dblp.org/pid/37/628-1.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xiangfeng Luo](https://dblp.org/pid/63/4996.html):

A Bayesian nonparametric model for multi-label learning. [Mach. Learn.106(11)](https://dblp.org/db/journals/ml/ml106.html#journals/ml/XuanLZXL17): 1787-1815 (2017)
- ![](https://dblp.org/img/n.png)

\[j15\]
[Zheng Xu](https://dblp.org/pid/83/2535-1.html), [Junchi Yan](https://dblp.org/pid/60/7949.html), Richard Yida Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Lin Mei](https://dblp.org/pid/84/4478-1.html):

Guest Editorial: Visual Multimedia Learning from Big Surveillance Data. [Multim. Tools Appl.76(13)](https://dblp.org/db/journals/mta/mta76.html#journals/mta/XuYXM17): 14557 (2017)
- ![](https://dblp.org/img/n.png)

\[j14\]
[Xuhui Fan](https://dblp.org/pid/117/4874.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Longbing Cao](https://dblp.org/pid/14/2589.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yin Song](https://dblp.org/pid/117/4296.html):

Learning Nonparametric Relational Models by Conjugately Incorporating Node Information in a Network. [IEEE Trans. Cybern.47(3)](https://dblp.org/db/journals/tcyb/tcyb47.html#journals/tcyb/FanXCS17): 589-599 (2017)
- ![](https://dblp.org/img/n.png)

\[j13\]
[Jiatong Li](https://dblp.org/pid/19/11348-4.html), [Chenwei Deng](https://dblp.org/pid/73/8538.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Dacheng Tao](https://dblp.org/pid/46/3391.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Baojun Zhao](https://dblp.org/pid/84/10182.html):

Robust Object Tracking With Discrete Graph-Based Multiple Experts. [IEEE Trans. Image Process.26(6)](https://dblp.org/db/journals/tip/tip26.html#journals/tip/LiDXTZ17): 2736-2750 (2017)
- ![](https://dblp.org/img/n.png)

\[j12\]
[Junyu Xuan](https://dblp.org/pid/08/10768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Lu](https://dblp.org/pid/39/2936-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guangquan Zhang](https://dblp.org/pid/37/628-1.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xiangfeng Luo](https://dblp.org/pid/63/4996.html):

Bayesian Nonparametric Relational Topic Model through Dependent Gamma Processes. [IEEE Trans. Knowl. Data Eng.29(7)](https://dblp.org/db/journals/tkde/tkde29.html#journals/tkde/XuanLZXL17): 1357-1369 (2017)
- ![](https://dblp.org/img/n.png)

\[i8\]
[Junyu Xuan](https://dblp.org/pid/08/10768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Lu](https://dblp.org/pid/39/2936-1.html), [Guangquan Zhang](https://dblp.org/pid/37/628-1.html), Richard Yi Da Xu:

Cooperative Hierarchical Dirichlet Processes: Superposition vs. Maximization. [CoRRabs/1707.05420](https://dblp.org/db/journals/corr/corr1707.html#journals/corr/XuanLZX17) (2017)
- 2016
- ![](https://dblp.org/img/n.png)

\[j11\]
[Furong Peng](https://dblp.org/pid/138/8117.html), [Jianfeng Lu](https://dblp.org/pid/82/6187-3.html), [Yongli Wang](https://dblp.org/pid/67/2851.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Chao Ma](https://dblp.org/pid/79/1552-2.html), [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

N-dimensional Markov random field prior for cold-start recommendation. [Neurocomputing191](https://dblp.org/db/journals/ijon/ijon191.html#journals/ijon/PengLWXMY16): 187-199 (2016)
- ![](https://dblp.org/img/n.png)

\[j10\]
[Jiatong Li](https://dblp.org/pid/19/11348-4.html), [Baojun Zhao](https://dblp.org/pid/84/10182.html), [Chenwei Deng](https://dblp.org/pid/73/8538.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Time Varying Metric Learning for visual tracking. [Pattern Recognit. Lett.80](https://dblp.org/db/journals/prl/prl80.html#journals/prl/LiZDX16): 157-164 (2016)
- ![](https://dblp.org/img/n.png)

\[j9\]
[Maoying Qiao](https://dblp.org/pid/62/9638.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Bian](https://dblp.org/pid/77/3270.html), [Dacheng Tao](https://dblp.org/pid/46/3391.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Fast Sampling for Time-Varying Determinantal Point Processes. [ACM Trans. Knowl. Discov. Data11(1)](https://dblp.org/db/journals/tkdd/tkdd11.html#journals/tkdd/QiaoXBT16): 8:1-8:24 (2016)
- ![](https://dblp.org/img/n.png)

\[c34\]
[Qiang Li](https://dblp.org/pid/72/872-24.html), [Wei Bian](https://dblp.org/pid/77/3270.html), Richard Yi Da Xu, [Jane You](https://dblp.org/pid/y/JaneYou.html), [Dacheng Tao](https://dblp.org/pid/46/3391.html):

Random Mixed Field Model for Mixed-Attribute Data Restoration. [AAAI2016](https://dblp.org/db/conf/aaai/aaai2016.html#conf/aaai/LiBXYT16): 1244-1250
- ![](https://dblp.org/img/n.png)

\[c33\]
[Furong Peng](https://dblp.org/pid/138/8117.html), [Xuan Lu](https://dblp.org/pid/51/3865-1.html), [Jianfeng Lu](https://dblp.org/pid/82/6187-3.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Cheng Luo](https://dblp.org/pid/68/6443.html), [Chao Ma](https://dblp.org/pid/79/1552-2.html), [Jingyu Yang](https://dblp.org/pid/65/2850-1.html):

MetricRec: Metric Learning for Cold-Start Recommendations. [ADMA2016](https://dblp.org/db/conf/adma/adma2016.html#conf/adma/PengLLXLMY16): 445-458
- ![](https://dblp.org/img/n.png)

\[c32\]
[Maoying Qiao](https://dblp.org/pid/62/9638.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Bian](https://dblp.org/pid/77/3270.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Dacheng Tao](https://dblp.org/pid/46/3391.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Diversified hidden Markov models for sequential labeling. [ICDE2016](https://dblp.org/db/conf/icde/icde2016.html#conf/icde/QiaoBXT16): 1512-1513
- ![](https://dblp.org/img/n.png)

\[c31\]
[Xuhui Fan](https://dblp.org/pid/117/4874.html), Richard Yi Da Xu, [Longbing Cao](https://dblp.org/pid/14/2589.html):

Copula Mixed-Membership Stochastic Blockmodel. [IJCAI2016](https://dblp.org/db/conf/ijcai/ijcai2016.html#conf/ijcai/FanXC16): 1462-1468
- 2015
- ![](https://dblp.org/img/n.png)

\[j8\]
[Michael Kemp](https://dblp.org/pid/56/8109.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Geometrically-constrained balloon fitting for multiple connected ellipses. [Pattern Recognit.48(7)](https://dblp.org/db/journals/pr/pr48.html#journals/pr/KempX15): 2198-2208 (2015)
- ![](https://dblp.org/img/n.png)

\[j7\]
[Maoying Qiao](https://dblp.org/pid/62/9638.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Bian](https://dblp.org/pid/77/3270.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Dacheng Tao](https://dblp.org/pid/46/3391.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Diversified Hidden Markov Models for Sequential Labeling. [IEEE Trans. Knowl. Data Eng.27(11)](https://dblp.org/db/journals/tkde/tkde27.html#journals/tkde/QiaoBXT15): 2947-2960 (2015)
- ![](https://dblp.org/img/n.png)

\[j6\]
[Xuhui Fan](https://dblp.org/pid/117/4874.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Longbing Cao](https://dblp.org/pid/14/2589.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Dynamic Infinite Mixed-Membership Stochastic Blockmodel. [IEEE Trans. Neural Networks Learn. Syst.26(9)](https://dblp.org/db/journals/tnn/tnn26.html#journals/tnn/FanCX15): 2072-2085 (2015)
- ![](https://dblp.org/img/n.png)

\[c30\]
[Junyu Xuan](https://dblp.org/pid/08/10768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Lu](https://dblp.org/pid/39/2936-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guangquan Zhang](https://dblp.org/pid/37/628-1.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xiangfeng Luo](https://dblp.org/pid/63/4996.html):

Infinite Author Topic Model Based on Mixed Gamma-Negative Binomial Process. [ICDM2015](https://dblp.org/db/conf/icdm/icdm2015.html#conf/icdm/XuanLZXL15): 489-498
- ![](https://dblp.org/img/n.png)

\[c29\]
[Minqi Li](https://dblp.org/pid/159/1126.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xiangjian He](https://dblp.org/pid/75/2122.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Face hallucination based on nonparametric Bayesian learning. [ICIP2015](https://dblp.org/db/conf/icip/icip2015.html#conf/icip/LiXH15): 986-990
- ![](https://dblp.org/img/n.png)

\[c28\]
[Fengli Zhang](https://dblp.org/pid/33/2071.html), [Jun Li](https://dblp.org/pid/116/1011.html), [Feng Li](https://dblp.org/pid/92/2954.html), [Min Xu](https://dblp.org/pid/09/0-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Xiangjian He](https://dblp.org/pid/75/2122.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Community Detection Based on Links and Node Features in Social Networks. [MMM (1)2015](https://dblp.org/db/conf/mmm/mmm2015-1.html#conf/mmm/ZhangLLXXH15): 418-429
- ![](https://dblp.org/img/n.png)

\[i7\]
[Ava Bargi](https://dblp.org/pid/64/9659.html), Richard Yi Da Xu, [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

An Adaptive Online HDP-HMM for Segmentation and Classification of Sequential Data. [CoRRabs/1503.02761](https://dblp.org/db/journals/corr/corr1503.html#journals/corr/BargiXP15) (2015)
- ![](https://dblp.org/img/n.png)

\[i6\]
[Junyu Xuan](https://dblp.org/pid/08/10768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Lu](https://dblp.org/pid/39/2936-1.html), [Guangquan Zhang](https://dblp.org/pid/37/628-1.html), Richard Yi Da Xu, [Xiangfeng Luo](https://dblp.org/pid/63/4996.html):

Infinite Author Topic Model based on Mixed Gamma-Negative Binomial Process. [CoRRabs/1503.08535](https://dblp.org/db/journals/corr/corr1503.html#journals/corr/XuanLZXL15) (2015)
- ![](https://dblp.org/img/n.png)

\[i5\]
[Junyu Xuan](https://dblp.org/pid/08/10768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Lu](https://dblp.org/pid/39/2936-1.html), [Guangquan Zhang](https://dblp.org/pid/37/628-1.html), Richard Yi Da Xu, [Xiangfeng Luo](https://dblp.org/pid/63/4996.html):

Nonparametric Relational Topic Models through Dependent Gamma Processes. [CoRRabs/1503.08542](https://dblp.org/db/journals/corr/corr1503.html#journals/corr/XuanLZXL15a) (2015)
- 2014
- ![](https://dblp.org/img/n.png)

\[c27\]
[Ava Bargi](https://dblp.org/pid/64/9659.html), Richard Yi Da Xu, [Zoubin Ghahramani](https://dblp.org/pid/g/ZoubinGhahramani.html), [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html):

A Non-parametric Conditional Factor Regression Model for Multi-Dimensional Input and Response. [AISTATS2014](https://dblp.org/db/conf/aistats/aistats2014.html#conf/aistats/BargiXGP14): 77-85
- ![](https://dblp.org/img/n.png)

\[c26\]
[Ava Bargi](https://dblp.org/pid/64/9659.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

An Infinite Adaptive Online Learning Model for Segmentation and Classification of Streaming Data. [ICPR2014](https://dblp.org/db/conf/icpr/icpr2014.html#conf/icpr/BargiXP14): 3440-3445
- 2013
- ![](https://dblp.org/img/n.png)

\[j5\]
[Ehsan Zare Borzeshi](https://dblp.org/pid/00/10106.html), [Óscar Pérez Concha](https://dblp.org/pid/52/364.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Joint Action Segmentation and Classification by an Extended Hidden Markov Model. [IEEE Signal Process. Lett.20(12)](https://dblp.org/db/journals/spl/spl20.html#journals/spl/BorzeshiCXP13): 1207-1210 (2013)
- ![](https://dblp.org/img/n.png)

\[i4\]
[Xuhui Fan](https://dblp.org/pid/117/4874.html), [Longbing Cao](https://dblp.org/pid/14/2589.html), Richard Yi Da Xu:

Copula Mixed-Membership Stochastic Blockmodel for Intra-Subgroup Correlations. [CoRRabs/1306.2733](https://dblp.org/db/journals/corr/corr1306.html#journals/corr/FanCX13) (2013)
- ![](https://dblp.org/img/n.png)

\[i3\]
[Xuhui Fan](https://dblp.org/pid/117/4874.html), [Longbing Cao](https://dblp.org/pid/14/2589.html), Richard Yi Da Xu:

Dynamic Infinite Mixed-Membership Stochastic Blockmodel. [CoRRabs/1306.2999](https://dblp.org/db/journals/corr/corr1306.html#journals/corr/FanCX13a) (2013)
- ![](https://dblp.org/img/n.png)

\[i2\]
[Ava Bargi](https://dblp.org/pid/64/9659.html), Richard Yi Da Xu, [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A non-parametric conditional factor regression model for high-dimensional input and response. [CoRRabs/1307.0578](https://dblp.org/db/journals/corr/corr1307.html#journals/corr/BargiXP13) (2013)
- ![](https://dblp.org/img/n.png)

\[i1\]
[Xuhui Fan](https://dblp.org/pid/117/4874.html), Richard Yi Da Xu, [Longbing Cao](https://dblp.org/pid/14/2589.html), [Yin Song](https://dblp.org/pid/117/4296.html):

Learning Hidden Structures with Relational Models by Adequately Involving Rich Information in A Network. [CoRRabs/1310.1545](https://dblp.org/db/journals/corr/corr1310.html#journals/corr/FanXCS13) (2013)
- 2012
- ![](https://dblp.org/img/n.png)

\[c25\]
[Ava Bargi](https://dblp.org/pid/64/9659.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

An online HDP-HMM for joint action segmentation and classification in motion capture data. [CVPR Workshops2012](https://dblp.org/db/conf/cvpr/cvprw2012.html#conf/cvpr/BargiXP12): 1-7
- 2011
- ![](https://dblp.org/img/n.png)

\[c24\]
[Óscar Pérez Concha](https://dblp.org/pid/52/364.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Zia Moghaddam](https://dblp.org/pid/59/7804.html), [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

HMM-MIO: An enhanced hidden Markov model for action recognition. [CVPR Workshops2011](https://dblp.org/db/conf/cvpr/cvprw2011.html#conf/cvpr/ConchaXMP11): 62-69
- ![](https://dblp.org/img/n.png)

\[c23\]
[Ehsan Zare Borzeshi](https://dblp.org/pid/00/10106.html), [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

A discriminative prototype selection approach for graph embedding in human action recognition. [ICCV Workshops2011](https://dblp.org/db/conf/iccvw/iccvw2011.html#conf/iccvw/BorzeshiPX11): 1295-1301
- ![](https://dblp.org/img/n.png)

\[c22\]
[Ehsan Zare Borzeshi](https://dblp.org/pid/00/10106.html), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Automatic Human Action Recognition in Videos by Graph Embedding. [ICIAP (2)2011](https://dblp.org/db/conf/iciap/iciap2011-2.html#conf/iciap/BorzeshiXP11): 19-28
- 2010
- ![](https://dblp.org/img/n.png)

\[j4\]
Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Kemp](https://dblp.org/pid/56/8109.html)![](https://dblp.org/img/orcid-mark.12x12.png):

An iterative approach for fitting multiple connected ellipse structure to silhouette. [Pattern Recognit. Lett.31(13)](https://dblp.org/db/journals/prl/prl31.html#journals/prl/XuK10): 1860-1867 (2010)
- ![](https://dblp.org/img/n.png)

\[j3\]
Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Kemp](https://dblp.org/pid/56/8109.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Fitting Multiple Connected Ellipses to an Image Silhouette Hierarchically. [IEEE Trans. Image Process.19(7)](https://dblp.org/db/journals/tip/tip19.html#journals/tip/XuK10): 1673-1682 (2010)
- ![](https://dblp.org/img/n.png)

\[c21\]
[Óscar Pérez Concha](https://dblp.org/pid/52/364.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Robust Dimensionality Reduction for Human Action Recognition. [DICTA2010](https://dblp.org/db/conf/dicta/dicta2010.html#conf/dicta/ConchaXP10): 349-356
- ![](https://dblp.org/img/n.png)

\[c20\]
[Óscar Pérez Concha](https://dblp.org/pid/52/364.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Compressive Sensing of Time Series for Human Action Recognition. [DICTA2010](https://dblp.org/db/conf/dicta/dicta2010.html#conf/dicta/ConchaXP10a): 454-461
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2009
- ![](https://dblp.org/img/n.png)

\[c19\]
[Peter F. Summons](https://dblp.org/pid/219/9799.html), [D. Newby](https://dblp.org/pid/375/5558.html), [Rukshan Athauda](https://dblp.org/pid/99/4201.html), [Mira Park](https://dblp.org/pid/p/MiraPark.html), [P. Shaw](https://dblp.org/pid/09/8273.html), [Ilung Pranata](https://dblp.org/pid/98/10307.html), [Jesse S. Jin](https://dblp.org/pid/07/3553.html), Richard Y. D. Xu:

Design Strategy for a Scalable Virtual Pharmacy Patient. [ACIS2009](https://dblp.org/db/conf/acis/acis2009.html#conf/acis/SummonsNA0SPJX09)
- ![](https://dblp.org/img/n.png)

\[c18\]
Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Kemp](https://dblp.org/pid/56/8109.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Multiple curvature based approach to human upper body parts detection with connected ellipse model fine-tuning. [ICIP2009](https://dblp.org/db/conf/icip/icip2009.html#conf/icip/XuK09): 2577-2580
- ![](https://dblp.org/img/n.png)

\[p1\]
Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Rationale, Design and Implementation of a Computer Vision-Based Interactive E-Learning System. [Methods and Applications for Advancing Distance Education Technologies2009](https://dblp.org/db/books/collections/R2009.html#books/collections/XuJ09): 268-287
- 2008
- ![](https://dblp.org/img/n.png)

\[c17\]
Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Junbin Gao](https://dblp.org/pid/30/3983.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Antolovich](https://dblp.org/pid/22/6680.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Novel methods for high-resolution facial image capture using calibrated PTZ and static cameras. [ICME2008](https://dblp.org/db/conf/icmcs/icme2008.html#conf/icmcs/XuGA08): 45-48
- ![](https://dblp.org/img/n.png)

\[c16\]
Richard Yi Da Xu, [Joshua M. Brown](https://dblp.org/pid/69/4010.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jason M. Traish](https://dblp.org/pid/61/2861.html), [Daniel Dezwa](https://dblp.org/pid/13/1033.html):

A computer vision based camera pedestal's vertical motion control. [ICPR2008](https://dblp.org/db/conf/icpr/icpr2008.html#conf/icpr/XuBTD08): 1-4
- ![](https://dblp.org/img/n.png)

\[c15\]
Richard Yi Da Xu![](https://dblp.org/img/orcid-mark.12x12.png):

A Computer Vision based Whiteboard Capture System. [WACV2008](https://dblp.org/db/conf/wacv/wacv2008.html#conf/wacv/Xu08): 1-6
- 2007
- ![](https://dblp.org/img/n.png)

\[j2\]
Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Rationale, Design and Implementation of a Computer Vision-Based Interactive E-Learning System. [Int. J. Distance Educ. Technol.5(4)](https://dblp.org/db/journals/ijdet/ijdet5.html#journals/ijdet/XuJ07): 26-45 (2007)
- ![](https://dblp.org/img/n.png)

\[j1\]
Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Camera Control and Multimedia Interaction using Individual Object Recognition. [J. Multim.2(3)](https://dblp.org/db/journals/jmm2/jmm2.html#journals/jmm2/XuJ07): 77-85 (2007)
- ![](https://dblp.org/img/n.png)

\[c14\]
[Junbin Gao](https://dblp.org/pid/30/3983.html)![](https://dblp.org/img/orcid-mark.12x12.png), Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png):

Mixture of the Robust L1 Distributions and Its Applications. [Australian Conference on Artificial Intelligence2007](https://dblp.org/db/conf/ausai/ausai2007.html#conf/ausai/GaoX07): 26-35
- 2006
- ![](https://dblp.org/img/n.png)

\[c13\]
Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png):

A Portable and Low-Cost E-Learning Video Capture System. [ACIVS2006](https://dblp.org/db/conf/acivs/acivs2006.html#conf/acivs/Xu06): 1088-1098
- ![](https://dblp.org/img/n.png)

\[c12\]
[Christopher J. Pavlovski](https://dblp.org/pid/89/2732.html), [Stella Mitchell](https://dblp.org/pid/41/5141.html), [Braam Smith](https://dblp.org/pid/84/229.html), Richard Xu:

Error Rate in Multimodal Mobility Systems. [AMT2006](https://dblp.org/db/conf/amt/amt2006.html#conf/amt/PavlovskiMSX06): 281-284
- ![](https://dblp.org/img/n.png)

\[c11\]
Richard Yi Da Xu, [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Individual Object Interaction for Camera Control and Multimedia Synchronization. [ICASSP (5)2006](https://dblp.org/db/conf/icassp/icassp2006.html#conf/icassp/XuJ06): 481-484
- 2005
- ![](https://dblp.org/img/n.png)

\[c10\]
Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Latency Insensitive Task Scheduling for Real-Time Video Processing and Streaming. [ACIVS2005](https://dblp.org/db/conf/acivs/acivs2005.html#conf/acivs/XuJ05): 387-394
- ![](https://dblp.org/img/n.png)

\[c9\]
Richard Y. D. Xu, [John G. Allen](https://dblp.org/pid/46/1755.html), [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Framework for Multimedia Lecture System using Real-Time Video Object Event Detection and Scripting. [EuroIMSA2005](https://dblp.org/db/conf/euroimsa/euroimsa2005.html#conf/euroimsa/XuAJ05): 349-352
- ![](https://dblp.org/img/n.png)

\[c8\]
Richard Y. D. Xu, [Jesse S. Jin](https://dblp.org/pid/07/3553.html), [John G. Allen](https://dblp.org/pid/46/1755.html):

Stream-Based Interactive Video Language Authoring Using Correlated Audiovisual Watermarking. [ICITA (2)2005](https://dblp.org/db/conf/icita/icita2005-2.html#conf/icita/XuJA05): 377-380
- ![](https://dblp.org/img/n.png)

\[c7\]
[John G. Allen](https://dblp.org/pid/46/1755.html), Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Mean Shift Object Tracking for a SIMD Computer. [ICITA (1)2005](https://dblp.org/db/conf/icita/icita2005-1.html#conf/icita/AllenXJ05): 692-697
- ![](https://dblp.org/img/n.png)

\[c6\]
Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Scheduling Latency Insensitive Computer Vision Tasks. [ISPA2005](https://dblp.org/db/conf/ispa/ispa2005.html#conf/ispa/XuJ05): 1089-1100
- ![](https://dblp.org/img/n.png)

\[c5\]
Richard Y. D. Xu![](https://dblp.org/img/orcid-mark.12x12.png), [Jesse S. Jin](https://dblp.org/pid/07/3553.html), [John G. Allen](https://dblp.org/pid/46/1755.html):

Framework for Script Based Virtual Directing and Multimedia Authoring in Live Video Streaming. [MMM2005](https://dblp.org/db/conf/mmm/mmm2005.html#conf/mmm/XuJA05): 427-432
- ![](https://dblp.org/img/n.png)

\[c4\]
[John G. Allen](https://dblp.org/pid/46/1755.html), Richard Y. D. Xu, [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Dependence Testing and Vectorization of Multimedia Agents. [VISION2005](https://dblp.org/db/conf/vision/vision2005.html#conf/vision/AllenXJ05): 40-46
- 2003
- ![](https://dblp.org/img/n.png)

\[c3\]
[John G. Allen](https://dblp.org/pid/46/1755.html), Richard Y. D. Xu, [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Tracking Using CamShift Algorithm and Multiple Quantized Feature Spaces. [VIP2003](https://dblp.org/db/conf/vip/vip2003.html#conf/vip/AllenXJ03): 3-7
- ![](https://dblp.org/img/n.png)

\[c2\]
Richard Y. D. Xu, [John G. Allen](https://dblp.org/pid/46/1755.html), [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Robust Real-Time Tracking of Non-Rigid Objects. [VIP2003](https://dblp.org/db/conf/vip/vip2003.html#conf/vip/XuAJ03): 95-98
- 2002
- ![](https://dblp.org/img/n.png)

\[c1\]
Richard Y. D. Xu, [Ruiyi Wang](https://dblp.org/pid/96/158.html), [Nandan Parameswaran](https://dblp.org/pid/p/NandanParameswaran.html), [Jesse S. Jin](https://dblp.org/pid/07/3553.html):

Media Streaming Synchronisation and Video Interaction: A Survey. [VIP2002](https://dblp.org/db/conf/vip/vip2002.html#conf/vip/XuWPJ02): 113-116
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/38/3064.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[John G. Allen](https://dblp.org/pid/46/1755.html)

[\[c9\]](https://dblp.org/pid/38/3064.html#c9) [\[c8\]](https://dblp.org/pid/38/3064.html#c8) [\[c7\]](https://dblp.org/pid/38/3064.html#c7) [\[c5\]](https://dblp.org/pid/38/3064.html#c5) [\[c4\]](https://dblp.org/pid/38/3064.html#c4) [\[c3\]](https://dblp.org/pid/38/3064.html#c3) [\[c2\]](https://dblp.org/pid/38/3064.html#c2)

[2](https://dblp.org/pid/38/3064.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Michael Antolovich](https://dblp.org/pid/22/6680.html)

[\[c17\]](https://dblp.org/pid/38/3064.html#c17)

[3](https://dblp.org/pid/38/3064.html?view=joint&param=3 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=2)

[Anton Arkhipov](https://dblp.org/pid/155/3493.html)

[\[j31\]](https://dblp.org/pid/38/3064.html#j31)

[4](https://dblp.org/pid/38/3064.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Rukshan Athauda](https://dblp.org/pid/99/4201.html)

[\[c19\]](https://dblp.org/pid/38/3064.html#c19)

[5](https://dblp.org/pid/38/3064.html?view=joint&param=5 "show joint publications")

[![6](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=6)

[Lamiae Azizi](https://dblp.org/pid/155/3944.html)

[\[j41\]](https://dblp.org/pid/38/3064.html#j41) [\[c56\]](https://dblp.org/pid/38/3064.html#c56) [\[i18\]](https://dblp.org/pid/38/3064.html#i18)

[6](https://dblp.org/pid/38/3064.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Liang Bai 0001](https://dblp.org/pid/91/6504-1.html)

[\[c67\]](https://dblp.org/pid/38/3064.html#c67) [\[c66\]](https://dblp.org/pid/38/3064.html#c66) [\[c61\]](https://dblp.org/pid/38/3064.html#c61)

[7](https://dblp.org/pid/38/3064.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Ava Bargi](https://dblp.org/pid/64/9659.html)

[\[j19\]](https://dblp.org/pid/38/3064.html#j19) [\[i7\]](https://dblp.org/pid/38/3064.html#i7) [\[c27\]](https://dblp.org/pid/38/3064.html#c27) [\[c26\]](https://dblp.org/pid/38/3064.html#c26) [\[i2\]](https://dblp.org/pid/38/3064.html#i2) [\[c25\]](https://dblp.org/pid/38/3064.html#c25)

[8](https://dblp.org/pid/38/3064.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Wei Bi](https://dblp.org/pid/38/1163.html)

[\[c67\]](https://dblp.org/pid/38/3064.html#c67)

[9](https://dblp.org/pid/38/3064.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Wei Bian](https://dblp.org/pid/77/3270.html)

[\[i14\]](https://dblp.org/pid/38/3064.html#i14) [\[j9\]](https://dblp.org/pid/38/3064.html#j9) [\[c34\]](https://dblp.org/pid/38/3064.html#c34) [\[c32\]](https://dblp.org/pid/38/3064.html#c32) [\[j7\]](https://dblp.org/pid/38/3064.html#j7)

[10](https://dblp.org/pid/38/3064.html?view=joint&param=10 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=2)

[Yazan N. Billeh](https://dblp.org/pid/166/8634.html)

[\[j31\]](https://dblp.org/pid/38/3064.html#j31)

[11](https://dblp.org/pid/38/3064.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Ehsan Zare Borzeshi](https://dblp.org/pid/00/10106.html)

[\[j5\]](https://dblp.org/pid/38/3064.html#j5) [\[c23\]](https://dblp.org/pid/38/3064.html#c23) [\[c22\]](https://dblp.org/pid/38/3064.html#c22)

[12](https://dblp.org/pid/38/3064.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Joshua M. Brown](https://dblp.org/pid/69/4010.html)

[\[c16\]](https://dblp.org/pid/38/3064.html#c16)

[13](https://dblp.org/pid/38/3064.html?view=joint&param=13 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=2)

[Binghuang Cai](https://dblp.org/pid/31/1412.html)

[\[j31\]](https://dblp.org/pid/38/3064.html#j31)

[14](https://dblp.org/pid/38/3064.html?view=joint&param=14 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=2)

[Nicholas Cain](https://dblp.org/pid/124/5187.html)

[\[j31\]](https://dblp.org/pid/38/3064.html#j31)

[15](https://dblp.org/pid/38/3064.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Longbing Cao](https://dblp.org/pid/14/2589.html)

[\[j14\]](https://dblp.org/pid/38/3064.html#j14) [\[c31\]](https://dblp.org/pid/38/3064.html#c31) [\[j6\]](https://dblp.org/pid/38/3064.html#j6) [\[i4\]](https://dblp.org/pid/38/3064.html#i4) [\[i3\]](https://dblp.org/pid/38/3064.html#i3) [\[i1\]](https://dblp.org/pid/38/3064.html#i1)

[16](https://dblp.org/pid/38/3064.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Qimeng Cao](https://dblp.org/pid/356/9490.html)

[\[c62\]](https://dblp.org/pid/38/3064.html#c62)

[17](https://dblp.org/pid/38/3064.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xiaofeng Cao 0002](https://dblp.org/pid/117/3982-2.html)

[\[c65\]](https://dblp.org/pid/38/3064.html#c65) [\[i34\]](https://dblp.org/pid/38/3064.html#i34)

[18](https://dblp.org/pid/38/3064.html?view=joint&param=18 "show joint publications")

[![6](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=6)

[Jennifer So-Kuen Chan](https://dblp.org/pid/09/4557.html)

aka: Jennifer S. K. Chan

[\[j41\]](https://dblp.org/pid/38/3064.html#j41) [\[c56\]](https://dblp.org/pid/38/3064.html#c56) [\[i18\]](https://dblp.org/pid/38/3064.html#i18)

[19](https://dblp.org/pid/38/3064.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Fang Chen 0001](https://dblp.org/pid/52/488-1.html)

[\[c47\]](https://dblp.org/pid/38/3064.html#c47)

[20](https://dblp.org/pid/38/3064.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Haoyu Chen](https://dblp.org/pid/146/8170.html)

[\[j21\]](https://dblp.org/pid/38/3064.html#j21)

[21](https://dblp.org/pid/38/3064.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Ling Chen 0006](https://dblp.org/pid/17/1237-6.html)

[\[c60\]](https://dblp.org/pid/38/3064.html#c60) [\[i26\]](https://dblp.org/pid/38/3064.html#i26)

[22](https://dblp.org/pid/38/3064.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yilan Chen 0002](https://dblp.org/pid/167/6638-2.html)

[\[j46\]](https://dblp.org/pid/38/3064.html#j46) [\[i30\]](https://dblp.org/pid/38/3064.html#i30)

[23](https://dblp.org/pid/38/3064.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yufei Chen 0002](https://dblp.org/pid/79/4489-2.html)

[\[j17\]](https://dblp.org/pid/38/3064.html#j17)

[24](https://dblp.org/pid/38/3064.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yujun Chen](https://dblp.org/pid/57/6294.html)

[\[c62\]](https://dblp.org/pid/38/3064.html#c62)

[25](https://dblp.org/pid/38/3064.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Adriel Cheng](https://dblp.org/pid/24/6615.html)

[\[j47\]](https://dblp.org/pid/38/3064.html#j47) [\[j44\]](https://dblp.org/pid/38/3064.html#j44) [\[j39\]](https://dblp.org/pid/38/3064.html#j39) [\[c35\]](https://dblp.org/pid/38/3064.html#c35)

[26](https://dblp.org/pid/38/3064.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Qingqing Cheng](https://dblp.org/pid/58/7703.html)

[\[j42\]](https://dblp.org/pid/38/3064.html#j42) [\[j35\]](https://dblp.org/pid/38/3064.html#j35) [\[c50\]](https://dblp.org/pid/38/3064.html#c50) [\[c49\]](https://dblp.org/pid/38/3064.html#c49) [\[c40\]](https://dblp.org/pid/38/3064.html#c40)

[27](https://dblp.org/pid/38/3064.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Madeleine Cochrane](https://dblp.org/pid/226/6263.html)

[\[c43\]](https://dblp.org/pid/38/3064.html#c43)

[28](https://dblp.org/pid/38/3064.html?view=joint&param=28 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=2)

[Kael Dai](https://dblp.org/pid/269/0476.html)

[\[j31\]](https://dblp.org/pid/38/3064.html#j31)

[29](https://dblp.org/pid/38/3064.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Chen Deng](https://dblp.org/pid/22/9348.html)

[\[c51\]](https://dblp.org/pid/38/3064.html#c51) [\[c48\]](https://dblp.org/pid/38/3064.html#c48) [\[i19\]](https://dblp.org/pid/38/3064.html#i19)

[30](https://dblp.org/pid/38/3064.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Chenwei Deng](https://dblp.org/pid/73/8538.html)

[\[j13\]](https://dblp.org/pid/38/3064.html#j13) [\[j10\]](https://dblp.org/pid/38/3064.html#j10)

[31](https://dblp.org/pid/38/3064.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Daniel Dezwa](https://dblp.org/pid/13/1033.html)

[\[c16\]](https://dblp.org/pid/38/3064.html#c16)

[32](https://dblp.org/pid/38/3064.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yaohong Ding](https://dblp.org/pid/313/1192.html)

[\[i29\]](https://dblp.org/pid/38/3064.html#i29)

[33](https://dblp.org/pid/38/3064.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Weitao Du](https://dblp.org/pid/17/10015.html)

[\[c60\]](https://dblp.org/pid/38/3064.html#c60) [\[c54\]](https://dblp.org/pid/38/3064.html#c54) [\[i26\]](https://dblp.org/pid/38/3064.html#i26) [\[c52\]](https://dblp.org/pid/38/3064.html#c52) [\[i17\]](https://dblp.org/pid/38/3064.html#i17) [\[i15\]](https://dblp.org/pid/38/3064.html#i15) [\[i13\]](https://dblp.org/pid/38/3064.html#i13)

[34](https://dblp.org/pid/38/3064.html?view=joint&param=34 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=2)

[Gaute T. Einevoll](https://dblp.org/pid/70/3700.html)

[\[j31\]](https://dblp.org/pid/38/3064.html#j31)

[35](https://dblp.org/pid/38/3064.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xuhui Fan 0001](https://dblp.org/pid/117/4874.html)

[\[j32\]](https://dblp.org/pid/38/3064.html#j32) [\[j28\]](https://dblp.org/pid/38/3064.html#j28) [\[j27\]](https://dblp.org/pid/38/3064.html#j27) [\[j14\]](https://dblp.org/pid/38/3064.html#j14) [\[c31\]](https://dblp.org/pid/38/3064.html#c31) [\[j6\]](https://dblp.org/pid/38/3064.html#j6) [\[i4\]](https://dblp.org/pid/38/3064.html#i4) [\[i3\]](https://dblp.org/pid/38/3064.html#i3) [\[i1\]](https://dblp.org/pid/38/3064.html#i1)

[36](https://dblp.org/pid/38/3064.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Gengfa Fang](https://dblp.org/pid/50/6377.html)

[\[c36\]](https://dblp.org/pid/38/3064.html#c36)

[37](https://dblp.org/pid/38/3064.html?view=joint&param=37 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=4)

[Jian Fang](https://dblp.org/pid/29/3425.html)

[\[j45\]](https://dblp.org/pid/38/3064.html#j45)

[38](https://dblp.org/pid/38/3064.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xiang Feng](https://dblp.org/pid/19/3734.html)

[\[j23\]](https://dblp.org/pid/38/3064.html#j23) [\[j22\]](https://dblp.org/pid/38/3064.html#j22) [\[j21\]](https://dblp.org/pid/38/3064.html#j21)

[39](https://dblp.org/pid/38/3064.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Sam Ferguson](https://dblp.org/pid/228/5939.html)

[\[c51\]](https://dblp.org/pid/38/3064.html#c51)

[40](https://dblp.org/pid/38/3064.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Karl J. Friston](https://dblp.org/pid/92/848.html)

[\[j40\]](https://dblp.org/pid/38/3064.html#j40)

[41](https://dblp.org/pid/38/3064.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Hamido Fujita](https://dblp.org/pid/49/6628.html)

[\[j17\]](https://dblp.org/pid/38/3064.html#j17)

[42](https://dblp.org/pid/38/3064.html?view=joint&param=42 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=4)

[Huilong Gai](https://dblp.org/pid/321/7744.html)

[\[j45\]](https://dblp.org/pid/38/3064.html#j45)

[43](https://dblp.org/pid/38/3064.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Junbin Gao](https://dblp.org/pid/30/3983.html)

[\[c17\]](https://dblp.org/pid/38/3064.html#c17) [\[c14\]](https://dblp.org/pid/38/3064.html#c14)

[44](https://dblp.org/pid/38/3064.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Zoubin Ghahramani](https://dblp.org/pid/g/ZoubinGhahramani.html)

[\[c27\]](https://dblp.org/pid/38/3064.html#c27)

[45](https://dblp.org/pid/38/3064.html?view=joint&param=45 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=2)

[Sergey L. Gratiy](https://dblp.org/pid/155/7888.html)

[\[j31\]](https://dblp.org/pid/38/3064.html#j31)

[46](https://dblp.org/pid/38/3064.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jingcai Guo](https://dblp.org/pid/192/7270.html)

[\[c65\]](https://dblp.org/pid/38/3064.html#c65) [\[i34\]](https://dblp.org/pid/38/3064.html#i34) [\[i28\]](https://dblp.org/pid/38/3064.html#i28)

[47](https://dblp.org/pid/38/3064.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Song Guo 0001](https://dblp.org/pid/01/267-1.html)

[\[c65\]](https://dblp.org/pid/38/3064.html#c65) [\[i34\]](https://dblp.org/pid/38/3064.html#i34) [\[i29\]](https://dblp.org/pid/38/3064.html#i29) [\[i28\]](https://dblp.org/pid/38/3064.html#i28)

[48](https://dblp.org/pid/38/3064.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yike Guo](https://dblp.org/pid/g/YikeGuo.html)

[\[j40\]](https://dblp.org/pid/38/3064.html#j40) [\[c61\]](https://dblp.org/pid/38/3064.html#c61)

[49](https://dblp.org/pid/38/3064.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Wei He 0001](https://dblp.org/pid/20/6417-1.html)

[\[j25\]](https://dblp.org/pid/38/3064.html#j25)

[50](https://dblp.org/pid/38/3064.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xiangjian He](https://dblp.org/pid/75/2122.html)

[\[c29\]](https://dblp.org/pid/38/3064.html#c29) [\[c28\]](https://dblp.org/pid/38/3064.html#c28)

[51](https://dblp.org/pid/38/3064.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Mark Hedley](https://dblp.org/pid/14/4985.html)

[\[c45\]](https://dblp.org/pid/38/3064.html#c45)

[52](https://dblp.org/pid/38/3064.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Timothy Heyes](https://dblp.org/pid/323/2133.html)

[\[j39\]](https://dblp.org/pid/38/3064.html#j39)

[53](https://dblp.org/pid/38/3064.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Congzhentao Huang](https://dblp.org/pid/258/0557.html)

[\[j37\]](https://dblp.org/pid/38/3064.html#j37) [\[j34\]](https://dblp.org/pid/38/3064.html#j34) [\[c55\]](https://dblp.org/pid/38/3064.html#c55) [\[i27\]](https://dblp.org/pid/38/3064.html#i27) [\[i24\]](https://dblp.org/pid/38/3064.html#i24) [\[c53\]](https://dblp.org/pid/38/3064.html#c53) [\[c51\]](https://dblp.org/pid/38/3064.html#c51) [\[c48\]](https://dblp.org/pid/38/3064.html#c48) [\[i19\]](https://dblp.org/pid/38/3064.html#i19) [\[i16\]](https://dblp.org/pid/38/3064.html#i16)

[54](https://dblp.org/pid/38/3064.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Wanming Huang](https://dblp.org/pid/92/7710.html)

[\[j48\]](https://dblp.org/pid/38/3064.html#j48) [\[c46\]](https://dblp.org/pid/38/3064.html#c46) [\[c42\]](https://dblp.org/pid/38/3064.html#c42) [\[c41\]](https://dblp.org/pid/38/3064.html#c41)

[55](https://dblp.org/pid/38/3064.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Wei Huang 0034](https://dblp.org/pid/81/6685-34.html)

[\[j46\]](https://dblp.org/pid/38/3064.html#j46) [\[c60\]](https://dblp.org/pid/38/3064.html#c60) [\[i30\]](https://dblp.org/pid/38/3064.html#i30) [\[j33\]](https://dblp.org/pid/38/3064.html#j33) [\[c54\]](https://dblp.org/pid/38/3064.html#c54) [\[i26\]](https://dblp.org/pid/38/3064.html#i26) [\[c52\]](https://dblp.org/pid/38/3064.html#c52) [\[i17\]](https://dblp.org/pid/38/3064.html#i17) [\[i15\]](https://dblp.org/pid/38/3064.html#i15) [\[i13\]](https://dblp.org/pid/38/3064.html#i13) [\[i12\]](https://dblp.org/pid/38/3064.html#i12)

[56](https://dblp.org/pid/38/3064.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yi Huang 0023](https://dblp.org/pid/15/6040-23.html)

[\[j47\]](https://dblp.org/pid/38/3064.html#j47) [\[j44\]](https://dblp.org/pid/38/3064.html#j44) [\[j39\]](https://dblp.org/pid/38/3064.html#j39) [\[c35\]](https://dblp.org/pid/38/3064.html#c35)

[57](https://dblp.org/pid/38/3064.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Sabine Van Huffel](https://dblp.org/pid/60/5071.html)

[\[j32\]](https://dblp.org/pid/38/3064.html#j32) [\[j28\]](https://dblp.org/pid/38/3064.html#j28) [\[j27\]](https://dblp.org/pid/38/3064.html#j27)

[58](https://dblp.org/pid/38/3064.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Shuai Jiang](https://dblp.org/pid/45/5080.html)

[\[j37\]](https://dblp.org/pid/38/3064.html#j37) [\[j36\]](https://dblp.org/pid/38/3064.html#j36) [\[j34\]](https://dblp.org/pid/38/3064.html#j34) [\[c55\]](https://dblp.org/pid/38/3064.html#c55) [\[i27\]](https://dblp.org/pid/38/3064.html#i27) [\[i24\]](https://dblp.org/pid/38/3064.html#i24) [\[c53\]](https://dblp.org/pid/38/3064.html#c53) [\[c51\]](https://dblp.org/pid/38/3064.html#c51) [\[c48\]](https://dblp.org/pid/38/3064.html#c48) [\[c46\]](https://dblp.org/pid/38/3064.html#c46) [\[i19\]](https://dblp.org/pid/38/3064.html#i19) [\[i16\]](https://dblp.org/pid/38/3064.html#i16) [\[j26\]](https://dblp.org/pid/38/3064.html#j26) [\[i11\]](https://dblp.org/pid/38/3064.html#i11) [\[i9\]](https://dblp.org/pid/38/3064.html#i9)

[59](https://dblp.org/pid/38/3064.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jesse S. Jin](https://dblp.org/pid/07/3553.html)

[\[c19\]](https://dblp.org/pid/38/3064.html#c19) [\[p1\]](https://dblp.org/pid/38/3064.html#p1) [\[j2\]](https://dblp.org/pid/38/3064.html#j2) [\[j1\]](https://dblp.org/pid/38/3064.html#j1) [\[c11\]](https://dblp.org/pid/38/3064.html#c11) [\[c10\]](https://dblp.org/pid/38/3064.html#c10) [\[c9\]](https://dblp.org/pid/38/3064.html#c9) [\[c8\]](https://dblp.org/pid/38/3064.html#c8) [\[c7\]](https://dblp.org/pid/38/3064.html#c7) [\[c6\]](https://dblp.org/pid/38/3064.html#c6) [\[c5\]](https://dblp.org/pid/38/3064.html#c5) [\[c4\]](https://dblp.org/pid/38/3064.html#c4) [\[c3\]](https://dblp.org/pid/38/3064.html#c3) [\[c2\]](https://dblp.org/pid/38/3064.html#c2) [\[c1\]](https://dblp.org/pid/38/3064.html#c1)

[60](https://dblp.org/pid/38/3064.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Junfeng Jing](https://dblp.org/pid/115/5261.html)

[\[j29\]](https://dblp.org/pid/38/3064.html#j29)

[61](https://dblp.org/pid/38/3064.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Guillaume Jourjon](https://dblp.org/pid/51/2666.html)

[\[j47\]](https://dblp.org/pid/38/3064.html#j47) [\[j44\]](https://dblp.org/pid/38/3064.html#j44) [\[j39\]](https://dblp.org/pid/38/3064.html#j39) [\[c35\]](https://dblp.org/pid/38/3064.html#c35)

[62](https://dblp.org/pid/38/3064.html?view=joint&param=62 "show joint publications")

[Michael Kemp](https://dblp.org/pid/56/8109.html)

[\[j8\]](https://dblp.org/pid/38/3064.html#j8) [\[j4\]](https://dblp.org/pid/38/3064.html#j4) [\[j3\]](https://dblp.org/pid/38/3064.html#j3) [\[c18\]](https://dblp.org/pid/38/3064.html#c18)

[63](https://dblp.org/pid/38/3064.html?view=joint&param=63 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=2)

[Christof Koch](https://dblp.org/pid/71/4603.html)

[\[j31\]](https://dblp.org/pid/38/3064.html#j31)

[64](https://dblp.org/pid/38/3064.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Caoyuan Li](https://dblp.org/pid/157/8323.html)

[\[i32\]](https://dblp.org/pid/38/3064.html#i32) [\[j32\]](https://dblp.org/pid/38/3064.html#j32) [\[j28\]](https://dblp.org/pid/38/3064.html#j28) [\[c44\]](https://dblp.org/pid/38/3064.html#c44) [\[j27\]](https://dblp.org/pid/38/3064.html#j27) [\[c37\]](https://dblp.org/pid/38/3064.html#c37)

[65](https://dblp.org/pid/38/3064.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Feng Li](https://dblp.org/pid/92/2954.html)

[\[c28\]](https://dblp.org/pid/38/3064.html#c28)

[66](https://dblp.org/pid/38/3064.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Guo Li 0002](https://dblp.org/pid/35/1964-2.html)

[\[c67\]](https://dblp.org/pid/38/3064.html#c67)

[67](https://dblp.org/pid/38/3064.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Haotian Li](https://dblp.org/pid/135/9708.html)

[\[j49\]](https://dblp.org/pid/38/3064.html#j49) [\[i33\]](https://dblp.org/pid/38/3064.html#i33) [\[i31\]](https://dblp.org/pid/38/3064.html#i31)

[68](https://dblp.org/pid/38/3064.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jiatong Li 0004](https://dblp.org/pid/19/11348-4.html)

[\[j13\]](https://dblp.org/pid/38/3064.html#j13) [\[j10\]](https://dblp.org/pid/38/3064.html#j10)

[69](https://dblp.org/pid/38/3064.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jun Li](https://dblp.org/pid/116/1011.html)

[\[c28\]](https://dblp.org/pid/38/3064.html#c28)

[70](https://dblp.org/pid/38/3064.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jun Li 0033](https://dblp.org/pid/116/1011-33.html)

[\[j24\]](https://dblp.org/pid/38/3064.html#j24)

[71](https://dblp.org/pid/38/3064.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Kan Li 0001](https://dblp.org/pid/21/2083-1.html)

[\[j36\]](https://dblp.org/pid/38/3064.html#j36) [\[j30\]](https://dblp.org/pid/38/3064.html#j30) [\[c53\]](https://dblp.org/pid/38/3064.html#c53) [\[j26\]](https://dblp.org/pid/38/3064.html#j26) [\[i11\]](https://dblp.org/pid/38/3064.html#i11) [\[i9\]](https://dblp.org/pid/38/3064.html#i9)

[72](https://dblp.org/pid/38/3064.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Ling Li 0010](https://dblp.org/pid/92/5001-10.html)

[\[j40\]](https://dblp.org/pid/38/3064.html#j40)

[73](https://dblp.org/pid/38/3064.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Miaoge Li](https://dblp.org/pid/330/3622.html)

[\[c65\]](https://dblp.org/pid/38/3064.html#c65) [\[i34\]](https://dblp.org/pid/38/3064.html#i34)

[74](https://dblp.org/pid/38/3064.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Minqi Li](https://dblp.org/pid/159/1126.html)

[\[j29\]](https://dblp.org/pid/38/3064.html#j29) [\[c29\]](https://dblp.org/pid/38/3064.html#c29)

[75](https://dblp.org/pid/38/3064.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Pengfei Li](https://dblp.org/pid/10/1749.html)

[\[j23\]](https://dblp.org/pid/38/3064.html#j23) [\[j21\]](https://dblp.org/pid/38/3064.html#j21)

[76](https://dblp.org/pid/38/3064.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Qiang Li 0024](https://dblp.org/pid/72/872-24.html)

[\[c34\]](https://dblp.org/pid/38/3064.html#c34)

[77](https://dblp.org/pid/38/3064.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yang Li 0082](https://dblp.org/pid/37/4190-82.html)

[\[j34\]](https://dblp.org/pid/38/3064.html#j34) [\[j30\]](https://dblp.org/pid/38/3064.html#j30) [\[c53\]](https://dblp.org/pid/38/3064.html#c53) [\[c51\]](https://dblp.org/pid/38/3064.html#c51) [\[c48\]](https://dblp.org/pid/38/3064.html#c48) [\[i19\]](https://dblp.org/pid/38/3064.html#i19) [\[i16\]](https://dblp.org/pid/38/3064.html#i16)

[78](https://dblp.org/pid/38/3064.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yayong Li](https://dblp.org/pid/187/5915.html)

[\[c60\]](https://dblp.org/pid/38/3064.html#c60) [\[i26\]](https://dblp.org/pid/38/3064.html#i26)

[79](https://dblp.org/pid/38/3064.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Ying Li 0039](https://dblp.org/pid/22/1805-39.html)

[\[j47\]](https://dblp.org/pid/38/3064.html#j47) [\[j44\]](https://dblp.org/pid/38/3064.html#j44) [\[j39\]](https://dblp.org/pid/38/3064.html#j39) [\[c35\]](https://dblp.org/pid/38/3064.html#c35)

[80](https://dblp.org/pid/38/3064.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Zhidong Li](https://dblp.org/pid/10/6710.html)

[\[c47\]](https://dblp.org/pid/38/3064.html#c47)

[81](https://dblp.org/pid/38/3064.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xuan Liang](https://dblp.org/pid/119/7993.html)

[\[c46\]](https://dblp.org/pid/38/3064.html#c46)

[82](https://dblp.org/pid/38/3064.html?view=joint&param=82 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=3)

[Albert Lin](https://dblp.org/pid/32/3460.html)

[\[c59\]](https://dblp.org/pid/38/3064.html#c59)

[83](https://dblp.org/pid/38/3064.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Hongzhan Lin 0001](https://dblp.org/pid/292/1751-1.html)

[\[c67\]](https://dblp.org/pid/38/3064.html#c67) [\[c66\]](https://dblp.org/pid/38/3064.html#c66)

[84](https://dblp.org/pid/38/3064.html?view=joint&param=84 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=4)

[Sidney Lin](https://dblp.org/pid/321/7255.html)

[\[j45\]](https://dblp.org/pid/38/3064.html#j45)

[85](https://dblp.org/pid/38/3064.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Chunrui Liu](https://dblp.org/pid/266/7209.html)

[\[j46\]](https://dblp.org/pid/38/3064.html#j46) [\[i30\]](https://dblp.org/pid/38/3064.html#i30) [\[i15\]](https://dblp.org/pid/38/3064.html#i15)

[86](https://dblp.org/pid/38/3064.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jingwei Liu](https://dblp.org/pid/29/4366.html)

[\[c45\]](https://dblp.org/pid/38/3064.html#c45)

[87](https://dblp.org/pid/38/3064.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Tianyu Liu](https://dblp.org/pid/134/1099.html)

[\[i30\]](https://dblp.org/pid/38/3064.html#i30)

[88](https://dblp.org/pid/38/3064.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Weidong Liu 0008](https://dblp.org/pid/92/9611-8.html)

[\[j18\]](https://dblp.org/pid/38/3064.html#j18)

[89](https://dblp.org/pid/38/3064.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yi Liu 0057](https://dblp.org/pid/97/4626-57.html)

[\[i28\]](https://dblp.org/pid/38/3064.html#i28)

[90](https://dblp.org/pid/38/3064.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Zexin Liu](https://dblp.org/pid/45/9879.html)

[\[j22\]](https://dblp.org/pid/38/3064.html#j22)

[91](https://dblp.org/pid/38/3064.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Riley Lodge](https://dblp.org/pid/245/5887.html)

[\[c43\]](https://dblp.org/pid/38/3064.html#c43)

[92](https://dblp.org/pid/38/3064.html?view=joint&param=92 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=4)

[Helen Huiru Lou](https://dblp.org/pid/421/7522.html)

[\[j45\]](https://dblp.org/pid/38/3064.html#j45)

[93](https://dblp.org/pid/38/3064.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jianfeng Lu 0003](https://dblp.org/pid/82/6187-3.html)

[\[j11\]](https://dblp.org/pid/38/3064.html#j11) [\[c33\]](https://dblp.org/pid/38/3064.html#c33)

[94](https://dblp.org/pid/38/3064.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jie Lu 0001](https://dblp.org/pid/39/2936-1.html)

[\[j20\]](https://dblp.org/pid/38/3064.html#j20) [\[j16\]](https://dblp.org/pid/38/3064.html#j16) [\[j12\]](https://dblp.org/pid/38/3064.html#j12) [\[i8\]](https://dblp.org/pid/38/3064.html#i8) [\[c30\]](https://dblp.org/pid/38/3064.html#c30) [\[i6\]](https://dblp.org/pid/38/3064.html#i6) [\[i5\]](https://dblp.org/pid/38/3064.html#i5)

[95](https://dblp.org/pid/38/3064.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xuan Lu 0001](https://dblp.org/pid/51/3865-1.html)

[\[c33\]](https://dblp.org/pid/38/3064.html#c33)

[96](https://dblp.org/pid/38/3064.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Cheng Luo](https://dblp.org/pid/68/6443.html)

[\[c33\]](https://dblp.org/pid/38/3064.html#c33)

[97](https://dblp.org/pid/38/3064.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Ling Luo 0002](https://dblp.org/pid/00/1811-2.html)

[\[c47\]](https://dblp.org/pid/38/3064.html#c47)

[98](https://dblp.org/pid/38/3064.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xiangfeng Luo](https://dblp.org/pid/63/4996.html)

[\[c39\]](https://dblp.org/pid/38/3064.html#c39) [\[c38\]](https://dblp.org/pid/38/3064.html#c38) [\[j20\]](https://dblp.org/pid/38/3064.html#j20) [\[j18\]](https://dblp.org/pid/38/3064.html#j18) [\[j16\]](https://dblp.org/pid/38/3064.html#j16) [\[j12\]](https://dblp.org/pid/38/3064.html#j12) [\[c30\]](https://dblp.org/pid/38/3064.html#c30) [\[i6\]](https://dblp.org/pid/38/3064.html#i6) [\[i5\]](https://dblp.org/pid/38/3064.html#i5)

[99](https://dblp.org/pid/38/3064.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Chao Ma 0002](https://dblp.org/pid/79/1552-2.html)

[\[j11\]](https://dblp.org/pid/38/3064.html#j11) [\[c33\]](https://dblp.org/pid/38/3064.html#c33)

[100](https://dblp.org/pid/38/3064.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jing Ma 0004](https://dblp.org/pid/96/6129-4.html)

[\[c67\]](https://dblp.org/pid/38/3064.html#c67) [\[c66\]](https://dblp.org/pid/38/3064.html#c66)

[101](https://dblp.org/pid/38/3064.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Christos Markos](https://dblp.org/pid/197/6658.html)

[\[c58\]](https://dblp.org/pid/38/3064.html#c58)

[102](https://dblp.org/pid/38/3064.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Luke Marsh](https://dblp.org/pid/178/8796.html)

[\[c43\]](https://dblp.org/pid/38/3064.html#c43)

[103](https://dblp.org/pid/38/3064.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Lin Mei 0001](https://dblp.org/pid/84/4478-1.html)

[\[j15\]](https://dblp.org/pid/38/3064.html#j15)

[104](https://dblp.org/pid/38/3064.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Gaofeng Meng](https://dblp.org/pid/78/6915.html)

[\[c64\]](https://dblp.org/pid/38/3064.html#c64) [\[c63\]](https://dblp.org/pid/38/3064.html#c63) [\[j43\]](https://dblp.org/pid/38/3064.html#j43) [\[i25\]](https://dblp.org/pid/38/3064.html#i25) [\[i20\]](https://dblp.org/pid/38/3064.html#i20)

[105](https://dblp.org/pid/38/3064.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Kerrie L. Mengersen](https://dblp.org/pid/64/3136.html)

[\[i32\]](https://dblp.org/pid/38/3064.html#i32) [\[j32\]](https://dblp.org/pid/38/3064.html#j32) [\[j28\]](https://dblp.org/pid/38/3064.html#j28) [\[c44\]](https://dblp.org/pid/38/3064.html#c44) [\[j27\]](https://dblp.org/pid/38/3064.html#j27) [\[c37\]](https://dblp.org/pid/38/3064.html#c37)

[106](https://dblp.org/pid/38/3064.html?view=joint&param=106 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=3)

[Lu Mi](https://dblp.org/pid/185/3258.html)

[\[c59\]](https://dblp.org/pid/38/3064.html#c59)

[107](https://dblp.org/pid/38/3064.html?view=joint&param=107 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=2)

[Stefan Mihalas](https://dblp.org/pid/90/7228.html)

[\[j31\]](https://dblp.org/pid/38/3064.html#j31)

[108](https://dblp.org/pid/38/3064.html?view=joint&param=108 "show joint publications")

[![5](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=5)

[Stella Mitchell](https://dblp.org/pid/41/5141.html)

[\[c12\]](https://dblp.org/pid/38/3064.html#c12)

[109](https://dblp.org/pid/38/3064.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Zia Moghaddam](https://dblp.org/pid/59/7804.html)

[\[c24\]](https://dblp.org/pid/38/3064.html#c24)

[110](https://dblp.org/pid/38/3064.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[D. Newby](https://dblp.org/pid/375/5558.html)

[\[c19\]](https://dblp.org/pid/38/3064.html#c19)

[111](https://dblp.org/pid/38/3064.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Wei Ni 0001](https://dblp.org/pid/31/2597-1.html)

[\[c45\]](https://dblp.org/pid/38/3064.html#c45)

[112](https://dblp.org/pid/38/3064.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Shuai Niu](https://dblp.org/pid/31/5390.html)

[\[c67\]](https://dblp.org/pid/38/3064.html#c67) [\[c66\]](https://dblp.org/pid/38/3064.html#c66) [\[c61\]](https://dblp.org/pid/38/3064.html#c61)

[113](https://dblp.org/pid/38/3064.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Ian J. Oppermann](https://dblp.org/pid/132/8466.html)

[\[c46\]](https://dblp.org/pid/38/3064.html#c46) [\[c42\]](https://dblp.org/pid/38/3064.html#c42) [\[c41\]](https://dblp.org/pid/38/3064.html#c41)

[114](https://dblp.org/pid/38/3064.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Chunhong Pan](https://dblp.org/pid/26/3810.html)

[\[j43\]](https://dblp.org/pid/38/3064.html#j43)

[115](https://dblp.org/pid/38/3064.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Nandan Parameswaran](https://dblp.org/pid/p/NandanParameswaran.html)

[\[c1\]](https://dblp.org/pid/38/3064.html#c1)

[116](https://dblp.org/pid/38/3064.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Mira Park 0001](https://dblp.org/pid/p/MiraPark.html)

[\[c19\]](https://dblp.org/pid/38/3064.html#c19)

[117](https://dblp.org/pid/38/3064.html?view=joint&param=117 "show joint publications")

[![5](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=5)

[Christopher J. Pavlovski](https://dblp.org/pid/89/2732.html)

[\[c12\]](https://dblp.org/pid/38/3064.html#c12)

[118](https://dblp.org/pid/38/3064.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Andre Pearce](https://dblp.org/pid/282/9349.html)

[\[j38\]](https://dblp.org/pid/38/3064.html#j38) [\[c50\]](https://dblp.org/pid/38/3064.html#c50) [\[c45\]](https://dblp.org/pid/38/3064.html#c45)

[119](https://dblp.org/pid/38/3064.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Sen Pei](https://dblp.org/pid/129/1503.html)

[\[c64\]](https://dblp.org/pid/38/3064.html#c64) [\[i25\]](https://dblp.org/pid/38/3064.html#i25) [\[i20\]](https://dblp.org/pid/38/3064.html#i20)

[120](https://dblp.org/pid/38/3064.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Furong Peng](https://dblp.org/pid/138/8117.html)

[\[j11\]](https://dblp.org/pid/38/3064.html#j11) [\[c33\]](https://dblp.org/pid/38/3064.html#c33)

[121](https://dblp.org/pid/38/3064.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Óscar Pérez](https://dblp.org/pid/52/364.html)

aka: Óscar Pérez Concha

[\[j5\]](https://dblp.org/pid/38/3064.html#j5) [\[c24\]](https://dblp.org/pid/38/3064.html#c24) [\[c21\]](https://dblp.org/pid/38/3064.html#c21) [\[c20\]](https://dblp.org/pid/38/3064.html#c20)

[122](https://dblp.org/pid/38/3064.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Stuart W. Perry](https://dblp.org/pid/50/6281.html)

[\[j23\]](https://dblp.org/pid/38/3064.html#j23) [\[j22\]](https://dblp.org/pid/38/3064.html#j22)

[123](https://dblp.org/pid/38/3064.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Massimo Piccardi](https://dblp.org/pid/p/MassimoPiccardi.html)

[\[j19\]](https://dblp.org/pid/38/3064.html#j19) [\[i7\]](https://dblp.org/pid/38/3064.html#i7) [\[c27\]](https://dblp.org/pid/38/3064.html#c27) [\[c26\]](https://dblp.org/pid/38/3064.html#c26) [\[j5\]](https://dblp.org/pid/38/3064.html#j5) [\[i2\]](https://dblp.org/pid/38/3064.html#i2) [\[c25\]](https://dblp.org/pid/38/3064.html#c25) [\[c24\]](https://dblp.org/pid/38/3064.html#c24) [\[c23\]](https://dblp.org/pid/38/3064.html#c23) [\[c22\]](https://dblp.org/pid/38/3064.html#c22) [\[c21\]](https://dblp.org/pid/38/3064.html#c21) [\[c20\]](https://dblp.org/pid/38/3064.html#c20)

[124](https://dblp.org/pid/38/3064.html?view=joint&param=124 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=3)

[Sridhama Prakhya](https://dblp.org/pid/242/9030.html)

[\[c59\]](https://dblp.org/pid/38/3064.html#c59)

[125](https://dblp.org/pid/38/3064.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Ilung Pranata](https://dblp.org/pid/98/10307.html)

[\[c19\]](https://dblp.org/pid/38/3064.html#c19)

[126](https://dblp.org/pid/38/3064.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Maoying Qiao](https://dblp.org/pid/62/9638.html)

[\[i14\]](https://dblp.org/pid/38/3064.html#i14) [\[j9\]](https://dblp.org/pid/38/3064.html#j9) [\[c32\]](https://dblp.org/pid/38/3064.html#c32) [\[j7\]](https://dblp.org/pid/38/3064.html#j7)

[127](https://dblp.org/pid/38/3064.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Zhijie Rao](https://dblp.org/pid/351/0660.html)

[\[c65\]](https://dblp.org/pid/38/3064.html#c65)

[128](https://dblp.org/pid/38/3064.html?view=joint&param=128 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=2)

[Atle E. Rimehaug](https://dblp.org/pid/311/9849.html)

[\[j31\]](https://dblp.org/pid/38/3064.html#j31)

[129](https://dblp.org/pid/38/3064.html?view=joint&param=129 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=3)

[Aravinthan D. T. Samuel](https://dblp.org/pid/275/6920.html)

[\[c59\]](https://dblp.org/pid/38/3064.html#c59)

[130](https://dblp.org/pid/38/3064.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[J. Alfredo Sánchez 0001](https://dblp.org/pid/s/JASanchez.html)

[\[j21\]](https://dblp.org/pid/38/3064.html#j21)

[131](https://dblp.org/pid/38/3064.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Suranga Seneviratne](https://dblp.org/pid/126/2555.html)

[\[j47\]](https://dblp.org/pid/38/3064.html#j47) [\[j44\]](https://dblp.org/pid/38/3064.html#j44) [\[j39\]](https://dblp.org/pid/38/3064.html#j39) [\[c35\]](https://dblp.org/pid/38/3064.html#c35)

[132](https://dblp.org/pid/38/3064.html?view=joint&param=132 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=3)

[Nir Shavit](https://dblp.org/pid/s/NirShavit.html)

[\[c59\]](https://dblp.org/pid/38/3064.html#c59)

[133](https://dblp.org/pid/38/3064.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[P. Shaw](https://dblp.org/pid/09/8273.html)

[\[c19\]](https://dblp.org/pid/38/3064.html#c19)

[134](https://dblp.org/pid/38/3064.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Zhenguo Shi](https://dblp.org/pid/89/4115.html)

[\[j42\]](https://dblp.org/pid/38/3064.html#j42) [\[j35\]](https://dblp.org/pid/38/3064.html#j35) [\[c50\]](https://dblp.org/pid/38/3064.html#c50) [\[c49\]](https://dblp.org/pid/38/3064.html#c49) [\[c40\]](https://dblp.org/pid/38/3064.html#c40) [\[c36\]](https://dblp.org/pid/38/3064.html#c36)

[135](https://dblp.org/pid/38/3064.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Brendan Sims](https://dblp.org/pid/224/1067.html)

[\[c43\]](https://dblp.org/pid/38/3064.html#c43)

[136](https://dblp.org/pid/38/3064.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Scott A. Sisson](https://dblp.org/pid/46/8608.html)

[\[j28\]](https://dblp.org/pid/38/3064.html#j28) [\[j27\]](https://dblp.org/pid/38/3064.html#j27)

[137](https://dblp.org/pid/38/3064.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Chapman Siu](https://dblp.org/pid/222/3167.html)

[\[c57\]](https://dblp.org/pid/38/3064.html#c57) [\[i23\]](https://dblp.org/pid/38/3064.html#i23) [\[i22\]](https://dblp.org/pid/38/3064.html#i22) [\[i21\]](https://dblp.org/pid/38/3064.html#i21) [\[i10\]](https://dblp.org/pid/38/3064.html#i10)

[138](https://dblp.org/pid/38/3064.html?view=joint&param=138 "show joint publications")

[![5](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=5)

[Braam Smith](https://dblp.org/pid/84/229.html)

[\[c12\]](https://dblp.org/pid/38/3064.html#c12)

[139](https://dblp.org/pid/38/3064.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[David B. Smith 0001](https://dblp.org/pid/47/3219.html)

[\[j44\]](https://dblp.org/pid/38/3064.html#j44)

[140](https://dblp.org/pid/38/3064.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yin Song](https://dblp.org/pid/117/4296.html)

[\[j14\]](https://dblp.org/pid/38/3064.html#j14) [\[i1\]](https://dblp.org/pid/38/3064.html#i1)

[141](https://dblp.org/pid/38/3064.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yunya Song](https://dblp.org/pid/165/3067.html)

[\[c66\]](https://dblp.org/pid/38/3064.html#c66) [\[c62\]](https://dblp.org/pid/38/3064.html#c62) [\[c61\]](https://dblp.org/pid/38/3064.html#c61)

[142](https://dblp.org/pid/38/3064.html?view=joint&param=142 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=2)

[Alexander J. Stasik](https://dblp.org/pid/269/1161.html)

[\[j31\]](https://dblp.org/pid/38/3064.html#j31)

[143](https://dblp.org/pid/38/3064.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Peter F. Summons](https://dblp.org/pid/219/9799.html)

[\[c19\]](https://dblp.org/pid/38/3064.html#c19)

[144](https://dblp.org/pid/38/3064.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Changyin Sun 0001](https://dblp.org/pid/64/221.html)

[\[j25\]](https://dblp.org/pid/38/3064.html#j25)

[145](https://dblp.org/pid/38/3064.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jiaxi Sun](https://dblp.org/pid/289/6842.html)

[\[c64\]](https://dblp.org/pid/38/3064.html#c64)

[146](https://dblp.org/pid/38/3064.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Dacheng Tao](https://dblp.org/pid/46/3391.html)

[\[i14\]](https://dblp.org/pid/38/3064.html#i14) [\[j13\]](https://dblp.org/pid/38/3064.html#j13) [\[j9\]](https://dblp.org/pid/38/3064.html#j9) [\[c34\]](https://dblp.org/pid/38/3064.html#c34) [\[c32\]](https://dblp.org/pid/38/3064.html#c32) [\[j7\]](https://dblp.org/pid/38/3064.html#j7)

[147](https://dblp.org/pid/38/3064.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Qiongxing Tao](https://dblp.org/pid/255/5561.html)

[\[c38\]](https://dblp.org/pid/38/3064.html#c38)

[148](https://dblp.org/pid/38/3064.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Kanchana Thilakarathna](https://dblp.org/pid/92/10700.html)

[\[j47\]](https://dblp.org/pid/38/3064.html#j47) [\[j44\]](https://dblp.org/pid/38/3064.html#j44) [\[j39\]](https://dblp.org/pid/38/3064.html#j39) [\[c35\]](https://dblp.org/pid/38/3064.html#c35)

[149](https://dblp.org/pid/38/3064.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jason Traish](https://dblp.org/pid/302/4716.html)

[\[c57\]](https://dblp.org/pid/38/3064.html#c57) [\[i21\]](https://dblp.org/pid/38/3064.html#i21)

[150](https://dblp.org/pid/38/3064.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jason M. Traish](https://dblp.org/pid/61/2861.html)

[\[i23\]](https://dblp.org/pid/38/3064.html#i23) [\[i22\]](https://dblp.org/pid/38/3064.html#i22) [\[c51\]](https://dblp.org/pid/38/3064.html#c51) [\[c43\]](https://dblp.org/pid/38/3064.html#c43) [\[c16\]](https://dblp.org/pid/38/3064.html#c16)

[151](https://dblp.org/pid/38/3064.html?view=joint&param=151 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=3)

[Srinivas C. Turaga](https://dblp.org/pid/91/747.html)

[\[c59\]](https://dblp.org/pid/38/3064.html#c59)

[152](https://dblp.org/pid/38/3064.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Wanggen Wan](https://dblp.org/pid/83/7086.html)

[\[j23\]](https://dblp.org/pid/38/3064.html#j23) [\[j22\]](https://dblp.org/pid/38/3064.html#j22) [\[j21\]](https://dblp.org/pid/38/3064.html#j21)

[153](https://dblp.org/pid/38/3064.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Bailing Wang](https://dblp.org/pid/31/7938.html)

[\[j49\]](https://dblp.org/pid/38/3064.html#j49) [\[i33\]](https://dblp.org/pid/38/3064.html#i33) [\[i31\]](https://dblp.org/pid/38/3064.html#i31)

[154](https://dblp.org/pid/38/3064.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Dongsheng Wang](https://dblp.org/pid/21/841.html)

[\[c65\]](https://dblp.org/pid/38/3064.html#c65) [\[i34\]](https://dblp.org/pid/38/3064.html#i34)

[155](https://dblp.org/pid/38/3064.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Hao Wang 0097](https://dblp.org/pid/181/2812-97.html)

[\[c39\]](https://dblp.org/pid/38/3064.html#c39) [\[c38\]](https://dblp.org/pid/38/3064.html#c38)

[156](https://dblp.org/pid/38/3064.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Junxiao Wang](https://dblp.org/pid/221/1246.html)

[\[i29\]](https://dblp.org/pid/38/3064.html#i29)

[157](https://dblp.org/pid/38/3064.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Kai Wang 0014](https://dblp.org/pid/78/2022-14.html)

[\[j49\]](https://dblp.org/pid/38/3064.html#j49) [\[i33\]](https://dblp.org/pid/38/3064.html#i33)

[158](https://dblp.org/pid/38/3064.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Lingzhi Wang](https://dblp.org/pid/66/8430.html)

[\[i33\]](https://dblp.org/pid/38/3064.html#i33) [\[i31\]](https://dblp.org/pid/38/3064.html#i31)

[159](https://dblp.org/pid/38/3064.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Ruiyi Wang](https://dblp.org/pid/96/158.html)

[\[c1\]](https://dblp.org/pid/38/3064.html#c1)

[160](https://dblp.org/pid/38/3064.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Shuliang Wang 0001](https://dblp.org/pid/36/4791-1.html)

[\[i32\]](https://dblp.org/pid/38/3064.html#i32) [\[c44\]](https://dblp.org/pid/38/3064.html#c44)

[161](https://dblp.org/pid/38/3064.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Shuo Wang 0011](https://dblp.org/pid/63/1591-11.html)

[\[j40\]](https://dblp.org/pid/38/3064.html#j40)

[162](https://dblp.org/pid/38/3064.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xinxin Wang](https://dblp.org/pid/24/3969.html)

[\[j30\]](https://dblp.org/pid/38/3064.html#j30)

[163](https://dblp.org/pid/38/3064.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yang Wang 0002](https://dblp.org/pid/w/YangWang2.html)

[\[c47\]](https://dblp.org/pid/38/3064.html#c47)

[164](https://dblp.org/pid/38/3064.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yingchun Wang](https://dblp.org/pid/15/6511.html)

[\[i28\]](https://dblp.org/pid/38/3064.html#i28)

[165](https://dblp.org/pid/38/3064.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yongli Wang](https://dblp.org/pid/67/2851.html)

[\[j11\]](https://dblp.org/pid/38/3064.html#j11)

[166](https://dblp.org/pid/38/3064.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Youwei Wang](https://dblp.org/pid/73/4416.html)

[\[i33\]](https://dblp.org/pid/38/3064.html#i33)

[167](https://dblp.org/pid/38/3064.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Zhihua Wang 0008](https://dblp.org/pid/66/6802-8.html)

[\[c67\]](https://dblp.org/pid/38/3064.html#c67) [\[c66\]](https://dblp.org/pid/38/3064.html#c66) [\[c62\]](https://dblp.org/pid/38/3064.html#c62) [\[c61\]](https://dblp.org/pid/38/3064.html#c61)

[168](https://dblp.org/pid/38/3064.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Darren Webb](https://dblp.org/pid/36/4297.html)

[\[j47\]](https://dblp.org/pid/38/3064.html#j47) [\[j44\]](https://dblp.org/pid/38/3064.html#j44) [\[j39\]](https://dblp.org/pid/38/3064.html#j39) [\[c35\]](https://dblp.org/pid/38/3064.html#c35)

[169](https://dblp.org/pid/38/3064.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yuliang Wei](https://dblp.org/pid/173/9369.html)

[\[j49\]](https://dblp.org/pid/38/3064.html#j49) [\[i33\]](https://dblp.org/pid/38/3064.html#i33) [\[i31\]](https://dblp.org/pid/38/3064.html#i31)

[170](https://dblp.org/pid/38/3064.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Tsui-Wei Weng](https://dblp.org/pid/177/9197.html)

[\[j46\]](https://dblp.org/pid/38/3064.html#j46)

[171](https://dblp.org/pid/38/3064.html?view=joint&param=171 "show joint publications")

[![6](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=6)

[Steven Y. K. Wong](https://dblp.org/pid/260/0739.html)

[\[j41\]](https://dblp.org/pid/38/3064.html#j41) [\[c56\]](https://dblp.org/pid/38/3064.html#c56) [\[i18\]](https://dblp.org/pid/38/3064.html#i18)

[172](https://dblp.org/pid/38/3064.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Leijie Wu](https://dblp.org/pid/303/7332.html)

[\[i29\]](https://dblp.org/pid/38/3064.html#i29)

[173](https://dblp.org/pid/38/3064.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Donald C. Wunsch II](https://dblp.org/pid/w/DCWunsch.html)

aka: Donald C. Wunsch

[\[j25\]](https://dblp.org/pid/38/3064.html#j25)

[174](https://dblp.org/pid/38/3064.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Shiming Xiang](https://dblp.org/pid/81/6575.html)

[\[c64\]](https://dblp.org/pid/38/3064.html#c64) [\[c63\]](https://dblp.org/pid/38/3064.html#c63) [\[j43\]](https://dblp.org/pid/38/3064.html#j43) [\[i25\]](https://dblp.org/pid/38/3064.html#i25)

[175](https://dblp.org/pid/38/3064.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Hong-Bo Xie](https://dblp.org/pid/54/7839.html)

[\[i32\]](https://dblp.org/pid/38/3064.html#i32) [\[j32\]](https://dblp.org/pid/38/3064.html#j32) [\[j28\]](https://dblp.org/pid/38/3064.html#j28) [\[c44\]](https://dblp.org/pid/38/3064.html#c44) [\[j27\]](https://dblp.org/pid/38/3064.html#j27) [\[c37\]](https://dblp.org/pid/38/3064.html#c37)

[176](https://dblp.org/pid/38/3064.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jing Xin](https://dblp.org/pid/81/1853.html)

[\[j29\]](https://dblp.org/pid/38/3064.html#j29)

[177](https://dblp.org/pid/38/3064.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yuting Xing](https://dblp.org/pid/212/0136.html)

[\[j40\]](https://dblp.org/pid/38/3064.html#j40)

[178](https://dblp.org/pid/38/3064.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Min Xu 0001](https://dblp.org/pid/09/0-1.html)

[\[c28\]](https://dblp.org/pid/38/3064.html#c28)

[179](https://dblp.org/pid/38/3064.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Wenchao Xu 0001](https://dblp.org/pid/96/8862-1.html)

[\[i29\]](https://dblp.org/pid/38/3064.html#i29)

[180](https://dblp.org/pid/38/3064.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Zheng Xu 0001](https://dblp.org/pid/83/2535-1.html)

[\[j15\]](https://dblp.org/pid/38/3064.html#j15)

[181](https://dblp.org/pid/38/3064.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Junyu Xuan](https://dblp.org/pid/08/10768.html)

[\[j20\]](https://dblp.org/pid/38/3064.html#j20) [\[j16\]](https://dblp.org/pid/38/3064.html#j16) [\[j12\]](https://dblp.org/pid/38/3064.html#j12) [\[i8\]](https://dblp.org/pid/38/3064.html#i8) [\[c30\]](https://dblp.org/pid/38/3064.html#c30) [\[i6\]](https://dblp.org/pid/38/3064.html#i6) [\[i5\]](https://dblp.org/pid/38/3064.html#i5)

[182](https://dblp.org/pid/38/3064.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Ruirong Xue](https://dblp.org/pid/203/4373.html)

[\[j18\]](https://dblp.org/pid/38/3064.html#j18)

[183](https://dblp.org/pid/38/3064.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Junchi Yan](https://dblp.org/pid/60/7949.html)

[\[j15\]](https://dblp.org/pid/38/3064.html#j15)

[184](https://dblp.org/pid/38/3064.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jing-Yu Yang 0001](https://dblp.org/pid/65/2850-1.html)

aka: Jingyu Yang 0001

[\[j11\]](https://dblp.org/pid/38/3064.html#j11) [\[c33\]](https://dblp.org/pid/38/3064.html#c33)

[185](https://dblp.org/pid/38/3064.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[j24\]](https://dblp.org/pid/38/3064.html#j24)

[186](https://dblp.org/pid/38/3064.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xian Yang 0001](https://dblp.org/pid/25/10624-1.html)

[\[c67\]](https://dblp.org/pid/38/3064.html#c67) [\[c66\]](https://dblp.org/pid/38/3064.html#c66) [\[c62\]](https://dblp.org/pid/38/3064.html#c62) [\[j40\]](https://dblp.org/pid/38/3064.html#j40) [\[c61\]](https://dblp.org/pid/38/3064.html#c61)

[187](https://dblp.org/pid/38/3064.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jie Yin 0001](https://dblp.org/pid/97/3358-1.html)

[\[c60\]](https://dblp.org/pid/38/3064.html#c60) [\[i26\]](https://dblp.org/pid/38/3064.html#i26)

[188](https://dblp.org/pid/38/3064.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Qing Yin](https://dblp.org/pid/55/10035.html)

[\[c62\]](https://dblp.org/pid/38/3064.html#c62) [\[c61\]](https://dblp.org/pid/38/3064.html#c61)

[189](https://dblp.org/pid/38/3064.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jane You](https://dblp.org/pid/y/JaneYou.html)

[\[c34\]](https://dblp.org/pid/38/3064.html#c34)

[190](https://dblp.org/pid/38/3064.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Bin Yu](https://dblp.org/pid/27/116.html)

[\[j49\]](https://dblp.org/pid/38/3064.html#j49) [\[i33\]](https://dblp.org/pid/38/3064.html#i33)

[191](https://dblp.org/pid/38/3064.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[James Jian Qiao Yu](https://dblp.org/pid/55/10087.html)

aka: James J. Q. Yu

[\[c58\]](https://dblp.org/pid/38/3064.html#c58)

[192](https://dblp.org/pid/38/3064.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xiaodong Yue 0002](https://dblp.org/pid/36/4716-2.html)

[\[j17\]](https://dblp.org/pid/38/3064.html#j17)

[193](https://dblp.org/pid/38/3064.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yutian Zeng](https://dblp.org/pid/255/5747.html)

[\[c52\]](https://dblp.org/pid/38/3064.html#c52) [\[i13\]](https://dblp.org/pid/38/3064.html#i13)

[194](https://dblp.org/pid/38/3064.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Can Zhang](https://dblp.org/pid/35/1714.html)

[\[j48\]](https://dblp.org/pid/38/3064.html#j48)

[195](https://dblp.org/pid/38/3064.html?view=joint&param=195 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Chenghao Zhang 0003](https://dblp.org/pid/186/0078-3.html)

[\[j43\]](https://dblp.org/pid/38/3064.html#j43)

[196](https://dblp.org/pid/38/3064.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Fengli Zhang](https://dblp.org/pid/33/2071.html)

[\[c28\]](https://dblp.org/pid/38/3064.html#c28)

[197](https://dblp.org/pid/38/3064.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Guangquan Zhang 0001](https://dblp.org/pid/37/628-1.html)

[\[j20\]](https://dblp.org/pid/38/3064.html#j20) [\[j16\]](https://dblp.org/pid/38/3064.html#j16) [\[j12\]](https://dblp.org/pid/38/3064.html#j12) [\[i8\]](https://dblp.org/pid/38/3064.html#i8) [\[c30\]](https://dblp.org/pid/38/3064.html#c30) [\[i6\]](https://dblp.org/pid/38/3064.html#i6) [\[i5\]](https://dblp.org/pid/38/3064.html#i5)

[198](https://dblp.org/pid/38/3064.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jian (Andrew) Zhang](https://dblp.org/pid/07/314-a.html)

aka: J. Andrew Zhang

[\[j42\]](https://dblp.org/pid/38/3064.html#j42) [\[j38\]](https://dblp.org/pid/38/3064.html#j38) [\[j35\]](https://dblp.org/pid/38/3064.html#j35) [\[c50\]](https://dblp.org/pid/38/3064.html#c50) [\[c49\]](https://dblp.org/pid/38/3064.html#c49) [\[c45\]](https://dblp.org/pid/38/3064.html#c45) [\[c40\]](https://dblp.org/pid/38/3064.html#c40) [\[c36\]](https://dblp.org/pid/38/3064.html#c36)

[199](https://dblp.org/pid/38/3064.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jie Zhang 0076](https://dblp.org/pid/84/6889-76.html)

[\[i29\]](https://dblp.org/pid/38/3064.html#i29) [\[i28\]](https://dblp.org/pid/38/3064.html#i28)

[200](https://dblp.org/pid/38/3064.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Jun Zhang 0038](https://dblp.org/pid/29/4190-38.html)

[\[j18\]](https://dblp.org/pid/38/3064.html#j18)

[201](https://dblp.org/pid/38/3064.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Kaibing Zhang](https://dblp.org/pid/91/10256.html)

[\[j29\]](https://dblp.org/pid/38/3064.html#j29)

[202](https://dblp.org/pid/38/3064.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Miao Zhang 0022](https://dblp.org/pid/60/7041-22.html)

[\[j46\]](https://dblp.org/pid/38/3064.html#j46) [\[c60\]](https://dblp.org/pid/38/3064.html#c60)

[203](https://dblp.org/pid/38/3064.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Rui Zhang 0050](https://dblp.org/pid/60/2536-50.html)

[\[i33\]](https://dblp.org/pid/38/3064.html#i33)

[204](https://dblp.org/pid/38/3064.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Siqi Zhang](https://dblp.org/pid/55/287.html)

[\[c47\]](https://dblp.org/pid/38/3064.html#c47)

[205](https://dblp.org/pid/38/3064.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Weizhan Zhang](https://dblp.org/pid/17/6858.html)

[\[i28\]](https://dblp.org/pid/38/3064.html#i28)

[206](https://dblp.org/pid/38/3064.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xin Zhang 0093](https://dblp.org/pid/76/1584-93.html)

[\[i20\]](https://dblp.org/pid/38/3064.html#i20)

[207](https://dblp.org/pid/38/3064.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Xu Zhang](https://dblp.org/pid/98/5660.html)

[\[j48\]](https://dblp.org/pid/38/3064.html#j48)

[208](https://dblp.org/pid/38/3064.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Zhaoxiang Zhang 0001](https://dblp.org/pid/55/2285-1.html)

[\[c63\]](https://dblp.org/pid/38/3064.html#c63)

[209](https://dblp.org/pid/38/3064.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Ziyue Zhang](https://dblp.org/pid/202/8855.html)

[\[j37\]](https://dblp.org/pid/38/3064.html#j37) [\[j34\]](https://dblp.org/pid/38/3064.html#j34) [\[c55\]](https://dblp.org/pid/38/3064.html#c55) [\[i27\]](https://dblp.org/pid/38/3064.html#i27) [\[i24\]](https://dblp.org/pid/38/3064.html#i24) [\[c53\]](https://dblp.org/pid/38/3064.html#c53) [\[c51\]](https://dblp.org/pid/38/3064.html#c51) [\[c48\]](https://dblp.org/pid/38/3064.html#c48) [\[i19\]](https://dblp.org/pid/38/3064.html#i19) [\[i16\]](https://dblp.org/pid/38/3064.html#i16)

[210](https://dblp.org/pid/38/3064.html?view=joint&param=210 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Baojun Zhao](https://dblp.org/pid/84/10182.html)

[\[j13\]](https://dblp.org/pid/38/3064.html#j13) [\[j10\]](https://dblp.org/pid/38/3064.html#j10)

[211](https://dblp.org/pid/38/3064.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Yunce Zhao](https://dblp.org/pid/255/5947.html)

[\[c52\]](https://dblp.org/pid/38/3064.html#c52) [\[i13\]](https://dblp.org/pid/38/3064.html#i13)

[212](https://dblp.org/pid/38/3064.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Hao Zheng](https://dblp.org/pid/31/6916.html)

[\[j24\]](https://dblp.org/pid/38/3064.html#j24)

[213](https://dblp.org/pid/38/3064.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Kai Zhou](https://dblp.org/pid/82/1512.html)

[\[c39\]](https://dblp.org/pid/38/3064.html#c39)

[214](https://dblp.org/pid/38/3064.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Shengchao Zhou](https://dblp.org/pid/194/4326.html)

[\[c63\]](https://dblp.org/pid/38/3064.html#c63)

[215](https://dblp.org/pid/38/3064.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/38/3064.html?view=group&param=1)

[Song Zhu](https://dblp.org/pid/00/4449.html)

[\[j23\]](https://dblp.org/pid/38/3064.html#j23) [\[j22\]](https://dblp.org/pid/38/3064.html#j22)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/38/3064.html#) [\[–\]](https://dblp.org/pid/38/3064.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/38/3064.html#) [\[–\]](https://dblp.org/pid/38/3064.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/38/3064.html#) [\[–\]](https://dblp.org/pid/38/3064.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/38/3064.html#) [\[–\]](https://dblp.org/pid/38/3064.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/38/3064.html#) [\[–\]](https://dblp.org/pid/38/3064.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)