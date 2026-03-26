> 抓取来源：https://dblp.org/pid/117/6314.html

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

- _affiliation:_ ETH Zurich, Switzerland
- _affiliation (former):_ University of California Berkeley, CA, USA
- _affiliation (PhD):_ Princeton University, NJ, USA

- [Fisher Yu 0002](https://dblp.org/pid/117/6314-2.html) — BabylonChain
- [Fisher Yu 0003](https://dblp.org/pid/405/3455.html) — Huawei

- [Mingchao Fisher Yu](https://dblp.org/pid/233/8956.html) — Australian National University, Canberra, Australia

🛈 Please note that only 70% of the items listed on this page have a DOI stored with their dblp record. Therefore, DOI-based queries can only provide partial results.

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Fisher+Yu+0001%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F117%2F6314%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Fisher+Yu+0001+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F117%2F6314%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Fisher+Yu+0001+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F117%2F6314%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Fisher+Yu+0001%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F117%2F6314%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Fisher+Yu+0001+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F117%2F6314%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Fisher+Yu+0001%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F117%2F6314%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Fisher+Yu+0001%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F117%2F6314%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F117%2F6314%3E+%7D+.%0A%0A%7D)

_showing all202 records_

20122025602012: 12014: 12015: 42015: 42016: 72016: 72016: 72017: 112017: 112018: 172018: 172019: 102019: 102020: 52020: 52021: 232021: 232022: 372022: 372022: 372023: 602023: 602023: 602024: 232024: 232024: 232025: 32025: 3

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

- ![](https://dblp.org/img/add-mark.12x12.png)Luc Van Gool (50)
- ![](https://dblp.org/img/add-mark.12x12.png)Martin Danelljan (50)
- ![](https://dblp.org/img/add-mark.12x12.png)Trevor Darrell (39)
- ![](https://dblp.org/img/add-mark.12x12.png)Lei Ke (22)
- ![](https://dblp.org/img/add-mark.12x12.png)Xin Wang 0066 (18)
- ![](https://dblp.org/img/add-mark.12x12.png)Mattia Segù (18)
- ![](https://dblp.org/img/add-mark.12x12.png)Chi-Keung Tang (17)
- ![](https://dblp.org/img/add-mark.12x12.png)Yu-Wing Tai (17)
- ![](https://dblp.org/img/add-mark.12x12.png)Christos Sakaridis (15)
- ![](https://dblp.org/img/add-mark.12x12.png)Thomas E. Huang (14)

- _531 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (193)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0001-8829-7344 (9)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (93)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (29)
- ![](https://dblp.org/img/add-mark.12x12.png)ICCV (18)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (12)
- ![](https://dblp.org/img/add-mark.12x12.png)ECCV (11)
- ![](https://dblp.org/img/add-mark.12x12.png)PMLR (8)
- ![](https://dblp.org/img/add-mark.12x12.png)ICML (6)
- ![](https://dblp.org/img/add-mark.12x12.png)IROS (6)
- ![](https://dblp.org/img/add-mark.12x12.png)WACV (5)
- ![](https://dblp.org/img/add-mark.12x12.png)ICRA (5)
- ![](https://dblp.org/img/add-mark.12x12.png)ICLR (5)

- _14 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)open (121)
- ![](https://dblp.org/img/add-mark.12x12.png)closed (81)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[j10\]
[Christos Sakaridis](https://dblp.org/pid/188/5858.html)![](https://dblp.org/img/orcid-mark.12x12.png), [David Brüggemann](https://dblp.org/pid/271/0154.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Condition-Invariant Semantic Segmentation. [IEEE Trans. Pattern Anal. Mach. Intell.47(4)](https://dblp.org/db/journals/pami/pami47.html#journals/pami/SakaridisBYG25): 3111-3125 (2025)
- ![](https://dblp.org/img/n.png)

\[j9\]
[Wenguan Wang](https://dblp.org/pid/145/1078.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hengshuang Zhao](https://dblp.org/pid/185/7848.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xinggang Wang](https://dblp.org/pid/95/3056.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu, [David Crandall](https://dblp.org/pid/c/DavidCrandall.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Guest Editorial Introduction to the Special Issue on Segment Anything for Videos and Beyond. [IEEE Trans. Circuits Syst. Video Technol.35(4)](https://dblp.org/db/journals/tcsv/tcsv35.html#journals/tcsv/WangZWYC25): 2947-2950 (2025)
- ![](https://dblp.org/img/n.png)

\[c99\]
[Frano Rajic](https://dblp.org/pid/331/2107.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

Segment Anything Meets Point Tracking. [WACV2025](https://dblp.org/db/conf/wacv/wacv2025.html#conf/wacv/RajicKTTD025): 9302-9311
- 2024
- ![](https://dblp.org/img/n.png)

\[j8\]
[Zhiyuan Wu](https://dblp.org/pid/60/5001.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Feng](https://dblp.org/pid/39/6758.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chuangwei Liu](https://dblp.org/pid/328/8854.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu![](https://dblp.org/img/orcid-mark.12x12.png), [Qijun Chen](https://dblp.org/pid/75/1639.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rui Fan](https://dblp.org/pid/03/1805-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

S$^{3}$M-Net: Joint Learning of Semantic Segmentation and Stereo Matching for Autonomous Driving. [IEEE Trans. Intell. Veh.9(2)](https://dblp.org/db/journals/tiv/tiv9.html#journals/tiv/WuFLYCF24): 3940-3951 (2024)
- ![](https://dblp.org/img/n.png)

\[c98\]
[Sanghwan Kim](https://dblp.org/pid/60/10274.html), [Hao Tang](https://dblp.org/pid/07/5751-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu:

Distilling ODE Solvers of Diffusion Models into Smaller Steps. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/KimT024): 9410-9419
- ![](https://dblp.org/img/n.png)

\[c97\]
[Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Yung-Hsu Yang](https://dblp.org/pid/288/0092.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), Fisher Yu:

UniDepth: Universal Monocular Metric Depth Estimation. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/PiccinelliYSSLG24): 10106-10116
- ![](https://dblp.org/img/n.png)

\[c96\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), Fisher Yu:

Matching Anything by Segmenting Anything. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/LiKDPSG024): 18963-18973
- ![](https://dblp.org/img/n.png)

\[c95\]
[Haofei Xu](https://dblp.org/pid/236/6248.html), [Anpei Chen](https://dblp.org/pid/210/2592.html), [Yuedong Chen](https://dblp.org/pid/236/6258.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Marc Pollefeys](https://dblp.org/pid/p/MarcPollefeys.html), [Andreas Geiger](https://dblp.org/pid/40/5825-1.html), Fisher Yu:

MuRF: Multi-Baseline Radiance Fields. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/XuCCSZP0024): 20041-20050
- ![](https://dblp.org/img/n.png)

\[c94\]
[Mattia Segù](https://dblp.org/pid/245/2565.html), [Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), Fisher Yu, [Bernt Schiele](https://dblp.org/pid/s/BerntSchiele.html):

Walker: Self-supervised Multiple Object Tracking by Walking on Temporal Appearance Graphs. [ECCV (8)2024](https://dblp.org/db/conf/eccv/eccv2024-8.html#conf/eccv/SeguPLGYS24): 1-18
- ![](https://dblp.org/img/n.png)

\[c93\]
[Mingqiao Ye](https://dblp.org/pid/285/9253.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu, [Lei Ke](https://dblp.org/pid/26/5225.html):

Gaussian Grouping: Segment and Edit Anything in 3D Scenes. [ECCV (29)2024](https://dblp.org/db/conf/eccv/eccv2024-29.html#conf/eccv/YeDYK24): 162-179
- ![](https://dblp.org/img/n.png)

\[c92\]
[Xiang Zhang](https://dblp.org/pid/91/4353-22.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu![](https://dblp.org/img/orcid-mark.12x12.png):

HiT-SR: Hierarchical Transformer for Efficient Image Super-Resolution. [ECCV (40)2024](https://dblp.org/db/conf/eccv/eccv2024-40.html#conf/eccv/ZhangZY24): 483-500
- ![](https://dblp.org/img/n.png)

\[c91\]
[Chunming He](https://dblp.org/pid/251/5104.html), [Kai Li](https://dblp.org/pid/l/KaiLi12.html), [Yachao Zhang](https://dblp.org/pid/40/10584-1.html), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Chenyu You](https://dblp.org/pid/191/9432.html), [Zhenhua Guo](https://dblp.org/pid/41/294-1.html), [Xiu Li](https://dblp.org/pid/13/1206-1.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

Strategic Preys Make Acute Predators: Enhancing Camouflaged Object Detectors by Generating Camouflaged Objects. [ICLR2024](https://dblp.org/db/conf/iclr/iclr2024.html#conf/iclr/HeLZZY0LD024)
- ![](https://dblp.org/img/n.png)

\[c90\]
[Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Haotong Qin](https://dblp.org/pid/262/3626.html), [Zixiang Zhao](https://dblp.org/pid/65/5420.html), [Xianglong Liu](https://dblp.org/pid/55/7901-1.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

Flexible Residual Binarization for Image Super-Resolution. [ICML2024](https://dblp.org/db/conf/icml/icml2024.html#conf/icml/ZhangQZ0D024): 59731-59740
- ![](https://dblp.org/img/n.png)

\[c89\]
[Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Kai Zhang](https://dblp.org/pid/55/957-8.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

Lightweight Image Super-Resolution via Flexible Meta Pruning. [ICML2024](https://dblp.org/db/conf/icml/icml2024.html#conf/icml/Zhang0GD024): 60305-60314
- ![](https://dblp.org/img/n.png)

\[c88\]
[René Zurbrügg](https://dblp.org/pid/292/2398.html), [Yifan Liu](https://dblp.org/pid/23/4955-1.html), [Francis Engelmann](https://dblp.org/pid/181/4077.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Suryansh Kumar](https://dblp.org/pid/124/2783.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Marco Hutter](https://dblp.org/pid/04/2753.html), [Vaishakh Patil](https://dblp.org/pid/255/5070.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu:

ICGNet: A Unified Approach for Instance-Centric Grasping. [ICRA2024](https://dblp.org/db/conf/icra/icra2024.html#conf/icra/Zurbrugg0E00P024): 4140-4146
- ![](https://dblp.org/img/n.png)

\[c87\]
[Yutong Hu](https://dblp.org/pid/199/9967-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kehan Wen](https://dblp.org/pid/372/4822.html), Fisher Yu:

DexDribbler: Learning Dexterous Soccer Manipulation via Dynamic Supervision. [IROS2024](https://dblp.org/db/conf/iros/iros2024.html#conf/iros/0006W024): 12910-12917
- ![](https://dblp.org/img/n.png)

\[c86\]
[Xavier Timoneda](https://dblp.org/pid/224/0074.html), [Markus Herb](https://dblp.org/pid/210/8215.html), [Fabian Duerr](https://dblp.org/pid/282/8598.html), [Daniel Goehring](https://dblp.org/pid/97/3289.html), Fisher Yu:

Multi-modal NeRF Self-Supervision for LiDAR Semantic Segmentation. [IROS2024](https://dblp.org/db/conf/iros/iros2024.html#conf/iros/TimonedaHDGY24): 12939-12946
- ![](https://dblp.org/img/n.png)

\[c85\]
[Yiming Li](https://dblp.org/pid/l/YimingLi-3.html), [Sihang Li](https://dblp.org/pid/137/6318-1.html), [Xinhao Liu](https://dblp.org/pid/126/4582-3.html), [Moonjun Gong](https://dblp.org/pid/349/4889.html), [Kenan Li](https://dblp.org/pid/193/9514.html), [Nuo Chen](https://dblp.org/pid/135/5622-3.html), [Zijun Wang](https://dblp.org/pid/93/1955.html), [Zhiheng Li](https://dblp.org/pid/89/6935.html), [Tao Jiang](https://dblp.org/pid/181/2813.html), Fisher Yu, [Yue Wang](https://dblp.org/pid/33/4822-41.html), [Hang Zhao](https://dblp.org/pid/31/2950-21.html), [Zhiding Yu](https://dblp.org/pid/67/5386.html), [Chen Feng](https://dblp.org/pid/01/161-2.html):

SSCBench: A Large-Scale 3D Semantic Scene Completion Benchmark for Autonomous Driving. [IROS2024](https://dblp.org/db/conf/iros/iros2024.html#conf/iros/LiLLGL0WLJ0WZY024): 13333-13340
- ![](https://dblp.org/img/n.png)

\[i93\]
[René Zurbrügg](https://dblp.org/pid/292/2398.html), [Yifan Liu](https://dblp.org/pid/23/4955-1.html), [Francis Engelmann](https://dblp.org/pid/181/4077.html), [Suryansh Kumar](https://dblp.org/pid/124/2783.html), [Marco Hutter](https://dblp.org/pid/04/2753.html), [Vaishakh Patil](https://dblp.org/pid/255/5070.html), Fisher Yu:

ICGNet: A Unified Approach for Instance-Centric Grasping. [CoRRabs/2401.09939](https://dblp.org/db/journals/corr/corr2401.html#journals/corr/abs-2401-09939) (2024)
- ![](https://dblp.org/img/n.png)

\[i92\]
[Zhiyuan Wu](https://dblp.org/pid/60/5001.html), [Yi Feng](https://dblp.org/pid/39/6758.html), [Chuangwei Liu](https://dblp.org/pid/328/8854.html), Fisher Yu, [Qijun Chen](https://dblp.org/pid/75/1639.html), [Rui Fan](https://dblp.org/pid/03/1805-1.html):

S3M-Net: Joint Learning of Semantic Segmentation and Stereo Matching for Autonomous Driving. [CoRRabs/2401.11414](https://dblp.org/db/journals/corr/corr2401.html#journals/corr/abs-2401-11414) (2024)
- ![](https://dblp.org/img/n.png)

\[i91\]
[Yutong Hu](https://dblp.org/pid/199/9967-1.html), [Kehan Wen](https://dblp.org/pid/372/4822.html), Fisher Yu:

DexDribbler: Learning Dexterous Soccer Manipulation via Dynamic Supervision. [CoRRabs/2403.14300](https://dblp.org/db/journals/corr/corr2403.html#journals/corr/abs-2403-14300) (2024)
- ![](https://dblp.org/img/n.png)

\[i90\]
[Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Yung-Hsu Yang](https://dblp.org/pid/288/0092.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), Fisher Yu:

UniDepth: Universal Monocular Metric Depth Estimation. [CoRRabs/2403.18913](https://dblp.org/db/journals/corr/corr2403.html#journals/corr/abs-2403-18913) (2024)
- ![](https://dblp.org/img/n.png)

\[i89\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), Fisher Yu:

Matching Anything by Segmenting Anything. [CoRRabs/2406.04221](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-04221) (2024)
- ![](https://dblp.org/img/n.png)

\[i88\]
[Xiang Zhang](https://dblp.org/pid/91/4353-22.html), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html), Fisher Yu:

HiT-SR: Hierarchical Transformer for Efficient Image Super-Resolution. [CoRRabs/2407.05878](https://dblp.org/db/journals/corr/corr2407.html#journals/corr/abs-2407-05878) (2024)
- ![](https://dblp.org/img/n.png)

\[i87\]
[Mattia Segù](https://dblp.org/pid/245/2565.html), [Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), Fisher Yu, [Bernt Schiele](https://dblp.org/pid/s/BerntSchiele.html):

Walker: Self-supervised Multiple Object Tracking by Walking on Temporal Appearance Graphs. [CoRRabs/2409.17221](https://dblp.org/db/journals/corr/corr2409.html#journals/corr/abs-2409-17221) (2024)
- ![](https://dblp.org/img/n.png)

\[i86\]
[Xavier Timoneda](https://dblp.org/pid/224/0074.html), [Markus Herb](https://dblp.org/pid/210/8215.html), [Fabian Duerr](https://dblp.org/pid/282/8598.html), [Daniel Goehring](https://dblp.org/pid/97/3289.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu:

Multi-modal NeRF Self-Supervision for LiDAR Semantic Segmentation. [CoRRabs/2411.02969](https://dblp.org/db/journals/corr/corr2411.html#journals/corr/abs-2411-02969) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j7\]
[Hou-Ning Hu](https://dblp.org/pid/199/3014.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yung-Hsu Yang](https://dblp.org/pid/288/0092.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tobias Fischer](https://dblp.org/pid/249/9213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu![](https://dblp.org/img/orcid-mark.12x12.png), [Min Sun](https://dblp.org/pid/62/2750-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Monocular Quasi-Dense 3D Object Tracking. [IEEE Trans. Pattern Anal. Mach. Intell.45(2)](https://dblp.org/db/journals/pami/pami45.html#journals/pami/HuYFDYS23): 1992-2008 (2023)
- ![](https://dblp.org/img/n.png)

\[j6\]
[Haofei Xu](https://dblp.org/pid/236/6248.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Zhang](https://dblp.org/pid/05/3499-37.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianfei Cai](https://dblp.org/pid/83/6096.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hamid Rezatofighi](https://dblp.org/pid/37/8192.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu![](https://dblp.org/img/orcid-mark.12x12.png), [Dacheng Tao](https://dblp.org/pid/46/3391.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Andreas Geiger](https://dblp.org/pid/40/5825-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Unifying Flow, Stereo and Depth Estimation. [IEEE Trans. Pattern Anal. Mach. Intell.45(11)](https://dblp.org/db/journals/pami/pami45.html#journals/pami/XuZCRYTG23): 13941-13958 (2023)
- ![](https://dblp.org/img/n.png)

\[j5\]
[Tobias Fischer](https://dblp.org/pid/249/9213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thomas E. Huang](https://dblp.org/pid/260/6642.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiangmiao Pang](https://dblp.org/pid/231/7630.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Linlu Qiu](https://dblp.org/pid/267/2348.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haofeng Chen](https://dblp.org/pid/120/5331.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu![](https://dblp.org/img/orcid-mark.12x12.png):

QDTrack: Quasi-Dense Similarity Learning for Appearance-Only Multiple Object Tracking. [IEEE Trans. Pattern Anal. Mach. Intell.45(12)](https://dblp.org/db/journals/pami/pami45.html#journals/pami/FischerHPQCDY23): 15380-15393 (2023)
- ![](https://dblp.org/img/n.png)

\[j4\]
[Weirong Chen](https://dblp.org/pid/96/398.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Suryansh Kumar](https://dblp.org/pid/124/2783.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu![](https://dblp.org/img/orcid-mark.12x12.png):

Uncertainty-Driven Dense Two-View Structure From Motion. [IEEE Robotics Autom. Lett.8(3)](https://dblp.org/db/journals/ral/ral8.html#journals/ral/ChenKY23): 1763-1770 (2023)
- ![](https://dblp.org/img/n.png)

\[c84\]
[Jan Ackermann](https://dblp.org/pid/348/6561.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html), Fisher Yu:

Maskomaly: Zero-Shot Mask Anomaly Segmentation. [BMVC2023](https://dblp.org/db/conf/bmvc/bmvc2023.html#conf/bmvc/AckermannS023): 329
- ![](https://dblp.org/img/n.png)

\[c83\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Tobias Fischer](https://dblp.org/pid/249/9213.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

OVTrack: Open-Vocabulary Multiple Object Tracking. [CVPR2023](https://dblp.org/db/conf/cvpr/cvpr2023.html#conf/cvpr/Li0KDDY23): 5567-5577
- ![](https://dblp.org/img/n.png)

\[c82\]
[Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu:

iDisc: Internal Discretization for Monocular Depth Estimation. [CVPR2023](https://dblp.org/db/conf/cvpr/cvpr2023.html#conf/cvpr/PiccinelliSY23): 21477-21487
- ![](https://dblp.org/img/n.png)

\[c81\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Fisher Yu:

Mask-Free Video Instance Segmentation. [CVPR2023](https://dblp.org/db/conf/cvpr/cvpr2023.html#conf/cvpr/KeDDTTY23): 22857-22866
- ![](https://dblp.org/img/n.png)

\[c80\]
[Zhizheng Liu](https://dblp.org/pid/287/4356.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mattia Segù](https://dblp.org/pid/245/2565.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu![](https://dblp.org/img/orcid-mark.12x12.png):

COOLer: Class-Incremental Learning for Appearance-Based Multiple Object Tracking. [DAGM2023](https://dblp.org/db/conf/dagm/dagm2023.html#conf/dagm/LiuSY23): 443-458
- ![](https://dblp.org/img/n.png)

\[c79\]
[Aron Schmied](https://dblp.org/pid/355/5910.html), [Tobias Fischer](https://dblp.org/pid/249/9213.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Marc Pollefeys](https://dblp.org/pid/p/MarcPollefeys.html), Fisher Yu:

R3D3: Dense 3D Reconstruction of Dynamic Scenes from Multiple Cameras. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/Schmied0DP023): 3193-3203
- ![](https://dblp.org/img/n.png)

\[c78\]
[Changyong Shu](https://dblp.org/pid/239/5094.html), [Jiajun Deng](https://dblp.org/pid/137/6093.html), Fisher Yu, [Yifan Liu](https://dblp.org/pid/23/4955-1.html):

3DPPE: 3D Point Positional Encoding for Transformer-based Multi-Camera 3D Object Detection. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/ShuD0023): 3557-3566
- ![](https://dblp.org/img/n.png)

\[c77\]
[Mingqiao Ye](https://dblp.org/pid/285/9253.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

Cascade-DETR: Delving into High-Quality Universal Object Detection. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/YeKLTTD023): 6681-6691
- ![](https://dblp.org/img/n.png)

\[c76\]
[Thomas E. Huang](https://dblp.org/pid/260/6642.html), [Yifan Liu](https://dblp.org/pid/23/4955-1.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), Fisher Yu:

Video Task Decathlon: Unifying Image and Video Tasks in Autonomous Driving. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/Huang0G023): 8613-8623
- ![](https://dblp.org/img/n.png)

\[c75\]
[Mattia Segù](https://dblp.org/pid/245/2565.html), [Bernt Schiele](https://dblp.org/pid/s/BerntSchiele.html), Fisher Yu:

DARTH: Holistic Test-time Adaptation for Multiple Object Tracking. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/SeguS023): 9683-9693
- ![](https://dblp.org/img/n.png)

\[c74\]
[Zheng Chen](https://dblp.org/pid/33/2592-14.html), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Jinjin Gu](https://dblp.org/pid/209/5709.html), [Linghe Kong](https://dblp.org/pid/23/7909.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaokang Yang](https://dblp.org/pid/06/3071-1.html), Fisher Yu:

Dual Aggregation Transformer for Image Super-Resolution. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/0014ZGKY023): 12278-12287
- ![](https://dblp.org/img/n.png)

\[c73\]
[Georg Heigold](https://dblp.org/pid/46/2236.html), [Daniel Keysers](https://dblp.org/pid/02/6955.html), [Matthias Minderer](https://dblp.org/pid/243/3155.html), [Mario Lucic](https://dblp.org/pid/155/1945.html), [Alexey A. Gritsenko](https://dblp.org/pid/30/11478.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu, [Alex Bewley](https://dblp.org/pid/39/9969.html), [Thomas Kipf](https://dblp.org/pid/186/8206.html):

Video OWL-ViT: Temporally-consistent open-world localization in video. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/HeigoldKMLG0BK23): 13756-13765
- ![](https://dblp.org/img/n.png)

\[c72\]
[Lucas Morin](https://dblp.org/pid/309/7785.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Maria Isabel Agea](https://dblp.org/pid/355/2674.html), [Ahmed S. Nassar](https://dblp.org/pid/321/9993.html), [Valéry Weber](https://dblp.org/pid/86/5323.html), [Ingmar Meijer](https://dblp.org/pid/46/5951.html), [Peter W. J. Staar](https://dblp.org/pid/136/7966.html), Fisher Yu:

MolGrapher: Graph-based Visual Recognition of Chemical Structures. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/MorinDANWMS023): 19495-19504
- ![](https://dblp.org/img/n.png)

\[c71\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Khanh-Tung Tran](https://dblp.org/pid/359/3793.html), [Xuan-Son Vu](https://dblp.org/pid/151/8673.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Noor Al-Shakarji](https://dblp.org/pid/188/7419.html), [Dong An](https://dblp.org/pid/02/7028.html), [Michael Arens](https://dblp.org/pid/69/5391.html), [Stefan Becker](https://dblp.org/pid/62/7091.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Sebastian Bullinger](https://dblp.org/pid/197/9724.html), [Antoni B. Chan](https://dblp.org/pid/55/5814.html), [Shijie Chang](https://dblp.org/pid/277/8125.html), [Hanyuan Chen](https://dblp.org/pid/363/8621.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Yan Chen](https://dblp.org/pid/88/2827-17.html), [Zhenyu Chen](https://dblp.org/pid/86/541-1.html), [Yangming Cheng](https://dblp.org/pid/340/1285.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Chunyuan Deng](https://dblp.org/pid/154/4071.html), [Jiahua Dong](https://dblp.org/pid/247/5746.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Jianlong Fu](https://dblp.org/pid/83/8692.html), [Jie Gao](https://dblp.org/pid/181/2794.html), [Ruize Han](https://dblp.org/pid/205/4022.html), [Zeqi Hao](https://dblp.org/pid/348/8961.html), [Jun-Yan He](https://dblp.org/pid/173/3747.html), [Keji He](https://dblp.org/pid/319/4518.html), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Xiantao Hu](https://dblp.org/pid/160/8016.html), [Kaer Huang](https://dblp.org/pid/317/0780.html), [Yuqing Huang](https://dblp.org/pid/134/5853.html), [Yi Jiang](https://dblp.org/pid/66/3172-4.html), [Ben Kang](https://dblp.org/pid/340/1671.html), [Jin-Peng Lan](https://dblp.org/pid/332/1033.html), [Hyungjun Lee](https://dblp.org/pid/324/8911.html), [Chenyang Li](https://dblp.org/pid/15/1523-7.html), [Jiahao Li](https://dblp.org/pid/150/5524-5.html), [Ning Li](https://dblp.org/pid/14/5410-44.html), [Wangkai Li](https://dblp.org/pid/340/1456.html), [Xiaodi Li](https://dblp.org/pid/63/7279.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Pengyu Liu](https://dblp.org/pid/73/7783-5.html), [Yue Liu](https://dblp.org/pid/74/1932.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Bin Luo](https://dblp.org/pid/36/4256-8.html), [Ping Luo](https://dblp.org/pid/54/4989-2.html), [Yinchao Ma](https://dblp.org/pid/189/1326.html), [Deshui Miao](https://dblp.org/pid/307/5501.html), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Kannappan Palaniappan](https://dblp.org/pid/21/700.html), [Hancheol Park](https://dblp.org/pid/161/3495.html), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Zekun Qian](https://dblp.org/pid/315/4066.html), [Gani Rahmon](https://dblp.org/pid/291/7224.html), [Norbert Scherer-Negenborn](https://dblp.org/pid/45/8662.html), [Pengcheng Shao](https://dblp.org/pid/364/8295.html), [Wooksu Shin](https://dblp.org/pid/327/3602.html), [Elham Soltani Kazemi](https://dblp.org/pid/318/1851.html), [Tianhui Song](https://dblp.org/pid/181/8738.html), [Rainer Stiefelhagen](https://dblp.org/pid/31/4699.html), [Rui Sun](https://dblp.org/pid/01/3595-6.html), [Chuanming Tang](https://dblp.org/pid/237/6254.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html), [Imad Eddine Toubal](https://dblp.org/pid/292/6360.html), [Jack Valmadre](https://dblp.org/pid/50/8535.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Jash Vira](https://dblp.org/pid/364/8266.html), [Stéphane Vujasinovic](https://dblp.org/pid/237/5053.html), [Cheng Wan](https://dblp.org/pid/118/7267-6.html), [Jia Wan](https://dblp.org/pid/13/6504-1.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Feifan Wang](https://dblp.org/pid/213/0685.html), [He Wang](https://dblp.org/pid/01/6368-28.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Song Wang](https://dblp.org/pid/62/3151-2.html), [Yaowei Wang](https://dblp.org/pid/68/2992-1.html), [Zhepeng Wang](https://dblp.org/pid/242/8456-2.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Jiannan Wu](https://dblp.org/pid/277/0616.html), [Qiangqiang Wu](https://dblp.org/pid/193/1415.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Anqi Xiao](https://dblp.org/pid/307/8649.html), [Jinxia Xie](https://dblp.org/pid/294/3376.html), [Chenlong Xu](https://dblp.org/pid/315/8714.html), [Min Xu](https://dblp.org/pid/09/0-1.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Yuanyou Xu](https://dblp.org/pid/248/7663.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Dawei Yang](https://dblp.org/pid/22/1038.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Tianyu Yang](https://dblp.org/pid/120/8076-3.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Xuanwu Yin](https://dblp.org/pid/119/0001.html), Fisher Yu, [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Qianjin Yu](https://dblp.org/pid/53/10179.html), [Weichen Yu](https://dblp.org/pid/325/1209.html), [Yongsheng Yuan](https://dblp.org/pid/364/8163.html), [Zehuan Yuan](https://dblp.org/pid/227/3298.html), [Jianlin Zhang](https://dblp.org/pid/37/1545-1.html), [Lu Zhang](https://dblp.org/pid/82/10609-53.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Guodongfang Zhao](https://dblp.org/pid/364/8196.html), [Shaochuan Zhao](https://dblp.org/pid/260/3125.html), [Yaozong Zheng](https://dblp.org/pid/344/6907.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html), [ChengAo Zong](https://dblp.org/pid/364/8208.html), [Kunlong Zuo](https://dblp.org/pid/354/8493.html):

The First Visual Object Tracking Segmentation VOTS2023 Challenge Results. [ICCV (Workshops)2023](https://dblp.org/db/conf/iccvw/iccvw2023.html#conf/iccvw/KristanMDFCZLDZ23): 1788-1810
- ![](https://dblp.org/img/n.png)

\[c70\]
[Qi Fan](https://dblp.org/pid/43/4386.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), Fisher Yu, [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Bernt Schiele](https://dblp.org/pid/s/BerntSchiele.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dengxin Dai](https://dblp.org/pid/98/8616.html):

Towards Robust Object Detection Invariant to Real-World Domain Shifts. [ICLR2023](https://dblp.org/db/conf/iclr/iclr2023.html#conf/iclr/FanSTYTSD23)
- ![](https://dblp.org/img/n.png)

\[c69\]
[Mostafa Dehghani](https://dblp.org/pid/125/4062.html), [Josip Djolonga](https://dblp.org/pid/139/1342.html), [Basil Mustafa](https://dblp.org/pid/223/4558.html), [Piotr Padlewski](https://dblp.org/pid/210/6394.html), [Jonathan Heek](https://dblp.org/pid/247/1004.html), [Justin Gilmer](https://dblp.org/pid/131/6545.html), [Andreas Peter Steiner](https://dblp.org/pid/s/AndreasSteiner.html), [Mathilde Caron](https://dblp.org/pid/223/4085.html), [Robert Geirhos](https://dblp.org/pid/176/0076.html), [Ibrahim Alabdulmohsin](https://dblp.org/pid/153/5393.html), [Rodolphe Jenatton](https://dblp.org/pid/68/8398.html), [Lucas Beyer](https://dblp.org/pid/126/4720.html), [Michael Tschannen](https://dblp.org/pid/134/9824.html), [Anurag Arnab](https://dblp.org/pid/165/9719.html), [Xiao Wang](https://dblp.org/pid/49/67-38.html), [Carlos Riquelme Ruiz](https://dblp.org/pid/142/2592.html), [Matthias Minderer](https://dblp.org/pid/243/3155.html), [Joan Puigcerver](https://dblp.org/pid/155/3271.html), [Utku Evci](https://dblp.org/pid/179/8146.html), [Manoj Kumar](https://dblp.org/pid/58/1076.html), [Sjoerd van Steenkiste](https://dblp.org/pid/183/9326.html), [Gamaleldin Fathy Elsayed](https://dblp.org/pid/215/4903.html), [Aravindh Mahendran](https://dblp.org/pid/131/5343.html), Fisher Yu, [Avital Oliver](https://dblp.org/pid/203/8700.html), [Fantine Huot](https://dblp.org/pid/216/4555.html), [Jasmijn Bastings](https://dblp.org/pid/146/3824.html), [Mark Collier](https://dblp.org/pid/223/9928.html), [Alexey A. Gritsenko](https://dblp.org/pid/30/11478.html), [Vighnesh Birodkar](https://dblp.org/pid/186/8043.html), [Cristina Nader Vasconcelos](https://dblp.org/pid/37/135.html), [Yi Tay](https://dblp.org/pid/188/6350.html), [Thomas Mensink](https://dblp.org/pid/95/2677.html), [Alexander Kolesnikov](https://dblp.org/pid/137/6963-3.html), [Filip Pavetic](https://dblp.org/pid/149/2329.html), [Dustin Tran](https://dblp.org/pid/163/2106.html), [Thomas Kipf](https://dblp.org/pid/186/8206.html), [Mario Lucic](https://dblp.org/pid/155/1945.html), [Xiaohua Zhai](https://dblp.org/pid/66/636.html), [Daniel Keysers](https://dblp.org/pid/02/6955.html), [Jeremiah J. Harmsen](https://dblp.org/pid/47/6650.html), [Neil Houlsby](https://dblp.org/pid/91/10669.html):

Scaling Vision Transformers to 22 Billion Parameters. [ICML2023](https://dblp.org/db/conf/icml/icml2023.html#conf/icml/0001DMPHGSCGAJB23): 7480-7512
- ![](https://dblp.org/img/n.png)

\[c68\]
[Haotong Qin](https://dblp.org/pid/262/3626.html), [Mingyuan Zhang](https://dblp.org/pid/98/69.html), [Yifu Ding](https://dblp.org/pid/219/1995.html), [Aoyu Li](https://dblp.org/pid/301/8358.html), [Zhongang Cai](https://dblp.org/pid/232/3190.html), [Ziwei Liu](https://dblp.org/pid/05/6300-2.html), Fisher Yu, [Xianglong Liu](https://dblp.org/pid/55/7901-1.html):

BiBench: Benchmarking and Analyzing Network Binarization. [ICML2023](https://dblp.org/db/conf/icml/icml2023.html#conf/icml/QinZDLC0Y023): 28351-28388
- ![](https://dblp.org/img/n.png)

\[c67\]
[Zhejun Zhang](https://dblp.org/pid/58/9847.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alexander Liniger](https://dblp.org/pid/162/5560.html), [Dengxin Dai](https://dblp.org/pid/98/8616.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

TrafficBots: Towards World Models for Autonomous Driving Simulation and Motion Prediction. [ICRA2023](https://dblp.org/db/conf/icra/icra2023.html#conf/icra/ZhangLDYG23): 1522-1529
- ![](https://dblp.org/img/n.png)

\[c66\]
[Jiawei Fu](https://dblp.org/pid/194/2277-3.html), [Yunlong Song](https://dblp.org/pid/83/10696.html), [Yan Wu](https://dblp.org/pid/04/3001.html), Fisher Yu, [Davide Scaramuzza](https://dblp.org/pid/62/3318.html):

Learning Deep Sensorimotor Policies for Vision-Based Autonomous Drone Racing. [IROS2023](https://dblp.org/db/conf/iros/iros2023.html#conf/iros/FuSW0023): 5243-5250
- ![](https://dblp.org/img/n.png)

\[c65\]
[Nick Bührer](https://dblp.org/pid/280/2118.html), [Zhejun Zhang](https://dblp.org/pid/58/9847.html), [Alexander Liniger](https://dblp.org/pid/162/5560.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

A Multiplicative Value Function for Safe and Efficient Reinforcement Learning. [IROS2023](https://dblp.org/db/conf/iros/iros2023.html#conf/iros/BuhrerZL0G23): 5582-5589
- ![](https://dblp.org/img/n.png)

\[c64\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Mingqiao Ye](https://dblp.org/pid/285/9253.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Yifan Liu](https://dblp.org/pid/23/4955-1.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Fisher Yu:

Segment Anything in High Quality. [NeurIPS2023](https://dblp.org/db/conf/nips/neurips2023.html#conf/nips/KeYDLTT023)
- ![](https://dblp.org/img/n.png)

\[c63\]
[Haotong Qin](https://dblp.org/pid/262/3626.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Xudong Ma](https://dblp.org/pid/19/2951.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Xianglong Liu](https://dblp.org/pid/55/7901-1.html), Fisher Yu:

BiMatting: Efficient Video Matting via Binarization. [NeurIPS2023](https://dblp.org/db/conf/nips/neurips2023.html#conf/nips/QinK0DTT0023)
- ![](https://dblp.org/img/n.png)

\[c62\]
[Haotong Qin](https://dblp.org/pid/262/3626.html), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Yifu Ding](https://dblp.org/pid/219/1995.html), [Yifan Liu](https://dblp.org/pid/23/4955-1.html), [Xianglong Liu](https://dblp.org/pid/55/7901-1.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

QuantSR: Accurate Low-bit Quantization for Efficient Image Super-Resolution. [NeurIPS2023](https://dblp.org/db/conf/nips/neurips2023.html#conf/nips/QinZD00D023)
- ![](https://dblp.org/img/n.png)

\[c61\]
[Zhejun Zhang](https://dblp.org/pid/58/9847.html), [Alexander Liniger](https://dblp.org/pid/162/5560.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Real-Time Motion Prediction via Heterogeneous Polyline Transformer with Relative Pose Encoding. [NeurIPS2023](https://dblp.org/db/conf/nips/neurips2023.html#conf/nips/ZhangLS0G23)
- ![](https://dblp.org/img/n.png)

\[c60\]
[Junting Chen](https://dblp.org/pid/56/9060.html), [Guohao Li](https://dblp.org/pid/211/7175-1.html), [Suryansh Kumar](https://dblp.org/pid/124/2783.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bernard Ghanem](https://dblp.org/pid/37/2516.html), Fisher Yu:

How To Not Train Your Dragon: Training-free Embodied Object Goal Navigation with Semantic Frontiers. [Robotics: Science and Systems2023](https://dblp.org/db/conf/rss/rss2023.html#conf/rss/ChenLKGY23)
- ![](https://dblp.org/img/n.png)

\[c59\]
[Yung-Hsu Yang](https://dblp.org/pid/288/0092.html), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), [Min Sun](https://dblp.org/pid/62/2750-1.html), [Samuel Rota Bulò](https://dblp.org/pid/05/4139.html), [Peter Kontschieder](https://dblp.org/pid/93/8066.html), Fisher Yu:

Dense Prediction with Attentive Feature Aggregation. [WACV2023](https://dblp.org/db/conf/wacv/wacv2023.html#conf/wacv/YangHSBKY23): 97-106
- ![](https://dblp.org/img/n.png)

\[c58\]
[Menelaos Kanakis](https://dblp.org/pid/208/1757.html), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), [David Brüggemann](https://dblp.org/pid/271/0154.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Composite Learning for Robust and Effective Dense Predictions. [WACV2023](https://dblp.org/db/conf/wacv/wacv2023.html#conf/wacv/KanakisHBYG23): 2298-2307
- ![](https://dblp.org/img/n.png)

\[c57\]
[Gurkirt Singh](https://dblp.org/pid/155/3301.html), [Vasileios Choutas](https://dblp.org/pid/230/1246.html), [Suman Saha](https://dblp.org/pid/96/893-1.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Spatio-Temporal Action Detection Under Large Motion. [WACV2023](https://dblp.org/db/conf/wacv/wacv2023.html#conf/wacv/SinghCSYG23): 5998-6007
- ![](https://dblp.org/img/n.png)

\[i85\]
[Haotong Qin](https://dblp.org/pid/262/3626.html), [Mingyuan Zhang](https://dblp.org/pid/98/69.html), [Yifu Ding](https://dblp.org/pid/219/1995.html), [Aoyu Li](https://dblp.org/pid/301/8358.html), [Zhongang Cai](https://dblp.org/pid/232/3190.html), [Ziwei Liu](https://dblp.org/pid/05/6300-2.html), Fisher Yu, [Xianglong Liu](https://dblp.org/pid/55/7901-1.html):

BiBench: Benchmarking and Analyzing Network Binarization. [CoRRabs/2301.11233](https://dblp.org/db/journals/corr/corr2301.html#journals/corr/abs-2301-11233) (2023)
- ![](https://dblp.org/img/n.png)

\[i84\]
[Weirong Chen](https://dblp.org/pid/96/398.html), [Suryansh Kumar](https://dblp.org/pid/124/2783.html), Fisher Yu:

Uncertainty-Driven Dense Two-View Structure from Motion. [CoRRabs/2302.00523](https://dblp.org/db/journals/corr/corr2302.html#journals/corr/abs-2302-00523) (2023)
- ![](https://dblp.org/img/n.png)

\[i83\]
[Mostafa Dehghani](https://dblp.org/pid/125/4062.html), [Josip Djolonga](https://dblp.org/pid/139/1342.html), [Basil Mustafa](https://dblp.org/pid/223/4558.html), [Piotr Padlewski](https://dblp.org/pid/210/6394.html), [Jonathan Heek](https://dblp.org/pid/247/1004.html), [Justin Gilmer](https://dblp.org/pid/131/6545.html), [Andreas Steiner](https://dblp.org/pid/s/AndreasSteiner.html), [Mathilde Caron](https://dblp.org/pid/223/4085.html), [Robert Geirhos](https://dblp.org/pid/176/0076.html), [Ibrahim Alabdulmohsin](https://dblp.org/pid/153/5393.html), [Rodolphe Jenatton](https://dblp.org/pid/68/8398.html), [Lucas Beyer](https://dblp.org/pid/126/4720.html), [Michael Tschannen](https://dblp.org/pid/134/9824.html), [Anurag Arnab](https://dblp.org/pid/165/9719.html), [Xiao Wang](https://dblp.org/pid/49/67-38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Carlos Riquelme](https://dblp.org/pid/142/2592.html), [Matthias Minderer](https://dblp.org/pid/243/3155.html), [Joan Puigcerver](https://dblp.org/pid/155/3271.html), [Utku Evci](https://dblp.org/pid/179/8146.html), [Manoj Kumar](https://dblp.org/pid/58/1076.html), [Sjoerd van Steenkiste](https://dblp.org/pid/183/9326.html), [Gamaleldin F. Elsayed](https://dblp.org/pid/215/4903.html), [Aravindh Mahendran](https://dblp.org/pid/131/5343.html), Fisher Yu, [Avital Oliver](https://dblp.org/pid/203/8700.html), [Fantine Huot](https://dblp.org/pid/216/4555.html), [Jasmijn Bastings](https://dblp.org/pid/146/3824.html), [Mark Patrick Collier](https://dblp.org/pid/223/9928.html), [Alexey A. Gritsenko](https://dblp.org/pid/30/11478.html), [Vighnesh Birodkar](https://dblp.org/pid/186/8043.html), [Cristina Nader Vasconcelos](https://dblp.org/pid/37/135.html), [Yi Tay](https://dblp.org/pid/188/6350.html), [Thomas Mensink](https://dblp.org/pid/95/2677.html), [Alexander Kolesnikov](https://dblp.org/pid/137/6963-3.html), [Filip Pavetic](https://dblp.org/pid/149/2329.html), [Dustin Tran](https://dblp.org/pid/163/2106.html), [Thomas Kipf](https://dblp.org/pid/186/8206.html), [Mario Lucic](https://dblp.org/pid/155/1945.html), [Xiaohua Zhai](https://dblp.org/pid/66/636.html), [Daniel Keysers](https://dblp.org/pid/02/6955.html), [Jeremiah Harmsen](https://dblp.org/pid/47/6650.html), [Neil Houlsby](https://dblp.org/pid/91/10669.html):

Scaling Vision Transformers to 22 Billion Parameters. [CoRRabs/2302.05442](https://dblp.org/db/journals/corr/corr2302.html#journals/corr/abs-2302-05442) (2023)
- ![](https://dblp.org/img/n.png)

\[i82\]
[Zhejun Zhang](https://dblp.org/pid/58/9847.html), [Alexander Liniger](https://dblp.org/pid/162/5560.html), [Dengxin Dai](https://dblp.org/pid/98/8616.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

TrafficBots: Towards World Models for Autonomous Driving Simulation and Motion Prediction. [CoRRabs/2303.04116](https://dblp.org/db/journals/corr/corr2303.html#journals/corr/abs-2303-04116) (2023)
- ![](https://dblp.org/img/n.png)

\[i81\]
[Nick Bührer](https://dblp.org/pid/280/2118.html), [Zhejun Zhang](https://dblp.org/pid/58/9847.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alexander Liniger](https://dblp.org/pid/162/5560.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

A Multiplicative Value Function for Safe and Efficient Reinforcement Learning. [CoRRabs/2303.04118](https://dblp.org/db/journals/corr/corr2303.html#journals/corr/abs-2303-04118) (2023)
- ![](https://dblp.org/img/n.png)

\[i80\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Henghui Ding](https://dblp.org/pid/230/1216.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Fisher Yu:

Mask-Free Video Instance Segmentation. [CoRRabs/2303.15904](https://dblp.org/db/journals/corr/corr2303.html#journals/corr/abs-2303-15904) (2023)
- ![](https://dblp.org/img/n.png)

\[i79\]
[Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html), Fisher Yu:

iDisc: Internal Discretization for Monocular Depth Estimation. [CoRRabs/2304.06334](https://dblp.org/db/journals/corr/corr2304.html#journals/corr/abs-2304-06334) (2023)
- ![](https://dblp.org/img/n.png)

\[i78\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Tobias Fischer](https://dblp.org/pid/249/9213.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

OVTrack: Open-Vocabulary Multiple Object Tracking. [CoRRabs/2304.08408](https://dblp.org/db/journals/corr/corr2304.html#journals/corr/abs-2304-08408) (2023)
- ![](https://dblp.org/img/n.png)

\[i77\]
[Junting Chen](https://dblp.org/pid/56/9060.html), [Guohao Li](https://dblp.org/pid/211/7175-1.html), [Suryansh Kumar](https://dblp.org/pid/124/2783.html), [Bernard Ghanem](https://dblp.org/pid/37/2516.html), Fisher Yu:

How To Not Train Your Dragon: Training-free Embodied Object Goal Navigation with Semantic Frontiers. [CoRRabs/2305.16925](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-16925) (2023)
- ![](https://dblp.org/img/n.png)

\[i76\]
[Jan Ackermann](https://dblp.org/pid/348/6561.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html), Fisher Yu:

Maskomaly: Zero-Shot Mask Anomaly Segmentation. [CoRRabs/2305.16972](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-16972) (2023)
- ![](https://dblp.org/img/n.png)

\[i75\]
[Christos Sakaridis](https://dblp.org/pid/188/5858.html), [David Brüggemann](https://dblp.org/pid/271/0154.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Condition-Invariant Semantic Segmentation. [CoRRabs/2305.17349](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-17349) (2023)
- ![](https://dblp.org/img/n.png)

\[i74\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Mingqiao Ye](https://dblp.org/pid/285/9253.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Yifan Liu](https://dblp.org/pid/23/4955-1.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Fisher Yu:

Segment Anything in High Quality. [CoRRabs/2306.01567](https://dblp.org/db/journals/corr/corr2306.html#journals/corr/abs-2306-01567) (2023)
- ![](https://dblp.org/img/n.png)

\[i73\]
[Yiming Li](https://dblp.org/pid/l/YimingLi-3.html), [Sihang Li](https://dblp.org/pid/137/6318-1.html), [Xinhao Liu](https://dblp.org/pid/126/4582-3.html), [Moonjun Gong](https://dblp.org/pid/349/4889.html), [Kenan Li](https://dblp.org/pid/193/9514.html), [Nuo Chen](https://dblp.org/pid/135/5622-3.html), [Zijun Wang](https://dblp.org/pid/93/1955.html), [Zhiheng Li](https://dblp.org/pid/89/6935.html), [Tao Jiang](https://dblp.org/pid/181/2813.html), Fisher Yu, [Yue Wang](https://dblp.org/pid/33/4822-36.html), [Hang Zhao](https://dblp.org/pid/31/2950-21.html), [Zhiding Yu](https://dblp.org/pid/67/5386.html), [Chen Feng](https://dblp.org/pid/01/161-2.html):

SSCBench: A Large-Scale 3D Semantic Scene Completion Benchmark for Autonomous Driving. [CoRRabs/2306.09001](https://dblp.org/db/journals/corr/corr2306.html#journals/corr/abs-2306-09001) (2023)
- ![](https://dblp.org/img/n.png)

\[i72\]
[Frano Rajic](https://dblp.org/pid/331/2107.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

Segment Anything Meets Point Tracking. [CoRRabs/2307.01197](https://dblp.org/db/journals/corr/corr2307.html#journals/corr/abs-2307-01197) (2023)
- ![](https://dblp.org/img/n.png)

\[i71\]
[Mingqiao Ye](https://dblp.org/pid/285/9253.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

Cascade-DETR: Delving into High-Quality Universal Object Detection. [CoRRabs/2307.11035](https://dblp.org/db/journals/corr/corr2307.html#journals/corr/abs-2307-11035) (2023)
- ![](https://dblp.org/img/n.png)

\[i70\]
[Chunming He](https://dblp.org/pid/251/5104.html), [Kai Li](https://dblp.org/pid/l/KaiLi12.html), [Yachao Zhang](https://dblp.org/pid/40/10584-1.html), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Zhenhua Guo](https://dblp.org/pid/41/294-1.html), [Xiu Li](https://dblp.org/pid/13/1206-1.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

Strategic Preys Make Acute Predators: Enhancing Camouflaged Object Detectors by Generating Camouflaged Objects. [CoRRabs/2308.03166](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-03166) (2023)
- ![](https://dblp.org/img/n.png)

\[i69\]
[Zheng Chen](https://dblp.org/pid/33/2592-14.html), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Jinjin Gu](https://dblp.org/pid/209/5709.html), [Linghe Kong](https://dblp.org/pid/23/7909.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaokang Yang](https://dblp.org/pid/06/3071-1.html), Fisher Yu:

Dual Aggregation Transformer for Image Super-Resolution. [CoRRabs/2308.03364](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-03364) (2023)
- ![](https://dblp.org/img/n.png)

\[i68\]
[Georg Heigold](https://dblp.org/pid/46/2236.html), [Matthias Minderer](https://dblp.org/pid/243/3155.html), [Alexey A. Gritsenko](https://dblp.org/pid/30/11478.html), [Alex Bewley](https://dblp.org/pid/39/9969.html), [Daniel Keysers](https://dblp.org/pid/02/6955.html), [Mario Lucic](https://dblp.org/pid/155/1945.html), Fisher Yu, [Thomas Kipf](https://dblp.org/pid/186/8206.html):

Video OWL-ViT: Temporally-consistent open-world localization in video. [CoRRabs/2308.11093](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-11093) (2023)
- ![](https://dblp.org/img/n.png)

\[i67\]
[Lucas Morin](https://dblp.org/pid/309/7785.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Maria Isabel Agea](https://dblp.org/pid/355/2674.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ahmed S. Nassar](https://dblp.org/pid/321/9993.html), [Valéry Weber](https://dblp.org/pid/86/5323.html), [Ingmar Meijer](https://dblp.org/pid/46/5951.html), [Peter W. J. Staar](https://dblp.org/pid/136/7966.html), Fisher Yu:

MolGrapher: Graph-based Visual Recognition of Chemical Structures. [CoRRabs/2308.12234](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-12234) (2023)
- ![](https://dblp.org/img/n.png)

\[i66\]
[Aron Schmied](https://dblp.org/pid/355/5910.html), [Tobias Fischer](https://dblp.org/pid/249/9213.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Marc Pollefeys](https://dblp.org/pid/p/MarcPollefeys.html), Fisher Yu:

R3D3: Dense 3D Reconstruction of Dynamic Scenes from Multiple Cameras. [CoRRabs/2308.14713](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-14713) (2023)
- ![](https://dblp.org/img/n.png)

\[i65\]
[Thomas E. Huang](https://dblp.org/pid/260/6642.html), [Yifan Liu](https://dblp.org/pid/23/4955-1.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), Fisher Yu:

Video Task Decathlon: Unifying Image and Video Tasks in Autonomous Driving. [CoRRabs/2309.04422](https://dblp.org/db/journals/corr/corr2309.html#journals/corr/abs-2309-04422) (2023)
- ![](https://dblp.org/img/n.png)

\[i64\]
[Ozan Unal](https://dblp.org/pid/250/4116.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html), [Suman Saha](https://dblp.org/pid/96/893-1.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Three Ways to Improve Verbo-visual Fusion for Dense 3D Visual Grounding. [CoRRabs/2309.04561](https://dblp.org/db/journals/corr/corr2309.html#journals/corr/abs-2309-04561) (2023)
- ![](https://dblp.org/img/n.png)

\[i63\]
[Sanghwan Kim](https://dblp.org/pid/60/10274.html), [Hao Tang](https://dblp.org/pid/07/5751-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu:

Distilling ODE Solvers of Diffusion Models into Smaller Steps. [CoRRabs/2309.16421](https://dblp.org/db/journals/corr/corr2309.html#journals/corr/abs-2309-16421) (2023)
- ![](https://dblp.org/img/n.png)

\[i62\]
[Mattia Segù](https://dblp.org/pid/245/2565.html), [Bernt Schiele](https://dblp.org/pid/s/BerntSchiele.html), Fisher Yu:

DARTH: Holistic Test-time Adaptation for Multiple Object Tracking. [CoRRabs/2310.01926](https://dblp.org/db/journals/corr/corr2310.html#journals/corr/abs-2310-01926) (2023)
- ![](https://dblp.org/img/n.png)

\[i61\]
[Zhizheng Liu](https://dblp.org/pid/287/4356.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), Fisher Yu:

COOLer: Class-Incremental Learning for Appearance-Based Multiple Object Tracking. [CoRRabs/2310.03006](https://dblp.org/db/journals/corr/corr2310.html#journals/corr/abs-2310-03006) (2023)
- ![](https://dblp.org/img/n.png)

\[i60\]
[Zhejun Zhang](https://dblp.org/pid/58/9847.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alexander Liniger](https://dblp.org/pid/162/5560.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Real-Time Motion Prediction via Heterogeneous Polyline Transformer with Relative Pose Encoding. [CoRRabs/2310.12970](https://dblp.org/db/journals/corr/corr2310.html#journals/corr/abs-2310-12970) (2023)
- ![](https://dblp.org/img/n.png)

\[i59\]
[Mingqiao Ye](https://dblp.org/pid/285/9253.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu, [Lei Ke](https://dblp.org/pid/26/5225.html):

Gaussian Grouping: Segment and Edit Anything in 3D Scenes. [CoRRabs/2312.00732](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-00732) (2023)
- ![](https://dblp.org/img/n.png)

\[i58\]
[Haofei Xu](https://dblp.org/pid/236/6248.html), [Anpei Chen](https://dblp.org/pid/210/2592.html), [Yuedong Chen](https://dblp.org/pid/236/6258.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Marc Pollefeys](https://dblp.org/pid/p/MarcPollefeys.html), [Andreas Geiger](https://dblp.org/pid/40/5825-1.html), Fisher Yu:

MuRF: Multi-Baseline Radiance Fields. [CoRRabs/2312.04565](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-04565) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j3\]
[Soomin Lee](https://dblp.org/pid/81/4155.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Le Chen](https://dblp.org/pid/19/576.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiahao Wang](https://dblp.org/pid/34/5354-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alexander Liniger](https://dblp.org/pid/162/5560.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Suryansh Kumar](https://dblp.org/pid/124/2783.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu![](https://dblp.org/img/orcid-mark.12x12.png):

Uncertainty Guided Policy for Active Robotic 3D Reconstruction Using Neural Radiance Fields. [IEEE Robotics Autom. Lett.7(4)](https://dblp.org/db/journals/ral/ral7.html#journals/ral/LeeCWLKY22): 12070-12077 (2022)
- ![](https://dblp.org/img/n.png)

\[c56\]
[Tobias Fischer](https://dblp.org/pid/249/9213.html), [Yung-Hsu Yang](https://dblp.org/pid/288/0092.html), [Suryansh Kumar](https://dblp.org/pid/124/2783.html), [Min Sun](https://dblp.org/pid/62/2750-1.html), Fisher Yu:

CC-3DT: Panoramic 3D Object Tracking via Cross-Camera Fusion. [CoRL2022](https://dblp.org/db/conf/corl/corl2022.html#conf/corl/0004YKSY22): 2294-2305
- ![](https://dblp.org/img/n.png)

\[c55\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Xia Li](https://dblp.org/pid/97/30-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yu-Wing Tai](https://dblp.org/pid/40/566.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Fisher Yu:

Mask Transfiner for High-Quality Instance Segmentation. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/KeDLTTY22): 4402-4411
- ![](https://dblp.org/img/n.png)

\[c54\]
[Prune Truong](https://dblp.org/pid/247/5738.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Probabilistic Warp Consistency for Weakly-Supervised Semantic Correspondences. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/TruongDYG22): 8698-8708
- ![](https://dblp.org/img/n.png)

\[c53\]
[Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Transforming Model Prediction for Tracking. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/0007DBPPYG22): 8721-8730
- ![](https://dblp.org/img/n.png)

\[c52\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Andrés Romero](https://dblp.org/pid/29/641.html), Fisher Yu, [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

RePaint: Inpainting using Denoising Diffusion Probabilistic Models. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/LugmayrDRYTG22): 11451-11461
- ![](https://dblp.org/img/n.png)

\[c51\]
[Muhammad Zaigham Zaheer](https://dblp.org/pid/260/4206.html), [Arif Mahmood](https://dblp.org/pid/18/4138.html), [Muhammad Haris Khan](https://dblp.org/pid/155/3076.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), Fisher Yu, [Seung-Ik Lee](https://dblp.org/pid/30/1902.html):

Generative Cooperative Learning for Unsupervised Video Anomaly Detection. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/ZaheerMKSYL22): 14724-14734
- ![](https://dblp.org/img/n.png)

\[c50\]
[Martin Hahner](https://dblp.org/pid/207/7633.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mario Bijelic](https://dblp.org/pid/228/4623.html), [Felix Heide](https://dblp.org/pid/01/9396.html), Fisher Yu, [Dengxin Dai](https://dblp.org/pid/98/8616.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

LiDAR Snowfall Simulation for Robust 3D Object Detection. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/HahnerSBHYDG22): 16343-16353
- ![](https://dblp.org/img/n.png)

\[c49\]
[Tao Sun](https://dblp.org/pid/74/3590-19.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Janis Postels](https://dblp.org/pid/246/4950.html), [Yuxuan Wang](https://dblp.org/pid/94/3940.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Bernt Schiele](https://dblp.org/pid/s/BerntSchiele.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Federico Tombari](https://dblp.org/pid/16/3539.html), Fisher Yu:

SHIFT: A Synthetic Driving Dataset for Continuous Multi-Task Domain Adaptation. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/SunSPWGSTY22): 21339-21350
- ![](https://dblp.org/img/n.png)

\[c48\]
[Rui Gong](https://dblp.org/pid/75/1938.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Dengxin Dai](https://dblp.org/pid/98/8616.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ajad Chhatkuli](https://dblp.org/pid/149/7655.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

TACS: Taxonomy Adaptive Cross-Domain Semantic Segmentation. [ECCV (34)2022](https://dblp.org/db/conf/eccv/eccv2022-34.html#conf/eccv/GongDDPCYG22): 19-35
- ![](https://dblp.org/img/n.png)

\[c47\]
[Erik Sandström](https://dblp.org/pid/192/9251.html), [Martin R. Oswald](https://dblp.org/pid/37/7272.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Suryansh Kumar](https://dblp.org/pid/124/2783.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Silvan Weder](https://dblp.org/pid/256/4902.html), Fisher Yu, [Cristian Sminchisescu](https://dblp.org/pid/96/3826.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Learning Online Multi-sensor Depth Fusion. [ECCV (32)2022](https://dblp.org/db/conf/eccv/eccv2022-32.html#conf/eccv/SandstromOKWYSG22): 87-105
- ![](https://dblp.org/img/n.png)

\[c46\]
[Yan Wu](https://dblp.org/pid/04/3001.html), [Jiahao Wang](https://dblp.org/pid/34/5354-1.html), [Yan Zhang](https://dblp.org/pid/04/3348-54.html), [Siwei Zhang](https://dblp.org/pid/68/11277.html), [Otmar Hilliges](https://dblp.org/pid/82/2289.html), Fisher Yu, [Siyu Tang](https://dblp.org/pid/22/845-1.html):

SAGA: Stochastic Whole-Body Grasping with Contact. [ECCV (6)2022](https://dblp.org/db/conf/eccv/eccv2022-6.html#conf/eccv/WuWZZHYT22): 257-274
- ![](https://dblp.org/img/n.png)

\[c45\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Wenyan Yang](https://dblp.org/pid/119/2426.html), [Dingding Cai](https://dblp.org/pid/198/1127.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Kang Ben](https://dblp.org/pid/340/0959.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Hong Chang](https://dblp.org/pid/02/2689-1.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Jiaye Chen](https://dblp.org/pid/116/2901.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xilin Chen](https://dblp.org/pid/c/XilinChen.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Xiuyi Chen](https://dblp.org/pid/218/7190.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu-Hsi Chen](https://dblp.org/pid/127/3933.html), [Zhixing Chen](https://dblp.org/pid/62/3074.html), [Yangming Cheng](https://dblp.org/pid/340/1285.html), [Angelo Ciaramella](https://dblp.org/pid/37/6845.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Benjamin Dzubur](https://dblp.org/pid/340/1520.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Debajyoti Dhar](https://dblp.org/pid/128/3182.html), [Shangzhe Di](https://dblp.org/pid/304/1344.html), [Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shang Gao](https://dblp.org/pid/28/435-12.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Eric Granger](https://dblp.org/pid/86/2306.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Q. H. Gu](https://dblp.org/pid/340/1209.html), [Himanshu Gupta](https://dblp.org/pid/330/0760-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianfeng He](https://dblp.org/pid/93/8352.html), [Keji He](https://dblp.org/pid/319/4518.html), [Yan Huang](https://dblp.org/pid/75/6434-8.html), [Deepak Jangid](https://dblp.org/pid/340/1460.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Ze Kang](https://dblp.org/pid/340/1063.html), [Madhu Kiran](https://dblp.org/pid/39/10281.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Simiao Lai](https://dblp.org/pid/282/1954.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Dongwook Lee](https://dblp.org/pid/25/6543.html), [Hyunjeong Lee](https://dblp.org/pid/00/3423.html), [Seohyung Lee](https://dblp.org/pid/210/4662.html), [Hui Li](https://dblp.org/pid/66/3387-37.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ming Li](https://dblp.org/pid/l/MingLi10.html), [Wangkai Li](https://dblp.org/pid/340/1456.html), [Xi Li](https://dblp.org/pid/46/2311-1.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Xiao Li](https://dblp.org/pid/66/2069.html), [Zhe Li](https://dblp.org/pid/11/751-8.html), [Liting Lin](https://dblp.org/pid/227/2204.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Si Liu](https://dblp.org/pid/60/7642.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html), [Bingpeng Ma](https://dblp.org/pid/62/1822.html), [Chao Ma](https://dblp.org/pid/79/1552-4.html), [Jie Ma](https://dblp.org/pid/62/5110.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yinchao Ma](https://dblp.org/pid/189/1326.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Payman Moallem](https://dblp.org/pid/63/5378.html), [Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html), [Siyang Pan](https://dblp.org/pid/250/5753.html), [ChangBeom Park](https://dblp.org/pid/340/0926.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Litu Rout](https://dblp.org/pid/206/6445.html), [Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Tianhui Song](https://dblp.org/pid/181/8738.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Chao Sun](https://dblp.org/pid/54/3957.html), [Jingna Sun](https://dblp.org/pid/255/0702.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Om Prakash Verma](https://dblp.org/pid/61/8145.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Qiang Wang](https://dblp.org/pid/64/5630-23.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Jinlin Wu](https://dblp.org/pid/123/7200.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Xu](https://dblp.org/pid/32/1213-17.html), [Yong Xu](https://dblp.org/pid/07/4630-7.html), [Yuanyou Xu](https://dblp.org/pid/248/7663.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zizheng Xun](https://dblp.org/pid/340/1441.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Dawei Yang](https://dblp.org/pid/22/1038.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Yichun Yang](https://dblp.org/pid/249/9678.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Botao Ye](https://dblp.org/pid/227/4610.html), Fisher Yu, [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Qianjin Yu](https://dblp.org/pid/53/10179.html), [Weichen Yu](https://dblp.org/pid/325/1209.html), [Kang Ze](https://dblp.org/pid/340/1107.html), [Jiang Zhai](https://dblp.org/pid/291/9340.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhu Zhang](https://dblp.org/pid/292/0953.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Haixia Zheng](https://dblp.org/pid/119/1585.html), [Min Zheng](https://dblp.org/pid/23/328.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html):

The Tenth Visual Object Tracking VOT2022 Challenge Results. [ECCV Workshops (8)2022](https://dblp.org/db/conf/eccv/eccv2022-w8.html#conf/eccv/KristanLMFPKCDZLDBZZYYCMFBBCCCCCCCCCCC22): 431-460
- ![](https://dblp.org/img/n.png)

\[c44\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), Fisher Yu:

Tracking Every Thing in the Wild. [ECCV (22)2022](https://dblp.org/db/conf/eccv/eccv2022-22.html#conf/eccv/LiDDHY22): 498-515
- ![](https://dblp.org/img/n.png)

\[c43\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Fisher Yu:

Video Mask Transfiner for High-Quality Video Instance Segmentation. [ECCV (28)2022](https://dblp.org/db/conf/eccv/eccv2022-28.html#conf/eccv/KeDDTTY22): 731-747
- ![](https://dblp.org/img/n.png)

\[c42\]
[Janis Postels](https://dblp.org/pid/246/4950.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Tao Sun](https://dblp.org/pid/74/3590-19.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luca Daniel Sieber](https://dblp.org/pid/323/8890.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), Fisher Yu, [Federico Tombari](https://dblp.org/pid/16/3539.html):

On the Practicality of Deterministic Epistemic Uncertainty. [ICML2022](https://dblp.org/db/conf/icml/icml2022.html#conf/icml/PostelsSSSGYT22): 17870-17909
- ![](https://dblp.org/img/n.png)

\[c41\]
[Yihang She](https://dblp.org/pid/294/4508.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

Fast Hierarchical Learning for Few-Shot Object Detection. [IROS2022](https://dblp.org/db/conf/iros/iros2022.html#conf/iros/SheBDY22): 1993-2000
- ![](https://dblp.org/img/n.png)

\[c40\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Normalizing Flow as a Flexible Fidelity Objective for Photo-Realistic Super-resolution. [WACV2022](https://dblp.org/db/conf/wacv/wacv2022.html#conf/wacv/LugmayrDYGT22): 874-883
- ![](https://dblp.org/img/n.png)

\[i57\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Andrés Romero](https://dblp.org/pid/29/641.html), Fisher Yu, [Radu Timofte](https://dblp.org/pid/24/8616.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

RePaint: Inpainting using Denoising Diffusion Probabilistic Models. [CoRRabs/2201.09865](https://dblp.org/db/journals/corr/corr2201.html#journals/corr/abs-2201-09865) (2022)
- ![](https://dblp.org/img/n.png)

\[i56\]
[Muhammad Zaigham Zaheer](https://dblp.org/pid/260/4206.html), [Arif Mahmood](https://dblp.org/pid/18/4138.html), [Muhammad Haris Khan](https://dblp.org/pid/155/3076.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), Fisher Yu, [Seung-Ik Lee](https://dblp.org/pid/30/1902.html):

Generative Cooperative Learning for Unsupervised Video Anomaly Detection. [CoRRabs/2203.03962](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-03962) (2022)
- ![](https://dblp.org/img/n.png)

\[i55\]
[Prune Truong](https://dblp.org/pid/247/5738.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Probabilistic Warp Consistency for Weakly-Supervised Semantic Correspondences. [CoRRabs/2203.04279](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-04279) (2022)
- ![](https://dblp.org/img/n.png)

\[i54\]
[Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Transforming Model Prediction for Tracking. [CoRRabs/2203.11192](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-11192) (2022)
- ![](https://dblp.org/img/n.png)

\[i53\]
[Martin Hahner](https://dblp.org/pid/207/7633.html), [Christos Sakaridis](https://dblp.org/pid/188/5858.html), [Mario Bijelic](https://dblp.org/pid/228/4623.html), [Felix Heide](https://dblp.org/pid/01/9396.html), Fisher Yu, [Dengxin Dai](https://dblp.org/pid/98/8616.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

LiDAR Snowfall Simulation for Robust 3D Object Detection. [CoRRabs/2203.15118](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-15118) (2022)
- ![](https://dblp.org/img/n.png)

\[i52\]
[Erik Sandström](https://dblp.org/pid/192/9251.html), [Martin R. Oswald](https://dblp.org/pid/37/7272.html), [Suryansh Kumar](https://dblp.org/pid/124/2783.html), [Silvan Weder](https://dblp.org/pid/256/4902.html), Fisher Yu, [Cristian Sminchisescu](https://dblp.org/pid/96/3826.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Learning Online Multi-Sensor Depth Fusion. [CoRRabs/2204.03353](https://dblp.org/db/journals/corr/corr2204.html#journals/corr/abs-2204-03353) (2022)
- ![](https://dblp.org/img/n.png)

\[i51\]
[Tao Sun](https://dblp.org/pid/74/3590-19.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Janis Postels](https://dblp.org/pid/246/4950.html), [Yuxuan Wang](https://dblp.org/pid/94/3940.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Bernt Schiele](https://dblp.org/pid/s/BerntSchiele.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Federico Tombari](https://dblp.org/pid/16/3539.html), Fisher Yu:

SHIFT: A Synthetic Driving Dataset for Continuous Multi-Task Domain Adaptation. [CoRRabs/2206.08367](https://dblp.org/db/journals/corr/corr2206.html#journals/corr/abs-2206-08367) (2022)
- ![](https://dblp.org/img/n.png)

\[i50\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), Fisher Yu:

Tracking Every Thing in the Wild. [CoRRabs/2207.12978](https://dblp.org/db/journals/corr/corr2207.html#journals/corr/abs-2207-12978) (2022)
- ![](https://dblp.org/img/n.png)

\[i49\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Fisher Yu:

Video Mask Transfiner for High-Quality Video Instance Segmentation. [CoRRabs/2207.14012](https://dblp.org/db/journals/corr/corr2207.html#journals/corr/abs-2207-14012) (2022)
- ![](https://dblp.org/img/n.png)

\[i48\]
[Gurkirt Singh](https://dblp.org/pid/155/3301.html), [Vasileios Choutas](https://dblp.org/pid/230/1246.html), [Suman Saha](https://dblp.org/pid/96/893-1.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Spatio-Temporal Action Detection Under Large Motion. [CoRRabs/2209.02250](https://dblp.org/db/journals/corr/corr2209.html#journals/corr/abs-2209-02250) (2022)
- ![](https://dblp.org/img/n.png)

\[i47\]
[Soomin Lee](https://dblp.org/pid/81/4155.html), [Le Chen](https://dblp.org/pid/19/576.html), [Jiahao Wang](https://dblp.org/pid/34/5354-1.html), [Alexander Liniger](https://dblp.org/pid/162/5560.html), [Suryansh Kumar](https://dblp.org/pid/124/2783.html), Fisher Yu:

Uncertainty Guided Policy for Active Robotic 3D Reconstruction using Neural Radiance Fields. [CoRRabs/2209.08409](https://dblp.org/db/journals/corr/corr2209.html#journals/corr/abs-2209-08409) (2022)
- ![](https://dblp.org/img/n.png)

\[i46\]
[Yihang She](https://dblp.org/pid/294/4508.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu:

Fast Hierarchical Learning for Few-Shot Object Detection. [CoRRabs/2210.05008](https://dblp.org/db/journals/corr/corr2210.html#journals/corr/abs-2210-05008) (2022)
- ![](https://dblp.org/img/n.png)

\[i45\]
[Tobias Fischer](https://dblp.org/pid/249/9213.html), [Jiangmiao Pang](https://dblp.org/pid/231/7630.html), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), [Linlu Qiu](https://dblp.org/pid/267/2348.html), [Haofeng Chen](https://dblp.org/pid/120/5331.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu:

QDTrack: Quasi-Dense Similarity Learning for Appearance-Only Multiple Object Tracking. [CoRRabs/2210.06984](https://dblp.org/db/journals/corr/corr2210.html#journals/corr/abs-2210-06984) (2022)
- ![](https://dblp.org/img/n.png)

\[i44\]
[Menelaos Kanakis](https://dblp.org/pid/208/1757.html), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), [David Brüggemann](https://dblp.org/pid/271/0154.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Composite Learning for Robust and Effective Dense Predictions. [CoRRabs/2210.07239](https://dblp.org/db/journals/corr/corr2210.html#journals/corr/abs-2210-07239) (2022)
- ![](https://dblp.org/img/n.png)

\[i43\]
[Jiawei Fu](https://dblp.org/pid/194/2277-3.html), [Yunlong Song](https://dblp.org/pid/83/10696.html), [Yan Wu](https://dblp.org/pid/04/3001.html), Fisher Yu, [Davide Scaramuzza](https://dblp.org/pid/62/3318.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning Deep Sensorimotor Policies for Vision-based Autonomous Drone Racing. [CoRRabs/2210.14985](https://dblp.org/db/journals/corr/corr2210.html#journals/corr/abs-2210-14985) (2022)
- ![](https://dblp.org/img/n.png)

\[i42\]
[Qi Fan](https://dblp.org/pid/43/4386.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu, [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Bernt Schiele](https://dblp.org/pid/s/BerntSchiele.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dengxin Dai](https://dblp.org/pid/98/8616.html):

Normalization Perturbation: A Simple Domain Generalization Method for Real-World Domain Shifts. [CoRRabs/2211.04393](https://dblp.org/db/journals/corr/corr2211.html#journals/corr/abs-2211-04393) (2022)
- ![](https://dblp.org/img/n.png)

\[i41\]
[Haofei Xu](https://dblp.org/pid/236/6248.html), [Jing Zhang](https://dblp.org/pid/05/3499-37.html), [Jianfei Cai](https://dblp.org/pid/83/6096.html), [Hamid Rezatofighi](https://dblp.org/pid/37/8192.html), Fisher Yu, [Dacheng Tao](https://dblp.org/pid/46/3391.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Andreas Geiger](https://dblp.org/pid/40/5825-1.html):

Unifying Flow, Stereo and Depth Estimation. [CoRRabs/2211.05783](https://dblp.org/db/journals/corr/corr2211.html#journals/corr/abs-2211-05783) (2022)
- ![](https://dblp.org/img/n.png)

\[i40\]
[Changyong Shu](https://dblp.org/pid/239/5094.html), Fisher Yu, [Yifan Liu](https://dblp.org/pid/23/4955-1.html):

3D Point Positional Encoding for Multi-Camera 3D Object Detection Transformers. [CoRRabs/2211.14710](https://dblp.org/db/journals/corr/corr2211.html#journals/corr/abs-2211-14710) (2022)
- ![](https://dblp.org/img/n.png)

\[i39\]
[Tobias Fischer](https://dblp.org/pid/249/9213.html), [Yung-Hsu Yang](https://dblp.org/pid/288/0092.html), [Suryansh Kumar](https://dblp.org/pid/124/2783.html), [Min Sun](https://dblp.org/pid/62/2750-1.html), Fisher Yu:

CC-3DT: Panoramic 3D Object Tracking via Cross-Camera Fusion. [CoRRabs/2212.01247](https://dblp.org/db/journals/corr/corr2212.html#journals/corr/abs-2212-01247) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[c39\]
[Jiangmiao Pang](https://dblp.org/pid/231/7630.html), [Linlu Qiu](https://dblp.org/pid/267/2348.html), [Xia Li](https://dblp.org/pid/97/30-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haofeng Chen](https://dblp.org/pid/120/5331.html), [Qi Li](https://dblp.org/pid/181/2688.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu:

Quasi-Dense Similarity Learning for Multiple Object Tracking. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/PangQLCLDY21): 164-173
- ![](https://dblp.org/img/n.png)

\[c38\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Deep Reparametrization of Multi-Frame Super-Resolution and Denoising. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/BhatDYGT21): 2440-2450
- ![](https://dblp.org/img/n.png)

\[c37\]
[Wenguan Wang](https://dblp.org/pid/145/1078.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianfei Zhou](https://dblp.org/pid/150/6710.html), Fisher Yu, [Jifeng Dai](https://dblp.org/pid/14/9399.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ender Konukoglu](https://dblp.org/pid/45/7041.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Exploring Cross-Image Pixel Contrast for Semantic Segmentation. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/WangZYDKG21): 7283-7293
- ![](https://dblp.org/img/n.png)

\[c36\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), [Benlin Liu](https://dblp.org/pid/274/0684.html), Fisher Yu, [Xiaolong Wang](https://dblp.org/pid/91/952-4.html), [Joseph E. Gonzalez](https://dblp.org/pid/61/8262.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Robust Object Detection via Instance-Level Temporal Cycle Confusion. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/0066HLY0GD21): 9123-9132
- ![](https://dblp.org/img/n.png)

\[c35\]
[Prune Truong](https://dblp.org/pid/247/5738.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Warp Consistency for Unsupervised Learning of Dense Correspondences. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/TruongDYG21): 10326-10336
- ![](https://dblp.org/img/n.png)

\[c34\]
[Zhejun Zhang](https://dblp.org/pid/58/9847.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alexander Liniger](https://dblp.org/pid/162/5560.html), [Dengxin Dai](https://dblp.org/pid/98/8616.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

End-to-End Urban Driving by Imitating a Reinforcement Learning Coach. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/ZhangLDYG21): 15202-15212
- ![](https://dblp.org/img/n.png)

\[c33\]
[Rui Fan](https://dblp.org/pid/03/1805-1.html), [Nemanja Djuric](https://dblp.org/pid/35/9989.html), Fisher Yu, [Rowan McAllister](https://dblp.org/pid/123/6416.html), [Ioannis Pitas](https://dblp.org/pid/p/IPitas.html):

Autonomous Vehicle Vision 2021: ICCV Workshop Summary. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/FanDYMP21): 3088-3095
- ![](https://dblp.org/img/n.png)

\[c32\]
[Jinkun Cao](https://dblp.org/pid/224/0126.html), [Xin Wang](https://dblp.org/pid/10/5630-66.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu:

Instance-Aware Predictive Navigation in Multi-Agent Environments. [ICRA2021](https://dblp.org/db/conf/icra/icra2021.html#conf/icra/CaoWDY21): 5096-5102
- ![](https://dblp.org/img/n.png)

\[c31\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Xia Li](https://dblp.org/pid/97/30-5.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Fisher Yu:

Prototypical Cross-Attention Networks for Multiple Object Tracking and Segmentation. [NeurIPS2021](https://dblp.org/db/conf/nips/neurips2021.html#conf/nips/KeLDTTY21): 1192-1203
- ![](https://dblp.org/img/n.png)

\[i38\]
[Jinkun Cao](https://dblp.org/pid/224/0126.html), [Xin Wang](https://dblp.org/pid/10/5630-66.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu:

Instance-Aware Predictive Navigation in Multi-Agent Environments. [CoRRabs/2101.05893](https://dblp.org/db/journals/corr/corr2101.html#journals/corr/abs-2101-05893) (2021)
- ![](https://dblp.org/img/n.png)

\[i37\]
[Wenguan Wang](https://dblp.org/pid/145/1078.html), [Tianfei Zhou](https://dblp.org/pid/150/6710.html), Fisher Yu, [Jifeng Dai](https://dblp.org/pid/14/9399.html), [Ender Konukoglu](https://dblp.org/pid/45/7041.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Exploring Cross-Image Pixel Contrast for Semantic Segmentation. [CoRRabs/2101.11939](https://dblp.org/db/journals/corr/corr2101.html#journals/corr/abs-2101-11939) (2021)
- ![](https://dblp.org/img/n.png)

\[i36\]
[Hou-Ning Hu](https://dblp.org/pid/199/3014.html), [Yung-Hsu Yang](https://dblp.org/pid/288/0092.html), [Tobias Fischer](https://dblp.org/pid/249/9213.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu, [Min Sun](https://dblp.org/pid/62/2750-1.html):

Monocular Quasi-Dense 3D Object Tracking. [CoRRabs/2103.07351](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-07351) (2021)
- ![](https://dblp.org/img/n.png)

\[i35\]
[Prune Truong](https://dblp.org/pid/247/5738.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Warp Consistency for Unsupervised Learning of Dense Correspondences. [CoRRabs/2104.03308](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-03308) (2021)
- ![](https://dblp.org/img/n.png)

\[i34\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), [Benlin Liu](https://dblp.org/pid/274/0684.html), Fisher Yu, [Xiaolong Wang](https://dblp.org/pid/91/952-4.html), [Joseph E. Gonzalez](https://dblp.org/pid/61/8262.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Robust Object Detection via Instance-Level Temporal Cycle Confusion. [CoRRabs/2104.08381](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-08381) (2021)
- ![](https://dblp.org/img/n.png)

\[i33\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Xia Li](https://dblp.org/pid/97/30-5.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Fisher Yu:

Prototypical Cross-Attention Networks for Multiple Object Tracking and Segmentation. [CoRRabs/2106.11958](https://dblp.org/db/journals/corr/corr2106.html#journals/corr/abs-2106-11958) (2021)
- ![](https://dblp.org/img/n.png)

\[i32\]
[Janis Postels](https://dblp.org/pid/246/4950.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Tao Sun](https://dblp.org/pid/74/3590-19.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), Fisher Yu, [Federico Tombari](https://dblp.org/pid/16/3539.html):

On the Practicality of Deterministic Epistemic Uncertainty. [CoRRabs/2107.00649](https://dblp.org/db/journals/corr/corr2107.html#journals/corr/abs-2107-00649) (2021)
- ![](https://dblp.org/img/n.png)

\[i31\]
[Zhejun Zhang](https://dblp.org/pid/58/9847.html), [Alexander Liniger](https://dblp.org/pid/162/5560.html), [Dengxin Dai](https://dblp.org/pid/98/8616.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

End-to-End Urban Driving by Imitating a Reinforcement Learning Coach. [CoRRabs/2108.08265](https://dblp.org/db/journals/corr/corr2108.html#journals/corr/abs-2108-08265) (2021)
- ![](https://dblp.org/img/n.png)

\[i30\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Deep Reparametrization of Multi-Frame Super-Resolution and Denoising. [CoRRabs/2108.08286](https://dblp.org/db/journals/corr/corr2108.html#journals/corr/abs-2108-08286) (2021)
- ![](https://dblp.org/img/n.png)

\[i29\]
[Rui Gong](https://dblp.org/pid/75/1938.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Dengxin Dai](https://dblp.org/pid/98/8616.html), [Wenguan Wang](https://dblp.org/pid/145/1078.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Ajad Chhatkuli](https://dblp.org/pid/149/7655.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

TADA: Taxonomy Adaptive Domain Adaptation. [CoRRabs/2109.04813](https://dblp.org/db/journals/corr/corr2109.html#journals/corr/abs-2109-04813) (2021)
- ![](https://dblp.org/img/n.png)

\[i28\]
[Yung-Hsu Yang](https://dblp.org/pid/288/0092.html), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), [Samuel Rota Bulò](https://dblp.org/pid/05/4139.html), [Peter Kontschieder](https://dblp.org/pid/93/8066.html), Fisher Yu:

Dense Prediction with Attentive Feature Aggregation. [CoRRabs/2111.00770](https://dblp.org/db/journals/corr/corr2111.html#journals/corr/abs-2111-00770) (2021)
- ![](https://dblp.org/img/n.png)

\[i27\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), Fisher Yu, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Normalizing Flow as a Flexible Fidelity Objective for Photo-Realistic Super-resolution. [CoRRabs/2111.03649](https://dblp.org/db/journals/corr/corr2111.html#journals/corr/abs-2111-03649) (2021)
- ![](https://dblp.org/img/n.png)

\[i26\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Xia Li](https://dblp.org/pid/97/30-5.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Fisher Yu:

Mask Transfiner for High-Quality Instance Segmentation. [CoRRabs/2111.13673](https://dblp.org/db/journals/corr/corr2111.html#journals/corr/abs-2111-13673) (2021)
- ![](https://dblp.org/img/n.png)

\[i25\]
[Yan Wu](https://dblp.org/pid/04/3001.html), [Jiahao Wang](https://dblp.org/pid/34/5354-1.html), [Yan Zhang](https://dblp.org/pid/04/3348-54.html), [Siwei Zhang](https://dblp.org/pid/68/11277.html), [Otmar Hilliges](https://dblp.org/pid/82/2289.html), Fisher Yu, [Siyu Tang](https://dblp.org/pid/22/845-1.html):

SAGA: Stochastic Whole-Body Grasping with Contact. [CoRRabs/2112.10103](https://dblp.org/db/journals/corr/corr2112.html#journals/corr/abs-2112-10103) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[c30\]
Fisher Yu, [Haofeng Chen](https://dblp.org/pid/120/5331.html), [Xin Wang](https://dblp.org/pid/10/5630-66.html), [Wenqi Xian](https://dblp.org/pid/202/2384.html), [Yingying Chen](https://dblp.org/pid/18/2343.html), [Fangchen Liu](https://dblp.org/pid/211/7883.html), [Vashisht Madhavan](https://dblp.org/pid/190/2112.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

BDD100K: A Diverse Driving Dataset for Heterogeneous Multitask Learning. [CVPR2020](https://dblp.org/db/conf/cvpr/cvpr2020.html#conf/cvpr/YuCWXCLMD20): 2633-2642
- ![](https://dblp.org/img/n.png)

\[c29\]
[Yanzhao Zhou](https://dblp.org/pid/194/2778.html), [Xin Wang](https://dblp.org/pid/10/5630-66.html), [Jianbin Jiao](https://dblp.org/pid/02/6888.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu:

Learning Saliency Propagation for Semi-Supervised Instance Segmentation. [CVPR2020](https://dblp.org/db/conf/cvpr/cvpr2020.html#conf/cvpr/ZhouWJDY20): 10304-10313
- ![](https://dblp.org/img/n.png)

\[c28\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), [Joseph Gonzalez](https://dblp.org/pid/61/8262.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu:

Frustratingly Simple Few-Shot Object Detection. [ICML2020](https://dblp.org/db/conf/icml/icml2020.html#conf/icml/WangH0DY20): 9919-9928
- ![](https://dblp.org/img/n.png)

\[i24\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), [Joseph E. Gonzalez](https://dblp.org/pid/61/8262.html), Fisher Yu:

Frustratingly Simple Few-Shot Object Detection. [CoRRabs/2003.06957](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-06957) (2020)
- ![](https://dblp.org/img/n.png)

\[i23\]
[Jiangmiao Pang](https://dblp.org/pid/231/7630.html), [Linlu Qiu](https://dblp.org/pid/267/2348.html), [Haofeng Chen](https://dblp.org/pid/120/5331.html), [Qi Li](https://dblp.org/pid/181/2688.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu:

Quasi-Dense Instance Similarity Learning. [CoRRabs/2006.06664](https://dblp.org/db/journals/corr/corr2006.html#journals/corr/abs-2006-06664) (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[c27\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), Fisher Yu, [Ruth Wang](https://dblp.org/pid/57/4644.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), [Joseph E. Gonzalez](https://dblp.org/pid/61/8262.html)![](https://dblp.org/img/orcid-mark.12x12.png):

TAFE-Net: Task-Aware Feature Embeddings for Low Shot Learning. [CVPR2019](https://dblp.org/db/conf/cvpr/cvpr2019.html#conf/cvpr/WangYWDG19): 1831-1840
- ![](https://dblp.org/img/n.png)

\[c26\]
[Zhichao Yin](https://dblp.org/pid/29/6211.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu:

Hierarchical Discrete Distribution Decomposition for Match Density Estimation. [CVPR2019](https://dblp.org/db/conf/cvpr/cvpr2019.html#conf/cvpr/YinDY19): 6044-6053
- ![](https://dblp.org/img/n.png)

\[c25\]
[Hou-Ning Hu](https://dblp.org/pid/199/3014.html), [Qi-Zhi Cai](https://dblp.org/pid/220/3290.html), [Dequan Wang](https://dblp.org/pid/168/4711.html), [Ji Lin](https://dblp.org/pid/02/8200-2.html), [Min Sun](https://dblp.org/pid/62/2750-1.html), [Philipp Krähenbühl](https://dblp.org/pid/43/7592.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu:

Joint Monocular 3D Vehicle Detection and Tracking. [ICCV2019](https://dblp.org/db/conf/iccv/iccv2019.html#conf/iccv/HuCWLSKDY19): 5389-5398
- ![](https://dblp.org/img/n.png)

\[c24\]
[Bingyi Kang](https://dblp.org/pid/119/7958.html), [Zhuang Liu](https://dblp.org/pid/56/11346-3.html), [Xin Wang](https://dblp.org/pid/10/5630-66.html), Fisher Yu, [Jiashi Feng](https://dblp.org/pid/56/8278.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Few-Shot Object Detection via Feature Reweighting. [ICCV2019](https://dblp.org/db/conf/iccv/iccv2019.html#conf/iccv/KangLWYFD19): 8419-8428
- ![](https://dblp.org/img/n.png)

\[c23\]
[Hang Gao](https://dblp.org/pid/16/6086.html), [Huazhe Xu](https://dblp.org/pid/164/9006.html), [Qi-Zhi Cai](https://dblp.org/pid/220/3290.html), [Ruth Wang](https://dblp.org/pid/57/4644.html), Fisher Yu, [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Disentangling Propagation and Generation for Video Prediction. [ICCV2019](https://dblp.org/db/conf/iccv/iccv2019.html#conf/iccv/GaoXCWYD19): 9005-9014
- ![](https://dblp.org/img/n.png)

\[c22\]
[Xinlei Pan](https://dblp.org/pid/188/6125.html), [Xiangyu Chen](https://dblp.org/pid/84/7543.html), [Qi-Zhi Cai](https://dblp.org/pid/220/3290.html), [John F. Canny](https://dblp.org/pid/c/JohnFCanny.html), Fisher Yu:

Semantic Predictive Control for Explainable and Efficient Policy Learning. [ICRA2019](https://dblp.org/db/conf/icra/icra2019.html#conf/icra/PanCCCY19): 3203-3209
- ![](https://dblp.org/img/n.png)

\[c21\]
[Dequan Wang](https://dblp.org/pid/168/4711.html), [Coline Devin](https://dblp.org/pid/153/1976.html), [Qi-Zhi Cai](https://dblp.org/pid/220/3290.html), Fisher Yu, [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Deep Object-Centric Policies for Autonomous Driving. [ICRA2019](https://dblp.org/db/conf/icra/icra2019.html#conf/icra/WangDCYD19): 8853-8859
- ![](https://dblp.org/img/n.png)

\[c20\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), Fisher Yu, [Lisa Dunlap](https://dblp.org/pid/245/1549.html), [Yi-An Ma](https://dblp.org/pid/178/3243.html), [Ruth Wang](https://dblp.org/pid/57/4644.html), [Azalia Mirhoseini](https://dblp.org/pid/18/8314.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), [Joseph E. Gonzalez](https://dblp.org/pid/61/8262.html):

Deep Mixture of Experts via Shallow Embedding. [UAI2019](https://dblp.org/db/conf/uai/uai2019.html#conf/uai/WangYDMWMDG19): 552-562
- ![](https://dblp.org/img/n.png)

\[i22\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), Fisher Yu, [Ruth Wang](https://dblp.org/pid/57/4644.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), [Joseph E. Gonzalez](https://dblp.org/pid/61/8262.html):

TAFE-Net: Task-Aware Feature Embeddings for Low Shot Learning. [CoRRabs/1904.05967](https://dblp.org/db/journals/corr/corr1904.html#journals/corr/abs-1904-05967) (2019)
- ![](https://dblp.org/img/n.png)

\[i21\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), Fisher Yu, [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), [Joseph E. Gonzalez](https://dblp.org/pid/61/8262.html):

Task-Aware Deep Sampling for Feature Generation. [CoRRabs/1906.04854](https://dblp.org/db/journals/corr/corr1906.html#journals/corr/abs-1906-04854) (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[c19\]
[Huiwen Chang](https://dblp.org/pid/131/4389.html), [Jingwan Lu](https://dblp.org/pid/08/7867.html), Fisher Yu, [Adam Finkelstein](https://dblp.org/pid/f/AdamFinkelstein.html):

PairedCycleGAN: Asymmetric Style Transfer for Applying and Removing Makeup. [CVPR2018](https://dblp.org/db/conf/cvpr/cvpr2018.html#conf/cvpr/ChangLYF18): 40-48
- ![](https://dblp.org/img/n.png)

\[c18\]
Fisher Yu, [Dequan Wang](https://dblp.org/pid/168/4711.html), [Evan Shelhamer](https://dblp.org/pid/150/6541.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Deep Layer Aggregation. [CVPR2018](https://dblp.org/db/conf/cvpr/cvpr2018.html#conf/cvpr/YuWSD18): 2403-2412
- ![](https://dblp.org/img/n.png)

\[c17\]
[Wenqi Xian](https://dblp.org/pid/202/2384.html), [Patsorn Sangkloy](https://dblp.org/pid/182/9370.html), [Varun Agrawal](https://dblp.org/pid/36/6498.html), [Amit Raj](https://dblp.org/pid/84/531.html), [Jingwan Lu](https://dblp.org/pid/08/7867.html), [Chen Fang](https://dblp.org/pid/60/2548.html), Fisher Yu, [James Hays](https://dblp.org/pid/57/5958.html):

TextureGAN: Controlling Deep Image Synthesis With Texture Patches. [CVPR2018](https://dblp.org/db/conf/cvpr/cvpr2018.html#conf/cvpr/XianSARLFYH18): 8456-8465
- ![](https://dblp.org/img/n.png)

\[c16\]
[Chaowei Xiao](https://dblp.org/pid/150/3317.html), [Ruizhi Deng](https://dblp.org/pid/211/6827.html), [Bo Li](https://dblp.org/pid/50/3402-26.html), Fisher Yu, [Mingyan Liu](https://dblp.org/pid/97/5725.html), [Dawn Song](https://dblp.org/pid/s/DXSong.html):

Characterizing Adversarial Examples Based on Spatial Consistency Information for Semantic Segmentation. [ECCV (10)2018](https://dblp.org/db/conf/eccv/eccv2018-10.html#conf/eccv/XiaoDLYLS18): 220-237
- ![](https://dblp.org/img/n.png)

\[c15\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), Fisher Yu, [Zi-Yi Dou](https://dblp.org/pid/205/8985.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), [Joseph E. Gonzalez](https://dblp.org/pid/61/8262.html)![](https://dblp.org/img/orcid-mark.12x12.png):

SkipNet: Learning Dynamic Routing in Convolutional Networks. [ECCV (13)2018](https://dblp.org/db/conf/eccv/eccv2018-13.html#conf/eccv/WangYDDG18): 420-436
- ![](https://dblp.org/img/n.png)

\[c14\]
[Yang Gao](https://dblp.org/pid/89/4402-29.html), [Huazhe Xu](https://dblp.org/pid/164/9006.html), [Ji Lin](https://dblp.org/pid/02/8200-2.html), Fisher Yu, [Sergey Levine](https://dblp.org/pid/80/7594.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Reinforcement Learning from Imperfect Demonstrations. [ICLR (Workshop)2018](https://dblp.org/db/conf/iclr/iclr2018w.html#conf/iclr/GaoXLYLD18)
- ![](https://dblp.org/img/n.png)

\[c13\]
Fisher Yu, [Dequan Wang](https://dblp.org/pid/168/4711.html), [Evan Shelhamer](https://dblp.org/pid/150/6541.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Learning Rich Image Representation with Deep Layer Aggregation. [ICLR (Workshop)2018](https://dblp.org/db/conf/iclr/iclr2018w.html#conf/iclr/YuWSD18)
- ![](https://dblp.org/img/n.png)

\[c12\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), [Yujia Luo](https://dblp.org/pid/202/2062.html), [Daniel Crankshaw](https://dblp.org/pid/132/8701.html), [Alexey Tumanov](https://dblp.org/pid/41/6224.html), Fisher Yu, [Joseph E. Gonzalez](https://dblp.org/pid/61/8262.html):

IDK Cascades: Fast Deep Learning by Learning not to Overthink. [UAI2018](https://dblp.org/db/conf/uai/uai2018.html#conf/uai/WangLCTYG18): 580-590
- ![](https://dblp.org/img/n.png)

\[i20\]
[Yang Gao](https://dblp.org/pid/89/4402-29.html), [Huazhe Xu](https://dblp.org/pid/164/9006.html), [Ji Lin](https://dblp.org/pid/02/8200-2.html), Fisher Yu, [Sergey Levine](https://dblp.org/pid/80/7594.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Reinforcement Learning from Imperfect Demonstrations. [CoRRabs/1802.05313](https://dblp.org/db/journals/corr/corr1802.html#journals/corr/abs-1802-05313) (2018)
- ![](https://dblp.org/img/n.png)

\[i19\]
Fisher Yu, [Wenqi Xian](https://dblp.org/pid/202/2384.html), [Yingying Chen](https://dblp.org/pid/18/2343.html), [Fangchen Liu](https://dblp.org/pid/211/7883.html), [Mike Liao](https://dblp.org/pid/220/3349.html), [Vashisht Madhavan](https://dblp.org/pid/190/2112.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

BDD100K: A Diverse Driving Video Database with Scalable Annotation Tooling. [CoRRabs/1805.04687](https://dblp.org/db/journals/corr/corr1805.html#journals/corr/abs-1805-04687) (2018)
- ![](https://dblp.org/img/n.png)

\[i18\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), Fisher Yu, [Ruth Wang](https://dblp.org/pid/57/4644.html), [Yi-An Ma](https://dblp.org/pid/178/3243.html), [Azalia Mirhoseini](https://dblp.org/pid/18/8314.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), [Joseph E. Gonzalez](https://dblp.org/pid/61/8262.html):

Deep Mixture of Experts via Shallow Embedding. [CoRRabs/1806.01531](https://dblp.org/db/journals/corr/corr1806.html#journals/corr/abs-1806-01531) (2018)
- ![](https://dblp.org/img/n.png)

\[i17\]
[Chaowei Xiao](https://dblp.org/pid/150/3317.html), [Ruizhi Deng](https://dblp.org/pid/211/6827.html), [Bo Li](https://dblp.org/pid/50/3402-26.html), Fisher Yu, [Mingyan Liu](https://dblp.org/pid/97/5725.html), [Dawn Song](https://dblp.org/pid/s/DXSong.html):

Characterizing Adversarial Examples Based on Spatial Consistency Information for Semantic Segmentation. [CoRRabs/1810.05162](https://dblp.org/db/journals/corr/corr1810.html#journals/corr/abs-1810-05162) (2018)
- ![](https://dblp.org/img/n.png)

\[i16\]
[Dequan Wang](https://dblp.org/pid/168/4711.html), [Coline Devin](https://dblp.org/pid/153/1976.html), [Qi-Zhi Cai](https://dblp.org/pid/220/3290.html), Fisher Yu, [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Deep Object Centric Policies for Autonomous Driving. [CoRRabs/1811.05432](https://dblp.org/db/journals/corr/corr1811.html#journals/corr/abs-1811-05432) (2018)
- ![](https://dblp.org/img/n.png)

\[i15\]
[Hou-Ning Hu](https://dblp.org/pid/199/3014.html), [Qi-Zhi Cai](https://dblp.org/pid/220/3290.html), [Dequan Wang](https://dblp.org/pid/168/4711.html), [Ji Lin](https://dblp.org/pid/02/8200-2.html), [Min Sun](https://dblp.org/pid/62/2750-1.html), [Philipp Krähenbühl](https://dblp.org/pid/43/7592.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu:

Joint Monocular 3D Vehicle Detection and Tracking. [CoRRabs/1811.10742](https://dblp.org/db/journals/corr/corr1811.html#journals/corr/abs-1811-10742) (2018)
- ![](https://dblp.org/img/n.png)

\[i14\]
[Hang Gao](https://dblp.org/pid/16/6086.html), [Huazhe Xu](https://dblp.org/pid/164/9006.html), [Qi-Zhi Cai](https://dblp.org/pid/220/3290.html), [Ruth Wang](https://dblp.org/pid/57/4644.html), Fisher Yu, [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Disentangling Propagation and Generation for Video Prediction. [CoRRabs/1812.00452](https://dblp.org/db/journals/corr/corr1812.html#journals/corr/abs-1812-00452) (2018)
- ![](https://dblp.org/img/n.png)

\[i13\]
[Bingyi Kang](https://dblp.org/pid/119/7958.html), [Zhuang Liu](https://dblp.org/pid/56/11346-3.html), [Xin Wang](https://dblp.org/pid/10/5630-66.html), Fisher Yu, [Jiashi Feng](https://dblp.org/pid/56/8278.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Few-shot Object Detection via Feature Reweighting. [CoRRabs/1812.01866](https://dblp.org/db/journals/corr/corr1812.html#journals/corr/abs-1812-01866) (2018)
- ![](https://dblp.org/img/n.png)

\[i12\]
[Zhichao Yin](https://dblp.org/pid/29/6211.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html), Fisher Yu:

Hierarchical Discrete Distribution Decomposition for Match Density Estimation. [CoRRabs/1812.06264](https://dblp.org/db/journals/corr/corr1812.html#journals/corr/abs-1812-06264) (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[c11\]
[Jerry Liu](https://dblp.org/pid/35/874.html), Fisher Yu, [Thomas A. Funkhouser](https://dblp.org/pid/f/TAFunkhouser.html):

Interactive 3D Modeling with a Generative Adversarial Network. [3DV2017](https://dblp.org/db/conf/3dim/3dv2017.html#conf/3dim/LiuYF17): 126-134
- ![](https://dblp.org/img/n.png)

\[c10\]
[Manolis Savva](https://dblp.org/pid/21/9924.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu, [Hao Su](https://dblp.org/pid/09/4945-1.html), [Asako Kanezaki](https://dblp.org/pid/37/7634.html), [Takahiko Furuya](https://dblp.org/pid/57/1639.html), [Ryutarou Ohbuchi](https://dblp.org/pid/57/3819.html), [Zhichao Zhou](https://dblp.org/pid/136/9853.html), [Rui Yu](https://dblp.org/pid/43/4940-2.html), [Song Bai](https://dblp.org/pid/151/6422-1.html), [Xiang Bai](https://dblp.org/pid/59/2741.html), [Masaki Aono](https://dblp.org/pid/48/2961.html), [Atsushi Tatsuma](https://dblp.org/pid/65/7527.html), [Spyridon Thermos](https://dblp.org/pid/181/7680.html), [Apostolos Axenopoulos](https://dblp.org/pid/34/3343.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Georgios Th. Papadopoulos](https://dblp.org/pid/p/GeorgiosThPapadopoulos.html), [Petros Daras](https://dblp.org/pid/30/714.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiao Deng](https://dblp.org/pid/33/8390.html), [Zhouhui Lian](https://dblp.org/pid/20/1780.html), [Bo Li](https://dblp.org/pid/50/3402-13.html), [Henry Johan](https://dblp.org/pid/56/5589.html), [Yijuan Lu](https://dblp.org/pid/30/6535.html), [Sanjeev Mk](https://dblp.org/pid/209/4207.html):

Large-Scale 3D Shape Retrieval from ShapeNet Core55. [3DOR@Eurographics2017](https://dblp.org/db/conf/3dor/3dor2017.html#conf/3dor/SavvaYSKFOZYBBA17)
- ![](https://dblp.org/img/n.png)

\[c9\]
[Shuran Song](https://dblp.org/pid/123/4433.html), Fisher Yu, [Andy Zeng](https://dblp.org/pid/159/1215.html), [Angel X. Chang](https://dblp.org/pid/46/10489.html), [Manolis Savva](https://dblp.org/pid/21/9924.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thomas A. Funkhouser](https://dblp.org/pid/f/TAFunkhouser.html):

Semantic Scene Completion from a Single Depth Image. [CVPR2017](https://dblp.org/db/conf/cvpr/cvpr2017.html#conf/cvpr/SongYZCSF17): 190-198
- ![](https://dblp.org/img/n.png)

\[c8\]
Fisher Yu, [Vladlen Koltun](https://dblp.org/pid/66/5458.html), [Thomas A. Funkhouser](https://dblp.org/pid/f/TAFunkhouser.html):

Dilated Residual Networks. [CVPR2017](https://dblp.org/db/conf/cvpr/cvpr2017.html#conf/cvpr/YuKF17): 636-644
- ![](https://dblp.org/img/n.png)

\[c7\]
[Huazhe Xu](https://dblp.org/pid/164/9006.html), [Yang Gao](https://dblp.org/pid/89/4402-29.html), Fisher Yu, [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

End-to-End Learning of Driving Models from Large-Scale Video Datasets. [CVPR2017](https://dblp.org/db/conf/cvpr/cvpr2017.html#conf/cvpr/XuGYD17): 3530-3538
- ![](https://dblp.org/img/n.png)

\[c6\]
[Patsorn Sangkloy](https://dblp.org/pid/182/9370.html), [Jingwan Lu](https://dblp.org/pid/08/7867.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chen Fang](https://dblp.org/pid/60/2548.html), Fisher Yu, [James Hays](https://dblp.org/pid/57/5958.html):

Scribbler: Controlling Deep Image Synthesis with Sketch and Color. [CVPR2017](https://dblp.org/db/conf/cvpr/cvpr2017.html#conf/cvpr/SangkloyLFYH17): 6836-6845
- ![](https://dblp.org/img/n.png)

\[i11\]
Fisher Yu, [Vladlen Koltun](https://dblp.org/pid/66/5458.html), [Thomas A. Funkhouser](https://dblp.org/pid/f/TAFunkhouser.html):

Dilated Residual Networks. [CoRRabs/1705.09914](https://dblp.org/db/journals/corr/corr1705.html#journals/corr/YuKF17) (2017)
- ![](https://dblp.org/img/n.png)

\[i10\]
[Wenqi Xian](https://dblp.org/pid/202/2384.html), [Patsorn Sangkloy](https://dblp.org/pid/182/9370.html), [Jingwan Lu](https://dblp.org/pid/08/7867.html), [Chen Fang](https://dblp.org/pid/60/2548.html), Fisher Yu, [James Hays](https://dblp.org/pid/57/5958.html):

TextureGAN: Controlling Deep Image Synthesis with Texture Patches. [CoRRabs/1706.02823](https://dblp.org/db/journals/corr/corr1706.html#journals/corr/XianSLFYH17) (2017)
- ![](https://dblp.org/img/n.png)

\[i9\]
[Jerry Liu](https://dblp.org/pid/35/874.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu, [Thomas A. Funkhouser](https://dblp.org/pid/f/TAFunkhouser.html):

Interactive 3D Modeling with a Generative Adversarial Network. [CoRRabs/1706.05170](https://dblp.org/db/journals/corr/corr1706.html#journals/corr/LiuYF17) (2017)
- ![](https://dblp.org/img/n.png)

\[i8\]
Fisher Yu, [Dequan Wang](https://dblp.org/pid/168/4711.html), [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

Deep Layer Aggregation. [CoRRabs/1707.06484](https://dblp.org/db/journals/corr/corr1707.html#journals/corr/YuWD17) (2017)
- ![](https://dblp.org/img/n.png)

\[i7\]
[Xin Wang](https://dblp.org/pid/10/5630-66.html), Fisher Yu, [Zi-Yi Dou](https://dblp.org/pid/205/8985.html), [Joseph E. Gonzalez](https://dblp.org/pid/61/8262.html):

SkipNet: Learning Dynamic Routing in Convolutional Networks. [CoRRabs/1711.09485](https://dblp.org/db/journals/corr/corr1711.html#journals/corr/abs-1711-09485) (2017)
- 2016
- ![](https://dblp.org/img/n.png)

\[j2\]
[Huiwen Chang](https://dblp.org/pid/131/4389.html), Fisher Yu, [Jue Wang](https://dblp.org/pid/69/393-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Douglas Ashley](https://dblp.org/pid/183/9389.html), [Adam Finkelstein](https://dblp.org/pid/f/AdamFinkelstein.html):

Automatic triage for a photo series. [ACM Trans. Graph.35(4)](https://dblp.org/db/journals/tog/tog35.html#journals/tog/Finkelstein16): 148:1-148:10 (2016)
- ![](https://dblp.org/img/n.png)

\[c5\]
[Manolis Savva](https://dblp.org/pid/21/9924.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu, [Hao Su](https://dblp.org/pid/09/4945-1.html), [Masaki Aono](https://dblp.org/pid/48/2961.html), [Baoquan Chen](https://dblp.org/pid/23/4197.html), [Daniel Cohen-Or](https://dblp.org/pid/c/DCohenOr.html), [Weihong Deng](https://dblp.org/pid/39/232.html), [Hang Su](https://dblp.org/pid/26/5371-5.html), [Song Bai](https://dblp.org/pid/151/6422-1.html), [Xiang Bai](https://dblp.org/pid/59/2741.html), [Noa Fish](https://dblp.org/pid/134/7200.html), [Jiajie Han](https://dblp.org/pid/169/7261.html), [Evangelos Kalogerakis](https://dblp.org/pid/36/3187.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Erik G. Learned-Miller](https://dblp.org/pid/l/ErikGLearnedMiller.html), [Yangyan Li](https://dblp.org/pid/50/8293.html), [Minghui Liao](https://dblp.org/pid/190/7335.html), [Subhransu Maji](https://dblp.org/pid/92/6598.html), [Atsushi Tatsuma](https://dblp.org/pid/65/7527.html), [Yida Wang](https://dblp.org/pid/17/1701-1.html), [Nanhai Zhang](https://dblp.org/pid/169/7234.html), [Zhichao Zhou](https://dblp.org/pid/136/9853.html):

Large-Scale 3D Shape Retrieval from ShapeNet Core55. [3DOR@Eurographics2016](https://dblp.org/db/conf/3dor/3dor2016.html#conf/3dor/SavvaYSACCDSBBF16)
- ![](https://dblp.org/img/n.png)

\[c4\]
Fisher Yu, [Vladlen Koltun](https://dblp.org/pid/66/5458.html):

Multi-Scale Context Aggregation by Dilated Convolutions. [ICLR (Poster)2016](https://dblp.org/db/conf/iclr/iclr2016.html#conf/iclr/YuK15)
- ![](https://dblp.org/img/n.png)

\[i6\]
[Shuran Song](https://dblp.org/pid/123/4433.html), Fisher Yu, [Andy Zeng](https://dblp.org/pid/159/1215.html), [Angel X. Chang](https://dblp.org/pid/46/10489.html), [Manolis Savva](https://dblp.org/pid/21/9924.html), [Thomas A. Funkhouser](https://dblp.org/pid/f/TAFunkhouser.html):

Semantic Scene Completion from a Single Depth Image. [CoRRabs/1611.08974](https://dblp.org/db/journals/corr/corr1611.html#journals/corr/SongYZCSF16) (2016)
- ![](https://dblp.org/img/n.png)

\[i5\]
[Patsorn Sangkloy](https://dblp.org/pid/182/9370.html), [Jingwan Lu](https://dblp.org/pid/08/7867.html), [Chen Fang](https://dblp.org/pid/60/2548.html), Fisher Yu, [James Hays](https://dblp.org/pid/57/5958.html):

Scribbler: Controlling Deep Image Synthesis with Sketch and Color. [CoRRabs/1612.00835](https://dblp.org/db/journals/corr/corr1612.html#journals/corr/SangkloyLFYH16) (2016)
- ![](https://dblp.org/img/n.png)

\[i4\]
[Huazhe Xu](https://dblp.org/pid/164/9006.html), [Yang Gao](https://dblp.org/pid/89/4402-29.html), Fisher Yu, [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

End-to-end Learning of Driving Models from Large-scale Video Datasets. [CoRRabs/1612.01079](https://dblp.org/db/journals/corr/corr1612.html#journals/corr/XuGYD16) (2016)
- ![](https://dblp.org/img/n.png)

\[i3\]
[Judy Hoffman](https://dblp.org/pid/45/10336.html), [Dequan Wang](https://dblp.org/pid/168/4711.html), Fisher Yu, [Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html):

FCNs in the Wild: Pixel-level Adversarial and Constraint-based Adaptation. [CoRRabs/1612.02649](https://dblp.org/db/journals/corr/corr1612.html#journals/corr/HoffmanWYD16) (2016)
- 2015
- ![](https://dblp.org/img/n.png)

\[c3\]
Fisher Yu, [Jianxiong Xiao](https://dblp.org/pid/57/5248.html), [Thomas A. Funkhouser](https://dblp.org/pid/f/TAFunkhouser.html):

Semantic alignment of LiDAR data at city scale. [CVPR2015](https://dblp.org/db/conf/cvpr/cvpr2015.html#conf/cvpr/YuXF15): 1722-1731
- ![](https://dblp.org/img/n.png)

\[c2\]
[Zhirong Wu](https://dblp.org/pid/147/5025.html), [Shuran Song](https://dblp.org/pid/123/4433.html), [Aditya Khosla](https://dblp.org/pid/01/8315.html), Fisher Yu, [Linguang Zhang](https://dblp.org/pid/166/1290.html), [Xiaoou Tang](https://dblp.org/pid/04/5226.html), [Jianxiong Xiao](https://dblp.org/pid/57/5248.html):

3D ShapeNets: A deep representation for volumetric shapes. [CVPR2015](https://dblp.org/db/conf/cvpr/cvpr2015.html#conf/cvpr/WuSKYZTX15): 1912-1920
- ![](https://dblp.org/img/n.png)

\[i2\]
Fisher Yu, [Yinda Zhang](https://dblp.org/pid/135/4896-1.html), [Shuran Song](https://dblp.org/pid/123/4433.html), [Ari Seff](https://dblp.org/pid/147/5247.html), [Jianxiong Xiao](https://dblp.org/pid/57/5248.html):

LSUN: Construction of a Large-scale Image Dataset using Deep Learning with Humans in the Loop. [CoRRabs/1506.03365](https://dblp.org/db/journals/corr/corr1506.html#journals/corr/YuZSSX15) (2015)
- ![](https://dblp.org/img/n.png)

\[i1\]
[Angel X. Chang](https://dblp.org/pid/46/10489.html), [Thomas A. Funkhouser](https://dblp.org/pid/f/TAFunkhouser.html), [Leonidas J. Guibas](https://dblp.org/pid/g/LeonidasJGuibas.html), [Pat Hanrahan](https://dblp.org/pid/h/PatHanrahan.html), [Qi-Xing Huang](https://dblp.org/pid/82/241.html), [Zimo Li](https://dblp.org/pid/150/6829.html), [Silvio Savarese](https://dblp.org/pid/50/3578.html), [Manolis Savva](https://dblp.org/pid/21/9924.html), [Shuran Song](https://dblp.org/pid/123/4433.html), [Hao Su](https://dblp.org/pid/09/4945-1.html), [Jianxiong Xiao](https://dblp.org/pid/57/5248.html), [Li Yi](https://dblp.org/pid/26/4239-1.html), Fisher Yu:

ShapeNet: An Information-Rich 3D Model Repository. [CoRRabs/1512.03012](https://dblp.org/db/journals/corr/corr1512.html#journals/corr/ChangFGHHLSSSSX15) (2015)
- 2014
- ![](https://dblp.org/img/n.png)

\[c1\]
Fisher Yu, [David Gallup](https://dblp.org/pid/28/5581.html):

3D Reconstruction from Accidental Motion. [CVPR2014](https://dblp.org/db/conf/cvpr/cvpr2014.html#conf/cvpr/YuG14a): 3986-3993
- 2012
- ![](https://dblp.org/img/n.png)

\[j1\]
[Jingwan Lu](https://dblp.org/pid/08/7867.html)![](https://dblp.org/img/orcid-mark.12x12.png), Fisher Yu, [Adam Finkelstein](https://dblp.org/pid/f/AdamFinkelstein.html), [Stephen DiVerdi](https://dblp.org/pid/03/2531.html):

HelpingHand: example-based stroke stylization. [ACM Trans. Graph.31(4)](https://dblp.org/db/journals/tog/tog31.html#journals/tog/LuYFD12): 46:1-46:10 (2012)
- _no results_

automatic loading of the coauthor graph disabled due to its size.

**click here to**
**load the graph.**

Note that this feature is _work in progress_ and that it is still far from being perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/117/6314.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jan Ackermann](https://dblp.org/pid/348/6561.html)

[\[c84\]](https://dblp.org/pid/117/6314.html#c84) [\[i76\]](https://dblp.org/pid/117/6314.html#i76)

[2](https://dblp.org/pid/117/6314.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Maria Isabel Agea](https://dblp.org/pid/355/2674.html)

[\[c72\]](https://dblp.org/pid/117/6314.html#c72) [\[i67\]](https://dblp.org/pid/117/6314.html#i67)

[3](https://dblp.org/pid/117/6314.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Varun Agrawal](https://dblp.org/pid/36/6498.html)

[\[c17\]](https://dblp.org/pid/117/6314.html#c17)

[4](https://dblp.org/pid/117/6314.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Noor Al-Shakarji](https://dblp.org/pid/188/7419.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[5](https://dblp.org/pid/117/6314.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ibrahim Alabdulmohsin](https://dblp.org/pid/153/5393.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[6](https://dblp.org/pid/117/6314.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Dong An](https://dblp.org/pid/02/7028.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[7](https://dblp.org/pid/117/6314.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Masaki Aono](https://dblp.org/pid/48/2961.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10) [\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[8](https://dblp.org/pid/117/6314.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Michael Arens](https://dblp.org/pid/69/5391.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[9](https://dblp.org/pid/117/6314.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Anurag Arnab](https://dblp.org/pid/165/9719.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[10](https://dblp.org/pid/117/6314.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Douglas Ashley](https://dblp.org/pid/183/9389.html)

[\[j2\]](https://dblp.org/pid/117/6314.html#j2)

[11](https://dblp.org/pid/117/6314.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Apostolos Axenopoulos](https://dblp.org/pid/34/3343.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[12](https://dblp.org/pid/117/6314.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Song Bai 0001](https://dblp.org/pid/151/6422-1.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10) [\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[13](https://dblp.org/pid/117/6314.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiang Bai](https://dblp.org/pid/59/2741.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10) [\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[14](https://dblp.org/pid/117/6314.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jasmijn Bastings](https://dblp.org/pid/146/3824.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[15](https://dblp.org/pid/117/6314.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Stefan Becker](https://dblp.org/pid/62/7091.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[16](https://dblp.org/pid/117/6314.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Kang Ben](https://dblp.org/pid/340/0959.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[17](https://dblp.org/pid/117/6314.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Alex Bewley](https://dblp.org/pid/39/9969.html)

[\[c73\]](https://dblp.org/pid/117/6314.html#c73) [\[i68\]](https://dblp.org/pid/117/6314.html#i68)

[18](https://dblp.org/pid/117/6314.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Lucas Beyer](https://dblp.org/pid/126/4720.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[19](https://dblp.org/pid/117/6314.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c53\]](https://dblp.org/pid/117/6314.html#c53) [\[c45\]](https://dblp.org/pid/117/6314.html#c45) [\[c41\]](https://dblp.org/pid/117/6314.html#c41) [\[i54\]](https://dblp.org/pid/117/6314.html#i54) [\[i46\]](https://dblp.org/pid/117/6314.html#i46) [\[c38\]](https://dblp.org/pid/117/6314.html#c38) [\[i30\]](https://dblp.org/pid/117/6314.html#i30)

[20](https://dblp.org/pid/117/6314.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Mario Bijelic](https://dblp.org/pid/228/4623.html)

[\[c50\]](https://dblp.org/pid/117/6314.html#c50) [\[i53\]](https://dblp.org/pid/117/6314.html#i53)

[21](https://dblp.org/pid/117/6314.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Vighnesh Birodkar](https://dblp.org/pid/186/8043.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[22](https://dblp.org/pid/117/6314.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Johanna Björklund](https://dblp.org/pid/75/5525.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[23](https://dblp.org/pid/117/6314.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[David Brüggemann](https://dblp.org/pid/271/0154.html)

[\[j10\]](https://dblp.org/pid/117/6314.html#j10) [\[c58\]](https://dblp.org/pid/117/6314.html#c58) [\[i75\]](https://dblp.org/pid/117/6314.html#i75) [\[i44\]](https://dblp.org/pid/117/6314.html#i44)

[24](https://dblp.org/pid/117/6314.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Nick Bührer](https://dblp.org/pid/280/2118.html)

[\[c65\]](https://dblp.org/pid/117/6314.html#c65) [\[i81\]](https://dblp.org/pid/117/6314.html#i81)

[25](https://dblp.org/pid/117/6314.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Sebastian Bullinger](https://dblp.org/pid/197/9724.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[26](https://dblp.org/pid/117/6314.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Samuel Rota Bulò](https://dblp.org/pid/05/4139.html)

[\[c59\]](https://dblp.org/pid/117/6314.html#c59) [\[i28\]](https://dblp.org/pid/117/6314.html#i28)

[27](https://dblp.org/pid/117/6314.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Dingding Cai](https://dblp.org/pid/198/1127.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[28](https://dblp.org/pid/117/6314.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jianfei Cai 0001](https://dblp.org/pid/83/6096.html)

[\[j6\]](https://dblp.org/pid/117/6314.html#j6) [\[i41\]](https://dblp.org/pid/117/6314.html#i41)

[29](https://dblp.org/pid/117/6314.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Qi-Zhi Cai](https://dblp.org/pid/220/3290.html)

[\[c25\]](https://dblp.org/pid/117/6314.html#c25) [\[c23\]](https://dblp.org/pid/117/6314.html#c23) [\[c22\]](https://dblp.org/pid/117/6314.html#c22) [\[c21\]](https://dblp.org/pid/117/6314.html#c21) [\[i16\]](https://dblp.org/pid/117/6314.html#i16) [\[i15\]](https://dblp.org/pid/117/6314.html#i15) [\[i14\]](https://dblp.org/pid/117/6314.html#i14)

[30](https://dblp.org/pid/117/6314.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhongang Cai](https://dblp.org/pid/232/3190.html)

[\[c68\]](https://dblp.org/pid/117/6314.html#c68) [\[i85\]](https://dblp.org/pid/117/6314.html#i85)

[31](https://dblp.org/pid/117/6314.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[John F. Canny](https://dblp.org/pid/c/JohnFCanny.html)

[\[c22\]](https://dblp.org/pid/117/6314.html#c22)

[32](https://dblp.org/pid/117/6314.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jinkun Cao](https://dblp.org/pid/224/0126.html)

[\[c32\]](https://dblp.org/pid/117/6314.html#c32) [\[i38\]](https://dblp.org/pid/117/6314.html#i38)

[33](https://dblp.org/pid/117/6314.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Mathilde Caron](https://dblp.org/pid/223/4085.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[34](https://dblp.org/pid/117/6314.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[35](https://dblp.org/pid/117/6314.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Antoni B. Chan](https://dblp.org/pid/55/5814.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[36](https://dblp.org/pid/117/6314.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Angel X. Chang](https://dblp.org/pid/46/10489.html)

[\[c9\]](https://dblp.org/pid/117/6314.html#c9) [\[i6\]](https://dblp.org/pid/117/6314.html#i6) [\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[37](https://dblp.org/pid/117/6314.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hong Chang 0001](https://dblp.org/pid/02/2689-1.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[38](https://dblp.org/pid/117/6314.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Huiwen Chang](https://dblp.org/pid/131/4389.html)

[\[c19\]](https://dblp.org/pid/117/6314.html#c19) [\[j2\]](https://dblp.org/pid/117/6314.html#j2)

[39](https://dblp.org/pid/117/6314.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[40](https://dblp.org/pid/117/6314.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Shijie Chang](https://dblp.org/pid/277/8125.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[41](https://dblp.org/pid/117/6314.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Anpei Chen](https://dblp.org/pid/210/2592.html)

[\[c95\]](https://dblp.org/pid/117/6314.html#c95) [\[i58\]](https://dblp.org/pid/117/6314.html#i58)

[42](https://dblp.org/pid/117/6314.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Baoquan Chen](https://dblp.org/pid/23/4197.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[43](https://dblp.org/pid/117/6314.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Guangqi Chen](https://dblp.org/pid/178/8116.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[44](https://dblp.org/pid/117/6314.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hanyuan Chen](https://dblp.org/pid/363/8621.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[45](https://dblp.org/pid/117/6314.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Haofeng Chen](https://dblp.org/pid/120/5331.html)

[\[j5\]](https://dblp.org/pid/117/6314.html#j5) [\[i45\]](https://dblp.org/pid/117/6314.html#i45) [\[c39\]](https://dblp.org/pid/117/6314.html#c39) [\[c30\]](https://dblp.org/pid/117/6314.html#c30) [\[i23\]](https://dblp.org/pid/117/6314.html#i23)

[46](https://dblp.org/pid/117/6314.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiaye Chen](https://dblp.org/pid/116/2901.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[47](https://dblp.org/pid/117/6314.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Junting Chen](https://dblp.org/pid/56/9060.html)

[\[c60\]](https://dblp.org/pid/117/6314.html#c60) [\[i77\]](https://dblp.org/pid/117/6314.html#i77)

[48](https://dblp.org/pid/117/6314.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Le Chen](https://dblp.org/pid/19/576.html)

[\[j3\]](https://dblp.org/pid/117/6314.html#j3) [\[i47\]](https://dblp.org/pid/117/6314.html#i47)

[49](https://dblp.org/pid/117/6314.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Nuo Chen 0003](https://dblp.org/pid/135/5622-3.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[50](https://dblp.org/pid/117/6314.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Qijun Chen](https://dblp.org/pid/75/1639.html)

[\[j8\]](https://dblp.org/pid/117/6314.html#j8) [\[i92\]](https://dblp.org/pid/117/6314.html#i92)

[51](https://dblp.org/pid/117/6314.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[52](https://dblp.org/pid/117/6314.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Weirong Chen](https://dblp.org/pid/96/398.html)

[\[j4\]](https://dblp.org/pid/117/6314.html#j4) [\[i84\]](https://dblp.org/pid/117/6314.html#i84)

[53](https://dblp.org/pid/117/6314.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiangyu Chen](https://dblp.org/pid/84/7543.html)

[\[c22\]](https://dblp.org/pid/117/6314.html#c22)

[54](https://dblp.org/pid/117/6314.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xilin Chen 0001](https://dblp.org/pid/c/XilinChen.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[55](https://dblp.org/pid/117/6314.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[56](https://dblp.org/pid/117/6314.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiuyi Chen](https://dblp.org/pid/218/7190.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[57](https://dblp.org/pid/117/6314.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yan Chen 0017](https://dblp.org/pid/88/2827-17.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[58](https://dblp.org/pid/117/6314.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yingying Chen](https://dblp.org/pid/18/2343.html)

[\[c30\]](https://dblp.org/pid/117/6314.html#c30) [\[i19\]](https://dblp.org/pid/117/6314.html#i19)

[59](https://dblp.org/pid/117/6314.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yiwei Chen](https://dblp.org/pid/28/2965.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[60](https://dblp.org/pid/117/6314.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yu-Hsi Chen](https://dblp.org/pid/127/3933.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[61](https://dblp.org/pid/117/6314.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yuedong Chen](https://dblp.org/pid/236/6258.html)

[\[c95\]](https://dblp.org/pid/117/6314.html#c95) [\[i58\]](https://dblp.org/pid/117/6314.html#i58)

[62](https://dblp.org/pid/117/6314.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zheng Chen 0014](https://dblp.org/pid/33/2592-14.html)

[\[c74\]](https://dblp.org/pid/117/6314.html#c74) [\[i69\]](https://dblp.org/pid/117/6314.html#i69)

[63](https://dblp.org/pid/117/6314.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhenyu Chen 0001](https://dblp.org/pid/86/541-1.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[64](https://dblp.org/pid/117/6314.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhixing Chen](https://dblp.org/pid/62/3074.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[65](https://dblp.org/pid/117/6314.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yangming Cheng](https://dblp.org/pid/340/1285.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[66](https://dblp.org/pid/117/6314.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ajad Chhatkuli](https://dblp.org/pid/149/7655.html)

[\[c48\]](https://dblp.org/pid/117/6314.html#c48) [\[i29\]](https://dblp.org/pid/117/6314.html#i29)

[67](https://dblp.org/pid/117/6314.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Vasileios Choutas](https://dblp.org/pid/230/1246.html)

[\[c57\]](https://dblp.org/pid/117/6314.html#c57) [\[i48\]](https://dblp.org/pid/117/6314.html#i48)

[68](https://dblp.org/pid/117/6314.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Angelo Ciaramella](https://dblp.org/pid/37/6845.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[69](https://dblp.org/pid/117/6314.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Daniel Cohen-Or](https://dblp.org/pid/c/DCohenOr.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[70](https://dblp.org/pid/117/6314.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Mark Collier](https://dblp.org/pid/223/9928.html)

aka: Mark Patrick Collier

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[71](https://dblp.org/pid/117/6314.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[David Crandall](https://dblp.org/pid/c/DavidCrandall.html)

[\[j9\]](https://dblp.org/pid/117/6314.html#j9)

[72](https://dblp.org/pid/117/6314.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Daniel Crankshaw](https://dblp.org/pid/132/8701.html)

[\[c12\]](https://dblp.org/pid/117/6314.html#c12)

[73](https://dblp.org/pid/117/6314.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[74](https://dblp.org/pid/117/6314.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[75](https://dblp.org/pid/117/6314.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Dengxin Dai](https://dblp.org/pid/98/8616.html)

[\[c70\]](https://dblp.org/pid/117/6314.html#c70) [\[c67\]](https://dblp.org/pid/117/6314.html#c67) [\[i82\]](https://dblp.org/pid/117/6314.html#i82) [\[c50\]](https://dblp.org/pid/117/6314.html#c50) [\[c48\]](https://dblp.org/pid/117/6314.html#c48) [\[i53\]](https://dblp.org/pid/117/6314.html#i53) [\[i42\]](https://dblp.org/pid/117/6314.html#i42) [\[c34\]](https://dblp.org/pid/117/6314.html#c34) [\[i31\]](https://dblp.org/pid/117/6314.html#i31) [\[i29\]](https://dblp.org/pid/117/6314.html#i29)

[76](https://dblp.org/pid/117/6314.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jifeng Dai](https://dblp.org/pid/14/9399.html)

[\[c37\]](https://dblp.org/pid/117/6314.html#c37) [\[i37\]](https://dblp.org/pid/117/6314.html#i37)

[77](https://dblp.org/pid/117/6314.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c99\]](https://dblp.org/pid/117/6314.html#c99) [\[c96\]](https://dblp.org/pid/117/6314.html#c96) [\[c93\]](https://dblp.org/pid/117/6314.html#c93) [\[c91\]](https://dblp.org/pid/117/6314.html#c91) [\[c90\]](https://dblp.org/pid/117/6314.html#c90) [\[c89\]](https://dblp.org/pid/117/6314.html#c89) [\[i89\]](https://dblp.org/pid/117/6314.html#i89) [\[c83\]](https://dblp.org/pid/117/6314.html#c83) [\[c81\]](https://dblp.org/pid/117/6314.html#c81) [\[c79\]](https://dblp.org/pid/117/6314.html#c79) [\[c77\]](https://dblp.org/pid/117/6314.html#c77) [\[c72\]](https://dblp.org/pid/117/6314.html#c72) [\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c64\]](https://dblp.org/pid/117/6314.html#c64) [\[c63\]](https://dblp.org/pid/117/6314.html#c63) [\[c62\]](https://dblp.org/pid/117/6314.html#c62) [\[i80\]](https://dblp.org/pid/117/6314.html#i80) [\[i78\]](https://dblp.org/pid/117/6314.html#i78) [\[i74\]](https://dblp.org/pid/117/6314.html#i74) [\[i72\]](https://dblp.org/pid/117/6314.html#i72) [\[i71\]](https://dblp.org/pid/117/6314.html#i71) [\[i70\]](https://dblp.org/pid/117/6314.html#i70) [\[i67\]](https://dblp.org/pid/117/6314.html#i67) [\[i66\]](https://dblp.org/pid/117/6314.html#i66) [\[i59\]](https://dblp.org/pid/117/6314.html#i59) [\[c55\]](https://dblp.org/pid/117/6314.html#c55) [\[c54\]](https://dblp.org/pid/117/6314.html#c54) [\[c53\]](https://dblp.org/pid/117/6314.html#c53) [\[c52\]](https://dblp.org/pid/117/6314.html#c52) [\[c48\]](https://dblp.org/pid/117/6314.html#c48) [\[c45\]](https://dblp.org/pid/117/6314.html#c45) [\[c44\]](https://dblp.org/pid/117/6314.html#c44) [\[c43\]](https://dblp.org/pid/117/6314.html#c43) [\[c41\]](https://dblp.org/pid/117/6314.html#c41) [\[c40\]](https://dblp.org/pid/117/6314.html#c40) [\[i57\]](https://dblp.org/pid/117/6314.html#i57) [\[i55\]](https://dblp.org/pid/117/6314.html#i55) [\[i54\]](https://dblp.org/pid/117/6314.html#i54) [\[i50\]](https://dblp.org/pid/117/6314.html#i50) [\[i49\]](https://dblp.org/pid/117/6314.html#i49) [\[i46\]](https://dblp.org/pid/117/6314.html#i46) [\[c38\]](https://dblp.org/pid/117/6314.html#c38) [\[c35\]](https://dblp.org/pid/117/6314.html#c35) [\[c31\]](https://dblp.org/pid/117/6314.html#c31) [\[i35\]](https://dblp.org/pid/117/6314.html#i35) [\[i33\]](https://dblp.org/pid/117/6314.html#i33) [\[i30\]](https://dblp.org/pid/117/6314.html#i30) [\[i29\]](https://dblp.org/pid/117/6314.html#i29) [\[i27\]](https://dblp.org/pid/117/6314.html#i27) [\[i26\]](https://dblp.org/pid/117/6314.html#i26)

[78](https://dblp.org/pid/117/6314.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Petros Daras](https://dblp.org/pid/30/714.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[79](https://dblp.org/pid/117/6314.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Trevor Darrell](https://dblp.org/pid/d/TrevorDarrell.html)

[\[j7\]](https://dblp.org/pid/117/6314.html#j7) [\[j5\]](https://dblp.org/pid/117/6314.html#j5) [\[i45\]](https://dblp.org/pid/117/6314.html#i45) [\[c39\]](https://dblp.org/pid/117/6314.html#c39) [\[c36\]](https://dblp.org/pid/117/6314.html#c36) [\[c32\]](https://dblp.org/pid/117/6314.html#c32) [\[i38\]](https://dblp.org/pid/117/6314.html#i38) [\[i36\]](https://dblp.org/pid/117/6314.html#i36) [\[i34\]](https://dblp.org/pid/117/6314.html#i34) [\[c30\]](https://dblp.org/pid/117/6314.html#c30) [\[c29\]](https://dblp.org/pid/117/6314.html#c29) [\[c28\]](https://dblp.org/pid/117/6314.html#c28) [\[i24\]](https://dblp.org/pid/117/6314.html#i24) [\[i23\]](https://dblp.org/pid/117/6314.html#i23) [\[c27\]](https://dblp.org/pid/117/6314.html#c27) [\[c26\]](https://dblp.org/pid/117/6314.html#c26) [\[c25\]](https://dblp.org/pid/117/6314.html#c25) [\[c24\]](https://dblp.org/pid/117/6314.html#c24) [\[c23\]](https://dblp.org/pid/117/6314.html#c23) [\[c21\]](https://dblp.org/pid/117/6314.html#c21) [\[c20\]](https://dblp.org/pid/117/6314.html#c20) [\[i22\]](https://dblp.org/pid/117/6314.html#i22) [\[i21\]](https://dblp.org/pid/117/6314.html#i21) [\[c18\]](https://dblp.org/pid/117/6314.html#c18) [\[c15\]](https://dblp.org/pid/117/6314.html#c15) [\[c14\]](https://dblp.org/pid/117/6314.html#c14) [\[c13\]](https://dblp.org/pid/117/6314.html#c13) [\[i20\]](https://dblp.org/pid/117/6314.html#i20) [\[i19\]](https://dblp.org/pid/117/6314.html#i19) [\[i18\]](https://dblp.org/pid/117/6314.html#i18) [\[i16\]](https://dblp.org/pid/117/6314.html#i16) [\[i15\]](https://dblp.org/pid/117/6314.html#i15) [\[i14\]](https://dblp.org/pid/117/6314.html#i14) [\[i13\]](https://dblp.org/pid/117/6314.html#i13) [\[i12\]](https://dblp.org/pid/117/6314.html#i12) [\[c7\]](https://dblp.org/pid/117/6314.html#c7) [\[i8\]](https://dblp.org/pid/117/6314.html#i8) [\[i4\]](https://dblp.org/pid/117/6314.html#i4) [\[i3\]](https://dblp.org/pid/117/6314.html#i3)

[80](https://dblp.org/pid/117/6314.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[81](https://dblp.org/pid/117/6314.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Mostafa Dehghani 0001](https://dblp.org/pid/125/4062.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[82](https://dblp.org/pid/117/6314.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chunyuan Deng](https://dblp.org/pid/154/4071.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[83](https://dblp.org/pid/117/6314.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiajun Deng](https://dblp.org/pid/137/6093.html)

[\[c78\]](https://dblp.org/pid/117/6314.html#c78)

[84](https://dblp.org/pid/117/6314.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[85](https://dblp.org/pid/117/6314.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ruizhi Deng](https://dblp.org/pid/211/6827.html)

[\[c16\]](https://dblp.org/pid/117/6314.html#c16) [\[i17\]](https://dblp.org/pid/117/6314.html#i17)

[86](https://dblp.org/pid/117/6314.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Weihong Deng](https://dblp.org/pid/39/232.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[87](https://dblp.org/pid/117/6314.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiao Deng](https://dblp.org/pid/33/8390.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[88](https://dblp.org/pid/117/6314.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Coline Devin](https://dblp.org/pid/153/1976.html)

[\[c21\]](https://dblp.org/pid/117/6314.html#c21) [\[i16\]](https://dblp.org/pid/117/6314.html#i16)

[89](https://dblp.org/pid/117/6314.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Debajyoti Dhar](https://dblp.org/pid/128/3182.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[90](https://dblp.org/pid/117/6314.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Shangzhe Di](https://dblp.org/pid/304/1344.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[91](https://dblp.org/pid/117/6314.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Henghui Ding](https://dblp.org/pid/230/1216.html)

[\[c83\]](https://dblp.org/pid/117/6314.html#c83) [\[c81\]](https://dblp.org/pid/117/6314.html#c81) [\[i80\]](https://dblp.org/pid/117/6314.html#i80) [\[i78\]](https://dblp.org/pid/117/6314.html#i78) [\[c44\]](https://dblp.org/pid/117/6314.html#c44) [\[c43\]](https://dblp.org/pid/117/6314.html#c43) [\[i50\]](https://dblp.org/pid/117/6314.html#i50) [\[i49\]](https://dblp.org/pid/117/6314.html#i49)

[92](https://dblp.org/pid/117/6314.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yifu Ding](https://dblp.org/pid/219/1995.html)

[\[c68\]](https://dblp.org/pid/117/6314.html#c68) [\[c62\]](https://dblp.org/pid/117/6314.html#c62) [\[i85\]](https://dblp.org/pid/117/6314.html#i85)

[93](https://dblp.org/pid/117/6314.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Stephen DiVerdi](https://dblp.org/pid/03/2531.html)

[\[j1\]](https://dblp.org/pid/117/6314.html#j1)

[94](https://dblp.org/pid/117/6314.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Josip Djolonga](https://dblp.org/pid/139/1342.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[95](https://dblp.org/pid/117/6314.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Nemanja Djuric](https://dblp.org/pid/35/9989.html)

[\[c33\]](https://dblp.org/pid/117/6314.html#c33)

[96](https://dblp.org/pid/117/6314.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiahua Dong 0001](https://dblp.org/pid/247/5746.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[97](https://dblp.org/pid/117/6314.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zi-Yi Dou](https://dblp.org/pid/205/8985.html)

[\[c15\]](https://dblp.org/pid/117/6314.html#c15) [\[i7\]](https://dblp.org/pid/117/6314.html#i7)

[98](https://dblp.org/pid/117/6314.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[99](https://dblp.org/pid/117/6314.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[100](https://dblp.org/pid/117/6314.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Fabian Duerr](https://dblp.org/pid/282/8598.html)

[\[c86\]](https://dblp.org/pid/117/6314.html#c86) [\[i86\]](https://dblp.org/pid/117/6314.html#i86)

[101](https://dblp.org/pid/117/6314.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Lisa Dunlap](https://dblp.org/pid/245/1549.html)

[\[c20\]](https://dblp.org/pid/117/6314.html#c20)

[102](https://dblp.org/pid/117/6314.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[103](https://dblp.org/pid/117/6314.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Benjamin Dzubur](https://dblp.org/pid/340/1520.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[104](https://dblp.org/pid/117/6314.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Gamaleldin F. Elsayed](https://dblp.org/pid/215/4903.html)

aka: Gamaleldin Fathy Elsayed

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[105](https://dblp.org/pid/117/6314.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Francis Engelmann](https://dblp.org/pid/181/4077.html)

[\[c88\]](https://dblp.org/pid/117/6314.html#c88) [\[i93\]](https://dblp.org/pid/117/6314.html#i93)

[106](https://dblp.org/pid/117/6314.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Utku Evci](https://dblp.org/pid/179/8146.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[107](https://dblp.org/pid/117/6314.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Heng Fan 0001](https://dblp.org/pid/20/10120-1.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[108](https://dblp.org/pid/117/6314.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Qi Fan](https://dblp.org/pid/43/4386.html)

[\[c70\]](https://dblp.org/pid/117/6314.html#c70) [\[i42\]](https://dblp.org/pid/117/6314.html#i42)

[109](https://dblp.org/pid/117/6314.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Rui Fan 0001](https://dblp.org/pid/03/1805-1.html)

[\[j8\]](https://dblp.org/pid/117/6314.html#j8) [\[i92\]](https://dblp.org/pid/117/6314.html#i92) [\[c33\]](https://dblp.org/pid/117/6314.html#c33)

[110](https://dblp.org/pid/117/6314.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chen Fang](https://dblp.org/pid/60/2548.html)

[\[c17\]](https://dblp.org/pid/117/6314.html#c17) [\[c6\]](https://dblp.org/pid/117/6314.html#c6) [\[i10\]](https://dblp.org/pid/117/6314.html#i10) [\[i5\]](https://dblp.org/pid/117/6314.html#i5)

[111](https://dblp.org/pid/117/6314.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[112](https://dblp.org/pid/117/6314.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chen Feng 0002](https://dblp.org/pid/01/161-2.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[113](https://dblp.org/pid/117/6314.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiashi Feng](https://dblp.org/pid/56/8278.html)

[\[c24\]](https://dblp.org/pid/117/6314.html#c24) [\[i13\]](https://dblp.org/pid/117/6314.html#i13)

[114](https://dblp.org/pid/117/6314.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Wei Feng 0005](https://dblp.org/pid/17/1152-5.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[115](https://dblp.org/pid/117/6314.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yi Feng](https://dblp.org/pid/39/6758.html)

[\[j8\]](https://dblp.org/pid/117/6314.html#j8) [\[i92\]](https://dblp.org/pid/117/6314.html#i92)

[116](https://dblp.org/pid/117/6314.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[117](https://dblp.org/pid/117/6314.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[118](https://dblp.org/pid/117/6314.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Adam Finkelstein](https://dblp.org/pid/f/AdamFinkelstein.html)

[\[c19\]](https://dblp.org/pid/117/6314.html#c19) [\[j2\]](https://dblp.org/pid/117/6314.html#j2) [\[j1\]](https://dblp.org/pid/117/6314.html#j1)

[119](https://dblp.org/pid/117/6314.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Tobias Fischer 0004](https://dblp.org/pid/249/9213.html)

[\[j7\]](https://dblp.org/pid/117/6314.html#j7) [\[j5\]](https://dblp.org/pid/117/6314.html#j5) [\[c83\]](https://dblp.org/pid/117/6314.html#c83) [\[c79\]](https://dblp.org/pid/117/6314.html#c79) [\[i78\]](https://dblp.org/pid/117/6314.html#i78) [\[i66\]](https://dblp.org/pid/117/6314.html#i66) [\[c56\]](https://dblp.org/pid/117/6314.html#c56) [\[i45\]](https://dblp.org/pid/117/6314.html#i45) [\[i39\]](https://dblp.org/pid/117/6314.html#i39) [\[i36\]](https://dblp.org/pid/117/6314.html#i36)

[120](https://dblp.org/pid/117/6314.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Noa Fish](https://dblp.org/pid/134/7200.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[121](https://dblp.org/pid/117/6314.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jianlong Fu](https://dblp.org/pid/83/8692.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[122](https://dblp.org/pid/117/6314.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiawei Fu 0003](https://dblp.org/pid/194/2277-3.html)

[\[c66\]](https://dblp.org/pid/117/6314.html#c66) [\[i43\]](https://dblp.org/pid/117/6314.html#i43)

[123](https://dblp.org/pid/117/6314.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[124](https://dblp.org/pid/117/6314.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Thomas A. Funkhouser](https://dblp.org/pid/f/TAFunkhouser.html)

[\[c11\]](https://dblp.org/pid/117/6314.html#c11) [\[c9\]](https://dblp.org/pid/117/6314.html#c9) [\[c8\]](https://dblp.org/pid/117/6314.html#c8) [\[i11\]](https://dblp.org/pid/117/6314.html#i11) [\[i9\]](https://dblp.org/pid/117/6314.html#i9) [\[i6\]](https://dblp.org/pid/117/6314.html#i6) [\[c3\]](https://dblp.org/pid/117/6314.html#c3) [\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[125](https://dblp.org/pid/117/6314.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Takahiko Furuya](https://dblp.org/pid/57/1639.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[126](https://dblp.org/pid/117/6314.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[David Gallup](https://dblp.org/pid/28/5581.html)

[\[c1\]](https://dblp.org/pid/117/6314.html#c1)

[127](https://dblp.org/pid/117/6314.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hang Gao](https://dblp.org/pid/16/6086.html)

[\[c23\]](https://dblp.org/pid/117/6314.html#c23) [\[i14\]](https://dblp.org/pid/117/6314.html#i14)

[128](https://dblp.org/pid/117/6314.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jie Gao](https://dblp.org/pid/181/2794.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[129](https://dblp.org/pid/117/6314.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Shang Gao 0012](https://dblp.org/pid/28/435-12.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[130](https://dblp.org/pid/117/6314.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yang Gao 0029](https://dblp.org/pid/89/4402-29.html)

[\[c14\]](https://dblp.org/pid/117/6314.html#c14) [\[i20\]](https://dblp.org/pid/117/6314.html#i20) [\[c7\]](https://dblp.org/pid/117/6314.html#c7) [\[i4\]](https://dblp.org/pid/117/6314.html#i4)

[131](https://dblp.org/pid/117/6314.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Andreas Geiger 0001](https://dblp.org/pid/40/5825-1.html)

[\[c95\]](https://dblp.org/pid/117/6314.html#c95) [\[j6\]](https://dblp.org/pid/117/6314.html#j6) [\[i58\]](https://dblp.org/pid/117/6314.html#i58) [\[i41\]](https://dblp.org/pid/117/6314.html#i41)

[132](https://dblp.org/pid/117/6314.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Robert Geirhos](https://dblp.org/pid/176/0076.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[133](https://dblp.org/pid/117/6314.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Bernard Ghanem](https://dblp.org/pid/37/2516.html)

[\[c60\]](https://dblp.org/pid/117/6314.html#c60) [\[i77\]](https://dblp.org/pid/117/6314.html#i77)

[134](https://dblp.org/pid/117/6314.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Justin Gilmer](https://dblp.org/pid/131/6545.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[135](https://dblp.org/pid/117/6314.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Daniel Göhring](https://dblp.org/pid/97/3289.html)

aka: Daniel Goehring

[\[c86\]](https://dblp.org/pid/117/6314.html#c86) [\[i86\]](https://dblp.org/pid/117/6314.html#i86)

[136](https://dblp.org/pid/117/6314.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Moonjun Gong](https://dblp.org/pid/349/4889.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[137](https://dblp.org/pid/117/6314.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Rui Gong](https://dblp.org/pid/75/1938.html)

[\[c48\]](https://dblp.org/pid/117/6314.html#c48) [\[i29\]](https://dblp.org/pid/117/6314.html#i29)

[138](https://dblp.org/pid/117/6314.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Joseph Gonzalez 0001](https://dblp.org/pid/61/8262.html)

aka: Joseph E. Gonzalez

[\[c36\]](https://dblp.org/pid/117/6314.html#c36) [\[i34\]](https://dblp.org/pid/117/6314.html#i34) [\[c28\]](https://dblp.org/pid/117/6314.html#c28) [\[i24\]](https://dblp.org/pid/117/6314.html#i24) [\[c27\]](https://dblp.org/pid/117/6314.html#c27) [\[c20\]](https://dblp.org/pid/117/6314.html#c20) [\[i22\]](https://dblp.org/pid/117/6314.html#i22) [\[i21\]](https://dblp.org/pid/117/6314.html#i21) [\[c15\]](https://dblp.org/pid/117/6314.html#c15) [\[c12\]](https://dblp.org/pid/117/6314.html#c12) [\[i18\]](https://dblp.org/pid/117/6314.html#i18) [\[i7\]](https://dblp.org/pid/117/6314.html#i7)

[139](https://dblp.org/pid/117/6314.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[j10\]](https://dblp.org/pid/117/6314.html#j10) [\[c97\]](https://dblp.org/pid/117/6314.html#c97) [\[c96\]](https://dblp.org/pid/117/6314.html#c96) [\[c94\]](https://dblp.org/pid/117/6314.html#c94) [\[c89\]](https://dblp.org/pid/117/6314.html#c89) [\[i90\]](https://dblp.org/pid/117/6314.html#i90) [\[i89\]](https://dblp.org/pid/117/6314.html#i89) [\[i87\]](https://dblp.org/pid/117/6314.html#i87) [\[c76\]](https://dblp.org/pid/117/6314.html#c76) [\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c67\]](https://dblp.org/pid/117/6314.html#c67) [\[c65\]](https://dblp.org/pid/117/6314.html#c65) [\[c61\]](https://dblp.org/pid/117/6314.html#c61) [\[c58\]](https://dblp.org/pid/117/6314.html#c58) [\[c57\]](https://dblp.org/pid/117/6314.html#c57) [\[i82\]](https://dblp.org/pid/117/6314.html#i82) [\[i81\]](https://dblp.org/pid/117/6314.html#i81) [\[i75\]](https://dblp.org/pid/117/6314.html#i75) [\[i65\]](https://dblp.org/pid/117/6314.html#i65) [\[i64\]](https://dblp.org/pid/117/6314.html#i64) [\[i60\]](https://dblp.org/pid/117/6314.html#i60) [\[c54\]](https://dblp.org/pid/117/6314.html#c54) [\[c53\]](https://dblp.org/pid/117/6314.html#c53) [\[c52\]](https://dblp.org/pid/117/6314.html#c52) [\[c50\]](https://dblp.org/pid/117/6314.html#c50) [\[c49\]](https://dblp.org/pid/117/6314.html#c49) [\[c48\]](https://dblp.org/pid/117/6314.html#c48) [\[c47\]](https://dblp.org/pid/117/6314.html#c47) [\[c45\]](https://dblp.org/pid/117/6314.html#c45) [\[c42\]](https://dblp.org/pid/117/6314.html#c42) [\[c40\]](https://dblp.org/pid/117/6314.html#c40) [\[i57\]](https://dblp.org/pid/117/6314.html#i57) [\[i55\]](https://dblp.org/pid/117/6314.html#i55) [\[i54\]](https://dblp.org/pid/117/6314.html#i54) [\[i53\]](https://dblp.org/pid/117/6314.html#i53) [\[i52\]](https://dblp.org/pid/117/6314.html#i52) [\[i51\]](https://dblp.org/pid/117/6314.html#i51) [\[i48\]](https://dblp.org/pid/117/6314.html#i48) [\[i44\]](https://dblp.org/pid/117/6314.html#i44) [\[c38\]](https://dblp.org/pid/117/6314.html#c38) [\[c37\]](https://dblp.org/pid/117/6314.html#c37) [\[c35\]](https://dblp.org/pid/117/6314.html#c35) [\[c34\]](https://dblp.org/pid/117/6314.html#c34) [\[i37\]](https://dblp.org/pid/117/6314.html#i37) [\[i35\]](https://dblp.org/pid/117/6314.html#i35) [\[i32\]](https://dblp.org/pid/117/6314.html#i32) [\[i31\]](https://dblp.org/pid/117/6314.html#i31) [\[i30\]](https://dblp.org/pid/117/6314.html#i30) [\[i29\]](https://dblp.org/pid/117/6314.html#i29) [\[i27\]](https://dblp.org/pid/117/6314.html#i27)

[140](https://dblp.org/pid/117/6314.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[141](https://dblp.org/pid/117/6314.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Eric Granger](https://dblp.org/pid/86/2306.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[142](https://dblp.org/pid/117/6314.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Alexey A. Gritsenko](https://dblp.org/pid/30/11478.html)

[\[c73\]](https://dblp.org/pid/117/6314.html#c73) [\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83) [\[i68\]](https://dblp.org/pid/117/6314.html#i68)

[143](https://dblp.org/pid/117/6314.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jinjin Gu](https://dblp.org/pid/209/5709.html)

[\[c74\]](https://dblp.org/pid/117/6314.html#c74) [\[i69\]](https://dblp.org/pid/117/6314.html#i69)

[144](https://dblp.org/pid/117/6314.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Q. H. Gu](https://dblp.org/pid/340/1209.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[145](https://dblp.org/pid/117/6314.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Leonidas J. Guibas](https://dblp.org/pid/g/LeonidasJGuibas.html)

[\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[146](https://dblp.org/pid/117/6314.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhenhua Guo 0001](https://dblp.org/pid/41/294-1.html)

[\[c91\]](https://dblp.org/pid/117/6314.html#c91) [\[i70\]](https://dblp.org/pid/117/6314.html#i70)

[147](https://dblp.org/pid/117/6314.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Himanshu Gupta 0003](https://dblp.org/pid/330/0760-3.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[148](https://dblp.org/pid/117/6314.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Martin Hahner](https://dblp.org/pid/207/7633.html)

[\[c50\]](https://dblp.org/pid/117/6314.html#c50) [\[i53\]](https://dblp.org/pid/117/6314.html#i53)

[149](https://dblp.org/pid/117/6314.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiajie Han](https://dblp.org/pid/169/7261.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[150](https://dblp.org/pid/117/6314.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Rui-Ze Han](https://dblp.org/pid/205/4022.html)

aka: Ruize Han

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[151](https://dblp.org/pid/117/6314.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Pat Hanrahan](https://dblp.org/pid/h/PatHanrahan.html)

[\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[152](https://dblp.org/pid/117/6314.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zeqi Hao](https://dblp.org/pid/348/8961.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[153](https://dblp.org/pid/117/6314.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jeremiah J. Harmsen](https://dblp.org/pid/47/6650.html)

aka: Jeremiah Harmsen

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[154](https://dblp.org/pid/117/6314.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[James Hays](https://dblp.org/pid/57/5958.html)

[\[c17\]](https://dblp.org/pid/117/6314.html#c17) [\[c6\]](https://dblp.org/pid/117/6314.html#c6) [\[i10\]](https://dblp.org/pid/117/6314.html#i10) [\[i5\]](https://dblp.org/pid/117/6314.html#i5)

[155](https://dblp.org/pid/117/6314.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chunming He](https://dblp.org/pid/251/5104.html)

[\[c91\]](https://dblp.org/pid/117/6314.html#c91) [\[i70\]](https://dblp.org/pid/117/6314.html#i70)

[156](https://dblp.org/pid/117/6314.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jianfeng He](https://dblp.org/pid/93/8352.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[157](https://dblp.org/pid/117/6314.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jun-Yan He](https://dblp.org/pid/173/3747.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[158](https://dblp.org/pid/117/6314.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Keji He](https://dblp.org/pid/319/4518.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[159](https://dblp.org/pid/117/6314.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhenyu He 0001](https://dblp.org/pid/57/6240-1.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[160](https://dblp.org/pid/117/6314.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jonathan Heek](https://dblp.org/pid/247/1004.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[161](https://dblp.org/pid/117/6314.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Felix Heide](https://dblp.org/pid/01/9396.html)

[\[c50\]](https://dblp.org/pid/117/6314.html#c50) [\[i53\]](https://dblp.org/pid/117/6314.html#i53)

[162](https://dblp.org/pid/117/6314.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Georg Heigold](https://dblp.org/pid/46/2236.html)

[\[c73\]](https://dblp.org/pid/117/6314.html#c73) [\[i68\]](https://dblp.org/pid/117/6314.html#i68)

[163](https://dblp.org/pid/117/6314.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Markus Herb](https://dblp.org/pid/210/8215.html)

[\[c86\]](https://dblp.org/pid/117/6314.html#c86) [\[i86\]](https://dblp.org/pid/117/6314.html#i86)

[164](https://dblp.org/pid/117/6314.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Otmar Hilliges](https://dblp.org/pid/82/2289.html)

[\[c46\]](https://dblp.org/pid/117/6314.html#c46) [\[i25\]](https://dblp.org/pid/117/6314.html#i25)

[165](https://dblp.org/pid/117/6314.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Judy Hoffman](https://dblp.org/pid/45/10336.html)

[\[i3\]](https://dblp.org/pid/117/6314.html#i3)

[166](https://dblp.org/pid/117/6314.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Neil Houlsby](https://dblp.org/pid/91/10669.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[167](https://dblp.org/pid/117/6314.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hou-Ning Hu](https://dblp.org/pid/199/3014.html)

[\[j7\]](https://dblp.org/pid/117/6314.html#j7) [\[i36\]](https://dblp.org/pid/117/6314.html#i36) [\[c25\]](https://dblp.org/pid/117/6314.html#c25) [\[i15\]](https://dblp.org/pid/117/6314.html#i15)

[168](https://dblp.org/pid/117/6314.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiantao Hu](https://dblp.org/pid/160/8016.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[169](https://dblp.org/pid/117/6314.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yutong Hu 0001](https://dblp.org/pid/199/9967-1.html)

[\[c87\]](https://dblp.org/pid/117/6314.html#c87) [\[i91\]](https://dblp.org/pid/117/6314.html#i91)

[170](https://dblp.org/pid/117/6314.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Kaer Huang](https://dblp.org/pid/317/0780.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[171](https://dblp.org/pid/117/6314.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Qixing Huang](https://dblp.org/pid/82/241.html)

aka: Qi-Xing Huang

[\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[172](https://dblp.org/pid/117/6314.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Thomas E. Huang](https://dblp.org/pid/260/6642.html)

[\[j5\]](https://dblp.org/pid/117/6314.html#j5) [\[c76\]](https://dblp.org/pid/117/6314.html#c76) [\[c59\]](https://dblp.org/pid/117/6314.html#c59) [\[c58\]](https://dblp.org/pid/117/6314.html#c58) [\[i65\]](https://dblp.org/pid/117/6314.html#i65) [\[c44\]](https://dblp.org/pid/117/6314.html#c44) [\[i50\]](https://dblp.org/pid/117/6314.html#i50) [\[i45\]](https://dblp.org/pid/117/6314.html#i45) [\[i44\]](https://dblp.org/pid/117/6314.html#i44) [\[c36\]](https://dblp.org/pid/117/6314.html#c36) [\[i34\]](https://dblp.org/pid/117/6314.html#i34) [\[i28\]](https://dblp.org/pid/117/6314.html#i28) [\[c28\]](https://dblp.org/pid/117/6314.html#c28) [\[i24\]](https://dblp.org/pid/117/6314.html#i24)

[173](https://dblp.org/pid/117/6314.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yan Huang 0008](https://dblp.org/pid/75/6434-8.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[174](https://dblp.org/pid/117/6314.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yuqing Huang](https://dblp.org/pid/134/5853.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[175](https://dblp.org/pid/117/6314.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Fantine Huot](https://dblp.org/pid/216/4555.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[176](https://dblp.org/pid/117/6314.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Marco Hutter 0001](https://dblp.org/pid/04/2753.html)

[\[c88\]](https://dblp.org/pid/117/6314.html#c88) [\[i93\]](https://dblp.org/pid/117/6314.html#i93)

[177](https://dblp.org/pid/117/6314.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Deepak Jangid](https://dblp.org/pid/340/1460.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[178](https://dblp.org/pid/117/6314.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Rodolphe Jenatton](https://dblp.org/pid/68/8398.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[179](https://dblp.org/pid/117/6314.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[180](https://dblp.org/pid/117/6314.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[181](https://dblp.org/pid/117/6314.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Tao Jiang](https://dblp.org/pid/181/2813.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[182](https://dblp.org/pid/117/6314.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yi Jiang 0004](https://dblp.org/pid/66/3172-4.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[183](https://dblp.org/pid/117/6314.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[184](https://dblp.org/pid/117/6314.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jianbin Jiao](https://dblp.org/pid/02/6888.html)

[\[c29\]](https://dblp.org/pid/117/6314.html#c29)

[185](https://dblp.org/pid/117/6314.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Henry Johan](https://dblp.org/pid/56/5589.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[186](https://dblp.org/pid/117/6314.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Evangelos Kalogerakis](https://dblp.org/pid/36/3187.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[187](https://dblp.org/pid/117/6314.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[188](https://dblp.org/pid/117/6314.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Menelaos Kanakis](https://dblp.org/pid/208/1757.html)

[\[c58\]](https://dblp.org/pid/117/6314.html#c58) [\[i44\]](https://dblp.org/pid/117/6314.html#i44)

[189](https://dblp.org/pid/117/6314.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Asako Kanezaki](https://dblp.org/pid/37/7634.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[190](https://dblp.org/pid/117/6314.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ben Kang](https://dblp.org/pid/340/1671.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[191](https://dblp.org/pid/117/6314.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Bingyi Kang](https://dblp.org/pid/119/7958.html)

[\[c24\]](https://dblp.org/pid/117/6314.html#c24) [\[i13\]](https://dblp.org/pid/117/6314.html#i13)

[192](https://dblp.org/pid/117/6314.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ze Kang](https://dblp.org/pid/340/1063.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[193](https://dblp.org/pid/117/6314.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Lei Ke](https://dblp.org/pid/26/5225.html)

[\[c99\]](https://dblp.org/pid/117/6314.html#c99) [\[c96\]](https://dblp.org/pid/117/6314.html#c96) [\[c93\]](https://dblp.org/pid/117/6314.html#c93) [\[i89\]](https://dblp.org/pid/117/6314.html#i89) [\[c83\]](https://dblp.org/pid/117/6314.html#c83) [\[c81\]](https://dblp.org/pid/117/6314.html#c81) [\[c77\]](https://dblp.org/pid/117/6314.html#c77) [\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c64\]](https://dblp.org/pid/117/6314.html#c64) [\[c63\]](https://dblp.org/pid/117/6314.html#c63) [\[i80\]](https://dblp.org/pid/117/6314.html#i80) [\[i78\]](https://dblp.org/pid/117/6314.html#i78) [\[i74\]](https://dblp.org/pid/117/6314.html#i74) [\[i72\]](https://dblp.org/pid/117/6314.html#i72) [\[i71\]](https://dblp.org/pid/117/6314.html#i71) [\[i59\]](https://dblp.org/pid/117/6314.html#i59) [\[c55\]](https://dblp.org/pid/117/6314.html#c55) [\[c43\]](https://dblp.org/pid/117/6314.html#c43) [\[i49\]](https://dblp.org/pid/117/6314.html#i49) [\[c31\]](https://dblp.org/pid/117/6314.html#c31) [\[i33\]](https://dblp.org/pid/117/6314.html#i33) [\[i26\]](https://dblp.org/pid/117/6314.html#i26)

[194](https://dblp.org/pid/117/6314.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Daniel Keysers](https://dblp.org/pid/02/6955.html)

[\[c73\]](https://dblp.org/pid/117/6314.html#c73) [\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83) [\[i68\]](https://dblp.org/pid/117/6314.html#i68)

[195](https://dblp.org/pid/117/6314.html?view=joint&param=195 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Muhammad Haris Khan](https://dblp.org/pid/155/3076.html)

[\[c51\]](https://dblp.org/pid/117/6314.html#c51) [\[i56\]](https://dblp.org/pid/117/6314.html#i56)

[196](https://dblp.org/pid/117/6314.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Aditya Khosla](https://dblp.org/pid/01/8315.html)

[\[c2\]](https://dblp.org/pid/117/6314.html#c2)

[197](https://dblp.org/pid/117/6314.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Sanghwan Kim](https://dblp.org/pid/60/10274.html)

[\[c98\]](https://dblp.org/pid/117/6314.html#c98) [\[i63\]](https://dblp.org/pid/117/6314.html#i63)

[198](https://dblp.org/pid/117/6314.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Thomas Kipf](https://dblp.org/pid/186/8206.html)

[\[c73\]](https://dblp.org/pid/117/6314.html#c73) [\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83) [\[i68\]](https://dblp.org/pid/117/6314.html#i68)

[199](https://dblp.org/pid/117/6314.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Madhu Kiran](https://dblp.org/pid/39/10281.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[200](https://dblp.org/pid/117/6314.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[201](https://dblp.org/pid/117/6314.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Alexander Kolesnikov 0003](https://dblp.org/pid/137/6963-3.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[202](https://dblp.org/pid/117/6314.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Vladlen Koltun](https://dblp.org/pid/66/5458.html)

[\[c8\]](https://dblp.org/pid/117/6314.html#c8) [\[i11\]](https://dblp.org/pid/117/6314.html#i11) [\[c4\]](https://dblp.org/pid/117/6314.html#c4)

[203](https://dblp.org/pid/117/6314.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Linghe Kong](https://dblp.org/pid/23/7909.html)

[\[c74\]](https://dblp.org/pid/117/6314.html#c74) [\[i69\]](https://dblp.org/pid/117/6314.html#i69)

[204](https://dblp.org/pid/117/6314.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Peter Kontschieder](https://dblp.org/pid/93/8066.html)

[\[c59\]](https://dblp.org/pid/117/6314.html#c59) [\[i28\]](https://dblp.org/pid/117/6314.html#i28)

[205](https://dblp.org/pid/117/6314.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ender Konukoglu](https://dblp.org/pid/45/7041.html)

[\[c37\]](https://dblp.org/pid/117/6314.html#c37) [\[i37\]](https://dblp.org/pid/117/6314.html#i37)

[206](https://dblp.org/pid/117/6314.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Philipp Krähenbühl](https://dblp.org/pid/43/7592.html)

[\[c25\]](https://dblp.org/pid/117/6314.html#c25) [\[i15\]](https://dblp.org/pid/117/6314.html#i15)

[207](https://dblp.org/pid/117/6314.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[208](https://dblp.org/pid/117/6314.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Manoj Kumar](https://dblp.org/pid/58/1076.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[209](https://dblp.org/pid/117/6314.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Suryansh Kumar 0001](https://dblp.org/pid/124/2783.html)

[\[c88\]](https://dblp.org/pid/117/6314.html#c88) [\[i93\]](https://dblp.org/pid/117/6314.html#i93) [\[j4\]](https://dblp.org/pid/117/6314.html#j4) [\[c60\]](https://dblp.org/pid/117/6314.html#c60) [\[i84\]](https://dblp.org/pid/117/6314.html#i84) [\[i77\]](https://dblp.org/pid/117/6314.html#i77) [\[j3\]](https://dblp.org/pid/117/6314.html#j3) [\[c56\]](https://dblp.org/pid/117/6314.html#c56) [\[c47\]](https://dblp.org/pid/117/6314.html#c47) [\[i52\]](https://dblp.org/pid/117/6314.html#i52) [\[i47\]](https://dblp.org/pid/117/6314.html#i47) [\[i39\]](https://dblp.org/pid/117/6314.html#i39)

[210](https://dblp.org/pid/117/6314.html?view=joint&param=210 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Simiao Lai](https://dblp.org/pid/282/1954.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[211](https://dblp.org/pid/117/6314.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jin-Peng Lan](https://dblp.org/pid/332/1033.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[212](https://dblp.org/pid/117/6314.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[213](https://dblp.org/pid/117/6314.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[214](https://dblp.org/pid/117/6314.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Erik G. Learned-Miller](https://dblp.org/pid/l/ErikGLearnedMiller.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[215](https://dblp.org/pid/117/6314.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Dongwook Lee](https://dblp.org/pid/25/6543.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[216](https://dblp.org/pid/117/6314.html?view=joint&param=216 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hyungjun Lee](https://dblp.org/pid/324/8911.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[217](https://dblp.org/pid/117/6314.html?view=joint&param=217 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hyunjeong Lee](https://dblp.org/pid/00/3423.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[218](https://dblp.org/pid/117/6314.html?view=joint&param=218 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Seohyung Lee](https://dblp.org/pid/210/4662.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[219](https://dblp.org/pid/117/6314.html?view=joint&param=219 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Seung-Ik Lee](https://dblp.org/pid/30/1902.html)

[\[c51\]](https://dblp.org/pid/117/6314.html#c51) [\[i56\]](https://dblp.org/pid/117/6314.html#i56)

[220](https://dblp.org/pid/117/6314.html?view=joint&param=220 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Soomin Lee](https://dblp.org/pid/81/4155.html)

[\[j3\]](https://dblp.org/pid/117/6314.html#j3) [\[i47\]](https://dblp.org/pid/117/6314.html#i47)

[221](https://dblp.org/pid/117/6314.html?view=joint&param=221 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[222](https://dblp.org/pid/117/6314.html?view=joint&param=222 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Sergey Levine](https://dblp.org/pid/80/7594.html)

[\[c14\]](https://dblp.org/pid/117/6314.html#c14) [\[i20\]](https://dblp.org/pid/117/6314.html#i20)

[223](https://dblp.org/pid/117/6314.html?view=joint&param=223 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Aoyu Li](https://dblp.org/pid/301/8358.html)

[\[c68\]](https://dblp.org/pid/117/6314.html#c68) [\[i85\]](https://dblp.org/pid/117/6314.html#i85)

[224](https://dblp.org/pid/117/6314.html?view=joint&param=224 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Bo Li 0013](https://dblp.org/pid/50/3402-13.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[225](https://dblp.org/pid/117/6314.html?view=joint&param=225 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Bo Li 0026](https://dblp.org/pid/50/3402-26.html)

[\[c16\]](https://dblp.org/pid/117/6314.html#c16) [\[i17\]](https://dblp.org/pid/117/6314.html#i17)

[226](https://dblp.org/pid/117/6314.html?view=joint&param=226 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chenyang Li 0007](https://dblp.org/pid/15/1523-7.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[227](https://dblp.org/pid/117/6314.html?view=joint&param=227 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Guohao Li 0001](https://dblp.org/pid/211/7175-1.html)

[\[c60\]](https://dblp.org/pid/117/6314.html#c60) [\[i77\]](https://dblp.org/pid/117/6314.html#i77)

[228](https://dblp.org/pid/117/6314.html?view=joint&param=228 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[229](https://dblp.org/pid/117/6314.html?view=joint&param=229 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiahao Li 0005](https://dblp.org/pid/150/5524-5.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[230](https://dblp.org/pid/117/6314.html?view=joint&param=230 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Kai Li 0012](https://dblp.org/pid/l/KaiLi12.html)

[\[c91\]](https://dblp.org/pid/117/6314.html#c91) [\[i70\]](https://dblp.org/pid/117/6314.html#i70)

[231](https://dblp.org/pid/117/6314.html?view=joint&param=231 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Kenan Li](https://dblp.org/pid/193/9514.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[232](https://dblp.org/pid/117/6314.html?view=joint&param=232 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ming Li 0010](https://dblp.org/pid/l/MingLi10.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[233](https://dblp.org/pid/117/6314.html?view=joint&param=233 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ning Li 0044](https://dblp.org/pid/14/5410-44.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[234](https://dblp.org/pid/117/6314.html?view=joint&param=234 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Qi Li](https://dblp.org/pid/181/2688.html)

[\[c39\]](https://dblp.org/pid/117/6314.html#c39) [\[i23\]](https://dblp.org/pid/117/6314.html#i23)

[235](https://dblp.org/pid/117/6314.html?view=joint&param=235 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Sihang Li 0001](https://dblp.org/pid/137/6318-1.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[236](https://dblp.org/pid/117/6314.html?view=joint&param=236 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Siyuan Li 0008](https://dblp.org/pid/63/9705-8.html)

[\[c97\]](https://dblp.org/pid/117/6314.html#c97) [\[c96\]](https://dblp.org/pid/117/6314.html#c96) [\[c94\]](https://dblp.org/pid/117/6314.html#c94) [\[i90\]](https://dblp.org/pid/117/6314.html#i90) [\[i89\]](https://dblp.org/pid/117/6314.html#i89) [\[i87\]](https://dblp.org/pid/117/6314.html#i87) [\[c83\]](https://dblp.org/pid/117/6314.html#c83) [\[c77\]](https://dblp.org/pid/117/6314.html#c77) [\[i78\]](https://dblp.org/pid/117/6314.html#i78) [\[i71\]](https://dblp.org/pid/117/6314.html#i71) [\[c44\]](https://dblp.org/pid/117/6314.html#c44) [\[i50\]](https://dblp.org/pid/117/6314.html#i50)

[237](https://dblp.org/pid/117/6314.html?view=joint&param=237 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Wangkai Li](https://dblp.org/pid/340/1456.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[238](https://dblp.org/pid/117/6314.html?view=joint&param=238 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xi Li 0001](https://dblp.org/pid/46/2311-1.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[239](https://dblp.org/pid/117/6314.html?view=joint&param=239 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xia Li 0005](https://dblp.org/pid/97/30-5.html)

[\[c55\]](https://dblp.org/pid/117/6314.html#c55) [\[c39\]](https://dblp.org/pid/117/6314.html#c39) [\[c31\]](https://dblp.org/pid/117/6314.html#c31) [\[i33\]](https://dblp.org/pid/117/6314.html#i33) [\[i26\]](https://dblp.org/pid/117/6314.html#i26)

[240](https://dblp.org/pid/117/6314.html?view=joint&param=240 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[241](https://dblp.org/pid/117/6314.html?view=joint&param=241 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiao Li](https://dblp.org/pid/66/2069.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[242](https://dblp.org/pid/117/6314.html?view=joint&param=242 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiaodi Li](https://dblp.org/pid/63/7279.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[243](https://dblp.org/pid/117/6314.html?view=joint&param=243 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xin Li 0034](https://dblp.org/pid/09/1365-34.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[244](https://dblp.org/pid/117/6314.html?view=joint&param=244 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiu Li 0001](https://dblp.org/pid/13/1206-1.html)

[\[c91\]](https://dblp.org/pid/117/6314.html#c91) [\[i70\]](https://dblp.org/pid/117/6314.html#i70)

[245](https://dblp.org/pid/117/6314.html?view=joint&param=245 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yangyan Li](https://dblp.org/pid/50/8293.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[246](https://dblp.org/pid/117/6314.html?view=joint&param=246 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yiming Li 0003](https://dblp.org/pid/l/YimingLi-3.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[247](https://dblp.org/pid/117/6314.html?view=joint&param=247 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhe Li 0008](https://dblp.org/pid/11/751-8.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[248](https://dblp.org/pid/117/6314.html?view=joint&param=248 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhiheng Li](https://dblp.org/pid/89/6935.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[249](https://dblp.org/pid/117/6314.html?view=joint&param=249 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zimo Li](https://dblp.org/pid/150/6829.html)

[\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[250](https://dblp.org/pid/117/6314.html?view=joint&param=250 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhouhui Lian](https://dblp.org/pid/20/1780.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[251](https://dblp.org/pid/117/6314.html?view=joint&param=251 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Mike Liao](https://dblp.org/pid/220/3349.html)

[\[i19\]](https://dblp.org/pid/117/6314.html#i19)

[252](https://dblp.org/pid/117/6314.html?view=joint&param=252 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Minghui Liao](https://dblp.org/pid/190/7335.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[253](https://dblp.org/pid/117/6314.html?view=joint&param=253 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ji Lin 0002](https://dblp.org/pid/02/8200-2.html)

[\[c25\]](https://dblp.org/pid/117/6314.html#c25) [\[c14\]](https://dblp.org/pid/117/6314.html#c14) [\[i20\]](https://dblp.org/pid/117/6314.html#i20) [\[i15\]](https://dblp.org/pid/117/6314.html#i15)

[254](https://dblp.org/pid/117/6314.html?view=joint&param=254 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Liting Lin](https://dblp.org/pid/227/2204.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[255](https://dblp.org/pid/117/6314.html?view=joint&param=255 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Haibin Ling](https://dblp.org/pid/93/3488.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[256](https://dblp.org/pid/117/6314.html?view=joint&param=256 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Alexander Liniger](https://dblp.org/pid/162/5560.html)

[\[c67\]](https://dblp.org/pid/117/6314.html#c67) [\[c65\]](https://dblp.org/pid/117/6314.html#c65) [\[c61\]](https://dblp.org/pid/117/6314.html#c61) [\[i82\]](https://dblp.org/pid/117/6314.html#i82) [\[i81\]](https://dblp.org/pid/117/6314.html#i81) [\[i60\]](https://dblp.org/pid/117/6314.html#i60) [\[j3\]](https://dblp.org/pid/117/6314.html#j3) [\[i47\]](https://dblp.org/pid/117/6314.html#i47) [\[c34\]](https://dblp.org/pid/117/6314.html#c34) [\[i31\]](https://dblp.org/pid/117/6314.html#i31)

[257](https://dblp.org/pid/117/6314.html?view=joint&param=257 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Benlin Liu](https://dblp.org/pid/274/0684.html)

[\[c36\]](https://dblp.org/pid/117/6314.html#c36) [\[i34\]](https://dblp.org/pid/117/6314.html#i34)

[258](https://dblp.org/pid/117/6314.html?view=joint&param=258 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[259](https://dblp.org/pid/117/6314.html?view=joint&param=259 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[260](https://dblp.org/pid/117/6314.html?view=joint&param=260 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chuangwei Liu](https://dblp.org/pid/328/8854.html)

[\[j8\]](https://dblp.org/pid/117/6314.html#j8) [\[i92\]](https://dblp.org/pid/117/6314.html#i92)

[261](https://dblp.org/pid/117/6314.html?view=joint&param=261 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Fangchen Liu](https://dblp.org/pid/211/7883.html)

[\[c30\]](https://dblp.org/pid/117/6314.html#c30) [\[i19\]](https://dblp.org/pid/117/6314.html#i19)

[262](https://dblp.org/pid/117/6314.html?view=joint&param=262 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jerry Liu](https://dblp.org/pid/35/874.html)

[\[c11\]](https://dblp.org/pid/117/6314.html#c11) [\[i9\]](https://dblp.org/pid/117/6314.html#i9)

[263](https://dblp.org/pid/117/6314.html?view=joint&param=263 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Mingyan Liu](https://dblp.org/pid/97/5725.html)

[\[c16\]](https://dblp.org/pid/117/6314.html#c16) [\[i17\]](https://dblp.org/pid/117/6314.html#i17)

[264](https://dblp.org/pid/117/6314.html?view=joint&param=264 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Pengyu Liu 0005](https://dblp.org/pid/73/7783-5.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[265](https://dblp.org/pid/117/6314.html?view=joint&param=265 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Si Liu 0001](https://dblp.org/pid/60/7642.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[266](https://dblp.org/pid/117/6314.html?view=joint&param=266 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xianglong Liu 0001](https://dblp.org/pid/55/7901-1.html)

[\[c90\]](https://dblp.org/pid/117/6314.html#c90) [\[c68\]](https://dblp.org/pid/117/6314.html#c68) [\[c63\]](https://dblp.org/pid/117/6314.html#c63) [\[c62\]](https://dblp.org/pid/117/6314.html#c62) [\[i85\]](https://dblp.org/pid/117/6314.html#i85)

[267](https://dblp.org/pid/117/6314.html?view=joint&param=267 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xinhao Liu 0003](https://dblp.org/pid/126/4582-3.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[268](https://dblp.org/pid/117/6314.html?view=joint&param=268 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yifan Liu 0001](https://dblp.org/pid/23/4955-1.html)

[\[c88\]](https://dblp.org/pid/117/6314.html#c88) [\[i93\]](https://dblp.org/pid/117/6314.html#i93) [\[c78\]](https://dblp.org/pid/117/6314.html#c78) [\[c76\]](https://dblp.org/pid/117/6314.html#c76) [\[c64\]](https://dblp.org/pid/117/6314.html#c64) [\[c62\]](https://dblp.org/pid/117/6314.html#c62) [\[i74\]](https://dblp.org/pid/117/6314.html#i74) [\[i65\]](https://dblp.org/pid/117/6314.html#i65) [\[i40\]](https://dblp.org/pid/117/6314.html#i40)

[269](https://dblp.org/pid/117/6314.html?view=joint&param=269 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yue Liu](https://dblp.org/pid/74/1932.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[270](https://dblp.org/pid/117/6314.html?view=joint&param=270 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhizheng Liu](https://dblp.org/pid/287/4356.html)

[\[c80\]](https://dblp.org/pid/117/6314.html#c80) [\[i61\]](https://dblp.org/pid/117/6314.html#i61)

[271](https://dblp.org/pid/117/6314.html?view=joint&param=271 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhuang Liu 0003](https://dblp.org/pid/56/11346-3.html)

[\[c24\]](https://dblp.org/pid/117/6314.html#c24) [\[i13\]](https://dblp.org/pid/117/6314.html#i13)

[272](https://dblp.org/pid/117/6314.html?view=joint&param=272 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ziwei Liu 0002](https://dblp.org/pid/05/6300-2.html)

[\[c68\]](https://dblp.org/pid/117/6314.html#c68) [\[i85\]](https://dblp.org/pid/117/6314.html#i85)

[273](https://dblp.org/pid/117/6314.html?view=joint&param=273 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[274](https://dblp.org/pid/117/6314.html?view=joint&param=274 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jingwan Lu](https://dblp.org/pid/08/7867.html)

[\[c19\]](https://dblp.org/pid/117/6314.html#c19) [\[c17\]](https://dblp.org/pid/117/6314.html#c17) [\[c6\]](https://dblp.org/pid/117/6314.html#c6) [\[i10\]](https://dblp.org/pid/117/6314.html#i10) [\[i5\]](https://dblp.org/pid/117/6314.html#i5) [\[j1\]](https://dblp.org/pid/117/6314.html#j1)

[275](https://dblp.org/pid/117/6314.html?view=joint&param=275 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yijuan Lu](https://dblp.org/pid/30/6535.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[276](https://dblp.org/pid/117/6314.html?view=joint&param=276 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Mario Lucic](https://dblp.org/pid/155/1945.html)

[\[c73\]](https://dblp.org/pid/117/6314.html#c73) [\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83) [\[i68\]](https://dblp.org/pid/117/6314.html#i68)

[277](https://dblp.org/pid/117/6314.html?view=joint&param=277 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Andreas Lugmayr](https://dblp.org/pid/249/2710.html)

[\[c52\]](https://dblp.org/pid/117/6314.html#c52) [\[c40\]](https://dblp.org/pid/117/6314.html#c40) [\[i57\]](https://dblp.org/pid/117/6314.html#i57) [\[i27\]](https://dblp.org/pid/117/6314.html#i27)

[278](https://dblp.org/pid/117/6314.html?view=joint&param=278 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[279](https://dblp.org/pid/117/6314.html?view=joint&param=279 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Bin Luo 0008](https://dblp.org/pid/36/4256-8.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[280](https://dblp.org/pid/117/6314.html?view=joint&param=280 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ping Luo 0002](https://dblp.org/pid/54/4989-2.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[281](https://dblp.org/pid/117/6314.html?view=joint&param=281 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yujia Luo](https://dblp.org/pid/202/2062.html)

[\[c12\]](https://dblp.org/pid/117/6314.html#c12)

[282](https://dblp.org/pid/117/6314.html?view=joint&param=282 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Bingpeng Ma](https://dblp.org/pid/62/1822.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[283](https://dblp.org/pid/117/6314.html?view=joint&param=283 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chao Ma 0004](https://dblp.org/pid/79/1552-4.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[284](https://dblp.org/pid/117/6314.html?view=joint&param=284 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[285](https://dblp.org/pid/117/6314.html?view=joint&param=285 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xudong Ma](https://dblp.org/pid/19/2951.html)

[\[c63\]](https://dblp.org/pid/117/6314.html#c63)

[286](https://dblp.org/pid/117/6314.html?view=joint&param=286 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yi-An Ma](https://dblp.org/pid/178/3243.html)

[\[c20\]](https://dblp.org/pid/117/6314.html#c20) [\[i18\]](https://dblp.org/pid/117/6314.html#i18)

[287](https://dblp.org/pid/117/6314.html?view=joint&param=287 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yinchao Ma](https://dblp.org/pid/189/1326.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[288](https://dblp.org/pid/117/6314.html?view=joint&param=288 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Vashisht Madhavan](https://dblp.org/pid/190/2112.html)

[\[c30\]](https://dblp.org/pid/117/6314.html#c30) [\[i19\]](https://dblp.org/pid/117/6314.html#i19)

[289](https://dblp.org/pid/117/6314.html?view=joint&param=289 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Aravindh Mahendran](https://dblp.org/pid/131/5343.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[290](https://dblp.org/pid/117/6314.html?view=joint&param=290 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Arif Mahmood](https://dblp.org/pid/18/4138.html)

[\[c51\]](https://dblp.org/pid/117/6314.html#c51) [\[i56\]](https://dblp.org/pid/117/6314.html#i56)

[291](https://dblp.org/pid/117/6314.html?view=joint&param=291 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Subhransu Maji](https://dblp.org/pid/92/6598.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[292](https://dblp.org/pid/117/6314.html?view=joint&param=292 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[293](https://dblp.org/pid/117/6314.html?view=joint&param=293 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[294](https://dblp.org/pid/117/6314.html?view=joint&param=294 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c53\]](https://dblp.org/pid/117/6314.html#c53) [\[c45\]](https://dblp.org/pid/117/6314.html#c45) [\[i54\]](https://dblp.org/pid/117/6314.html#i54)

[295](https://dblp.org/pid/117/6314.html?view=joint&param=295 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Rowan McAllister](https://dblp.org/pid/123/6416.html)

[\[c33\]](https://dblp.org/pid/117/6314.html#c33)

[296](https://dblp.org/pid/117/6314.html?view=joint&param=296 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Gerhard Ingmar Meijer](https://dblp.org/pid/46/5951.html)

aka: Ingmar Meijer

[\[c72\]](https://dblp.org/pid/117/6314.html#c72) [\[i67\]](https://dblp.org/pid/117/6314.html#i67)

[297](https://dblp.org/pid/117/6314.html?view=joint&param=297 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[298](https://dblp.org/pid/117/6314.html?view=joint&param=298 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Thomas Mensink](https://dblp.org/pid/95/2677.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[299](https://dblp.org/pid/117/6314.html?view=joint&param=299 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Deshui Miao](https://dblp.org/pid/307/5501.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[300](https://dblp.org/pid/117/6314.html?view=joint&param=300 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[301](https://dblp.org/pid/117/6314.html?view=joint&param=301 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Matthias Minderer](https://dblp.org/pid/243/3155.html)

[\[c73\]](https://dblp.org/pid/117/6314.html#c73) [\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83) [\[i68\]](https://dblp.org/pid/117/6314.html#i68)

[302](https://dblp.org/pid/117/6314.html?view=joint&param=302 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Azalia Mirhoseini](https://dblp.org/pid/18/8314.html)

[\[c20\]](https://dblp.org/pid/117/6314.html#c20) [\[i18\]](https://dblp.org/pid/117/6314.html#i18)

[303](https://dblp.org/pid/117/6314.html?view=joint&param=303 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Sanjeev Mk](https://dblp.org/pid/209/4207.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[304](https://dblp.org/pid/117/6314.html?view=joint&param=304 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Payman Moallem](https://dblp.org/pid/63/5378.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[305](https://dblp.org/pid/117/6314.html?view=joint&param=305 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Lucas Morin](https://dblp.org/pid/309/7785.html)

[\[c72\]](https://dblp.org/pid/117/6314.html#c72) [\[i67\]](https://dblp.org/pid/117/6314.html#i67)

[306](https://dblp.org/pid/117/6314.html?view=joint&param=306 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Basil Mustafa](https://dblp.org/pid/223/4558.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[307](https://dblp.org/pid/117/6314.html?view=joint&param=307 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[308](https://dblp.org/pid/117/6314.html?view=joint&param=308 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ahmed S. Nassar](https://dblp.org/pid/321/9993.html)

[\[c72\]](https://dblp.org/pid/117/6314.html#c72) [\[i67\]](https://dblp.org/pid/117/6314.html#i67)

[309](https://dblp.org/pid/117/6314.html?view=joint&param=309 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[310](https://dblp.org/pid/117/6314.html?view=joint&param=310 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ryutarou Ohbuchi](https://dblp.org/pid/57/3819.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[311](https://dblp.org/pid/117/6314.html?view=joint&param=311 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Avital Oliver](https://dblp.org/pid/203/8700.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[312](https://dblp.org/pid/117/6314.html?view=joint&param=312 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Martin R. Oswald](https://dblp.org/pid/37/7272.html)

[\[c47\]](https://dblp.org/pid/117/6314.html#c47) [\[i52\]](https://dblp.org/pid/117/6314.html#i52)

[313](https://dblp.org/pid/117/6314.html?view=joint&param=313 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Piotr Padlewski](https://dblp.org/pid/210/6394.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[314](https://dblp.org/pid/117/6314.html?view=joint&param=314 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Kannappan Palaniappan](https://dblp.org/pid/21/700.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[315](https://dblp.org/pid/117/6314.html?view=joint&param=315 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Siyang Pan](https://dblp.org/pid/250/5753.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[316](https://dblp.org/pid/117/6314.html?view=joint&param=316 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xinlei Pan](https://dblp.org/pid/188/6125.html)

[\[c22\]](https://dblp.org/pid/117/6314.html#c22)

[317](https://dblp.org/pid/117/6314.html?view=joint&param=317 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiangmiao Pang](https://dblp.org/pid/231/7630.html)

[\[j5\]](https://dblp.org/pid/117/6314.html#j5) [\[i45\]](https://dblp.org/pid/117/6314.html#i45) [\[c39\]](https://dblp.org/pid/117/6314.html#c39) [\[i23\]](https://dblp.org/pid/117/6314.html#i23)

[318](https://dblp.org/pid/117/6314.html?view=joint&param=318 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Georgios Th. Papadopoulos](https://dblp.org/pid/p/GeorgiosThPapadopoulos.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[319](https://dblp.org/pid/117/6314.html?view=joint&param=319 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[ChangBeom Park](https://dblp.org/pid/340/0926.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[320](https://dblp.org/pid/117/6314.html?view=joint&param=320 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hancheol Park](https://dblp.org/pid/161/3495.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[321](https://dblp.org/pid/117/6314.html?view=joint&param=321 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Vaishakh Patil](https://dblp.org/pid/255/5070.html)

[\[c88\]](https://dblp.org/pid/117/6314.html#c88) [\[i93\]](https://dblp.org/pid/117/6314.html#i93)

[322](https://dblp.org/pid/117/6314.html?view=joint&param=322 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c53\]](https://dblp.org/pid/117/6314.html#c53) [\[c48\]](https://dblp.org/pid/117/6314.html#c48) [\[c45\]](https://dblp.org/pid/117/6314.html#c45) [\[i54\]](https://dblp.org/pid/117/6314.html#i54) [\[i29\]](https://dblp.org/pid/117/6314.html#i29)

[323](https://dblp.org/pid/117/6314.html?view=joint&param=323 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Matthieu Paul](https://dblp.org/pid/255/6113.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c53\]](https://dblp.org/pid/117/6314.html#c53) [\[c45\]](https://dblp.org/pid/117/6314.html#c45) [\[i54\]](https://dblp.org/pid/117/6314.html#i54)

[324](https://dblp.org/pid/117/6314.html?view=joint&param=324 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Filip Pavetic](https://dblp.org/pid/149/2329.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[325](https://dblp.org/pid/117/6314.html?view=joint&param=325 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[326](https://dblp.org/pid/117/6314.html?view=joint&param=326 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[327](https://dblp.org/pid/117/6314.html?view=joint&param=327 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Luigi Piccinelli](https://dblp.org/pid/328/8549.html)

[\[c97\]](https://dblp.org/pid/117/6314.html#c97) [\[c96\]](https://dblp.org/pid/117/6314.html#c96) [\[c94\]](https://dblp.org/pid/117/6314.html#c94) [\[i90\]](https://dblp.org/pid/117/6314.html#i90) [\[i89\]](https://dblp.org/pid/117/6314.html#i89) [\[i87\]](https://dblp.org/pid/117/6314.html#i87) [\[c82\]](https://dblp.org/pid/117/6314.html#c82) [\[i79\]](https://dblp.org/pid/117/6314.html#i79)

[328](https://dblp.org/pid/117/6314.html?view=joint&param=328 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ioannis Pitas](https://dblp.org/pid/p/IPitas.html)

[\[c33\]](https://dblp.org/pid/117/6314.html#c33)

[329](https://dblp.org/pid/117/6314.html?view=joint&param=329 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Marc Pollefeys](https://dblp.org/pid/p/MarcPollefeys.html)

[\[c95\]](https://dblp.org/pid/117/6314.html#c95) [\[c79\]](https://dblp.org/pid/117/6314.html#c79) [\[i66\]](https://dblp.org/pid/117/6314.html#i66) [\[i58\]](https://dblp.org/pid/117/6314.html#i58)

[330](https://dblp.org/pid/117/6314.html?view=joint&param=330 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Janis Postels](https://dblp.org/pid/246/4950.html)

[\[c49\]](https://dblp.org/pid/117/6314.html#c49) [\[c42\]](https://dblp.org/pid/117/6314.html#c42) [\[i51\]](https://dblp.org/pid/117/6314.html#i51) [\[i32\]](https://dblp.org/pid/117/6314.html#i32)

[331](https://dblp.org/pid/117/6314.html?view=joint&param=331 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Joan Puigcerver](https://dblp.org/pid/155/3271.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[332](https://dblp.org/pid/117/6314.html?view=joint&param=332 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zekun Qian](https://dblp.org/pid/315/4066.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[333](https://dblp.org/pid/117/6314.html?view=joint&param=333 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Haotong Qin](https://dblp.org/pid/262/3626.html)

[\[c90\]](https://dblp.org/pid/117/6314.html#c90) [\[c68\]](https://dblp.org/pid/117/6314.html#c68) [\[c63\]](https://dblp.org/pid/117/6314.html#c63) [\[c62\]](https://dblp.org/pid/117/6314.html#c62) [\[i85\]](https://dblp.org/pid/117/6314.html#i85)

[334](https://dblp.org/pid/117/6314.html?view=joint&param=334 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Linlu Qiu](https://dblp.org/pid/267/2348.html)

[\[j5\]](https://dblp.org/pid/117/6314.html#j5) [\[i45\]](https://dblp.org/pid/117/6314.html#i45) [\[c39\]](https://dblp.org/pid/117/6314.html#c39) [\[i23\]](https://dblp.org/pid/117/6314.html#i23)

[335](https://dblp.org/pid/117/6314.html?view=joint&param=335 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Gani Rahmon](https://dblp.org/pid/291/7224.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[336](https://dblp.org/pid/117/6314.html?view=joint&param=336 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Amit Raj](https://dblp.org/pid/84/531.html)

[\[c17\]](https://dblp.org/pid/117/6314.html#c17)

[337](https://dblp.org/pid/117/6314.html?view=joint&param=337 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Frano Rajic](https://dblp.org/pid/331/2107.html)

[\[c99\]](https://dblp.org/pid/117/6314.html#c99) [\[i72\]](https://dblp.org/pid/117/6314.html#i72)

[338](https://dblp.org/pid/117/6314.html?view=joint&param=338 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Seyed Hamid Rezatofighi](https://dblp.org/pid/37/8192.html)

aka: Hamid Rezatofighi

[\[j6\]](https://dblp.org/pid/117/6314.html#j6) [\[i41\]](https://dblp.org/pid/117/6314.html#i41)

[339](https://dblp.org/pid/117/6314.html?view=joint&param=339 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Carlos Riquelme](https://dblp.org/pid/142/2592.html)

aka: Carlos Riquelme Ruiz

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[340](https://dblp.org/pid/117/6314.html?view=joint&param=340 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[341](https://dblp.org/pid/117/6314.html?view=joint&param=341 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Andrés Romero](https://dblp.org/pid/29/641.html)

[\[c52\]](https://dblp.org/pid/117/6314.html#c52) [\[i57\]](https://dblp.org/pid/117/6314.html#i57)

[342](https://dblp.org/pid/117/6314.html?view=joint&param=342 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Litu Rout](https://dblp.org/pid/206/6445.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[343](https://dblp.org/pid/117/6314.html?view=joint&param=343 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Suman Saha 0001](https://dblp.org/pid/96/893-1.html)

[\[c57\]](https://dblp.org/pid/117/6314.html#c57) [\[i64\]](https://dblp.org/pid/117/6314.html#i64) [\[i48\]](https://dblp.org/pid/117/6314.html#i48)

[344](https://dblp.org/pid/117/6314.html?view=joint&param=344 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Christos Sakaridis](https://dblp.org/pid/188/5858.html)

[\[j10\]](https://dblp.org/pid/117/6314.html#j10) [\[c97\]](https://dblp.org/pid/117/6314.html#c97) [\[c95\]](https://dblp.org/pid/117/6314.html#c95) [\[i90\]](https://dblp.org/pid/117/6314.html#i90) [\[c84\]](https://dblp.org/pid/117/6314.html#c84) [\[c82\]](https://dblp.org/pid/117/6314.html#c82) [\[c61\]](https://dblp.org/pid/117/6314.html#c61) [\[i79\]](https://dblp.org/pid/117/6314.html#i79) [\[i76\]](https://dblp.org/pid/117/6314.html#i76) [\[i75\]](https://dblp.org/pid/117/6314.html#i75) [\[i64\]](https://dblp.org/pid/117/6314.html#i64) [\[i60\]](https://dblp.org/pid/117/6314.html#i60) [\[i58\]](https://dblp.org/pid/117/6314.html#i58) [\[c50\]](https://dblp.org/pid/117/6314.html#c50) [\[i53\]](https://dblp.org/pid/117/6314.html#i53)

[345](https://dblp.org/pid/117/6314.html?view=joint&param=345 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Erik Sandström](https://dblp.org/pid/192/9251.html)

[\[c47\]](https://dblp.org/pid/117/6314.html#c47) [\[i52\]](https://dblp.org/pid/117/6314.html#i52)

[346](https://dblp.org/pid/117/6314.html?view=joint&param=346 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Patsorn Sangkloy](https://dblp.org/pid/182/9370.html)

[\[c17\]](https://dblp.org/pid/117/6314.html#c17) [\[c6\]](https://dblp.org/pid/117/6314.html#c6) [\[i10\]](https://dblp.org/pid/117/6314.html#i10) [\[i5\]](https://dblp.org/pid/117/6314.html#i5)

[347](https://dblp.org/pid/117/6314.html?view=joint&param=347 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Silvio Savarese](https://dblp.org/pid/50/3578.html)

[\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[348](https://dblp.org/pid/117/6314.html?view=joint&param=348 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Manolis Savva](https://dblp.org/pid/21/9924.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10) [\[c9\]](https://dblp.org/pid/117/6314.html#c9) [\[c5\]](https://dblp.org/pid/117/6314.html#c5) [\[i6\]](https://dblp.org/pid/117/6314.html#i6) [\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[349](https://dblp.org/pid/117/6314.html?view=joint&param=349 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Davide Scaramuzza 0001](https://dblp.org/pid/62/3318.html)

[\[c66\]](https://dblp.org/pid/117/6314.html#c66) [\[i43\]](https://dblp.org/pid/117/6314.html#i43)

[350](https://dblp.org/pid/117/6314.html?view=joint&param=350 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Norbert Scherer-Negenborn](https://dblp.org/pid/45/8662.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[351](https://dblp.org/pid/117/6314.html?view=joint&param=351 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Bernt Schiele](https://dblp.org/pid/s/BerntSchiele.html)

[\[c94\]](https://dblp.org/pid/117/6314.html#c94) [\[i87\]](https://dblp.org/pid/117/6314.html#i87) [\[c75\]](https://dblp.org/pid/117/6314.html#c75) [\[c70\]](https://dblp.org/pid/117/6314.html#c70) [\[i62\]](https://dblp.org/pid/117/6314.html#i62) [\[c49\]](https://dblp.org/pid/117/6314.html#c49) [\[i51\]](https://dblp.org/pid/117/6314.html#i51) [\[i42\]](https://dblp.org/pid/117/6314.html#i42)

[352](https://dblp.org/pid/117/6314.html?view=joint&param=352 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Aron Schmied](https://dblp.org/pid/355/5910.html)

[\[c79\]](https://dblp.org/pid/117/6314.html#c79) [\[i66\]](https://dblp.org/pid/117/6314.html#i66)

[353](https://dblp.org/pid/117/6314.html?view=joint&param=353 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ari Seff](https://dblp.org/pid/147/5247.html)

[\[i2\]](https://dblp.org/pid/117/6314.html#i2)

[354](https://dblp.org/pid/117/6314.html?view=joint&param=354 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Mattia Segù](https://dblp.org/pid/245/2565.html)

[\[c97\]](https://dblp.org/pid/117/6314.html#c97) [\[c96\]](https://dblp.org/pid/117/6314.html#c96) [\[c94\]](https://dblp.org/pid/117/6314.html#c94) [\[i90\]](https://dblp.org/pid/117/6314.html#i90) [\[i89\]](https://dblp.org/pid/117/6314.html#i89) [\[i87\]](https://dblp.org/pid/117/6314.html#i87) [\[c80\]](https://dblp.org/pid/117/6314.html#c80) [\[c75\]](https://dblp.org/pid/117/6314.html#c75) [\[c70\]](https://dblp.org/pid/117/6314.html#c70) [\[i62\]](https://dblp.org/pid/117/6314.html#i62) [\[i61\]](https://dblp.org/pid/117/6314.html#i61) [\[c51\]](https://dblp.org/pid/117/6314.html#c51) [\[c49\]](https://dblp.org/pid/117/6314.html#c49) [\[c42\]](https://dblp.org/pid/117/6314.html#c42) [\[i56\]](https://dblp.org/pid/117/6314.html#i56) [\[i51\]](https://dblp.org/pid/117/6314.html#i51) [\[i42\]](https://dblp.org/pid/117/6314.html#i42) [\[i32\]](https://dblp.org/pid/117/6314.html#i32)

[355](https://dblp.org/pid/117/6314.html?view=joint&param=355 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[356](https://dblp.org/pid/117/6314.html?view=joint&param=356 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Pengcheng Shao](https://dblp.org/pid/364/8295.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[357](https://dblp.org/pid/117/6314.html?view=joint&param=357 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yihang She](https://dblp.org/pid/294/4508.html)

[\[c41\]](https://dblp.org/pid/117/6314.html#c41) [\[i46\]](https://dblp.org/pid/117/6314.html#i46)

[358](https://dblp.org/pid/117/6314.html?view=joint&param=358 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Evan Shelhamer](https://dblp.org/pid/150/6541.html)

[\[c18\]](https://dblp.org/pid/117/6314.html#c18) [\[c13\]](https://dblp.org/pid/117/6314.html#c13)

[359](https://dblp.org/pid/117/6314.html?view=joint&param=359 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Wooksu Shin](https://dblp.org/pid/327/3602.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[360](https://dblp.org/pid/117/6314.html?view=joint&param=360 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Changyong Shu](https://dblp.org/pid/239/5094.html)

[\[c78\]](https://dblp.org/pid/117/6314.html#c78) [\[i40\]](https://dblp.org/pid/117/6314.html#i40)

[361](https://dblp.org/pid/117/6314.html?view=joint&param=361 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Luca Daniel Sieber](https://dblp.org/pid/323/8890.html)

[\[c42\]](https://dblp.org/pid/117/6314.html#c42)

[362](https://dblp.org/pid/117/6314.html?view=joint&param=362 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[363](https://dblp.org/pid/117/6314.html?view=joint&param=363 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Gurkirt Singh](https://dblp.org/pid/155/3301.html)

[\[c57\]](https://dblp.org/pid/117/6314.html#c57) [\[i48\]](https://dblp.org/pid/117/6314.html#i48)

[364](https://dblp.org/pid/117/6314.html?view=joint&param=364 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Cristian Sminchisescu](https://dblp.org/pid/96/3826.html)

[\[c47\]](https://dblp.org/pid/117/6314.html#c47) [\[i52\]](https://dblp.org/pid/117/6314.html#i52)

[365](https://dblp.org/pid/117/6314.html?view=joint&param=365 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Elham Soltanikazemi](https://dblp.org/pid/318/1851.html)

aka: Elham Soltani Kazemi

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[366](https://dblp.org/pid/117/6314.html?view=joint&param=366 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Dawn Song](https://dblp.org/pid/s/DXSong.html)

[\[c16\]](https://dblp.org/pid/117/6314.html#c16) [\[i17\]](https://dblp.org/pid/117/6314.html#i17)

[367](https://dblp.org/pid/117/6314.html?view=joint&param=367 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Shuran Song](https://dblp.org/pid/123/4433.html)

[\[c9\]](https://dblp.org/pid/117/6314.html#c9) [\[i6\]](https://dblp.org/pid/117/6314.html#i6) [\[c2\]](https://dblp.org/pid/117/6314.html#c2) [\[i2\]](https://dblp.org/pid/117/6314.html#i2) [\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[368](https://dblp.org/pid/117/6314.html?view=joint&param=368 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Tianhui Song](https://dblp.org/pid/181/8738.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[369](https://dblp.org/pid/117/6314.html?view=joint&param=369 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[370](https://dblp.org/pid/117/6314.html?view=joint&param=370 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yunlong Song](https://dblp.org/pid/83/10696.html)

[\[c66\]](https://dblp.org/pid/117/6314.html#c66) [\[i43\]](https://dblp.org/pid/117/6314.html#i43)

[371](https://dblp.org/pid/117/6314.html?view=joint&param=371 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Peter W. J. Staar](https://dblp.org/pid/136/7966.html)

[\[c72\]](https://dblp.org/pid/117/6314.html#c72) [\[i67\]](https://dblp.org/pid/117/6314.html#i67)

[372](https://dblp.org/pid/117/6314.html?view=joint&param=372 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Sjoerd van Steenkiste](https://dblp.org/pid/183/9326.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[373](https://dblp.org/pid/117/6314.html?view=joint&param=373 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Andreas Steiner 0001](https://dblp.org/pid/s/AndreasSteiner.html)

aka: Andreas Peter Steiner

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[374](https://dblp.org/pid/117/6314.html?view=joint&param=374 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Rainer Stiefelhagen](https://dblp.org/pid/31/4699.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[375](https://dblp.org/pid/117/6314.html?view=joint&param=375 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hang Su 0005](https://dblp.org/pid/26/5371-5.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[376](https://dblp.org/pid/117/6314.html?view=joint&param=376 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hao Su 0001](https://dblp.org/pid/09/4945-1.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10) [\[c5\]](https://dblp.org/pid/117/6314.html#c5) [\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[377](https://dblp.org/pid/117/6314.html?view=joint&param=377 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chao Sun](https://dblp.org/pid/54/3957.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[378](https://dblp.org/pid/117/6314.html?view=joint&param=378 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jingna Sun](https://dblp.org/pid/255/0702.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[379](https://dblp.org/pid/117/6314.html?view=joint&param=379 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Min Sun 0001](https://dblp.org/pid/62/2750-1.html)

[\[j7\]](https://dblp.org/pid/117/6314.html#j7) [\[c59\]](https://dblp.org/pid/117/6314.html#c59) [\[c56\]](https://dblp.org/pid/117/6314.html#c56) [\[i39\]](https://dblp.org/pid/117/6314.html#i39) [\[i36\]](https://dblp.org/pid/117/6314.html#i36) [\[c25\]](https://dblp.org/pid/117/6314.html#c25) [\[i15\]](https://dblp.org/pid/117/6314.html#i15)

[380](https://dblp.org/pid/117/6314.html?view=joint&param=380 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Rui Sun 0006](https://dblp.org/pid/01/3595-6.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[381](https://dblp.org/pid/117/6314.html?view=joint&param=381 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Tao Sun 0019](https://dblp.org/pid/74/3590-19.html)

[\[c49\]](https://dblp.org/pid/117/6314.html#c49) [\[c42\]](https://dblp.org/pid/117/6314.html#c42) [\[i51\]](https://dblp.org/pid/117/6314.html#i51) [\[i32\]](https://dblp.org/pid/117/6314.html#i32)

[382](https://dblp.org/pid/117/6314.html?view=joint&param=382 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yu-Wing Tai](https://dblp.org/pid/40/566.html)

[\[c99\]](https://dblp.org/pid/117/6314.html#c99) [\[c81\]](https://dblp.org/pid/117/6314.html#c81) [\[c77\]](https://dblp.org/pid/117/6314.html#c77) [\[c70\]](https://dblp.org/pid/117/6314.html#c70) [\[c64\]](https://dblp.org/pid/117/6314.html#c64) [\[c63\]](https://dblp.org/pid/117/6314.html#c63) [\[i80\]](https://dblp.org/pid/117/6314.html#i80) [\[i74\]](https://dblp.org/pid/117/6314.html#i74) [\[i72\]](https://dblp.org/pid/117/6314.html#i72) [\[i71\]](https://dblp.org/pid/117/6314.html#i71) [\[c55\]](https://dblp.org/pid/117/6314.html#c55) [\[c43\]](https://dblp.org/pid/117/6314.html#c43) [\[i49\]](https://dblp.org/pid/117/6314.html#i49) [\[i42\]](https://dblp.org/pid/117/6314.html#i42) [\[c31\]](https://dblp.org/pid/117/6314.html#c31) [\[i33\]](https://dblp.org/pid/117/6314.html#i33) [\[i26\]](https://dblp.org/pid/117/6314.html#i26)

[383](https://dblp.org/pid/117/6314.html?view=joint&param=383 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chi-Keung Tang](https://dblp.org/pid/34/4366.html)

[\[c99\]](https://dblp.org/pid/117/6314.html#c99) [\[c81\]](https://dblp.org/pid/117/6314.html#c81) [\[c77\]](https://dblp.org/pid/117/6314.html#c77) [\[c70\]](https://dblp.org/pid/117/6314.html#c70) [\[c64\]](https://dblp.org/pid/117/6314.html#c64) [\[c63\]](https://dblp.org/pid/117/6314.html#c63) [\[i80\]](https://dblp.org/pid/117/6314.html#i80) [\[i74\]](https://dblp.org/pid/117/6314.html#i74) [\[i72\]](https://dblp.org/pid/117/6314.html#i72) [\[i71\]](https://dblp.org/pid/117/6314.html#i71) [\[c55\]](https://dblp.org/pid/117/6314.html#c55) [\[c43\]](https://dblp.org/pid/117/6314.html#c43) [\[i49\]](https://dblp.org/pid/117/6314.html#i49) [\[i42\]](https://dblp.org/pid/117/6314.html#i42) [\[c31\]](https://dblp.org/pid/117/6314.html#c31) [\[i33\]](https://dblp.org/pid/117/6314.html#i33) [\[i26\]](https://dblp.org/pid/117/6314.html#i26)

[384](https://dblp.org/pid/117/6314.html?view=joint&param=384 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chuanming Tang](https://dblp.org/pid/237/6254.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[385](https://dblp.org/pid/117/6314.html?view=joint&param=385 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hao Tang 0005](https://dblp.org/pid/07/5751-5.html)

[\[c98\]](https://dblp.org/pid/117/6314.html#c98) [\[i63\]](https://dblp.org/pid/117/6314.html#i63)

[386](https://dblp.org/pid/117/6314.html?view=joint&param=386 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Siyu Tang 0001](https://dblp.org/pid/22/845-1.html)

[\[c46\]](https://dblp.org/pid/117/6314.html#c46) [\[i25\]](https://dblp.org/pid/117/6314.html#i25)

[387](https://dblp.org/pid/117/6314.html?view=joint&param=387 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiaoou Tang](https://dblp.org/pid/04/5226.html)

[\[c2\]](https://dblp.org/pid/117/6314.html#c2)

[388](https://dblp.org/pid/117/6314.html?view=joint&param=388 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[389](https://dblp.org/pid/117/6314.html?view=joint&param=389 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Dacheng Tao](https://dblp.org/pid/46/3391.html)

[\[j6\]](https://dblp.org/pid/117/6314.html#j6) [\[i41\]](https://dblp.org/pid/117/6314.html#i41)

[390](https://dblp.org/pid/117/6314.html?view=joint&param=390 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Atsushi Tatsuma](https://dblp.org/pid/65/7527.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10) [\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[391](https://dblp.org/pid/117/6314.html?view=joint&param=391 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yi Tay](https://dblp.org/pid/188/6350.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[392](https://dblp.org/pid/117/6314.html?view=joint&param=392 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Spyridon Thermos](https://dblp.org/pid/181/7680.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[393](https://dblp.org/pid/117/6314.html?view=joint&param=393 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c52\]](https://dblp.org/pid/117/6314.html#c52) [\[c45\]](https://dblp.org/pid/117/6314.html#c45) [\[c40\]](https://dblp.org/pid/117/6314.html#c40) [\[i57\]](https://dblp.org/pid/117/6314.html#i57) [\[c38\]](https://dblp.org/pid/117/6314.html#c38) [\[i30\]](https://dblp.org/pid/117/6314.html#i30) [\[i27\]](https://dblp.org/pid/117/6314.html#i27)

[394](https://dblp.org/pid/117/6314.html?view=joint&param=394 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xavier Timoneda](https://dblp.org/pid/224/0074.html)

[\[c86\]](https://dblp.org/pid/117/6314.html#c86) [\[i86\]](https://dblp.org/pid/117/6314.html#i86)

[395](https://dblp.org/pid/117/6314.html?view=joint&param=395 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Federico Tombari](https://dblp.org/pid/16/3539.html)

[\[c49\]](https://dblp.org/pid/117/6314.html#c49) [\[c42\]](https://dblp.org/pid/117/6314.html#c42) [\[i51\]](https://dblp.org/pid/117/6314.html#i51) [\[i32\]](https://dblp.org/pid/117/6314.html#i32)

[396](https://dblp.org/pid/117/6314.html?view=joint&param=396 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Imad Eddine Toubal](https://dblp.org/pid/292/6360.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[397](https://dblp.org/pid/117/6314.html?view=joint&param=397 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Dustin Tran](https://dblp.org/pid/163/2106.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[398](https://dblp.org/pid/117/6314.html?view=joint&param=398 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Khanh-Tung Tran](https://dblp.org/pid/359/3793.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[399](https://dblp.org/pid/117/6314.html?view=joint&param=399 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Prune Truong](https://dblp.org/pid/247/5738.html)

[\[c54\]](https://dblp.org/pid/117/6314.html#c54) [\[i55\]](https://dblp.org/pid/117/6314.html#i55) [\[c35\]](https://dblp.org/pid/117/6314.html#c35) [\[i35\]](https://dblp.org/pid/117/6314.html#i35)

[400](https://dblp.org/pid/117/6314.html?view=joint&param=400 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[401](https://dblp.org/pid/117/6314.html?view=joint&param=401 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Michael Tschannen](https://dblp.org/pid/134/9824.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[402](https://dblp.org/pid/117/6314.html?view=joint&param=402 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Alexey Tumanov](https://dblp.org/pid/41/6224.html)

[\[c12\]](https://dblp.org/pid/117/6314.html#c12)

[403](https://dblp.org/pid/117/6314.html?view=joint&param=403 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ozan Unal](https://dblp.org/pid/250/4116.html)

[\[i64\]](https://dblp.org/pid/117/6314.html#i64)

[404](https://dblp.org/pid/117/6314.html?view=joint&param=404 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jack Valmadre](https://dblp.org/pid/50/8535.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[405](https://dblp.org/pid/117/6314.html?view=joint&param=405 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Cristina Nader Vasconcelos](https://dblp.org/pid/37/135.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[406](https://dblp.org/pid/117/6314.html?view=joint&param=406 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Om Prakash Verma](https://dblp.org/pid/61/8145.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[407](https://dblp.org/pid/117/6314.html?view=joint&param=407 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jash Vira](https://dblp.org/pid/364/8266.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[408](https://dblp.org/pid/117/6314.html?view=joint&param=408 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xuan-Son Vu](https://dblp.org/pid/151/8673.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[409](https://dblp.org/pid/117/6314.html?view=joint&param=409 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Stéphane Vujasinovic](https://dblp.org/pid/237/5053.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[410](https://dblp.org/pid/117/6314.html?view=joint&param=410 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Cheng Wan 0006](https://dblp.org/pid/118/7267-6.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[411](https://dblp.org/pid/117/6314.html?view=joint&param=411 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jia Wan 0001](https://dblp.org/pid/13/6504-1.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[412](https://dblp.org/pid/117/6314.html?view=joint&param=412 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Dequan Wang](https://dblp.org/pid/168/4711.html)

[\[c25\]](https://dblp.org/pid/117/6314.html#c25) [\[c21\]](https://dblp.org/pid/117/6314.html#c21) [\[c18\]](https://dblp.org/pid/117/6314.html#c18) [\[c13\]](https://dblp.org/pid/117/6314.html#c13) [\[i16\]](https://dblp.org/pid/117/6314.html#i16) [\[i15\]](https://dblp.org/pid/117/6314.html#i15) [\[i8\]](https://dblp.org/pid/117/6314.html#i8) [\[i3\]](https://dblp.org/pid/117/6314.html#i3)

[413](https://dblp.org/pid/117/6314.html?view=joint&param=413 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[414](https://dblp.org/pid/117/6314.html?view=joint&param=414 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Fei Wang 0032](https://dblp.org/pid/52/3194-32.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[415](https://dblp.org/pid/117/6314.html?view=joint&param=415 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Feifan Wang](https://dblp.org/pid/213/0685.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[416](https://dblp.org/pid/117/6314.html?view=joint&param=416 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[He Wang 0028](https://dblp.org/pid/01/6368-28.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[417](https://dblp.org/pid/117/6314.html?view=joint&param=417 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiahao Wang 0001](https://dblp.org/pid/34/5354-1.html)

[\[j3\]](https://dblp.org/pid/117/6314.html#j3) [\[c46\]](https://dblp.org/pid/117/6314.html#c46) [\[i47\]](https://dblp.org/pid/117/6314.html#i47) [\[i25\]](https://dblp.org/pid/117/6314.html#i25)

[418](https://dblp.org/pid/117/6314.html?view=joint&param=418 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jue Wang 0001](https://dblp.org/pid/69/393-1.html)

[\[j2\]](https://dblp.org/pid/117/6314.html#j2)

[419](https://dblp.org/pid/117/6314.html?view=joint&param=419 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Liang Wang 0001](https://dblp.org/pid/56/4499-1.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[420](https://dblp.org/pid/117/6314.html?view=joint&param=420 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[421](https://dblp.org/pid/117/6314.html?view=joint&param=421 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[422](https://dblp.org/pid/117/6314.html?view=joint&param=422 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[423](https://dblp.org/pid/117/6314.html?view=joint&param=423 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Qiang Wang 0023](https://dblp.org/pid/64/5630-23.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[424](https://dblp.org/pid/117/6314.html?view=joint&param=424 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ruth Wang](https://dblp.org/pid/57/4644.html)

[\[c27\]](https://dblp.org/pid/117/6314.html#c27) [\[c23\]](https://dblp.org/pid/117/6314.html#c23) [\[c20\]](https://dblp.org/pid/117/6314.html#c20) [\[i22\]](https://dblp.org/pid/117/6314.html#i22) [\[i18\]](https://dblp.org/pid/117/6314.html#i18) [\[i14\]](https://dblp.org/pid/117/6314.html#i14)

[425](https://dblp.org/pid/117/6314.html?view=joint&param=425 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Song Wang 0002](https://dblp.org/pid/62/3151-2.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[426](https://dblp.org/pid/117/6314.html?view=joint&param=426 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Wenguan Wang](https://dblp.org/pid/145/1078.html)

[\[j9\]](https://dblp.org/pid/117/6314.html#j9) [\[c37\]](https://dblp.org/pid/117/6314.html#c37) [\[i37\]](https://dblp.org/pid/117/6314.html#i37) [\[i29\]](https://dblp.org/pid/117/6314.html#i29)

[427](https://dblp.org/pid/117/6314.html?view=joint&param=427 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiao Wang 0038](https://dblp.org/pid/49/67-38.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[428](https://dblp.org/pid/117/6314.html?view=joint&param=428 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiaolong Wang 0004](https://dblp.org/pid/91/952-4.html)

[\[c36\]](https://dblp.org/pid/117/6314.html#c36) [\[i34\]](https://dblp.org/pid/117/6314.html#i34)

[429](https://dblp.org/pid/117/6314.html?view=joint&param=429 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xin Wang 0066](https://dblp.org/pid/10/5630-66.html)

[\[c36\]](https://dblp.org/pid/117/6314.html#c36) [\[c32\]](https://dblp.org/pid/117/6314.html#c32) [\[i38\]](https://dblp.org/pid/117/6314.html#i38) [\[i34\]](https://dblp.org/pid/117/6314.html#i34) [\[c30\]](https://dblp.org/pid/117/6314.html#c30) [\[c29\]](https://dblp.org/pid/117/6314.html#c29) [\[c28\]](https://dblp.org/pid/117/6314.html#c28) [\[i24\]](https://dblp.org/pid/117/6314.html#i24) [\[c27\]](https://dblp.org/pid/117/6314.html#c27) [\[c24\]](https://dblp.org/pid/117/6314.html#c24) [\[c20\]](https://dblp.org/pid/117/6314.html#c20) [\[i22\]](https://dblp.org/pid/117/6314.html#i22) [\[i21\]](https://dblp.org/pid/117/6314.html#i21) [\[c15\]](https://dblp.org/pid/117/6314.html#c15) [\[c12\]](https://dblp.org/pid/117/6314.html#c12) [\[i18\]](https://dblp.org/pid/117/6314.html#i18) [\[i13\]](https://dblp.org/pid/117/6314.html#i13) [\[i7\]](https://dblp.org/pid/117/6314.html#i7)

[430](https://dblp.org/pid/117/6314.html?view=joint&param=430 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xinggang Wang](https://dblp.org/pid/95/3056.html)

[\[j9\]](https://dblp.org/pid/117/6314.html#j9)

[431](https://dblp.org/pid/117/6314.html?view=joint&param=431 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yaowei Wang 0001](https://dblp.org/pid/68/2992-1.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[432](https://dblp.org/pid/117/6314.html?view=joint&param=432 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yida Wang 0001](https://dblp.org/pid/17/1701-1.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[433](https://dblp.org/pid/117/6314.html?view=joint&param=433 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yue Wang 0036](https://dblp.org/pid/33/4822-36.html)

[\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[434](https://dblp.org/pid/117/6314.html?view=joint&param=434 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yue Wang 0041](https://dblp.org/pid/33/4822-41.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85)

[435](https://dblp.org/pid/117/6314.html?view=joint&param=435 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yuxuan Wang](https://dblp.org/pid/94/3940.html)

[\[c49\]](https://dblp.org/pid/117/6314.html#c49) [\[i51\]](https://dblp.org/pid/117/6314.html#i51)

[436](https://dblp.org/pid/117/6314.html?view=joint&param=436 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhepeng Wang 0002](https://dblp.org/pid/242/8456-2.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[437](https://dblp.org/pid/117/6314.html?view=joint&param=437 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zijun Wang](https://dblp.org/pid/93/1955.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[438](https://dblp.org/pid/117/6314.html?view=joint&param=438 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Valéry Weber](https://dblp.org/pid/86/5323.html)

[\[c72\]](https://dblp.org/pid/117/6314.html#c72) [\[i67\]](https://dblp.org/pid/117/6314.html#i67)

[439](https://dblp.org/pid/117/6314.html?view=joint&param=439 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Silvan Weder](https://dblp.org/pid/256/4902.html)

[\[c47\]](https://dblp.org/pid/117/6314.html#c47) [\[i52\]](https://dblp.org/pid/117/6314.html#i52)

[440](https://dblp.org/pid/117/6314.html?view=joint&param=440 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Joost van de Weijer 0001](https://dblp.org/pid/67/3379.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[441](https://dblp.org/pid/117/6314.html?view=joint&param=441 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Kehan Wen](https://dblp.org/pid/372/4822.html)

[\[c87\]](https://dblp.org/pid/117/6314.html#c87) [\[i91\]](https://dblp.org/pid/117/6314.html#i91)

[442](https://dblp.org/pid/117/6314.html?view=joint&param=442 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[443](https://dblp.org/pid/117/6314.html?view=joint&param=443 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiannan Wu](https://dblp.org/pid/277/0616.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[444](https://dblp.org/pid/117/6314.html?view=joint&param=444 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jinlin Wu](https://dblp.org/pid/123/7200.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[445](https://dblp.org/pid/117/6314.html?view=joint&param=445 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Qiangqiang Wu](https://dblp.org/pid/193/1415.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[446](https://dblp.org/pid/117/6314.html?view=joint&param=446 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[447](https://dblp.org/pid/117/6314.html?view=joint&param=447 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yan Wu](https://dblp.org/pid/04/3001.html)

[\[c66\]](https://dblp.org/pid/117/6314.html#c66) [\[c46\]](https://dblp.org/pid/117/6314.html#c46) [\[i43\]](https://dblp.org/pid/117/6314.html#i43) [\[i25\]](https://dblp.org/pid/117/6314.html#i25)

[448](https://dblp.org/pid/117/6314.html?view=joint&param=448 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhirong Wu](https://dblp.org/pid/147/5025.html)

[\[c2\]](https://dblp.org/pid/117/6314.html#c2)

[449](https://dblp.org/pid/117/6314.html?view=joint&param=449 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhiyuan Wu](https://dblp.org/pid/60/5001.html)

[\[j8\]](https://dblp.org/pid/117/6314.html#j8) [\[i92\]](https://dblp.org/pid/117/6314.html#i92)

[450](https://dblp.org/pid/117/6314.html?view=joint&param=450 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Wenqi Xian](https://dblp.org/pid/202/2384.html)

[\[c30\]](https://dblp.org/pid/117/6314.html#c30) [\[c17\]](https://dblp.org/pid/117/6314.html#c17) [\[i19\]](https://dblp.org/pid/117/6314.html#i19) [\[i10\]](https://dblp.org/pid/117/6314.html#i10)

[451](https://dblp.org/pid/117/6314.html?view=joint&param=451 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Anqi Xiao](https://dblp.org/pid/307/8649.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[452](https://dblp.org/pid/117/6314.html?view=joint&param=452 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chaowei Xiao](https://dblp.org/pid/150/3317.html)

[\[c16\]](https://dblp.org/pid/117/6314.html#c16) [\[i17\]](https://dblp.org/pid/117/6314.html#i17)

[453](https://dblp.org/pid/117/6314.html?view=joint&param=453 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jianxiong Xiao](https://dblp.org/pid/57/5248.html)

[\[c3\]](https://dblp.org/pid/117/6314.html#c3) [\[c2\]](https://dblp.org/pid/117/6314.html#c2) [\[i2\]](https://dblp.org/pid/117/6314.html#i2) [\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[454](https://dblp.org/pid/117/6314.html?view=joint&param=454 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[455](https://dblp.org/pid/117/6314.html?view=joint&param=455 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jinxia Xie](https://dblp.org/pid/294/3376.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[456](https://dblp.org/pid/117/6314.html?view=joint&param=456 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chenlong Xu](https://dblp.org/pid/315/8714.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[457](https://dblp.org/pid/117/6314.html?view=joint&param=457 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Haofei Xu](https://dblp.org/pid/236/6248.html)

[\[c95\]](https://dblp.org/pid/117/6314.html#c95) [\[j6\]](https://dblp.org/pid/117/6314.html#j6) [\[i58\]](https://dblp.org/pid/117/6314.html#i58) [\[i41\]](https://dblp.org/pid/117/6314.html#i41)

[458](https://dblp.org/pid/117/6314.html?view=joint&param=458 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Huazhe Xu](https://dblp.org/pid/164/9006.html)

[\[c23\]](https://dblp.org/pid/117/6314.html#c23) [\[c14\]](https://dblp.org/pid/117/6314.html#c14) [\[i20\]](https://dblp.org/pid/117/6314.html#i20) [\[i14\]](https://dblp.org/pid/117/6314.html#i14) [\[c7\]](https://dblp.org/pid/117/6314.html#c7) [\[i4\]](https://dblp.org/pid/117/6314.html#i4)

[459](https://dblp.org/pid/117/6314.html?view=joint&param=459 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Min Xu 0001](https://dblp.org/pid/09/0-1.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[460](https://dblp.org/pid/117/6314.html?view=joint&param=460 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[461](https://dblp.org/pid/117/6314.html?view=joint&param=461 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Wei Xu 0017](https://dblp.org/pid/32/1213-17.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[462](https://dblp.org/pid/117/6314.html?view=joint&param=462 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yong Xu 0007](https://dblp.org/pid/07/4630-7.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[463](https://dblp.org/pid/117/6314.html?view=joint&param=463 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yuanyou Xu](https://dblp.org/pid/248/7663.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[464](https://dblp.org/pid/117/6314.html?view=joint&param=464 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[465](https://dblp.org/pid/117/6314.html?view=joint&param=465 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zizheng Xun](https://dblp.org/pid/340/1441.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[466](https://dblp.org/pid/117/6314.html?view=joint&param=466 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[467](https://dblp.org/pid/117/6314.html?view=joint&param=467 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[468](https://dblp.org/pid/117/6314.html?view=joint&param=468 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Dawei Yang](https://dblp.org/pid/22/1038.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[469](https://dblp.org/pid/117/6314.html?view=joint&param=469 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[470](https://dblp.org/pid/117/6314.html?view=joint&param=470 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Ming-Hsuan Yang 0001](https://dblp.org/pid/79/3711.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[471](https://dblp.org/pid/117/6314.html?view=joint&param=471 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Tianyu Yang 0003](https://dblp.org/pid/120/8076-3.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[472](https://dblp.org/pid/117/6314.html?view=joint&param=472 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[473](https://dblp.org/pid/117/6314.html?view=joint&param=473 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Wenyan Yang](https://dblp.org/pid/119/2426.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[474](https://dblp.org/pid/117/6314.html?view=joint&param=474 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiaokang Yang 0001](https://dblp.org/pid/06/3071-1.html)

[\[c74\]](https://dblp.org/pid/117/6314.html#c74) [\[i69\]](https://dblp.org/pid/117/6314.html#i69)

[475](https://dblp.org/pid/117/6314.html?view=joint&param=475 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[476](https://dblp.org/pid/117/6314.html?view=joint&param=476 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yi Yang 0001](https://dblp.org/pid/33/4854-1.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[477](https://dblp.org/pid/117/6314.html?view=joint&param=477 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yichun Yang](https://dblp.org/pid/249/9678.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[478](https://dblp.org/pid/117/6314.html?view=joint&param=478 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yung-Hsu Yang](https://dblp.org/pid/288/0092.html)

[\[c97\]](https://dblp.org/pid/117/6314.html#c97) [\[i90\]](https://dblp.org/pid/117/6314.html#i90) [\[j7\]](https://dblp.org/pid/117/6314.html#j7) [\[c59\]](https://dblp.org/pid/117/6314.html#c59) [\[c56\]](https://dblp.org/pid/117/6314.html#c56) [\[i39\]](https://dblp.org/pid/117/6314.html#i39) [\[i36\]](https://dblp.org/pid/117/6314.html#i36) [\[i28\]](https://dblp.org/pid/117/6314.html#i28)

[479](https://dblp.org/pid/117/6314.html?view=joint&param=479 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zongxin Yang](https://dblp.org/pid/249/5456.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[480](https://dblp.org/pid/117/6314.html?view=joint&param=480 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Botao Ye](https://dblp.org/pid/227/4610.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[481](https://dblp.org/pid/117/6314.html?view=joint&param=481 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Mingqiao Ye](https://dblp.org/pid/285/9253.html)

[\[c93\]](https://dblp.org/pid/117/6314.html#c93) [\[c77\]](https://dblp.org/pid/117/6314.html#c77) [\[c64\]](https://dblp.org/pid/117/6314.html#c64) [\[i74\]](https://dblp.org/pid/117/6314.html#i74) [\[i71\]](https://dblp.org/pid/117/6314.html#i71) [\[i59\]](https://dblp.org/pid/117/6314.html#i59)

[482](https://dblp.org/pid/117/6314.html?view=joint&param=482 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Li Yi 0001](https://dblp.org/pid/26/4239-1.html)

[\[i1\]](https://dblp.org/pid/117/6314.html#i1)

[483](https://dblp.org/pid/117/6314.html?view=joint&param=483 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xuanwu Yin](https://dblp.org/pid/119/0001.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[484](https://dblp.org/pid/117/6314.html?view=joint&param=484 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhichao Yin](https://dblp.org/pid/29/6211.html)

[\[c26\]](https://dblp.org/pid/117/6314.html#c26) [\[i12\]](https://dblp.org/pid/117/6314.html#i12)

[485](https://dblp.org/pid/117/6314.html?view=joint&param=485 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chenyu You](https://dblp.org/pid/191/9432.html)

[\[c91\]](https://dblp.org/pid/117/6314.html#c91)

[486](https://dblp.org/pid/117/6314.html?view=joint&param=486 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hongyuan Yu](https://dblp.org/pid/232/2265.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[487](https://dblp.org/pid/117/6314.html?view=joint&param=487 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiaqian Yu](https://dblp.org/pid/164/7325.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[488](https://dblp.org/pid/117/6314.html?view=joint&param=488 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Qianjin Yu](https://dblp.org/pid/53/10179.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[489](https://dblp.org/pid/117/6314.html?view=joint&param=489 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Rui Yu 0002](https://dblp.org/pid/43/4940-2.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10)

[490](https://dblp.org/pid/117/6314.html?view=joint&param=490 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Weichen Yu](https://dblp.org/pid/325/1209.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[491](https://dblp.org/pid/117/6314.html?view=joint&param=491 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhiding Yu](https://dblp.org/pid/67/5386.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[492](https://dblp.org/pid/117/6314.html?view=joint&param=492 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yongsheng Yuan](https://dblp.org/pid/364/8163.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[493](https://dblp.org/pid/117/6314.html?view=joint&param=493 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zehuan Yuan](https://dblp.org/pid/227/3298.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[494](https://dblp.org/pid/117/6314.html?view=joint&param=494 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Muhammad Zaigham Zaheer](https://dblp.org/pid/260/4206.html)

[\[c51\]](https://dblp.org/pid/117/6314.html#c51) [\[i56\]](https://dblp.org/pid/117/6314.html#i56)

[495](https://dblp.org/pid/117/6314.html?view=joint&param=495 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Kang Ze](https://dblp.org/pid/340/1107.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[496](https://dblp.org/pid/117/6314.html?view=joint&param=496 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Andy Zeng 0001](https://dblp.org/pid/159/1215.html)

[\[c9\]](https://dblp.org/pid/117/6314.html#c9) [\[i6\]](https://dblp.org/pid/117/6314.html#i6)

[497](https://dblp.org/pid/117/6314.html?view=joint&param=497 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiang Zhai](https://dblp.org/pid/291/9340.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[498](https://dblp.org/pid/117/6314.html?view=joint&param=498 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiaohua Zhai](https://dblp.org/pid/66/636.html)

[\[c69\]](https://dblp.org/pid/117/6314.html#c69) [\[i83\]](https://dblp.org/pid/117/6314.html#i83)

[499](https://dblp.org/pid/117/6314.html?view=joint&param=499 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[500](https://dblp.org/pid/117/6314.html?view=joint&param=500 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Chunhu Zhang](https://dblp.org/pid/292/0953.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[501](https://dblp.org/pid/117/6314.html?view=joint&param=501 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jianlin Zhang 0001](https://dblp.org/pid/37/1545-1.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[502](https://dblp.org/pid/117/6314.html?view=joint&param=502 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jing Zhang 0037](https://dblp.org/pid/05/3499-37.html)

[\[j6\]](https://dblp.org/pid/117/6314.html#j6) [\[i41\]](https://dblp.org/pid/117/6314.html#i41)

[503](https://dblp.org/pid/117/6314.html?view=joint&param=503 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Kai Zhang 0008](https://dblp.org/pid/55/957-8.html)

[\[c89\]](https://dblp.org/pid/117/6314.html#c89)

[504](https://dblp.org/pid/117/6314.html?view=joint&param=504 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[505](https://dblp.org/pid/117/6314.html?view=joint&param=505 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Linguang Zhang](https://dblp.org/pid/166/1290.html)

[\[c2\]](https://dblp.org/pid/117/6314.html#c2)

[506](https://dblp.org/pid/117/6314.html?view=joint&param=506 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Lu Zhang 0053](https://dblp.org/pid/82/10609-53.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[507](https://dblp.org/pid/117/6314.html?view=joint&param=507 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Mingyuan Zhang](https://dblp.org/pid/98/69.html)

[\[c68\]](https://dblp.org/pid/117/6314.html#c68) [\[i85\]](https://dblp.org/pid/117/6314.html#i85)

[508](https://dblp.org/pid/117/6314.html?view=joint&param=508 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Nanhai Zhang](https://dblp.org/pid/169/7234.html)

[\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[509](https://dblp.org/pid/117/6314.html?view=joint&param=509 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Siwei Zhang](https://dblp.org/pid/68/11277.html)

[\[c46\]](https://dblp.org/pid/117/6314.html#c46) [\[i25\]](https://dblp.org/pid/117/6314.html#i25)

[510](https://dblp.org/pid/117/6314.html?view=joint&param=510 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Tianzhu Zhang 0001](https://dblp.org/pid/15/7643-1.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[511](https://dblp.org/pid/117/6314.html?view=joint&param=511 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Wenkang Zhang](https://dblp.org/pid/340/0966.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[512](https://dblp.org/pid/117/6314.html?view=joint&param=512 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xiang Zhang 0022](https://dblp.org/pid/91/4353-22.html)

[\[c92\]](https://dblp.org/pid/117/6314.html#c92) [\[i88\]](https://dblp.org/pid/117/6314.html#i88)

[513](https://dblp.org/pid/117/6314.html?view=joint&param=513 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yachao Zhang 0001](https://dblp.org/pid/40/10584-1.html)

[\[c91\]](https://dblp.org/pid/117/6314.html#c91) [\[i70\]](https://dblp.org/pid/117/6314.html#i70)

[514](https://dblp.org/pid/117/6314.html?view=joint&param=514 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yan Zhang 0054](https://dblp.org/pid/04/3348-54.html)

[\[c46\]](https://dblp.org/pid/117/6314.html#c46) [\[i25\]](https://dblp.org/pid/117/6314.html#i25)

[515](https://dblp.org/pid/117/6314.html?view=joint&param=515 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yinda Zhang 0001](https://dblp.org/pid/135/4896-1.html)

[\[i2\]](https://dblp.org/pid/117/6314.html#i2)

[516](https://dblp.org/pid/117/6314.html?view=joint&param=516 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yulun Zhang 0001](https://dblp.org/pid/166/2763-1.html)

[\[c95\]](https://dblp.org/pid/117/6314.html#c95) [\[c92\]](https://dblp.org/pid/117/6314.html#c92) [\[c91\]](https://dblp.org/pid/117/6314.html#c91) [\[c90\]](https://dblp.org/pid/117/6314.html#c90) [\[c89\]](https://dblp.org/pid/117/6314.html#c89) [\[i88\]](https://dblp.org/pid/117/6314.html#i88) [\[c74\]](https://dblp.org/pid/117/6314.html#c74) [\[c62\]](https://dblp.org/pid/117/6314.html#c62) [\[i70\]](https://dblp.org/pid/117/6314.html#i70) [\[i69\]](https://dblp.org/pid/117/6314.html#i69) [\[i58\]](https://dblp.org/pid/117/6314.html#i58)

[517](https://dblp.org/pid/117/6314.html?view=joint&param=517 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yushan Zhang](https://dblp.org/pid/50/10702.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[518](https://dblp.org/pid/117/6314.html?view=joint&param=518 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhejun Zhang](https://dblp.org/pid/58/9847.html)

[\[c67\]](https://dblp.org/pid/117/6314.html#c67) [\[c65\]](https://dblp.org/pid/117/6314.html#c65) [\[c61\]](https://dblp.org/pid/117/6314.html#c61) [\[i82\]](https://dblp.org/pid/117/6314.html#i82) [\[i81\]](https://dblp.org/pid/117/6314.html#i81) [\[i60\]](https://dblp.org/pid/117/6314.html#i60) [\[c34\]](https://dblp.org/pid/117/6314.html#c34) [\[i31\]](https://dblp.org/pid/117/6314.html#i31)

[519](https://dblp.org/pid/117/6314.html?view=joint&param=519 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[520](https://dblp.org/pid/117/6314.html?view=joint&param=520 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhipeng Zhang](https://dblp.org/pid/49/4941.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[521](https://dblp.org/pid/117/6314.html?view=joint&param=521 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[522](https://dblp.org/pid/117/6314.html?view=joint&param=522 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Guodongfang Zhao](https://dblp.org/pid/364/8196.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[523](https://dblp.org/pid/117/6314.html?view=joint&param=523 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hang Zhao 0021](https://dblp.org/pid/31/2950-21.html)

[\[c85\]](https://dblp.org/pid/117/6314.html#c85) [\[i73\]](https://dblp.org/pid/117/6314.html#i73)

[524](https://dblp.org/pid/117/6314.html?view=joint&param=524 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Hengshuang Zhao](https://dblp.org/pid/185/7848.html)

[\[j9\]](https://dblp.org/pid/117/6314.html#j9)

[525](https://dblp.org/pid/117/6314.html?view=joint&param=525 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jie Zhao 0014](https://dblp.org/pid/23/3168-14.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[526](https://dblp.org/pid/117/6314.html?view=joint&param=526 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

aka: Shaochuan Zhao

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[527](https://dblp.org/pid/117/6314.html?view=joint&param=527 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zixiang Zhao](https://dblp.org/pid/65/5420.html)

[\[c90\]](https://dblp.org/pid/117/6314.html#c90)

[528](https://dblp.org/pid/117/6314.html?view=joint&param=528 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Feng Zheng 0001](https://dblp.org/pid/39/800-1.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[529](https://dblp.org/pid/117/6314.html?view=joint&param=529 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Haixia Zheng](https://dblp.org/pid/119/1585.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[530](https://dblp.org/pid/117/6314.html?view=joint&param=530 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Min Zheng](https://dblp.org/pid/23/328.html)

[\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[531](https://dblp.org/pid/117/6314.html?view=joint&param=531 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yaozong Zheng](https://dblp.org/pid/344/6907.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[532](https://dblp.org/pid/117/6314.html?view=joint&param=532 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[533](https://dblp.org/pid/117/6314.html?view=joint&param=533 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Tianfei Zhou](https://dblp.org/pid/150/6710.html)

[\[c37\]](https://dblp.org/pid/117/6314.html#c37) [\[i37\]](https://dblp.org/pid/117/6314.html#i37)

[534](https://dblp.org/pid/117/6314.html?view=joint&param=534 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yanzhao Zhou](https://dblp.org/pid/194/2778.html)

[\[c29\]](https://dblp.org/pid/117/6314.html#c29)

[535](https://dblp.org/pid/117/6314.html?view=joint&param=535 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Zhichao Zhou](https://dblp.org/pid/136/9853.html)

[\[c10\]](https://dblp.org/pid/117/6314.html#c10) [\[c5\]](https://dblp.org/pid/117/6314.html#c5)

[536](https://dblp.org/pid/117/6314.html?view=joint&param=536 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[537](https://dblp.org/pid/117/6314.html?view=joint&param=537 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[538](https://dblp.org/pid/117/6314.html?view=joint&param=538 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Yueting Zhuang](https://dblp.org/pid/218/7793.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71) [\[c45\]](https://dblp.org/pid/117/6314.html#c45)

[539](https://dblp.org/pid/117/6314.html?view=joint&param=539 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[ChengAo Zong](https://dblp.org/pid/364/8208.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[540](https://dblp.org/pid/117/6314.html?view=joint&param=540 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[Kunlong Zuo](https://dblp.org/pid/354/8493.html)

[\[c71\]](https://dblp.org/pid/117/6314.html#c71)

[541](https://dblp.org/pid/117/6314.html?view=joint&param=541 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/117/6314.html?view=group&param=1)

[René Zurbrügg](https://dblp.org/pid/292/2398.html)

[\[c88\]](https://dblp.org/pid/117/6314.html#c88) [\[i93\]](https://dblp.org/pid/117/6314.html#i93)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/117/6314.html#) [\[–\]](https://dblp.org/pid/117/6314.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/117/6314.html#) [\[–\]](https://dblp.org/pid/117/6314.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/117/6314.html#) [\[–\]](https://dblp.org/pid/117/6314.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/117/6314.html#) [\[–\]](https://dblp.org/pid/117/6314.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/117/6314.html#) [\[–\]](https://dblp.org/pid/117/6314.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)