> 抓取来源：https://dblp.org/pid/158/1357.html

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

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Biyun+Sheng%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F158%2F1357%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Biyun+Sheng+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F158%2F1357%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Biyun+Sheng+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F158%2F1357%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Biyun+Sheng%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F158%2F1357%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Biyun+Sheng+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F158%2F1357%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Biyun+Sheng%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F158%2F1357%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Biyun+Sheng%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F158%2F1357%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F158%2F1357%3E+%7D+.%0A%0A%7D)

_showing all49 records_

20142026102014: 12015: 32015: 32016: 22016: 22017: 12018: 12019: 12020: 72020: 72021: 12022: 32023: 92023: 92024: 102024: 102024: 102025: 62025: 62026: 4

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

- ![](https://dblp.org/img/add-mark.12x12.png)Fu Xiao 0001 (39)
- ![](https://dblp.org/img/add-mark.12x12.png)Linqing Gui (17)
- ![](https://dblp.org/img/add-mark.12x12.png)Zhengxin Guo (15)
- ![](https://dblp.org/img/add-mark.12x12.png)Hui Cai (11)
- ![](https://dblp.org/img/add-mark.12x12.png)Wankou Yang (9)
- ![](https://dblp.org/img/add-mark.12x12.png)Changyin Sun 0001 (8)
- ![](https://dblp.org/img/add-mark.12x12.png)Yiping Zuo (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Lijuan Sun (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Shi Jin 0002 (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Jiajia Guo 0001 (5)

- _54 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-5006-3822 (28)
- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (20)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-6462-9532 (1)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Mob. Comput. (6)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Veh. Technol. (4)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Internet Things J. (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Neurocomputing (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Syst. J. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Circuits Syst. Video Technol. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)ACM Trans. Sens. Networks (2)
- ![](https://dblp.org/img/add-mark.12x12.png)ACM TUR-C (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. (2)

- _18 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (46)
- ![](https://dblp.org/img/add-mark.12x12.png)open (3)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[j35\]
[Hui Cai](https://dblp.org/pid/09/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chen Lan](https://dblp.org/pid/203/5284.html), [Yuanyuan Yang](https://dblp.org/pid/10/2031-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanmin Zhu](https://dblp.org/pid/25/8709-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhou](https://dblp.org/pid/97/97-9.html)![](https://dblp.org/img/orcid-mark.12x12.png), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png):

Toward Personalized Location Privacy Trading for Mobile Crowd Sensing. [IEEE Trans. Dependable Secur. Comput.23(1)](https://dblp.org/db/journals/tdsc/tdsc23.html#journals/tdsc/CaiLYXZZS26): 1439-1453 (2026)
- ![](https://dblp.org/img/n.png)

\[j34\]
[Hui Cai](https://dblp.org/pid/09/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chen Lan](https://dblp.org/pid/203/5284.html), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhou](https://dblp.org/pid/97/97-9.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuanyuan Yang](https://dblp.org/pid/10/2031-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yanmin Zhu](https://dblp.org/pid/25/8709-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

ADGTrace: Achieving Adaptive Trajectory Synthesis With Generated Data. [IEEE Trans. Mob. Comput.25(1)](https://dblp.org/db/journals/tmc/tmc25.html#journals/tmc/CaiLSZYZX26): 148-163 (2026)
- ![](https://dblp.org/img/n.png)

\[j33\]
[Yiping Zuo](https://dblp.org/pid/198/1473.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weicong Chen](https://dblp.org/pid/194/1786.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiajia Guo](https://dblp.org/pid/163/8752-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weibei Fan](https://dblp.org/pid/202/3794.html)![](https://dblp.org/img/orcid-mark.12x12.png), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Shi Jin](https://dblp.org/pid/49/5340-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Fluid Antenna-Enabled Integrated Sensing, Communication, and Computing Systems With Mobile Blockchain. [IEEE Trans. Netw. Sci. Eng.13](https://dblp.org/db/journals/tnse/tnse13.html#journals/tnse/ZuoCGFSJ26): 3720-3738 (2026)
- ![](https://dblp.org/img/n.png)

\[j32\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Pengju Ding](https://dblp.org/pid/344/6870.html), [Hui Cai](https://dblp.org/pid/09/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chuyu Wang](https://dblp.org/pid/145/0641.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tie Qiu](https://dblp.org/pid/53/9359.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Toward Adaptive Person Re-Identification via mmWave Radar Point Clouds. [IEEE Trans. Netw.34](https://dblp.org/db/journals/ton/ton34.html#journals/ton/ShengDCWXQ26): 2047-2060 (2026)
- 2025
- ![](https://dblp.org/img/n.png)

\[j31\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Shuqi Sun](https://dblp.org/pid/21/9088.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Cai](https://dblp.org/pid/09/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chen Dai](https://dblp.org/pid/130/9868.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

From Coarse to Fine: Fast and Effortless Facial Landmark Detection via mmWave Signals. [Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.9(4)](https://dblp.org/db/journals/imwut/imwut9.html#journals/imwut/ShengSCDX25): 208:1-208:25 (2025)
- ![](https://dblp.org/img/n.png)

\[j30\]
[Chong Han](https://dblp.org/pid/65/8230-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Siyu Chen](https://dblp.org/pid/23/7930.html), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Guo](https://dblp.org/pid/96/2596-6.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lijuan Sun](https://dblp.org/pid/39/478.html)![](https://dblp.org/img/orcid-mark.12x12.png):

mmReID: Person Reidentification Based on Commodity Millimeter-Wave Radar. [IEEE Internet Things J.12(13)](https://dblp.org/db/journals/iotj/iotj12.html#journals/iotj/HanCSGS25): 24057-24070 (2025)
- ![](https://dblp.org/img/n.png)

\[j29\]
[Xiao Fang](https://dblp.org/pid/84/204.html), [Hui Cai](https://dblp.org/pid/09/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Juan Li](https://dblp.org/pid/59/2144-11.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhou](https://dblp.org/pid/97/97-9.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haiping Huang](https://dblp.org/pid/22/6402.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mang Ye](https://dblp.org/pid/156/0610.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Blockchain-Based Secure and Fair Online Incentive Mechanism for Crowdsensed Data Trading. [IEEE Trans. Inf. Forensics Secur.20](https://dblp.org/db/journals/tifs/tifs20.html#journals/tifs/FangCSLZHYX25): 9372-9386 (2025)
- ![](https://dblp.org/img/n.png)

\[j28\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Yan Bao](https://dblp.org/pid/88/8492.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Cai](https://dblp.org/pid/09/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Linqing Gui](https://dblp.org/pid/28/10607.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

I Sense You Fast: Simultaneous Action and Identity Inference by Slimming Multi-Branch RadarNet. [IEEE Trans. Mob. Comput.24(10)](https://dblp.org/db/journals/tmc/tmc24.html#journals/tmc/ShengBCGX25): 10743-10759 (2025)
- ![](https://dblp.org/img/n.png)

\[j27\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Jiabin Li](https://dblp.org/pid/43/5182.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Cai](https://dblp.org/pid/09/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yiping Zuo](https://dblp.org/pid/198/1473.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Li Lu](https://dblp.org/pid/49/2793-8.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

mmZeAR: Zero-Effort Cross-Category Action Recognition With mmWave Radar. [IEEE Trans. Mob. Comput.24(10)](https://dblp.org/db/journals/tmc/tmc24.html#journals/tmc/ShengLCZLX25): 11164-11179 (2025)
- ![](https://dblp.org/img/n.png)

\[c11\]
[Jinming Ju](https://dblp.org/pid/415/8095.html), [Hui Cai](https://dblp.org/pid/09/8662.html), [Tianyang Zhou](https://dblp.org/pid/160/4707.html), Biyun Sheng, [Jian Zhou](https://dblp.org/pid/97/97-9.html), [Weibei Fan](https://dblp.org/pid/202/3794.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html):

Correlation-Aware Multi-Similarity Learning for Federated Human Activity Recognition. [IWQoS2025](https://dblp.org/db/conf/iwqos/iwqos2025.html#conf/iwqos/JuCZSZFX25): 1-10
- 2024
- ![](https://dblp.org/img/n.png)

\[j26\]
[Yiping Zuo](https://dblp.org/pid/198/1473.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiajia Guo](https://dblp.org/pid/163/8752-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Chen Dai](https://dblp.org/pid/130/9868.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shi Jin](https://dblp.org/pid/49/5340-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Fluid Antenna for Mobile Edge Computing. [IEEE Commun. Lett.28(7)](https://dblp.org/db/journals/icl/icl28.html#journals/icl/ZuoGSDXJ24): 1728-1732 (2024)
- ![](https://dblp.org/img/n.png)

\[j25\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Rui Han](https://dblp.org/pid/87/7513.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhengxin Guo](https://dblp.org/pid/203/9349.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Linqing Gui](https://dblp.org/pid/28/10607.html)![](https://dblp.org/img/orcid-mark.12x12.png):

MetaFormer: Domain-Adaptive WiFi Sensing with Only One Labelled Target Sample. [Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.8(1)](https://dblp.org/db/journals/imwut/imwut8.html#journals/imwut/ShengHXGG24): 39:1-39:27 (2024)
- ![](https://dblp.org/img/n.png)

\[j24\]
[Cheng Peng](https://dblp.org/pid/82/3044-19.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Linqing Gui](https://dblp.org/pid/28/10607.html)![](https://dblp.org/img/orcid-mark.12x12.png), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Zhengxin Guo](https://dblp.org/pid/203/9349.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

RoSeFi: A Robust Sedentary Behavior Monitoring System With Commodity WiFi Devices. [IEEE Trans. Mob. Comput.23(5)](https://dblp.org/db/journals/tmc/tmc23.html#journals/tmc/PengGSGX24): 6470-6489 (2024)
- ![](https://dblp.org/img/n.png)

\[j23\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Rui Han](https://dblp.org/pid/87/7513.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Cai](https://dblp.org/pid/09/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Linqing Gui](https://dblp.org/pid/28/10607.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhengxin Guo](https://dblp.org/pid/203/9349.html)![](https://dblp.org/img/orcid-mark.12x12.png):

CDFi: Cross-Domain Action Recognition Using WiFi Signals. [IEEE Trans. Mob. Comput.23(8)](https://dblp.org/db/journals/tmc/tmc23.html#journals/tmc/ShengHCXGG24): 8463-8477 (2024)
- ![](https://dblp.org/img/n.png)

\[j22\]
[Zhengxin Guo](https://dblp.org/pid/203/9349.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dongzi Wang](https://dblp.org/pid/275/7735.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Linqing Gui](https://dblp.org/pid/28/10607.html)![](https://dblp.org/img/orcid-mark.12x12.png), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Cai](https://dblp.org/pid/09/8662.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jinsong Han](https://dblp.org/pid/96/6606.html)![](https://dblp.org/img/orcid-mark.12x12.png):

UWTracking: Passive Human Tracking Under LOS/NLOS Scenarios Using IR-UWB Radar. [IEEE Trans. Mob. Comput.23(12)](https://dblp.org/db/journals/tmc/tmc23.html#journals/tmc/GuoWGSCXH24): 11853-11870 (2024)
- ![](https://dblp.org/img/n.png)

\[j21\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Jiabin Li](https://dblp.org/pid/43/5182.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Linqing Gui](https://dblp.org/pid/28/10607.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhengxin Guo](https://dblp.org/pid/203/9349.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

LiteWiSys: A Lightweight System for WiFi-based Dual-task Action Perception. [ACM Trans. Sens. Networks20(4)](https://dblp.org/db/journals/tosn/tosn20.html#journals/tosn/ShengLGGX24): 78:1-78:19 (2024)
- ![](https://dblp.org/img/n.png)

\[j20\]
[Yimin Mao](https://dblp.org/pid/219/5149.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhengxin Guo](https://dblp.org/pid/203/9349.html)![](https://dblp.org/img/orcid-mark.12x12.png), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Linqing Gui](https://dblp.org/pid/28/10607.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Wi-Cro: WiFi-Based Cross Domain Activity Recognition via Modified GAN. [IEEE Trans. Veh. Technol.73(10)](https://dblp.org/db/journals/tvt/tvt73.html#journals/tvt/MaoGSGX24): 14961-14973 (2024)
- ![](https://dblp.org/img/n.png)

\[c10\]
[Yiping Zuo](https://dblp.org/pid/198/1473.html), [Jiajia Guo](https://dblp.org/pid/163/8752-1.html), [Weicong Chen](https://dblp.org/pid/194/1786.html), [Weibei Fan](https://dblp.org/pid/202/3794.html), Biyun Sheng, [Fu Xiao](https://dblp.org/pid/91/8079-1.html), [Shi Jin](https://dblp.org/pid/49/5340-2.html):

Fluid Antenna-enabled Integrated Sensing, Communication, and Computing Systems. [WCSP2024](https://dblp.org/db/conf/wcsp/wcsp2024.html#conf/wcsp/ZuoGCFS0024): 900-905
- ![](https://dblp.org/img/n.png)

\[i3\]
[Yiping Zuo](https://dblp.org/pid/198/1473.html), [Jiajia Guo](https://dblp.org/pid/163/8752-1.html), Biyun Sheng, [Chen Dai](https://dblp.org/pid/130/9868.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html), [Shi Jin](https://dblp.org/pid/49/5340-2.html):

Fluid Antenna for Mobile Edge Computing. [CoRRabs/2403.11806](https://dblp.org/db/journals/corr/corr2403.html#journals/corr/abs-2403-11806) (2024)
- ![](https://dblp.org/img/n.png)

\[i2\]
[Yiping Zuo](https://dblp.org/pid/198/1473.html), [Jiajia Guo](https://dblp.org/pid/163/8752-1.html), [Weicong Chen](https://dblp.org/pid/194/1786.html), [Weibei Fan](https://dblp.org/pid/202/3794.html), Biyun Sheng, [Fu Xiao](https://dblp.org/pid/91/8079-1.html), [Shi Jin](https://dblp.org/pid/49/5340-2.html):

Fluid Antenna-enabled Integrated Sensing, Communication, and Computing Systems. [CoRRabs/2409.11622](https://dblp.org/db/journals/corr/corr2409.html#journals/corr/abs-2409-11622) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j19\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Chaorun Sun](https://dblp.org/pid/348/8186.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Linqing Gui](https://dblp.org/pid/28/10607.html), [Zhengxin Guo](https://dblp.org/pid/203/9349.html):

MuAt-Va: Multi-Attention and Video-Auxiliary Network for Device-Free Action Recognition. [IEEE Internet Things J.10(12)](https://dblp.org/db/journals/iotj/iotj10.html#journals/iotj/ShengSXGG23): 10870-10880 (2023)
- ![](https://dblp.org/img/n.png)

\[j18\]
[Linqing Gui](https://dblp.org/pid/28/10607.html), [Chunzhe Ma](https://dblp.org/pid/349/8460.html), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Zhengxin Guo](https://dblp.org/pid/203/9349.html), [Jun Cai](https://dblp.org/pid/72/3887-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

In-Home Monitoring Sleep Turnover Activities and Breath Rate via WiFi Signals. [IEEE Syst. J.17(2)](https://dblp.org/db/journals/sj/sj17.html#journals/sj/GuiMSGCX23): 2355-2365 (2023)
- ![](https://dblp.org/img/n.png)

\[j17\]
[Zhengxin Guo](https://dblp.org/pid/203/9349.html), [Xu Zhu](https://dblp.org/pid/65/2899.html), [Linqing Gui](https://dblp.org/pid/28/10607.html), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

BreathID: Respiration Sensing for Human Identification Using Commodity Wi-Fi. [IEEE Syst. J.17(2)](https://dblp.org/db/journals/sj/sj17.html#journals/sj/GuoZGSX23): 3059-3070 (2023)
- ![](https://dblp.org/img/n.png)

\[j16\]
[Mingming Xu](https://dblp.org/pid/43/6921-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhengxin Guo](https://dblp.org/pid/203/9349.html), [Linqing Gui](https://dblp.org/pid/28/10607.html), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

WiSPE: A COTS Wi-Fi-Based 2-D Static Human Pose Estimation. [IEEE Syst. J.17(3)](https://dblp.org/db/journals/sj/sj17.html#journals/sj/XuGGSX23): 3560-3571 (2023)
- ![](https://dblp.org/img/n.png)

\[j15\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Linqing Gui](https://dblp.org/pid/28/10607.html), [Zhengxin Guo](https://dblp.org/pid/203/9349.html):

Context-Aware Faster RCNN for CSI-Based Human Action Perception. [IEEE Trans. Hum. Mach. Syst.53(2)](https://dblp.org/db/journals/thms/thms53.html#journals/thms/ShengXGG23): 438-448 (2023)
- ![](https://dblp.org/img/n.png)

\[j14\]
[Zhengxin Guo](https://dblp.org/pid/203/9349.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenyang Yuan](https://dblp.org/pid/324/4067.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Linqing Gui](https://dblp.org/pid/28/10607.html)![](https://dblp.org/img/orcid-mark.12x12.png), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

BreatheBand: A Fine-grained and Robust Respiration Monitor System Using WiFi Signals. [ACM Trans. Sens. Networks19(4)](https://dblp.org/db/journals/tosn/tosn19.html#journals/tosn/GuoYGSX23): 82:1-82:18 (2023)
- ![](https://dblp.org/img/n.png)

\[c9\]
[Zhicheng Xu](https://dblp.org/pid/39/1625.html), [Ling Deng](https://dblp.org/pid/125/7750.html), Biyun Sheng, [Linqing Gui](https://dblp.org/pid/28/10607.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html):

Efficient Respiration Rate Estimation Based on MIMO mmWave Radar. [ICA3PP (3)2023](https://dblp.org/db/conf/ica3pp/ica3pp2023-3.html#conf/ica3pp/XuDSGX23): 423-442
- ![](https://dblp.org/img/n.png)

\[c8\]
Biyun Sheng, [Yan Bao](https://dblp.org/pid/88/8492.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html), [Linqing Gui](https://dblp.org/pid/28/10607.html):

DyLiteRADHAR: Dynamic Lightweight Slowfast Network for Human Activity Recognition Using MMWAVE Radar. [ICASSP2023](https://dblp.org/db/conf/icassp/icassp2023.html#conf/icassp/ShengBXG23): 1-5
- ![](https://dblp.org/img/n.png)

\[c7\]
[Linqing Gui](https://dblp.org/pid/28/10607.html), [Ling Deng](https://dblp.org/pid/125/7750.html), [Cheng Peng](https://dblp.org/pid/82/3044-19.html), [Hui Cai](https://dblp.org/pid/09/8662.html), Biyun Sheng, [Zhengxin Guo](https://dblp.org/pid/203/9349.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html):

MMHeart: An Efficient Heartbeat Monitoring System Based on MIMO mmWave Radar. [MSN2023](https://dblp.org/db/conf/msn/msn2023.html#conf/msn/GuiDPCSG023): 1-8
- 2022
- ![](https://dblp.org/img/n.png)

\[j13\]
[Yuanrun Fang](https://dblp.org/pid/270/6267.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html), Biyun Sheng, [Letian Sha](https://dblp.org/pid/184/0402.html), [Lijuan Sun](https://dblp.org/pid/39/478.html):

Cross-scene passive human activity recognition using commodity WiFi. [Frontiers Comput. Sci.16(1)](https://dblp.org/db/journals/fcsc/fcsc16.html#journals/fcsc/FangXSSS22): 161502 (2022)
- ![](https://dblp.org/img/n.png)

\[j12\]
[Qun Li](https://dblp.org/pid/42/6066-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html), [Bir Bhanu](https://dblp.org/pid/b/BirBhanu.html), Biyun Sheng, [Richang Hong](https://dblp.org/pid/59/1501.html):

Inner Knowledge-based Img2Doc Scheme for Visual Question Answering. [ACM Trans. Multim. Comput. Commun. Appl.18(3)](https://dblp.org/db/journals/tomccap/tomccap18.html#journals/tomccap/LiXBSH22): 76:1-76:21 (2022)
- ![](https://dblp.org/img/n.png)

\[j11\]
[Zhengxin Guo](https://dblp.org/pid/203/9349.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Lijuan Sun](https://dblp.org/pid/39/478.html), [Shui Yu](https://dblp.org/pid/90/3575-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

TWCC: A Robust Through-the-Wall Crowd Counting System Using Ambient WiFi Signals. [IEEE Trans. Veh. Technol.71(4)](https://dblp.org/db/journals/tvt/tvt71.html#journals/tvt/GuoXSSY22): 4198-4211 (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[c6\]
Biyun Sheng, [Linqing Gui](https://dblp.org/pid/28/10607.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html):

TS-Net: Device-Free Action Recognition with Cross-Modal Learning. [WASA (1)2021](https://dblp.org/db/conf/wasa/wasa2021-1.html#conf/wasa/ShengGX21): 404-415
- 2020
- ![](https://dblp.org/img/n.png)

\[j10\]
Biyun Sheng, [Jun Li](https://dblp.org/pid/116/1011.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wankou Yang](https://dblp.org/pid/99/3602.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Multilayer deep features with multiple kernel learning for action recognition. [Neurocomputing399](https://dblp.org/db/journals/ijon/ijon399.html#journals/ijon/ShengLXY20): 65-74 (2020)
- ![](https://dblp.org/img/n.png)

\[j9\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Letian Sha](https://dblp.org/pid/184/0402.html), [Lijuan Sun](https://dblp.org/pid/39/478.html):

Deep Spatial-Temporal Model Based Cross-Scene Action Recognition Using Commodity WiFi. [IEEE Internet Things J.7(4)](https://dblp.org/db/journals/iotj/iotj7.html#journals/iotj/ShengXSS20): 3592-3601 (2020)
- ![](https://dblp.org/img/n.png)

\[j8\]
[Zhengxin Guo](https://dblp.org/pid/203/9349.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Huan Fei](https://dblp.org/pid/247/5152.html), [Shui Yu](https://dblp.org/pid/90/3575-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

WiReader: Adaptive Air Handwriting Recognition Based on Commercial WiFi Signal. [IEEE Internet Things J.7(10)](https://dblp.org/db/journals/iotj/iotj7.html#journals/iotj/GuoXSFY20): 10483-10494 (2020)
- ![](https://dblp.org/img/n.png)

\[j7\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Li](https://dblp.org/pid/116/1011-33.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qun Li](https://dblp.org/pid/42/6066-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Junwei Han](https://dblp.org/pid/00/3003.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Discriminative Multi-View Subspace Feature Learning for Action Recognition. [IEEE Trans. Circuits Syst. Video Technol.30(12)](https://dblp.org/db/journals/tcsv/tcsv30.html#journals/tcsv/ShengLXLYH20): 4591-4600 (2020)
- ![](https://dblp.org/img/n.png)

\[j6\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Yuanrun Fang](https://dblp.org/pid/270/6267.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lijuan Sun](https://dblp.org/pid/39/478.html):

An Accurate Device-Free Action Recognition System Using Two-Stream Network. [IEEE Trans. Veh. Technol.69(7)](https://dblp.org/db/journals/tvt/tvt69.html#journals/tvt/ShengFXS20): 7930-7939 (2020)
- ![](https://dblp.org/img/n.png)

\[c5\]
[Yuanrun Fang](https://dblp.org/pid/270/6267.html), Biyun Sheng, [Haiyan Wang](https://dblp.org/pid/27/59-7.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html):

WiTransfer: A Cross-scene Transfer Activity Recognition System Using WiFi. [ACM TUR-C2020](https://dblp.org/db/conf/acmturc/acmturc2020.html#conf/acmturc/FangSWX20): 59-63
- ![](https://dblp.org/img/n.png)

\[c4\]
Biyun Sheng, [Fu Xiao](https://dblp.org/pid/91/8079-1.html), [Yuanrun Fang](https://dblp.org/pid/270/6267.html), [Haiyan Wang](https://dblp.org/pid/27/59-7.html):

WiFi Based Passive Action Recognition with Fully-connected Network. [ACM TUR-C2020](https://dblp.org/db/conf/acmturc/acmturc2020.html#conf/acmturc/ShengXFW20): 113-117
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j5\]
[Huan Fei](https://dblp.org/pid/247/5152.html), [Fu Xiao](https://dblp.org/pid/91/8079-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Haiping Huang](https://dblp.org/pid/22/6402.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Lijuan Sun](https://dblp.org/pid/39/478.html):

Motion Path Reconstruction in Indoor Environment Using Commodity Wi-Fi. [IEEE Trans. Veh. Technol.68(8)](https://dblp.org/db/journals/tvt/tvt68.html#journals/tvt/FeiXSHS19): 7668-7678 (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[j4\]
Biyun Sheng![](https://dblp.org/img/orcid-mark.12x12.png), [Chunhua Shen](https://dblp.org/pid/56/1673.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guosheng Lin](https://dblp.org/pid/126/4778.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Li](https://dblp.org/pid/116/1011-33.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Changyin Sun](https://dblp.org/pid/64/221.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Crowd Counting via Weighted VLAD on a Dense Attribute Feature Map. [IEEE Trans. Circuits Syst. Video Technol.28(8)](https://dblp.org/db/journals/tcsv/tcsv28.html#journals/tcsv/ShengSLLYS18): 1788-1797 (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[j3\]
Biyun Sheng, [Qichang Hu](https://dblp.org/pid/169/9980.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jun Li](https://dblp.org/pid/116/1011-33.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Filtered shallow-deep feature channels for pedestrian detection. [Neurocomputing249](https://dblp.org/db/journals/ijon/ijon249.html#journals/ijon/ShengHLYZS17): 19-27 (2017)
- 2016
- ![](https://dblp.org/img/n.png)

\[j2\]
[Hoangvu Nguyen](https://dblp.org/pid/160/2774.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wankou Yang](https://dblp.org/pid/99/3602.html), Biyun Sheng, [Changyin Sun](https://dblp.org/pid/64/221.html):

Discriminative low-rank dictionary learning for face recognition. [Neurocomputing173](https://dblp.org/db/journals/ijon/ijon173.html#journals/ijon/NguyenYSS16): 541-551 (2016)
- ![](https://dblp.org/img/n.png)

\[i1\]
Biyun Sheng, [Chunhua Shen](https://dblp.org/pid/56/1673.html), [Guosheng Lin](https://dblp.org/pid/126/4778.html), [Jun Li](https://dblp.org/pid/116/1011-33.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Crowd Counting via Weighted VLAD on Dense Attribute Feature Maps. [CoRRabs/1604.08660](https://dblp.org/db/journals/corr/corr1604.html#journals/corr/ShengSLLYS16) (2016)
- 2015
- ![](https://dblp.org/img/n.png)

\[j1\]
Biyun Sheng, [Wankou Yang](https://dblp.org/pid/99/3602.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Action recognition using direction-dependent feature pairs and non-negative low rank sparse model. [Neurocomputing158](https://dblp.org/db/journals/ijon/ijon158.html#journals/ijon/ShengYS15): 73-80 (2015)
- ![](https://dblp.org/img/n.png)

\[c3\]
Biyun Sheng, [Yan Yan](https://dblp.org/pid/13/3953-23.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Encoding spatio-temporal distribution by generalized VLAD for action recognition. [CCECE2015](https://dblp.org/db/conf/ccece/ccece2015.html#conf/ccece/ShengYS15): 620-625
- ![](https://dblp.org/img/n.png)

\[c2\]
[Jiayu Sheng](https://dblp.org/pid/169/4623.html), Biyun Sheng, [Wankou Yang](https://dblp.org/pid/99/3602.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Assigning PLS Based Descriptors by SVM in Action Recognition. [IScIDE (1)2015](https://dblp.org/db/conf/iscide/iscide2015-1.html#conf/iscide/ShengSYS15): 145-153
- 2014
- ![](https://dblp.org/img/n.png)

\[c1\]
Biyun Sheng, [Wankou Yang](https://dblp.org/pid/99/3602.html), [Baochang Zhang](https://dblp.org/pid/80/3887-1.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

A Non-negative Low Rank and Sparse Model for Action Recognition. [CCPR (2)2014](https://dblp.org/db/conf/ccpr/ccpr2014-2.html#conf/ccpr/ShengYZS14): 266-275
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/158/1357.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Yan Bao](https://dblp.org/pid/88/8492.html)

[\[j28\]](https://dblp.org/pid/158/1357.html#j28) [\[c8\]](https://dblp.org/pid/158/1357.html#c8)

[2](https://dblp.org/pid/158/1357.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Bir Bhanu](https://dblp.org/pid/b/BirBhanu.html)

[\[j12\]](https://dblp.org/pid/158/1357.html#j12)

[3](https://dblp.org/pid/158/1357.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Hui Cai](https://dblp.org/pid/09/8662.html)

[\[j35\]](https://dblp.org/pid/158/1357.html#j35) [\[j34\]](https://dblp.org/pid/158/1357.html#j34) [\[j32\]](https://dblp.org/pid/158/1357.html#j32) [\[j31\]](https://dblp.org/pid/158/1357.html#j31) [\[j29\]](https://dblp.org/pid/158/1357.html#j29) [\[j28\]](https://dblp.org/pid/158/1357.html#j28) [\[j27\]](https://dblp.org/pid/158/1357.html#j27) [\[c11\]](https://dblp.org/pid/158/1357.html#c11) [\[j23\]](https://dblp.org/pid/158/1357.html#j23) [\[j22\]](https://dblp.org/pid/158/1357.html#j22) [\[c7\]](https://dblp.org/pid/158/1357.html#c7)

[4](https://dblp.org/pid/158/1357.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Jun Cai 0001](https://dblp.org/pid/72/3887-1.html)

[\[j18\]](https://dblp.org/pid/158/1357.html#j18)

[5](https://dblp.org/pid/158/1357.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Siyu Chen](https://dblp.org/pid/23/7930.html)

[\[j30\]](https://dblp.org/pid/158/1357.html#j30)

[6](https://dblp.org/pid/158/1357.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Weicong Chen](https://dblp.org/pid/194/1786.html)

[\[j33\]](https://dblp.org/pid/158/1357.html#j33) [\[c10\]](https://dblp.org/pid/158/1357.html#c10) [\[i2\]](https://dblp.org/pid/158/1357.html#i2)

[7](https://dblp.org/pid/158/1357.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Chen Dai](https://dblp.org/pid/130/9868.html)

[\[j31\]](https://dblp.org/pid/158/1357.html#j31) [\[j26\]](https://dblp.org/pid/158/1357.html#j26) [\[i3\]](https://dblp.org/pid/158/1357.html#i3)

[8](https://dblp.org/pid/158/1357.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Ling Deng](https://dblp.org/pid/125/7750.html)

[\[c9\]](https://dblp.org/pid/158/1357.html#c9) [\[c7\]](https://dblp.org/pid/158/1357.html#c7)

[9](https://dblp.org/pid/158/1357.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Pengju Ding](https://dblp.org/pid/344/6870.html)

[\[j32\]](https://dblp.org/pid/158/1357.html#j32)

[10](https://dblp.org/pid/158/1357.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Weibei Fan](https://dblp.org/pid/202/3794.html)

[\[j33\]](https://dblp.org/pid/158/1357.html#j33) [\[c11\]](https://dblp.org/pid/158/1357.html#c11) [\[c10\]](https://dblp.org/pid/158/1357.html#c10) [\[i2\]](https://dblp.org/pid/158/1357.html#i2)

[11](https://dblp.org/pid/158/1357.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Xiao Fang](https://dblp.org/pid/84/204.html)

[\[j29\]](https://dblp.org/pid/158/1357.html#j29)

[12](https://dblp.org/pid/158/1357.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Yuanrun Fang](https://dblp.org/pid/270/6267.html)

[\[j13\]](https://dblp.org/pid/158/1357.html#j13) [\[j6\]](https://dblp.org/pid/158/1357.html#j6) [\[c5\]](https://dblp.org/pid/158/1357.html#c5) [\[c4\]](https://dblp.org/pid/158/1357.html#c4)

[13](https://dblp.org/pid/158/1357.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Huan Fei](https://dblp.org/pid/247/5152.html)

[\[j8\]](https://dblp.org/pid/158/1357.html#j8) [\[j5\]](https://dblp.org/pid/158/1357.html#j5)

[14](https://dblp.org/pid/158/1357.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Linqing Gui](https://dblp.org/pid/28/10607.html)

[\[j28\]](https://dblp.org/pid/158/1357.html#j28) [\[j25\]](https://dblp.org/pid/158/1357.html#j25) [\[j24\]](https://dblp.org/pid/158/1357.html#j24) [\[j23\]](https://dblp.org/pid/158/1357.html#j23) [\[j22\]](https://dblp.org/pid/158/1357.html#j22) [\[j21\]](https://dblp.org/pid/158/1357.html#j21) [\[j20\]](https://dblp.org/pid/158/1357.html#j20) [\[j19\]](https://dblp.org/pid/158/1357.html#j19) [\[j18\]](https://dblp.org/pid/158/1357.html#j18) [\[j17\]](https://dblp.org/pid/158/1357.html#j17) [\[j16\]](https://dblp.org/pid/158/1357.html#j16) [\[j15\]](https://dblp.org/pid/158/1357.html#j15) [\[j14\]](https://dblp.org/pid/158/1357.html#j14) [\[c9\]](https://dblp.org/pid/158/1357.html#c9) [\[c8\]](https://dblp.org/pid/158/1357.html#c8) [\[c7\]](https://dblp.org/pid/158/1357.html#c7) [\[c6\]](https://dblp.org/pid/158/1357.html#c6)

[15](https://dblp.org/pid/158/1357.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Jiajia Guo 0001](https://dblp.org/pid/163/8752-1.html)

[\[j33\]](https://dblp.org/pid/158/1357.html#j33) [\[j26\]](https://dblp.org/pid/158/1357.html#j26) [\[c10\]](https://dblp.org/pid/158/1357.html#c10) [\[i3\]](https://dblp.org/pid/158/1357.html#i3) [\[i2\]](https://dblp.org/pid/158/1357.html#i2)

[16](https://dblp.org/pid/158/1357.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Jian Guo 0006](https://dblp.org/pid/96/2596-6.html)

[\[j30\]](https://dblp.org/pid/158/1357.html#j30)

[17](https://dblp.org/pid/158/1357.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Zhengxin Guo](https://dblp.org/pid/203/9349.html)

[\[j25\]](https://dblp.org/pid/158/1357.html#j25) [\[j24\]](https://dblp.org/pid/158/1357.html#j24) [\[j23\]](https://dblp.org/pid/158/1357.html#j23) [\[j22\]](https://dblp.org/pid/158/1357.html#j22) [\[j21\]](https://dblp.org/pid/158/1357.html#j21) [\[j20\]](https://dblp.org/pid/158/1357.html#j20) [\[j19\]](https://dblp.org/pid/158/1357.html#j19) [\[j18\]](https://dblp.org/pid/158/1357.html#j18) [\[j17\]](https://dblp.org/pid/158/1357.html#j17) [\[j16\]](https://dblp.org/pid/158/1357.html#j16) [\[j15\]](https://dblp.org/pid/158/1357.html#j15) [\[j14\]](https://dblp.org/pid/158/1357.html#j14) [\[c7\]](https://dblp.org/pid/158/1357.html#c7) [\[j11\]](https://dblp.org/pid/158/1357.html#j11) [\[j8\]](https://dblp.org/pid/158/1357.html#j8)

[18](https://dblp.org/pid/158/1357.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Chong Han 0002](https://dblp.org/pid/65/8230-2.html)

[\[j30\]](https://dblp.org/pid/158/1357.html#j30)

[19](https://dblp.org/pid/158/1357.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Jinsong Han](https://dblp.org/pid/96/6606.html)

[\[j22\]](https://dblp.org/pid/158/1357.html#j22)

[20](https://dblp.org/pid/158/1357.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Junwei Han 0001](https://dblp.org/pid/00/3003.html)

[\[j7\]](https://dblp.org/pid/158/1357.html#j7)

[21](https://dblp.org/pid/158/1357.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Rui Han](https://dblp.org/pid/87/7513.html)

[\[j25\]](https://dblp.org/pid/158/1357.html#j25) [\[j23\]](https://dblp.org/pid/158/1357.html#j23)

[22](https://dblp.org/pid/158/1357.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Richang Hong](https://dblp.org/pid/59/1501.html)

[\[j12\]](https://dblp.org/pid/158/1357.html#j12)

[23](https://dblp.org/pid/158/1357.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Qichang Hu](https://dblp.org/pid/169/9980.html)

[\[j3\]](https://dblp.org/pid/158/1357.html#j3)

[24](https://dblp.org/pid/158/1357.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Haiping Huang](https://dblp.org/pid/22/6402.html)

[\[j29\]](https://dblp.org/pid/158/1357.html#j29) [\[j5\]](https://dblp.org/pid/158/1357.html#j5)

[25](https://dblp.org/pid/158/1357.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Shi Jin 0002](https://dblp.org/pid/49/5340-2.html)

[\[j33\]](https://dblp.org/pid/158/1357.html#j33) [\[j26\]](https://dblp.org/pid/158/1357.html#j26) [\[c10\]](https://dblp.org/pid/158/1357.html#c10) [\[i3\]](https://dblp.org/pid/158/1357.html#i3) [\[i2\]](https://dblp.org/pid/158/1357.html#i2)

[26](https://dblp.org/pid/158/1357.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Jinming Ju](https://dblp.org/pid/415/8095.html)

[\[c11\]](https://dblp.org/pid/158/1357.html#c11)

[27](https://dblp.org/pid/158/1357.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Chen Lan](https://dblp.org/pid/203/5284.html)

[\[j35\]](https://dblp.org/pid/158/1357.html#j35) [\[j34\]](https://dblp.org/pid/158/1357.html#j34)

[28](https://dblp.org/pid/158/1357.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Jiabin Li](https://dblp.org/pid/43/5182.html)

[\[j27\]](https://dblp.org/pid/158/1357.html#j27) [\[j21\]](https://dblp.org/pid/158/1357.html#j21)

[29](https://dblp.org/pid/158/1357.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Juan Li 0011](https://dblp.org/pid/59/2144-11.html)

[\[j29\]](https://dblp.org/pid/158/1357.html#j29)

[30](https://dblp.org/pid/158/1357.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Jun Li](https://dblp.org/pid/116/1011.html)

[\[j10\]](https://dblp.org/pid/158/1357.html#j10)

[31](https://dblp.org/pid/158/1357.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Jun Li 0033](https://dblp.org/pid/116/1011-33.html)

[\[j7\]](https://dblp.org/pid/158/1357.html#j7) [\[j4\]](https://dblp.org/pid/158/1357.html#j4) [\[j3\]](https://dblp.org/pid/158/1357.html#j3) [\[i1\]](https://dblp.org/pid/158/1357.html#i1)

[32](https://dblp.org/pid/158/1357.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Qun Li 0002](https://dblp.org/pid/42/6066-2.html)

[\[j12\]](https://dblp.org/pid/158/1357.html#j12) [\[j7\]](https://dblp.org/pid/158/1357.html#j7)

[33](https://dblp.org/pid/158/1357.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Guosheng Lin](https://dblp.org/pid/126/4778.html)

[\[j4\]](https://dblp.org/pid/158/1357.html#j4) [\[i1\]](https://dblp.org/pid/158/1357.html#i1)

[34](https://dblp.org/pid/158/1357.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Li Lu 0008](https://dblp.org/pid/49/2793-8.html)

[\[j27\]](https://dblp.org/pid/158/1357.html#j27)

[35](https://dblp.org/pid/158/1357.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Chunzhe Ma](https://dblp.org/pid/349/8460.html)

[\[j18\]](https://dblp.org/pid/158/1357.html#j18)

[36](https://dblp.org/pid/158/1357.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Yimin Mao](https://dblp.org/pid/219/5149.html)

[\[j20\]](https://dblp.org/pid/158/1357.html#j20)

[37](https://dblp.org/pid/158/1357.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Hoangvu Nguyen](https://dblp.org/pid/160/2774.html)

[\[j2\]](https://dblp.org/pid/158/1357.html#j2)

[38](https://dblp.org/pid/158/1357.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Cheng Peng 0019](https://dblp.org/pid/82/3044-19.html)

[\[j24\]](https://dblp.org/pid/158/1357.html#j24) [\[c7\]](https://dblp.org/pid/158/1357.html#c7)

[39](https://dblp.org/pid/158/1357.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Tie Qiu 0001](https://dblp.org/pid/53/9359.html)

[\[j32\]](https://dblp.org/pid/158/1357.html#j32)

[40](https://dblp.org/pid/158/1357.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Letian Sha](https://dblp.org/pid/184/0402.html)

[\[j13\]](https://dblp.org/pid/158/1357.html#j13) [\[j9\]](https://dblp.org/pid/158/1357.html#j9)

[41](https://dblp.org/pid/158/1357.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Chunhua Shen](https://dblp.org/pid/56/1673.html)

[\[j4\]](https://dblp.org/pid/158/1357.html#j4) [\[i1\]](https://dblp.org/pid/158/1357.html#i1)

[42](https://dblp.org/pid/158/1357.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Jiayu Sheng](https://dblp.org/pid/169/4623.html)

[\[c2\]](https://dblp.org/pid/158/1357.html#c2)

[43](https://dblp.org/pid/158/1357.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Changyin Sun 0001](https://dblp.org/pid/64/221.html)

[\[j4\]](https://dblp.org/pid/158/1357.html#j4) [\[j3\]](https://dblp.org/pid/158/1357.html#j3) [\[j2\]](https://dblp.org/pid/158/1357.html#j2) [\[i1\]](https://dblp.org/pid/158/1357.html#i1) [\[j1\]](https://dblp.org/pid/158/1357.html#j1) [\[c3\]](https://dblp.org/pid/158/1357.html#c3) [\[c2\]](https://dblp.org/pid/158/1357.html#c2) [\[c1\]](https://dblp.org/pid/158/1357.html#c1)

[44](https://dblp.org/pid/158/1357.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Chaorun Sun](https://dblp.org/pid/348/8186.html)

[\[j19\]](https://dblp.org/pid/158/1357.html#j19)

[45](https://dblp.org/pid/158/1357.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Lijuan Sun](https://dblp.org/pid/39/478.html)

[\[j30\]](https://dblp.org/pid/158/1357.html#j30) [\[j13\]](https://dblp.org/pid/158/1357.html#j13) [\[j11\]](https://dblp.org/pid/158/1357.html#j11) [\[j9\]](https://dblp.org/pid/158/1357.html#j9) [\[j6\]](https://dblp.org/pid/158/1357.html#j6) [\[j5\]](https://dblp.org/pid/158/1357.html#j5)

[46](https://dblp.org/pid/158/1357.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Shu-Qi Sun](https://dblp.org/pid/21/9088.html)

aka: Shuqi Sun

[\[j31\]](https://dblp.org/pid/158/1357.html#j31)

[47](https://dblp.org/pid/158/1357.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Chuyu Wang](https://dblp.org/pid/145/0641.html)

[\[j32\]](https://dblp.org/pid/158/1357.html#j32)

[48](https://dblp.org/pid/158/1357.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Dongzi Wang](https://dblp.org/pid/275/7735.html)

[\[j22\]](https://dblp.org/pid/158/1357.html#j22)

[49](https://dblp.org/pid/158/1357.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Haiyan Wang 0007](https://dblp.org/pid/27/59-7.html)

[\[c5\]](https://dblp.org/pid/158/1357.html#c5) [\[c4\]](https://dblp.org/pid/158/1357.html#c4)

[50](https://dblp.org/pid/158/1357.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Fu Xiao 0001](https://dblp.org/pid/91/8079-1.html)

[\[j35\]](https://dblp.org/pid/158/1357.html#j35) [\[j34\]](https://dblp.org/pid/158/1357.html#j34) [\[j32\]](https://dblp.org/pid/158/1357.html#j32) [\[j31\]](https://dblp.org/pid/158/1357.html#j31) [\[j29\]](https://dblp.org/pid/158/1357.html#j29) [\[j28\]](https://dblp.org/pid/158/1357.html#j28) [\[j27\]](https://dblp.org/pid/158/1357.html#j27) [\[c11\]](https://dblp.org/pid/158/1357.html#c11) [\[j26\]](https://dblp.org/pid/158/1357.html#j26) [\[j25\]](https://dblp.org/pid/158/1357.html#j25) [\[j24\]](https://dblp.org/pid/158/1357.html#j24) [\[j23\]](https://dblp.org/pid/158/1357.html#j23) [\[j22\]](https://dblp.org/pid/158/1357.html#j22) [\[j21\]](https://dblp.org/pid/158/1357.html#j21) [\[j20\]](https://dblp.org/pid/158/1357.html#j20) [\[c10\]](https://dblp.org/pid/158/1357.html#c10) [\[i3\]](https://dblp.org/pid/158/1357.html#i3) [\[i2\]](https://dblp.org/pid/158/1357.html#i2) [\[j19\]](https://dblp.org/pid/158/1357.html#j19) [\[j18\]](https://dblp.org/pid/158/1357.html#j18) [\[j17\]](https://dblp.org/pid/158/1357.html#j17) [\[j16\]](https://dblp.org/pid/158/1357.html#j16) [\[j15\]](https://dblp.org/pid/158/1357.html#j15) [\[j14\]](https://dblp.org/pid/158/1357.html#j14) [\[c9\]](https://dblp.org/pid/158/1357.html#c9) [\[c8\]](https://dblp.org/pid/158/1357.html#c8) [\[c7\]](https://dblp.org/pid/158/1357.html#c7) [\[j13\]](https://dblp.org/pid/158/1357.html#j13) [\[j12\]](https://dblp.org/pid/158/1357.html#j12) [\[j11\]](https://dblp.org/pid/158/1357.html#j11) [\[c6\]](https://dblp.org/pid/158/1357.html#c6) [\[j10\]](https://dblp.org/pid/158/1357.html#j10) [\[j9\]](https://dblp.org/pid/158/1357.html#j9) [\[j8\]](https://dblp.org/pid/158/1357.html#j8) [\[j7\]](https://dblp.org/pid/158/1357.html#j7) [\[j6\]](https://dblp.org/pid/158/1357.html#j6) [\[c5\]](https://dblp.org/pid/158/1357.html#c5) [\[c4\]](https://dblp.org/pid/158/1357.html#c4) [\[j5\]](https://dblp.org/pid/158/1357.html#j5)

[51](https://dblp.org/pid/158/1357.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Mingming Xu 0002](https://dblp.org/pid/43/6921-2.html)

[\[j16\]](https://dblp.org/pid/158/1357.html#j16)

[52](https://dblp.org/pid/158/1357.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Zhicheng Xu](https://dblp.org/pid/39/1625.html)

[\[c9\]](https://dblp.org/pid/158/1357.html#c9)

[53](https://dblp.org/pid/158/1357.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Yan Yan 0023](https://dblp.org/pid/13/3953-23.html)

[\[c3\]](https://dblp.org/pid/158/1357.html#c3)

[54](https://dblp.org/pid/158/1357.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[j10\]](https://dblp.org/pid/158/1357.html#j10) [\[j7\]](https://dblp.org/pid/158/1357.html#j7) [\[j4\]](https://dblp.org/pid/158/1357.html#j4) [\[j3\]](https://dblp.org/pid/158/1357.html#j3) [\[j2\]](https://dblp.org/pid/158/1357.html#j2) [\[i1\]](https://dblp.org/pid/158/1357.html#i1) [\[j1\]](https://dblp.org/pid/158/1357.html#j1) [\[c2\]](https://dblp.org/pid/158/1357.html#c2) [\[c1\]](https://dblp.org/pid/158/1357.html#c1)

[55](https://dblp.org/pid/158/1357.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Yuanyuan Yang 0001](https://dblp.org/pid/10/2031-1.html)

[\[j35\]](https://dblp.org/pid/158/1357.html#j35) [\[j34\]](https://dblp.org/pid/158/1357.html#j34)

[56](https://dblp.org/pid/158/1357.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Mang Ye](https://dblp.org/pid/156/0610.html)

[\[j29\]](https://dblp.org/pid/158/1357.html#j29)

[57](https://dblp.org/pid/158/1357.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Shui Yu 0001](https://dblp.org/pid/90/3575-1.html)

[\[j11\]](https://dblp.org/pid/158/1357.html#j11) [\[j8\]](https://dblp.org/pid/158/1357.html#j8)

[58](https://dblp.org/pid/158/1357.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Wenyang Yuan](https://dblp.org/pid/324/4067.html)

[\[j14\]](https://dblp.org/pid/158/1357.html#j14)

[59](https://dblp.org/pid/158/1357.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Baochang Zhang 0001](https://dblp.org/pid/80/3887-1.html)

[\[j3\]](https://dblp.org/pid/158/1357.html#j3) [\[c1\]](https://dblp.org/pid/158/1357.html#c1)

[60](https://dblp.org/pid/158/1357.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Jian Zhou 0009](https://dblp.org/pid/97/97-9.html)

[\[j35\]](https://dblp.org/pid/158/1357.html#j35) [\[j34\]](https://dblp.org/pid/158/1357.html#j34) [\[j29\]](https://dblp.org/pid/158/1357.html#j29) [\[c11\]](https://dblp.org/pid/158/1357.html#c11)

[61](https://dblp.org/pid/158/1357.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Tianyang Zhou](https://dblp.org/pid/160/4707.html)

[\[c11\]](https://dblp.org/pid/158/1357.html#c11)

[62](https://dblp.org/pid/158/1357.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Xu Zhu](https://dblp.org/pid/65/2899.html)

[\[j17\]](https://dblp.org/pid/158/1357.html#j17)

[63](https://dblp.org/pid/158/1357.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Yanmin Zhu 0006](https://dblp.org/pid/25/8709-6.html)

[\[j35\]](https://dblp.org/pid/158/1357.html#j35) [\[j34\]](https://dblp.org/pid/158/1357.html#j34)

[64](https://dblp.org/pid/158/1357.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/158/1357.html?view=group&param=1)

[Yiping Zuo](https://dblp.org/pid/198/1473.html)

[\[j33\]](https://dblp.org/pid/158/1357.html#j33) [\[j27\]](https://dblp.org/pid/158/1357.html#j27) [\[j26\]](https://dblp.org/pid/158/1357.html#j26) [\[c10\]](https://dblp.org/pid/158/1357.html#c10) [\[i3\]](https://dblp.org/pid/158/1357.html#i3) [\[i2\]](https://dblp.org/pid/158/1357.html#i2)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/158/1357.html#) [\[–\]](https://dblp.org/pid/158/1357.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/158/1357.html#) [\[–\]](https://dblp.org/pid/158/1357.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/158/1357.html#) [\[–\]](https://dblp.org/pid/158/1357.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/158/1357.html#) [\[–\]](https://dblp.org/pid/158/1357.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/158/1357.html#) [\[–\]](https://dblp.org/pid/158/1357.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)