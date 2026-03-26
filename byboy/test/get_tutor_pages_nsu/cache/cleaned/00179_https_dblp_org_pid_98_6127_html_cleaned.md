> 抓取来源：https://dblp.org/pid/98/6127.html

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

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Jungong+Han%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F98%2F6127%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Jungong+Han+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F98%2F6127%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Jungong+Han+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F98%2F6127%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Jungong+Han%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F98%2F6127%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Jungong+Han+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F98%2F6127%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Jungong+Han%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F98%2F6127%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Jungong+Han%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F98%2F6127%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F98%2F6127%3E+%7D+.%0A%0A%7D)

_showing all526 records_

20022026802002: 12004: 22005: 22006: 42006: 42007: 52008: 42008: 42009: 22009: 22010: 22011: 52011: 52012: 32012: 32013: 52014: 82015: 42016: 72016: 72017: 312017: 312017: 312018: 432018: 432018: 432019: 562019: 562019: 562019: 562020: 332020: 332020: 332021: 372021: 372021: 372022: 552022: 552022: 552023: 362023: 362023: 362024: 762024: 762024: 762025: 882025: 882025: 882026: 17

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

- ![](https://dblp.org/img/add-mark.12x12.png)Guiguang Ding (139)
- ![](https://dblp.org/img/add-mark.12x12.png)Qiang Zhang 0020 (65)
- ![](https://dblp.org/img/add-mark.12x12.png)Hui Chen 0013 (54)
- ![](https://dblp.org/img/add-mark.12x12.png)Ling Shao 0001 (52)
- ![](https://dblp.org/img/add-mark.12x12.png)Zijia Lin (49)
- ![](https://dblp.org/img/add-mark.12x12.png)Yanwei Pang (46)
- ![](https://dblp.org/img/add-mark.12x12.png)Yuchen Guo (40)
- ![](https://dblp.org/img/add-mark.12x12.png)Baochang Zhang 0001 (40)
- ![](https://dblp.org/img/add-mark.12x12.png)Zhong Ji (37)
- ![](https://dblp.org/img/add-mark.12x12.png)Sicheng Zhao (30)

- _880 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (369)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0003-4361-956X (157)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (118)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Image Process. (37)
- ![](https://dblp.org/img/add-mark.12x12.png)Pattern Recognit. (31)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Circuits Syst. Video Technol. (23)
- ![](https://dblp.org/img/add-mark.12x12.png)Neurocomputing (23)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (23)
- ![](https://dblp.org/img/add-mark.12x12.png)IJCAI (21)
- ![](https://dblp.org/img/add-mark.12x12.png)AAAI (19)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (19)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Neural Networks Learn. Syst. (18)
- ![](https://dblp.org/img/add-mark.12x12.png)ECCV (11)

- _88 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (314)
- ![](https://dblp.org/img/add-mark.12x12.png)open (208)
- ![](https://dblp.org/img/add-mark.12x12.png)unavailable (3)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[j277\]
[Xiaowei Gu](https://dblp.org/pid/128/5017-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Abdulrahman Kerim](https://dblp.org/pid/291/4782.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jinghao Zhang](https://dblp.org/pid/284/0853.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Qiang Shen](https://dblp.org/pid/s/QiangShen.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peter M. Atkinson](https://dblp.org/pid/74/41.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ce Zhang](https://dblp.org/pid/97/919-5.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Self-organising explainable multi-view representation learning for remote sensing scene classification. [Appl. Soft Comput.190](https://dblp.org/db/journals/asc/asc190.html#journals/asc/GuKZHSAZ26): 114579 (2026)
- ![](https://dblp.org/img/n.png)

\[j276\]
[Bingchen Dong](https://dblp.org/pid/325/6093.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Gengshen Wu](https://dblp.org/pid/204/2949.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xia Feng](https://dblp.org/pid/67/5915.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

AMK-CDiffNet: Adaptive-multiscale K-space cold diffusion network for fast MRI reconstruction. [Expert Syst. Appl.297](https://dblp.org/db/journals/eswa/eswa297.html#journals/eswa/DongWFLH26): 129384 (2026)
- ![](https://dblp.org/img/n.png)

\[j275\]
[Xin Zhao](https://dblp.org/pid/68/2766-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liang Zheng](https://dblp.org/pid/61/7360.html), [Qiang Qiu](https://dblp.org/pid/97/360-1.html), [Yin Li](https://dblp.org/pid/49/5981.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [José Lezama](https://dblp.org/pid/151/8861.html), [Qiuhong Ke](https://dblp.org/pid/151/3574.html), [Yongchan Kwon](https://dblp.org/pid/189/2046.html), [Ruoxi Jia](https://dblp.org/pid/147/5355-1.html), Jungong Han:

Guest Editorial: Special Issue on Visual Datasets. [Int. J. Comput. Vis.134(1)](https://dblp.org/db/journals/ijcv/ijcv134.html#journals/ijcv/ZhaoZQLWLKKJH26): 19 (2026)
- ![](https://dblp.org/img/n.png)

\[j274\]
[Carlos Francisco Moreno-García](https://dblp.org/pid/150/4768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Gerardo Aragon-Camarasa](https://dblp.org/pid/69/8016.html), [Edmond S. L. Ho](https://dblp.org/pid/19/4864.html), [Paul Henderson](https://dblp.org/pid/172/1394.html), [Nicolas Pugeault](https://dblp.org/pid/35/1348.html), Jungong Han, [Sergio Escalera](https://dblp.org/pid/77/5527.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Guest Editorial: Special Issue for the British Machine Vision Conference (BMVC), 2024 (Glasgow, Scotland, UK). [Int. J. Comput. Vis.134(2)](https://dblp.org/db/journals/ijcv/ijcv134.html#journals/ijcv/MorenoGarciaAHHPHE26): 57 (2026)
- ![](https://dblp.org/img/n.png)

\[j273\]
[Feixiang Liu](https://dblp.org/pid/204/9610.html), [Yang Liu](https://dblp.org/pid/51/3710-0069.html), Jungong Han:

Unbiased max-min embedding classification for transductive few-shot learning: Clustering and classification are all you need. [Neurocomputing669](https://dblp.org/db/journals/ijon/ijon669.html#journals/ijon/Liu0H26): 132484 (2026)
- ![](https://dblp.org/img/n.png)

\[j272\]
[Jingkun Chen](https://dblp.org/pid/212/6645.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jingchao Peng](https://dblp.org/pid/287/9324.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Junde Wu](https://dblp.org/pid/39/2439.html), [Tianlu Zhang](https://dblp.org/pid/255/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thomas Bashford-Rogers](https://dblp.org/pid/54/1287.html), [Kurt Debattista](https://dblp.org/pid/29/5944.html), [Vicente Grau](https://dblp.org/pid/g/VicenteGrau.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Balancing light and shadow: Multi-modal image exposure restoration via frequency-phase-driven RGB-IR integration. [Inf. Fusion127](https://dblp.org/db/journals/inffus/inffus127.html#journals/inffus/ChenPWZBDGH26): 103901 (2026)
- ![](https://dblp.org/img/n.png)

\[j271\]
[Ao Wang](https://dblp.org/pid/87/3443.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Chen](https://dblp.org/pid/12/417-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zijia Lin](https://dblp.org/pid/78/9911.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sicheng Zhao](https://dblp.org/pid/65/10574.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png):

CAIT: Triple-Win Compression Toward High Accuracy, Fast Inference, and Favorable Transferability for ViTs. [IEEE Trans. Pattern Anal. Mach. Intell.48(2)](https://dblp.org/db/journals/pami/pami48.html#journals/pami/WangCLZHD26): 1373-1389 (2026)
- ![](https://dblp.org/img/n.png)

\[j270\]
[Ding Sheng Ong](https://dblp.org/pid/284/9241.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changjing Shang](https://dblp.org/pid/03/6446.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Shen](https://dblp.org/pid/s/QiangShen.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Fixing Background Misclassification in Few-Shot Object Detection via Product of Experts. [IEEE Trans. Pattern Anal. Mach. Intell.48(2)](https://dblp.org/db/journals/pami/pami48.html#journals/pami/OngLSDSH26): 1825-1841 (2026)
- ![](https://dblp.org/img/n.png)

\[j269\]
[Yang Yang](https://dblp.org/pid/48/450-9.html), [Nianchang Huang](https://dblp.org/pid/258/2761.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Mitigating fusion bias for RGB-D salient object detection. [Pattern Recognit.171](https://dblp.org/db/journals/pr/pr171.html#journals/pr/YangHZH26): 112135 (2026)
- ![](https://dblp.org/img/n.png)

\[j268\]
[Qi Liu](https://dblp.org/pid/95/2446.html), [Xuemei Fu](https://dblp.org/pid/204/0988.html), [Huang Zhang](https://dblp.org/pid/132/6996.html), [Long Cheng](https://dblp.org/pid/49/225-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Catarina Moreira](https://dblp.org/pid/28/10108.html), [Xin Ning](https://dblp.org/pid/28/8118-1.html), [Xiao Bai](https://dblp.org/pid/99/4833-1.html):

HybridEditDif: Text and exemplar guided image editing with diffusion models. [Pattern Recognit.172](https://dblp.org/db/journals/pr/pr172.html#journals/pr/LiuFZLHMNB26): 112510 (2026)
- ![](https://dblp.org/img/n.png)

\[j267\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html), [Jialiang Wang](https://dblp.org/pid/27/8578.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han, [Jin Huang](https://dblp.org/pid/49/2488.html):

'Knowledge and experience' for visible-infrared person re-identification. [Pattern Recognit.172](https://dblp.org/db/journals/pr/pr172.html#journals/pr/HuangWZHH26): 112553 (2026)
- ![](https://dblp.org/img/n.png)

\[j266\]
[Hanzhao Pan](https://dblp.org/pid/421/4187.html), [Gengshen Wu](https://dblp.org/pid/204/2949.html), [Yi Liu](https://dblp.org/pid/97/4626-38.html), Jungong Han:

Text-Centric multimodal sentiment analysis with asymmetric fine-tuning. [Pattern Recognit.173](https://dblp.org/db/journals/pr/pr173.html#journals/pr/PanWLH26): 112842 (2026)
- ![](https://dblp.org/img/n.png)

\[j265\]
[Huaizhou Qi](https://dblp.org/pid/413/5945.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-0069.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Lei Zhang](https://dblp.org/pid/64/5666-38.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Generative model-based mixed-semantic enhancement for transductive zero-shot learning. [Pattern Recognit.176](https://dblp.org/db/journals/pr/pr176.html#journals/pr/QiLHZ26): 113124 (2026)
- ![](https://dblp.org/img/n.png)

\[j264\]
[Jiayi Yang](https://dblp.org/pid/91/9190.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Ye](https://dblp.org/pid/09/5394-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Sun](https://dblp.org/pid/20/3535.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rui Fan](https://dblp.org/pid/03/1805-1.html), Jungong Han:

Enhancing graph learning interpretability through modulating cluster information flow. [Pattern Recognit.176](https://dblp.org/db/journals/pr/pr176.html#journals/pr/YangYSFH26): 113178 (2026)
- ![](https://dblp.org/img/n.png)

\[j263\]
[Hongsheng Zhang](https://dblp.org/pid/19/4547.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jingren Liu](https://dblp.org/pid/269/7845.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Multi-Stage Knowledge Integration of Vision-Language Models for Continual Learning. [IEEE Trans. Image Process.35](https://dblp.org/db/journals/tip/tip35.html#journals/tip/ZhangJLPH26): 615-628 (2026)
- ![](https://dblp.org/img/n.png)

\[j262\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rongshuai Wei](https://dblp.org/pid/409/7340.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jingren Liu](https://dblp.org/pid/269/7845.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Interpretable Few-Shot Image Classification via Prototypical Concept-Guided Mixture of LoRA Experts. [IEEE Trans. Image Process.35](https://dblp.org/db/journals/tip/tip35.html#journals/tip/JiWLPH26): 930-942 (2026)
- ![](https://dblp.org/img/n.png)

\[j261\]
[Bing Wang](https://dblp.org/pid/06/1909-18.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ximing Li](https://dblp.org/pid/130/1013-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changchun Li](https://dblp.org/pid/73/7819.html), [Bingrui Zhao](https://dblp.org/pid/327/1173.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Renchu Guan](https://dblp.org/pid/84/8179.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lin Yuanbo Wu](https://dblp.org/pid/65/6292-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Detecting Misinformation by Uncovering Commonsense Conflicts With LLM Workflows. [IEEE Trans. Knowl. Data Eng.38(3)](https://dblp.org/db/journals/tkde/tkde38.html#journals/tkde/WangLLZGWH26): 1589-1603 (2026)
- 2025
- ![](https://dblp.org/img/n.png)

\[j260\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chengxin Li](https://dblp.org/pid/166/6518.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaohui Dong](https://dblp.org/pid/152/7855.html), [Lei Li](https://dblp.org/pid/13/7007.html), [Dingwen Zhang](https://dblp.org/pid/150/6620.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shoukun Xu](https://dblp.org/pid/73/7832.html), Jungong Han:

Seamless Detection: Unifying Salient Object Detection and Camouflaged Object Detection. [Expert Syst. Appl.274](https://dblp.org/db/journals/eswa/eswa274.html#journals/eswa/LiuLDLZXH25): 126912 (2025)
- ![](https://dblp.org/img/n.png)

\[j259\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html), [Chengxin Li](https://dblp.org/pid/166/6518.html), [Shoukun Xu](https://dblp.org/pid/73/7832.html), Jungong Han:

Part-Whole Relational Fusion Towards Multi-Modal Scene Understanding. [Int. J. Comput. Vis.133(7)](https://dblp.org/db/journals/ijcv/ijcv133.html#journals/ijcv/LiuLXH25): 4483-4503 (2025)
- ![](https://dblp.org/img/n.png)

\[j258\]
[Haoran Duan](https://dblp.org/pid/82/4334-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shuai Shao](https://dblp.org/pid/71/8201.html), [Bing Zhai](https://dblp.org/pid/182/9111.html), [Tejal Shah](https://dblp.org/pid/142/7854.html), Jungong Han, [Rajiv Ranjan](https://dblp.org/pid/68/163-1.html):

Parameter Efficient Fine-Tuning for Multi-modal Generative Vision Models with Möbius-Inspired Transformation. [Int. J. Comput. Vis.133(7)](https://dblp.org/db/journals/ijcv/ijcv133.html#journals/ijcv/DuanSZSHR25): 4590-4603 (2025)
- ![](https://dblp.org/img/n.png)

\[j257\]
[Haoran Duan](https://dblp.org/pid/82/4334-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shuai Shao](https://dblp.org/pid/71/8201.html), [Bing Zhai](https://dblp.org/pid/182/9111.html), [Tejal Shah](https://dblp.org/pid/142/7854.html), Jungong Han, [Rajiv Ranjan](https://dblp.org/pid/68/163-1.html):

Correction: Parameter Efficient Fine-Tuning for Multi-modal Generative Vision Models with Möbius-Inspired Transformation. [Int. J. Comput. Vis.133(9)](https://dblp.org/db/journals/ijcv/ijcv133.html#journals/ijcv/DuanSZSHR25a): 6637 (2025)
- ![](https://dblp.org/img/n.png)

\[j256\]
[Yumna Zahid](https://dblp.org/pid/227/0373.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christine Zarges](https://dblp.org/pid/13/6472.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bernie Tiddeman](https://dblp.org/pid/37/5442.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Adversarial diffusion for few-shot scene adaptive video anomaly detection. [Neurocomputing614](https://dblp.org/db/journals/ijon/ijon614.html#journals/ijon/ZahidZTH25): 128796 (2025)
- ![](https://dblp.org/img/n.png)

\[j255\]
[Yu Fu](https://dblp.org/pid/09/3263-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Xiang Chang](https://dblp.org/pid/232/5246.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changrui Chen](https://dblp.org/pid/232/4719.html), [Changjing Shang](https://dblp.org/pid/03/6446.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Shen](https://dblp.org/pid/s/QiangShen.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Long-tailed recognition via key attribute learning. [Neurocomputing627](https://dblp.org/db/journals/ijon/ijon627.html#journals/ijon/FuHCCSS25): 129586 (2025)
- ![](https://dblp.org/img/n.png)

\[j254\]
[Xun Zhang](https://dblp.org/pid/18/3246.html), [Yang Liu](https://dblp.org/pid/51/3710-0069.html), Jungong Han:

Out-of-distribution detection: Sparsification meets subspace. [Neurocomputing654](https://dblp.org/db/journals/ijon/ijon654.html#journals/ijon/ZhangLH25): 131240 (2025)
- ![](https://dblp.org/img/n.png)

\[j253\]
[Shenlu Zhao](https://dblp.org/pid/300/5768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jingyi Wang](https://dblp.org/pid/18/3178.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Towards efficient RGB-T semantic segmentation via feature generative distillation strategy. [Inf. Fusion123](https://dblp.org/db/journals/inffus/inffus123.html#journals/inffus/ZhaoWZH25): 103282 (2025)
- ![](https://dblp.org/img/n.png)

\[j252\]
[Yan Zhang](https://dblp.org/pid/04/3348-135.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han:

Hierarchical and complementary experts transformer with momentum invariance for image-text retrieval. [Knowl. Based Syst.309](https://dblp.org/db/journals/kbs/kbs309.html#journals/kbs/ZhangJPH25): 112912 (2025)
- ![](https://dblp.org/img/n.png)

\[j251\]
[Mushui Liu](https://dblp.org/pid/334/2912.html), [Weijie He](https://dblp.org/pid/94/8876.html), [Ziqian Lu](https://dblp.org/pid/271/6997.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Dan](https://dblp.org/pid/156/9683.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yunlong Yu](https://dblp.org/pid/45/7404.html), [Yingming Li](https://dblp.org/pid/119/1901.html), [Xi Li](https://dblp.org/pid/46/2311-1.html), Jungong Han:

Synth-CLIP: Synthetic data make CLIP generalize better in data-limited scenarios. [Neural Networks184](https://dblp.org/db/journals/nn/nn184.html#journals/nn/LiuHLDYLLH25): 107083 (2025)
- ![](https://dblp.org/img/n.png)

\[j250\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Yuhao Dang](https://dblp.org/pid/370/3843.html), [Huaizhou Qi](https://dblp.org/pid/413/5945.html), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html):

Zero-shot sketch-based remote sensing image retrieval based on cross-modal fusion. [Neural Networks191](https://dblp.org/db/journals/nn/nn191.html#journals/nn/LiuDQHS25): 107796 (2025)
- ![](https://dblp.org/img/n.png)

\[j249\]
[Tianlu Zhang](https://dblp.org/pid/255/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kurt Debattista](https://dblp.org/pid/29/5944.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Cross-Modality Distillation for Multi-Modal Tracking. [IEEE Trans. Pattern Anal. Mach. Intell.47(7)](https://dblp.org/db/journals/pami/pami47.html#journals/pami/ZhangZDH25): 5847-5865 (2025)
- ![](https://dblp.org/img/n.png)

\[j248\]
[Junbo Yang](https://dblp.org/pid/14/7508.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Borui Hu](https://dblp.org/pid/393/7322.html), [Hanyu Li](https://dblp.org/pid/11/6652.html), [Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html), Jungong Han, [Fanglin Chen](https://dblp.org/pid/85/7057-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xuangou Wu](https://dblp.org/pid/133/0466.html):

Dynamic VAEs via semantic-aligned matching for continual zero-shot learning. [Pattern Recognit.160](https://dblp.org/db/journals/pr/pr160.html#journals/pr/YangHLLGHCW25): 111199 (2025)
- ![](https://dblp.org/img/n.png)

\[j247\]
[Shenlu Zhao](https://dblp.org/pid/300/5768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ziniu Jin](https://dblp.org/pid/396/8685.html), [Qiang Jiao](https://dblp.org/pid/166/3845.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Resolving semantic conflicts in RGB-T semantic segmentation. [Pattern Recognit.162](https://dblp.org/db/journals/pr/pr162.html#journals/pr/ZhaoJJZH25): 111398 (2025)
- ![](https://dblp.org/img/n.png)

\[j246\]
[Jiale Du](https://dblp.org/pid/241/3709.html), [Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html), Jungong Han, [Lei Zhang](https://dblp.org/pid/64/5666-38.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Zero-Shot Sketch-Based Image Retrieval with teacher-guided and student-centered cross-modal bidirectional knowledge distillation. [Pattern Recognit.164](https://dblp.org/db/journals/pr/pr164.html#journals/pr/DuLGHZ25): 111529 (2025)
- ![](https://dblp.org/img/n.png)

\[j245\]
[Shanjuan Chen](https://dblp.org/pid/387/5848.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yunlong Yu](https://dblp.org/pid/45/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yingming Li](https://dblp.org/pid/119/1901.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhao Wang](https://dblp.org/pid/86/981.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xi Li](https://dblp.org/pid/46/2311-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Multiscale Adapter Based on SAM for Remote Sensing Semantic Segmentation. [IEEE J. Sel. Top. Appl. Earth Obs. Remote. Sens.18](https://dblp.org/db/journals/staeors/staeors18.html#journals/staeors/ChenYLWLH25): 6806-6819 (2025)
- ![](https://dblp.org/img/n.png)

\[j244\]
[Penghui Niu](https://dblp.org/pid/118/3791.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Taotao Cai](https://dblp.org/pid/168/4683.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yajuan Zhang](https://dblp.org/pid/09/10185.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ping Zhang](https://dblp.org/pid/13/4682-25.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenjia Xu](https://dblp.org/pid/34/9467.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Junhua Gu](https://dblp.org/pid/26/6721.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

LG-Umer: UNet-Like Network Integrate Local-Global Feature With Novel Attention for Road Extraction From Remote Sensing Images. [IEEE J. Sel. Top. Appl. Earth Obs. Remote. Sens.18](https://dblp.org/db/journals/staeors/staeors18.html#journals/staeors/NiuCZZXGH25): 21755-21768 (2025)
- ![](https://dblp.org/img/n.png)

\[j243\]
[Amit Kumar Singh](https://dblp.org/pid/10/7647-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Stefano Berretti](https://dblp.org/pid/41/561.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Guest Editorial: Special Issue on Trends in Social Multimedia Computing: Models, Methodologies, and Applications. [IEEE Trans. Comput. Soc. Syst.12(5)](https://dblp.org/db/journals/tcss/tcss12.html#journals/tcss/SinghHB25): 3747-3750 (2025)
- ![](https://dblp.org/img/n.png)

\[j242\]
[Ziqian Lu](https://dblp.org/pid/271/6997.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mushui Liu](https://dblp.org/pid/334/2912.html), [Yunlong Yu](https://dblp.org/pid/45/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhao Wang](https://dblp.org/pid/86/981.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xi Li](https://dblp.org/pid/46/2311-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Variational Adapter: Improving CLIP in Data-Imbalanced Scenarios. [IEEE Trans. Circuits Syst. Video Technol.35(6)](https://dblp.org/db/journals/tcsv/tcsv35.html#journals/tcsv/LuLYWLH25): 5251-5264 (2025)
- ![](https://dblp.org/img/n.png)

\[j241\]
[Juexiao Feng](https://dblp.org/pid/371/4491.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuhong Yang](https://dblp.org/pid/365/8877.html), [Mengyao Lyu](https://dblp.org/pid/244/8467.html), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi-Jie Huang](https://dblp.org/pid/184/6951.html), [Yanchun Xie](https://dblp.org/pid/184/9463.html), [Yaqian Li](https://dblp.org/pid/154/1961.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Liuyu Xiang](https://dblp.org/pid/242/7959.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Toward Realistic Hierarchical Object Detection: Problem, Benchmark, and Solution. [IEEE Trans. Circuits Syst. Video Technol.35(9)](https://dblp.org/db/journals/tcsv/tcsv35.html#journals/tcsv/FengYLHHXLHXD25): 9351-9364 (2025)
- ![](https://dblp.org/img/n.png)

\[j240\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiale Du](https://dblp.org/pid/241/3709.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Relation-Aware Meta-Learning for Zero-Shot Sketch-Based Image Retrieval. [IEEE Trans. Circuits Syst. Video Technol.35(12)](https://dblp.org/db/journals/tcsv/tcsv35.html#journals/tcsv/LiuDGHS25): 12538-12549 (2025)
- ![](https://dblp.org/img/n.png)

\[j239\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weixing Luo](https://dblp.org/pid/412/4581.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Robust and Discriminative Visual-Semantic Alignment for Zero-Shot Remote Sensing Image Scene Classification. [IEEE Trans. Geosci. Remote. Sens.63](https://dblp.org/db/journals/tgrs/tgrs63.html#journals/tgrs/LiuLGHS25): 1-14 (2025)
- ![](https://dblp.org/img/n.png)

\[j238\]
[Shanwen Wang](https://dblp.org/pid/331/7051.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Sun](https://dblp.org/pid/20/3535-21.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changrui Chen](https://dblp.org/pid/232/4719.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Danfeng Hong](https://dblp.org/pid/153/2550.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Semi-Supervised Semantic Segmentation for Remote Sensing Images via Multiscale Uncertainty Consistency and Cross-Teacher-Student Attention. [IEEE Trans. Geosci. Remote. Sens.63](https://dblp.org/db/journals/tgrs/tgrs63.html#journals/tgrs/WangSCHH25): 1-15 (2025)
- ![](https://dblp.org/img/n.png)

\[j237\]
[Ruida Xi](https://dblp.org/pid/328/5432.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenyang Fu](https://dblp.org/pid/356/6667.html), [Nianchang Huang](https://dblp.org/pid/258/2761.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaowei Zhao](https://dblp.org/pid/02/8134-2.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

CSANet: Cross-Modality Self-Paced Association Network for Unsupervised Visible-Infrared Person Re-Identification. [IEEE Trans. Inf. Forensics Secur.20](https://dblp.org/db/journals/tifs/tifs20.html#journals/tifs/XiFHZZH25): 8672-8686 (2025)
- ![](https://dblp.org/img/n.png)

\[j236\]
[Jingkun Chen](https://dblp.org/pid/212/6645.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenjian Huang](https://dblp.org/pid/142/1752-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianguo Zhang](https://dblp.org/pid/90/6415-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kurt Debattista](https://dblp.org/pid/29/5944.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Addressing Inconsistent Labeling With Cross Image Matching for Scribble-Based Medical Image Segmentation. [IEEE Trans. Image Process.34](https://dblp.org/db/journals/tip/tip34.html#journals/tip/ChenHZDH25): 842-853 (2025)
- ![](https://dblp.org/img/n.png)

\[j235\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yimu Su](https://dblp.org/pid/342/3338.html), [Yan Zhang](https://dblp.org/pid/04/3348-135.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiacheng Hou](https://dblp.org/pid/226/4634.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Raformer: Redundancy-Aware Transformer for Video Wire Inpainting. [IEEE Trans. Image Process.34](https://dblp.org/db/journals/tip/tip34.html#journals/tip/JiSZHPH25): 1795-1809 (2025)
- ![](https://dblp.org/img/n.png)

\[j234\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhilong Wang](https://dblp.org/pid/70/7765-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiyao Liu](https://dblp.org/pid/138/9719-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yunlong Yu](https://dblp.org/pid/45/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Frequency-Spatial Complementation: Unified Channel-Specific Style Attack for Cross-Domain Few-Shot Learning. [IEEE Trans. Image Process.34](https://dblp.org/db/journals/tip/tip34.html#journals/tip/JiWLYPH25): 2242-2253 (2025)
- ![](https://dblp.org/img/n.png)

\[j233\]
[Junbo Qiao](https://dblp.org/pid/336/2803.html), [Wei Li](https://dblp.org/pid/64/6025.html), [Haizhen Xie](https://dblp.org/pid/375/0995.html), [Hanting Chen](https://dblp.org/pid/232/2060.html), [Jie Hu](https://dblp.org/pid/90/5064-21.html), [Shaohui Lin](https://dblp.org/pid/183/0917.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

LIPT: Latency-Aware Image Processing Transformer. [IEEE Trans. Image Process.34](https://dblp.org/db/journals/tip/tip34.html#journals/tip/QiaoLXCHLH25): 3056-3069 (2025)
- ![](https://dblp.org/img/n.png)

\[j232\]
[Yunlong Yu](https://dblp.org/pid/45/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dingyi Zhang](https://dblp.org/pid/132/6761.html), [Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xi Li](https://dblp.org/pid/46/2311-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Zhongfei Zhang](https://dblp.org/pid/z/ZhongfeiMarkZhang.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Balancing Feature Alignment and Uniformity for Few-Shot Classification. [IEEE Trans. Image Process.34](https://dblp.org/db/journals/tip/tip34.html#journals/tip/YuZJLHZ25): 4456-4469 (2025)
- ![](https://dblp.org/img/n.png)

\[j231\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xinshuo Wang](https://dblp.org/pid/208/4029.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Multi-Level Contextual Prototype Modulation for Compositional Zero-Shot Learning. [IEEE Trans. Image Process.34](https://dblp.org/db/journals/tip/tip34.html#journals/tip/LiuWGHS25): 4856-4868 (2025)
- ![](https://dblp.org/img/n.png)

\[j230\]
[Yiwen Liang](https://dblp.org/pid/88/2113.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Chen](https://dblp.org/pid/12/417-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zijia Lin](https://dblp.org/pid/78/9911.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pengzhang Liu](https://dblp.org/pid/44/7674.html), [Jiaxing Wang](https://dblp.org/pid/118/4638.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guoxin Wang](https://dblp.org/pid/05/1182.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lin Li](https://dblp.org/pid/73/2252.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png):

DAR-Prompt: Dynamic Regulation in Prompt Tuning for Multi-Label Zero-Shot Learning. [IEEE Trans. Image Process.34](https://dblp.org/db/journals/tip/tip34.html#journals/tip/LiangCLLWWLZHD25): 7697-7711 (2025)
- ![](https://dblp.org/img/n.png)

\[j229\]
[Yuyang Luo](https://dblp.org/pid/307/1940.html), [Gengshen Wu](https://dblp.org/pid/204/2949.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenjian Liu](https://dblp.org/pid/92/251.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Towards High-Quality MRI Reconstruction With Anisotropic Diffusion-Assisted Generative Adversarial Networks and Its Multi-Modal Images Extension. [IEEE J. Biomed. Health Informatics29(5)](https://dblp.org/db/journals/titb/titb29.html#journals/titb/LuoWLLH25): 3098-3111 (2025)
- ![](https://dblp.org/img/n.png)

\[j228\]
[Wenli Liang](https://dblp.org/pid/175/8786.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Caifeng Shan](https://dblp.org/pid/98/428.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuanjian Yang](https://dblp.org/pid/130/3568.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Multi-Branch Differential Bidirectional Fusion Network for RGB-T Semantic Segmentation. [IEEE Trans. Intell. Veh.10(4)](https://dblp.org/db/journals/tiv/tiv10.html#journals/tiv/LiangSYH25): 2362-2372 (2025)
- ![](https://dblp.org/img/n.png)

\[j227\]
[Ding Sheng Ong](https://dblp.org/pid/284/9241.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Towards Few-Shot Object Detection Through Dual Calibration. [IEEE Trans. Intell. Veh.10(6)](https://dblp.org/db/journals/tiv/tiv10.html#journals/tiv/OngLH25): 3670-3683 (2025)
- ![](https://dblp.org/img/n.png)

\[j226\]
[Zixuan Ding](https://dblp.org/pid/230/1821.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zihan Zhou](https://dblp.org/pid/00/6525.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Chen](https://dblp.org/pid/12/417-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yizhe Xiong](https://dblp.org/pid/358/3714.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sicheng Zhao](https://dblp.org/pid/65/10574.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Cross-Modality Prompts: Few-Shot Multi-Label Recognition With Single-Label Training. [IEEE Trans. Multim.27](https://dblp.org/db/journals/tmm/tmm27.html#journals/tmm/DingZCHXZZH25): 3023-3033 (2025)
- ![](https://dblp.org/img/n.png)

\[j225\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [De Cheng](https://dblp.org/pid/154/1991.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dingwen Zhang](https://dblp.org/pid/150/6620.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shoukun Xu](https://dblp.org/pid/73/7832.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Capsule Networks With Residual Pose Routing. [IEEE Trans. Neural Networks Learn. Syst.36(2)](https://dblp.org/db/journals/tnn/tnn36.html#journals/tnn/LiuCZXH25): 2648-2661 (2025)
- ![](https://dblp.org/img/n.png)

\[j224\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhanyu Jiao](https://dblp.org/pid/397/5892.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wang](https://dblp.org/pid/64/5630-56.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Imbalance Mitigation for Continual Learning via Knowledge Decoupling and Dual Enhanced Contrastive Learning. [IEEE Trans. Neural Networks Learn. Syst.36(2)](https://dblp.org/db/journals/tnn/tnn36.html#journals/tnn/JiJWPH25): 3450-3463 (2025)
- ![](https://dblp.org/img/n.png)

\[j223\]
[Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Runqi Wang](https://dblp.org/pid/266/9915.html), [Xiaodi Wang](https://dblp.org/pid/07/8227.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Rongrong Ji](https://dblp.org/pid/86/5681.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Modulated Convolutional Networks. [IEEE Trans. Neural Networks Learn. Syst.36(3)](https://dblp.org/db/journals/tnn/tnn36.html#journals/tnn/ZhangWWHJ25): 3916-3929 (2025)
- ![](https://dblp.org/img/n.png)

\[j222\]
[Zhuang Shao](https://dblp.org/pid/51/9057.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Demetris Marnerides](https://dblp.org/pid/217/1523.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kurt Debattista](https://dblp.org/pid/29/5944.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Region-Object Relation-Aware Dense Captioning via Transformer. [IEEE Trans. Neural Networks Learn. Syst.36(3)](https://dblp.org/db/journals/tnn/tnn36.html#journals/tnn/ShaoHMD25): 4184-4195 (2025)
- ![](https://dblp.org/img/n.png)

\[j221\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xinshuo Wang](https://dblp.org/pid/208/4029.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Concept-Aware Graph Convolutional Network for Compositional Zero-Shot Learning. [IEEE Trans. Neural Networks Learn. Syst.36(6)](https://dblp.org/db/journals/tnn/tnn36.html#journals/tnn/LiuWGHS25): 10394-10406 (2025)
- ![](https://dblp.org/img/n.png)

\[j220\]
[Ruida Xi](https://dblp.org/pid/328/5432.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Nianchang Huang](https://dblp.org/pid/258/2761.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changzhou Lai](https://dblp.org/pid/330/1965.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

FMCNet+: Feature-Level Modality Compensation for Visible-Infrared Person Re-Identification. [IEEE Trans. Neural Networks Learn. Syst.36(7)](https://dblp.org/db/journals/tnn/tnn36.html#journals/tnn/XiHLZH25): 13247-13261 (2025)
- ![](https://dblp.org/img/n.png)

\[j219\]
[Leqi Shen](https://dblp.org/pid/323/9555.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tao He](https://dblp.org/pid/94/5035.html), [Yifeng Zhang](https://dblp.org/pid/88/2666.html), [Pengzhang Liu](https://dblp.org/pid/44/7674.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Temporal Modeling With Frozen Vision-Language Foundation Models for Parameter-Efficient Text-Video Retrieval. [IEEE Trans. Neural Networks Learn. Syst.36(10)](https://dblp.org/db/journals/tnn/tnn36.html#journals/tnn/ShenHHZLZHD25): 17527-17540 (2025)
- ![](https://dblp.org/img/n.png)

\[c130\]
[Hanxi Yin](https://dblp.org/pid/334/9389.html), [Shaodi You](https://dblp.org/pid/72/7950.html), Jungong Han, [Zhixiang Chen](https://dblp.org/pid/70/3894-3.html):

Sequential Joint Dependency Aware Human Pose Estimation with State Space Model. [AAAI2025](https://dblp.org/db/conf/aaai/aaai2025.html#conf/aaai/YinYH025): 9499-9507
- ![](https://dblp.org/img/n.png)

\[c129\]
[Hui-Yue Yang](https://dblp.org/pid/385/6987.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Ao Wang](https://dblp.org/pid/87/3443.html), [Kai Chen](https://dblp.org/pid/181/2839.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Yongliang Tang](https://dblp.org/pid/201/0244.html), [Pengcheng Gao](https://dblp.org/pid/41/11514.html), [Yuming Quan](https://dblp.org/pid/393/1043.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Promptable Anomaly Segmentation with SAM Through Self-Perception Tuning. [AAAI2025](https://dblp.org/db/conf/aaai/aaai2025.html#conf/aaai/Yang0WCLTGQHD25): 13017-13025
- ![](https://dblp.org/img/n.png)

\[c128\]
[Haoran Lian](https://dblp.org/pid/376/2960.html), [Yizhe Xiong](https://dblp.org/pid/358/3714.html), [Jianwei Niu](https://dblp.org/pid/25/4653-2.html), [Shasha Mo](https://dblp.org/pid/166/7129.html), [Zhenpeng Su](https://dblp.org/pid/348/9741.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Scaffold-BPE: Enhancing Byte Pair Encoding for Large Language Models with Simple and Effective Scaffold Token Removal. [AAAI2025](https://dblp.org/db/conf/aaai/aaai2025.html#conf/aaai/LianX0MSL0HD25): 24539-24548
- ![](https://dblp.org/img/n.png)

\[c127\]
[Xinhao Xu](https://dblp.org/pid/58/8844.html), [Jiaxin Li](https://dblp.org/pid/69/327.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Extending LLM Context Window with Adaptive Grouped Positional Encoding: A Training-Free Method. [ACL (1)2025](https://dblp.org/db/conf/acl/acl2025-1.html#conf/acl/XuL0LHD25): 573-587
- ![](https://dblp.org/img/n.png)

\[c126\]
[Ao Wang](https://dblp.org/pid/87/3443.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

LSNet: See Large, Focus Small. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/WangCLHD25): 9718-9729
- ![](https://dblp.org/img/n.png)

\[c125\]
[Leqi Shen](https://dblp.org/pid/323/9555.html), [Guoqiang Gong](https://dblp.org/pid/168/4603.html), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html), [Tao He](https://dblp.org/pid/94/5035.html), [Yifeng Zhang](https://dblp.org/pid/88/2666.html), [Pengzhang Liu](https://dblp.org/pid/44/7674.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

DiscoVLA: Discrepancy Reduction in Vision, Language, and Alignment for Parameter-Efficient Video-Text Retrieval. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/ShenGHHZLZHD25): 19702-19712
- ![](https://dblp.org/img/n.png)

\[c124\]
[Fengyuan Sun](https://dblp.org/pid/147/6919.html), [Leqi Shen](https://dblp.org/pid/323/9555.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

AdaTP: Attention-Debiased Token Pruning for Video Large Language Models. [EMNLP (Findings)2025](https://dblp.org/db/conf/emnlp/emnlp2025f.html#conf/emnlp/SunSCZHD25): 3273-3286
- ![](https://dblp.org/img/n.png)

\[c123\]
[Minxuan Lv](https://dblp.org/pid/359/3555.html), [Zhenpeng Su](https://dblp.org/pid/348/9741.html), [Leiyu Pan](https://dblp.org/pid/359/6474.html), [Yizhe Xiong](https://dblp.org/pid/358/3714.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Wei Zhou](https://dblp.org/pid/69/5011-19.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html), [Wenwu Ou](https://dblp.org/pid/198/5430.html), [Di Zhang](https://dblp.org/pid/80/3482-26.html), [Kun Gai](https://dblp.org/pid/59/2902.html), [Songlin Hu](https://dblp.org/pid/67/4108-1.html):

DSMoE: Matrix-Partitioned Experts with Dynamic Routing for Computation-Efficient Dense LLMs. [EMNLP2025](https://dblp.org/db/conf/emnlp/emnlp2025.html#conf/emnlp/LvSPXLCZHDOZGH25): 19711-19722
- ![](https://dblp.org/img/n.png)

\[c122\]
[Yizhe Xiong](https://dblp.org/pid/358/3714.html), [Xiansheng Chen](https://dblp.org/pid/245/4652.html), [Xin Ye](https://dblp.org/pid/69/3992.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Haoran Lian](https://dblp.org/pid/376/2960.html), [Zhenpeng Su](https://dblp.org/pid/348/9741.html), [Wei Huang](https://dblp.org/pid/81/6685.html), [Jianwei Niu](https://dblp.org/pid/25/4653-2.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Temporal Scaling Law for Large Language Models. [EMNLP2025](https://dblp.org/db/conf/emnlp/emnlp2025.html#conf/emnlp/XiongCYCLLSHNHD25): 24463-24483
- ![](https://dblp.org/img/n.png)

\[c121\]
[Xingyu Miao](https://dblp.org/pid/280/7469.html), [Haoran Duan](https://dblp.org/pid/82/4334-1.html), [Yang Long](https://dblp.org/pid/82/10183-1.html), Jungong Han:

Rethinking Score Distilling Sampling for 3D Editing and Generation. [ICML2025](https://dblp.org/db/conf/icml/icml2025.html#conf/icml/Miao00H25)
- ![](https://dblp.org/img/n.png)

\[c120\]
[Yiwen Liang](https://dblp.org/pid/88/2113.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Chen](https://dblp.org/pid/12/417-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yizhe Xiong](https://dblp.org/pid/358/3714.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zihan Zhou](https://dblp.org/pid/00/6525.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mengyao Lyu](https://dblp.org/pid/244/8467.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zijia Lin](https://dblp.org/pid/78/9911.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shuaicheng Niu](https://dblp.org/pid/254/1388.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sicheng Zhao](https://dblp.org/pid/65/10574.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Advancing Reliable Test-Time Adaptation of Vision-Language Models under Visual Variations. [ACM Multimedia2025](https://dblp.org/db/conf/mm/mm2025.html#conf/mm/Liang0XZLLNZHD25): 4788-4797
- ![](https://dblp.org/img/n.png)

\[c119\]
[Wei Zhou](https://dblp.org/pid/69/5011-21.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hadi Amirpour](https://dblp.org/pid/186/1301.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Li Yu](https://dblp.org/pid/70/5913-4.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Richang Hong](https://dblp.org/pid/59/1501.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Paul L. Rosin](https://dblp.org/pid/r/PaulLRosin.html)![](https://dblp.org/img/orcid-mark.12x12.png):

MCHM25: Multimedia Computing for Health and Medicine. [ACM Multimedia2025](https://dblp.org/db/conf/mm/mm2025.html#conf/mm/0021A0HHR25): 14293-14295
- ![](https://dblp.org/img/n.png)

\[c118\]
[Xinhao Xu](https://dblp.org/pid/58/8844.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Mengyao Lyu](https://dblp.org/pid/244/8467.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), [Yizhe Xiong](https://dblp.org/pid/358/3714.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Mitigating Hallucinations in Multi-modal Large Language Models via Image Token Attention-Guided Decoding. [NAACL (Long Papers)2025](https://dblp.org/db/conf/naacl/naacl2025-1.html#conf/naacl/XuCLZXLHD25): 1571-1590
- ![](https://dblp.org/img/n.png)

\[i118\]
[Shanwen Wang](https://dblp.org/pid/331/7051.html), [Changrui Chen](https://dblp.org/pid/232/4719.html), [Xin Sun](https://dblp.org/pid/20/3535-21.html), [Danfeng Hong](https://dblp.org/pid/153/2550.html), Jungong Han:

Semi-supervised Semantic Segmentation for Remote Sensing Images via Multi-scale Uncertainty Consistency and Cross-Teacher-Student Attention. [CoRRabs/2501.10736](https://dblp.org/db/journals/corr/corr2501.html#journals/corr/abs-2501-10736) (2025)
- ![](https://dblp.org/img/n.png)

\[i117\]
[Jingkun Chen](https://dblp.org/pid/212/6645.html), [Guang Yang](https://dblp.org/pid/25/5712-72.html), [Xiao Zhang](https://dblp.org/pid/49/4478.html), [Jingchao Peng](https://dblp.org/pid/287/9324.html), [Tianlu Zhang](https://dblp.org/pid/255/8662.html), [Jianguo Zhang](https://dblp.org/pid/90/6415-1.html), Jungong Han, [Vicente Grau](https://dblp.org/pid/g/VicenteGrau.html):

Unsupervised Patch-GAN with Targeted Patch Ranking for Fine-Grained Novelty Detection in Medical Imaging. [CoRRabs/2501.17906](https://dblp.org/db/journals/corr/corr2501.html#journals/corr/abs-2501-17906) (2025)
- ![](https://dblp.org/img/n.png)

\[i116\]
[Haohan Shi](https://dblp.org/pid/361/2593.html), [Fei Zhou](https://dblp.org/pid/84/5639-9.html), [Xin Sun](https://dblp.org/pid/20/3535-21.html), Jungong Han:

Rethinking the Upsampling Layer in Hyperspectral Image Super Resolution. [CoRRabs/2501.18664](https://dblp.org/db/journals/corr/corr2501.html#journals/corr/abs-2501-18664) (2025)
- ![](https://dblp.org/img/n.png)

\[i115\]
[Yizhe Xiong](https://dblp.org/pid/358/3714.html), [Wei Huang](https://dblp.org/pid/81/6685.html), [Xin Ye](https://dblp.org/pid/69/3992.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Haoran Lian](https://dblp.org/pid/376/2960.html), [Zhenpeng Su](https://dblp.org/pid/348/9741.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

UniAttn: Reducing Inference Costs via Softmax Unification for Post-Training LLMs. [CoRRabs/2502.00439](https://dblp.org/db/journals/corr/corr2502.html#journals/corr/abs-2502-00439) (2025)
- ![](https://dblp.org/img/n.png)

\[i114\]
[Minxuan Lv](https://dblp.org/pid/359/3555.html), [Zhenpeng Su](https://dblp.org/pid/348/9741.html), [Leiyu Pan](https://dblp.org/pid/359/6474.html), [Yizhe Xiong](https://dblp.org/pid/358/3714.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Wei Zhou](https://dblp.org/pid/69/5011-19.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html), [Cheng Luo](https://dblp.org/pid/68/6443.html), [Di Zhang](https://dblp.org/pid/80/3482-26.html), [Kun Gai](https://dblp.org/pid/59/2902.html), [Songlin Hu](https://dblp.org/pid/67/4108-1.html):

DSMoE: Matrix-Partitioned Experts with Dynamic Routing for Computation-Efficient Dense LLMs. [CoRRabs/2502.12455](https://dblp.org/db/journals/corr/corr2502.html#journals/corr/abs-2502-12455) (2025)
- ![](https://dblp.org/img/n.png)

\[i113\]
[Leiyu Pan](https://dblp.org/pid/359/6474.html), [Zhenpeng Su](https://dblp.org/pid/348/9741.html), [Minxuan Lv](https://dblp.org/pid/359/3555.html), [Yizhe Xiong](https://dblp.org/pid/358/3714.html), [Xiangwen Zhang](https://dblp.org/pid/68/646.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html), [Cheng Luo](https://dblp.org/pid/68/6443.html), [Di Zhang](https://dblp.org/pid/80/3482-26.html), [Kun Gai](https://dblp.org/pid/59/2902.html), [Deyi Xiong](https://dblp.org/pid/55/6548.html):

Finedeep: Mitigating Sparse Activation in Dense LLMs via Multi-Layer Fine-Grained Experts. [CoRRabs/2502.12928](https://dblp.org/db/journals/corr/corr2502.html#journals/corr/abs-2502-12928) (2025)
- ![](https://dblp.org/img/n.png)

\[i112\]
[Zhong Ji](https://dblp.org/pid/36/6466.html), [Weilong Cao](https://dblp.org/pid/401/7489.html), [Yan Zhang](https://dblp.org/pid/04/3348-135.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han, [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html):

Underlying Semantic Diffusion for Effective and Efficient In-Context Learning. [CoRRabs/2503.04050](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-04050) (2025)
- ![](https://dblp.org/img/n.png)

\[i111\]
[Ao Wang](https://dblp.org/pid/87/3443.html), [Lihao Liu](https://dblp.org/pid/21/309.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

YOLOE: Real-Time Seeing Anything. [CoRRabs/2503.07465](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-07465) (2025)
- ![](https://dblp.org/img/n.png)

\[i110\]
[Mengyao Lyu](https://dblp.org/pid/244/8467.html), [Yan Li](https://dblp.org/pid/87/660.html), [Huasong Zhong](https://dblp.org/pid/227/3501.html), [Wenhao Yang](https://dblp.org/pid/233/4699.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html), [Zhenheng Yang](https://dblp.org/pid/186/7818.html):

Cream of the Crop: Harvesting Rich, Scalable and Transferable Multi-Modal Data for Instruction Fine-Tuning. [CoRRabs/2503.13383](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-13383) (2025)
- ![](https://dblp.org/img/n.png)

\[i109\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Feixiang Liu](https://dblp.org/pid/204/9610.html), [Jiale Du](https://dblp.org/pid/241/3709.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html), Jungong Han:

Unbiased Max-Min Embedding Classification for Transductive Few-Shot Learning: Clustering and Classification Are All You Need. [CoRRabs/2503.22193](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-22193) (2025)
- ![](https://dblp.org/img/n.png)

\[i108\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Xun Zhang](https://dblp.org/pid/18/3246.html), [Jiale Du](https://dblp.org/pid/241/3709.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html), Jungong Han:

Extremely Simple Out-of-distribution Detection for Audio-visual Generalized Zero-shot Learning. [CoRRabs/2503.22197](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-22197) (2025)
- ![](https://dblp.org/img/n.png)

\[i107\]
[Ao Wang](https://dblp.org/pid/87/3443.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

LSNet: See Large, Focus Small. [CoRRabs/2503.23135](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-23135) (2025)
- ![](https://dblp.org/img/n.png)

\[i106\]
[Yuan Zhou](https://dblp.org/pid/40/7018-23.html), [Shilong Jin](https://dblp.org/pid/248/2203.html), [Litao Hua](https://dblp.org/pid/405/1724.html), [Wanjun Lv](https://dblp.org/pid/281/5591.html), [Haoran Duan](https://dblp.org/pid/82/4334-1.html), Jungong Han:

ConsDreamer: Advancing Multi-View Consistency for Zero-Shot Text-to-3D Generation. [CoRRabs/2504.02316](https://dblp.org/db/journals/corr/corr2504.html#journals/corr/abs-2504-02316) (2025)
- ![](https://dblp.org/img/n.png)

\[i105\]
[Yan Zhang](https://dblp.org/pid/04/3348-135.html), [Zhong Ji](https://dblp.org/pid/36/6466.html), [Changxu Meng](https://dblp.org/pid/361/4963.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han:

iEBAKER: Improved Remote Sensing Image-Text Retrieval Framework via Eliminate Before Align and Keyword Explicit Reasoning. [CoRRabs/2504.05644](https://dblp.org/db/journals/corr/corr2504.html#journals/corr/abs-2504-05644) (2025)
- ![](https://dblp.org/img/n.png)

\[i104\]
[Jingkun Chen](https://dblp.org/pid/212/6645.html), [Haoran Duan](https://dblp.org/pid/82/4334-1.html), [Xiao Zhang](https://dblp.org/pid/49/4478.html), [Boyan Gao](https://dblp.org/pid/251/3330.html), [Tao Tan](https://dblp.org/pid/06/7832-2.html), [Vicente Grau](https://dblp.org/pid/g/VicenteGrau.html), Jungong Han:

From Gaze to Insight: Bridging Human Visual Attention and Vision Language Model Explanation for Weakly-Supervised Medical Image Segmentation. [CoRRabs/2504.11368](https://dblp.org/db/journals/corr/corr2504.html#journals/corr/abs-2504-11368) (2025)
- ![](https://dblp.org/img/n.png)

\[i103\]
[Xingyu Miao](https://dblp.org/pid/280/7469.html), [Haoran Duan](https://dblp.org/pid/82/4334-1.html), [Yang Long](https://dblp.org/pid/82/10183-1.html), Jungong Han:

Rethinking Score Distilling Sampling for 3D Editing and Generation. [CoRRabs/2505.01888](https://dblp.org/db/journals/corr/corr2505.html#journals/corr/abs-2505-01888) (2025)
- ![](https://dblp.org/img/n.png)

\[i102\]
[Fengyuan Sun](https://dblp.org/pid/147/6919.html), [Leqi Shen](https://dblp.org/pid/323/9555.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

AdaTP: Attention-Debiased Token Pruning for Video Large Language Models. [CoRRabs/2505.20100](https://dblp.org/db/journals/corr/corr2505.html#journals/corr/abs-2505-20100) (2025)
- ![](https://dblp.org/img/n.png)

\[i101\]
[Zhong Ji](https://dblp.org/pid/36/6466.html), [Rongshuai Wei](https://dblp.org/pid/409/7340.html), [Jingren Liu](https://dblp.org/pid/269/7845.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han:

Interpretable Few-Shot Image Classification via Prototypical Concept-Guided Mixture of LoRA Experts. [CoRRabs/2506.04673](https://dblp.org/db/journals/corr/corr2506.html#journals/corr/abs-2506-04673) (2025)
- ![](https://dblp.org/img/n.png)

\[i100\]
[Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Haoran Duan](https://dblp.org/pid/82/4334-1.html), [Tianlu Zhang](https://dblp.org/pid/255/8662.html), Jungong Han:

THU-Warwick Submission for EPIC-KITCHEN Challenge 2025: Semi-Supervised Video Object Segmentation. [CoRRabs/2506.06748](https://dblp.org/db/journals/corr/corr2506.html#journals/corr/abs-2506-06748) (2025)
- ![](https://dblp.org/img/n.png)

\[i99\]
[Leqi Shen](https://dblp.org/pid/323/9555.html), [Guoqiang Gong](https://dblp.org/pid/168/4603.html), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html), [Tao He](https://dblp.org/pid/94/5035.html), [Yifeng Zhang](https://dblp.org/pid/88/2666.html), [Pengzhang Liu](https://dblp.org/pid/44/7674.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

DiscoVLA: Discrepancy Reduction in Vision, Language, and Alignment for Parameter-Efficient Video-Text Retrieval. [CoRRabs/2506.08887](https://dblp.org/db/journals/corr/corr2506.html#journals/corr/abs-2506-08887) (2025)
- ![](https://dblp.org/img/n.png)

\[i98\]
[Yiwen Liang](https://dblp.org/pid/88/2113.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Yizhe Xiong](https://dblp.org/pid/358/3714.html), [Zihan Zhou](https://dblp.org/pid/00/6525.html), [Mengyao Lyu](https://dblp.org/pid/244/8467.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Shuaicheng Niu](https://dblp.org/pid/254/1388.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Advancing Reliable Test-Time Adaptation of Vision-Language Models under Visual Variations. [CoRRabs/2507.09500](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-09500) (2025)
- ![](https://dblp.org/img/n.png)

\[i97\]
[Hanting Li](https://dblp.org/pid/276/2638.html), [Fei Zhou](https://dblp.org/pid/84/5639-9.html), [Xin Sun](https://dblp.org/pid/20/3535-21.html), [Yang Hua](https://dblp.org/pid/396/8608.html), Jungong Han, [Liang-Jie Zhang](https://dblp.org/pid/z/LiangJieZhang.html):

SAIGFormer: A Spatially-Adaptive Illumination-Guided Network for Low-Light Image Enhancement. [CoRRabs/2507.15520](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-15520) (2025)
- ![](https://dblp.org/img/n.png)

\[i96\]
[Sijie Li](https://dblp.org/pid/58/6303.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), Jungong Han:

SimMLM: A Simple Framework for Multi-modal Learning with Missing Modality. [CoRRabs/2507.19264](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-19264) (2025)
- ![](https://dblp.org/img/n.png)

\[i95\]
[Weide Liu](https://dblp.org/pid/261/9166.html), [Wei Zhou](https://dblp.org/pid/69/5011-21.html), [Jun Liu](https://dblp.org/pid/95/3736-69.html), [Ping Hu](https://dblp.org/pid/53/5490.html), [Jun Cheng](https://dblp.org/pid/78/5816-3.html), Jungong Han, [Weisi Lin](https://dblp.org/pid/14/3737.html):

Modality-Aware Feature Matching: A Comprehensive Review of Single- and Cross-Modality Techniques. [CoRRabs/2507.22791](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-22791) (2025)
- ![](https://dblp.org/img/n.png)

\[i94\]
[Yizhe Xiong](https://dblp.org/pid/358/3714.html), [Zihan Zhou](https://dblp.org/pid/00/6525.html), [Yiwen Liang](https://dblp.org/pid/88/2113.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html), [Fan Zhang](https://dblp.org/pid/21/3626.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Neutralizing Token Aggregation via Information Augmentation for Efficient Test-Time Adaptation. [CoRRabs/2508.03388](https://dblp.org/db/journals/corr/corr2508.html#journals/corr/abs-2508-03388) (2025)
- ![](https://dblp.org/img/n.png)

\[i93\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html), [Zhiyu Qu](https://dblp.org/pid/183/8997.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Changrui Chen](https://dblp.org/pid/232/4719.html), [Jifei Song](https://dblp.org/pid/198/2576.html), Jungong Han, [Jiankang Deng](https://dblp.org/pid/156/7808.html):

Unlocking the Potential of Diffusion Priors in Blind Face Restoration. [CoRRabs/2508.08556](https://dblp.org/db/journals/corr/corr2508.html#journals/corr/abs-2508-08556) (2025)
- ![](https://dblp.org/img/n.png)

\[i92\]
[Zhuoxu Huang](https://dblp.org/pid/331/8231.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), Jungong Han:

Point Linguist Model: Segment Any Object via Bridged Large 3D-Language Model. [CoRRabs/2509.07825](https://dblp.org/db/journals/corr/corr2509.html#journals/corr/abs-2509-07825) (2025)
- ![](https://dblp.org/img/n.png)

\[i91\]
[Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Jingkun Chen](https://dblp.org/pid/212/6645.html), [Yunqi Miao](https://dblp.org/pid/207/3366.html), [Gengshen Wu](https://dblp.org/pid/204/2949.html), [Zhijin Qin](https://dblp.org/pid/157/9149.html), Jungong Han:

The 1st Solution for MOSEv2 Challenge 2025: Long-term and Concept-aware Video Segmentation via SeC. [CoRRabs/2509.19183](https://dblp.org/db/journals/corr/corr2509.html#journals/corr/abs-2509-19183) (2025)
- ![](https://dblp.org/img/n.png)

\[i90\]
[Chang Liu](https://dblp.org/pid/52/5716.html), [Henghui Ding](https://dblp.org/pid/230/1216.html), [Kaining Ying](https://dblp.org/pid/291/9018.html), [Lingyi Hong](https://dblp.org/pid/311/7466.html), [Ning Xu](https://dblp.org/pid/04/5856.html), [Linjie Yang](https://dblp.org/pid/126/6794.html), [Yuchen Fan](https://dblp.org/pid/120/4095.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Jingkun Chen](https://dblp.org/pid/212/6645.html), [Yunqi Miao](https://dblp.org/pid/207/3366.html), [Gengshen Wu](https://dblp.org/pid/204/2949.html), [Zhijin Qin](https://dblp.org/pid/157/9149.html), Jungong Han, [Zhixiong Zhang](https://dblp.org/pid/12/1950.html), [Shuangrui Ding](https://dblp.org/pid/267/1780.html), [Xiaoyi Dong](https://dblp.org/pid/230/3711.html), [Yuhang Zang](https://dblp.org/pid/230/4433.html), [Yuhang Cao](https://dblp.org/pid/212/6480.html), [Jiaqi Wang](https://dblp.org/pid/44/740.html), [Chang Soo Lim](https://dblp.org/pid/54/4422.html), [Joonyoung Moon](https://dblp.org/pid/214/6590.html), [Donghyeon Cho](https://dblp.org/pid/142/2590.html), [Tingmin Li](https://dblp.org/pid/380/5999.html), [Yixuan Li](https://dblp.org/pid/144/6087.html), [Yang Yang](https://dblp.org/pid/48/450.html), [An Yan](https://dblp.org/pid/37/10133.html), [Leilei Cao](https://dblp.org/pid/183/9806.html), [Feng Lu](https://dblp.org/pid/97/6483.html), [Ran Hong](https://dblp.org/pid/278/0621.html), [Youhai Jiang](https://dblp.org/pid/405/2309.html), [Fengjie Zhu](https://dblp.org/pid/350/3991.html), [Yujie Xie](https://dblp.org/pid/204/3880.html), [Hongyang Zhang](https://dblp.org/pid/23/10537.html), [Zhihui Liu](https://dblp.org/pid/56/807.html), [Shihai Ruan](https://dblp.org/pid/417/9681.html), [Quanzhu Niu](https://dblp.org/pid/412/8967.html), [Dengxian Gong](https://dblp.org/pid/415/2440.html), [Shihao Chen](https://dblp.org/pid/61/7845.html), [Tao Zhang](https://dblp.org/pid/15/4777.html), [Yikang Zhou](https://dblp.org/pid/337/1781.html), [Haobo Yuan](https://dblp.org/pid/280/2872.html), [Lu Qi](https://dblp.org/pid/87/3332.html), [Xiangtai Li](https://dblp.org/pid/239/4017.html), [Shunping Ji](https://dblp.org/pid/123/0960.html), [Alexey Nekrasov](https://dblp.org/pid/32/1352-1.html), [Ali Athar](https://dblp.org/pid/187/5650.html), [Daan de Geus](https://dblp.org/pid/227/2962.html), [Alexander Hermans](https://dblp.org/pid/151/9332.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html):

LSVOS 2025 Challenge Report: Recent Advances in Complex Video Object Segmentation. [CoRRabs/2510.11063](https://dblp.org/db/journals/corr/corr2510.html#journals/corr/abs-2510-11063) (2025)
- ![](https://dblp.org/img/n.png)

\[i89\]
[Fengyuan Sun](https://dblp.org/pid/147/6919.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Xinhao Xu](https://dblp.org/pid/58/8844.html), [Dandan Zheng](https://dblp.org/pid/41/5401.html), [Jingdong Chen](https://dblp.org/pid/33/5656.html), [Jun Zhou](https://dblp.org/pid/99/3847.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

PruneHal: Reducing Hallucinations in Multi-modal Large Language Models through Adaptive KV Cache Pruning. [CoRRabs/2510.19183](https://dblp.org/db/journals/corr/corr2510.html#journals/corr/abs-2510-19183) (2025)
- ![](https://dblp.org/img/n.png)

\[i88\]
[Penghui Niu](https://dblp.org/pid/118/3791.html), [Taotao Cai](https://dblp.org/pid/168/4683.html), [Jiashuai She](https://dblp.org/pid/421/9070.html), [Yajuan Zhang](https://dblp.org/pid/09/10185.html), [Junhua Gu](https://dblp.org/pid/26/6721.html), [Ping Zhang](https://dblp.org/pid/13/4682-25.html), Jungong Han, [Jianxin Li](https://dblp.org/pid/l/JianxinLi.html):

USF-Net: A Unified Spatiotemporal Fusion Network for Ground-Based Remote Sensing Cloud Image Sequence Extrapolation. [CoRRabs/2511.09045](https://dblp.org/db/journals/corr/corr2511.html#journals/corr/abs-2511-09045) (2025)
- ![](https://dblp.org/img/n.png)

\[i87\]
[Tianlu Zhang](https://dblp.org/pid/255/8662.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

Tracking and Segmenting Anything in Any Modality. [CoRRabs/2511.19475](https://dblp.org/db/journals/corr/corr2511.html#journals/corr/abs-2511-19475) (2025)
- ![](https://dblp.org/img/n.png)

\[i86\]
[Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Yunqi Miao](https://dblp.org/pid/207/3366.html), Jungong Han:

SAM-Body4D: Training-Free 4D Human Body Mesh Recovery from Videos. [CoRRabs/2512.08406](https://dblp.org/db/journals/corr/corr2512.html#journals/corr/abs-2512-08406) (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j218\]
[Yan Zhang](https://dblp.org/pid/04/3348-135.html), [Zhong Ji](https://dblp.org/pid/36/6466.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han, [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Modality-experts coordinated adaptation for large multimodal models. [Sci. China Inf. Sci.67(12)](https://dblp.org/db/journals/chinaf/chinaf67.html#journals/chinaf/ZhangJPHL24) (2024)
- ![](https://dblp.org/img/n.png)

\[j217\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html), [Yang Yang](https://dblp.org/pid/48/450-9.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Jin Huang](https://dblp.org/pid/49/2488.html):

Lightweight cross-modal transformer for RGB-D salient object detection. [Comput. Vis. Image Underst.249](https://dblp.org/db/journals/cviu/cviu249.html#journals/cviu/HuangYZHH24): 104194 (2024)
- ![](https://dblp.org/img/n.png)

\[j216\]
[Yu Fu](https://dblp.org/pid/09/3263-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changjing Shang](https://dblp.org/pid/03/6446.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Qiang Shen](https://dblp.org/pid/s/QiangShen.html)![](https://dblp.org/img/orcid-mark.12x12.png):

ECMEE: Expert Constrained Multi-Expert Ensembles with Category Entropy Minimization for Long-tailed Visual Recognition. [Neurocomputing576](https://dblp.org/db/journals/ijon/ijon576.html#journals/ijon/FuSHS24): 127357 (2024)
- ![](https://dblp.org/img/n.png)

\[j215\]
[Hao Chen](https://dblp.org/pid/175/3324-107.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yonghan Dong](https://dblp.org/pid/342/4266.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zheming Lu](https://dblp.org/pid/148/1888-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yunlong Yu](https://dblp.org/pid/45/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yingming Li](https://dblp.org/pid/119/1901.html), Jungong Han, [Zhongfei Zhang](https://dblp.org/pid/z/ZhongfeiMarkZhang.html):

Dense affinity matching for Few-Shot Segmentation. [Neurocomputing577](https://dblp.org/db/journals/ijon/ijon577.html#journals/ijon/ChenDLYLHZ24): 127348 (2024)
- ![](https://dblp.org/img/n.png)

\[j214\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html), [Baichao Xing](https://dblp.org/pid/365/8770.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Jin Huang](https://dblp.org/pid/49/2488.html):

Co-segmentation assisted cross-modality person re-identification. [Inf. Fusion104](https://dblp.org/db/journals/inffus/inffus104.html#journals/inffus/HuangXZHH24): 102194 (2024)
- ![](https://dblp.org/img/n.png)

\[j213\]
[Hanqing Sun](https://dblp.org/pid/228/6382-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Supervised biadjacency networks for stereo matching. [Multim. Tools Appl.83(4)](https://dblp.org/db/journals/mta/mta83.html#journals/mta/SunHPL24): 10247-10272 (2024)
- ![](https://dblp.org/img/n.png)

\[j212\]
[Mushui Liu](https://dblp.org/pid/334/2912.html), [Yunlong Yu](https://dblp.org/pid/45/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Zhongfei Zhang](https://dblp.org/pid/z/ZhongfeiMarkZhang.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Tolerant Self-Distillation for image classification. [Neural Networks174](https://dblp.org/db/journals/nn/nn174.html#journals/nn/LiuYJHZ24): 106215 (2024)
- ![](https://dblp.org/img/n.png)

\[j211\]
[Xun Zhang](https://dblp.org/pid/18/3246.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Yuhao Dang](https://dblp.org/pid/370/3843.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Adaptive Relation-Aware Network for zero-shot classification. [Neural Networks174](https://dblp.org/db/journals/nn/nn174.html#journals/nn/ZhangLDGHS24): 106227 (2024)
- ![](https://dblp.org/img/n.png)

\[j210\]
[Changrui Chen](https://dblp.org/pid/232/4719.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Kurt Debattista](https://dblp.org/pid/29/5944.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Virtual Category Learning: A Semi-Supervised Learning Method for Dense Prediction With Extremely Limited Labels. [IEEE Trans. Pattern Anal. Mach. Intell.46(8)](https://dblp.org/db/journals/pami/pami46.html#journals/pami/ChenHD24): 5595-5611 (2024)
- ![](https://dblp.org/img/n.png)

\[j209\]
[Jingkun Chen](https://dblp.org/pid/212/6645.html), [Changrui Chen](https://dblp.org/pid/232/4719.html), [Wenjian Huang](https://dblp.org/pid/142/1752-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianguo Zhang](https://dblp.org/pid/90/6415-1.html), [Kurt Debattista](https://dblp.org/pid/29/5944.html), Jungong Han:

Dynamic contrastive learning guided by class confidence and confusion degree for medical image segmentation. [Pattern Recognit.145](https://dblp.org/db/journals/pr/pr145.html#journals/pr/ChenCHZDH24): 109881 (2024)
- ![](https://dblp.org/img/n.png)

\[j208\]
[Yutao Hu](https://dblp.org/pid/37/5215-2.html), [Xin Huang](https://dblp.org/pid/98/5766.html), [Xiaoyan Luo](https://dblp.org/pid/28/7701.html), Jungong Han, [Xianbin Cao](https://dblp.org/pid/22/3485.html), [Jun Zhang](https://dblp.org/pid/z/JunZhang7.html):

Learning Foreground Information Bottleneck for few-shot semantic segmentation. [Pattern Recognit.146](https://dblp.org/db/journals/pr/pr146.html#journals/pr/HuHLHCZ24): 109993 (2024)
- ![](https://dblp.org/img/n.png)

\[j207\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Yuhao Dang](https://dblp.org/pid/370/3843.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html):

Zero-shot sketch-based image retrieval via adaptive relation-aware metric learning. [Pattern Recognit.152](https://dblp.org/db/journals/pr/pr152.html#journals/pr/LiuDGHS24): 110452 (2024)
- ![](https://dblp.org/img/n.png)

\[j206\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Keda Tao](https://dblp.org/pid/380/6968.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianhui Tian](https://dblp.org/pid/380/6771.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html):

Transductive zero-shot learning with generative model-driven structure alignment. [Pattern Recognit.153](https://dblp.org/db/journals/pr/pr153.html#journals/pr/LiuTTGHS24): 110561 (2024)
- ![](https://dblp.org/img/n.png)

\[j205\]
[Tianlu Zhang](https://dblp.org/pid/255/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaoyi He](https://dblp.org/pid/220/3273.html), [Yongjiang Luo](https://dblp.org/pid/174/4309.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Exploring target-related information with reliable global pixel relationships for robust RGB-T tracking. [Pattern Recognit.155](https://dblp.org/db/journals/pr/pr155.html#journals/pr/ZhangHLZH24): 110707 (2024)
- ![](https://dblp.org/img/n.png)

\[j204\]
[Penghui Niu](https://dblp.org/pid/118/3791.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Junhua Gu](https://dblp.org/pid/26/6721.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yajuan Zhang](https://dblp.org/pid/09/10185.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ping Zhang](https://dblp.org/pid/13/4682-25.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Taotao Cai](https://dblp.org/pid/168/4683.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenjia Xu](https://dblp.org/pid/34/9467.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

MDCGA-Net: Multiscale Direction Context-Aware Network With Global Attention for Building Extraction From Remote Sensing Images. [IEEE J. Sel. Top. Appl. Earth Obs. Remote. Sens.17](https://dblp.org/db/journals/staeors/staeors17.html#journals/staeors/NiuGZZCXH24): 8461-8476 (2024)
- ![](https://dblp.org/img/n.png)

\[j203\]
[Fang Zhao](https://dblp.org/pid/72/4898-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shengcai Liao](https://dblp.org/pid/16/8313.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiantong Huo](https://dblp.org/pid/252/7172.html), [Zhisheng Huo](https://dblp.org/pid/171/1089.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenhao Wang](https://dblp.org/pid/57/9813.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Caifeng Shan](https://dblp.org/pid/98/428.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Weakly Supervised Joint Transfer and Regression of Textures for 3-D Human Reconstruction. [IEEE Trans. Consumer Electron.70(1)](https://dblp.org/db/journals/tce/tce70.html#journals/tce/ZhaoLHHWHS24): 4400-4410 (2024)
- ![](https://dblp.org/img/n.png)

\[j202\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qi Qin](https://dblp.org/pid/143/4836.html), [Yang Yang](https://dblp.org/pid/48/450-132.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Jiao](https://dblp.org/pid/166/3845.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Feature Calibrating and Fusing Network for RGB-D Salient Object Detection. [IEEE Trans. Circuits Syst. Video Technol.34(3)](https://dblp.org/db/journals/tcsv/tcsv34.html#journals/tcsv/ZhangQYJH24): 1493-1507 (2024)
- ![](https://dblp.org/img/n.png)

\[j201\]
[Hao Chen](https://dblp.org/pid/175/3324-107.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yonghan Dong](https://dblp.org/pid/342/4266.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhe-Ming Lu](https://dblp.org/pid/148/1888-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yunlong Yu](https://dblp.org/pid/45/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Self-Prompting Perceptual Edge Learning for Dense Prediction. [IEEE Trans. Circuits Syst. Video Technol.34(6)](https://dblp.org/db/journals/tcsv/tcsv34.html#journals/tcsv/ChenDLYH24): 4528-4541 (2024)
- ![](https://dblp.org/img/n.png)

\[j200\]
[Guangfei Li](https://dblp.org/pid/226/4297.html), [Quanxue Gao](https://dblp.org/pid/63/804.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Coarse-to-Fine Cell Division Approach for Hyperspectral Remote Sensing Image Classification. [IEEE Trans. Circuits Syst. Video Technol.34(6)](https://dblp.org/db/journals/tcsv/tcsv34.html#journals/tcsv/LiGHG24): 4928-4941 (2024)
- ![](https://dblp.org/img/n.png)

\[j199\]
[Guangfei Li](https://dblp.org/pid/226/4297.html), [Wenbing Liu](https://dblp.org/pid/03/782.html), [Quanxue Gao](https://dblp.org/pid/63/804.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qianqian Wang](https://dblp.org/pid/118/6735-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Self-Supervised Edge Perceptual Learning Framework for High-Resolution Remote Sensing Images Classification. [IEEE Trans. Circuits Syst. Video Technol.34(7)](https://dblp.org/db/journals/tcsv/tcsv34.html#journals/tcsv/LiLG0H024): 6024-6038 (2024)
- ![](https://dblp.org/img/n.png)

\[j198\]
[Tianlu Zhang](https://dblp.org/pid/255/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaoyi He](https://dblp.org/pid/220/3273.html), [Qiang Jiao](https://dblp.org/pid/166/3845.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

AMNet: Learning to Align Multi-Modality for RGB-T Tracking. [IEEE Trans. Circuits Syst. Video Technol.34(8)](https://dblp.org/db/journals/tcsv/tcsv34.html#journals/tcsv/ZhangHJZH24): 7386-7400 (2024)
- ![](https://dblp.org/img/n.png)

\[j197\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiahe Wu](https://dblp.org/pid/253/0589.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yaodong Wang](https://dblp.org/pid/28/8544.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Aiping Yang](https://dblp.org/pid/31/9145.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Progressive Semantic Reconstruction Network for Weakly Supervised Referring Expression Grounding. [IEEE Trans. Circuits Syst. Video Technol.34(12)](https://dblp.org/db/journals/tcsv/tcsv34.html#journals/tcsv/JiWWYH24): 13058-13070 (2024)
- ![](https://dblp.org/img/n.png)

\[j196\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiankang Deng](https://dblp.org/pid/156/7808.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Confidence-Guided Centroids for Unsupervised Person Re-Identification. [IEEE Trans. Inf. Forensics Secur.19](https://dblp.org/db/journals/tifs/tifs19.html#journals/tifs/MiaoDDH24): 6471-6483 (2024)
- ![](https://dblp.org/img/n.png)

\[j195\]
[Tianlu Zhang](https://dblp.org/pid/255/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Jiao](https://dblp.org/pid/166/3845.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Exploring Multi-Modal Spatial-Temporal Contexts for High-Performance RGB-T Tracking. [IEEE Trans. Image Process.33](https://dblp.org/db/journals/tip/tip33.html#journals/tip/ZhangJZH24): 4303-4318 (2024)
- ![](https://dblp.org/img/n.png)

\[j194\]
[Xuan Wang](https://dblp.org/pid/34/4799-16.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yunlong Yu](https://dblp.org/pid/45/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Model Attention Expansion for Few-Shot Class-Incremental Learning. [IEEE Trans. Image Process.33](https://dblp.org/db/journals/tip/tip33.html#journals/tip/WangJYPH24): 4419-4431 (2024)
- ![](https://dblp.org/img/n.png)

\[j193\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Yang](https://dblp.org/pid/48/450-132.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ruida Xi](https://dblp.org/pid/328/5432.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Jin Huang](https://dblp.org/pid/49/2488.html):

Salient Object Detection From Arbitrary Modalities. [IEEE Trans. Image Process.33](https://dblp.org/db/journals/tip/tip33.html#journals/tip/HuangYXZHH24): 6268-6282 (2024)
- ![](https://dblp.org/img/n.png)

\[j192\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Zhou](https://dblp.org/pid/86/949-2.html), [Gengshen Wu](https://dblp.org/pid/204/2949.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shoukun Xu](https://dblp.org/pid/73/7832.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

TCGNet: Type-Correlation Guidance for Salient Object Detection. [IEEE Trans. Intell. Transp. Syst.25(7)](https://dblp.org/db/journals/tits/tits25.html#journals/tits/LiuZWXH24): 6633-6644 (2024)
- ![](https://dblp.org/img/n.png)

\[j191\]
[Yuanjian Yang](https://dblp.org/pid/130/3568.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Caifeng Shan](https://dblp.org/pid/98/428.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fang Zhao](https://dblp.org/pid/72/4898-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenli Liang](https://dblp.org/pid/175/8786.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

On Exploring Shape and Semantic Enhancements for RGB-X Semantic Segmentation. [IEEE Trans. Intell. Veh.9(1)](https://dblp.org/db/journals/tiv/tiv9.html#journals/tiv/YangSZLH24): 2223-2235 (2024)
- ![](https://dblp.org/img/n.png)

\[j190\]
[Zhuang Shao](https://dblp.org/pid/51/9057.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Kurt Debattista](https://dblp.org/pid/29/5944.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png):

DCMSTRD: End-to-end Dense Captioning via Multi-Scale Transformer Decoding. [IEEE Trans. Multim.26](https://dblp.org/db/journals/tmm/tmm26.html#journals/tmm/ShaoHDP24): 7581-7593 (2024)
- ![](https://dblp.org/img/n.png)

\[j189\]
[Jing Nie](https://dblp.org/pid/39/5493-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jin Xie](https://dblp.org/pid/80/1949-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Binocular Image Dehazing via a Plain Network Without Disparity Estimation. [IEEE Trans. Multim.26](https://dblp.org/db/journals/tmm/tmm26.html#journals/tmm/NiePXHL24): 7973-7986 (2024)
- ![](https://dblp.org/img/n.png)

\[j188\]
[Zhenkun Fan](https://dblp.org/pid/315/3130.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhuoxu Huang](https://dblp.org/pid/331/8231.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhixiang Chen](https://dblp.org/pid/70/3894-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tao Xu](https://dblp.org/pid/96/6771-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Lightweight Multiperson Pose Estimation With Staggered Alignment Self-Distillation. [IEEE Trans. Multim.26](https://dblp.org/db/journals/tmm/tmm26.html#journals/tmm/FanHCXHK24): 9228-9240 (2024)
- ![](https://dblp.org/img/n.png)

\[j187\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuhao Dang](https://dblp.org/pid/370/3843.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Zero-Shot Learning With Attentive Region Embedding and Enhanced Semantics. [IEEE Trans. Neural Networks Learn. Syst.35(3)](https://dblp.org/db/journals/tnn/tnn35.html#journals/tnn/LiuDGHS24): 4220-4231 (2024)
- ![](https://dblp.org/img/n.png)

\[j186\]
[Shenlu Zhao](https://dblp.org/pid/300/5768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yichen Liu](https://dblp.org/pid/72/8807.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Jiao](https://dblp.org/pid/166/3845.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Mitigating Modality Discrepancies for RGB-T Semantic Segmentation. [IEEE Trans. Neural Networks Learn. Syst.35(7)](https://dblp.org/db/journals/tnn/tnn35.html#journals/tnn/ZhaoLJZH24): 9380-9394 (2024)
- ![](https://dblp.org/img/n.png)

\[j185\]
[Tianxiang Hao](https://dblp.org/pid/270/0611-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaohan Ding](https://dblp.org/pid/218/7379.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Yuchen Guo](https://dblp.org/pid/132/7979.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Manipulating Identical Filter Redundancy for Efficient Pruning on Deep and Complicated CNN. [IEEE Trans. Neural Networks Learn. Syst.35(11)](https://dblp.org/db/journals/tnn/tnn35.html#journals/tnn/HaoDHGD24): 16831-16844 (2024)
- ![](https://dblp.org/img/n.png)

\[j184\]
[Zhenyu Liu](https://dblp.org/pid/74/4038.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Da Li](https://dblp.org/pid/43/4804-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xinyu Zhang](https://dblp.org/pid/58/4582.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhang Zhang](https://dblp.org/pid/94/2468-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peng Zhang](https://dblp.org/pid/21/1048-57.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Caifeng Shan](https://dblp.org/pid/98/428.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Pedestrian Attribute Recognition via Spatio-temporal Relationship Learning for Visual Surveillance. [ACM Trans. Multim. Comput. Commun. Appl.20(6)](https://dblp.org/db/journals/tomccap/tomccap20.html#journals/tomccap/LiuLZZZSH24): 159:1-159:15 (2024)
- ![](https://dblp.org/img/n.png)

\[c117\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html), [Jiankang Deng](https://dblp.org/pid/156/7808.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

WaveFace: Authentic Face Restoration with Efficient Frequency Recovery. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/MiaoDH24): 6583-6592
- ![](https://dblp.org/img/n.png)

\[c116\]
[Mengyao Lyu](https://dblp.org/pid/244/8467.html), [Yuhong Yang](https://dblp.org/pid/365/8877.html), [Haiwen Hong](https://dblp.org/pid/297/4419.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Xuan Jin](https://dblp.org/pid/80/5681.html), [Yuan He](https://dblp.org/pid/11/1735-11.html), [Hui Xue](https://dblp.org/pid/27/3541-1.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

One-dimensional Adapter to Rule Them All: Concepts, Diffusion Models and Erasing Applications. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/Lyu0HCJ00HD24): 7559-7568
- ![](https://dblp.org/img/n.png)

\[c115\]
[Ao Wang](https://dblp.org/pid/87/3443.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Rep ViT: Revisiting Mobile CNN From ViT Perspective. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/Wang0LHD24): 15909-15920
- ![](https://dblp.org/img/n.png)

\[c114\]
[Hui-Yue Yang](https://dblp.org/pid/385/6987.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Lihao Liu](https://dblp.org/pid/21/309.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Kai Chen](https://dblp.org/pid/181/2839.html), [Liejun Wang](https://dblp.org/pid/116/7864.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Context Enhancement with Reconstruction as Sequence for Unified Unsupervised Anomaly Detection. [ECAI2024](https://dblp.org/db/conf/ecai/ecai2024.html#conf/ecai/YangCLLCWHD24): 2098-2105
- ![](https://dblp.org/img/n.png)

\[c113\]
[Xuan Wang](https://dblp.org/pid/34/4799-16.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiyao Liu](https://dblp.org/pid/138/9719-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

On the Approximation Risk of Few-Shot Class-Incremental Learning. [ECCV (51)2024](https://dblp.org/db/conf/eccv/eccv2024-51.html#conf/eccv/WangJLPH24): 162-178
- ![](https://dblp.org/img/n.png)

\[c112\]
[Mengyao Lyu](https://dblp.org/pid/244/8467.html), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html), [Xinhao Xu](https://dblp.org/pid/58/8844.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Learn from the Learnt: Source-Free Active Domain Adaptation via Contrastive Sampling and Visual Persistence. [ECCV (1)2024](https://dblp.org/db/conf/eccv/eccv2024-1.html#conf/eccv/LyuHXCLHD24): 228-246
- ![](https://dblp.org/img/n.png)

\[c111\]
[Changrui Chen](https://dblp.org/pid/232/4719.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kurt Debattista](https://dblp.org/pid/29/5944.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Pseudo-labelling Should Be Aware of Disguising Channel Activations. [ECCV (63)2024](https://dblp.org/db/conf/eccv/eccv2024-63.html#conf/eccv/ChenDH24): 312-328
- ![](https://dblp.org/img/n.png)

\[c110\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Pavel Tokmakov](https://dblp.org/pid/153/2264.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Khanh-Tung Tran](https://dblp.org/pid/359/3793.html), [Xuan-Son Vu](https://dblp.org/pid/151/8673.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Minasadat Attari](https://dblp.org/pid/370/3618.html), [Antoni B. Chan](https://dblp.org/pid/55/5814.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liang Chen](https://dblp.org/pid/01/5394.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Jaired Collins](https://dblp.org/pid/211/4242.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Ganesh Sai Manas Devarapu](https://dblp.org/pid/406/4906.html), [Yinglong Du](https://dblp.org/pid/199/1274.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Wan-Cyuan Fan](https://dblp.org/pid/300/5836.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Raghav Goyal](https://dblp.org/pid/191/6034.html), Jungong Han, [Bijaya Kumar Hatuwal](https://dblp.org/pid/318/9407.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Xiantao Hu](https://dblp.org/pid/160/8016.html), [Xingsen Huang](https://dblp.org/pid/284/1333.html), [Yuqing Huang](https://dblp.org/pid/134/5853.html), [Dongmei Jiang](https://dblp.org/pid/47/1926.html), [Ben Kang](https://dblp.org/pid/340/1671.html), [Kannappan Palaniappan](https://dblp.org/pid/21/700.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Simiao Lai](https://dblp.org/pid/282/1954.html), [Ning Li](https://dblp.org/pid/14/5410-44.html), [Xiaohai Li](https://dblp.org/pid/00/38.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Cheng Liang](https://dblp.org/pid/81/9078.html), [Liting Lin](https://dblp.org/pid/227/2204.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Ting Liu](https://dblp.org/pid/52/5150-18.html), [Ziquan Liu](https://dblp.org/pid/207/9035.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Yifei Luo](https://dblp.org/pid/58/3045.html), [Deshui Miao](https://dblp.org/pid/307/5501.html), [Juan David Mogollon](https://dblp.org/pid/325/7624.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ziqi Pang](https://dblp.org/pid/255/9210.html), [Jaswanth Reddy Pochimireddy](https://dblp.org/pid/406/5059.html), [Viktor Prutyanov](https://dblp.org/pid/245/3321.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Gani Rahmon](https://dblp.org/pid/291/7224.html), [Aleksandr Romanov](https://dblp.org/pid/239/5991.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liangtao Shi](https://dblp.org/pid/366/5426.html), [Mennatullah Siam](https://dblp.org/pid/163/9048.html), [Leonid Sigal](https://dblp.org/pid/09/4991.html), [Arun Kumar Sivapuram](https://dblp.org/pid/344/4532.html), [Roman A. Solovyev](https://dblp.org/pid/163/3390.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Elham Soltani Kazemi](https://dblp.org/pid/318/1851.html), [Imad Eddine Toubal](https://dblp.org/pid/292/6360.html), [Jia Wan](https://dblp.org/pid/13/6504-1.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Xinying Wang](https://dblp.org/pid/06/3244-5.html), [Yaowei Wang](https://dblp.org/pid/68/2992-1.html), [Yu-Xiong Wang](https://dblp.org/pid/35/10700.html), [Zhiquan Wang](https://dblp.org/pid/18/5129.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Qiangqiang Wu](https://dblp.org/pid/193/1415.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Zihao Xia](https://dblp.org/pid/382/4580.html), [Jinxia Xie](https://dblp.org/pid/294/3376.html), [Chenlong Xu](https://dblp.org/pid/315/8714.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Yong Xu](https://dblp.org/pid/07/4630-7.html), [Chaocan Xue](https://dblp.org/pid/334/6591.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chao Yang](https://dblp.org/pid/00/5867.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Chenyang Yu](https://dblp.org/pid/287/4163.html), [Ke Yu](https://dblp.org/pid/23/2089.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiaming Zhang](https://dblp.org/pid/81/10010-6.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Yaozong Zheng](https://dblp.org/pid/344/6907.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jinglin Zhou](https://dblp.org/pid/48/6808.html), [Junbao Zhou](https://dblp.org/pid/340/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yong Zhou](https://dblp.org/pid/90/5836.html), [Zikun Zhou](https://dblp.org/pid/271/8084.html), [Guibo Zhu](https://dblp.org/pid/125/2113.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Vladimir V. Zunin](https://dblp.org/pid/372/7918.html)![](https://dblp.org/img/orcid-mark.12x12.png):

The Second Visual Object Tracking Segmentation VOTS2024 Challenge Results. [ECCV Workshops (7)2024](https://dblp.org/db/conf/eccv/eccv2024-w7.html#conf/eccv/KristanMTFZLTVBCFACCCCC24): 357-383
- ![](https://dblp.org/img/n.png)

\[c109\]
[Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chang Liu](https://dblp.org/pid/52/5716-72.html), [Yunchao Wei](https://dblp.org/pid/118/5394.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Nikhila Ravi](https://dblp.org/pid/248/7650.html), [Shuting He](https://dblp.org/pid/255/9456.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Song Bai](https://dblp.org/pid/151/6422-1.html), [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Deshui Miao](https://dblp.org/pid/307/5501.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Yaowei Wang](https://dblp.org/pid/68/2992-1.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Zhensong Xu](https://dblp.org/pid/149/5188.html), [Jiangtao Yao](https://dblp.org/pid/294/5962.html), [Chengjing Wu](https://dblp.org/pid/379/5986.html), [Ting Liu](https://dblp.org/pid/52/5150-18.html), [Luoqi Liu](https://dblp.org/pid/29/8842.html), [Xinyu Liu](https://dblp.org/pid/98/738.html), [Jing Zhang](https://dblp.org/pid/05/3499-37.html), [Kexin Zhang](https://dblp.org/pid/119/0668-3.html), [Yuting Yang](https://dblp.org/pid/25/3635-8.html), [Licheng Jiao](https://dblp.org/pid/40/3714.html), [Shuyuan Yang](https://dblp.org/pid/81/2383.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Jingnan Luo](https://dblp.org/pid/379/6720.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), Jungong Han, [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Bin Cao](https://dblp.org/pid/17/1169.html), [Yisi Zhang](https://dblp.org/pid/318/0710.html), [Xuanxu Lin](https://dblp.org/pid/380/2324.html), [Xingjian He](https://dblp.org/pid/204/0216.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html), [Jing Liu](https://dblp.org/pid/72/2590-1.html), [Feiyu Pan](https://dblp.org/pid/142/1276.html), [Hao Fang](https://dblp.org/pid/06/2484-10.html), [Xiankai Lu](https://dblp.org/pid/153/2122.html):

PVUW 2024 Challenge on Complex Video Understanding: Methods and Results. [ECCV Workshops (10)2024](https://dblp.org/db/conf/eccv/eccv2024-w10.html#conf/eccv/DingLWRHBTMLHWYXYWLLLZZ24): 361-377
- ![](https://dblp.org/img/n.png)

\[c108\]
[Yizhe Xiong](https://dblp.org/pid/358/3714.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Chen](https://dblp.org/pid/12/417-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zijia Lin](https://dblp.org/pid/78/9911.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Yuesong Zhang](https://dblp.org/pid/155/5084.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guoxin Wang](https://dblp.org/pid/05/1182.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yongjun Bao](https://dblp.org/pid/52/5055.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png):

PYRA: Parallel Yielding Re-activation for Training-Inference Efficient Task Adaptation. [ECCV (9)2024](https://dblp.org/db/conf/eccv/eccv2024-9.html#conf/eccv/XiongCHLHZWBD24): 455-473
- ![](https://dblp.org/img/n.png)

\[c107\]
[Xinhao Xu](https://dblp.org/pid/58/8844.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Lixing Gong](https://dblp.org/pid/331/1426.html), [Guoxin Wang](https://dblp.org/pid/05/1182.html), [Yongjun Bao](https://dblp.org/pid/52/5055.html), [Guiguang Ding](https://dblp.org/pid/51/740.html):

TaD: A Plug-and-Play Task-Aware Decoding Method to Better Adapt LLMs on Downstream Tasks. [IJCAI2024](https://dblp.org/db/conf/ijcai/ijcai2024.html#conf/ijcai/Xu0LHGWBD24): 6587-6596
- ![](https://dblp.org/img/n.png)

\[c106\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Changxu Meng](https://dblp.org/pid/361/4963.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yan Zhang](https://dblp.org/pid/04/3348-135.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haoran Wang](https://dblp.org/pid/28/3021-4.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Eliminate Before Align: A Remote Sensing Image-Text Retrieval Framework with Keyword Explicit Reasoning. [ACM Multimedia2024](https://dblp.org/db/conf/mm/mm2024.html#conf/mm/JiMZWPH24): 1662-1671
- ![](https://dblp.org/img/n.png)

\[c105\]
[Ao Wang](https://dblp.org/pid/87/3443.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Lihao Liu](https://dblp.org/pid/21/309.html), [Kai Chen](https://dblp.org/pid/181/2839.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

YOLOv10: Real-Time End-to-End Object Detection. [NeurIPS2024](https://dblp.org/db/conf/nips/neurips2024.html#conf/nips/WangCLCLHD24)
- ![](https://dblp.org/img/n.png)

\[c104\]
[Tianlu Zhang](https://dblp.org/pid/255/8662.html), [Kurt Debattista](https://dblp.org/pid/29/5944.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

Revisiting motion information for RGB-Event tracking with MOT philosophy. [NeurIPS2024](https://dblp.org/db/conf/nips/neurips2024.html#conf/nips/ZhangD0DH24)
- ![](https://dblp.org/img/n.png)

\[c103\]
[Jianqiao Zhang](https://dblp.org/pid/219/2760-2.html), [Caifeng Shan](https://dblp.org/pid/98/428.html), Jungong Han:

FedGMKD: An Efficient Prototype Federated Learning Framework through Knowledge Distillation and Discrepancy-Aware Aggregation. [NeurIPS2024](https://dblp.org/db/conf/nips/neurips2024.html#conf/nips/ZhangSH24)
- ![](https://dblp.org/img/n.png)

\[c102\]
[Hao Chen](https://dblp.org/pid/175/3324-107.html), [Yonghan Dong](https://dblp.org/pid/342/4266.html), [Zheming Lu](https://dblp.org/pid/148/1888-1.html), [Yunlong Yu](https://dblp.org/pid/45/7404.html), Jungong Han:

Pixel Matching Network for Cross-Domain Few-Shot Segmentation. [WACV2024](https://dblp.org/db/conf/wacv/wacv2024.html#conf/wacv/ChenDLYH24): 967-976
- ![](https://dblp.org/img/n.png)

\[i85\]
[Chenghao Xiao](https://dblp.org/pid/325/2555.html), [Zhuoxu Huang](https://dblp.org/pid/331/8231.html), [Danlu Chen](https://dblp.org/pid/188/6023.html), [G. Thomas Hudson](https://dblp.org/pid/307/8392.html), [Yizhi Li](https://dblp.org/pid/234/5954.html), [Haoran Duan](https://dblp.org/pid/82/4334-1.html), [Chenghua Lin](https://dblp.org/pid/11/7536.html), [Jie Fu](https://dblp.org/pid/16/7565.html), Jungong Han, [Noura Al Moubayed](https://dblp.org/pid/27/8509.html):

Pixel Sentence Representation Learning. [CoRRabs/2402.08183](https://dblp.org/db/journals/corr/corr2402.html#journals/corr/abs-2402-08183) (2024)
- ![](https://dblp.org/img/n.png)

\[i84\]
[Yizhe Xiong](https://dblp.org/pid/358/3714.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Yuesong Zhang](https://dblp.org/pid/155/5084.html), [Guoxin Wang](https://dblp.org/pid/05/1182.html), [Yongjun Bao](https://dblp.org/pid/52/5055.html), [Guiguang Ding](https://dblp.org/pid/51/740.html):

PYRA: Parallel Yielding Re-Activation for Training-Inference Efficient Task Adaptation. [CoRRabs/2403.09192](https://dblp.org/db/journals/corr/corr2403.html#journals/corr/abs-2403-09192) (2024)
- ![](https://dblp.org/img/n.png)

\[i83\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html), [Jiankang Deng](https://dblp.org/pid/156/7808.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

WaveFace: Authentic Face Restoration with Efficient Frequency Recovery. [CoRRabs/2403.12760](https://dblp.org/db/journals/corr/corr2403.html#journals/corr/abs-2403-12760) (2024)
- ![](https://dblp.org/img/n.png)

\[i82\]
[Zhuoxu Huang](https://dblp.org/pid/331/8231.html), [Zhenkun Fan](https://dblp.org/pid/315/3130.html), [Tao Xu](https://dblp.org/pid/96/6771-38.html), Jungong Han:

On Exploring PDE Modeling for Point Cloud Video Representation Learning. [CoRRabs/2404.04720](https://dblp.org/db/journals/corr/corr2404.html#journals/corr/abs-2404-04720) (2024)
- ![](https://dblp.org/img/n.png)

\[i81\]
[Zhong Ji](https://dblp.org/pid/36/6466.html), [Yimu Su](https://dblp.org/pid/342/3338.html), [Yan Zhang](https://dblp.org/pid/04/3348-135.html), [Jiacheng Hou](https://dblp.org/pid/226/4634.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han:

Raformer: Redundancy-Aware Transformer for Video Wire Inpainting. [CoRRabs/2404.15802](https://dblp.org/db/journals/corr/corr2404.html#journals/corr/abs-2404-15802) (2024)
- ![](https://dblp.org/img/n.png)

\[i80\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html), [Yang Yang](https://dblp.org/pid/48/450-9.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han, [Jin Huang](https://dblp.org/pid/49/2488.html):

Modality Prompts for Arbitrary Modality Salient Object Detection. [CoRRabs/2405.03351](https://dblp.org/db/journals/corr/corr2405.html#journals/corr/abs-2405-03351) (2024)
- ![](https://dblp.org/img/n.png)

\[i79\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html), [Yang Yang](https://dblp.org/pid/48/450-9.html), [Ruida Xi](https://dblp.org/pid/328/5432.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han, [Jin Huang](https://dblp.org/pid/49/2488.html):

Salient Object Detection From Arbitrary Modalities. [CoRRabs/2405.03352](https://dblp.org/db/journals/corr/corr2405.html#journals/corr/abs-2405-03352) (2024)
- ![](https://dblp.org/img/n.png)

\[i78\]
[Ao Wang](https://dblp.org/pid/87/3443.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Lihao Liu](https://dblp.org/pid/21/309.html), [Kai Chen](https://dblp.org/pid/181/2839.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

YOLOv10: Real-Time End-to-End Object Detection. [CoRRabs/2405.14458](https://dblp.org/db/journals/corr/corr2405.html#journals/corr/abs-2405-14458) (2024)
- ![](https://dblp.org/img/n.png)

\[i77\]
[Jinze Yang](https://dblp.org/pid/162/1636.html), [Haoran Wang](https://dblp.org/pid/28/3021-4.html), [Zining Zhu](https://dblp.org/pid/378/1808.html), [Chenglong Liu](https://dblp.org/pid/123/5266.html), [Meng Wymond Wu](https://dblp.org/pid/379/4809.html), [Zeke Xie](https://dblp.org/pid/210/1039.html), [Zhong Ji](https://dblp.org/pid/36/6466.html), Jungong Han, [Mingming Sun](https://dblp.org/pid/87/8665-1.html):

VIP: Versatile Image Outpainting Empowered by Multimodal Large Language Model. [CoRRabs/2406.01059](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-01059) (2024)
- ![](https://dblp.org/img/n.png)

\[i76\]
[Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Jingnan Luo](https://dblp.org/pid/379/6720.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), Jungong Han, [Feng Zheng](https://dblp.org/pid/39/800-1.html):

1st Place Solution for MeViS Track in CVPR 2024 PVUW Workshop: Motion Expression guided Video Segmentation. [CoRRabs/2406.07043](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-07043) (2024)
- ![](https://dblp.org/img/n.png)

\[i75\]
[Henghui Ding](https://dblp.org/pid/230/1216.html), [Chang Liu](https://dblp.org/pid/52/5716-72.html), [Yunchao Wei](https://dblp.org/pid/118/5394.html), [Nikhila Ravi](https://dblp.org/pid/248/7650.html), [Shuting He](https://dblp.org/pid/255/9456.html), [Song Bai](https://dblp.org/pid/151/6422-1.html), [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Deshui Miao](https://dblp.org/pid/307/5501.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Yaowei Wang](https://dblp.org/pid/68/2992-1.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Zhensong Xu](https://dblp.org/pid/149/5188.html), [Jiangtao Yao](https://dblp.org/pid/294/5962.html), [Chengjing Wu](https://dblp.org/pid/379/5986.html), [Ting Liu](https://dblp.org/pid/52/5150-18.html), [Luoqi Liu](https://dblp.org/pid/29/8842.html), [Xinyu Liu](https://dblp.org/pid/98/738.html), [Jing Zhang](https://dblp.org/pid/05/3499-37.html), [Kexin Zhang](https://dblp.org/pid/119/0668-3.html), [Yuting Yang](https://dblp.org/pid/25/3635-8.html), [Licheng Jiao](https://dblp.org/pid/40/3714.html), [Shuyuan Yang](https://dblp.org/pid/81/2383.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Jingnan Luo](https://dblp.org/pid/379/6720.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), Jungong Han, [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Bin Cao](https://dblp.org/pid/17/1169.html), [Yisi Zhang](https://dblp.org/pid/318/0710.html), [Xuanxu Lin](https://dblp.org/pid/380/2324.html), [Xingjian He](https://dblp.org/pid/204/0216.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html), [Jing Liu](https://dblp.org/pid/72/2590-1.html), [Feiyu Pan](https://dblp.org/pid/142/1276.html), [Hao Fang](https://dblp.org/pid/06/2484-10.html), [Xiankai Lu](https://dblp.org/pid/153/2122.html):

PVUW 2024 Challenge on Complex Video Understanding: Methods and Results. [CoRRabs/2406.17005](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-17005) (2024)
- ![](https://dblp.org/img/n.png)

\[i74\]
[Jingren Liu](https://dblp.org/pid/269/7845.html), [Zhong Ji](https://dblp.org/pid/36/6466.html), [Yunlong Yu](https://dblp.org/pid/45/7404.html), [Jiale Cao](https://dblp.org/pid/167/3851.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han, [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html):

Parameter-Efficient Fine-Tuning for Continual Learning: A Neural Tangent Kernel Perspective. [CoRRabs/2407.17120](https://dblp.org/db/journals/corr/corr2407.html#journals/corr/abs-2407-17120) (2024)
- ![](https://dblp.org/img/n.png)

\[i73\]
[Mengyao Lyu](https://dblp.org/pid/244/8467.html), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html), [Xinhao Xu](https://dblp.org/pid/58/8844.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Learn from the Learnt: Source-Free Active Domain Adaptation via Contrastive Sampling and Visual Persistence. [CoRRabs/2407.18899](https://dblp.org/db/journals/corr/corr2407.html#journals/corr/abs-2407-18899) (2024)
- ![](https://dblp.org/img/n.png)

\[i72\]
[Fan Yang](https://dblp.org/pid/29/3081-83.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), [Yanhao Zhang](https://dblp.org/pid/84/10486-1.html), [Haoxiang Chen](https://dblp.org/pid/385/7338.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Wenbo Tang](https://dblp.org/pid/219/1693.html), [Haonan Lu](https://dblp.org/pid/129/0998.html), [Pengfei Xu](https://dblp.org/pid/04/383-3.html), [Zhenyu Yang](https://dblp.org/pid/13/5969.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

LLMI3D: Empowering LLM with 3D Perception from a Single 2D Image. [CoRRabs/2408.07422](https://dblp.org/db/journals/corr/corr2408.html#journals/corr/abs-2408-07422) (2024)
- ![](https://dblp.org/img/n.png)

\[i71\]
[Hui-Yue Yang](https://dblp.org/pid/385/6987.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Lihao Liu](https://dblp.org/pid/21/309.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Kai Chen](https://dblp.org/pid/181/2839.html), [Liejun Wang](https://dblp.org/pid/116/7864.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Context Enhancement with Reconstruction as Sequence for Unified Unsupervised Anomaly Detection. [CoRRabs/2409.06285](https://dblp.org/db/journals/corr/corr2409.html#journals/corr/abs-2409-06285) (2024)
- ![](https://dblp.org/img/n.png)

\[i70\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html), [Chengxin Li](https://dblp.org/pid/166/6518.html), [Shoukun Xu](https://dblp.org/pid/73/7832.html), Jungong Han:

Part-Whole Relational Fusion Towards Multi-Modal Scene Understanding. [CoRRabs/2410.14944](https://dblp.org/db/journals/corr/corr2410.html#journals/corr/abs-2410-14944) (2024)
- ![](https://dblp.org/img/n.png)

\[i69\]
[Zhong Ji](https://dblp.org/pid/36/6466.html), [Shuo Yang](https://dblp.org/pid/78/1102.html), [Jingren Liu](https://dblp.org/pid/269/7845.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han:

A Fresh Look at Generalized Category Discovery through Non-negative Matrix Factorization. [CoRRabs/2410.21807](https://dblp.org/db/journals/corr/corr2410.html#journals/corr/abs-2410-21807) (2024)
- ![](https://dblp.org/img/n.png)

\[i68\]
[Hongsheng Zhang](https://dblp.org/pid/19/4547.html), [Zhong Ji](https://dblp.org/pid/36/6466.html), [Jingren Liu](https://dblp.org/pid/269/7845.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han:

Multi-Stage Knowledge Integration of Vision-Language Models for Continual Learning. [CoRRabs/2411.06764](https://dblp.org/db/journals/corr/corr2411.html#journals/corr/abs-2411-06764) (2024)
- ![](https://dblp.org/img/n.png)

\[i67\]
[Hui-Yue Yang](https://dblp.org/pid/385/6987.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Ao Wang](https://dblp.org/pid/87/3443.html), [Kai Chen](https://dblp.org/pid/181/2839.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Yongliang Tang](https://dblp.org/pid/201/0244.html), [Pengcheng Gao](https://dblp.org/pid/41/11514.html), [Yuming Quan](https://dblp.org/pid/393/1043.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Promptable Anomaly Segmentation with SAM Through Self-Perception Tuning. [CoRRabs/2411.17217](https://dblp.org/db/journals/corr/corr2411.html#journals/corr/abs-2411-17217) (2024)
- ![](https://dblp.org/img/n.png)

\[i66\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Jiale Du](https://dblp.org/pid/241/3709.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html), Jungong Han:

Relation-Aware Meta-Learning for Zero-shot Sketch-Based Image Retrieval. [CoRRabs/2412.00120](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-00120) (2024)
- ![](https://dblp.org/img/n.png)

\[i65\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Xinshuo Wang](https://dblp.org/pid/208/4029.html), [Jiale Du](https://dblp.org/pid/241/3709.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html), Jungong Han:

Hybrid Discriminative Attribute-Object Embedding Network for Compositional Zero-Shot Learning. [CoRRabs/2412.00121](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-00121) (2024)
- ![](https://dblp.org/img/n.png)

\[i64\]
[Ao Wang](https://dblp.org/pid/87/3443.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Jianchao Tan](https://dblp.org/pid/165/9938.html), [Kefeng Zhang](https://dblp.org/pid/84/5516.html), [Xunliang Cai](https://dblp.org/pid/294/8410.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

PrefixKV: Adaptive Prefix KV Cache is What Vision Instruction-Following Models Need for Efficient Generation. [CoRRabs/2412.03409](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-03409) (2024)
- ![](https://dblp.org/img/n.png)

\[i63\]
[Ao Wang](https://dblp.org/pid/87/3443.html), [Fengyuan Sun](https://dblp.org/pid/147/6919.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

\[CLS\] Token Tells Everything Needed for Training-free Efficient MLLMs. [CoRRabs/2412.05819](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-05819) (2024)
- ![](https://dblp.org/img/n.png)

\[i62\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html), [Chengxin Li](https://dblp.org/pid/166/6518.html), [Xiaohui Dong](https://dblp.org/pid/152/7855.html), [Lei Li](https://dblp.org/pid/13/7007.html), [Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Shoukun Xu](https://dblp.org/pid/73/7832.html), Jungong Han:

Seamless Detection: Unifying Salient Object Detection and Camouflaged Object Detection. [CoRRabs/2412.16840](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-16840) (2024)
- ![](https://dblp.org/img/n.png)

\[i61\]
[Lihao Liu](https://dblp.org/pid/21/309.html), [Juexiao Feng](https://dblp.org/pid/371/4491.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Ao Wang](https://dblp.org/pid/87/3443.html), [Lin Song](https://dblp.org/pid/49/1217-2.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

YOLO-UniOW: Efficient Universal Open-World Object Detection. [CoRRabs/2412.20645](https://dblp.org/db/journals/corr/corr2412.html#journals/corr/abs-2412-20645) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j183\]
[Mingqi Gao](https://dblp.org/pid/191/2698-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [James J. Q. Yu](https://dblp.org/pid/55/10087.html), [Caifeng Shan](https://dblp.org/pid/98/428.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Deep learning for video object segmentation: a review. [Artif. Intell. Rev.56(1)](https://dblp.org/db/journals/air/air56.html#journals/air/GaoZYSDH23): 457-531 (2023)
- ![](https://dblp.org/img/n.png)

\[j182\]
[Xiaowei Gu](https://dblp.org/pid/128/5017-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Qiang Shen](https://dblp.org/pid/s/QiangShen.html), [Plamen P. Angelov](https://dblp.org/pid/16/6228.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Autonomous learning for fuzzy systems: a review. [Artif. Intell. Rev.56(8)](https://dblp.org/db/journals/air/air56.html#journals/air/GuH0A23): 7549-7595 (2023)
- ![](https://dblp.org/img/n.png)

\[j181\]
[Xin Wang](https://dblp.org/pid/10/5630-121.html), [Ruisheng Su](https://dblp.org/pid/258/3495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weiyi Xie](https://dblp.org/pid/154/1297.html), [Wenjin Wang](https://dblp.org/pid/61/4908-2.html), [Yi Xu](https://dblp.org/pid/14/5580-1.html), [Ritse Mann](https://dblp.org/pid/137/8733.html), Jungong Han, [Tao Tan](https://dblp.org/pid/06/7832-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

2.75D: Boosting learning by representing 3D Medical imaging to 2D features for small data. [Biomed. Signal Process. Control.84](https://dblp.org/db/journals/bspc/bspc84.html#journals/bspc/WangSXWXMHT23): 104858 (2023)
- ![](https://dblp.org/img/n.png)

\[j180\]
[Shuo Zhang](https://dblp.org/pid/83/3714.html), [Mingqi Gao](https://dblp.org/pid/191/2698-3.html), [Qiang Ni](https://dblp.org/pid/87/3074.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Filter pruning with uniqueness mechanism in the frequency domain for efficient neural networks. [Neurocomputing530](https://dblp.org/db/journals/ijon/ijon530.html#journals/ijon/ZhangGNH23): 116-124 (2023)
- ![](https://dblp.org/img/n.png)

\[j179\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html), [Nianchang Huang](https://dblp.org/pid/258/2761.html), [Xiao Ma](https://dblp.org/pid/35/573-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han:

On exploring pose estimation as an auxiliary learning task for Visible-Infrared Person Re-identification. [Neurocomputing556](https://dblp.org/db/journals/ijon/ijon556.html#journals/ijon/MiaoHMZH23): 126652 (2023)
- ![](https://dblp.org/img/n.png)

\[j178\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html), [Jianan Liu](https://dblp.org/pid/146/6864.html), [Yunqi Miao](https://dblp.org/pid/207/3366.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Deep learning for visible-infrared cross-modality person re-identification: A comprehensive review. [Inf. Fusion91](https://dblp.org/db/journals/inffus/inffus91.html#journals/inffus/HuangLMZH23): 396-411 (2023)
- ![](https://dblp.org/img/n.png)

\[j177\]
[Heng Liu](https://dblp.org/pid/59/3260-2.html), [Jianyong Liu](https://dblp.org/pid/10/1468.html), [Shudong Hou](https://dblp.org/pid/28/8546.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tao Tao](https://dblp.org/pid/73/3197-5.html), Jungong Han:

Perception consistency ultrasound image super-resolution via self-supervised CycleGAN. [Neural Comput. Appl.35(17)](https://dblp.org/db/journals/nca/nca35.html#journals/nca/LiuLHTH23): 12331-12341 (2023)
- ![](https://dblp.org/img/n.png)

\[j176\]
[Mingqi Gao](https://dblp.org/pid/191/2698-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Feng Zheng](https://dblp.org/pid/39/800-1.html), [James J. Q. Yu](https://dblp.org/pid/55/10087.html), [Giovanni Montana](https://dblp.org/pid/89/449.html):

Video Object Segmentation using Point-based Memory Network. [Pattern Recognit.134](https://dblp.org/db/journals/pr/pr134.html#journals/pr/GaoHZYM23): 109073 (2023)
- ![](https://dblp.org/img/n.png)

\[j175\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html), [Jianan Liu](https://dblp.org/pid/146/6864.html), [Yongjiang Luo](https://dblp.org/pid/174/4309.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Exploring modality-shared appearance features and modality-invariant relation features for cross-modality person Re-IDentification. [Pattern Recognit.135](https://dblp.org/db/journals/pr/pr135.html#journals/pr/HuangLLZH23): 109145 (2023)
- ![](https://dblp.org/img/n.png)

\[j174\]
[De Cheng](https://dblp.org/pid/154/1991.html), [Gerong Wang](https://dblp.org/pid/289/1259.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bo Wang](https://dblp.org/pid/72/6811-11.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Dingwen Zhang](https://dblp.org/pid/150/6620.html):

Hybrid routing transformer for zero-shot learning. [Pattern Recognit.137](https://dblp.org/db/journals/pr/pr137.html#journals/pr/ChengWWZHZ23): 109270 (2023)
- ![](https://dblp.org/img/n.png)

\[j173\]
[Liuyu Xiang](https://dblp.org/pid/242/7959.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Margin-aware rectified augmentation for long-tailed recognition. [Pattern Recognit.141](https://dblp.org/db/journals/pr/pr141.html#journals/pr/XiangHD23): 109608 (2023)
- ![](https://dblp.org/img/n.png)

\[j172\]
[Xin Huang](https://dblp.org/pid/98/5766.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yutao Hu](https://dblp.org/pid/37/5215-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaoyan Luo](https://dblp.org/pid/28/7701.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xianbin Cao](https://dblp.org/pid/22/3485.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Boosting Variational Inference With Margin Learning for Few-Shot Scene-Adaptive Anomaly Detection. [IEEE Trans. Circuits Syst. Video Technol.33(6)](https://dblp.org/db/journals/tcsv/tcsv33.html#journals/tcsv/HuangHLHZC23): 2813-2825 (2023)
- ![](https://dblp.org/img/n.png)

\[j171\]
[Mingqi Gao](https://dblp.org/pid/191/2698-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jinyu Yang](https://dblp.org/pid/138/6456.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ke Lu](https://dblp.org/pid/33/1254-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Feng Zheng](https://dblp.org/pid/39/800-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Giovanni Montana](https://dblp.org/pid/89/449.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Decoupling Multimodal Transformers for Referring Video Object Segmentation. [IEEE Trans. Circuits Syst. Video Technol.33(9)](https://dblp.org/db/journals/tcsv/tcsv33.html#journals/tcsv/GaoYHLZM23): 4518-4528 (2023)
- ![](https://dblp.org/img/n.png)

\[j170\]
[Zhuoxu Huang](https://dblp.org/pid/331/8231.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhiyou Zhao](https://dblp.org/pid/331/8216.html), [Banghuai Li](https://dblp.org/pid/181/1410.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

LCPFormer: Towards Effective 3D Point Cloud Analysis via Local Context Propagation in Transformers. [IEEE Trans. Circuits Syst. Video Technol.33(9)](https://dblp.org/db/journals/tcsv/tcsv33.html#journals/tcsv/HuangZLH23): 4985-4996 (2023)
- ![](https://dblp.org/img/n.png)

\[j169\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Discriminative Cross-Aligned Variational Autoencoder for Zero-Shot Learning. [IEEE Trans. Cybern.53(6)](https://dblp.org/db/journals/tcyb/tcyb53.html#journals/tcyb/LiuGHS23): 3794-3805 (2023)
- ![](https://dblp.org/img/n.png)

\[j168\]
[Xiaowei Gu](https://dblp.org/pid/128/5017-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Plamen Angelov](https://dblp.org/pid/16/6228.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Qiang Shen](https://dblp.org/pid/s/QiangShen.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Multilayer Evolving Fuzzy Neural Networks. [IEEE Trans. Fuzzy Syst.31(12)](https://dblp.org/db/journals/tfs/tfs31.html#journals/tfs/GuAHS23): 4158-4169 (2023)
- ![](https://dblp.org/img/n.png)

\[j167\]
[Jia Li](https://dblp.org/pid/23/6950-32.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Junjie Zhang](https://dblp.org/pid/99/6243-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Chenggang Yan](https://dblp.org/pid/146/1605.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dan Zeng](https://dblp.org/pid/06/6575-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Progressive Recurrent Neural Network for Multispectral Remote Sensing Image Destriping. [IEEE Trans. Geosci. Remote. Sens.61](https://dblp.org/db/journals/tgrs/tgrs61.html#journals/tgrs/LiZHYZ23): 1-18 (2023)
- ![](https://dblp.org/img/n.png)

\[j166\]
[Jingkun Chen](https://dblp.org/pid/212/6645.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianguo Zhang](https://dblp.org/pid/90/6415-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kurt Debattista](https://dblp.org/pid/29/5944.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Semi-Supervised Unpaired Medical Image Segmentation Through Task-Affinity Consistency. [IEEE Trans. Medical Imaging42(3)](https://dblp.org/db/journals/tmi/tmi42.html#journals/tmi/ChenZDH23): 594-605 (2023)
- ![](https://dblp.org/img/n.png)

\[j165\]
[Jin Xie](https://dblp.org/pid/80/1949-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Nie](https://dblp.org/pid/39/5493-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiale Cao](https://dblp.org/pid/167/3851.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Latent Feature Pyramid Network for Object Detection. [IEEE Trans. Multim.25](https://dblp.org/db/journals/tmm/tmm25.html#journals/tmm/0005PNCH23): 2153-2163 (2023)
- ![](https://dblp.org/img/n.png)

\[j164\]
[Zhuang Shao](https://dblp.org/pid/51/9057.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Kurt Debattista](https://dblp.org/pid/29/5944.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Textual Context-Aware Dense Captioning With Diverse Words. [IEEE Trans. Multim.25](https://dblp.org/db/journals/tmm/tmm25.html#journals/tmm/ShaoHDP23): 8753-8766 (2023)
- ![](https://dblp.org/img/n.png)

\[j163\]
[Jiale Cao](https://dblp.org/pid/167/3851.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Hierarchical Regression and Classification for Accurate Object Detection. [IEEE Trans. Neural Networks Learn. Syst.34(5)](https://dblp.org/db/journals/tnn/tnn34.html#journals/tnn/CaoPHL23): 2425-2439 (2023)
- ![](https://dblp.org/img/n.png)

\[j162\]
[Yunlong Yu](https://dblp.org/pid/45/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bin Li](https://dblp.org/pid/89/6764-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Zhongfei Zhang](https://dblp.org/pid/z/ZhongfeiMarkZhang.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Knowledge Distillation Classifier Generation Network for Zero-Shot Learning. [IEEE Trans. Neural Networks Learn. Syst.34(6)](https://dblp.org/db/journals/tnn/tnn34.html#journals/tnn/YuLJHZ23): 3183-3194 (2023)
- ![](https://dblp.org/img/n.png)

\[j161\]
[Jin Xie](https://dblp.org/pid/80/1949-5.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), [Jing Pan](https://dblp.org/pid/13/718.html), [Jing Nie](https://dblp.org/pid/39/5493-1.html), [Jiale Cao](https://dblp.org/pid/167/3851.html), Jungong Han:

Complementary Feature Pyramid Network for Object Detection. [ACM Trans. Multim. Comput. Commun. Appl.19(6)](https://dblp.org/db/journals/tomccap/tomccap19.html#journals/tomccap/XiePPNCH23): 1-15 (2023)
- ![](https://dblp.org/img/n.png)

\[c101\]
[Zixuan Ding](https://dblp.org/pid/230/1821.html), [Ao Wang](https://dblp.org/pid/87/3443.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Pengzhang Liu](https://dblp.org/pid/44/7674.html), [Yongjun Bao](https://dblp.org/pid/52/5055.html), [Weipeng Yan](https://dblp.org/pid/216/8297.html), Jungong Han:

Exploring Structured Semantic Prior for Multi Label Recognition with Incomplete Labels. [CVPR2023](https://dblp.org/db/conf/cvpr/cvpr2023.html#conf/cvpr/DingWCZLBYH23): 3398-3407
- ![](https://dblp.org/img/n.png)

\[c100\]
[Tianlu Zhang](https://dblp.org/pid/255/8662.html), [Hongyuan Guo](https://dblp.org/pid/336/9827.html), [Qiang Jiao](https://dblp.org/pid/166/3845.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han:

Efficient RGB-T Tracking via Cross-Modality Distillation. [CVPR2023](https://dblp.org/db/conf/cvpr/cvpr2023.html#conf/cvpr/ZhangGJZH23): 5404-5413
- ![](https://dblp.org/img/n.png)

\[c99\]
[Yutao Hu](https://dblp.org/pid/37/5215-2.html), [Qixiong Wang](https://dblp.org/pid/285/7078.html), [Wenqi Shao](https://dblp.org/pid/227/3122.html), [Enze Xie](https://dblp.org/pid/218/5441.html), [Zhenguo Li](https://dblp.org/pid/23/6479.html), Jungong Han, [Ping Luo](https://dblp.org/pid/54/4989-2.html):

Beyond One-to-One: Rethinking the Referring Image Segmentation. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/HuWSXLHL23): 4044-4054
- ![](https://dblp.org/img/n.png)

\[c98\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Honghao Chen](https://dblp.org/pid/279/9807.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), [Kaiqi Huang](https://dblp.org/pid/89/7026.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Re-parameterizing Your Optimizers rather than Architectures. [ICLR2023](https://dblp.org/db/conf/iclr/iclr2023.html#conf/iclr/DingC0HHD23)
- ![](https://dblp.org/img/n.png)

\[i60\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html), [Shoukun Xu](https://dblp.org/pid/73/7832.html), [Dingwen Zhang](https://dblp.org/pid/150/6620.html), Jungong Han:

SegGPT Meets Co-Saliency Scene. [CoRRabs/2305.04396](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-04396) (2023)
- ![](https://dblp.org/img/n.png)

\[i59\]
[Shaohui Lin](https://dblp.org/pid/183/0917.html), [Wenxuan Huang](https://dblp.org/pid/192/1157-1.html), [Jiao Xie](https://dblp.org/pid/171/5781.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Yunhang Shen](https://dblp.org/pid/146/1800.html), [Zhou Yu](https://dblp.org/pid/83/3205.html), Jungong Han, [David S. Doermann](https://dblp.org/pid/88/6921.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Filter Pruning for Efficient CNNs via Knowledge-driven Differential Filter Sampler. [CoRRabs/2307.00198](https://dblp.org/db/journals/corr/corr2307.html#journals/corr/abs-2307-00198) (2023)
- ![](https://dblp.org/img/n.png)

\[i58\]
[Hao Chen](https://dblp.org/pid/175/3324-107.html), [Yonghan Dong](https://dblp.org/pid/342/4266.html), [Zheming Lu](https://dblp.org/pid/148/1888-1.html), [Yunlong Yu](https://dblp.org/pid/45/7404.html), [Yingming Li](https://dblp.org/pid/119/1901.html), Jungong Han, [Zhongfei Zhang](https://dblp.org/pid/z/ZhongfeiMarkZhang.html):

Dense Affinity Matching for Few-Shot Segmentation. [CoRRabs/2307.08434](https://dblp.org/db/journals/corr/corr2307.html#journals/corr/abs-2307-08434) (2023)
- ![](https://dblp.org/img/n.png)

\[i57\]
[Yutao Hu](https://dblp.org/pid/37/5215-2.html), [Qixiong Wang](https://dblp.org/pid/285/7078.html), [Wenqi Shao](https://dblp.org/pid/227/3122.html), [Enze Xie](https://dblp.org/pid/218/5441.html), [Zhenguo Li](https://dblp.org/pid/23/6479.html), Jungong Han, [Ping Luo](https://dblp.org/pid/54/4989-2.html):

Beyond One-to-One: Rethinking the Referring Image Segmentation. [CoRRabs/2308.13853](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-13853) (2023)
- ![](https://dblp.org/img/n.png)

\[i56\]
[Ao Wang](https://dblp.org/pid/87/3443.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

CAIT: Triple-Win Compression towards High Accuracy, Fast Inference, and Favorable Transferability For ViTs. [CoRRabs/2309.15755](https://dblp.org/db/journals/corr/corr2309.html#journals/corr/abs-2309-15755) (2023)
- ![](https://dblp.org/img/n.png)

\[i55\]
[Changrui Chen](https://dblp.org/pid/232/4719.html), Jungong Han, [Kurt Debattista](https://dblp.org/pid/29/5944.html):

Virtual Category Learning: A Semi-Supervised Learning Method for Dense Prediction with Extremely Limited Labels. [CoRRabs/2312.01169](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-01169) (2023)
- ![](https://dblp.org/img/n.png)

\[i54\]
[Ao Wang](https://dblp.org/pid/87/3443.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

RepViT-SAM: Towards Real-Time Segmenting Anything. [CoRRabs/2312.05760](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-05760) (2023)
- ![](https://dblp.org/img/n.png)

\[i53\]
[Tianxiang Hao](https://dblp.org/pid/270/0611-1.html), [Mengyao Lyu](https://dblp.org/pid/244/8467.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Re-parameterized Low-rank Prompt: Generalize a Vision-Language Model within 0.5K Parameters. [CoRRabs/2312.10813](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-10813) (2023)
- ![](https://dblp.org/img/n.png)

\[i52\]
[Mengyao Lyu](https://dblp.org/pid/244/8467.html), [Yuhong Yang](https://dblp.org/pid/365/8877.html), [Haiwen Hong](https://dblp.org/pid/297/4419.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Xuan Jin](https://dblp.org/pid/80/5681.html), [Yuan He](https://dblp.org/pid/11/1735-11.html), [Hui Xue](https://dblp.org/pid/27/3541-1.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

One-dimensional Adapter to Rule Them All: Concepts, Diffusion Models and Erasing Applications. [CoRRabs/2312.16145](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-16145) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j160\]
[Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Bo Wang](https://dblp.org/pid/72/6811-11.html), [Gerong Wang](https://dblp.org/pid/289/1259.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Jiajia Zhang](https://dblp.org/pid/08/267.html), Jungong Han, [Zheng You](https://dblp.org/pid/04/2178.html):

Onfocus detection: identifying individual-camera eye contact from unconstrained images. [Sci. China Inf. Sci.65(6)](https://dblp.org/db/journals/chinaf/chinaf65.html#journals/chinaf/ZhangWWZZHY22): 1-12 (2022)
- ![](https://dblp.org/img/n.png)

\[j159\]
[Chaowei Fang](https://dblp.org/pid/159/1655.html), [Haibin Tian](https://dblp.org/pid/280/1349.html), [Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han, [Junwei Han](https://dblp.org/pid/00/3003.html):

Densely nested top-down flows for salient object detection. [Sci. China Inf. Sci.65(8)](https://dblp.org/db/journals/chinaf/chinaf65.html#journals/chinaf/FangTZZHH22): 1-14 (2022)
- ![](https://dblp.org/img/n.png)

\[j158\]
[Yuezhong Chu](https://dblp.org/pid/228/7471.html), [Yunan Qiao](https://dblp.org/pid/320/9668.html), [Heng Liu](https://dblp.org/pid/59/3260-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Dual Attention with the Self-Attention Alignment for Efficient Video Super-resolution. [Cogn. Comput.14(3)](https://dblp.org/db/journals/cogcom/cogcom14.html#journals/cogcom/ChuQLH22): 1140-1151 (2022)
- ![](https://dblp.org/img/n.png)

\[j157\]
[Yinghui Kong](https://dblp.org/pid/23/867.html), [Shuaitong Zhang](https://dblp.org/pid/239/1871.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ke Zhang](https://dblp.org/pid/20/4152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Ni](https://dblp.org/pid/87/3074.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Real-time facial expression recognition based on iterative transfer learning and efficient attention network. [IET Image Process.16(6)](https://dblp.org/db/journals/iet-ipr/iet-ipr16.html#journals/iet-ipr/KongZZNH22): 1694-1708 (2022)
- ![](https://dblp.org/img/n.png)

\[j156\]
[Yan Xu](https://dblp.org/pid/03/4702.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lifu Mu](https://dblp.org/pid/322/8822.html), [Zhong Ji](https://dblp.org/pid/36/6466.html), [Xiyao Liu](https://dblp.org/pid/138/9719-2.html), Jungong Han:

Meta hyperbolic networks for zero-shot learning. [Neurocomputing491](https://dblp.org/db/journals/ijon/ijon491.html#journals/ijon/XuMJLH22): 57-66 (2022)
- ![](https://dblp.org/img/n.png)

\[j155\]
[Yu Fu](https://dblp.org/pid/09/3263-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liuyu Xiang](https://dblp.org/pid/242/7959.html), [Yumna Zahid](https://dblp.org/pid/227/0373.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Tao Mei](https://dblp.org/pid/12/5444-1.html), [Qiang Shen](https://dblp.org/pid/s/QiangShen.html), Jungong Han:

Long-tailed visual recognition with deep models: A methodological survey and evaluation. [Neurocomputing509](https://dblp.org/db/journals/ijon/ijon509.html#journals/ijon/FuXZDMSH22): 290-309 (2022)
- ![](https://dblp.org/img/n.png)

\[j154\]
[Xiaowei Gu](https://dblp.org/pid/128/5017-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ce Zhang](https://dblp.org/pid/97/919-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Shen](https://dblp.org/pid/s/QiangShen.html), Jungong Han, [Plamen P. Angelov](https://dblp.org/pid/16/6228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peter M. Atkinson](https://dblp.org/pid/74/41.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Self-Training Hierarchical Prototype-based Ensemble Framework for Remote Sensing Scene Classification. [Inf. Fusion80](https://dblp.org/db/journals/inffus/inffus80.html#journals/inffus/GuZSHAA22): 179-204 (2022)
- ![](https://dblp.org/img/n.png)

\[j153\]
[Wei Xia](https://dblp.org/pid/77/1243-7.html), [Sen Wang](https://dblp.org/pid/69/6403.html), [Ming Yang](https://dblp.org/pid/98/2604-24.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Quanxue Gao](https://dblp.org/pid/63/804.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Xinbo Gao](https://dblp.org/pid/99/4522.html):

Multi-view graph embedding clustering network: Joint self-supervision and block diagonal representation. [Neural Networks145](https://dblp.org/db/journals/nn/nn145.html#journals/nn/XiaWYGHG22): 1-9 (2022)
- ![](https://dblp.org/img/n.png)

\[j152\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Part-Object Relational Visual Saliency. [IEEE Trans. Pattern Anal. Mach. Intell.44(7)](https://dblp.org/db/journals/pami/pami44.html#journals/pami/LiuZZH22): 3688-3704 (2022)
- ![](https://dblp.org/img/n.png)

\[j151\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html), Jungong Han, [Li Liu](https://dblp.org/pid/33/4528-4.html), [Ling Shao](https://dblp.org/pid/75/1281.html):

Zero-shot learning via a specific rank-controlled semantic autoencoder. [Pattern Recognit.122](https://dblp.org/db/journals/pr/pr122.html#journals/pr/LiuGHLS22): 108237 (2022)
- ![](https://dblp.org/img/n.png)

\[j150\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html), [Yongjiang Luo](https://dblp.org/pid/174/4309.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han:

Discriminative unimodal feature selection and fusion for RGB-D salient object detection. [Pattern Recognit.122](https://dblp.org/db/journals/pr/pr122.html#journals/pr/HuangLZH22): 108359 (2022)
- ![](https://dblp.org/img/n.png)

\[j149\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html), [Kunlong Liu](https://dblp.org/pid/274/2407.html), [Yang Liu](https://dblp.org/pid/51/3710-0069.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Cross-modality person re-identification via multi-task learning. [Pattern Recognit.128](https://dblp.org/db/journals/pr/pr128.html#journals/pr/HuangLLZH22): 108653 (2022)
- ![](https://dblp.org/img/n.png)

\[j148\]
[Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han, [Xin Lu](https://dblp.org/pid/11/1952.html), [Nicola Conci](https://dblp.org/pid/32/3652.html):

Editorial for the special issue on deep learning for precise and efficient object detection. [Pattern Recognit. Lett.162](https://dblp.org/db/journals/prl/prl162.html#journals/prl/PangHLC22): 7-8 (2022)
- ![](https://dblp.org/img/n.png)

\[j147\]
[Jia Li](https://dblp.org/pid/23/6950-32.html), [Dan Zeng](https://dblp.org/pid/06/6575-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Junjie Zhang](https://dblp.org/pid/99/6243-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Tao Mei](https://dblp.org/pid/12/5444-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Column-Spatial Correction Network for Remote Sensing Image Destriping. [Remote. Sens.14(14)](https://dblp.org/db/journals/remotesensing/remotesensing14.html#journals/remotesensing/LiZ0H022): 3376 (2022)
- ![](https://dblp.org/img/n.png)

\[j146\]
[Dewei Yi](https://dblp.org/pid/181/0412.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Fang](https://dblp.org/pid/03/2511-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yining Hua](https://dblp.org/pid/220/1318.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jinya Su](https://dblp.org/pid/131/9643.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mohammed Quddus](https://dblp.org/pid/38/7133.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Improving Synthetic to Realistic Semantic Segmentation With Parallel Generative Ensembles for Autonomous Urban Driving. [IEEE Trans. Cogn. Dev. Syst.14(4)](https://dblp.org/db/journals/tamd/tamd14.html#journals/tamd/YiFHSQH22): 1496-1506 (2022)
- ![](https://dblp.org/img/n.png)

\[j145\]
[Tianlu Zhang](https://dblp.org/pid/255/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xueru Liu](https://dblp.org/pid/316/3084.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

SiamCDA: Complementarity- and Distractor-Aware RGB-T Tracking Based on Siamese Network. [IEEE Trans. Circuits Syst. Video Technol.32(3)](https://dblp.org/db/journals/tcsv/tcsv32.html#journals/tcsv/ZhangLZH22): 1403-1417 (2022)
- ![](https://dblp.org/img/n.png)

\[j144\]
[Jing Nie](https://dblp.org/pid/39/5493-1.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), [Jin Xie](https://dblp.org/pid/80/1949-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Pan](https://dblp.org/pid/13/718.html), Jungong Han:

Stereo Refinement Dehazing Network. [IEEE Trans. Circuits Syst. Video Technol.32(6)](https://dblp.org/db/journals/tcsv/tcsv32.html#journals/tcsv/NiePXPH22): 3334-3345 (2022)
- ![](https://dblp.org/img/n.png)

\[j143\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mingxing Duanmu](https://dblp.org/pid/285/6888.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yongjiang Luo](https://dblp.org/pid/174/4309.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Engaging Part-Whole Hierarchies and Contrast Cues for Salient Object Detection. [IEEE Trans. Circuits Syst. Video Technol.32(6)](https://dblp.org/db/journals/tcsv/tcsv32.html#journals/tcsv/ZhangDLLH22): 3644-3658 (2022)
- ![](https://dblp.org/img/n.png)

\[j142\]
[Yang Yang](https://dblp.org/pid/48/450-132.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qi Qin](https://dblp.org/pid/143/4836.html), [Yongjiang Luo](https://dblp.org/pid/174/4309.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Bi-Directional Progressive Guidance Network for RGB-D Salient Object Detection. [IEEE Trans. Circuits Syst. Video Technol.32(8)](https://dblp.org/db/journals/tcsv/tcsv32.html#journals/tcsv/YangQLLZH22): 5346-5360 (2022)
- ![](https://dblp.org/img/n.png)

\[j141\]
[Jianan Liu](https://dblp.org/pid/146/6864.html), [Jialiang Wang](https://dblp.org/pid/27/8578.html), [Nianchang Huang](https://dblp.org/pid/258/2761.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Revisiting Modality-Specific Feature Compensation for Visible-Infrared Person Re-Identification. [IEEE Trans. Circuits Syst. Video Technol.32(10)](https://dblp.org/db/journals/tcsv/tcsv32.html#journals/tcsv/LiuWHZH22): 7226-7240 (2022)
- ![](https://dblp.org/img/n.png)

\[j140\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haoran Wang](https://dblp.org/pid/28/3021-4.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png):

SMAN: Stacked Multimodal Attention Network for Cross-Modal Image-Text Retrieval. [IEEE Trans. Cybern.52(2)](https://dblp.org/db/journals/tcyb/tcyb52.html#journals/tcyb/JiWHP22): 1086-1097 (2022)
- ![](https://dblp.org/img/n.png)

\[j139\]
[Xiyao Liu](https://dblp.org/pid/138/9719-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

DGIG-Net: Dynamic Graph-in-Graph Networks for Few-Shot Human-Object Interaction. [IEEE Trans. Cybern.52(8)](https://dblp.org/db/journals/tcyb/tcyb52.html#journals/tcyb/LiuJPHL22): 7852-7864 (2022)
- ![](https://dblp.org/img/n.png)

\[j138\]
[Wei Xia](https://dblp.org/pid/77/1243-7.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiangdong Zhang](https://dblp.org/pid/26/1791.html), [Quanxue Gao](https://dblp.org/pid/63/804.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaochuang Shu](https://dblp.org/pid/325/3814.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Multiview Subspace Clustering by an Enhanced Tensor Nuclear Norm. [IEEE Trans. Cybern.52(9)](https://dblp.org/db/journals/tcyb/tcyb52.html#journals/tcyb/XiaZGSHG22): 8962-8975 (2022)
- ![](https://dblp.org/img/n.png)

\[j137\]
[Xiaoxu Feng](https://dblp.org/pid/253/1916.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiwen Yao](https://dblp.org/pid/163/0541.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Gong Cheng](https://dblp.org/pid/69/1215-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Junwei Han](https://dblp.org/pid/00/3003.html)![](https://dblp.org/img/orcid-mark.12x12.png):

SAENet: Self-Supervised Adversarial and Equivariant Network for Weakly Supervised Object Detection in Remote Sensing Images. [IEEE Trans. Geosci. Remote. Sens.60](https://dblp.org/db/journals/tgrs/tgrs60.html#journals/tgrs/FengYCHH22): 1-11 (2022)
- ![](https://dblp.org/img/n.png)

\[j136\]
[Yutao Hu](https://dblp.org/pid/37/5215-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Huang](https://dblp.org/pid/98/5766.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaoyan Luo](https://dblp.org/pid/28/7701.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Xianbin Cao](https://dblp.org/pid/22/3485.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Zhang](https://dblp.org/pid/z/JunZhang7.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Variational Self-Distillation for Remote Sensing Scene Classification. [IEEE Trans. Geosci. Remote. Sens.60](https://dblp.org/db/journals/tgrs/tgrs60.html#journals/tgrs/HuHLHCZ22): 1-13 (2022)
- ![](https://dblp.org/img/n.png)

\[j135\]
[Lingjun Li](https://dblp.org/pid/39/201.html), [Xiwen Yao](https://dblp.org/pid/163/0541.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Gong Cheng](https://dblp.org/pid/69/1215-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mingliang Xu](https://dblp.org/pid/13/8698-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Junwei Han](https://dblp.org/pid/00/3003.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Solo-to-Collaborative Dual-Attention Network for One-Shot Object Detection in Remote Sensing Images. [IEEE Trans. Geosci. Remote. Sens.60](https://dblp.org/db/journals/tgrs/tgrs60.html#journals/tgrs/LiYCXHH22): 1-11 (2022)
- ![](https://dblp.org/img/n.png)

\[j134\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhishen Hou](https://dblp.org/pid/301/8258.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiyao Liu](https://dblp.org/pid/138/9719-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Information Symmetry Matters: A Modal-Alternating Propagation Network for Few-Shot Learning. [IEEE Trans. Image Process.31](https://dblp.org/db/journals/tip/tip31.html#journals/tip/JiHLPH22): 1520-1531 (2022)
- ![](https://dblp.org/img/n.png)

\[j133\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Jiao](https://dblp.org/pid/166/3845.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Middle-Level Feature Fusion for Lightweight RGB-D Salient Object Detection. [IEEE Trans. Image Process.31](https://dblp.org/db/journals/tip/tip31.html#journals/tip/HuangJ0H22): 6621-6634 (2022)
- ![](https://dblp.org/img/n.png)

\[j132\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dingwen Zhang](https://dblp.org/pid/150/6620.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Nian Liu](https://dblp.org/pid/30/2704-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shoukun Xu](https://dblp.org/pid/73/7832.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Disentangled Capsule Routing for Fast Part-Object Relational Saliency. [IEEE Trans. Image Process.31](https://dblp.org/db/journals/tip/tip31.html#journals/tip/LiuZLXH22): 6719-6732 (2022)
- ![](https://dblp.org/img/n.png)

\[j131\]
[Tao Tan](https://dblp.org/pid/06/7832-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ravi Soni](https://dblp.org/pid/249/3157.html), Jungong Han, [Shuo Li](https://dblp.org/pid/49/595-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Guest Editorial Artificial Intelligence in Pre-DICOM. [IEEE J. Biomed. Health Informatics26(9)](https://dblp.org/db/journals/titb/titb26.html#journals/titb/TanSHL22): 4357-4358 (2022)
- ![](https://dblp.org/img/n.png)

\[j130\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Yang](https://dblp.org/pid/48/450-132.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dingwen Zhang](https://dblp.org/pid/150/6620.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Employing Bilinear Fusion and Saliency Prior Information for RGB-D Salient Object Detection. [IEEE Trans. Multim.24](https://dblp.org/db/journals/tmm/tmm24.html#journals/tmm/HuangYZZH22): 1651-1664 (2022)
- ![](https://dblp.org/img/n.png)

\[j129\]
[Ce Li](https://dblp.org/pid/58/411-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chunyu Xie](https://dblp.org/pid/187/1594.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Xiantong Zhen](https://dblp.org/pid/78/10651.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Chen](https://dblp.org/pid/92/6289-1.html):

Memory Attention Networks for Skeleton-Based Action Recognition. [IEEE Trans. Neural Networks Learn. Syst.33(9)](https://dblp.org/db/journals/tnn/tnn33.html#journals/tnn/LiXZHZC22): 4800-4814 (2022)
- ![](https://dblp.org/img/n.png)

\[c97\]
[Liuyu Xiang](https://dblp.org/pid/242/7959.html), [Jundong Zhou](https://dblp.org/pid/263/7754.html), [Jirui Liu](https://dblp.org/pid/302/7791.html), [Zerun Wang](https://dblp.org/pid/260/7013.html), [Haidong Huang](https://dblp.org/pid/245/4034.html), [Jie Hu](https://dblp.org/pid/90/5064-21.html), Jungong Han, [Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html):

ReMoNet: Recurrent Multi-Output Network for Efficient Video Denoising. [AAAI2022](https://dblp.org/db/conf/aaai/aaai2022.html#conf/aaai/XiangZLWHHHGD22): 2786-2794
- ![](https://dblp.org/img/n.png)

\[c96\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Honghao Chen](https://dblp.org/pid/279/9807.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

RepMLPNet: Hierarchical Vision MLP with Re-parameterized Locality. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/DingC0HD22): 568-577
- ![](https://dblp.org/img/n.png)

\[c95\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Changzhou Lai](https://dblp.org/pid/330/1965.html), [Jianan Liu](https://dblp.org/pid/146/6864.html), [Nianchang Huang](https://dblp.org/pid/258/2761.html), Jungong Han:

FMCNet: Feature-Level Modality Compensation for Visible-Infrared Person Re-Identification. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/ZhangLLHH22): 7339-7348
- ![](https://dblp.org/img/n.png)

\[c94\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Scaling Up Your Kernels to 31×31: Revisiting Large Kernel Design in CNNs. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/Ding0HD22): 11953-11965
- ![](https://dblp.org/img/n.png)

\[c93\]
[Changrui Chen](https://dblp.org/pid/232/4719.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kurt Debattista](https://dblp.org/pid/29/5944.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Semi-supervised Object Detection via VC Learning. [ECCV (31)2022](https://dblp.org/db/conf/eccv/eccv2022-31.html#conf/eccv/ChenDH22): 169-185
- ![](https://dblp.org/img/n.png)

\[c92\]
[Boyang Xia](https://dblp.org/pid/289/2080.html), [Zhihao Wang](https://dblp.org/pid/52/253.html), [Wenhao Wu](https://dblp.org/pid/149/0005.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haoran Wang](https://dblp.org/pid/28/3021-4.html), Jungong Han:

Temporal Saliency Query Network for Efficient Video Recognition. [ECCV (34)2022](https://dblp.org/db/conf/eccv/eccv2022-34.html#conf/eccv/XiaWWWH22): 741-759
- ![](https://dblp.org/img/n.png)

\[c91\]
[Xiaodong Chen](https://dblp.org/pid/70/4319-11.html), [Wu Liu](https://dblp.org/pid/31/4112-5.html), [Xinchen Liu](https://dblp.org/pid/36/2028.html), [Yongdong Zhang](https://dblp.org/pid/z/YongdongZhang.html), Jungong Han, [Tao Mei](https://dblp.org/pid/12/5444-1.html):

MAPLE: Masked Pseudo-Labeling autoEncoder for Semi-supervised Point Cloud Action Recognition. [ACM Multimedia2022](https://dblp.org/db/conf/mm/mm2022.html#conf/mm/ChenLL0H022): 708-718
- ![](https://dblp.org/img/n.png)

\[c90\]
[Haoran Wang](https://dblp.org/pid/28/3021-4.html), [Di Xu](https://dblp.org/pid/95/7448.html), [Dongliang He](https://dblp.org/pid/167/0539.html), [Fu Li](https://dblp.org/pid/37/4556-3.html), [Zhong Ji](https://dblp.org/pid/36/6466.html), Jungong Han, [Errui Ding](https://dblp.org/pid/180/5531.html):

Boosting Video-Text Retrieval with Explicit High-Level Semantics. [ACM Multimedia2022](https://dblp.org/db/conf/mm/mm2022.html#conf/mm/WangXHLJHD22): 4887-4898
- ![](https://dblp.org/img/n.png)

\[c89\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html), [Alexandros Lattas](https://dblp.org/pid/221/0633.html), [Jiankang Deng](https://dblp.org/pid/156/7808.html), Jungong Han, [Stefanos Zafeiriou](https://dblp.org/pid/25/1885.html):

Physically-Based Face Rendering for NIR-VIS Face Recognition. [NeurIPS2022](https://dblp.org/db/conf/nips/neurips2022.html#conf/nips/MiaoLDHZ22)
- ![](https://dblp.org/img/n.png)

\[c88\]
[Yumna Zahid](https://dblp.org/pid/227/0373.html), [Muhammad Atif Tahir](https://dblp.org/pid/73/1942.html), Jungong Han, [Qiang Shen](https://dblp.org/pid/s/QiangShen.html):

Laplacian Regularized Variational Few-Shot Learning for Image Classification. [UKCI2022](https://dblp.org/db/conf/ukci/ukci2022.html#conf/ukci/ZahidTH022): 105-116
- ![](https://dblp.org/img/n.png)

\[i51\]
[Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Guohai Huang](https://dblp.org/pid/275/3809.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han, [Junwei Han](https://dblp.org/pid/00/3003.html), [Yizhou Yu](https://dblp.org/pid/90/6896.html):

Cross-Modality Deep Feature Learning for Brain Tumor Segmentation. [CoRRabs/2201.02356](https://dblp.org/db/journals/corr/corr2201.html#journals/corr/abs-2201-02356) (2022)
- ![](https://dblp.org/img/n.png)

\[i50\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html), [Nianchang Huang](https://dblp.org/pid/258/2761.html), [Xiao Ma](https://dblp.org/pid/35/573-13.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han:

On Exploring Pose Estimation as an Auxiliary Learning Task for Visible-Infrared Person Re-identification. [CoRRabs/2201.03859](https://dblp.org/db/journals/corr/corr2201.html#journals/corr/abs-2201-03859) (2022)
- ![](https://dblp.org/img/n.png)

\[i49\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), [Yizhuang Zhou](https://dblp.org/pid/315/9514.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html), [Jian Sun](https://dblp.org/pid/68/4942-1.html):

Scaling Up Your Kernels to 31x31: Revisiting Large Kernel Design in CNNs. [CoRRabs/2203.06717](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-06717) (2022)
- ![](https://dblp.org/img/n.png)

\[i48\]
[De Cheng](https://dblp.org/pid/154/1991.html), [Gerong Wang](https://dblp.org/pid/289/1259.html), [Bo Wang](https://dblp.org/pid/72/6811-11.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han, [Dingwen Zhang](https://dblp.org/pid/150/6620.html):

Hybrid Routing Transformer for Zero-Shot Learning. [CoRRabs/2203.15310](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-15310) (2022)
- ![](https://dblp.org/img/n.png)

\[i47\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Honghao Chen](https://dblp.org/pid/279/9807.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), [Kaiqi Huang](https://dblp.org/pid/89/7026.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Re-parameterizing Your Optimizers rather than Architectures. [CoRRabs/2205.15242](https://dblp.org/db/journals/corr/corr2205.html#journals/corr/abs-2205-15242) (2022)
- ![](https://dblp.org/img/n.png)

\[i46\]
[Changrui Chen](https://dblp.org/pid/232/4719.html), [Kurt Debattista](https://dblp.org/pid/29/5944.html), Jungong Han:

Semi-supervised Object Detection via Virtual Category Learning. [CoRRabs/2207.03433](https://dblp.org/db/journals/corr/corr2207.html#journals/corr/abs-2207-03433) (2022)
- ![](https://dblp.org/img/n.png)

\[i45\]
[Boyang Xia](https://dblp.org/pid/289/2080.html), [Zhihao Wang](https://dblp.org/pid/52/253.html), [Wenhao Wu](https://dblp.org/pid/149/0005.html), [Haoran Wang](https://dblp.org/pid/28/3021-4.html), Jungong Han:

Temporal Saliency Query Network for Efficient Video Recognition. [CoRRabs/2207.10379](https://dblp.org/db/journals/corr/corr2207.html#journals/corr/abs-2207-10379) (2022)
- ![](https://dblp.org/img/n.png)

\[i44\]
[Haoran Wang](https://dblp.org/pid/28/3021-4.html), [Di Xu](https://dblp.org/pid/95/7448.html), [Dongliang He](https://dblp.org/pid/167/0539.html), [Fu Li](https://dblp.org/pid/37/4556-3.html), [Zhong Ji](https://dblp.org/pid/36/6466.html), Jungong Han, [Errui Ding](https://dblp.org/pid/180/5531.html):

Boosting Video-Text Retrieval with Explicit High-Level Semantics. [CoRRabs/2208.04215](https://dblp.org/db/journals/corr/corr2208.html#journals/corr/abs-2208-04215) (2022)
- ![](https://dblp.org/img/n.png)

\[i43\]
[Xiaodong Chen](https://dblp.org/pid/70/4319-11.html), [Wu Liu](https://dblp.org/pid/31/4112-5.html), [Xinchen Liu](https://dblp.org/pid/36/2028.html), [Yongdong Zhang](https://dblp.org/pid/z/YongdongZhang.html), Jungong Han, [Tao Mei](https://dblp.org/pid/12/5444-1.html):

MAPLE: Masked Pseudo-Labeling autoEncoder for Semi-supervised Point Cloud Action Recognition. [CoRRabs/2209.00407](https://dblp.org/db/journals/corr/corr2209.html#journals/corr/abs-2209-00407) (2022)
- ![](https://dblp.org/img/n.png)

\[i42\]
[Zhuoxu Huang](https://dblp.org/pid/331/8231.html), [Zhiyou Zhao](https://dblp.org/pid/331/8216.html), [Banghuai Li](https://dblp.org/pid/181/1410.html), Jungong Han:

LCPFormer: Towards Effective 3D Point Cloud Analysis via Local Context Propagation in Transformers. [CoRRabs/2210.12755](https://dblp.org/db/journals/corr/corr2210.html#journals/corr/abs-2210-12755) (2022)
- ![](https://dblp.org/img/n.png)

\[i41\]
[Fan Yang](https://dblp.org/pid/29/3081-83.html), [Xinhao Xu](https://dblp.org/pid/58/8844.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), Jungong Han, [Kai Ni](https://dblp.org/pid/46/3815.html), [Guiguang Ding](https://dblp.org/pid/51/740.html):

Ground Plane Matters: Picking Up Ground Plane Prior in Monocular 3D Object Detection. [CoRRabs/2211.01556](https://dblp.org/db/journals/corr/corr2211.html#journals/corr/abs-2211-01556) (2022)
- ![](https://dblp.org/img/n.png)

\[i40\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html), [Alexandros Lattas](https://dblp.org/pid/221/0633.html), [Jiankang Deng](https://dblp.org/pid/156/7808.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Stefanos Zafeiriou](https://dblp.org/pid/25/1885.html):

Physically-Based Face Rendering for NIR-VIS Face Recognition. [CoRRabs/2211.06408](https://dblp.org/db/journals/corr/corr2211.html#journals/corr/abs-2211-06408) (2022)
- ![](https://dblp.org/img/n.png)

\[i39\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html), [Jiankang Deng](https://dblp.org/pid/156/7808.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

Confidence-guided Centroids for Unsupervised Person Re-Identification. [CoRRabs/2211.11921](https://dblp.org/db/journals/corr/corr2211.html#journals/corr/abs-2211-11921) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[j128\]
[Nan Xing](https://dblp.org/pid/61/3825.html), [Yang Liu](https://dblp.org/pid/51/3710-0069.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hong Zhu](https://dblp.org/pid/55/521-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Wang](https://dblp.org/pid/02/736-136.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Zero-Shot Learning via Discriminative Dual Semantic Auto-Encoder. [IEEE Access9](https://dblp.org/db/journals/access/access9.html#journals/access/XingLZWH21): 733-742 (2021)
- ![](https://dblp.org/img/n.png)

\[j127\]
[Caifeng Shan](https://dblp.org/pid/98/428.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tao Tan](https://dblp.org/pid/06/7832-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Di Huang](https://dblp.org/pid/45/780-1.html):

Ultrasound tissue classification: a review. [Artif. Intell. Rev.54(4)](https://dblp.org/db/journals/air/air54.html#journals/air/ShanTH021): 3055-3088 (2021)
- ![](https://dblp.org/img/n.png)

\[j126\]
[Hui Chen](https://dblp.org/pid/12/417-13.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), [Caifeng Shan](https://dblp.org/pid/98/428.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Image Captioning with Memorized Knowledge. [Cogn. Comput.13(4)](https://dblp.org/db/journals/cogcom/cogcom13.html#journals/cogcom/ChenDLGSH21): 807-820 (2021)
- ![](https://dblp.org/img/n.png)

\[j125\]
[Yinghui Kong](https://dblp.org/pid/23/867.html), [Zhaohan Ren](https://dblp.org/pid/305/9069.html), [Ke Zhang](https://dblp.org/pid/20/4152-5.html), [Shuaitong Zhang](https://dblp.org/pid/239/1871.html), [Qiang Ni](https://dblp.org/pid/87/3074.html), Jungong Han:

Lightweight facial expression recognition method based on attention mechanism and key region fusion. [J. Electronic Imaging30(6)](https://dblp.org/db/journals/jei/jei30.html#journals/jei/KongRZZNH21) (2021)
- ![](https://dblp.org/img/n.png)

\[j124\]
[Zixi Wang](https://dblp.org/pid/67/3752.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Fan Li](https://dblp.org/pid/73/237-3.html):

Deep image compression with multi-stage representation. [J. Vis. Commun. Image Represent.79](https://dblp.org/db/journals/jvcir/jvcir79.html#journals/jvcir/WangDHL21): 103226 (2021)
- ![](https://dblp.org/img/n.png)

\[j123\]
[Huiling Xu](https://dblp.org/pid/63/1770.html), [Wei Xia](https://dblp.org/pid/77/1243-7.html), [Quanxue Gao](https://dblp.org/pid/63/804.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Xinbo Gao](https://dblp.org/pid/99/4522.html):

Graph embedding clustering: Graph attention auto-encoder with cluster-specificity distribution. [Neural Networks142](https://dblp.org/db/journals/nn/nn142.html#journals/nn/XuXGHG21): 221-230 (2021)
- ![](https://dblp.org/img/n.png)

\[j122\]
[Duona Zhang](https://dblp.org/pid/217/3671.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenrui Ding](https://dblp.org/pid/08/10143.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chunhui Liu](https://dblp.org/pid/20/5393-4.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [David S. Doermann](https://dblp.org/pid/88/6921.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning modulation filter networks for weak signal detection in noise. [Pattern Recognit.109](https://dblp.org/db/journals/pr/pr109.html#journals/pr/ZhangDZLHD21): 107590 (2021)
- ![](https://dblp.org/img/n.png)

\[j121\]
[Dingwen Zhang](https://dblp.org/pid/150/6620.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guohai Huang](https://dblp.org/pid/275/3809.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Junwei Han](https://dblp.org/pid/00/3003.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yizhou Yu](https://dblp.org/pid/90/6896.html):

Cross-modality deep feature learning for brain tumor segmentation. [Pattern Recognit.110](https://dblp.org/db/journals/pr/pr110.html#journals/pr/ZhangHZHHY21): 107562 (2021)
- ![](https://dblp.org/img/n.png)

\[j120\]
[Xuhang Lian](https://dblp.org/pid/195/4363.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Pan](https://dblp.org/pid/13/718.html):

Cascaded hierarchical atrous spatial pyramid pooling module for semantic segmentation. [Pattern Recognit.110](https://dblp.org/db/journals/pr/pr110.html#journals/pr/LianPHP21): 107622 (2021)
- ![](https://dblp.org/img/n.png)

\[j119\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Fan Wang](https://dblp.org/pid/88/898.html), [Yongjiang Luo](https://dblp.org/pid/174/4309.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Exploring a unified low rank representation for multi-focus image fusion. [Pattern Recognit.113](https://dblp.org/db/journals/pr/pr113.html#journals/pr/ZhangWLH21): 107752 (2021)
- ![](https://dblp.org/img/n.png)

\[j118\]
[Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Jiajia Zhang](https://dblp.org/pid/08/267.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han, [Shu Zhang](https://dblp.org/pid/30/2700-1.html), [Junwei Han](https://dblp.org/pid/00/3003.html):

Automatic pancreas segmentation based on lightweight DCNN modules and spatial prior propagation. [Pattern Recognit.114](https://dblp.org/db/journals/pr/pr114.html#journals/pr/ZhangZZHZH21): 107762 (2021)
- ![](https://dblp.org/img/n.png)

\[j117\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Quanxue Gao](https://dblp.org/pid/63/804.html), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html):

Relation-based Discriminative Cooperation Network for Zero-Shot Classification. [Pattern Recognit.118](https://dblp.org/db/journals/pr/pr118.html#journals/pr/LiuGGHS21): 108024 (2021)
- ![](https://dblp.org/img/n.png)

\[j116\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tonglin Xiao](https://dblp.org/pid/292/1102.html), [Nianchang Huang](https://dblp.org/pid/258/2761.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dingwen Zhang](https://dblp.org/pid/150/6620.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Revisiting Feature Fusion for RGB-T Salient Object Detection. [IEEE Trans. Circuits Syst. Video Technol.31(5)](https://dblp.org/db/journals/tcsv/tcsv31.html#journals/tcsv/ZhangXHZH21): 1804-1818 (2021)
- ![](https://dblp.org/img/n.png)

\[j115\]
[Jing Nie](https://dblp.org/pid/39/5493-1.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shengjie Zhao](https://dblp.org/pid/47/5183-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Efficient Selective Context Network for Accurate Object Detection. [IEEE Trans. Circuits Syst. Video Technol.31(9)](https://dblp.org/db/journals/tcsv/tcsv31.html#journals/tcsv/NiePZHL21): 3456-3468 (2021)
- ![](https://dblp.org/img/n.png)

\[j114\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dingwen Zhang](https://dblp.org/pid/150/6620.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Integrating Part-Object Relationship and Contrast for Camouflaged Object Detection. [IEEE Trans. Inf. Forensics Secur.16](https://dblp.org/db/journals/tifs/tifs16.html#journals/tifs/LiuZZH21): 5154-5166 (2021)
- ![](https://dblp.org/img/n.png)

\[j113\]
[Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shuo Zhang](https://dblp.org/pid/83/3714.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zizhou Jia](https://dblp.org/pid/248/9172.html), [Jing Zhong](https://dblp.org/pid/09/2522.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Where to Prune: Using LSTM to Guide Data-Dependent Soft Pruning. [IEEE Trans. Image Process.30](https://dblp.org/db/journals/tip/tip30.html#journals/tip/DingZJZH21): 293-304 (2021)
- ![](https://dblp.org/img/n.png)

\[j112\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zijia Lin](https://dblp.org/pid/78/9911.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiao Ma](https://dblp.org/pid/35/573-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Learning Transformation-Invariant Local Descriptors With Low-Coupling Binary Codes. [IEEE Trans. Image Process.30](https://dblp.org/db/journals/tip/tip30.html#journals/tip/MiaoLMDH21): 7554-7566 (2021)
- ![](https://dblp.org/img/n.png)

\[j111\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Liu](https://dblp.org/pid/97/4626-38.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Joint Cross-Modal and Unimodal Features for RGB-D Salient Object Detection. [IEEE Trans. Multim.23](https://dblp.org/db/journals/tmm/tmm23.html#journals/tmm/HuangLZH21): 2428-2441 (2021)
- ![](https://dblp.org/img/n.png)

\[j110\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuxiao Zhao](https://dblp.org/pid/68/875.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xi Li](https://dblp.org/pid/46/2311-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Deep Attentive Video Summarization With Distribution Consistency Learning. [IEEE Trans. Neural Networks Learn. Syst.32(4)](https://dblp.org/db/journals/tnn/tnn32.html#journals/tnn/JiZPLH21): 1765-1775 (2021)
- ![](https://dblp.org/img/n.png)

\[j109\]
[Yutao Hu](https://dblp.org/pid/37/5215-2.html), [Xuhui Liu](https://dblp.org/pid/09/4802.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han, [Xianbin Cao](https://dblp.org/pid/22/3485.html):

Alignment Enhancement Network for Fine-grained Visual Categorization. [ACM Trans. Multim. Comput. Commun. Appl.17(1s)](https://dblp.org/db/journals/tomccap/tomccap17.html#journals/tomccap/HuL0H021): 12:1-12:20 (2021)
- ![](https://dblp.org/img/n.png)

\[c87\]
[Liuyu Xiang](https://dblp.org/pid/242/7959.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

Increasing Oversampling Diversity for Long-Tailed Visual Recognition. [CICAI2021](https://dblp.org/db/conf/cicai/cicai2021.html#conf/cicai/XiangDH21): 39-50
- ![](https://dblp.org/img/n.png)

\[c86\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Shenlu Zhao](https://dblp.org/pid/300/5768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yongjiang Luo](https://dblp.org/pid/174/4309.html), [Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Nianchang Huang](https://dblp.org/pid/258/2761.html), Jungong Han:

ABMDRNet: Adaptive-Weighted Bi-Directional Modality Difference Reduction Network for RGB-T Semantic Segmentation. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/0020ZLZHH21): 2633-2642
- ![](https://dblp.org/img/n.png)

\[c85\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Diverse Branch Block: Building a Convolution as an Inception-Like Unit. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/Ding0HD21): 10886-10895
- ![](https://dblp.org/img/n.png)

\[c84\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), [Ningning Ma](https://dblp.org/pid/30/2310.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html), [Jian Sun](https://dblp.org/pid/68/4942-1.html):

RepVGG: Making VGG-Style ConvNets Great Again. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/Ding0MHD021): 13733-13742
- ![](https://dblp.org/img/n.png)

\[c83\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html), [Jianchao Tan](https://dblp.org/pid/165/9938.html), [Ji Liu](https://dblp.org/pid/51/4433-2.html), Jungong Han, [Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html):

ResRep: Lossless CNN Pruning via Decoupling Remembering and Forgetting. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/DingHT0HGD21): 4490-4500
- ![](https://dblp.org/img/n.png)

\[i38\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), [Ningning Ma](https://dblp.org/pid/30/2310.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html), [Jian Sun](https://dblp.org/pid/68/4942-1.html):

RepVGG: Making VGG-style ConvNets Great Again. [CoRRabs/2101.03697](https://dblp.org/db/journals/corr/corr2101.html#journals/corr/abs-2101-03697) (2021)
- ![](https://dblp.org/img/n.png)

\[i37\]
[Chaowei Fang](https://dblp.org/pid/159/1655.html), [Haibin Tian](https://dblp.org/pid/280/1349.html), [Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han, [Junwei Han](https://dblp.org/pid/00/3003.html):

Densely Nested Top-Down Flows for Salient Object Detection. [CoRRabs/2102.09133](https://dblp.org/db/journals/corr/corr2102.html#journals/corr/abs-2102-09133) (2021)
- ![](https://dblp.org/img/n.png)

\[i36\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

Diverse Branch Block: Building a Convolution as an Inception-like Unit. [CoRRabs/2103.13425](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-13425) (2021)
- ![](https://dblp.org/img/n.png)

\[i35\]
[Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Bo Wang](https://dblp.org/pid/72/6811-11.html), [Gerong Wang](https://dblp.org/pid/289/1259.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Jiajia Zhang](https://dblp.org/pid/08/267.html), Jungong Han, [Zheng You](https://dblp.org/pid/04/2178.html):

Onfocus Detection: Identifying Individual-Camera Eye Contact from Unconstrained Images. [CoRRabs/2103.15307](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-15307) (2021)
- ![](https://dblp.org/img/n.png)

\[i34\]
[Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Haibin Tian](https://dblp.org/pid/280/1349.html), Jungong Han:

Few-Cost Salient Object Detection with Adversarial-Paced Learning. [CoRRabs/2104.01928](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-01928) (2021)
- ![](https://dblp.org/img/n.png)

\[i33\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html), [Jianan Liu](https://dblp.org/pid/146/6864.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han:

Exploring Modality-shared Appearance Features and Modality-invariant Relation Features for Cross-modality Person Re-Identification. [CoRRabs/2104.11539](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-11539) (2021)
- ![](https://dblp.org/img/n.png)

\[i32\]
[Nianchang Huang](https://dblp.org/pid/258/2761.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han:

Middle-level Fusion for Lightweight RGB-D Salient Object Detection. [CoRRabs/2104.11543](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-11543) (2021)
- ![](https://dblp.org/img/n.png)

\[i31\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

RepMLP: Re-parameterizing Convolutions into Fully-connected Layers for Image Recognition. [CoRRabs/2105.01883](https://dblp.org/db/journals/corr/corr2105.html#journals/corr/abs-2105-01883) (2021)
- ![](https://dblp.org/img/n.png)

\[i30\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html), Jungong Han, [Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html):

Manipulating Identical Filter Redundancy for Efficient Pruning on Deep and Complicated CNN. [CoRRabs/2107.14444](https://dblp.org/db/journals/corr/corr2107.html#journals/corr/abs-2107-14444) (2021)
- ![](https://dblp.org/img/n.png)

\[i29\]
[Zhong Ji](https://dblp.org/pid/36/6466.html), [Zhishen Hou](https://dblp.org/pid/301/8258.html), [Xiyao Liu](https://dblp.org/pid/138/9719-2.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han:

Information Symmetry Matters: A Modal-Alternating Propagation Network for Few-Shot Learning. [CoRRabs/2109.01295](https://dblp.org/db/journals/corr/corr2109.html#journals/corr/abs-2109-01295) (2021)
- ![](https://dblp.org/img/n.png)

\[i28\]
[Zerun Wang](https://dblp.org/pid/260/7013.html), [Liuyu Xiang](https://dblp.org/pid/242/7959.html), [Fan Yang](https://dblp.org/pid/29/3081-83.html), [Jinzhao Qian](https://dblp.org/pid/231/1835.html), [Jie Hu](https://dblp.org/pid/90/5064-21.html), [Haidong Huang](https://dblp.org/pid/245/4034.html), Jungong Han, [Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html):

LODE: Deep Local Deblurring and A New Benchmark. [CoRRabs/2109.09149](https://dblp.org/db/journals/corr/corr2109.html#journals/corr/abs-2109-09149) (2021)
- ![](https://dblp.org/img/n.png)

\[i27\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Honghao Chen](https://dblp.org/pid/279/9807.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), Jungong Han, [Guiguang Ding](https://dblp.org/pid/51/740.html):

RepMLPNet: Hierarchical Vision MLP with Re-parameterized Locality. [CoRRabs/2112.11081](https://dblp.org/db/journals/corr/corr2112.html#journals/corr/abs-2112-11081) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[j108\]
[Jiaojiao Zhao](https://dblp.org/pid/150/4197.html), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Cees G. M. Snoek](https://dblp.org/pid/s/CeesSnoek.html):

Pixelated Semantic Colorization. [Int. J. Comput. Vis.128(4)](https://dblp.org/db/journals/ijcv/ijcv128.html#journals/ijcv/ZhaoHSS20): 818-834 (2020)
- ![](https://dblp.org/img/n.png)

\[j107\]
[Xuhang Lian](https://dblp.org/pid/195/4363.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han, [Jing Pan](https://dblp.org/pid/13/718.html):

Semantic segmentation with hybrid pyramid pooling and stacked pyramid structure. [Neurocomputing410](https://dblp.org/db/journals/ijon/ijon410.html#journals/ijon/LianPHP20): 454-467 (2020)
- ![](https://dblp.org/img/n.png)

\[j106\]
[Heng Liu](https://dblp.org/pid/59/3260-2.html), [Jiajun Qin](https://dblp.org/pid/127/0562.html), [Zilin Fu](https://dblp.org/pid/218/9871.html), [Xue Li](https://dblp.org/pid/181/2710.html), Jungong Han:

Fast simultaneous image super-resolution and motion deblurring with decoupled cooperative learning. [J. Real Time Image Process.17(6)](https://dblp.org/db/journals/jrtip/jrtip17.html#journals/jrtip/LiuQFLH20): 1787-1800 (2020)
- ![](https://dblp.org/img/n.png)

\[j105\]
[Wei Li](https://dblp.org/pid/64/6025-130.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Junhua Gu](https://dblp.org/pid/26/6721.html), [Yongfeng Dong](https://dblp.org/pid/12/1159.html), [Yao Dong](https://dblp.org/pid/80/8588-5.html), Jungong Han:

Indoor scene understanding via RGB-D image segmentation employing depth-based CNN and CRFs. [Multim. Tools Appl.79(47)](https://dblp.org/db/journals/mta/mta79.html#journals/mta/0130GDDH20): 35475-35489 (2020)
- ![](https://dblp.org/img/n.png)

\[j104\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Quanxue Gao](https://dblp.org/pid/63/804.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Label-activating framework for zero-shot learning. [Neural Networks121](https://dblp.org/db/journals/nn/nn121.html#journals/nn/LiuGGHS20): 1-9 (2020)
- ![](https://dblp.org/img/n.png)

\[j103\]
[Suqi Zhang](https://dblp.org/pid/145/6076.html), [Xinyun Xu](https://dblp.org/pid/260/3880.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Multi-layer Attention Based CNN for Target-Dependent Sentiment Classification. [Neural Process. Lett.51(3)](https://dblp.org/db/journals/npl/npl51.html#journals/npl/ZhangXPH20): 2089-2103 (2020)
- ![](https://dblp.org/img/n.png)

\[j102\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Guanghe Li](https://dblp.org/pid/121/6489.html), [Yunfeng Cao](https://dblp.org/pid/177/0271.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Multi-focus image fusion based on non-negative sparse representation and patch-level consistency rectification. [Pattern Recognit.104](https://dblp.org/db/journals/pr/pr104.html#journals/pr/ZhangLCH20): 107325 (2020)
- ![](https://dblp.org/img/n.png)

\[j101\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenfei Hu](https://dblp.org/pid/278/7777.html), [Erlu He](https://dblp.org/pid/240/1897.html), Jungong Han, [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Pedestrian attribute recognition based on multiple time steps attention. [Pattern Recognit. Lett.138](https://dblp.org/db/journals/prl/prl138.html#journals/prl/JiHHHP20): 170-176 (2020)
- ![](https://dblp.org/img/n.png)

\[j100\]
[Sicheng Zhao](https://dblp.org/pid/65/10574.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yue Gao](https://dblp.org/pid/33/3099-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Zhao](https://dblp.org/pid/68/2766-20.html), [Youbao Tang](https://dblp.org/pid/20/8578.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Hongxun Yao](https://dblp.org/pid/y/HongxunYao.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qingming Huang](https://dblp.org/pid/68/4388.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Discrete Probability Distribution Prediction of Image Emotions with Shared Sparse Learning. [IEEE Trans. Affect. Comput.11(4)](https://dblp.org/db/journals/taffco/taffco11.html#journals/taffco/ZhaoDGZTHYH20): 574-587 (2020)
- ![](https://dblp.org/img/n.png)

\[j99\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Caifeng Shan](https://dblp.org/pid/98/428.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Deep Salient Object Detection With Contextual Information Guidance. [IEEE Trans. Image Process.29](https://dblp.org/db/journals/tip/tip29.html#journals/tip/LiuH0S20): 360-374 (2020)
- ![](https://dblp.org/img/n.png)

\[j98\]
[Chunlei Liu](https://dblp.org/pid/76/5853-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenrui Ding](https://dblp.org/pid/08/10143.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Vittorio Murino](https://dblp.org/pid/62/6790.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Guodong Guo](https://dblp.org/pid/92/4520.html):

Aggregation Signature for Small Object Tracking. [IEEE Trans. Image Process.29](https://dblp.org/db/journals/tip/tip29.html#journals/tip/LiuDYMZHG20): 1738-1747 (2020)
- ![](https://dblp.org/img/n.png)

\[j97\]
[Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wankou Yang](https://dblp.org/pid/99/3602.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ze Wang](https://dblp.org/pid/35/6674-8.html), [Lian Zhuo](https://dblp.org/pid/218/5220.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Xiantong Zhen](https://dblp.org/pid/78/10651.html):

The Structure Transfer Machine Theory and Applications. [IEEE Trans. Image Process.29](https://dblp.org/db/journals/tip/tip29.html#journals/tip/ZhangYWZHZ20): 2889-2902 (2020)
- ![](https://dblp.org/img/n.png)

\[j96\]
[Jiale Cao](https://dblp.org/pid/167/3851.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Bolin Gao](https://dblp.org/pid/120/1968.html), [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Taking a Look at Small-Scale Pedestrians and Occluded Pedestrians. [IEEE Trans. Image Process.29](https://dblp.org/db/journals/tip/tip29.html#journals/tip/CaoPHGL20): 3143-3152 (2020)
- ![](https://dblp.org/img/n.png)

\[j95\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Nianchang Huang](https://dblp.org/pid/258/2761.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lin Yao](https://dblp.org/pid/37/752.html), [Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Caifeng Shan](https://dblp.org/pid/98/428.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

RGB-T Salient Object Detection via Fusing Multi-Level CNN Features. [IEEE Trans. Image Process.29](https://dblp.org/db/journals/tip/tip29.html#journals/tip/ZhangHYZSH20): 3321-3335 (2020)
- ![](https://dblp.org/img/n.png)

\[j94\]
[Dingwen Zhang](https://dblp.org/pid/150/6620.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guohai Huang](https://dblp.org/pid/275/3809.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Junwei Han](https://dblp.org/pid/00/3003.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yizhou Wang](https://dblp.org/pid/71/3387-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yizhou Yu](https://dblp.org/pid/90/6896.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Exploring Task Structure for Brain Tumor Segmentation From Multi-Modality MR Images. [IEEE Trans. Image Process.29](https://dblp.org/db/journals/tip/tip29.html#journals/tip/ZhangHZHHWY20): 9032-9043 (2020)
- ![](https://dblp.org/img/n.png)

\[j93\]
[Gengshen Wu](https://dblp.org/pid/204/2949.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zijia Lin](https://dblp.org/pid/78/9911.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Ni](https://dblp.org/pid/87/3074.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

On Aggregation of Unsupervised Deep Binary Descriptor With Weak Bits. [IEEE Trans. Image Process.29](https://dblp.org/db/journals/tip/tip29.html#journals/tip/WuLDNH20): 9266-9278 (2020)
- ![](https://dblp.org/img/n.png)

\[j92\]
[Guixin Ye](https://dblp.org/pid/125/3245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhanyong Tang](https://dblp.org/pid/38/7487.html), [Dingyi Fang](https://dblp.org/pid/80/3909.html), [Zhanxing Zhu](https://dblp.org/pid/87/7756.html), [Yansong Feng](https://dblp.org/pid/25/2643-2.html), [Pengfei Xu](https://dblp.org/pid/04/383-3.html), [Xiaojiang Chen](https://dblp.org/pid/95/10521.html), Jungong Han, [Zheng Wang](https://dblp.org/pid/w/ZhengWang1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Using Generative Adversarial Networks to Break and Protect Text Captchas. [ACM Trans. Priv. Secur.23(2)](https://dblp.org/db/journals/tissec/tissec23.html#journals/tissec/YeTFZFXCHW20): 7:1-7:29 (2020)
- ![](https://dblp.org/img/n.png)

\[j91\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuxin Sun](https://dblp.org/pid/158/7549.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yunlong Yu](https://dblp.org/pid/45/7404.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Attribute-Guided Network for Cross-Modal Zero-Shot Hashing. [IEEE Trans. Neural Networks Learn. Syst.31(1)](https://dblp.org/db/journals/tnn/tnn31.html#journals/tnn/JiSYPH20): 321-330 (2020)
- ![](https://dblp.org/img/n.png)

\[j90\]
[Hui Chen](https://dblp.org/pid/12/417-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaopeng Gu](https://dblp.org/pid/313/6436.html), [Wenyuan Xu](https://dblp.org/pid/10/3878-1.html), Jungong Han:

ACMNet: Adaptive Confidence Matching Network for Human Behavior Analysis via Cross-modal Retrieval. [ACM Trans. Multim. Comput. Commun. Appl.16(1s)](https://dblp.org/db/journals/tomccap/tomccap16.html#journals/tomccap/ChenDLZGXH20): 27:1-27:21 (2020)
- ![](https://dblp.org/img/n.png)

\[c82\]
[Yuwei He](https://dblp.org/pid/222/8475.html), [Xiaoming Jin](https://dblp.org/pid/26/5593.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), Jungong Han, [Jiyong Zhang](https://dblp.org/pid/95/6425-1.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html):

Heterogeneous Transfer Learning with Weighted Instance-Correspondence Data. [AAAI2020](https://dblp.org/db/conf/aaai/aaai2020.html#conf/aaai/HeJDGHZZ20): 4099-4106
- ![](https://dblp.org/img/n.png)

\[c81\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

Shallow Feature Based Dense Attention Network for Crowd Counting. [AAAI2020](https://dblp.org/db/conf/aaai/aaai2020.html#conf/aaai/MiaoLDH20): 11765-11772
- ![](https://dblp.org/img/n.png)

\[c80\]
[Yanwei Pang](https://dblp.org/pid/35/5889.html), [Jing Nie](https://dblp.org/pid/39/5493-1.html), [Jin Xie](https://dblp.org/pid/80/1949-5.html), Jungong Han, [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html):

BidNet: Binocular Image Dehazing Without Explicit Disparity Estimation. [CVPR2020](https://dblp.org/db/conf/cvpr/cvpr2020.html#conf/cvpr/PangNXHL20): 5930-5939
- ![](https://dblp.org/img/n.png)

\[c79\]
[Hui Chen](https://dblp.org/pid/12/417-13.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Xudong Liu](https://dblp.org/pid/90/2144.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Ji Liu](https://dblp.org/pid/51/4433-2.html), Jungong Han:

IMRAM: Iterative Matching With Recurrent Attention Memory for Cross-Modal Image-Text Retrieval. [CVPR2020](https://dblp.org/db/conf/cvpr/cvpr2020.html#conf/cvpr/ChenDLLLH20): 12652-12660
- ![](https://dblp.org/img/n.png)

\[c78\]
[Yunlong Yu](https://dblp.org/pid/45/7404.html), [Zhong Ji](https://dblp.org/pid/36/6466.html), Jungong Han, [Zhongfei Zhang](https://dblp.org/pid/z/ZhongfeiMarkZhang.html):

Episode-Based Prototype Generating Network for Zero-Shot Learning. [CVPR2020](https://dblp.org/db/conf/cvpr/cvpr2020.html#conf/cvpr/YuJHZ20): 14032-14041
- ![](https://dblp.org/img/n.png)

\[c77\]
[Liuyu Xiang](https://dblp.org/pid/242/7959.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

Learning From Multiple Experts: Self-paced Knowledge Distillation for Long-Tailed Classification. [ECCV (5)2020](https://dblp.org/db/conf/eccv/eccv2020-5.html#conf/eccv/XiangDH20): 247-263
- ![](https://dblp.org/img/n.png)

\[c76\]
[Yutao Hu](https://dblp.org/pid/37/5215-2.html), [Xiaolong Jiang](https://dblp.org/pid/56/5097.html), [Xuhui Liu](https://dblp.org/pid/09/4802.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han, [Xianbin Cao](https://dblp.org/pid/22/3485.html), [David S. Doermann](https://dblp.org/pid/88/6921.html):

NAS-Count: Counting-by-Density with Neural Architecture Search. [ECCV (22)2020](https://dblp.org/db/conf/eccv/eccv2020-22.html#conf/eccv/HuJLZHCD20): 747-766
- ![](https://dblp.org/img/n.png)

\[c75\]
[Jianyong Liu](https://dblp.org/pid/10/1468.html), [Heng Liu](https://dblp.org/pid/59/3260-2.html), [Xiaoyu Zheng](https://dblp.org/pid/20/3589.html), Jungong Han:

Exploring Multi-scale Deep Encoder-Decoder and PatchGAN for Perceptual Ultrasound Image Super-Resolution. [NCAA2020](https://dblp.org/db/conf/ncaa/ncaa2020.html#conf/ncaa/Liu0ZH20): 47-59
- ![](https://dblp.org/img/n.png)

\[c74\]
[Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Haibin Tian](https://dblp.org/pid/280/1349.html), Jungong Han:

Few-Cost Salient Object Detection with Adversarial-Paced Learning. [NeurIPS2020](https://dblp.org/db/conf/nips/neurips2020.html#conf/nips/ZhangTH20)
- ![](https://dblp.org/img/n.png)

\[i26\]
[Yutao Hu](https://dblp.org/pid/37/5215-2.html), [Xiaolong Jiang](https://dblp.org/pid/56/5097.html), [Xuhui Liu](https://dblp.org/pid/09/4802.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han, [Xianbin Cao](https://dblp.org/pid/22/3485.html), [David S. Doermann](https://dblp.org/pid/88/6921.html):

NAS-Count: Counting-by-Density with Neural Architecture Search. [CoRRabs/2003.00217](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-00217) (2020)
- ![](https://dblp.org/img/n.png)

\[i25\]
[Hui Chen](https://dblp.org/pid/12/417-13.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Xudong Liu](https://dblp.org/pid/90/2144.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Ji Liu](https://dblp.org/pid/51/4433-2.html), Jungong Han:

IMRAM: Iterative Matching with Recurrent Attention Memory for Cross-Modal Image-Text Retrieval. [CoRRabs/2003.03772](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-03772) (2020)
- ![](https://dblp.org/img/n.png)

\[i24\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

Shallow Feature Based Dense Attention Network for Crowd Counting. [CoRRabs/2006.09853](https://dblp.org/db/journals/corr/corr2006.html#journals/corr/abs-2006-09853) (2020)
- ![](https://dblp.org/img/n.png)

\[i23\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Tianxiang Hao](https://dblp.org/pid/270/0611-1.html), [Ji Liu](https://dblp.org/pid/51/4433-2.html), Jungong Han, [Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html):

Lossless CNN Channel Pruning via Gradient Resetting and Convolutional Re-parameterization. [CoRRabs/2007.03260](https://dblp.org/db/journals/corr/corr2007.html#journals/corr/abs-2007-03260) (2020)
- ![](https://dblp.org/img/n.png)

\[i22\]
[Heng Liu](https://dblp.org/pid/59/3260-2.html), [Jianyong Liu](https://dblp.org/pid/10/1468.html), [Tao Tao](https://dblp.org/pid/73/3197-5.html), [Shudong Hou](https://dblp.org/pid/28/8546.html), Jungong Han:

Perception Consistency Ultrasound Image Super-resolution via Self-supervised CycleGAN. [CoRRabs/2012.14142](https://dblp.org/db/journals/corr/corr2012.html#journals/corr/abs-2012-14142) (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j89\]
[Guiguang Ding](https://dblp.org/pid/51/740.html), [Minghai Chen](https://dblp.org/pid/195/8186.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Liu](https://dblp.org/pid/61/3234-16.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Neural Image Caption Generation with Weighted Training and Reference. [Cogn. Comput.11(6)](https://dblp.org/db/journals/cogcom/cogcom11.html#journals/cogcom/DingCZCHL19): 763-777 (2019)
- ![](https://dblp.org/img/n.png)

\[j88\]
[Li Zhang](https://dblp.org/pid/89/5992-13.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chee Peng Lim](https://dblp.org/pid/28/6855.html), Jungong Han:

Complex Deep Learning and Evolutionary Computing Models in Computer Vision. [Complex.2019](https://dblp.org/db/journals/complexity/complexity2019.html#journals/complexity/ZhangLH19): 1671340:1-1671340:2 (2019)
- ![](https://dblp.org/img/n.png)

\[j87\]
[Hang Shao](https://dblp.org/pid/390/0465.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

Zero-shot multi-label learning via label factorisation. [IET Comput. Vis.13(2)](https://dblp.org/db/journals/iet-cvi/iet-cvi13.html#journals/iet-cvi/ShaoGDH19): 117-124 (2019)
- ![](https://dblp.org/img/n.png)

\[j86\]
[Xianghai Cao](https://dblp.org/pid/177/0184.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yamei Ji](https://dblp.org/pid/228/7312.html), [Lin Wang](https://dblp.org/pid/17/6729.html), [Beibei Ji](https://dblp.org/pid/228/7534.html), [Licheng Jiao](https://dblp.org/pid/40/3714.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

SAR image change detection based on deep denoising and CNN. [IET Image Process.13(9)](https://dblp.org/db/journals/iet-ipr/iet-ipr13.html#journals/iet-ipr/CaoJWJJH19): 1509-1515 (2019)
- ![](https://dblp.org/img/n.png)

\[j85\]
[Heng Liu](https://dblp.org/pid/59/3260-2.html), [Xiaoyu Zheng](https://dblp.org/pid/20/3589.html), Jungong Han, [Yuezhong Chu](https://dblp.org/pid/228/7471.html), [Tao Tao](https://dblp.org/pid/73/3197-5.html):

Survey on GAN-based face hallucination with its model development. [IET Image Process.13(14)](https://dblp.org/db/journals/iet-ipr/iet-ipr13.html#journals/iet-ipr/LiuZHCT19): 2662-2672 (2019)
- ![](https://dblp.org/img/n.png)

\[j84\]
[Zhong Ji](https://dblp.org/pid/36/6466.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Junyue Wang](https://dblp.org/pid/236/0369.html), [Yunlong Yu](https://dblp.org/pid/45/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Class-specific synthesized dictionary model for Zero-Shot Learning. [Neurocomputing329](https://dblp.org/db/journals/ijon/ijon329.html#journals/ijon/JiWYPH19): 339-347 (2019)
- ![](https://dblp.org/img/n.png)

\[j83\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Caifeng Shan](https://dblp.org/pid/98/428.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Quanxue Gao](https://dblp.org/pid/63/804.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Rongmei Cui](https://dblp.org/pid/222/2238.html):

Hyperspectral image denoising via minimizing the partial sum of singular values and superpixel segmentation. [Neurocomputing330](https://dblp.org/db/journals/ijon/ijon330.html#journals/ijon/LiuSGGHC19): 465-482 (2019)
- ![](https://dblp.org/img/n.png)

\[j82\]
[Heng Liu](https://dblp.org/pid/59/3260-2.html), [Zilin Fu](https://dblp.org/pid/218/9871.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shudong Hou](https://dblp.org/pid/28/8546.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuezhong Chu](https://dblp.org/pid/228/7471.html):

Single image super-resolution using multi-scale deep encoder-decoder with phase congruency edge map guidance. [Inf. Sci.473](https://dblp.org/db/journals/isci/isci473.html#journals/isci/LiuFHSHC19): 44-58 (2019)
- ![](https://dblp.org/img/n.png)

\[j81\]
[Yinghui Kong](https://dblp.org/pid/23/867.html), [Li Li](https://dblp.org/pid/53/2189.html), [Ke Zhang](https://dblp.org/pid/20/4152-5.html), [Qiang Ni](https://dblp.org/pid/87/3074.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Attention module-based spatial-temporal graph convolutional networks for skeleton-based action recognition. [J. Electronic Imaging28(4)](https://dblp.org/db/journals/jei/jei28.html#journals/jei/KongLZNH19): 043032 (2019)
- ![](https://dblp.org/img/n.png)

\[j80\]
[Li Zhang](https://dblp.org/pid/89/5992-13.html), [Chee Peng Lim](https://dblp.org/pid/28/6855.html), Jungong Han:

Guest editorial: Automatic facial and bodily expression perception for human behaviour understanding. [Multim. Tools Appl.78(21)](https://dblp.org/db/journals/mta/mta78.html#journals/mta/ZhangLH19): 30331-30334 (2019)
- ![](https://dblp.org/img/n.png)

\[j79\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Feiping Nie](https://dblp.org/pid/80/5755.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Quanxue Gao](https://dblp.org/pid/63/804.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Flexible unsupervised feature extraction for image classification. [Neural Networks115](https://dblp.org/db/journals/nn/nn115.html#journals/nn/LiuNGGHS19): 65-71 (2019)
- ![](https://dblp.org/img/n.png)

\[j78\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Quanxue Gao](https://dblp.org/pid/63/804.html), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Adaptive robust principal component analysis. [Neural Networks119](https://dblp.org/db/journals/nn/nn119.html#journals/nn/LiuGGSH19): 85-92 (2019)
- ![](https://dblp.org/img/n.png)

\[j77\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Lin Yao](https://dblp.org/pid/37/752.html), [Yajun Li](https://dblp.org/pid/202/0089.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Video Synchronization Based on Projective-Invariant Descriptor. [Neural Process. Lett.49(3)](https://dblp.org/db/journals/npl/npl49.html#journals/npl/ZhangYLH19): 1093-1110 (2019)
- ![](https://dblp.org/img/n.png)

\[j76\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Zhen Huo](https://dblp.org/pid/239/6395.html), [Yi Liu](https://dblp.org/pid/97/4626-38.html), [Yunhui Pan](https://dblp.org/pid/239/6380.html), [Caifeng Shan](https://dblp.org/pid/98/428.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Salient object detection employing a local tree-structured low-rank representation and foreground consistency. [Pattern Recognit.92](https://dblp.org/db/journals/pr/pr92.html#journals/pr/ZhangHLPSH19): 119-134 (2019)
- ![](https://dblp.org/img/n.png)

\[j75\]
[Chaoqun Chu](https://dblp.org/pid/233/6032.html), [Dahan Gong](https://dblp.org/pid/187/2613.html), [Kai Chen](https://dblp.org/pid/181/2839.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html):

Optimized projection for hashing. [Pattern Recognit. Lett.117](https://dblp.org/db/journals/prl/prl117.html#journals/prl/ChuGCGHD19): 169-178 (2019)
- ![](https://dblp.org/img/n.png)

\[j74\]
[Heng Liu](https://dblp.org/pid/59/3260-2.html), [Liangliang Dai](https://dblp.org/pid/184/8786.html), [Shudong Hou](https://dblp.org/pid/28/8546.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Hongshen Liu](https://dblp.org/pid/169/4604.html):

Are mid-air dynamic gestures applicable to user identification? [Pattern Recognit. Lett.117](https://dblp.org/db/journals/prl/prl117.html#journals/prl/LiuDHHL19): 179-185 (2019)
- ![](https://dblp.org/img/n.png)

\[j73\]
[Yunqi Miao](https://dblp.org/pid/207/3366.html), Jungong Han, [Yongsheng Gao](https://dblp.org/pid/22/6786-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html):

ST-CNN: Spatial-Temporal Convolutional Neural Network for crowd counting in videos. [Pattern Recognit. Lett.125](https://dblp.org/db/journals/prl/prl125.html#journals/prl/MiaoHGZ19): 113-118 (2019)
- ![](https://dblp.org/img/n.png)

\[j72\]
[Jing Pan](https://dblp.org/pid/13/718.html), [Hanqing Sun](https://dblp.org/pid/228/6382-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhanjie Song](https://dblp.org/pid/31/5015.html), Jungong Han:

Dual-Resolution Dual-Path Convolutional Neural Networks for Fast Object Detection. [Sensors19(14)](https://dblp.org/db/journals/sensors/sensors19.html#journals/sensors/PanSSH19): 3111 (2019)
- ![](https://dblp.org/img/n.png)

\[j71\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Long Wang](https://dblp.org/pid/68/4459-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Salient Object Detection via Two-Stage Graphs. [IEEE Trans. Circuits Syst. Video Technol.29(4)](https://dblp.org/db/journals/tcsv/tcsv29.html#journals/tcsv/LiuHZW19): 1023-1037 (2019)
- ![](https://dblp.org/img/n.png)

\[j70\]
[Gengshen Wu](https://dblp.org/pid/204/2949.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Qiang Ni](https://dblp.org/pid/87/3074.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Joint Image-Text Hashing for Fast Large-Scale Cross-Media Retrieval Using Self-Supervised Deep Learning. [IEEE Trans. Ind. Electron.66(12)](https://dblp.org/db/journals/tie/tie66.html#journals/tie/WuHLDZN19): 9868-9877 (2019)
- ![](https://dblp.org/img/n.png)

\[j69\]
[Yanwei Pang](https://dblp.org/pid/35/5889.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiale Cao](https://dblp.org/pid/167/3851.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Wang](https://dblp.org/pid/39/449-87.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

JCS-Net: Joint Classification and Super-Resolution Network for Small-Scale Pedestrian Detection in Surveillance Images. [IEEE Trans. Inf. Forensics Secur.14(12)](https://dblp.org/db/journals/tifs/tifs14.html#journals/tifs/PangCWH19): 3322-3331 (2019)
- ![](https://dblp.org/img/n.png)

\[j68\]
[Gengshen Wu](https://dblp.org/pid/204/2949.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Yuchen Guo](https://dblp.org/pid/132/7979.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Li Liu](https://dblp.org/pid/33/4528-4.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Qiang Ni](https://dblp.org/pid/87/3074.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Unsupervised Deep Video Hashing via Balanced Code for Large-Scale Video Retrieval. [IEEE Trans. Image Process.28(4)](https://dblp.org/db/journals/tip/tip28.html#journals/tip/WuHGLDNS19): 1993-2007 (2019)
- ![](https://dblp.org/img/n.png)

\[j67\]
[Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuchen Guo](https://dblp.org/pid/132/7979.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kai Chen](https://dblp.org/pid/181/2839.html), [Chaoqun Chu](https://dblp.org/pid/233/6032.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Qionghai Dai](https://dblp.org/pid/39/4543.html):

DECODE: Deep Confidence Network for Robust Image Classification. [IEEE Trans. Image Process.28(8)](https://dblp.org/db/journals/tip/tip28.html#journals/tip/DingGCCHD19): 3752-3765 (2019)
- ![](https://dblp.org/img/n.png)

\[j66\]
[Ce Li](https://dblp.org/pid/58/411-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chen Chen](https://dblp.org/pid/65/4423-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qixiang Ye](https://dblp.org/pid/06/4335.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Guodong Guo](https://dblp.org/pid/92/4520.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Deep Manifold Structure Transfer for Action Recognition. [IEEE Trans. Image Process.28(9)](https://dblp.org/db/journals/tip/tip28.html#journals/tip/LiZCYHGJ19): 4646-4658 (2019)
- ![](https://dblp.org/img/n.png)

\[j65\]
[Sicheng Zhao](https://dblp.org/pid/65/10574.html), [Amir Gholaminejad](https://dblp.org/pid/150/6303.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Yue Gao](https://dblp.org/pid/33/3099-2.html), Jungong Han, [Kurt Keutzer](https://dblp.org/pid/k/KurtKeutzer.html):

Personalized Emotion Recognition by Personality-Aware High-Order Learning of Physiological Signals. [ACM Trans. Multim. Comput. Commun. Appl.15(1s)](https://dblp.org/db/journals/tomccap/tomccap15.html#journals/tomccap/ZhaoGDGHK19): 14:1-14:18 (2019)
- ![](https://dblp.org/img/n.png)

\[c73\]
[Jiaxin Gu](https://dblp.org/pid/218/5361.html), [Ce Li](https://dblp.org/pid/58/411-2.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han, [Xianbin Cao](https://dblp.org/pid/22/3485.html), [Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html), [David S. Doermann](https://dblp.org/pid/88/6921.html):

Projection Convolutional Neural Networks for 1-bit CNNs via Discrete Back Propagation. [AAAI2019](https://dblp.org/db/conf/aaai/aaai2019.html#conf/aaai/GuLZH0LD19): 8344-8351
- ![](https://dblp.org/img/n.png)

\[c72\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), [Zheng Wang](https://dblp.org/pid/w/ZhengWang1.html), [Chenggang Yan](https://dblp.org/pid/146/1605.html), [Qionghai Dai](https://dblp.org/pid/39/4543.html):

Dual-View Ranking with Hardness Assessment for Zero-Shot Learning. [AAAI2019](https://dblp.org/db/conf/aaai/aaai2019.html#conf/aaai/GuoDHDZWYD19): 8360-8367
- ![](https://dblp.org/img/n.png)

\[c71\]
[Yuanjun Huang](https://dblp.org/pid/168/0702.html), [Xianbin Cao](https://dblp.org/pid/22/3485.html), [Xiantong Zhen](https://dblp.org/pid/78/10651.html), Jungong Han:

Attentive Temporal Pyramid Network for Dynamic Scene Classification. [AAAI2019](https://dblp.org/db/conf/aaai/aaai2019.html#conf/aaai/Huang0ZH19): 8497-8504
- ![](https://dblp.org/img/n.png)

\[c70\]
[Xiangyang Li](https://dblp.org/pid/80/4579-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shuqiang Jiang](https://dblp.org/pid/90/3651.html), Jungong Han:

Learning Object Context for Dense Captioning. [AAAI2019](https://dblp.org/db/conf/aaai/aaai2019.html#conf/aaai/0002JH19): 8650-8657
- ![](https://dblp.org/img/n.png)

\[c69\]
[Xin Zhao](https://dblp.org/pid/68/2766-20.html), [Liufang Sang](https://dblp.org/pid/222/7857.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Na Di](https://dblp.org/pid/38/10015.html), [Chenggang Yan](https://dblp.org/pid/146/1605.html):

Recurrent Attention Model for Pedestrian Attribute Recognition. [AAAI2019](https://dblp.org/db/conf/aaai/aaai2019.html#conf/aaai/ZhaoSDHDY19): 9275-9282
- ![](https://dblp.org/img/n.png)

\[c68\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), Jungong Han:

Centripetal SGD for Pruning Very Deep Convolutional Networks With Complicated Structure. [CVPR2019](https://dblp.org/db/conf/cvpr/cvpr2019.html#conf/cvpr/DingDGH19): 4943-4953
- ![](https://dblp.org/img/n.png)

\[c67\]
[Yi Liu](https://dblp.org/pid/97/4626-38.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Dingwen Zhang](https://dblp.org/pid/150/6620.html), Jungong Han:

Employing Deep Part-Object Relationships for Salient Object Detection. [ICCV2019](https://dblp.org/db/conf/iccv/iccv2019.html#conf/iccv/00380ZH19): 1232-1241
- ![](https://dblp.org/img/n.png)

\[c66\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

ACNet: Strengthening the Kernel Skeletons for Powerful CNN via Asymmetric Convolution Blocks. [ICCV2019](https://dblp.org/db/conf/iccv/iccv2019.html#conf/iccv/DingGDH19): 1911-1920
- ![](https://dblp.org/img/n.png)

\[c65\]
[Zhong Ji](https://dblp.org/pid/36/6466.html), [Haoran Wang](https://dblp.org/pid/28/3021-4.html), Jungong Han, [Yanwei Pang](https://dblp.org/pid/35/5889.html):

Saliency-Guided Attention Network for Image-Sentence Matching. [ICCV2019](https://dblp.org/db/conf/iccv/iccv2019.html#conf/iccv/JiWHP19): 5753-5762
- ![](https://dblp.org/img/n.png)

\[c64\]
[Jiale Cao](https://dblp.org/pid/167/3851.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han, [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html):

Hierarchical Shot Detector. [ICCV2019](https://dblp.org/db/conf/iccv/iccv2019.html#conf/iccv/CaoPHL19): 9704-9713
- ![](https://dblp.org/img/n.png)

\[c63\]
[Yuefeng Wu](https://dblp.org/pid/31/8555.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), [Bolin Gao](https://dblp.org/pid/120/1968.html), Jungong Han:

Complementary Features with Reasonable Receptive Field for Road Scene 3D Object Detection. [ICIP2019](https://dblp.org/db/conf/icip/icip2019.html#conf/icip/WuPGH19): 3905-3909
- ![](https://dblp.org/img/n.png)

\[c62\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), Jungong Han, [Chenggang Yan](https://dblp.org/pid/146/1605.html):

Approximated Oracle Filter Pruning for Destructive CNN Width Optimization. [ICML2019](https://dblp.org/db/conf/icml/icml2019.html#conf/icml/DingDGHY19): 1607-1616
- ![](https://dblp.org/img/n.png)

\[c61\]
[Tianxiang Pan](https://dblp.org/pid/195/8239.html), [Bin Wang](https://dblp.org/pid/13/1898-21.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Jun-Hai Yong](https://dblp.org/pid/50/4074.html):

Low Shot Box Correction for Weakly Supervised Object Detection. [IJCAI2019](https://dblp.org/db/conf/ijcai/ijcai2019.html#conf/ijcai/PanWDHY19): 890-896
- ![](https://dblp.org/img/n.png)

\[c60\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Hang Shao](https://dblp.org/pid/390/0465.html), [Xin Lou](https://dblp.org/pid/133/5204.html), [Qionghai Dai](https://dblp.org/pid/39/4543.html):

Zero-shot Learning with Many Classes by High-rank Deep Embedding Networks. [IJCAI2019](https://dblp.org/db/conf/ijcai/ijcai2019.html#conf/ijcai/GuoDHSLD19): 2428-2434
- ![](https://dblp.org/img/n.png)

\[c59\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Chenggang Yan](https://dblp.org/pid/146/1605.html), [Jiyong Zhang](https://dblp.org/pid/95/6425-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qionghai Dai](https://dblp.org/pid/39/4543.html):

Landmark Selection for Zero-shot Learning. [IJCAI2019](https://dblp.org/db/conf/ijcai/ijcai2019.html#conf/ijcai/GuoDHYZD19): 2435-2441
- ![](https://dblp.org/img/n.png)

\[c58\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [De-Yan Xie](https://dblp.org/pid/02/8462.html), [Quanxue Gao](https://dblp.org/pid/63/804.html), Jungong Han, [Shujian Wang](https://dblp.org/pid/37/1991.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html):

Graph and Autoencoder Based Feature Extraction for Zero-shot Learning. [IJCAI2019](https://dblp.org/db/conf/ijcai/ijcai2019.html#conf/ijcai/LiuXGHWG19): 3038-3044
- ![](https://dblp.org/img/n.png)

\[c57\]
[Liuyu Xiang](https://dblp.org/pid/242/7959.html), [Xiaoming Jin](https://dblp.org/pid/26/5593.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Leida Li](https://dblp.org/pid/92/6630.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Incremental Few-Shot Learning for Pedestrian Attribute Recognition. [IJCAI2019](https://dblp.org/db/conf/ijcai/ijcai2019.html#conf/ijcai/XiangJDHL19): 3912-3918
- ![](https://dblp.org/img/n.png)

\[c56\]
[Hui Chen](https://dblp.org/pid/12/417-13.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), Jungong Han:

Cross-Modal Image-Text Retrieval with Semantic Consistency. [ACM Multimedia2019](https://dblp.org/db/conf/mm/mm2019.html#conf/mm/ChenDLZH19): 1749-1757
- ![](https://dblp.org/img/n.png)

\[c55\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Xiangxin Zhou](https://dblp.org/pid/247/9275.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), Jungong Han, [Ji Liu](https://dblp.org/pid/51/4433-2.html):

Global Sparse Momentum SGD for Pruning Very Deep Neural Networks. [NeurIPS2019](https://dblp.org/db/conf/nips/nips2019.html#conf/nips/DingDZGHL19): 6379-6391
- ![](https://dblp.org/img/n.png)

\[c54\]
[Xiaoyu Zheng](https://dblp.org/pid/20/3589.html), [Heng Liu](https://dblp.org/pid/59/3260-2.html), Jungong Han, [Shudong Hou](https://dblp.org/pid/28/8546.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Deep Feature-Preserving Based Face Hallucination: Feature Discrimination Versus Pixels Approximation. [PRCV (2)2019](https://dblp.org/db/conf/prcv/prcv2019-2.html#conf/prcv/Zheng0HH19): 114-125
- ![](https://dblp.org/img/n.png)

\[c53\]
[Xiaodi Wang](https://dblp.org/pid/07/8227.html), [Ce Li](https://dblp.org/pid/58/411-2.html), [Yipeng Mou](https://dblp.org/pid/237/1187.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han, [Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html):

Taylor Convolutional Networks for Image Classification. [WACV2019](https://dblp.org/db/conf/wacv/wacv2019.html#conf/wacv/WangLMZHL19): 1271-1279
- ![](https://dblp.org/img/n.png)

\[e1\]
[Nicola Conci](https://dblp.org/pid/32/3652.html), [Caifeng Shan](https://dblp.org/pid/98/428.html), [Lucio Marcenaro](https://dblp.org/pid/84/355.html), Jungong Han:

Proceedings of the 13th International Conference on Distributed Smart Cameras, ICDSC 2019, Trento, Italy, September 9-11, 2019.ACM2019, ISBN 978-1-4503-7189-6 [\[contents\]](https://dblp.org/db/conf/icdsc/icdsc2019.html)
- ![](https://dblp.org/img/n.png)

\[i21\]
[Jiaojiao Zhao](https://dblp.org/pid/150/4197.html), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html), [Cees G. M. Snoek](https://dblp.org/pid/s/CeesSnoek.html):

Pixelated Semantic Colorization. [CoRRabs/1901.10889](https://dblp.org/db/journals/corr/corr1901.html#journals/corr/abs-1901-10889) (2019)
- ![](https://dblp.org/img/n.png)

\[i20\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), Jungong Han:

Centripetal SGD for Pruning Very Deep Convolutional Networks with Complicated Structure. [CoRRabs/1904.03837](https://dblp.org/db/journals/corr/corr1904.html#journals/corr/abs-1904-03837) (2019)
- ![](https://dblp.org/img/n.png)

\[i19\]
[Zhong Ji](https://dblp.org/pid/36/6466.html), [Haoran Wang](https://dblp.org/pid/28/3021-4.html), Jungong Han, [Yanwei Pang](https://dblp.org/pid/35/5889.html):

Saliency-Guided Attention Network for Image-Sentence Matching. [CoRRabs/1904.09471](https://dblp.org/db/journals/corr/corr1904.html#journals/corr/abs-1904-09471) (2019)
- ![](https://dblp.org/img/n.png)

\[i18\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), Jungong Han, [Chenggang Yan](https://dblp.org/pid/146/1605.html):

Approximated Oracle Filter Pruning for Destructive CNN Width Optimization. [CoRRabs/1905.04748](https://dblp.org/db/journals/corr/corr1905.html#journals/corr/abs-1905-04748) (2019)
- ![](https://dblp.org/img/n.png)

\[i17\]
[Liuyu Xiang](https://dblp.org/pid/242/7959.html), [Xiaoming Jin](https://dblp.org/pid/26/5593.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Leida Li](https://dblp.org/pid/92/6630.html):

Incremental Few-Shot Learning for Pedestrian Attribute Recognition. [CoRRabs/1906.00330](https://dblp.org/db/journals/corr/corr1906.html#journals/corr/abs-1906-00330) (2019)
- ![](https://dblp.org/img/n.png)

\[i16\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

ACNet: Strengthening the Kernel Skeletons for Powerful CNN via Asymmetric Convolution Blocks. [CoRRabs/1908.03930](https://dblp.org/db/journals/corr/corr1908.html#journals/corr/abs-1908-03930) (2019)
- ![](https://dblp.org/img/n.png)

\[i15\]
[Yunlong Yu](https://dblp.org/pid/45/7404.html), [Zhongfei Zhang](https://dblp.org/pid/z/ZhongfeiMarkZhang.html), Jungong Han:

Meta-Transfer Networks for Zero-Shot Learning. [CoRRabs/1909.03360](https://dblp.org/db/journals/corr/corr1909.html#journals/corr/abs-1909-03360) (2019)
- ![](https://dblp.org/img/n.png)

\[i14\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Xiangxin Zhou](https://dblp.org/pid/247/9275.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), [Ji Liu](https://dblp.org/pid/51/4433-2.html), Jungong Han:

Global Sparse Momentum SGD for Pruning Very Deep Neural Networks. [CoRRabs/1909.12778](https://dblp.org/db/journals/corr/corr1909.html#journals/corr/abs-1909-12778) (2019)
- ![](https://dblp.org/img/n.png)

\[i13\]
[Chunlei Liu](https://dblp.org/pid/76/5853-1.html), [Wenrui Ding](https://dblp.org/pid/08/10143.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Vittorio Murino](https://dblp.org/pid/62/6790.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han, [Guodong Guo](https://dblp.org/pid/92/4520.html):

Aggregation Signature for Small Object Tracking. [CoRRabs/1910.10859](https://dblp.org/db/journals/corr/corr1910.html#journals/corr/abs-1910-10859) (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[j64\]
[Heng Liu](https://dblp.org/pid/59/3260-2.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Shudong Hou](https://dblp.org/pid/28/8546.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yue Ruan](https://dblp.org/pid/117/4718.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Single image super-resolution using a deep encoder-decoder symmetrical network with iterative back projection. [Neurocomputing282](https://dblp.org/db/journals/ijon/ijon282.html#journals/ijon/LiuHHSY18): 52-59 (2018)
- ![](https://dblp.org/img/n.png)

\[j63\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Yi Liu](https://dblp.org/pid/97/4626-38.html), [Rick S. Blum](https://dblp.org/pid/11/4798.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Dacheng Tao](https://dblp.org/pid/46/3391.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Sparse representation based multi-sensor image fusion for multi-focus and multi-modality images: A review. [Inf. Fusion40](https://dblp.org/db/journals/inffus/inffus40.html#journals/inffus/ZhangLBHT18): 57-75 (2018)
- ![](https://dblp.org/img/n.png)

\[j62\]
[Liu Yi](https://dblp.org/pid/46/3050.html), [Qiang Zhang](https://dblp.org/pid/72/3527-20.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Long Wang](https://dblp.org/pid/68/4459-1.html):

Salient object detection employing robust sparse representation and local consistency. [Image Vis. Comput.69](https://dblp.org/db/journals/ivc/ivc69.html#journals/ivc/YiZHW18): 155-167 (2018)
- ![](https://dblp.org/img/n.png)

\[j61\]
[Xianghai Cao](https://dblp.org/pid/177/0184.html), [Yamei Ji](https://dblp.org/pid/228/7312.html), [Lin Wang](https://dblp.org/pid/17/6729.html), [Beibei Ji](https://dblp.org/pid/228/7534.html), [Licheng Jiao](https://dblp.org/pid/40/3714.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Fast hyperspectral band selection based on spatial feature extraction. [J. Real Time Image Process.15(3)](https://dblp.org/db/journals/jrtip/jrtip15.html#journals/jrtip/CaoJWJJH18): 555-564 (2018)
- ![](https://dblp.org/img/n.png)

\[j60\]
[Heng Liu](https://dblp.org/pid/59/3260-2.html), [Zilin Fu](https://dblp.org/pid/218/9871.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongshen Liu](https://dblp.org/pid/169/4604.html):

Single satellite imagery simultaneous super-resolution and colorization using multi-task deep neural networks. [J. Vis. Commun. Image Represent.53](https://dblp.org/db/journals/jvcir/jvcir53.html#journals/jvcir/0002FH0L18): 20-30 (2018)
- ![](https://dblp.org/img/n.png)

\[j59\]
[Dimitrios Sakkos](https://dblp.org/pid/224/7712.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Heng Liu](https://dblp.org/pid/59/3260-2.html), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

End-to-end video background subtraction with 3d convolutional neural networks. [Multim. Tools Appl.77(17)](https://dblp.org/db/journals/mta/mta77.html#journals/mta/SakkosLHS18): 23023-23041 (2018)
- ![](https://dblp.org/img/n.png)

\[j58\]
[Ce Li](https://dblp.org/pid/58/411-2.html), [Chunyu Xie](https://dblp.org/pid/187/1594.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Deep Fisher discriminant learning for mobile hand gesture recognition. [Pattern Recognit.77](https://dblp.org/db/journals/pr/pr77.html#journals/pr/LiXZCH18): 276-288 (2018)
- ![](https://dblp.org/img/n.png)

\[j57\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Tao Shi](https://dblp.org/pid/42/1958.html), [Fan Wang](https://dblp.org/pid/88/898.html), [Rick S. Blum](https://dblp.org/pid/11/4798.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Robust sparse representation based multi-focus image fusion with dictionary construction and local spatial consistency. [Pattern Recognit.83](https://dblp.org/db/journals/pr/pr83.html#journals/pr/ZhangSWBH18): 299-313 (2018)
- ![](https://dblp.org/img/n.png)

\[j56\]
[Duona Zhang](https://dblp.org/pid/217/3671.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenrui Ding](https://dblp.org/pid/08/10143.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Chunyu Xie](https://dblp.org/pid/187/1594.html), [Hongguang Li](https://dblp.org/pid/02/3703.html), [Chunhui Liu](https://dblp.org/pid/20/5393-4.html), Jungong Han:

Automatic Modulation Classification Based on Deep Learning for Unmanned Aerial Vehicles. [Sensors18(3)](https://dblp.org/db/journals/sensors/sensors18.html#journals/sensors/ZhangDZXLLH18): 924 (2018)
- ![](https://dblp.org/img/n.png)

\[j55\]
[Hai Li](https://dblp.org/pid/30/5330.html), [Jie Wang](https://dblp.org/pid/29/5259.html), [Yi Fan](https://dblp.org/pid/10/2921.html), Jungong Han:

High-Fidelity Inhomogeneous Ground Clutter Simulation of Airborne Phased Array PD Radar Aided by Digital Elevation Model and Digital Land Classification Data. [Sensors18(9)](https://dblp.org/db/journals/sensors/sensors18.html#journals/sensors/LiWFH18): 2925 (2018)
- ![](https://dblp.org/img/n.png)

\[j54\]
[Fouad Khelifi](https://dblp.org/pid/95/4960.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tahar Brahimi](https://dblp.org/pid/88/8631.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Xuelong Li](https://dblp.org/pid/l/XuelongLi.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Secure and privacy-preserving data sharing in the cloud based on lossless image coding. [Signal Process.148](https://dblp.org/db/journals/sigpro/sigpro148.html#journals/sigpro/KhelifiBHL18): 91-101 (2018)
- ![](https://dblp.org/img/n.png)

\[j53\]
[Shoubiao Tan](https://dblp.org/pid/64/7731.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Li Liu](https://dblp.org/pid/33/4528-4.html), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Dense Invariant Feature-Based Support Vector Ranking for Cross-Camera Person Reidentification. [IEEE Trans. Circuits Syst. Video Technol.28(2)](https://dblp.org/db/journals/tcsv/tcsv28.html#journals/tcsv/TanZLHS18): 356-363 (2018)
- ![](https://dblp.org/img/n.png)

\[j52\]
[Jiaojiao Zhao](https://dblp.org/pid/150/4197.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Unconstrained Face Recognition Using a Set-to-Set Distance Measure on Deep Learned Features. [IEEE Trans. Circuits Syst. Video Technol.28(10)](https://dblp.org/db/journals/tcsv/tcsv28.html#journals/tcsv/ZhaoHS18): 2679-2689 (2018)
- ![](https://dblp.org/img/n.png)

\[j51\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Robust Quantization for General Similarity Search. [IEEE Trans. Image Process.27(2)](https://dblp.org/db/journals/tip/tip27.html#journals/tip/GuoDH18): 949-963 (2018)
- ![](https://dblp.org/img/n.png)

\[j50\]
[Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Shangzhen Luan](https://dblp.org/pid/182/1956.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), Jungong Han, [Wei Wang](https://dblp.org/pid/w/WeiWang16.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alessandro Perina](https://dblp.org/pid/54/1195.html), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Latent Constrained Correlation Filter. [IEEE Trans. Image Process.27(3)](https://dblp.org/db/journals/tip/tip27.html#journals/tip/ZhangLCHWPS18): 1038-1048 (2018)
- ![](https://dblp.org/img/n.png)

\[j49\]
[Shangzhen Luan](https://dblp.org/pid/182/1956.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html):

Gabor Convolutional Networks. [IEEE Trans. Image Process.27(9)](https://dblp.org/db/journals/tip/tip27.html#journals/tip/LuanCZHL18): 4357-4366 (2018)
- ![](https://dblp.org/img/n.png)

\[j48\]
[Jingtian Zhang](https://dblp.org/pid/181/3959.html), [Hubert P. H. Shum](https://dblp.org/pid/14/4870.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Action Recognition From Arbitrary Views Using Transferable Dictionary Learning. [IEEE Trans. Image Process.27(10)](https://dblp.org/db/journals/tip/tip27.html#journals/tip/ZhangSHS18): 4709-4723 (2018)
- ![](https://dblp.org/img/n.png)

\[j47\]
[Shuangli Liao](https://dblp.org/pid/218/7458.html), [Quanxue Gao](https://dblp.org/pid/63/804.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhaohua Yang](https://dblp.org/pid/117/3393.html), [Fang Chen](https://dblp.org/pid/52/488.html), [Feiping Nie](https://dblp.org/pid/80/5755.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Discriminant Analysis via Joint Euler Transform and ℓ2, 1-Norm. [IEEE Trans. Image Process.27(11)](https://dblp.org/db/journals/tip/tip27.html#journals/tip/LiaoGYCNH18): 5668-5682 (2018)
- ![](https://dblp.org/img/n.png)

\[j46\]
[Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenshuo Chen](https://dblp.org/pid/193/3404.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Qiaoyan Liu](https://dblp.org/pid/212/1390.html):

Real-Time Scalable Visual Tracking via Quadrangle Kernelized Correlation Filters. [IEEE Trans. Intell. Transp. Syst.19(1)](https://dblp.org/db/journals/tits/tits19.html#journals/tits/DingCZHL18): 140-150 (2018)
- ![](https://dblp.org/img/n.png)

\[j45\]
[Zijia Lin](https://dblp.org/pid/78/9911.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

End-to-End Feature-Aware Label Space Encoding for Multilabel Classification With Many Classes. [IEEE Trans. Neural Networks Learn. Syst.29(6)](https://dblp.org/db/journals/tnn/tnn29.html#journals/tnn/LinDHS18): 2472-2487 (2018)
- ![](https://dblp.org/img/n.png)

\[c52\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html), [Xin Zhao](https://dblp.org/pid/68/2766-20.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

On Trivial Solution and High Correlation Problems in Deep Supervised Hashing. [AAAI2018](https://dblp.org/db/conf/aaai/aaai2018.html#conf/aaai/GuoZDH18): 2240-2247
- ![](https://dblp.org/img/n.png)

\[c51\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Quanxue Gao](https://dblp.org/pid/63/804.html), Jungong Han, [Shujian Wang](https://dblp.org/pid/37/1991.html):

Euler Sparse Representation for Image Classification. [AAAI2018](https://dblp.org/db/conf/aaai/aaai2018.html#conf/aaai/LiuGHW18): 3691-3697
- ![](https://dblp.org/img/n.png)

\[c50\]
[Hui Chen](https://dblp.org/pid/12/417-13.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), Jungong Han:

Temporal-Difference Learning With Sampling Baseline for Image Captioning. [AAAI2018](https://dblp.org/db/conf/aaai/aaai2018.html#conf/aaai/ChenDZH18): 6706-6713
- ![](https://dblp.org/img/n.png)

\[c49\]
[Xiaohan Ding](https://dblp.org/pid/218/7379.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Sheng Tang](https://dblp.org/pid/62/1647.html):

Auto-Balanced Filter Pruning for Efficient Convolutional Neural Networks. [AAAI2018](https://dblp.org/db/conf/aaai/aaai2018.html#conf/aaai/DingDHT18): 6797-6804
- ![](https://dblp.org/img/n.png)

\[c48\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Sheng Tang](https://dblp.org/pid/62/1647.html):

Zero-Shot Learning With Attribute Selection. [AAAI2018](https://dblp.org/db/conf/aaai/aaai2018.html#conf/aaai/GuoDHT18): 6870-6877
- ![](https://dblp.org/img/n.png)

\[c47\]
[Hui Chen](https://dblp.org/pid/12/417-13.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), Jungong Han:

Attend to Knowledge: Memory-Enhanced Attention Network for Image Captioning. [BICS2018](https://dblp.org/db/conf/bics/bics2018.html#conf/bics/ChenDLGH18): 161-171
- ![](https://dblp.org/img/n.png)

\[c46\]
[Jiaojiao Zhao](https://dblp.org/pid/150/4197.html), [Li Liu](https://dblp.org/pid/33/4528-4.html), [Cees Snoek](https://dblp.org/pid/s/CeesSnoek.html), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html):

Pixel-level Semantics Guided Image Colorization. [BMVC2018](https://dblp.org/db/conf/bmvc/bmvc2018.html#conf/bmvc/Zhao0SH018): 156
- ![](https://dblp.org/img/n.png)

\[c45\]
[Xiaodi Wang](https://dblp.org/pid/07/8227.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Ce Li](https://dblp.org/pid/58/411-2.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Xianbin Cao](https://dblp.org/pid/22/3485.html), [Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html):

Modulated Convolutional Networks. [CVPR2018](https://dblp.org/db/conf/cvpr/cvpr2018.html#conf/cvpr/WangZLJH0L18): 840-848
- ![](https://dblp.org/img/n.png)

\[c44\]
[Longyin Wen](https://dblp.org/pid/119/1468.html), [Pengfei Zhu](https://dblp.org/pid/40/6172-1.html), [Dawei Du](https://dblp.org/pid/51/6958.html), [Xiao Bian](https://dblp.org/pid/116/5018.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Qinghua Hu](https://dblp.org/pid/30/2395.html), [Chenfeng Liu](https://dblp.org/pid/174/4324.html), [Hao Cheng](https://dblp.org/pid/09/5158-10.html), [Xiaoyu Liu](https://dblp.org/pid/78/6195-5.html), [Wenya Ma](https://dblp.org/pid/180/7077.html), [Qinqin Nie](https://dblp.org/pid/234/1733.html), [Haotian Wu](https://dblp.org/pid/145/5323-6.html), [Lianjie Wang](https://dblp.org/pid/18/2688.html), [Asanka G. Perera](https://dblp.org/pid/231/9229.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Byeongho Heo](https://dblp.org/pid/142/2705.html), [Chunlei Liu](https://dblp.org/pid/76/5853-1.html), [Dongdong Li](https://dblp.org/pid/14/5457.html), [Emmanouil Michail](https://dblp.org/pid/72/7219.html), [Hanlin Chen](https://dblp.org/pid/97/1735.html), [Hao Liu](https://dblp.org/pid/09/3214-19.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haojie Li](https://dblp.org/pid/61/4041.html), [Ioannis Kompatsiaris](https://dblp.org/pid/k/YiannisKompatsiaris.html), [Jian Cheng](https://dblp.org/pid/14/6145-1.html), [Jiaqing Fan](https://dblp.org/pid/227/6586.html), [Jie Zhang](https://dblp.org/pid/84/6889-91.html), [Jin Young Choi](https://dblp.org/pid/30/1428-2.html), [Jing Li](https://dblp.org/pid/l/JingLi36.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Jongwon Choi](https://dblp.org/pid/126/0675-2.html), [Juanping Zhao](https://dblp.org/pid/120/5177.html), Jungong Han, [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kaiwen Duan](https://dblp.org/pid/190/4878.html), [Ke Song](https://dblp.org/pid/194/3688-3.html), [Konstantinos Avgerinakis](https://dblp.org/pid/15/10110.html), [Kyuewang Lee](https://dblp.org/pid/189/5760.html), [Lu Ding](https://dblp.org/pid/135/0285.html), [Martin Lauer](https://dblp.org/pid/87/2031.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Panagiotis Giannakeris](https://dblp.org/pid/213/4135.html), [Peizhen Zhang](https://dblp.org/pid/115/9027.html), [Qiang Wang](https://dblp.org/pid/64/5630-51.html), [Qianqian Xu](https://dblp.org/pid/07/7627-1.html), [Qingming Huang](https://dblp.org/pid/68/4388.html), [Qingshan Liu](https://dblp.org/pid/95/1247.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Robert Laganière](https://dblp.org/pid/32/1448.html), [Ruixin Zhang](https://dblp.org/pid/132/6250.html), [Sangdoo Yun](https://dblp.org/pid/124/3009.html), [Shengyin Zhu](https://dblp.org/pid/234/1707.html), [Sihang Wu](https://dblp.org/pid/234/0006.html), [Stefanos Vrochidis](https://dblp.org/pid/44/6029.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Tian](https://dblp.org/pid/56/3860-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Zhang](https://dblp.org/pid/10/4661-21.html), [Weidong Chen](https://dblp.org/pid/196/5142-13.html), [Weiming Hu](https://dblp.org/pid/41/6824-4.html), [Wenhao Wang](https://dblp.org/pid/57/9813.html), [Wenhua Zhang](https://dblp.org/pid/28/1877.html), [Wenrui Ding](https://dblp.org/pid/08/10143.html), [Xiaohao He](https://dblp.org/pid/219/4446.html), [Xiaotong Li](https://dblp.org/pid/35/4953.html), [Xin Zhang](https://dblp.org/pid/76/1584-8.html), [Xinbin Luo](https://dblp.org/pid/234/1736.html), [Xixi Hu](https://dblp.org/pid/234/1710-3.html), [Yang Meng](https://dblp.org/pid/41/7386.html), [Yangliu Kuai](https://dblp.org/pid/202/5604.html), [Yanyun Zhao](https://dblp.org/pid/12/7547.html), [Yaxuan Li](https://dblp.org/pid/92/6967.html), [Yifan Yang](https://dblp.org/pid/83/89.html), [Yifan Zhang](https://dblp.org/pid/57/4707-1.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yuankai Qi](https://dblp.org/pid/136/5491.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhipeng Deng](https://dblp.org/pid/30/10701.html), [Zhiqun He](https://dblp.org/pid/213/4141.html):

VisDrone-SOT2018: The Vision Meets Drone Single-Object Tracking Challenge Results. [ECCV Workshops (5)2018](https://dblp.org/db/conf/eccv/eccv2018w5.html#conf/eccv/WenZDBLHLCLMNWW18): 469-495
- ![](https://dblp.org/img/n.png)

\[c43\]
[Hui Chen](https://dblp.org/pid/12/417-13.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), Jungong Han:

Show, Observe and Tell: Attribute-driven Attention Model for Image Captioning. [IJCAI2018](https://dblp.org/db/conf/ijcai/ijcai2018.html#conf/ijcai/ChenDLZH18): 606-612
- ![](https://dblp.org/img/n.png)

\[c42\]
[Chunyu Xie](https://dblp.org/pid/187/1594.html), [Ce Li](https://dblp.org/pid/58/411-2.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), Jungong Han, [Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html):

Memory Attention Networks for Skeleton-based Action Recognition. [IJCAI2018](https://dblp.org/db/conf/ijcai/ijcai2018.html#conf/ijcai/XieLZ0HL18): 1639-1645
- ![](https://dblp.org/img/n.png)

\[c41\]
[Sicheng Zhao](https://dblp.org/pid/65/10574.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Yue Gao](https://dblp.org/pid/33/3099-2.html):

Personality-Aware Personalized Emotion Recognition from Physiological Signals. [IJCAI2018](https://dblp.org/db/conf/ijcai/ijcai2018.html#conf/ijcai/ZhaoDHG18): 1660-1667
- ![](https://dblp.org/img/n.png)

\[c40\]
[Yang Liu](https://dblp.org/pid/51/3710-0069.html), [Quanxue Gao](https://dblp.org/pid/63/804.html), [Jin Li](https://dblp.org/pid/48/1097-11.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html):

Zero Shot Learning via Low-rank Embedded Semantic AutoEncoder. [IJCAI2018](https://dblp.org/db/conf/ijcai/ijcai2018.html#conf/ijcai/LiuGLH018): 2490-2496
- ![](https://dblp.org/img/n.png)

\[c39\]
[Gengshen Wu](https://dblp.org/pid/204/2949.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), Jungong Han, [Li Liu](https://dblp.org/pid/33/4528-4.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Jialie Shen](https://dblp.org/pid/33/7046.html):

Unsupervised Deep Hashing via Binary Latent Factor Models for Large-scale Cross-modal Retrieval. [IJCAI2018](https://dblp.org/db/conf/ijcai/ijcai2018.html#conf/ijcai/WuLHLDZS18): 2854-2860
- ![](https://dblp.org/img/n.png)

\[c38\]
[Jing Zhong](https://dblp.org/pid/09/2522.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), Jungong Han, [Bin Wang](https://dblp.org/pid/13/1898-21.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Where to Prune: Using LSTM to Guide End-to-end Pruning. [IJCAI2018](https://dblp.org/db/conf/ijcai/ijcai2018.html#conf/ijcai/ZhongDGHW18): 3205-3211
- ![](https://dblp.org/img/n.png)

\[c37\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Sicheng Zhao](https://dblp.org/pid/65/10574.html), [Bin Wang](https://dblp.org/pid/13/1898-21.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Implicit Non-linear Similarity Scoring for Recognizing Unseen Classes. [IJCAI2018](https://dblp.org/db/conf/ijcai/ijcai2018.html#conf/ijcai/GuoDHZW18): 4898-4904
- ![](https://dblp.org/img/n.png)

\[c36\]
[Shangzhen Luan](https://dblp.org/pid/182/1956.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Siyue Zhou](https://dblp.org/pid/218/9477.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), Jungong Han, [Wankou Yang](https://dblp.org/pid/99/3602.html), [Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html):

Gabor Convolutional Networks. [WACV2018](https://dblp.org/db/conf/wacv/wacv2018.html#conf/wacv/LuanZZ0HYL18): 1254-1262
- ![](https://dblp.org/img/n.png)

\[i12\]
[Zhong Ji](https://dblp.org/pid/36/6466.html), [Yunxin Sun](https://dblp.org/pid/200/7880-2.html), [Yunlong Yu](https://dblp.org/pid/45/7404.html), [Yanwei Pang](https://dblp.org/pid/35/5889.html), Jungong Han:

Attribute-Guided Network for Cross-Modal Zero-Shot Hashing. [CoRRabs/1802.01943](https://dblp.org/db/journals/corr/corr1802.html#journals/corr/abs-1802-01943) (2018)
- ![](https://dblp.org/img/n.png)

\[i11\]
[Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Lian Zhuo](https://dblp.org/pid/218/5220.html), [Ze Wang](https://dblp.org/pid/35/6674-8.html), Jungong Han, [Xiantong Zhen](https://dblp.org/pid/78/10651.html):

The Structure Transfer Machine Theory and Applications. [CoRRabs/1804.00243](https://dblp.org/db/journals/corr/corr1804.html#journals/corr/abs-1804-00243) (2018)
- ![](https://dblp.org/img/n.png)

\[i10\]
[Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Jiaxin Gu](https://dblp.org/pid/218/5361.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), Jungong Han, [Xiangbo Su](https://dblp.org/pid/188/7852.html), [Xianbin Cao](https://dblp.org/pid/22/3485.html), [Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html):

One-Two-One Networks for Compression Artifacts Reduction in Remote Sensing. [CoRRabs/1804.00256](https://dblp.org/db/journals/corr/corr1804.html#journals/corr/abs-1804-00256) (2018)
- ![](https://dblp.org/img/n.png)

\[i9\]
[Chunyu Xie](https://dblp.org/pid/187/1594.html), [Ce Li](https://dblp.org/pid/58/411-2.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), Jungong Han, [Changqing Zou](https://dblp.org/pid/126/1043.html), [Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html):

Memory Attention Networks for Skeleton-based Action Recognition. [CoRRabs/1804.08254](https://dblp.org/db/journals/corr/corr1804.html#journals/corr/abs-1804-08254) (2018)
- ![](https://dblp.org/img/n.png)

\[i8\]
[Jiaojiao Zhao](https://dblp.org/pid/150/4197.html), [Li Liu](https://dblp.org/pid/33/4528-4.html), [Cees G. M. Snoek](https://dblp.org/pid/s/CeesSnoek.html), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html):

Pixel-level Semantics Guided Image Colorization. [CoRRabs/1808.01597](https://dblp.org/db/journals/corr/corr1808.html#journals/corr/abs-1808-01597) (2018)
- ![](https://dblp.org/img/n.png)

\[i7\]
[Jiaxin Gu](https://dblp.org/pid/218/5361.html), [Ce Li](https://dblp.org/pid/58/411-2.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han, [Xianbin Cao](https://dblp.org/pid/22/3485.html), [Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html), [David S. Doermann](https://dblp.org/pid/88/6921.html):

Projection Convolutional Neural Networks for 1-bit CNNs via Discrete Back Propagation. [CoRRabs/1811.12755](https://dblp.org/db/journals/corr/corr1811.html#journals/corr/abs-1811-12755) (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[j44\]
[Chen Chen](https://dblp.org/pid/65/4423-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mengyuan Liu](https://dblp.org/pid/143/0160.html), [Hong Liu](https://dblp.org/pid/29/5010-8.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Nasser Kehtarnavaz](https://dblp.org/pid/62/3700.html):

Multi-Temporal Depth Motion Maps-Based Local Binary Patterns for 3-D Human Action Recognition. [IEEE Access5](https://dblp.org/db/journals/access/access5.html#journals/access/ChenLLZHK17): 22590-22604 (2017)
- ![](https://dblp.org/img/n.png)

\[j43\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Yi Liu](https://dblp.org/pid/97/4626-38.html), [Siyang Zhu](https://dblp.org/pid/206/2887.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Salient object detection based on super-pixel clustering and unified low-rank representation. [Comput. Vis. Image Underst.161](https://dblp.org/db/journals/cviu/cviu161.html#journals/cviu/ZhangLZH17): 51-64 (2017)
- ![](https://dblp.org/img/n.png)

\[j42\]
[Kai Chen](https://dblp.org/pid/181/2839.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

Attribute-based supervised deep learning model for action recognition. [Frontiers Comput. Sci.11(2)](https://dblp.org/db/journals/fcsc/fcsc11.html#journals/fcsc/ChenDH17): 219-229 (2017)
- ![](https://dblp.org/img/n.png)

\[j41\]
[Guiguang Ding](https://dblp.org/pid/51/740.html), [Jile Zhou](https://dblp.org/pid/147/9084.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), Jungong Han:

Large-scale image retrieval with Sparse Embedded Hashing. [Neurocomputing257](https://dblp.org/db/journals/ijon/ijon257.html#journals/ijon/DingZGLZH17): 24-36 (2017)
- ![](https://dblp.org/img/n.png)

\[j40\]
[Linlin Yang](https://dblp.org/pid/84/6484.html), [Ce Li](https://dblp.org/pid/58/411-2.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Chen Chen](https://dblp.org/pid/65/4423-1.html), [Qixiang Ye](https://dblp.org/pid/06/4335.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Xianbin Cao](https://dblp.org/pid/22/3485.html), [Wanquan Liu](https://dblp.org/pid/53/4712.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Image Reconstruction via Manifold Constrained Convolutional Sparse Coding for Image Sets. [IEEE J. Sel. Top. Signal Process.11(7)](https://dblp.org/db/journals/jstsp/jstsp11.html#journals/jstsp/YangLHCYZCL17): 1072-1081 (2017)
- ![](https://dblp.org/img/n.png)

\[j39\]
[Xianghai Cao](https://dblp.org/pid/177/0184.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Cuicui Wei](https://dblp.org/pid/208/0154.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Licheng Jiao](https://dblp.org/pid/40/3714.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Hyperspectral Band Selection Using Improved Classification Map. [IEEE Geosci. Remote. Sens. Lett.14(11)](https://dblp.org/db/journals/lgrs/lgrs14.html#journals/lgrs/CaoWHJ17): 2147-2151 (2017)
- ![](https://dblp.org/img/n.png)

\[j38\]
[Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Guest Editorial: Feature Learning from RGB-D Data for Multimedia Applications. [Multim. Tools Appl.76(3)](https://dblp.org/db/journals/mta/mta76.html#journals/mta/ZhangHS17): 4243-4248 (2017)
- ![](https://dblp.org/img/n.png)

\[j37\]
[Ziyun Cai](https://dblp.org/pid/179/6081.html), Jungong Han, [Li Liu](https://dblp.org/pid/33/4528-4.html), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

RGB-D datasets using microsoft kinect or similar sensors: a survey. [Multim. Tools Appl.76(3)](https://dblp.org/db/journals/mta/mta76.html#journals/mta/CaiHLS17): 4313-4355 (2017)
- ![](https://dblp.org/img/n.png)

\[j36\]
[Zijia Lin](https://dblp.org/pid/78/9911.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Jianmin Wang](https://dblp.org/pid/06/3456-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Cross-View Retrieval via Probability-Based Semantics-Preserving Hashing. [IEEE Trans. Cybern.47(12)](https://dblp.org/db/journals/tcyb/tcyb47.html#journals/tcyb/LinDHW17): 4342-4355 (2017)
- ![](https://dblp.org/img/n.png)

\[j35\]
[Li Liu](https://dblp.org/pid/33/4528-4.html), [Zijia Lin](https://dblp.org/pid/78/9911.html), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fumin Shen](https://dblp.org/pid/92/10934.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png):

Sequential Discrete Hashing for Scalable Cross-Modality Similarity Retrieval. [IEEE Trans. Image Process.26(1)](https://dblp.org/db/journals/tip/tip26.html#journals/tip/LiuLSSDH17): 107-118 (2017)
- ![](https://dblp.org/img/n.png)

\[j34\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Li Liu](https://dblp.org/pid/33/4528-4.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning to Hash With Optimized Anchor Embedding for Scalable Retrieval. [IEEE Trans. Image Process.26(3)](https://dblp.org/db/journals/tip/tip26.html#journals/tip/GuoDLHS17): 1344-1354 (2017)
- ![](https://dblp.org/img/n.png)

\[j33\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guiguang Ding](https://dblp.org/pid/51/740.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Yue Gao](https://dblp.org/pid/33/3099-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Zero-Shot Learning With Transferred Samples. [IEEE Trans. Image Process.26(7)](https://dblp.org/db/journals/tip/tip26.html#journals/tip/GuoDHG17): 3277-3290 (2017)
- ![](https://dblp.org/img/n.png)

\[j32\]
[Baochang Zhang](https://dblp.org/pid/80/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yun Yang](https://dblp.org/pid/90/3406.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), [Linlin Yang](https://dblp.org/pid/84/6484.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Action Recognition Using 3D Histograms of Texture and A Multi-Class Boosting Classifier. [IEEE Trans. Image Process.26(10)](https://dblp.org/db/journals/tip/tip26.html#journals/tip/ZhangYCYHS17): 4648-4660 (2017)
- ![](https://dblp.org/img/n.png)

\[j31\]
[Chao Yao](https://dblp.org/pid/99/6747.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ya-Feng Liu](https://dblp.org/pid/29/8760.html), [Bo Jiang](https://dblp.org/pid/34/2005-10.html), Jungong Han, [Junwei Han](https://dblp.org/pid/00/3003.html)![](https://dblp.org/img/orcid-mark.12x12.png):

LLE Score: A New Filter-Based Unsupervised Feature Selection Method Based on Nonlinear Manifold Embedding and Its Application to Image Recognition. [IEEE Trans. Image Process.26(11)](https://dblp.org/db/journals/tip/tip26.html#journals/tip/YaoLJHH17): 5257-5269 (2017)
- ![](https://dblp.org/img/n.png)

\[c35\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Yue Gao](https://dblp.org/pid/33/3099-2.html), Jungong Han:

Active Learning with Cross-Class Similarity Transfer. [AAAI2017](https://dblp.org/db/conf/aaai/aaai2017.html#conf/aaai/GuoDGH17): 1338-1344
- ![](https://dblp.org/img/n.png)

\[c34\]
[Minghai Chen](https://dblp.org/pid/195/8186.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Sicheng Zhao](https://dblp.org/pid/65/10574.html), [Hui Chen](https://dblp.org/pid/12/417-13.html), [Qiang Liu](https://dblp.org/pid/61/3234-16.html), Jungong Han:

Reference Based LSTM for Image Captioning. [AAAI2017](https://dblp.org/db/conf/aaai/aaai2017.html#conf/aaai/ChenDZCLH17): 3981-3987
- ![](https://dblp.org/img/n.png)

\[c33\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Yue Gao](https://dblp.org/pid/33/3099-2.html):

Zero-Shot Recognition via Direct Classifier Learning with Transferred Samples and Pseudo Labels. [AAAI2017](https://dblp.org/db/conf/aaai/aaai2017.html#conf/aaai/GuoDHG17): 4061-4067
- ![](https://dblp.org/img/n.png)

\[c32\]
[Yang Long](https://dblp.org/pid/82/10183-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Li Liu](https://dblp.org/pid/33/4528-4.html), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fumin Shen](https://dblp.org/pid/92/10934.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

From Zero-Shot Learning to Conventional Supervised Classification: Unseen Visual Data Synthesis. [CVPR2017](https://dblp.org/db/conf/cvpr/cvpr2017.html#conf/cvpr/LongLSSDH17): 6165-6174
- ![](https://dblp.org/img/n.png)

\[c31\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Yue Gao](https://dblp.org/pid/33/3099-2.html):

SitNet: Discrete Similarity Transfer Network for Zero-shot Hashing. [IJCAI2017](https://dblp.org/db/conf/ijcai/ijcai2017.html#conf/ijcai/GuoDHG17): 1767-1773
- ![](https://dblp.org/img/n.png)

\[c30\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Yue Gao](https://dblp.org/pid/33/3099-2.html):

Synthesizing Samples for Zero-shot Learning. [IJCAI2017](https://dblp.org/db/conf/ijcai/ijcai2017.html#conf/ijcai/GuoDHG17a): 1774-1780
- ![](https://dblp.org/img/n.png)

\[c29\]
[Gengshen Wu](https://dblp.org/pid/204/2949.html), [Li Liu](https://dblp.org/pid/33/4528-4.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Jialie Shen](https://dblp.org/pid/33/7046.html), [Ling Shao](https://dblp.org/pid/75/1281.html):

Unsupervised Deep Video Hashing with Balanced Rotation. [IJCAI2017](https://dblp.org/db/conf/ijcai/ijcai2017.html#conf/ijcai/WuLGDHSS17): 3076-3082
- ![](https://dblp.org/img/n.png)

\[c28\]
[Liang Xie](https://dblp.org/pid/81/2806-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jialie Shen](https://dblp.org/pid/33/7046.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Lei Zhu](https://dblp.org/pid/99/549-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html):

Dynamic Multi-View Hashing for Online Image Retrieval. [IJCAI2017](https://dblp.org/db/conf/ijcai/ijcai2017.html#conf/ijcai/XieSHZS17): 3133-3139
- ![](https://dblp.org/img/n.png)

\[c27\]
[Xin Zhao](https://dblp.org/pid/68/2766-20.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Yuchen Guo](https://dblp.org/pid/132/7979.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Yue Gao](https://dblp.org/pid/33/3099-2.html):

TUCH: Turning Cross-view Hashing into Single-view Hashing via Generative Adversarial Nets. [IJCAI2017](https://dblp.org/db/conf/ijcai/ijcai2017.html#conf/ijcai/ZhaoDGHG17): 3511-3517
- ![](https://dblp.org/img/n.png)

\[c26\]
[Sicheng Zhao](https://dblp.org/pid/65/10574.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Yue Gao](https://dblp.org/pid/33/3099-2.html), Jungong Han:

Approximating Discrete Probability Distribution of Image Emotions by Multi-Modal Features Fusion. [IJCAI2017](https://dblp.org/db/conf/ijcai/ijcai2017.html#conf/ijcai/ZhaoDGH17): 4669-4675
- ![](https://dblp.org/img/n.png)

\[c25\]
[Sicheng Zhao](https://dblp.org/pid/65/10574.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), [Yue Gao](https://dblp.org/pid/33/3099-2.html), Jungong Han:

Learning Visual Emotion Distributions via Multi-Modal Features Fusion. [ACM Multimedia2017](https://dblp.org/db/conf/mm/mm2017.html#conf/mm/ZhaoDGH17): 369-377
- ![](https://dblp.org/img/n.png)

\[i6\]
[Qiang Zhang](https://dblp.org/pid/72/3527-20.html), [Yi Liu](https://dblp.org/pid/97/4626-38.html), [Rick S. Blum](https://dblp.org/pid/11/4798.html), Jungong Han, [Dacheng Tao](https://dblp.org/pid/46/3391.html):

Sparse Representation based Multi-sensor Image Fusion: A Review. [CoRRabs/1702.03515](https://dblp.org/db/journals/corr/corr1702.html#journals/corr/ZhangLBHT17) (2017)
- ![](https://dblp.org/img/n.png)

\[i5\]
[Shangzhen Luan](https://dblp.org/pid/182/1956.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), [Xianbin Cao](https://dblp.org/pid/22/3485.html), Jungong Han, [Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html):

Gabor Convolutional Networks. [CoRRabs/1705.01450](https://dblp.org/db/journals/corr/corr1705.html#journals/corr/LuanZ0CHL17) (2017)
- ![](https://dblp.org/img/n.png)

\[i4\]
[Yang Long](https://dblp.org/pid/82/10183-1.html), [Li Liu](https://dblp.org/pid/33/4528-4.html), [Ling Shao](https://dblp.org/pid/75/1281.html), [Fumin Shen](https://dblp.org/pid/92/10934.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han:

From Zero-shot Learning to Conventional Supervised Classification: Unseen Visual Data Synthesis. [CoRRabs/1705.01782](https://dblp.org/db/journals/corr/corr1705.html#journals/corr/LongLSSDH17) (2017)
- ![](https://dblp.org/img/n.png)

\[i3\]
[Ce Li](https://dblp.org/pid/58/411-2.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Qixiang Ye](https://dblp.org/pid/06/4335.html), Jungong Han, [Rongrong Ji](https://dblp.org/pid/86/5681.html):

Deep Spatio-temporal Manifold Network for Action Recognition. [CoRRabs/1705.03148](https://dblp.org/db/journals/corr/corr1705.html#journals/corr/LiCZYHJ17) (2017)
- ![](https://dblp.org/img/n.png)

\[i2\]
[Chunyu Xie](https://dblp.org/pid/187/1594.html), [Ce Li](https://dblp.org/pid/58/411-2.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), Jungong Han:

Deep Fisher Discriminant Learning for Mobile Hand Gesture Recognition. [CoRRabs/1707.03692](https://dblp.org/db/journals/corr/corr1707.html#journals/corr/XieLZCH17) (2017)
- ![](https://dblp.org/img/n.png)

\[i1\]
[Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Shangzhen Luan](https://dblp.org/pid/182/1956.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), Jungong Han, [Wei Wang](https://dblp.org/pid/w/WeiWang16.html), [Alessandro Perina](https://dblp.org/pid/54/1195.html), [Ling Shao](https://dblp.org/pid/75/1281.html):

Latent Constrained Correlation Filter. [CoRRabs/1711.04192](https://dblp.org/db/journals/corr/corr1711.html#journals/corr/abs-1711-04192) (2017)
- 2016
- ![](https://dblp.org/img/n.png)

\[j30\]
[Chao Yao](https://dblp.org/pid/99/6747.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhaoyang Lu](https://dblp.org/pid/59/568.html), [Jing Li](https://dblp.org/pid/l/JingLi10.html), [Wei Jiang](https://dblp.org/pid/21/3839.html), Jungong Han:

An improved Fisher discriminant vector employing updated between-scatter matrix. [Neurocomputing173](https://dblp.org/db/journals/ijon/ijon173.html#journals/ijon/YaoLLJH16): 154-162 (2016)
- ![](https://dblp.org/img/n.png)

\[j29\]
[Lei Wang](https://dblp.org/pid/w/LeiWang18.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han, [Linlin Shen](https://dblp.org/pid/88/5607.html), [Chengshan Qian](https://dblp.org/pid/133/3243.html):

Robust object representation by boosting-like deep learning architecture. [Signal Process. Image Commun.47](https://dblp.org/db/journals/spic/spic47.html#journals/spic/WangZHSQ16): 490-499 (2016)
- ![](https://dblp.org/img/n.png)

\[j28\]
[Junwei Han](https://dblp.org/pid/00/3003.html), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Nuno Vasconcelos](https://dblp.org/pid/78/4806.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Dong Xu](https://dblp.org/pid/09/3493-1.html):

Guest Editorial Special Section on Visual Saliency Computing and Learning. [IEEE Trans. Neural Networks Learn. Syst.27(6)](https://dblp.org/db/journals/tnn/tnn27.html#journals/tnn/HanSVHX16): 1118-1121 (2016)
- ![](https://dblp.org/img/n.png)

\[j27\]
[Dingwen Zhang](https://dblp.org/pid/150/6620.html), [Junwei Han](https://dblp.org/pid/00/3003.html), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Cosaliency Detection Based on Intrasaliency Prior Transfer and Deep Intersaliency Mining. [IEEE Trans. Neural Networks Learn. Syst.27(6)](https://dblp.org/db/journals/tnn/tnn27.html#journals/tnn/ZhangHHS16): 1163-1176 (2016)
- ![](https://dblp.org/img/n.png)

\[c24\]
[Chen Chen](https://dblp.org/pid/65/4423-1.html), [Mengyuan Liu](https://dblp.org/pid/143/0160.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han, [Junjun Jiang](https://dblp.org/pid/119/0230.html), [Hong Liu](https://dblp.org/pid/29/5010-8.html):

3D Action Recognition Using Multi-Temporal Depth Motion Maps and Fisher Vector. [IJCAI2016](https://dblp.org/db/conf/ijcai/ijcai2016.html#conf/ijcai/ChenLZHJL16): 3331-3337
- ![](https://dblp.org/img/n.png)

\[c23\]
[Yuchen Guo](https://dblp.org/pid/132/7979.html), [Guiguang Ding](https://dblp.org/pid/51/740.html), Jungong Han, [Xiaoming Jin](https://dblp.org/pid/26/5593.html):

Robust Iterative Quantization for Efficient ℓp-norm Similarity Search. [IJCAI2016](https://dblp.org/db/conf/ijcai/ijcai2016.html#conf/ijcai/GuoDHJ16): 3382-3388
- ![](https://dblp.org/img/n.png)

\[c22\]
[Linlin Yang](https://dblp.org/pid/84/6484.html), [Chen Chen](https://dblp.org/pid/65/4423-1.html), [Hainan Wang](https://dblp.org/pid/54/10365.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), Jungong Han:

Adaptive Multi-class Correlation Filters. [PCM (2)2016](https://dblp.org/db/conf/pcm/pcm2016-2.html#conf/pcm/Yang0WZH16): 680-688
- 2015
- ![](https://dblp.org/img/n.png)

\[j26\]
[Gong Cheng](https://dblp.org/pid/69/1215-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peicheng Zhou](https://dblp.org/pid/153/9172.html), [Junwei Han](https://dblp.org/pid/00/3003.html), [Lei Guo](https://dblp.org/pid/64/1967-2.html), Jungong Han:

Auto-encoder-based shared mid-level visual dictionary learning for scene classification using very high resolution remote sensing images. [IET Comput. Vis.9(5)](https://dblp.org/db/journals/iet-cvi/iet-cvi9.html#journals/iet-cvi/ChengZH0H15): 639-647 (2015)
- ![](https://dblp.org/img/n.png)

\[j25\]
[Peng Peng](https://dblp.org/pid/49/683.html), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Junwei Han](https://dblp.org/pid/00/3003.html):

Saliency-aware image-to-class distances for image classification. [Neurocomputing166](https://dblp.org/db/journals/ijon/ijon166.html#journals/ijon/PengSHH15): 337-345 (2015)
- ![](https://dblp.org/img/n.png)

\[j24\]
[Xiang Ji](https://dblp.org/pid/46/2563.html), [Junwei Han](https://dblp.org/pid/00/3003.html), [Xi Jiang](https://dblp.org/pid/31/3804-1.html), [Xintao Hu](https://dblp.org/pid/97/8526.html), [Lei Guo](https://dblp.org/pid/64/1967-2.html), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianming Liu](https://dblp.org/pid/96/5013-1.html):

Analysis of music/speech via integration of audio content and functional brain response. [Inf. Sci.297](https://dblp.org/db/journals/isci/isci297.html#journals/isci/JiHJHGHSL15): 271-282 (2015)
- ![](https://dblp.org/img/n.png)

\[j23\]
[Junwei Han](https://dblp.org/pid/00/3003.html), [Changyuan Chen](https://dblp.org/pid/150/3635.html), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xintao Hu](https://dblp.org/pid/97/8526.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Tianming Liu](https://dblp.org/pid/96/5013-1.html):

Learning Computational Models of Video Memorability from fMRI Brain Imaging. [IEEE Trans. Cybern.45(8)](https://dblp.org/db/journals/tcyb/tcyb45.html#journals/tcyb/HanCSHHL15): 1692-1703 (2015)
- 2014
- ![](https://dblp.org/img/n.png)

\[j22\]
[Dabo Guo](https://dblp.org/pid/136/2210.html), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Feature-based motion compensated interpolation for frame rate up-conversion. [Neurocomputing123](https://dblp.org/db/journals/ijon/ijon123.html#journals/ijon/GuoSH14): 390-397 (2014)
- ![](https://dblp.org/img/n.png)

\[j21\]
[Chao Yao](https://dblp.org/pid/99/6747.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhaoyang Lu](https://dblp.org/pid/59/568.html), [Jing Li](https://dblp.org/pid/l/JingLi10.html), [Yamei Xu](https://dblp.org/pid/145/5213.html), Jungong Han:

A subset method for improving Linear Discriminant Analysis. [Neurocomputing138](https://dblp.org/db/journals/ijon/ijon138.html#journals/ijon/YaoLLXH14): 310-315 (2014)
- ![](https://dblp.org/img/n.png)

\[j20\]
[Fei Zuo](https://dblp.org/pid/08/2047.html), Jungong Han, [Pingkun Yan](https://dblp.org/pid/y/PingkunYan.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hans C. van Assen](https://dblp.org/pid/68/947.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kenji Suzuki](https://dblp.org/pid/99/5441-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Guest Editorial: Special issue on advanced computing for image-guided intervention. [Neurocomputing144](https://dblp.org/db/journals/ijon/ijon144.html#journals/ijon/ZuoHYAS14): 1-2 (2014)
- ![](https://dblp.org/img/n.png)

\[j19\]
[Junwei Han](https://dblp.org/pid/00/3003.html), [Xiang Ji](https://dblp.org/pid/46/2563.html), [Xintao Hu](https://dblp.org/pid/97/8526.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Tianming Liu](https://dblp.org/pid/96/5013-1.html):

Clustering and retrieval of video shots based on natural stimulus fMRI. [Neurocomputing144](https://dblp.org/db/journals/ijon/ijon144.html#journals/ijon/HanJHHL14): 128-137 (2014)
- ![](https://dblp.org/img/n.png)

\[j18\]
[Junwei Han](https://dblp.org/pid/00/3003.html), [Liye Sun](https://dblp.org/pid/150/6663.html), [Xintao Hu](https://dblp.org/pid/97/8526.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Spatial and temporal visual attention prediction in videos using eye movement data. [Neurocomputing145](https://dblp.org/db/journals/ijon/ijon145.html#journals/ijon/HanSHHS14): 140-153 (2014)
- ![](https://dblp.org/img/n.png)

\[j17\]
[Junwei Han](https://dblp.org/pid/00/3003.html), [Kaiming Li](https://dblp.org/pid/18/7426.html), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xintao Hu](https://dblp.org/pid/97/8526.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sheng He](https://dblp.org/pid/86/8249.html), [Lei Guo](https://dblp.org/pid/64/1967-2.html), Jungong Han, [Tianming Liu](https://dblp.org/pid/96/5013-1.html):

Video abstraction based on fMRI-driven visual attention model. [Inf. Sci.281](https://dblp.org/db/journals/isci/isci281.html#journals/isci/HanLSHHGHL14): 781-796 (2014)
- ![](https://dblp.org/img/n.png)

\[j16\]
[Junwei Han](https://dblp.org/pid/00/3003.html), [Dongyang Wang](https://dblp.org/pid/137/0229.html), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaoliang Qian](https://dblp.org/pid/31/467.html), [Gong Cheng](https://dblp.org/pid/69/1215-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han:

Image visual attention computation and application via the learning of object attributes. [Mach. Vis. Appl.25(7)](https://dblp.org/db/journals/mva/mva25.html#journals/mva/HanWSQCH14): 1671-1683 (2014)
- ![](https://dblp.org/img/n.png)

\[j15\]
[Dahai Yu](https://dblp.org/pid/31/2647.html), [Junwei Han](https://dblp.org/pid/00/3003.html), [Xing Jin](https://dblp.org/pid/02/2442.html), Jungong Han:

Efficient highlight removal of metal surfaces. [Signal Process.103](https://dblp.org/db/journals/sigpro/sigpro103.html#journals/sigpro/YuHJH14): 367-379 (2014)
- 2013
- ![](https://dblp.org/img/n.png)

\[j14\]
Jungong Han, [Eric J. Pauwels](https://dblp.org/pid/30/3284.html), [Paul M. de Zeeuw](https://dblp.org/pid/84/1406.html):

Fast saliency-aware multi-modality image fusion. [Neurocomputing111](https://dblp.org/db/journals/ijon/ijon111.html#journals/ijon/HanPZ13): 70-80 (2013)
- ![](https://dblp.org/img/n.png)

\[j13\]
Jungong Han, [Eric J. Pauwels](https://dblp.org/pid/30/3284.html), [Feng Wu](https://dblp.org/pid/25/3972-1.html), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Extracting semantics from multi-spectrum video. [Pattern Recognit. Lett.34(1)](https://dblp.org/db/journals/prl/prl34.html#journals/prl/HanPWW13): 1-2 (2013)
- ![](https://dblp.org/img/n.png)

\[j12\]
Jungong Han, [Eric J. Pauwels](https://dblp.org/pid/30/3284.html), [Paul M. de Zeeuw](https://dblp.org/pid/84/1406.html):

Visible and infrared image registration in man-made environments employing hybrid visual features. [Pattern Recognit. Lett.34(1)](https://dblp.org/db/journals/prl/prl34.html#journals/prl/HanPZ13): 42-51 (2013)
- ![](https://dblp.org/img/n.png)

\[j11\]
[Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Dong Xu](https://dblp.org/pid/09/3493-1.html), [Jamie Shotton](https://dblp.org/pid/47/572.html):

Computer vision for RGB-D sensors: Kinect and its applications \[special issue intro.\]. [IEEE Trans. Cybern.43(5)](https://dblp.org/db/journals/tcyb/tcyb43.html#journals/tcyb/ShaoHXS13): 1314-1317 (2013)
- ![](https://dblp.org/img/n.png)

\[j10\]
Jungong Han![](https://dblp.org/img/orcid-mark.12x12.png), [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Xu](https://dblp.org/pid/09/3493-1.html), [Jamie Shotton](https://dblp.org/pid/47/572.html):

Enhanced Computer Vision With Microsoft Kinect Sensor: A Review. [IEEE Trans. Cybern.43(5)](https://dblp.org/db/journals/tcyb/tcyb43.html#journals/tcyb/HanSXS13): 1318-1334 (2013)
- 2012
- ![](https://dblp.org/img/n.png)

\[j9\]
Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html), [Ashley Merien](https://dblp.org/pid/08/10729.html), [Guid Oei](https://dblp.org/pid/90/10732.html):

Intelligent trainee behavior assessment system for medical training employing video analysis. [Pattern Recognit. Lett.33(4)](https://dblp.org/db/journals/prl/prl33.html#journals/prl/HanWMO12): 453-461 (2012)
- ![](https://dblp.org/img/n.png)

\[j8\]
Jungong Han, [Eric J. Pauwels](https://dblp.org/pid/30/3284.html), [Paul M. de Zeeuw](https://dblp.org/pid/84/1406.html), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Employing a RGB-D sensor for real-time tracking of humans across multiple re-entries in a smart environment. [IEEE Trans. Consumer Electron.58(2)](https://dblp.org/db/journals/tce/tce58.html#journals/tce/HanPZW12): 255-263 (2012)
- ![](https://dblp.org/img/n.png)

\[c21\]
[Paul M. de Zeeuw](https://dblp.org/pid/84/1406.html), [Eric J. Pauwels](https://dblp.org/pid/30/3284.html), Jungong Han:

Multimodality and Multiresolution Image Fusion. [VISAPP (1)2012](https://dblp.org/db/conf/visapp/visapp2012-1.html#conf/visapp/ZeeuwPH12): 151-157
- 2011
- ![](https://dblp.org/img/n.png)

\[j7\]
Jungong Han, [Dirk Farin](https://dblp.org/pid/00/2295.html), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

A Mixed-Reality System for Broadcasting Sports Video to Mobile Devices. [IEEE Multim.18(2)](https://dblp.org/db/journals/ieeemm/ieeemm18.html#journals/ieeemm/HanFW11): 72-84 (2011)
- ![](https://dblp.org/img/n.png)

\[j6\]
Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Real-time multiple people tracking for automatic group-behavior evaluation in delivery simulation training. [Multim. Tools Appl.51(3)](https://dblp.org/db/journals/mta/mta51.html#journals/mta/HanW11): 913-933 (2011)
- ![](https://dblp.org/img/n.png)

\[c20\]
[Albert Ali Salah](https://dblp.org/pid/75/4848.html)![](https://dblp.org/img/orcid-mark.12x12.png), Jungong Han, [Eric J. Pauwels](https://dblp.org/pid/30/3284.html), [Paul M. de Zeeuw](https://dblp.org/pid/84/1406.html):

Multimodal monitoring of cultural heritage sites and the FIRESENSE project. [ISABEL2011](https://dblp.org/db/conf/isabel/isabel2011.html#conf/isabel/SalahHPZ11): 152:1-152:5
- ![](https://dblp.org/img/n.png)

\[c19\]
Jungong Han, [Eric J. Pauwels](https://dblp.org/pid/30/3284.html), [Paul M. de Zeeuw](https://dblp.org/pid/84/1406.html):

Visible and Infrared Image Registration Employing Line-Based Geometric Analysis. [MUSCLE2011](https://dblp.org/db/conf/muscle/muscle2011.html#conf/muscle/HanPZ11): 114-125
- ![](https://dblp.org/img/n.png)

\[c18\]
[Stephan Kopf](https://dblp.org/pid/33/724.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Benjamin Guthier](https://dblp.org/pid/51/3413.html), [Dirk Farin](https://dblp.org/pid/00/2295.html), Jungong Han:

Analysis and retargeting of ball sports video. [WACV2011](https://dblp.org/db/conf/wacv/wacv2011.html#conf/wacv/KopfGFH11): 9-14
- 2010
- ![](https://dblp.org/img/n.png)

\[j5\]
Jungong Han, [Ling Shao](https://dblp.org/pid/75/1281.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html), [Ling Guan](https://dblp.org/pid/66/4324.html):

Video Analysis, Abstraction, and Retrieval: Techniques and Applications. [Int. J. Digit. Multim. Broadcast.2010](https://dblp.org/db/journals/ijdmbc/ijdmbc2010.html#journals/ijdmbc/HanSWG10): 348914:1-348914:2 (2010)
- ![](https://dblp.org/img/n.png)

\[j4\]
[Weilun Lao](https://dblp.org/pid/05/843.html), Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Flexible Human Behavior Analysis Framework for Video Surveillance Applications. [Int. J. Digit. Multim. Broadcast.2010](https://dblp.org/db/journals/ijdmbc/ijdmbc2010.html#journals/ijdmbc/LaoHW10): 920121:1-920121:9 (2010)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2009
- ![](https://dblp.org/img/n.png)

\[j3\]
[Weilun Lao](https://dblp.org/pid/05/843.html), Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Automatic video-based human motion analyzer for consumer surveillance system. [IEEE Trans. Consumer Electron.55(2)](https://dblp.org/db/journals/tce/tce55.html#journals/tce/LaoHW09): 591-598 (2009)
- ![](https://dblp.org/img/n.png)

\[c17\]
[Lykele B. Hazelhoff](https://dblp.org/pid/40/649.html), Jungong Han, [Sidarto Bambang-Oetomo](https://dblp.org/pid/76/7414.html), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Behavioral State Detection of Newborns Based on Facial Expression Analysis. [ACIVS2009](https://dblp.org/db/conf/acivs/acivs2009.html#conf/acivs/HazelhoffHBW09): 698-709
- 2008
- ![](https://dblp.org/img/n.png)

\[j2\]
Jungong Han, [Dirk Farin](https://dblp.org/pid/00/2295.html), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Broadcast Court-Net Sports Video Analysis Using Fast 3-D Camera Modeling. [IEEE Trans. Circuits Syst. Video Technol.18(11)](https://dblp.org/db/journals/tcsv/tcsv18.html#journals/tcsv/HanFW08): 1628-1638 (2008)
- ![](https://dblp.org/img/n.png)

\[c16\]
[Lykele B. Hazelhoff](https://dblp.org/pid/40/649.html), Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Video-Based Fall Detection in the Home Using Principal Component Analysis. [ACIVS2008](https://dblp.org/db/conf/acivs/acivs2008.html#conf/acivs/HazelhoffHW08): 298-309
- ![](https://dblp.org/img/n.png)

\[c15\]
[Weilun Lao](https://dblp.org/pid/05/843.html), Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Fast Detection and Modeling of Human-Body Parts from Monocular Video. [AMDO2008](https://dblp.org/db/conf/amdo/amdo2008.html#conf/amdo/LaoHW08): 380-389
- ![](https://dblp.org/img/n.png)

\[c14\]
Jungong Han, [Minwei Feng](https://dblp.org/pid/30/2881.html), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

A real-time video surveillance system with human occlusion handling using nonlinear regression. [ICME2008](https://dblp.org/db/conf/icmcs/icme2008.html#conf/icmcs/HanFW08): 305-308
- 2007
- ![](https://dblp.org/img/n.png)

\[c13\]
[Julien A. Vijverberg](https://dblp.org/pid/52/7249.html), [Nick A. H. M. de Koning](https://dblp.org/pid/144/2054.html), Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html), [Dion Cornelissen](https://dblp.org/pid/144/1751.html):

High-Level Traffic-Violation Detection for Embedded Traffic Analysis. [ICASSP (2)2007](https://dblp.org/db/conf/icassp/icassp2007.html#conf/icassp/VijverbergKHWC07): 793-796
- ![](https://dblp.org/img/n.png)

\[c12\]
Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

3-D Camera Modeling and Its Applications in Sports Broadcast Video Analysis. [MCAM2007](https://dblp.org/db/conf/mcam/mcam2007.html#conf/mcam/HanW07): 434-443
- ![](https://dblp.org/img/n.png)

\[c11\]
Jungong Han, [Dirk Farin](https://dblp.org/pid/00/2295.html), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

A real-time augmented-reality system for sports broadcast video enhancement. [ACM Multimedia2007](https://dblp.org/db/conf/mm/mm2007.html#conf/mm/HanFW07): 337-340
- ![](https://dblp.org/img/n.png)

\[c10\]
Jungong Han, [Dirk Farin](https://dblp.org/pid/00/2295.html), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Generic 3-D Modeling for Content Analysis of Court-Net Sports Sequences. [MMM (2)2007](https://dblp.org/db/conf/mmm/mmm2007-2.html#conf/mmm/HanFW07): 279-288
- ![](https://dblp.org/img/n.png)

\[c9\]
[Weilun Lao](https://dblp.org/pid/05/843.html), Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

A Matching-Based Approach for Human Motion Analysis. [MMM (2)2007](https://dblp.org/db/conf/mmm/mmm2007-2.html#conf/mmm/LaoHW07): 405-414
- 2006
- ![](https://dblp.org/img/n.png)

\[j1\]
Jungong Han, [Dirk Farin](https://dblp.org/pid/00/2295.html), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html), [Weilun Lao](https://dblp.org/pid/05/843.html):

Real-time video content analysis tool for consumer media storage system. [IEEE Trans. Consumer Electron.52(3)](https://dblp.org/db/journals/tce/tce52.html#journals/tce/HanFWL06): 870-878 (2006)
- ![](https://dblp.org/img/n.png)

\[c8\]
Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Content-Based Model Template Adaptation and Real-Time System for Behavior Interpretation in Sports Video. [ACIVS2006](https://dblp.org/db/conf/acivs/acivs2006.html#conf/acivs/HanW06): 474-484
- ![](https://dblp.org/img/n.png)

\[c7\]
Jungong Han, [Weilun Lao](https://dblp.org/pid/05/843.html), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Scene-Level Analysis for Tennis Sports Video using Weighted Linear Combination of Visual Cues. [EuroIMSA2006](https://dblp.org/db/conf/euroimsa/euroimsa2006.html#conf/euroimsa/HanLW06): 193-197
- ![](https://dblp.org/img/n.png)

\[c6\]
[Weilun Lao](https://dblp.org/pid/05/843.html), Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Automatic Sports Video Analysis using Audio Clues and Context Knowledge. [EuroIMSA2006](https://dblp.org/db/conf/euroimsa/euroimsa2006.html#conf/euroimsa/LaoHW06): 198-202
- 2005
- ![](https://dblp.org/img/n.png)

\[c5\]
[Dirk Farin](https://dblp.org/pid/00/2295.html), Jungong Han, [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html):

Fast camera calibration for the analysis of sport sequences. [ICME2005](https://dblp.org/db/conf/icmcs/icme2005.html#conf/icmcs/FarinHW05): 482-485
- ![](https://dblp.org/img/n.png)

\[c4\]
[Jan Nesvadba](https://dblp.org/pid/58/6462.html), [Pedro Fonseca](https://dblp.org/pid/11/3119-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alexander Sinitsyn](https://dblp.org/pid/06/4648.html), [Fons de Lange](https://dblp.org/pid/85/1849.html), [Martijn Thijssen](https://dblp.org/pid/72/5570.html), [Patrick van Kaam](https://dblp.org/pid/49/4925.html), [Hong Liu](https://dblp.org/pid/29/5010-8.html), [Rien van Leeuwen](https://dblp.org/pid/37/4896.html), [Johan J. Lukkien](https://dblp.org/pid/l/JJLukkien.html), [Andrei Korostelev](https://dblp.org/pid/70/3744.html), [Jan Ypma](https://dblp.org/pid/96/2843.html), [Bart Kroon](https://dblp.org/pid/83/537.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hasan Celik](https://dblp.org/pid/68/4570.html), [Alan Hanjalic](https://dblp.org/pid/88/3884.html), [Suphi Umut Naci](https://dblp.org/pid/91/6874.html), [Jenny Benois-Pineau](https://dblp.org/pid/59/4268.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html), Jungong Han:

Real-Time and Distributed AV Content Analysis System for Consumer Electronics Networks. [ICME2005](https://dblp.org/db/conf/icmcs/icme2005.html#conf/icmcs/NesvadbaFSLTKLLLKYKCHNBWH05): 1549-1552
- 2004
- ![](https://dblp.org/img/n.png)

\[c3\]
Jungong Han, [Xiaoyan Sun](https://dblp.org/pid/13/1574-1.html), [Feng Wu](https://dblp.org/pid/25/3972-1.html), [Shipeng Li](https://dblp.org/pid/31/3974-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhaoyang Lu](https://dblp.org/pid/59/568.html):

Variable block-size transform and entropy coding at the enhancement layer of FGS. [ICIP2004](https://dblp.org/db/conf/icip/icip2004-1.html#conf/icip/HanSWLL04): 481-484
- ![](https://dblp.org/img/n.png)

\[c2\]
Jungong Han, [Zhaoyang Lu](https://dblp.org/pid/59/568.html):

A novel stereo image coding algorithm based on delaunay triangulation mesh. [VCIP2004](https://dblp.org/db/conf/vcip/vcip2004.html#conf/vcip/HanL04)
- 2002
- ![](https://dblp.org/img/n.png)

\[c1\]
[Junwei Han](https://dblp.org/pid/00/3003.html), Jungong Han, [Lei Guo](https://dblp.org/pid/64/1967-2.html):

Novel image retrieval technique using salient edges. [Storage and Retrieval for Media Databases2002](https://dblp.org/db/conf/spieSR/spieSR2002.html#conf/spieSR/HanHG02): 69-78
- _no results_

automatic loading of the coauthor graph disabled due to its size.

**click here to**
**load the graph.**

Note that this feature is _work in progress_ and that it is still far from being perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/98/6127.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hadi Amirpour](https://dblp.org/pid/186/1301.html)

[\[c119\]](https://dblp.org/pid/98/6127.html#c119)

[2](https://dblp.org/pid/98/6127.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Plamen Angelov 0001](https://dblp.org/pid/16/6228.html)

aka: Plamen P. Angelov

[\[j182\]](https://dblp.org/pid/98/6127.html#j182) [\[j168\]](https://dblp.org/pid/98/6127.html#j168) [\[j154\]](https://dblp.org/pid/98/6127.html#j154)

[3](https://dblp.org/pid/98/6127.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Gerardo Aragon-Camarasa](https://dblp.org/pid/69/8016.html)

[\[j274\]](https://dblp.org/pid/98/6127.html#j274)

[4](https://dblp.org/pid/98/6127.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hans C. van Assen](https://dblp.org/pid/68/947.html)

[\[j20\]](https://dblp.org/pid/98/6127.html#j20)

[5](https://dblp.org/pid/98/6127.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ali Athar](https://dblp.org/pid/187/5650.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[6](https://dblp.org/pid/98/6127.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Peter M. Atkinson](https://dblp.org/pid/74/41.html)

[\[j277\]](https://dblp.org/pid/98/6127.html#j277) [\[j154\]](https://dblp.org/pid/98/6127.html#j154)

[7](https://dblp.org/pid/98/6127.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Minasadat Attari](https://dblp.org/pid/370/3618.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[8](https://dblp.org/pid/98/6127.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Konstantinos Avgerinakis](https://dblp.org/pid/15/10110.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[9](https://dblp.org/pid/98/6127.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Song Bai 0001](https://dblp.org/pid/151/6422-1.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[10](https://dblp.org/pid/98/6127.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiao Bai 0001](https://dblp.org/pid/99/4833-1.html)

[\[j268\]](https://dblp.org/pid/98/6127.html#j268)

[11](https://dblp.org/pid/98/6127.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Sidarto Bambang-Oetomo](https://dblp.org/pid/76/7414.html)

[\[c17\]](https://dblp.org/pid/98/6127.html#c17)

[12](https://dblp.org/pid/98/6127.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yongjun Bao](https://dblp.org/pid/52/5055.html)

[\[c108\]](https://dblp.org/pid/98/6127.html#c108) [\[c107\]](https://dblp.org/pid/98/6127.html#c107) [\[i84\]](https://dblp.org/pid/98/6127.html#i84) [\[c101\]](https://dblp.org/pid/98/6127.html#c101)

[13](https://dblp.org/pid/98/6127.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Thomas Bashford-Rogers](https://dblp.org/pid/54/1287.html)

[\[j272\]](https://dblp.org/pid/98/6127.html#j272)

[14](https://dblp.org/pid/98/6127.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jenny Benois-Pineau](https://dblp.org/pid/59/4268.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[15](https://dblp.org/pid/98/6127.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Stefano Berretti](https://dblp.org/pid/41/561.html)

[\[j243\]](https://dblp.org/pid/98/6127.html#j243)

[16](https://dblp.org/pid/98/6127.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiao Bian](https://dblp.org/pid/116/5018.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[17](https://dblp.org/pid/98/6127.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Johanna Björklund](https://dblp.org/pid/75/5525.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[18](https://dblp.org/pid/98/6127.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Rick S. Blum](https://dblp.org/pid/11/4798.html)

[\[j63\]](https://dblp.org/pid/98/6127.html#j63) [\[j57\]](https://dblp.org/pid/98/6127.html#j57) [\[i6\]](https://dblp.org/pid/98/6127.html#i6)

[19](https://dblp.org/pid/98/6127.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tahar Brahimi](https://dblp.org/pid/88/8631.html)

[\[j54\]](https://dblp.org/pid/98/6127.html#j54)

[20](https://dblp.org/pid/98/6127.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Taotao Cai](https://dblp.org/pid/168/4683.html)

[\[j244\]](https://dblp.org/pid/98/6127.html#j244) [\[i88\]](https://dblp.org/pid/98/6127.html#i88) [\[j204\]](https://dblp.org/pid/98/6127.html#j204)

[21](https://dblp.org/pid/98/6127.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xunliang Cai](https://dblp.org/pid/294/8410.html)

[\[i64\]](https://dblp.org/pid/98/6127.html#i64)

[22](https://dblp.org/pid/98/6127.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ziyun Cai](https://dblp.org/pid/179/6081.html)

[\[j37\]](https://dblp.org/pid/98/6127.html#j37)

[23](https://dblp.org/pid/98/6127.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bin Cao](https://dblp.org/pid/17/1169.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[24](https://dblp.org/pid/98/6127.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiale Cao](https://dblp.org/pid/167/3851.html)

[\[i74\]](https://dblp.org/pid/98/6127.html#i74) [\[j165\]](https://dblp.org/pid/98/6127.html#j165) [\[j163\]](https://dblp.org/pid/98/6127.html#j163) [\[j161\]](https://dblp.org/pid/98/6127.html#j161) [\[j96\]](https://dblp.org/pid/98/6127.html#j96) [\[j69\]](https://dblp.org/pid/98/6127.html#j69) [\[c64\]](https://dblp.org/pid/98/6127.html#c64)

[25](https://dblp.org/pid/98/6127.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Leilei Cao](https://dblp.org/pid/183/9806.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[26](https://dblp.org/pid/98/6127.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Weilong Cao](https://dblp.org/pid/401/7489.html)

[\[i112\]](https://dblp.org/pid/98/6127.html#i112)

[27](https://dblp.org/pid/98/6127.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xianbin Cao 0001](https://dblp.org/pid/22/3485.html)

[\[j208\]](https://dblp.org/pid/98/6127.html#j208) [\[j172\]](https://dblp.org/pid/98/6127.html#j172) [\[j136\]](https://dblp.org/pid/98/6127.html#j136) [\[j109\]](https://dblp.org/pid/98/6127.html#j109) [\[c76\]](https://dblp.org/pid/98/6127.html#c76) [\[i26\]](https://dblp.org/pid/98/6127.html#i26) [\[c73\]](https://dblp.org/pid/98/6127.html#c73) [\[c71\]](https://dblp.org/pid/98/6127.html#c71) [\[c45\]](https://dblp.org/pid/98/6127.html#c45) [\[i10\]](https://dblp.org/pid/98/6127.html#i10) [\[i7\]](https://dblp.org/pid/98/6127.html#i7) [\[j40\]](https://dblp.org/pid/98/6127.html#j40) [\[i5\]](https://dblp.org/pid/98/6127.html#i5)

[28](https://dblp.org/pid/98/6127.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xianghai Cao](https://dblp.org/pid/177/0184.html)

[\[j86\]](https://dblp.org/pid/98/6127.html#j86) [\[j61\]](https://dblp.org/pid/98/6127.html#j61) [\[j39\]](https://dblp.org/pid/98/6127.html#j39)

[29](https://dblp.org/pid/98/6127.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuhang Cao](https://dblp.org/pid/212/6480.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[30](https://dblp.org/pid/98/6127.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yunfeng Cao](https://dblp.org/pid/177/0271.html)

[\[j102\]](https://dblp.org/pid/98/6127.html#j102)

[31](https://dblp.org/pid/98/6127.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[32](https://dblp.org/pid/98/6127.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hasan Celik](https://dblp.org/pid/68/4570.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[33](https://dblp.org/pid/98/6127.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Antoni B. Chan](https://dblp.org/pid/55/5814.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[34](https://dblp.org/pid/98/6127.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[35](https://dblp.org/pid/98/6127.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiang Chang](https://dblp.org/pid/232/5246.html)

[\[j255\]](https://dblp.org/pid/98/6127.html#j255)

[36](https://dblp.org/pid/98/6127.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Changrui Chen](https://dblp.org/pid/232/4719.html)

[\[j255\]](https://dblp.org/pid/98/6127.html#j255) [\[j238\]](https://dblp.org/pid/98/6127.html#j238) [\[i118\]](https://dblp.org/pid/98/6127.html#i118) [\[i93\]](https://dblp.org/pid/98/6127.html#i93) [\[j210\]](https://dblp.org/pid/98/6127.html#j210) [\[j209\]](https://dblp.org/pid/98/6127.html#j209) [\[c111\]](https://dblp.org/pid/98/6127.html#c111) [\[i55\]](https://dblp.org/pid/98/6127.html#i55) [\[c93\]](https://dblp.org/pid/98/6127.html#c93) [\[i46\]](https://dblp.org/pid/98/6127.html#i46)

[37](https://dblp.org/pid/98/6127.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Changyuan Chen](https://dblp.org/pid/150/3635.html)

[\[j23\]](https://dblp.org/pid/98/6127.html#j23)

[38](https://dblp.org/pid/98/6127.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chen Chen 0001](https://dblp.org/pid/65/4423-1.html)

[\[i96\]](https://dblp.org/pid/98/6127.html#i96) [\[j66\]](https://dblp.org/pid/98/6127.html#j66) [\[j58\]](https://dblp.org/pid/98/6127.html#j58) [\[j50\]](https://dblp.org/pid/98/6127.html#j50) [\[j49\]](https://dblp.org/pid/98/6127.html#j49) [\[c42\]](https://dblp.org/pid/98/6127.html#c42) [\[c36\]](https://dblp.org/pid/98/6127.html#c36) [\[i10\]](https://dblp.org/pid/98/6127.html#i10) [\[i9\]](https://dblp.org/pid/98/6127.html#i9) [\[j44\]](https://dblp.org/pid/98/6127.html#j44) [\[j40\]](https://dblp.org/pid/98/6127.html#j40) [\[j32\]](https://dblp.org/pid/98/6127.html#j32) [\[i5\]](https://dblp.org/pid/98/6127.html#i5) [\[i3\]](https://dblp.org/pid/98/6127.html#i3) [\[i2\]](https://dblp.org/pid/98/6127.html#i2) [\[i1\]](https://dblp.org/pid/98/6127.html#i1) [\[c24\]](https://dblp.org/pid/98/6127.html#c24) [\[c22\]](https://dblp.org/pid/98/6127.html#c22)

[39](https://dblp.org/pid/98/6127.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Danlu Chen](https://dblp.org/pid/188/6023.html)

[\[i85\]](https://dblp.org/pid/98/6127.html#i85)

[40](https://dblp.org/pid/98/6127.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fang Chen](https://dblp.org/pid/52/488.html)

[\[j47\]](https://dblp.org/pid/98/6127.html#j47)

[41](https://dblp.org/pid/98/6127.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fanglin Chen 0001](https://dblp.org/pid/85/7057-1.html)

[\[j248\]](https://dblp.org/pid/98/6127.html#j248)

[42](https://dblp.org/pid/98/6127.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hanlin Chen](https://dblp.org/pid/97/1735.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[43](https://dblp.org/pid/98/6127.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hanting Chen](https://dblp.org/pid/232/2060.html)

[\[j233\]](https://dblp.org/pid/98/6127.html#j233)

[44](https://dblp.org/pid/98/6127.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hao Chen 0107](https://dblp.org/pid/175/3324-107.html)

[\[j215\]](https://dblp.org/pid/98/6127.html#j215) [\[j201\]](https://dblp.org/pid/98/6127.html#j201) [\[c102\]](https://dblp.org/pid/98/6127.html#c102) [\[i58\]](https://dblp.org/pid/98/6127.html#i58)

[45](https://dblp.org/pid/98/6127.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haoxiang Chen 0007](https://dblp.org/pid/385/7338.html)

[\[i72\]](https://dblp.org/pid/98/6127.html#i72)

[46](https://dblp.org/pid/98/6127.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Honghao Chen](https://dblp.org/pid/279/9807.html)

[\[c98\]](https://dblp.org/pid/98/6127.html#c98) [\[c96\]](https://dblp.org/pid/98/6127.html#c96) [\[i47\]](https://dblp.org/pid/98/6127.html#i47) [\[i27\]](https://dblp.org/pid/98/6127.html#i27)

[47](https://dblp.org/pid/98/6127.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hui Chen 0013](https://dblp.org/pid/12/417-13.html)

[\[j271\]](https://dblp.org/pid/98/6127.html#j271) [\[j230\]](https://dblp.org/pid/98/6127.html#j230) [\[j226\]](https://dblp.org/pid/98/6127.html#j226) [\[c129\]](https://dblp.org/pid/98/6127.html#c129) [\[c128\]](https://dblp.org/pid/98/6127.html#c128) [\[c127\]](https://dblp.org/pid/98/6127.html#c127) [\[c126\]](https://dblp.org/pid/98/6127.html#c126) [\[c124\]](https://dblp.org/pid/98/6127.html#c124) [\[c123\]](https://dblp.org/pid/98/6127.html#c123) [\[c122\]](https://dblp.org/pid/98/6127.html#c122) [\[c120\]](https://dblp.org/pid/98/6127.html#c120) [\[c118\]](https://dblp.org/pid/98/6127.html#c118) [\[i115\]](https://dblp.org/pid/98/6127.html#i115) [\[i114\]](https://dblp.org/pid/98/6127.html#i114) [\[i113\]](https://dblp.org/pid/98/6127.html#i113) [\[i111\]](https://dblp.org/pid/98/6127.html#i111) [\[i110\]](https://dblp.org/pid/98/6127.html#i110) [\[i107\]](https://dblp.org/pid/98/6127.html#i107) [\[i102\]](https://dblp.org/pid/98/6127.html#i102) [\[i98\]](https://dblp.org/pid/98/6127.html#i98) [\[i94\]](https://dblp.org/pid/98/6127.html#i94) [\[i89\]](https://dblp.org/pid/98/6127.html#i89) [\[c116\]](https://dblp.org/pid/98/6127.html#c116) [\[c115\]](https://dblp.org/pid/98/6127.html#c115) [\[c114\]](https://dblp.org/pid/98/6127.html#c114) [\[c112\]](https://dblp.org/pid/98/6127.html#c112) [\[c108\]](https://dblp.org/pid/98/6127.html#c108) [\[c107\]](https://dblp.org/pid/98/6127.html#c107) [\[c105\]](https://dblp.org/pid/98/6127.html#c105) [\[i84\]](https://dblp.org/pid/98/6127.html#i84) [\[i78\]](https://dblp.org/pid/98/6127.html#i78) [\[i73\]](https://dblp.org/pid/98/6127.html#i73) [\[i72\]](https://dblp.org/pid/98/6127.html#i72) [\[i71\]](https://dblp.org/pid/98/6127.html#i71) [\[i67\]](https://dblp.org/pid/98/6127.html#i67) [\[i64\]](https://dblp.org/pid/98/6127.html#i64) [\[i63\]](https://dblp.org/pid/98/6127.html#i63) [\[i61\]](https://dblp.org/pid/98/6127.html#i61) [\[c101\]](https://dblp.org/pid/98/6127.html#c101) [\[i56\]](https://dblp.org/pid/98/6127.html#i56) [\[i54\]](https://dblp.org/pid/98/6127.html#i54) [\[i53\]](https://dblp.org/pid/98/6127.html#i53) [\[i52\]](https://dblp.org/pid/98/6127.html#i52) [\[i41\]](https://dblp.org/pid/98/6127.html#i41) [\[j126\]](https://dblp.org/pid/98/6127.html#j126) [\[j90\]](https://dblp.org/pid/98/6127.html#j90) [\[c79\]](https://dblp.org/pid/98/6127.html#c79) [\[i25\]](https://dblp.org/pid/98/6127.html#i25) [\[j89\]](https://dblp.org/pid/98/6127.html#j89) [\[c56\]](https://dblp.org/pid/98/6127.html#c56) [\[c50\]](https://dblp.org/pid/98/6127.html#c50) [\[c47\]](https://dblp.org/pid/98/6127.html#c47) [\[c43\]](https://dblp.org/pid/98/6127.html#c43) [\[c34\]](https://dblp.org/pid/98/6127.html#c34)

[48](https://dblp.org/pid/98/6127.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jie Chen 0001](https://dblp.org/pid/92/6289-1.html)

[\[j129\]](https://dblp.org/pid/98/6127.html#j129)

[49](https://dblp.org/pid/98/6127.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jingdong Chen](https://dblp.org/pid/33/5656.html)

[\[i89\]](https://dblp.org/pid/98/6127.html#i89)

[50](https://dblp.org/pid/98/6127.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jingkun Chen](https://dblp.org/pid/212/6645.html)

[\[j272\]](https://dblp.org/pid/98/6127.html#j272) [\[j236\]](https://dblp.org/pid/98/6127.html#j236) [\[i117\]](https://dblp.org/pid/98/6127.html#i117) [\[i104\]](https://dblp.org/pid/98/6127.html#i104) [\[i91\]](https://dblp.org/pid/98/6127.html#i91) [\[i90\]](https://dblp.org/pid/98/6127.html#i90) [\[j209\]](https://dblp.org/pid/98/6127.html#j209) [\[j166\]](https://dblp.org/pid/98/6127.html#j166)

[51](https://dblp.org/pid/98/6127.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kai Chen](https://dblp.org/pid/181/2839.html)

[\[c129\]](https://dblp.org/pid/98/6127.html#c129) [\[c114\]](https://dblp.org/pid/98/6127.html#c114) [\[c105\]](https://dblp.org/pid/98/6127.html#c105) [\[i78\]](https://dblp.org/pid/98/6127.html#i78) [\[i71\]](https://dblp.org/pid/98/6127.html#i71) [\[i67\]](https://dblp.org/pid/98/6127.html#i67) [\[j75\]](https://dblp.org/pid/98/6127.html#j75) [\[j67\]](https://dblp.org/pid/98/6127.html#j67) [\[j42\]](https://dblp.org/pid/98/6127.html#j42)

[52](https://dblp.org/pid/98/6127.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liang Chen](https://dblp.org/pid/01/5394.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[53](https://dblp.org/pid/98/6127.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Minghai Chen](https://dblp.org/pid/195/8186.html)

[\[j89\]](https://dblp.org/pid/98/6127.html#j89) [\[c34\]](https://dblp.org/pid/98/6127.html#c34)

[54](https://dblp.org/pid/98/6127.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shanjuan Chen](https://dblp.org/pid/387/5848.html)

[\[j245\]](https://dblp.org/pid/98/6127.html#j245)

[55](https://dblp.org/pid/98/6127.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shihao Chen](https://dblp.org/pid/61/7845.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[56](https://dblp.org/pid/98/6127.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Weidong Chen 0013](https://dblp.org/pid/196/5142-13.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[57](https://dblp.org/pid/98/6127.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenshuo Chen](https://dblp.org/pid/193/3404.html)

[\[j46\]](https://dblp.org/pid/98/6127.html#j46)

[58](https://dblp.org/pid/98/6127.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiansheng Chen](https://dblp.org/pid/245/4652.html)

[\[c122\]](https://dblp.org/pid/98/6127.html#c122)

[59](https://dblp.org/pid/98/6127.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaodong Chen 0011](https://dblp.org/pid/70/4319-11.html)

[\[c91\]](https://dblp.org/pid/98/6127.html#c91) [\[i43\]](https://dblp.org/pid/98/6127.html#i43)

[60](https://dblp.org/pid/98/6127.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaojiang Chen](https://dblp.org/pid/95/10521.html)

[\[j92\]](https://dblp.org/pid/98/6127.html#j92)

[61](https://dblp.org/pid/98/6127.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[62](https://dblp.org/pid/98/6127.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhixiang Chen 0003](https://dblp.org/pid/70/3894-3.html)

[\[c130\]](https://dblp.org/pid/98/6127.html#c130) [\[j188\]](https://dblp.org/pid/98/6127.html#j188)

[63](https://dblp.org/pid/98/6127.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[De Cheng](https://dblp.org/pid/154/1991.html)

[\[j225\]](https://dblp.org/pid/98/6127.html#j225) [\[j174\]](https://dblp.org/pid/98/6127.html#j174) [\[i48\]](https://dblp.org/pid/98/6127.html#i48)

[64](https://dblp.org/pid/98/6127.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Gong Cheng 0003](https://dblp.org/pid/69/1215-3.html)

[\[j137\]](https://dblp.org/pid/98/6127.html#j137) [\[j135\]](https://dblp.org/pid/98/6127.html#j135) [\[j26\]](https://dblp.org/pid/98/6127.html#j26) [\[j16\]](https://dblp.org/pid/98/6127.html#j16)

[65](https://dblp.org/pid/98/6127.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hao Cheng 0010](https://dblp.org/pid/09/5158-10.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[66](https://dblp.org/pid/98/6127.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jian Cheng 0001](https://dblp.org/pid/14/6145-1.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[67](https://dblp.org/pid/98/6127.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jun Cheng 0003](https://dblp.org/pid/78/5816-3.html)

[\[i95\]](https://dblp.org/pid/98/6127.html#i95)

[68](https://dblp.org/pid/98/6127.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Long Cheng 0003](https://dblp.org/pid/49/225-3.html)

[\[j268\]](https://dblp.org/pid/98/6127.html#j268)

[69](https://dblp.org/pid/98/6127.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Donghyeon Cho](https://dblp.org/pid/142/2590.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[70](https://dblp.org/pid/98/6127.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jin Young Choi 0002](https://dblp.org/pid/30/1428-2.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[71](https://dblp.org/pid/98/6127.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jongwon Choi 0002](https://dblp.org/pid/126/0675-2.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[72](https://dblp.org/pid/98/6127.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chaoqun Chu](https://dblp.org/pid/233/6032.html)

[\[j75\]](https://dblp.org/pid/98/6127.html#j75) [\[j67\]](https://dblp.org/pid/98/6127.html#j67)

[73](https://dblp.org/pid/98/6127.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuezhong Chu](https://dblp.org/pid/228/7471.html)

[\[j158\]](https://dblp.org/pid/98/6127.html#j158) [\[j85\]](https://dblp.org/pid/98/6127.html#j85) [\[j82\]](https://dblp.org/pid/98/6127.html#j82)

[74](https://dblp.org/pid/98/6127.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jaired Collins](https://dblp.org/pid/211/4242.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[75](https://dblp.org/pid/98/6127.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Nicola Conci](https://dblp.org/pid/32/3652.html)

[\[j148\]](https://dblp.org/pid/98/6127.html#j148) [\[e1\]](https://dblp.org/pid/98/6127.html#e1)

[76](https://dblp.org/pid/98/6127.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dion Cornelissen](https://dblp.org/pid/144/1751.html)

[\[c13\]](https://dblp.org/pid/98/6127.html#c13)

[77](https://dblp.org/pid/98/6127.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Rongmei Cui](https://dblp.org/pid/222/2238.html)

[\[j83\]](https://dblp.org/pid/98/6127.html#j83)

[78](https://dblp.org/pid/98/6127.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[79](https://dblp.org/pid/98/6127.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liangliang Dai](https://dblp.org/pid/184/8786.html)

[\[j74\]](https://dblp.org/pid/98/6127.html#j74)

[80](https://dblp.org/pid/98/6127.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qionghai Dai](https://dblp.org/pid/39/4543.html)

[\[j67\]](https://dblp.org/pid/98/6127.html#j67) [\[c72\]](https://dblp.org/pid/98/6127.html#c72) [\[c60\]](https://dblp.org/pid/98/6127.html#c60) [\[c59\]](https://dblp.org/pid/98/6127.html#c59)

[81](https://dblp.org/pid/98/6127.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jun Dan](https://dblp.org/pid/156/9683.html)

[\[j251\]](https://dblp.org/pid/98/6127.html#j251)

[82](https://dblp.org/pid/98/6127.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuhao Dang](https://dblp.org/pid/370/3843.html)

[\[j250\]](https://dblp.org/pid/98/6127.html#j250) [\[j211\]](https://dblp.org/pid/98/6127.html#j211) [\[j207\]](https://dblp.org/pid/98/6127.html#j207) [\[j187\]](https://dblp.org/pid/98/6127.html#j187)

[83](https://dblp.org/pid/98/6127.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kurt Debattista](https://dblp.org/pid/29/5944.html)

[\[j272\]](https://dblp.org/pid/98/6127.html#j272) [\[j249\]](https://dblp.org/pid/98/6127.html#j249) [\[j236\]](https://dblp.org/pid/98/6127.html#j236) [\[j222\]](https://dblp.org/pid/98/6127.html#j222) [\[j210\]](https://dblp.org/pid/98/6127.html#j210) [\[j209\]](https://dblp.org/pid/98/6127.html#j209) [\[j190\]](https://dblp.org/pid/98/6127.html#j190) [\[c111\]](https://dblp.org/pid/98/6127.html#c111) [\[c104\]](https://dblp.org/pid/98/6127.html#c104) [\[j166\]](https://dblp.org/pid/98/6127.html#j166) [\[j164\]](https://dblp.org/pid/98/6127.html#j164) [\[i55\]](https://dblp.org/pid/98/6127.html#i55) [\[c93\]](https://dblp.org/pid/98/6127.html#c93) [\[i46\]](https://dblp.org/pid/98/6127.html#i46)

[84](https://dblp.org/pid/98/6127.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiankang Deng](https://dblp.org/pid/156/7808.html)

[\[i93\]](https://dblp.org/pid/98/6127.html#i93) [\[j196\]](https://dblp.org/pid/98/6127.html#j196) [\[c117\]](https://dblp.org/pid/98/6127.html#c117) [\[i83\]](https://dblp.org/pid/98/6127.html#i83) [\[c89\]](https://dblp.org/pid/98/6127.html#c89) [\[i40\]](https://dblp.org/pid/98/6127.html#i40) [\[i39\]](https://dblp.org/pid/98/6127.html#i39)

[85](https://dblp.org/pid/98/6127.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhipeng Deng](https://dblp.org/pid/30/10701.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[86](https://dblp.org/pid/98/6127.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ganesh Sai Manas Devarapu](https://dblp.org/pid/406/4906.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[87](https://dblp.org/pid/98/6127.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Na Di](https://dblp.org/pid/38/10015.html)

[\[c69\]](https://dblp.org/pid/98/6127.html#c69)

[88](https://dblp.org/pid/98/6127.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Errui Ding](https://dblp.org/pid/180/5531.html)

[\[c90\]](https://dblp.org/pid/98/6127.html#c90) [\[i44\]](https://dblp.org/pid/98/6127.html#i44)

[89](https://dblp.org/pid/98/6127.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Guiguang Ding](https://dblp.org/pid/51/740.html)

[\[j271\]](https://dblp.org/pid/98/6127.html#j271) [\[j270\]](https://dblp.org/pid/98/6127.html#j270) [\[j241\]](https://dblp.org/pid/98/6127.html#j241) [\[j230\]](https://dblp.org/pid/98/6127.html#j230) [\[j219\]](https://dblp.org/pid/98/6127.html#j219) [\[c129\]](https://dblp.org/pid/98/6127.html#c129) [\[c128\]](https://dblp.org/pid/98/6127.html#c128) [\[c127\]](https://dblp.org/pid/98/6127.html#c127) [\[c126\]](https://dblp.org/pid/98/6127.html#c126) [\[c125\]](https://dblp.org/pid/98/6127.html#c125) [\[c124\]](https://dblp.org/pid/98/6127.html#c124) [\[c123\]](https://dblp.org/pid/98/6127.html#c123) [\[c122\]](https://dblp.org/pid/98/6127.html#c122) [\[c120\]](https://dblp.org/pid/98/6127.html#c120) [\[c118\]](https://dblp.org/pid/98/6127.html#c118) [\[i115\]](https://dblp.org/pid/98/6127.html#i115) [\[i114\]](https://dblp.org/pid/98/6127.html#i114) [\[i113\]](https://dblp.org/pid/98/6127.html#i113) [\[i111\]](https://dblp.org/pid/98/6127.html#i111) [\[i110\]](https://dblp.org/pid/98/6127.html#i110) [\[i107\]](https://dblp.org/pid/98/6127.html#i107) [\[i102\]](https://dblp.org/pid/98/6127.html#i102) [\[i99\]](https://dblp.org/pid/98/6127.html#i99) [\[i98\]](https://dblp.org/pid/98/6127.html#i98) [\[i94\]](https://dblp.org/pid/98/6127.html#i94) [\[i89\]](https://dblp.org/pid/98/6127.html#i89) [\[i87\]](https://dblp.org/pid/98/6127.html#i87) [\[j196\]](https://dblp.org/pid/98/6127.html#j196) [\[j185\]](https://dblp.org/pid/98/6127.html#j185) [\[c116\]](https://dblp.org/pid/98/6127.html#c116) [\[c115\]](https://dblp.org/pid/98/6127.html#c115) [\[c114\]](https://dblp.org/pid/98/6127.html#c114) [\[c112\]](https://dblp.org/pid/98/6127.html#c112) [\[c108\]](https://dblp.org/pid/98/6127.html#c108) [\[c107\]](https://dblp.org/pid/98/6127.html#c107) [\[c105\]](https://dblp.org/pid/98/6127.html#c105) [\[c104\]](https://dblp.org/pid/98/6127.html#c104) [\[i84\]](https://dblp.org/pid/98/6127.html#i84) [\[i78\]](https://dblp.org/pid/98/6127.html#i78) [\[i73\]](https://dblp.org/pid/98/6127.html#i73) [\[i72\]](https://dblp.org/pid/98/6127.html#i72) [\[i71\]](https://dblp.org/pid/98/6127.html#i71) [\[i67\]](https://dblp.org/pid/98/6127.html#i67) [\[i64\]](https://dblp.org/pid/98/6127.html#i64) [\[i63\]](https://dblp.org/pid/98/6127.html#i63) [\[i61\]](https://dblp.org/pid/98/6127.html#i61) [\[j183\]](https://dblp.org/pid/98/6127.html#j183) [\[j173\]](https://dblp.org/pid/98/6127.html#j173) [\[c98\]](https://dblp.org/pid/98/6127.html#c98) [\[i56\]](https://dblp.org/pid/98/6127.html#i56) [\[i54\]](https://dblp.org/pid/98/6127.html#i54) [\[i53\]](https://dblp.org/pid/98/6127.html#i53) [\[i52\]](https://dblp.org/pid/98/6127.html#i52) [\[j155\]](https://dblp.org/pid/98/6127.html#j155) [\[c97\]](https://dblp.org/pid/98/6127.html#c97) [\[c96\]](https://dblp.org/pid/98/6127.html#c96) [\[c94\]](https://dblp.org/pid/98/6127.html#c94) [\[i49\]](https://dblp.org/pid/98/6127.html#i49) [\[i47\]](https://dblp.org/pid/98/6127.html#i47) [\[i41\]](https://dblp.org/pid/98/6127.html#i41) [\[i39\]](https://dblp.org/pid/98/6127.html#i39) [\[j126\]](https://dblp.org/pid/98/6127.html#j126) [\[j124\]](https://dblp.org/pid/98/6127.html#j124) [\[j113\]](https://dblp.org/pid/98/6127.html#j113) [\[j112\]](https://dblp.org/pid/98/6127.html#j112) [\[c87\]](https://dblp.org/pid/98/6127.html#c87) [\[c85\]](https://dblp.org/pid/98/6127.html#c85) [\[c84\]](https://dblp.org/pid/98/6127.html#c84) [\[c83\]](https://dblp.org/pid/98/6127.html#c83) [\[i38\]](https://dblp.org/pid/98/6127.html#i38) [\[i36\]](https://dblp.org/pid/98/6127.html#i36) [\[i31\]](https://dblp.org/pid/98/6127.html#i31) [\[i30\]](https://dblp.org/pid/98/6127.html#i30) [\[i28\]](https://dblp.org/pid/98/6127.html#i28) [\[i27\]](https://dblp.org/pid/98/6127.html#i27) [\[j100\]](https://dblp.org/pid/98/6127.html#j100) [\[j93\]](https://dblp.org/pid/98/6127.html#j93) [\[j90\]](https://dblp.org/pid/98/6127.html#j90) [\[c82\]](https://dblp.org/pid/98/6127.html#c82) [\[c81\]](https://dblp.org/pid/98/6127.html#c81) [\[c79\]](https://dblp.org/pid/98/6127.html#c79) [\[c77\]](https://dblp.org/pid/98/6127.html#c77) [\[i25\]](https://dblp.org/pid/98/6127.html#i25) [\[i24\]](https://dblp.org/pid/98/6127.html#i24) [\[i23\]](https://dblp.org/pid/98/6127.html#i23) [\[j89\]](https://dblp.org/pid/98/6127.html#j89) [\[j87\]](https://dblp.org/pid/98/6127.html#j87) [\[j75\]](https://dblp.org/pid/98/6127.html#j75) [\[j70\]](https://dblp.org/pid/98/6127.html#j70) [\[j68\]](https://dblp.org/pid/98/6127.html#j68) [\[j67\]](https://dblp.org/pid/98/6127.html#j67) [\[j65\]](https://dblp.org/pid/98/6127.html#j65) [\[c72\]](https://dblp.org/pid/98/6127.html#c72) [\[c69\]](https://dblp.org/pid/98/6127.html#c69) [\[c68\]](https://dblp.org/pid/98/6127.html#c68) [\[c66\]](https://dblp.org/pid/98/6127.html#c66) [\[c62\]](https://dblp.org/pid/98/6127.html#c62) [\[c61\]](https://dblp.org/pid/98/6127.html#c61) [\[c60\]](https://dblp.org/pid/98/6127.html#c60) [\[c59\]](https://dblp.org/pid/98/6127.html#c59) [\[c57\]](https://dblp.org/pid/98/6127.html#c57) [\[c56\]](https://dblp.org/pid/98/6127.html#c56) [\[c55\]](https://dblp.org/pid/98/6127.html#c55) [\[i20\]](https://dblp.org/pid/98/6127.html#i20) [\[i18\]](https://dblp.org/pid/98/6127.html#i18) [\[i17\]](https://dblp.org/pid/98/6127.html#i17) [\[i16\]](https://dblp.org/pid/98/6127.html#i16) [\[i14\]](https://dblp.org/pid/98/6127.html#i14) [\[j51\]](https://dblp.org/pid/98/6127.html#j51) [\[j46\]](https://dblp.org/pid/98/6127.html#j46) [\[j45\]](https://dblp.org/pid/98/6127.html#j45) [\[c52\]](https://dblp.org/pid/98/6127.html#c52) [\[c50\]](https://dblp.org/pid/98/6127.html#c50) [\[c49\]](https://dblp.org/pid/98/6127.html#c49) [\[c48\]](https://dblp.org/pid/98/6127.html#c48) [\[c47\]](https://dblp.org/pid/98/6127.html#c47) [\[c43\]](https://dblp.org/pid/98/6127.html#c43) [\[c41\]](https://dblp.org/pid/98/6127.html#c41) [\[c39\]](https://dblp.org/pid/98/6127.html#c39) [\[c38\]](https://dblp.org/pid/98/6127.html#c38) [\[c37\]](https://dblp.org/pid/98/6127.html#c37) [\[j42\]](https://dblp.org/pid/98/6127.html#j42) [\[j41\]](https://dblp.org/pid/98/6127.html#j41) [\[j36\]](https://dblp.org/pid/98/6127.html#j36) [\[j35\]](https://dblp.org/pid/98/6127.html#j35) [\[j34\]](https://dblp.org/pid/98/6127.html#j34) [\[j33\]](https://dblp.org/pid/98/6127.html#j33) [\[c35\]](https://dblp.org/pid/98/6127.html#c35) [\[c34\]](https://dblp.org/pid/98/6127.html#c34) [\[c33\]](https://dblp.org/pid/98/6127.html#c33) [\[c32\]](https://dblp.org/pid/98/6127.html#c32) [\[c31\]](https://dblp.org/pid/98/6127.html#c31) [\[c30\]](https://dblp.org/pid/98/6127.html#c30) [\[c29\]](https://dblp.org/pid/98/6127.html#c29) [\[c27\]](https://dblp.org/pid/98/6127.html#c27) [\[c26\]](https://dblp.org/pid/98/6127.html#c26) [\[c25\]](https://dblp.org/pid/98/6127.html#c25) [\[i4\]](https://dblp.org/pid/98/6127.html#i4) [\[c23\]](https://dblp.org/pid/98/6127.html#c23)

[90](https://dblp.org/pid/98/6127.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Henghui Ding](https://dblp.org/pid/230/1216.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90) [\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[91](https://dblp.org/pid/98/6127.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lu Ding](https://dblp.org/pid/135/0285.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[92](https://dblp.org/pid/98/6127.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shuangrui Ding](https://dblp.org/pid/267/1780.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[93](https://dblp.org/pid/98/6127.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenrui Ding](https://dblp.org/pid/08/10143.html)

[\[j122\]](https://dblp.org/pid/98/6127.html#j122) [\[j98\]](https://dblp.org/pid/98/6127.html#j98) [\[i13\]](https://dblp.org/pid/98/6127.html#i13) [\[j56\]](https://dblp.org/pid/98/6127.html#j56) [\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[94](https://dblp.org/pid/98/6127.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaohan Ding](https://dblp.org/pid/218/7379.html)

[\[j185\]](https://dblp.org/pid/98/6127.html#j185) [\[c98\]](https://dblp.org/pid/98/6127.html#c98) [\[c96\]](https://dblp.org/pid/98/6127.html#c96) [\[c94\]](https://dblp.org/pid/98/6127.html#c94) [\[i49\]](https://dblp.org/pid/98/6127.html#i49) [\[i47\]](https://dblp.org/pid/98/6127.html#i47) [\[c85\]](https://dblp.org/pid/98/6127.html#c85) [\[c84\]](https://dblp.org/pid/98/6127.html#c84) [\[c83\]](https://dblp.org/pid/98/6127.html#c83) [\[i38\]](https://dblp.org/pid/98/6127.html#i38) [\[i36\]](https://dblp.org/pid/98/6127.html#i36) [\[i31\]](https://dblp.org/pid/98/6127.html#i31) [\[i30\]](https://dblp.org/pid/98/6127.html#i30) [\[i27\]](https://dblp.org/pid/98/6127.html#i27) [\[i23\]](https://dblp.org/pid/98/6127.html#i23) [\[c72\]](https://dblp.org/pid/98/6127.html#c72) [\[c68\]](https://dblp.org/pid/98/6127.html#c68) [\[c66\]](https://dblp.org/pid/98/6127.html#c66) [\[c62\]](https://dblp.org/pid/98/6127.html#c62) [\[c55\]](https://dblp.org/pid/98/6127.html#c55) [\[i20\]](https://dblp.org/pid/98/6127.html#i20) [\[i18\]](https://dblp.org/pid/98/6127.html#i18) [\[i16\]](https://dblp.org/pid/98/6127.html#i16) [\[i14\]](https://dblp.org/pid/98/6127.html#i14) [\[c49\]](https://dblp.org/pid/98/6127.html#c49)

[95](https://dblp.org/pid/98/6127.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zixuan Ding](https://dblp.org/pid/230/1821.html)

[\[j226\]](https://dblp.org/pid/98/6127.html#j226) [\[c101\]](https://dblp.org/pid/98/6127.html#c101)

[96](https://dblp.org/pid/98/6127.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[David S. Doermann](https://dblp.org/pid/88/6921.html)

[\[i59\]](https://dblp.org/pid/98/6127.html#i59) [\[j122\]](https://dblp.org/pid/98/6127.html#j122) [\[c76\]](https://dblp.org/pid/98/6127.html#c76) [\[i26\]](https://dblp.org/pid/98/6127.html#i26) [\[c73\]](https://dblp.org/pid/98/6127.html#c73) [\[i7\]](https://dblp.org/pid/98/6127.html#i7)

[97](https://dblp.org/pid/98/6127.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bingchen Dong](https://dblp.org/pid/325/6093.html)

[\[j276\]](https://dblp.org/pid/98/6127.html#j276)

[98](https://dblp.org/pid/98/6127.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaohui Dong](https://dblp.org/pid/152/7855.html)

[\[j260\]](https://dblp.org/pid/98/6127.html#j260) [\[i62\]](https://dblp.org/pid/98/6127.html#i62)

[99](https://dblp.org/pid/98/6127.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaoyi Dong](https://dblp.org/pid/230/3711.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[100](https://dblp.org/pid/98/6127.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yao Dong 0005](https://dblp.org/pid/80/8588-5.html)

[\[j105\]](https://dblp.org/pid/98/6127.html#j105)

[101](https://dblp.org/pid/98/6127.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yongfeng Dong](https://dblp.org/pid/12/1159.html)

[\[j105\]](https://dblp.org/pid/98/6127.html#j105)

[102](https://dblp.org/pid/98/6127.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yonghan Dong](https://dblp.org/pid/342/4266.html)

[\[j215\]](https://dblp.org/pid/98/6127.html#j215) [\[j201\]](https://dblp.org/pid/98/6127.html#j201) [\[c102\]](https://dblp.org/pid/98/6127.html#c102) [\[i58\]](https://dblp.org/pid/98/6127.html#i58)

[103](https://dblp.org/pid/98/6127.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dawei Du](https://dblp.org/pid/51/6958.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[104](https://dblp.org/pid/98/6127.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiale Du](https://dblp.org/pid/241/3709.html)

[\[j246\]](https://dblp.org/pid/98/6127.html#j246) [\[j240\]](https://dblp.org/pid/98/6127.html#j240) [\[i109\]](https://dblp.org/pid/98/6127.html#i109) [\[i108\]](https://dblp.org/pid/98/6127.html#i108) [\[i66\]](https://dblp.org/pid/98/6127.html#i66) [\[i65\]](https://dblp.org/pid/98/6127.html#i65)

[105](https://dblp.org/pid/98/6127.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yinglong Du](https://dblp.org/pid/199/1274.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[106](https://dblp.org/pid/98/6127.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haoran Duan 0001](https://dblp.org/pid/82/4334-1.html)

[\[j258\]](https://dblp.org/pid/98/6127.html#j258) [\[j257\]](https://dblp.org/pid/98/6127.html#j257) [\[c121\]](https://dblp.org/pid/98/6127.html#c121) [\[i106\]](https://dblp.org/pid/98/6127.html#i106) [\[i104\]](https://dblp.org/pid/98/6127.html#i104) [\[i103\]](https://dblp.org/pid/98/6127.html#i103) [\[i100\]](https://dblp.org/pid/98/6127.html#i100) [\[i85\]](https://dblp.org/pid/98/6127.html#i85)

[107](https://dblp.org/pid/98/6127.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kaiwen Duan](https://dblp.org/pid/190/4878.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[108](https://dblp.org/pid/98/6127.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Mingxing Duanmu](https://dblp.org/pid/285/6888.html)

[\[j143\]](https://dblp.org/pid/98/6127.html#j143)

[109](https://dblp.org/pid/98/6127.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Sergio Escalera](https://dblp.org/pid/77/5527.html)

[\[j274\]](https://dblp.org/pid/98/6127.html#j274)

[110](https://dblp.org/pid/98/6127.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Heng Fan 0001](https://dblp.org/pid/20/10120-1.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[111](https://dblp.org/pid/98/6127.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiaqing Fan](https://dblp.org/pid/227/6586.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[112](https://dblp.org/pid/98/6127.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Rui Fan 0001](https://dblp.org/pid/03/1805-1.html)

[\[j264\]](https://dblp.org/pid/98/6127.html#j264)

[113](https://dblp.org/pid/98/6127.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wan-Cyuan Fan](https://dblp.org/pid/300/5836.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[114](https://dblp.org/pid/98/6127.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yi Fan](https://dblp.org/pid/10/2921.html)

[\[j55\]](https://dblp.org/pid/98/6127.html#j55)

[115](https://dblp.org/pid/98/6127.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuchen Fan](https://dblp.org/pid/120/4095.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[116](https://dblp.org/pid/98/6127.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhenkun Fan](https://dblp.org/pid/315/3130.html)

[\[j188\]](https://dblp.org/pid/98/6127.html#j188) [\[i82\]](https://dblp.org/pid/98/6127.html#i82)

[117](https://dblp.org/pid/98/6127.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chaowei Fang](https://dblp.org/pid/159/1655.html)

[\[j159\]](https://dblp.org/pid/98/6127.html#j159) [\[i37\]](https://dblp.org/pid/98/6127.html#i37)

[118](https://dblp.org/pid/98/6127.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dingyi Fang](https://dblp.org/pid/80/3909.html)

[\[j92\]](https://dblp.org/pid/98/6127.html#j92)

[119](https://dblp.org/pid/98/6127.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hao Fang 0010](https://dblp.org/pid/06/2484-10.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[120](https://dblp.org/pid/98/6127.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hui Fang 0003](https://dblp.org/pid/03/2511-3.html)

[\[j146\]](https://dblp.org/pid/98/6127.html#j146)

[121](https://dblp.org/pid/98/6127.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dirk Farin](https://dblp.org/pid/00/2295.html)

[\[j7\]](https://dblp.org/pid/98/6127.html#j7) [\[c18\]](https://dblp.org/pid/98/6127.html#c18) [\[j2\]](https://dblp.org/pid/98/6127.html#j2) [\[c11\]](https://dblp.org/pid/98/6127.html#c11) [\[c10\]](https://dblp.org/pid/98/6127.html#c10) [\[j1\]](https://dblp.org/pid/98/6127.html#j1) [\[c5\]](https://dblp.org/pid/98/6127.html#c5)

[122](https://dblp.org/pid/98/6127.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[123](https://dblp.org/pid/98/6127.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Juexiao Feng](https://dblp.org/pid/371/4491.html)

[\[j241\]](https://dblp.org/pid/98/6127.html#j241) [\[i61\]](https://dblp.org/pid/98/6127.html#i61)

[124](https://dblp.org/pid/98/6127.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Minwei Feng](https://dblp.org/pid/30/2881.html)

[\[c14\]](https://dblp.org/pid/98/6127.html#c14)

[125](https://dblp.org/pid/98/6127.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xia Feng](https://dblp.org/pid/67/5915.html)

[\[j276\]](https://dblp.org/pid/98/6127.html#j276)

[126](https://dblp.org/pid/98/6127.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaoxu Feng](https://dblp.org/pid/253/1916.html)

[\[j137\]](https://dblp.org/pid/98/6127.html#j137)

[127](https://dblp.org/pid/98/6127.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yansong Feng 0002](https://dblp.org/pid/25/2643-2.html)

[\[j92\]](https://dblp.org/pid/98/6127.html#j92)

[128](https://dblp.org/pid/98/6127.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[129](https://dblp.org/pid/98/6127.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[130](https://dblp.org/pid/98/6127.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Pedro Fonseca 0002](https://dblp.org/pid/11/3119-2.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[131](https://dblp.org/pid/98/6127.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jie Fu](https://dblp.org/pid/16/7565.html)

[\[i85\]](https://dblp.org/pid/98/6127.html#i85)

[132](https://dblp.org/pid/98/6127.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xuemei Fu](https://dblp.org/pid/204/0988.html)

[\[j268\]](https://dblp.org/pid/98/6127.html#j268)

[133](https://dblp.org/pid/98/6127.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yu Fu 0006](https://dblp.org/pid/09/3263-6.html)

[\[j255\]](https://dblp.org/pid/98/6127.html#j255) [\[j216\]](https://dblp.org/pid/98/6127.html#j216) [\[j155\]](https://dblp.org/pid/98/6127.html#j155)

[134](https://dblp.org/pid/98/6127.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhenyang Fu](https://dblp.org/pid/356/6667.html)

[\[j237\]](https://dblp.org/pid/98/6127.html#j237)

[135](https://dblp.org/pid/98/6127.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zilin Fu](https://dblp.org/pid/218/9871.html)

[\[j106\]](https://dblp.org/pid/98/6127.html#j106) [\[j82\]](https://dblp.org/pid/98/6127.html#j82) [\[j60\]](https://dblp.org/pid/98/6127.html#j60)

[136](https://dblp.org/pid/98/6127.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kun Gai](https://dblp.org/pid/59/2902.html)

[\[c123\]](https://dblp.org/pid/98/6127.html#c123) [\[i114\]](https://dblp.org/pid/98/6127.html#i114) [\[i113\]](https://dblp.org/pid/98/6127.html#i113)

[137](https://dblp.org/pid/98/6127.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bolin Gao](https://dblp.org/pid/120/1968.html)

[\[j96\]](https://dblp.org/pid/98/6127.html#j96) [\[c63\]](https://dblp.org/pid/98/6127.html#c63)

[138](https://dblp.org/pid/98/6127.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Boyan Gao](https://dblp.org/pid/251/3330.html)

[\[i104\]](https://dblp.org/pid/98/6127.html#i104)

[139](https://dblp.org/pid/98/6127.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Mingqi Gao 0003](https://dblp.org/pid/191/2698-3.html)

[\[i100\]](https://dblp.org/pid/98/6127.html#i100) [\[i93\]](https://dblp.org/pid/98/6127.html#i93) [\[i92\]](https://dblp.org/pid/98/6127.html#i92) [\[i91\]](https://dblp.org/pid/98/6127.html#i91) [\[i90\]](https://dblp.org/pid/98/6127.html#i90) [\[i86\]](https://dblp.org/pid/98/6127.html#i86) [\[c110\]](https://dblp.org/pid/98/6127.html#c110) [\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i76\]](https://dblp.org/pid/98/6127.html#i76) [\[i75\]](https://dblp.org/pid/98/6127.html#i75) [\[j183\]](https://dblp.org/pid/98/6127.html#j183) [\[j180\]](https://dblp.org/pid/98/6127.html#j180) [\[j176\]](https://dblp.org/pid/98/6127.html#j176) [\[j171\]](https://dblp.org/pid/98/6127.html#j171)

[140](https://dblp.org/pid/98/6127.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Pengcheng Gao](https://dblp.org/pid/41/11514.html)

[\[c129\]](https://dblp.org/pid/98/6127.html#c129) [\[i67\]](https://dblp.org/pid/98/6127.html#i67)

[141](https://dblp.org/pid/98/6127.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Quanxue Gao](https://dblp.org/pid/63/804.html)

[\[j200\]](https://dblp.org/pid/98/6127.html#j200) [\[j199\]](https://dblp.org/pid/98/6127.html#j199) [\[j153\]](https://dblp.org/pid/98/6127.html#j153) [\[j138\]](https://dblp.org/pid/98/6127.html#j138) [\[j123\]](https://dblp.org/pid/98/6127.html#j123) [\[j117\]](https://dblp.org/pid/98/6127.html#j117) [\[j104\]](https://dblp.org/pid/98/6127.html#j104) [\[j83\]](https://dblp.org/pid/98/6127.html#j83) [\[j79\]](https://dblp.org/pid/98/6127.html#j79) [\[j78\]](https://dblp.org/pid/98/6127.html#j78) [\[c58\]](https://dblp.org/pid/98/6127.html#c58) [\[j47\]](https://dblp.org/pid/98/6127.html#j47) [\[c51\]](https://dblp.org/pid/98/6127.html#c51) [\[c40\]](https://dblp.org/pid/98/6127.html#c40)

[142](https://dblp.org/pid/98/6127.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xinbo Gao 0001](https://dblp.org/pid/99/4522.html)

[\[j248\]](https://dblp.org/pid/98/6127.html#j248) [\[j246\]](https://dblp.org/pid/98/6127.html#j246) [\[j240\]](https://dblp.org/pid/98/6127.html#j240) [\[j239\]](https://dblp.org/pid/98/6127.html#j239) [\[j231\]](https://dblp.org/pid/98/6127.html#j231) [\[j221\]](https://dblp.org/pid/98/6127.html#j221) [\[i109\]](https://dblp.org/pid/98/6127.html#i109) [\[i108\]](https://dblp.org/pid/98/6127.html#i108) [\[j211\]](https://dblp.org/pid/98/6127.html#j211) [\[j207\]](https://dblp.org/pid/98/6127.html#j207) [\[j206\]](https://dblp.org/pid/98/6127.html#j206) [\[j200\]](https://dblp.org/pid/98/6127.html#j200) [\[j199\]](https://dblp.org/pid/98/6127.html#j199) [\[j187\]](https://dblp.org/pid/98/6127.html#j187) [\[i66\]](https://dblp.org/pid/98/6127.html#i66) [\[i65\]](https://dblp.org/pid/98/6127.html#i65) [\[j169\]](https://dblp.org/pid/98/6127.html#j169) [\[j153\]](https://dblp.org/pid/98/6127.html#j153) [\[j151\]](https://dblp.org/pid/98/6127.html#j151) [\[j138\]](https://dblp.org/pid/98/6127.html#j138) [\[j123\]](https://dblp.org/pid/98/6127.html#j123) [\[j117\]](https://dblp.org/pid/98/6127.html#j117) [\[j104\]](https://dblp.org/pid/98/6127.html#j104) [\[j83\]](https://dblp.org/pid/98/6127.html#j83) [\[j79\]](https://dblp.org/pid/98/6127.html#j79) [\[j78\]](https://dblp.org/pid/98/6127.html#j78) [\[c58\]](https://dblp.org/pid/98/6127.html#c58)

[143](https://dblp.org/pid/98/6127.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yongsheng Gao 0001](https://dblp.org/pid/22/6786-1.html)

[\[j73\]](https://dblp.org/pid/98/6127.html#j73)

[144](https://dblp.org/pid/98/6127.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yue Gao 0002](https://dblp.org/pid/33/3099-2.html)

[\[j100\]](https://dblp.org/pid/98/6127.html#j100) [\[j65\]](https://dblp.org/pid/98/6127.html#j65) [\[c41\]](https://dblp.org/pid/98/6127.html#c41) [\[j33\]](https://dblp.org/pid/98/6127.html#j33) [\[c35\]](https://dblp.org/pid/98/6127.html#c35) [\[c33\]](https://dblp.org/pid/98/6127.html#c33) [\[c31\]](https://dblp.org/pid/98/6127.html#c31) [\[c30\]](https://dblp.org/pid/98/6127.html#c30) [\[c27\]](https://dblp.org/pid/98/6127.html#c27) [\[c26\]](https://dblp.org/pid/98/6127.html#c26) [\[c25\]](https://dblp.org/pid/98/6127.html#c25)

[145](https://dblp.org/pid/98/6127.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Daan de Geus](https://dblp.org/pid/227/2962.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[146](https://dblp.org/pid/98/6127.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Amir Gholami](https://dblp.org/pid/150/6303.html)

aka: Amir Gholaminejad

[\[j65\]](https://dblp.org/pid/98/6127.html#j65)

[147](https://dblp.org/pid/98/6127.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Panagiotis Giannakeris](https://dblp.org/pid/213/4135.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[148](https://dblp.org/pid/98/6127.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dahan Gong](https://dblp.org/pid/187/2613.html)

[\[j75\]](https://dblp.org/pid/98/6127.html#j75)

[149](https://dblp.org/pid/98/6127.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dengxian Gong](https://dblp.org/pid/415/2440.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[150](https://dblp.org/pid/98/6127.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Guoqiang Gong](https://dblp.org/pid/168/4603.html)

[\[c125\]](https://dblp.org/pid/98/6127.html#c125) [\[i99\]](https://dblp.org/pid/98/6127.html#i99)

[151](https://dblp.org/pid/98/6127.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lixing Gong](https://dblp.org/pid/331/1426.html)

[\[c107\]](https://dblp.org/pid/98/6127.html#c107)

[152](https://dblp.org/pid/98/6127.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[153](https://dblp.org/pid/98/6127.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Raghav Goyal](https://dblp.org/pid/191/6034.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[154](https://dblp.org/pid/98/6127.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Vicente Grau](https://dblp.org/pid/g/VicenteGrau.html)

[\[j272\]](https://dblp.org/pid/98/6127.html#j272) [\[i117\]](https://dblp.org/pid/98/6127.html#i117) [\[i104\]](https://dblp.org/pid/98/6127.html#i104)

[155](https://dblp.org/pid/98/6127.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiaxin Gu](https://dblp.org/pid/218/5361.html)

[\[c73\]](https://dblp.org/pid/98/6127.html#c73) [\[i10\]](https://dblp.org/pid/98/6127.html#i10) [\[i7\]](https://dblp.org/pid/98/6127.html#i7)

[156](https://dblp.org/pid/98/6127.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Junhua Gu](https://dblp.org/pid/26/6721.html)

[\[j244\]](https://dblp.org/pid/98/6127.html#j244) [\[i88\]](https://dblp.org/pid/98/6127.html#i88) [\[j204\]](https://dblp.org/pid/98/6127.html#j204) [\[j105\]](https://dblp.org/pid/98/6127.html#j105)

[157](https://dblp.org/pid/98/6127.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaopeng Gu](https://dblp.org/pid/313/6436.html)

[\[j90\]](https://dblp.org/pid/98/6127.html#j90)

[158](https://dblp.org/pid/98/6127.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaowei Gu 0001](https://dblp.org/pid/128/5017-1.html)

[\[j277\]](https://dblp.org/pid/98/6127.html#j277) [\[j182\]](https://dblp.org/pid/98/6127.html#j182) [\[j168\]](https://dblp.org/pid/98/6127.html#j168) [\[j154\]](https://dblp.org/pid/98/6127.html#j154)

[159](https://dblp.org/pid/98/6127.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ling Guan](https://dblp.org/pid/66/4324.html)

[\[j5\]](https://dblp.org/pid/98/6127.html#j5)

[160](https://dblp.org/pid/98/6127.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Renchu Guan](https://dblp.org/pid/84/8179.html)

[\[j261\]](https://dblp.org/pid/98/6127.html#j261)

[161](https://dblp.org/pid/98/6127.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dabo Guo](https://dblp.org/pid/136/2210.html)

[\[j22\]](https://dblp.org/pid/98/6127.html#j22)

[162](https://dblp.org/pid/98/6127.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Guodong Guo](https://dblp.org/pid/92/4520.html)

[\[j98\]](https://dblp.org/pid/98/6127.html#j98) [\[j66\]](https://dblp.org/pid/98/6127.html#j66) [\[i13\]](https://dblp.org/pid/98/6127.html#i13)

[163](https://dblp.org/pid/98/6127.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hongyuan Guo](https://dblp.org/pid/336/9827.html)

[\[c100\]](https://dblp.org/pid/98/6127.html#c100)

[164](https://dblp.org/pid/98/6127.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lei Guo 0002](https://dblp.org/pid/64/1967-2.html)

[\[j26\]](https://dblp.org/pid/98/6127.html#j26) [\[j24\]](https://dblp.org/pid/98/6127.html#j24) [\[j17\]](https://dblp.org/pid/98/6127.html#j17) [\[c1\]](https://dblp.org/pid/98/6127.html#c1)

[165](https://dblp.org/pid/98/6127.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuchen Guo](https://dblp.org/pid/132/7979.html)

[\[j185\]](https://dblp.org/pid/98/6127.html#j185) [\[c97\]](https://dblp.org/pid/98/6127.html#c97) [\[i41\]](https://dblp.org/pid/98/6127.html#i41) [\[j126\]](https://dblp.org/pid/98/6127.html#j126) [\[c83\]](https://dblp.org/pid/98/6127.html#c83) [\[i30\]](https://dblp.org/pid/98/6127.html#i30) [\[i28\]](https://dblp.org/pid/98/6127.html#i28) [\[c82\]](https://dblp.org/pid/98/6127.html#c82) [\[i23\]](https://dblp.org/pid/98/6127.html#i23) [\[j87\]](https://dblp.org/pid/98/6127.html#j87) [\[j75\]](https://dblp.org/pid/98/6127.html#j75) [\[j68\]](https://dblp.org/pid/98/6127.html#j68) [\[j67\]](https://dblp.org/pid/98/6127.html#j67) [\[c72\]](https://dblp.org/pid/98/6127.html#c72) [\[c68\]](https://dblp.org/pid/98/6127.html#c68) [\[c66\]](https://dblp.org/pid/98/6127.html#c66) [\[c62\]](https://dblp.org/pid/98/6127.html#c62) [\[c60\]](https://dblp.org/pid/98/6127.html#c60) [\[c59\]](https://dblp.org/pid/98/6127.html#c59) [\[c55\]](https://dblp.org/pid/98/6127.html#c55) [\[i20\]](https://dblp.org/pid/98/6127.html#i20) [\[i18\]](https://dblp.org/pid/98/6127.html#i18) [\[i16\]](https://dblp.org/pid/98/6127.html#i16) [\[i14\]](https://dblp.org/pid/98/6127.html#i14) [\[j51\]](https://dblp.org/pid/98/6127.html#j51) [\[c52\]](https://dblp.org/pid/98/6127.html#c52) [\[c48\]](https://dblp.org/pid/98/6127.html#c48) [\[c47\]](https://dblp.org/pid/98/6127.html#c47) [\[c38\]](https://dblp.org/pid/98/6127.html#c38) [\[c37\]](https://dblp.org/pid/98/6127.html#c37) [\[j41\]](https://dblp.org/pid/98/6127.html#j41) [\[j34\]](https://dblp.org/pid/98/6127.html#j34) [\[j33\]](https://dblp.org/pid/98/6127.html#j33) [\[c35\]](https://dblp.org/pid/98/6127.html#c35) [\[c33\]](https://dblp.org/pid/98/6127.html#c33) [\[c31\]](https://dblp.org/pid/98/6127.html#c31) [\[c30\]](https://dblp.org/pid/98/6127.html#c30) [\[c29\]](https://dblp.org/pid/98/6127.html#c29) [\[c27\]](https://dblp.org/pid/98/6127.html#c27) [\[c23\]](https://dblp.org/pid/98/6127.html#c23)

[166](https://dblp.org/pid/98/6127.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Benjamin Guthier](https://dblp.org/pid/51/3413.html)

[\[c18\]](https://dblp.org/pid/98/6127.html#c18)

[167](https://dblp.org/pid/98/6127.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Junwei Han 0001](https://dblp.org/pid/00/3003.html)

[\[j159\]](https://dblp.org/pid/98/6127.html#j159) [\[j137\]](https://dblp.org/pid/98/6127.html#j137) [\[j135\]](https://dblp.org/pid/98/6127.html#j135) [\[i51\]](https://dblp.org/pid/98/6127.html#i51) [\[j121\]](https://dblp.org/pid/98/6127.html#j121) [\[j118\]](https://dblp.org/pid/98/6127.html#j118) [\[i37\]](https://dblp.org/pid/98/6127.html#i37) [\[j94\]](https://dblp.org/pid/98/6127.html#j94) [\[j31\]](https://dblp.org/pid/98/6127.html#j31) [\[j28\]](https://dblp.org/pid/98/6127.html#j28) [\[j27\]](https://dblp.org/pid/98/6127.html#j27) [\[j26\]](https://dblp.org/pid/98/6127.html#j26) [\[j25\]](https://dblp.org/pid/98/6127.html#j25) [\[j24\]](https://dblp.org/pid/98/6127.html#j24) [\[j23\]](https://dblp.org/pid/98/6127.html#j23) [\[j19\]](https://dblp.org/pid/98/6127.html#j19) [\[j18\]](https://dblp.org/pid/98/6127.html#j18) [\[j17\]](https://dblp.org/pid/98/6127.html#j17) [\[j16\]](https://dblp.org/pid/98/6127.html#j16) [\[j15\]](https://dblp.org/pid/98/6127.html#j15) [\[c1\]](https://dblp.org/pid/98/6127.html#c1)

[168](https://dblp.org/pid/98/6127.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Alan Hanjalic](https://dblp.org/pid/88/3884.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[169](https://dblp.org/pid/98/6127.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tianxiang Hao 0001](https://dblp.org/pid/270/0611-1.html)

[\[j241\]](https://dblp.org/pid/98/6127.html#j241) [\[j226\]](https://dblp.org/pid/98/6127.html#j226) [\[j219\]](https://dblp.org/pid/98/6127.html#j219) [\[c125\]](https://dblp.org/pid/98/6127.html#c125) [\[i99\]](https://dblp.org/pid/98/6127.html#i99) [\[i94\]](https://dblp.org/pid/98/6127.html#i94) [\[j185\]](https://dblp.org/pid/98/6127.html#j185) [\[c112\]](https://dblp.org/pid/98/6127.html#c112) [\[c108\]](https://dblp.org/pid/98/6127.html#c108) [\[i84\]](https://dblp.org/pid/98/6127.html#i84) [\[i73\]](https://dblp.org/pid/98/6127.html#i73) [\[i53\]](https://dblp.org/pid/98/6127.html#i53) [\[c83\]](https://dblp.org/pid/98/6127.html#c83) [\[i30\]](https://dblp.org/pid/98/6127.html#i30) [\[i23\]](https://dblp.org/pid/98/6127.html#i23)

[170](https://dblp.org/pid/98/6127.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bijaya Kumar Hatuwal](https://dblp.org/pid/318/9407.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[171](https://dblp.org/pid/98/6127.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lykele B. Hazelhoff](https://dblp.org/pid/40/649.html)

[\[c17\]](https://dblp.org/pid/98/6127.html#c17) [\[c16\]](https://dblp.org/pid/98/6127.html#c16)

[172](https://dblp.org/pid/98/6127.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dongliang He](https://dblp.org/pid/167/0539.html)

[\[c90\]](https://dblp.org/pid/98/6127.html#c90) [\[i44\]](https://dblp.org/pid/98/6127.html#i44)

[173](https://dblp.org/pid/98/6127.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Erlu He](https://dblp.org/pid/240/1897.html)

[\[j101\]](https://dblp.org/pid/98/6127.html#j101)

[174](https://dblp.org/pid/98/6127.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Sheng He](https://dblp.org/pid/86/8249.html)

[\[j17\]](https://dblp.org/pid/98/6127.html#j17)

[175](https://dblp.org/pid/98/6127.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shuting He](https://dblp.org/pid/255/9456.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[176](https://dblp.org/pid/98/6127.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tao He](https://dblp.org/pid/94/5035.html)

[\[j219\]](https://dblp.org/pid/98/6127.html#j219) [\[c125\]](https://dblp.org/pid/98/6127.html#c125) [\[i99\]](https://dblp.org/pid/98/6127.html#i99)

[177](https://dblp.org/pid/98/6127.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Weijie He](https://dblp.org/pid/94/8876.html)

[\[j251\]](https://dblp.org/pid/98/6127.html#j251)

[178](https://dblp.org/pid/98/6127.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaohao He](https://dblp.org/pid/219/4446.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[179](https://dblp.org/pid/98/6127.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaoyi He](https://dblp.org/pid/220/3273.html)

[\[j205\]](https://dblp.org/pid/98/6127.html#j205) [\[j198\]](https://dblp.org/pid/98/6127.html#j198)

[180](https://dblp.org/pid/98/6127.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xingjian He](https://dblp.org/pid/204/0216.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[181](https://dblp.org/pid/98/6127.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuan He 0011](https://dblp.org/pid/11/1735-11.html)

[\[c116\]](https://dblp.org/pid/98/6127.html#c116) [\[i52\]](https://dblp.org/pid/98/6127.html#i52)

[182](https://dblp.org/pid/98/6127.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuwei He](https://dblp.org/pid/222/8475.html)

[\[c82\]](https://dblp.org/pid/98/6127.html#c82)

[183](https://dblp.org/pid/98/6127.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhenyu He 0001](https://dblp.org/pid/57/6240-1.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110) [\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[184](https://dblp.org/pid/98/6127.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhiqun He](https://dblp.org/pid/213/4141.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[185](https://dblp.org/pid/98/6127.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Paul Henderson](https://dblp.org/pid/172/1394.html)

[\[j274\]](https://dblp.org/pid/98/6127.html#j274)

[186](https://dblp.org/pid/98/6127.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Byeongho Heo](https://dblp.org/pid/142/2705.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[187](https://dblp.org/pid/98/6127.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Alexander Hermans](https://dblp.org/pid/151/9332.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[188](https://dblp.org/pid/98/6127.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Edmond S. L. Ho](https://dblp.org/pid/19/4864.html)

[\[j274\]](https://dblp.org/pid/98/6127.html#j274)

[189](https://dblp.org/pid/98/6127.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Danfeng Hong](https://dblp.org/pid/153/2550.html)

[\[j238\]](https://dblp.org/pid/98/6127.html#j238) [\[i118\]](https://dblp.org/pid/98/6127.html#i118)

[190](https://dblp.org/pid/98/6127.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haiwen Hong](https://dblp.org/pid/297/4419.html)

[\[c116\]](https://dblp.org/pid/98/6127.html#c116) [\[i52\]](https://dblp.org/pid/98/6127.html#i52)

[191](https://dblp.org/pid/98/6127.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lingyi Hong](https://dblp.org/pid/311/7466.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[192](https://dblp.org/pid/98/6127.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ran Hong](https://dblp.org/pid/278/0621.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[193](https://dblp.org/pid/98/6127.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Richang Hong](https://dblp.org/pid/59/1501.html)

[\[c119\]](https://dblp.org/pid/98/6127.html#c119)

[194](https://dblp.org/pid/98/6127.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiacheng Hou](https://dblp.org/pid/226/4634.html)

[\[j235\]](https://dblp.org/pid/98/6127.html#j235) [\[i81\]](https://dblp.org/pid/98/6127.html#i81)

[195](https://dblp.org/pid/98/6127.html?view=joint&param=195 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shudong Hou](https://dblp.org/pid/28/8546.html)

[\[j177\]](https://dblp.org/pid/98/6127.html#j177) [\[i22\]](https://dblp.org/pid/98/6127.html#i22) [\[j82\]](https://dblp.org/pid/98/6127.html#j82) [\[j74\]](https://dblp.org/pid/98/6127.html#j74) [\[c54\]](https://dblp.org/pid/98/6127.html#c54) [\[j64\]](https://dblp.org/pid/98/6127.html#j64)

[196](https://dblp.org/pid/98/6127.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhishen Hou](https://dblp.org/pid/301/8258.html)

[\[j134\]](https://dblp.org/pid/98/6127.html#j134) [\[i29\]](https://dblp.org/pid/98/6127.html#i29)

[197](https://dblp.org/pid/98/6127.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Borui Hu](https://dblp.org/pid/393/7322.html)

[\[j248\]](https://dblp.org/pid/98/6127.html#j248)

[198](https://dblp.org/pid/98/6127.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jie Hu 0021](https://dblp.org/pid/90/5064-21.html)

[\[j233\]](https://dblp.org/pid/98/6127.html#j233) [\[c97\]](https://dblp.org/pid/98/6127.html#c97) [\[i28\]](https://dblp.org/pid/98/6127.html#i28)

[199](https://dblp.org/pid/98/6127.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ping Hu](https://dblp.org/pid/53/5490.html)

[\[i95\]](https://dblp.org/pid/98/6127.html#i95)

[200](https://dblp.org/pid/98/6127.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qinghua Hu](https://dblp.org/pid/30/2395.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[201](https://dblp.org/pid/98/6127.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Songlin Hu 0001](https://dblp.org/pid/67/4108-1.html)

[\[c123\]](https://dblp.org/pid/98/6127.html#c123) [\[i114\]](https://dblp.org/pid/98/6127.html#i114)

[202](https://dblp.org/pid/98/6127.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Weiming Hu 0004](https://dblp.org/pid/41/6824-4.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[203](https://dblp.org/pid/98/6127.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiantao Hu](https://dblp.org/pid/160/8016.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[204](https://dblp.org/pid/98/6127.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xintao Hu](https://dblp.org/pid/97/8526.html)

[\[j24\]](https://dblp.org/pid/98/6127.html#j24) [\[j23\]](https://dblp.org/pid/98/6127.html#j23) [\[j19\]](https://dblp.org/pid/98/6127.html#j19) [\[j18\]](https://dblp.org/pid/98/6127.html#j18) [\[j17\]](https://dblp.org/pid/98/6127.html#j17)

[205](https://dblp.org/pid/98/6127.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xixi Hu 0003](https://dblp.org/pid/234/1710-3.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[206](https://dblp.org/pid/98/6127.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yutao Hu 0002](https://dblp.org/pid/37/5215-2.html)

[\[j208\]](https://dblp.org/pid/98/6127.html#j208) [\[j172\]](https://dblp.org/pid/98/6127.html#j172) [\[c99\]](https://dblp.org/pid/98/6127.html#c99) [\[i57\]](https://dblp.org/pid/98/6127.html#i57) [\[j136\]](https://dblp.org/pid/98/6127.html#j136) [\[j109\]](https://dblp.org/pid/98/6127.html#j109) [\[c76\]](https://dblp.org/pid/98/6127.html#c76) [\[i26\]](https://dblp.org/pid/98/6127.html#i26)

[207](https://dblp.org/pid/98/6127.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhenfei Hu](https://dblp.org/pid/278/7777.html)

[\[j101\]](https://dblp.org/pid/98/6127.html#j101)

[208](https://dblp.org/pid/98/6127.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Litao Hua](https://dblp.org/pid/405/1724.html)

[\[i106\]](https://dblp.org/pid/98/6127.html#i106)

[209](https://dblp.org/pid/98/6127.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yang Hua](https://dblp.org/pid/396/8608.html)

[\[i97\]](https://dblp.org/pid/98/6127.html#i97)

[210](https://dblp.org/pid/98/6127.html?view=joint&param=210 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yining Hua](https://dblp.org/pid/220/1318.html)

[\[j146\]](https://dblp.org/pid/98/6127.html#j146)

[211](https://dblp.org/pid/98/6127.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Di Huang 0001](https://dblp.org/pid/45/780-1.html)

[\[j127\]](https://dblp.org/pid/98/6127.html#j127)

[212](https://dblp.org/pid/98/6127.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Guohai Huang](https://dblp.org/pid/275/3809.html)

[\[i51\]](https://dblp.org/pid/98/6127.html#i51) [\[j121\]](https://dblp.org/pid/98/6127.html#j121) [\[j94\]](https://dblp.org/pid/98/6127.html#j94)

[213](https://dblp.org/pid/98/6127.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haidong Huang](https://dblp.org/pid/245/4034.html)

[\[c97\]](https://dblp.org/pid/98/6127.html#c97) [\[i28\]](https://dblp.org/pid/98/6127.html#i28)

[214](https://dblp.org/pid/98/6127.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jin Huang](https://dblp.org/pid/49/2488.html)

[\[j267\]](https://dblp.org/pid/98/6127.html#j267) [\[j217\]](https://dblp.org/pid/98/6127.html#j217) [\[j214\]](https://dblp.org/pid/98/6127.html#j214) [\[j193\]](https://dblp.org/pid/98/6127.html#j193) [\[i80\]](https://dblp.org/pid/98/6127.html#i80) [\[i79\]](https://dblp.org/pid/98/6127.html#i79)

[215](https://dblp.org/pid/98/6127.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kaiqi Huang](https://dblp.org/pid/89/7026.html)

[\[c98\]](https://dblp.org/pid/98/6127.html#c98) [\[i47\]](https://dblp.org/pid/98/6127.html#i47)

[216](https://dblp.org/pid/98/6127.html?view=joint&param=216 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Nianchang Huang](https://dblp.org/pid/258/2761.html)

[\[j269\]](https://dblp.org/pid/98/6127.html#j269) [\[j267\]](https://dblp.org/pid/98/6127.html#j267) [\[j237\]](https://dblp.org/pid/98/6127.html#j237) [\[j220\]](https://dblp.org/pid/98/6127.html#j220) [\[j217\]](https://dblp.org/pid/98/6127.html#j217) [\[j214\]](https://dblp.org/pid/98/6127.html#j214) [\[j193\]](https://dblp.org/pid/98/6127.html#j193) [\[i80\]](https://dblp.org/pid/98/6127.html#i80) [\[i79\]](https://dblp.org/pid/98/6127.html#i79) [\[j179\]](https://dblp.org/pid/98/6127.html#j179) [\[j178\]](https://dblp.org/pid/98/6127.html#j178) [\[j175\]](https://dblp.org/pid/98/6127.html#j175) [\[j150\]](https://dblp.org/pid/98/6127.html#j150) [\[j149\]](https://dblp.org/pid/98/6127.html#j149) [\[j141\]](https://dblp.org/pid/98/6127.html#j141) [\[j133\]](https://dblp.org/pid/98/6127.html#j133) [\[j130\]](https://dblp.org/pid/98/6127.html#j130) [\[c95\]](https://dblp.org/pid/98/6127.html#c95) [\[i50\]](https://dblp.org/pid/98/6127.html#i50) [\[j116\]](https://dblp.org/pid/98/6127.html#j116) [\[j111\]](https://dblp.org/pid/98/6127.html#j111) [\[c86\]](https://dblp.org/pid/98/6127.html#c86) [\[i33\]](https://dblp.org/pid/98/6127.html#i33) [\[i32\]](https://dblp.org/pid/98/6127.html#i32) [\[j95\]](https://dblp.org/pid/98/6127.html#j95)

[217](https://dblp.org/pid/98/6127.html?view=joint&param=217 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qingming Huang](https://dblp.org/pid/68/4388.html)

[\[j100\]](https://dblp.org/pid/98/6127.html#j100) [\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[218](https://dblp.org/pid/98/6127.html?view=joint&param=218 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wei Huang](https://dblp.org/pid/81/6685.html)

[\[c122\]](https://dblp.org/pid/98/6127.html#c122) [\[i115\]](https://dblp.org/pid/98/6127.html#i115)

[219](https://dblp.org/pid/98/6127.html?view=joint&param=219 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenjian Huang 0001](https://dblp.org/pid/142/1752-1.html)

[\[j236\]](https://dblp.org/pid/98/6127.html#j236) [\[j209\]](https://dblp.org/pid/98/6127.html#j209)

[220](https://dblp.org/pid/98/6127.html?view=joint&param=220 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenxuan Huang 0001](https://dblp.org/pid/192/1157-1.html)

[\[i59\]](https://dblp.org/pid/98/6127.html#i59)

[221](https://dblp.org/pid/98/6127.html?view=joint&param=221 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Huang](https://dblp.org/pid/98/5766.html)

[\[j208\]](https://dblp.org/pid/98/6127.html#j208) [\[j172\]](https://dblp.org/pid/98/6127.html#j172) [\[j136\]](https://dblp.org/pid/98/6127.html#j136)

[222](https://dblp.org/pid/98/6127.html?view=joint&param=222 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xingsen Huang](https://dblp.org/pid/284/1333.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[223](https://dblp.org/pid/98/6127.html?view=joint&param=223 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yi-Jie Huang](https://dblp.org/pid/184/6951.html)

[\[j241\]](https://dblp.org/pid/98/6127.html#j241)

[224](https://dblp.org/pid/98/6127.html?view=joint&param=224 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuanjun Huang](https://dblp.org/pid/168/0702.html)

[\[c71\]](https://dblp.org/pid/98/6127.html#c71)

[225](https://dblp.org/pid/98/6127.html?view=joint&param=225 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuqing Huang](https://dblp.org/pid/134/5853.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[226](https://dblp.org/pid/98/6127.html?view=joint&param=226 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhuoxu Huang](https://dblp.org/pid/331/8231.html)

[\[i92\]](https://dblp.org/pid/98/6127.html#i92) [\[j188\]](https://dblp.org/pid/98/6127.html#j188) [\[i85\]](https://dblp.org/pid/98/6127.html#i85) [\[i82\]](https://dblp.org/pid/98/6127.html#i82) [\[j170\]](https://dblp.org/pid/98/6127.html#j170) [\[i42\]](https://dblp.org/pid/98/6127.html#i42)

[227](https://dblp.org/pid/98/6127.html?view=joint&param=227 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[G. Thomas Hudson](https://dblp.org/pid/307/8392.html)

[\[i85\]](https://dblp.org/pid/98/6127.html#i85)

[228](https://dblp.org/pid/98/6127.html?view=joint&param=228 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiantong Huo](https://dblp.org/pid/252/7172.html)

[\[j203\]](https://dblp.org/pid/98/6127.html#j203)

[229](https://dblp.org/pid/98/6127.html?view=joint&param=229 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhen Huo](https://dblp.org/pid/239/6395.html)

[\[j76\]](https://dblp.org/pid/98/6127.html#j76)

[230](https://dblp.org/pid/98/6127.html?view=joint&param=230 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhisheng Huo](https://dblp.org/pid/171/1089.html)

[\[j203\]](https://dblp.org/pid/98/6127.html#j203)

[231](https://dblp.org/pid/98/6127.html?view=joint&param=231 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Beibei Ji](https://dblp.org/pid/228/7534.html)

[\[j86\]](https://dblp.org/pid/98/6127.html#j86) [\[j61\]](https://dblp.org/pid/98/6127.html#j61)

[232](https://dblp.org/pid/98/6127.html?view=joint&param=232 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[j223\]](https://dblp.org/pid/98/6127.html#j223) [\[j66\]](https://dblp.org/pid/98/6127.html#j66) [\[c45\]](https://dblp.org/pid/98/6127.html#c45) [\[i3\]](https://dblp.org/pid/98/6127.html#i3)

[233](https://dblp.org/pid/98/6127.html?view=joint&param=233 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shunping Ji](https://dblp.org/pid/123/0960.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[234](https://dblp.org/pid/98/6127.html?view=joint&param=234 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiang Ji](https://dblp.org/pid/46/2563.html)

[\[j24\]](https://dblp.org/pid/98/6127.html#j24) [\[j19\]](https://dblp.org/pid/98/6127.html#j19)

[235](https://dblp.org/pid/98/6127.html?view=joint&param=235 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yamei Ji](https://dblp.org/pid/228/7312.html)

[\[j86\]](https://dblp.org/pid/98/6127.html#j86) [\[j61\]](https://dblp.org/pid/98/6127.html#j61)

[236](https://dblp.org/pid/98/6127.html?view=joint&param=236 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhong Ji](https://dblp.org/pid/36/6466.html)

[\[j263\]](https://dblp.org/pid/98/6127.html#j263) [\[j262\]](https://dblp.org/pid/98/6127.html#j262) [\[j252\]](https://dblp.org/pid/98/6127.html#j252) [\[j235\]](https://dblp.org/pid/98/6127.html#j235) [\[j234\]](https://dblp.org/pid/98/6127.html#j234) [\[j232\]](https://dblp.org/pid/98/6127.html#j232) [\[j224\]](https://dblp.org/pid/98/6127.html#j224) [\[i112\]](https://dblp.org/pid/98/6127.html#i112) [\[i105\]](https://dblp.org/pid/98/6127.html#i105) [\[i101\]](https://dblp.org/pid/98/6127.html#i101) [\[j218\]](https://dblp.org/pid/98/6127.html#j218) [\[j212\]](https://dblp.org/pid/98/6127.html#j212) [\[j197\]](https://dblp.org/pid/98/6127.html#j197) [\[j194\]](https://dblp.org/pid/98/6127.html#j194) [\[c113\]](https://dblp.org/pid/98/6127.html#c113) [\[c106\]](https://dblp.org/pid/98/6127.html#c106) [\[i81\]](https://dblp.org/pid/98/6127.html#i81) [\[i77\]](https://dblp.org/pid/98/6127.html#i77) [\[i74\]](https://dblp.org/pid/98/6127.html#i74) [\[i69\]](https://dblp.org/pid/98/6127.html#i69) [\[i68\]](https://dblp.org/pid/98/6127.html#i68) [\[j162\]](https://dblp.org/pid/98/6127.html#j162) [\[j156\]](https://dblp.org/pid/98/6127.html#j156) [\[j140\]](https://dblp.org/pid/98/6127.html#j140) [\[j139\]](https://dblp.org/pid/98/6127.html#j139) [\[j134\]](https://dblp.org/pid/98/6127.html#j134) [\[c90\]](https://dblp.org/pid/98/6127.html#c90) [\[i44\]](https://dblp.org/pid/98/6127.html#i44) [\[j110\]](https://dblp.org/pid/98/6127.html#j110) [\[i29\]](https://dblp.org/pid/98/6127.html#i29) [\[j101\]](https://dblp.org/pid/98/6127.html#j101) [\[j91\]](https://dblp.org/pid/98/6127.html#j91) [\[c78\]](https://dblp.org/pid/98/6127.html#c78) [\[j84\]](https://dblp.org/pid/98/6127.html#j84) [\[c65\]](https://dblp.org/pid/98/6127.html#c65) [\[i19\]](https://dblp.org/pid/98/6127.html#i19) [\[i12\]](https://dblp.org/pid/98/6127.html#i12)

[237](https://dblp.org/pid/98/6127.html?view=joint&param=237 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ruoxi Jia 0001](https://dblp.org/pid/147/5355-1.html)

[\[j275\]](https://dblp.org/pid/98/6127.html#j275)

[238](https://dblp.org/pid/98/6127.html?view=joint&param=238 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zizhou Jia](https://dblp.org/pid/248/9172.html)

[\[j113\]](https://dblp.org/pid/98/6127.html#j113)

[239](https://dblp.org/pid/98/6127.html?view=joint&param=239 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bo Jiang 0010](https://dblp.org/pid/34/2005-10.html)

[\[j31\]](https://dblp.org/pid/98/6127.html#j31)

[240](https://dblp.org/pid/98/6127.html?view=joint&param=240 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dongmei Jiang](https://dblp.org/pid/47/1926.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[241](https://dblp.org/pid/98/6127.html?view=joint&param=241 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Junjun Jiang](https://dblp.org/pid/119/0230.html)

[\[c24\]](https://dblp.org/pid/98/6127.html#c24)

[242](https://dblp.org/pid/98/6127.html?view=joint&param=242 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shuqiang Jiang](https://dblp.org/pid/90/3651.html)

[\[c70\]](https://dblp.org/pid/98/6127.html#c70)

[243](https://dblp.org/pid/98/6127.html?view=joint&param=243 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wei Jiang](https://dblp.org/pid/21/3839.html)

[\[j30\]](https://dblp.org/pid/98/6127.html#j30)

[244](https://dblp.org/pid/98/6127.html?view=joint&param=244 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xi Jiang 0001](https://dblp.org/pid/31/3804-1.html)

[\[j24\]](https://dblp.org/pid/98/6127.html#j24)

[245](https://dblp.org/pid/98/6127.html?view=joint&param=245 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaolong Jiang](https://dblp.org/pid/56/5097.html)

[\[c76\]](https://dblp.org/pid/98/6127.html#c76) [\[i26\]](https://dblp.org/pid/98/6127.html#i26)

[246](https://dblp.org/pid/98/6127.html?view=joint&param=246 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Youhai Jiang](https://dblp.org/pid/405/2309.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[247](https://dblp.org/pid/98/6127.html?view=joint&param=247 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Licheng Jiao](https://dblp.org/pid/40/3714.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75) [\[j86\]](https://dblp.org/pid/98/6127.html#j86) [\[j61\]](https://dblp.org/pid/98/6127.html#j61) [\[j39\]](https://dblp.org/pid/98/6127.html#j39)

[248](https://dblp.org/pid/98/6127.html?view=joint&param=248 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qiang Jiao](https://dblp.org/pid/166/3845.html)

[\[j247\]](https://dblp.org/pid/98/6127.html#j247) [\[j202\]](https://dblp.org/pid/98/6127.html#j202) [\[j198\]](https://dblp.org/pid/98/6127.html#j198) [\[j195\]](https://dblp.org/pid/98/6127.html#j195) [\[j186\]](https://dblp.org/pid/98/6127.html#j186) [\[c100\]](https://dblp.org/pid/98/6127.html#c100) [\[j133\]](https://dblp.org/pid/98/6127.html#j133)

[249](https://dblp.org/pid/98/6127.html?view=joint&param=249 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhanyu Jiao](https://dblp.org/pid/397/5892.html)

[\[j224\]](https://dblp.org/pid/98/6127.html#j224)

[250](https://dblp.org/pid/98/6127.html?view=joint&param=250 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shilong Jin](https://dblp.org/pid/248/2203.html)

[\[i106\]](https://dblp.org/pid/98/6127.html#i106)

[251](https://dblp.org/pid/98/6127.html?view=joint&param=251 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaoming Jin](https://dblp.org/pid/26/5593.html)

[\[c82\]](https://dblp.org/pid/98/6127.html#c82) [\[c57\]](https://dblp.org/pid/98/6127.html#c57) [\[i17\]](https://dblp.org/pid/98/6127.html#i17) [\[c23\]](https://dblp.org/pid/98/6127.html#c23)

[252](https://dblp.org/pid/98/6127.html?view=joint&param=252 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xing Jin](https://dblp.org/pid/02/2442.html)

[\[j15\]](https://dblp.org/pid/98/6127.html#j15)

[253](https://dblp.org/pid/98/6127.html?view=joint&param=253 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xuan Jin](https://dblp.org/pid/80/5681.html)

[\[c116\]](https://dblp.org/pid/98/6127.html#c116) [\[i52\]](https://dblp.org/pid/98/6127.html#i52)

[254](https://dblp.org/pid/98/6127.html?view=joint&param=254 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ziniu Jin](https://dblp.org/pid/396/8685.html)

[\[j247\]](https://dblp.org/pid/98/6127.html#j247)

[255](https://dblp.org/pid/98/6127.html?view=joint&param=255 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Patrick van Kaam](https://dblp.org/pid/49/4925.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[256](https://dblp.org/pid/98/6127.html?view=joint&param=256 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ben Kang](https://dblp.org/pid/340/1671.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[257](https://dblp.org/pid/98/6127.html?view=joint&param=257 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qiuhong Ke](https://dblp.org/pid/151/3574.html)

[\[j275\]](https://dblp.org/pid/98/6127.html#j275)

[258](https://dblp.org/pid/98/6127.html?view=joint&param=258 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Nasser Kehtarnavaz](https://dblp.org/pid/62/3700.html)

[\[j44\]](https://dblp.org/pid/98/6127.html#j44)

[259](https://dblp.org/pid/98/6127.html?view=joint&param=259 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Abdulrahman Kerim](https://dblp.org/pid/291/4782.html)

[\[j277\]](https://dblp.org/pid/98/6127.html#j277)

[260](https://dblp.org/pid/98/6127.html?view=joint&param=260 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kurt Keutzer](https://dblp.org/pid/k/KurtKeutzer.html)

[\[j65\]](https://dblp.org/pid/98/6127.html#j65)

[261](https://dblp.org/pid/98/6127.html?view=joint&param=261 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fouad Khelifi](https://dblp.org/pid/95/4960.html)

[\[j54\]](https://dblp.org/pid/98/6127.html#j54)

[262](https://dblp.org/pid/98/6127.html?view=joint&param=262 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[j188\]](https://dblp.org/pid/98/6127.html#j188) [\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[263](https://dblp.org/pid/98/6127.html?view=joint&param=263 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ioannis Kompatsiaris](https://dblp.org/pid/k/YiannisKompatsiaris.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[264](https://dblp.org/pid/98/6127.html?view=joint&param=264 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yinghui Kong](https://dblp.org/pid/23/867.html)

[\[j157\]](https://dblp.org/pid/98/6127.html#j157) [\[j125\]](https://dblp.org/pid/98/6127.html#j125) [\[j81\]](https://dblp.org/pid/98/6127.html#j81)

[265](https://dblp.org/pid/98/6127.html?view=joint&param=265 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Nick A. H. M. de Koning](https://dblp.org/pid/144/2054.html)

[\[c13\]](https://dblp.org/pid/98/6127.html#c13)

[266](https://dblp.org/pid/98/6127.html?view=joint&param=266 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Stephan Kopf](https://dblp.org/pid/33/724.html)

[\[c18\]](https://dblp.org/pid/98/6127.html#c18)

[267](https://dblp.org/pid/98/6127.html?view=joint&param=267 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Andrei Korostelev](https://dblp.org/pid/70/3744.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[268](https://dblp.org/pid/98/6127.html?view=joint&param=268 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[269](https://dblp.org/pid/98/6127.html?view=joint&param=269 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bart Kroon](https://dblp.org/pid/83/537.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[270](https://dblp.org/pid/98/6127.html?view=joint&param=270 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yangliu Kuai](https://dblp.org/pid/202/5604.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[271](https://dblp.org/pid/98/6127.html?view=joint&param=271 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yongchan Kwon](https://dblp.org/pid/189/2046.html)

[\[j275\]](https://dblp.org/pid/98/6127.html#j275)

[272](https://dblp.org/pid/98/6127.html?view=joint&param=272 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Robert Laganière](https://dblp.org/pid/32/1448.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[273](https://dblp.org/pid/98/6127.html?view=joint&param=273 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Changzhou Lai](https://dblp.org/pid/330/1965.html)

[\[j220\]](https://dblp.org/pid/98/6127.html#j220) [\[c95\]](https://dblp.org/pid/98/6127.html#c95)

[274](https://dblp.org/pid/98/6127.html?view=joint&param=274 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Simiao Lai](https://dblp.org/pid/282/1954.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[275](https://dblp.org/pid/98/6127.html?view=joint&param=275 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fons de Lange](https://dblp.org/pid/85/1849.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[276](https://dblp.org/pid/98/6127.html?view=joint&param=276 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Weilun Lao](https://dblp.org/pid/05/843.html)

[\[j4\]](https://dblp.org/pid/98/6127.html#j4) [\[j3\]](https://dblp.org/pid/98/6127.html#j3) [\[c15\]](https://dblp.org/pid/98/6127.html#c15) [\[c9\]](https://dblp.org/pid/98/6127.html#c9) [\[j1\]](https://dblp.org/pid/98/6127.html#j1) [\[c7\]](https://dblp.org/pid/98/6127.html#c7) [\[c6\]](https://dblp.org/pid/98/6127.html#c6)

[277](https://dblp.org/pid/98/6127.html?view=joint&param=277 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Alexander Lattas](https://dblp.org/pid/221/0633.html)

aka: Alexandros Lattas

[\[c89\]](https://dblp.org/pid/98/6127.html#c89) [\[i40\]](https://dblp.org/pid/98/6127.html#i40)

[278](https://dblp.org/pid/98/6127.html?view=joint&param=278 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Martin Lauer](https://dblp.org/pid/87/2031.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[279](https://dblp.org/pid/98/6127.html?view=joint&param=279 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kyuewang Lee](https://dblp.org/pid/189/5760.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[280](https://dblp.org/pid/98/6127.html?view=joint&param=280 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Rien van Leeuwen](https://dblp.org/pid/37/4896.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[281](https://dblp.org/pid/98/6127.html?view=joint&param=281 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[282](https://dblp.org/pid/98/6127.html?view=joint&param=282 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[José Lezama](https://dblp.org/pid/151/8861.html)

[\[j275\]](https://dblp.org/pid/98/6127.html#j275)

[283](https://dblp.org/pid/98/6127.html?view=joint&param=283 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Banghuai Li](https://dblp.org/pid/181/1410.html)

[\[j170\]](https://dblp.org/pid/98/6127.html#j170) [\[i42\]](https://dblp.org/pid/98/6127.html#i42)

[284](https://dblp.org/pid/98/6127.html?view=joint&param=284 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bin Li 0038](https://dblp.org/pid/89/6764-38.html)

[\[j162\]](https://dblp.org/pid/98/6127.html#j162)

[285](https://dblp.org/pid/98/6127.html?view=joint&param=285 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ce Li 0002](https://dblp.org/pid/58/411-2.html)

[\[j129\]](https://dblp.org/pid/98/6127.html#j129) [\[j66\]](https://dblp.org/pid/98/6127.html#j66) [\[c73\]](https://dblp.org/pid/98/6127.html#c73) [\[c53\]](https://dblp.org/pid/98/6127.html#c53) [\[j58\]](https://dblp.org/pid/98/6127.html#j58) [\[c45\]](https://dblp.org/pid/98/6127.html#c45) [\[c42\]](https://dblp.org/pid/98/6127.html#c42) [\[i9\]](https://dblp.org/pid/98/6127.html#i9) [\[i7\]](https://dblp.org/pid/98/6127.html#i7) [\[j40\]](https://dblp.org/pid/98/6127.html#j40) [\[i3\]](https://dblp.org/pid/98/6127.html#i3) [\[i2\]](https://dblp.org/pid/98/6127.html#i2)

[286](https://dblp.org/pid/98/6127.html?view=joint&param=286 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Changchun Li](https://dblp.org/pid/73/7819.html)

[\[j261\]](https://dblp.org/pid/98/6127.html#j261)

[287](https://dblp.org/pid/98/6127.html?view=joint&param=287 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chengxin Li](https://dblp.org/pid/166/6518.html)

[\[j260\]](https://dblp.org/pid/98/6127.html#j260) [\[j259\]](https://dblp.org/pid/98/6127.html#j259) [\[i70\]](https://dblp.org/pid/98/6127.html#i70) [\[i62\]](https://dblp.org/pid/98/6127.html#i62)

[288](https://dblp.org/pid/98/6127.html?view=joint&param=288 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Da Li 0003](https://dblp.org/pid/43/4804-3.html)

[\[j184\]](https://dblp.org/pid/98/6127.html#j184)

[289](https://dblp.org/pid/98/6127.html?view=joint&param=289 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dongdong Li](https://dblp.org/pid/14/5457.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[290](https://dblp.org/pid/98/6127.html?view=joint&param=290 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fan Li 0003](https://dblp.org/pid/73/237-3.html)

[\[j124\]](https://dblp.org/pid/98/6127.html#j124)

[291](https://dblp.org/pid/98/6127.html?view=joint&param=291 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fu Li 0003](https://dblp.org/pid/37/4556-3.html)

[\[c90\]](https://dblp.org/pid/98/6127.html#c90) [\[i44\]](https://dblp.org/pid/98/6127.html#i44)

[292](https://dblp.org/pid/98/6127.html?view=joint&param=292 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Guangfei Li](https://dblp.org/pid/226/4297.html)

[\[j200\]](https://dblp.org/pid/98/6127.html#j200) [\[j199\]](https://dblp.org/pid/98/6127.html#j199)

[293](https://dblp.org/pid/98/6127.html?view=joint&param=293 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Guanghe Li](https://dblp.org/pid/121/6489.html)

[\[j102\]](https://dblp.org/pid/98/6127.html#j102)

[294](https://dblp.org/pid/98/6127.html?view=joint&param=294 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hai Li](https://dblp.org/pid/30/5330.html)

[\[j55\]](https://dblp.org/pid/98/6127.html#j55)

[295](https://dblp.org/pid/98/6127.html?view=joint&param=295 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hanting Li](https://dblp.org/pid/276/2638.html)

[\[i97\]](https://dblp.org/pid/98/6127.html#i97)

[296](https://dblp.org/pid/98/6127.html?view=joint&param=296 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hanyu Li](https://dblp.org/pid/11/6652.html)

[\[j248\]](https://dblp.org/pid/98/6127.html#j248)

[297](https://dblp.org/pid/98/6127.html?view=joint&param=297 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haojie Li](https://dblp.org/pid/61/4041.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[298](https://dblp.org/pid/98/6127.html?view=joint&param=298 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hongguang Li](https://dblp.org/pid/02/3703.html)

[\[j56\]](https://dblp.org/pid/98/6127.html#j56)

[299](https://dblp.org/pid/98/6127.html?view=joint&param=299 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jia Li 0032](https://dblp.org/pid/23/6950-32.html)

[\[j167\]](https://dblp.org/pid/98/6127.html#j167) [\[j147\]](https://dblp.org/pid/98/6127.html#j147)

[300](https://dblp.org/pid/98/6127.html?view=joint&param=300 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jianxin Li 0001](https://dblp.org/pid/l/JianxinLi.html)

[\[i88\]](https://dblp.org/pid/98/6127.html#i88)

[301](https://dblp.org/pid/98/6127.html?view=joint&param=301 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiaxin Li](https://dblp.org/pid/69/327.html)

[\[c127\]](https://dblp.org/pid/98/6127.html#c127)

[302](https://dblp.org/pid/98/6127.html?view=joint&param=302 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jin Li 0011](https://dblp.org/pid/48/1097-11.html)

[\[c40\]](https://dblp.org/pid/98/6127.html#c40)

[303](https://dblp.org/pid/98/6127.html?view=joint&param=303 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jing Li 0010](https://dblp.org/pid/l/JingLi10.html)

[\[j30\]](https://dblp.org/pid/98/6127.html#j30) [\[j21\]](https://dblp.org/pid/98/6127.html#j21)

[304](https://dblp.org/pid/98/6127.html?view=joint&param=304 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jing Li 0036](https://dblp.org/pid/l/JingLi36.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[305](https://dblp.org/pid/98/6127.html?view=joint&param=305 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kaiming Li](https://dblp.org/pid/18/7426.html)

[\[j17\]](https://dblp.org/pid/98/6127.html#j17)

[306](https://dblp.org/pid/98/6127.html?view=joint&param=306 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lei Li](https://dblp.org/pid/13/7007.html)

[\[j260\]](https://dblp.org/pid/98/6127.html#j260) [\[i62\]](https://dblp.org/pid/98/6127.html#i62)

[307](https://dblp.org/pid/98/6127.html?view=joint&param=307 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Leida Li](https://dblp.org/pid/92/6630.html)

[\[c57\]](https://dblp.org/pid/98/6127.html#c57) [\[i17\]](https://dblp.org/pid/98/6127.html#i17)

[308](https://dblp.org/pid/98/6127.html?view=joint&param=308 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Li Li](https://dblp.org/pid/53/2189.html)

[\[j81\]](https://dblp.org/pid/98/6127.html#j81)

[309](https://dblp.org/pid/98/6127.html?view=joint&param=309 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lin Li](https://dblp.org/pid/73/2252.html)

[\[j230\]](https://dblp.org/pid/98/6127.html#j230)

[310](https://dblp.org/pid/98/6127.html?view=joint&param=310 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lingjun Li](https://dblp.org/pid/39/201.html)

[\[j135\]](https://dblp.org/pid/98/6127.html#j135)

[311](https://dblp.org/pid/98/6127.html?view=joint&param=311 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ning Li 0044](https://dblp.org/pid/14/5410-44.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[312](https://dblp.org/pid/98/6127.html?view=joint&param=312 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shipeng Li 0001](https://dblp.org/pid/31/3974-1.html)

[\[c3\]](https://dblp.org/pid/98/6127.html#c3)

[313](https://dblp.org/pid/98/6127.html?view=joint&param=313 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shuo Li 0001](https://dblp.org/pid/49/595-1.html)

[\[j131\]](https://dblp.org/pid/98/6127.html#j131)

[314](https://dblp.org/pid/98/6127.html?view=joint&param=314 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Sijie Li](https://dblp.org/pid/58/6303.html)

[\[i96\]](https://dblp.org/pid/98/6127.html#i96)

[315](https://dblp.org/pid/98/6127.html?view=joint&param=315 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tingmin Li](https://dblp.org/pid/380/5999.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[316](https://dblp.org/pid/98/6127.html?view=joint&param=316 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wei Li](https://dblp.org/pid/64/6025.html)

[\[j233\]](https://dblp.org/pid/98/6127.html#j233)

[317](https://dblp.org/pid/98/6127.html?view=joint&param=317 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wei Li 0130](https://dblp.org/pid/64/6025-130.html)

[\[j105\]](https://dblp.org/pid/98/6127.html#j105)

[318](https://dblp.org/pid/98/6127.html?view=joint&param=318 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xi Li 0001](https://dblp.org/pid/46/2311-1.html)

[\[j251\]](https://dblp.org/pid/98/6127.html#j251) [\[j245\]](https://dblp.org/pid/98/6127.html#j245) [\[j242\]](https://dblp.org/pid/98/6127.html#j242) [\[j232\]](https://dblp.org/pid/98/6127.html#j232) [\[j110\]](https://dblp.org/pid/98/6127.html#j110)

[319](https://dblp.org/pid/98/6127.html?view=joint&param=319 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiangtai Li](https://dblp.org/pid/239/4017.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[320](https://dblp.org/pid/98/6127.html?view=joint&param=320 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiangyang Li 0002](https://dblp.org/pid/80/4579-2.html)

[\[c70\]](https://dblp.org/pid/98/6127.html#c70)

[321](https://dblp.org/pid/98/6127.html?view=joint&param=321 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaohai Li](https://dblp.org/pid/00/38.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[322](https://dblp.org/pid/98/6127.html?view=joint&param=322 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaotong Li](https://dblp.org/pid/35/4953.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[323](https://dblp.org/pid/98/6127.html?view=joint&param=323 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ximing Li 0002](https://dblp.org/pid/130/1013-2.html)

[\[j261\]](https://dblp.org/pid/98/6127.html#j261)

[324](https://dblp.org/pid/98/6127.html?view=joint&param=324 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Li 0034](https://dblp.org/pid/09/1365-34.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110) [\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[325](https://dblp.org/pid/98/6127.html?view=joint&param=325 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xue Li](https://dblp.org/pid/181/2710.html)

[\[j106\]](https://dblp.org/pid/98/6127.html#j106)

[326](https://dblp.org/pid/98/6127.html?view=joint&param=326 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xuelong Li 0001](https://dblp.org/pid/l/XuelongLi.html)

[\[i112\]](https://dblp.org/pid/98/6127.html#i112) [\[j218\]](https://dblp.org/pid/98/6127.html#j218) [\[j213\]](https://dblp.org/pid/98/6127.html#j213) [\[j189\]](https://dblp.org/pid/98/6127.html#j189) [\[i74\]](https://dblp.org/pid/98/6127.html#i74) [\[j163\]](https://dblp.org/pid/98/6127.html#j163) [\[j139\]](https://dblp.org/pid/98/6127.html#j139) [\[j115\]](https://dblp.org/pid/98/6127.html#j115) [\[j96\]](https://dblp.org/pid/98/6127.html#j96) [\[c80\]](https://dblp.org/pid/98/6127.html#c80) [\[c64\]](https://dblp.org/pid/98/6127.html#c64) [\[j54\]](https://dblp.org/pid/98/6127.html#j54)

[327](https://dblp.org/pid/98/6127.html?view=joint&param=327 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ya-jun Li](https://dblp.org/pid/202/0089.html)

aka: Yajun Li

[\[j77\]](https://dblp.org/pid/98/6127.html#j77)

[328](https://dblp.org/pid/98/6127.html?view=joint&param=328 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yan Li](https://dblp.org/pid/87/660.html)

[\[i110\]](https://dblp.org/pid/98/6127.html#i110)

[329](https://dblp.org/pid/98/6127.html?view=joint&param=329 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yaqian Li](https://dblp.org/pid/154/1961.html)

[\[j241\]](https://dblp.org/pid/98/6127.html#j241)

[330](https://dblp.org/pid/98/6127.html?view=joint&param=330 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yaxuan Li](https://dblp.org/pid/92/6967.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[331](https://dblp.org/pid/98/6127.html?view=joint&param=331 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yin Li](https://dblp.org/pid/49/5981.html)

[\[j275\]](https://dblp.org/pid/98/6127.html#j275)

[332](https://dblp.org/pid/98/6127.html?view=joint&param=332 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yingming Li](https://dblp.org/pid/119/1901.html)

[\[j251\]](https://dblp.org/pid/98/6127.html#j251) [\[j245\]](https://dblp.org/pid/98/6127.html#j245) [\[j215\]](https://dblp.org/pid/98/6127.html#j215) [\[i58\]](https://dblp.org/pid/98/6127.html#i58)

[333](https://dblp.org/pid/98/6127.html?view=joint&param=333 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yixuan Li](https://dblp.org/pid/144/6087.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[334](https://dblp.org/pid/98/6127.html?view=joint&param=334 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yizhi Li](https://dblp.org/pid/234/5954.html)

[\[i85\]](https://dblp.org/pid/98/6127.html#i85)

[335](https://dblp.org/pid/98/6127.html?view=joint&param=335 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhenguo Li](https://dblp.org/pid/23/6479.html)

[\[c99\]](https://dblp.org/pid/98/6127.html#c99) [\[i57\]](https://dblp.org/pid/98/6127.html#i57)

[336](https://dblp.org/pid/98/6127.html?view=joint&param=336 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haoran Lian](https://dblp.org/pid/376/2960.html)

[\[c128\]](https://dblp.org/pid/98/6127.html#c128) [\[c122\]](https://dblp.org/pid/98/6127.html#c122) [\[i115\]](https://dblp.org/pid/98/6127.html#i115)

[337](https://dblp.org/pid/98/6127.html?view=joint&param=337 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xuhang Lian](https://dblp.org/pid/195/4363.html)

[\[j120\]](https://dblp.org/pid/98/6127.html#j120) [\[j107\]](https://dblp.org/pid/98/6127.html#j107)

[338](https://dblp.org/pid/98/6127.html?view=joint&param=338 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Cheng Liang](https://dblp.org/pid/81/9078.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[339](https://dblp.org/pid/98/6127.html?view=joint&param=339 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenli Liang](https://dblp.org/pid/175/8786.html)

[\[j228\]](https://dblp.org/pid/98/6127.html#j228) [\[j191\]](https://dblp.org/pid/98/6127.html#j191)

[340](https://dblp.org/pid/98/6127.html?view=joint&param=340 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yiwen Liang](https://dblp.org/pid/88/2113.html)

[\[j230\]](https://dblp.org/pid/98/6127.html#j230) [\[c120\]](https://dblp.org/pid/98/6127.html#c120) [\[i98\]](https://dblp.org/pid/98/6127.html#i98) [\[i94\]](https://dblp.org/pid/98/6127.html#i94)

[341](https://dblp.org/pid/98/6127.html?view=joint&param=341 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shengcai Liao](https://dblp.org/pid/16/8313.html)

[\[j203\]](https://dblp.org/pid/98/6127.html#j203)

[342](https://dblp.org/pid/98/6127.html?view=joint&param=342 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shuangli Liao](https://dblp.org/pid/218/7458.html)

[\[j47\]](https://dblp.org/pid/98/6127.html#j47)

[343](https://dblp.org/pid/98/6127.html?view=joint&param=343 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chang Soo Lim](https://dblp.org/pid/54/4422.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[344](https://dblp.org/pid/98/6127.html?view=joint&param=344 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chee Peng Lim](https://dblp.org/pid/28/6855.html)

[\[j88\]](https://dblp.org/pid/98/6127.html#j88) [\[j80\]](https://dblp.org/pid/98/6127.html#j80)

[345](https://dblp.org/pid/98/6127.html?view=joint&param=345 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chenghua Lin](https://dblp.org/pid/11/7536.html)

[\[i85\]](https://dblp.org/pid/98/6127.html#i85)

[346](https://dblp.org/pid/98/6127.html?view=joint&param=346 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liting Lin](https://dblp.org/pid/227/2204.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[347](https://dblp.org/pid/98/6127.html?view=joint&param=347 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shaohui Lin](https://dblp.org/pid/183/0917.html)

[\[j233\]](https://dblp.org/pid/98/6127.html#j233) [\[i59\]](https://dblp.org/pid/98/6127.html#i59)

[348](https://dblp.org/pid/98/6127.html?view=joint&param=348 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Weisi Lin](https://dblp.org/pid/14/3737.html)

[\[i95\]](https://dblp.org/pid/98/6127.html#i95)

[349](https://dblp.org/pid/98/6127.html?view=joint&param=349 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xuanxu Lin](https://dblp.org/pid/380/2324.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[350](https://dblp.org/pid/98/6127.html?view=joint&param=350 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zijia Lin](https://dblp.org/pid/78/9911.html)

[\[j271\]](https://dblp.org/pid/98/6127.html#j271) [\[j230\]](https://dblp.org/pid/98/6127.html#j230) [\[c129\]](https://dblp.org/pid/98/6127.html#c129) [\[c128\]](https://dblp.org/pid/98/6127.html#c128) [\[c127\]](https://dblp.org/pid/98/6127.html#c127) [\[c126\]](https://dblp.org/pid/98/6127.html#c126) [\[c123\]](https://dblp.org/pid/98/6127.html#c123) [\[c122\]](https://dblp.org/pid/98/6127.html#c122) [\[c120\]](https://dblp.org/pid/98/6127.html#c120) [\[c118\]](https://dblp.org/pid/98/6127.html#c118) [\[i115\]](https://dblp.org/pid/98/6127.html#i115) [\[i114\]](https://dblp.org/pid/98/6127.html#i114) [\[i113\]](https://dblp.org/pid/98/6127.html#i113) [\[i111\]](https://dblp.org/pid/98/6127.html#i111) [\[i107\]](https://dblp.org/pid/98/6127.html#i107) [\[i98\]](https://dblp.org/pid/98/6127.html#i98) [\[i94\]](https://dblp.org/pid/98/6127.html#i94) [\[c115\]](https://dblp.org/pid/98/6127.html#c115) [\[c114\]](https://dblp.org/pid/98/6127.html#c114) [\[c112\]](https://dblp.org/pid/98/6127.html#c112) [\[c108\]](https://dblp.org/pid/98/6127.html#c108) [\[c107\]](https://dblp.org/pid/98/6127.html#c107) [\[c105\]](https://dblp.org/pid/98/6127.html#c105) [\[i84\]](https://dblp.org/pid/98/6127.html#i84) [\[i78\]](https://dblp.org/pid/98/6127.html#i78) [\[i73\]](https://dblp.org/pid/98/6127.html#i73) [\[i71\]](https://dblp.org/pid/98/6127.html#i71) [\[i67\]](https://dblp.org/pid/98/6127.html#i67) [\[i64\]](https://dblp.org/pid/98/6127.html#i64) [\[i63\]](https://dblp.org/pid/98/6127.html#i63) [\[i56\]](https://dblp.org/pid/98/6127.html#i56) [\[i54\]](https://dblp.org/pid/98/6127.html#i54) [\[j126\]](https://dblp.org/pid/98/6127.html#j126) [\[j112\]](https://dblp.org/pid/98/6127.html#j112) [\[j93\]](https://dblp.org/pid/98/6127.html#j93) [\[j90\]](https://dblp.org/pid/98/6127.html#j90) [\[c81\]](https://dblp.org/pid/98/6127.html#c81) [\[c79\]](https://dblp.org/pid/98/6127.html#c79) [\[i25\]](https://dblp.org/pid/98/6127.html#i25) [\[i24\]](https://dblp.org/pid/98/6127.html#i24) [\[j70\]](https://dblp.org/pid/98/6127.html#j70) [\[c56\]](https://dblp.org/pid/98/6127.html#c56) [\[j45\]](https://dblp.org/pid/98/6127.html#j45) [\[c47\]](https://dblp.org/pid/98/6127.html#c47) [\[c43\]](https://dblp.org/pid/98/6127.html#c43) [\[c39\]](https://dblp.org/pid/98/6127.html#c39) [\[j41\]](https://dblp.org/pid/98/6127.html#j41) [\[j36\]](https://dblp.org/pid/98/6127.html#j36) [\[j35\]](https://dblp.org/pid/98/6127.html#j35)

[351](https://dblp.org/pid/98/6127.html?view=joint&param=351 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haibin Ling](https://dblp.org/pid/93/3488.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110) [\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[352](https://dblp.org/pid/98/6127.html?view=joint&param=352 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chang Liu](https://dblp.org/pid/52/5716.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[353](https://dblp.org/pid/98/6127.html?view=joint&param=353 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chang Liu 0072](https://dblp.org/pid/52/5716-72.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[354](https://dblp.org/pid/98/6127.html?view=joint&param=354 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chenfeng Liu](https://dblp.org/pid/174/4324.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[355](https://dblp.org/pid/98/6127.html?view=joint&param=355 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chenglong Liu](https://dblp.org/pid/123/5266.html)

[\[i77\]](https://dblp.org/pid/98/6127.html#i77)

[356](https://dblp.org/pid/98/6127.html?view=joint&param=356 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chunhui Liu 0004](https://dblp.org/pid/20/5393-4.html)

[\[j122\]](https://dblp.org/pid/98/6127.html#j122) [\[j56\]](https://dblp.org/pid/98/6127.html#j56)

[357](https://dblp.org/pid/98/6127.html?view=joint&param=357 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chunlei Liu 0001](https://dblp.org/pid/76/5853-1.html)

[\[j98\]](https://dblp.org/pid/98/6127.html#j98) [\[i13\]](https://dblp.org/pid/98/6127.html#i13) [\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[358](https://dblp.org/pid/98/6127.html?view=joint&param=358 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Feixiang Liu](https://dblp.org/pid/204/9610.html)

[\[j273\]](https://dblp.org/pid/98/6127.html#j273) [\[i109\]](https://dblp.org/pid/98/6127.html#i109)

[359](https://dblp.org/pid/98/6127.html?view=joint&param=359 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hao Liu 0019](https://dblp.org/pid/09/3214-19.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[360](https://dblp.org/pid/98/6127.html?view=joint&param=360 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Heng Liu 0002](https://dblp.org/pid/59/3260-2.html)

[\[j177\]](https://dblp.org/pid/98/6127.html#j177) [\[j158\]](https://dblp.org/pid/98/6127.html#j158) [\[j106\]](https://dblp.org/pid/98/6127.html#j106) [\[c75\]](https://dblp.org/pid/98/6127.html#c75) [\[i22\]](https://dblp.org/pid/98/6127.html#i22) [\[j85\]](https://dblp.org/pid/98/6127.html#j85) [\[j82\]](https://dblp.org/pid/98/6127.html#j82) [\[j74\]](https://dblp.org/pid/98/6127.html#j74) [\[c54\]](https://dblp.org/pid/98/6127.html#c54) [\[j64\]](https://dblp.org/pid/98/6127.html#j64) [\[j60\]](https://dblp.org/pid/98/6127.html#j60) [\[j59\]](https://dblp.org/pid/98/6127.html#j59)

[361](https://dblp.org/pid/98/6127.html?view=joint&param=361 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hong Liu 0008](https://dblp.org/pid/29/5010-8.html)

[\[j44\]](https://dblp.org/pid/98/6127.html#j44) [\[c24\]](https://dblp.org/pid/98/6127.html#c24) [\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[362](https://dblp.org/pid/98/6127.html?view=joint&param=362 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hongshen Liu](https://dblp.org/pid/169/4604.html)

[\[j74\]](https://dblp.org/pid/98/6127.html#j74) [\[j60\]](https://dblp.org/pid/98/6127.html#j60)

[363](https://dblp.org/pid/98/6127.html?view=joint&param=363 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ji Liu 0002](https://dblp.org/pid/51/4433-2.html)

[\[c83\]](https://dblp.org/pid/98/6127.html#c83) [\[c79\]](https://dblp.org/pid/98/6127.html#c79) [\[i25\]](https://dblp.org/pid/98/6127.html#i25) [\[i23\]](https://dblp.org/pid/98/6127.html#i23) [\[c55\]](https://dblp.org/pid/98/6127.html#c55) [\[i14\]](https://dblp.org/pid/98/6127.html#i14)

[364](https://dblp.org/pid/98/6127.html?view=joint&param=364 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jianan Liu](https://dblp.org/pid/146/6864.html)

[\[j178\]](https://dblp.org/pid/98/6127.html#j178) [\[j175\]](https://dblp.org/pid/98/6127.html#j175) [\[j141\]](https://dblp.org/pid/98/6127.html#j141) [\[c95\]](https://dblp.org/pid/98/6127.html#c95) [\[i33\]](https://dblp.org/pid/98/6127.html#i33)

[365](https://dblp.org/pid/98/6127.html?view=joint&param=365 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jianyong Liu](https://dblp.org/pid/10/1468.html)

[\[j177\]](https://dblp.org/pid/98/6127.html#j177) [\[c75\]](https://dblp.org/pid/98/6127.html#c75) [\[i22\]](https://dblp.org/pid/98/6127.html#i22)

[366](https://dblp.org/pid/98/6127.html?view=joint&param=366 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jianzhuang Liu](https://dblp.org/pid/l/JianzhuangLiu.html)

[\[c73\]](https://dblp.org/pid/98/6127.html#c73) [\[c53\]](https://dblp.org/pid/98/6127.html#c53) [\[j49\]](https://dblp.org/pid/98/6127.html#j49) [\[c45\]](https://dblp.org/pid/98/6127.html#c45) [\[c42\]](https://dblp.org/pid/98/6127.html#c42) [\[c36\]](https://dblp.org/pid/98/6127.html#c36) [\[i10\]](https://dblp.org/pid/98/6127.html#i10) [\[i9\]](https://dblp.org/pid/98/6127.html#i9) [\[i7\]](https://dblp.org/pid/98/6127.html#i7) [\[i5\]](https://dblp.org/pid/98/6127.html#i5)

[367](https://dblp.org/pid/98/6127.html?view=joint&param=367 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jing Liu 0001](https://dblp.org/pid/72/2590-1.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[368](https://dblp.org/pid/98/6127.html?view=joint&param=368 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jingren Liu](https://dblp.org/pid/269/7845.html)

[\[j263\]](https://dblp.org/pid/98/6127.html#j263) [\[j262\]](https://dblp.org/pid/98/6127.html#j262) [\[i101\]](https://dblp.org/pid/98/6127.html#i101) [\[i74\]](https://dblp.org/pid/98/6127.html#i74) [\[i69\]](https://dblp.org/pid/98/6127.html#i69) [\[i68\]](https://dblp.org/pid/98/6127.html#i68)

[369](https://dblp.org/pid/98/6127.html?view=joint&param=369 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jirui Liu](https://dblp.org/pid/302/7791.html)

[\[c97\]](https://dblp.org/pid/98/6127.html#c97)

[370](https://dblp.org/pid/98/6127.html?view=joint&param=370 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jun Liu 0069](https://dblp.org/pid/95/3736-69.html)

[\[i95\]](https://dblp.org/pid/98/6127.html#i95)

[371](https://dblp.org/pid/98/6127.html?view=joint&param=371 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kunlong Liu](https://dblp.org/pid/274/2407.html)

[\[j149\]](https://dblp.org/pid/98/6127.html#j149)

[372](https://dblp.org/pid/98/6127.html?view=joint&param=372 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Li Liu 0004](https://dblp.org/pid/33/4528-4.html)

[\[j151\]](https://dblp.org/pid/98/6127.html#j151) [\[j68\]](https://dblp.org/pid/98/6127.html#j68) [\[j53\]](https://dblp.org/pid/98/6127.html#j53) [\[c46\]](https://dblp.org/pid/98/6127.html#c46) [\[c39\]](https://dblp.org/pid/98/6127.html#c39) [\[i8\]](https://dblp.org/pid/98/6127.html#i8) [\[j37\]](https://dblp.org/pid/98/6127.html#j37) [\[j35\]](https://dblp.org/pid/98/6127.html#j35) [\[j34\]](https://dblp.org/pid/98/6127.html#j34) [\[c32\]](https://dblp.org/pid/98/6127.html#c32) [\[c29\]](https://dblp.org/pid/98/6127.html#c29) [\[i4\]](https://dblp.org/pid/98/6127.html#i4)

[373](https://dblp.org/pid/98/6127.html?view=joint&param=373 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lihao Liu](https://dblp.org/pid/21/309.html)

[\[i111\]](https://dblp.org/pid/98/6127.html#i111) [\[c114\]](https://dblp.org/pid/98/6127.html#c114) [\[c105\]](https://dblp.org/pid/98/6127.html#c105) [\[i78\]](https://dblp.org/pid/98/6127.html#i78) [\[i71\]](https://dblp.org/pid/98/6127.html#i71) [\[i61\]](https://dblp.org/pid/98/6127.html#i61)

[374](https://dblp.org/pid/98/6127.html?view=joint&param=374 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Luoqi Liu](https://dblp.org/pid/29/8842.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[375](https://dblp.org/pid/98/6127.html?view=joint&param=375 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Mengyuan Liu](https://dblp.org/pid/143/0160.html)

[\[j44\]](https://dblp.org/pid/98/6127.html#j44) [\[c24\]](https://dblp.org/pid/98/6127.html#c24)

[376](https://dblp.org/pid/98/6127.html?view=joint&param=376 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Mushui Liu](https://dblp.org/pid/334/2912.html)

[\[j251\]](https://dblp.org/pid/98/6127.html#j251) [\[j242\]](https://dblp.org/pid/98/6127.html#j242) [\[j212\]](https://dblp.org/pid/98/6127.html#j212)

[377](https://dblp.org/pid/98/6127.html?view=joint&param=377 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Nian Liu 0002](https://dblp.org/pid/30/2704-2.html)

[\[j132\]](https://dblp.org/pid/98/6127.html#j132)

[378](https://dblp.org/pid/98/6127.html?view=joint&param=378 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Pengzhang Liu](https://dblp.org/pid/44/7674.html)

[\[j230\]](https://dblp.org/pid/98/6127.html#j230) [\[j219\]](https://dblp.org/pid/98/6127.html#j219) [\[c125\]](https://dblp.org/pid/98/6127.html#c125) [\[i99\]](https://dblp.org/pid/98/6127.html#i99) [\[c101\]](https://dblp.org/pid/98/6127.html#c101)

[379](https://dblp.org/pid/98/6127.html?view=joint&param=379 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qi Liu](https://dblp.org/pid/95/2446.html)

[\[j268\]](https://dblp.org/pid/98/6127.html#j268)

[380](https://dblp.org/pid/98/6127.html?view=joint&param=380 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qiang Liu 0016](https://dblp.org/pid/61/3234-16.html)

[\[j89\]](https://dblp.org/pid/98/6127.html#j89) [\[c34\]](https://dblp.org/pid/98/6127.html#c34)

[381](https://dblp.org/pid/98/6127.html?view=joint&param=381 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qiaoyan Liu](https://dblp.org/pid/212/1390.html)

[\[j46\]](https://dblp.org/pid/98/6127.html#j46)

[382](https://dblp.org/pid/98/6127.html?view=joint&param=382 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qingshan Liu 0001](https://dblp.org/pid/95/1247.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[383](https://dblp.org/pid/98/6127.html?view=joint&param=383 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tianming Liu 0001](https://dblp.org/pid/96/5013-1.html)

[\[j24\]](https://dblp.org/pid/98/6127.html#j24) [\[j23\]](https://dblp.org/pid/98/6127.html#j23) [\[j19\]](https://dblp.org/pid/98/6127.html#j19) [\[j17\]](https://dblp.org/pid/98/6127.html#j17)

[384](https://dblp.org/pid/98/6127.html?view=joint&param=384 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ting Liu 0018](https://dblp.org/pid/52/5150-18.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110) [\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[385](https://dblp.org/pid/98/6127.html?view=joint&param=385 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wanquan Liu](https://dblp.org/pid/53/4712.html)

[\[j40\]](https://dblp.org/pid/98/6127.html#j40)

[386](https://dblp.org/pid/98/6127.html?view=joint&param=386 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Weide Liu](https://dblp.org/pid/261/9166.html)

[\[i95\]](https://dblp.org/pid/98/6127.html#i95)

[387](https://dblp.org/pid/98/6127.html?view=joint&param=387 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenbing Liu](https://dblp.org/pid/03/782.html)

[\[j199\]](https://dblp.org/pid/98/6127.html#j199)

[388](https://dblp.org/pid/98/6127.html?view=joint&param=388 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenjian Liu](https://dblp.org/pid/92/251.html)

[\[j229\]](https://dblp.org/pid/98/6127.html#j229)

[389](https://dblp.org/pid/98/6127.html?view=joint&param=389 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wu Liu 0005](https://dblp.org/pid/31/4112-5.html)

[\[c91\]](https://dblp.org/pid/98/6127.html#c91) [\[i43\]](https://dblp.org/pid/98/6127.html#i43)

[390](https://dblp.org/pid/98/6127.html?view=joint&param=390 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaoyu Liu 0005](https://dblp.org/pid/78/6195-5.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[391](https://dblp.org/pid/98/6127.html?view=joint&param=391 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xinchen Liu](https://dblp.org/pid/36/2028.html)

[\[c91\]](https://dblp.org/pid/98/6127.html#c91) [\[i43\]](https://dblp.org/pid/98/6127.html#i43)

[392](https://dblp.org/pid/98/6127.html?view=joint&param=392 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xinyu Liu](https://dblp.org/pid/98/738.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[393](https://dblp.org/pid/98/6127.html?view=joint&param=393 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiyao Liu 0002](https://dblp.org/pid/138/9719-2.html)

[\[j234\]](https://dblp.org/pid/98/6127.html#j234) [\[c113\]](https://dblp.org/pid/98/6127.html#c113) [\[j156\]](https://dblp.org/pid/98/6127.html#j156) [\[j139\]](https://dblp.org/pid/98/6127.html#j139) [\[j134\]](https://dblp.org/pid/98/6127.html#j134) [\[i29\]](https://dblp.org/pid/98/6127.html#i29)

[394](https://dblp.org/pid/98/6127.html?view=joint&param=394 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xudong Liu](https://dblp.org/pid/90/2144.html)

[\[c79\]](https://dblp.org/pid/98/6127.html#c79) [\[i25\]](https://dblp.org/pid/98/6127.html#i25)

[395](https://dblp.org/pid/98/6127.html?view=joint&param=395 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xueru Liu](https://dblp.org/pid/316/3084.html)

[\[j145\]](https://dblp.org/pid/98/6127.html#j145)

[396](https://dblp.org/pid/98/6127.html?view=joint&param=396 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xuhui Liu](https://dblp.org/pid/09/4802.html)

[\[j109\]](https://dblp.org/pid/98/6127.html#j109) [\[c76\]](https://dblp.org/pid/98/6127.html#c76) [\[i26\]](https://dblp.org/pid/98/6127.html#i26)

[397](https://dblp.org/pid/98/6127.html?view=joint&param=397 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ya-Feng Liu](https://dblp.org/pid/29/8760.html)

[\[j31\]](https://dblp.org/pid/98/6127.html#j31)

[398](https://dblp.org/pid/98/6127.html?view=joint&param=398 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yang Liu 0069](https://dblp.org/pid/51/3710-0069.html)

[\[j273\]](https://dblp.org/pid/98/6127.html#j273) [\[j265\]](https://dblp.org/pid/98/6127.html#j265) [\[j254\]](https://dblp.org/pid/98/6127.html#j254) [\[j250\]](https://dblp.org/pid/98/6127.html#j250) [\[j248\]](https://dblp.org/pid/98/6127.html#j248) [\[j246\]](https://dblp.org/pid/98/6127.html#j246) [\[j240\]](https://dblp.org/pid/98/6127.html#j240) [\[j239\]](https://dblp.org/pid/98/6127.html#j239) [\[j231\]](https://dblp.org/pid/98/6127.html#j231) [\[j221\]](https://dblp.org/pid/98/6127.html#j221) [\[i109\]](https://dblp.org/pid/98/6127.html#i109) [\[i108\]](https://dblp.org/pid/98/6127.html#i108) [\[j211\]](https://dblp.org/pid/98/6127.html#j211) [\[j207\]](https://dblp.org/pid/98/6127.html#j207) [\[j206\]](https://dblp.org/pid/98/6127.html#j206) [\[j187\]](https://dblp.org/pid/98/6127.html#j187) [\[i66\]](https://dblp.org/pid/98/6127.html#i66) [\[i65\]](https://dblp.org/pid/98/6127.html#i65) [\[j169\]](https://dblp.org/pid/98/6127.html#j169) [\[j151\]](https://dblp.org/pid/98/6127.html#j151) [\[j149\]](https://dblp.org/pid/98/6127.html#j149) [\[j128\]](https://dblp.org/pid/98/6127.html#j128) [\[j117\]](https://dblp.org/pid/98/6127.html#j117) [\[j104\]](https://dblp.org/pid/98/6127.html#j104) [\[j83\]](https://dblp.org/pid/98/6127.html#j83) [\[j79\]](https://dblp.org/pid/98/6127.html#j79) [\[j78\]](https://dblp.org/pid/98/6127.html#j78) [\[c58\]](https://dblp.org/pid/98/6127.html#c58) [\[c51\]](https://dblp.org/pid/98/6127.html#c51) [\[c40\]](https://dblp.org/pid/98/6127.html#c40)

[399](https://dblp.org/pid/98/6127.html?view=joint&param=399 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yi Liu 0038](https://dblp.org/pid/97/4626-38.html)

[\[j276\]](https://dblp.org/pid/98/6127.html#j276) [\[j270\]](https://dblp.org/pid/98/6127.html#j270) [\[j266\]](https://dblp.org/pid/98/6127.html#j266) [\[j260\]](https://dblp.org/pid/98/6127.html#j260) [\[j259\]](https://dblp.org/pid/98/6127.html#j259) [\[j229\]](https://dblp.org/pid/98/6127.html#j229) [\[j227\]](https://dblp.org/pid/98/6127.html#j227) [\[j225\]](https://dblp.org/pid/98/6127.html#j225) [\[j192\]](https://dblp.org/pid/98/6127.html#j192) [\[i70\]](https://dblp.org/pid/98/6127.html#i70) [\[i62\]](https://dblp.org/pid/98/6127.html#i62) [\[i60\]](https://dblp.org/pid/98/6127.html#i60) [\[j152\]](https://dblp.org/pid/98/6127.html#j152) [\[j143\]](https://dblp.org/pid/98/6127.html#j143) [\[j142\]](https://dblp.org/pid/98/6127.html#j142) [\[j132\]](https://dblp.org/pid/98/6127.html#j132) [\[j114\]](https://dblp.org/pid/98/6127.html#j114) [\[j111\]](https://dblp.org/pid/98/6127.html#j111) [\[j99\]](https://dblp.org/pid/98/6127.html#j99) [\[j76\]](https://dblp.org/pid/98/6127.html#j76) [\[j71\]](https://dblp.org/pid/98/6127.html#j71) [\[c67\]](https://dblp.org/pid/98/6127.html#c67) [\[j63\]](https://dblp.org/pid/98/6127.html#j63) [\[j43\]](https://dblp.org/pid/98/6127.html#j43) [\[i6\]](https://dblp.org/pid/98/6127.html#i6)

[400](https://dblp.org/pid/98/6127.html?view=joint&param=400 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yichen Liu](https://dblp.org/pid/72/8807.html)

[\[j186\]](https://dblp.org/pid/98/6127.html#j186)

[401](https://dblp.org/pid/98/6127.html?view=joint&param=401 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhenyu Liu](https://dblp.org/pid/74/4038.html)

[\[j184\]](https://dblp.org/pid/98/6127.html#j184)

[402](https://dblp.org/pid/98/6127.html?view=joint&param=402 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhihui Liu](https://dblp.org/pid/56/807.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[403](https://dblp.org/pid/98/6127.html?view=joint&param=403 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ziquan Liu](https://dblp.org/pid/207/9035.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[404](https://dblp.org/pid/98/6127.html?view=joint&param=404 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yang Long 0001](https://dblp.org/pid/82/10183-1.html)

[\[c121\]](https://dblp.org/pid/98/6127.html#c121) [\[i103\]](https://dblp.org/pid/98/6127.html#i103) [\[c32\]](https://dblp.org/pid/98/6127.html#c32) [\[i4\]](https://dblp.org/pid/98/6127.html#i4)

[405](https://dblp.org/pid/98/6127.html?view=joint&param=405 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Lou](https://dblp.org/pid/133/5204.html)

[\[c60\]](https://dblp.org/pid/98/6127.html#c60)

[406](https://dblp.org/pid/98/6127.html?view=joint&param=406 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Feng Lu](https://dblp.org/pid/97/6483.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[407](https://dblp.org/pid/98/6127.html?view=joint&param=407 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haonan Lu](https://dblp.org/pid/129/0998.html)

[\[i72\]](https://dblp.org/pid/98/6127.html#i72)

[408](https://dblp.org/pid/98/6127.html?view=joint&param=408 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[409](https://dblp.org/pid/98/6127.html?view=joint&param=409 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ke Lu 0002](https://dblp.org/pid/33/1254-2.html)

[\[j171\]](https://dblp.org/pid/98/6127.html#j171)

[410](https://dblp.org/pid/98/6127.html?view=joint&param=410 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiankai Lu](https://dblp.org/pid/153/2122.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[411](https://dblp.org/pid/98/6127.html?view=joint&param=411 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Lu](https://dblp.org/pid/11/1952.html)

[\[j148\]](https://dblp.org/pid/98/6127.html#j148)

[412](https://dblp.org/pid/98/6127.html?view=joint&param=412 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhaoyang Lu](https://dblp.org/pid/59/568.html)

[\[j30\]](https://dblp.org/pid/98/6127.html#j30) [\[j21\]](https://dblp.org/pid/98/6127.html#j21) [\[c3\]](https://dblp.org/pid/98/6127.html#c3) [\[c2\]](https://dblp.org/pid/98/6127.html#c2)

[413](https://dblp.org/pid/98/6127.html?view=joint&param=413 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zheming Lu 0001](https://dblp.org/pid/148/1888-1.html)

aka: Zhe-Ming Lu 0001

[\[j215\]](https://dblp.org/pid/98/6127.html#j215) [\[j201\]](https://dblp.org/pid/98/6127.html#j201) [\[c102\]](https://dblp.org/pid/98/6127.html#c102) [\[i58\]](https://dblp.org/pid/98/6127.html#i58)

[414](https://dblp.org/pid/98/6127.html?view=joint&param=414 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ziqian Lu](https://dblp.org/pid/271/6997.html)

[\[j251\]](https://dblp.org/pid/98/6127.html#j251) [\[j242\]](https://dblp.org/pid/98/6127.html#j242)

[415](https://dblp.org/pid/98/6127.html?view=joint&param=415 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shangzhen Luan](https://dblp.org/pid/182/1956.html)

[\[j50\]](https://dblp.org/pid/98/6127.html#j50) [\[j49\]](https://dblp.org/pid/98/6127.html#j49) [\[c36\]](https://dblp.org/pid/98/6127.html#c36) [\[i5\]](https://dblp.org/pid/98/6127.html#i5) [\[i1\]](https://dblp.org/pid/98/6127.html#i1)

[416](https://dblp.org/pid/98/6127.html?view=joint&param=416 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[417](https://dblp.org/pid/98/6127.html?view=joint&param=417 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Johan J. Lukkien](https://dblp.org/pid/l/JJLukkien.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[418](https://dblp.org/pid/98/6127.html?view=joint&param=418 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Cheng Luo](https://dblp.org/pid/68/6443.html)

[\[i114\]](https://dblp.org/pid/98/6127.html#i114) [\[i113\]](https://dblp.org/pid/98/6127.html#i113)

[419](https://dblp.org/pid/98/6127.html?view=joint&param=419 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jingnan Luo](https://dblp.org/pid/379/6720.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i76\]](https://dblp.org/pid/98/6127.html#i76) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[420](https://dblp.org/pid/98/6127.html?view=joint&param=420 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ping Luo 0002](https://dblp.org/pid/54/4989-2.html)

[\[c99\]](https://dblp.org/pid/98/6127.html#c99) [\[i57\]](https://dblp.org/pid/98/6127.html#i57)

[421](https://dblp.org/pid/98/6127.html?view=joint&param=421 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Weixing Luo](https://dblp.org/pid/412/4581.html)

[\[j239\]](https://dblp.org/pid/98/6127.html#j239)

[422](https://dblp.org/pid/98/6127.html?view=joint&param=422 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaoyan Luo](https://dblp.org/pid/28/7701.html)

[\[j208\]](https://dblp.org/pid/98/6127.html#j208) [\[j172\]](https://dblp.org/pid/98/6127.html#j172) [\[j136\]](https://dblp.org/pid/98/6127.html#j136)

[423](https://dblp.org/pid/98/6127.html?view=joint&param=423 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xinbin Luo](https://dblp.org/pid/234/1736.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[424](https://dblp.org/pid/98/6127.html?view=joint&param=424 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yifei Luo](https://dblp.org/pid/58/3045.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[425](https://dblp.org/pid/98/6127.html?view=joint&param=425 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yongjiang Luo](https://dblp.org/pid/174/4309.html)

[\[j205\]](https://dblp.org/pid/98/6127.html#j205) [\[j175\]](https://dblp.org/pid/98/6127.html#j175) [\[j150\]](https://dblp.org/pid/98/6127.html#j150) [\[j143\]](https://dblp.org/pid/98/6127.html#j143) [\[j142\]](https://dblp.org/pid/98/6127.html#j142) [\[j119\]](https://dblp.org/pid/98/6127.html#j119) [\[c86\]](https://dblp.org/pid/98/6127.html#c86)

[426](https://dblp.org/pid/98/6127.html?view=joint&param=426 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuyang Luo](https://dblp.org/pid/307/1940.html)

[\[j229\]](https://dblp.org/pid/98/6127.html#j229)

[427](https://dblp.org/pid/98/6127.html?view=joint&param=427 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Minxuan Lv](https://dblp.org/pid/359/3555.html)

[\[c123\]](https://dblp.org/pid/98/6127.html#c123) [\[i114\]](https://dblp.org/pid/98/6127.html#i114) [\[i113\]](https://dblp.org/pid/98/6127.html#i113)

[428](https://dblp.org/pid/98/6127.html?view=joint&param=428 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wanjun Lv](https://dblp.org/pid/281/5591.html)

[\[i106\]](https://dblp.org/pid/98/6127.html#i106)

[429](https://dblp.org/pid/98/6127.html?view=joint&param=429 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Mengyao Lyu](https://dblp.org/pid/244/8467.html)

[\[j241\]](https://dblp.org/pid/98/6127.html#j241) [\[c120\]](https://dblp.org/pid/98/6127.html#c120) [\[c118\]](https://dblp.org/pid/98/6127.html#c118) [\[i110\]](https://dblp.org/pid/98/6127.html#i110) [\[i98\]](https://dblp.org/pid/98/6127.html#i98) [\[c116\]](https://dblp.org/pid/98/6127.html#c116) [\[c112\]](https://dblp.org/pid/98/6127.html#c112) [\[i73\]](https://dblp.org/pid/98/6127.html#i73) [\[i53\]](https://dblp.org/pid/98/6127.html#i53) [\[i52\]](https://dblp.org/pid/98/6127.html#i52)

[430](https://dblp.org/pid/98/6127.html?view=joint&param=430 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ningning Ma](https://dblp.org/pid/30/2310.html)

[\[c84\]](https://dblp.org/pid/98/6127.html#c84) [\[i38\]](https://dblp.org/pid/98/6127.html#i38)

[431](https://dblp.org/pid/98/6127.html?view=joint&param=431 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenya Ma](https://dblp.org/pid/180/7077.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[432](https://dblp.org/pid/98/6127.html?view=joint&param=432 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiao Ma 0013](https://dblp.org/pid/35/573-13.html)

[\[j179\]](https://dblp.org/pid/98/6127.html#j179) [\[i50\]](https://dblp.org/pid/98/6127.html#i50) [\[j112\]](https://dblp.org/pid/98/6127.html#j112)

[433](https://dblp.org/pid/98/6127.html?view=joint&param=433 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ritse Mann](https://dblp.org/pid/137/8733.html)

[\[j181\]](https://dblp.org/pid/98/6127.html#j181)

[434](https://dblp.org/pid/98/6127.html?view=joint&param=434 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lucio Marcenaro](https://dblp.org/pid/84/355.html)

[\[e1\]](https://dblp.org/pid/98/6127.html#e1)

[435](https://dblp.org/pid/98/6127.html?view=joint&param=435 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Demetris Marnerides](https://dblp.org/pid/217/1523.html)

[\[j222\]](https://dblp.org/pid/98/6127.html#j222)

[436](https://dblp.org/pid/98/6127.html?view=joint&param=436 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[437](https://dblp.org/pid/98/6127.html?view=joint&param=437 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tao Mei 0001](https://dblp.org/pid/12/5444-1.html)

[\[j155\]](https://dblp.org/pid/98/6127.html#j155) [\[j147\]](https://dblp.org/pid/98/6127.html#j147) [\[c91\]](https://dblp.org/pid/98/6127.html#c91) [\[i43\]](https://dblp.org/pid/98/6127.html#i43)

[438](https://dblp.org/pid/98/6127.html?view=joint&param=438 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Changxu Meng](https://dblp.org/pid/361/4963.html)

[\[i105\]](https://dblp.org/pid/98/6127.html#i105) [\[c106\]](https://dblp.org/pid/98/6127.html#c106)

[439](https://dblp.org/pid/98/6127.html?view=joint&param=439 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yang Meng](https://dblp.org/pid/41/7386.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[440](https://dblp.org/pid/98/6127.html?view=joint&param=440 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ashley Merien](https://dblp.org/pid/08/10729.html)

[\[j9\]](https://dblp.org/pid/98/6127.html#j9)

[441](https://dblp.org/pid/98/6127.html?view=joint&param=441 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Deshui Miao](https://dblp.org/pid/307/5501.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110) [\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[442](https://dblp.org/pid/98/6127.html?view=joint&param=442 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xingyu Miao](https://dblp.org/pid/280/7469.html)

[\[c121\]](https://dblp.org/pid/98/6127.html#c121) [\[i103\]](https://dblp.org/pid/98/6127.html#i103)

[443](https://dblp.org/pid/98/6127.html?view=joint&param=443 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yunqi Miao](https://dblp.org/pid/207/3366.html)

[\[i93\]](https://dblp.org/pid/98/6127.html#i93) [\[i91\]](https://dblp.org/pid/98/6127.html#i91) [\[i90\]](https://dblp.org/pid/98/6127.html#i90) [\[i86\]](https://dblp.org/pid/98/6127.html#i86) [\[j196\]](https://dblp.org/pid/98/6127.html#j196) [\[c117\]](https://dblp.org/pid/98/6127.html#c117) [\[i83\]](https://dblp.org/pid/98/6127.html#i83) [\[j179\]](https://dblp.org/pid/98/6127.html#j179) [\[j178\]](https://dblp.org/pid/98/6127.html#j178) [\[c89\]](https://dblp.org/pid/98/6127.html#c89) [\[i50\]](https://dblp.org/pid/98/6127.html#i50) [\[i40\]](https://dblp.org/pid/98/6127.html#i40) [\[i39\]](https://dblp.org/pid/98/6127.html#i39) [\[j112\]](https://dblp.org/pid/98/6127.html#j112) [\[c81\]](https://dblp.org/pid/98/6127.html#c81) [\[i24\]](https://dblp.org/pid/98/6127.html#i24) [\[j73\]](https://dblp.org/pid/98/6127.html#j73)

[444](https://dblp.org/pid/98/6127.html?view=joint&param=444 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Emmanouil Michail](https://dblp.org/pid/72/7219.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[445](https://dblp.org/pid/98/6127.html?view=joint&param=445 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shasha Mo](https://dblp.org/pid/166/7129.html)

[\[c128\]](https://dblp.org/pid/98/6127.html#c128)

[446](https://dblp.org/pid/98/6127.html?view=joint&param=446 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Juan David Mogollon](https://dblp.org/pid/325/7624.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[447](https://dblp.org/pid/98/6127.html?view=joint&param=447 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Giovanni Montana](https://dblp.org/pid/89/449.html)

[\[j176\]](https://dblp.org/pid/98/6127.html#j176) [\[j171\]](https://dblp.org/pid/98/6127.html#j171)

[448](https://dblp.org/pid/98/6127.html?view=joint&param=448 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Joonyoung Moon](https://dblp.org/pid/214/6590.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[449](https://dblp.org/pid/98/6127.html?view=joint&param=449 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Catarina Moreira](https://dblp.org/pid/28/10108.html)

[\[j268\]](https://dblp.org/pid/98/6127.html#j268)

[450](https://dblp.org/pid/98/6127.html?view=joint&param=450 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Carlos Francisco Moreno-García](https://dblp.org/pid/150/4768.html)

[\[j274\]](https://dblp.org/pid/98/6127.html#j274)

[451](https://dblp.org/pid/98/6127.html?view=joint&param=451 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yipeng Mou](https://dblp.org/pid/237/1187.html)

[\[c53\]](https://dblp.org/pid/98/6127.html#c53)

[452](https://dblp.org/pid/98/6127.html?view=joint&param=452 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Noura Al Moubayed](https://dblp.org/pid/27/8509.html)

[\[i85\]](https://dblp.org/pid/98/6127.html#i85)

[453](https://dblp.org/pid/98/6127.html?view=joint&param=453 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lifu Mu](https://dblp.org/pid/322/8822.html)

[\[j156\]](https://dblp.org/pid/98/6127.html#j156)

[454](https://dblp.org/pid/98/6127.html?view=joint&param=454 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Vittorio Murino](https://dblp.org/pid/62/6790.html)

[\[j98\]](https://dblp.org/pid/98/6127.html#j98) [\[i13\]](https://dblp.org/pid/98/6127.html#i13)

[455](https://dblp.org/pid/98/6127.html?view=joint&param=455 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Suphi Umut Naci](https://dblp.org/pid/91/6874.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[456](https://dblp.org/pid/98/6127.html?view=joint&param=456 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Alexey Nekrasov 0001](https://dblp.org/pid/32/1352-1.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[457](https://dblp.org/pid/98/6127.html?view=joint&param=457 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jan Nesvadba](https://dblp.org/pid/58/6462.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[458](https://dblp.org/pid/98/6127.html?view=joint&param=458 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kai Ni](https://dblp.org/pid/46/3815.html)

[\[i41\]](https://dblp.org/pid/98/6127.html#i41)

[459](https://dblp.org/pid/98/6127.html?view=joint&param=459 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qiang Ni](https://dblp.org/pid/87/3074.html)

[\[j180\]](https://dblp.org/pid/98/6127.html#j180) [\[j157\]](https://dblp.org/pid/98/6127.html#j157) [\[j125\]](https://dblp.org/pid/98/6127.html#j125) [\[j93\]](https://dblp.org/pid/98/6127.html#j93) [\[j81\]](https://dblp.org/pid/98/6127.html#j81) [\[j70\]](https://dblp.org/pid/98/6127.html#j70) [\[j68\]](https://dblp.org/pid/98/6127.html#j68)

[460](https://dblp.org/pid/98/6127.html?view=joint&param=460 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Feiping Nie 0001](https://dblp.org/pid/80/5755.html)

[\[j79\]](https://dblp.org/pid/98/6127.html#j79) [\[j47\]](https://dblp.org/pid/98/6127.html#j47)

[461](https://dblp.org/pid/98/6127.html?view=joint&param=461 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jing Nie 0001](https://dblp.org/pid/39/5493-1.html)

[\[j189\]](https://dblp.org/pid/98/6127.html#j189) [\[j165\]](https://dblp.org/pid/98/6127.html#j165) [\[j161\]](https://dblp.org/pid/98/6127.html#j161) [\[j144\]](https://dblp.org/pid/98/6127.html#j144) [\[j115\]](https://dblp.org/pid/98/6127.html#j115) [\[c80\]](https://dblp.org/pid/98/6127.html#c80)

[462](https://dblp.org/pid/98/6127.html?view=joint&param=462 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qinqin Nie](https://dblp.org/pid/234/1733.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[463](https://dblp.org/pid/98/6127.html?view=joint&param=463 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Ning 0001](https://dblp.org/pid/28/8118-1.html)

[\[j268\]](https://dblp.org/pid/98/6127.html#j268)

[464](https://dblp.org/pid/98/6127.html?view=joint&param=464 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jianwei Niu 0002](https://dblp.org/pid/25/4653-2.html)

[\[c128\]](https://dblp.org/pid/98/6127.html#c128) [\[c122\]](https://dblp.org/pid/98/6127.html#c122)

[465](https://dblp.org/pid/98/6127.html?view=joint&param=465 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Penghui Niu](https://dblp.org/pid/118/3791.html)

[\[j244\]](https://dblp.org/pid/98/6127.html#j244) [\[i88\]](https://dblp.org/pid/98/6127.html#i88) [\[j204\]](https://dblp.org/pid/98/6127.html#j204)

[466](https://dblp.org/pid/98/6127.html?view=joint&param=466 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Quanzhu Niu](https://dblp.org/pid/412/8967.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[467](https://dblp.org/pid/98/6127.html?view=joint&param=467 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shuaicheng Niu](https://dblp.org/pid/254/1388.html)

[\[c120\]](https://dblp.org/pid/98/6127.html#c120) [\[i98\]](https://dblp.org/pid/98/6127.html#i98)

[468](https://dblp.org/pid/98/6127.html?view=joint&param=468 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Guid Oei](https://dblp.org/pid/90/10732.html)

[\[j9\]](https://dblp.org/pid/98/6127.html#j9)

[469](https://dblp.org/pid/98/6127.html?view=joint&param=469 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ding Sheng Ong](https://dblp.org/pid/284/9241.html)

[\[j270\]](https://dblp.org/pid/98/6127.html#j270) [\[j227\]](https://dblp.org/pid/98/6127.html#j227)

[470](https://dblp.org/pid/98/6127.html?view=joint&param=470 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenwu Ou](https://dblp.org/pid/198/5430.html)

[\[c123\]](https://dblp.org/pid/98/6127.html#c123)

[471](https://dblp.org/pid/98/6127.html?view=joint&param=471 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kannappan Palaniappan](https://dblp.org/pid/21/700.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[472](https://dblp.org/pid/98/6127.html?view=joint&param=472 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Feiyu Pan](https://dblp.org/pid/142/1276.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[473](https://dblp.org/pid/98/6127.html?view=joint&param=473 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hanzhao Pan](https://dblp.org/pid/421/4187.html)

[\[j266\]](https://dblp.org/pid/98/6127.html#j266)

[474](https://dblp.org/pid/98/6127.html?view=joint&param=474 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jing Pan](https://dblp.org/pid/13/718.html)

[\[j161\]](https://dblp.org/pid/98/6127.html#j161) [\[j144\]](https://dblp.org/pid/98/6127.html#j144) [\[j120\]](https://dblp.org/pid/98/6127.html#j120) [\[j107\]](https://dblp.org/pid/98/6127.html#j107) [\[j72\]](https://dblp.org/pid/98/6127.html#j72)

[475](https://dblp.org/pid/98/6127.html?view=joint&param=475 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Leiyu Pan](https://dblp.org/pid/359/6474.html)

[\[c123\]](https://dblp.org/pid/98/6127.html#c123) [\[i114\]](https://dblp.org/pid/98/6127.html#i114) [\[i113\]](https://dblp.org/pid/98/6127.html#i113)

[476](https://dblp.org/pid/98/6127.html?view=joint&param=476 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tianxiang Pan](https://dblp.org/pid/195/8239.html)

[\[c61\]](https://dblp.org/pid/98/6127.html#c61)

[477](https://dblp.org/pid/98/6127.html?view=joint&param=477 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yunhui Pan](https://dblp.org/pid/239/6380.html)

[\[j76\]](https://dblp.org/pid/98/6127.html#j76)

[478](https://dblp.org/pid/98/6127.html?view=joint&param=478 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yanwei Pang](https://dblp.org/pid/35/5889.html)

[\[j263\]](https://dblp.org/pid/98/6127.html#j263) [\[j262\]](https://dblp.org/pid/98/6127.html#j262) [\[j252\]](https://dblp.org/pid/98/6127.html#j252) [\[j235\]](https://dblp.org/pid/98/6127.html#j235) [\[j234\]](https://dblp.org/pid/98/6127.html#j234) [\[j224\]](https://dblp.org/pid/98/6127.html#j224) [\[i112\]](https://dblp.org/pid/98/6127.html#i112) [\[i105\]](https://dblp.org/pid/98/6127.html#i105) [\[i101\]](https://dblp.org/pid/98/6127.html#i101) [\[j218\]](https://dblp.org/pid/98/6127.html#j218) [\[j213\]](https://dblp.org/pid/98/6127.html#j213) [\[j194\]](https://dblp.org/pid/98/6127.html#j194) [\[j190\]](https://dblp.org/pid/98/6127.html#j190) [\[j189\]](https://dblp.org/pid/98/6127.html#j189) [\[c113\]](https://dblp.org/pid/98/6127.html#c113) [\[c106\]](https://dblp.org/pid/98/6127.html#c106) [\[i81\]](https://dblp.org/pid/98/6127.html#i81) [\[i74\]](https://dblp.org/pid/98/6127.html#i74) [\[i69\]](https://dblp.org/pid/98/6127.html#i69) [\[i68\]](https://dblp.org/pid/98/6127.html#i68) [\[j165\]](https://dblp.org/pid/98/6127.html#j165) [\[j164\]](https://dblp.org/pid/98/6127.html#j164) [\[j163\]](https://dblp.org/pid/98/6127.html#j163) [\[j161\]](https://dblp.org/pid/98/6127.html#j161) [\[j148\]](https://dblp.org/pid/98/6127.html#j148) [\[j144\]](https://dblp.org/pid/98/6127.html#j144) [\[j140\]](https://dblp.org/pid/98/6127.html#j140) [\[j139\]](https://dblp.org/pid/98/6127.html#j139) [\[j134\]](https://dblp.org/pid/98/6127.html#j134) [\[j120\]](https://dblp.org/pid/98/6127.html#j120) [\[j115\]](https://dblp.org/pid/98/6127.html#j115) [\[j110\]](https://dblp.org/pid/98/6127.html#j110) [\[i29\]](https://dblp.org/pid/98/6127.html#i29) [\[j107\]](https://dblp.org/pid/98/6127.html#j107) [\[j103\]](https://dblp.org/pid/98/6127.html#j103) [\[j101\]](https://dblp.org/pid/98/6127.html#j101) [\[j96\]](https://dblp.org/pid/98/6127.html#j96) [\[j91\]](https://dblp.org/pid/98/6127.html#j91) [\[c80\]](https://dblp.org/pid/98/6127.html#c80) [\[j84\]](https://dblp.org/pid/98/6127.html#j84) [\[j69\]](https://dblp.org/pid/98/6127.html#j69) [\[c65\]](https://dblp.org/pid/98/6127.html#c65) [\[c64\]](https://dblp.org/pid/98/6127.html#c64) [\[c63\]](https://dblp.org/pid/98/6127.html#c63) [\[i19\]](https://dblp.org/pid/98/6127.html#i19) [\[i12\]](https://dblp.org/pid/98/6127.html#i12)

[479](https://dblp.org/pid/98/6127.html?view=joint&param=479 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ziqi Pang](https://dblp.org/pid/255/9210.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[480](https://dblp.org/pid/98/6127.html?view=joint&param=480 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Eric J. Pauwels](https://dblp.org/pid/30/3284.html)

[\[j14\]](https://dblp.org/pid/98/6127.html#j14) [\[j13\]](https://dblp.org/pid/98/6127.html#j13) [\[j12\]](https://dblp.org/pid/98/6127.html#j12) [\[j8\]](https://dblp.org/pid/98/6127.html#j8) [\[c21\]](https://dblp.org/pid/98/6127.html#c21) [\[c20\]](https://dblp.org/pid/98/6127.html#c20) [\[c19\]](https://dblp.org/pid/98/6127.html#c19)

[481](https://dblp.org/pid/98/6127.html?view=joint&param=481 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jingchao Peng](https://dblp.org/pid/287/9324.html)

[\[j272\]](https://dblp.org/pid/98/6127.html#j272) [\[i117\]](https://dblp.org/pid/98/6127.html#i117)

[482](https://dblp.org/pid/98/6127.html?view=joint&param=482 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Peng Peng](https://dblp.org/pid/49/683.html)

[\[j25\]](https://dblp.org/pid/98/6127.html#j25)

[483](https://dblp.org/pid/98/6127.html?view=joint&param=483 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Asanka G. Perera](https://dblp.org/pid/231/9229.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[484](https://dblp.org/pid/98/6127.html?view=joint&param=484 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Alessandro Perina](https://dblp.org/pid/54/1195.html)

[\[j50\]](https://dblp.org/pid/98/6127.html#j50) [\[i1\]](https://dblp.org/pid/98/6127.html#i1)

[485](https://dblp.org/pid/98/6127.html?view=joint&param=485 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jaswanth Reddy Pochimireddy](https://dblp.org/pid/406/5059.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[486](https://dblp.org/pid/98/6127.html?view=joint&param=486 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Viktor Prutyanov](https://dblp.org/pid/245/3321.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[487](https://dblp.org/pid/98/6127.html?view=joint&param=487 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Nicolas Pugeault](https://dblp.org/pid/35/1348.html)

[\[j274\]](https://dblp.org/pid/98/6127.html#j274)

[488](https://dblp.org/pid/98/6127.html?view=joint&param=488 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Huaizhou Qi](https://dblp.org/pid/413/5945.html)

[\[j265\]](https://dblp.org/pid/98/6127.html#j265) [\[j250\]](https://dblp.org/pid/98/6127.html#j250)

[489](https://dblp.org/pid/98/6127.html?view=joint&param=489 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lu Qi](https://dblp.org/pid/87/3332.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[490](https://dblp.org/pid/98/6127.html?view=joint&param=490 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuankai Qi](https://dblp.org/pid/136/5491.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[491](https://dblp.org/pid/98/6127.html?view=joint&param=491 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chengshan Qian](https://dblp.org/pid/133/3243.html)

[\[j29\]](https://dblp.org/pid/98/6127.html#j29)

[492](https://dblp.org/pid/98/6127.html?view=joint&param=492 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jinzhao Qian](https://dblp.org/pid/231/1835.html)

[\[i28\]](https://dblp.org/pid/98/6127.html#i28)

[493](https://dblp.org/pid/98/6127.html?view=joint&param=493 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaoliang Qian](https://dblp.org/pid/31/467.html)

[\[j16\]](https://dblp.org/pid/98/6127.html#j16)

[494](https://dblp.org/pid/98/6127.html?view=joint&param=494 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Junbo Qiao](https://dblp.org/pid/336/2803.html)

[\[j233\]](https://dblp.org/pid/98/6127.html#j233)

[495](https://dblp.org/pid/98/6127.html?view=joint&param=495 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yunan Qiao](https://dblp.org/pid/320/9668.html)

[\[j158\]](https://dblp.org/pid/98/6127.html#j158)

[496](https://dblp.org/pid/98/6127.html?view=joint&param=496 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiajun Qin](https://dblp.org/pid/127/0562.html)

[\[j106\]](https://dblp.org/pid/98/6127.html#j106)

[497](https://dblp.org/pid/98/6127.html?view=joint&param=497 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qi Qin](https://dblp.org/pid/143/4836.html)

[\[j202\]](https://dblp.org/pid/98/6127.html#j202) [\[j142\]](https://dblp.org/pid/98/6127.html#j142)

[498](https://dblp.org/pid/98/6127.html?view=joint&param=498 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhijin Qin](https://dblp.org/pid/157/9149.html)

[\[i91\]](https://dblp.org/pid/98/6127.html#i91) [\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[499](https://dblp.org/pid/98/6127.html?view=joint&param=499 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qiang Qiu 0001](https://dblp.org/pid/97/360-1.html)

[\[j275\]](https://dblp.org/pid/98/6127.html#j275)

[500](https://dblp.org/pid/98/6127.html?view=joint&param=500 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhiyu Qu](https://dblp.org/pid/183/8997.html)

[\[i93\]](https://dblp.org/pid/98/6127.html#i93)

[501](https://dblp.org/pid/98/6127.html?view=joint&param=501 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuming Quan](https://dblp.org/pid/393/1043.html)

[\[c129\]](https://dblp.org/pid/98/6127.html#c129) [\[i67\]](https://dblp.org/pid/98/6127.html#i67)

[502](https://dblp.org/pid/98/6127.html?view=joint&param=502 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Mohammed A. Quddus 0001](https://dblp.org/pid/38/7133.html)

aka: Mohammed Quddus 0001

[\[j146\]](https://dblp.org/pid/98/6127.html#j146)

[503](https://dblp.org/pid/98/6127.html?view=joint&param=503 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Gani Rahmon](https://dblp.org/pid/291/7224.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[504](https://dblp.org/pid/98/6127.html?view=joint&param=504 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Rajiv Ranjan 0001](https://dblp.org/pid/68/163-1.html)

[\[j258\]](https://dblp.org/pid/98/6127.html#j258) [\[j257\]](https://dblp.org/pid/98/6127.html#j257)

[505](https://dblp.org/pid/98/6127.html?view=joint&param=505 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Nikhila Ravi](https://dblp.org/pid/248/7650.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[506](https://dblp.org/pid/98/6127.html?view=joint&param=506 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhaohan Ren](https://dblp.org/pid/305/9069.html)

[\[j125\]](https://dblp.org/pid/98/6127.html#j125)

[507](https://dblp.org/pid/98/6127.html?view=joint&param=507 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Aleksandr Romanov 0001](https://dblp.org/pid/239/5991.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[508](https://dblp.org/pid/98/6127.html?view=joint&param=508 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Paul L. Rosin](https://dblp.org/pid/r/PaulLRosin.html)

[\[c119\]](https://dblp.org/pid/98/6127.html#c119)

[509](https://dblp.org/pid/98/6127.html?view=joint&param=509 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shihai Ruan](https://dblp.org/pid/417/9681.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[510](https://dblp.org/pid/98/6127.html?view=joint&param=510 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yue Ruan](https://dblp.org/pid/117/4718.html)

[\[j64\]](https://dblp.org/pid/98/6127.html#j64)

[511](https://dblp.org/pid/98/6127.html?view=joint&param=511 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dimitrios Sakkos](https://dblp.org/pid/224/7712.html)

[\[j59\]](https://dblp.org/pid/98/6127.html#j59)

[512](https://dblp.org/pid/98/6127.html?view=joint&param=512 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Albert Ali Salah](https://dblp.org/pid/75/4848.html)

[\[c20\]](https://dblp.org/pid/98/6127.html#c20)

[513](https://dblp.org/pid/98/6127.html?view=joint&param=513 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liufang Sang](https://dblp.org/pid/222/7857.html)

[\[c69\]](https://dblp.org/pid/98/6127.html#c69)

[514](https://dblp.org/pid/98/6127.html?view=joint&param=514 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tejal Shah](https://dblp.org/pid/142/7854.html)

[\[j258\]](https://dblp.org/pid/98/6127.html#j258) [\[j257\]](https://dblp.org/pid/98/6127.html#j257)

[515](https://dblp.org/pid/98/6127.html?view=joint&param=515 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Caifeng Shan](https://dblp.org/pid/98/428.html)

[\[j228\]](https://dblp.org/pid/98/6127.html#j228) [\[j203\]](https://dblp.org/pid/98/6127.html#j203) [\[j191\]](https://dblp.org/pid/98/6127.html#j191) [\[j184\]](https://dblp.org/pid/98/6127.html#j184) [\[c103\]](https://dblp.org/pid/98/6127.html#c103) [\[j183\]](https://dblp.org/pid/98/6127.html#j183) [\[j127\]](https://dblp.org/pid/98/6127.html#j127) [\[j126\]](https://dblp.org/pid/98/6127.html#j126) [\[j99\]](https://dblp.org/pid/98/6127.html#j99) [\[j95\]](https://dblp.org/pid/98/6127.html#j95) [\[j83\]](https://dblp.org/pid/98/6127.html#j83) [\[j76\]](https://dblp.org/pid/98/6127.html#j76) [\[e1\]](https://dblp.org/pid/98/6127.html#e1)

[516](https://dblp.org/pid/98/6127.html?view=joint&param=516 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Changjing Shang](https://dblp.org/pid/03/6446.html)

[\[j270\]](https://dblp.org/pid/98/6127.html#j270) [\[j255\]](https://dblp.org/pid/98/6127.html#j255) [\[j216\]](https://dblp.org/pid/98/6127.html#j216)

[517](https://dblp.org/pid/98/6127.html?view=joint&param=517 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hang Shao](https://dblp.org/pid/390/0465.html)

[\[j87\]](https://dblp.org/pid/98/6127.html#j87) [\[c60\]](https://dblp.org/pid/98/6127.html#c60)

[518](https://dblp.org/pid/98/6127.html?view=joint&param=518 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[j250\]](https://dblp.org/pid/98/6127.html#j250) [\[j240\]](https://dblp.org/pid/98/6127.html#j240) [\[j239\]](https://dblp.org/pid/98/6127.html#j239) [\[j231\]](https://dblp.org/pid/98/6127.html#j231) [\[j221\]](https://dblp.org/pid/98/6127.html#j221) [\[j211\]](https://dblp.org/pid/98/6127.html#j211) [\[j207\]](https://dblp.org/pid/98/6127.html#j207) [\[j206\]](https://dblp.org/pid/98/6127.html#j206) [\[j187\]](https://dblp.org/pid/98/6127.html#j187) [\[j169\]](https://dblp.org/pid/98/6127.html#j169) [\[j151\]](https://dblp.org/pid/98/6127.html#j151) [\[j117\]](https://dblp.org/pid/98/6127.html#j117) [\[j108\]](https://dblp.org/pid/98/6127.html#j108) [\[j104\]](https://dblp.org/pid/98/6127.html#j104) [\[j82\]](https://dblp.org/pid/98/6127.html#j82) [\[j79\]](https://dblp.org/pid/98/6127.html#j79) [\[j78\]](https://dblp.org/pid/98/6127.html#j78) [\[j68\]](https://dblp.org/pid/98/6127.html#j68) [\[i21\]](https://dblp.org/pid/98/6127.html#i21) [\[j64\]](https://dblp.org/pid/98/6127.html#j64) [\[j60\]](https://dblp.org/pid/98/6127.html#j60) [\[j59\]](https://dblp.org/pid/98/6127.html#j59) [\[j53\]](https://dblp.org/pid/98/6127.html#j53) [\[j52\]](https://dblp.org/pid/98/6127.html#j52) [\[j50\]](https://dblp.org/pid/98/6127.html#j50) [\[j48\]](https://dblp.org/pid/98/6127.html#j48) [\[j45\]](https://dblp.org/pid/98/6127.html#j45) [\[c46\]](https://dblp.org/pid/98/6127.html#c46) [\[c40\]](https://dblp.org/pid/98/6127.html#c40) [\[i8\]](https://dblp.org/pid/98/6127.html#i8) [\[j38\]](https://dblp.org/pid/98/6127.html#j38) [\[j37\]](https://dblp.org/pid/98/6127.html#j37) [\[j35\]](https://dblp.org/pid/98/6127.html#j35) [\[j34\]](https://dblp.org/pid/98/6127.html#j34) [\[j32\]](https://dblp.org/pid/98/6127.html#j32) [\[c32\]](https://dblp.org/pid/98/6127.html#c32) [\[c29\]](https://dblp.org/pid/98/6127.html#c29) [\[c28\]](https://dblp.org/pid/98/6127.html#c28) [\[i4\]](https://dblp.org/pid/98/6127.html#i4) [\[i1\]](https://dblp.org/pid/98/6127.html#i1) [\[j28\]](https://dblp.org/pid/98/6127.html#j28) [\[j27\]](https://dblp.org/pid/98/6127.html#j27) [\[j25\]](https://dblp.org/pid/98/6127.html#j25) [\[j24\]](https://dblp.org/pid/98/6127.html#j24) [\[j23\]](https://dblp.org/pid/98/6127.html#j23) [\[j22\]](https://dblp.org/pid/98/6127.html#j22) [\[j18\]](https://dblp.org/pid/98/6127.html#j18) [\[j17\]](https://dblp.org/pid/98/6127.html#j17) [\[j16\]](https://dblp.org/pid/98/6127.html#j16) [\[j11\]](https://dblp.org/pid/98/6127.html#j11) [\[j10\]](https://dblp.org/pid/98/6127.html#j10) [\[j5\]](https://dblp.org/pid/98/6127.html#j5)

[519](https://dblp.org/pid/98/6127.html?view=joint&param=519 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shuai Shao](https://dblp.org/pid/71/8201.html)

[\[j258\]](https://dblp.org/pid/98/6127.html#j258) [\[j257\]](https://dblp.org/pid/98/6127.html#j257)

[520](https://dblp.org/pid/98/6127.html?view=joint&param=520 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenqi Shao](https://dblp.org/pid/227/3122.html)

[\[c99\]](https://dblp.org/pid/98/6127.html#c99) [\[i57\]](https://dblp.org/pid/98/6127.html#i57)

[521](https://dblp.org/pid/98/6127.html?view=joint&param=521 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhuang Shao](https://dblp.org/pid/51/9057.html)

[\[j222\]](https://dblp.org/pid/98/6127.html#j222) [\[j190\]](https://dblp.org/pid/98/6127.html#j190) [\[j164\]](https://dblp.org/pid/98/6127.html#j164)

[522](https://dblp.org/pid/98/6127.html?view=joint&param=522 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiashuai She](https://dblp.org/pid/421/9070.html)

[\[i88\]](https://dblp.org/pid/98/6127.html#i88)

[523](https://dblp.org/pid/98/6127.html?view=joint&param=523 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fumin Shen](https://dblp.org/pid/92/10934.html)

[\[j35\]](https://dblp.org/pid/98/6127.html#j35) [\[c32\]](https://dblp.org/pid/98/6127.html#c32) [\[i4\]](https://dblp.org/pid/98/6127.html#i4)

[524](https://dblp.org/pid/98/6127.html?view=joint&param=524 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jialie Shen 0001](https://dblp.org/pid/33/7046.html)

[\[c39\]](https://dblp.org/pid/98/6127.html#c39) [\[c29\]](https://dblp.org/pid/98/6127.html#c29) [\[c28\]](https://dblp.org/pid/98/6127.html#c28)

[525](https://dblp.org/pid/98/6127.html?view=joint&param=525 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Leqi Shen](https://dblp.org/pid/323/9555.html)

[\[j219\]](https://dblp.org/pid/98/6127.html#j219) [\[c125\]](https://dblp.org/pid/98/6127.html#c125) [\[c124\]](https://dblp.org/pid/98/6127.html#c124) [\[i102\]](https://dblp.org/pid/98/6127.html#i102) [\[i99\]](https://dblp.org/pid/98/6127.html#i99)

[526](https://dblp.org/pid/98/6127.html?view=joint&param=526 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[LinLin Shen](https://dblp.org/pid/88/5607.html)

aka: Linlin Shen

[\[j29\]](https://dblp.org/pid/98/6127.html#j29)

[527](https://dblp.org/pid/98/6127.html?view=joint&param=527 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qiang Shen 0001](https://dblp.org/pid/s/QiangShen.html)

[\[j277\]](https://dblp.org/pid/98/6127.html#j277) [\[j270\]](https://dblp.org/pid/98/6127.html#j270) [\[j255\]](https://dblp.org/pid/98/6127.html#j255) [\[j216\]](https://dblp.org/pid/98/6127.html#j216) [\[j182\]](https://dblp.org/pid/98/6127.html#j182) [\[j168\]](https://dblp.org/pid/98/6127.html#j168) [\[j155\]](https://dblp.org/pid/98/6127.html#j155) [\[j154\]](https://dblp.org/pid/98/6127.html#j154) [\[c88\]](https://dblp.org/pid/98/6127.html#c88)

[528](https://dblp.org/pid/98/6127.html?view=joint&param=528 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yunhang Shen](https://dblp.org/pid/146/1800.html)

[\[i59\]](https://dblp.org/pid/98/6127.html#i59)

[529](https://dblp.org/pid/98/6127.html?view=joint&param=529 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haohan Shi](https://dblp.org/pid/361/2593.html)

[\[i116\]](https://dblp.org/pid/98/6127.html#i116)

[530](https://dblp.org/pid/98/6127.html?view=joint&param=530 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liangtao Shi](https://dblp.org/pid/366/5426.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[531](https://dblp.org/pid/98/6127.html?view=joint&param=531 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tao Shi](https://dblp.org/pid/42/1958.html)

[\[j57\]](https://dblp.org/pid/98/6127.html#j57)

[532](https://dblp.org/pid/98/6127.html?view=joint&param=532 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jamie Shotton](https://dblp.org/pid/47/572.html)

[\[j11\]](https://dblp.org/pid/98/6127.html#j11) [\[j10\]](https://dblp.org/pid/98/6127.html#j10)

[533](https://dblp.org/pid/98/6127.html?view=joint&param=533 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaochuang Shu](https://dblp.org/pid/325/3814.html)

[\[j138\]](https://dblp.org/pid/98/6127.html#j138)

[534](https://dblp.org/pid/98/6127.html?view=joint&param=534 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hubert P. H. Shum](https://dblp.org/pid/14/4870.html)

[\[j48\]](https://dblp.org/pid/98/6127.html#j48)

[535](https://dblp.org/pid/98/6127.html?view=joint&param=535 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Mennatullah Siam](https://dblp.org/pid/163/9048.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[536](https://dblp.org/pid/98/6127.html?view=joint&param=536 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Leonid Sigal](https://dblp.org/pid/09/4991.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[537](https://dblp.org/pid/98/6127.html?view=joint&param=537 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Amit Kumar Singh 0001](https://dblp.org/pid/10/7647-1.html)

[\[j243\]](https://dblp.org/pid/98/6127.html#j243)

[538](https://dblp.org/pid/98/6127.html?view=joint&param=538 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Alexander Sinitsyn](https://dblp.org/pid/06/4648.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[539](https://dblp.org/pid/98/6127.html?view=joint&param=539 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Arun Kumar Sivapuram](https://dblp.org/pid/344/4532.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[540](https://dblp.org/pid/98/6127.html?view=joint&param=540 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Cees Snoek](https://dblp.org/pid/s/CeesSnoek.html)

aka: Cees G. M. Snoek

[\[j108\]](https://dblp.org/pid/98/6127.html#j108) [\[i21\]](https://dblp.org/pid/98/6127.html#i21) [\[c46\]](https://dblp.org/pid/98/6127.html#c46) [\[i8\]](https://dblp.org/pid/98/6127.html#i8)

[541](https://dblp.org/pid/98/6127.html?view=joint&param=541 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Roman A. Solovyev](https://dblp.org/pid/163/3390.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[542](https://dblp.org/pid/98/6127.html?view=joint&param=542 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Elham Soltanikazemi](https://dblp.org/pid/318/1851.html)

aka: Elham Soltani Kazemi

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[543](https://dblp.org/pid/98/6127.html?view=joint&param=543 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jifei Song](https://dblp.org/pid/198/2576.html)

[\[i93\]](https://dblp.org/pid/98/6127.html#i93)

[544](https://dblp.org/pid/98/6127.html?view=joint&param=544 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ke Song 0003](https://dblp.org/pid/194/3688-3.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[545](https://dblp.org/pid/98/6127.html?view=joint&param=545 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lin Song 0002](https://dblp.org/pid/49/1217-2.html)

[\[i61\]](https://dblp.org/pid/98/6127.html#i61)

[546](https://dblp.org/pid/98/6127.html?view=joint&param=546 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhanjie Song](https://dblp.org/pid/31/5015.html)

[\[j72\]](https://dblp.org/pid/98/6127.html#j72)

[547](https://dblp.org/pid/98/6127.html?view=joint&param=547 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ravi Soni](https://dblp.org/pid/249/3157.html)

[\[j131\]](https://dblp.org/pid/98/6127.html#j131)

[548](https://dblp.org/pid/98/6127.html?view=joint&param=548 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jinya Su](https://dblp.org/pid/131/9643.html)

[\[j146\]](https://dblp.org/pid/98/6127.html#j146)

[549](https://dblp.org/pid/98/6127.html?view=joint&param=549 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ruisheng Su](https://dblp.org/pid/258/3495.html)

[\[j181\]](https://dblp.org/pid/98/6127.html#j181)

[550](https://dblp.org/pid/98/6127.html?view=joint&param=550 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiangbo Su](https://dblp.org/pid/188/7852.html)

[\[i10\]](https://dblp.org/pid/98/6127.html#i10)

[551](https://dblp.org/pid/98/6127.html?view=joint&param=551 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yimu Su](https://dblp.org/pid/342/3338.html)

[\[j235\]](https://dblp.org/pid/98/6127.html#j235) [\[i81\]](https://dblp.org/pid/98/6127.html#i81)

[552](https://dblp.org/pid/98/6127.html?view=joint&param=552 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhenpeng Su](https://dblp.org/pid/348/9741.html)

[\[c128\]](https://dblp.org/pid/98/6127.html#c128) [\[c123\]](https://dblp.org/pid/98/6127.html#c123) [\[c122\]](https://dblp.org/pid/98/6127.html#c122) [\[i115\]](https://dblp.org/pid/98/6127.html#i115) [\[i114\]](https://dblp.org/pid/98/6127.html#i114) [\[i113\]](https://dblp.org/pid/98/6127.html#i113)

[553](https://dblp.org/pid/98/6127.html?view=joint&param=553 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fengyuan Sun](https://dblp.org/pid/147/6919.html)

[\[c124\]](https://dblp.org/pid/98/6127.html#c124) [\[i102\]](https://dblp.org/pid/98/6127.html#i102) [\[i89\]](https://dblp.org/pid/98/6127.html#i89) [\[i63\]](https://dblp.org/pid/98/6127.html#i63)

[554](https://dblp.org/pid/98/6127.html?view=joint&param=554 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hanqing Sun 0001](https://dblp.org/pid/228/6382-1.html)

[\[j213\]](https://dblp.org/pid/98/6127.html#j213) [\[j72\]](https://dblp.org/pid/98/6127.html#j72)

[555](https://dblp.org/pid/98/6127.html?view=joint&param=555 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jian Sun 0001](https://dblp.org/pid/68/4942-1.html)

[\[i49\]](https://dblp.org/pid/98/6127.html#i49) [\[c84\]](https://dblp.org/pid/98/6127.html#c84) [\[i38\]](https://dblp.org/pid/98/6127.html#i38)

[556](https://dblp.org/pid/98/6127.html?view=joint&param=556 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liye Sun](https://dblp.org/pid/150/6663.html)

[\[j18\]](https://dblp.org/pid/98/6127.html#j18)

[557](https://dblp.org/pid/98/6127.html?view=joint&param=557 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Mingming Sun 0001](https://dblp.org/pid/87/8665-1.html)

[\[i77\]](https://dblp.org/pid/98/6127.html#i77)

[558](https://dblp.org/pid/98/6127.html?view=joint&param=558 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaoyan Sun 0001](https://dblp.org/pid/13/1574-1.html)

[\[c3\]](https://dblp.org/pid/98/6127.html#c3)

[559](https://dblp.org/pid/98/6127.html?view=joint&param=559 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Sun](https://dblp.org/pid/20/3535.html)

[\[j264\]](https://dblp.org/pid/98/6127.html#j264)

[560](https://dblp.org/pid/98/6127.html?view=joint&param=560 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Sun 0021](https://dblp.org/pid/20/3535-21.html)

[\[j238\]](https://dblp.org/pid/98/6127.html#j238) [\[i118\]](https://dblp.org/pid/98/6127.html#i118) [\[i116\]](https://dblp.org/pid/98/6127.html#i116) [\[i97\]](https://dblp.org/pid/98/6127.html#i97)

[561](https://dblp.org/pid/98/6127.html?view=joint&param=561 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yunxin Sun 0002](https://dblp.org/pid/200/7880-2.html)

[\[i12\]](https://dblp.org/pid/98/6127.html#i12)

[562](https://dblp.org/pid/98/6127.html?view=joint&param=562 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuxin Sun](https://dblp.org/pid/158/7549.html)

[\[j91\]](https://dblp.org/pid/98/6127.html#j91)

[563](https://dblp.org/pid/98/6127.html?view=joint&param=563 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kenji Suzuki 0001](https://dblp.org/pid/99/5441-1.html)

[\[j20\]](https://dblp.org/pid/98/6127.html#j20)

[564](https://dblp.org/pid/98/6127.html?view=joint&param=564 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Muhammad Atif Tahir](https://dblp.org/pid/73/1942.html)

[\[c88\]](https://dblp.org/pid/98/6127.html#c88)

[565](https://dblp.org/pid/98/6127.html?view=joint&param=565 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jianchao Tan](https://dblp.org/pid/165/9938.html)

[\[i64\]](https://dblp.org/pid/98/6127.html#i64) [\[c83\]](https://dblp.org/pid/98/6127.html#c83)

[566](https://dblp.org/pid/98/6127.html?view=joint&param=566 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shoubiao Tan](https://dblp.org/pid/64/7731.html)

[\[j53\]](https://dblp.org/pid/98/6127.html#j53)

[567](https://dblp.org/pid/98/6127.html?view=joint&param=567 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tao Tan 0002](https://dblp.org/pid/06/7832-2.html)

[\[i104\]](https://dblp.org/pid/98/6127.html#i104) [\[j181\]](https://dblp.org/pid/98/6127.html#j181) [\[j131\]](https://dblp.org/pid/98/6127.html#j131) [\[j127\]](https://dblp.org/pid/98/6127.html#j127)

[568](https://dblp.org/pid/98/6127.html?view=joint&param=568 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Sheng Tang](https://dblp.org/pid/62/1647.html)

[\[c49\]](https://dblp.org/pid/98/6127.html#c49) [\[c48\]](https://dblp.org/pid/98/6127.html#c48)

[569](https://dblp.org/pid/98/6127.html?view=joint&param=569 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenbo Tang](https://dblp.org/pid/219/1693.html)

[\[i72\]](https://dblp.org/pid/98/6127.html#i72)

[570](https://dblp.org/pid/98/6127.html?view=joint&param=570 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yongliang Tang](https://dblp.org/pid/201/0244.html)

[\[c129\]](https://dblp.org/pid/98/6127.html#c129) [\[i67\]](https://dblp.org/pid/98/6127.html#i67)

[571](https://dblp.org/pid/98/6127.html?view=joint&param=571 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Youbao Tang](https://dblp.org/pid/20/8578.html)

[\[j100\]](https://dblp.org/pid/98/6127.html#j100)

[572](https://dblp.org/pid/98/6127.html?view=joint&param=572 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhanyong Tang](https://dblp.org/pid/38/7487.html)

[\[j92\]](https://dblp.org/pid/98/6127.html#j92)

[573](https://dblp.org/pid/98/6127.html?view=joint&param=573 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dacheng Tao](https://dblp.org/pid/46/3391.html)

[\[j63\]](https://dblp.org/pid/98/6127.html#j63) [\[i6\]](https://dblp.org/pid/98/6127.html#i6)

[574](https://dblp.org/pid/98/6127.html?view=joint&param=574 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Keda Tao](https://dblp.org/pid/380/6968.html)

[\[j206\]](https://dblp.org/pid/98/6127.html#j206)

[575](https://dblp.org/pid/98/6127.html?view=joint&param=575 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tao Tao 0005](https://dblp.org/pid/73/3197-5.html)

[\[j177\]](https://dblp.org/pid/98/6127.html#j177) [\[i22\]](https://dblp.org/pid/98/6127.html#i22) [\[j85\]](https://dblp.org/pid/98/6127.html#j85)

[576](https://dblp.org/pid/98/6127.html?view=joint&param=576 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Martijn Thijssen](https://dblp.org/pid/72/5570.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[577](https://dblp.org/pid/98/6127.html?view=joint&param=577 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haibin Tian](https://dblp.org/pid/280/1349.html)

[\[j159\]](https://dblp.org/pid/98/6127.html#j159) [\[i37\]](https://dblp.org/pid/98/6127.html#i37) [\[i34\]](https://dblp.org/pid/98/6127.html#i34) [\[c74\]](https://dblp.org/pid/98/6127.html#c74)

[578](https://dblp.org/pid/98/6127.html?view=joint&param=578 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tianhui Tian](https://dblp.org/pid/380/6771.html)

[\[j206\]](https://dblp.org/pid/98/6127.html#j206)

[579](https://dblp.org/pid/98/6127.html?view=joint&param=579 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wei Tian 0001](https://dblp.org/pid/56/3860-1.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[580](https://dblp.org/pid/98/6127.html?view=joint&param=580 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bernard Tiddeman](https://dblp.org/pid/37/5442.html)

aka: Bernie Tiddeman

[\[j256\]](https://dblp.org/pid/98/6127.html#j256)

[581](https://dblp.org/pid/98/6127.html?view=joint&param=581 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Pavel Tokmakov](https://dblp.org/pid/153/2264.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[582](https://dblp.org/pid/98/6127.html?view=joint&param=582 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[583](https://dblp.org/pid/98/6127.html?view=joint&param=583 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Imad Eddine Toubal](https://dblp.org/pid/292/6360.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[584](https://dblp.org/pid/98/6127.html?view=joint&param=584 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Khanh-Tung Tran](https://dblp.org/pid/359/3793.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[585](https://dblp.org/pid/98/6127.html?view=joint&param=585 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Nuno Vasconcelos](https://dblp.org/pid/78/4806.html)

[\[j28\]](https://dblp.org/pid/98/6127.html#j28)

[586](https://dblp.org/pid/98/6127.html?view=joint&param=586 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Julien A. Vijverberg](https://dblp.org/pid/52/7249.html)

[\[c13\]](https://dblp.org/pid/98/6127.html#c13)

[587](https://dblp.org/pid/98/6127.html?view=joint&param=587 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Stefanos Vrochidis](https://dblp.org/pid/44/6029.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[588](https://dblp.org/pid/98/6127.html?view=joint&param=588 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xuan-Son Vu](https://dblp.org/pid/151/8673.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[589](https://dblp.org/pid/98/6127.html?view=joint&param=589 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jia Wan 0001](https://dblp.org/pid/13/6504-1.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[590](https://dblp.org/pid/98/6127.html?view=joint&param=590 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ao Wang](https://dblp.org/pid/87/3443.html)

[\[j271\]](https://dblp.org/pid/98/6127.html#j271) [\[c129\]](https://dblp.org/pid/98/6127.html#c129) [\[c126\]](https://dblp.org/pid/98/6127.html#c126) [\[i111\]](https://dblp.org/pid/98/6127.html#i111) [\[i107\]](https://dblp.org/pid/98/6127.html#i107) [\[c115\]](https://dblp.org/pid/98/6127.html#c115) [\[c105\]](https://dblp.org/pid/98/6127.html#c105) [\[i78\]](https://dblp.org/pid/98/6127.html#i78) [\[i67\]](https://dblp.org/pid/98/6127.html#i67) [\[i64\]](https://dblp.org/pid/98/6127.html#i64) [\[i63\]](https://dblp.org/pid/98/6127.html#i63) [\[i61\]](https://dblp.org/pid/98/6127.html#i61) [\[c101\]](https://dblp.org/pid/98/6127.html#c101) [\[i56\]](https://dblp.org/pid/98/6127.html#i56) [\[i54\]](https://dblp.org/pid/98/6127.html#i54)

[591](https://dblp.org/pid/98/6127.html?view=joint&param=591 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bin Wang 0021](https://dblp.org/pid/13/1898-21.html)

[\[c61\]](https://dblp.org/pid/98/6127.html#c61) [\[c38\]](https://dblp.org/pid/98/6127.html#c38) [\[c37\]](https://dblp.org/pid/98/6127.html#c37)

[592](https://dblp.org/pid/98/6127.html?view=joint&param=592 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bing Wang 0018](https://dblp.org/pid/06/1909-18.html)

[\[j261\]](https://dblp.org/pid/98/6127.html#j261)

[593](https://dblp.org/pid/98/6127.html?view=joint&param=593 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bo Wang 0011](https://dblp.org/pid/72/6811-11.html)

[\[j174\]](https://dblp.org/pid/98/6127.html#j174) [\[j160\]](https://dblp.org/pid/98/6127.html#j160) [\[i48\]](https://dblp.org/pid/98/6127.html#i48) [\[i35\]](https://dblp.org/pid/98/6127.html#i35)

[594](https://dblp.org/pid/98/6127.html?view=joint&param=594 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dongyang Wang](https://dblp.org/pid/137/0229.html)

[\[j16\]](https://dblp.org/pid/98/6127.html#j16)

[595](https://dblp.org/pid/98/6127.html?view=joint&param=595 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fan Wang](https://dblp.org/pid/88/898.html)

[\[j119\]](https://dblp.org/pid/98/6127.html#j119) [\[j57\]](https://dblp.org/pid/98/6127.html#j57)

[596](https://dblp.org/pid/98/6127.html?view=joint&param=596 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Gerong Wang](https://dblp.org/pid/289/1259.html)

[\[j174\]](https://dblp.org/pid/98/6127.html#j174) [\[j160\]](https://dblp.org/pid/98/6127.html#j160) [\[i48\]](https://dblp.org/pid/98/6127.html#i48) [\[i35\]](https://dblp.org/pid/98/6127.html#i35)

[597](https://dblp.org/pid/98/6127.html?view=joint&param=597 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Guoxin Wang](https://dblp.org/pid/05/1182.html)

[\[j230\]](https://dblp.org/pid/98/6127.html#j230) [\[c108\]](https://dblp.org/pid/98/6127.html#c108) [\[c107\]](https://dblp.org/pid/98/6127.html#c107) [\[i84\]](https://dblp.org/pid/98/6127.html#i84)

[598](https://dblp.org/pid/98/6127.html?view=joint&param=598 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hainan Wang](https://dblp.org/pid/54/10365.html)

[\[c22\]](https://dblp.org/pid/98/6127.html#c22)

[599](https://dblp.org/pid/98/6127.html?view=joint&param=599 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haoran Wang 0004](https://dblp.org/pid/28/3021-4.html)

[\[c106\]](https://dblp.org/pid/98/6127.html#c106) [\[i77\]](https://dblp.org/pid/98/6127.html#i77) [\[j140\]](https://dblp.org/pid/98/6127.html#j140) [\[c92\]](https://dblp.org/pid/98/6127.html#c92) [\[c90\]](https://dblp.org/pid/98/6127.html#c90) [\[i45\]](https://dblp.org/pid/98/6127.html#i45) [\[i44\]](https://dblp.org/pid/98/6127.html#i44) [\[c65\]](https://dblp.org/pid/98/6127.html#c65) [\[i19\]](https://dblp.org/pid/98/6127.html#i19)

[600](https://dblp.org/pid/98/6127.html?view=joint&param=600 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jialiang Wang](https://dblp.org/pid/27/8578.html)

[\[j267\]](https://dblp.org/pid/98/6127.html#j267) [\[j141\]](https://dblp.org/pid/98/6127.html#j141)

[601](https://dblp.org/pid/98/6127.html?view=joint&param=601 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jian Wang 0087](https://dblp.org/pid/39/449-87.html)

[\[j69\]](https://dblp.org/pid/98/6127.html#j69)

[602](https://dblp.org/pid/98/6127.html?view=joint&param=602 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jianmin Wang 0001](https://dblp.org/pid/06/3456-1.html)

[\[j36\]](https://dblp.org/pid/98/6127.html#j36)

[603](https://dblp.org/pid/98/6127.html?view=joint&param=603 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiaqi Wang](https://dblp.org/pid/44/740.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[604](https://dblp.org/pid/98/6127.html?view=joint&param=604 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiaxing Wang](https://dblp.org/pid/118/4638.html)

[\[j230\]](https://dblp.org/pid/98/6127.html#j230)

[605](https://dblp.org/pid/98/6127.html?view=joint&param=605 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jie Wang](https://dblp.org/pid/29/5259.html)

[\[j55\]](https://dblp.org/pid/98/6127.html#j55)

[606](https://dblp.org/pid/98/6127.html?view=joint&param=606 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jing Wang 0136](https://dblp.org/pid/02/736-136.html)

[\[j128\]](https://dblp.org/pid/98/6127.html#j128)

[607](https://dblp.org/pid/98/6127.html?view=joint&param=607 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jingyi Wang](https://dblp.org/pid/18/3178.html)

[\[j253\]](https://dblp.org/pid/98/6127.html#j253)

[608](https://dblp.org/pid/98/6127.html?view=joint&param=608 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Junyue Wang](https://dblp.org/pid/236/0369.html)

[\[j84\]](https://dblp.org/pid/98/6127.html#j84)

[609](https://dblp.org/pid/98/6127.html?view=joint&param=609 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lei Wang 0018](https://dblp.org/pid/w/LeiWang18.html)

[\[j29\]](https://dblp.org/pid/98/6127.html#j29)

[610](https://dblp.org/pid/98/6127.html?view=joint&param=610 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lianjie Wang](https://dblp.org/pid/18/2688.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[611](https://dblp.org/pid/98/6127.html?view=joint&param=611 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liejun Wang](https://dblp.org/pid/116/7864.html)

[\[c114\]](https://dblp.org/pid/98/6127.html#c114) [\[i71\]](https://dblp.org/pid/98/6127.html#i71)

[612](https://dblp.org/pid/98/6127.html?view=joint&param=612 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[j275\]](https://dblp.org/pid/98/6127.html#j275) [\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[613](https://dblp.org/pid/98/6127.html?view=joint&param=613 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lin Wang](https://dblp.org/pid/17/6729.html)

[\[j86\]](https://dblp.org/pid/98/6127.html#j86) [\[j61\]](https://dblp.org/pid/98/6127.html#j61)

[614](https://dblp.org/pid/98/6127.html?view=joint&param=614 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Long Wang 0001](https://dblp.org/pid/68/4459-1.html)

[\[j71\]](https://dblp.org/pid/98/6127.html#j71) [\[j62\]](https://dblp.org/pid/98/6127.html#j62)

[615](https://dblp.org/pid/98/6127.html?view=joint&param=615 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qiang Wang 0051](https://dblp.org/pid/64/5630-51.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[616](https://dblp.org/pid/98/6127.html?view=joint&param=616 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qiang Wang 0056](https://dblp.org/pid/64/5630-56.html)

[\[j224\]](https://dblp.org/pid/98/6127.html#j224)

[617](https://dblp.org/pid/98/6127.html?view=joint&param=617 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qianqian Wang 0001](https://dblp.org/pid/118/6735-1.html)

[\[j199\]](https://dblp.org/pid/98/6127.html#j199)

[618](https://dblp.org/pid/98/6127.html?view=joint&param=618 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qixiong Wang](https://dblp.org/pid/285/7078.html)

[\[c99\]](https://dblp.org/pid/98/6127.html#c99) [\[i57\]](https://dblp.org/pid/98/6127.html#i57)

[619](https://dblp.org/pid/98/6127.html?view=joint&param=619 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Runqi Wang](https://dblp.org/pid/266/9915.html)

[\[j223\]](https://dblp.org/pid/98/6127.html#j223)

[620](https://dblp.org/pid/98/6127.html?view=joint&param=620 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Sen Wang](https://dblp.org/pid/69/6403.html)

[\[j153\]](https://dblp.org/pid/98/6127.html#j153)

[621](https://dblp.org/pid/98/6127.html?view=joint&param=621 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shanwen Wang](https://dblp.org/pid/331/7051.html)

[\[j238\]](https://dblp.org/pid/98/6127.html#j238) [\[i118\]](https://dblp.org/pid/98/6127.html#i118)

[622](https://dblp.org/pid/98/6127.html?view=joint&param=622 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shujian Wang](https://dblp.org/pid/37/1991.html)

[\[c58\]](https://dblp.org/pid/98/6127.html#c58) [\[c51\]](https://dblp.org/pid/98/6127.html#c51)

[623](https://dblp.org/pid/98/6127.html?view=joint&param=623 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wei Wang 0016](https://dblp.org/pid/w/WeiWang16.html)

[\[j50\]](https://dblp.org/pid/98/6127.html#j50) [\[i1\]](https://dblp.org/pid/98/6127.html#i1)

[624](https://dblp.org/pid/98/6127.html?view=joint&param=624 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenhao Wang](https://dblp.org/pid/57/9813.html)

[\[j203\]](https://dblp.org/pid/98/6127.html#j203) [\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[625](https://dblp.org/pid/98/6127.html?view=joint&param=625 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenjin Wang 0002](https://dblp.org/pid/61/4908-2.html)

[\[j181\]](https://dblp.org/pid/98/6127.html#j181)

[626](https://dblp.org/pid/98/6127.html?view=joint&param=626 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaodi Wang](https://dblp.org/pid/07/8227.html)

[\[j223\]](https://dblp.org/pid/98/6127.html#j223) [\[c53\]](https://dblp.org/pid/98/6127.html#c53) [\[c45\]](https://dblp.org/pid/98/6127.html#c45)

[627](https://dblp.org/pid/98/6127.html?view=joint&param=627 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Wang 0121](https://dblp.org/pid/10/5630-121.html)

[\[j181\]](https://dblp.org/pid/98/6127.html#j181)

[628](https://dblp.org/pid/98/6127.html?view=joint&param=628 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xinshuo Wang](https://dblp.org/pid/208/4029.html)

[\[j231\]](https://dblp.org/pid/98/6127.html#j231) [\[j221\]](https://dblp.org/pid/98/6127.html#j221) [\[i65\]](https://dblp.org/pid/98/6127.html#i65)

[629](https://dblp.org/pid/98/6127.html?view=joint&param=629 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xinying Wang 0005](https://dblp.org/pid/06/3244-5.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[630](https://dblp.org/pid/98/6127.html?view=joint&param=630 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xuan Wang 0016](https://dblp.org/pid/34/4799-16.html)

[\[j194\]](https://dblp.org/pid/98/6127.html#j194) [\[c113\]](https://dblp.org/pid/98/6127.html#c113)

[631](https://dblp.org/pid/98/6127.html?view=joint&param=631 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yaodong Wang](https://dblp.org/pid/28/8544.html)

[\[j197\]](https://dblp.org/pid/98/6127.html#j197)

[632](https://dblp.org/pid/98/6127.html?view=joint&param=632 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yaowei Wang 0001](https://dblp.org/pid/68/2992-1.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110) [\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[633](https://dblp.org/pid/98/6127.html?view=joint&param=633 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yizhou Wang 0001](https://dblp.org/pid/71/3387-1.html)

[\[j94\]](https://dblp.org/pid/98/6127.html#j94)

[634](https://dblp.org/pid/98/6127.html?view=joint&param=634 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[635](https://dblp.org/pid/98/6127.html?view=joint&param=635 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yu-Xiong Wang](https://dblp.org/pid/35/10700.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[636](https://dblp.org/pid/98/6127.html?view=joint&param=636 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ze Wang 0008](https://dblp.org/pid/35/6674-8.html)

[\[j97\]](https://dblp.org/pid/98/6127.html#j97) [\[i11\]](https://dblp.org/pid/98/6127.html#i11)

[637](https://dblp.org/pid/98/6127.html?view=joint&param=637 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zerun Wang](https://dblp.org/pid/260/7013.html)

[\[c97\]](https://dblp.org/pid/98/6127.html#c97) [\[i28\]](https://dblp.org/pid/98/6127.html#i28)

[638](https://dblp.org/pid/98/6127.html?view=joint&param=638 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhao Wang](https://dblp.org/pid/86/981.html)

[\[j245\]](https://dblp.org/pid/98/6127.html#j245) [\[j242\]](https://dblp.org/pid/98/6127.html#j242)

[639](https://dblp.org/pid/98/6127.html?view=joint&param=639 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zheng Wang 0001](https://dblp.org/pid/w/ZhengWang1.html)

[\[j92\]](https://dblp.org/pid/98/6127.html#j92) [\[c72\]](https://dblp.org/pid/98/6127.html#c72)

[640](https://dblp.org/pid/98/6127.html?view=joint&param=640 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhihao Wang](https://dblp.org/pid/52/253.html)

[\[c92\]](https://dblp.org/pid/98/6127.html#c92) [\[i45\]](https://dblp.org/pid/98/6127.html#i45)

[641](https://dblp.org/pid/98/6127.html?view=joint&param=641 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhilong Wang 0001](https://dblp.org/pid/70/7765-1.html)

[\[j234\]](https://dblp.org/pid/98/6127.html#j234)

[642](https://dblp.org/pid/98/6127.html?view=joint&param=642 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhiquan Wang](https://dblp.org/pid/18/5129.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[643](https://dblp.org/pid/98/6127.html?view=joint&param=643 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zixi Wang](https://dblp.org/pid/67/3752.html)

[\[j124\]](https://dblp.org/pid/98/6127.html#j124)

[644](https://dblp.org/pid/98/6127.html?view=joint&param=644 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Cuicui Wei](https://dblp.org/pid/208/0154.html)

[\[j39\]](https://dblp.org/pid/98/6127.html#j39)

[645](https://dblp.org/pid/98/6127.html?view=joint&param=645 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Rongshuai Wei](https://dblp.org/pid/409/7340.html)

[\[j262\]](https://dblp.org/pid/98/6127.html#j262) [\[i101\]](https://dblp.org/pid/98/6127.html#i101)

[646](https://dblp.org/pid/98/6127.html?view=joint&param=646 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yunchao Wei](https://dblp.org/pid/118/5394.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[647](https://dblp.org/pid/98/6127.html?view=joint&param=647 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Longyin Wen](https://dblp.org/pid/119/1468.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[648](https://dblp.org/pid/98/6127.html?view=joint&param=648 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Peter H. N. de With](https://dblp.org/pid/w/PeterHNdeWith.html)

[\[j13\]](https://dblp.org/pid/98/6127.html#j13) [\[j9\]](https://dblp.org/pid/98/6127.html#j9) [\[j8\]](https://dblp.org/pid/98/6127.html#j8) [\[j7\]](https://dblp.org/pid/98/6127.html#j7) [\[j6\]](https://dblp.org/pid/98/6127.html#j6) [\[j5\]](https://dblp.org/pid/98/6127.html#j5) [\[j4\]](https://dblp.org/pid/98/6127.html#j4) [\[j3\]](https://dblp.org/pid/98/6127.html#j3) [\[c17\]](https://dblp.org/pid/98/6127.html#c17) [\[j2\]](https://dblp.org/pid/98/6127.html#j2) [\[c16\]](https://dblp.org/pid/98/6127.html#c16) [\[c15\]](https://dblp.org/pid/98/6127.html#c15) [\[c14\]](https://dblp.org/pid/98/6127.html#c14) [\[c13\]](https://dblp.org/pid/98/6127.html#c13) [\[c12\]](https://dblp.org/pid/98/6127.html#c12) [\[c11\]](https://dblp.org/pid/98/6127.html#c11) [\[c10\]](https://dblp.org/pid/98/6127.html#c10) [\[c9\]](https://dblp.org/pid/98/6127.html#c9) [\[j1\]](https://dblp.org/pid/98/6127.html#j1) [\[c8\]](https://dblp.org/pid/98/6127.html#c8) [\[c7\]](https://dblp.org/pid/98/6127.html#c7) [\[c6\]](https://dblp.org/pid/98/6127.html#c6) [\[c5\]](https://dblp.org/pid/98/6127.html#c5) [\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[649](https://dblp.org/pid/98/6127.html?view=joint&param=649 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chengjing Wu](https://dblp.org/pid/379/5986.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[650](https://dblp.org/pid/98/6127.html?view=joint&param=650 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Feng Wu 0001](https://dblp.org/pid/25/3972-1.html)

[\[j13\]](https://dblp.org/pid/98/6127.html#j13) [\[c3\]](https://dblp.org/pid/98/6127.html#c3)

[651](https://dblp.org/pid/98/6127.html?view=joint&param=651 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[652](https://dblp.org/pid/98/6127.html?view=joint&param=652 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Gengshen Wu](https://dblp.org/pid/204/2949.html)

[\[j276\]](https://dblp.org/pid/98/6127.html#j276) [\[j266\]](https://dblp.org/pid/98/6127.html#j266) [\[j229\]](https://dblp.org/pid/98/6127.html#j229) [\[i91\]](https://dblp.org/pid/98/6127.html#i91) [\[i90\]](https://dblp.org/pid/98/6127.html#i90) [\[j192\]](https://dblp.org/pid/98/6127.html#j192) [\[j93\]](https://dblp.org/pid/98/6127.html#j93) [\[j70\]](https://dblp.org/pid/98/6127.html#j70) [\[j68\]](https://dblp.org/pid/98/6127.html#j68) [\[c39\]](https://dblp.org/pid/98/6127.html#c39) [\[c29\]](https://dblp.org/pid/98/6127.html#c29)

[653](https://dblp.org/pid/98/6127.html?view=joint&param=653 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haotian Wu 0006](https://dblp.org/pid/145/5323-6.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[654](https://dblp.org/pid/98/6127.html?view=joint&param=654 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiahe Wu](https://dblp.org/pid/253/0589.html)

[\[j197\]](https://dblp.org/pid/98/6127.html#j197)

[655](https://dblp.org/pid/98/6127.html?view=joint&param=655 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Junde Wu](https://dblp.org/pid/39/2439.html)

[\[j272\]](https://dblp.org/pid/98/6127.html#j272)

[656](https://dblp.org/pid/98/6127.html?view=joint&param=656 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lin Wu 0001](https://dblp.org/pid/65/6292-1.html)

aka: Lin Yuanbo Wu

[\[j261\]](https://dblp.org/pid/98/6127.html#j261)

[657](https://dblp.org/pid/98/6127.html?view=joint&param=657 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Meng Wymond Wu](https://dblp.org/pid/379/4809.html)

[\[i77\]](https://dblp.org/pid/98/6127.html#i77)

[658](https://dblp.org/pid/98/6127.html?view=joint&param=658 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qiangqiang Wu](https://dblp.org/pid/193/1415.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[659](https://dblp.org/pid/98/6127.html?view=joint&param=659 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Sihang Wu](https://dblp.org/pid/234/0006.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[660](https://dblp.org/pid/98/6127.html?view=joint&param=660 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenhao Wu](https://dblp.org/pid/149/0005.html)

[\[c92\]](https://dblp.org/pid/98/6127.html#c92) [\[i45\]](https://dblp.org/pid/98/6127.html#i45)

[661](https://dblp.org/pid/98/6127.html?view=joint&param=661 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[662](https://dblp.org/pid/98/6127.html?view=joint&param=662 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xuangou Wu](https://dblp.org/pid/133/0466.html)

[\[j248\]](https://dblp.org/pid/98/6127.html#j248)

[663](https://dblp.org/pid/98/6127.html?view=joint&param=663 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuefeng Wu](https://dblp.org/pid/31/8555.html)

[\[c63\]](https://dblp.org/pid/98/6127.html#c63)

[664](https://dblp.org/pid/98/6127.html?view=joint&param=664 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ruida Xi](https://dblp.org/pid/328/5432.html)

[\[j237\]](https://dblp.org/pid/98/6127.html#j237) [\[j220\]](https://dblp.org/pid/98/6127.html#j220) [\[j193\]](https://dblp.org/pid/98/6127.html#j193) [\[i79\]](https://dblp.org/pid/98/6127.html#i79)

[665](https://dblp.org/pid/98/6127.html?view=joint&param=665 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Boyang Xia](https://dblp.org/pid/289/2080.html)

[\[c92\]](https://dblp.org/pid/98/6127.html#c92) [\[i45\]](https://dblp.org/pid/98/6127.html#i45)

[666](https://dblp.org/pid/98/6127.html?view=joint&param=666 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wei Xia 0007](https://dblp.org/pid/77/1243-7.html)

[\[j153\]](https://dblp.org/pid/98/6127.html#j153) [\[j138\]](https://dblp.org/pid/98/6127.html#j138) [\[j123\]](https://dblp.org/pid/98/6127.html#j123)

[667](https://dblp.org/pid/98/6127.html?view=joint&param=667 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zihao Xia](https://dblp.org/pid/382/4580.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[668](https://dblp.org/pid/98/6127.html?view=joint&param=668 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liuyu Xiang](https://dblp.org/pid/242/7959.html)

[\[j241\]](https://dblp.org/pid/98/6127.html#j241) [\[j173\]](https://dblp.org/pid/98/6127.html#j173) [\[j155\]](https://dblp.org/pid/98/6127.html#j155) [\[c97\]](https://dblp.org/pid/98/6127.html#c97) [\[c87\]](https://dblp.org/pid/98/6127.html#c87) [\[i28\]](https://dblp.org/pid/98/6127.html#i28) [\[c77\]](https://dblp.org/pid/98/6127.html#c77) [\[c57\]](https://dblp.org/pid/98/6127.html#c57) [\[i17\]](https://dblp.org/pid/98/6127.html#i17)

[669](https://dblp.org/pid/98/6127.html?view=joint&param=669 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chenghao Xiao](https://dblp.org/pid/325/2555.html)

[\[i85\]](https://dblp.org/pid/98/6127.html#i85)

[670](https://dblp.org/pid/98/6127.html?view=joint&param=670 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tonglin Xiao](https://dblp.org/pid/292/1102.html)

[\[j116\]](https://dblp.org/pid/98/6127.html#j116)

[671](https://dblp.org/pid/98/6127.html?view=joint&param=671 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chunyu Xie](https://dblp.org/pid/187/1594.html)

[\[j129\]](https://dblp.org/pid/98/6127.html#j129) [\[j58\]](https://dblp.org/pid/98/6127.html#j58) [\[j56\]](https://dblp.org/pid/98/6127.html#j56) [\[c42\]](https://dblp.org/pid/98/6127.html#c42) [\[i9\]](https://dblp.org/pid/98/6127.html#i9) [\[i2\]](https://dblp.org/pid/98/6127.html#i2)

[672](https://dblp.org/pid/98/6127.html?view=joint&param=672 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[De-Yan Xie](https://dblp.org/pid/02/8462.html)

[\[c58\]](https://dblp.org/pid/98/6127.html#c58)

[673](https://dblp.org/pid/98/6127.html?view=joint&param=673 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Enze Xie](https://dblp.org/pid/218/5441.html)

[\[c99\]](https://dblp.org/pid/98/6127.html#c99) [\[i57\]](https://dblp.org/pid/98/6127.html#i57)

[674](https://dblp.org/pid/98/6127.html?view=joint&param=674 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haizhen Xie](https://dblp.org/pid/375/0995.html)

[\[j233\]](https://dblp.org/pid/98/6127.html#j233)

[675](https://dblp.org/pid/98/6127.html?view=joint&param=675 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiao Xie](https://dblp.org/pid/171/5781.html)

[\[i59\]](https://dblp.org/pid/98/6127.html#i59)

[676](https://dblp.org/pid/98/6127.html?view=joint&param=676 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jin Xie 0005](https://dblp.org/pid/80/1949-5.html)

[\[j189\]](https://dblp.org/pid/98/6127.html#j189) [\[j165\]](https://dblp.org/pid/98/6127.html#j165) [\[j161\]](https://dblp.org/pid/98/6127.html#j161) [\[j144\]](https://dblp.org/pid/98/6127.html#j144) [\[c80\]](https://dblp.org/pid/98/6127.html#c80)

[677](https://dblp.org/pid/98/6127.html?view=joint&param=677 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jinxia Xie](https://dblp.org/pid/294/3376.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[678](https://dblp.org/pid/98/6127.html?view=joint&param=678 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liang Xie 0001](https://dblp.org/pid/81/2806-1.html)

[\[c28\]](https://dblp.org/pid/98/6127.html#c28)

[679](https://dblp.org/pid/98/6127.html?view=joint&param=679 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Weiyi Xie](https://dblp.org/pid/154/1297.html)

[\[j181\]](https://dblp.org/pid/98/6127.html#j181)

[680](https://dblp.org/pid/98/6127.html?view=joint&param=680 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yanchun Xie](https://dblp.org/pid/184/9463.html)

[\[j241\]](https://dblp.org/pid/98/6127.html#j241)

[681](https://dblp.org/pid/98/6127.html?view=joint&param=681 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yujie Xie](https://dblp.org/pid/204/3880.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[682](https://dblp.org/pid/98/6127.html?view=joint&param=682 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zeke Xie](https://dblp.org/pid/210/1039.html)

[\[i77\]](https://dblp.org/pid/98/6127.html#i77)

[683](https://dblp.org/pid/98/6127.html?view=joint&param=683 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Baichao Xing](https://dblp.org/pid/365/8770.html)

[\[j214\]](https://dblp.org/pid/98/6127.html#j214)

[684](https://dblp.org/pid/98/6127.html?view=joint&param=684 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Nan Xing](https://dblp.org/pid/61/3825.html)

[\[j128\]](https://dblp.org/pid/98/6127.html#j128)

[685](https://dblp.org/pid/98/6127.html?view=joint&param=685 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Deyi Xiong](https://dblp.org/pid/55/6548.html)

[\[i113\]](https://dblp.org/pid/98/6127.html#i113)

[686](https://dblp.org/pid/98/6127.html?view=joint&param=686 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yizhe Xiong](https://dblp.org/pid/358/3714.html)

[\[j226\]](https://dblp.org/pid/98/6127.html#j226) [\[c128\]](https://dblp.org/pid/98/6127.html#c128) [\[c123\]](https://dblp.org/pid/98/6127.html#c123) [\[c122\]](https://dblp.org/pid/98/6127.html#c122) [\[c120\]](https://dblp.org/pid/98/6127.html#c120) [\[c118\]](https://dblp.org/pid/98/6127.html#c118) [\[i115\]](https://dblp.org/pid/98/6127.html#i115) [\[i114\]](https://dblp.org/pid/98/6127.html#i114) [\[i113\]](https://dblp.org/pid/98/6127.html#i113) [\[i98\]](https://dblp.org/pid/98/6127.html#i98) [\[i94\]](https://dblp.org/pid/98/6127.html#i94) [\[c108\]](https://dblp.org/pid/98/6127.html#c108) [\[i84\]](https://dblp.org/pid/98/6127.html#i84)

[687](https://dblp.org/pid/98/6127.html?view=joint&param=687 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chenlong Xu](https://dblp.org/pid/315/8714.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[688](https://dblp.org/pid/98/6127.html?view=joint&param=688 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Di Xu](https://dblp.org/pid/95/7448.html)

[\[c90\]](https://dblp.org/pid/98/6127.html#c90) [\[i44\]](https://dblp.org/pid/98/6127.html#i44)

[689](https://dblp.org/pid/98/6127.html?view=joint&param=689 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dong Xu 0001](https://dblp.org/pid/09/3493-1.html)

[\[j28\]](https://dblp.org/pid/98/6127.html#j28) [\[j11\]](https://dblp.org/pid/98/6127.html#j11) [\[j10\]](https://dblp.org/pid/98/6127.html#j10)

[690](https://dblp.org/pid/98/6127.html?view=joint&param=690 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Huiling Xu](https://dblp.org/pid/63/1770.html)

[\[j123\]](https://dblp.org/pid/98/6127.html#j123)

[691](https://dblp.org/pid/98/6127.html?view=joint&param=691 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Mingliang Xu 0001](https://dblp.org/pid/13/8698-1.html)

[\[j135\]](https://dblp.org/pid/98/6127.html#j135)

[692](https://dblp.org/pid/98/6127.html?view=joint&param=692 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ning Xu](https://dblp.org/pid/04/5856.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[693](https://dblp.org/pid/98/6127.html?view=joint&param=693 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Pengfei Xu 0003](https://dblp.org/pid/04/383-3.html)

[\[i72\]](https://dblp.org/pid/98/6127.html#i72) [\[j92\]](https://dblp.org/pid/98/6127.html#j92)

[694](https://dblp.org/pid/98/6127.html?view=joint&param=694 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qianqian Xu 0001](https://dblp.org/pid/07/7627-1.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[695](https://dblp.org/pid/98/6127.html?view=joint&param=695 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shoukun Xu](https://dblp.org/pid/73/7832.html)

[\[j260\]](https://dblp.org/pid/98/6127.html#j260) [\[j259\]](https://dblp.org/pid/98/6127.html#j259) [\[j225\]](https://dblp.org/pid/98/6127.html#j225) [\[j192\]](https://dblp.org/pid/98/6127.html#j192) [\[i70\]](https://dblp.org/pid/98/6127.html#i70) [\[i62\]](https://dblp.org/pid/98/6127.html#i62) [\[i60\]](https://dblp.org/pid/98/6127.html#i60) [\[j132\]](https://dblp.org/pid/98/6127.html#j132)

[696](https://dblp.org/pid/98/6127.html?view=joint&param=696 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tao Xu 0038](https://dblp.org/pid/96/6771-38.html)

[\[j188\]](https://dblp.org/pid/98/6127.html#j188) [\[i82\]](https://dblp.org/pid/98/6127.html#i82)

[697](https://dblp.org/pid/98/6127.html?view=joint&param=697 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[698](https://dblp.org/pid/98/6127.html?view=joint&param=698 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenjia Xu](https://dblp.org/pid/34/9467.html)

[\[j244\]](https://dblp.org/pid/98/6127.html#j244) [\[j204\]](https://dblp.org/pid/98/6127.html#j204)

[699](https://dblp.org/pid/98/6127.html?view=joint&param=699 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenyuan Xu 0001](https://dblp.org/pid/10/3878-1.html)

[\[j90\]](https://dblp.org/pid/98/6127.html#j90)

[700](https://dblp.org/pid/98/6127.html?view=joint&param=700 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xinhao Xu](https://dblp.org/pid/58/8844.html)

[\[c127\]](https://dblp.org/pid/98/6127.html#c127) [\[c118\]](https://dblp.org/pid/98/6127.html#c118) [\[i89\]](https://dblp.org/pid/98/6127.html#i89) [\[c112\]](https://dblp.org/pid/98/6127.html#c112) [\[c107\]](https://dblp.org/pid/98/6127.html#c107) [\[i73\]](https://dblp.org/pid/98/6127.html#i73) [\[i41\]](https://dblp.org/pid/98/6127.html#i41)

[701](https://dblp.org/pid/98/6127.html?view=joint&param=701 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xinyun Xu](https://dblp.org/pid/260/3880.html)

[\[j103\]](https://dblp.org/pid/98/6127.html#j103)

[702](https://dblp.org/pid/98/6127.html?view=joint&param=702 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yamei Xu](https://dblp.org/pid/145/5213.html)

[\[j21\]](https://dblp.org/pid/98/6127.html#j21)

[703](https://dblp.org/pid/98/6127.html?view=joint&param=703 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yan Xu](https://dblp.org/pid/03/4702.html)

[\[j156\]](https://dblp.org/pid/98/6127.html#j156)

[704](https://dblp.org/pid/98/6127.html?view=joint&param=704 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yi Xu 0001](https://dblp.org/pid/14/5580-1.html)

[\[j181\]](https://dblp.org/pid/98/6127.html#j181)

[705](https://dblp.org/pid/98/6127.html?view=joint&param=705 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yong Xu 0007](https://dblp.org/pid/07/4630-7.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[706](https://dblp.org/pid/98/6127.html?view=joint&param=706 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhensong Xu](https://dblp.org/pid/149/5188.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[707](https://dblp.org/pid/98/6127.html?view=joint&param=707 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chaocan Xue](https://dblp.org/pid/334/6591.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[708](https://dblp.org/pid/98/6127.html?view=joint&param=708 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hui Xue 0001](https://dblp.org/pid/27/3541-1.html)

[\[c116\]](https://dblp.org/pid/98/6127.html#c116) [\[i52\]](https://dblp.org/pid/98/6127.html#i52)

[709](https://dblp.org/pid/98/6127.html?view=joint&param=709 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[An Yan](https://dblp.org/pid/37/10133.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[710](https://dblp.org/pid/98/6127.html?view=joint&param=710 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chenggang Yan 0001](https://dblp.org/pid/146/1605.html)

[\[j167\]](https://dblp.org/pid/98/6127.html#j167) [\[c72\]](https://dblp.org/pid/98/6127.html#c72) [\[c69\]](https://dblp.org/pid/98/6127.html#c69) [\[c62\]](https://dblp.org/pid/98/6127.html#c62) [\[c59\]](https://dblp.org/pid/98/6127.html#c59) [\[i18\]](https://dblp.org/pid/98/6127.html#i18)

[711](https://dblp.org/pid/98/6127.html?view=joint&param=711 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Pingkun Yan](https://dblp.org/pid/y/PingkunYan.html)

[\[j20\]](https://dblp.org/pid/98/6127.html#j20)

[712](https://dblp.org/pid/98/6127.html?view=joint&param=712 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Weipeng Yan](https://dblp.org/pid/216/8297.html)

[\[c101\]](https://dblp.org/pid/98/6127.html#c101)

[713](https://dblp.org/pid/98/6127.html?view=joint&param=713 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ai-Ping Yang](https://dblp.org/pid/31/9145.html)

aka: Aiping Yang

[\[j197\]](https://dblp.org/pid/98/6127.html#j197)

[714](https://dblp.org/pid/98/6127.html?view=joint&param=714 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chao Yang](https://dblp.org/pid/00/5867.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[715](https://dblp.org/pid/98/6127.html?view=joint&param=715 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fan Yang 0083](https://dblp.org/pid/29/3081-83.html)

[\[i72\]](https://dblp.org/pid/98/6127.html#i72) [\[i41\]](https://dblp.org/pid/98/6127.html#i41) [\[i28\]](https://dblp.org/pid/98/6127.html#i28)

[716](https://dblp.org/pid/98/6127.html?view=joint&param=716 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Guang Yang 0072](https://dblp.org/pid/25/5712-72.html)

[\[i117\]](https://dblp.org/pid/98/6127.html#i117)

[717](https://dblp.org/pid/98/6127.html?view=joint&param=717 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hui-Yue Yang](https://dblp.org/pid/385/6987.html)

[\[c129\]](https://dblp.org/pid/98/6127.html#c129) [\[c114\]](https://dblp.org/pid/98/6127.html#c114) [\[i71\]](https://dblp.org/pid/98/6127.html#i71) [\[i67\]](https://dblp.org/pid/98/6127.html#i67)

[718](https://dblp.org/pid/98/6127.html?view=joint&param=718 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiayi Yang](https://dblp.org/pid/91/9190.html)

[\[j264\]](https://dblp.org/pid/98/6127.html#j264)

[719](https://dblp.org/pid/98/6127.html?view=joint&param=719 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110) [\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i76\]](https://dblp.org/pid/98/6127.html#i76) [\[i75\]](https://dblp.org/pid/98/6127.html#i75) [\[j171\]](https://dblp.org/pid/98/6127.html#j171) [\[j98\]](https://dblp.org/pid/98/6127.html#j98) [\[i13\]](https://dblp.org/pid/98/6127.html#i13) [\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[720](https://dblp.org/pid/98/6127.html?view=joint&param=720 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jinze Yang](https://dblp.org/pid/162/1636.html)

[\[i77\]](https://dblp.org/pid/98/6127.html#i77)

[721](https://dblp.org/pid/98/6127.html?view=joint&param=721 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Junbo Yang](https://dblp.org/pid/14/7508.html)

[\[j248\]](https://dblp.org/pid/98/6127.html#j248)

[722](https://dblp.org/pid/98/6127.html?view=joint&param=722 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Linjie Yang](https://dblp.org/pid/126/6794.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[723](https://dblp.org/pid/98/6127.html?view=joint&param=723 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Linlin Yang](https://dblp.org/pid/84/6484.html)

[\[j40\]](https://dblp.org/pid/98/6127.html#j40) [\[j32\]](https://dblp.org/pid/98/6127.html#j32) [\[c22\]](https://dblp.org/pid/98/6127.html#c22)

[724](https://dblp.org/pid/98/6127.html?view=joint&param=724 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ming Yang 0024](https://dblp.org/pid/98/2604-24.html)

[\[j153\]](https://dblp.org/pid/98/6127.html#j153)

[725](https://dblp.org/pid/98/6127.html?view=joint&param=725 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ming-Hsuan Yang 0001](https://dblp.org/pid/79/3711.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110) [\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[726](https://dblp.org/pid/98/6127.html?view=joint&param=726 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shuo Yang](https://dblp.org/pid/78/1102.html)

[\[i69\]](https://dblp.org/pid/98/6127.html#i69)

[727](https://dblp.org/pid/98/6127.html?view=joint&param=727 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shuyuan Yang 0001](https://dblp.org/pid/81/2383.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[728](https://dblp.org/pid/98/6127.html?view=joint&param=728 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[j97\]](https://dblp.org/pid/98/6127.html#j97) [\[c36\]](https://dblp.org/pid/98/6127.html#c36)

[729](https://dblp.org/pid/98/6127.html?view=joint&param=729 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenhao Yang](https://dblp.org/pid/233/4699.html)

[\[i110\]](https://dblp.org/pid/98/6127.html#i110)

[730](https://dblp.org/pid/98/6127.html?view=joint&param=730 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yang Yang](https://dblp.org/pid/48/450.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[731](https://dblp.org/pid/98/6127.html?view=joint&param=731 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yang Yang 0009](https://dblp.org/pid/48/450-9.html)

[\[j269\]](https://dblp.org/pid/98/6127.html#j269) [\[j217\]](https://dblp.org/pid/98/6127.html#j217) [\[i80\]](https://dblp.org/pid/98/6127.html#i80) [\[i79\]](https://dblp.org/pid/98/6127.html#i79)

[732](https://dblp.org/pid/98/6127.html?view=joint&param=732 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yang Yang 0132](https://dblp.org/pid/48/450-132.html)

[\[j202\]](https://dblp.org/pid/98/6127.html#j202) [\[j193\]](https://dblp.org/pid/98/6127.html#j193) [\[j142\]](https://dblp.org/pid/98/6127.html#j142) [\[j130\]](https://dblp.org/pid/98/6127.html#j130)

[733](https://dblp.org/pid/98/6127.html?view=joint&param=733 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yifan Yang](https://dblp.org/pid/83/89.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[734](https://dblp.org/pid/98/6127.html?view=joint&param=734 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuanjian Yang](https://dblp.org/pid/130/3568.html)

[\[j228\]](https://dblp.org/pid/98/6127.html#j228) [\[j191\]](https://dblp.org/pid/98/6127.html#j191)

[735](https://dblp.org/pid/98/6127.html?view=joint&param=735 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuhong Yang 0008](https://dblp.org/pid/365/8877.html)

[\[j241\]](https://dblp.org/pid/98/6127.html#j241) [\[c116\]](https://dblp.org/pid/98/6127.html#c116) [\[i52\]](https://dblp.org/pid/98/6127.html#i52)

[736](https://dblp.org/pid/98/6127.html?view=joint&param=736 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yun Yang](https://dblp.org/pid/90/3406.html)

[\[j32\]](https://dblp.org/pid/98/6127.html#j32)

[737](https://dblp.org/pid/98/6127.html?view=joint&param=737 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuting Yang 0008](https://dblp.org/pid/25/3635-8.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[738](https://dblp.org/pid/98/6127.html?view=joint&param=738 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhaohua Yang](https://dblp.org/pid/117/3393.html)

[\[j47\]](https://dblp.org/pid/98/6127.html#j47)

[739](https://dblp.org/pid/98/6127.html?view=joint&param=739 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhenheng Yang](https://dblp.org/pid/186/7818.html)

[\[i110\]](https://dblp.org/pid/98/6127.html#i110)

[740](https://dblp.org/pid/98/6127.html?view=joint&param=740 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhenyu Yang](https://dblp.org/pid/13/5969.html)

[\[i72\]](https://dblp.org/pid/98/6127.html#i72)

[741](https://dblp.org/pid/98/6127.html?view=joint&param=741 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chao Yao](https://dblp.org/pid/99/6747.html)

[\[j31\]](https://dblp.org/pid/98/6127.html#j31) [\[j30\]](https://dblp.org/pid/98/6127.html#j30) [\[j21\]](https://dblp.org/pid/98/6127.html#j21)

[742](https://dblp.org/pid/98/6127.html?view=joint&param=742 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hongxun Yao](https://dblp.org/pid/y/HongxunYao.html)

[\[j100\]](https://dblp.org/pid/98/6127.html#j100)

[743](https://dblp.org/pid/98/6127.html?view=joint&param=743 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiangtao Yao](https://dblp.org/pid/294/5962.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[744](https://dblp.org/pid/98/6127.html?view=joint&param=744 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lin Yao](https://dblp.org/pid/37/752.html)

[\[j95\]](https://dblp.org/pid/98/6127.html#j95) [\[j77\]](https://dblp.org/pid/98/6127.html#j77)

[745](https://dblp.org/pid/98/6127.html?view=joint&param=745 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiwen Yao](https://dblp.org/pid/163/0541.html)

[\[j137\]](https://dblp.org/pid/98/6127.html#j137) [\[j135\]](https://dblp.org/pid/98/6127.html#j135)

[746](https://dblp.org/pid/98/6127.html?view=joint&param=746 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Guixin Ye](https://dblp.org/pid/125/3245.html)

[\[j92\]](https://dblp.org/pid/98/6127.html#j92)

[747](https://dblp.org/pid/98/6127.html?view=joint&param=747 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qixiang Ye](https://dblp.org/pid/06/4335.html)

[\[j66\]](https://dblp.org/pid/98/6127.html#j66) [\[j40\]](https://dblp.org/pid/98/6127.html#j40) [\[i3\]](https://dblp.org/pid/98/6127.html#i3)

[748](https://dblp.org/pid/98/6127.html?view=joint&param=748 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wei Ye 0001](https://dblp.org/pid/09/5394-1.html)

[\[j264\]](https://dblp.org/pid/98/6127.html#j264)

[749](https://dblp.org/pid/98/6127.html?view=joint&param=749 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Ye](https://dblp.org/pid/69/3992.html)

[\[c122\]](https://dblp.org/pid/98/6127.html#c122) [\[i115\]](https://dblp.org/pid/98/6127.html#i115)

[750](https://dblp.org/pid/98/6127.html?view=joint&param=750 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dewei Yi](https://dblp.org/pid/181/0412.html)

[\[j146\]](https://dblp.org/pid/98/6127.html#j146)

[751](https://dblp.org/pid/98/6127.html?view=joint&param=751 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liu Yi](https://dblp.org/pid/46/3050.html)

[\[j62\]](https://dblp.org/pid/98/6127.html#j62)

[752](https://dblp.org/pid/98/6127.html?view=joint&param=752 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hanxi Yin](https://dblp.org/pid/334/9389.html)

[\[c130\]](https://dblp.org/pid/98/6127.html#c130)

[753](https://dblp.org/pid/98/6127.html?view=joint&param=753 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kaining Ying](https://dblp.org/pid/291/9018.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[754](https://dblp.org/pid/98/6127.html?view=joint&param=754 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jun-Hai Yong](https://dblp.org/pid/50/4074.html)

[\[c61\]](https://dblp.org/pid/98/6127.html#c61)

[755](https://dblp.org/pid/98/6127.html?view=joint&param=755 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shaodi You](https://dblp.org/pid/72/7950.html)

[\[c130\]](https://dblp.org/pid/98/6127.html#c130)

[756](https://dblp.org/pid/98/6127.html?view=joint&param=756 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zheng You](https://dblp.org/pid/04/2178.html)

[\[j160\]](https://dblp.org/pid/98/6127.html#j160) [\[i35\]](https://dblp.org/pid/98/6127.html#i35)

[757](https://dblp.org/pid/98/6127.html?view=joint&param=757 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jan Ypma](https://dblp.org/pid/96/2843.html)

[\[c4\]](https://dblp.org/pid/98/6127.html#c4)

[758](https://dblp.org/pid/98/6127.html?view=joint&param=758 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chenyang Yu](https://dblp.org/pid/287/4163.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[759](https://dblp.org/pid/98/6127.html?view=joint&param=759 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dahai Yu](https://dblp.org/pid/31/2647.html)

[\[j15\]](https://dblp.org/pid/98/6127.html#j15)

[760](https://dblp.org/pid/98/6127.html?view=joint&param=760 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[James Jian Qiao Yu](https://dblp.org/pid/55/10087.html)

aka: James J. Q. Yu

[\[j183\]](https://dblp.org/pid/98/6127.html#j183) [\[j176\]](https://dblp.org/pid/98/6127.html#j176)

[761](https://dblp.org/pid/98/6127.html?view=joint&param=761 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ke Yu](https://dblp.org/pid/23/2089.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[762](https://dblp.org/pid/98/6127.html?view=joint&param=762 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Li Yu 0004](https://dblp.org/pid/70/5913-4.html)

[\[c119\]](https://dblp.org/pid/98/6127.html#c119)

[763](https://dblp.org/pid/98/6127.html?view=joint&param=763 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yizhou Yu](https://dblp.org/pid/90/6896.html)

[\[i51\]](https://dblp.org/pid/98/6127.html#i51) [\[j121\]](https://dblp.org/pid/98/6127.html#j121) [\[j94\]](https://dblp.org/pid/98/6127.html#j94)

[764](https://dblp.org/pid/98/6127.html?view=joint&param=764 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yunlong Yu](https://dblp.org/pid/45/7404.html)

[\[j251\]](https://dblp.org/pid/98/6127.html#j251) [\[j245\]](https://dblp.org/pid/98/6127.html#j245) [\[j242\]](https://dblp.org/pid/98/6127.html#j242) [\[j234\]](https://dblp.org/pid/98/6127.html#j234) [\[j232\]](https://dblp.org/pid/98/6127.html#j232) [\[j215\]](https://dblp.org/pid/98/6127.html#j215) [\[j212\]](https://dblp.org/pid/98/6127.html#j212) [\[j201\]](https://dblp.org/pid/98/6127.html#j201) [\[j194\]](https://dblp.org/pid/98/6127.html#j194) [\[c102\]](https://dblp.org/pid/98/6127.html#c102) [\[i74\]](https://dblp.org/pid/98/6127.html#i74) [\[j162\]](https://dblp.org/pid/98/6127.html#j162) [\[i58\]](https://dblp.org/pid/98/6127.html#i58) [\[j91\]](https://dblp.org/pid/98/6127.html#j91) [\[c78\]](https://dblp.org/pid/98/6127.html#c78) [\[j84\]](https://dblp.org/pid/98/6127.html#j84) [\[i15\]](https://dblp.org/pid/98/6127.html#i15) [\[i12\]](https://dblp.org/pid/98/6127.html#i12)

[765](https://dblp.org/pid/98/6127.html?view=joint&param=765 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhou Yu](https://dblp.org/pid/83/3205.html)

[\[i59\]](https://dblp.org/pid/98/6127.html#i59)

[766](https://dblp.org/pid/98/6127.html?view=joint&param=766 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Haobo Yuan](https://dblp.org/pid/280/2872.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[767](https://dblp.org/pid/98/6127.html?view=joint&param=767 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Sangdoo Yun](https://dblp.org/pid/124/3009.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[768](https://dblp.org/pid/98/6127.html?view=joint&param=768 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Stefanos Zafeiriou](https://dblp.org/pid/25/1885.html)

[\[c89\]](https://dblp.org/pid/98/6127.html#c89) [\[i40\]](https://dblp.org/pid/98/6127.html#i40)

[769](https://dblp.org/pid/98/6127.html?view=joint&param=769 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yumna Zahid](https://dblp.org/pid/227/0373.html)

[\[j256\]](https://dblp.org/pid/98/6127.html#j256) [\[j155\]](https://dblp.org/pid/98/6127.html#j155) [\[c88\]](https://dblp.org/pid/98/6127.html#c88)

[770](https://dblp.org/pid/98/6127.html?view=joint&param=770 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuhang Zang](https://dblp.org/pid/230/4433.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[771](https://dblp.org/pid/98/6127.html?view=joint&param=771 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Christine Zarges](https://dblp.org/pid/13/6472.html)

[\[j256\]](https://dblp.org/pid/98/6127.html#j256)

[772](https://dblp.org/pid/98/6127.html?view=joint&param=772 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Paul M. de Zeeuw](https://dblp.org/pid/84/1406.html)

[\[j14\]](https://dblp.org/pid/98/6127.html#j14) [\[j12\]](https://dblp.org/pid/98/6127.html#j12) [\[j8\]](https://dblp.org/pid/98/6127.html#j8) [\[c21\]](https://dblp.org/pid/98/6127.html#c21) [\[c20\]](https://dblp.org/pid/98/6127.html#c20) [\[c19\]](https://dblp.org/pid/98/6127.html#c19)

[773](https://dblp.org/pid/98/6127.html?view=joint&param=773 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dan Zeng 0001](https://dblp.org/pid/06/6575-1.html)

[\[j167\]](https://dblp.org/pid/98/6127.html#j167) [\[j147\]](https://dblp.org/pid/98/6127.html#j147)

[774](https://dblp.org/pid/98/6127.html?view=joint&param=774 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bing Zhai](https://dblp.org/pid/182/9111.html)

[\[j258\]](https://dblp.org/pid/98/6127.html#j258) [\[j257\]](https://dblp.org/pid/98/6127.html#j257)

[775](https://dblp.org/pid/98/6127.html?view=joint&param=775 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Baochang Zhang 0001](https://dblp.org/pid/80/3887-1.html)

[\[j223\]](https://dblp.org/pid/98/6127.html#j223) [\[j172\]](https://dblp.org/pid/98/6127.html#j172) [\[i59\]](https://dblp.org/pid/98/6127.html#i59) [\[j129\]](https://dblp.org/pid/98/6127.html#j129) [\[j122\]](https://dblp.org/pid/98/6127.html#j122) [\[j109\]](https://dblp.org/pid/98/6127.html#j109) [\[j98\]](https://dblp.org/pid/98/6127.html#j98) [\[j97\]](https://dblp.org/pid/98/6127.html#j97) [\[c76\]](https://dblp.org/pid/98/6127.html#c76) [\[i26\]](https://dblp.org/pid/98/6127.html#i26) [\[j73\]](https://dblp.org/pid/98/6127.html#j73) [\[j70\]](https://dblp.org/pid/98/6127.html#j70) [\[j66\]](https://dblp.org/pid/98/6127.html#j66) [\[c73\]](https://dblp.org/pid/98/6127.html#c73) [\[c53\]](https://dblp.org/pid/98/6127.html#c53) [\[i13\]](https://dblp.org/pid/98/6127.html#i13) [\[j58\]](https://dblp.org/pid/98/6127.html#j58) [\[j56\]](https://dblp.org/pid/98/6127.html#j56) [\[j50\]](https://dblp.org/pid/98/6127.html#j50) [\[j49\]](https://dblp.org/pid/98/6127.html#j49) [\[c45\]](https://dblp.org/pid/98/6127.html#c45) [\[c44\]](https://dblp.org/pid/98/6127.html#c44) [\[c42\]](https://dblp.org/pid/98/6127.html#c42) [\[c39\]](https://dblp.org/pid/98/6127.html#c39) [\[c36\]](https://dblp.org/pid/98/6127.html#c36) [\[i11\]](https://dblp.org/pid/98/6127.html#i11) [\[i10\]](https://dblp.org/pid/98/6127.html#i10) [\[i9\]](https://dblp.org/pid/98/6127.html#i9) [\[i7\]](https://dblp.org/pid/98/6127.html#i7) [\[j44\]](https://dblp.org/pid/98/6127.html#j44) [\[j40\]](https://dblp.org/pid/98/6127.html#j40) [\[j38\]](https://dblp.org/pid/98/6127.html#j38) [\[j32\]](https://dblp.org/pid/98/6127.html#j32) [\[i5\]](https://dblp.org/pid/98/6127.html#i5) [\[i3\]](https://dblp.org/pid/98/6127.html#i3) [\[i2\]](https://dblp.org/pid/98/6127.html#i2) [\[i1\]](https://dblp.org/pid/98/6127.html#i1) [\[j29\]](https://dblp.org/pid/98/6127.html#j29) [\[c24\]](https://dblp.org/pid/98/6127.html#c24) [\[c22\]](https://dblp.org/pid/98/6127.html#c22)

[776](https://dblp.org/pid/98/6127.html?view=joint&param=776 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ce Zhang 0005](https://dblp.org/pid/97/919-5.html)

[\[j277\]](https://dblp.org/pid/98/6127.html#j277) [\[j154\]](https://dblp.org/pid/98/6127.html#j154)

[777](https://dblp.org/pid/98/6127.html?view=joint&param=777 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[778](https://dblp.org/pid/98/6127.html?view=joint&param=778 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Di Zhang 0026](https://dblp.org/pid/80/3482-26.html)

[\[c123\]](https://dblp.org/pid/98/6127.html#c123) [\[i114\]](https://dblp.org/pid/98/6127.html#i114) [\[i113\]](https://dblp.org/pid/98/6127.html#i113)

[779](https://dblp.org/pid/98/6127.html?view=joint&param=779 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dingwen Zhang](https://dblp.org/pid/150/6620.html)

[\[j260\]](https://dblp.org/pid/98/6127.html#j260) [\[j225\]](https://dblp.org/pid/98/6127.html#j225) [\[i62\]](https://dblp.org/pid/98/6127.html#i62) [\[j174\]](https://dblp.org/pid/98/6127.html#j174) [\[i60\]](https://dblp.org/pid/98/6127.html#i60) [\[j160\]](https://dblp.org/pid/98/6127.html#j160) [\[j159\]](https://dblp.org/pid/98/6127.html#j159) [\[j152\]](https://dblp.org/pid/98/6127.html#j152) [\[j132\]](https://dblp.org/pid/98/6127.html#j132) [\[j130\]](https://dblp.org/pid/98/6127.html#j130) [\[i51\]](https://dblp.org/pid/98/6127.html#i51) [\[i48\]](https://dblp.org/pid/98/6127.html#i48) [\[j121\]](https://dblp.org/pid/98/6127.html#j121) [\[j118\]](https://dblp.org/pid/98/6127.html#j118) [\[j116\]](https://dblp.org/pid/98/6127.html#j116) [\[j114\]](https://dblp.org/pid/98/6127.html#j114) [\[c86\]](https://dblp.org/pid/98/6127.html#c86) [\[i37\]](https://dblp.org/pid/98/6127.html#i37) [\[i35\]](https://dblp.org/pid/98/6127.html#i35) [\[i34\]](https://dblp.org/pid/98/6127.html#i34) [\[j95\]](https://dblp.org/pid/98/6127.html#j95) [\[j94\]](https://dblp.org/pid/98/6127.html#j94) [\[c74\]](https://dblp.org/pid/98/6127.html#c74) [\[c67\]](https://dblp.org/pid/98/6127.html#c67) [\[j27\]](https://dblp.org/pid/98/6127.html#j27)

[780](https://dblp.org/pid/98/6127.html?view=joint&param=780 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dingyi Zhang](https://dblp.org/pid/132/6761.html)

[\[j232\]](https://dblp.org/pid/98/6127.html#j232)

[781](https://dblp.org/pid/98/6127.html?view=joint&param=781 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Duona Zhang](https://dblp.org/pid/217/3671.html)

[\[j122\]](https://dblp.org/pid/98/6127.html#j122) [\[j56\]](https://dblp.org/pid/98/6127.html#j56)

[782](https://dblp.org/pid/98/6127.html?view=joint&param=782 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fan Zhang](https://dblp.org/pid/21/3626.html)

[\[i94\]](https://dblp.org/pid/98/6127.html#i94)

[783](https://dblp.org/pid/98/6127.html?view=joint&param=783 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hongsheng Zhang](https://dblp.org/pid/19/4547.html)

[\[j263\]](https://dblp.org/pid/98/6127.html#j263) [\[i68\]](https://dblp.org/pid/98/6127.html#i68)

[784](https://dblp.org/pid/98/6127.html?view=joint&param=784 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hongyang Zhang](https://dblp.org/pid/23/10537.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[785](https://dblp.org/pid/98/6127.html?view=joint&param=785 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Huang Zhang](https://dblp.org/pid/132/6996.html)

[\[j268\]](https://dblp.org/pid/98/6127.html#j268)

[786](https://dblp.org/pid/98/6127.html?view=joint&param=786 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiajia Zhang](https://dblp.org/pid/08/267.html)

[\[j160\]](https://dblp.org/pid/98/6127.html#j160) [\[j118\]](https://dblp.org/pid/98/6127.html#j118) [\[i35\]](https://dblp.org/pid/98/6127.html#i35)

[787](https://dblp.org/pid/98/6127.html?view=joint&param=787 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiaming Zhang 0006](https://dblp.org/pid/81/10010-6.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[788](https://dblp.org/pid/98/6127.html?view=joint&param=788 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jianguo Zhang 0001](https://dblp.org/pid/90/6415-1.html)

[\[j236\]](https://dblp.org/pid/98/6127.html#j236) [\[i117\]](https://dblp.org/pid/98/6127.html#i117) [\[j209\]](https://dblp.org/pid/98/6127.html#j209) [\[j166\]](https://dblp.org/pid/98/6127.html#j166)

[789](https://dblp.org/pid/98/6127.html?view=joint&param=789 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jianqiao Zhang 0002](https://dblp.org/pid/219/2760-2.html)

[\[c103\]](https://dblp.org/pid/98/6127.html#c103)

[790](https://dblp.org/pid/98/6127.html?view=joint&param=790 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jie Zhang 0091](https://dblp.org/pid/84/6889-91.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[791](https://dblp.org/pid/98/6127.html?view=joint&param=791 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jing Zhang 0037](https://dblp.org/pid/05/3499-37.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[792](https://dblp.org/pid/98/6127.html?view=joint&param=792 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jinghao Zhang](https://dblp.org/pid/284/0853.html)

[\[j277\]](https://dblp.org/pid/98/6127.html#j277)

[793](https://dblp.org/pid/98/6127.html?view=joint&param=793 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jingtian Zhang](https://dblp.org/pid/181/3959.html)

[\[j48\]](https://dblp.org/pid/98/6127.html#j48)

[794](https://dblp.org/pid/98/6127.html?view=joint&param=794 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiyong Zhang 0001](https://dblp.org/pid/95/6425-1.html)

[\[c82\]](https://dblp.org/pid/98/6127.html#c82) [\[c59\]](https://dblp.org/pid/98/6127.html#c59)

[795](https://dblp.org/pid/98/6127.html?view=joint&param=795 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jun Zhang 0007](https://dblp.org/pid/z/JunZhang7.html)

[\[j208\]](https://dblp.org/pid/98/6127.html#j208) [\[j136\]](https://dblp.org/pid/98/6127.html#j136)

[796](https://dblp.org/pid/98/6127.html?view=joint&param=796 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Junjie Zhang 0002](https://dblp.org/pid/99/6243-2.html)

[\[j167\]](https://dblp.org/pid/98/6127.html#j167) [\[j147\]](https://dblp.org/pid/98/6127.html#j147)

[797](https://dblp.org/pid/98/6127.html?view=joint&param=797 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[798](https://dblp.org/pid/98/6127.html?view=joint&param=798 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ke Zhang 0005](https://dblp.org/pid/20/4152-5.html)

[\[j157\]](https://dblp.org/pid/98/6127.html#j157) [\[j125\]](https://dblp.org/pid/98/6127.html#j125) [\[j81\]](https://dblp.org/pid/98/6127.html#j81)

[799](https://dblp.org/pid/98/6127.html?view=joint&param=799 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kefeng Zhang](https://dblp.org/pid/84/5516.html)

[\[i64\]](https://dblp.org/pid/98/6127.html#i64)

[800](https://dblp.org/pid/98/6127.html?view=joint&param=800 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Kexin Zhang 0003](https://dblp.org/pid/119/0668-3.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[801](https://dblp.org/pid/98/6127.html?view=joint&param=801 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lei Zhang 0038](https://dblp.org/pid/64/5666-38.html)

[\[j265\]](https://dblp.org/pid/98/6127.html#j265) [\[j246\]](https://dblp.org/pid/98/6127.html#j246)

[802](https://dblp.org/pid/98/6127.html?view=joint&param=802 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Li Zhang 0013](https://dblp.org/pid/89/5992-13.html)

[\[j88\]](https://dblp.org/pid/98/6127.html#j88) [\[j80\]](https://dblp.org/pid/98/6127.html#j80)

[803](https://dblp.org/pid/98/6127.html?view=joint&param=803 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liang-Jie Zhang](https://dblp.org/pid/z/LiangJieZhang.html)

[\[i97\]](https://dblp.org/pid/98/6127.html#i97)

[804](https://dblp.org/pid/98/6127.html?view=joint&param=804 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Peizhen Zhang](https://dblp.org/pid/115/9027.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[805](https://dblp.org/pid/98/6127.html?view=joint&param=805 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Peng Zhang 0057](https://dblp.org/pid/21/1048-57.html)

[\[j184\]](https://dblp.org/pid/98/6127.html#j184)

[806](https://dblp.org/pid/98/6127.html?view=joint&param=806 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ping Zhang 0025](https://dblp.org/pid/13/4682-25.html)

[\[j244\]](https://dblp.org/pid/98/6127.html#j244) [\[i88\]](https://dblp.org/pid/98/6127.html#i88) [\[j204\]](https://dblp.org/pid/98/6127.html#j204)

[807](https://dblp.org/pid/98/6127.html?view=joint&param=807 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Qiang Zhang 0020](https://dblp.org/pid/72/3527-20.html)

[\[j269\]](https://dblp.org/pid/98/6127.html#j269) [\[j267\]](https://dblp.org/pid/98/6127.html#j267) [\[j253\]](https://dblp.org/pid/98/6127.html#j253) [\[j249\]](https://dblp.org/pid/98/6127.html#j249) [\[j247\]](https://dblp.org/pid/98/6127.html#j247) [\[j237\]](https://dblp.org/pid/98/6127.html#j237) [\[j226\]](https://dblp.org/pid/98/6127.html#j226) [\[j220\]](https://dblp.org/pid/98/6127.html#j220) [\[i87\]](https://dblp.org/pid/98/6127.html#i87) [\[j217\]](https://dblp.org/pid/98/6127.html#j217) [\[j214\]](https://dblp.org/pid/98/6127.html#j214) [\[j205\]](https://dblp.org/pid/98/6127.html#j205) [\[j202\]](https://dblp.org/pid/98/6127.html#j202) [\[j198\]](https://dblp.org/pid/98/6127.html#j198) [\[j195\]](https://dblp.org/pid/98/6127.html#j195) [\[j193\]](https://dblp.org/pid/98/6127.html#j193) [\[j186\]](https://dblp.org/pid/98/6127.html#j186) [\[c104\]](https://dblp.org/pid/98/6127.html#c104) [\[i80\]](https://dblp.org/pid/98/6127.html#i80) [\[i79\]](https://dblp.org/pid/98/6127.html#i79) [\[j179\]](https://dblp.org/pid/98/6127.html#j179) [\[j178\]](https://dblp.org/pid/98/6127.html#j178) [\[j175\]](https://dblp.org/pid/98/6127.html#j175) [\[j174\]](https://dblp.org/pid/98/6127.html#j174) [\[c101\]](https://dblp.org/pid/98/6127.html#c101) [\[c100\]](https://dblp.org/pid/98/6127.html#c100) [\[j160\]](https://dblp.org/pid/98/6127.html#j160) [\[j159\]](https://dblp.org/pid/98/6127.html#j159) [\[j152\]](https://dblp.org/pid/98/6127.html#j152) [\[j150\]](https://dblp.org/pid/98/6127.html#j150) [\[j149\]](https://dblp.org/pid/98/6127.html#j149) [\[j145\]](https://dblp.org/pid/98/6127.html#j145) [\[j143\]](https://dblp.org/pid/98/6127.html#j143) [\[j142\]](https://dblp.org/pid/98/6127.html#j142) [\[j141\]](https://dblp.org/pid/98/6127.html#j141) [\[j133\]](https://dblp.org/pid/98/6127.html#j133) [\[j130\]](https://dblp.org/pid/98/6127.html#j130) [\[c95\]](https://dblp.org/pid/98/6127.html#c95) [\[i51\]](https://dblp.org/pid/98/6127.html#i51) [\[i50\]](https://dblp.org/pid/98/6127.html#i50) [\[i48\]](https://dblp.org/pid/98/6127.html#i48) [\[j121\]](https://dblp.org/pid/98/6127.html#j121) [\[j119\]](https://dblp.org/pid/98/6127.html#j119) [\[j118\]](https://dblp.org/pid/98/6127.html#j118) [\[j116\]](https://dblp.org/pid/98/6127.html#j116) [\[j114\]](https://dblp.org/pid/98/6127.html#j114) [\[j111\]](https://dblp.org/pid/98/6127.html#j111) [\[c86\]](https://dblp.org/pid/98/6127.html#c86) [\[i37\]](https://dblp.org/pid/98/6127.html#i37) [\[i35\]](https://dblp.org/pid/98/6127.html#i35) [\[i33\]](https://dblp.org/pid/98/6127.html#i33) [\[i32\]](https://dblp.org/pid/98/6127.html#i32) [\[j102\]](https://dblp.org/pid/98/6127.html#j102) [\[j99\]](https://dblp.org/pid/98/6127.html#j99) [\[j95\]](https://dblp.org/pid/98/6127.html#j95) [\[j94\]](https://dblp.org/pid/98/6127.html#j94) [\[j77\]](https://dblp.org/pid/98/6127.html#j77) [\[j76\]](https://dblp.org/pid/98/6127.html#j76) [\[j71\]](https://dblp.org/pid/98/6127.html#j71) [\[c67\]](https://dblp.org/pid/98/6127.html#c67) [\[j63\]](https://dblp.org/pid/98/6127.html#j63) [\[j62\]](https://dblp.org/pid/98/6127.html#j62) [\[j57\]](https://dblp.org/pid/98/6127.html#j57) [\[j43\]](https://dblp.org/pid/98/6127.html#j43) [\[i6\]](https://dblp.org/pid/98/6127.html#i6)

[808](https://dblp.org/pid/98/6127.html?view=joint&param=808 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ruixin Zhang](https://dblp.org/pid/132/6250.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[809](https://dblp.org/pid/98/6127.html?view=joint&param=809 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shu Zhang 0001](https://dblp.org/pid/30/2700-1.html)

[\[j118\]](https://dblp.org/pid/98/6127.html#j118)

[810](https://dblp.org/pid/98/6127.html?view=joint&param=810 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shuaitong Zhang](https://dblp.org/pid/239/1871.html)

[\[j157\]](https://dblp.org/pid/98/6127.html#j157) [\[j125\]](https://dblp.org/pid/98/6127.html#j125)

[811](https://dblp.org/pid/98/6127.html?view=joint&param=811 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shuo Zhang](https://dblp.org/pid/83/3714.html)

[\[j180\]](https://dblp.org/pid/98/6127.html#j180) [\[j113\]](https://dblp.org/pid/98/6127.html#j113)

[812](https://dblp.org/pid/98/6127.html?view=joint&param=812 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Suqi Zhang](https://dblp.org/pid/145/6076.html)

[\[j103\]](https://dblp.org/pid/98/6127.html#j103)

[813](https://dblp.org/pid/98/6127.html?view=joint&param=813 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tao Zhang](https://dblp.org/pid/15/4777.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[814](https://dblp.org/pid/98/6127.html?view=joint&param=814 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Tianlu Zhang](https://dblp.org/pid/255/8662.html)

[\[j272\]](https://dblp.org/pid/98/6127.html#j272) [\[j249\]](https://dblp.org/pid/98/6127.html#j249) [\[i117\]](https://dblp.org/pid/98/6127.html#i117) [\[i100\]](https://dblp.org/pid/98/6127.html#i100) [\[i87\]](https://dblp.org/pid/98/6127.html#i87) [\[j205\]](https://dblp.org/pid/98/6127.html#j205) [\[j198\]](https://dblp.org/pid/98/6127.html#j198) [\[j195\]](https://dblp.org/pid/98/6127.html#j195) [\[c104\]](https://dblp.org/pid/98/6127.html#c104) [\[c100\]](https://dblp.org/pid/98/6127.html#c100) [\[j145\]](https://dblp.org/pid/98/6127.html#j145)

[815](https://dblp.org/pid/98/6127.html?view=joint&param=815 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wei Zhang 0021](https://dblp.org/pid/10/4661-21.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[816](https://dblp.org/pid/98/6127.html?view=joint&param=816 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wenhua Zhang](https://dblp.org/pid/28/1877.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[817](https://dblp.org/pid/98/6127.html?view=joint&param=817 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiangdong Zhang](https://dblp.org/pid/26/1791.html)

[\[j138\]](https://dblp.org/pid/98/6127.html#j138)

[818](https://dblp.org/pid/98/6127.html?view=joint&param=818 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiangwen Zhang](https://dblp.org/pid/68/646.html)

[\[i113\]](https://dblp.org/pid/98/6127.html#i113)

[819](https://dblp.org/pid/98/6127.html?view=joint&param=819 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiangyu Zhang 0005](https://dblp.org/pid/95/3760-5.html)

[\[c98\]](https://dblp.org/pid/98/6127.html#c98) [\[c96\]](https://dblp.org/pid/98/6127.html#c96) [\[c94\]](https://dblp.org/pid/98/6127.html#c94) [\[i49\]](https://dblp.org/pid/98/6127.html#i49) [\[i47\]](https://dblp.org/pid/98/6127.html#i47) [\[c85\]](https://dblp.org/pid/98/6127.html#c85) [\[c84\]](https://dblp.org/pid/98/6127.html#c84) [\[i38\]](https://dblp.org/pid/98/6127.html#i38) [\[i36\]](https://dblp.org/pid/98/6127.html#i36) [\[i31\]](https://dblp.org/pid/98/6127.html#i31) [\[i27\]](https://dblp.org/pid/98/6127.html#i27)

[820](https://dblp.org/pid/98/6127.html?view=joint&param=820 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiao Zhang](https://dblp.org/pid/49/4478.html)

[\[i117\]](https://dblp.org/pid/98/6127.html#i117) [\[i104\]](https://dblp.org/pid/98/6127.html#i104)

[821](https://dblp.org/pid/98/6127.html?view=joint&param=821 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Zhang 0008](https://dblp.org/pid/76/1584-8.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[822](https://dblp.org/pid/98/6127.html?view=joint&param=822 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xinyu Zhang](https://dblp.org/pid/58/4582.html)

[\[j184\]](https://dblp.org/pid/98/6127.html#j184)

[823](https://dblp.org/pid/98/6127.html?view=joint&param=823 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xun Zhang](https://dblp.org/pid/18/3246.html)

[\[j254\]](https://dblp.org/pid/98/6127.html#j254) [\[i108\]](https://dblp.org/pid/98/6127.html#i108) [\[j211\]](https://dblp.org/pid/98/6127.html#j211)

[824](https://dblp.org/pid/98/6127.html?view=joint&param=824 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yajuan Zhang](https://dblp.org/pid/09/10185.html)

[\[j244\]](https://dblp.org/pid/98/6127.html#j244) [\[i88\]](https://dblp.org/pid/98/6127.html#i88) [\[j204\]](https://dblp.org/pid/98/6127.html#j204)

[825](https://dblp.org/pid/98/6127.html?view=joint&param=825 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yan Zhang 0135](https://dblp.org/pid/04/3348-135.html)

[\[j252\]](https://dblp.org/pid/98/6127.html#j252) [\[j235\]](https://dblp.org/pid/98/6127.html#j235) [\[i112\]](https://dblp.org/pid/98/6127.html#i112) [\[i105\]](https://dblp.org/pid/98/6127.html#i105) [\[j218\]](https://dblp.org/pid/98/6127.html#j218) [\[c106\]](https://dblp.org/pid/98/6127.html#c106) [\[i81\]](https://dblp.org/pid/98/6127.html#i81)

[826](https://dblp.org/pid/98/6127.html?view=joint&param=826 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yanhao Zhang 0001](https://dblp.org/pid/84/10486-1.html)

[\[i72\]](https://dblp.org/pid/98/6127.html#i72)

[827](https://dblp.org/pid/98/6127.html?view=joint&param=827 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yifan Zhang 0001](https://dblp.org/pid/57/4707-1.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[828](https://dblp.org/pid/98/6127.html?view=joint&param=828 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yifeng Zhang](https://dblp.org/pid/88/2666.html)

[\[j219\]](https://dblp.org/pid/98/6127.html#j219) [\[c125\]](https://dblp.org/pid/98/6127.html#c125) [\[i99\]](https://dblp.org/pid/98/6127.html#i99)

[829](https://dblp.org/pid/98/6127.html?view=joint&param=829 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yisi Zhang](https://dblp.org/pid/318/0710.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[830](https://dblp.org/pid/98/6127.html?view=joint&param=830 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yongdong Zhang 0001](https://dblp.org/pid/z/YongdongZhang.html)

[\[c91\]](https://dblp.org/pid/98/6127.html#c91) [\[i43\]](https://dblp.org/pid/98/6127.html#i43)

[831](https://dblp.org/pid/98/6127.html?view=joint&param=831 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuesong Zhang](https://dblp.org/pid/155/5084.html)

[\[c108\]](https://dblp.org/pid/98/6127.html#c108) [\[i84\]](https://dblp.org/pid/98/6127.html#i84)

[832](https://dblp.org/pid/98/6127.html?view=joint&param=832 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhang Zhang 0001](https://dblp.org/pid/94/2468-1.html)

[\[j184\]](https://dblp.org/pid/98/6127.html#j184)

[833](https://dblp.org/pid/98/6127.html?view=joint&param=833 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhipeng Zhang](https://dblp.org/pid/49/4941.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[834](https://dblp.org/pid/98/6127.html?view=joint&param=834 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhixiong Zhang](https://dblp.org/pid/12/1950.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[835](https://dblp.org/pid/98/6127.html?view=joint&param=835 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhongfei Zhang](https://dblp.org/pid/z/ZhongfeiMarkZhang.html)

[\[j232\]](https://dblp.org/pid/98/6127.html#j232) [\[j215\]](https://dblp.org/pid/98/6127.html#j215) [\[j212\]](https://dblp.org/pid/98/6127.html#j212) [\[j162\]](https://dblp.org/pid/98/6127.html#j162) [\[i58\]](https://dblp.org/pid/98/6127.html#i58) [\[c78\]](https://dblp.org/pid/98/6127.html#c78) [\[i15\]](https://dblp.org/pid/98/6127.html#i15)

[836](https://dblp.org/pid/98/6127.html?view=joint&param=836 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bingrui Zhao](https://dblp.org/pid/327/1173.html)

[\[j261\]](https://dblp.org/pid/98/6127.html#j261)

[837](https://dblp.org/pid/98/6127.html?view=joint&param=837 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bo Zhao 0037](https://dblp.org/pid/94/4810-37.html)

[\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i75\]](https://dblp.org/pid/98/6127.html#i75)

[838](https://dblp.org/pid/98/6127.html?view=joint&param=838 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fang Zhao 0006](https://dblp.org/pid/72/4898-6.html)

[\[j203\]](https://dblp.org/pid/98/6127.html#j203) [\[j191\]](https://dblp.org/pid/98/6127.html#j191)

[839](https://dblp.org/pid/98/6127.html?view=joint&param=839 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiaojiao Zhao](https://dblp.org/pid/150/4197.html)

[\[j108\]](https://dblp.org/pid/98/6127.html#j108) [\[i21\]](https://dblp.org/pid/98/6127.html#i21) [\[j52\]](https://dblp.org/pid/98/6127.html#j52) [\[c46\]](https://dblp.org/pid/98/6127.html#c46) [\[i8\]](https://dblp.org/pid/98/6127.html#i8)

[840](https://dblp.org/pid/98/6127.html?view=joint&param=840 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Juanping Zhao](https://dblp.org/pid/120/5177.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[841](https://dblp.org/pid/98/6127.html?view=joint&param=841 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shengjie Zhao 0001](https://dblp.org/pid/47/5183-1.html)

[\[j115\]](https://dblp.org/pid/98/6127.html#j115)

[842](https://dblp.org/pid/98/6127.html?view=joint&param=842 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shenlu Zhao](https://dblp.org/pid/300/5768.html)

[\[j253\]](https://dblp.org/pid/98/6127.html#j253) [\[j247\]](https://dblp.org/pid/98/6127.html#j247) [\[j186\]](https://dblp.org/pid/98/6127.html#j186) [\[c86\]](https://dblp.org/pid/98/6127.html#c86)

[843](https://dblp.org/pid/98/6127.html?view=joint&param=843 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Sicheng Zhao](https://dblp.org/pid/65/10574.html)

[\[j271\]](https://dblp.org/pid/98/6127.html#j271) [\[j230\]](https://dblp.org/pid/98/6127.html#j230) [\[j226\]](https://dblp.org/pid/98/6127.html#j226) [\[j219\]](https://dblp.org/pid/98/6127.html#j219) [\[c125\]](https://dblp.org/pid/98/6127.html#c125) [\[c124\]](https://dblp.org/pid/98/6127.html#c124) [\[c120\]](https://dblp.org/pid/98/6127.html#c120) [\[c118\]](https://dblp.org/pid/98/6127.html#c118) [\[i102\]](https://dblp.org/pid/98/6127.html#i102) [\[i99\]](https://dblp.org/pid/98/6127.html#i99) [\[i98\]](https://dblp.org/pid/98/6127.html#i98) [\[i72\]](https://dblp.org/pid/98/6127.html#i72) [\[i56\]](https://dblp.org/pid/98/6127.html#i56) [\[i53\]](https://dblp.org/pid/98/6127.html#i53) [\[j100\]](https://dblp.org/pid/98/6127.html#j100) [\[j90\]](https://dblp.org/pid/98/6127.html#j90) [\[c82\]](https://dblp.org/pid/98/6127.html#c82) [\[j89\]](https://dblp.org/pid/98/6127.html#j89) [\[j65\]](https://dblp.org/pid/98/6127.html#j65) [\[c72\]](https://dblp.org/pid/98/6127.html#c72) [\[c56\]](https://dblp.org/pid/98/6127.html#c56) [\[j46\]](https://dblp.org/pid/98/6127.html#j46) [\[c50\]](https://dblp.org/pid/98/6127.html#c50) [\[c43\]](https://dblp.org/pid/98/6127.html#c43) [\[c41\]](https://dblp.org/pid/98/6127.html#c41) [\[c37\]](https://dblp.org/pid/98/6127.html#c37) [\[j41\]](https://dblp.org/pid/98/6127.html#j41) [\[c34\]](https://dblp.org/pid/98/6127.html#c34) [\[c26\]](https://dblp.org/pid/98/6127.html#c26) [\[c25\]](https://dblp.org/pid/98/6127.html#c25)

[844](https://dblp.org/pid/98/6127.html?view=joint&param=844 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaowei Zhao 0002](https://dblp.org/pid/02/8134-2.html)

[\[j237\]](https://dblp.org/pid/98/6127.html#j237)

[845](https://dblp.org/pid/98/6127.html?view=joint&param=845 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xin Zhao 0020](https://dblp.org/pid/68/2766-20.html)

[\[j275\]](https://dblp.org/pid/98/6127.html#j275) [\[j100\]](https://dblp.org/pid/98/6127.html#j100) [\[c69\]](https://dblp.org/pid/98/6127.html#c69) [\[c52\]](https://dblp.org/pid/98/6127.html#c52) [\[c27\]](https://dblp.org/pid/98/6127.html#c27)

[846](https://dblp.org/pid/98/6127.html?view=joint&param=846 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yanyun Zhao](https://dblp.org/pid/12/7547.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[847](https://dblp.org/pid/98/6127.html?view=joint&param=847 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuxiao Zhao](https://dblp.org/pid/68/875.html)

[\[j110\]](https://dblp.org/pid/98/6127.html#j110)

[848](https://dblp.org/pid/98/6127.html?view=joint&param=848 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhiyou Zhao](https://dblp.org/pid/331/8216.html)

[\[j170\]](https://dblp.org/pid/98/6127.html#j170) [\[i42\]](https://dblp.org/pid/98/6127.html#i42)

[849](https://dblp.org/pid/98/6127.html?view=joint&param=849 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiantong Zhen](https://dblp.org/pid/78/10651.html)

[\[j129\]](https://dblp.org/pid/98/6127.html#j129) [\[j97\]](https://dblp.org/pid/98/6127.html#j97) [\[c71\]](https://dblp.org/pid/98/6127.html#c71) [\[i11\]](https://dblp.org/pid/98/6127.html#i11)

[850](https://dblp.org/pid/98/6127.html?view=joint&param=850 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Dandan Zheng](https://dblp.org/pid/41/5401.html)

[\[i89\]](https://dblp.org/pid/98/6127.html#i89)

[851](https://dblp.org/pid/98/6127.html?view=joint&param=851 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Feng Zheng 0001](https://dblp.org/pid/39/800-1.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110) [\[c109\]](https://dblp.org/pid/98/6127.html#c109) [\[i76\]](https://dblp.org/pid/98/6127.html#i76) [\[i75\]](https://dblp.org/pid/98/6127.html#i75) [\[j183\]](https://dblp.org/pid/98/6127.html#j183) [\[j176\]](https://dblp.org/pid/98/6127.html#j176) [\[j171\]](https://dblp.org/pid/98/6127.html#j171) [\[j53\]](https://dblp.org/pid/98/6127.html#j53)

[852](https://dblp.org/pid/98/6127.html?view=joint&param=852 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Liang Zheng](https://dblp.org/pid/61/7360.html)

[\[j275\]](https://dblp.org/pid/98/6127.html#j275)

[853](https://dblp.org/pid/98/6127.html?view=joint&param=853 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiaoyu Zheng](https://dblp.org/pid/20/3589.html)

[\[c75\]](https://dblp.org/pid/98/6127.html#c75) [\[j85\]](https://dblp.org/pid/98/6127.html#j85) [\[c54\]](https://dblp.org/pid/98/6127.html#c54)

[854](https://dblp.org/pid/98/6127.html?view=joint&param=854 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yaozong Zheng](https://dblp.org/pid/344/6907.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[855](https://dblp.org/pid/98/6127.html?view=joint&param=855 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[856](https://dblp.org/pid/98/6127.html?view=joint&param=856 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Huasong Zhong](https://dblp.org/pid/227/3501.html)

[\[i110\]](https://dblp.org/pid/98/6127.html#i110)

[857](https://dblp.org/pid/98/6127.html?view=joint&param=857 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jing Zhong](https://dblp.org/pid/09/2522.html)

[\[j113\]](https://dblp.org/pid/98/6127.html#j113) [\[c38\]](https://dblp.org/pid/98/6127.html#c38)

[858](https://dblp.org/pid/98/6127.html?view=joint&param=858 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fei Zhou 0009](https://dblp.org/pid/84/5639-9.html)

[\[i116\]](https://dblp.org/pid/98/6127.html#i116) [\[i97\]](https://dblp.org/pid/98/6127.html#i97)

[859](https://dblp.org/pid/98/6127.html?view=joint&param=859 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jile Zhou](https://dblp.org/pid/147/9084.html)

[\[j41\]](https://dblp.org/pid/98/6127.html#j41)

[860](https://dblp.org/pid/98/6127.html?view=joint&param=860 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jinglin Zhou](https://dblp.org/pid/48/6808.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[861](https://dblp.org/pid/98/6127.html?view=joint&param=861 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jun Zhou](https://dblp.org/pid/99/3847.html)

[\[i89\]](https://dblp.org/pid/98/6127.html#i89)

[862](https://dblp.org/pid/98/6127.html?view=joint&param=862 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Junbao Zhou](https://dblp.org/pid/340/7404.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[863](https://dblp.org/pid/98/6127.html?view=joint&param=863 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jundong Zhou](https://dblp.org/pid/263/7754.html)

[\[c97\]](https://dblp.org/pid/98/6127.html#c97)

[864](https://dblp.org/pid/98/6127.html?view=joint&param=864 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Ling Zhou 0002](https://dblp.org/pid/86/949-2.html)

[\[j192\]](https://dblp.org/pid/98/6127.html#j192)

[865](https://dblp.org/pid/98/6127.html?view=joint&param=865 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Peicheng Zhou](https://dblp.org/pid/153/9172.html)

[\[j26\]](https://dblp.org/pid/98/6127.html#j26)

[866](https://dblp.org/pid/98/6127.html?view=joint&param=866 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Siyue Zhou](https://dblp.org/pid/218/9477.html)

[\[c36\]](https://dblp.org/pid/98/6127.html#c36)

[867](https://dblp.org/pid/98/6127.html?view=joint&param=867 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wei Zhou 0019](https://dblp.org/pid/69/5011-19.html)

[\[c123\]](https://dblp.org/pid/98/6127.html#c123) [\[i114\]](https://dblp.org/pid/98/6127.html#i114)

[868](https://dblp.org/pid/98/6127.html?view=joint&param=868 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Wei Zhou 0021](https://dblp.org/pid/69/5011-21.html)

[\[c119\]](https://dblp.org/pid/98/6127.html#c119) [\[i95\]](https://dblp.org/pid/98/6127.html#i95)

[869](https://dblp.org/pid/98/6127.html?view=joint&param=869 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xiangxin Zhou](https://dblp.org/pid/247/9275.html)

[\[c55\]](https://dblp.org/pid/98/6127.html#c55) [\[i14\]](https://dblp.org/pid/98/6127.html#i14)

[870](https://dblp.org/pid/98/6127.html?view=joint&param=870 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yikang Zhou](https://dblp.org/pid/337/1781.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[871](https://dblp.org/pid/98/6127.html?view=joint&param=871 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yizhuang Zhou](https://dblp.org/pid/315/9514.html)

[\[i49\]](https://dblp.org/pid/98/6127.html#i49)

[872](https://dblp.org/pid/98/6127.html?view=joint&param=872 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yong Zhou](https://dblp.org/pid/90/5836.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[873](https://dblp.org/pid/98/6127.html?view=joint&param=873 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Yuan Zhou 0023](https://dblp.org/pid/40/7018-23.html)

[\[i106\]](https://dblp.org/pid/98/6127.html#i106)

[874](https://dblp.org/pid/98/6127.html?view=joint&param=874 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zihan Zhou](https://dblp.org/pid/00/6525.html)

[\[j226\]](https://dblp.org/pid/98/6127.html#j226) [\[c120\]](https://dblp.org/pid/98/6127.html#c120) [\[i98\]](https://dblp.org/pid/98/6127.html#i98) [\[i94\]](https://dblp.org/pid/98/6127.html#i94)

[875](https://dblp.org/pid/98/6127.html?view=joint&param=875 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zikun Zhou](https://dblp.org/pid/271/8084.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[876](https://dblp.org/pid/98/6127.html?view=joint&param=876 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fengjie Zhu](https://dblp.org/pid/350/3991.html)

[\[i90\]](https://dblp.org/pid/98/6127.html#i90)

[877](https://dblp.org/pid/98/6127.html?view=joint&param=877 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Guibo Zhu](https://dblp.org/pid/125/2113.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[878](https://dblp.org/pid/98/6127.html?view=joint&param=878 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Hong Zhu 0006](https://dblp.org/pid/55/521-6.html)

[\[j128\]](https://dblp.org/pid/98/6127.html#j128)

[879](https://dblp.org/pid/98/6127.html?view=joint&param=879 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[880](https://dblp.org/pid/98/6127.html?view=joint&param=880 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lei Zhu 0002](https://dblp.org/pid/99/549-2.html)

[\[c28\]](https://dblp.org/pid/98/6127.html#c28)

[881](https://dblp.org/pid/98/6127.html?view=joint&param=881 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Pengfei Zhu 0001](https://dblp.org/pid/40/6172-1.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[882](https://dblp.org/pid/98/6127.html?view=joint&param=882 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Shengyin Zhu](https://dblp.org/pid/234/1707.html)

[\[c44\]](https://dblp.org/pid/98/6127.html#c44)

[883](https://dblp.org/pid/98/6127.html?view=joint&param=883 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Siyang Zhu](https://dblp.org/pid/206/2887.html)

[\[j43\]](https://dblp.org/pid/98/6127.html#j43)

[884](https://dblp.org/pid/98/6127.html?view=joint&param=884 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[885](https://dblp.org/pid/98/6127.html?view=joint&param=885 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zhanxing Zhu](https://dblp.org/pid/87/7756.html)

[\[j92\]](https://dblp.org/pid/98/6127.html#j92)

[886](https://dblp.org/pid/98/6127.html?view=joint&param=886 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Zining Zhu 0004](https://dblp.org/pid/378/1808.html)

[\[i77\]](https://dblp.org/pid/98/6127.html#i77)

[887](https://dblp.org/pid/98/6127.html?view=joint&param=887 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Lian Zhuo](https://dblp.org/pid/218/5220.html)

[\[j97\]](https://dblp.org/pid/98/6127.html#j97) [\[i11\]](https://dblp.org/pid/98/6127.html#i11)

[888](https://dblp.org/pid/98/6127.html?view=joint&param=888 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Changqing Zou](https://dblp.org/pid/126/1043.html)

[\[i9\]](https://dblp.org/pid/98/6127.html#i9)

[889](https://dblp.org/pid/98/6127.html?view=joint&param=889 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Vladimir V. Zunin](https://dblp.org/pid/372/7918.html)

[\[c110\]](https://dblp.org/pid/98/6127.html#c110)

[890](https://dblp.org/pid/98/6127.html?view=joint&param=890 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/98/6127.html?view=group&param=1)

[Fei Zuo](https://dblp.org/pid/08/2047.html)

[\[j20\]](https://dblp.org/pid/98/6127.html#j20)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/98/6127.html#) [\[–\]](https://dblp.org/pid/98/6127.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/98/6127.html#) [\[–\]](https://dblp.org/pid/98/6127.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/98/6127.html#) [\[–\]](https://dblp.org/pid/98/6127.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/98/6127.html#) [\[–\]](https://dblp.org/pid/98/6127.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/98/6127.html#) [\[–\]](https://dblp.org/pid/98/6127.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)