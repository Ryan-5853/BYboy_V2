> 抓取来源：https://dblp.org/pid/79/1282.html

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

- [Eric K. Patterson](https://dblp.org/pid/93/9217.html)
- [Eric M. Patterson](https://dblp.org/pid/394/5234.html)

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Eric+Patterson%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F79%2F1282%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Eric+Patterson+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F79%2F1282%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Eric+Patterson+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F79%2F1282%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Eric+Patterson%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F79%2F1282%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Eric+Patterson+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F79%2F1282%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Eric+Patterson%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F79%2F1282%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Eric+Patterson%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F79%2F1282%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F79%2F1282%3E+%7D+.%0A%0A%7D)

_showing all16 records_

1991202551991: 12009: 12010: 22011: 22012: 12013: 12014: 12017: 12018: 12019: 22020: 12024: 12025: 1

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

- ![](https://dblp.org/img/add-mark.12x12.png)Amrutha Sethuram (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Karl Ricanek (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Nghia Nguyen (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Kha Gia Quach (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Khoa Luu (2)
- ![](https://dblp.org/img/add-mark.12x12.png)T. Hoang Ngan Le (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Chi Nhan Duong (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Tien D. Bui (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Devin Simpson (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Warren N. White (1)

- _21 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)0009-0005-6953-032X (13)
- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (3)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (2)
- ![](https://dblp.org/img/add-mark.12x12.png)BTAS (2)
- ![](https://dblp.org/img/add-mark.12x12.png)IJCB (2)
- ![](https://dblp.org/img/add-mark.12x12.png)CVMP (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ICFSP (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ICVGIP (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ACC (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ISNN (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IUI (1)
- ![](https://dblp.org/img/add-mark.12x12.png)SIGGRAPH (1)

- _5 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (10)
- ![](https://dblp.org/img/add-mark.12x12.png)open (6)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[c14\]
[Jessica Baron-Lis](https://dblp.org/pid/427/3571.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Krzysztof Baron-Lis](https://dblp.org/pid/167/4194.html)![](https://dblp.org/img/orcid-mark.12x12.png), Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png):

Capturing the Complexity of Spatially Varying Surfaces with Adaptive Parameterization and Distribution Metrics. [CVMP2025](https://dblp.org/db/conf/cvmp/cvmp2025.html#conf/cvmp/Baron-LisBP25): 4:1-4:10
- 2024
- ![](https://dblp.org/img/n.png)

\[c13\]
[Michael P. Scafuri](https://dblp.org/pid/372/9474.html), Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png), [Nicholas DeLong](https://dblp.org/pid/372/9505.html):

Visualizing H. L. Hunley: Understanding the past through novel facial approximation of the crew of a Civil War submarine (short paper). [IUI Workshops2024](https://dblp.org/db/conf/iui/iui2024w.html#conf/iui/ScafuriPD24)
- 2020
- ![](https://dblp.org/img/n.png)

\[c12\]
[Warren N. White](https://dblp.org/pid/157/8187.html), Eric Patterson, [Nahid Uzzaman](https://dblp.org/pid/271/6634.html):

A Voltage Control Paradigm for Economic Brushless DC Motor Control. [ACC2020](https://dblp.org/db/conf/amcc/amcc2020.html#conf/amcc/WhitePU20): 4289-4294
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[c11\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Khoa Luu](https://dblp.org/pid/43/8092.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Nghia Nguyen](https://dblp.org/pid/230/7933.html), Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Automatic Face Aging in Videos via Deep Reinforcement Learning. [CVPR2019](https://dblp.org/db/conf/cvpr/cvpr2019.html#conf/cvpr/DuongLQNPBL19): 10013-10022
- ![](https://dblp.org/img/n.png)

\[c10\]
[Samuel Park](https://dblp.org/pid/329/9974.html), Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png), [Carl Baum](https://dblp.org/pid/261/8859.html):

Long Short-Term Memory and Convolutional Neural Networks for Active Noise Control. [ICFSP2019](https://dblp.org/db/conf/icfsp/icfsp2019.html#conf/icfsp/ParkPB19): 121-125
- 2018
- ![](https://dblp.org/img/n.png)

\[i1\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Khoa Luu](https://dblp.org/pid/43/8092.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Nghia Nguyen](https://dblp.org/pid/230/7933.html), Eric Patterson, [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), [Ngan Le](https://dblp.org/pid/37/245.html):

Automatic Face Aging in Videos via Deep Reinforcement Learning. [CoRRabs/1811.11082](https://dblp.org/db/journals/corr/corr1811.html#journals/corr/abs-1811-11082) (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[c9\]
Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png), [Devin Simpson](https://dblp.org/pid/157/7599.html):

Dataset and Metrics for Adult Age-Progression Evaluation. [ACM Southeast Regional Conference2017](https://dblp.org/db/conf/ACMse/ACMse2017.html#conf/ACMse/PattersonS17): 248-251
- 2014
- ![](https://dblp.org/img/n.png)

\[c8\]
Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png), [Devin Simpson](https://dblp.org/pid/157/7599.html), [Amrutha Sethuram](https://dblp.org/pid/72/233.html):

Establishing a test set and initial comparisons for quantitatively evaluating synthetic age progression for adult aging. [IJCB2014](https://dblp.org/db/conf/icb/ijcb2014.html#conf/icb/PattersonSS14): 1-8
- 2013
- ![](https://dblp.org/img/n.png)

\[c7\]
Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png), [Amrutha Sethuram](https://dblp.org/pid/72/233.html), [Karl Ricanek](https://dblp.org/pid/39/609.html):

An improved rendering technique for active-appearance-model-based automated age progression. [SIGGRAPH Posters2013](https://dblp.org/db/conf/siggraph/siggraph2013posters.html#conf/siggraph/PattersonSR13): 60
- 2012
- ![](https://dblp.org/img/n.png)

\[c6\]
[Jason Vandeventer](https://dblp.org/pid/39/8855.html), Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png):

Differentiating Duchenne from non-Duchenne smiles using active appearance models. [BTAS2012](https://dblp.org/db/conf/btas/btas2012.html#conf/btas/VandeventerP12): 319-324
- 2011
- ![](https://dblp.org/img/n.png)

\[c5\]
[Adam E. Gaweda](https://dblp.org/pid/86/6226.html), Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png):

Individual identification based on facial dynamics during expressions using active-appearance-based Hidden Markov Models. [FG2011](https://dblp.org/db/conf/fgr/fg2011.html#conf/fgr/GawedaP11): 797-802
- ![](https://dblp.org/img/n.png)

\[c4\]
[Wankou Yang](https://dblp.org/pid/99/3602.html), [Amrutha Sethuram](https://dblp.org/pid/72/233.html), Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png), [Karl Ricanek](https://dblp.org/pid/39/609.html), [Changyin Sun](https://dblp.org/pid/64/221.html):

Gender Classification Using the Profile. [ISNN (2)2011](https://dblp.org/db/conf/isnn/isnn2011-2.html#conf/isnn/YangSPRS11): 288-295
- 2010
- ![](https://dblp.org/img/n.png)

\[c3\]
[Amrutha Sethuram](https://dblp.org/pid/72/233.html), [Karl Ricanek](https://dblp.org/pid/39/609.html), Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png):

A hierarchical approach to facial aging. [CVPR Workshops2010](https://dblp.org/db/conf/cvpr/cvprw2010.html#conf/cvpr/SethuramRP10): 100-107
- ![](https://dblp.org/img/n.png)

\[c2\]
[Amrutha Sethuram](https://dblp.org/pid/72/233.html), [Karl Ricanek](https://dblp.org/pid/39/609.html), Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png):

A comparative study of active appearance model annotation schemes for the face. [ICVGIP2010](https://dblp.org/db/conf/icvgip/icvgip2010.html#conf/icvgip/SethuramRP10): 367-374
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2009
- ![](https://dblp.org/img/n.png)

\[c1\]
[Amrutha Sethuram](https://dblp.org/pid/72/233.html), Eric Patterson![](https://dblp.org/img/orcid-mark.12x12.png), [Karl Ricanek](https://dblp.org/pid/39/609.html), [Allen Rawls](https://dblp.org/pid/49/5332.html):

Improvements and Performance Evaluation Concerning Synthetic Age Progression and Face Recognition Affected by Adult Aging. [ICB2009](https://dblp.org/db/conf/icb/icb2009.html#conf/icb/SethuramPRR09): 62-71
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 1991
- ![](https://dblp.org/img/n.png)

\[j1\]
[Hiro-omi Tamura](https://dblp.org/pid/19/6789.html), [Chie Kohchi](https://dblp.org/pid/91/57.html), [Ryutaro Yamada](https://dblp.org/pid/94/3809.html), [Tomotake Ikeda](https://dblp.org/pid/34/3895.html), [Osamu Koiwai](https://dblp.org/pid/18/202.html), Eric Patterson, [Jack D. Keene](https://dblp.org/pid/42/5752.html), [Kosuke Okada](https://dblp.org/pid/56/4779.html), [Eigil Kjeldsen](https://dblp.org/pid/90/1641.html), [Ken Nishikawa](https://dblp.org/pid/45/6433.html):

Molecular cloning of a cDNA of a camptothecin-resistant human DNA topoisomerase I and identification of mutation sites. [Nucleic Acids Res.19(1)](https://dblp.org/db/journals/nar/nar19.html#journals/nar/TamuraKYIKPKOKN91): 69-75 (1991)
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/79/1282.html?view=joint&param=1 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=3)

[Jessica Baron-Lis](https://dblp.org/pid/427/3571.html)

[\[c14\]](https://dblp.org/pid/79/1282.html#c14)

[2](https://dblp.org/pid/79/1282.html?view=joint&param=2 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=4)

[Carl Baum](https://dblp.org/pid/261/8859.html)

[\[c10\]](https://dblp.org/pid/79/1282.html#c10)

[3](https://dblp.org/pid/79/1282.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[Tien D. Bui](https://dblp.org/pid/b/TienDBui.html)

[\[c11\]](https://dblp.org/pid/79/1282.html#c11) [\[i1\]](https://dblp.org/pid/79/1282.html#i1)

[4](https://dblp.org/pid/79/1282.html?view=joint&param=4 "show joint publications")

[![5](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=5)

[Nicholas DeLong](https://dblp.org/pid/372/9505.html)

[\[c13\]](https://dblp.org/pid/79/1282.html#c13)

[5](https://dblp.org/pid/79/1282.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[Chi Nhan Duong](https://dblp.org/pid/16/11112.html)

[\[c11\]](https://dblp.org/pid/79/1282.html#c11) [\[i1\]](https://dblp.org/pid/79/1282.html#i1)

[6](https://dblp.org/pid/79/1282.html?view=joint&param=6 "show joint publications")

[Adam E. Gaweda](https://dblp.org/pid/86/6226.html)

[\[c5\]](https://dblp.org/pid/79/1282.html#c5)

[7](https://dblp.org/pid/79/1282.html?view=joint&param=7 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=2)

[Tomotake Ikeda](https://dblp.org/pid/34/3895.html)

[\[j1\]](https://dblp.org/pid/79/1282.html#j1)

[8](https://dblp.org/pid/79/1282.html?view=joint&param=8 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=2)

[Jack D. Keene](https://dblp.org/pid/42/5752.html)

[\[j1\]](https://dblp.org/pid/79/1282.html#j1)

[9](https://dblp.org/pid/79/1282.html?view=joint&param=9 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=2)

[Eigil Kjeldsen](https://dblp.org/pid/90/1641.html)

[\[j1\]](https://dblp.org/pid/79/1282.html#j1)

[10](https://dblp.org/pid/79/1282.html?view=joint&param=10 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=2)

[Chie Kohchi](https://dblp.org/pid/91/57.html)

[\[j1\]](https://dblp.org/pid/79/1282.html#j1)

[11](https://dblp.org/pid/79/1282.html?view=joint&param=11 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=2)

[Osamu Koiwai](https://dblp.org/pid/18/202.html)

[\[j1\]](https://dblp.org/pid/79/1282.html#j1)

[12](https://dblp.org/pid/79/1282.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)

aka: Ngan Le

[\[c11\]](https://dblp.org/pid/79/1282.html#c11) [\[i1\]](https://dblp.org/pid/79/1282.html#i1)

[13](https://dblp.org/pid/79/1282.html?view=joint&param=13 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=3)

[Krzysztof Lis](https://dblp.org/pid/167/4194.html)

aka: Krzysztof Baron-Lis

[\[c14\]](https://dblp.org/pid/79/1282.html#c14)

[14](https://dblp.org/pid/79/1282.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[Khoa Luu](https://dblp.org/pid/43/8092.html)

[\[c11\]](https://dblp.org/pid/79/1282.html#c11) [\[i1\]](https://dblp.org/pid/79/1282.html#i1)

[15](https://dblp.org/pid/79/1282.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[Nghia Nguyen](https://dblp.org/pid/230/7933.html)

[\[c11\]](https://dblp.org/pid/79/1282.html#c11) [\[i1\]](https://dblp.org/pid/79/1282.html#i1)

[16](https://dblp.org/pid/79/1282.html?view=joint&param=16 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=2)

[Ken Nishikawa](https://dblp.org/pid/45/6433.html)

[\[j1\]](https://dblp.org/pid/79/1282.html#j1)

[17](https://dblp.org/pid/79/1282.html?view=joint&param=17 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=2)

[Kosuke Okada](https://dblp.org/pid/56/4779.html)

[\[j1\]](https://dblp.org/pid/79/1282.html#j1)

[18](https://dblp.org/pid/79/1282.html?view=joint&param=18 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=4)

[Samuel Park](https://dblp.org/pid/329/9974.html)

[\[c10\]](https://dblp.org/pid/79/1282.html#c10)

[19](https://dblp.org/pid/79/1282.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[Kha Gia Quach](https://dblp.org/pid/73/11111.html)

[\[c11\]](https://dblp.org/pid/79/1282.html#c11) [\[i1\]](https://dblp.org/pid/79/1282.html#i1)

[20](https://dblp.org/pid/79/1282.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[Allen Rawls](https://dblp.org/pid/49/5332.html)

[\[c1\]](https://dblp.org/pid/79/1282.html#c1)

[21](https://dblp.org/pid/79/1282.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[Karl Ricanek](https://dblp.org/pid/39/609.html)

[\[c7\]](https://dblp.org/pid/79/1282.html#c7) [\[c4\]](https://dblp.org/pid/79/1282.html#c4) [\[c3\]](https://dblp.org/pid/79/1282.html#c3) [\[c2\]](https://dblp.org/pid/79/1282.html#c2) [\[c1\]](https://dblp.org/pid/79/1282.html#c1)

[22](https://dblp.org/pid/79/1282.html?view=joint&param=22 "show joint publications")

[![5](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=5)

[Michael P. Scafuri](https://dblp.org/pid/372/9474.html)

[\[c13\]](https://dblp.org/pid/79/1282.html#c13)

[23](https://dblp.org/pid/79/1282.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[Amrutha Sethuram](https://dblp.org/pid/72/233.html)

[\[c8\]](https://dblp.org/pid/79/1282.html#c8) [\[c7\]](https://dblp.org/pid/79/1282.html#c7) [\[c4\]](https://dblp.org/pid/79/1282.html#c4) [\[c3\]](https://dblp.org/pid/79/1282.html#c3) [\[c2\]](https://dblp.org/pid/79/1282.html#c2) [\[c1\]](https://dblp.org/pid/79/1282.html#c1)

[24](https://dblp.org/pid/79/1282.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[Devin Simpson](https://dblp.org/pid/157/7599.html)

[\[c9\]](https://dblp.org/pid/79/1282.html#c9) [\[c8\]](https://dblp.org/pid/79/1282.html#c8)

[25](https://dblp.org/pid/79/1282.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[Changyin Sun 0001](https://dblp.org/pid/64/221.html)

[\[c4\]](https://dblp.org/pid/79/1282.html#c4)

[26](https://dblp.org/pid/79/1282.html?view=joint&param=26 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=2)

[Hiro-omi Tamura](https://dblp.org/pid/19/6789.html)

[\[j1\]](https://dblp.org/pid/79/1282.html#j1)

[27](https://dblp.org/pid/79/1282.html?view=joint&param=27 "show joint publications")

[![6](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=6)

[Nahid Uzzaman](https://dblp.org/pid/271/6634.html)

[\[c12\]](https://dblp.org/pid/79/1282.html#c12)

[28](https://dblp.org/pid/79/1282.html?view=joint&param=28 "show joint publications")

[Jason Vandeventer](https://dblp.org/pid/39/8855.html)

[\[c6\]](https://dblp.org/pid/79/1282.html#c6)

[29](https://dblp.org/pid/79/1282.html?view=joint&param=29 "show joint publications")

[![6](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=6)

[Warren N. White](https://dblp.org/pid/157/8187.html)

[\[c12\]](https://dblp.org/pid/79/1282.html#c12)

[30](https://dblp.org/pid/79/1282.html?view=joint&param=30 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=2)

[Ryutaro Yamada](https://dblp.org/pid/94/3809.html)

[\[j1\]](https://dblp.org/pid/79/1282.html#j1)

[31](https://dblp.org/pid/79/1282.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/79/1282.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c4\]](https://dblp.org/pid/79/1282.html#c4)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/79/1282.html#) [\[–\]](https://dblp.org/pid/79/1282.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/79/1282.html#) [\[–\]](https://dblp.org/pid/79/1282.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/79/1282.html#) [\[–\]](https://dblp.org/pid/79/1282.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/79/1282.html#) [\[–\]](https://dblp.org/pid/79/1282.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/79/1282.html#) [\[–\]](https://dblp.org/pid/79/1282.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)