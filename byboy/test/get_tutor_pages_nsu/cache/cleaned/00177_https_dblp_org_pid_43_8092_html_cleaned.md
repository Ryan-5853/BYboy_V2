> 抓取来源：https://dblp.org/pid/43/8092.html

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

- _affiliation:_ University of Arkansas, Fayetteville, AR, USA

- [Anh Khoa Lanh Luu](https://dblp.org/pid/297/5357.html)
- [Khoa D. Luu](https://dblp.org/pid/410/3112.html)

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Khoa+Luu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F43%2F8092%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Khoa+Luu+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F43%2F8092%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Khoa+Luu+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F43%2F8092%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Khoa+Luu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F43%2F8092%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Khoa+Luu+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F43%2F8092%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Khoa+Luu%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F43%2F8092%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Khoa+Luu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F43%2F8092%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F43%2F8092%3E+%7D+.%0A%0A%7D)

_showing all209 records_

20102026302010: 32011: 42012: 82013: 12014: 12015: 62015: 62016: 122016: 122017: 122017: 122017: 122018: 122018: 122018: 122019: 102019: 102019: 102019: 102020: 122020: 122020: 122020: 122021: 162021: 162021: 162022: 242022: 242022: 242023: 272023: 272023: 272024: 342024: 342024: 342025: 252025: 252025: 252026: 2

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

- ![](https://dblp.org/img/add-mark.12x12.png)T. Hoang Ngan Le (73)
- ![](https://dblp.org/img/add-mark.12x12.png)Chi Nhan Duong (57)
- ![](https://dblp.org/img/add-mark.12x12.png)Thanh-Dat Truong (49)
- ![](https://dblp.org/img/add-mark.12x12.png)Marios Savvides (45)
- ![](https://dblp.org/img/add-mark.12x12.png)Kha Gia Quach (41)
- ![](https://dblp.org/img/add-mark.12x12.png)Xuan-Bac Nguyen (37)
- ![](https://dblp.org/img/add-mark.12x12.png)Pha A. Nguyen (30)
- ![](https://dblp.org/img/add-mark.12x12.png)Tien D. Bui (25)
- ![](https://dblp.org/img/add-mark.12x12.png)Xin Li 0005 (22)
- ![](https://dblp.org/img/add-mark.12x12.png)Hoang-Quan Nguyen (18)

- _165 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (135)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0003-2104-0901 (75)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (99)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (23)
- ![](https://dblp.org/img/add-mark.12x12.png)ICIP (8)
- ![](https://dblp.org/img/add-mark.12x12.png)BTAS (7)
- ![](https://dblp.org/img/add-mark.12x12.png)ICPR (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Pattern Recognit. (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Int. J. Comput. Vis. (5)
- ![](https://dblp.org/img/add-mark.12x12.png)NeurIPS (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Neurocomputing (4)
- ![](https://dblp.org/img/add-mark.12x12.png)ICCV (4)

- _31 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)open (125)
- ![](https://dblp.org/img/add-mark.12x12.png)closed (82)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[j35\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Manuel Serna-Aguilera](https://dblp.org/pid/336/4123.html), [Arabinda Kumar Choudhary](https://dblp.org/pid/393/1551.html), [Pawan Sinha](https://dblp.org/pid/51/6599.html), [Xin Li](https://dblp.org/pid/09/1365-5.html), Khoa Luu:

COBRA: A Continual Learning Approach to Vision-Brain Understanding. [Int. J. Comput. Vis.134(1)](https://dblp.org/db/journals/ijcv/ijcv134.html#journals/ijcv/NguyenSCSLL26): 30 (2026)
- ![](https://dblp.org/img/n.png)

\[j34\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hojin Jang](https://dblp.org/pid/193/8557.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pawan Sinha](https://dblp.org/pid/51/6599.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

BRACTIVE: A Brain Activation Approach to Human Visual Brain Learning. [IEEE Trans. Pattern Anal. Mach. Intell.48(2)](https://dblp.org/db/journals/pami/pami48.html#journals/pami/NguyenJLKSL26): 1202-1214 (2026)
- 2025
- ![](https://dblp.org/img/n.png)

\[j33\]
[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alexander H. Nelson](https://dblp.org/pid/140/7986-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Han-Seok Seo](https://dblp.org/pid/138/6741.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Page Daniel Dobbs](https://dblp.org/pid/344/0595.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

SoGAR: Self-Supervised Spatiotemporal Attention-Based Social Group Activity Recognition. [IEEE Access13](https://dblp.org/db/journals/access/access13.html#journals/access/ChappaNNSLDL25): 33631-33642 (2025)
- ![](https://dblp.org/img/n.png)

\[j32\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rishi Madhok](https://dblp.org/pid/216/7116.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), Khoa Luu:

Autoregressive Temporal Modeling for Advanced Tracking-by-Diffusion. [Int. J. Comput. Vis.133(8)](https://dblp.org/db/journals/ijcv/ijcv133.html#journals/ijcv/NguyenMRL25): 5505-5526 (2025)
- ![](https://dblp.org/img/n.png)

\[j31\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Ashley Dowling](https://dblp.org/pid/321/0870.html), [Xin Li](https://dblp.org/pid/09/1365-5.html), Khoa Luu:

Insect-Foundation: A Foundation Model and Large Multimodal Dataset for Vision-Language Insect Understanding. [Int. J. Comput. Vis.133(10)](https://dblp.org/db/journals/ijcv/ijcv133.html#journals/ijcv/TruongNNDLL25): 7128-7153 (2025)
- ![](https://dblp.org/img/n.png)

\[j30\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

Cross-view action recognition understanding from exocentric to egocentric perspective. [Neurocomputing614](https://dblp.org/db/journals/ijon/ijon614.html#journals/ijon/TruongL25): 128731 (2025)
- ![](https://dblp.org/img/n.png)

\[j29\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pawan Sinha](https://dblp.org/pid/51/6599.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

Brainformer: Mimic human visual brain functions to machine vision models via fMRI. [Neurocomputing620](https://dblp.org/db/journals/ijon/ijon620.html#journals/ijon/NguyenLSKL25): 129213 (2025)
- ![](https://dblp.org/img/n.png)

\[j28\]
[Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Samuel Yen-Chi Chen](https://dblp.org/pid/244/2264.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), [Nicholas Borys](https://dblp.org/pid/381/4679.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html), Khoa Luu:

Diffusion-inspired quantum noise mitigation in parameterized quantum circuits. [Quantum Mach. Intell.7(1)](https://dblp.org/db/journals/qmi/qmi7.html#journals/qmi/NguyenNCCBKL25): 55 (2025)
- ![](https://dblp.org/img/n.png)

\[c73\]
[Huu-Thien Tran](https://dblp.org/pid/400/4998.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), Khoa Luu:

BIMA: Bijective Maximum Likelihood Learning Approach to Hallucination Prediction and Mitigation in Large Vision-Language Models. [CVPR Workshops2025](https://dblp.org/db/conf/cvpr/cvprw2025.html#conf/cvpr/TranTL25): 5302-5311
- ![](https://dblp.org/img/n.png)

\[c72\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Utsav Prabhu](https://dblp.org/pid/54/10072.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html), Khoa Luu:

FALCON: Fairness Learning via Contrastive Attention Approach to Continual Semantic Scene Understanding. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/TruongPRCL25): 15065-15075
- ![](https://dblp.org/img/n.png)

\[c71\]
[Trong-Thuan Nguyen](https://dblp.org/pid/344/5384.html), [Pha Nguyen](https://dblp.org/pid/398/0197.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html), [Alper Yilmaz](https://dblp.org/pid/11/1315-1.html), Khoa Luu:

HyperGLM: HyperGraph for Video Scene Graph Generation and Anticipation. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/NguyenNCYL25): 29150-29160
- ![](https://dblp.org/img/n.png)

\[c70\]
[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html), Khoa Luu:

LiGAR: LiDAR-Guided Hierarchical Transformer for Multi-Modal Group Activity Recognition. [WACV2025](https://dblp.org/db/conf/wacv/wacv2025.html#conf/wacv/ChappaL25): 3035-3044
- ![](https://dblp.org/img/n.png)

\[i100\]
[James Holliday](https://dblp.org/pid/376/0876.html), [Eneko Osaba](https://dblp.org/pid/47/10138.html), Khoa Luu:

An Advanced Hybrid Quantum Tabu Search Approach to Vehicle Routing Problems. [CoRRabs/2501.12652](https://dblp.org/db/journals/corr/corr2501.html#journals/corr/abs-2501-12652) (2025)
- ![](https://dblp.org/img/n.png)

\[i99\]
[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html), [Matthew Shepard](https://dblp.org/pid/397/9407.html), [Connor McCurtain](https://dblp.org/pid/397/9089.html), [Charlotte McCormick](https://dblp.org/pid/393/5022.html), [Page Daniel Dobbs](https://dblp.org/pid/344/0595.html), Khoa Luu:

DEFEND: A Large-scale 1M Dataset and Foundation Model for Tobacco Addiction Prevention. [CoRRabs/2501.13950](https://dblp.org/db/journals/corr/corr2501.html#journals/corr/abs-2501-13950) (2025)
- ![](https://dblp.org/img/n.png)

\[i98\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Ashley Dowling](https://dblp.org/pid/321/0870.html), [Xin Li](https://dblp.org/pid/09/1365-5.html), Khoa Luu:

Insect-Foundation: A Foundation Model and Large Multimodal Dataset for Vision-Language Insect Understanding. [CoRRabs/2502.09906](https://dblp.org/db/journals/corr/corr2502.html#journals/corr/abs-2502-09906) (2025)
- ![](https://dblp.org/img/n.png)

\[i97\]
[Huu-Thien Tran](https://dblp.org/pid/400/4998.html), [Phuoc-Sang Pham](https://dblp.org/pid/387/6533.html), [Thai-Son Tran](https://dblp.org/pid/06/5210.html), Khoa Luu:

MEX: Memory-efficient Approach to Referring Multi-Object Tracking. [CoRRabs/2502.13875](https://dblp.org/db/journals/corr/corr2502.html#journals/corr/abs-2502-13875) (2025)
- ![](https://dblp.org/img/n.png)

\[i96\]
[James B. Holliday](https://dblp.org/pid/402/5752.html), [Darren Blount](https://dblp.org/pid/402/6929.html), [Eneko Osaba](https://dblp.org/pid/47/10138.html), Khoa Luu:

Advanced Quantum Annealing Approach to Vehicle Routing Problems with Time Windows. [CoRRabs/2503.24285](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-24285) (2025)
- ![](https://dblp.org/img/n.png)

\[i95\]
[James Holliday](https://dblp.org/pid/376/0876.html), [Darren Blount](https://dblp.org/pid/402/6929.html), [Hoang Quan Nguyen](https://dblp.org/pid/402/6121.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html), Khoa Luu:

QUADRO: A Hybrid Quantum Optimization Framework for Drone Delivery. [CoRRabs/2503.24301](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-24301) (2025)
- ![](https://dblp.org/img/n.png)

\[i94\]
[Huu-Thien Tran](https://dblp.org/pid/400/4998.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), Khoa Luu:

BIMA: Bijective Maximum Likelihood Learning Approach to Hallucination Prediction and Mitigation in Large Vision-Language Models. [CoRRabs/2505.24649](https://dblp.org/db/journals/corr/corr2505.html#journals/corr/abs-2505-24649) (2025)
- ![](https://dblp.org/img/n.png)

\[i93\]
[Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Sankalp Pandey](https://dblp.org/pid/412/8073.html), [Tim Faltermeier](https://dblp.org/pid/412/8876.html), [Nicholas Borys](https://dblp.org/pid/381/4679.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), Khoa Luu:

φ-Adapt: A Physics-Informed Adaptation Learning Approach to 2D Quantum Material Discovery. [CoRRabs/2507.05184](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-05184) (2025)
- ![](https://dblp.org/img/n.png)

\[i92\]
[Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Sankalp Pandey](https://dblp.org/pid/412/8073.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html), [Ilya Safro](https://dblp.org/pid/64/5096.html), Khoa Luu:

QMoE: A Quantum Mixture of Experts Framework for Scalable Quantum Neural Networks. [CoRRabs/2507.05190](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-05190) (2025)
- ![](https://dblp.org/img/n.png)

\[i91\]
[Trong-Thuan Nguyen](https://dblp.org/pid/344/5384.html), [Pha Nguyen](https://dblp.org/pid/398/0197.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html), [Alper Yilmaz](https://dblp.org/pid/11/1315-1.html), [Minh-Triet Tran](https://dblp.org/pid/44/7448.html), Khoa Luu:

THYME: Temporal Hierarchical-Cyclic Interactivity Modeling for Video Scene Graphs in Aerial Footage. [CoRRabs/2507.09200](https://dblp.org/db/journals/corr/corr2507.html#journals/corr/abs-2507-09200) (2025)
- ![](https://dblp.org/img/n.png)

\[i90\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Christophe Bobda](https://dblp.org/pid/b/ChristopheBobda.html), [Nitin Agarwal](https://dblp.org/pid/72/1395.html), Khoa Luu:

MANGO: Multimodal Attention-based Normalizing Flow Approach to Fusion Learning. [CoRRabs/2508.10133](https://dblp.org/db/journals/corr/corr2508.html#journals/corr/abs-2508-10133) (2025)
- ![](https://dblp.org/img/n.png)

\[i89\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Huu-Thien Tran](https://dblp.org/pid/400/4998.html), [Tran Thai Son](https://dblp.org/pid/06/5210.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), Khoa Luu:

Directed-Tokens: A Robust Multi-Modality Alignment Approach to Large Language-Vision Models. [CoRRabs/2508.14264](https://dblp.org/db/journals/corr/corr2508.html#journals/corr/abs-2508-14264) (2025)
- ![](https://dblp.org/img/n.png)

\[i88\]
[Manuel Serna-Aguilera](https://dblp.org/pid/336/4123.html), [Fiona L. Goggin](https://dblp.org/pid/415/8043.html), [Aranyak Goswami](https://dblp.org/pid/415/8022.html), [Alexander Bucksch](https://dblp.org/pid/44/7634.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Suxing Liu](https://dblp.org/pid/59/7086.html), Khoa Luu:

AGP: A Novel Arabidopsis thaliana Genomics-Phenomics Dataset and its HyperGraph Baseline Benchmarking. [CoRRabs/2508.14934](https://dblp.org/db/journals/corr/corr2508.html#journals/corr/abs-2508-14934) (2025)
- ![](https://dblp.org/img/n.png)

\[i87\]
[Sankalp Pandey](https://dblp.org/pid/412/8073.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Nicholas Borys](https://dblp.org/pid/381/4679.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), Khoa Luu:

CLIFF: Continual Learning for Incremental Flake Features in 2D Material Identification. [CoRRabs/2508.17261](https://dblp.org/db/journals/corr/corr2508.html#journals/corr/abs-2508-17261) (2025)
- ![](https://dblp.org/img/n.png)

\[i86\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Pawan Sinha](https://dblp.org/pid/51/6599.html), Khoa Luu:

BRAIN: Bias-Mitigation Continual Learning Approach to Vision-Brain Understanding. [CoRRabs/2508.18187](https://dblp.org/db/journals/corr/corr2508.html#journals/corr/abs-2508-18187) (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j27\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Apoorva Bisht](https://dblp.org/pid/321/4247.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Benjamin Thompson](https://dblp.org/pid/53/3789.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), Khoa Luu, [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Two-Dimensional Quantum Material Identification via Self-Attention and Soft-Labeling in Deep Learning. [IEEE Access12](https://dblp.org/db/journals/access/access12.html#journals/access/NguyenBTCLK24): 139683-139691 (2024)
- ![](https://dblp.org/img/n.png)

\[j26\]
[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Page Daniel Dobbs](https://dblp.org/pid/344/0595.html), Khoa Luu:

React: recognize every action everywhere all at once. [Mach. Vis. Appl.35(4)](https://dblp.org/db/journals/mva/mva35.html#journals/mva/ChappaNDL24): 102 (2024)
- ![](https://dblp.org/img/n.png)

\[j25\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Son Lam Phung](https://dblp.org/pid/93/737.html), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

Multi-camera multi-object tracking on the move via single-stage global association approach. [Pattern Recognit.152](https://dblp.org/db/journals/pr/pr152.html#journals/pr/NguyenQDPLL24): 110457 (2024)
- ![](https://dblp.org/img/n.png)

\[j24\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

Quantum visual feature encoding revisited. [Quantum Mach. Intell.6(2)](https://dblp.org/db/journals/qmi/qmi6.html#journals/qmi/NguyenNCKL24): 61 (2024)
- ![](https://dblp.org/img/n.png)

\[j23\]
[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thi Hoang Ngan Le](https://dblp.org/pid/37/245.html), [Page Daniel Dobbs](https://dblp.org/pid/344/0595.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

HAtt-Flow: Hierarchical Attention-Flow Mechanism for Group-Activity Scene Graph Generation in Videos. [Sensors24(11)](https://dblp.org/db/journals/sensors/sensors24.html#journals/sensors/ChappaNLDL24): 3372 (2024)
- ![](https://dblp.org/img/n.png)

\[c69\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Pierce Helton](https://dblp.org/pid/328/9598.html), [Ahmed Moustafa](https://dblp.org/pid/117/1672.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

CONDA: Continual Unsupervised Domain Adaptation Learning in Visual Perception for Self-Driving Cars. [CVPR Workshops2024](https://dblp.org/db/conf/cvpr/cvprw2024.html#conf/cvpr/TruongHMCL22): 5642-5650
- ![](https://dblp.org/img/n.png)

\[c68\]
[Trong-Thuan Nguyen](https://dblp.org/pid/344/5384.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), Khoa Luu:

HIG: Hierarchical Interlacement Graph Approach to Scene Graph Generation in Video Understanding. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/NguyenNL24): 18384-18394
- ![](https://dblp.org/img/n.png)

\[c67\]
[Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Ashley Dowling](https://dblp.org/pid/321/0870.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

Insect-Foundation: A Foundation Model and Large-Scale 1M Dataset for Visual Insect Understanding. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/NguyenTND0L24): 21945-21955
- ![](https://dblp.org/img/n.png)

\[c66\]
[Kim Hoang Tran](https://dblp.org/pid/348/6627.html), [Anh Duy Le Dinh](https://dblp.org/pid/348/6822.html), [Tien-Phat Nguyen](https://dblp.org/pid/271/7464.html), [Thinh Phan](https://dblp.org/pid/331/3164.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), Khoa Luu, [Donald A. Adjeroh](https://dblp.org/pid/30/1579.html), [Gianfranco Doretto](https://dblp.org/pid/61/3857.html), [Ngan Hoang Le](https://dblp.org/pid/361/2252.html):

Z-GMOT: Zero-shot Generic Multiple Object Tracking. [NAACL-HLT (Findings)2024](https://dblp.org/db/conf/naacl/naacl2024f.html#conf/naacl/TranDNPNLADL24): 3468-3479
- ![](https://dblp.org/img/n.png)

\[c65\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Ngan Le](https://dblp.org/pid/37/245.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html), [Alper Yilmaz](https://dblp.org/pid/11/1315-1.html), Khoa Luu:

DINTR: Tracking via Diffusion-based Interpolation. [NeurIPS2024](https://dblp.org/db/conf/nips/neurips2024.html#conf/nips/NguyenLCYL24)
- ![](https://dblp.org/img/n.png)

\[c64\]
[Trong-Thuan Nguyen](https://dblp.org/pid/344/5384.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Xin Li](https://dblp.org/pid/09/1365-5.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html), [Alper Yilmaz](https://dblp.org/pid/11/1315-1.html), Khoa Luu:

CYCLO: Cyclic Graph Transformer Approach to Multi-Object Relationship Modeling in Aerial Videos. [NeurIPS2024](https://dblp.org/db/conf/nips/neurips2024.html#conf/nips/NguyenN0CYL24)
- ![](https://dblp.org/img/n.png)

\[c63\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Utsav Prabhu](https://dblp.org/pid/54/10072.html), [Dongyi Wang](https://dblp.org/pid/70/10768.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), [Susan Gauch](https://dblp.org/pid/g/SusanGauch.html), [Jeyamkondan Subbiah](https://dblp.org/pid/178/0722.html), Khoa Luu:

EAGLE: Efficient Adaptive Geometry-based Learning in Cross-view Understanding. [NeurIPS2024](https://dblp.org/db/conf/nips/neurips2024.html#conf/nips/TruongPWRGSL24)
- ![](https://dblp.org/img/n.png)

\[c62\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Samuel Yen-Chi Chen](https://dblp.org/pid/244/2264.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), Khoa Luu:

QClusformer: A Quantum Transformer-based Framework for Unsupervised Visual Clustering. [QCE2024](https://dblp.org/db/conf/qce/qce2024.html#conf/qce/NguyenNCKCL24): 347-352
- ![](https://dblp.org/img/n.png)

\[c61\]
[James Holliday](https://dblp.org/pid/376/0876.html), [Braeden Morgan](https://dblp.org/pid/376/0612.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), Khoa Luu:

Hybrid Quantum Tabu Search for Solving the Vehicle Routing Problem. [QCE2024](https://dblp.org/db/conf/qce/qce2024.html#conf/qce/HollidayMCL24): 353-358
- ![](https://dblp.org/img/n.png)

\[c60\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html), Khoa Luu:

Hierarchical Quantum Control Gates for Functional MRI Understanding. [SiPS2024](https://dblp.org/db/conf/sips/sips2024.html#conf/sips/NguyenNCKL24): 159-164
- ![](https://dblp.org/img/n.png)

\[i85\]
[Manuel Serna-Aguilera](https://dblp.org/pid/336/4123.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Asmita Singh](https://dblp.org/pid/371/4265.html), [Lydia Rockers](https://dblp.org/pid/371/4142.html), [Se-Woong Park](https://dblp.org/pid/94/411.html), [Leslie Neely](https://dblp.org/pid/286/1228.html), [Han-Seok Seo](https://dblp.org/pid/138/6741.html), Khoa Luu:

Video-Based Autism Detection with Deep Learning. [CoRRabs/2402.16774](https://dblp.org/db/journals/corr/corr2402.html#journals/corr/abs-2402-16774) (2024)
- ![](https://dblp.org/img/n.png)

\[i84\]
[James Holliday](https://dblp.org/pid/376/0876.html), [Braeden Morgan](https://dblp.org/pid/376/0612.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), Khoa Luu:

Hybrid Quantum Tabu Search for Solving the Vehicle Routing Problem. [CoRRabs/2404.13203](https://dblp.org/db/journals/corr/corr2404.html#journals/corr/abs-2404-13203) (2024)
- ![](https://dblp.org/img/n.png)

\[i83\]
[Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), Khoa Luu:

Multi-view Action Recognition via Directed Gromov-Wasserstein Discrepancy. [CoRRabs/2405.01337](https://dblp.org/db/journals/corr/corr2405.html#journals/corr/abs-2405-01337) (2024)
- ![](https://dblp.org/img/n.png)

\[i82\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Hojin Jang](https://dblp.org/pid/193/8557.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pawan Sinha](https://dblp.org/pid/51/6599.html), Khoa Luu:

BRACTIVE: A Brain Activation Approach to Human Visual Brain Learning. [CoRRabs/2405.18808](https://dblp.org/db/journals/corr/corr2405.html#journals/corr/abs-2405-18808) (2024)
- ![](https://dblp.org/img/n.png)

\[i81\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Samuel Yen-Chi Chen](https://dblp.org/pid/244/2264.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hugh Churchill](https://dblp.org/pid/241/9507.html), Khoa Luu:

QClusformer: A Quantum Transformer-based Framework for Unsupervised Visual Clustering. [CoRRabs/2405.19722](https://dblp.org/db/journals/corr/corr2405.html#journals/corr/abs-2405-19722) (2024)
- ![](https://dblp.org/img/n.png)

\[i80\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

Quantum Visual Feature Encoding Revisited. [CoRRabs/2405.19725](https://dblp.org/db/journals/corr/corr2405.html#journals/corr/abs-2405-19725) (2024)
- ![](https://dblp.org/img/n.png)

\[i79\]
[Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Samuel Yen-Chi Chen](https://dblp.org/pid/244/2264.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), [Nicholas Borys](https://dblp.org/pid/381/4679.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

Diffusion-Inspired Quantum Noise Mitigation in Parameterized Quantum Circuits. [CoRRabs/2406.00843](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-00843) (2024)
- ![](https://dblp.org/img/n.png)

\[i78\]
[Trong-Thuan Nguyen](https://dblp.org/pid/344/5384.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jackson David Cothren](https://dblp.org/pid/335/1787.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alper Yilmaz](https://dblp.org/pid/11/1315-1.html), Khoa Luu:

CYCLO: Cyclic Graph Transformer Approach to Multi-Object Relationship Modeling in Aerial Videos. [CoRRabs/2406.01029](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-01029) (2024)
- ![](https://dblp.org/img/n.png)

\[i77\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Utsav Prabhu](https://dblp.org/pid/54/10072.html), [Dongyi Wang](https://dblp.org/pid/70/10768.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), [Susan Gauch](https://dblp.org/pid/g/SusanGauch.html), [Jeyamkondan Subbiah](https://dblp.org/pid/178/0722.html), Khoa Luu:

EAGLE: Efficient Adaptive Geometry-based Learning in Cross-view Understanding. [CoRRabs/2406.01429](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-01429) (2024)
- ![](https://dblp.org/img/n.png)

\[i76\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

ED-SAM: An Efficient Diffusion Sampling Approach to Domain Generalization in Vision-Language Foundation Models. [CoRRabs/2406.01432](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-01432) (2024)
- ![](https://dblp.org/img/n.png)

\[i75\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html), Khoa Luu:

Hierarchical Quantum Control Gates for Functional MRI Understanding. [CoRRabs/2408.03596](https://dblp.org/db/journals/corr/corr2408.html#journals/corr/abs-2408-03596) (2024)
- ![](https://dblp.org/img/n.png)

\[i74\]
[Manuel Serna-Aguilera](https://dblp.org/pid/336/4123.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Han-Seok Seo](https://dblp.org/pid/138/6741.html), Khoa Luu:

A Novel Dataset for Video-Based Autism Classification Leveraging Extra-Stimulatory Behavior. [CoRRabs/2409.04598](https://dblp.org/db/journals/corr/corr2409.html#journals/corr/abs-2409-04598) (2024)
- ![](https://dblp.org/img/n.png)

\[i73\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Ngan Le](https://dblp.org/pid/37/245.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alper Yilmaz](https://dblp.org/pid/11/1315-1.html), Khoa Luu:

DINTR: Tracking via Diffusion-based Interpolation. [CoRRabs/2410.10053](https://dblp.org/db/journals/corr/corr2410.html#journals/corr/abs-2410-10053) (2024)
- ![](https://dblp.org/img/n.png)

\[i72\]
[Ravi Teja N. V. S. Chappa](https://dblp.org/pid/321/0642.html), [Page Daniel Dobbs](https://dblp.org/pid/344/0595.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), Khoa Luu:

FLAASH: Flow-Attention Adaptive Semantic Hierarchical Fusion for Multi-Modal Tobacco Content Analysis. [CoRRabs/2410.19896](https://dblp.org/db/journals/corr/corr2410.html#journals/corr/abs-2410-19896) (2024)
- ![](https://dblp.org/img/n.png)

\[i71\]
[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html), Khoa Luu:

LiGAR: LiDAR-Guided Hierarchical Transformer for Multi-Modal Group Activity Recognition. [CoRRabs/2410.21108](https://dblp.org/db/journals/corr/corr2410.html#journals/corr/abs-2410-21108) (2024)
- ![](https://dblp.org/img/n.png)

\[i70\]
[Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), [Arabinda Kumar Choudhary](https://dblp.org/pid/393/1551.html), [Pawan Sinha](https://dblp.org/pid/51/6599.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html), Khoa Luu:

Quantum-Brain: Quantum-Inspired Neural Network Approach to Vision-Brain Understanding. [CoRRabs/2411.13378](https://dblp.org/db/journals/corr/corr2411.html#journals/corr/abs-2411-13378) (2024)
- ![](https://dblp.org/img/n.png)

\[i69\]
[Ravi Teja N. V. S. Chappa](https://dblp.org/pid/321/0642.html), [Charlotte McCormick](https://dblp.org/pid/393/5022.html), [Susana Rodriguez Gongora](https://dblp.org/pid/393/0878.html), [Page Daniel Dobbs](https://dblp.org/pid/344/0595.html), Khoa Luu:

Public Health Advocacy Dataset: A Dataset of Tobacco Usage Videos from Social Media. [CoRRabs/2411.13572](https://dblp.org/db/journals/corr/corr2411.html#journals/corr/abs-2411-13572) (2024)
- ![](https://dblp.org/img/n.png)

\[i68\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Arabinda Kumar Choudhary](https://dblp.org/pid/393/1551.html), [Pawan Sinha](https://dblp.org/pid/51/6599.html), [Xi Li](https://dblp.org/pid/46/2311-3.html), Khoa Luu:

COBRA: A Continual Learning Approach to Vision-Brain Understanding. [CoRRabs/2411.17475](https://dblp.org/db/journals/corr/corr2411.html#journals/corr/abs-2411-17475) (2024)
- ![](https://dblp.org/img/n.png)

\[i67\]
[Trong-Thuan Nguyen](https://dblp.org/pid/344/5384.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alper Yilmaz](https://dblp.org/pid/11/1315-1.html), Khoa Luu:

HyperGLM: HyperGraph for Video Scene Graph Generation and Anticipation. [CoRRabs/2411.18042](https://dblp.org/db/journals/corr/corr2411.html#journals/corr/abs-2411-18042) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j22\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), Khoa Luu:

LIAAD: Lightweight attentive angular distillation for large-scale age-invariant face recognition. [Neurocomputing543](https://dblp.org/db/journals/ijon/ijon543.html#journals/ijon/TruongDQLBL23): 126198 (2023)
- ![](https://dblp.org/img/n.png)

\[c59\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Susan Gauch](https://dblp.org/pid/g/SusanGauch.html), [Han-Seok Seo](https://dblp.org/pid/138/6741.html), Khoa Luu:

Micron-BERT: BERT-Based Facial Micro-Expression Recognition. [CVPR2023](https://dblp.org/db/conf/cvpr/cvpr2023.html#conf/cvpr/NguyenD0GSL23): 1482-1492
- ![](https://dblp.org/img/n.png)

\[c58\]
[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Alexander H. Nelson](https://dblp.org/pid/140/7986-1.html), [Han-Seok Seo](https://dblp.org/pid/138/6741.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Page Daniel Dobbs](https://dblp.org/pid/344/0595.html), Khoa Luu:

SPARTAN: Self-supervised Spatiotemporal Transformers Approach to Group Activity Recognition. [CVPR Workshops2023](https://dblp.org/db/conf/cvpr/cvprw2023.html#conf/cvpr/ChappaNNSLDL23): 5158-5168
- ![](https://dblp.org/img/n.png)

\[c57\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

FREDOM: Fairness Domain Adaptation Approach to Semantic Scene Understanding. [CVPR2023](https://dblp.org/db/conf/cvpr/cvpr2023.html#conf/cvpr/TruongLRCL23): 19988-19997
- ![](https://dblp.org/img/n.png)

\[c56\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Kris Kitani](https://dblp.org/pid/42/163.html), Khoa Luu:

Type-to-Track: Retrieve Any Object via Prompt-based Tracking. [NeurIPS2023](https://dblp.org/db/conf/nips/neurips2023.html#conf/nips/NguyenQKL23)
- ![](https://dblp.org/img/n.png)

\[c55\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), Khoa Luu:

Fairness Continual Learning Approach to Semantic Scene Understanding in Open-World Environments. [NeurIPS2023](https://dblp.org/db/conf/nips/neurips2023.html#conf/nips/TruongNRL23)
- ![](https://dblp.org/img/n.png)

\[c54\]
[Yatish Dubasi](https://dblp.org/pid/356/9091.html), [Qinghua Li](https://dblp.org/pid/34/4755.html), Khoa Luu:

POP-HIT: Partially Order-Preserving Hash-Induced Transformation for Privacy Protection in Face Recognition Access Control. [SecureComm (2)2023](https://dblp.org/db/conf/securecomm/securecomm2023-2.html#conf/securecomm/DubasiLL23): 80-98
- ![](https://dblp.org/img/n.png)

\[i66\]
[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alexander H. Nelson](https://dblp.org/pid/140/7986-1.html), [Han-Seok Seo](https://dblp.org/pid/138/6741.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Page Daniel Dobbs](https://dblp.org/pid/344/0595.html), Khoa Luu:

SPARTAN: Self-supervised Spatiotemporal Transformers Approach to Group Activity Recognition. [CoRRabs/2303.12149](https://dblp.org/db/journals/corr/corr2303.html#journals/corr/abs-2303-12149) (2023)
- ![](https://dblp.org/img/n.png)

\[i65\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Ngan Le](https://dblp.org/pid/37/245.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

FREDOM: Fairness Domain Adaptation Approach to Semantic Scene Understanding. [CoRRabs/2304.02135](https://dblp.org/db/journals/corr/corr2304.html#journals/corr/abs-2304-02135) (2023)
- ![](https://dblp.org/img/n.png)

\[i64\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Susan Gauch](https://dblp.org/pid/g/SusanGauch.html), [Han-Seok Seo](https://dblp.org/pid/138/6741.html), Khoa Luu:

Micron-BERT: BERT-based Facial Micro-Expression Recognition. [CoRRabs/2304.03195](https://dblp.org/db/journals/corr/corr2304.html#journals/corr/abs-2304-03195) (2023)
- ![](https://dblp.org/img/n.png)

\[i63\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Ashley Dowling](https://dblp.org/pid/321/0870.html), [Son Lam Phung](https://dblp.org/pid/93/737.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

CROVIA: Seeing Drone Scenes from Car Perspective via Cross-View Adaptation. [CoRRabs/2304.07199](https://dblp.org/db/journals/corr/corr2304.html#journals/corr/abs-2304-07199) (2023)
- ![](https://dblp.org/img/n.png)

\[i62\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Pierce Helton](https://dblp.org/pid/328/9598.html), [Ashley Dowling](https://dblp.org/pid/321/0870.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

CoMaL: Conditional Maximum Likelihood Approach to Self-supervised Domain Adaptation in Long-tail Semantic Segmentation. [CoRRabs/2304.07372](https://dblp.org/db/journals/corr/corr2304.html#journals/corr/abs-2304-07372) (2023)
- ![](https://dblp.org/img/n.png)

\[i61\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Marios Savvides](https://dblp.org/pid/13/3793.html), [Kaushik Roy](https://dblp.org/pid/r/KaushikRoy3.html), Khoa Luu:

Fairness in Visual Clustering: A Novel Transformer Clustering Approach. [CoRRabs/2304.07408](https://dblp.org/db/journals/corr/corr2304.html#journals/corr/abs-2304-07408) (2023)
- ![](https://dblp.org/img/n.png)

\[i60\]
[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Alexander H. Nelson](https://dblp.org/pid/140/7986-1.html), [Han-Seok Seo](https://dblp.org/pid/138/6741.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Page Daniel Dobbs](https://dblp.org/pid/344/0595.html), Khoa Luu:

SoGAR: Self-supervised Spatiotemporal Attention-based Social Group Activity Recognition. [CoRRabs/2305.06310](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-06310) (2023)
- ![](https://dblp.org/img/n.png)

\[i59\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Kris Kitani](https://dblp.org/pid/42/163.html), Khoa Luu:

Type-to-Track: Retrieve Any Object via Prompt-based Tracking. [CoRRabs/2305.13495](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-13495) (2023)
- ![](https://dblp.org/img/n.png)

\[i58\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), Khoa Luu:

Cross-view Action Recognition Understanding From Exocentric to Egocentric Perspective. [CoRRabs/2305.15699](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-15699) (2023)
- ![](https://dblp.org/img/n.png)

\[i57\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), Khoa Luu:

Fairness Continual Learning Approach to Semantic Scene Understanding in Open-World Environments. [CoRRabs/2305.15700](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-15700) (2023)
- ![](https://dblp.org/img/n.png)

\[i56\]
[Kim Hoang Tran](https://dblp.org/pid/348/6627.html), [Anh Duy Le Dinh](https://dblp.org/pid/348/6822.html), [Tien-Phat Nguyen](https://dblp.org/pid/271/7464.html), [Thinh Phan](https://dblp.org/pid/331/3164.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), Khoa Luu, [Donald A. Adjeroh](https://dblp.org/pid/30/1579.html), [Gianfranco Doretto](https://dblp.org/pid/61/3857.html), [Ngan Hoang Le](https://dblp.org/pid/361/2252.html):

Z-GMOT: Zero-shot Generic Multiple Object Tracking. [CoRRabs/2305.17648](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-17648) (2023)
- ![](https://dblp.org/img/n.png)

\[i55\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [John Gauch](https://dblp.org/pid/70/5847.html), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), Khoa Luu:

UTOPIA: Unconstrained Tracking Objects without Preliminary Examination via Cross-Domain Adaptation. [CoRRabs/2306.09613](https://dblp.org/db/journals/corr/corr2306.html#journals/corr/abs-2306-09613) (2023)
- ![](https://dblp.org/img/n.png)

\[i54\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Xudong Liu](https://dblp.org/pid/90/2144-6.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

The Algonauts Project 2023 Challenge: UARK-UAlbany Team Solution. [CoRRabs/2308.00262](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-00262) (2023)
- ![](https://dblp.org/img/n.png)

\[i53\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Benjamin Thompson](https://dblp.org/pid/53/3789.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), Khoa Luu, [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Quantum Vision Clustering. [CoRRabs/2309.09907](https://dblp.org/db/journals/corr/corr2309.html#journals/corr/abs-2309-09907) (2023)
- ![](https://dblp.org/img/n.png)

\[i52\]
[Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Ashley Dowling](https://dblp.org/pid/321/0870.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

Insect-Foundation: A Foundation Model and Large-scale 1M Dataset for Visual Insect Understanding. [CoRRabs/2311.15206](https://dblp.org/db/journals/corr/corr2311.html#journals/corr/abs-2311-15206) (2023)
- ![](https://dblp.org/img/n.png)

\[i51\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Utsav Prabhu](https://dblp.org/pid/54/10072.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

FALCON: Fairness Learning via Contrastive Attention Approach to Continual Semantic Scene Understanding in Open World. [CoRRabs/2311.15965](https://dblp.org/db/journals/corr/corr2311.html#journals/corr/abs-2311-15965) (2023)
- ![](https://dblp.org/img/n.png)

\[i50\]
[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Page Daniel Dobbs](https://dblp.org/pid/344/0595.html), Khoa Luu:

REACT: Recognize Every Action Everywhere All At Once. [CoRRabs/2312.00188](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-00188) (2023)
- ![](https://dblp.org/img/n.png)

\[i49\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Samee U. Khan](https://dblp.org/pid/k/SameeUllahKhan.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

Brainformer: Modeling MRI Brain Functions to Machine Vision. [CoRRabs/2312.00236](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-00236) (2023)
- ![](https://dblp.org/img/n.png)

\[i48\]
[Trong-Thuan Nguyen](https://dblp.org/pid/344/5384.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), Khoa Luu:

HIG: Hierarchical Interlacement Graph Approach to Scene Graph Generation in Video Understanding. [CoRRabs/2312.03050](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-03050) (2023)
- ![](https://dblp.org/img/n.png)

\[i47\]
[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu:

HAtt-Flow: Hierarchical Attention-Flow Mechanism for Group Activity Scene Graph Generation in Videos. [CoRRabs/2312.07740](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-07740) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j21\]
[Ibsa Jalata](https://dblp.org/pid/230/8158.html), [Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Pierce Helton](https://dblp.org/pid/328/9598.html), [Chase Rainwater](https://dblp.org/pid/57/6270.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

EQAdap: Equipollent Domain Adaptation Approach to Image Deblurring. [IEEE Access10](https://dblp.org/db/journals/access/access10.html#journals/access/JalataCTHRL22): 93203-93211 (2022)
- ![](https://dblp.org/img/n.png)

\[j20\]
[Yunjia Lei](https://dblp.org/pid/330/5177.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Son Lam Phung](https://dblp.org/pid/93/737.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Abdesselam Bouzerdoum](https://dblp.org/pid/00/5421.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hoang Thanh Le](https://dblp.org/pid/226/5364-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

Pedestrian Lane Detection for Assistive Navigation of Vision-Impaired People: Survey and Experimental Evaluation. [IEEE Access10](https://dblp.org/db/journals/access/access10.html#journals/access/LeiPBLL22): 101071-101089 (2022)
- ![](https://dblp.org/img/n.png)

\[j19\]
[Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Vidhiwar Singh Rathour](https://dblp.org/pid/286/5747.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kashu Yamazaki](https://dblp.org/pid/280/0133.html), Khoa Luu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Deep reinforcement learning in computer vision: a comprehensive survey. [Artif. Intell. Rev.55(4)](https://dblp.org/db/journals/air/air55.html#journals/air/LeRYLS22): 2733-2819 (2022)
- ![](https://dblp.org/img/n.png)

\[j18\]
[Minh-Hieu Phan](https://dblp.org/pid/268/1849.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Son Lam Phung](https://dblp.org/pid/93/737.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu, [Abdesselam Bouzerdoum](https://dblp.org/pid/00/5421.html):

Efficient hyperspectral image segmentation for biosecurity scanning using knowledge distillation from multi-head teacher. [Neurocomputing504](https://dblp.org/db/journals/ijon/ijon504.html#journals/ijon/PhanPLB22): 189-203 (2022)
- ![](https://dblp.org/img/n.png)

\[j17\]
[Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Ibsa Jalata](https://dblp.org/pid/230/8158.html), [Kaushik Roy](https://dblp.org/pid/r/KaushikRoy3.html), Khoa Luu:

Non-volume preserving-based fusion to group-level emotion recognition on crowd videos. [Pattern Recognit.128](https://dblp.org/db/journals/pr/pr128.html#journals/pr/QuachLDJRL22): 108646 (2022)
- ![](https://dblp.org/img/n.png)

\[c53\]
[Khoa Vo](https://dblp.org/pid/224/1953.html), [Kashu Yamazaki](https://dblp.org/pid/280/0133.html), [Phong X. Nguyen](https://dblp.org/pid/332/2436.html), [Phat Nguyen](https://dblp.org/pid/225/8229.html), Khoa Luu, [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Contextual Explainable Video Representation: Human Perception-based Understanding. [IEEECONF2022](https://dblp.org/db/conf/acssc/acssc2022.html#conf/acssc/VoYNNLL22): 1326-1333
- ![](https://dblp.org/img/n.png)

\[c52\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Ngan Le](https://dblp.org/pid/37/245.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), Khoa Luu:

Multi-Camera Multiple 3D Object Tracking on the Move for Autonomous Vehicles. [CVPR Workshops2022](https://dblp.org/db/conf/cvpr/cvpr2022w.html#conf/cvpr/NguyenQDLNL22): 2568-2577
- ![](https://dblp.org/img/n.png)

\[c51\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Quoc-Huy Bui](https://dblp.org/pid/317/0417.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Han-Seok Seo](https://dblp.org/pid/138/6741.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Son Lam Phung](https://dblp.org/pid/93/737.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

DirecFormer: A Directed Attention in Transformer Approach to Robust Action Recognition. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/TruongBDSPLL22): 19998-20008
- ![](https://dblp.org/img/n.png)

\[c50\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Miaoqing Huang](https://dblp.org/pid/45/5897.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Liang](https://dblp.org/pid/23/6696.html), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

Self-Supervised Domain Adaptation in Crowd Counting. [ICIP2022](https://dblp.org/db/conf/icip/icip2022.html#conf/icip/NguyenTHLLL22): 2786-2790
- ![](https://dblp.org/img/n.png)

\[c49\]
[Kashu Yamazaki](https://dblp.org/pid/280/0133.html), [Sang Truong](https://dblp.org/pid/301/9134.html), [Viet-Khoa Vo-Ho](https://dblp.org/pid/224/1953.html), [Michael Kidd](https://dblp.org/pid/200/4886.html), [Chase Rainwater](https://dblp.org/pid/57/6270.html), Khoa Luu, [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png):

VLCAP: Vision-Language with Contrastive Learning for Coherent Video Paragraph Captioning. [ICIP2022](https://dblp.org/db/conf/icip/icip2022.html#conf/icip/YamazakiTVKRLL22): 3656-3661
- ![](https://dblp.org/img/n.png)

\[c48\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Ravi Teja N. V. S. Chappa](https://dblp.org/pid/321/0642.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ashley P. G. Dowling](https://dblp.org/pid/321/0870.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

OTAdapt: Optimal Transport-based Approach For Unsupervised Domain Adaptation. [ICPR2022](https://dblp.org/db/conf/icpr/icpr2022.html#conf/icpr/TruongCNLDL22): 2850-2856
- ![](https://dblp.org/img/n.png)

\[i46\]
[Minh Q. Tran](https://dblp.org/pid/281/8723.html), [Viet-Khoa Vo-Ho](https://dblp.org/pid/224/1953.html), [Kyle Quinn](https://dblp.org/pid/317/2546.html), [Hien Nguyen](https://dblp.org/pid/26/1622.html), Khoa Luu, [Ngan Le](https://dblp.org/pid/37/245.html):

CapsNet for Medical Image Segmentation. [CoRRabs/2203.08948](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-08948) (2022)
- ![](https://dblp.org/img/n.png)

\[i45\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Quoc-Huy Bui](https://dblp.org/pid/317/0417.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Han-Seok Seo](https://dblp.org/pid/138/6741.html), [Son Lam Phung](https://dblp.org/pid/93/737.html), [Xin Li](https://dblp.org/pid/09/1365-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

DirecFormer: A Directed Attention in Transformer Approach to Robust Action Recognition. [CoRRabs/2203.10233](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-10233) (2022)
- ![](https://dblp.org/img/n.png)

\[i44\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Ngan Le](https://dblp.org/pid/37/245.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), Khoa Luu:

Multi-Camera Multiple 3D Object Tracking on the Move for Autonomous Vehicles. [CoRRabs/2204.09151](https://dblp.org/db/journals/corr/corr2204.html#journals/corr/abs-2204-09151) (2022)
- ![](https://dblp.org/img/n.png)

\[i43\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html), [Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Ngan Le](https://dblp.org/pid/37/245.html), [Ashley Dowling](https://dblp.org/pid/321/0870.html), Khoa Luu:

OTAdapt: Optimal Transport-based Approach For Unsupervised Domain Adaptation. [CoRRabs/2205.10738](https://dblp.org/db/journals/corr/corr2205.html#journals/corr/abs-2205-10738) (2022)
- ![](https://dblp.org/img/n.png)

\[i42\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Apoorva Bisht](https://dblp.org/pid/321/4247.html), [Hugh Churchill](https://dblp.org/pid/241/9507.html), Khoa Luu:

Two-Dimensional Quantum Material Identification via Self-Attention and Soft-labeling in Deep Learning. [CoRRabs/2205.15948](https://dblp.org/db/journals/corr/corr2205.html#journals/corr/abs-2205-15948) (2022)
- ![](https://dblp.org/img/n.png)

\[i41\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Miaoqing Huang](https://dblp.org/pid/45/5897.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Liang](https://dblp.org/pid/23/6696.html), [Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu:

Self-supervised Domain Adaptation in Crowd Counting. [CoRRabs/2206.03431](https://dblp.org/db/journals/corr/corr2206.html#journals/corr/abs-2206-03431) (2022)
- ![](https://dblp.org/img/n.png)

\[i40\]
[Kashu Yamazaki](https://dblp.org/pid/280/0133.html), [Sang Truong](https://dblp.org/pid/301/9134.html), [Khoa Vo](https://dblp.org/pid/224/1953.html), [Michael Kidd](https://dblp.org/pid/200/4886.html), [Chase Rainwater](https://dblp.org/pid/57/6270.html), Khoa Luu, [Ngan Le](https://dblp.org/pid/37/245.html):

VLCap: Vision-Language with Contrastive Learning for Coherent Video Paragraph Captioning. [CoRRabs/2206.12972](https://dblp.org/db/journals/corr/corr2206.html#journals/corr/abs-2206-12972) (2022)
- ![](https://dblp.org/img/n.png)

\[i39\]
[Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Huu Le](https://dblp.org/pid/191/4630.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Tien Dai Bui](https://dblp.org/pid/b/TienDBui.html), Khoa Luu:

Depth Perspective-aware Multiple Object Tracking. [CoRRabs/2207.04551](https://dblp.org/db/journals/corr/corr2207.html#journals/corr/abs-2207-04551) (2022)
- ![](https://dblp.org/img/n.png)

\[i38\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Ngan Le](https://dblp.org/pid/37/245.html), [Marios Savvides](https://dblp.org/pid/13/3793.html), Khoa Luu:

Vec2Face-v2: Unveil Human Faces from their Blackbox Features via Attention-based Network in Face Recognition. [CoRRabs/2209.04920](https://dblp.org/db/journals/corr/corr2209.html#journals/corr/abs-2209-04920) (2022)
- ![](https://dblp.org/img/n.png)

\[i37\]
[Pha A. Nguyen](https://dblp.org/pid/270/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Son Lam Phung](https://dblp.org/pid/93/737.html), [Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu:

Multi-Camera Multi-Object Tracking on the Move via Single-Stage Global Association Approach. [CoRRabs/2211.09663](https://dblp.org/db/journals/corr/corr2211.html#journals/corr/abs-2211-09663) (2022)
- ![](https://dblp.org/img/n.png)

\[i36\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Pierce Helton](https://dblp.org/pid/328/9598.html), [Ahmed Moustafa](https://dblp.org/pid/117/1672.html), [Jackson David Cothren](https://dblp.org/pid/335/1787.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

CONDA: Continual Unsupervised Domain Adaptation Learning in Visual Perception for Self-Driving Cars. [CoRRabs/2212.00621](https://dblp.org/db/journals/corr/corr2212.html#journals/corr/abs-2212-00621) (2022)
- ![](https://dblp.org/img/n.png)

\[i35\]
[Manuel Serna-Aguilera](https://dblp.org/pid/336/4123.html), Khoa Luu, [Nathaniel Harris](https://dblp.org/pid/336/2673.html), [Min Zou](https://dblp.org/pid/97/2960.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Neural Cell Video Synthesis via Optical-Flow Diffusion. [CoRRabs/2212.03250](https://dblp.org/db/journals/corr/corr2212.html#journals/corr/abs-2212-03250) (2022)
- ![](https://dblp.org/img/n.png)

\[i34\]
[Khoa Vo](https://dblp.org/pid/224/1953.html), [Kashu Yamazaki](https://dblp.org/pid/280/0133.html), [Phong X. Nguyen](https://dblp.org/pid/332/2436.html), [Phat Nguyen](https://dblp.org/pid/225/8229.html), Khoa Luu, [Ngan Le](https://dblp.org/pid/37/245.html):

Contextual Explainable Video Representation: Human Perception-based Understanding. [CoRRabs/2212.06206](https://dblp.org/db/journals/corr/corr2212.html#journals/corr/abs-2212-06206) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[j16\]
[Xiang Li](https://dblp.org/pid/40/1491-92.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianzheng Liu](https://dblp.org/pid/169/7220.html), [Jessica R. Baron](https://dblp.org/pid/216/5214.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Eric K. Patterson](https://dblp.org/pid/93/9217.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Evaluating effects of focal length and viewing angle in a comparison of recent face landmark and alignment methods. [EURASIP J. Image Video Process.2021(1)](https://dblp.org/db/journals/ejivp/ejivp2021.html#journals/ejivp/LiLBLP21): 9 (2021)
- ![](https://dblp.org/img/n.png)

\[j15\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Minh-Triet Tran](https://dblp.org/pid/44/7448.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu:

Fast Flow Reconstruction via Robust Invertible n × n Convolution. [Future Internet13(7)](https://dblp.org/db/journals/fi/fi13.html#journals/fi/TruongDTLL21): 179 (2021)
- ![](https://dblp.org/img/n.png)

\[j14\]
[Ibsa Jalata](https://dblp.org/pid/230/8158.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Jessica L. Allen](https://dblp.org/pid/158/2631.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Han-Seok Seo](https://dblp.org/pid/138/6741.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

Movement Analysis for Neurological and Musculoskeletal Disorders Using Graph Convolutional Neural Network. [Future Internet13(8)](https://dblp.org/db/journals/fi/fi13.html#journals/fi/JalataTASL21): 194 (2021)
- ![](https://dblp.org/img/n.png)

\[j13\]
[S. Kevin Zhou](https://dblp.org/pid/57/98.html)![](https://dblp.org/img/orcid-mark.12x12.png), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu, [Hien Van Nguyen](https://dblp.org/pid/59/9550.html), [Nicholas Ayache](https://dblp.org/pid/a/NicholasAyache.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Deep reinforcement learning in medical imaging: A literature review. [Medical Image Anal.73](https://dblp.org/db/journals/mia/mia73.html#journals/mia/ZhouLLNA21): 102193 (2021)
- ![](https://dblp.org/img/n.png)

\[c47\]
[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html), [Duc Toan Bui](https://dblp.org/pid/253/0379-2.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), Khoa Luu:

Clusformer: A Transformer Based Clustering Approach to Unsupervised Large-Scale Face and Visual Landmark Recognition. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/NguyenBDBL21): 10847-10856
- ![](https://dblp.org/img/n.png)

\[c46\]
[Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Huu Le](https://dblp.org/pid/191/4630.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Minh-Triet Tran](https://dblp.org/pid/44/7448.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

DyGLIP: A Dynamic Graph Model With Link Prediction for Accurate Multi-Camera Multiple Object Tracking. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/QuachNLTDTL21): 13784-13793
- ![](https://dblp.org/img/n.png)

\[c45\]
[Chuong Huynh](https://dblp.org/pid/289/7090.html), [Anh Tuan Tran](https://dblp.org/pid/150/5269-1.html), Khoa Luu, [Minh Hoai](https://dblp.org/pid/135/4935.html):

Progressive Semantic Segmentation. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/HuynhTLH21): 16755-16764
- ![](https://dblp.org/img/n.png)

\[c44\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [The De Vu](https://dblp.org/pid/192/3667.html), [Hoang Anh Pham](https://dblp.org/pid/54/7957.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu:

The Right to Talk: An Audio-Visual Transformer Approach. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/TruongDVPRLL21): 1085-1094
- ![](https://dblp.org/img/n.png)

\[c43\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Son Lam Phung](https://dblp.org/pid/93/737.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chase Rainwater](https://dblp.org/pid/57/6270.html), Khoa Luu:

BiMaL: Bijective Maximum Likelihood Approach to Domain Adaptation in Semantic Scene Segmentation. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/TruongDLPRL21): 8528-8537
- ![](https://dblp.org/img/n.png)

\[c42\]
[Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [James Sorensen](https://dblp.org/pid/312/7241.html), [Toan Duc Bui](https://dblp.org/pid/143/9351.html), [Arabinda Choudhary](https://dblp.org/pid/312/7044.html), Khoa Luu, [Hien Van Nguyen](https://dblp.org/pid/59/9550.html):

PairFlow: Enhancing Portable Chest X-Ray By Flow-Based Deformation For Covid-19 Diagnosing. [ICIP2021](https://dblp.org/db/conf/icip/icip2021.html#conf/icip/LeSBCLN21): 215-219
- ![](https://dblp.org/img/n.png)

\[i33\]
[S. Kevin Zhou](https://dblp.org/pid/57/98.html), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Hien Van Nguyen](https://dblp.org/pid/59/9550.html), [Nicholas Ayache](https://dblp.org/pid/a/NicholasAyache.html):

Deep reinforcement learning in medical imaging: A literature review. [CoRRabs/2103.05115](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-05115) (2021)
- ![](https://dblp.org/img/n.png)

\[i32\]
[Chuong Huynh](https://dblp.org/pid/289/7090.html), [Anh Tran](https://dblp.org/pid/150/5269-1.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Minh Hoai](https://dblp.org/pid/135/4935.html):

Progressive Semantic Segmentation. [CoRRabs/2104.03778](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-03778) (2021)
- ![](https://dblp.org/img/n.png)

\[i31\]
[Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Pha A. Nguyen](https://dblp.org/pid/270/6213.html), [Huu Le](https://dblp.org/pid/191/4630.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Minh-Triet Tran](https://dblp.org/pid/44/7448.html), Khoa Luu:

DyGLIP: A Dynamic Graph Model with Link Prediction for Accurate Multi-Camera Multiple Object Tracking. [CoRRabs/2106.06856](https://dblp.org/db/journals/corr/corr2106.html#journals/corr/abs-2106-06856) (2021)
- ![](https://dblp.org/img/n.png)

\[i30\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [The De Vu](https://dblp.org/pid/192/3667.html), [Hoang Anh Pham](https://dblp.org/pid/54/7957.html), [Bhiksha Raj](https://dblp.org/pid/60/3996.html), [Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu:

The Right to Talk: An Audio-Visual Transformer Approach. [CoRRabs/2108.03256](https://dblp.org/db/journals/corr/corr2108.html#journals/corr/abs-2108-03256) (2021)
- ![](https://dblp.org/img/n.png)

\[i29\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Ngan Le](https://dblp.org/pid/37/245.html), [Son Lam Phung](https://dblp.org/pid/93/737.html), [Chase Rainwater](https://dblp.org/pid/57/6270.html), Khoa Luu:

BiMaL: Bijective Maximum Likelihood Approach to Domain Adaptation in Semantic Scene Segmentation. [CoRRabs/2108.03267](https://dblp.org/db/journals/corr/corr2108.html#journals/corr/abs-2108-03267) (2021)
- ![](https://dblp.org/img/n.png)

\[i28\]
[Ngan Le](https://dblp.org/pid/37/245.html), [Vidhiwar Singh Rathour](https://dblp.org/pid/286/5747.html), [Kashu Yamazaki](https://dblp.org/pid/280/0133.html), Khoa Luu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Deep Reinforcement Learning in Computer Vision: A Comprehensive Survey. [CoRRabs/2108.11510](https://dblp.org/db/journals/corr/corr2108.html#journals/corr/abs-2108-11510) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[j12\]
[David M. Ford](https://dblp.org/pid/116/9240.html), [Aditya Dendukuri](https://dblp.org/pid/232/3153.html), [Gülce Kalyoncu](https://dblp.org/pid/273/7438.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Matthew J. Patitz](https://dblp.org/pid/31/4769.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Machine learning to identify variables in thermodynamically small systems. [Comput. Chem. Eng.141](https://dblp.org/db/journals/cce/cce141.html#journals/cce/FordDKLP20): 106989 (2020)
- ![](https://dblp.org/img/n.png)

\[c41\]
[Sonya J. Burroughs](https://dblp.org/pid/292/5602.html), [Balakrishna Gokaraju](https://dblp.org/pid/61/8963.html), [Kaushik Roy](https://dblp.org/pid/r/KaushikRoy3.html), Khoa Luu:

DeepFakes Detection in Videos using Feature Engineering Techniques in Deep Learning Convolution Neural Network Frameworks. [AIPR2020](https://dblp.org/db/conf/aipr/aipr2020.html#conf/aipr/BurroughsGRL20): 1-4
- ![](https://dblp.org/img/n.png)

\[c40\]
[Dat T. Truong](https://dblp.org/pid/268/3805.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Minh-Triet Tran](https://dblp.org/pid/44/7448.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Domain Generalization via Universal Non-volume Preserving Approach. [CRV2020](https://dblp.org/db/conf/crv/crv2020.html#conf/crv/TruongDLTL20): 93-100
- ![](https://dblp.org/img/n.png)

\[c39\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Hung Bui](https://dblp.org/pid/59/10562.html), [Kaushik Roy](https://dblp.org/pid/r/KaushikRoy3.html):

Vec2Face: Unveil Human Faces From Their Blackbox Features in Face Recognition. [CVPR2020](https://dblp.org/db/conf/cvpr/cvpr2020.html#conf/cvpr/DuongTLQBR20): 6131-6140
- ![](https://dblp.org/img/n.png)

\[c38\]
[Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), [Kashu Yamazaki](https://dblp.org/pid/280/0133.html), [Toan Duc Bui](https://dblp.org/pid/143/9351.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Offset Curves Loss for Imbalanced Problem in Medical Segmentation. [ICPR2020](https://dblp.org/db/conf/icpr/icpr2020.html#conf/icpr/LeLYBLS20): 6189-6195
- ![](https://dblp.org/img/n.png)

\[c37\]
[Jaime S. Cardoso](https://dblp.org/pid/65/5236.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hien Van Nguyen](https://dblp.org/pid/59/9550.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Nicholas Heller](https://dblp.org/pid/205/5397.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pedro Henriques Abreu](https://dblp.org/pid/66/6482.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ivana Isgum](https://dblp.org/pid/62/5757.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wilson Silva](https://dblp.org/pid/228/1570.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ricardo P. M. Cruz](https://dblp.org/pid/362/3525.html)![](https://dblp.org/img/orcid-mark.12x12.png), [José Pereira Amorim](https://dblp.org/pid/275/9315.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Vishal Patel](https://dblp.org/pid/86/4726-1.html), [Badri Roysam](https://dblp.org/pid/r/BRoysam.html), [S. Kevin Zhou](https://dblp.org/pid/57/98.html), [Steve B. Jiang](https://dblp.org/pid/73/2968.html), [Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu, [Raphael Sznitman](https://dblp.org/pid/29/8000.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Veronika Cheplygina](https://dblp.org/pid/91/10084.html), [Diana Mateus](https://dblp.org/pid/55/6754.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Emanuele Trucco](https://dblp.org/pid/60/1409.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Samaneh Abbasi-Sureshjani](https://dblp.org/pid/164/7548.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Correction to: Interpretable and Annotation-Efficient Learning for Medical Image Computing. [iMIMIC/MIL3ID/LABELS@MICCAI2020](https://dblp.org/db/conf/miccai/imimic2020.html#conf/miccai/CardosoNHAISCAP20): 1
- ![](https://dblp.org/img/n.png)

\[c36\]
[Toan Duc Bui](https://dblp.org/pid/143/9351.html), [Manh Nguyen](https://dblp.org/pid/242/6386-2.html), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

Flow-Based Deformation Guidance for Unpaired Multi-contrast MRI Image-to-Image Translation. [MICCAI (2)2020](https://dblp.org/db/conf/miccai/miccai2020-2.html#conf/miccai/BuiNLL20): 728-737
- ![](https://dblp.org/img/n.png)

\[e2\]
[Jaime S. Cardoso](https://dblp.org/pid/65/5236.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hien Van Nguyen](https://dblp.org/pid/59/9550.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Nicholas Heller](https://dblp.org/pid/205/5397.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pedro Henriques Abreu](https://dblp.org/pid/66/6482.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ivana Isgum](https://dblp.org/pid/62/5757.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wilson Silva](https://dblp.org/pid/228/1570.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ricardo P. M. Cruz](https://dblp.org/pid/362/3525.html)![](https://dblp.org/img/orcid-mark.12x12.png), [José Pereira Amorim](https://dblp.org/pid/275/9315.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Vishal Patel](https://dblp.org/pid/86/4726-1.html), [Badri Roysam](https://dblp.org/pid/r/BRoysam.html), [S. Kevin Zhou](https://dblp.org/pid/57/98.html), [Steve B. Jiang](https://dblp.org/pid/73/2968.html), [Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Raphael Sznitman](https://dblp.org/pid/29/8000.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Veronika Cheplygina](https://dblp.org/pid/91/10084.html), [Diana Mateus](https://dblp.org/pid/55/6754.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Emanuele Trucco](https://dblp.org/pid/60/1409.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Samaneh Abbasi-Sureshjani](https://dblp.org/pid/164/7548.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Interpretable and Annotation-Efficient Learning for Medical Image Computing - Third International Workshop, iMIMIC 2020, Second International Workshop, MIL3ID 2020, and 5th International Workshop, LABELS 2020, Held in Conjunction with MICCAI 2020, Lima, Peru, October 4-8, 2020, Proceedings. [Lecture Notes in Computer Science](https://dblp.org/db/series/lncs/index.html) 12446, Springer2020, ISBN 978-3-030-61165-1 [\[contents\]](https://dblp.org/db/conf/miccai/imimic2020.html)
- ![](https://dblp.org/img/n.png)

\[i27\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hung Bui](https://dblp.org/pid/59/10562.html), [Kaushik Roy](https://dblp.org/pid/r/KaushikRoy3.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

Vec2Face: Unveil Human Faces from their Blackbox Features in Face Recognition. [CoRRabs/2003.06958](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-06958) (2020)
- ![](https://dblp.org/img/n.png)

\[i26\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), Khoa Luu:

LIAAD: Lightweight Attentive Angular Distillation for Large-scale Age-Invariant Face Recognition. [CoRRabs/2004.05085](https://dblp.org/db/journals/corr/corr2004.html#journals/corr/abs-2004-05085) (2020)
- ![](https://dblp.org/img/n.png)

\[i25\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), Khoa Luu:

LIAAD: Lightweight Attentive Angular Distillation for Large-scale Age-Invariant Face Recognition. [CoRRabs/2004.05085](https://dblp.org/db/journals/corr/corr2004.html#journals/corr/abs-2004-05085) (2020)
- ![](https://dblp.org/img/n.png)

\[i24\]
[Toan Duc Bui](https://dblp.org/pid/143/9351.html), [Manh Nguyen](https://dblp.org/pid/242/6386-2.html), [Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu:

Flow-based Deformation Guidance for Unpaired Multi-Contrast MRI Image-to-Image Translation. [CoRRabs/2012.01777](https://dblp.org/db/journals/corr/corr2012.html#journals/corr/abs-2012-01777) (2020)
- ![](https://dblp.org/img/n.png)

\[i23\]
[Ngan Le](https://dblp.org/pid/37/245.html), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), [Kashu Yamazaki](https://dblp.org/pid/280/0133.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Toan Duc Bui](https://dblp.org/pid/143/9351.html), Khoa Luu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Offset Curves Loss for Imbalanced Problem in Medical Segmentation. [CoRRabs/2012.02463](https://dblp.org/db/journals/corr/corr2012.html#journals/corr/abs-2012-02463) (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j11\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html):

Deep Appearance Models: A Deep Boltzmann Machine Approach for Face Modeling. [Int. J. Comput. Vis.127(5)](https://dblp.org/db/journals/ijcv/ijcv127.html#journals/ijcv/DuongLQB19): 437-455 (2019)
- ![](https://dblp.org/img/n.png)

\[j10\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), [Marios Savvides](https://dblp.org/pid/13/3793.html), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html):

Learning from Longitudinal Face Demonstration - Where Tractable Deep Modeling Meets Inverse Reinforcement Learning. [Int. J. Comput. Vis.127(6-7)](https://dblp.org/db/journals/ijcv/ijcv127.html#journals/ijcv/DuongQLLSB19): 957-971 (2019)
- ![](https://dblp.org/img/n.png)

\[c35\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Ibsa Jalata](https://dblp.org/pid/230/8158.html), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

MobiFace: A Lightweight Deep Learning Face Recognition on Mobile Devices. [BTAS2019](https://dblp.org/db/conf/btas/btas2019.html#conf/btas/DuongQJLL19): 1-6
- ![](https://dblp.org/img/n.png)

\[c34\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Nghia Nguyen](https://dblp.org/pid/230/7933.html), [Eric Patterson](https://dblp.org/pid/79/1282.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), [Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Automatic Face Aging in Videos via Deep Reinforcement Learning. [CVPR2019](https://dblp.org/db/conf/cvpr/cvpr2019.html#conf/cvpr/DuongLQNPBL19): 10013-10022
- ![](https://dblp.org/img/n.png)

\[e1\]
[Qian Wang](https://dblp.org/pid/75/5723-1.html), [Fausto Milletari](https://dblp.org/pid/134/9886.html), [Hien Van Nguyen](https://dblp.org/pid/59/9550.html), [Shadi Albarqouni](https://dblp.org/pid/165/7751.html)![](https://dblp.org/img/orcid-mark.12x12.png), [M. Jorge Cardoso](https://dblp.org/pid/17/7426.html), [Nicola Rieke](https://dblp.org/pid/149/7726.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ziyue Xu](https://dblp.org/pid/59/9160-1.html), [Konstantinos Kamnitsas](https://dblp.org/pid/177/9280.html), [Vishal Patel](https://dblp.org/pid/86/4726-1.html), [Badri Roysam](https://dblp.org/pid/r/BRoysam.html), [Steve B. Jiang](https://dblp.org/pid/73/2968.html), [S. Kevin Zhou](https://dblp.org/pid/57/98.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Ngan Le](https://dblp.org/pid/37/245.html):

Domain Adaptation and Representation Transfer and Medical Image Learning with Less Labels and Imperfect Data - First MICCAI Workshop, DART 2019, and First International Workshop, MIL3ID 2019, Shenzhen, Held in Conjunction with MICCAI 2019, Shenzhen, China, October 13 and 17, 2019, Proceedings. [Lecture Notes in Computer Science](https://dblp.org/db/series/lncs/index.html) 11795, Springer2019, ISBN 978-3-030-33390-4 [\[contents\]](https://dblp.org/db/conf/miccai/dart2019.html)
- ![](https://dblp.org/img/n.png)

\[i22\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Ngan Le](https://dblp.org/pid/37/245.html), [Minh-Triet Tran](https://dblp.org/pid/44/7448.html):

Generative Flow via Invertible nxn Convolution. [CoRRabs/1905.10170](https://dblp.org/db/journals/corr/corr1905.html#journals/corr/abs-1905-10170) (2019)
- ![](https://dblp.org/img/n.png)

\[i21\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Ngan Le](https://dblp.org/pid/37/245.html):

ShrinkTeaNet: Million-scale Lightweight Face Recognition via Shrinking Teacher-Student Networks. [CoRRabs/1905.10620](https://dblp.org/db/journals/corr/corr1905.html#journals/corr/abs-1905-10620) (2019)
- ![](https://dblp.org/img/n.png)

\[i20\]
[Aditya Dendukuri](https://dblp.org/pid/232/3153.html), [Blake Keeling](https://dblp.org/pid/241/9366.html), [Arash Fereidouni](https://dblp.org/pid/241/9731.html), [Joshua Burbridge](https://dblp.org/pid/241/9738.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Hugh Churchill](https://dblp.org/pid/241/9507.html):

Defining Quantum Neural Networks via Quantum Time Evolution. [CoRRabs/1905.10912](https://dblp.org/db/journals/corr/corr1905.html#journals/corr/abs-1905-10912) (2019)
- ![](https://dblp.org/img/n.png)

\[i19\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Ngan Le](https://dblp.org/pid/37/245.html), [Minh-Triet Tran](https://dblp.org/pid/44/7448.html):

Image Alignment in Unseen Domains via Domain Deep Generalization. [CoRRabs/1905.12028](https://dblp.org/db/journals/corr/corr1905.html#journals/corr/abs-1905-12028) (2019)
- ![](https://dblp.org/img/n.png)

\[i18\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), Khoa Luu, [Minh-Triet Tran](https://dblp.org/pid/44/7448.html):

Recognition in Unseen Domains: Domain Generalization via Universal Non-volume Preserving Models. [CoRRabs/1905.13040](https://dblp.org/db/journals/corr/corr1905.html#journals/corr/abs-1905-13040) (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[j9\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ligong Han](https://dblp.org/pid/187/1675.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Deep contextual recurrent residual networks for scene labeling. [Pattern Recognit.80](https://dblp.org/db/journals/pr/pr80.html#journals/pr/LeDHLQS18): 32-41 (2018)
- ![](https://dblp.org/img/n.png)

\[j8\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Reformulating Level Sets as Deep Recurrent Neural Network Approach to Semantic Segmentation. [IEEE Trans. Image Process.27(5)](https://dblp.org/db/journals/tip/tip27.html#journals/tip/LeQLDS18): 2393-2407 (2018)
- ![](https://dblp.org/img/n.png)

\[c33\]
[Chenchen Zhu](https://dblp.org/pid/50/6994.html), [Ran Tao](https://dblp.org/pid/99/955-13.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Seeing Small Faces From Robust Anchor's Perspective. [CVPR2018](https://dblp.org/db/conf/cvpr/cvpr2018.html#conf/cvpr/ZhuTLS18): 5127-5136
- ![](https://dblp.org/img/n.png)

\[c32\]
[Chenchen Zhu](https://dblp.org/pid/50/6994.html), [Yutong Zheng](https://dblp.org/pid/164/0869.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Enhancing Interior and Exterior Deep Facial Features for Face Detection in the Wild. [FG2018](https://dblp.org/db/conf/fgr/fg2018.html#conf/fgr/ZhuZLS18): 226-233
- ![](https://dblp.org/img/n.png)

\[c31\]
[Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

Lp Norm Relaxation Approach for Large Scale Data Analysis: A Review. [ICIAR2018](https://dblp.org/db/conf/iciar/iciar2018.html#conf/iciar/BuiQDL18): 285-292
- ![](https://dblp.org/img/n.png)

\[i17\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html):

Longitudinal Face Aging in the Wild - Recent Deep Learning Approaches. [CoRRabs/1802.08726](https://dblp.org/db/journals/corr/corr1802.html#journals/corr/abs-1802-08726) (2018)
- ![](https://dblp.org/img/n.png)

\[i16\]
[Chenchen Zhu](https://dblp.org/pid/50/6994.html), [Ran Tao](https://dblp.org/pid/99/955-13.html), Khoa Luu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Seeing Small Faces from Robust Anchor's Perspective. [CoRRabs/1802.09058](https://dblp.org/db/journals/corr/corr1802.html#journals/corr/abs-1802-09058) (2018)
- ![](https://dblp.org/img/n.png)

\[i15\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ngan Le](https://dblp.org/pid/37/245.html), [Nghia Nguyen](https://dblp.org/pid/230/7933.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

MobiFace: A Lightweight Deep Learning Face Recognition on Mobile Devices. [CoRRabs/1811.11080](https://dblp.org/db/journals/corr/corr1811.html#journals/corr/abs-1811-11080) (2018)
- ![](https://dblp.org/img/n.png)

\[i14\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), Khoa Luu, [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Nghia Nguyen](https://dblp.org/pid/230/7933.html), [Eric Patterson](https://dblp.org/pid/79/1282.html), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), [Ngan Le](https://dblp.org/pid/37/245.html):

Automatic Face Aging in Videos via Deep Reinforcement Learning. [CoRRabs/1811.11082](https://dblp.org/db/journals/corr/corr1811.html#journals/corr/abs-1811-11082) (2018)
- ![](https://dblp.org/img/n.png)

\[i13\]
[Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Ngan Le](https://dblp.org/pid/37/245.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Ibsa Jalata](https://dblp.org/pid/230/8158.html), [Karl Ricanek](https://dblp.org/pid/39/609.html):

Non-Volume Preserving-based Feature Fusion Approach to Group-Level Expression Recognition on Crowd Videos. [CoRRabs/1811.11849](https://dblp.org/db/journals/corr/corr1811.html#journals/corr/abs-1811-11849) (2018)
- ![](https://dblp.org/img/n.png)

\[i12\]
[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Minh-Triet Tran](https://dblp.org/pid/44/7448.html), [Minh N. Do](https://dblp.org/pid/d/MinhNDo.html):

Beyond Domain Adaptation: Unseen Domain Encapsulation via Universal Non-volume Preserving Models. [CoRRabs/1812.03407](https://dblp.org/db/journals/corr/corr1812.html#journals/corr/abs-1812-03407) (2018)
- ![](https://dblp.org/img/n.png)

\[i11\]
[Aditya Dendukuri](https://dblp.org/pid/232/3153.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

Image Processing in Quantum Computers. [CoRRabs/1812.11042](https://dblp.org/db/journals/corr/corr1812.html#journals/corr/abs-1812-11042) (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[j7\]
[Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html):

Non-convex online robust PCA: Enhance sparsity via ℓp-norm minimization. [Comput. Vis. Image Underst.158](https://dblp.org/db/journals/cviu/cviu158.html#journals/cviu/QuachDLB17): 126-140 (2017)
- ![](https://dblp.org/img/n.png)

\[j6\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Chenchen Zhu](https://dblp.org/pid/50/6994.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Semi self-training beard/moustache detection and segmentation simultaneously. [Image Vis. Comput.58](https://dblp.org/db/journals/ivc/ivc58.html#journals/ivc/LeLZS17): 214-223 (2017)
- ![](https://dblp.org/img/n.png)

\[j5\]
Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), [Ching Y. Suen](https://dblp.org/pid/s/ChingYSuen.html):

Compressed Submanifold Multifactor Analysis. [IEEE Trans. Pattern Anal. Mach. Intell.39(3)](https://dblp.org/db/journals/pami/pami39.html#journals/pami/LuuSBS17): 444-456 (2017)
- ![](https://dblp.org/img/n.png)

\[j4\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), [Chenchen Zhu](https://dblp.org/pid/50/6994.html), [Yutong Zheng](https://dblp.org/pid/164/0869.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

DeepSafeDrive: A grammar-aware driver parsing approach to Driver Behavioral Situational Awareness (DB-SAW). [Pattern Recognit.66](https://dblp.org/db/journals/pr/pr66.html#journals/pr/LeZZLS17): 229-238 (2017)
- ![](https://dblp.org/img/n.png)

\[c30\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Chenchen Zhu](https://dblp.org/pid/50/6994.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Robust Hand Detection and Classification in Vehicles and in the Wild. [CVPR Workshops2017](https://dblp.org/db/conf/cvpr/cvprw2017.html#conf/cvpr/LeQZDLS17): 1203-1210
- ![](https://dblp.org/img/n.png)

\[c29\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Temporal Non-volume Preserving Approach to Facial Age-Progression and Age-Invariant Face Recognition. [ICCV2017](https://dblp.org/db/conf/iccv/iccv2017.html#conf/iccv/DuongQLLS17): 3755-3763
- ![](https://dblp.org/img/n.png)

\[c28\]
[Chandrasekhar Bhagavatula](https://dblp.org/pid/126/4520.html), [Chenchen Zhu](https://dblp.org/pid/50/6994.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Faster than Real-Time Facial Alignment: A 3D Spatial Transformer Network Approach in Unconstrained Poses. [ICCV2017](https://dblp.org/db/conf/iccv/iccv2017.html#conf/iccv/BhagavatulaZLS17): 4000-4009
- ![](https://dblp.org/img/n.png)

\[i10\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu, [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Temporal Non-Volume Preserving Approach to Facial Age-Progression and Age-Invariant Face Recognition. [CoRRabs/1703.08617](https://dblp.org/db/journals/corr/corr1703.html#journals/corr/DuongQLLS17) (2017)
- ![](https://dblp.org/img/n.png)

\[i9\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), Khoa Luu, [Marios Savvides](https://dblp.org/pid/13/3793.html), [Chenchen Zhu](https://dblp.org/pid/50/6994.html):

Reformulating Level Sets as Deep Recurrent Neural Network Approach to Semantic Segmentation. [CoRRabs/1704.03593](https://dblp.org/db/journals/corr/corr1704.html#journals/corr/LeQLSZ17) (2017)
- ![](https://dblp.org/img/n.png)

\[i8\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Ligong Han](https://dblp.org/pid/187/1675.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html), [Dipan K. Pal](https://dblp.org/pid/148/1005.html):

Deep Contextual Recurrent Residual Networks for Scene Labeling. [CoRRabs/1704.03594](https://dblp.org/db/journals/corr/corr1704.html#journals/corr/LeDHLSP17) (2017)
- ![](https://dblp.org/img/n.png)

\[i7\]
[Chandrasekhar Bhagavatula](https://dblp.org/pid/126/4520.html), [Chenchen Zhu](https://dblp.org/pid/50/6994.html), Khoa Luu, [Marios Savvides](https://dblp.org/pid/13/3793.html):

Faster Than Real-time Facial Alignment: A 3D Spatial Transformer Network Approach in Unconstrained Poses. [CoRRabs/1707.05653](https://dblp.org/db/journals/corr/corr1707.html#journals/corr/BhagavatulaZLS17) (2017)
- ![](https://dblp.org/img/n.png)

\[i6\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu, [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Learning from Longitudinal Face Demonstration - Where Tractable Deep Modeling Meets Inverse Reinforcement Learning. [CoRRabs/1711.10520](https://dblp.org/db/journals/corr/corr1711.html#journals/corr/abs-1711-10520) (2017)
- 2016
- ![](https://dblp.org/img/n.png)

\[c27\]
[Yutong Zheng](https://dblp.org/pid/164/0869.html), [Chenchen Zhu](https://dblp.org/pid/50/6994.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Chandrasekhar Bhagavatula](https://dblp.org/pid/126/4520.html), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Towards a deep learning framework for unconstrained face detection. [BTAS2016](https://dblp.org/db/conf/btas/btas2016.html#conf/btas/ZhengZLBLS16): 1-8
- ![](https://dblp.org/img/n.png)

\[c26\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yutong Zheng](https://dblp.org/pid/164/0869.html), [Chenchen Zhu](https://dblp.org/pid/50/6994.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Multiple Scale Faster-RCNN Approach to Driver's Cell-Phone Usage and Hands on Steering Wheel Detection. [CVPR Workshops2016](https://dblp.org/db/conf/cvpr/cvprw2016.html#conf/cvpr/LeZZLS16): 46-53
- ![](https://dblp.org/img/n.png)

\[c25\]
[Chenchen Zhu](https://dblp.org/pid/50/6994.html), [Yutong Zheng](https://dblp.org/pid/164/0869.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chandrasekhar Bhagavatula](https://dblp.org/pid/126/4520.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Weakly Supervised Facial Analysis with Dense Hyper-Column Features. [CVPR Workshops2016](https://dblp.org/db/conf/cvpr/cvprw2016.html#conf/cvpr/ZhuZLLBS16): 93-101
- ![](https://dblp.org/img/n.png)

\[c24\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html):

Longitudinal Face Modeling via Temporal Deep Restricted Boltzmann Machines. [CVPR2016](https://dblp.org/db/conf/cvpr/cvpr2016.html#conf/cvpr/DuongLQB16): 5772-5780
- ![](https://dblp.org/img/n.png)

\[c23\]
[Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html):

Robust Deep Appearance Models. [ICPR2016](https://dblp.org/db/conf/icpr/icpr2016.html#conf/icpr/QuachDLB16): 390-395
- ![](https://dblp.org/img/n.png)

\[c22\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), [Chenchen Zhu](https://dblp.org/pid/50/6994.html), [Yutong Zheng](https://dblp.org/pid/164/0869.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Robust hand detection in Vehicles. [ICPR2016](https://dblp.org/db/conf/icpr/icpr2016.html#conf/icpr/LeZZLS16): 573-578
- ![](https://dblp.org/img/n.png)

\[c21\]
[Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html):

Depth-based 3D hand pose tracking. [ICPR2016](https://dblp.org/db/conf/icpr/icpr2016.html#conf/icpr/QuachDLB16a): 2746-2751
- ![](https://dblp.org/img/n.png)

\[i5\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), Khoa Luu, [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html):

Longitudinal Face Modeling via Temporal Deep Restricted Boltzmann Machines. [CoRRabs/1606.02254](https://dblp.org/db/journals/corr/corr1606.html#journals/corr/DuongLQB16) (2016)
- ![](https://dblp.org/img/n.png)

\[i4\]
[Chenchen Zhu](https://dblp.org/pid/50/6994.html), [Yutong Zheng](https://dblp.org/pid/164/0869.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

CMS-RCNN: Contextual Multi-Scale Region-based CNN for Unconstrained Face Detection. [CoRRabs/1606.05413](https://dblp.org/db/journals/corr/corr1606.html#journals/corr/ZhuZLS16) (2016)
- ![](https://dblp.org/img/n.png)

\[i3\]
[Kha Gia Quach](https://dblp.org/pid/73/11111.html), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html):

Robust Deep Appearance Models. [CoRRabs/1607.00659](https://dblp.org/db/journals/corr/corr1607.html#journals/corr/QuachDLB16) (2016)
- ![](https://dblp.org/img/n.png)

\[i2\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html), Khoa Luu, [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html):

Deep Appearance Models: A Deep Boltzmann Machine Approach for Face Modeling. [CoRRabs/1607.06871](https://dblp.org/db/journals/corr/corr1607.html#journals/corr/DuongLQB16a) (2016)
- ![](https://dblp.org/img/n.png)

\[i1\]
[Yutong Zheng](https://dblp.org/pid/164/0869.html), [Chenchen Zhu](https://dblp.org/pid/50/6994.html), Khoa Luu, [Chandrasekhar Bhagavatula](https://dblp.org/pid/126/4520.html), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Towards a Deep Learning Framework for Unconstrained Face Detection. [CoRRabs/1612.05322](https://dblp.org/db/journals/corr/corr1612.html#journals/corr/ZhengZLBLS16) (2016)
- 2015
- ![](https://dblp.org/img/n.png)

\[j3\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Keshav Seshadri](https://dblp.org/pid/95/10072.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Facial aging and asymmetry decomposition based approaches to identification of twins. [Pattern Recognit.48(12)](https://dblp.org/db/journals/pr/pr48.html#journals/pr/LeSLS15): 3843-3856 (2015)
- ![](https://dblp.org/img/n.png)

\[j2\]
[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Spartans: Single-Sample Periocular-Based Alignment-Robust Recognition Technique Applied to Non-Frontal Scenarios. [IEEE Trans. Image Process.24(12)](https://dblp.org/db/journals/tip/tip24.html#journals/tip/Juefei-XuLS15): 4780-4795 (2015)
- ![](https://dblp.org/img/n.png)

\[c20\]
[Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html):

Beyond Principal Components: Deep Boltzmann Machines for face modeling. [CVPR2015](https://dblp.org/db/conf/cvpr/cvpr2015.html#conf/cvpr/DuongLQB15): 4786-4794
- ![](https://dblp.org/img/n.png)

\[c19\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Fast and robust self-training beard/moustache detection and segmentation. [ICB2015](https://dblp.org/db/conf/icb/icb2015.html#conf/icb/LeLS15): 507-512
- ![](https://dblp.org/img/n.png)

\[c18\]
[Karanhaar Singh](https://dblp.org/pid/11/10698.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

A robust contour sampling and tensor-based approach to facial beard and mustache shape segmentation and matching. [ICIP2015](https://dblp.org/db/conf/icip/icip2015.html#conf/icip/SinghLLS15): 1399-1403
- ![](https://dblp.org/img/n.png)

\[c17\]
[Raied Aljadaany](https://dblp.org/pid/172/9558.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Shreyas Venugopalan](https://dblp.org/pid/70/9171.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

IRIS super-resolution via nonparametric over-complete dictionary learning. [ICIP2015](https://dblp.org/db/conf/icip/icip2015.html#conf/icip/AljadaanyLVS15): 3856-3860
- 2014
- ![](https://dblp.org/img/n.png)

\[c16\]
Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Chenchen Zhu](https://dblp.org/pid/50/6994.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Distributed class dependent feature analysis - A big data approach. [IEEE BigData2014](https://dblp.org/db/conf/bigdataconf/bigdataconf2014.html#conf/bigdataconf/LuuZS14): 201-206
- 2013
- ![](https://dblp.org/img/n.png)

\[j1\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

SparCLeS: Dynamic 퓁 1 Sparse Classifiers With Level Sets for Robust Beard/Moustache Detection and Segmentation. [IEEE Trans. Image Process.22(8)](https://dblp.org/db/journals/tip/tip22.html#journals/tip/LeLS13): 3097-3107 (2013)
- 2012
- ![](https://dblp.org/img/n.png)

\[c15\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Keshav Seshadri](https://dblp.org/pid/95/10072.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

A facial aging approach to identification of identical twins. [BTAS2012](https://dblp.org/db/conf/btas/btas2012.html#conf/btas/LeLSS12): 91-98
- ![](https://dblp.org/img/n.png)

\[c14\]
[Yiting Xie](https://dblp.org/pid/143/4278.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

A robust approach to facial ethnicity classification on large scale face databases. [BTAS2012](https://dblp.org/db/conf/btas/btas2012.html#conf/btas/XieLS12): 143-149
- ![](https://dblp.org/img/n.png)

\[c13\]
[Sasikanth Bendapudi](https://dblp.org/pid/157/7592.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Hallucinating faces in the dark. [BTAS2012](https://dblp.org/db/conf/btas/btas2012.html#conf/btas/BendapudiLS12): 311-318
- ![](https://dblp.org/img/n.png)

\[c12\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Keshav Seshadri](https://dblp.org/pid/95/10072.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Beard and mustache segmentation using sparse classifiers on self-quotient images. [ICIP2012](https://dblp.org/db/conf/icip/icip2012.html#conf/icip/LeLSS12): 165-168
- ![](https://dblp.org/img/n.png)

\[c11\]
Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Keshav Seshadri](https://dblp.org/pid/95/10072.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

Facecut - a robust approach for facial feature segmentation. [ICIP2012](https://dblp.org/db/conf/icip/icip2012.html#conf/icip/LuuLSS12): 1841-1844
- ![](https://dblp.org/img/n.png)

\[c10\]
[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Utsav Prabhu](https://dblp.org/pid/54/10072.html), [Marios Savvides](https://dblp.org/pid/13/3793.html):

A novel energy based filter for cross-blink eye detection. [ICIP2012](https://dblp.org/db/conf/icip/icip2012.html#conf/icip/LeLPS12): 1845-1848
- ![](https://dblp.org/img/n.png)

\[c9\]
Khoa Luu, [Marios Savvides](https://dblp.org/pid/13/3793.html), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), [Ching Y. Suen](https://dblp.org/pid/s/ChingYSuen.html):

Compressed Submanifold Multifactor Analysis with adaptive factor structures. [ICPR2012](https://dblp.org/db/conf/icpr/icpr2012.html#conf/icpr/LuuSBS12): 2715-2718
- ![](https://dblp.org/img/n.png)

\[c8\]
[Kha Gia Quach](https://dblp.org/pid/73/11111.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi Nhan Duong](https://dblp.org/pid/16/11112.html)![](https://dblp.org/img/orcid-mark.12x12.png), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Hoai Bac Le](https://dblp.org/pid/93/5448.html):

Gabor Wavelet-Based Appearance Models. [RIVF2012](https://dblp.org/db/conf/rivf/rivf2012.html#conf/rivf/QuachDLL12): 1-6
- 2011
- ![](https://dblp.org/img/n.png)

\[c7\]
Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Tien Dai Bui](https://dblp.org/pid/b/TienDBui.html), [Ching Y. Suen](https://dblp.org/pid/s/ChingYSuen.html):

Kernel spectral regression of perceived age from hybrid facial features. [FG2011](https://dblp.org/db/conf/fgr/fg2011.html#conf/fgr/LuuBS11): 71-76
- ![](https://dblp.org/img/n.png)

\[c6\]
[Cuixian Chen](https://dblp.org/pid/06/9606.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Yishi Wang](https://dblp.org/pid/15/9606.html), [Karl Ricanek](https://dblp.org/pid/39/609.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

Facial feature fusion and model selection for age estimation. [FG2011](https://dblp.org/db/conf/fgr/fg2011.html#conf/fgr/ChenYWRL11): 200-205
- ![](https://dblp.org/img/n.png)

\[c5\]
[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Marios Savvides](https://dblp.org/pid/13/3793.html), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), [Ching Y. Suen](https://dblp.org/pid/s/ChingYSuen.html):

Investigating age invariant face recognition based on periocular biometrics. [IJCB2011](https://dblp.org/db/conf/icb/ijcb2011.html#conf/icb/Juefei-XuLSBS11): 1-7
- ![](https://dblp.org/img/n.png)

\[c4\]
Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Keshav Seshadri](https://dblp.org/pid/95/10072.html), [Marios Savvides](https://dblp.org/pid/13/3793.html), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), [Ching Y. Suen](https://dblp.org/pid/s/ChingYSuen.html):

Contourlet appearance model for facial age estimation. [IJCB2011](https://dblp.org/db/conf/icb/ijcb2011.html#conf/icb/LuuSSBS11): 1-8
- 2010
- ![](https://dblp.org/img/n.png)

\[c3\]
Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png):

A Computer Approach for Face Aging Problems. [Canadian AI2010](https://dblp.org/db/conf/ai/ai2010.html#conf/ai/Luu10): 405-409
- ![](https://dblp.org/img/n.png)

\[c2\]
Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Tien Dai Bui](https://dblp.org/pid/b/TienDBui.html), [Ching Y. Suen](https://dblp.org/pid/s/ChingYSuen.html), [Karl Ricanek](https://dblp.org/pid/39/609.html):

Spectral Regression based age determination. [CVPR Workshops2010](https://dblp.org/db/conf/cvpr/cvprw2010.html#conf/cvpr/LuuBSR10): 103-107
- ![](https://dblp.org/img/n.png)

\[c1\]
Khoa Luu![](https://dblp.org/img/orcid-mark.12x12.png), [Tien D. Bui](https://dblp.org/pid/b/TienDBui.html), [Ching Y. Suen](https://dblp.org/pid/s/ChingYSuen.html), [Karl Ricanek](https://dblp.org/pid/39/609.html):

Combined local and holistic facial features for age-determination. [ICARCV2010](https://dblp.org/db/conf/icarcv/icarcv2010.html#conf/icarcv/LuuBSR10): 900-904
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/43/8092.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Samaneh Abbasi-Sureshjani](https://dblp.org/pid/164/7548.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[2](https://dblp.org/pid/43/8092.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Pedro H. Abreu](https://dblp.org/pid/66/6482.html)

aka: Pedro Henriques Abreu

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[3](https://dblp.org/pid/43/8092.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Donald A. Adjeroh](https://dblp.org/pid/30/1579.html)

[\[c66\]](https://dblp.org/pid/43/8092.html#c66) [\[i56\]](https://dblp.org/pid/43/8092.html#i56)

[4](https://dblp.org/pid/43/8092.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Nitin Agarwal](https://dblp.org/pid/72/1395.html)

[\[i90\]](https://dblp.org/pid/43/8092.html#i90)

[5](https://dblp.org/pid/43/8092.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Shadi Albarqouni](https://dblp.org/pid/165/7751.html)

[\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[6](https://dblp.org/pid/43/8092.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Raied Aljadaany](https://dblp.org/pid/172/9558.html)

[\[c17\]](https://dblp.org/pid/43/8092.html#c17)

[7](https://dblp.org/pid/43/8092.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Jessica L. Allen](https://dblp.org/pid/158/2631.html)

[\[j14\]](https://dblp.org/pid/43/8092.html#j14)

[8](https://dblp.org/pid/43/8092.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[José Pereira Amorim](https://dblp.org/pid/275/9315.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[9](https://dblp.org/pid/43/8092.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Nicholas Ayache](https://dblp.org/pid/a/NicholasAyache.html)

[\[j13\]](https://dblp.org/pid/43/8092.html#j13) [\[i33\]](https://dblp.org/pid/43/8092.html#i33)

[10](https://dblp.org/pid/43/8092.html?view=joint&param=10 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=2)

[Jessica R. Baron](https://dblp.org/pid/216/5214.html)

[\[j16\]](https://dblp.org/pid/43/8092.html#j16)

[11](https://dblp.org/pid/43/8092.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Sasikanth Bendapudi](https://dblp.org/pid/157/7592.html)

[\[c13\]](https://dblp.org/pid/43/8092.html#c13)

[12](https://dblp.org/pid/43/8092.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Chandrasekhar Bhagavatula](https://dblp.org/pid/126/4520.html)

[\[c28\]](https://dblp.org/pid/43/8092.html#c28) [\[i7\]](https://dblp.org/pid/43/8092.html#i7) [\[c27\]](https://dblp.org/pid/43/8092.html#c27) [\[c25\]](https://dblp.org/pid/43/8092.html#c25) [\[i1\]](https://dblp.org/pid/43/8092.html#i1)

[13](https://dblp.org/pid/43/8092.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Apoorva Bisht](https://dblp.org/pid/321/4247.html)

[\[j27\]](https://dblp.org/pid/43/8092.html#j27) [\[i42\]](https://dblp.org/pid/43/8092.html#i42)

[14](https://dblp.org/pid/43/8092.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Darren Blount](https://dblp.org/pid/402/6929.html)

[\[i96\]](https://dblp.org/pid/43/8092.html#i96) [\[i95\]](https://dblp.org/pid/43/8092.html#i95)

[15](https://dblp.org/pid/43/8092.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Christophe Bobda](https://dblp.org/pid/b/ChristopheBobda.html)

[\[i90\]](https://dblp.org/pid/43/8092.html#i90)

[16](https://dblp.org/pid/43/8092.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Nicholas Borys](https://dblp.org/pid/381/4679.html)

[\[j28\]](https://dblp.org/pid/43/8092.html#j28) [\[i93\]](https://dblp.org/pid/43/8092.html#i93) [\[i87\]](https://dblp.org/pid/43/8092.html#i87) [\[i79\]](https://dblp.org/pid/43/8092.html#i79)

[17](https://dblp.org/pid/43/8092.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Abdesselam Bouzerdoum](https://dblp.org/pid/00/5421.html)

[\[j20\]](https://dblp.org/pid/43/8092.html#j20) [\[j18\]](https://dblp.org/pid/43/8092.html#j18)

[18](https://dblp.org/pid/43/8092.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Alexander Bucksch](https://dblp.org/pid/44/7634.html)

[\[i88\]](https://dblp.org/pid/43/8092.html#i88)

[19](https://dblp.org/pid/43/8092.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Duc Toan Bui 0002](https://dblp.org/pid/253/0379-2.html)

[\[c47\]](https://dblp.org/pid/43/8092.html#c47)

[20](https://dblp.org/pid/43/8092.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Hung Bui](https://dblp.org/pid/59/10562.html)

[\[c39\]](https://dblp.org/pid/43/8092.html#c39) [\[i27\]](https://dblp.org/pid/43/8092.html#i27)

[21](https://dblp.org/pid/43/8092.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Quoc-Huy Bui](https://dblp.org/pid/317/0417.html)

[\[c51\]](https://dblp.org/pid/43/8092.html#c51) [\[i45\]](https://dblp.org/pid/43/8092.html#i45)

[22](https://dblp.org/pid/43/8092.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Tien D. Bui](https://dblp.org/pid/b/TienDBui.html)

aka: Tien Dai Bui

[\[j22\]](https://dblp.org/pid/43/8092.html#j22) [\[i39\]](https://dblp.org/pid/43/8092.html#i39) [\[c47\]](https://dblp.org/pid/43/8092.html#c47) [\[i26\]](https://dblp.org/pid/43/8092.html#i26) [\[i25\]](https://dblp.org/pid/43/8092.html#i25) [\[j11\]](https://dblp.org/pid/43/8092.html#j11) [\[j10\]](https://dblp.org/pid/43/8092.html#j10) [\[c34\]](https://dblp.org/pid/43/8092.html#c34) [\[c31\]](https://dblp.org/pid/43/8092.html#c31) [\[i17\]](https://dblp.org/pid/43/8092.html#i17) [\[i14\]](https://dblp.org/pid/43/8092.html#i14) [\[j7\]](https://dblp.org/pid/43/8092.html#j7) [\[j5\]](https://dblp.org/pid/43/8092.html#j5) [\[c24\]](https://dblp.org/pid/43/8092.html#c24) [\[c23\]](https://dblp.org/pid/43/8092.html#c23) [\[c21\]](https://dblp.org/pid/43/8092.html#c21) [\[i5\]](https://dblp.org/pid/43/8092.html#i5) [\[i3\]](https://dblp.org/pid/43/8092.html#i3) [\[i2\]](https://dblp.org/pid/43/8092.html#i2) [\[c20\]](https://dblp.org/pid/43/8092.html#c20) [\[c9\]](https://dblp.org/pid/43/8092.html#c9) [\[c7\]](https://dblp.org/pid/43/8092.html#c7) [\[c5\]](https://dblp.org/pid/43/8092.html#c5) [\[c4\]](https://dblp.org/pid/43/8092.html#c4) [\[c2\]](https://dblp.org/pid/43/8092.html#c2) [\[c1\]](https://dblp.org/pid/43/8092.html#c1)

[23](https://dblp.org/pid/43/8092.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Toan Duc Bui](https://dblp.org/pid/143/9351.html)

[\[c42\]](https://dblp.org/pid/43/8092.html#c42) [\[c38\]](https://dblp.org/pid/43/8092.html#c38) [\[c36\]](https://dblp.org/pid/43/8092.html#c36) [\[i24\]](https://dblp.org/pid/43/8092.html#i24) [\[i23\]](https://dblp.org/pid/43/8092.html#i23)

[24](https://dblp.org/pid/43/8092.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Joshua Burbridge](https://dblp.org/pid/241/9738.html)

[\[i20\]](https://dblp.org/pid/43/8092.html#i20)

[25](https://dblp.org/pid/43/8092.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Sonya J. Burroughs](https://dblp.org/pid/292/5602.html)

[\[c41\]](https://dblp.org/pid/43/8092.html#c41)

[26](https://dblp.org/pid/43/8092.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Jaime S. Cardoso 0001](https://dblp.org/pid/65/5236.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[27](https://dblp.org/pid/43/8092.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Manuel Jorge Cardoso](https://dblp.org/pid/17/7426.html)

aka: M. Jorge Cardoso

[\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[28](https://dblp.org/pid/43/8092.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Naga Venkata Sai Raviteja Chappa](https://dblp.org/pid/321/0642.html)

aka: Ravi Teja N. V. S. Chappa

[\[j33\]](https://dblp.org/pid/43/8092.html#j33) [\[c70\]](https://dblp.org/pid/43/8092.html#c70) [\[i99\]](https://dblp.org/pid/43/8092.html#i99) [\[j26\]](https://dblp.org/pid/43/8092.html#j26) [\[j23\]](https://dblp.org/pid/43/8092.html#j23) [\[i72\]](https://dblp.org/pid/43/8092.html#i72) [\[i71\]](https://dblp.org/pid/43/8092.html#i71) [\[i69\]](https://dblp.org/pid/43/8092.html#i69) [\[c58\]](https://dblp.org/pid/43/8092.html#c58) [\[i66\]](https://dblp.org/pid/43/8092.html#i66) [\[i60\]](https://dblp.org/pid/43/8092.html#i60) [\[i50\]](https://dblp.org/pid/43/8092.html#i50) [\[i47\]](https://dblp.org/pid/43/8092.html#i47) [\[j21\]](https://dblp.org/pid/43/8092.html#j21) [\[c48\]](https://dblp.org/pid/43/8092.html#c48) [\[i43\]](https://dblp.org/pid/43/8092.html#i43)

[29](https://dblp.org/pid/43/8092.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Cuixian Chen](https://dblp.org/pid/06/9606.html)

[\[c6\]](https://dblp.org/pid/43/8092.html#c6)

[30](https://dblp.org/pid/43/8092.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Samuel Yen-Chi Chen](https://dblp.org/pid/244/2264.html)

[\[j28\]](https://dblp.org/pid/43/8092.html#j28) [\[c62\]](https://dblp.org/pid/43/8092.html#c62) [\[i81\]](https://dblp.org/pid/43/8092.html#i81) [\[i79\]](https://dblp.org/pid/43/8092.html#i79)

[31](https://dblp.org/pid/43/8092.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Veronika Cheplygina](https://dblp.org/pid/91/10084.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[32](https://dblp.org/pid/43/8092.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Arabinda Choudhary](https://dblp.org/pid/312/7044.html)

[\[c42\]](https://dblp.org/pid/43/8092.html#c42)

[33](https://dblp.org/pid/43/8092.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Arabinda Kumar Choudhary](https://dblp.org/pid/393/1551.html)

[\[j35\]](https://dblp.org/pid/43/8092.html#j35) [\[i70\]](https://dblp.org/pid/43/8092.html#i70) [\[i68\]](https://dblp.org/pid/43/8092.html#i68)

[34](https://dblp.org/pid/43/8092.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Hugh Churchill](https://dblp.org/pid/241/9507.html)

[\[j28\]](https://dblp.org/pid/43/8092.html#j28) [\[i93\]](https://dblp.org/pid/43/8092.html#i93) [\[i87\]](https://dblp.org/pid/43/8092.html#i87) [\[j27\]](https://dblp.org/pid/43/8092.html#j27) [\[j24\]](https://dblp.org/pid/43/8092.html#j24) [\[c62\]](https://dblp.org/pid/43/8092.html#c62) [\[c61\]](https://dblp.org/pid/43/8092.html#c61) [\[c60\]](https://dblp.org/pid/43/8092.html#c60) [\[i84\]](https://dblp.org/pid/43/8092.html#i84) [\[i81\]](https://dblp.org/pid/43/8092.html#i81) [\[i80\]](https://dblp.org/pid/43/8092.html#i80) [\[i79\]](https://dblp.org/pid/43/8092.html#i79) [\[i75\]](https://dblp.org/pid/43/8092.html#i75) [\[i70\]](https://dblp.org/pid/43/8092.html#i70) [\[i53\]](https://dblp.org/pid/43/8092.html#i53) [\[i42\]](https://dblp.org/pid/43/8092.html#i42) [\[i20\]](https://dblp.org/pid/43/8092.html#i20)

[35](https://dblp.org/pid/43/8092.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Jackson David Cothren](https://dblp.org/pid/335/1787.html)

[\[c72\]](https://dblp.org/pid/43/8092.html#c72) [\[c71\]](https://dblp.org/pid/43/8092.html#c71) [\[i91\]](https://dblp.org/pid/43/8092.html#i91) [\[c69\]](https://dblp.org/pid/43/8092.html#c69) [\[c65\]](https://dblp.org/pid/43/8092.html#c65) [\[c64\]](https://dblp.org/pid/43/8092.html#c64) [\[i78\]](https://dblp.org/pid/43/8092.html#i78) [\[i76\]](https://dblp.org/pid/43/8092.html#i76) [\[i73\]](https://dblp.org/pid/43/8092.html#i73) [\[i67\]](https://dblp.org/pid/43/8092.html#i67) [\[c57\]](https://dblp.org/pid/43/8092.html#c57) [\[i65\]](https://dblp.org/pid/43/8092.html#i65) [\[i63\]](https://dblp.org/pid/43/8092.html#i63) [\[i51\]](https://dblp.org/pid/43/8092.html#i51) [\[i36\]](https://dblp.org/pid/43/8092.html#i36)

[36](https://dblp.org/pid/43/8092.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Ricardo P. M. Cruz](https://dblp.org/pid/362/3525.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[37](https://dblp.org/pid/43/8092.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Aditya Dendukuri](https://dblp.org/pid/232/3153.html)

[\[j12\]](https://dblp.org/pid/43/8092.html#j12) [\[i20\]](https://dblp.org/pid/43/8092.html#i20) [\[i11\]](https://dblp.org/pid/43/8092.html#i11)

[38](https://dblp.org/pid/43/8092.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Anh Duy Le Dinh](https://dblp.org/pid/348/6822.html)

[\[c66\]](https://dblp.org/pid/43/8092.html#c66) [\[i56\]](https://dblp.org/pid/43/8092.html#i56)

[39](https://dblp.org/pid/43/8092.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Minh N. Do](https://dblp.org/pid/d/MinhNDo.html)

[\[i12\]](https://dblp.org/pid/43/8092.html#i12)

[40](https://dblp.org/pid/43/8092.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Page Daniel Dobbs](https://dblp.org/pid/344/0595.html)

[\[j33\]](https://dblp.org/pid/43/8092.html#j33) [\[i99\]](https://dblp.org/pid/43/8092.html#i99) [\[j26\]](https://dblp.org/pid/43/8092.html#j26) [\[j23\]](https://dblp.org/pid/43/8092.html#j23) [\[i72\]](https://dblp.org/pid/43/8092.html#i72) [\[i69\]](https://dblp.org/pid/43/8092.html#i69) [\[c58\]](https://dblp.org/pid/43/8092.html#c58) [\[i66\]](https://dblp.org/pid/43/8092.html#i66) [\[i60\]](https://dblp.org/pid/43/8092.html#i60) [\[i50\]](https://dblp.org/pid/43/8092.html#i50)

[41](https://dblp.org/pid/43/8092.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Gianfranco Doretto](https://dblp.org/pid/61/3857.html)

[\[c66\]](https://dblp.org/pid/43/8092.html#c66) [\[i56\]](https://dblp.org/pid/43/8092.html#i56)

[42](https://dblp.org/pid/43/8092.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Ashley Dowling](https://dblp.org/pid/321/0870.html)

aka: Ashley P. G. Dowling

[\[j31\]](https://dblp.org/pid/43/8092.html#j31) [\[i98\]](https://dblp.org/pid/43/8092.html#i98) [\[c67\]](https://dblp.org/pid/43/8092.html#c67) [\[i63\]](https://dblp.org/pid/43/8092.html#i63) [\[i62\]](https://dblp.org/pid/43/8092.html#i62) [\[i52\]](https://dblp.org/pid/43/8092.html#i52) [\[c48\]](https://dblp.org/pid/43/8092.html#c48) [\[i43\]](https://dblp.org/pid/43/8092.html#i43)

[43](https://dblp.org/pid/43/8092.html?view=joint&param=43 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=3)

[Yatish Dubasi](https://dblp.org/pid/356/9091.html)

[\[c54\]](https://dblp.org/pid/43/8092.html#c54)

[44](https://dblp.org/pid/43/8092.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Chi Nhan Duong](https://dblp.org/pid/16/11112.html)

[\[j25\]](https://dblp.org/pid/43/8092.html#j25) [\[j22\]](https://dblp.org/pid/43/8092.html#j22) [\[c59\]](https://dblp.org/pid/43/8092.html#c59) [\[i64\]](https://dblp.org/pid/43/8092.html#i64) [\[i63\]](https://dblp.org/pid/43/8092.html#i63) [\[i62\]](https://dblp.org/pid/43/8092.html#i62) [\[i61\]](https://dblp.org/pid/43/8092.html#i61) [\[j17\]](https://dblp.org/pid/43/8092.html#j17) [\[c52\]](https://dblp.org/pid/43/8092.html#c52) [\[c51\]](https://dblp.org/pid/43/8092.html#c51) [\[i45\]](https://dblp.org/pid/43/8092.html#i45) [\[i44\]](https://dblp.org/pid/43/8092.html#i44) [\[i39\]](https://dblp.org/pid/43/8092.html#i39) [\[i38\]](https://dblp.org/pid/43/8092.html#i38) [\[i37\]](https://dblp.org/pid/43/8092.html#i37) [\[j15\]](https://dblp.org/pid/43/8092.html#j15) [\[c47\]](https://dblp.org/pid/43/8092.html#c47) [\[c46\]](https://dblp.org/pid/43/8092.html#c46) [\[c44\]](https://dblp.org/pid/43/8092.html#c44) [\[c43\]](https://dblp.org/pid/43/8092.html#c43) [\[i31\]](https://dblp.org/pid/43/8092.html#i31) [\[i30\]](https://dblp.org/pid/43/8092.html#i30) [\[i29\]](https://dblp.org/pid/43/8092.html#i29) [\[c40\]](https://dblp.org/pid/43/8092.html#c40) [\[c39\]](https://dblp.org/pid/43/8092.html#c39) [\[i27\]](https://dblp.org/pid/43/8092.html#i27) [\[i26\]](https://dblp.org/pid/43/8092.html#i26) [\[i25\]](https://dblp.org/pid/43/8092.html#i25) [\[j11\]](https://dblp.org/pid/43/8092.html#j11) [\[j10\]](https://dblp.org/pid/43/8092.html#j10) [\[c35\]](https://dblp.org/pid/43/8092.html#c35) [\[c34\]](https://dblp.org/pid/43/8092.html#c34) [\[i22\]](https://dblp.org/pid/43/8092.html#i22) [\[i21\]](https://dblp.org/pid/43/8092.html#i21) [\[i19\]](https://dblp.org/pid/43/8092.html#i19) [\[i18\]](https://dblp.org/pid/43/8092.html#i18) [\[j9\]](https://dblp.org/pid/43/8092.html#j9) [\[j8\]](https://dblp.org/pid/43/8092.html#j8) [\[c31\]](https://dblp.org/pid/43/8092.html#c31) [\[i17\]](https://dblp.org/pid/43/8092.html#i17) [\[i15\]](https://dblp.org/pid/43/8092.html#i15) [\[i14\]](https://dblp.org/pid/43/8092.html#i14) [\[i13\]](https://dblp.org/pid/43/8092.html#i13) [\[i12\]](https://dblp.org/pid/43/8092.html#i12) [\[j7\]](https://dblp.org/pid/43/8092.html#j7) [\[c30\]](https://dblp.org/pid/43/8092.html#c30) [\[c29\]](https://dblp.org/pid/43/8092.html#c29) [\[i10\]](https://dblp.org/pid/43/8092.html#i10) [\[i8\]](https://dblp.org/pid/43/8092.html#i8) [\[i6\]](https://dblp.org/pid/43/8092.html#i6) [\[c24\]](https://dblp.org/pid/43/8092.html#c24) [\[c23\]](https://dblp.org/pid/43/8092.html#c23) [\[c21\]](https://dblp.org/pid/43/8092.html#c21) [\[i5\]](https://dblp.org/pid/43/8092.html#i5) [\[i3\]](https://dblp.org/pid/43/8092.html#i3) [\[i2\]](https://dblp.org/pid/43/8092.html#i2) [\[c20\]](https://dblp.org/pid/43/8092.html#c20) [\[c8\]](https://dblp.org/pid/43/8092.html#c8)

[45](https://dblp.org/pid/43/8092.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Tim Faltermeier](https://dblp.org/pid/412/8876.html)

[\[i93\]](https://dblp.org/pid/43/8092.html#i93)

[46](https://dblp.org/pid/43/8092.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Arash Fereidouni](https://dblp.org/pid/241/9731.html)

[\[i20\]](https://dblp.org/pid/43/8092.html#i20)

[47](https://dblp.org/pid/43/8092.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[David M. Ford](https://dblp.org/pid/116/9240.html)

[\[j12\]](https://dblp.org/pid/43/8092.html#j12)

[48](https://dblp.org/pid/43/8092.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[John Gauch](https://dblp.org/pid/70/5847.html)

[\[i55\]](https://dblp.org/pid/43/8092.html#i55)

[49](https://dblp.org/pid/43/8092.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Susan Gauch](https://dblp.org/pid/g/SusanGauch.html)

[\[c63\]](https://dblp.org/pid/43/8092.html#c63) [\[i77\]](https://dblp.org/pid/43/8092.html#i77) [\[c59\]](https://dblp.org/pid/43/8092.html#c59) [\[i64\]](https://dblp.org/pid/43/8092.html#i64)

[50](https://dblp.org/pid/43/8092.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Fiona L. Goggin](https://dblp.org/pid/415/8043.html)

[\[i88\]](https://dblp.org/pid/43/8092.html#i88)

[51](https://dblp.org/pid/43/8092.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Balakrishna Gokaraju](https://dblp.org/pid/61/8963.html)

[\[c41\]](https://dblp.org/pid/43/8092.html#c41)

[52](https://dblp.org/pid/43/8092.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Susana Rodriguez Gongora](https://dblp.org/pid/393/0878.html)

[\[i69\]](https://dblp.org/pid/43/8092.html#i69)

[53](https://dblp.org/pid/43/8092.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Aranyak Goswami](https://dblp.org/pid/415/8022.html)

[\[i88\]](https://dblp.org/pid/43/8092.html#i88)

[54](https://dblp.org/pid/43/8092.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Ligong Han](https://dblp.org/pid/187/1675.html)

[\[j9\]](https://dblp.org/pid/43/8092.html#j9) [\[i8\]](https://dblp.org/pid/43/8092.html#i8)

[55](https://dblp.org/pid/43/8092.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Nathaniel Harris](https://dblp.org/pid/336/2673.html)

[\[i35\]](https://dblp.org/pid/43/8092.html#i35)

[56](https://dblp.org/pid/43/8092.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Nicholas Heller](https://dblp.org/pid/205/5397.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[57](https://dblp.org/pid/43/8092.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Pierce Helton](https://dblp.org/pid/328/9598.html)

[\[c69\]](https://dblp.org/pid/43/8092.html#c69) [\[i62\]](https://dblp.org/pid/43/8092.html#i62) [\[j21\]](https://dblp.org/pid/43/8092.html#j21) [\[i36\]](https://dblp.org/pid/43/8092.html#i36)

[58](https://dblp.org/pid/43/8092.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Minh Hoai](https://dblp.org/pid/135/4935.html)

[\[c45\]](https://dblp.org/pid/43/8092.html#c45) [\[i32\]](https://dblp.org/pid/43/8092.html#i32)

[59](https://dblp.org/pid/43/8092.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[James Holliday](https://dblp.org/pid/376/0876.html)

[\[i100\]](https://dblp.org/pid/43/8092.html#i100) [\[i95\]](https://dblp.org/pid/43/8092.html#i95) [\[c61\]](https://dblp.org/pid/43/8092.html#c61) [\[i84\]](https://dblp.org/pid/43/8092.html#i84)

[60](https://dblp.org/pid/43/8092.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[James B. Holliday](https://dblp.org/pid/402/5752.html)

[\[i96\]](https://dblp.org/pid/43/8092.html#i96)

[61](https://dblp.org/pid/43/8092.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Miaoqing Huang](https://dblp.org/pid/45/5897.html)

[\[c50\]](https://dblp.org/pid/43/8092.html#c50) [\[i41\]](https://dblp.org/pid/43/8092.html#i41)

[62](https://dblp.org/pid/43/8092.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Chuong Huynh](https://dblp.org/pid/289/7090.html)

[\[c45\]](https://dblp.org/pid/43/8092.html#c45) [\[i32\]](https://dblp.org/pid/43/8092.html#i32)

[63](https://dblp.org/pid/43/8092.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Ivana Isgum](https://dblp.org/pid/62/5757.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[64](https://dblp.org/pid/43/8092.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Ibsa Jalata](https://dblp.org/pid/230/8158.html)

[\[j21\]](https://dblp.org/pid/43/8092.html#j21) [\[j17\]](https://dblp.org/pid/43/8092.html#j17) [\[j14\]](https://dblp.org/pid/43/8092.html#j14) [\[c35\]](https://dblp.org/pid/43/8092.html#c35) [\[i13\]](https://dblp.org/pid/43/8092.html#i13)

[65](https://dblp.org/pid/43/8092.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Hojin Jang](https://dblp.org/pid/193/8557.html)

[\[j34\]](https://dblp.org/pid/43/8092.html#j34) [\[i82\]](https://dblp.org/pid/43/8092.html#i82)

[66](https://dblp.org/pid/43/8092.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Steve B. Jiang](https://dblp.org/pid/73/2968.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2) [\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[67](https://dblp.org/pid/43/8092.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html)

[\[j2\]](https://dblp.org/pid/43/8092.html#j2) [\[c5\]](https://dblp.org/pid/43/8092.html#c5)

[68](https://dblp.org/pid/43/8092.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Gülce Kalyoncu](https://dblp.org/pid/273/7438.html)

[\[j12\]](https://dblp.org/pid/43/8092.html#j12)

[69](https://dblp.org/pid/43/8092.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Konstantinos Kamnitsas](https://dblp.org/pid/177/9280.html)

[\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[70](https://dblp.org/pid/43/8092.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Blake Keeling](https://dblp.org/pid/241/9366.html)

[\[i20\]](https://dblp.org/pid/43/8092.html#i20)

[71](https://dblp.org/pid/43/8092.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Samee Ullah Khan](https://dblp.org/pid/k/SameeUllahKhan.html)

aka: Samee U. Khan

[\[j34\]](https://dblp.org/pid/43/8092.html#j34) [\[j29\]](https://dblp.org/pid/43/8092.html#j29) [\[j28\]](https://dblp.org/pid/43/8092.html#j28) [\[i95\]](https://dblp.org/pid/43/8092.html#i95) [\[i92\]](https://dblp.org/pid/43/8092.html#i92) [\[j27\]](https://dblp.org/pid/43/8092.html#j27) [\[j24\]](https://dblp.org/pid/43/8092.html#j24) [\[c62\]](https://dblp.org/pid/43/8092.html#c62) [\[c60\]](https://dblp.org/pid/43/8092.html#c60) [\[i82\]](https://dblp.org/pid/43/8092.html#i82) [\[i81\]](https://dblp.org/pid/43/8092.html#i81) [\[i80\]](https://dblp.org/pid/43/8092.html#i80) [\[i79\]](https://dblp.org/pid/43/8092.html#i79) [\[i75\]](https://dblp.org/pid/43/8092.html#i75) [\[i70\]](https://dblp.org/pid/43/8092.html#i70) [\[i55\]](https://dblp.org/pid/43/8092.html#i55) [\[i53\]](https://dblp.org/pid/43/8092.html#i53) [\[i49\]](https://dblp.org/pid/43/8092.html#i49)

[72](https://dblp.org/pid/43/8092.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Michael Kidd](https://dblp.org/pid/200/4886.html)

[\[c49\]](https://dblp.org/pid/43/8092.html#c49) [\[i40\]](https://dblp.org/pid/43/8092.html#i40)

[73](https://dblp.org/pid/43/8092.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Kris Makoto Kitani](https://dblp.org/pid/42/163.html)

aka: Kris Kitani

[\[c56\]](https://dblp.org/pid/43/8092.html#c56) [\[i59\]](https://dblp.org/pid/43/8092.html#i59)

[74](https://dblp.org/pid/43/8092.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Bac Le](https://dblp.org/pid/93/5448.html)

aka: Hoai Bac Le

[\[c8\]](https://dblp.org/pid/43/8092.html#c8)

[75](https://dblp.org/pid/43/8092.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Hoang Thanh Le 0001](https://dblp.org/pid/226/5364-1.html)

[\[j20\]](https://dblp.org/pid/43/8092.html#j20)

[76](https://dblp.org/pid/43/8092.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Huu Le](https://dblp.org/pid/191/4630.html)

[\[i39\]](https://dblp.org/pid/43/8092.html#i39) [\[c46\]](https://dblp.org/pid/43/8092.html#c46) [\[i31\]](https://dblp.org/pid/43/8092.html#i31)

[77](https://dblp.org/pid/43/8092.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Ngan Hoang Le](https://dblp.org/pid/361/2252.html)

[\[c66\]](https://dblp.org/pid/43/8092.html#c66) [\[i56\]](https://dblp.org/pid/43/8092.html#i56)

[78](https://dblp.org/pid/43/8092.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[T. Hoang Ngan Le](https://dblp.org/pid/37/245.html)

aka: Ngan Le

aka: Thi Hoang Ngan Le

[\[j25\]](https://dblp.org/pid/43/8092.html#j25) [\[j23\]](https://dblp.org/pid/43/8092.html#j23) [\[c65\]](https://dblp.org/pid/43/8092.html#c65) [\[i73\]](https://dblp.org/pid/43/8092.html#i73) [\[j22\]](https://dblp.org/pid/43/8092.html#j22) [\[c57\]](https://dblp.org/pid/43/8092.html#c57) [\[i65\]](https://dblp.org/pid/43/8092.html#i65) [\[i47\]](https://dblp.org/pid/43/8092.html#i47) [\[j19\]](https://dblp.org/pid/43/8092.html#j19) [\[j17\]](https://dblp.org/pid/43/8092.html#j17) [\[c53\]](https://dblp.org/pid/43/8092.html#c53) [\[c52\]](https://dblp.org/pid/43/8092.html#c52) [\[c50\]](https://dblp.org/pid/43/8092.html#c50) [\[c49\]](https://dblp.org/pid/43/8092.html#c49) [\[c48\]](https://dblp.org/pid/43/8092.html#c48) [\[i46\]](https://dblp.org/pid/43/8092.html#i46) [\[i44\]](https://dblp.org/pid/43/8092.html#i44) [\[i43\]](https://dblp.org/pid/43/8092.html#i43) [\[i41\]](https://dblp.org/pid/43/8092.html#i41) [\[i40\]](https://dblp.org/pid/43/8092.html#i40) [\[i38\]](https://dblp.org/pid/43/8092.html#i38) [\[i37\]](https://dblp.org/pid/43/8092.html#i37) [\[i34\]](https://dblp.org/pid/43/8092.html#i34) [\[j15\]](https://dblp.org/pid/43/8092.html#j15) [\[j13\]](https://dblp.org/pid/43/8092.html#j13) [\[c44\]](https://dblp.org/pid/43/8092.html#c44) [\[c43\]](https://dblp.org/pid/43/8092.html#c43) [\[c42\]](https://dblp.org/pid/43/8092.html#c42) [\[i33\]](https://dblp.org/pid/43/8092.html#i33) [\[i30\]](https://dblp.org/pid/43/8092.html#i30) [\[i29\]](https://dblp.org/pid/43/8092.html#i29) [\[i28\]](https://dblp.org/pid/43/8092.html#i28) [\[c40\]](https://dblp.org/pid/43/8092.html#c40) [\[c38\]](https://dblp.org/pid/43/8092.html#c38) [\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[c36\]](https://dblp.org/pid/43/8092.html#c36) [\[e2\]](https://dblp.org/pid/43/8092.html#e2) [\[i26\]](https://dblp.org/pid/43/8092.html#i26) [\[i25\]](https://dblp.org/pid/43/8092.html#i25) [\[i24\]](https://dblp.org/pid/43/8092.html#i24) [\[i23\]](https://dblp.org/pid/43/8092.html#i23) [\[j10\]](https://dblp.org/pid/43/8092.html#j10) [\[c35\]](https://dblp.org/pid/43/8092.html#c35) [\[c34\]](https://dblp.org/pid/43/8092.html#c34) [\[e1\]](https://dblp.org/pid/43/8092.html#e1) [\[i22\]](https://dblp.org/pid/43/8092.html#i22) [\[i21\]](https://dblp.org/pid/43/8092.html#i21) [\[i19\]](https://dblp.org/pid/43/8092.html#i19) [\[j9\]](https://dblp.org/pid/43/8092.html#j9) [\[j8\]](https://dblp.org/pid/43/8092.html#j8) [\[i15\]](https://dblp.org/pid/43/8092.html#i15) [\[i14\]](https://dblp.org/pid/43/8092.html#i14) [\[i13\]](https://dblp.org/pid/43/8092.html#i13) [\[j6\]](https://dblp.org/pid/43/8092.html#j6) [\[j4\]](https://dblp.org/pid/43/8092.html#j4) [\[c30\]](https://dblp.org/pid/43/8092.html#c30) [\[c29\]](https://dblp.org/pid/43/8092.html#c29) [\[i10\]](https://dblp.org/pid/43/8092.html#i10) [\[i9\]](https://dblp.org/pid/43/8092.html#i9) [\[i8\]](https://dblp.org/pid/43/8092.html#i8) [\[i6\]](https://dblp.org/pid/43/8092.html#i6) [\[c27\]](https://dblp.org/pid/43/8092.html#c27) [\[c26\]](https://dblp.org/pid/43/8092.html#c26) [\[c25\]](https://dblp.org/pid/43/8092.html#c25) [\[c22\]](https://dblp.org/pid/43/8092.html#c22) [\[i1\]](https://dblp.org/pid/43/8092.html#i1) [\[j3\]](https://dblp.org/pid/43/8092.html#j3) [\[c19\]](https://dblp.org/pid/43/8092.html#c19) [\[c18\]](https://dblp.org/pid/43/8092.html#c18) [\[j1\]](https://dblp.org/pid/43/8092.html#j1) [\[c15\]](https://dblp.org/pid/43/8092.html#c15) [\[c12\]](https://dblp.org/pid/43/8092.html#c12) [\[c11\]](https://dblp.org/pid/43/8092.html#c11) [\[c10\]](https://dblp.org/pid/43/8092.html#c10)

[79](https://dblp.org/pid/43/8092.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Yunjia Lei](https://dblp.org/pid/330/5177.html)

[\[j20\]](https://dblp.org/pid/43/8092.html#j20)

[80](https://dblp.org/pid/43/8092.html?view=joint&param=80 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=3)

[Qinghua Li](https://dblp.org/pid/34/4755.html)

[\[c54\]](https://dblp.org/pid/43/8092.html#c54)

[81](https://dblp.org/pid/43/8092.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Xi Li 0003](https://dblp.org/pid/46/2311-3.html)

[\[i68\]](https://dblp.org/pid/43/8092.html#i68)

[82](https://dblp.org/pid/43/8092.html?view=joint&param=82 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=2)

[Xiang Li 0092](https://dblp.org/pid/40/1491-92.html)

[\[j16\]](https://dblp.org/pid/43/8092.html#j16)

[83](https://dblp.org/pid/43/8092.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Xin Li 0005](https://dblp.org/pid/09/1365-5.html)

[\[j35\]](https://dblp.org/pid/43/8092.html#j35) [\[j34\]](https://dblp.org/pid/43/8092.html#j34) [\[j33\]](https://dblp.org/pid/43/8092.html#j33) [\[j31\]](https://dblp.org/pid/43/8092.html#j31) [\[j29\]](https://dblp.org/pid/43/8092.html#j29) [\[i98\]](https://dblp.org/pid/43/8092.html#i98) [\[c67\]](https://dblp.org/pid/43/8092.html#c67) [\[c64\]](https://dblp.org/pid/43/8092.html#c64) [\[i82\]](https://dblp.org/pid/43/8092.html#i82) [\[i78\]](https://dblp.org/pid/43/8092.html#i78) [\[i76\]](https://dblp.org/pid/43/8092.html#i76) [\[c59\]](https://dblp.org/pid/43/8092.html#c59) [\[c58\]](https://dblp.org/pid/43/8092.html#c58) [\[i66\]](https://dblp.org/pid/43/8092.html#i66) [\[i64\]](https://dblp.org/pid/43/8092.html#i64) [\[i62\]](https://dblp.org/pid/43/8092.html#i62) [\[i60\]](https://dblp.org/pid/43/8092.html#i60) [\[i54\]](https://dblp.org/pid/43/8092.html#i54) [\[i52\]](https://dblp.org/pid/43/8092.html#i52) [\[i49\]](https://dblp.org/pid/43/8092.html#i49) [\[c51\]](https://dblp.org/pid/43/8092.html#c51) [\[i45\]](https://dblp.org/pid/43/8092.html#i45)

[84](https://dblp.org/pid/43/8092.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Yi Liang](https://dblp.org/pid/23/6696.html)

[\[c50\]](https://dblp.org/pid/43/8092.html#c50) [\[i41\]](https://dblp.org/pid/43/8092.html#i41)

[85](https://dblp.org/pid/43/8092.html?view=joint&param=85 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=2)

[Jianzheng Liu](https://dblp.org/pid/169/7220.html)

[\[j16\]](https://dblp.org/pid/43/8092.html#j16)

[86](https://dblp.org/pid/43/8092.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Suxing Liu](https://dblp.org/pid/59/7086.html)

[\[i88\]](https://dblp.org/pid/43/8092.html#i88)

[87](https://dblp.org/pid/43/8092.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Xudong Liu 0006](https://dblp.org/pid/90/2144-6.html)

[\[i54\]](https://dblp.org/pid/43/8092.html#i54)

[88](https://dblp.org/pid/43/8092.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Rishi Madhok](https://dblp.org/pid/216/7116.html)

[\[j32\]](https://dblp.org/pid/43/8092.html#j32)

[89](https://dblp.org/pid/43/8092.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Diana Mateus](https://dblp.org/pid/55/6754.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[90](https://dblp.org/pid/43/8092.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Charlotte McCormick](https://dblp.org/pid/393/5022.html)

[\[i99\]](https://dblp.org/pid/43/8092.html#i99) [\[i69\]](https://dblp.org/pid/43/8092.html#i69)

[91](https://dblp.org/pid/43/8092.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Connor McCurtain](https://dblp.org/pid/397/9089.html)

[\[i99\]](https://dblp.org/pid/43/8092.html#i99)

[92](https://dblp.org/pid/43/8092.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Fausto Milletari](https://dblp.org/pid/134/9886.html)

[\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[93](https://dblp.org/pid/43/8092.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Braeden Morgan](https://dblp.org/pid/376/0612.html)

[\[c61\]](https://dblp.org/pid/43/8092.html#c61) [\[i84\]](https://dblp.org/pid/43/8092.html#i84)

[94](https://dblp.org/pid/43/8092.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Ahmed Moustafa](https://dblp.org/pid/117/1672.html)

[\[c69\]](https://dblp.org/pid/43/8092.html#c69) [\[i36\]](https://dblp.org/pid/43/8092.html#i36)

[95](https://dblp.org/pid/43/8092.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Leslie Neely](https://dblp.org/pid/286/1228.html)

[\[i85\]](https://dblp.org/pid/43/8092.html#i85)

[96](https://dblp.org/pid/43/8092.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Alexander Nelson 0001](https://dblp.org/pid/140/7986-1.html)

aka: Alexander H. Nelson 0001

[\[j33\]](https://dblp.org/pid/43/8092.html#j33) [\[c58\]](https://dblp.org/pid/43/8092.html#c58) [\[i66\]](https://dblp.org/pid/43/8092.html#i66) [\[i60\]](https://dblp.org/pid/43/8092.html#i60)

[97](https://dblp.org/pid/43/8092.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Hien Nguyen](https://dblp.org/pid/26/1622.html)

[\[i46\]](https://dblp.org/pid/43/8092.html#i46)

[98](https://dblp.org/pid/43/8092.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Hien Van Nguyen](https://dblp.org/pid/59/9550.html)

[\[j13\]](https://dblp.org/pid/43/8092.html#j13) [\[c42\]](https://dblp.org/pid/43/8092.html#c42) [\[i33\]](https://dblp.org/pid/43/8092.html#i33) [\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2) [\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[99](https://dblp.org/pid/43/8092.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Hoang Quan Nguyen](https://dblp.org/pid/402/6121.html)

[\[i95\]](https://dblp.org/pid/43/8092.html#i95)

[100](https://dblp.org/pid/43/8092.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Hoang-Quan Nguyen](https://dblp.org/pid/302/3196.html)

[\[j31\]](https://dblp.org/pid/43/8092.html#j31) [\[j28\]](https://dblp.org/pid/43/8092.html#j28) [\[i98\]](https://dblp.org/pid/43/8092.html#i98) [\[i93\]](https://dblp.org/pid/43/8092.html#i93) [\[i92\]](https://dblp.org/pid/43/8092.html#i92) [\[j24\]](https://dblp.org/pid/43/8092.html#j24) [\[c67\]](https://dblp.org/pid/43/8092.html#c67) [\[c62\]](https://dblp.org/pid/43/8092.html#c62) [\[c60\]](https://dblp.org/pid/43/8092.html#c60) [\[i83\]](https://dblp.org/pid/43/8092.html#i83) [\[i81\]](https://dblp.org/pid/43/8092.html#i81) [\[i80\]](https://dblp.org/pid/43/8092.html#i80) [\[i79\]](https://dblp.org/pid/43/8092.html#i79) [\[i75\]](https://dblp.org/pid/43/8092.html#i75) [\[i70\]](https://dblp.org/pid/43/8092.html#i70) [\[c55\]](https://dblp.org/pid/43/8092.html#c55) [\[i57\]](https://dblp.org/pid/43/8092.html#i57) [\[i52\]](https://dblp.org/pid/43/8092.html#i52)

[101](https://dblp.org/pid/43/8092.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Manh Nguyen 0002](https://dblp.org/pid/242/6386-2.html)

[\[c36\]](https://dblp.org/pid/43/8092.html#c36) [\[i24\]](https://dblp.org/pid/43/8092.html#i24)

[102](https://dblp.org/pid/43/8092.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Nghia Nguyen](https://dblp.org/pid/230/7933.html)

[\[c34\]](https://dblp.org/pid/43/8092.html#c34) [\[i15\]](https://dblp.org/pid/43/8092.html#i15) [\[i14\]](https://dblp.org/pid/43/8092.html#i14)

[103](https://dblp.org/pid/43/8092.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Pha Nguyen](https://dblp.org/pid/398/0197.html)

[\[c71\]](https://dblp.org/pid/43/8092.html#c71) [\[i91\]](https://dblp.org/pid/43/8092.html#i91)

[104](https://dblp.org/pid/43/8092.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Pha A. Nguyen](https://dblp.org/pid/270/6213.html)

[\[j33\]](https://dblp.org/pid/43/8092.html#j33) [\[j32\]](https://dblp.org/pid/43/8092.html#j32) [\[j26\]](https://dblp.org/pid/43/8092.html#j26) [\[j25\]](https://dblp.org/pid/43/8092.html#j25) [\[j23\]](https://dblp.org/pid/43/8092.html#j23) [\[c68\]](https://dblp.org/pid/43/8092.html#c68) [\[c66\]](https://dblp.org/pid/43/8092.html#c66) [\[c65\]](https://dblp.org/pid/43/8092.html#c65) [\[c64\]](https://dblp.org/pid/43/8092.html#c64) [\[i78\]](https://dblp.org/pid/43/8092.html#i78) [\[i73\]](https://dblp.org/pid/43/8092.html#i73) [\[i67\]](https://dblp.org/pid/43/8092.html#i67) [\[c58\]](https://dblp.org/pid/43/8092.html#c58) [\[c56\]](https://dblp.org/pid/43/8092.html#c56) [\[i66\]](https://dblp.org/pid/43/8092.html#i66) [\[i60\]](https://dblp.org/pid/43/8092.html#i60) [\[i59\]](https://dblp.org/pid/43/8092.html#i59) [\[i56\]](https://dblp.org/pid/43/8092.html#i56) [\[i55\]](https://dblp.org/pid/43/8092.html#i55) [\[i50\]](https://dblp.org/pid/43/8092.html#i50) [\[i48\]](https://dblp.org/pid/43/8092.html#i48) [\[i47\]](https://dblp.org/pid/43/8092.html#i47) [\[c52\]](https://dblp.org/pid/43/8092.html#c52) [\[c50\]](https://dblp.org/pid/43/8092.html#c50) [\[i44\]](https://dblp.org/pid/43/8092.html#i44) [\[i41\]](https://dblp.org/pid/43/8092.html#i41) [\[i39\]](https://dblp.org/pid/43/8092.html#i39) [\[i37\]](https://dblp.org/pid/43/8092.html#i37) [\[c46\]](https://dblp.org/pid/43/8092.html#c46) [\[i31\]](https://dblp.org/pid/43/8092.html#i31)

[105](https://dblp.org/pid/43/8092.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Phat Nguyen](https://dblp.org/pid/225/8229.html)

[\[c53\]](https://dblp.org/pid/43/8092.html#c53) [\[i34\]](https://dblp.org/pid/43/8092.html#i34)

[106](https://dblp.org/pid/43/8092.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Phong X. Nguyen](https://dblp.org/pid/332/2436.html)

[\[c53\]](https://dblp.org/pid/43/8092.html#c53) [\[i34\]](https://dblp.org/pid/43/8092.html#i34)

[107](https://dblp.org/pid/43/8092.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Tien-Phat Nguyen](https://dblp.org/pid/271/7464.html)

[\[c66\]](https://dblp.org/pid/43/8092.html#c66) [\[i56\]](https://dblp.org/pid/43/8092.html#i56)

[108](https://dblp.org/pid/43/8092.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Trong-Thuan Nguyen](https://dblp.org/pid/344/5384.html)

[\[c71\]](https://dblp.org/pid/43/8092.html#c71) [\[i91\]](https://dblp.org/pid/43/8092.html#i91) [\[c68\]](https://dblp.org/pid/43/8092.html#c68) [\[c64\]](https://dblp.org/pid/43/8092.html#c64) [\[i78\]](https://dblp.org/pid/43/8092.html#i78) [\[i67\]](https://dblp.org/pid/43/8092.html#i67) [\[i48\]](https://dblp.org/pid/43/8092.html#i48)

[109](https://dblp.org/pid/43/8092.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Xuan-Bac Nguyen](https://dblp.org/pid/260/3161.html)

[\[j35\]](https://dblp.org/pid/43/8092.html#j35) [\[j34\]](https://dblp.org/pid/43/8092.html#j34) [\[j31\]](https://dblp.org/pid/43/8092.html#j31) [\[j29\]](https://dblp.org/pid/43/8092.html#j29) [\[j28\]](https://dblp.org/pid/43/8092.html#j28) [\[i98\]](https://dblp.org/pid/43/8092.html#i98) [\[i93\]](https://dblp.org/pid/43/8092.html#i93) [\[i92\]](https://dblp.org/pid/43/8092.html#i92) [\[i87\]](https://dblp.org/pid/43/8092.html#i87) [\[i86\]](https://dblp.org/pid/43/8092.html#i86) [\[j27\]](https://dblp.org/pid/43/8092.html#j27) [\[j24\]](https://dblp.org/pid/43/8092.html#j24) [\[c67\]](https://dblp.org/pid/43/8092.html#c67) [\[c62\]](https://dblp.org/pid/43/8092.html#c62) [\[c60\]](https://dblp.org/pid/43/8092.html#c60) [\[i85\]](https://dblp.org/pid/43/8092.html#i85) [\[i82\]](https://dblp.org/pid/43/8092.html#i82) [\[i81\]](https://dblp.org/pid/43/8092.html#i81) [\[i80\]](https://dblp.org/pid/43/8092.html#i80) [\[i79\]](https://dblp.org/pid/43/8092.html#i79) [\[i75\]](https://dblp.org/pid/43/8092.html#i75) [\[i74\]](https://dblp.org/pid/43/8092.html#i74) [\[i70\]](https://dblp.org/pid/43/8092.html#i70) [\[i68\]](https://dblp.org/pid/43/8092.html#i68) [\[c59\]](https://dblp.org/pid/43/8092.html#c59) [\[i64\]](https://dblp.org/pid/43/8092.html#i64) [\[i61\]](https://dblp.org/pid/43/8092.html#i61) [\[i54\]](https://dblp.org/pid/43/8092.html#i54) [\[i53\]](https://dblp.org/pid/43/8092.html#i53) [\[i52\]](https://dblp.org/pid/43/8092.html#i52) [\[i49\]](https://dblp.org/pid/43/8092.html#i49) [\[c52\]](https://dblp.org/pid/43/8092.html#c52) [\[c48\]](https://dblp.org/pid/43/8092.html#c48) [\[i44\]](https://dblp.org/pid/43/8092.html#i44) [\[i43\]](https://dblp.org/pid/43/8092.html#i43) [\[i42\]](https://dblp.org/pid/43/8092.html#i42) [\[c47\]](https://dblp.org/pid/43/8092.html#c47)

[110](https://dblp.org/pid/43/8092.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Eneko Osaba](https://dblp.org/pid/47/10138.html)

[\[i100\]](https://dblp.org/pid/43/8092.html#i100) [\[i96\]](https://dblp.org/pid/43/8092.html#i96)

[111](https://dblp.org/pid/43/8092.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Dipan K. Pal](https://dblp.org/pid/148/1005.html)

[\[i8\]](https://dblp.org/pid/43/8092.html#i8)

[112](https://dblp.org/pid/43/8092.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Sankalp Pandey](https://dblp.org/pid/412/8073.html)

[\[i93\]](https://dblp.org/pid/43/8092.html#i93) [\[i92\]](https://dblp.org/pid/43/8092.html#i92) [\[i87\]](https://dblp.org/pid/43/8092.html#i87)

[113](https://dblp.org/pid/43/8092.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Se-Woong Park](https://dblp.org/pid/94/411.html)

[\[i85\]](https://dblp.org/pid/43/8092.html#i85)

[114](https://dblp.org/pid/43/8092.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Vishal M. Patel](https://dblp.org/pid/86/4726-1.html)

aka: Vishal Patel 0001

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2) [\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[115](https://dblp.org/pid/43/8092.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Matthew J. Patitz](https://dblp.org/pid/31/4769.html)

[\[j12\]](https://dblp.org/pid/43/8092.html#j12)

[116](https://dblp.org/pid/43/8092.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Eric Patterson](https://dblp.org/pid/79/1282.html)

[\[c34\]](https://dblp.org/pid/43/8092.html#c34) [\[i14\]](https://dblp.org/pid/43/8092.html#i14)

[117](https://dblp.org/pid/43/8092.html?view=joint&param=117 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=2)

[Eric K. Patterson](https://dblp.org/pid/93/9217.html)

[\[j16\]](https://dblp.org/pid/43/8092.html#j16)

[118](https://dblp.org/pid/43/8092.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Hoang-Anh Pham](https://dblp.org/pid/54/7957.html)

aka: Hoang Anh Pham

[\[c44\]](https://dblp.org/pid/43/8092.html#c44) [\[i30\]](https://dblp.org/pid/43/8092.html#i30)

[119](https://dblp.org/pid/43/8092.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Phuoc-Sang Pham](https://dblp.org/pid/387/6533.html)

[\[i97\]](https://dblp.org/pid/43/8092.html#i97)

[120](https://dblp.org/pid/43/8092.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Minh-Hieu Phan](https://dblp.org/pid/268/1849.html)

[\[j18\]](https://dblp.org/pid/43/8092.html#j18)

[121](https://dblp.org/pid/43/8092.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Thinh Phan](https://dblp.org/pid/331/3164.html)

[\[c66\]](https://dblp.org/pid/43/8092.html#c66) [\[i56\]](https://dblp.org/pid/43/8092.html#i56)

[122](https://dblp.org/pid/43/8092.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Son Lam Phung](https://dblp.org/pid/93/737.html)

[\[j25\]](https://dblp.org/pid/43/8092.html#j25) [\[i63\]](https://dblp.org/pid/43/8092.html#i63) [\[j20\]](https://dblp.org/pid/43/8092.html#j20) [\[j18\]](https://dblp.org/pid/43/8092.html#j18) [\[c51\]](https://dblp.org/pid/43/8092.html#c51) [\[i45\]](https://dblp.org/pid/43/8092.html#i45) [\[i37\]](https://dblp.org/pid/43/8092.html#i37) [\[c43\]](https://dblp.org/pid/43/8092.html#c43) [\[i29\]](https://dblp.org/pid/43/8092.html#i29)

[123](https://dblp.org/pid/43/8092.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Utsav Prabhu](https://dblp.org/pid/54/10072.html)

[\[c72\]](https://dblp.org/pid/43/8092.html#c72) [\[c63\]](https://dblp.org/pid/43/8092.html#c63) [\[i77\]](https://dblp.org/pid/43/8092.html#i77) [\[i51\]](https://dblp.org/pid/43/8092.html#i51) [\[c10\]](https://dblp.org/pid/43/8092.html#c10)

[124](https://dblp.org/pid/43/8092.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Kha Gia Quach](https://dblp.org/pid/73/11111.html)

[\[j25\]](https://dblp.org/pid/43/8092.html#j25) [\[j22\]](https://dblp.org/pid/43/8092.html#j22) [\[c56\]](https://dblp.org/pid/43/8092.html#c56) [\[i59\]](https://dblp.org/pid/43/8092.html#i59) [\[i55\]](https://dblp.org/pid/43/8092.html#i55) [\[j17\]](https://dblp.org/pid/43/8092.html#j17) [\[c52\]](https://dblp.org/pid/43/8092.html#c52) [\[i44\]](https://dblp.org/pid/43/8092.html#i44) [\[i39\]](https://dblp.org/pid/43/8092.html#i39) [\[i37\]](https://dblp.org/pid/43/8092.html#i37) [\[c46\]](https://dblp.org/pid/43/8092.html#c46) [\[i31\]](https://dblp.org/pid/43/8092.html#i31) [\[c39\]](https://dblp.org/pid/43/8092.html#c39) [\[i27\]](https://dblp.org/pid/43/8092.html#i27) [\[i26\]](https://dblp.org/pid/43/8092.html#i26) [\[i25\]](https://dblp.org/pid/43/8092.html#i25) [\[j11\]](https://dblp.org/pid/43/8092.html#j11) [\[j10\]](https://dblp.org/pid/43/8092.html#j10) [\[c35\]](https://dblp.org/pid/43/8092.html#c35) [\[c34\]](https://dblp.org/pid/43/8092.html#c34) [\[i21\]](https://dblp.org/pid/43/8092.html#i21) [\[j9\]](https://dblp.org/pid/43/8092.html#j9) [\[j8\]](https://dblp.org/pid/43/8092.html#j8) [\[c31\]](https://dblp.org/pid/43/8092.html#c31) [\[i17\]](https://dblp.org/pid/43/8092.html#i17) [\[i15\]](https://dblp.org/pid/43/8092.html#i15) [\[i14\]](https://dblp.org/pid/43/8092.html#i14) [\[i13\]](https://dblp.org/pid/43/8092.html#i13) [\[j7\]](https://dblp.org/pid/43/8092.html#j7) [\[c30\]](https://dblp.org/pid/43/8092.html#c30) [\[c29\]](https://dblp.org/pid/43/8092.html#c29) [\[i10\]](https://dblp.org/pid/43/8092.html#i10) [\[i9\]](https://dblp.org/pid/43/8092.html#i9) [\[i6\]](https://dblp.org/pid/43/8092.html#i6) [\[c24\]](https://dblp.org/pid/43/8092.html#c24) [\[c23\]](https://dblp.org/pid/43/8092.html#c23) [\[c21\]](https://dblp.org/pid/43/8092.html#c21) [\[i5\]](https://dblp.org/pid/43/8092.html#i5) [\[i3\]](https://dblp.org/pid/43/8092.html#i3) [\[i2\]](https://dblp.org/pid/43/8092.html#i2) [\[c20\]](https://dblp.org/pid/43/8092.html#c20) [\[c8\]](https://dblp.org/pid/43/8092.html#c8)

[125](https://dblp.org/pid/43/8092.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Kyle Quinn](https://dblp.org/pid/317/2546.html)

[\[i46\]](https://dblp.org/pid/43/8092.html#i46)

[126](https://dblp.org/pid/43/8092.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Chase Rainwater](https://dblp.org/pid/57/6270.html)

[\[j21\]](https://dblp.org/pid/43/8092.html#j21) [\[c49\]](https://dblp.org/pid/43/8092.html#c49) [\[i40\]](https://dblp.org/pid/43/8092.html#i40) [\[c43\]](https://dblp.org/pid/43/8092.html#c43) [\[i29\]](https://dblp.org/pid/43/8092.html#i29)

[127](https://dblp.org/pid/43/8092.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Bhiksha Raj](https://dblp.org/pid/60/3996.html)

[\[j32\]](https://dblp.org/pid/43/8092.html#j32) [\[c72\]](https://dblp.org/pid/43/8092.html#c72) [\[i89\]](https://dblp.org/pid/43/8092.html#i89) [\[c63\]](https://dblp.org/pid/43/8092.html#c63) [\[i77\]](https://dblp.org/pid/43/8092.html#i77) [\[i76\]](https://dblp.org/pid/43/8092.html#i76) [\[i72\]](https://dblp.org/pid/43/8092.html#i72) [\[c57\]](https://dblp.org/pid/43/8092.html#c57) [\[c55\]](https://dblp.org/pid/43/8092.html#c55) [\[i65\]](https://dblp.org/pid/43/8092.html#i65) [\[i57\]](https://dblp.org/pid/43/8092.html#i57) [\[i55\]](https://dblp.org/pid/43/8092.html#i55) [\[i51\]](https://dblp.org/pid/43/8092.html#i51) [\[c44\]](https://dblp.org/pid/43/8092.html#c44) [\[i30\]](https://dblp.org/pid/43/8092.html#i30)

[128](https://dblp.org/pid/43/8092.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Vidhiwar Singh Rathour](https://dblp.org/pid/286/5747.html)

[\[j19\]](https://dblp.org/pid/43/8092.html#j19) [\[i28\]](https://dblp.org/pid/43/8092.html#i28)

[129](https://dblp.org/pid/43/8092.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Karl Ricanek](https://dblp.org/pid/39/609.html)

[\[i13\]](https://dblp.org/pid/43/8092.html#i13) [\[c6\]](https://dblp.org/pid/43/8092.html#c6) [\[c2\]](https://dblp.org/pid/43/8092.html#c2) [\[c1\]](https://dblp.org/pid/43/8092.html#c1)

[130](https://dblp.org/pid/43/8092.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Nicola Rieke](https://dblp.org/pid/149/7726.html)

[\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[131](https://dblp.org/pid/43/8092.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Lydia Rockers](https://dblp.org/pid/371/4142.html)

[\[i85\]](https://dblp.org/pid/43/8092.html#i85)

[132](https://dblp.org/pid/43/8092.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Kaushik Roy 0003](https://dblp.org/pid/r/KaushikRoy3.html)

[\[i61\]](https://dblp.org/pid/43/8092.html#i61) [\[j17\]](https://dblp.org/pid/43/8092.html#j17) [\[c41\]](https://dblp.org/pid/43/8092.html#c41) [\[c39\]](https://dblp.org/pid/43/8092.html#c39) [\[i27\]](https://dblp.org/pid/43/8092.html#i27)

[133](https://dblp.org/pid/43/8092.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Badrinath Roysam](https://dblp.org/pid/r/BRoysam.html)

aka: Badri Roysam

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2) [\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[134](https://dblp.org/pid/43/8092.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Ilya Safro](https://dblp.org/pid/64/5096.html)

[\[i92\]](https://dblp.org/pid/43/8092.html#i92)

[135](https://dblp.org/pid/43/8092.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Marios Savvides](https://dblp.org/pid/13/3793.html)

[\[i61\]](https://dblp.org/pid/43/8092.html#i61) [\[j19\]](https://dblp.org/pid/43/8092.html#j19) [\[i38\]](https://dblp.org/pid/43/8092.html#i38) [\[i28\]](https://dblp.org/pid/43/8092.html#i28) [\[c38\]](https://dblp.org/pid/43/8092.html#c38) [\[i23\]](https://dblp.org/pid/43/8092.html#i23) [\[j10\]](https://dblp.org/pid/43/8092.html#j10) [\[j9\]](https://dblp.org/pid/43/8092.html#j9) [\[j8\]](https://dblp.org/pid/43/8092.html#j8) [\[c33\]](https://dblp.org/pid/43/8092.html#c33) [\[c32\]](https://dblp.org/pid/43/8092.html#c32) [\[i16\]](https://dblp.org/pid/43/8092.html#i16) [\[j6\]](https://dblp.org/pid/43/8092.html#j6) [\[j5\]](https://dblp.org/pid/43/8092.html#j5) [\[j4\]](https://dblp.org/pid/43/8092.html#j4) [\[c30\]](https://dblp.org/pid/43/8092.html#c30) [\[c29\]](https://dblp.org/pid/43/8092.html#c29) [\[c28\]](https://dblp.org/pid/43/8092.html#c28) [\[i10\]](https://dblp.org/pid/43/8092.html#i10) [\[i9\]](https://dblp.org/pid/43/8092.html#i9) [\[i8\]](https://dblp.org/pid/43/8092.html#i8) [\[i7\]](https://dblp.org/pid/43/8092.html#i7) [\[i6\]](https://dblp.org/pid/43/8092.html#i6) [\[c27\]](https://dblp.org/pid/43/8092.html#c27) [\[c26\]](https://dblp.org/pid/43/8092.html#c26) [\[c25\]](https://dblp.org/pid/43/8092.html#c25) [\[c22\]](https://dblp.org/pid/43/8092.html#c22) [\[i4\]](https://dblp.org/pid/43/8092.html#i4) [\[i1\]](https://dblp.org/pid/43/8092.html#i1) [\[j3\]](https://dblp.org/pid/43/8092.html#j3) [\[j2\]](https://dblp.org/pid/43/8092.html#j2) [\[c19\]](https://dblp.org/pid/43/8092.html#c19) [\[c18\]](https://dblp.org/pid/43/8092.html#c18) [\[c17\]](https://dblp.org/pid/43/8092.html#c17) [\[c16\]](https://dblp.org/pid/43/8092.html#c16) [\[j1\]](https://dblp.org/pid/43/8092.html#j1) [\[c15\]](https://dblp.org/pid/43/8092.html#c15) [\[c14\]](https://dblp.org/pid/43/8092.html#c14) [\[c13\]](https://dblp.org/pid/43/8092.html#c13) [\[c12\]](https://dblp.org/pid/43/8092.html#c12) [\[c11\]](https://dblp.org/pid/43/8092.html#c11) [\[c10\]](https://dblp.org/pid/43/8092.html#c10) [\[c9\]](https://dblp.org/pid/43/8092.html#c9) [\[c5\]](https://dblp.org/pid/43/8092.html#c5) [\[c4\]](https://dblp.org/pid/43/8092.html#c4)

[136](https://dblp.org/pid/43/8092.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Han-Seok Seo](https://dblp.org/pid/138/6741.html)

[\[j33\]](https://dblp.org/pid/43/8092.html#j33) [\[i85\]](https://dblp.org/pid/43/8092.html#i85) [\[i74\]](https://dblp.org/pid/43/8092.html#i74) [\[c59\]](https://dblp.org/pid/43/8092.html#c59) [\[c58\]](https://dblp.org/pid/43/8092.html#c58) [\[i66\]](https://dblp.org/pid/43/8092.html#i66) [\[i64\]](https://dblp.org/pid/43/8092.html#i64) [\[i60\]](https://dblp.org/pid/43/8092.html#i60) [\[c51\]](https://dblp.org/pid/43/8092.html#c51) [\[i45\]](https://dblp.org/pid/43/8092.html#i45) [\[j14\]](https://dblp.org/pid/43/8092.html#j14)

[137](https://dblp.org/pid/43/8092.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Manuel Serna-Aguilera](https://dblp.org/pid/336/4123.html)

[\[j35\]](https://dblp.org/pid/43/8092.html#j35) [\[i88\]](https://dblp.org/pid/43/8092.html#i88) [\[i85\]](https://dblp.org/pid/43/8092.html#i85) [\[i74\]](https://dblp.org/pid/43/8092.html#i74) [\[i35\]](https://dblp.org/pid/43/8092.html#i35)

[138](https://dblp.org/pid/43/8092.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Keshav Seshadri](https://dblp.org/pid/95/10072.html)

[\[j3\]](https://dblp.org/pid/43/8092.html#j3) [\[c15\]](https://dblp.org/pid/43/8092.html#c15) [\[c12\]](https://dblp.org/pid/43/8092.html#c12) [\[c11\]](https://dblp.org/pid/43/8092.html#c11) [\[c4\]](https://dblp.org/pid/43/8092.html#c4)

[139](https://dblp.org/pid/43/8092.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Matthew Shepard](https://dblp.org/pid/397/9407.html)

[\[i99\]](https://dblp.org/pid/43/8092.html#i99)

[140](https://dblp.org/pid/43/8092.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Wilson Silva](https://dblp.org/pid/228/1570.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[141](https://dblp.org/pid/43/8092.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Asmita Singh](https://dblp.org/pid/371/4265.html)

[\[i85\]](https://dblp.org/pid/43/8092.html#i85)

[142](https://dblp.org/pid/43/8092.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Karanhaar Singh](https://dblp.org/pid/11/10698.html)

[\[c18\]](https://dblp.org/pid/43/8092.html#c18)

[143](https://dblp.org/pid/43/8092.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Pawan Sinha](https://dblp.org/pid/51/6599.html)

[\[j35\]](https://dblp.org/pid/43/8092.html#j35) [\[j34\]](https://dblp.org/pid/43/8092.html#j34) [\[j29\]](https://dblp.org/pid/43/8092.html#j29) [\[i86\]](https://dblp.org/pid/43/8092.html#i86) [\[i82\]](https://dblp.org/pid/43/8092.html#i82) [\[i70\]](https://dblp.org/pid/43/8092.html#i70) [\[i68\]](https://dblp.org/pid/43/8092.html#i68)

[144](https://dblp.org/pid/43/8092.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Tran Thai Son](https://dblp.org/pid/06/5210.html)

aka: Thai-Son Tran

[\[i97\]](https://dblp.org/pid/43/8092.html#i97) [\[i89\]](https://dblp.org/pid/43/8092.html#i89)

[145](https://dblp.org/pid/43/8092.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[James Sorensen](https://dblp.org/pid/312/7241.html)

[\[c42\]](https://dblp.org/pid/43/8092.html#c42)

[146](https://dblp.org/pid/43/8092.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Jeyamkondan Subbiah](https://dblp.org/pid/178/0722.html)

[\[c63\]](https://dblp.org/pid/43/8092.html#c63) [\[i77\]](https://dblp.org/pid/43/8092.html#i77)

[147](https://dblp.org/pid/43/8092.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Ching Y. Suen](https://dblp.org/pid/s/ChingYSuen.html)

[\[j5\]](https://dblp.org/pid/43/8092.html#j5) [\[c9\]](https://dblp.org/pid/43/8092.html#c9) [\[c7\]](https://dblp.org/pid/43/8092.html#c7) [\[c5\]](https://dblp.org/pid/43/8092.html#c5) [\[c4\]](https://dblp.org/pid/43/8092.html#c4) [\[c2\]](https://dblp.org/pid/43/8092.html#c2) [\[c1\]](https://dblp.org/pid/43/8092.html#c1)

[148](https://dblp.org/pid/43/8092.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Raphael Sznitman](https://dblp.org/pid/29/8000.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[149](https://dblp.org/pid/43/8092.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Ran Tao 0013](https://dblp.org/pid/99/955-13.html)

[\[c33\]](https://dblp.org/pid/43/8092.html#c33) [\[i16\]](https://dblp.org/pid/43/8092.html#i16)

[150](https://dblp.org/pid/43/8092.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Benjamin Thompson](https://dblp.org/pid/53/3789.html)

[\[j27\]](https://dblp.org/pid/43/8092.html#j27) [\[i53\]](https://dblp.org/pid/43/8092.html#i53)

[151](https://dblp.org/pid/43/8092.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Anh Tuan Tran 0001](https://dblp.org/pid/150/5269-1.html)

aka: Anh Tran 0001

[\[c45\]](https://dblp.org/pid/43/8092.html#c45) [\[i32\]](https://dblp.org/pid/43/8092.html#i32)

[152](https://dblp.org/pid/43/8092.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Huu-Thien Tran](https://dblp.org/pid/400/4998.html)

[\[c73\]](https://dblp.org/pid/43/8092.html#c73) [\[i97\]](https://dblp.org/pid/43/8092.html#i97) [\[i94\]](https://dblp.org/pid/43/8092.html#i94) [\[i89\]](https://dblp.org/pid/43/8092.html#i89)

[153](https://dblp.org/pid/43/8092.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Kim Hoang Tran](https://dblp.org/pid/348/6627.html)

[\[c66\]](https://dblp.org/pid/43/8092.html#c66) [\[i56\]](https://dblp.org/pid/43/8092.html#i56)

[154](https://dblp.org/pid/43/8092.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Minh Q. Tran](https://dblp.org/pid/281/8723.html)

[\[i46\]](https://dblp.org/pid/43/8092.html#i46)

[155](https://dblp.org/pid/43/8092.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Minh-Triet Tran](https://dblp.org/pid/44/7448.html)

[\[i91\]](https://dblp.org/pid/43/8092.html#i91) [\[j15\]](https://dblp.org/pid/43/8092.html#j15) [\[c46\]](https://dblp.org/pid/43/8092.html#c46) [\[i31\]](https://dblp.org/pid/43/8092.html#i31) [\[c40\]](https://dblp.org/pid/43/8092.html#c40) [\[i22\]](https://dblp.org/pid/43/8092.html#i22) [\[i19\]](https://dblp.org/pid/43/8092.html#i19) [\[i18\]](https://dblp.org/pid/43/8092.html#i18) [\[i12\]](https://dblp.org/pid/43/8092.html#i12)

[156](https://dblp.org/pid/43/8092.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Emanuele Trucco](https://dblp.org/pid/60/1409.html)

[\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2)

[157](https://dblp.org/pid/43/8092.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Dat T. Truong](https://dblp.org/pid/268/3805.html)

[\[c40\]](https://dblp.org/pid/43/8092.html#c40)

[158](https://dblp.org/pid/43/8092.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Sang Truong](https://dblp.org/pid/301/9134.html)

[\[c49\]](https://dblp.org/pid/43/8092.html#c49) [\[i40\]](https://dblp.org/pid/43/8092.html#i40)

[159](https://dblp.org/pid/43/8092.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Thanh-Dat Truong](https://dblp.org/pid/213/5771.html)

[\[j31\]](https://dblp.org/pid/43/8092.html#j31) [\[j30\]](https://dblp.org/pid/43/8092.html#j30) [\[c73\]](https://dblp.org/pid/43/8092.html#c73) [\[c72\]](https://dblp.org/pid/43/8092.html#c72) [\[i98\]](https://dblp.org/pid/43/8092.html#i98) [\[i94\]](https://dblp.org/pid/43/8092.html#i94) [\[i90\]](https://dblp.org/pid/43/8092.html#i90) [\[i89\]](https://dblp.org/pid/43/8092.html#i89) [\[i86\]](https://dblp.org/pid/43/8092.html#i86) [\[c69\]](https://dblp.org/pid/43/8092.html#c69) [\[c67\]](https://dblp.org/pid/43/8092.html#c67) [\[c63\]](https://dblp.org/pid/43/8092.html#c63) [\[i83\]](https://dblp.org/pid/43/8092.html#i83) [\[i77\]](https://dblp.org/pid/43/8092.html#i77) [\[i76\]](https://dblp.org/pid/43/8092.html#i76) [\[j22\]](https://dblp.org/pid/43/8092.html#j22) [\[c57\]](https://dblp.org/pid/43/8092.html#c57) [\[c55\]](https://dblp.org/pid/43/8092.html#c55) [\[i65\]](https://dblp.org/pid/43/8092.html#i65) [\[i63\]](https://dblp.org/pid/43/8092.html#i63) [\[i62\]](https://dblp.org/pid/43/8092.html#i62) [\[i58\]](https://dblp.org/pid/43/8092.html#i58) [\[i57\]](https://dblp.org/pid/43/8092.html#i57) [\[i52\]](https://dblp.org/pid/43/8092.html#i52) [\[i51\]](https://dblp.org/pid/43/8092.html#i51) [\[j21\]](https://dblp.org/pid/43/8092.html#j21) [\[c51\]](https://dblp.org/pid/43/8092.html#c51) [\[c50\]](https://dblp.org/pid/43/8092.html#c50) [\[c48\]](https://dblp.org/pid/43/8092.html#c48) [\[i45\]](https://dblp.org/pid/43/8092.html#i45) [\[i43\]](https://dblp.org/pid/43/8092.html#i43) [\[i41\]](https://dblp.org/pid/43/8092.html#i41) [\[i38\]](https://dblp.org/pid/43/8092.html#i38) [\[i36\]](https://dblp.org/pid/43/8092.html#i36) [\[j15\]](https://dblp.org/pid/43/8092.html#j15) [\[j14\]](https://dblp.org/pid/43/8092.html#j14) [\[c46\]](https://dblp.org/pid/43/8092.html#c46) [\[c44\]](https://dblp.org/pid/43/8092.html#c44) [\[c43\]](https://dblp.org/pid/43/8092.html#c43) [\[i31\]](https://dblp.org/pid/43/8092.html#i31) [\[i30\]](https://dblp.org/pid/43/8092.html#i30) [\[i29\]](https://dblp.org/pid/43/8092.html#i29) [\[c39\]](https://dblp.org/pid/43/8092.html#c39) [\[i27\]](https://dblp.org/pid/43/8092.html#i27) [\[i26\]](https://dblp.org/pid/43/8092.html#i26) [\[i25\]](https://dblp.org/pid/43/8092.html#i25) [\[i22\]](https://dblp.org/pid/43/8092.html#i22) [\[i19\]](https://dblp.org/pid/43/8092.html#i19) [\[i18\]](https://dblp.org/pid/43/8092.html#i18) [\[i12\]](https://dblp.org/pid/43/8092.html#i12)

[160](https://dblp.org/pid/43/8092.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Shreyas Venugopalan](https://dblp.org/pid/70/9171.html)

[\[c17\]](https://dblp.org/pid/43/8092.html#c17)

[161](https://dblp.org/pid/43/8092.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Viet-Khoa Vo-Ho](https://dblp.org/pid/224/1953.html)

aka: Khoa Vo 0001

[\[c53\]](https://dblp.org/pid/43/8092.html#c53) [\[c49\]](https://dblp.org/pid/43/8092.html#c49) [\[i46\]](https://dblp.org/pid/43/8092.html#i46) [\[i40\]](https://dblp.org/pid/43/8092.html#i40) [\[i34\]](https://dblp.org/pid/43/8092.html#i34)

[162](https://dblp.org/pid/43/8092.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[The De Vu](https://dblp.org/pid/192/3667.html)

[\[c44\]](https://dblp.org/pid/43/8092.html#c44) [\[i30\]](https://dblp.org/pid/43/8092.html#i30)

[163](https://dblp.org/pid/43/8092.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Dongyi Wang](https://dblp.org/pid/70/10768.html)

[\[c63\]](https://dblp.org/pid/43/8092.html#c63) [\[i77\]](https://dblp.org/pid/43/8092.html#i77)

[164](https://dblp.org/pid/43/8092.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Qian Wang 0001](https://dblp.org/pid/75/5723-1.html)

[\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[165](https://dblp.org/pid/43/8092.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Yishi Wang](https://dblp.org/pid/15/9606.html)

[\[c6\]](https://dblp.org/pid/43/8092.html#c6)

[166](https://dblp.org/pid/43/8092.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Yiting Xie](https://dblp.org/pid/143/4278.html)

[\[c14\]](https://dblp.org/pid/43/8092.html#c14)

[167](https://dblp.org/pid/43/8092.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Ziyue Xu 0001](https://dblp.org/pid/59/9160-1.html)

[\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[168](https://dblp.org/pid/43/8092.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Kashu Yamazaki](https://dblp.org/pid/280/0133.html)

[\[j19\]](https://dblp.org/pid/43/8092.html#j19) [\[c53\]](https://dblp.org/pid/43/8092.html#c53) [\[c49\]](https://dblp.org/pid/43/8092.html#c49) [\[i40\]](https://dblp.org/pid/43/8092.html#i40) [\[i34\]](https://dblp.org/pid/43/8092.html#i34) [\[i28\]](https://dblp.org/pid/43/8092.html#i28) [\[c38\]](https://dblp.org/pid/43/8092.html#c38) [\[i23\]](https://dblp.org/pid/43/8092.html#i23)

[169](https://dblp.org/pid/43/8092.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c6\]](https://dblp.org/pid/43/8092.html#c6)

[170](https://dblp.org/pid/43/8092.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Alper Yilmaz 0001](https://dblp.org/pid/11/1315-1.html)

[\[c71\]](https://dblp.org/pid/43/8092.html#c71) [\[i91\]](https://dblp.org/pid/43/8092.html#i91) [\[c65\]](https://dblp.org/pid/43/8092.html#c65) [\[c64\]](https://dblp.org/pid/43/8092.html#c64) [\[i78\]](https://dblp.org/pid/43/8092.html#i78) [\[i73\]](https://dblp.org/pid/43/8092.html#i73) [\[i67\]](https://dblp.org/pid/43/8092.html#i67)

[171](https://dblp.org/pid/43/8092.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Yutong Zheng](https://dblp.org/pid/164/0869.html)

[\[c32\]](https://dblp.org/pid/43/8092.html#c32) [\[j4\]](https://dblp.org/pid/43/8092.html#j4) [\[c27\]](https://dblp.org/pid/43/8092.html#c27) [\[c26\]](https://dblp.org/pid/43/8092.html#c26) [\[c25\]](https://dblp.org/pid/43/8092.html#c25) [\[c22\]](https://dblp.org/pid/43/8092.html#c22) [\[i4\]](https://dblp.org/pid/43/8092.html#i4) [\[i1\]](https://dblp.org/pid/43/8092.html#i1)

[172](https://dblp.org/pid/43/8092.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Shaohua Kevin Zhou](https://dblp.org/pid/57/98.html)

aka: S. Kevin Zhou

[\[j13\]](https://dblp.org/pid/43/8092.html#j13) [\[i33\]](https://dblp.org/pid/43/8092.html#i33) [\[c37\]](https://dblp.org/pid/43/8092.html#c37) [\[e2\]](https://dblp.org/pid/43/8092.html#e2) [\[e1\]](https://dblp.org/pid/43/8092.html#e1)

[173](https://dblp.org/pid/43/8092.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Chenchen Zhu](https://dblp.org/pid/50/6994.html)

[\[c33\]](https://dblp.org/pid/43/8092.html#c33) [\[c32\]](https://dblp.org/pid/43/8092.html#c32) [\[i16\]](https://dblp.org/pid/43/8092.html#i16) [\[j6\]](https://dblp.org/pid/43/8092.html#j6) [\[j4\]](https://dblp.org/pid/43/8092.html#j4) [\[c30\]](https://dblp.org/pid/43/8092.html#c30) [\[c28\]](https://dblp.org/pid/43/8092.html#c28) [\[i9\]](https://dblp.org/pid/43/8092.html#i9) [\[i7\]](https://dblp.org/pid/43/8092.html#i7) [\[c27\]](https://dblp.org/pid/43/8092.html#c27) [\[c26\]](https://dblp.org/pid/43/8092.html#c26) [\[c25\]](https://dblp.org/pid/43/8092.html#c25) [\[c22\]](https://dblp.org/pid/43/8092.html#c22) [\[i4\]](https://dblp.org/pid/43/8092.html#i4) [\[i1\]](https://dblp.org/pid/43/8092.html#i1) [\[c16\]](https://dblp.org/pid/43/8092.html#c16)

[174](https://dblp.org/pid/43/8092.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/43/8092.html?view=group&param=1)

[Min Zou](https://dblp.org/pid/97/2960.html)

[\[i35\]](https://dblp.org/pid/43/8092.html#i35)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/43/8092.html#) [\[–\]](https://dblp.org/pid/43/8092.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/43/8092.html#) [\[–\]](https://dblp.org/pid/43/8092.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/43/8092.html#) [\[–\]](https://dblp.org/pid/43/8092.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/43/8092.html#) [\[–\]](https://dblp.org/pid/43/8092.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/43/8092.html#) [\[–\]](https://dblp.org/pid/43/8092.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)