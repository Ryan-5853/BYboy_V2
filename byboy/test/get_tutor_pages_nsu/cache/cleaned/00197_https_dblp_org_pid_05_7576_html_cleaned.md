> 抓取来源：https://dblp.org/pid/05/7576.html

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

- _affiliation:_ Mahidol University, Nakhon Pathom, Thailand

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Worapan+Kusakunniran%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F05%2F7576%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Worapan+Kusakunniran+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F05%2F7576%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Worapan+Kusakunniran+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F05%2F7576%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Worapan+Kusakunniran%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F05%2F7576%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Worapan+Kusakunniran+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F05%2F7576%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Worapan+Kusakunniran%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F05%2F7576%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Worapan+Kusakunniran%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F05%2F7576%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F05%2F7576%3E+%7D+.%0A%0A%7D)

_showing all81 records_

20092026102009: 32010: 22011: 22012: 32013: 22013: 22014: 32015: 22017: 32018: 132018: 132019: 22019: 22020: 82020: 82021: 72022: 82022: 82023: 62023: 62024: 92024: 92025: 52026: 3

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

- ![](https://dblp.org/img/add-mark.12x12.png)Jian Zhang 0002 (23)
- ![](https://dblp.org/img/add-mark.12x12.png)Qiang Wu 0001 (22)
- ![](https://dblp.org/img/add-mark.12x12.png)Hongdong Li (12)
- ![](https://dblp.org/img/add-mark.12x12.png)Kittikhun Thongkanchorn (12)
- ![](https://dblp.org/img/add-mark.12x12.png)Thanandon Imaromkul (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Thanongchai Siriapisith (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Panrasee Ritthipravat (8)
- ![](https://dblp.org/img/add-mark.12x12.png)Peter Haddawy (8)
- ![](https://dblp.org/img/add-mark.12x12.png)Lingxiang Yao (8)
- ![](https://dblp.org/img/add-mark.12x12.png)Sarattha Kanchanapreechakorn (7)

- _102 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)0000-0002-2896-611X (45)
- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (36)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)PeerJ Comput. Sci. (6)
- ![](https://dblp.org/img/add-mark.12x12.png)TENCON (6)
- ![](https://dblp.org/img/add-mark.12x12.png)DICTA (6)
- ![](https://dblp.org/img/add-mark.12x12.png)Intell. Syst. Appl. (5)
- ![](https://dblp.org/img/add-mark.12x12.png)KST (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Multim. Tools Appl. (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Biol. Medicine (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Medical Biol. Eng. Comput. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Inf. Forensics Secur. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Mach. Intell. Res. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)ICPR (2)

- _31 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (65)
- ![](https://dblp.org/img/add-mark.12x12.png)open (16)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[j49\]
[Javad Khodadoust](https://dblp.org/pid/198/7056.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Raúl Monroy](https://dblp.org/pid/m/RaulMonroy.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Miguel Angel Medina-Pérez](https://dblp.org/pid/87/5148.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Emanuela Marasco](https://dblp.org/pid/64/7404.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png):

Minutiae-based palm photo recognition using deep neural networks. [Eng. Appl. Artif. Intell.165](https://dblp.org/db/journals/eaai/eaai165.html#journals/eaai/KhodadoustMMMK26): 113366 (2026)
- ![](https://dblp.org/img/n.png)

\[j48\]
[Sirawich Vachmanus](https://dblp.org/pid/278/0854.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wimolsiri Pridasawas](https://dblp.org/pid/421/4877.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Kitti Thamrongaphichartkul](https://dblp.org/pid/380/6731.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Noppanan Phinklao](https://dblp.org/pid/386/4373.html):

AL-ViT: Label-efficient Robusta coffee-bean defect detection in Thailand using active learning vision transformers. [Intell. Syst. Appl.29](https://dblp.org/db/journals/iswa/iswa29.html#journals/iswa/VachmanusPKTP26): 200612 (2026)
- ![](https://dblp.org/img/n.png)

\[j47\]
[Javad Khodadoust](https://dblp.org/pid/198/7056.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Raúl Monroy](https://dblp.org/pid/m/RaulMonroy.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Miguel Angel Medina-Pérez](https://dblp.org/pid/87/5148.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Ali Mohammad Khodadoust](https://dblp.org/pid/198/7087.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A multibiometric system based on finger photo and palm photo. [Multim. Tools Appl.85(2)](https://dblp.org/db/journals/mta/mta85.html#journals/mta/KhodadoustMMKK26): 168 (2026)
- 2025
- ![](https://dblp.org/img/n.png)

\[j46\]
[Sai Thu Ya Aung](https://dblp.org/pid/393/8474.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Yew Kwang Hooi](https://dblp.org/pid/141/5757.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Leveraging Fusion Methods of Human Pose and Motion Dynamics for Accurate Violence Detection in Video Surveillance. [IEEE Access13](https://dblp.org/db/journals/access/access13.html#journals/access/AungKH25): 168116-168125 (2025)
- ![](https://dblp.org/img/n.png)

\[j45\]
[Kittisak Chotikkakamthorn](https://dblp.org/pid/384/8376.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wen-Nung Lie](https://dblp.org/pid/07/5659.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Panrasee Ritthipravat](https://dblp.org/pid/07/2677.html), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Pimchanok Tuakta](https://dblp.org/pid/316/6452.html), [Paitoon Benjapornlert](https://dblp.org/pid/316/6517.html):

Medical application of deep-learning-based head pose estimation from RGB image sequence. [Comput. Biol. Medicine195](https://dblp.org/db/journals/cbm/cbm195.html#journals/cbm/ChotikkakamthornLRKTB25): 110620 (2025)
- ![](https://dblp.org/img/n.png)

\[j44\]
[Akara Supratak](https://dblp.org/pid/155/7090.html), [Siripra Kingchan](https://dblp.org/pid/329/7524.html), [Phuriwat Angkoondittaphong](https://dblp.org/pid/414/0257.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Poonsuta Nava-apisak](https://dblp.org/pid/413/9803.html), [Jitsupa Wongsripuemtet](https://dblp.org/pid/414/0268.html), [Thanapon Noraset](https://dblp.org/pid/151/3092.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Peter Haddawy](https://dblp.org/pid/h/PeterHaddawy.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dittapong Songsaeng](https://dblp.org/pid/328/2181.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Normal Pressure Hydrocephalus Classification using Weakly-Supervised Local Feature Extraction. [Comput. Biol. Medicine196](https://dblp.org/db/journals/cbm/cbm196.html#journals/cbm/SupratakKANWNKHS25): 110751 (2025)
- ![](https://dblp.org/img/n.png)

\[j43\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Thanandon Imaromkul](https://dblp.org/pid/244/5576.html), [Kittinun Aukkapinyo](https://dblp.org/pid/271/3524.html), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pimpinan Somsong](https://dblp.org/pid/375/3959.html), [Pimsiri Tiyayon](https://dblp.org/pid/408/3285.html):

Detection of translucent flesh disorder and automatic grading of mangosteens in multi-view images. [Neural Comput. Appl.37(18)](https://dblp.org/db/journals/nca/nca37.html#journals/nca/KusakunniranIATST25): 12103-12121 (2025)
- ![](https://dblp.org/img/n.png)

\[j42\]
[Kittin Thongsrimoung](https://dblp.org/pid/425/6191.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Kontawat Wisetpaitoon](https://dblp.org/pid/377/4052.html), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Terdsak Yano](https://dblp.org/pid/425/6980.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Weerapong Thanapongtharm](https://dblp.org/pid/288/4253.html), [Khemmapat Boonyo](https://dblp.org/pid/425/6624.html):

Sow posture detection for determining piglet crushing through a camera system. [PeerJ Comput. Sci.11](https://dblp.org/db/journals/peerj-cs/peerj-cs11.html#journals/peerj-cs/ThongsrimoungKWTYTB25): e3400 (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j41\]
[Rangwan Kasantikul](https://dblp.org/pid/195/9444.html), Worapan Kusakunniran:

Augmented inputs for surveillance re-identification. [Int. J. Multim. Inf. Retr.13(1)](https://dblp.org/db/journals/ijmir/ijmir13.html#journals/ijmir/KasantikulK24): 2 (2024)
- ![](https://dblp.org/img/n.png)

\[j40\]
[Javad Khodadoust](https://dblp.org/pid/198/7056.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Raúl Monroy](https://dblp.org/pid/m/RaulMonroy.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Miguel Angel Medina-Pérez](https://dblp.org/pid/87/5148.html), [Octavio Loyola-González](https://dblp.org/pid/131/1778.html), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [André Boller](https://dblp.org/pid/294/8809.html), [Philipp Terhörst](https://dblp.org/pid/203/2506.html):

A novel indexing algorithm for latent palmprints leveraging minutiae and orientation field. [Intell. Syst. Appl.21](https://dblp.org/db/journals/iswa/iswa21.html#journals/iswa/KhodadoustMMLKBT24): 200320 (2024)
- ![](https://dblp.org/img/n.png)

\[j39\]
[Kittikan Charoenjai](https://dblp.org/pid/371/3422.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Tipajin Thaipisutikul](https://dblp.org/pid/277/1591.html), [Nutcha Yodrabum](https://dblp.org/pid/345/0964.html), [Irin Chaikangwan](https://dblp.org/pid/371/3596.html):

Automatic detection of nostril and key markers in images. [Intell. Syst. Appl.21](https://dblp.org/db/journals/iswa/iswa21.html#journals/iswa/CharoenjaiKTYC24): 200327 (2024)
- ![](https://dblp.org/img/n.png)

\[j38\]
[Javad Khodadoust](https://dblp.org/pid/198/7056.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Raúl Monroy](https://dblp.org/pid/m/RaulMonroy.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Miguel Angel Medina-Pérez](https://dblp.org/pid/87/5148.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Octavio Loyola-González](https://dblp.org/pid/131/1778.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Vutipong Areekul](https://dblp.org/pid/56/6323.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png):

Enhancing latent palmprints using frequency domain analysis. [Intell. Syst. Appl.23](https://dblp.org/db/journals/iswa/iswa23.html#journals/iswa/KhodadoustMMLAK24): 200414 (2024)
- ![](https://dblp.org/img/n.png)

\[j37\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Thanandon Imaromkul](https://dblp.org/pid/244/5576.html), [Sophon Mongkolluksamee](https://dblp.org/pid/122/4993.html), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Panrasee Ritthipravat](https://dblp.org/pid/07/2677.html), [Pimchanok Tuakta](https://dblp.org/pid/316/6452.html), [Paitoon Benjapornlert](https://dblp.org/pid/316/6517.html):

Deep Upscale U-Net for automatic tongue segmentation. [Medical Biol. Eng. Comput.62(6)](https://dblp.org/db/journals/mbec/mbec62.html#journals/mbec/KusakunniranIMTRTB24): 1751-1762 (2024)
- ![](https://dblp.org/img/n.png)

\[j36\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Thanandon Imaromkul](https://dblp.org/pid/244/5576.html), [Kittinun Aukkapinyo](https://dblp.org/pid/271/3524.html), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pimpinan Somsong](https://dblp.org/pid/375/3959.html):

Automatic classification of mangosteens and ripe status in images using deep learning based approaches. [Multim. Tools Appl.83(16)](https://dblp.org/db/journals/mta/mta83.html#journals/mta/KusakunniranIATS24): 48275-48290 (2024)
- ![](https://dblp.org/img/n.png)

\[j35\]
[Panrasee Ritthipravat](https://dblp.org/pid/07/2677.html), [Kittisak Chotikkakamthorn](https://dblp.org/pid/384/8376.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wen-Nung Lie](https://dblp.org/pid/07/5659.html), Worapan Kusakunniran, [Pimchanok Tuakta](https://dblp.org/pid/316/6452.html), [Paitoon Benjapornlert](https://dblp.org/pid/316/6517.html):

Deep-learning-based head pose estimation from a single RGB image and its application to medical CROM measurement. [Multim. Tools Appl.83(31)](https://dblp.org/db/journals/mta/mta83.html#journals/mta/RitthipravatCLKTB24): 77009-77028 (2024)
- ![](https://dblp.org/img/n.png)

\[j34\]
[Sai Thu Ya Aung](https://dblp.org/pid/393/8474.html), Worapan Kusakunniran:

A comprehensive review of gait analysis using deep learning approaches in criminal investigation. [PeerJ Comput. Sci.10](https://dblp.org/db/journals/peerj-cs/peerj-cs10.html#journals/peerj-cs/AungK24): e2456 (2024)
- ![](https://dblp.org/img/n.png)

\[c31\]
[Kasidit Ruaydee](https://dblp.org/pid/400/0512.html), Worapan Kusakunniran, [Warangkana Srichamnong](https://dblp.org/pid/400/0242.html):

Deep Learning for Automatic Classification of Carotenoid Associated Color Pigmentation. [TENCON2024](https://dblp.org/db/conf/tencon/tencon2024.html#conf/tencon/RuaydeeKS24): 822-825
- 2023
- ![](https://dblp.org/img/n.png)

\[j33\]
[Trongtum Tongdee](https://dblp.org/pid/259/3204.html), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Thanongchai Siriapisith](https://dblp.org/pid/225/6300.html), [Pairash Saiviroonporn](https://dblp.org/pid/52/720.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thanandon Imaromkul](https://dblp.org/pid/244/5576.html), [Pakorn Yodprom](https://dblp.org/pid/295/4105.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Classification of chest radiography from general radiography using deep learning approach. [ICT Express9(3)](https://dblp.org/db/journals/ict-express/ict-express9.html#journals/ict-express/TongdeeKSSIY23): 313-319 (2023)
- ![](https://dblp.org/img/n.png)

\[j32\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Sarattha Kanchanapreechakorn](https://dblp.org/pid/244/5580.html), [Thanongchai Siriapisith](https://dblp.org/pid/225/6300.html), [Pairash Saiviroonporn](https://dblp.org/pid/52/720.html):

Fast MRI reconstruction using StrainNet with dual-domain loss on spatial and frequency spaces. [Intell. Syst. Appl.18](https://dblp.org/db/journals/iswa/iswa18.html#journals/iswa/KusakunniranKSS23): 200203 (2023)
- ![](https://dblp.org/img/n.png)

\[j31\]
Worapan Kusakunniran, [Punyanuch Borwarnginn](https://dblp.org/pid/283/9848.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sarattha Kanchanapreechakorn](https://dblp.org/pid/244/5580.html), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Panrasee Ritthipravat](https://dblp.org/pid/07/2677.html), [Pimchanok Tuakta](https://dblp.org/pid/316/6452.html), [Paitoon Benjapornlert](https://dblp.org/pid/316/6517.html):

Encoder-decoder network with RMP for tongue segmentation. [Medical Biol. Eng. Comput.61(5)](https://dblp.org/db/journals/mbec/mbec61.html#journals/mbec/KusakunniranBKTRTB23): 1193-1207 (2023)
- ![](https://dblp.org/img/n.png)

\[j30\]
Worapan Kusakunniran, [Punyanuch Borwarnginn](https://dblp.org/pid/283/9848.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thanandon Imaromkul](https://dblp.org/pid/244/5576.html), [Kittinun Aukkapinyo](https://dblp.org/pid/271/3524.html), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Disathon Wattanadhirach](https://dblp.org/pid/247/3899.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sophon Mongkolluksamee](https://dblp.org/pid/122/4993.html), [Ratchainant Thammasudjarit](https://dblp.org/pid/205/7872.html), [Panrasee Ritthipravat](https://dblp.org/pid/07/2677.html), [Pimchanok Tuakta](https://dblp.org/pid/316/6452.html), [Paitoon Benjapornlert](https://dblp.org/pid/316/6517.html):

Automated tongue segmentation using deep encoder-decoder model. [Multim. Tools Appl.82(24)](https://dblp.org/db/journals/mta/mta82.html#journals/mta/KusakunniranBIATWMTRTB23): 37661-37686 (2023)
- ![](https://dblp.org/img/n.png)

\[j29\]
[Lingxiang Yao](https://dblp.org/pid/207/9512.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Peng Zhang](https://dblp.org/pid/21/1048-57.html), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Improving Disentangled Representation Learning for Gait Recognition Using Group Supervision. [IEEE Trans. Multim.25](https://dblp.org/db/journals/tmm/tmm25.html#journals/tmm/YaoKZWZ23): 4187-4198 (2023)
- ![](https://dblp.org/img/n.png)

\[c30\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Kunthorn Phongluelert](https://dblp.org/pid/363/3189.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chanathip Sirisangpaival](https://dblp.org/pid/363/3274.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Osh Narayan](https://dblp.org/pid/363/3255.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Anuwat Wiratsudakul](https://dblp.org/pid/179/2075.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Cattle AutoID: Biometric for Cattle Identification: Cattle AutoID. [SIET2023](https://dblp.org/db/conf/siet/siet2023.html#conf/siet/KusakunniranPSN23): 570-574
- 2022
- ![](https://dblp.org/img/n.png)

\[j28\]
[Punyanuch Borwarnginn](https://dblp.org/pid/283/9848.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jason H. Haga](https://dblp.org/pid/78/3586.html), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png):

Predicting river water height using deep learning-based features. [ICT Express8(4)](https://dblp.org/db/journals/ict-express/ict-express8.html#journals/ict-express/BorwarnginnHK22): 588-594 (2022)
- ![](https://dblp.org/img/n.png)

\[j27\]
[Zaw Htet Aung](https://dblp.org/pid/175/3706.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Soonthareeya Sanium](https://dblp.org/pid/336/5953.html), [Chuenchat Songsaksuppachok](https://dblp.org/pid/336/4950.html), Worapan Kusakunniran, [Monamorn Precharattana](https://dblp.org/pid/09/11314.html), [Suparat Chuechote](https://dblp.org/pid/336/5619.html), [Khemmawadee Pongsanon](https://dblp.org/pid/336/5910.html), [Panrasee Ritthipravat](https://dblp.org/pid/07/2677.html):

Designing a novel teaching platform for AI: A case study in a Thai school context. [J. Comput. Assist. Learn.38(6)](https://dblp.org/db/journals/jcal/jcal38.html#journals/jcal/AungSSKPCPR22): 1714-1729 (2022)
- ![](https://dblp.org/img/n.png)

\[j26\]
[Thanongchai Siriapisith](https://dblp.org/pid/225/6300.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Peter Haddawy](https://dblp.org/pid/h/PeterHaddawy.html):

A retrospective study of 3D deep learning approach incorporating coordinate information to improve the segmentation of pre- and post-operative abdominal aortic aneurysm. [PeerJ Comput. Sci.8](https://dblp.org/db/journals/peerj-cs/peerj-cs8.html#journals/peerj-cs/SiriapisithKH22): e1033 (2022)
- ![](https://dblp.org/img/n.png)

\[j25\]
[Sarattha Kanchanapreechakorn](https://dblp.org/pid/244/5580.html), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Thanongchai Siriapisith](https://dblp.org/pid/225/6300.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pairash Saiviroonporn](https://dblp.org/pid/52/720.html):

Multi-level pooling encoder-decoder convolution neural network for MRI reconstruction. [PeerJ Comput. Sci.8](https://dblp.org/db/journals/peerj-cs/peerj-cs8.html#journals/peerj-cs/Kanchanapreechakorn22): e934 (2022)
- ![](https://dblp.org/img/n.png)

\[j24\]
[Lingxiang Yao](https://dblp.org/pid/207/9512.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jingsong Xu](https://dblp.org/pid/118/9311.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Collaborative Feature Learning for Gait Recognition Under Cloth Changes. [IEEE Trans. Circuits Syst. Video Technol.32(6)](https://dblp.org/db/journals/tcsv/tcsv32.html#journals/tcsv/YaoKWXZ22): 3615-3629 (2022)
- ![](https://dblp.org/img/n.png)

\[j23\]
[Lingxiang Yao](https://dblp.org/pid/207/9512.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jingsong Xu](https://dblp.org/pid/118/9311.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Recognizing Gaits Across Walking and Running Speeds. [ACM Trans. Multim. Comput. Commun. Appl.18(3)](https://dblp.org/db/journals/tomccap/tomccap18.html#journals/tomccap/YaoKWXZ22): 75:1-75:22 (2022)
- ![](https://dblp.org/img/n.png)

\[c29\]
[Kosin Saramas](https://dblp.org/pid/325/6769.html), [Jidapa Kraisangka](https://dblp.org/pid/150/6946.html), [Akara Supratak](https://dblp.org/pid/155/7090.html), [Thanapon Noraset](https://dblp.org/pid/151/3092.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Boonsit Yimwadsana](https://dblp.org/pid/72/6575.html), Worapan Kusakunniran:

HUMAN DETECTION AND SOCIAL DISTANCING MEASUREMENT IN A VIDEO. [JCSSE2022](https://dblp.org/db/conf/jcsse/jcsse2022.html#conf/jcsse/SaramasKSNYK22): 1-4
- ![](https://dblp.org/img/n.png)

\[c28\]
Worapan Kusakunniran, [Kittinun Aukkapinyo](https://dblp.org/pid/271/3524.html), [Punyanuch Borwarnginn](https://dblp.org/pid/283/9848.html), [Thanandon Imaromkul](https://dblp.org/pid/244/5576.html), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Disathon Wattanadhirach](https://dblp.org/pid/247/3899.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sophon Mongkolluksamee](https://dblp.org/pid/122/4993.html), [Ratchainant Thammasudjarit](https://dblp.org/pid/205/7872.html), [Panrasee Ritthipravat](https://dblp.org/pid/07/2677.html), [Pimchanok Tuakta](https://dblp.org/pid/316/6452.html), [Paitoon Benjapornlert](https://dblp.org/pid/316/6517.html):

Measurement of Tongue Motion using Optical Flows on Segmented Areas. [KST2022](https://dblp.org/db/conf/kst/kst2022.html#conf/kst/KusakunniranABI22): 24-28
- 2021
- ![](https://dblp.org/img/n.png)

\[j22\]
[Punyanuch Borwarnginn](https://dblp.org/pid/283/9848.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Sarattha Kanchanapreechakorn](https://dblp.org/pid/244/5580.html), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Knowing Your Dog Breed: Identifying a Dog Breed with Deep Learning. [Int. J. Autom. Comput.18(1)](https://dblp.org/db/journals/ijautcomp/ijautcomp18.html#journals/ijautcomp/BorwarnginnKKT21): 45-54 (2021)
- ![](https://dblp.org/img/n.png)

\[j21\]
Worapan Kusakunniran, [Anuwat Wiratsudakul](https://dblp.org/pid/179/2075.html), [Udom Chuachan](https://dblp.org/pid/244/5560.html), [Thanandon Imaromkul](https://dblp.org/pid/244/5576.html), [Sarattha Kanchanapreechakorn](https://dblp.org/pid/244/5580.html), [Noppanut Suksriupatham](https://dblp.org/pid/280/7706.html), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Analysing muzzle pattern images as a biometric for cattle identification. [Int. J. Biom.13(4)](https://dblp.org/db/journals/ijbm/ijbm13.html#journals/ijbm/KusakunniranWCI21): 367-384 (2021)
- ![](https://dblp.org/img/n.png)

\[j20\]
[Jirawat Jiwattanakul](https://dblp.org/pid/288/4121.html), [Chawapat Youngjitikornkun](https://dblp.org/pid/288/4207.html), Worapan Kusakunniran, [Anuwat Wiratsudakul](https://dblp.org/pid/179/2075.html), [Weerapong Thanapongtharm](https://dblp.org/pid/288/4253.html), [Kansuda Leelahapongsathon](https://dblp.org/pid/288/4042.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Map simulation of dogs' behaviour using population density of probabilistic model. [Int. J. Comput. Appl. Technol.65(1)](https://dblp.org/db/journals/ijcat/ijcat65.html#journals/ijcat/JiwattanakulYKW21): 14-24 (2021)
- ![](https://dblp.org/img/n.png)

\[j19\]
Worapan Kusakunniran, [Thearith Ponn](https://dblp.org/pid/346/4948.html), [Nuttapol Boonsom](https://dblp.org/pid/346/5429.html), [Suwimol Wahakit](https://dblp.org/pid/346/4699.html), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Construction of H5-Index for Conference Ranking Indicator and its Correlation to ERA. [J. Inf. Knowl. Manag.20(1)](https://dblp.org/db/journals/jikm/jikm20.html#journals/jikm/KusakunniranPBWT21): 2150011 (2021)
- ![](https://dblp.org/img/n.png)

\[j18\]
[Lingxiang Yao](https://dblp.org/pid/207/9512.html), Worapan Kusakunniran, [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Gait recognition using a few gait frames. [PeerJ Comput. Sci.7](https://dblp.org/db/journals/peerj-cs/peerj-cs7.html#journals/peerj-cs/YaoKWZ21): e382 (2021)
- ![](https://dblp.org/img/n.png)

\[j17\]
[Thanongchai Siriapisith](https://dblp.org/pid/225/6300.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Peter Haddawy](https://dblp.org/pid/h/PeterHaddawy.html):

A 3D deep learning approach to epicardial fat segmentation in non-contrast and post-contrast cardiac CT images. [PeerJ Comput. Sci.7](https://dblp.org/db/journals/peerj-cs/peerj-cs7.html#journals/peerj-cs/SiriapisithKH21): e806 (2021)
- ![](https://dblp.org/img/n.png)

\[j16\]
[Lingxiang Yao](https://dblp.org/pid/207/9512.html)![](https://dblp.org/img/orcid-mark.12x12.png), Worapan Kusakunniran, [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenmin Tang](https://dblp.org/pid/13/6728.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wankou Yang](https://dblp.org/pid/99/3602.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Robust gait recognition using hybrid descriptors based on Skeleton Gait Energy Image. [Pattern Recognit. Lett.150](https://dblp.org/db/journals/prl/prl150.html#journals/prl/YaoKWZTY21): 289-296 (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[j15\]
[Thanongchai Siriapisith](https://dblp.org/pid/225/6300.html), Worapan Kusakunniran, [Peter Haddawy](https://dblp.org/pid/h/PeterHaddawy.html):

Pyramid graph cut: Integrating intensity and gradient information for grayscale medical image segmentation. [Comput. Biol. Medicine126](https://dblp.org/db/journals/cbm/cbm126.html#journals/cbm/SiriapisithKH20): 103997 (2020)
- ![](https://dblp.org/img/n.png)

\[j14\]
Worapan Kusakunniran:

Review of gait recognition approaches and their challenges on view changes. [IET Biom.9(6)](https://dblp.org/db/journals/iet-bmt/iet-bmt9.html#journals/iet-bmt/Kusakunniran20): 238-250 (2020)
- ![](https://dblp.org/img/n.png)

\[j13\]
[Kittinun Aukkapinyo](https://dblp.org/pid/271/3524.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Suchakree Sawangwong](https://dblp.org/pid/271/3613.html), [Parintorn Pooyoi](https://dblp.org/pid/271/3612.html), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png):

Localization and Classification of Rice-grain Images Using Region Proposals-based Convolutional Neural Network. [Int. J. Autom. Comput.17(2)](https://dblp.org/db/journals/ijautcomp/ijautcomp17.html#journals/ijautcomp/AukkapinyoSPK20): 233-246 (2020)
- ![](https://dblp.org/img/n.png)

\[j12\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Anuwat Wiratsudakul](https://dblp.org/pid/179/2075.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Udom Chuachan](https://dblp.org/pid/244/5560.html), [Sarattha Kanchanapreechakorn](https://dblp.org/pid/244/5580.html), [Thanandon Imaromkul](https://dblp.org/pid/244/5576.html), [Noppanut Suksriupatham](https://dblp.org/pid/280/7706.html), [Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Biometric for Cattle Identification using Muzzle Patterns. [Int. J. Pattern Recognit. Artif. Intell.34(12)](https://dblp.org/db/journals/ijprai/ijprai34.html#journals/ijprai/KusakunniranWCK20): 2056007:1-2056007:21 (2020)
- ![](https://dblp.org/img/n.png)

\[c27\]
[Lingxiang Yao](https://dblp.org/pid/207/9512.html), Worapan Kusakunniran, [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jingsong Xu](https://dblp.org/pid/118/9311.html):

Part-based Collaborative Spatio-temporal Feature Learning for Cloth-changing Gait Recognition. [ICPR2020](https://dblp.org/db/conf/icpr/icpr2020.html#conf/icpr/YaoKWZX20): 2057-2064
- ![](https://dblp.org/img/n.png)

\[c26\]
[Phum Natakuaithung](https://dblp.org/pid/292/2893.html), Worapan Kusakunniran:

Development of AR Learning Assistance Tool for Clay-Sculpting 3D Model. [KST2020](https://dblp.org/db/conf/kst/kst2020.html#conf/kst/NatakuaithungK20): 109-114
- ![](https://dblp.org/img/n.png)

\[c25\]
[Napat Romlamduan](https://dblp.org/pid/283/9379.html), Worapan Kusakunniran:

Game-based Learning Tool for Photography. [TENCON2020](https://dblp.org/db/conf/tencon/tencon2020.html#conf/tencon/RomlamduanK20): 1255-1259
- ![](https://dblp.org/img/n.png)

\[c24\]
[Punyanuch Borwarnginn](https://dblp.org/pid/283/9848.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jason H. Haga](https://dblp.org/pid/78/3586.html), Worapan Kusakunniran:

Water Level Detection from CCTV Cameras using a Deep Learning Approach. [TENCON2020](https://dblp.org/db/conf/tencon/tencon2020.html#conf/tencon/BorwarnginnHK20): 1283-1288
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j11\]
[Thanongchai Siriapisith](https://dblp.org/pid/225/6300.html), Worapan Kusakunniran, [Peter Haddawy](https://dblp.org/pid/h/PeterHaddawy.html):

3D segmentation of exterior wall surface of abdominal aortic aneurysm from CT images using variable neighborhood search. [Comput. Biol. Medicine107](https://dblp.org/db/journals/cbm/cbm107.html#journals/cbm/SiriapisithKH19): 73-85 (2019)
- ![](https://dblp.org/img/n.png)

\[i1\]
[Dina B. Efremova](https://dblp.org/pid/246/4824.html), [Dmitry A. Konovalov](https://dblp.org/pid/57/3289.html), [Thanongchai Siriapisith](https://dblp.org/pid/225/6300.html), Worapan Kusakunniran, [Peter Haddawy](https://dblp.org/pid/h/PeterHaddawy.html):

Automatic segmentation of kidney and liver tumors in CT images. [CoRRabs/1908.01279](https://dblp.org/db/journals/corr/corr1908.html#journals/corr/abs-1908-01279) (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[j10\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Panrasee Ritthipravat](https://dblp.org/pid/07/2677.html), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Hard exudates segmentation based on learned initial seeds and iterative graph cut. [Comput. Methods Programs Biomed.158](https://dblp.org/db/journals/cmpb/cmpb158.html#journals/cmpb/KusakunniranWRZ18): 173-183 (2018)
- ![](https://dblp.org/img/n.png)

\[j9\]
[Thanongchai Siriapisith](https://dblp.org/pid/225/6300.html), Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Peter Haddawy](https://dblp.org/pid/h/PeterHaddawy.html):

Outer Wall Segmentation of Abdominal Aortic Aneurysm by Variable Neighborhood Search Through Intensity and Gradient Spaces. [J. Digit. Imaging31(4)](https://dblp.org/db/journals/jdi/jdi31.html#journals/jdi/SiriapisithKH18): 490-504 (2018)
- ![](https://dblp.org/img/n.png)

\[j8\]
Worapan Kusakunniran, [Amit Singh Dahal](https://dblp.org/pid/233/6689.html), [Wantanee Viriyasitavat](https://dblp.org/pid/03/3950.html):

Journal Co-Citation Analysis for Identifying Trends of Inter-Disciplinary Research: An Exploratory Case Study in a University. [J. Inf. Knowl. Manag.17(4)](https://dblp.org/db/journals/jikm/jikm17.html#journals/jikm/KusakunniranDV18): 1850040:1-1850040:22 (2018)
- ![](https://dblp.org/img/n.png)

\[c23\]
[Rangwan Kasantikul](https://dblp.org/pid/195/9444.html), Worapan Kusakunniran:

Improving Supervised Microaneurysm Segmentation using Autoencoder-Regularized Neural Network. [DICTA2018](https://dblp.org/db/conf/dicta/dicta2018.html#conf/dicta/KasantikulK18): 1-7
- ![](https://dblp.org/img/n.png)

\[c22\]
[Thanongchai Siriapisith](https://dblp.org/pid/225/6300.html), Worapan Kusakunniran, [Peter Haddawy](https://dblp.org/pid/h/PeterHaddawy.html):

A General Approach to Segmentation in CT Grayscale Images using Variable Neighborhood Search. [DICTA2018](https://dblp.org/db/conf/dicta/dicta2018.html#conf/dicta/SiriapisithKH18): 1-7
- ![](https://dblp.org/img/n.png)

\[c21\]
[Lingxiang Yao](https://dblp.org/pid/207/9512.html), Worapan Kusakunniran, [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenmin Tang](https://dblp.org/pid/13/6728.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Robust CNN-based Gait Verification and Identification using Skeleton Gait Energy Image. [DICTA2018](https://dblp.org/db/conf/dicta/dicta2018.html#conf/dicta/YaoKWZT18): 1-7
- ![](https://dblp.org/img/n.png)

\[c20\]
Worapan Kusakunniran, [Anuwat Wiratsudakul](https://dblp.org/pid/179/2075.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Udom Chuachan](https://dblp.org/pid/244/5560.html), [Sarattha Kanchanapreechakorn](https://dblp.org/pid/244/5580.html), [Thanandon Imaromkul](https://dblp.org/pid/244/5576.html):

Automatic cattle identification based on fusion of texture features extracted from muzzle images. [ICIT2018](https://dblp.org/db/conf/icit2/icit2018.html#conf/icit2/KusakunniranWCK18): 1484-1489
- ![](https://dblp.org/img/n.png)

\[c19\]
[Benjarat Tirasirichai](https://dblp.org/pid/280/4826.html), [Peeraya Thanomboon](https://dblp.org/pid/280/5557.html), [Pimpaknat Soontorntham](https://dblp.org/pid/280/5132.html), Worapan Kusakunniran, [Mark A. Robinson](https://dblp.org/pid/69/8465.html):

Bloom Balance: Calorie Balancing Application With Scientific Validation. [JCSSE2018](https://dblp.org/db/conf/jcsse/jcsse2018.html#conf/jcsse/TirasirichaiTSK18): 1-6
- ![](https://dblp.org/img/n.png)

\[c18\]
[Cheng Jiang](https://dblp.org/pid/15/11195.html), Worapan Kusakunniran:

Optimizing Location-Routing Problem using Iterative Combination of GA and VNS. [KST2018](https://dblp.org/db/conf/kst/kst2018.html#conf/kst/JiangK18): 24-29
- ![](https://dblp.org/img/n.png)

\[c17\]
[Thanandon Imaromkul](https://dblp.org/pid/244/5576.html), [Wiphada Dendee](https://dblp.org/pid/292/4260.html), [Sarocha Chokewiwattana](https://dblp.org/pid/292/3775.html), Worapan Kusakunniran:

3D Reconstruction of Long Bone using Kinect. [KST2018](https://dblp.org/db/conf/kst/kst2018.html#conf/kst/ImaromkulDCK18): 129-133
- ![](https://dblp.org/img/n.png)

\[c16\]
[Atid Puwatnuttasit](https://dblp.org/pid/245/6694.html), Worapan Kusakunniran:

Gesture Recognition for Traffic Hand-Signals Training Simulator Using Kinect. [TENCON2018](https://dblp.org/db/conf/tencon/tencon2018.html#conf/tencon/PuwatnuttasitK18): 297-302
- ![](https://dblp.org/img/n.png)

\[c15\]
[Chanat Sinpithakkul](https://dblp.org/pid/245/7319.html), Worapan Kusakunniran, [Sunee Bovonsunthonchai](https://dblp.org/pid/245/6902.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peemongkon Wattananon](https://dblp.org/pid/245/6646.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Game-based Enhancement for Rehabilitation Based on Action Recognition Using Kinect. [TENCON2018](https://dblp.org/db/conf/tencon/tencon2018.html#conf/tencon/SinpithakkulKBW18): 303-308
- ![](https://dblp.org/img/n.png)

\[c14\]
[Thunwa Sattrupai](https://dblp.org/pid/245/6870.html), Worapan Kusakunniran:

Deep Trajectory Based Gait Recognition for Human Re-identification. [TENCON2018](https://dblp.org/db/conf/tencon/tencon2018.html#conf/tencon/SattrupaiK18): 1723-1726
- 2017
- ![](https://dblp.org/img/n.png)

\[c13\]
Worapan Kusakunniran, [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Action Recognition Based on Correlated Codewords of Body Movements. [DICTA2017](https://dblp.org/db/conf/dicta/dicta2017.html#conf/dicta/KusakunniranWZ17): 1-8
- ![](https://dblp.org/img/n.png)

\[c12\]
[Lingxiang Yao](https://dblp.org/pid/207/9512.html), Worapan Kusakunniran, [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenmin Tang](https://dblp.org/pid/13/6728.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Robust Gait Recognition under Unconstrained Environments Using Hybrid Descriptions. [DICTA2017](https://dblp.org/db/conf/dicta/dicta2017.html#conf/dicta/YaoKWZT17): 1-7
- ![](https://dblp.org/img/n.png)

\[c11\]
Worapan Kusakunniran, [Nantawat Prachasri](https://dblp.org/pid/165/1877.html), [Nattaporn Dirakbussarakom](https://dblp.org/pid/165/1782.html), [Duangkamol Yangchaem](https://dblp.org/pid/165/1905.html):

Distinguishing ACL patients from healthy individuals using multilayer perceptron on motion patterns. [KST2017](https://dblp.org/db/conf/kst/kst2017.html#conf/kst/KusakunniranPDY17): 1-5
- 2015
- ![](https://dblp.org/img/n.png)

\[c10\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png):

Extracting Gait Figures in a Video Based on Markerless Motion. [KSE2015](https://dblp.org/db/conf/kse/kse2015.html#conf/kse/Kusakunniran15): 306-309
- ![](https://dblp.org/img/n.png)

\[c9\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Nattaporn Dirakbussarakom](https://dblp.org/pid/165/1782.html), [Nantawat Prachasri](https://dblp.org/pid/165/1877.html), [Duangkamol Yangchaem](https://dblp.org/pid/165/1905.html), [Jos Vanrenterghem](https://dblp.org/pid/165/1686.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mark A. Robinson](https://dblp.org/pid/69/8465.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Discriminating motion patterns of ACL reconstructed patients from healthy individuals. [MVA2015](https://dblp.org/db/conf/mva/mva2015.html#conf/mva/KusakunniranDPY15): 447-450
- 2014
- ![](https://dblp.org/img/n.png)

\[j7\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png):

Attribute-based learning for gait recognition using spatio-temporal interest points. [Image Vis. Comput.32(12)](https://dblp.org/db/journals/ivc/ivc32.html#journals/ivc/Kusakunniran14): 1117-1126 (2014)
- ![](https://dblp.org/img/n.png)

\[j6\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png):

Recognizing Gaits on Spatio-Temporal Feature Domain. [IEEE Trans. Inf. Forensics Secur.9(9)](https://dblp.org/db/journals/tifs/tifs9.html#journals/tifs/Kusakunniran14): 1416-1423 (2014)
- ![](https://dblp.org/img/n.png)

\[j5\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liang Wang](https://dblp.org/pid/56/4499-1.html):

Recognizing Gaits Across Views Through Correlated Motion Co-Clustering. [IEEE Trans. Image Process.23(2)](https://dblp.org/db/journals/tip/tip23.html#journals/tip/KusakunniranWZLW14): 696-709 (2014)
- 2013
- ![](https://dblp.org/img/n.png)

\[j4\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Ma](https://dblp.org/pid/69/1112.html), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A New View-Invariant Feature for Cross-View Gait Recognition. [IEEE Trans. Inf. Forensics Secur.8(10)](https://dblp.org/db/journals/tifs/tifs8.html#journals/tifs/KusakunniranWZML13): 1642-1653 (2013)
- ![](https://dblp.org/img/n.png)

\[c8\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Shin'ichi Satoh](https://dblp.org/pid/50/290.html), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Attribute-based learning for large scale object classification. [ICME2013](https://dblp.org/db/conf/icmcs/icme2013.html#conf/icmcs/KusakunniranSZW13): 1-6
- 2012
- ![](https://dblp.org/img/n.png)

\[j3\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Cross-view and multi-view gait recognitions based on view transformation model using multi-layer perceptron. [Pattern Recognit. Lett.33(7)](https://dblp.org/db/journals/prl/prl33.html#journals/prl/KusakunniranWZL12): 882-889 (2012)
- ![](https://dblp.org/img/n.png)

\[j2\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Gait Recognition Under Various Viewing Angles Based on Correlated Motion Regression. [IEEE Trans. Circuits Syst. Video Technol.22(6)](https://dblp.org/db/journals/tcsv/tcsv22.html#journals/tcsv/KusakunniranWZL12): 966-980 (2012)
- ![](https://dblp.org/img/n.png)

\[j1\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Gait Recognition Across Various Walking Speeds Using Higher Order Shape Configuration Based on a Differential Composition Model. [IEEE Trans. Syst. Man Cybern. Part B42(6)](https://dblp.org/db/journals/tsmc/tsmcb42.html#journals/tsmc/KusakunniranWZL12): 1654-1668 (2012)
- 2011
- ![](https://dblp.org/img/n.png)

\[c7\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Pairwise Shape configuration-based PSA for gait recognition under small viewing angle change. [AVSS2011](https://dblp.org/db/conf/avss/avss2011.html#conf/avss/KusakunniranWZL11): 17-22
- ![](https://dblp.org/img/n.png)

\[c6\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Speed-invariant gait recognition based on Procrustes Shape Analysis using higher-order shape configuration. [ICIP2011](https://dblp.org/db/conf/icip/icip2011.html#conf/icip/KusakunniranWZL11): 545-548
- 2010
- ![](https://dblp.org/img/n.png)

\[c5\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Support vector regression for multi-view gait recognition based on local motion feature selection. [CVPR2010](https://dblp.org/db/conf/cvpr/cvpr2010.html#conf/cvpr/KusakunniranWZL10): 974-981
- ![](https://dblp.org/img/n.png)

\[c4\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Multi-view Gait Recognition Based on Motion Regression Using Multilayer Perceptron. [ICPR2010](https://dblp.org/db/conf/icpr/icpr2010.html#conf/icpr/KusakunniranWZL10): 2186-2189
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2009
- ![](https://dblp.org/img/n.png)

\[c3\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Automatic Gait Recognition Using Weighted Binary Pattern on Video. [AVSS2009](https://dblp.org/db/conf/avss/avss2009.html#conf/avss/KusakunniranWLZ09): 49-54
- ![](https://dblp.org/img/n.png)

\[c2\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Direct Method to Self-Calibrate a Surveillance Camera by Observing a Walking Pedestrian. [DICTA2009](https://dblp.org/db/conf/dicta/dicta2009.html#conf/dicta/KusakunniranLZ09): 250-255
- ![](https://dblp.org/img/n.png)

\[c1\]
Worapan Kusakunniran![](https://dblp.org/img/orcid-mark.12x12.png), [Qiang Wu](https://dblp.org/pid/87/2533-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jian Zhang](https://dblp.org/pid/07/314-2.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Multiple views gait recognition using View Transformation Model based on optimized Gait Energy Image. [ICCV Workshops2009](https://dblp.org/db/conf/iccvw/iccvw2009.html#conf/iccvw/Kusakunniran0L009): 1058-1064
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/05/7576.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Phuriwat Angkoondittaphong](https://dblp.org/pid/414/0257.html)

[\[j44\]](https://dblp.org/pid/05/7576.html#j44)

[2](https://dblp.org/pid/05/7576.html?view=joint&param=2 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=2)

[Vutipong Areekul](https://dblp.org/pid/56/6323.html)

[\[j38\]](https://dblp.org/pid/05/7576.html#j38)

[3](https://dblp.org/pid/05/7576.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Kittinun Aukkapinyo](https://dblp.org/pid/271/3524.html)

[\[j43\]](https://dblp.org/pid/05/7576.html#j43) [\[j36\]](https://dblp.org/pid/05/7576.html#j36) [\[j30\]](https://dblp.org/pid/05/7576.html#j30) [\[c28\]](https://dblp.org/pid/05/7576.html#c28) [\[j13\]](https://dblp.org/pid/05/7576.html#j13)

[4](https://dblp.org/pid/05/7576.html?view=joint&param=4 "show joint publications")

[![7](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=7)

[Sai Thu Ya Aung](https://dblp.org/pid/393/8474.html)

[\[j46\]](https://dblp.org/pid/05/7576.html#j46) [\[j34\]](https://dblp.org/pid/05/7576.html#j34)

[5](https://dblp.org/pid/05/7576.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Zaw Htet Aung](https://dblp.org/pid/175/3706.html)

[\[j27\]](https://dblp.org/pid/05/7576.html#j27)

[6](https://dblp.org/pid/05/7576.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Paitoon Benjapornlert](https://dblp.org/pid/316/6517.html)

[\[j45\]](https://dblp.org/pid/05/7576.html#j45) [\[j37\]](https://dblp.org/pid/05/7576.html#j37) [\[j35\]](https://dblp.org/pid/05/7576.html#j35) [\[j31\]](https://dblp.org/pid/05/7576.html#j31) [\[j30\]](https://dblp.org/pid/05/7576.html#j30) [\[c28\]](https://dblp.org/pid/05/7576.html#c28)

[7](https://dblp.org/pid/05/7576.html?view=joint&param=7 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=2)

[André Boller](https://dblp.org/pid/294/8809.html)

[\[j40\]](https://dblp.org/pid/05/7576.html#j40)

[8](https://dblp.org/pid/05/7576.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Nuttapol Boonsom](https://dblp.org/pid/346/5429.html)

[\[j19\]](https://dblp.org/pid/05/7576.html#j19)

[9](https://dblp.org/pid/05/7576.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Khemmapat Boonyo](https://dblp.org/pid/425/6624.html)

[\[j42\]](https://dblp.org/pid/05/7576.html#j42)

[10](https://dblp.org/pid/05/7576.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Punyanuch Borwarnginn](https://dblp.org/pid/283/9848.html)

[\[j31\]](https://dblp.org/pid/05/7576.html#j31) [\[j30\]](https://dblp.org/pid/05/7576.html#j30) [\[j28\]](https://dblp.org/pid/05/7576.html#j28) [\[c28\]](https://dblp.org/pid/05/7576.html#c28) [\[j22\]](https://dblp.org/pid/05/7576.html#j22) [\[c24\]](https://dblp.org/pid/05/7576.html#c24)

[11](https://dblp.org/pid/05/7576.html?view=joint&param=11 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=4)

[Sunee Bovonsunthonchai](https://dblp.org/pid/245/6902.html)

[\[c15\]](https://dblp.org/pid/05/7576.html#c15)

[12](https://dblp.org/pid/05/7576.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Irin Chaikangwan](https://dblp.org/pid/371/3596.html)

[\[j39\]](https://dblp.org/pid/05/7576.html#j39)

[13](https://dblp.org/pid/05/7576.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Kittikan Charoenjai](https://dblp.org/pid/371/3422.html)

[\[j39\]](https://dblp.org/pid/05/7576.html#j39)

[14](https://dblp.org/pid/05/7576.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Sarocha Chokewiwattana](https://dblp.org/pid/292/3775.html)

[\[c17\]](https://dblp.org/pid/05/7576.html#c17)

[15](https://dblp.org/pid/05/7576.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Kittisak Chotikkakamthorn](https://dblp.org/pid/384/8376.html)

[\[j45\]](https://dblp.org/pid/05/7576.html#j45) [\[j35\]](https://dblp.org/pid/05/7576.html#j35)

[16](https://dblp.org/pid/05/7576.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Udom Chuachan](https://dblp.org/pid/244/5560.html)

[\[j21\]](https://dblp.org/pid/05/7576.html#j21) [\[j12\]](https://dblp.org/pid/05/7576.html#j12) [\[c20\]](https://dblp.org/pid/05/7576.html#c20)

[17](https://dblp.org/pid/05/7576.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Suparat Chuechote](https://dblp.org/pid/336/5619.html)

[\[j27\]](https://dblp.org/pid/05/7576.html#j27)

[18](https://dblp.org/pid/05/7576.html?view=joint&param=18 "show joint publications")

[![5](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=5)

[Amit Singh Dahal](https://dblp.org/pid/233/6689.html)

[\[j8\]](https://dblp.org/pid/05/7576.html#j8)

[19](https://dblp.org/pid/05/7576.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Wiphada Dendee](https://dblp.org/pid/292/4260.html)

[\[c17\]](https://dblp.org/pid/05/7576.html#c17)

[20](https://dblp.org/pid/05/7576.html?view=joint&param=20 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=3)

[Nattaporn Dirakbussarakom](https://dblp.org/pid/165/1782.html)

[\[c11\]](https://dblp.org/pid/05/7576.html#c11) [\[c9\]](https://dblp.org/pid/05/7576.html#c9)

[21](https://dblp.org/pid/05/7576.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Dina B. Efremova](https://dblp.org/pid/246/4824.html)

[\[i1\]](https://dblp.org/pid/05/7576.html#i1)

[22](https://dblp.org/pid/05/7576.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Peter Haddawy](https://dblp.org/pid/h/PeterHaddawy.html)

[\[j44\]](https://dblp.org/pid/05/7576.html#j44) [\[j26\]](https://dblp.org/pid/05/7576.html#j26) [\[j17\]](https://dblp.org/pid/05/7576.html#j17) [\[j15\]](https://dblp.org/pid/05/7576.html#j15) [\[j11\]](https://dblp.org/pid/05/7576.html#j11) [\[i1\]](https://dblp.org/pid/05/7576.html#i1) [\[j9\]](https://dblp.org/pid/05/7576.html#j9) [\[c22\]](https://dblp.org/pid/05/7576.html#c22)

[23](https://dblp.org/pid/05/7576.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Jason H. Haga](https://dblp.org/pid/78/3586.html)

[\[j28\]](https://dblp.org/pid/05/7576.html#j28) [\[c24\]](https://dblp.org/pid/05/7576.html#c24)

[24](https://dblp.org/pid/05/7576.html?view=joint&param=24 "show joint publications")

[![7](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=7)

[Yew Kwang Hooi](https://dblp.org/pid/141/5757.html)

[\[j46\]](https://dblp.org/pid/05/7576.html#j46)

[25](https://dblp.org/pid/05/7576.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Thanandon Imaromkul](https://dblp.org/pid/244/5576.html)

[\[j43\]](https://dblp.org/pid/05/7576.html#j43) [\[j37\]](https://dblp.org/pid/05/7576.html#j37) [\[j36\]](https://dblp.org/pid/05/7576.html#j36) [\[j33\]](https://dblp.org/pid/05/7576.html#j33) [\[j30\]](https://dblp.org/pid/05/7576.html#j30) [\[c28\]](https://dblp.org/pid/05/7576.html#c28) [\[j21\]](https://dblp.org/pid/05/7576.html#j21) [\[j12\]](https://dblp.org/pid/05/7576.html#j12) [\[c20\]](https://dblp.org/pid/05/7576.html#c20) [\[c17\]](https://dblp.org/pid/05/7576.html#c17)

[26](https://dblp.org/pid/05/7576.html?view=joint&param=26 "show joint publications")

[Cheng Jiang](https://dblp.org/pid/15/11195.html)

[\[c18\]](https://dblp.org/pid/05/7576.html#c18)

[27](https://dblp.org/pid/05/7576.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Jirawat Jiwattanakul](https://dblp.org/pid/288/4121.html)

[\[j20\]](https://dblp.org/pid/05/7576.html#j20)

[28](https://dblp.org/pid/05/7576.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Sarattha Kanchanapreechakorn](https://dblp.org/pid/244/5580.html)

[\[j32\]](https://dblp.org/pid/05/7576.html#j32) [\[j31\]](https://dblp.org/pid/05/7576.html#j31) [\[j25\]](https://dblp.org/pid/05/7576.html#j25) [\[j22\]](https://dblp.org/pid/05/7576.html#j22) [\[j21\]](https://dblp.org/pid/05/7576.html#j21) [\[j12\]](https://dblp.org/pid/05/7576.html#j12) [\[c20\]](https://dblp.org/pid/05/7576.html#c20)

[29](https://dblp.org/pid/05/7576.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Rangwan Kasantikul](https://dblp.org/pid/195/9444.html)

[\[j41\]](https://dblp.org/pid/05/7576.html#j41) [\[c23\]](https://dblp.org/pid/05/7576.html#c23)

[30](https://dblp.org/pid/05/7576.html?view=joint&param=30 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=2)

[Ali Mohammad Khodadoust](https://dblp.org/pid/198/7087.html)

[\[j47\]](https://dblp.org/pid/05/7576.html#j47)

[31](https://dblp.org/pid/05/7576.html?view=joint&param=31 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=2)

[Javad Khodadoust](https://dblp.org/pid/198/7056.html)

[\[j49\]](https://dblp.org/pid/05/7576.html#j49) [\[j47\]](https://dblp.org/pid/05/7576.html#j47) [\[j40\]](https://dblp.org/pid/05/7576.html#j40) [\[j38\]](https://dblp.org/pid/05/7576.html#j38)

[32](https://dblp.org/pid/05/7576.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Siripra Kingchan](https://dblp.org/pid/329/7524.html)

[\[j44\]](https://dblp.org/pid/05/7576.html#j44)

[33](https://dblp.org/pid/05/7576.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Dmitry A. Konovalov](https://dblp.org/pid/57/3289.html)

[\[i1\]](https://dblp.org/pid/05/7576.html#i1)

[34](https://dblp.org/pid/05/7576.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Jidapa Kraisangka](https://dblp.org/pid/150/6946.html)

[\[c29\]](https://dblp.org/pid/05/7576.html#c29)

[35](https://dblp.org/pid/05/7576.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Kansuda Leelahapongsathon](https://dblp.org/pid/288/4042.html)

[\[j20\]](https://dblp.org/pid/05/7576.html#j20)

[36](https://dblp.org/pid/05/7576.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Hongdong Li](https://dblp.org/pid/59/4859.html)

[\[j5\]](https://dblp.org/pid/05/7576.html#j5) [\[j4\]](https://dblp.org/pid/05/7576.html#j4) [\[j3\]](https://dblp.org/pid/05/7576.html#j3) [\[j2\]](https://dblp.org/pid/05/7576.html#j2) [\[j1\]](https://dblp.org/pid/05/7576.html#j1) [\[c7\]](https://dblp.org/pid/05/7576.html#c7) [\[c6\]](https://dblp.org/pid/05/7576.html#c6) [\[c5\]](https://dblp.org/pid/05/7576.html#c5) [\[c4\]](https://dblp.org/pid/05/7576.html#c4) [\[c3\]](https://dblp.org/pid/05/7576.html#c3) [\[c2\]](https://dblp.org/pid/05/7576.html#c2) [\[c1\]](https://dblp.org/pid/05/7576.html#c1)

[37](https://dblp.org/pid/05/7576.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Wen-Nung Lie](https://dblp.org/pid/07/5659.html)

[\[j45\]](https://dblp.org/pid/05/7576.html#j45) [\[j35\]](https://dblp.org/pid/05/7576.html#j35)

[38](https://dblp.org/pid/05/7576.html?view=joint&param=38 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=2)

[Octavio Loyola-González](https://dblp.org/pid/131/1778.html)

[\[j40\]](https://dblp.org/pid/05/7576.html#j40) [\[j38\]](https://dblp.org/pid/05/7576.html#j38)

[39](https://dblp.org/pid/05/7576.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Yi Ma](https://dblp.org/pid/69/1112.html)

[\[j4\]](https://dblp.org/pid/05/7576.html#j4)

[40](https://dblp.org/pid/05/7576.html?view=joint&param=40 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=2)

[Emanuela Marasco](https://dblp.org/pid/64/7404.html)

[\[j49\]](https://dblp.org/pid/05/7576.html#j49)

[41](https://dblp.org/pid/05/7576.html?view=joint&param=41 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=2)

[Miguel Angel Medina-Pérez](https://dblp.org/pid/87/5148.html)

[\[j49\]](https://dblp.org/pid/05/7576.html#j49) [\[j47\]](https://dblp.org/pid/05/7576.html#j47) [\[j40\]](https://dblp.org/pid/05/7576.html#j40) [\[j38\]](https://dblp.org/pid/05/7576.html#j38)

[42](https://dblp.org/pid/05/7576.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Sophon Mongkolluksamee](https://dblp.org/pid/122/4993.html)

[\[j37\]](https://dblp.org/pid/05/7576.html#j37) [\[j30\]](https://dblp.org/pid/05/7576.html#j30) [\[c28\]](https://dblp.org/pid/05/7576.html#c28)

[43](https://dblp.org/pid/05/7576.html?view=joint&param=43 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=2)

[Raúl Monroy](https://dblp.org/pid/m/RaulMonroy.html)

[\[j49\]](https://dblp.org/pid/05/7576.html#j49) [\[j47\]](https://dblp.org/pid/05/7576.html#j47) [\[j40\]](https://dblp.org/pid/05/7576.html#j40) [\[j38\]](https://dblp.org/pid/05/7576.html#j38)

[44](https://dblp.org/pid/05/7576.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Osh Narayan](https://dblp.org/pid/363/3255.html)

[\[c30\]](https://dblp.org/pid/05/7576.html#c30)

[45](https://dblp.org/pid/05/7576.html?view=joint&param=45 "show joint publications")

[Phum Natakuaithung](https://dblp.org/pid/292/2893.html)

[\[c26\]](https://dblp.org/pid/05/7576.html#c26)

[46](https://dblp.org/pid/05/7576.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Poonsuta Nava-apisak](https://dblp.org/pid/413/9803.html)

[\[j44\]](https://dblp.org/pid/05/7576.html#j44)

[47](https://dblp.org/pid/05/7576.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Thanapon Noraset](https://dblp.org/pid/151/3092.html)

[\[j44\]](https://dblp.org/pid/05/7576.html#j44) [\[c29\]](https://dblp.org/pid/05/7576.html#c29)

[48](https://dblp.org/pid/05/7576.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Noppanan Phinklao](https://dblp.org/pid/386/4373.html)

[\[j48\]](https://dblp.org/pid/05/7576.html#j48)

[49](https://dblp.org/pid/05/7576.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Kunthorn Phongluelert](https://dblp.org/pid/363/3189.html)

[\[c30\]](https://dblp.org/pid/05/7576.html#c30)

[50](https://dblp.org/pid/05/7576.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Khemmawadee Pongsanon](https://dblp.org/pid/336/5910.html)

[\[j27\]](https://dblp.org/pid/05/7576.html#j27)

[51](https://dblp.org/pid/05/7576.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Thearith Ponn](https://dblp.org/pid/346/4948.html)

[\[j19\]](https://dblp.org/pid/05/7576.html#j19)

[52](https://dblp.org/pid/05/7576.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Parintorn Pooyoi](https://dblp.org/pid/271/3612.html)

[\[j13\]](https://dblp.org/pid/05/7576.html#j13)

[53](https://dblp.org/pid/05/7576.html?view=joint&param=53 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=3)

[Nantawat Prachasri](https://dblp.org/pid/165/1877.html)

[\[c11\]](https://dblp.org/pid/05/7576.html#c11) [\[c9\]](https://dblp.org/pid/05/7576.html#c9)

[54](https://dblp.org/pid/05/7576.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Monamorn Precharattana](https://dblp.org/pid/09/11314.html)

[\[j27\]](https://dblp.org/pid/05/7576.html#j27)

[55](https://dblp.org/pid/05/7576.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Wimolsiri Pridasawas](https://dblp.org/pid/421/4877.html)

[\[j48\]](https://dblp.org/pid/05/7576.html#j48)

[56](https://dblp.org/pid/05/7576.html?view=joint&param=56 "show joint publications")

[Atid Puwatnuttasit](https://dblp.org/pid/245/6694.html)

[\[c16\]](https://dblp.org/pid/05/7576.html#c16)

[57](https://dblp.org/pid/05/7576.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Panrasee Ritthipravat](https://dblp.org/pid/07/2677.html)

[\[j45\]](https://dblp.org/pid/05/7576.html#j45) [\[j37\]](https://dblp.org/pid/05/7576.html#j37) [\[j35\]](https://dblp.org/pid/05/7576.html#j35) [\[j31\]](https://dblp.org/pid/05/7576.html#j31) [\[j30\]](https://dblp.org/pid/05/7576.html#j30) [\[j27\]](https://dblp.org/pid/05/7576.html#j27) [\[c28\]](https://dblp.org/pid/05/7576.html#c28) [\[j10\]](https://dblp.org/pid/05/7576.html#j10)

[58](https://dblp.org/pid/05/7576.html?view=joint&param=58 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=3)

[Mark A. Robinson](https://dblp.org/pid/69/8465.html)

[\[c19\]](https://dblp.org/pid/05/7576.html#c19) [\[c9\]](https://dblp.org/pid/05/7576.html#c9)

[59](https://dblp.org/pid/05/7576.html?view=joint&param=59 "show joint publications")

[Napat Romlamduan](https://dblp.org/pid/283/9379.html)

[\[c25\]](https://dblp.org/pid/05/7576.html#c25)

[60](https://dblp.org/pid/05/7576.html?view=joint&param=60 "show joint publications")

[![6](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=6)

[Kasidit Ruaydee](https://dblp.org/pid/400/0512.html)

[\[c31\]](https://dblp.org/pid/05/7576.html#c31)

[61](https://dblp.org/pid/05/7576.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Pairash Saiviroonporn](https://dblp.org/pid/52/720.html)

[\[j33\]](https://dblp.org/pid/05/7576.html#j33) [\[j32\]](https://dblp.org/pid/05/7576.html#j32) [\[j25\]](https://dblp.org/pid/05/7576.html#j25)

[62](https://dblp.org/pid/05/7576.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Soonthareeya Sanium](https://dblp.org/pid/336/5953.html)

[\[j27\]](https://dblp.org/pid/05/7576.html#j27)

[63](https://dblp.org/pid/05/7576.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Kosin Saramas](https://dblp.org/pid/325/6769.html)

[\[c29\]](https://dblp.org/pid/05/7576.html#c29)

[64](https://dblp.org/pid/05/7576.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Shin'ichi Satoh 0001](https://dblp.org/pid/50/290.html)

[\[c8\]](https://dblp.org/pid/05/7576.html#c8)

[65](https://dblp.org/pid/05/7576.html?view=joint&param=65 "show joint publications")

[Thunwa Sattrupai](https://dblp.org/pid/245/6870.html)

[\[c14\]](https://dblp.org/pid/05/7576.html#c14)

[66](https://dblp.org/pid/05/7576.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Suchakree Sawangwong](https://dblp.org/pid/271/3613.html)

[\[j13\]](https://dblp.org/pid/05/7576.html#j13)

[67](https://dblp.org/pid/05/7576.html?view=joint&param=67 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=4)

[Chanat Sinpithakkul](https://dblp.org/pid/245/7319.html)

[\[c15\]](https://dblp.org/pid/05/7576.html#c15)

[68](https://dblp.org/pid/05/7576.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Thanongchai Siriapisith](https://dblp.org/pid/225/6300.html)

[\[j33\]](https://dblp.org/pid/05/7576.html#j33) [\[j32\]](https://dblp.org/pid/05/7576.html#j32) [\[j26\]](https://dblp.org/pid/05/7576.html#j26) [\[j25\]](https://dblp.org/pid/05/7576.html#j25) [\[j17\]](https://dblp.org/pid/05/7576.html#j17) [\[j15\]](https://dblp.org/pid/05/7576.html#j15) [\[j11\]](https://dblp.org/pid/05/7576.html#j11) [\[i1\]](https://dblp.org/pid/05/7576.html#i1) [\[j9\]](https://dblp.org/pid/05/7576.html#j9) [\[c22\]](https://dblp.org/pid/05/7576.html#c22)

[69](https://dblp.org/pid/05/7576.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Chanathip Sirisangpaival](https://dblp.org/pid/363/3274.html)

[\[c30\]](https://dblp.org/pid/05/7576.html#c30)

[70](https://dblp.org/pid/05/7576.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Pimpinan Somsong](https://dblp.org/pid/375/3959.html)

[\[j43\]](https://dblp.org/pid/05/7576.html#j43) [\[j36\]](https://dblp.org/pid/05/7576.html#j36)

[71](https://dblp.org/pid/05/7576.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Dittapong Songsaeng](https://dblp.org/pid/328/2181.html)

[\[j44\]](https://dblp.org/pid/05/7576.html#j44)

[72](https://dblp.org/pid/05/7576.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Chuenchat Songsaksuppachok](https://dblp.org/pid/336/4950.html)

[\[j27\]](https://dblp.org/pid/05/7576.html#j27)

[73](https://dblp.org/pid/05/7576.html?view=joint&param=73 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=3)

[Pimpaknat Soontorntham](https://dblp.org/pid/280/5132.html)

[\[c19\]](https://dblp.org/pid/05/7576.html#c19)

[74](https://dblp.org/pid/05/7576.html?view=joint&param=74 "show joint publications")

[![6](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=6)

[Warangkana Srichamnong](https://dblp.org/pid/400/0242.html)

[\[c31\]](https://dblp.org/pid/05/7576.html#c31)

[75](https://dblp.org/pid/05/7576.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Noppanut Suksriupatham](https://dblp.org/pid/280/7706.html)

[\[j21\]](https://dblp.org/pid/05/7576.html#j21) [\[j12\]](https://dblp.org/pid/05/7576.html#j12)

[76](https://dblp.org/pid/05/7576.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Akara Supratak](https://dblp.org/pid/155/7090.html)

[\[j44\]](https://dblp.org/pid/05/7576.html#j44) [\[c29\]](https://dblp.org/pid/05/7576.html#c29)

[77](https://dblp.org/pid/05/7576.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Zhenmin Tang](https://dblp.org/pid/13/6728.html)

[\[j16\]](https://dblp.org/pid/05/7576.html#j16) [\[c21\]](https://dblp.org/pid/05/7576.html#c21) [\[c12\]](https://dblp.org/pid/05/7576.html#c12)

[78](https://dblp.org/pid/05/7576.html?view=joint&param=78 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=2)

[Philipp Terhörst](https://dblp.org/pid/203/2506.html)

[\[j40\]](https://dblp.org/pid/05/7576.html#j40)

[79](https://dblp.org/pid/05/7576.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Tipajin Thaipisutikul](https://dblp.org/pid/277/1591.html)

[\[j39\]](https://dblp.org/pid/05/7576.html#j39)

[80](https://dblp.org/pid/05/7576.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Ratchainant Thammasudjarit](https://dblp.org/pid/205/7872.html)

[\[j30\]](https://dblp.org/pid/05/7576.html#j30) [\[c28\]](https://dblp.org/pid/05/7576.html#c28)

[81](https://dblp.org/pid/05/7576.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Kitti Thamrongaphichartkul](https://dblp.org/pid/380/6731.html)

[\[j48\]](https://dblp.org/pid/05/7576.html#j48)

[82](https://dblp.org/pid/05/7576.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Weerapong Thanapongtharm](https://dblp.org/pid/288/4253.html)

[\[j42\]](https://dblp.org/pid/05/7576.html#j42) [\[j20\]](https://dblp.org/pid/05/7576.html#j20)

[83](https://dblp.org/pid/05/7576.html?view=joint&param=83 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=3)

[Peeraya Thanomboon](https://dblp.org/pid/280/5557.html)

[\[c19\]](https://dblp.org/pid/05/7576.html#c19)

[84](https://dblp.org/pid/05/7576.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Kittikhun Thongkanchorn](https://dblp.org/pid/280/7600.html)

[\[j43\]](https://dblp.org/pid/05/7576.html#j43) [\[j42\]](https://dblp.org/pid/05/7576.html#j42) [\[j37\]](https://dblp.org/pid/05/7576.html#j37) [\[j36\]](https://dblp.org/pid/05/7576.html#j36) [\[j31\]](https://dblp.org/pid/05/7576.html#j31) [\[j30\]](https://dblp.org/pid/05/7576.html#j30) [\[c30\]](https://dblp.org/pid/05/7576.html#c30) [\[c28\]](https://dblp.org/pid/05/7576.html#c28) [\[j22\]](https://dblp.org/pid/05/7576.html#j22) [\[j21\]](https://dblp.org/pid/05/7576.html#j21) [\[j19\]](https://dblp.org/pid/05/7576.html#j19) [\[j12\]](https://dblp.org/pid/05/7576.html#j12)

[85](https://dblp.org/pid/05/7576.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Kittin Thongsrimoung](https://dblp.org/pid/425/6191.html)

[\[j42\]](https://dblp.org/pid/05/7576.html#j42)

[86](https://dblp.org/pid/05/7576.html?view=joint&param=86 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=3)

[Benjarat Tirasirichai](https://dblp.org/pid/280/4826.html)

[\[c19\]](https://dblp.org/pid/05/7576.html#c19)

[87](https://dblp.org/pid/05/7576.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Pimsiri Tiyayon](https://dblp.org/pid/408/3285.html)

[\[j43\]](https://dblp.org/pid/05/7576.html#j43)

[88](https://dblp.org/pid/05/7576.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Trongtum Tongdee](https://dblp.org/pid/259/3204.html)

[\[j33\]](https://dblp.org/pid/05/7576.html#j33)

[89](https://dblp.org/pid/05/7576.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Pimchanok Tuakta](https://dblp.org/pid/316/6452.html)

[\[j45\]](https://dblp.org/pid/05/7576.html#j45) [\[j37\]](https://dblp.org/pid/05/7576.html#j37) [\[j35\]](https://dblp.org/pid/05/7576.html#j35) [\[j31\]](https://dblp.org/pid/05/7576.html#j31) [\[j30\]](https://dblp.org/pid/05/7576.html#j30) [\[c28\]](https://dblp.org/pid/05/7576.html#c28)

[90](https://dblp.org/pid/05/7576.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Sirawich Vachmanus](https://dblp.org/pid/278/0854.html)

[\[j48\]](https://dblp.org/pid/05/7576.html#j48)

[91](https://dblp.org/pid/05/7576.html?view=joint&param=91 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=3)

[Jos Vanrenterghem](https://dblp.org/pid/165/1686.html)

[\[c9\]](https://dblp.org/pid/05/7576.html#c9)

[92](https://dblp.org/pid/05/7576.html?view=joint&param=92 "show joint publications")

[![5](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=5)

[Wantanee Viriyasitavat](https://dblp.org/pid/03/3950.html)

[\[j8\]](https://dblp.org/pid/05/7576.html#j8)

[93](https://dblp.org/pid/05/7576.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Suwimol Wahakit](https://dblp.org/pid/346/4699.html)

[\[j19\]](https://dblp.org/pid/05/7576.html#j19)

[94](https://dblp.org/pid/05/7576.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Liang Wang 0001](https://dblp.org/pid/56/4499-1.html)

[\[j5\]](https://dblp.org/pid/05/7576.html#j5)

[95](https://dblp.org/pid/05/7576.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Disathon Wattanadhirach](https://dblp.org/pid/247/3899.html)

[\[j30\]](https://dblp.org/pid/05/7576.html#j30) [\[c28\]](https://dblp.org/pid/05/7576.html#c28)

[96](https://dblp.org/pid/05/7576.html?view=joint&param=96 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=4)

[Peemongkon Wattananon](https://dblp.org/pid/245/6646.html)

[\[c15\]](https://dblp.org/pid/05/7576.html#c15)

[97](https://dblp.org/pid/05/7576.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Anuwat Wiratsudakul](https://dblp.org/pid/179/2075.html)

[\[c30\]](https://dblp.org/pid/05/7576.html#c30) [\[j21\]](https://dblp.org/pid/05/7576.html#j21) [\[j20\]](https://dblp.org/pid/05/7576.html#j20) [\[j12\]](https://dblp.org/pid/05/7576.html#j12) [\[c20\]](https://dblp.org/pid/05/7576.html#c20)

[98](https://dblp.org/pid/05/7576.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Kontawat Wisetpaitoon](https://dblp.org/pid/377/4052.html)

[\[j42\]](https://dblp.org/pid/05/7576.html#j42)

[99](https://dblp.org/pid/05/7576.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Jitsupa Wongsripuemtet](https://dblp.org/pid/414/0268.html)

[\[j44\]](https://dblp.org/pid/05/7576.html#j44)

[100](https://dblp.org/pid/05/7576.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Qiang Wu 0001](https://dblp.org/pid/87/2533-1.html)

[\[j29\]](https://dblp.org/pid/05/7576.html#j29) [\[j24\]](https://dblp.org/pid/05/7576.html#j24) [\[j23\]](https://dblp.org/pid/05/7576.html#j23) [\[j18\]](https://dblp.org/pid/05/7576.html#j18) [\[j16\]](https://dblp.org/pid/05/7576.html#j16) [\[c27\]](https://dblp.org/pid/05/7576.html#c27) [\[j10\]](https://dblp.org/pid/05/7576.html#j10) [\[c21\]](https://dblp.org/pid/05/7576.html#c21) [\[c13\]](https://dblp.org/pid/05/7576.html#c13) [\[c12\]](https://dblp.org/pid/05/7576.html#c12) [\[j5\]](https://dblp.org/pid/05/7576.html#j5) [\[j4\]](https://dblp.org/pid/05/7576.html#j4) [\[c8\]](https://dblp.org/pid/05/7576.html#c8) [\[j3\]](https://dblp.org/pid/05/7576.html#j3) [\[j2\]](https://dblp.org/pid/05/7576.html#j2) [\[j1\]](https://dblp.org/pid/05/7576.html#j1) [\[c7\]](https://dblp.org/pid/05/7576.html#c7) [\[c6\]](https://dblp.org/pid/05/7576.html#c6) [\[c5\]](https://dblp.org/pid/05/7576.html#c5) [\[c4\]](https://dblp.org/pid/05/7576.html#c4) [\[c3\]](https://dblp.org/pid/05/7576.html#c3) [\[c1\]](https://dblp.org/pid/05/7576.html#c1)

[101](https://dblp.org/pid/05/7576.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Jingsong Xu](https://dblp.org/pid/118/9311.html)

[\[j24\]](https://dblp.org/pid/05/7576.html#j24) [\[j23\]](https://dblp.org/pid/05/7576.html#j23) [\[c27\]](https://dblp.org/pid/05/7576.html#c27)

[102](https://dblp.org/pid/05/7576.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[j16\]](https://dblp.org/pid/05/7576.html#j16)

[103](https://dblp.org/pid/05/7576.html?view=joint&param=103 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=3)

[Duangkamol Yangchaem](https://dblp.org/pid/165/1905.html)

[\[c11\]](https://dblp.org/pid/05/7576.html#c11) [\[c9\]](https://dblp.org/pid/05/7576.html#c9)

[104](https://dblp.org/pid/05/7576.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Terdsak Yano](https://dblp.org/pid/425/6980.html)

[\[j42\]](https://dblp.org/pid/05/7576.html#j42)

[105](https://dblp.org/pid/05/7576.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Lingxiang Yao](https://dblp.org/pid/207/9512.html)

[\[j29\]](https://dblp.org/pid/05/7576.html#j29) [\[j24\]](https://dblp.org/pid/05/7576.html#j24) [\[j23\]](https://dblp.org/pid/05/7576.html#j23) [\[j18\]](https://dblp.org/pid/05/7576.html#j18) [\[j16\]](https://dblp.org/pid/05/7576.html#j16) [\[c27\]](https://dblp.org/pid/05/7576.html#c27) [\[c21\]](https://dblp.org/pid/05/7576.html#c21) [\[c12\]](https://dblp.org/pid/05/7576.html#c12)

[106](https://dblp.org/pid/05/7576.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Boonsit Yimwadsana](https://dblp.org/pid/72/6575.html)

[\[c29\]](https://dblp.org/pid/05/7576.html#c29)

[107](https://dblp.org/pid/05/7576.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Pakorn Yodprom](https://dblp.org/pid/295/4105.html)

[\[j33\]](https://dblp.org/pid/05/7576.html#j33)

[108](https://dblp.org/pid/05/7576.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Nutcha Yodrabum](https://dblp.org/pid/345/0964.html)

[\[j39\]](https://dblp.org/pid/05/7576.html#j39)

[109](https://dblp.org/pid/05/7576.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Chawapat Youngjitikornkun](https://dblp.org/pid/288/4207.html)

[\[j20\]](https://dblp.org/pid/05/7576.html#j20)

[110](https://dblp.org/pid/05/7576.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Jian Zhang 0002](https://dblp.org/pid/07/314-2.html)

[\[j29\]](https://dblp.org/pid/05/7576.html#j29) [\[j24\]](https://dblp.org/pid/05/7576.html#j24) [\[j23\]](https://dblp.org/pid/05/7576.html#j23) [\[j18\]](https://dblp.org/pid/05/7576.html#j18) [\[j16\]](https://dblp.org/pid/05/7576.html#j16) [\[c27\]](https://dblp.org/pid/05/7576.html#c27) [\[j10\]](https://dblp.org/pid/05/7576.html#j10) [\[c21\]](https://dblp.org/pid/05/7576.html#c21) [\[c13\]](https://dblp.org/pid/05/7576.html#c13) [\[c12\]](https://dblp.org/pid/05/7576.html#c12) [\[j5\]](https://dblp.org/pid/05/7576.html#j5) [\[j4\]](https://dblp.org/pid/05/7576.html#j4) [\[c8\]](https://dblp.org/pid/05/7576.html#c8) [\[j3\]](https://dblp.org/pid/05/7576.html#j3) [\[j2\]](https://dblp.org/pid/05/7576.html#j2) [\[j1\]](https://dblp.org/pid/05/7576.html#j1) [\[c7\]](https://dblp.org/pid/05/7576.html#c7) [\[c6\]](https://dblp.org/pid/05/7576.html#c6) [\[c5\]](https://dblp.org/pid/05/7576.html#c5) [\[c4\]](https://dblp.org/pid/05/7576.html#c4) [\[c3\]](https://dblp.org/pid/05/7576.html#c3) [\[c2\]](https://dblp.org/pid/05/7576.html#c2) [\[c1\]](https://dblp.org/pid/05/7576.html#c1)

[111](https://dblp.org/pid/05/7576.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/05/7576.html?view=group&param=1)

[Peng Zhang 0057](https://dblp.org/pid/21/1048-57.html)

[\[j29\]](https://dblp.org/pid/05/7576.html#j29)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/05/7576.html#) [\[–\]](https://dblp.org/pid/05/7576.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/05/7576.html#) [\[–\]](https://dblp.org/pid/05/7576.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/05/7576.html#) [\[–\]](https://dblp.org/pid/05/7576.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/05/7576.html#) [\[–\]](https://dblp.org/pid/05/7576.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/05/7576.html#) [\[–\]](https://dblp.org/pid/05/7576.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)