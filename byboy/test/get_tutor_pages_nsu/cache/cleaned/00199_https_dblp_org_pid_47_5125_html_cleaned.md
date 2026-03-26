> 抓取来源：https://dblp.org/pid/47/5125.html

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

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Bilge+G%C3%BCnsel%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F47%2F5125%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Bilge+G%C3%BCnsel+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F47%2F5125%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Bilge+G%C3%BCnsel+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F47%2F5125%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Bilge+G%C3%BCnsel%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F47%2F5125%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Bilge+G%C3%BCnsel+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F47%2F5125%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Bilge+G%C3%BCnsel%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F47%2F5125%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Bilge+G%C3%BCnsel%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F47%2F5125%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F47%2F5125%3E+%7D+.%0A%0A%7D)

_showing all94 records_

1992202551992: 11994: 21995: 11996: 31996: 31997: 31998: 51998: 52001: 32002: 12004: 32005: 22006: 42006: 42007: 22008: 42008: 42009: 22009: 22010: 72011: 22011: 22012: 52012: 52013: 82013: 82014: 52014: 52015: 52015: 52016: 42017: 42017: 42018: 42018: 42019: 42019: 42019: 42020: 12021: 42021: 42021: 42022: 12023: 22024: 12025: 1

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

- ![](https://dblp.org/img/add-mark.12x12.png)Filiz Gurkan (15)
- ![](https://dblp.org/img/add-mark.12x12.png)A. Murat Tekalp (14)
- ![](https://dblp.org/img/add-mark.12x12.png)Serap Kirbiz (12)
- ![](https://dblp.org/img/add-mark.12x12.png)Demir Y. Yavas (9)
- ![](https://dblp.org/img/add-mark.12x12.png)Ibrahim Hökelek (9)
- ![](https://dblp.org/img/add-mark.12x12.png)Ozgun Cirakman (8)
- ![](https://dblp.org/img/add-mark.12x12.png)Yener Ülker (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Mehmet Cenk Sezgin (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Serhat Selcuk Bucak (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Anil K. Jain 0001 (4)

- _166 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)0000-0003-3628-3316 (67)
- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (27)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)ICPR (12)
- ![](https://dblp.org/img/add-mark.12x12.png)SIU (12)
- ![](https://dblp.org/img/add-mark.12x12.png)ICIP (11)
- ![](https://dblp.org/img/add-mark.12x12.png)EUSIPCO (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (5)
- ![](https://dblp.org/img/add-mark.12x12.png)ICASSP (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Digit. Signal Process. (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Pattern Recognit. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Multim. Tools Appl. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)TRECVID (2)
- ![](https://dblp.org/img/add-mark.12x12.png)ICIAR (2)

- _33 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (83)
- ![](https://dblp.org/img/add-mark.12x12.png)open (7)
- ![](https://dblp.org/img/add-mark.12x12.png)unavailable (3)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[c66\]
[Yusuf K. Hanoglu](https://dblp.org/pid/365/9612.html), Bilge Günsel, [Filiz Gurkan](https://dblp.org/pid/202/7040.html):

Cross-Domain One-Shot Video Object Detection. [EUSIPCO2025](https://dblp.org/db/conf/eusipco/eusipco2025.html#conf/eusipco/HanogluGG25): 641-645
- 2024
- ![](https://dblp.org/img/n.png)

\[j25\]
[Elif Ecem Akbaba](https://dblp.org/pid/365/9832.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Filiz Gurkan](https://dblp.org/pid/202/7040.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Boosting person ReID feature extraction via dynamic convolution. [Pattern Anal. Appl.27(3)](https://dblp.org/db/journals/paa/paa27.html#journals/paa/AkbabaGG24): 80 (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[c65\]
[Elif Ecem Akbaba](https://dblp.org/pid/365/9832.html), Bilge Günsel, [Filiz Gurkan](https://dblp.org/pid/202/7040.html):

Improved Scene Classification by Dynamic CNNs. [ICECS2023](https://dblp.org/db/conf/icecsys/icecsys2023.html#conf/icecsys/AkbabaGG23): 1-4
- ![](https://dblp.org/img/n.png)

\[c64\]
[Yusuf K. Hanoglu](https://dblp.org/pid/365/9612.html), Bilge Günsel, [Meltem Gulbas](https://dblp.org/pid/365/9123.html):

Vehicle Crowd Analysis via Transfer Learning. [ICECS2023](https://dblp.org/db/conf/icecsys/icecsys2023.html#conf/icecsys/HanogluGG23): 1-4
- 2022
- ![](https://dblp.org/img/n.png)

\[c63\]
[Irem Beyza Onur](https://dblp.org/pid/328/4617.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), Bilge Günsel:

Video Object Verification via Meta-learning. [SIU2022](https://dblp.org/db/conf/siu/siu2022.html#conf/siu/OnurGG22): 1-4
- 2021
- ![](https://dblp.org/img/n.png)

\[j24\]
[Filiz Gurkan](https://dblp.org/pid/202/7040.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Integration of regularized _l_ 1 tracking and instance segmentation for video object tracking. [Neurocomputing423](https://dblp.org/db/journals/ijon/ijon423.html#journals/ijon/GurkanG21): 284-300 (2021)
- ![](https://dblp.org/img/n.png)

\[j23\]
[Filiz Gurkan](https://dblp.org/pid/202/7040.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

TDIOT: Target-Driven Inference for Deep Video Object Tracking. [IEEE Trans. Image Process.30](https://dblp.org/db/journals/tip/tip30.html#journals/tip/GurkanCCG21): 7938-7951 (2021)
- ![](https://dblp.org/img/n.png)

\[c62\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Yu-Chen Chiu](https://dblp.org/pid/199/2494.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Xingping Dong](https://dblp.org/pid/156/3020.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), Bilge Günsel, [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Wencheng Han](https://dblp.org/pid/280/3348.html), [Yanyan Huang](https://dblp.org/pid/88/4316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [J. Yin](https://dblp.org/pid/51/2242.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Jingen Liu](https://dblp.org/pid/10/5849.html), [Li Liu](https://dblp.org/pid/33/4528-36.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Jonathon Luiten](https://dblp.org/pid/211/7992.html), [Jie Ma](https://dblp.org/pid/62/5110.html), [Ziang Ma](https://dblp.org/pid/165/9621.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Yuzhen Niu](https://dblp.org/pid/28/7442.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Aravindh Rajiv](https://dblp.org/pid/307/9144.html), [Muhammad Rana](https://dblp.org/pid/276/0222.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Ling Shao](https://dblp.org/pid/75/1281.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furao Shen](https://dblp.org/pid/80/4685.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Paul Voigtlaender](https://dblp.org/pid/166/6430.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html), [Chenyan Wu](https://dblp.org/pid/76/1190.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang Xu](https://dblp.org/pid/126/2962.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Xiaohan Zhang](https://dblp.org/pid/96/6053.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Ming Zhen](https://dblp.org/pid/307/8430.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html):

The Ninth Visual Object Tracking VOT2021 Challenge Results. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/KristanMLFPKCDZ21): 2711-2738
- ![](https://dblp.org/img/n.png)

\[i2\]
[Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), Bilge Günsel:

TDIOT: Target-driven Inference for Deep Video Object Tracking. [CoRRabs/2103.11017](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-11017) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[j22\]
[Yusuf Yaslan](https://dblp.org/pid/47/5558.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

A context-aware mobile application framework using audio watermarking. [Multim. Syst.26(3)](https://dblp.org/db/journals/mms/mms26.html#journals/mms/YaslanG20): 323-337 (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j21\]
[Filiz Gurkan](https://dblp.org/pid/202/7040.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Caner Ozer](https://dblp.org/pid/225/3305.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Robust object tracking via integration of particle filtering with deep detection. [Digit. Signal Process.87](https://dblp.org/db/journals/dsp/dsp87.html#journals/dsp/GurkanGO19): 112-124 (2019)
- ![](https://dblp.org/img/n.png)

\[c61\]
[Caner Ozer](https://dblp.org/pid/225/3305.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Target Aware Visual Object Tracking. [ICIAR (2)2019](https://dblp.org/db/conf/iciar/iciar2019-2.html#conf/iciar/OzerGG19): 186-198
- ![](https://dblp.org/img/n.png)

\[c60\]
[Ozan Cakiroglu](https://dblp.org/pid/247/8584.html), [Caner Ozer](https://dblp.org/pid/225/3305.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Design of a Deep Face Detector by Mask R-CNN. [SIU2019](https://dblp.org/db/conf/siu/siu2019.html#conf/siu/CakirogluOG19): 1-4
- ![](https://dblp.org/img/n.png)

\[i1\]
[Filiz Gurkan](https://dblp.org/pid/202/7040.html), Bilge Günsel:

Integration of Regularized l1 Tracking and Instance Segmentation for Video Object Tracking. [CoRRabs/1912.12883](https://dblp.org/db/journals/corr/corr1912.html#journals/corr/abs-1912-12883) (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[j20\]
[Demir Y. Yavas](https://dblp.org/pid/140/0989.html), [Ibrahim Hökelek](https://dblp.org/pid/56/4337.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

On modeling of priority-based SIP request scheduling. [Simul. Model. Pract. Theory80](https://dblp.org/db/journals/simpra/simpra80.html#journals/simpra/YavasHG18): 128-144 (2018)
- ![](https://dblp.org/img/n.png)

\[c59\]
[Erdem Onur Ozyurt](https://dblp.org/pid/226/2643.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel:

Wami Object Tracking Using L1Tracker Integrated with a Deep Detector. [ICIP2018](https://dblp.org/db/conf/icip/icip2018.html#conf/icip/OzyurtG18): 2690-2694
- ![](https://dblp.org/img/n.png)

\[c58\]
[Oguzhan Gultekin](https://dblp.org/pid/225/3069.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Robust object tracking by variable rate kernel particle filter. [SIU2018](https://dblp.org/db/conf/siu/siu2018.html#conf/siu/GultekinG18): 1-4
- ![](https://dblp.org/img/n.png)

\[c57\]
[Caner Ozer](https://dblp.org/pid/225/3305.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Object tracking by deep object detectors and particle filtering. [SIU2018](https://dblp.org/db/conf/siu/siu2018.html#conf/siu/OzerGG18): 1-4
- 2017
- ![](https://dblp.org/img/n.png)

\[j19\]
[Demir Y. Yavas](https://dblp.org/pid/140/0989.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ibrahim Hökelek](https://dblp.org/pid/56/4337.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

On fluid-flow modeling of priority based request scheduling for finite buffer SIP server. [Int. J. Commun. Syst.30(17)](https://dblp.org/db/journals/ijcomsys/ijcomsys30.html#journals/ijcomsys/YavasHG17) (2017)
- ![](https://dblp.org/img/n.png)

\[c56\]
[Demir Y. Yavas](https://dblp.org/pid/140/0989.html), [Ibrahim Hökelek](https://dblp.org/pid/56/4337.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Modeling of SIP retransmission traffic under lossy network conditions. [BlackSeaCom2017](https://dblp.org/db/conf/blackseecom/blackseecom2017.html#conf/blackseecom/YavasHG17): 1-5
- ![](https://dblp.org/img/n.png)

\[c55\]
[B. Akok](https://dblp.org/pid/214/9729.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Onur Kaplan](https://dblp.org/pid/202/7619.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Robust object tracking by interleaving variable rate color particle filtering and deep learning. [ICIP2017](https://dblp.org/db/conf/icip/icip2017.html#conf/icip/AkokGKG17): 3665-3669
- ![](https://dblp.org/img/n.png)

\[c54\]
[Esra Ergün](https://dblp.org/pid/202/7332.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Onur Kaplan](https://dblp.org/pid/202/7619.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Video action classification by deep learning. [SIU2017](https://dblp.org/db/conf/siu/siu2017.html#conf/siu/ErgunGKG17): 1-4
- 2016
- ![](https://dblp.org/img/n.png)

\[c53\]
[Deniz Kumlu](https://dblp.org/pid/191/2621.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Variable rate adaptive color-based particle filter tracking. [ICIP2016](https://dblp.org/db/conf/icip/icip2016.html#conf/icip/KumluG16): 1679-1683
- ![](https://dblp.org/img/n.png)

\[c52\]
[Ozgun Cirakman](https://dblp.org/pid/86/8843.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Online speaker emotion tracking with a dynamic state transition model. [ICPR2016](https://dblp.org/db/conf/icpr/icpr2016.html#conf/icpr/CirakmanG16): 307-312
- ![](https://dblp.org/img/n.png)

\[c51\]
[Demir Y. Yavas](https://dblp.org/pid/140/0989.html), [Ibrahim Hökelek](https://dblp.org/pid/56/4337.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Analytical Model of Priority Based Request Scheduling Mechanism Preventing SIP Server Overload. [MILCOM2016](https://dblp.org/db/conf/milcom/milcom2016.html#conf/milcom/YavasHG16): 1041-1046
- ![](https://dblp.org/img/n.png)

\[c50\]
[Demir Y. Yavas](https://dblp.org/pid/140/0989.html), [Ibrahim Hökelek](https://dblp.org/pid/56/4337.html), Bilge Günsel:

Modeling of Priority-based Request Scheduling Mechanism for Finite Buffer SIP Servers. [QTNA2016](https://dblp.org/db/conf/qtna/qtna2016.html#conf/qtna/YavasHG16): 6
- 2015
- ![](https://dblp.org/img/n.png)

\[j18\]
[Mehmet Cenk Sezgin](https://dblp.org/pid/36/9606.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Jarek Krajewski](https://dblp.org/pid/37/119.html):

Medium term speaker state detection by perceptually masked spectral features. [Speech Commun.67](https://dblp.org/db/journals/speech/speech67.html#journals/speech/SezginGK15): 26-41 (2015)
- ![](https://dblp.org/img/n.png)

\[c49\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Jarek Krajewski](https://dblp.org/pid/37/119.html):

Speaker emotional state classification by DPM models with annealed SMC samplers. [EUSIPCO2015](https://dblp.org/db/conf/eusipco/eusipco2015.html#conf/eusipco/GunselCK15): 120-124
- ![](https://dblp.org/img/n.png)

\[c48\]
[Demir Y. Yavas](https://dblp.org/pid/140/0989.html), [Ibrahim Hökelek](https://dblp.org/pid/56/4337.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Controlling SIP server overload with priority based request scheduling. [ICNC2015](https://dblp.org/db/conf/iccnc/iccnc2015.html#conf/iccnc/YavasHG15): 510-514
- ![](https://dblp.org/img/n.png)

\[c47\]
[Demir Y. Yavas](https://dblp.org/pid/140/0989.html), [Ibrahim Hökelek](https://dblp.org/pid/56/4337.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Analysis tool for SIP server loading. [SIU2015](https://dblp.org/db/conf/siu/siu2015.html#conf/siu/YavasHG15): 548-551
- ![](https://dblp.org/img/n.png)

\[c46\]
[Filiz Gurkan](https://dblp.org/pid/202/7040.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Erdem Basyurt](https://dblp.org/pid/258/0116.html):

Integration of motion and localization features for head movement classification. [SIU2015](https://dblp.org/db/conf/siu/siu2015.html#conf/siu/GurkanGB15): 1586-1589
- 2014
- ![](https://dblp.org/img/n.png)

\[j17\]
[Demir Y. Yavas](https://dblp.org/pid/140/0989.html), [Ibrahim Hökelek](https://dblp.org/pid/56/4337.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Strict Prioritization of New Requests over Retransmissions for Enhancing Scalability of SIP Servers. [IEICE Trans. Commun.97-B(12)](https://dblp.org/db/journals/ieicet/ieicet97b.html#journals/ieicet/YavasHG14): 2680-2688 (2014)
- ![](https://dblp.org/img/n.png)

\[j16\]
[Ozgun Cirakman](https://dblp.org/pid/86/8843.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Neslihan Serap Sengör](https://dblp.org/pid/77/6438.html), [Sezer Kutluk](https://dblp.org/pid/05/10845.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Content-based copy detection by a subspace learning based video fingerprinting scheme. [Multim. Tools Appl.71(3)](https://dblp.org/db/journals/mta/mta71.html#journals/mta/CirakmanGSK14): 1381-1409 (2014)
- ![](https://dblp.org/img/n.png)

\[j15\]
[Serap Kirbiz](https://dblp.org/pid/32/2240.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

A multiresolution non-negative tensor factorization approach for single channel sound source separation. [Signal Process.105](https://dblp.org/db/journals/sigpro/sigpro105.html#journals/sigpro/KirbizG14): 56-69 (2014)
- ![](https://dblp.org/img/n.png)

\[c45\]
[Inci M. Baytas](https://dblp.org/pid/158/1920.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Head motion classification with 2D motion estimation. [SIU2014](https://dblp.org/db/conf/siu/siu2014.html#conf/siu/BaytasG14): 325-328
- ![](https://dblp.org/img/n.png)

\[c44\]
[Serap Kirbiz](https://dblp.org/pid/32/2240.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Single channel audio source separation by Clustered NMF. [SIU2014](https://dblp.org/db/conf/siu/siu2014.html#conf/siu/KirbizG14): 469-472
- 2013
- ![](https://dblp.org/img/n.png)

\[j14\]
[Serap Kirbiz](https://dblp.org/pid/32/2240.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Perceptually enhanced blind single-channel music source separation by Non-negative Matrix Factorization. [Digit. Signal Process.23(2)](https://dblp.org/db/journals/dsp/dsp23.html#journals/dsp/KirbizG13): 646-658 (2013)
- ![](https://dblp.org/img/n.png)

\[j13\]
[Koray Kayabol](https://dblp.org/pid/27/2076.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Unsupervised classification of SAR images using normalized gamma process mixtures. [Digit. Signal Process.23(5)](https://dblp.org/db/journals/dsp/dsp23.html#journals/dsp/KayabolG13): 1344-1352 (2013)
- ![](https://dblp.org/img/n.png)

\[j12\]
[Serhat Selcuk Bucak](https://dblp.org/pid/96/3326.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Online video scene clustering by competitive incremental NMF. [Signal Image Video Process.7(4)](https://dblp.org/db/journals/sivp/sivp7.html#journals/sivp/BucakG13): 723-739 (2013)
- ![](https://dblp.org/img/n.png)

\[c43\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Mehmet Cenk Sezgin](https://dblp.org/pid/36/9606.html), [Jarek Krajewski](https://dblp.org/pid/37/119.html):

Sleepiness detection from speech by perceptual features. [ICASSP2013](https://dblp.org/db/conf/icassp/icassp2013.html#conf/icassp/GunselSK13): 788-792
- ![](https://dblp.org/img/n.png)

\[c42\]
[Serap Kirbiz](https://dblp.org/pid/32/2240.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

An adaptive time-frequency resolution framework for single channel source separation based on non-negative tensor factorization. [ICASSP2013](https://dblp.org/db/conf/icassp/icassp2013.html#conf/icassp/KirbizG13): 905-909
- ![](https://dblp.org/img/n.png)

\[c41\]
[Koray Kayabol](https://dblp.org/pid/27/2076.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

SAR image classification with normalized gamma process mixtures. [ICIP2013](https://dblp.org/db/conf/icip/icip2013.html#conf/icip/KayabolG13): 320-324
- ![](https://dblp.org/img/n.png)

\[c40\]
[Demir Y. Yavas](https://dblp.org/pid/140/0989.html), [Ibrahim Hökelek](https://dblp.org/pid/56/4337.html), Bilge Günsel:

An Analysis Tool to Evaluate Effect of Retransmissions on SIP Server Overloading. [NGMAST2013](https://dblp.org/db/conf/ngmast/ngmast2013.html#conf/ngmast/YavasHG13): 99-104
- ![](https://dblp.org/img/n.png)

\[c39\]
[Sezer Kutluk](https://dblp.org/pid/05/10845.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Tissue density classification in mammographic images using local features. [SIU2013](https://dblp.org/db/conf/siu/siu2013.html#conf/siu/KutlukG13): 1-4
- 2012
- ![](https://dblp.org/img/n.png)

\[j11\]
[Yener Ülker](https://dblp.org/pid/29/4313.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Multiple model target tracking with variable rate particle filters. [Digit. Signal Process.22(3)](https://dblp.org/db/journals/dsp/dsp22.html#journals/dsp/UlkerG12): 417-429 (2012)
- ![](https://dblp.org/img/n.png)

\[j10\]
[Mehmet Cenk Sezgin](https://dblp.org/pid/36/9606.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Gunes Karabulut-Kurt](https://dblp.org/pid/39/3095.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Perceptual audio features for emotion detection. [EURASIP J. Audio Speech Music. Process.2012](https://dblp.org/db/journals/ejasmp/ejasmp2012.html#journals/ejasmp/SezginGK12): 16 (2012)
- ![](https://dblp.org/img/n.png)

\[c38\]
[Serap Kirbiz](https://dblp.org/pid/32/2240.html), Bilge Günsel:

Perceptually weighted Non-negative Matrix Factorization for blind single-channel music source separation. [ICPR2012](https://dblp.org/db/conf/icpr/icpr2012.html#conf/icpr/KirbizG12): 226-229
- ![](https://dblp.org/img/n.png)

\[c37\]
[Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Sezer Kutluk](https://dblp.org/pid/05/10845.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel, [Onur Calikus](https://dblp.org/pid/158/0612.html):

A vocabulary-tree implementation for mobile product recognition. [SIU2012](https://dblp.org/db/conf/siu/siu2012.html#conf/siu/CirakmanKGC12): 1-4
- ![](https://dblp.org/img/n.png)

\[c36\]
[Mehmet Cenk Sezgin](https://dblp.org/pid/36/9606.html), Bilge Günsel, [Canberk Hacioglu](https://dblp.org/pid/158/0587.html):

Audio emotion recognition by perceptual features. [SIU2012](https://dblp.org/db/conf/siu/siu2012.html#conf/siu/SezginGH12): 1-4
- 2011
- ![](https://dblp.org/img/n.png)

\[j9\]
[Yener Ülker](https://dblp.org/pid/29/4313.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Ali Taylan Cemgil](https://dblp.org/pid/41/6613.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Annealed SMC Samplers for Nonparametric Bayesian Mixture Models. [IEEE Signal Process. Lett.18(1)](https://dblp.org/db/journals/spl/spl18.html#journals/spl/UlkerGC11): 3-6 (2011)
- ![](https://dblp.org/img/n.png)

\[c35\]
[Mehmet Cenk Sezgin](https://dblp.org/pid/36/9606.html), Bilge Günsel, [Gunes Karabulut-Kurt](https://dblp.org/pid/39/3095.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A novel perceptual feature set for audio emotion recognition. [FG2011](https://dblp.org/db/conf/fgr/fg2011.html#conf/fgr/SezginGK11): 780-785
- 2010
- ![](https://dblp.org/img/n.png)

\[c34\]
[Serap Kirbiz](https://dblp.org/pid/32/2240.html), Bilge Günsel:

A perceptually enhanced blind single-channel audio source separation by non-negative matrix factorization. [EUSIPCO2010](https://dblp.org/db/conf/eusipco/eusipco2010.html#conf/eusipco/KirbizG10): 731-735
- ![](https://dblp.org/img/n.png)

\[c33\]
[Yigitcan Savran](https://dblp.org/pid/28/8192.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Novelty Detection on Metallic Surfaces by GMM Learning in Gabor Space. [ICIAR (2)2010](https://dblp.org/db/conf/iciar/iciar2010-2.html#conf/iciar/SavranG10): 325-334
- ![](https://dblp.org/img/n.png)

\[c32\]
[Ozgun Cirakman](https://dblp.org/pid/86/8843.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Neslihan Serap Sengör](https://dblp.org/pid/77/6438.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ozan Gursoy](https://dblp.org/pid/00/1549.html):

Key-frame based video fingerprinting by NMF. [ICIP2010](https://dblp.org/db/conf/icip/icip2010.html#conf/icip/CirakmanGSG10): 2373-2376
- ![](https://dblp.org/img/n.png)

\[c31\]
[Yener Ülker](https://dblp.org/pid/29/4313.html), Bilge Günsel, [Ali Taylan Cemgil](https://dblp.org/pid/41/6613.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Annealed SMC Samplers for Dirichlet Process Mixture Models. [ICPR2010](https://dblp.org/db/conf/icpr/icpr2010.html#conf/icpr/UlkerGC10): 2808-2811
- ![](https://dblp.org/img/n.png)

\[c30\]
[Serap Kirbiz](https://dblp.org/pid/32/2240.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ali Taylan Cemgil](https://dblp.org/pid/41/6613.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel:

Bayesian Inference for Nonnegative Matrix Factor Deconvolution Models. [ICPR2010](https://dblp.org/db/conf/icpr/icpr2010.html#conf/icpr/KirbizCG10): 2812-2815
- ![](https://dblp.org/img/n.png)

\[c29\]
[Sezer Kutluk](https://dblp.org/pid/05/10845.html), Bilge Günsel:

ITU MSPR TRECVID 2010 Video Copy Detection System. [TRECVID2010](https://dblp.org/db/conf/trecvid/trecvid2010.html#conf/trecvid/KutlukG10)
- ![](https://dblp.org/img/n.png)

\[c28\]
[Yener Ülker](https://dblp.org/pid/29/4313.html), Bilge Günsel, [Ali Taylan Cemgil](https://dblp.org/pid/41/6613.html):

Sequential Monte Carlo Samplers for Dirichlet Process Mixtures. [AISTATS2010](https://dblp.org/db/journals/jmlr/jmlrp9.html#journals/jmlr/UlkerGC10): 876-883
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2009
- ![](https://dblp.org/img/n.png)

\[j8\]
[Serhat Selcuk Bucak](https://dblp.org/pid/96/3326.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Incremental subspace learning via non-negative matrix factorization. [Pattern Recognit.42(5)](https://dblp.org/db/journals/pr/pr42.html#journals/pr/BucakG09): 788-797 (2009)
- ![](https://dblp.org/img/n.png)

\[c27\]
[Ozan Gursoy](https://dblp.org/pid/00/1549.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Neslihan Serap Sengör](https://dblp.org/pid/77/6438.html):

Transform Invariant Video Fingerprinting by NMF. [CAIP2009](https://dblp.org/db/conf/caip/caip2009.html#conf/caip/GursoyGS09): 452-459
- 2008
- ![](https://dblp.org/img/n.png)

\[j7\]
[Yusuf Yaslan](https://dblp.org/pid/47/5558.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

An integrated on-line audio watermark decoding scheme for broadcast monitoring. [Multim. Tools Appl.40(1)](https://dblp.org/db/journals/mta/mta40.html#journals/mta/YaslanG08): 1-21 (2008)
- ![](https://dblp.org/img/n.png)

\[c26\]
[Serhat Selcuk Bucak](https://dblp.org/pid/96/3326.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Incremental clustering via nonnegative matrix factorization. [ICPR2008](https://dblp.org/db/conf/icpr/icpr2008.html#conf/icpr/BucakG08): 1-4
- ![](https://dblp.org/img/n.png)

\[c25\]
[Yener Ülker](https://dblp.org/pid/29/4313.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Serap Kirbiz](https://dblp.org/pid/32/2240.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A multiple model structure for tracking by variable rate particle filters. [ICPR2008](https://dblp.org/db/conf/icpr/icpr2008.html#conf/icpr/UlkerGK08): 1-4
- ![](https://dblp.org/img/n.png)

\[c24\]
[Ozan Gursoy](https://dblp.org/pid/00/1549.html), Bilge Günsel:

Istanbul Technical University at TRECVID2008. [TRECVID2008](https://dblp.org/db/conf/trecvid/trecvid2008.html#conf/trecvid/GursoyG08)
- 2007
- ![](https://dblp.org/img/n.png)

\[c23\]
[Serhat Selcuk Bucak](https://dblp.org/pid/96/3326.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Video Content Representation by Incremental Non-Negative Matrix Factorization. [ICIP (2)2007](https://dblp.org/db/conf/icip/icip2007-2.html#conf/icip/BucakG07): 113-116
- ![](https://dblp.org/img/n.png)

\[c22\]
[Serhat Selcuk Bucak](https://dblp.org/pid/96/3326.html), Bilge Günsel, [Ozan Gursoy](https://dblp.org/pid/00/1549.html):

Incremental Non-negative Matrix Factorization for Dynamic Background Modelling. [PRIS2007](https://dblp.org/db/conf/pris/pris2007.html#conf/pris/BucakGG07): 107-116
- 2006
- ![](https://dblp.org/img/n.png)

\[c21\]
[Serap Kirbiz](https://dblp.org/pid/32/2240.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Robust Audio Watermark Decoding by Supervised Learning. [ICASSP (5)2006](https://dblp.org/db/conf/icassp/icassp2006.html#conf/icassp/KirbizG06): 761-764
- ![](https://dblp.org/img/n.png)

\[c20\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Serap Kirbiz](https://dblp.org/pid/32/2240.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Perceptual Audio Watermarking by Learning in Wavelet Domain. [ICPR (3)2006](https://dblp.org/db/conf/icpr/icpr2006-3.html#conf/icpr/GunselK06): 383-386
- ![](https://dblp.org/img/n.png)

\[c19\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Yener Ülker](https://dblp.org/pid/29/4313.html), [Serap Kirbiz](https://dblp.org/pid/32/2240.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Statistical Framework for Audio Watermark Detection and Decoding. [MRCS2006](https://dblp.org/db/conf/mrcs/mrcs2006.html#conf/mrcs/GunselUK06): 241-248
- ![](https://dblp.org/img/n.png)

\[e1\]
Bilge Günsel, [Anil K. Jain](https://dblp.org/pid/j/AnilKJain.html), [A. Murat Tekalp](https://dblp.org/pid/00/5029.html), [Bülent Sankur](https://dblp.org/pid/35/2351.html):

Multimedia Content Representation, Classification and Security, International Workshop, MRCS 2006, Istanbul, Turkey, September 11-13, 2006, Proceedings. [Lecture Notes in Computer Science](https://dblp.org/db/series/lncs/index.html) 4105, Springer2006, ISBN 3-540-39392-7 [\[contents\]](https://dblp.org/db/conf/mrcs/mrcs2006.html)
- 2005
- ![](https://dblp.org/img/n.png)

\[c18\]
[Serap Kirbiz](https://dblp.org/pid/32/2240.html), [Yusuf Yaslan](https://dblp.org/pid/47/5558.html), Bilge Günsel:

Robust audio watermark decoding by nonlinear classification. [EUSIPCO2005](https://dblp.org/db/conf/eusipco/eusipco2005.html#conf/eusipco/KirbizYG05): 1-4
- ![](https://dblp.org/img/n.png)

\[c17\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Sanem Sariel](https://dblp.org/pid/17/8399.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Oguz Icoglu](https://dblp.org/pid/79/6990.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Content-based access to art paintings. [ICIP (2)2005](https://dblp.org/db/conf/icip/icip2005-2.html#conf/icip/GunselSI05): 558-561
- 2004
- ![](https://dblp.org/img/n.png)

\[c16\]
[Oguz Icoglu](https://dblp.org/pid/79/6990.html), Bilge Günsel, [Sanem Sariel](https://dblp.org/pid/17/8399.html):

Classification and indexing of paintings based on art movements. [EUSIPCO2004](https://dblp.org/db/conf/eusipco/eusipco2004.html#conf/eusipco/IcogluGS04): 749-752
- ![](https://dblp.org/img/n.png)

\[c15\]
[Sait Sener](https://dblp.org/pid/97/5945.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Blind Audio Watermark Decoding Using Independent Component Analysis. [ICPR (2)2004](https://dblp.org/db/conf/icpr/icpr2004-2.html#conf/icpr/SenerG04): 875-878
- ![](https://dblp.org/img/n.png)

\[c14\]
[Yusuf Yaslan](https://dblp.org/pid/47/5558.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

An Integrated Decoding Framework for Audio Watermark Extraction. [ICPR (2)2004](https://dblp.org/db/conf/icpr/icpr2004-2.html#conf/icpr/YaslanG04): 879-882
- 2002
- ![](https://dblp.org/img/n.png)

\[j6\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Umut Uludag](https://dblp.org/pid/55/802.html), [A. Murat Tekalp](https://dblp.org/pid/00/5029.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Robust watermarking of fingerprint images. [Pattern Recognit.35(12)](https://dblp.org/db/journals/pr/pr35.html#journals/pr/GunselUT02): 2739-2747 (2002)
- 2001
- ![](https://dblp.org/img/n.png)

\[c13\]
[Umut Uludag](https://dblp.org/pid/55/802.html), Bilge Günsel, [Meltem Ballan](https://dblp.org/pid/51/6882.html):

A Spatial Method for Watermarking of Fingerprint Images. [PRIS2001](https://dblp.org/db/conf/pris/pris2001.html#conf/pris/UludagGB01): 26-33
- ![](https://dblp.org/img/n.png)

\[c12\]
[Oguz Icoglu](https://dblp.org/pid/79/6990.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yavuz Erdogan](https://dblp.org/pid/15/8305.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [A. Murat Tekalp](https://dblp.org/pid/00/5029.html)![](https://dblp.org/img/orcid-mark.12x12.png):

User preference matching for smart browsing of media contents. [Storage and Retrieval for Media Databases2001](https://dblp.org/db/conf/spieSR/spieSR2001.html#conf/spieSR/IcogluEGT01): 330-340
- ![](https://dblp.org/img/n.png)

\[c11\]
[Umut Uludag](https://dblp.org/pid/55/802.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [A. Murat Tekalp](https://dblp.org/pid/00/5029.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Robust watermarking of busy images. [Security and Watermarking of Multimedia Contents2001](https://dblp.org/db/conf/sswmc/swmc2001.html#conf/sswmc/UludagGT01): 18-25
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 1998
- ![](https://dblp.org/img/n.png)

\[j5\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [A. Müfit Ferman](https://dblp.org/pid/50/969.html), [A. Murat Tekalp](https://dblp.org/pid/00/5029.html):

Temporal video segmentation using unsupervised clustering and semantic object tracking. [J. Electronic Imaging7(3)](https://dblp.org/db/journals/jei/jei7.html#journals/jei/GunselFT98): 592-604 (1998)
- ![](https://dblp.org/img/n.png)

\[j4\]
[A. Murat Tekalp](https://dblp.org/pid/00/5029.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peter J. L. van Beek](https://dblp.org/pid/58/333.html), [Candemir Toklu](https://dblp.org/pid/01/5568.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png):

Two-dimensional mesh-based visual-object representation for interactive synthetic/natural digital video. [Proc. IEEE86(6)](https://dblp.org/db/journals/pieee/pieee86.html#journals/pieee/TekalpBTG98): 1029-1051 (1998)
- ![](https://dblp.org/img/n.png)

\[j3\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [A. Murat Tekalp](https://dblp.org/pid/00/5029.html):

Shape similarity matching for query-by-example. [Pattern Recognit.31(7)](https://dblp.org/db/journals/pr/pr31.html#journals/pr/GunselT98): 931-944 (1998)
- ![](https://dblp.org/img/n.png)

\[j2\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [A. Murat Tekalp](https://dblp.org/pid/00/5029.html), [Peter J. L. van Beek](https://dblp.org/pid/58/333.html):

Content-based access to video objects: Temporal Segmentation, visual summarization, and feature extraction. [Signal Process.66(2)](https://dblp.org/db/journals/sigpro/sigpro66.html#journals/sigpro/GunselTB98): 261-280 (1998)
- ![](https://dblp.org/img/n.png)

\[c10\]
Bilge Günsel, [A. Murat Tekalp](https://dblp.org/pid/00/5029.html):

Content-based Video Abstraction. [ICIP (3)1998](https://dblp.org/db/conf/icip/icip1998-3.html#conf/icip/GunselT98): 128-132
- 1997
- ![](https://dblp.org/img/n.png)

\[c9\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [A. Murat Tekalp](https://dblp.org/pid/00/5029.html), [Peter J. L. van Beek](https://dblp.org/pid/58/333.html):

Object-Based Video Indexing for Virtual Studio Productions. [CVPR1997](https://dblp.org/db/conf/cvpr/cvpr1997.html#conf/cvpr/GunselTB97): 769-774
- ![](https://dblp.org/img/n.png)

\[c8\]
[Ahmet Müfit Ferman](https://dblp.org/pid/50/969.html), Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [A. Murat Tekalp](https://dblp.org/pid/00/5029.html):

Motion and shape signatures for object-based indexing of MPEG-4 compressed video. [ICASSP1997](https://dblp.org/db/conf/icassp/icassp1997.html#conf/icassp/FermanGT97): 2601-2604
- ![](https://dblp.org/img/n.png)

\[c7\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [A. Murat Tekalp](https://dblp.org/pid/00/5029.html), [Peter J. L. van Beek](https://dblp.org/pid/58/333.html):

Moving Visual Representations of Video Objects for Content-Based Search and Browsing. [ICIP (2)1997](https://dblp.org/db/conf/icip/icip1997-2.html#conf/icip/GunselTB97): 502-505
- 1996
- ![](https://dblp.org/img/n.png)

\[j1\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Anil K. Jain](https://dblp.org/pid/j/AnilKJain.html), [Erdal Panayirci](https://dblp.org/pid/17/664.html):

Reconstruction and Boundary Detection of Range and Intensity Images Using Multiscale MRF Representations. [Comput. Vis. Image Underst.63(2)](https://dblp.org/db/journals/cviu/cviu63.html#journals/cviu/GunselJP96): 353-366 (1996)
- ![](https://dblp.org/img/n.png)

\[c6\]
Bilge Günsel, [A. Murat Tekalp](https://dblp.org/pid/00/5029.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Similarity analysis for shape retrieval by example. [ICPR1996](https://dblp.org/db/conf/icpr/icpr1996.html#conf/icpr/GunselT96): 330-334
- ![](https://dblp.org/img/n.png)

\[c5\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [A. Müfit Ferman](https://dblp.org/pid/50/969.html), [A. Murat Tekalp](https://dblp.org/pid/00/5029.html):

Video indexing through integration of syntactic and semantic features. [WACV1996](https://dblp.org/db/conf/wacv/wacv1996.html#conf/wacv/GunselFT96): 90-95
- 1995
- ![](https://dblp.org/img/n.png)

\[c4\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Cüneyt Güzelis](https://dblp.org/pid/36/4696.html):

Supervised learning of smoothing parameters in image restoration by regularization under cellular neural networks framework. [ICIP1995](https://dblp.org/db/conf/icip/icip1995-1.html#conf/icip/GunselG95): 470-473
- 1994
- ![](https://dblp.org/img/n.png)

\[c3\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Erdal Panayirci](https://dblp.org/pid/17/664.html):

Segmentation of Range and Intensity Images Using Multiscale Markov Random Field Representations. [ICIP (2)1994](https://dblp.org/db/conf/icip/icip1994-2.html#conf/icip/GunselP94): 187-191
- ![](https://dblp.org/img/n.png)

\[c2\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Erdal Panayirci](https://dblp.org/pid/17/664.html), [Anil K. Jain](https://dblp.org/pid/j/AnilKJain.html):

Boundary detection using multiscale Markov random fields. [ICPR (2)1994](https://dblp.org/db/conf/icpr/icpr1994-2.html#conf/icpr/GunselP094): 173-177
- 1992
- ![](https://dblp.org/img/n.png)

\[c1\]
Bilge Günsel![](https://dblp.org/img/orcid-mark.12x12.png), [Anil K. Jain](https://dblp.org/pid/j/AnilKJain.html):

Visual surface reconstruction and boundary detection using stochastic models. [ICPR (3)1992](https://dblp.org/db/conf/icpr/icpr1992-3.html#conf/icpr/GunselJ92): 343-346
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/47/5125.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[2](https://dblp.org/pid/47/5125.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Elif Ecem Akbaba](https://dblp.org/pid/365/9832.html)

[\[j25\]](https://dblp.org/pid/47/5125.html#j25) [\[c65\]](https://dblp.org/pid/47/5125.html#c65)

[3](https://dblp.org/pid/47/5125.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[B. Akok](https://dblp.org/pid/214/9729.html)

[\[c55\]](https://dblp.org/pid/47/5125.html#c55)

[4](https://dblp.org/pid/47/5125.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Meltem Ballan](https://dblp.org/pid/51/6882.html)

[\[c13\]](https://dblp.org/pid/47/5125.html#c13)

[5](https://dblp.org/pid/47/5125.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Erdem Basyurt](https://dblp.org/pid/258/0116.html)

[\[c46\]](https://dblp.org/pid/47/5125.html#c46)

[6](https://dblp.org/pid/47/5125.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Inci M. Baytas](https://dblp.org/pid/158/1920.html)

[\[c45\]](https://dblp.org/pid/47/5125.html#c45)

[7](https://dblp.org/pid/47/5125.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Peter J. L. van Beek](https://dblp.org/pid/58/333.html)

[\[j4\]](https://dblp.org/pid/47/5125.html#j4) [\[j2\]](https://dblp.org/pid/47/5125.html#j2) [\[c9\]](https://dblp.org/pid/47/5125.html#c9) [\[c7\]](https://dblp.org/pid/47/5125.html#c7)

[8](https://dblp.org/pid/47/5125.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[9](https://dblp.org/pid/47/5125.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Serhat Selcuk Bucak](https://dblp.org/pid/96/3326.html)

[\[j12\]](https://dblp.org/pid/47/5125.html#j12) [\[j8\]](https://dblp.org/pid/47/5125.html#j8) [\[c26\]](https://dblp.org/pid/47/5125.html#c26) [\[c23\]](https://dblp.org/pid/47/5125.html#c23) [\[c22\]](https://dblp.org/pid/47/5125.html#c22)

[10](https://dblp.org/pid/47/5125.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Ozan Cakiroglu](https://dblp.org/pid/247/8584.html)

[\[c60\]](https://dblp.org/pid/47/5125.html#c60)

[11](https://dblp.org/pid/47/5125.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Onur Calikus](https://dblp.org/pid/158/0612.html)

[\[c37\]](https://dblp.org/pid/47/5125.html#c37)

[12](https://dblp.org/pid/47/5125.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[13](https://dblp.org/pid/47/5125.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[A. Taylan Cemgil](https://dblp.org/pid/41/6613.html)

aka: Ali Taylan Cemgil

[\[j9\]](https://dblp.org/pid/47/5125.html#j9) [\[c31\]](https://dblp.org/pid/47/5125.html#c31) [\[c30\]](https://dblp.org/pid/47/5125.html#c30) [\[c28\]](https://dblp.org/pid/47/5125.html#c28)

[14](https://dblp.org/pid/47/5125.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Llukman Cerkezi](https://dblp.org/pid/208/1312.html)

[\[j23\]](https://dblp.org/pid/47/5125.html#j23) [\[c62\]](https://dblp.org/pid/47/5125.html#c62) [\[i2\]](https://dblp.org/pid/47/5125.html#i2)

[15](https://dblp.org/pid/47/5125.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Hakan Çevikalp](https://dblp.org/pid/14/6210.html)

aka: Hakan Cevikalp

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[16](https://dblp.org/pid/47/5125.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[17](https://dblp.org/pid/47/5125.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[18](https://dblp.org/pid/47/5125.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[19](https://dblp.org/pid/47/5125.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Miao Cheng](https://dblp.org/pid/79/7377.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[20](https://dblp.org/pid/47/5125.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Ziyi Cheng](https://dblp.org/pid/290/9342.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[21](https://dblp.org/pid/47/5125.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yu-Chen Chiu](https://dblp.org/pid/199/2494.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[22](https://dblp.org/pid/47/5125.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Ozgun Cirakman](https://dblp.org/pid/86/8843.html)

[\[j23\]](https://dblp.org/pid/47/5125.html#j23) [\[c62\]](https://dblp.org/pid/47/5125.html#c62) [\[i2\]](https://dblp.org/pid/47/5125.html#i2) [\[c52\]](https://dblp.org/pid/47/5125.html#c52) [\[c49\]](https://dblp.org/pid/47/5125.html#c49) [\[j16\]](https://dblp.org/pid/47/5125.html#j16) [\[c37\]](https://dblp.org/pid/47/5125.html#c37) [\[c32\]](https://dblp.org/pid/47/5125.html#c32)

[23](https://dblp.org/pid/47/5125.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[24](https://dblp.org/pid/47/5125.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Kenan Dai](https://dblp.org/pid/250/4445.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[25](https://dblp.org/pid/47/5125.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[26](https://dblp.org/pid/47/5125.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[27](https://dblp.org/pid/47/5125.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[28](https://dblp.org/pid/47/5125.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xingping Dong](https://dblp.org/pid/156/3020.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[29](https://dblp.org/pid/47/5125.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[30](https://dblp.org/pid/47/5125.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[31](https://dblp.org/pid/47/5125.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[32](https://dblp.org/pid/47/5125.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yavuz Erdogan](https://dblp.org/pid/15/8305.html)

[\[c12\]](https://dblp.org/pid/47/5125.html#c12)

[33](https://dblp.org/pid/47/5125.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Esra Ergün](https://dblp.org/pid/202/7332.html)

[\[c54\]](https://dblp.org/pid/47/5125.html#c54)

[34](https://dblp.org/pid/47/5125.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[35](https://dblp.org/pid/47/5125.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[36](https://dblp.org/pid/47/5125.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Zhiyong Feng 0001](https://dblp.org/pid/48/195-1.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[37](https://dblp.org/pid/47/5125.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[A. Müfit Ferman](https://dblp.org/pid/50/969.html)

aka: Ahmet Müfit Ferman

[\[j5\]](https://dblp.org/pid/47/5125.html#j5) [\[c8\]](https://dblp.org/pid/47/5125.html#c8) [\[c5\]](https://dblp.org/pid/47/5125.html#c5)

[38](https://dblp.org/pid/47/5125.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[39](https://dblp.org/pid/47/5125.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[40](https://dblp.org/pid/47/5125.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Shiming Ge](https://dblp.org/pid/93/8104.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[41](https://dblp.org/pid/47/5125.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[42](https://dblp.org/pid/47/5125.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[43](https://dblp.org/pid/47/5125.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yuzhang Gu](https://dblp.org/pid/122/3790.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[44](https://dblp.org/pid/47/5125.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Meltem Gulbas](https://dblp.org/pid/365/9123.html)

[\[c64\]](https://dblp.org/pid/47/5125.html#c64)

[45](https://dblp.org/pid/47/5125.html?view=joint&param=45 "show joint publications")

[Oguzhan Gultekin](https://dblp.org/pid/225/3069.html)

[\[c58\]](https://dblp.org/pid/47/5125.html#c58)

[46](https://dblp.org/pid/47/5125.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Qing Guo 0005](https://dblp.org/pid/25/3038-5.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[47](https://dblp.org/pid/47/5125.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Filiz Gurkan](https://dblp.org/pid/202/7040.html)

[\[c66\]](https://dblp.org/pid/47/5125.html#c66) [\[j25\]](https://dblp.org/pid/47/5125.html#j25) [\[c65\]](https://dblp.org/pid/47/5125.html#c65) [\[c63\]](https://dblp.org/pid/47/5125.html#c63) [\[j24\]](https://dblp.org/pid/47/5125.html#j24) [\[j23\]](https://dblp.org/pid/47/5125.html#j23) [\[c62\]](https://dblp.org/pid/47/5125.html#c62) [\[i2\]](https://dblp.org/pid/47/5125.html#i2) [\[j21\]](https://dblp.org/pid/47/5125.html#j21) [\[c61\]](https://dblp.org/pid/47/5125.html#c61) [\[i1\]](https://dblp.org/pid/47/5125.html#i1) [\[c57\]](https://dblp.org/pid/47/5125.html#c57) [\[c55\]](https://dblp.org/pid/47/5125.html#c55) [\[c54\]](https://dblp.org/pid/47/5125.html#c54) [\[c46\]](https://dblp.org/pid/47/5125.html#c46)

[48](https://dblp.org/pid/47/5125.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Ozan Gursoy](https://dblp.org/pid/00/1549.html)

[\[c32\]](https://dblp.org/pid/47/5125.html#c32) [\[c27\]](https://dblp.org/pid/47/5125.html#c27) [\[c24\]](https://dblp.org/pid/47/5125.html#c24) [\[c22\]](https://dblp.org/pid/47/5125.html#c22)

[49](https://dblp.org/pid/47/5125.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Cüneyt Güzelis](https://dblp.org/pid/36/4696.html)

[\[c4\]](https://dblp.org/pid/47/5125.html#c4)

[50](https://dblp.org/pid/47/5125.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Canberk Hacioglu](https://dblp.org/pid/158/0587.html)

[\[c36\]](https://dblp.org/pid/47/5125.html#c36)

[51](https://dblp.org/pid/47/5125.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Gustav Häger](https://dblp.org/pid/157/3602.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[52](https://dblp.org/pid/47/5125.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Wencheng Han](https://dblp.org/pid/280/3348.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[53](https://dblp.org/pid/47/5125.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yusuf K. Hanoglu](https://dblp.org/pid/365/9612.html)

[\[c66\]](https://dblp.org/pid/47/5125.html#c66) [\[c64\]](https://dblp.org/pid/47/5125.html#c64)

[54](https://dblp.org/pid/47/5125.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Ibrahim Hökelek](https://dblp.org/pid/56/4337.html)

[\[j20\]](https://dblp.org/pid/47/5125.html#j20) [\[j19\]](https://dblp.org/pid/47/5125.html#j19) [\[c56\]](https://dblp.org/pid/47/5125.html#c56) [\[c51\]](https://dblp.org/pid/47/5125.html#c51) [\[c50\]](https://dblp.org/pid/47/5125.html#c50) [\[c48\]](https://dblp.org/pid/47/5125.html#c48) [\[c47\]](https://dblp.org/pid/47/5125.html#c47) [\[j17\]](https://dblp.org/pid/47/5125.html#j17) [\[c40\]](https://dblp.org/pid/47/5125.html#c40)

[55](https://dblp.org/pid/47/5125.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yanyan Huang](https://dblp.org/pid/88/4316.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[56](https://dblp.org/pid/47/5125.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Oguz Icoglu](https://dblp.org/pid/79/6990.html)

[\[c17\]](https://dblp.org/pid/47/5125.html#c17) [\[c16\]](https://dblp.org/pid/47/5125.html#c16) [\[c12\]](https://dblp.org/pid/47/5125.html#c12)

[57](https://dblp.org/pid/47/5125.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Anil K. Jain 0001](https://dblp.org/pid/j/AnilKJain.html)

[\[e1\]](https://dblp.org/pid/47/5125.html#e1) [\[j1\]](https://dblp.org/pid/47/5125.html#j1) [\[c2\]](https://dblp.org/pid/47/5125.html#c2) [\[c1\]](https://dblp.org/pid/47/5125.html#c1)

[58](https://dblp.org/pid/47/5125.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[59](https://dblp.org/pid/47/5125.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[60](https://dblp.org/pid/47/5125.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[61](https://dblp.org/pid/47/5125.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[62](https://dblp.org/pid/47/5125.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[63](https://dblp.org/pid/47/5125.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[64](https://dblp.org/pid/47/5125.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Onur Kaplan](https://dblp.org/pid/202/7619.html)

[\[c55\]](https://dblp.org/pid/47/5125.html#c55) [\[c54\]](https://dblp.org/pid/47/5125.html#c54)

[65](https://dblp.org/pid/47/5125.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jani Käpylä](https://dblp.org/pid/244/2529.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[66](https://dblp.org/pid/47/5125.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Gunes Karabulut-Kurt](https://dblp.org/pid/39/3095.html)

[\[j10\]](https://dblp.org/pid/47/5125.html#j10) [\[c35\]](https://dblp.org/pid/47/5125.html#c35)

[67](https://dblp.org/pid/47/5125.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Koray Kayabol](https://dblp.org/pid/27/2076.html)

[\[j13\]](https://dblp.org/pid/47/5125.html#j13) [\[c41\]](https://dblp.org/pid/47/5125.html#c41)

[68](https://dblp.org/pid/47/5125.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xiao Ke](https://dblp.org/pid/78/9040.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[69](https://dblp.org/pid/47/5125.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[70](https://dblp.org/pid/47/5125.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Byeong Hak Kim](https://dblp.org/pid/214/8978.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[71](https://dblp.org/pid/47/5125.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Serap Kirbiz](https://dblp.org/pid/32/2240.html)

[\[j15\]](https://dblp.org/pid/47/5125.html#j15) [\[c44\]](https://dblp.org/pid/47/5125.html#c44) [\[j14\]](https://dblp.org/pid/47/5125.html#j14) [\[c42\]](https://dblp.org/pid/47/5125.html#c42) [\[c38\]](https://dblp.org/pid/47/5125.html#c38) [\[c34\]](https://dblp.org/pid/47/5125.html#c34) [\[c30\]](https://dblp.org/pid/47/5125.html#c30) [\[c25\]](https://dblp.org/pid/47/5125.html#c25) [\[c21\]](https://dblp.org/pid/47/5125.html#c21) [\[c20\]](https://dblp.org/pid/47/5125.html#c20) [\[c19\]](https://dblp.org/pid/47/5125.html#c19) [\[c18\]](https://dblp.org/pid/47/5125.html#c18)

[72](https://dblp.org/pid/47/5125.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[73](https://dblp.org/pid/47/5125.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jarek Krajewski](https://dblp.org/pid/37/119.html)

[\[j18\]](https://dblp.org/pid/47/5125.html#j18) [\[c49\]](https://dblp.org/pid/47/5125.html#c49) [\[c43\]](https://dblp.org/pid/47/5125.html#c43)

[74](https://dblp.org/pid/47/5125.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[75](https://dblp.org/pid/47/5125.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Deniz Kumlu](https://dblp.org/pid/191/2621.html)

[\[c53\]](https://dblp.org/pid/47/5125.html#c53)

[76](https://dblp.org/pid/47/5125.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Sezer Kutluk](https://dblp.org/pid/05/10845.html)

[\[j16\]](https://dblp.org/pid/47/5125.html#j16) [\[c39\]](https://dblp.org/pid/47/5125.html#c39) [\[c37\]](https://dblp.org/pid/47/5125.html#c37) [\[c29\]](https://dblp.org/pid/47/5125.html#c29)

[77](https://dblp.org/pid/47/5125.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[78](https://dblp.org/pid/47/5125.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[79](https://dblp.org/pid/47/5125.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jun Ha Lee](https://dblp.org/pid/260/2774.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[80](https://dblp.org/pid/47/5125.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[81](https://dblp.org/pid/47/5125.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[82](https://dblp.org/pid/47/5125.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[83](https://dblp.org/pid/47/5125.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jianhua Li](https://dblp.org/pid/93/3389.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[84](https://dblp.org/pid/47/5125.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[85](https://dblp.org/pid/47/5125.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yuezhou Li](https://dblp.org/pid/284/2562.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[86](https://dblp.org/pid/47/5125.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[87](https://dblp.org/pid/47/5125.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[88](https://dblp.org/pid/47/5125.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jingen Liu](https://dblp.org/pid/10/5849.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[89](https://dblp.org/pid/47/5125.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Li Liu 0036](https://dblp.org/pid/33/4528-36.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[90](https://dblp.org/pid/47/5125.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Qingjie Liu 0001](https://dblp.org/pid/72/10584.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[91](https://dblp.org/pid/47/5125.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[92](https://dblp.org/pid/47/5125.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Wei Lu](https://dblp.org/pid/98/6613.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[93](https://dblp.org/pid/47/5125.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jonathon Luiten](https://dblp.org/pid/211/7992.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[94](https://dblp.org/pid/47/5125.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[95](https://dblp.org/pid/47/5125.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[96](https://dblp.org/pid/47/5125.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Ziang Ma](https://dblp.org/pid/165/9621.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[97](https://dblp.org/pid/47/5125.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[98](https://dblp.org/pid/47/5125.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[99](https://dblp.org/pid/47/5125.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[100](https://dblp.org/pid/47/5125.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[101](https://dblp.org/pid/47/5125.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[102](https://dblp.org/pid/47/5125.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yuzhen Niu](https://dblp.org/pid/28/7442.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[103](https://dblp.org/pid/47/5125.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Irem Beyza Onur](https://dblp.org/pid/328/4617.html)

[\[c63\]](https://dblp.org/pid/47/5125.html#c63)

[104](https://dblp.org/pid/47/5125.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Caner Ozer](https://dblp.org/pid/225/3305.html)

[\[j21\]](https://dblp.org/pid/47/5125.html#j21) [\[c61\]](https://dblp.org/pid/47/5125.html#c61) [\[c60\]](https://dblp.org/pid/47/5125.html#c60) [\[c57\]](https://dblp.org/pid/47/5125.html#c57)

[105](https://dblp.org/pid/47/5125.html?view=joint&param=105 "show joint publications")

[Erdem Onur Ozyurt](https://dblp.org/pid/226/2643.html)

[\[c59\]](https://dblp.org/pid/47/5125.html#c59)

[106](https://dblp.org/pid/47/5125.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Erdal Panayirci](https://dblp.org/pid/17/664.html)

[\[j1\]](https://dblp.org/pid/47/5125.html#j1) [\[c3\]](https://dblp.org/pid/47/5125.html#c3) [\[c2\]](https://dblp.org/pid/47/5125.html#c2)

[107](https://dblp.org/pid/47/5125.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[108](https://dblp.org/pid/47/5125.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[109](https://dblp.org/pid/47/5125.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[110](https://dblp.org/pid/47/5125.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Shoumeng Qiu](https://dblp.org/pid/284/2537.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[111](https://dblp.org/pid/47/5125.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Aravindh Rajiv](https://dblp.org/pid/307/9144.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[112](https://dblp.org/pid/47/5125.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Muhammad Rana](https://dblp.org/pid/276/0222.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[113](https://dblp.org/pid/47/5125.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[114](https://dblp.org/pid/47/5125.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Bülent Sankur](https://dblp.org/pid/35/2351.html)

[\[e1\]](https://dblp.org/pid/47/5125.html#e1)

[115](https://dblp.org/pid/47/5125.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Hasan Saribas](https://dblp.org/pid/225/3263.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[116](https://dblp.org/pid/47/5125.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Sanem Sariel](https://dblp.org/pid/17/8399.html)

[\[c17\]](https://dblp.org/pid/47/5125.html#c17) [\[c16\]](https://dblp.org/pid/47/5125.html#c16)

[117](https://dblp.org/pid/47/5125.html?view=joint&param=117 "show joint publications")

[Yigitcan Savran](https://dblp.org/pid/28/8192.html)

[\[c33\]](https://dblp.org/pid/47/5125.html#c33)

[118](https://dblp.org/pid/47/5125.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Sait Sener](https://dblp.org/pid/97/5945.html)

[\[c15\]](https://dblp.org/pid/47/5125.html#c15)

[119](https://dblp.org/pid/47/5125.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Neslihan Serap Sengör](https://dblp.org/pid/77/6438.html)

[\[j16\]](https://dblp.org/pid/47/5125.html#j16) [\[c32\]](https://dblp.org/pid/47/5125.html#c32) [\[c27\]](https://dblp.org/pid/47/5125.html#c27)

[120](https://dblp.org/pid/47/5125.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Mehmet Cenk Sezgin](https://dblp.org/pid/36/9606.html)

[\[j18\]](https://dblp.org/pid/47/5125.html#j18) [\[c43\]](https://dblp.org/pid/47/5125.html#c43) [\[j10\]](https://dblp.org/pid/47/5125.html#j10) [\[c36\]](https://dblp.org/pid/47/5125.html#c36) [\[c35\]](https://dblp.org/pid/47/5125.html#c35)

[121](https://dblp.org/pid/47/5125.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[122](https://dblp.org/pid/47/5125.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Mohamed S. Shehata](https://dblp.org/pid/33/2495.html)

aka: Mohamed Shehata 0001

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[123](https://dblp.org/pid/47/5125.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Furao Shen](https://dblp.org/pid/80/4685.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[124](https://dblp.org/pid/47/5125.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jianbing Shen](https://dblp.org/pid/38/5435.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[125](https://dblp.org/pid/47/5125.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[126](https://dblp.org/pid/47/5125.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[127](https://dblp.org/pid/47/5125.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[128](https://dblp.org/pid/47/5125.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[A. Murat Tekalp](https://dblp.org/pid/00/5029.html)

[\[e1\]](https://dblp.org/pid/47/5125.html#e1) [\[j6\]](https://dblp.org/pid/47/5125.html#j6) [\[c12\]](https://dblp.org/pid/47/5125.html#c12) [\[c11\]](https://dblp.org/pid/47/5125.html#c11) [\[j5\]](https://dblp.org/pid/47/5125.html#j5) [\[j4\]](https://dblp.org/pid/47/5125.html#j4) [\[j3\]](https://dblp.org/pid/47/5125.html#j3) [\[j2\]](https://dblp.org/pid/47/5125.html#j2) [\[c10\]](https://dblp.org/pid/47/5125.html#c10) [\[c9\]](https://dblp.org/pid/47/5125.html#c9) [\[c8\]](https://dblp.org/pid/47/5125.html#c8) [\[c7\]](https://dblp.org/pid/47/5125.html#c7) [\[c6\]](https://dblp.org/pid/47/5125.html#c6) [\[c5\]](https://dblp.org/pid/47/5125.html#c5)

[129](https://dblp.org/pid/47/5125.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[130](https://dblp.org/pid/47/5125.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Candemir Toklu](https://dblp.org/pid/01/5568.html)

[\[j4\]](https://dblp.org/pid/47/5125.html#j4)

[131](https://dblp.org/pid/47/5125.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[132](https://dblp.org/pid/47/5125.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[133](https://dblp.org/pid/47/5125.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yener Ülker](https://dblp.org/pid/29/4313.html)

[\[j11\]](https://dblp.org/pid/47/5125.html#j11) [\[j9\]](https://dblp.org/pid/47/5125.html#j9) [\[c31\]](https://dblp.org/pid/47/5125.html#c31) [\[c28\]](https://dblp.org/pid/47/5125.html#c28) [\[c25\]](https://dblp.org/pid/47/5125.html#c25) [\[c19\]](https://dblp.org/pid/47/5125.html#c19)

[134](https://dblp.org/pid/47/5125.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Umut Uludag](https://dblp.org/pid/55/802.html)

[\[j6\]](https://dblp.org/pid/47/5125.html#j6) [\[c13\]](https://dblp.org/pid/47/5125.html#c13) [\[c11\]](https://dblp.org/pid/47/5125.html#c11)

[135](https://dblp.org/pid/47/5125.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Bedirhan Uzun](https://dblp.org/pid/247/8937.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[136](https://dblp.org/pid/47/5125.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Paul Voigtlaender](https://dblp.org/pid/166/6430.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[137](https://dblp.org/pid/47/5125.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[138](https://dblp.org/pid/47/5125.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Guangting Wang](https://dblp.org/pid/227/7195.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[139](https://dblp.org/pid/47/5125.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[140](https://dblp.org/pid/47/5125.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[141](https://dblp.org/pid/47/5125.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[142](https://dblp.org/pid/47/5125.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Linyuan Wang](https://dblp.org/pid/138/5963.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[143](https://dblp.org/pid/47/5125.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[144](https://dblp.org/pid/47/5125.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yunhong Wang 0001](https://dblp.org/pid/95/6251.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[145](https://dblp.org/pid/47/5125.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Chenyan Wu](https://dblp.org/pid/76/1190.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[146](https://dblp.org/pid/47/5125.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[147](https://dblp.org/pid/47/5125.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[148](https://dblp.org/pid/47/5125.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[149](https://dblp.org/pid/47/5125.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[150](https://dblp.org/pid/47/5125.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xiang Xu](https://dblp.org/pid/126/2962.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[151](https://dblp.org/pid/47/5125.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[152](https://dblp.org/pid/47/5125.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[153](https://dblp.org/pid/47/5125.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[154](https://dblp.org/pid/47/5125.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[155](https://dblp.org/pid/47/5125.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[156](https://dblp.org/pid/47/5125.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[157](https://dblp.org/pid/47/5125.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yusuf Yaslan](https://dblp.org/pid/47/5558.html)

[\[j22\]](https://dblp.org/pid/47/5125.html#j22) [\[j7\]](https://dblp.org/pid/47/5125.html#j7) [\[c18\]](https://dblp.org/pid/47/5125.html#c18) [\[c14\]](https://dblp.org/pid/47/5125.html#c14)

[158](https://dblp.org/pid/47/5125.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Demir Y. Yavas](https://dblp.org/pid/140/0989.html)

[\[j20\]](https://dblp.org/pid/47/5125.html#j20) [\[j19\]](https://dblp.org/pid/47/5125.html#j19) [\[c56\]](https://dblp.org/pid/47/5125.html#c56) [\[c51\]](https://dblp.org/pid/47/5125.html#c51) [\[c50\]](https://dblp.org/pid/47/5125.html#c50) [\[c48\]](https://dblp.org/pid/47/5125.html#c48) [\[c47\]](https://dblp.org/pid/47/5125.html#c47) [\[j17\]](https://dblp.org/pid/47/5125.html#j17) [\[c40\]](https://dblp.org/pid/47/5125.html#c40)

[159](https://dblp.org/pid/47/5125.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Yu Ye 0004](https://dblp.org/pid/129/0969-4.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[160](https://dblp.org/pid/47/5125.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[J. Yin](https://dblp.org/pid/51/2242.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[161](https://dblp.org/pid/47/5125.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jun Yin 0003](https://dblp.org/pid/58/5423-3.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[162](https://dblp.org/pid/47/5125.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[163](https://dblp.org/pid/47/5125.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[164](https://dblp.org/pid/47/5125.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Haitao Zhang](https://dblp.org/pid/19/6669.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[165](https://dblp.org/pid/47/5125.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[166](https://dblp.org/pid/47/5125.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Kangkai Zhang](https://dblp.org/pid/260/2990.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[167](https://dblp.org/pid/47/5125.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xiaohan Zhang](https://dblp.org/pid/96/6053.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[168](https://dblp.org/pid/47/5125.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xiaolin Zhang](https://dblp.org/pid/99/2516.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[169](https://dblp.org/pid/47/5125.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xinyu Zhang 0020](https://dblp.org/pid/58/4582-20.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[170](https://dblp.org/pid/47/5125.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[171](https://dblp.org/pid/47/5125.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[172](https://dblp.org/pid/47/5125.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[173](https://dblp.org/pid/47/5125.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Ming Zhen](https://dblp.org/pid/307/8430.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[174](https://dblp.org/pid/47/5125.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[175](https://dblp.org/pid/47/5125.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

[176](https://dblp.org/pid/47/5125.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/47/5125.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c62\]](https://dblp.org/pid/47/5125.html#c62)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/47/5125.html#) [\[–\]](https://dblp.org/pid/47/5125.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/47/5125.html#) [\[–\]](https://dblp.org/pid/47/5125.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/47/5125.html#) [\[–\]](https://dblp.org/pid/47/5125.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/47/5125.html#) [\[–\]](https://dblp.org/pid/47/5125.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/47/5125.html#) [\[–\]](https://dblp.org/pid/47/5125.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)