> 抓取来源：https://dblp.org/pid/151/8848.html

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

🛈 Please note that only 63% of the items listed on this page have a DOI stored with their dblp record. Therefore, DOI-based queries can only provide partial results.

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Martin+Danelljan%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F151%2F8848%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Martin+Danelljan+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F151%2F8848%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Martin+Danelljan+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F151%2F8848%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Martin+Danelljan%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F151%2F8848%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Martin+Danelljan+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F151%2F8848%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Martin+Danelljan%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F151%2F8848%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Martin+Danelljan%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F151%2F8848%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F151%2F8848%3E+%7D+.%0A%0A%7D)

_showing all224 records_

20142025302014: 42015: 42016: 142016: 142017: 72017: 72017: 72018: 112018: 112018: 112019: 232019: 232019: 232020: 352020: 352021: 392021: 392022: 372022: 372022: 372023: 322023: 322023: 322024: 152024: 152025: 3

**refine by search term**

![](https://dblp.org/img/clear-mark.medium.16x16.png)![filter active](https://dblp.org/img/filter-mark.12x12.png)

**refine by type**

- [ ] Books and Theses(only)
- [ ] Journal Articles(only)
- [ ] Conference and Workshop Papers(only)
- [ ] Informal and Other Publications(only)

- select all \| deselect all

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by coauthor**

- ![](https://dblp.org/img/add-mark.12x12.png)Luc Van Gool (95)
- ![](https://dblp.org/img/add-mark.12x12.png)Radu Timofte (73)
- ![](https://dblp.org/img/add-mark.12x12.png)Fahad Shahbaz Khan (63)
- ![](https://dblp.org/img/add-mark.12x12.png)Michael Felsberg (59)
- ![](https://dblp.org/img/add-mark.12x12.png)Fisher Yu 0001 (50)
- ![](https://dblp.org/img/add-mark.12x12.png)Goutam Bhat (40)
- ![](https://dblp.org/img/add-mark.12x12.png)Lei Ke (24)
- ![](https://dblp.org/img/add-mark.12x12.png)Andreas Lugmayr (19)
- ![](https://dblp.org/img/add-mark.12x12.png)Yu-Wing Tai (16)
- ![](https://dblp.org/img/add-mark.12x12.png)Danda Pani Paudel (16)

- _998 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (219)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0001-6144-9520 (5)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (96)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (34)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (30)
- ![](https://dblp.org/img/add-mark.12x12.png)ICCV (24)
- ![](https://dblp.org/img/add-mark.12x12.png)ECCV (24)
- ![](https://dblp.org/img/add-mark.12x12.png)WACV (8)
- ![](https://dblp.org/img/add-mark.12x12.png)NeurIPS (6)
- ![](https://dblp.org/img/add-mark.12x12.png)BMVC (5)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Pattern Anal. Mach. Intell. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)PMLR (3)
- ![](https://dblp.org/img/add-mark.12x12.png)SCIA (2)

- _16 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)open (134)
- ![](https://dblp.org/img/add-mark.12x12.png)closed (88)
- ![](https://dblp.org/img/add-mark.12x12.png)unavailable (2)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[c119\]
[Asen Nachkov](https://dblp.org/pid/354/6217.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Diffusion-Based Particle-DETR for BEV Perception. [WACV2025](https://dblp.org/db/conf/wacv/wacv2025.html#conf/wacv/NachkovPDG25): 2725-2735
- ![](https://dblp.org/img/n.png)

\[c118\]
[Abdelrahman M. Shaker](https://dblp.org/pid/250/0334.html), [Syed Talal Wasim](https://dblp.org/pid/344/4424.html), Martin Danelljan, [Salman H. Khan](https://dblp.org/pid/32/11535-1.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html):

Efficient Video Object Segmentation via Modulated Cross-Attention Memory. [WACV2025](https://dblp.org/db/conf/wacv/wacv2025.html#conf/wacv/ShakerWD00K25): 8681-8690
- ![](https://dblp.org/img/n.png)

\[c117\]
[Frano Rajic](https://dblp.org/pid/331/2107.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

Segment Anything Meets Point Tracking. [WACV2025](https://dblp.org/db/conf/wacv/wacv2025.html#conf/wacv/RajicKTTD025): 9302-9311
- 2024
- ![](https://dblp.org/img/n.png)

\[c116\]
[Rui Gong](https://dblp.org/pid/75/1938.html), Martin Danelljan, [Han Sun](https://dblp.org/pid/49/6614.html), [Julio Delgado Mangas](https://dblp.org/pid/351/0410.html), [Nikolay Marin](https://dblp.org/pid/407/2079.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Prompting Diffusion Representations for Cross-Domain Semantic Segmentation. [BMVC2024](https://dblp.org/db/conf/bmvc/bmvc2024.html#conf/bmvc/GongDSMMG24)
- ![](https://dblp.org/img/n.png)

\[c115\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Lei Ke](https://dblp.org/pid/26/5225.html), Martin Danelljan, [Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Matching Anything by Segmenting Anything. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/LiKDPSG024): 18963-18973
- ![](https://dblp.org/img/n.png)

\[c114\]
[Jan-Nico Zaech](https://dblp.org/pid/217/2208.html), Martin Danelljan, [Tolga Birdal](https://dblp.org/pid/143/7056.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Probabilistic Sampling of Balanced K-Means using Adiabatic Quantum Computing. [CVPR2024](https://dblp.org/db/conf/cvpr/cvpr2024.html#conf/cvpr/ZaechDBG24): 26191-26201
- ![](https://dblp.org/img/n.png)

\[c113\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Yung-Hsu Yang](https://dblp.org/pid/288/0092.html), [Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

SLAck: Semantic, Location, and Appearance Aware Open-Vocabulary Tracking. [ECCV (27)2024](https://dblp.org/db/conf/eccv/eccv2024-27.html#conf/eccv/LiKYPSDG24): 1-18
- ![](https://dblp.org/img/n.png)

\[c112\]
[Mingqiao Ye](https://dblp.org/pid/285/9253.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html), [Lei Ke](https://dblp.org/pid/26/5225.html):

Gaussian Grouping: Segment and Edit Anything in 3D Scenes. [ECCV (29)2024](https://dblp.org/db/conf/eccv/eccv2024-29.html#conf/eccv/YeDYK24): 162-179
- ![](https://dblp.org/img/n.png)

\[c111\]
[Chunming He](https://dblp.org/pid/251/5104.html), [Kai Li](https://dblp.org/pid/l/KaiLi12.html), [Yachao Zhang](https://dblp.org/pid/40/10584-1.html), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Chenyu You](https://dblp.org/pid/191/9432.html), [Zhenhua Guo](https://dblp.org/pid/41/294-1.html), [Xiu Li](https://dblp.org/pid/13/1206-1.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

Strategic Preys Make Acute Predators: Enhancing Camouflaged Object Detectors by Generating Camouflaged Objects. [ICLR2024](https://dblp.org/db/conf/iclr/iclr2024.html#conf/iclr/HeLZZY0LD024)
- ![](https://dblp.org/img/n.png)

\[c110\]
[Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Haotong Qin](https://dblp.org/pid/262/3626.html), [Zixiang Zhao](https://dblp.org/pid/65/5420.html), [Xianglong Liu](https://dblp.org/pid/55/7901-1.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

Flexible Residual Binarization for Image Super-Resolution. [ICML2024](https://dblp.org/db/conf/icml/icml2024.html#conf/icml/ZhangQZ0D024): 59731-59740
- ![](https://dblp.org/img/n.png)

\[c109\]
[Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Kai Zhang](https://dblp.org/pid/55/957-8.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

Lightweight Image Super-Resolution via Flexible Meta Pruning. [ICML2024](https://dblp.org/db/conf/icml/icml2024.html#conf/icml/Zhang0GD024): 60305-60314
- ![](https://dblp.org/img/n.png)

\[c108\]
[Evangelos Ntavelis](https://dblp.org/pid/262/6311.html), [Mohamad Shahbazi](https://dblp.org/pid/236/6647.html), [Iason Kastanis](https://dblp.org/pid/52/4455.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

StyleGenes: Discrete and Efficient Latent Distributions for GANs. [WACV2024](https://dblp.org/db/conf/wacv/wacv2024.html#conf/wacv/NtavelisSKDG24): 4065-4074
- ![](https://dblp.org/img/n.png)

\[c107\]
[Christoph Mayer](https://dblp.org/pid/163/0032-7.html), Martin Danelljan, [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Vittorio Ferrari](https://dblp.org/pid/16/3608.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Alina Kuznetsova](https://dblp.org/pid/117/5897.html):

Beyond SOT: Tracking Multiple Generic Objects at Once. [WACV2024](https://dblp.org/db/conf/wacv/wacv2024.html#conf/wacv/0007D0FGK24): 6812-6822
- ![](https://dblp.org/img/n.png)

\[i96\]
[Ani Vanyan](https://dblp.org/pid/313/5252.html), [Alvard Barseghyan](https://dblp.org/pid/365/4108.html), [Hakob Tamazyan](https://dblp.org/pid/365/3819.html), [Vahan Huroyan](https://dblp.org/pid/200/8385.html), [Hrant Khachatrian](https://dblp.org/pid/20/10360.html), Martin Danelljan:

Analyzing Local Representations of Self-supervised Vision Transformers. [CoRRabs/2401.00463](https://dblp.org/db/journals/corr/corr2401.html#journals/corr/abs-2401-00463) (2024)
- ![](https://dblp.org/img/n.png)

\[i95\]
[Abdelrahman M. Shaker](https://dblp.org/pid/250/0334.html), [Syed Talal Wasim](https://dblp.org/pid/344/4424.html), Martin Danelljan, [Salman Khan](https://dblp.org/pid/32/11535-1.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html):

Efficient Video Object Segmentation via Modulated Cross-Attention Memory. [CoRRabs/2403.17937](https://dblp.org/db/journals/corr/corr2403.html#journals/corr/abs-2403-17937) (2024)
- ![](https://dblp.org/img/n.png)

\[i94\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Lei Ke](https://dblp.org/pid/26/5225.html), Martin Danelljan, [Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Matching Anything by Segmenting Anything. [CoRRabs/2406.04221](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-04221) (2024)
- ![](https://dblp.org/img/n.png)

\[i93\]
[Sohyeong Kim](https://dblp.org/pid/184/5475.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Jean-Philippe Thiran](https://dblp.org/pid/t/JeanPhilippeThiran.html):

PIV3CAMS: a multi-camera dataset for multiple computer vision problems and its application to novel view-point synthesis. [CoRRabs/2407.18695](https://dblp.org/db/journals/corr/corr2407.html#journals/corr/abs-2407-18695) (2024)
- ![](https://dblp.org/img/n.png)

\[i92\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Yung-Hsu Yang](https://dblp.org/pid/288/0092.html), [Luigi Piccinelli](https://dblp.org/pid/328/8549.html), [Mattia Segù](https://dblp.org/pid/245/2565.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

SLAck: Semantic, Location, and Appearance Aware Open-Vocabulary Tracking. [CoRRabs/2409.11235](https://dblp.org/db/journals/corr/corr2409.html#journals/corr/abs-2409-11235) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j8\]
[Emil Brissman](https://dblp.org/pid/230/7851.html), [Joakim Johnander](https://dblp.org/pid/202/2479.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Michael Felsberg](https://dblp.org/pid/00/78.html):

Recurrent Graph Neural Networks for Video Instance Segmentation. [Int. J. Comput. Vis.131(2)](https://dblp.org/db/journals/ijcv/ijcv131.html#journals/ijcv/BrissmanJDF23): 471-495 (2023)
- ![](https://dblp.org/img/n.png)

\[j7\]
[Sajid Javed](https://dblp.org/pid/143/2961.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan![](https://dblp.org/img/orcid-mark.12x12.png), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Muhammad Haris Khan](https://dblp.org/pid/155/3076.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Visual Object Tracking With Discriminative Filters and Siamese Networks: A Survey and Outlook. [IEEE Trans. Pattern Anal. Mach. Intell.45(5)](https://dblp.org/db/journals/pami/pami45.html#journals/pami/JavedDKKFM23): 6552-6574 (2023)
- ![](https://dblp.org/img/n.png)

\[j6\]
[Prune Truong](https://dblp.org/pid/247/5738.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html)![](https://dblp.org/img/orcid-mark.12x12.png):

PDC-Net+: Enhanced Probabilistic Dense Correspondence Network. [IEEE Trans. Pattern Anal. Mach. Intell.45(8)](https://dblp.org/db/journals/pami/pami45.html#journals/pami/TruongDTG23): 10247-10266 (2023)
- ![](https://dblp.org/img/n.png)

\[j5\]
[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html), Martin Danelljan, [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

How Reliable is Your Regression Model's Uncertainty Under Real-World Distribution Shifts? [Trans. Mach. Learn. Res.2023](https://dblp.org/db/journals/tmlr/tmlr2023.html#journals/tmlr/GustafssonDS23) (2023)
- ![](https://dblp.org/img/n.png)

\[c106\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Tobias Fischer](https://dblp.org/pid/249/9213.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

OVTrack: Open-Vocabulary Multiple Object Tracking. [CVPR2023](https://dblp.org/db/conf/cvpr/cvpr2023.html#conf/cvpr/Li0KDDY23): 5567-5577
- ![](https://dblp.org/img/n.png)

\[c105\]
[Rui Gong](https://dblp.org/pid/75/1938.html), [Qin Wang](https://dblp.org/pid/35/1647-13.html), Martin Danelljan, [Dengxin Dai](https://dblp.org/pid/98/8616.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Continuous Pseudo-Label Rectified Domain Adaptive Semantic Segmentation with Implicit Neural Representations. [CVPR2023](https://dblp.org/db/conf/cvpr/cvpr2023.html#conf/cvpr/GongWDDG23): 7225-7235
- ![](https://dblp.org/img/n.png)

\[c104\]
[Lei Ke](https://dblp.org/pid/26/5225.html), Martin Danelljan, [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Mask-Free Video Instance Segmentation. [CVPR2023](https://dblp.org/db/conf/cvpr/cvpr2023.html#conf/cvpr/KeDDTTY23): 22857-22866
- ![](https://dblp.org/img/n.png)

\[c103\]
[Aron Schmied](https://dblp.org/pid/355/5910.html), [Tobias Fischer](https://dblp.org/pid/249/9213.html), Martin Danelljan, [Marc Pollefeys](https://dblp.org/pid/p/MarcPollefeys.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

R3D3: Dense 3D Reconstruction of Dynamic Scenes from Multiple Cameras. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/Schmied0DP023): 3193-3203
- ![](https://dblp.org/img/n.png)

\[c102\]
[Mingqiao Ye](https://dblp.org/pid/285/9253.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

Cascade-DETR: Delving into High-Quality Universal Object Detection. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/YeKLTTD023): 6681-6691
- ![](https://dblp.org/img/n.png)

\[c101\]
[Lucas Morin](https://dblp.org/pid/309/7785.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Maria Isabel Agea](https://dblp.org/pid/355/2674.html), [Ahmed S. Nassar](https://dblp.org/pid/321/9993.html), [Valéry Weber](https://dblp.org/pid/86/5323.html), [Ingmar Meijer](https://dblp.org/pid/46/5951.html), [Peter W. J. Staar](https://dblp.org/pid/136/7966.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

MolGrapher: Graph-based Visual Recognition of Chemical Structures. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/MorinDANWMS023): 19495-19504
- ![](https://dblp.org/img/n.png)

\[c100\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), Martin Danelljan, [Michael Felsberg](https://dblp.org/pid/00/78.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Khanh-Tung Tran](https://dblp.org/pid/359/3793.html), [Xuan-Son Vu](https://dblp.org/pid/151/8673.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Noor Al-Shakarji](https://dblp.org/pid/188/7419.html), [Dong An](https://dblp.org/pid/02/7028.html), [Michael Arens](https://dblp.org/pid/69/5391.html), [Stefan Becker](https://dblp.org/pid/62/7091.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Sebastian Bullinger](https://dblp.org/pid/197/9724.html), [Antoni B. Chan](https://dblp.org/pid/55/5814.html), [Shijie Chang](https://dblp.org/pid/277/8125.html), [Hanyuan Chen](https://dblp.org/pid/363/8621.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Yan Chen](https://dblp.org/pid/88/2827-17.html), [Zhenyu Chen](https://dblp.org/pid/86/541-1.html), [Yangming Cheng](https://dblp.org/pid/340/1285.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Chunyuan Deng](https://dblp.org/pid/154/4071.html), [Jiahua Dong](https://dblp.org/pid/247/5746.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Jianlong Fu](https://dblp.org/pid/83/8692.html), [Jie Gao](https://dblp.org/pid/181/2794.html), [Ruize Han](https://dblp.org/pid/205/4022.html), [Zeqi Hao](https://dblp.org/pid/348/8961.html), [Jun-Yan He](https://dblp.org/pid/173/3747.html), [Keji He](https://dblp.org/pid/319/4518.html), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Xiantao Hu](https://dblp.org/pid/160/8016.html), [Kaer Huang](https://dblp.org/pid/317/0780.html), [Yuqing Huang](https://dblp.org/pid/134/5853.html), [Yi Jiang](https://dblp.org/pid/66/3172-4.html), [Ben Kang](https://dblp.org/pid/340/1671.html), [Jin-Peng Lan](https://dblp.org/pid/332/1033.html), [Hyungjun Lee](https://dblp.org/pid/324/8911.html), [Chenyang Li](https://dblp.org/pid/15/1523-7.html), [Jiahao Li](https://dblp.org/pid/150/5524-5.html), [Ning Li](https://dblp.org/pid/14/5410-44.html), [Wangkai Li](https://dblp.org/pid/340/1456.html), [Xiaodi Li](https://dblp.org/pid/63/7279.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Pengyu Liu](https://dblp.org/pid/73/7783-5.html), [Yue Liu](https://dblp.org/pid/74/1932.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Bin Luo](https://dblp.org/pid/36/4256-8.html), [Ping Luo](https://dblp.org/pid/54/4989-2.html), [Yinchao Ma](https://dblp.org/pid/189/1326.html), [Deshui Miao](https://dblp.org/pid/307/5501.html), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Kannappan Palaniappan](https://dblp.org/pid/21/700.html), [Hancheol Park](https://dblp.org/pid/161/3495.html), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Zekun Qian](https://dblp.org/pid/315/4066.html), [Gani Rahmon](https://dblp.org/pid/291/7224.html), [Norbert Scherer-Negenborn](https://dblp.org/pid/45/8662.html), [Pengcheng Shao](https://dblp.org/pid/364/8295.html), [Wooksu Shin](https://dblp.org/pid/327/3602.html), [Elham Soltani Kazemi](https://dblp.org/pid/318/1851.html), [Tianhui Song](https://dblp.org/pid/181/8738.html), [Rainer Stiefelhagen](https://dblp.org/pid/31/4699.html), [Rui Sun](https://dblp.org/pid/01/3595-6.html), [Chuanming Tang](https://dblp.org/pid/237/6254.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html), [Imad Eddine Toubal](https://dblp.org/pid/292/6360.html), [Jack Valmadre](https://dblp.org/pid/50/8535.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Jash Vira](https://dblp.org/pid/364/8266.html), [Stéphane Vujasinovic](https://dblp.org/pid/237/5053.html), [Cheng Wan](https://dblp.org/pid/118/7267-6.html), [Jia Wan](https://dblp.org/pid/13/6504-1.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Feifan Wang](https://dblp.org/pid/213/0685.html), [He Wang](https://dblp.org/pid/01/6368-28.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Song Wang](https://dblp.org/pid/62/3151-2.html), [Yaowei Wang](https://dblp.org/pid/68/2992-1.html), [Zhepeng Wang](https://dblp.org/pid/242/8456-2.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Jiannan Wu](https://dblp.org/pid/277/0616.html), [Qiangqiang Wu](https://dblp.org/pid/193/1415.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Anqi Xiao](https://dblp.org/pid/307/8649.html), [Jinxia Xie](https://dblp.org/pid/294/3376.html), [Chenlong Xu](https://dblp.org/pid/315/8714.html), [Min Xu](https://dblp.org/pid/09/0-1.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Yuanyou Xu](https://dblp.org/pid/248/7663.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Dawei Yang](https://dblp.org/pid/22/1038.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Tianyu Yang](https://dblp.org/pid/120/8076-3.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Xuanwu Yin](https://dblp.org/pid/119/0001.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Qianjin Yu](https://dblp.org/pid/53/10179.html), [Weichen Yu](https://dblp.org/pid/325/1209.html), [Yongsheng Yuan](https://dblp.org/pid/364/8163.html), [Zehuan Yuan](https://dblp.org/pid/227/3298.html), [Jianlin Zhang](https://dblp.org/pid/37/1545-1.html), [Lu Zhang](https://dblp.org/pid/82/10609-53.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Guodongfang Zhao](https://dblp.org/pid/364/8196.html), [Shaochuan Zhao](https://dblp.org/pid/260/3125.html), [Yaozong Zheng](https://dblp.org/pid/344/6907.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html), [ChengAo Zong](https://dblp.org/pid/364/8208.html), [Kunlong Zuo](https://dblp.org/pid/354/8493.html):

The First Visual Object Tracking Segmentation VOTS2023 Challenge Results. [ICCV (Workshops)2023](https://dblp.org/db/conf/iccvw/iccvw2023.html#conf/iccvw/KristanMDFCZLDZ23): 1788-1810
- ![](https://dblp.org/img/n.png)

\[c99\]
[Mohamad Shahbazi](https://dblp.org/pid/236/6647.html), [Evangelos Ntavelis](https://dblp.org/pid/262/6311.html), [Alessio Tonioni](https://dblp.org/pid/203/8831.html), [Edo Collins](https://dblp.org/pid/176/2794.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

NeRF-GAN Distillation for Efficient 3D-Aware Generation with Convolutions. [ICCV (Workshops)2023](https://dblp.org/db/conf/iccvw/iccvw2023.html#conf/iccvw/ShahbaziNTCPDG23): 2880-2890
- ![](https://dblp.org/img/n.png)

\[c98\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Mingqiao Ye](https://dblp.org/pid/285/9253.html), Martin Danelljan, [Yifan Liu](https://dblp.org/pid/23/4955-1.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Segment Anything in High Quality. [NeurIPS2023](https://dblp.org/db/conf/nips/neurips2023.html#conf/nips/KeYDLTT023)
- ![](https://dblp.org/img/n.png)

\[c97\]
[Haotong Qin](https://dblp.org/pid/262/3626.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Xudong Ma](https://dblp.org/pid/19/2951.html), Martin Danelljan, [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Xianglong Liu](https://dblp.org/pid/55/7901-1.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

BiMatting: Efficient Video Matting via Binarization. [NeurIPS2023](https://dblp.org/db/conf/nips/neurips2023.html#conf/nips/QinK0DTT0023)
- ![](https://dblp.org/img/n.png)

\[c96\]
[Haotong Qin](https://dblp.org/pid/262/3626.html), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Yifu Ding](https://dblp.org/pid/219/1995.html), [Yifan Liu](https://dblp.org/pid/23/4955-1.html), [Xianglong Liu](https://dblp.org/pid/55/7901-1.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

QuantSR: Accurate Low-bit Quantization for Efficient Image Super-Resolution. [NeurIPS2023](https://dblp.org/db/conf/nips/neurips2023.html#conf/nips/QinZD00D023)
- ![](https://dblp.org/img/n.png)

\[c95\]
[Philippe Blatter](https://dblp.org/pid/309/5966.html), [Menelaos Kanakis](https://dblp.org/pid/208/1757.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Efficient Visual Tracking with Exemplar Transformers. [WACV2023](https://dblp.org/db/conf/wacv/wacv2023.html#conf/wacv/BlatterKDG23): 1571-1581
- ![](https://dblp.org/img/n.png)

\[c94\]
[Dario Fuoli](https://dblp.org/pid/260/3093.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Fast Online Video Super-Resolution with Deformable Attention Pyramid. [WACV2023](https://dblp.org/db/conf/wacv/wacv2023.html#conf/wacv/FuoliDTG23): 1735-1744
- ![](https://dblp.org/img/n.png)

\[i91\]
[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html), Martin Danelljan, [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

How Reliable is Your Regression Model's Uncertainty Under Real-World Distribution Shifts? [CoRRabs/2302.03679](https://dblp.org/db/journals/corr/corr2302.html#journals/corr/abs-2302-03679) (2023)
- ![](https://dblp.org/img/n.png)

\[i90\]
[Mohamad Shahbazi](https://dblp.org/pid/236/6647.html), [Evangelos Ntavelis](https://dblp.org/pid/262/6311.html), [Alessio Tonioni](https://dblp.org/pid/203/8831.html), [Edo Collins](https://dblp.org/pid/176/2794.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

NeRF-GAN Distillation for Efficient 3D-Aware Generation with Convolutions. [CoRRabs/2303.12865](https://dblp.org/db/journals/corr/corr2303.html#journals/corr/abs-2303-12865) (2023)
- ![](https://dblp.org/img/n.png)

\[i89\]
[Lei Ke](https://dblp.org/pid/26/5225.html), Martin Danelljan, [Henghui Ding](https://dblp.org/pid/230/1216.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Mask-Free Video Instance Segmentation. [CoRRabs/2303.15904](https://dblp.org/db/journals/corr/corr2303.html#journals/corr/abs-2303-15904) (2023)
- ![](https://dblp.org/img/n.png)

\[i88\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Tobias Fischer](https://dblp.org/pid/249/9213.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

OVTrack: Open-Vocabulary Multiple Object Tracking. [CoRRabs/2304.08408](https://dblp.org/db/journals/corr/corr2304.html#journals/corr/abs-2304-08408) (2023)
- ![](https://dblp.org/img/n.png)

\[i87\]
[Evangelos Ntavelis](https://dblp.org/pid/262/6311.html), [Mohamad Shahbazi](https://dblp.org/pid/236/6647.html), [Iason Kastanis](https://dblp.org/pid/52/4455.html), [Radu Timofte](https://dblp.org/pid/24/8616.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

StyleGenes: Discrete and Efficient Latent Distributions for GANs. [CoRRabs/2305.00599](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-00599) (2023)
- ![](https://dblp.org/img/n.png)

\[i86\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Mingqiao Ye](https://dblp.org/pid/285/9253.html), Martin Danelljan, [Yifan Liu](https://dblp.org/pid/23/4955-1.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Segment Anything in High Quality. [CoRRabs/2306.01567](https://dblp.org/db/journals/corr/corr2306.html#journals/corr/abs-2306-01567) (2023)
- ![](https://dblp.org/img/n.png)

\[i85\]
[Frano Rajic](https://dblp.org/pid/331/2107.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

Segment Anything Meets Point Tracking. [CoRRabs/2307.01197](https://dblp.org/db/journals/corr/corr2307.html#journals/corr/abs-2307-01197) (2023)
- ![](https://dblp.org/img/n.png)

\[i84\]
[Rui Gong](https://dblp.org/pid/75/1938.html), Martin Danelljan, [Han Sun](https://dblp.org/pid/49/6614.html), [Julio Delgado Mangas](https://dblp.org/pid/351/0410.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Prompting Diffusion Representations for Cross-Domain Semantic Segmentation. [CoRRabs/2307.02138](https://dblp.org/db/journals/corr/corr2307.html#journals/corr/abs-2307-02138) (2023)
- ![](https://dblp.org/img/n.png)

\[i83\]
[Mingqiao Ye](https://dblp.org/pid/285/9253.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Siyuan Li](https://dblp.org/pid/63/9705-8.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

Cascade-DETR: Delving into High-Quality Universal Object Detection. [CoRRabs/2307.11035](https://dblp.org/db/journals/corr/corr2307.html#journals/corr/abs-2307-11035) (2023)
- ![](https://dblp.org/img/n.png)

\[i82\]
[Chunming He](https://dblp.org/pid/251/5104.html), [Kai Li](https://dblp.org/pid/l/KaiLi12.html), [Yachao Zhang](https://dblp.org/pid/40/10584-1.html), [Yulun Zhang](https://dblp.org/pid/166/2763-1.html), [Zhenhua Guo](https://dblp.org/pid/41/294-1.html), [Xiu Li](https://dblp.org/pid/13/1206-1.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

Strategic Preys Make Acute Predators: Enhancing Camouflaged Object Detectors by Generating Camouflaged Objects. [CoRRabs/2308.03166](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-03166) (2023)
- ![](https://dblp.org/img/n.png)

\[i81\]
[Lucas Morin](https://dblp.org/pid/309/7785.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Maria Isabel Agea](https://dblp.org/pid/355/2674.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ahmed S. Nassar](https://dblp.org/pid/321/9993.html), [Valéry Weber](https://dblp.org/pid/86/5323.html), [Ingmar Meijer](https://dblp.org/pid/46/5951.html), [Peter W. J. Staar](https://dblp.org/pid/136/7966.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

MolGrapher: Graph-based Visual Recognition of Chemical Structures. [CoRRabs/2308.12234](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-12234) (2023)
- ![](https://dblp.org/img/n.png)

\[i80\]
[Aron Schmied](https://dblp.org/pid/355/5910.html), [Tobias Fischer](https://dblp.org/pid/249/9213.html), Martin Danelljan, [Marc Pollefeys](https://dblp.org/pid/p/MarcPollefeys.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

R3D3: Dense 3D Reconstruction of Dynamic Scenes from Multiple Cameras. [CoRRabs/2308.14713](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-14713) (2023)
- ![](https://dblp.org/img/n.png)

\[i79\]
[Jan-Nico Zaech](https://dblp.org/pid/217/2208.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Probabilistic Sampling of Balanced K-Means using Adiabatic Quantum Computing. [CoRRabs/2310.12153](https://dblp.org/db/journals/corr/corr2310.html#journals/corr/abs-2310-12153) (2023)
- ![](https://dblp.org/img/n.png)

\[i78\]
[Mingqiao Ye](https://dblp.org/pid/285/9253.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html), [Lei Ke](https://dblp.org/pid/26/5225.html):

Gaussian Grouping: Segment and Edit Anything in 3D Scenes. [CoRRabs/2312.00732](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-00732) (2023)
- ![](https://dblp.org/img/n.png)

\[i77\]
[Asen Nachkov](https://dblp.org/pid/354/6217.html), Martin Danelljan, [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Diffusion-Based Particle-DETR for BEV Perception. [CoRRabs/2312.11578](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-11578) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j4\]
[Jan-Nico Zaech](https://dblp.org/pid/217/2208.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alexander Liniger](https://dblp.org/pid/162/5560.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dengxin Dai](https://dblp.org/pid/98/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learnable Online Graph Representations for 3D Multi-Object Tracking. [IEEE Robotics Autom. Lett.7(2)](https://dblp.org/db/journals/ral/ral7.html#journals/ral/ZaechLDDG22): 5103-5110 (2022)
- ![](https://dblp.org/img/n.png)

\[c93\]
[Janis Postels](https://dblp.org/pid/246/4950.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Federico Tombari](https://dblp.org/pid/16/3539.html):

ManiFlow: Implicitly Representing Manifolds with Normalizing Flows. [3DV2022](https://dblp.org/db/conf/3dim/3dv2022.html#conf/3dim/PostelsDGT22): 84-93
- ![](https://dblp.org/img/n.png)

\[c92\]
[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html), Martin Danelljan, [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

Learning Proposals for Practical Energy-Based Regression. [AISTATS2022](https://dblp.org/db/conf/aistats/aistats2022.html#conf/aistats/GustafssonDS22): 4685-4704
- ![](https://dblp.org/img/n.png)

\[c91\]
[Mubashir Noman](https://dblp.org/pid/192/3732.html), [Wafa Al Ghallabi](https://dblp.org/pid/326/6543.html), [Daniya Kareem](https://dblp.org/pid/340/1779.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Akshay Dudhane](https://dblp.org/pid/213/7979.html), Martin Danelljan, [Hisham Cholakkal](https://dblp.org/pid/129/2046.html), [Salman Khan](https://dblp.org/pid/32/11535-1.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html):

AVisT: A Benchmark for Visual Object Tracking in Adverse Visibility. [BMVC2022](https://dblp.org/db/conf/bmvc/bmvc2022.html#conf/bmvc/NomanGK0DDC0GK22): 817
- ![](https://dblp.org/img/n.png)

\[c90\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kang-wook Kim](https://dblp.org/pid/16/9584-4.html), [Younggeun Kim](https://dblp.org/pid/294/6642.html), [Jae-Young Lee](https://dblp.org/pid/46/985.html), [Zechao Li](https://dblp.org/pid/51/8693.html), [Jinshan Pan](https://dblp.org/pid/06/10816.html), [Dongseok Shim](https://dblp.org/pid/274/0985.html), [Ki-Ung Song](https://dblp.org/pid/318/8996.html), [Jinhui Tang](https://dblp.org/pid/75/1030.html), [Cong Wang](https://dblp.org/pid/18/2771-18.html), [Zhihao Zhao](https://dblp.org/pid/144/0233.html):

NTIRE 2022 Challenge on Learning the Super-Resolution Space. [CVPR Workshops2022](https://dblp.org/db/conf/cvpr/cvpr2022w.html#conf/cvpr/LugmayrDTKKLLPS22): 785-796
- ![](https://dblp.org/img/n.png)

\[c89\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yizhen Cao](https://dblp.org/pid/202/4950.html), [Yuntian Cao](https://dblp.org/pid/327/3208.html), [Meiya Chen](https://dblp.org/pid/13/8141.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xihao Chen](https://dblp.org/pid/40/304.html), [Shen Cheng](https://dblp.org/pid/176/7871.html), [Akshay Dudhane](https://dblp.org/pid/213/7979.html), [Haoqiang Fan](https://dblp.org/pid/143/7181.html), [Ruipeng Gang](https://dblp.org/pid/252/5526.html), [Jian Gao](https://dblp.org/pid/02/563-8.html), [Yan Gu](https://dblp.org/pid/174/1818.html), [Jie Huang](https://dblp.org/pid/29/6643-17.html), [Liufeng Huang](https://dblp.org/pid/327/3404.html), [Youngsu Jo](https://dblp.org/pid/327/3609.html), [Sukju Kang](https://dblp.org/pid/327/3219.html), [Salman Khan](https://dblp.org/pid/32/11535-1.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Yuki Kondo](https://dblp.org/pid/53/3635.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chenghua Li](https://dblp.org/pid/70/10190.html), [Fangya Li](https://dblp.org/pid/300/7266.html), [Jinjing Li](https://dblp.org/pid/91/8541.html), [Youwei Li](https://dblp.org/pid/61/3956.html), [Zechao Li](https://dblp.org/pid/51/8693.html), [Chenming Liu](https://dblp.org/pid/321/0688.html), [Shuaicheng Liu](https://dblp.org/pid/49/8652.html), [Zikun Liu](https://dblp.org/pid/172/9824-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhuoming Liu](https://dblp.org/pid/289/2864-4.html), [Ziwei Luo](https://dblp.org/pid/166/7005-2.html), [Zhengxiong Luo](https://dblp.org/pid/253/1632-1.html), [Nancy Mehta](https://dblp.org/pid/305/3859.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Subrahmanyam Murala](https://dblp.org/pid/61/10849.html), [Yoonchan Nam](https://dblp.org/pid/327/3722.html), [Chihiro Nakatani](https://dblp.org/pid/300/2074.html), [Pavel Ostyakov](https://dblp.org/pid/227/2398.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jinshan Pan](https://dblp.org/pid/06/10816.html), [Ge Song](https://dblp.org/pid/86/2187.html), [Jian Sun](https://dblp.org/pid/68/4942-1.html), [Long Sun](https://dblp.org/pid/151/4095.html), [Jinhui Tang](https://dblp.org/pid/75/1030.html), [Norimichi Ukita](https://dblp.org/pid/46/5881.html), [Zhihong Wen](https://dblp.org/pid/216/7668.html), [Qi Wu](https://dblp.org/pid/96/3446-17.html), [Xiaohe Wu](https://dblp.org/pid/20/3663.html), [Zeyu Xiao](https://dblp.org/pid/276/3139.html), [Zhiwei Xiong](https://dblp.org/pid/54/6827.html), [Rongjian Xu](https://dblp.org/pid/193/0865.html), [Ruikang Xu](https://dblp.org/pid/292/4088.html), [Youliang Yan](https://dblp.org/pid/135/5316.html), [Jialin Yang](https://dblp.org/pid/52/5406.html), [Wentao Yang](https://dblp.org/pid/65/9079-3.html), [Zhongbao Yang](https://dblp.org/pid/327/3472.html), [Fuma Yasue](https://dblp.org/pid/327/3315.html), [Mingde Yao](https://dblp.org/pid/253/9580.html), [Lei Yu](https://dblp.org/pid/01/2775.html), [Cong Zhang](https://dblp.org/pid/18/2908.html), [Syed Waqas Zamir](https://dblp.org/pid/140/7811.html), [Jianxing Zhang](https://dblp.org/pid/62/7794.html), [Shuohao Zhang](https://dblp.org/pid/11/2195.html), [Zhilu Zhang](https://dblp.org/pid/220/3795-1.html), [Qian Zheng](https://dblp.org/pid/28/8138.html), [Gaofeng Zhou](https://dblp.org/pid/258/5676.html), [Magauiya Zhussip](https://dblp.org/pid/222/2064.html), [Xueyi Zou](https://dblp.org/pid/150/8081.html), [Wangmeng Zuo](https://dblp.org/pid/93/2671.html):

NTIRE 2022 Burst Super-Resolution Challenge. [CVPR Workshops2022](https://dblp.org/db/conf/cvpr/cvpr2022w.html#conf/cvpr/BhatDTCCCCCDFGG22): 1040-1060
- ![](https://dblp.org/img/n.png)

\[c88\]
[Lei Ke](https://dblp.org/pid/26/5225.html), Martin Danelljan, [Xia Li](https://dblp.org/pid/97/30-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yu-Wing Tai](https://dblp.org/pid/40/566.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Mask Transfiner for High-Quality Instance Segmentation. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/KeDLTTY22): 4402-4411
- ![](https://dblp.org/img/n.png)

\[c87\]
[Prune Truong](https://dblp.org/pid/247/5738.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Probabilistic Warp Consistency for Weakly-Supervised Semantic Correspondences. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/TruongDYG22): 8698-8708
- ![](https://dblp.org/img/n.png)

\[c86\]
[Christoph Mayer](https://dblp.org/pid/163/0032-7.html), Martin Danelljan, [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Transforming Model Prediction for Tracking. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/0007DBPPYG22): 8721-8730
- ![](https://dblp.org/img/n.png)

\[c85\]
[Jan-Nico Zaech](https://dblp.org/pid/217/2208.html), [Alexander Liniger](https://dblp.org/pid/162/5560.html), Martin Danelljan, [Dengxin Dai](https://dblp.org/pid/98/8616.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Adiabatic Quantum Computing for Multi Object Tracking. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/ZaechLDDG22): 8801-8812
- ![](https://dblp.org/img/n.png)

\[c84\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Andrés Romero](https://dblp.org/pid/29/641.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

RePaint: Inpainting using Denoising Diffusion Probabilistic Models. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/LugmayrDRYTG22): 11451-11461
- ![](https://dblp.org/img/n.png)

\[c83\]
[Evangelos Ntavelis](https://dblp.org/pid/262/6311.html), [Mohamad Shahbazi](https://dblp.org/pid/236/6647.html), [Iason Kastanis](https://dblp.org/pid/52/4455.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Arbitrary-Scale Image Synthesis. [CVPR2022](https://dblp.org/db/conf/cvpr/cvpr2022.html#conf/cvpr/NtavelisSKTDG22): 11523-11532
- ![](https://dblp.org/img/n.png)

\[c82\]
[Rui Gong](https://dblp.org/pid/75/1938.html), Martin Danelljan, [Dengxin Dai](https://dblp.org/pid/98/8616.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ajad Chhatkuli](https://dblp.org/pid/149/7655.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

TACS: Taxonomy Adaptive Cross-Domain Semantic Segmentation. [ECCV (34)2022](https://dblp.org/db/conf/eccv/eccv2022-34.html#conf/eccv/GongDDPCYG22): 19-35
- ![](https://dblp.org/img/n.png)

\[c81\]
[Joakim Johnander](https://dblp.org/pid/202/2479.html), [Johan Edstedt](https://dblp.org/pid/289/1724.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), Martin Danelljan:

Dense Gaussian Processes for Few-Shot Segmentation. [ECCV (29)2022](https://dblp.org/db/conf/eccv/eccv2022-29.html#conf/eccv/JohnanderEFKD22): 217-234
- ![](https://dblp.org/img/n.png)

\[c80\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), Martin Danelljan, [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Wenyan Yang](https://dblp.org/pid/119/2426.html), [Dingding Cai](https://dblp.org/pid/198/1127.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Kang Ben](https://dblp.org/pid/340/0959.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Hong Chang](https://dblp.org/pid/02/2689-1.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Jiaye Chen](https://dblp.org/pid/116/2901.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xilin Chen](https://dblp.org/pid/c/XilinChen.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Xiuyi Chen](https://dblp.org/pid/218/7190.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu-Hsi Chen](https://dblp.org/pid/127/3933.html), [Zhixing Chen](https://dblp.org/pid/62/3074.html), [Yangming Cheng](https://dblp.org/pid/340/1285.html), [Angelo Ciaramella](https://dblp.org/pid/37/6845.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Benjamin Dzubur](https://dblp.org/pid/340/1520.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Debajyoti Dhar](https://dblp.org/pid/128/3182.html), [Shangzhe Di](https://dblp.org/pid/304/1344.html), [Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shang Gao](https://dblp.org/pid/28/435-12.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Eric Granger](https://dblp.org/pid/86/2306.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Q. H. Gu](https://dblp.org/pid/340/1209.html), [Himanshu Gupta](https://dblp.org/pid/330/0760-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianfeng He](https://dblp.org/pid/93/8352.html), [Keji He](https://dblp.org/pid/319/4518.html), [Yan Huang](https://dblp.org/pid/75/6434-8.html), [Deepak Jangid](https://dblp.org/pid/340/1460.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Ze Kang](https://dblp.org/pid/340/1063.html), [Madhu Kiran](https://dblp.org/pid/39/10281.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Simiao Lai](https://dblp.org/pid/282/1954.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Dongwook Lee](https://dblp.org/pid/25/6543.html), [Hyunjeong Lee](https://dblp.org/pid/00/3423.html), [Seohyung Lee](https://dblp.org/pid/210/4662.html), [Hui Li](https://dblp.org/pid/66/3387-37.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ming Li](https://dblp.org/pid/l/MingLi10.html), [Wangkai Li](https://dblp.org/pid/340/1456.html), [Xi Li](https://dblp.org/pid/46/2311-1.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Xiao Li](https://dblp.org/pid/66/2069.html), [Zhe Li](https://dblp.org/pid/11/751-8.html), [Liting Lin](https://dblp.org/pid/227/2204.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Si Liu](https://dblp.org/pid/60/7642.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html), [Bingpeng Ma](https://dblp.org/pid/62/1822.html), [Chao Ma](https://dblp.org/pid/79/1552-4.html), [Jie Ma](https://dblp.org/pid/62/5110.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yinchao Ma](https://dblp.org/pid/189/1326.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Payman Moallem](https://dblp.org/pid/63/5378.html), [Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html), [Siyang Pan](https://dblp.org/pid/250/5753.html), [ChangBeom Park](https://dblp.org/pid/340/0926.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Litu Rout](https://dblp.org/pid/206/6445.html), [Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Tianhui Song](https://dblp.org/pid/181/8738.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Chao Sun](https://dblp.org/pid/54/3957.html), [Jingna Sun](https://dblp.org/pid/255/0702.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Om Prakash Verma](https://dblp.org/pid/61/8145.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Qiang Wang](https://dblp.org/pid/64/5630-23.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Jinlin Wu](https://dblp.org/pid/123/7200.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Xu](https://dblp.org/pid/32/1213-17.html), [Yong Xu](https://dblp.org/pid/07/4630-7.html), [Yuanyou Xu](https://dblp.org/pid/248/7663.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zizheng Xun](https://dblp.org/pid/340/1441.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Dawei Yang](https://dblp.org/pid/22/1038.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Yichun Yang](https://dblp.org/pid/249/9678.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Botao Ye](https://dblp.org/pid/227/4610.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Qianjin Yu](https://dblp.org/pid/53/10179.html), [Weichen Yu](https://dblp.org/pid/325/1209.html), [Kang Ze](https://dblp.org/pid/340/1107.html), [Jiang Zhai](https://dblp.org/pid/291/9340.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhu Zhang](https://dblp.org/pid/292/0953.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Haixia Zheng](https://dblp.org/pid/119/1585.html), [Min Zheng](https://dblp.org/pid/23/328.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html):

The Tenth Visual Object Tracking VOT2022 Challenge Results. [ECCV Workshops (8)2022](https://dblp.org/db/conf/eccv/eccv2022-w8.html#conf/eccv/KristanLMFPKCDZLDBZZYYCMFBBCCCCCCCCCCC22): 431-460
- ![](https://dblp.org/img/n.png)

\[c79\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), Martin Danelljan, [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Tracking Every Thing in the Wild. [ECCV (22)2022](https://dblp.org/db/conf/eccv/eccv2022-22.html#conf/eccv/LiDDHY22): 498-515
- ![](https://dblp.org/img/n.png)

\[c78\]
[Matthieu Paul](https://dblp.org/pid/255/6113.html), Martin Danelljan, [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Robust Visual Tracking by Segmentation. [ECCV (22)2022](https://dblp.org/db/conf/eccv/eccv2022-22.html#conf/eccv/PaulDMG22): 571-588
- ![](https://dblp.org/img/n.png)

\[c77\]
[Ardhendu Shekhar Tripathi](https://dblp.org/pid/141/9949.html), Martin Danelljan, [Samarth Shukla](https://dblp.org/pid/220/4107.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Transform Your Smartphone into a DSLR Camera: Learning the ISP in the Wild. [ECCV (6)2022](https://dblp.org/db/conf/eccv/eccv2022-6.html#conf/eccv/TripathiDSTG22): 625-641
- ![](https://dblp.org/img/n.png)

\[c76\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Yu-Wing Tai](https://dblp.org/pid/40/566.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Video Mask Transfiner for High-Quality Video Instance Segmentation. [ECCV (28)2022](https://dblp.org/db/conf/eccv/eccv2022-28.html#conf/eccv/KeDDTTY22): 731-747
- ![](https://dblp.org/img/n.png)

\[c75\]
[Mohamad Shahbazi](https://dblp.org/pid/236/6647.html), Martin Danelljan, [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Collapse by Conditioning: Training Class-conditional GANs with Limited Data. [ICLR2022](https://dblp.org/db/conf/iclr/iclr2022.html#conf/iclr/ShahbaziDPG22)
- ![](https://dblp.org/img/n.png)

\[c74\]
[Yihang She](https://dblp.org/pid/294/4508.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

Fast Hierarchical Learning for Few-Shot Object Detection. [IROS2022](https://dblp.org/db/conf/iros/iros2022.html#conf/iros/SheBDY22): 1993-2000
- ![](https://dblp.org/img/n.png)

\[c73\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Normalizing Flow as a Flexible Fidelity Objective for Photo-Realistic Super-resolution. [WACV2022](https://dblp.org/db/conf/wacv/wacv2022.html#conf/wacv/LugmayrDYGT22): 874-883
- ![](https://dblp.org/img/n.png)

\[i76\]
[Mohamad Shahbazi](https://dblp.org/pid/236/6647.html), Martin Danelljan, [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Collapse by Conditioning: Training Class-conditional GANs with Limited Data. [CoRRabs/2201.06578](https://dblp.org/db/journals/corr/corr2201.html#journals/corr/abs-2201-06578) (2022)
- ![](https://dblp.org/img/n.png)

\[i75\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Andrés Romero](https://dblp.org/pid/29/641.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Radu Timofte](https://dblp.org/pid/24/8616.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

RePaint: Inpainting using Denoising Diffusion Probabilistic Models. [CoRRabs/2201.09865](https://dblp.org/db/journals/corr/corr2201.html#journals/corr/abs-2201-09865) (2022)
- ![](https://dblp.org/img/n.png)

\[i74\]
[Dario Fuoli](https://dblp.org/pid/260/3093.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Fast Online Video Super-Resolution with Deformable Attention Pyramid. [CoRRabs/2202.01731](https://dblp.org/db/journals/corr/corr2202.html#journals/corr/abs-2202-01731) (2022)
- ![](https://dblp.org/img/n.png)

\[i73\]
[Jan-Nico Zaech](https://dblp.org/pid/217/2208.html), [Alexander Liniger](https://dblp.org/pid/162/5560.html), Martin Danelljan, [Dengxin Dai](https://dblp.org/pid/98/8616.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Adiabatic Quantum Computing for Multi Object Tracking. [CoRRabs/2202.08837](https://dblp.org/db/journals/corr/corr2202.html#journals/corr/abs-2202-08837) (2022)
- ![](https://dblp.org/img/n.png)

\[i72\]
[Prune Truong](https://dblp.org/pid/247/5738.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Probabilistic Warp Consistency for Weakly-Supervised Semantic Correspondences. [CoRRabs/2203.04279](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-04279) (2022)
- ![](https://dblp.org/img/n.png)

\[i71\]
[Ardhendu Shekhar Tripathi](https://dblp.org/pid/141/9949.html), Martin Danelljan, [Samarth Shukla](https://dblp.org/pid/220/4107.html), [Radu Timofte](https://dblp.org/pid/24/8616.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Transform your Smartphone into a DSLR Camera: Learning the ISP in the Wild. [CoRRabs/2203.10636](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-10636) (2022)
- ![](https://dblp.org/img/n.png)

\[i70\]
[Matthieu Paul](https://dblp.org/pid/255/6113.html), Martin Danelljan, [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Robust Visual Tracking by Segmentation. [CoRRabs/2203.11191](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-11191) (2022)
- ![](https://dblp.org/img/n.png)

\[i69\]
[Christoph Mayer](https://dblp.org/pid/163/0032-7.html), Martin Danelljan, [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Transforming Model Prediction for Tracking. [CoRRabs/2203.11192](https://dblp.org/db/journals/corr/corr2203.html#journals/corr/abs-2203-11192) (2022)
- ![](https://dblp.org/img/n.png)

\[i68\]
[Evangelos Ntavelis](https://dblp.org/pid/262/6311.html), [Mohamad Shahbazi](https://dblp.org/pid/236/6647.html), [Iason Kastanis](https://dblp.org/pid/52/4455.html), [Radu Timofte](https://dblp.org/pid/24/8616.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Arbitrary-Scale Image Synthesis. [CoRRabs/2204.02273](https://dblp.org/db/journals/corr/corr2204.html#journals/corr/abs-2204-02273) (2022)
- ![](https://dblp.org/img/n.png)

\[i67\]
[Siyuan Li](https://dblp.org/pid/63/9705-8.html), Martin Danelljan, [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Thomas E. Huang](https://dblp.org/pid/260/6642.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Tracking Every Thing in the Wild. [CoRRabs/2207.12978](https://dblp.org/db/journals/corr/corr2207.html#journals/corr/abs-2207-12978) (2022)
- ![](https://dblp.org/img/n.png)

\[i66\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Henghui Ding](https://dblp.org/pid/230/1216.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Yu-Wing Tai](https://dblp.org/pid/40/566.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Video Mask Transfiner for High-Quality Video Instance Segmentation. [CoRRabs/2207.14012](https://dblp.org/db/journals/corr/corr2207.html#journals/corr/abs-2207-14012) (2022)
- ![](https://dblp.org/img/n.png)

\[i65\]
[Mubashir Noman](https://dblp.org/pid/192/3732.html), [Wafa Al Ghallabi](https://dblp.org/pid/326/6543.html), [Daniya Najiha](https://dblp.org/pid/326/6241.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Akshay Dudhane](https://dblp.org/pid/213/7979.html), Martin Danelljan, [Hisham Cholakkal](https://dblp.org/pid/129/2046.html), [Salman Khan](https://dblp.org/pid/32/11535-1.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html):

AVisT: A Benchmark for Visual Object Tracking in Adverse Visibility. [CoRRabs/2208.06888](https://dblp.org/db/journals/corr/corr2208.html#journals/corr/abs-2208-06888) (2022)
- ![](https://dblp.org/img/n.png)

\[i64\]
[Janis Postels](https://dblp.org/pid/246/4950.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Federico Tombari](https://dblp.org/pid/16/3539.html):

ManiFlow: Implicitly Representing Manifolds with Normalizing Flows. [CoRRabs/2208.08932](https://dblp.org/db/journals/corr/corr2208.html#journals/corr/abs-2208-08932) (2022)
- ![](https://dblp.org/img/n.png)

\[i63\]
[Yihang She](https://dblp.org/pid/294/4508.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html):

Fast Hierarchical Learning for Few-Shot Object Detection. [CoRRabs/2210.05008](https://dblp.org/db/journals/corr/corr2210.html#journals/corr/abs-2210-05008) (2022)
- ![](https://dblp.org/img/n.png)

\[i62\]
[Christoph Mayer](https://dblp.org/pid/163/0032-7.html), Martin Danelljan, [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Vittorio Ferrari](https://dblp.org/pid/16/3608.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Alina Kuznetsova](https://dblp.org/pid/117/5897.html):

Beyond SOT: It's Time to Track Multiple Generic Objects at Once. [CoRRabs/2212.11920](https://dblp.org/db/journals/corr/corr2212.html#journals/corr/abs-2212-11920) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[c72\]
[Valentin Wolf](https://dblp.org/pid/283/5347.html), [Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

DeFlow: Learning Complex Image Degradations From Unpaired Data With Conditional Flows. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/WolfLDGT21): 94-103
- ![](https://dblp.org/img/n.png)

\[c71\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

NTIRE 2021 Learning the Super-Resolution Space Challenge. [CVPR Workshops2021](https://dblp.org/db/conf/cvpr/cvprw2021.html#conf/cvpr/LugmayrDT21): 596-612
- ![](https://dblp.org/img/n.png)

\[c70\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

NTIRE 2021 Challenge on Burst Super-Resolution: Methods and Results. [CVPR Workshops2021](https://dblp.org/db/conf/cvpr/cvprw2021.html#conf/cvpr/BhatDT21): 613-626
- ![](https://dblp.org/img/n.png)

\[c69\]
[Yawei Li](https://dblp.org/pid/32/6740-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wen Li](https://dblp.org/pid/06/721-1.html), Martin Danelljan, [Kai Zhang](https://dblp.org/pid/55/957-8.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shuhang Gu](https://dblp.org/pid/126/1028.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

The Heterogeneity Hypothesis: Finding Layer-Wise Differentiated Network Architectures. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/Li0D0GGT21): 2144-2153
- ![](https://dblp.org/img/n.png)

\[c68\]
[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html), Martin Danelljan, [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

Accurate 3D Object Detection Using Energy-Based Models. [CVPR Workshops2021](https://dblp.org/db/conf/cvpr/cvprw2021.html#conf/cvpr/GustafssonDS21): 2855-2864
- ![](https://dblp.org/img/n.png)

\[c67\]
[Prune Truong](https://dblp.org/pid/247/5738.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning Accurate Dense Correspondences and When To Trust Them. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/TruongDGT21): 5714-5724
- ![](https://dblp.org/img/n.png)

\[c66\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Deep Burst Super-Resolution. [CVPR2021](https://dblp.org/db/conf/cvpr/cvpr2021.html#conf/cvpr/BhatDGT21): 9209-9218
- ![](https://dblp.org/img/n.png)

\[c65\]
[Joakim Johnander](https://dblp.org/pid/202/2479.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Emil Brissman](https://dblp.org/pid/230/7851.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Video Instance Segmentation with Recurrent Graph Neural Networks. [GCPR2021](https://dblp.org/db/conf/dagm/gcpr2021.html#conf/dagm/JohnanderBDF21): 206-221
- ![](https://dblp.org/img/n.png)

\[c64\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Deep Reparametrization of Multi-Frame Super-Resolution and Denoising. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/BhatDYGT21): 2440-2450
- ![](https://dblp.org/img/n.png)

\[c63\]
[Jingyun Liang](https://dblp.org/pid/210/5052.html), [Andreas Lugmayr](https://dblp.org/pid/249/2710.html), [Kai Zhang](https://dblp.org/pid/55/957-8.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Hierarchical Conditional Flow: A Unified Framework for Image Super-Resolution and Image Rescaling. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/LiangL0DGT21): 4056-4065
- ![](https://dblp.org/img/n.png)

\[c62\]
[Shipra Jain](https://dblp.org/pid/143/8973.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Scaling Semantic Segmentation Beyond 1K Classes on a Single GPU. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/JainPDG21): 7406-7416
- ![](https://dblp.org/img/n.png)

\[c61\]
[Prune Truong](https://dblp.org/pid/247/5738.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Warp Consistency for Unsupervised Learning of Dense Correspondences. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/TruongDYG21): 10326-10336
- ![](https://dblp.org/img/n.png)

\[c60\]
[Christoph Mayer](https://dblp.org/pid/163/0032-7.html), Martin Danelljan, [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Learning Target Candidate Association to Keep Track of What Not to Track. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/0007DPG21): 13424-13434
- ![](https://dblp.org/img/n.png)

\[c59\]
[Bin Zhao](https://dblp.org/pid/73/4325.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Generating Masks from Boxes by Mining Spatio-Temporal Consistencies in Videos. [ICCV2021](https://dblp.org/db/conf/iccv/iccv2021.html#conf/iccv/ZhaoBDGT21): 13536-13546
- ![](https://dblp.org/img/n.png)

\[c58\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), Martin Danelljan, [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Yu-Chen Chiu](https://dblp.org/pid/199/2494.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Xingping Dong](https://dblp.org/pid/156/3020.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Bilge Günsel](https://dblp.org/pid/47/5125.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Wencheng Han](https://dblp.org/pid/280/3348.html), [Yanyan Huang](https://dblp.org/pid/88/4316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [J. Yin](https://dblp.org/pid/51/2242.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Jingen Liu](https://dblp.org/pid/10/5849.html), [Li Liu](https://dblp.org/pid/33/4528-36.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Jonathon Luiten](https://dblp.org/pid/211/7992.html), [Jie Ma](https://dblp.org/pid/62/5110.html), [Ziang Ma](https://dblp.org/pid/165/9621.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Yuzhen Niu](https://dblp.org/pid/28/7442.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Aravindh Rajiv](https://dblp.org/pid/307/9144.html), [Muhammad Rana](https://dblp.org/pid/276/0222.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Ling Shao](https://dblp.org/pid/75/1281.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furao Shen](https://dblp.org/pid/80/4685.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Paul Voigtlaender](https://dblp.org/pid/166/6430.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html), [Chenyan Wu](https://dblp.org/pid/76/1190.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang Xu](https://dblp.org/pid/126/2962.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Xiaohan Zhang](https://dblp.org/pid/96/6053.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Ming Zhen](https://dblp.org/pid/307/8430.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html):

The Ninth Visual Object Tracking VOT2021 Challenge Results. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/KristanMLFPKCDZ21): 2711-2738
- ![](https://dblp.org/img/n.png)

\[c57\]
[Ardhendu Shekhar Tripathi](https://dblp.org/pid/141/9949.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Fast Few-Shot Classification by Few-Iteration Meta-Learning. [ICRA2021](https://dblp.org/db/conf/icra/icra2021.html#conf/icra/TripathiDGT21): 9522-9528
- ![](https://dblp.org/img/n.png)

\[c56\]
[Matthieu Paul](https://dblp.org/pid/255/6113.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Local Memory Attention for Fast Video Semantic Segmentation. [IROS2021](https://dblp.org/db/conf/iros/iros2021.html#conf/iros/PaulDGT21): 1102-1109
- ![](https://dblp.org/img/n.png)

\[c55\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Xia Li](https://dblp.org/pid/97/30-5.html), Martin Danelljan, [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Prototypical Cross-Attention Networks for Multiple Object Tracking and Segmentation. [NeurIPS2021](https://dblp.org/db/conf/nips/neurips2021.html#conf/nips/KeLDTTY21): 1192-1203
- ![](https://dblp.org/img/n.png)

\[i61\]
[Prune Truong](https://dblp.org/pid/247/5738.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Learning Accurate Dense Correspondences and When to Trust Them. [CoRRabs/2101.01710](https://dblp.org/db/journals/corr/corr2101.html#journals/corr/abs-2101-01710) (2021)
- ![](https://dblp.org/img/n.png)

\[i60\]
[Matthieu Paul](https://dblp.org/pid/255/6113.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Local Memory Attention for Fast Video Semantic Segmentation. [CoRRabs/2101.01715](https://dblp.org/db/journals/corr/corr2101.html#journals/corr/abs-2101-01715) (2021)
- ![](https://dblp.org/img/n.png)

\[i59\]
[Bin Zhao](https://dblp.org/pid/73/4325.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Generating Masks from Boxes by Mining Spatio-Temporal Consistencies in Videos. [CoRRabs/2101.02196](https://dblp.org/db/journals/corr/corr2101.html#journals/corr/abs-2101-02196) (2021)
- ![](https://dblp.org/img/n.png)

\[i58\]
[Valentin Wolf](https://dblp.org/pid/283/5347.html), [Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

DeFlow: Learning Complex Image Degradations from Unpaired Data with Conditional Flows. [CoRRabs/2101.05796](https://dblp.org/db/journals/corr/corr2101.html#journals/corr/abs-2101-05796) (2021)
- ![](https://dblp.org/img/n.png)

\[i57\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Deep Burst Super-Resolution. [CoRRabs/2101.10997](https://dblp.org/db/journals/corr/corr2101.html#journals/corr/abs-2101-10997) (2021)
- ![](https://dblp.org/img/n.png)

\[i56\]
[Joakim Johnander](https://dblp.org/pid/202/2479.html), [Johan Edstedt](https://dblp.org/pid/289/1724.html), Martin Danelljan, [Michael Felsberg](https://dblp.org/pid/00/78.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html):

Deep Gaussian Processes for Few-Shot Segmentation. [CoRRabs/2103.16549](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-16549) (2021)
- ![](https://dblp.org/img/n.png)

\[i55\]
[Christoph Mayer](https://dblp.org/pid/163/0032-7.html), Martin Danelljan, [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Learning Target Candidate Association to Keep Track of What Not to Track. [CoRRabs/2103.16556](https://dblp.org/db/journals/corr/corr2103.html#journals/corr/abs-2103-16556) (2021)
- ![](https://dblp.org/img/n.png)

\[i54\]
[Prune Truong](https://dblp.org/pid/247/5738.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Warp Consistency for Unsupervised Learning of Dense Correspondences. [CoRRabs/2104.03308](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-03308) (2021)
- ![](https://dblp.org/img/n.png)

\[i53\]
[Jan-Nico Zaech](https://dblp.org/pid/217/2208.html), [Dengxin Dai](https://dblp.org/pid/98/8616.html), [Alexander Liniger](https://dblp.org/pid/162/5560.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Learnable Online Graph Representations for 3D Multi-Object Tracking. [CoRRabs/2104.11747](https://dblp.org/db/journals/corr/corr2104.html#journals/corr/abs-2104-11747) (2021)
- ![](https://dblp.org/img/n.png)

\[i52\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html), [Kazutoshi Akita](https://dblp.org/pid/260/3239.html), [Wooyeong Cho](https://dblp.org/pid/227/6116.html), [Haoqiang Fan](https://dblp.org/pid/143/7181.html), [Lanpeng Jia](https://dblp.org/pid/248/9198.html), [Daeshik Kim](https://dblp.org/pid/25/2348.html), [Bruno Lecouat](https://dblp.org/pid/215/4371.html), [Youwei Li](https://dblp.org/pid/61/3956.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shuaicheng Liu](https://dblp.org/pid/49/8652.html), [Ziluan Liu](https://dblp.org/pid/158/4864.html), [Ziwei Luo](https://dblp.org/pid/166/7005-2.html), [Takahiro Maeda](https://dblp.org/pid/26/5679-1.html), [Julien Mairal](https://dblp.org/pid/49/6555.html), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Xuan Mo](https://dblp.org/pid/09/7643.html), [Takeru Oba](https://dblp.org/pid/282/8759.html), [Pavel Ostyakov](https://dblp.org/pid/227/2398.html), [Jean Ponce](https://dblp.org/pid/p/JeanPonce.html), [Sanghyeok Son](https://dblp.org/pid/294/4695.html), [Jian Sun](https://dblp.org/pid/68/4942-1.html), [Norimichi Ukita](https://dblp.org/pid/46/5881.html), [Rao Muhammad Umer](https://dblp.org/pid/248/9258.html), [Youliang Yan](https://dblp.org/pid/135/5316.html), [Lei Yu](https://dblp.org/pid/01/2775.html), [Magauiya Zhussip](https://dblp.org/pid/222/2064.html), [Xueyi Zou](https://dblp.org/pid/150/8081.html):

NTIRE 2021 Challenge on Burst Super-Resolution: Methods and Results. [CoRRabs/2106.03839](https://dblp.org/db/journals/corr/corr2106.html#journals/corr/abs-2106-03839) (2021)
- ![](https://dblp.org/img/n.png)

\[i51\]
[Lei Ke](https://dblp.org/pid/26/5225.html), [Xia Li](https://dblp.org/pid/97/30-5.html), Martin Danelljan, [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Prototypical Cross-Attention Networks for Multiple Object Tracking and Segmentation. [CoRRabs/2106.11958](https://dblp.org/db/journals/corr/corr2106.html#journals/corr/abs-2106-11958) (2021)
- ![](https://dblp.org/img/n.png)

\[i50\]
[Jingyun Liang](https://dblp.org/pid/210/5052.html), [Andreas Lugmayr](https://dblp.org/pid/249/2710.html), [Kai Zhang](https://dblp.org/pid/55/957-8.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Hierarchical Conditional Flow: A Unified Framework for Image Super-Resolution and Image Rescaling. [CoRRabs/2108.05301](https://dblp.org/db/journals/corr/corr2108.html#journals/corr/abs-2108-05301) (2021)
- ![](https://dblp.org/img/n.png)

\[i49\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Deep Reparametrization of Multi-Frame Super-Resolution and Denoising. [CoRRabs/2108.08286](https://dblp.org/db/journals/corr/corr2108.html#journals/corr/abs-2108-08286) (2021)
- ![](https://dblp.org/img/n.png)

\[i48\]
[Rui Gong](https://dblp.org/pid/75/1938.html), Martin Danelljan, [Dengxin Dai](https://dblp.org/pid/98/8616.html), [Wenguan Wang](https://dblp.org/pid/145/1078.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Ajad Chhatkuli](https://dblp.org/pid/149/7655.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

TADA: Taxonomy Adaptive Domain Adaptation. [CoRRabs/2109.04813](https://dblp.org/db/journals/corr/corr2109.html#journals/corr/abs-2109-04813) (2021)
- ![](https://dblp.org/img/n.png)

\[i47\]
[Prune Truong](https://dblp.org/pid/247/5738.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

PDC-Net+: Enhanced Probabilistic Dense Correspondence Network. [CoRRabs/2109.13912](https://dblp.org/db/journals/corr/corr2109.html#journals/corr/abs-2109-13912) (2021)
- ![](https://dblp.org/img/n.png)

\[i46\]
[Joakim Johnander](https://dblp.org/pid/202/2479.html), [Johan Edstedt](https://dblp.org/pid/289/1724.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), Martin Danelljan:

Dense Gaussian Processes for Few-Shot Segmentation. [CoRRabs/2110.03674](https://dblp.org/db/journals/corr/corr2110.html#journals/corr/abs-2110-03674) (2021)
- ![](https://dblp.org/img/n.png)

\[i45\]
[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html), Martin Danelljan, [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

Learning Proposals for Practical Energy-Based Regression. [CoRRabs/2110.11948](https://dblp.org/db/journals/corr/corr2110.html#journals/corr/abs-2110-11948) (2021)
- ![](https://dblp.org/img/n.png)

\[i44\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Fisher Yu](https://dblp.org/pid/117/6314.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Normalizing Flow as a Flexible Fidelity Objective for Photo-Realistic Super-resolution. [CoRRabs/2111.03649](https://dblp.org/db/journals/corr/corr2111.html#journals/corr/abs-2111-03649) (2021)
- ![](https://dblp.org/img/n.png)

\[i43\]
[Lei Ke](https://dblp.org/pid/26/5225.html), Martin Danelljan, [Xia Li](https://dblp.org/pid/97/30-5.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html), [Chi-Keung Tang](https://dblp.org/pid/34/4366.html), [Fisher Yu](https://dblp.org/pid/117/6314.html):

Mask Transfiner for High-Quality Instance Segmentation. [CoRRabs/2111.13673](https://dblp.org/db/journals/corr/corr2111.html#journals/corr/abs-2111-13673) (2021)
- ![](https://dblp.org/img/n.png)

\[i42\]
[Sajid Javed](https://dblp.org/pid/143/2961.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Muhammad Haris Khan](https://dblp.org/pid/155/3076.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Jiri Matas](https://dblp.org/pid/m/JiriMatas.html):

Visual Object Tracking with Discriminative Filters and Siamese Networks: A Survey and Outlook. [CoRRabs/2112.02838](https://dblp.org/db/journals/corr/corr2112.html#journals/corr/abs-2112-02838) (2021)
- ![](https://dblp.org/img/n.png)

\[i41\]
[Philippe Blatter](https://dblp.org/pid/309/5966.html), [Menelaos Kanakis](https://dblp.org/pid/208/1757.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Efficient Visual Tracking with Exemplar Transformers. [CoRRabs/2112.09686](https://dblp.org/db/journals/corr/corr2112.html#journals/corr/abs-2112-09686) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[c54\]
[Fredrik Gustafsson](https://dblp.org/pid/394/4497.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html), [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

How to Train Your Energy-Based Model for Regression. [BMVC2020](https://dblp.org/db/conf/bmvc/bmvc2020.html#conf/bmvc/GustafssonDTS20)
- ![](https://dblp.org/img/n.png)

\[c53\]
[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html), Martin Danelljan, [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

Evaluating Scalable Bayesian Deep Learning Methods for Robust Computer Vision. [CVPR Workshops2020](https://dblp.org/db/conf/cvpr/cvprw2020.html#conf/cvpr/GustafssonDS20): 1289-1298
- ![](https://dblp.org/img/n.png)

\[c52\]
[Dario Fuoli](https://dblp.org/pid/260/3093.html), [Zhiwu Huang](https://dblp.org/pid/47/7711.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hua Wang](https://dblp.org/pid/33/3535-15.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Longcun Jin](https://dblp.org/pid/51/7090.html), [Dewei Su](https://dblp.org/pid/249/5714.html), [Jing Liu](https://dblp.org/pid/72/2590-31.html), [Jaehoon Lee](https://dblp.org/pid/95/386.html), [Michal Kudelski](https://dblp.org/pid/50/6979.html), [Lukasz Bala](https://dblp.org/pid/264/5872.html), [Dmitry Hrybov](https://dblp.org/pid/264/5801.html), [Marcin Mozejko](https://dblp.org/pid/228/6840.html), [Muchen Li](https://dblp.org/pid/122/2666.html), [Siyao Li](https://dblp.org/pid/163/8053.html), [Bo Pang](https://dblp.org/pid/16/6344-3.html), [Cewu Lu](https://dblp.org/pid/96/10571.html), [Chao Li](https://dblp.org/pid/66/190-34.html), [Dongliang He](https://dblp.org/pid/167/0539.html), [Fu Li](https://dblp.org/pid/37/4556-3.html), [Shilei Wen](https://dblp.org/pid/159/2939.html):

NTIRE 2020 Challenge on Video Quality Mapping: Methods and Results. [CVPR Workshops2020](https://dblp.org/db/conf/cvpr/cvprw2020.html#conf/cvpr/FuoliHDTWJSLLKB20): 1962-1974
- ![](https://dblp.org/img/n.png)

\[c51\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Namhyuk Ahn](https://dblp.org/pid/217/1998.html), [Dongwoon Bai](https://dblp.org/pid/07/2673.html), [Jie Cai](https://dblp.org/pid/95/3916-1.html), [Yun Cao](https://dblp.org/pid/40/2407-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Junyang Chen](https://dblp.org/pid/196/7893.html), [Kaihua Cheng](https://dblp.org/pid/264/5745.html), [Se Young Chun](https://dblp.org/pid/85/2542.html), [Wei Deng](https://dblp.org/pid/69/508.html), [Mostafa El-Khamy](https://dblp.org/pid/00/4303.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chiu Man Ho](https://dblp.org/pid/228/8363.html), [Xiaozhong Ji](https://dblp.org/pid/237/9544.html), [Amin Kheradmand](https://dblp.org/pid/93/9199.html), [Gwantae Kim](https://dblp.org/pid/264/5954.html), [Hanseok Ko](https://dblp.org/pid/67/5314.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kanghyu Lee](https://dblp.org/pid/218/1511.html), [Jungwon Lee](https://dblp.org/pid/87/381.html), [Hao Li](https://dblp.org/pid/17/5705-58.html), [Ziluan Liu](https://dblp.org/pid/158/4864.html), [Zhi-Song Liu](https://dblp.org/pid/144/8750.html), [Shuai Liu](https://dblp.org/pid/76/5789-0009.html), [Yunhua Lu](https://dblp.org/pid/45/2957.html), [Zibo Meng](https://dblp.org/pid/126/8042.html), [Pablo Navarrete Michelini](https://dblp.org/pid/63/1474.html), [Christian Micheloni](https://dblp.org/pid/28/38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Kalpesh Prajapati](https://dblp.org/pid/264/5768.html), [Haoyu Ren](https://dblp.org/pid/53/8616.html), [Yonghyeok Seo](https://dblp.org/pid/227/2546.html), [Wan-Chi Siu](https://dblp.org/pid/61/5203.html), [Kyung-Ah Sohn](https://dblp.org/pid/65/3835.html), [Ying Tai](https://dblp.org/pid/158/1384.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rao Muhammad Umer](https://dblp.org/pid/248/9258.html), [Shuangquan Wang](https://dblp.org/pid/23/5003.html), [Huibing Wang](https://dblp.org/pid/150/0713.html), [Timothy Haoning Wu](https://dblp.org/pid/264/5802-1.html), [Haoning Wu](https://dblp.org/pid/264/5802-1.html), [Biao Yang](https://dblp.org/pid/26/103.html), [Fuzhi Yang](https://dblp.org/pid/264/5783.html), [Jaejun Yoo](https://dblp.org/pid/141/8878-1.html), [Tongtong Zhao](https://dblp.org/pid/191/5253.html), [Yuanbo Zhou](https://dblp.org/pid/262/5471.html), [Haijie Zhuo](https://dblp.org/pid/209/2325.html), [Ziyao Zong](https://dblp.org/pid/264/5589.html), [Xueyi Zou](https://dblp.org/pid/150/8081.html):

NTIRE 2020 Challenge on Real-World Image Super-Resolution: Methods and Results. [CVPR Workshops2020](https://dblp.org/db/conf/cvpr/cvprw2020.html#conf/cvpr/LugmayrDTABCCCC20): 2058-2076
- ![](https://dblp.org/img/n.png)

\[c50\]
[Tiancai Wang](https://dblp.org/pid/179/0530.html), [Tong Yang](https://dblp.org/pid/44/7710-5.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), [Jian Sun](https://dblp.org/pid/68/4942-1.html):

Learning Human-Object Interaction Detection Using Interaction Points. [CVPR2020](https://dblp.org/db/conf/cvpr/cvpr2020.html#conf/cvpr/WangYDK0S20): 4115-4124
- ![](https://dblp.org/img/n.png)

\[c49\]
[Prune Truong](https://dblp.org/pid/247/5738.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

GLU-Net: Global-Local Universal Network for Dense Flow and Correspondences. [CVPR2020](https://dblp.org/db/conf/cvpr/cvpr2020.html#conf/cvpr/TruongDT20): 6257-6267
- ![](https://dblp.org/img/n.png)

\[c48\]
Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Probabilistic Regression for Visual Tracking. [CVPR2020](https://dblp.org/db/conf/cvpr/cvpr2020.html#conf/cvpr/DanelljanGT20): 7181-7190
- ![](https://dblp.org/img/n.png)

\[c47\]
[Andreas Robinson](https://dblp.org/pid/158/5786.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Learning Fast and Robust Target Models for Video Object Segmentation. [CVPR2020](https://dblp.org/db/conf/cvpr/cvpr2020.html#conf/cvpr/RobinsonLDKF20): 7404-7413
- ![](https://dblp.org/img/n.png)

\[c46\]
[Kai Zhang](https://dblp.org/pid/55/957-8.html), Martin Danelljan, [Yawei Li](https://dblp.org/pid/32/6740-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Liu](https://dblp.org/pid/03/2134-40.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jie Tang](https://dblp.org/pid/181/2702-6.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Yu Zhu](https://dblp.org/pid/38/5267-4.html), [Xiangyu He](https://dblp.org/pid/173/4661.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wenjie Xu](https://dblp.org/pid/25/1820.html), [Chenghua Li](https://dblp.org/pid/70/10190.html), [Cong Leng](https://dblp.org/pid/147/9188.html), [Jian Cheng](https://dblp.org/pid/14/6145-1.html), [Guangyang Wu](https://dblp.org/pid/254/8240.html), [Wenyi Wang](https://dblp.org/pid/79/2722-5.html), [Xiaohong Liu](https://dblp.org/pid/95/2454-1.html), [Hengyuan Zhao](https://dblp.org/pid/260/3042.html), [Xiangtao Kong](https://dblp.org/pid/274/3262.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jingwen He](https://dblp.org/pid/14/2195.html), [Yu Qiao](https://dblp.org/pid/q/YuQiao1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chao Dong](https://dblp.org/pid/16/1278-5.html), [Xiaotong Luo](https://dblp.org/pid/169/3960.html), [Liang Chen](https://dblp.org/pid/01/5394.html), [Jiangtao Zhang](https://dblp.org/pid/38/8912.html), [Maitreya Suin](https://dblp.org/pid/254/1457.html), [Kuldeep Purohit](https://dblp.org/pid/191/2655.html), [A. N. Rajagopalan](https://dblp.org/pid/73/3473.html), [Xiaochuan Li](https://dblp.org/pid/10/8076-1.html), [Zhiqiang Lang](https://dblp.org/pid/238/0425.html), [Jiangtao Nie](https://dblp.org/pid/252/4948.html), [Wei Wei](https://dblp.org/pid/24/4105-8.html), [Lei Zhang](https://dblp.org/pid/64/5666-6.html), [Abdul Muqeet](https://dblp.org/pid/245/0047.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiwon Hwang](https://dblp.org/pid/157/7832.html), [Subin Yang](https://dblp.org/pid/144/2910.html), [Jung Heum Kang](https://dblp.org/pid/274/1655.html), [Sung-Ho Bae](https://dblp.org/pid/76/2068.html), [Yongwoo Kim](https://dblp.org/pid/90/8739.html), [Yanyun Qu](https://dblp.org/pid/03/3500.html), [Geun-Woo Jeon](https://dblp.org/pid/274/3180.html), [Jun-Ho Choi](https://dblp.org/pid/139/4714.html), [Jun-Hyuk Kim](https://dblp.org/pid/193/6547.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jong-Seok Lee](https://dblp.org/pid/70/1152.html), [Steven Marty](https://dblp.org/pid/274/2797.html), [Éric Marty](https://dblp.org/pid/222/9632.html), [Dongliang Xiong](https://dblp.org/pid/192/3737.html), [Siang Chen](https://dblp.org/pid/260/2691.html), [Lin Zha](https://dblp.org/pid/133/3991.html), [Jiande Jiang](https://dblp.org/pid/264/5784.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html), [Wen Lu](https://dblp.org/pid/31/6140-4.html), [Haicheng Wang](https://dblp.org/pid/150/4188.html), [Vineeth Bhaskara](https://dblp.org/pid/197/6505.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alex Levinshtein](https://dblp.org/pid/40/6950.html), [Stavros Tsogkas](https://dblp.org/pid/119/1444.html), [Allan D. Jepson](https://dblp.org/pid/93/4241.html), [Xiangzhen Kong](https://dblp.org/pid/80/531.html), [Tongtong Zhao](https://dblp.org/pid/191/5253.html), [Shanshan Zhao](https://dblp.org/pid/02/7781-3.html), [Hrishikesh P. S](https://dblp.org/pid/264/5454.html), [Densen Puthussery](https://dblp.org/pid/264/5624.html), [C. V. Jiji](https://dblp.org/pid/75/3033.html), [Nan Nan](https://dblp.org/pid/26/3712.html), [Shuai Liu](https://dblp.org/pid/76/5789-0009.html), [Jie Cai](https://dblp.org/pid/95/3916-1.html), [Zibo Meng](https://dblp.org/pid/126/8042.html), [Jiaming Ding](https://dblp.org/pid/274/2850.html), [Chiu Man Ho](https://dblp.org/pid/228/8363.html), [Xuehui Wang](https://dblp.org/pid/78/6531.html), [Qiong Yan](https://dblp.org/pid/122/4814.html), [Yuzhi Zhao](https://dblp.org/pid/240/3833.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Long Chen](https://dblp.org/pid/64/5725-5.html), [Long Sun](https://dblp.org/pid/151/4095.html), [Wenhao Wang](https://dblp.org/pid/57/9813.html), [Zhenbing Liu](https://dblp.org/pid/19/7578.html), [Rushi Lan](https://dblp.org/pid/44/8845.html), [Rao Muhammad Umer](https://dblp.org/pid/248/9258.html), [Christian Micheloni](https://dblp.org/pid/28/38.html)![](https://dblp.org/img/orcid-mark.12x12.png):

AIM 2020 Challenge on Efficient Super-Resolution: Methods and Results. [ECCV Workshops (3)2020](https://dblp.org/db/conf/eccv/eccv2020-w3.html#conf/eccv/ZhangDLTLTWZHXL20): 5-40
- ![](https://dblp.org/img/n.png)

\[c45\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Know Your Surroundings: Exploiting Scene Information for Object Tracking. [ECCV (23)2020](https://dblp.org/db/conf/eccv/eccv2020-23.html#conf/eccv/BhatDGT20): 205-221
- ![](https://dblp.org/img/n.png)

\[c44\]
[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html), Martin Danelljan, [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

Energy-Based Models for Deep Probabilistic Regression. [ECCV (20)2020](https://dblp.org/db/conf/eccv/eccv2020-20.html#conf/eccv/GustafssonDBS20): 325-343
- ![](https://dblp.org/img/n.png)

\[c43\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), Martin Danelljan, [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Linbo He](https://dblp.org/pid/26/741.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Alexander G. Hauptmann](https://dblp.org/pid/h/AlexanderGHauptmann.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Álvaro García-Martín](https://dblp.org/pid/39/1542.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Anton Varfolomieiev](https://dblp.org/pid/188/7504.html), [Awet Haileslassie Gebrehiwot](https://dblp.org/pid/284/2554.html), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Bing Li](https://dblp.org/pid/13/2692-1.html), [Chen Qian](https://dblp.org/pid/70/3604-6.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Fredrik Gustafsson](https://dblp.org/pid/394/4497.html), [Gian Luca Foresti](https://dblp.org/pid/93/5522.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Haojie Zhao](https://dblp.org/pid/216/7590.html), [Haoran Bai](https://dblp.org/pid/235/9510.html), [Hari Chandana Kuchibhotla](https://dblp.org/pid/284/2570.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Hossein Ghanei-Yakhdan](https://dblp.org/pid/188/5964.html), [Houqiang Li](https://dblp.org/pid/59/7017.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Javad Khaghani](https://dblp.org/pid/233/0334.html), [Jesús Bescós](https://dblp.org/pid/97/2333.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Jianlong Fu](https://dblp.org/pid/83/8692.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Jingtao Xu](https://dblp.org/pid/119/1746.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Junhyun Lee](https://dblp.org/pid/155/8661.html), [Kaicheng Yu](https://dblp.org/pid/198/0861.html), [Kaiwen Liu](https://dblp.org/pid/231/4262.html), [Kang Yang](https://dblp.org/pid/86/8501.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Li Cheng](https://dblp.org/pid/13/4938-1.html), [Li Zhang](https://dblp.org/pid/89/5992-40.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Luca Bertinetto](https://dblp.org/pid/154/1351.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Ning Wang](https://dblp.org/pid/46/2005-20.html), [Pengyu Zhang](https://dblp.org/pid/33/4816.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Qiang Wang](https://dblp.org/pid/64/5630-51.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rama Krishna Sai Subrahmanyam Gorthi](https://dblp.org/pid/45/7595.html), [Seokeon Choi](https://dblp.org/pid/214/2200.html), [Seyed Mojtaba Marvasti-Zadeh](https://dblp.org/pid/188/6262.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Shohreh Kasaei](https://dblp.org/pid/78/5062.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Shuhao Chen](https://dblp.org/pid/43/2127.html), [Thomas B. Schön](https://dblp.org/pid/85/4891.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Weiming Hu](https://dblp.org/pid/41/6824-4.html), [Wengang Zhou](https://dblp.org/pid/22/4544-1.html), [Xi Qiu](https://dblp.org/pid/115/5698.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Xiao-Jun Wu](https://dblp.org/pid/13/5168-1.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Yingming Wang](https://dblp.org/pid/59/605.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuncon Yao](https://dblp.org/pid/284/2556.html), [Yunsung Lee](https://dblp.org/pid/227/9311.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Zezhou Wang](https://dblp.org/pid/204/1179.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhijun Mai](https://dblp.org/pid/247/9401.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Zhirong Wu](https://dblp.org/pid/147/5025.html), [Ziang Ma](https://dblp.org/pid/165/9621.html):

The Eighth Visual Object Tracking VOT2020 Challenge Results. [ECCV Workshops (5)2020](https://dblp.org/db/conf/eccv/eccv2020-w5.html#conf/eccv/KristanLMFPKDZL20): 547-601
- ![](https://dblp.org/img/n.png)

\[c42\]
[Xiankai Lu](https://dblp.org/pid/153/2122.html), [Wenguan Wang](https://dblp.org/pid/145/1078.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Tianfei Zhou](https://dblp.org/pid/150/6710.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianbing Shen](https://dblp.org/pid/38/5435.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Video Object Segmentation with Episodic Graph Memory Networks. [ECCV (3)2020](https://dblp.org/db/conf/eccv/eccv2020-3.html#conf/eccv/LuWDZSG20): 661-679
- ![](https://dblp.org/img/n.png)

\[c41\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

SRFlow: Learning the Super-Resolution Space with Normalizing Flow. [ECCV (5)2020](https://dblp.org/db/conf/eccv/eccv2020-5.html#conf/eccv/LugmayrDGT20): 715-732
- ![](https://dblp.org/img/n.png)

\[c40\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), Martin Danelljan, [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning What to Learn for Video Object Segmentation. [ECCV (2)2020](https://dblp.org/db/conf/eccv/eccv2020-2.html#conf/eccv/BhatLDRFGT20): 777-794
- ![](https://dblp.org/img/n.png)

\[c39\]
[Alexandre Carlier](https://dblp.org/pid/271/0428.html), Martin Danelljan, [Alexandre Alahi](https://dblp.org/pid/48/3455.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

DeepSVG: A Hierarchical Generative Network for Vector Graphics Animation. [NeurIPS2020](https://dblp.org/db/conf/nips/neurips2020.html#conf/nips/CarlierDAT20)
- ![](https://dblp.org/img/n.png)

\[c38\]
[Prune Truong](https://dblp.org/pid/247/5738.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

GOCor: Bringing Globally Optimized Correspondence Volumes into Your Neural Network. [NeurIPS2020](https://dblp.org/db/conf/nips/neurips2020.html#conf/nips/TruongDGT20)
- ![](https://dblp.org/img/n.png)

\[i40\]
[Andreas Robinson](https://dblp.org/pid/158/5786.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Learning Fast and Robust Target Models for Video Object Segmentation. [CoRRabs/2003.00908](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-00908) (2020)
- ![](https://dblp.org/img/n.png)

\[i39\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Know Your Surroundings: Exploiting Scene Information for Object Tracking. [CoRRabs/2003.11014](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-11014) (2020)
- ![](https://dblp.org/img/n.png)

\[i38\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), Martin Danelljan, [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Learning What to Learn for Video Object Segmentation. [CoRRabs/2003.11540](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-11540) (2020)
- ![](https://dblp.org/img/n.png)

\[i37\]
Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Probabilistic Regression for Visual Tracking. [CoRRabs/2003.12565](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-12565) (2020)
- ![](https://dblp.org/img/n.png)

\[i36\]
[Tiancai Wang](https://dblp.org/pid/179/0530.html), [Tong Yang](https://dblp.org/pid/44/7710-5.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Xiangyu Zhang](https://dblp.org/pid/95/3760-5.html), [Jian Sun](https://dblp.org/pid/68/4942-1.html):

Learning Human-Object Interaction Detection using Interaction Points. [CoRRabs/2003.14023](https://dblp.org/db/journals/corr/corr2003.html#journals/corr/abs-2003-14023) (2020)
- ![](https://dblp.org/img/n.png)

\[i35\]
[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html), [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

How to Train Your Energy-Based Model for Regression. [CoRRabs/2005.01698](https://dblp.org/db/journals/corr/corr2005.html#journals/corr/abs-2005-01698) (2020)
- ![](https://dblp.org/img/n.png)

\[i34\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html), [Namhyuk Ahn](https://dblp.org/pid/217/1998.html), [Dongwoon Bai](https://dblp.org/pid/07/2673.html), [Jie Cai](https://dblp.org/pid/95/3916-1.html), [Yun Cao](https://dblp.org/pid/40/2407-2.html), [Junyang Chen](https://dblp.org/pid/196/7893.html), [Kaihua Cheng](https://dblp.org/pid/264/5745.html), [Se Young Chun](https://dblp.org/pid/85/2542.html), [Wei Deng](https://dblp.org/pid/69/508.html), [Mostafa El-Khamy](https://dblp.org/pid/00/4303.html), [Chiu Man Ho](https://dblp.org/pid/228/8363.html), [Xiaozhong Ji](https://dblp.org/pid/237/9544.html), [Amin Kheradmand](https://dblp.org/pid/93/9199.html), [Gwantae Kim](https://dblp.org/pid/264/5954.html), [Hanseok Ko](https://dblp.org/pid/67/5314.html), [Kanghyu Lee](https://dblp.org/pid/218/1511.html), [Jungwon Lee](https://dblp.org/pid/87/381.html), [Hao Li](https://dblp.org/pid/17/5705-58.html), [Ziluan Liu](https://dblp.org/pid/158/4864.html), [Zhi-Song Liu](https://dblp.org/pid/144/8750.html), [Shuai Liu](https://dblp.org/pid/76/5789-0009.html), [Yunhua Lu](https://dblp.org/pid/45/2957.html), [Zibo Meng](https://dblp.org/pid/126/8042.html), [Pablo Navarrete Michelini](https://dblp.org/pid/63/1474.html), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Kalpesh Prajapati](https://dblp.org/pid/264/5768.html), [Haoyu Ren](https://dblp.org/pid/53/8616.html), [Yonghyeok Seo](https://dblp.org/pid/227/2546.html), [Wan-Chi Siu](https://dblp.org/pid/61/5203.html), [Kyung-Ah Sohn](https://dblp.org/pid/65/3835.html), [Ying Tai](https://dblp.org/pid/158/1384.html), [Rao Muhammad Umer](https://dblp.org/pid/248/9258.html), [Shuangquan Wang](https://dblp.org/pid/23/5003.html), [Huibing Wang](https://dblp.org/pid/150/0713.html), [Timothy Haoning Wu](https://dblp.org/pid/264/5802-1.html), [Haoning Wu](https://dblp.org/pid/264/5802-1.html), [Biao Yang](https://dblp.org/pid/26/103.html), [Fuzhi Yang](https://dblp.org/pid/264/5783.html), [Jaejun Yoo](https://dblp.org/pid/141/8878-1.html), [Tongtong Zhao](https://dblp.org/pid/191/5253.html), [Yuanbo Zhou](https://dblp.org/pid/262/5471.html), [Haijie Zhuo](https://dblp.org/pid/209/2325.html), [Ziyao Zong](https://dblp.org/pid/264/5589.html), [Xueyi Zou](https://dblp.org/pid/150/8081.html):

NTIRE 2020 Challenge on Real-World Image Super-Resolution: Methods and Results. [CoRRabs/2005.01996](https://dblp.org/db/journals/corr/corr2005.html#journals/corr/abs-2005-01996) (2020)
- ![](https://dblp.org/img/n.png)

\[i33\]
[Dario Fuoli](https://dblp.org/pid/260/3093.html), [Zhiwu Huang](https://dblp.org/pid/47/7711.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html), [Hua Wang](https://dblp.org/pid/33/3535-15.html), [Longcun Jin](https://dblp.org/pid/51/7090.html), [Dewei Su](https://dblp.org/pid/249/5714.html), [Jing Liu](https://dblp.org/pid/72/2590-31.html), [Jaehoon Lee](https://dblp.org/pid/95/386.html), [Michal Kudelski](https://dblp.org/pid/50/6979.html), [Lukasz Bala](https://dblp.org/pid/264/5872.html), [Dmitry Hrybov](https://dblp.org/pid/264/5801.html), [Marcin Mozejko](https://dblp.org/pid/228/6840.html), [Muchen Li](https://dblp.org/pid/122/2666.html), [Siyao Li](https://dblp.org/pid/163/8053.html), [Bo Pang](https://dblp.org/pid/16/6344-3.html), [Cewu Lu](https://dblp.org/pid/96/10571.html), [Chao Li](https://dblp.org/pid/66/190-34.html), [Dongliang He](https://dblp.org/pid/167/0539.html), [Fu Li](https://dblp.org/pid/37/4556-3.html), [Shilei Wen](https://dblp.org/pid/159/2939.html):

NTIRE 2020 Challenge on Video Quality Mapping: Methods and Results. [CoRRabs/2005.02291](https://dblp.org/db/journals/corr/corr2005.html#journals/corr/abs-2005-02291) (2020)
- ![](https://dblp.org/img/n.png)

\[i32\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

SRFlow: Learning the Super-Resolution Space with Normalizing Flow. [CoRRabs/2006.14200](https://dblp.org/db/journals/corr/corr2006.html#journals/corr/abs-2006-14200) (2020)
- ![](https://dblp.org/img/n.png)

\[i31\]
[Yawei Li](https://dblp.org/pid/32/6740-1.html), [Wen Li](https://dblp.org/pid/06/721-1.html), Martin Danelljan, [Kai Zhang](https://dblp.org/pid/55/957-8.html), [Shuhang Gu](https://dblp.org/pid/126/1028.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

The Heterogeneity Hypothesis: Finding Layer-Wise Dissimilated Network Architecture. [CoRRabs/2006.16242](https://dblp.org/db/journals/corr/corr2006.html#journals/corr/abs-2006-16242) (2020)
- ![](https://dblp.org/img/n.png)

\[i30\]
[Xiankai Lu](https://dblp.org/pid/153/2122.html), [Wenguan Wang](https://dblp.org/pid/145/1078.html), Martin Danelljan, [Tianfei Zhou](https://dblp.org/pid/150/6710.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Video Object Segmentation with Episodic Graph Memory Networks. [CoRRabs/2007.07020](https://dblp.org/db/journals/corr/corr2007.html#journals/corr/abs-2007-07020) (2020)
- ![](https://dblp.org/img/n.png)

\[i29\]
[Alexandre Carlier](https://dblp.org/pid/271/0428.html), Martin Danelljan, [Alexandre Alahi](https://dblp.org/pid/48/3455.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

DeepSVG: A Hierarchical Generative Network for Vector Graphics Animation. [CoRRabs/2007.11301](https://dblp.org/db/journals/corr/corr2007.html#journals/corr/abs-2007-11301) (2020)
- ![](https://dblp.org/img/n.png)

\[i28\]
[Kai Zhang](https://dblp.org/pid/55/957-8.html), Martin Danelljan, [Yawei Li](https://dblp.org/pid/32/6740-1.html), [Radu Timofte](https://dblp.org/pid/24/8616.html), [Jie Liu](https://dblp.org/pid/03/2134-40.html), [Jie Tang](https://dblp.org/pid/181/2702-6.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Yu Zhu](https://dblp.org/pid/38/5267-4.html), [Xiangyu He](https://dblp.org/pid/173/4661.html), [Wenjie Xu](https://dblp.org/pid/25/1820.html), [Chenghua Li](https://dblp.org/pid/70/10190.html), [Cong Leng](https://dblp.org/pid/147/9188.html), [Jian Cheng](https://dblp.org/pid/14/6145-1.html), [Guangyang Wu](https://dblp.org/pid/254/8240.html), [Wenyi Wang](https://dblp.org/pid/79/2722-5.html), [Xiaohong Liu](https://dblp.org/pid/95/2454-1.html), [Hengyuan Zhao](https://dblp.org/pid/260/3042.html), [Xiangtao Kong](https://dblp.org/pid/274/3262.html), [Jingwen He](https://dblp.org/pid/14/2195.html), [Yu Qiao](https://dblp.org/pid/q/YuQiao1.html), [Chao Dong](https://dblp.org/pid/16/1278-5.html), [Jiangtao Zhang](https://dblp.org/pid/38/8912.html), [Maitreya Suin](https://dblp.org/pid/254/1457.html), [Kuldeep Purohit](https://dblp.org/pid/191/2655.html), [A. N. Rajagopalan](https://dblp.org/pid/73/3473.html), [Xiaochuan Li](https://dblp.org/pid/10/8076-1.html), [Zhiqiang Lang](https://dblp.org/pid/238/0425.html), [Jiangtao Nie](https://dblp.org/pid/252/4948.html), [Wei Wei](https://dblp.org/pid/24/4105-8.html), [Lei Zhang](https://dblp.org/pid/64/5666-6.html), [Abdul Muqeet](https://dblp.org/pid/245/0047.html), [Jiwon Hwang](https://dblp.org/pid/157/7832.html), [Subin Yang](https://dblp.org/pid/144/2910.html), [Jung Heum Kang](https://dblp.org/pid/274/1655.html), [Sung-Ho Bae](https://dblp.org/pid/76/2068.html), [Yongwoo Kim](https://dblp.org/pid/90/8739.html), [Liang Chen](https://dblp.org/pid/01/5394.html), [Xiaotong Luo](https://dblp.org/pid/169/3960.html), [Yanyun Qu](https://dblp.org/pid/03/3500.html), [Geun-Woo Jeon](https://dblp.org/pid/274/3180.html), [Jun-Ho Choi](https://dblp.org/pid/139/4714.html), [Jun-Hyuk Kim](https://dblp.org/pid/193/6547.html), [Jong-Seok Lee](https://dblp.org/pid/70/1152.html), [Steven Marty](https://dblp.org/pid/274/2797.html), [Éric Marty](https://dblp.org/pid/222/9632.html), [Dongliang Xiong](https://dblp.org/pid/192/3737.html), [Siang Chen](https://dblp.org/pid/260/2691.html), [Lin Zha](https://dblp.org/pid/133/3991.html), [Jiande Jiang](https://dblp.org/pid/264/5784.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html), [Wen Lu](https://dblp.org/pid/31/6140-4.html), [Haicheng Wang](https://dblp.org/pid/150/4188.html), [Vineeth Bhaskara](https://dblp.org/pid/197/6505.html), [Alex Levinshtein](https://dblp.org/pid/40/6950.html), [Stavros Tsogkas](https://dblp.org/pid/119/1444.html), [Allan D. Jepson](https://dblp.org/pid/93/4241.html), [Xiangzhen Kong](https://dblp.org/pid/80/531.html), [Tongtong Zhao](https://dblp.org/pid/191/5253.html), [Shanshan Zhao](https://dblp.org/pid/02/7781-3.html), [Hrishikesh P. S](https://dblp.org/pid/264/5454.html), [Densen Puthussery](https://dblp.org/pid/264/5624.html), [C. Victor Jiji](https://dblp.org/pid/75/3033.html), [Nan Nan](https://dblp.org/pid/26/3712.html), [Shuai Liu](https://dblp.org/pid/76/5789-0009.html), [Jie Cai](https://dblp.org/pid/95/3916-1.html), [Zibo Meng](https://dblp.org/pid/126/8042.html), [Jiaming Ding](https://dblp.org/pid/274/2850.html), [Chiu Man Ho](https://dblp.org/pid/228/8363.html), [Xuehui Wang](https://dblp.org/pid/78/6531.html), [Qiong Yan](https://dblp.org/pid/122/4814.html), [Yuzhi Zhao](https://dblp.org/pid/240/3833.html), [Long Chen](https://dblp.org/pid/64/5725-5.html), [Long Sun](https://dblp.org/pid/151/4095.html), [Wenhao Wang](https://dblp.org/pid/57/9813.html), [Zhenbing Liu](https://dblp.org/pid/19/7578.html), [Rushi Lan](https://dblp.org/pid/44/8845.html), [Rao Muhammad Umer](https://dblp.org/pid/248/9258.html), [Christian Micheloni](https://dblp.org/pid/28/38.html):

AIM 2020 Challenge on Efficient Super-Resolution: Methods and Results. [CoRRabs/2009.06943](https://dblp.org/db/journals/corr/corr2009.html#journals/corr/abs-2009-06943) (2020)
- ![](https://dblp.org/img/n.png)

\[i27\]
[Prune Truong](https://dblp.org/pid/247/5738.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

GOCor: Bringing Globally Optimized Correspondence Volumes into Your Neural Network. [CoRRabs/2009.07823](https://dblp.org/db/journals/corr/corr2009.html#journals/corr/abs-2009-07823) (2020)
- ![](https://dblp.org/img/n.png)

\[i26\]
[Ardhendu Shekhar Tripathi](https://dblp.org/pid/141/9949.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Few-Shot Classification By Few-Iteration Meta-Learning. [CoRRabs/2010.00511](https://dblp.org/db/journals/corr/corr2010.html#journals/corr/abs-2010-00511) (2020)
- ![](https://dblp.org/img/n.png)

\[i25\]
[Joakim Johnander](https://dblp.org/pid/202/2479.html), [Emil Brissman](https://dblp.org/pid/230/7851.html), Martin Danelljan, [Michael Felsberg](https://dblp.org/pid/00/78.html):

Learning Video Instance Segmentation with Recurrent Graph Neural Networks. [CoRRabs/2012.03911](https://dblp.org/db/journals/corr/corr2012.html#journals/corr/abs-2012-03911) (2020)
- ![](https://dblp.org/img/n.png)

\[i24\]
[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html), Martin Danelljan, [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

Accurate 3D Object Detection using Energy-Based Models. [CoRRabs/2012.04634](https://dblp.org/db/journals/corr/corr2012.html#journals/corr/abs-2012-04634) (2020)
- ![](https://dblp.org/img/n.png)

\[i23\]
[Shipra Jain](https://dblp.org/pid/143/8973.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html):

Scaling Semantic Segmentation Beyond 1K Classes on a Single GPU. [CoRRabs/2012.07489](https://dblp.org/db/journals/corr/corr2012.html#journals/corr/abs-2012-07489) (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j3\]
Martin Danelljan![](https://dblp.org/img/orcid-mark.12x12.png), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Susanna Gladh](https://dblp.org/pid/192/1542.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Deep motion and appearance cues for visual tracking. [Pattern Recognit. Lett.124](https://dblp.org/db/journals/prl/prl124.html#journals/prl/DanelljanBGKF19): 74-81 (2019)
- ![](https://dblp.org/img/n.png)

\[j2\]
[Lichao Zhang](https://dblp.org/pid/126/8027-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Abel Gonzalez-Garcia](https://dblp.org/pid/156/0213.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Joost van de Weijer](https://dblp.org/pid/67/3379.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Synthetic Data Generation for End-to-End Thermal Infrared Tracking. [IEEE Trans. Image Process.28(4)](https://dblp.org/db/journals/tip/tip28.html#journals/tip/ZhangGWDK19): 1837-1850 (2019)
- ![](https://dblp.org/img/n.png)

\[c37\]
[Ardhendu Shekhar Tripathi](https://dblp.org/pid/141/9949.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Tracking the Known and the Unknown by Leveraging Semantic Information. [BMVC2019](https://dblp.org/db/conf/bmvc/bmvc2019.html#conf/bmvc/TripathiDGT19): Article 292
- ![](https://dblp.org/img/n.png)

\[c36\]
Martin Danelljan, [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

ATOM: Accurate Tracking by Overlap Maximization. [CVPR2019](https://dblp.org/db/conf/cvpr/cvpr2019.html#conf/cvpr/DanelljanBKF19): 4660-4669
- ![](https://dblp.org/img/n.png)

\[c35\]
[Joakim Johnander](https://dblp.org/pid/202/2479.html), Martin Danelljan, [Emil Brissman](https://dblp.org/pid/230/7851.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Generative Appearance Model for End-To-End Video Object Segmentation. [CVPR2019](https://dblp.org/db/conf/cvpr/cvpr2019.html#conf/cvpr/JohnanderDBKF19): 8953-8962
- ![](https://dblp.org/img/n.png)

\[c34\]
[Lichao Zhang](https://dblp.org/pid/126/8027-1.html), [Abel Gonzalez-Garcia](https://dblp.org/pid/156/0213.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html)![](https://dblp.org/img/orcid-mark.12x12.png), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning the Model Update for Siamese Trackers. [ICCV2019](https://dblp.org/db/conf/iccv/iccv2019.html#conf/iccv/ZhangGWDK19): 4009-4018
- ![](https://dblp.org/img/n.png)

\[c33\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning Discriminative Model Prediction for Tracking. [ICCV2019](https://dblp.org/db/conf/iccv/iccv2019.html#conf/iccv/BhatDGT19): 6181-6190
- ![](https://dblp.org/img/n.png)

\[c32\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Amanda Berg](https://dblp.org/pid/163/4511.html), [Linyu Zheng](https://dblp.org/pid/210/2313.html), [Litu Rout](https://dblp.org/pid/206/6445.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Luca Bertinetto](https://dblp.org/pid/154/1351.html), Martin Danelljan, [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Meng Ni](https://dblp.org/pid/174/2809.html), [Min Young Kim](https://dblp.org/pid/34/5733-3.html), [Ming Tang](https://dblp.org/pid/73/4373-1.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Abdelrahman Eldesokey](https://dblp.org/pid/154/9080.html), [Naveen Paluru](https://dblp.org/pid/260/3261.html), [Niki Martinel](https://dblp.org/pid/56/10105.html), [Pengfei Xu](https://dblp.org/pid/04/383-13.html), [Pengfei Zhang](https://dblp.org/pid/58/4525-5.html), [Pengkun Zheng](https://dblp.org/pid/260/2752.html), [Pengyu Zhang](https://dblp.org/pid/33/4816.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Qi Zhang](https://dblp.org/pid/52/323.html), [Qiang Wang](https://dblp.org/pid/64/5630-51.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Radu Timofte](https://dblp.org/pid/24/8616.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Rama Krishna Sai Subrahmanyam Gorthi](https://dblp.org/pid/45/7595.html), [Richard M. Everson](https://dblp.org/pid/07/6331.html), [Ruize Han](https://dblp.org/pid/205/4022.html), [Ruohan Zhang](https://dblp.org/pid/160/9929.html), [Shan You](https://dblp.org/pid/179/2548.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Shengwei Zhao](https://dblp.org/pid/155/9654.html), [Shihu Li](https://dblp.org/pid/242/1376.html), [Shikun Li](https://dblp.org/pid/255/0117.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Shuai Bai](https://dblp.org/pid/208/8033.html), [Shuosen Guan](https://dblp.org/pid/245/8954.html), [Tengfei Xing](https://dblp.org/pid/82/1822.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Tianyu Yang](https://dblp.org/pid/120/8076-3.html), [Ting Zhang](https://dblp.org/pid/06/5919-6.html), [Tomás Vojír](https://dblp.org/pid/142/5749.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Weiming Hu](https://dblp.org/pid/41/6824.html), [Weizhao Wang](https://dblp.org/pid/39/2359.html), [Abel Gonzalez-Garcia](https://dblp.org/pid/156/0213.html), [Wenjie Tang](https://dblp.org/pid/87/7879.html), [Wenjun Zeng](https://dblp.org/pid/57/145.html), [Wenyu Liu](https://dblp.org/pid/42/4110-1.html), [Xi Chen](https://dblp.org/pid/16/3283.html), [Xi Qiu](https://dblp.org/pid/115/5698.html), [Xiang Bai](https://dblp.org/pid/59/2741.html), [Xiao-Jun Wu](https://dblp.org/pid/13/5168-1.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Xier Chen](https://dblp.org/pid/260/3035.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xing Sun](https://dblp.org/pid/90/2719-1.html), [Xingyu Chen](https://dblp.org/pid/59/7651.html), [Xinmei Tian](https://dblp.org/pid/03/5204-1.html), [Xu Tang](https://dblp.org/pid/123/7064.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yan Huang](https://dblp.org/pid/75/6434-8.html), [Yanan Chen](https://dblp.org/pid/78/10104.html), [Yanchao Lian](https://dblp.org/pid/253/3698.html), [Yang Gu](https://dblp.org/pid/01/5858.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Andong Lu](https://dblp.org/pid/245/2878.html), [Yanjie Chen](https://dblp.org/pid/02/7548.html), [Yi Zhang](https://dblp.org/pid/64/6544.html), [Yinda Xu](https://dblp.org/pid/254/1072.html), [Yingming Wang](https://dblp.org/pid/59/605.html), [Yingping Li](https://dblp.org/pid/172/4240.html), [Yu Zhou](https://dblp.org/pid/36/2728-16.html), [Yuan Dong](https://dblp.org/pid/66/875.html), [Yufei Xu](https://dblp.org/pid/43/7400.html), [Yunhua Zhang](https://dblp.org/pid/60/9627.html), [Yunkun Li](https://dblp.org/pid/260/2938.html), [Anfeng He](https://dblp.org/pid/188/1205.html), [Zeyu Wang](https://dblp.org/pid/132/7882-8.html), [Zhao Luo](https://dblp.org/pid/187/1232.html), [Zhaoliang Zhang](https://dblp.org/pid/81/7883.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Zhichao Song](https://dblp.org/pid/169/4022.html), [Zhihao Chen](https://dblp.org/pid/50/505-4.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Zhirong Wu](https://dblp.org/pid/147/5025.html), [Zhiwei Xiong](https://dblp.org/pid/54/6827.html), [Zhongjian Huang](https://dblp.org/pid/251/0619.html), [Anton Varfolomieiev](https://dblp.org/pid/188/7504.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhu Teng](https://dblp.org/pid/132/2247.html), [Zihan Ni](https://dblp.org/pid/187/9123.html), [Antoni B. Chan](https://dblp.org/pid/55/5814.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Ardhendu Shekhar Tripathi](https://dblp.org/pid/141/9949.html), [Arnold W. M. Smeulders](https://dblp.org/pid/15/5400.html), [Bala Suraj Pedasingu](https://dblp.org/pid/260/3120.html), [Bao Xin Chen](https://dblp.org/pid/153/1895.html), [Baopeng Zhang](https://dblp.org/pid/22/3524.html), [Baoyuan Wu](https://dblp.org/pid/73/7781.html), [Bi Li](https://dblp.org/pid/174/9761.html), [Bin He](https://dblp.org/pid/78/4523.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Bing Bai](https://dblp.org/pid/54/5260.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Bing Li](https://dblp.org/pid/13/2692-1.html), [Bo Li](https://dblp.org/pid/50/3402-114.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Chao Ma](https://dblp.org/pid/79/1552-4.html), [Chen Fang](https://dblp.org/pid/60/2548.html), [Chen Qian](https://dblp.org/pid/70/3604-1.html), [Cheng Chen](https://dblp.org/pid/10/217.html), [Chenglong Li](https://dblp.org/pid/83/7820-2.html), [Chengquan Zhang](https://dblp.org/pid/163/1795.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chong Luo](https://dblp.org/pid/79/3712-1.html), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Dacheng Tao](https://dblp.org/pid/46/3391.html), [Deepak Gupta](https://dblp.org/pid/65/2751.html), [Dejia Song](https://dblp.org/pid/260/2975.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Efstratios Gavves](https://dblp.org/pid/03/8693.html), [Eunu Yi](https://dblp.org/pid/260/3303.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Fangyi Zhang](https://dblp.org/pid/10/8496.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Fei Zhao](https://dblp.org/pid/21/6180.html), [George De Ath](https://dblp.org/pid/220/3209.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Guoxuan Li](https://dblp.org/pid/121/6265.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Hao Du](https://dblp.org/pid/13/6441-6.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Haojie Zhao](https://dblp.org/pid/216/7590.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Ho Min Jung](https://dblp.org/pid/36/5839.html), [Hongliang Bai](https://dblp.org/pid/34/5268.html), [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jiakun Li](https://dblp.org/pid/69/7673.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Jianlong Fu](https://dblp.org/pid/83/8692.html), [Jie Chen](https://dblp.org/pid/92/6289.html), [Jie Gao](https://dblp.org/pid/181/2794.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Jin Tang](https://dblp.org/pid/56/4951-1.html), [Jing Li](https://dblp.org/pid/l/JingLi36.html), [Jingjing Wu](https://dblp.org/pid/27/2384.html), [Jingtuo Liu](https://dblp.org/pid/164/5911.html), [Jinqiao Wang](https://dblp.org/pid/67/4236.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jinqing Qi](https://dblp.org/pid/09/287.html), [Jinyue Zhang](https://dblp.org/pid/10/2874.html), [John K. Tsotsos](https://dblp.org/pid/t/JohnKTsotsos.html), [Jong Hyuk Lee](https://dblp.org/pid/39/2874.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Junfei Zhuang](https://dblp.org/pid/213/4212.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Kangkang Wang](https://dblp.org/pid/03/9859.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Lei Chen](https://dblp.org/pid/09/3666.html), [Lei Liu](https://dblp.org/pid/21/2715-49.html), [Leida Guo](https://dblp.org/pid/249/8242.html), [Li Zhang](https://dblp.org/pid/89/5992-40.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lichao Zhang](https://dblp.org/pid/126/8027-1.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Lijun Zhou](https://dblp.org/pid/14/1719.html):

The Seventh Visual Object Tracking VOT2019 Challenge Results. [ICCV Workshops2019](https://dblp.org/db/conf/iccvw/iccvw2019.html#conf/iccvw/KristanBZRGBDDN19): 2206-2241
- ![](https://dblp.org/img/n.png)

\[c31\]
[Lichao Zhang](https://dblp.org/pid/126/8027-1.html), Martin Danelljan, [Abel Gonzalez-Garcia](https://dblp.org/pid/156/0213.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Multi-Modal Fusion for End-to-End RGB-T Tracking. [ICCV Workshops2019](https://dblp.org/db/conf/iccvw/iccvw2019.html#conf/iccvw/ZhangDGWK19): 2252-2261
- ![](https://dblp.org/img/n.png)

\[c30\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Unsupervised Learning for Real-World Super-Resolution. [ICCV Workshops2019](https://dblp.org/db/conf/iccvw/iccvw2019.html#conf/iccvw/LugmayrDT19): 3408-3416
- ![](https://dblp.org/img/n.png)

\[c29\]
[Shuhang Gu](https://dblp.org/pid/126/1028.html), [Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Manuel Fritsche](https://dblp.org/pid/228/6850.html), [Julien Lamour](https://dblp.org/pid/260/3181.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

DIV8K: DIVerse 8K Resolution Image Dataset. [ICCV Workshops2019](https://dblp.org/db/conf/iccvw/iccvw2019.html#conf/iccvw/GuLDFLT19): 3512-3516
- ![](https://dblp.org/img/n.png)

\[c28\]
[Shuhang Gu](https://dblp.org/pid/126/1028.html), [Hanwen Liu](https://dblp.org/pid/178/1112.html), [Dan Zhu](https://dblp.org/pid/50/6054.html), [Tangxin Xie](https://dblp.org/pid/255/7347.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xin Yang](https://dblp.org/pid/44/1152-9.html), [Chen Zhu](https://dblp.org/pid/59/10522.html), [Jia Yu](https://dblp.org/pid/86/3457-18.html), [Wenyu Sun](https://dblp.org/pid/92/6021.html), [Xin Tao](https://dblp.org/pid/98/7443-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zijun Deng](https://dblp.org/pid/222/7952.html), [Liying Lu](https://dblp.org/pid/152/5445.html), Martin Danelljan, [Wenbo Li](https://dblp.org/pid/51/3185-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Taian Guo](https://dblp.org/pid/254/9326.html), [Xiaoyong Shen](https://dblp.org/pid/71/11418.html), [Xuemiao Xu](https://dblp.org/pid/74/6722.html), [Yu-Wing Tai](https://dblp.org/pid/40/566.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiaya Jia](https://dblp.org/pid/31/5649.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Peng Yi](https://dblp.org/pid/98/1202-2.html), [Zhongyuan Wang](https://dblp.org/pid/84/6394-1.html), [Kui Jiang](https://dblp.org/pid/124/2034.html), [Junjun Jiang](https://dblp.org/pid/119/0230.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jiayi Ma](https://dblp.org/pid/96/9989.html), [Zhi-Song Liu](https://dblp.org/pid/144/8750.html), [Li-Wen Wang](https://dblp.org/pid/33/10711.html), [Chu-Tak Li](https://dblp.org/pid/235/0657.html), [Wan-Chi Siu](https://dblp.org/pid/61/5203.html), [Yui-Lam Chan](https://dblp.org/pid/04/2096.html), [Ruofan Zhou](https://dblp.org/pid/205/3902.html), [Majed El Helou](https://dblp.org/pid/214/9598.html), [Kuldeep Purohit](https://dblp.org/pid/191/2655.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Praveen Kandula](https://dblp.org/pid/228/6711.html), [Muhammad Haris](https://dblp.org/pid/142/1614-2.html), [Maitreya Suin](https://dblp.org/pid/254/1457.html), [A. N. Rajagopalan](https://dblp.org/pid/73/3473.html), [Kazutoshi Akita](https://dblp.org/pid/260/3239.html), [Greg Shakhnarovich](https://dblp.org/pid/17/1926.html), [Norimichi Ukita](https://dblp.org/pid/46/5881.html), [Pablo Navarrete Michelini](https://dblp.org/pid/63/1474.html), [Wenbin Chen](https://dblp.org/pid/181/2912.html):

AIM 2019 Challenge on Image Extreme Super-Resolution: Methods and Results. [ICCV Workshops2019](https://dblp.org/db/conf/iccvw/iccvw2019.html#conf/iccvw/GuLZXYZYSTDLDLG19): 3556-3564
- ![](https://dblp.org/img/n.png)

\[c27\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), [Nam Hyung Joon](https://dblp.org/pid/254/1586.html), [Yu Seung Won](https://dblp.org/pid/254/1498.html), [Guisik Kim](https://dblp.org/pid/197/6673.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dokyeong Kwon](https://dblp.org/pid/242/3552.html), [Chih-Chung Hsu](https://dblp.org/pid/35/547.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chia-Hsiang Lin](https://dblp.org/pid/71/660.html), [Yuanfei Huang](https://dblp.org/pid/207/5397.html), [Xiaopeng Sun](https://dblp.org/pid/74/9057.html), [Wen Lu](https://dblp.org/pid/31/6140-4.html), [Jie Li](https://dblp.org/pid/17/2703-1.html), Martin Danelljan, [Xinbo Gao](https://dblp.org/pid/99/4522.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sefi Bell-Kligler](https://dblp.org/pid/249/2218.html), [Assaf Shocher](https://dblp.org/pid/211/8006.html), [Michal Irani](https://dblp.org/pid/04/3190.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Manuel Fritsche](https://dblp.org/pid/228/6850.html), [Shuhang Gu](https://dblp.org/pid/126/1028.html), [Kuldeep Purohit](https://dblp.org/pid/191/2655.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Praveen Kandula](https://dblp.org/pid/228/6711.html), [Maitreya Suin](https://dblp.org/pid/254/1457.html), [A. N. Rajagopalan](https://dblp.org/pid/73/3473.html):

AIM 2019 Challenge on Real-World Image Super-Resolution: Methods and Results. [ICCV Workshops2019](https://dblp.org/db/conf/iccvw/iccvw2019.html#conf/iccvw/LugmayrJWKKHLHS19): 3575-3583
- ![](https://dblp.org/img/n.png)

\[c26\]
[Sohyeong Kim](https://dblp.org/pid/184/5475.html), [Guanju Li](https://dblp.org/pid/251/5559.html), [Dario Fuoli](https://dblp.org/pid/260/3093.html), Martin Danelljan, [Zhiwu Huang](https://dblp.org/pid/47/7711.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shuhang Gu](https://dblp.org/pid/126/1028.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png):

The Vid3oC and IntVID Datasets for Video Super Resolution and Quality Mapping. [ICCV Workshops2019](https://dblp.org/db/conf/iccvw/iccvw2019.html#conf/iccvw/KimLFDHGT19): 3609-3616
- ![](https://dblp.org/img/n.png)

\[i22\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Radu Timofte](https://dblp.org/pid/24/8616.html):

Learning Discriminative Model Prediction for Tracking. [CoRRabs/1904.07220](https://dblp.org/db/journals/corr/corr1904.html#journals/corr/abs-1904-07220) (2019)
- ![](https://dblp.org/img/n.png)

\[i21\]
[Andreas Robinson](https://dblp.org/pid/158/5786.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Discriminative Online Learning for Fast Video Object Segmentation. [CoRRabs/1904.08630](https://dblp.org/db/journals/corr/corr1904.html#journals/corr/abs-1904-08630) (2019)
- ![](https://dblp.org/img/n.png)

\[i20\]
[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html), Martin Danelljan, [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

Evaluating Scalable Bayesian Deep Learning Methods for Robust Computer Vision. [CoRRabs/1906.01620](https://dblp.org/db/journals/corr/corr1906.html#journals/corr/abs-1906-01620) (2019)
- ![](https://dblp.org/img/n.png)

\[i19\]
[Lichao Zhang](https://dblp.org/pid/126/8027-1.html), [Abel Gonzalez-Garcia](https://dblp.org/pid/156/0213.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html):

Learning the Model Update for Siamese Trackers. [CoRRabs/1908.00855](https://dblp.org/db/journals/corr/corr1908.html#journals/corr/abs-1908-00855) (2019)
- ![](https://dblp.org/img/n.png)

\[i18\]
[Lichao Zhang](https://dblp.org/pid/126/8027-1.html), Martin Danelljan, [Abel Gonzalez-Garcia](https://dblp.org/pid/156/0213.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html):

Multi-Modal Fusion for End-to-End RGB-T Tracking. [CoRRabs/1908.11714](https://dblp.org/db/journals/corr/corr1908.html#journals/corr/abs-1908-11714) (2019)
- ![](https://dblp.org/img/n.png)

\[i17\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html):

Unsupervised Learning for Real-World Super-Resolution. [CoRRabs/1909.09629](https://dblp.org/db/journals/corr/corr1909.html#journals/corr/abs-1909-09629) (2019)
- ![](https://dblp.org/img/n.png)

\[i16\]
[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html), Martin Danelljan, [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Thomas B. Schön](https://dblp.org/pid/85/4891.html):

DCTD: Deep Conditional Target Densities for Accurate Regression. [CoRRabs/1909.12297](https://dblp.org/db/journals/corr/corr1909.html#journals/corr/abs-1909-12297) (2019)
- ![](https://dblp.org/img/n.png)

\[i15\]
[Andreas Lugmayr](https://dblp.org/pid/249/2710.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html), [Manuel Fritsche](https://dblp.org/pid/228/6850.html), [Shuhang Gu](https://dblp.org/pid/126/1028.html), [Kuldeep Purohit](https://dblp.org/pid/191/2655.html), [Praveen Kandula](https://dblp.org/pid/228/6711.html), [Maitreya Suin](https://dblp.org/pid/254/1457.html), [A. N. Rajagopalan](https://dblp.org/pid/73/3473.html), [Nam Hyung Joon](https://dblp.org/pid/254/1586.html), [Yu Seung Won](https://dblp.org/pid/254/1498.html), [Guisik Kim](https://dblp.org/pid/197/6673.html), [Dokyeong Kwon](https://dblp.org/pid/242/3552.html), [Chih-Chung Hsu](https://dblp.org/pid/35/547.html), [Chia-Hsiang Lin](https://dblp.org/pid/71/660.html), [Yuanfei Huang](https://dblp.org/pid/207/5397.html), [Xiaopeng Sun](https://dblp.org/pid/74/9057.html), [Wen Lu](https://dblp.org/pid/31/6140-4.html), [Jie Li](https://dblp.org/pid/17/2703-1.html), [Xinbo Gao](https://dblp.org/pid/99/4522.html), [Sefi Bell-Kligler](https://dblp.org/pid/249/2218.html):

AIM 2019 Challenge on Real-World Image Super-Resolution: Methods and Results. [CoRRabs/1911.07783](https://dblp.org/db/journals/corr/corr1911.html#journals/corr/abs-1911-07783) (2019)
- ![](https://dblp.org/img/n.png)

\[i14\]
[Prune Truong](https://dblp.org/pid/247/5738.html), Martin Danelljan, [Radu Timofte](https://dblp.org/pid/24/8616.html):

GLU-Net: Global-Local Universal Network for Dense Flow and Correspondences. [CoRRabs/1912.05524](https://dblp.org/db/journals/corr/corr1912.html#journals/corr/abs-1912-05524) (2019)
- 2018
- ![](https://dblp.org/img/n.png)

\[b1\]
Martin Danelljan![](https://dblp.org/img/orcid-mark.12x12.png):

Learning Convolution Operators for Visual Tracking. Linköping University, Sweden, 2018
- ![](https://dblp.org/img/n.png)

\[c25\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Combining Local and Global Models for Robust Re-detection. [AVSS2018](https://dblp.org/db/conf/avss/avss2018.html#conf/avss/BhatDKF18): 1-6
- ![](https://dblp.org/img/n.png)

\[c24\]
[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Per-Erik Forssén](https://dblp.org/pid/84/306.html), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Density Adaptive Point Set Registration. [CVPR2018](https://dblp.org/db/conf/cvpr/cvpr2018.html#conf/cvpr/LawinDKFF18): 3829-3837
- ![](https://dblp.org/img/n.png)

\[c23\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Tomás Vojír](https://dblp.org/pid/142/5749.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Abdelrahman Eldesokey](https://dblp.org/pid/154/9080.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Álvaro García-Martín](https://dblp.org/pid/39/1542.html), [Álvaro Iglesias-Arias](https://dblp.org/pid/234/0091.html), [A. Aydin Alatan](https://dblp.org/pid/08/4639.html), [Abel González-García](https://dblp.org/pid/156/0213.html), [Alfredo Petrosino](https://dblp.org/pid/20/3145.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Andrea Vedaldi](https://dblp.org/pid/99/2825.html), [Andrej Muhic](https://dblp.org/pid/119/0869.html), [Anfeng He](https://dblp.org/pid/188/1205.html), [Arnold W. M. Smeulders](https://dblp.org/pid/15/5400.html), [Asanka G. Perera](https://dblp.org/pid/231/9229.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bo Li](https://dblp.org/pid/50/3402-114.html), [Boyu Chen](https://dblp.org/pid/166/5205.html), [Changick Kim](https://dblp.org/pid/40/5999.html), [Changsheng Xu](https://dblp.org/pid/85/1301.html), [Changzhen Xiong](https://dblp.org/pid/14/965.html), [Cheng Tian](https://dblp.org/pid/76/8808.html), [Chong Luo](https://dblp.org/pid/79/3712-1.html), [Chong Sun](https://dblp.org/pid/56/2576.html), [Cong Hao](https://dblp.org/pid/129/2059.html), [Daijin Kim](https://dblp.org/pid/k/DaijinKim.html), [Deepak Mishra](https://dblp.org/pid/65/6758-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Deming Chen](https://dblp.org/pid/37/1234.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Dongyoon Wee](https://dblp.org/pid/234/0087.html), [Efstratios Gavves](https://dblp.org/pid/03/8693.html), [Erhan Gundogdu](https://dblp.org/pid/147/4597.html), [Erik Velasco-Salido](https://dblp.org/pid/213/4199.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Fan Yang](https://dblp.org/pid/29/3081-35.html), [Fei Zhao](https://dblp.org/pid/21/6180-8.html), [Feng Li](https://dblp.org/pid/92/2954-31.html), [Francesco Battistone](https://dblp.org/pid/167/1252.html), [George De Ath](https://dblp.org/pid/220/3209.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Gorthi R. K. Sai Subrahmanyam](https://dblp.org/pid/45/7595.html), [Guilherme Sousa Bastos](https://dblp.org/pid/166/2034.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Hamed Kiani Galoogahi](https://dblp.org/pid/119/0363.html), [Hankyeol Lee](https://dblp.org/pid/234/0073.html), [Haojie Li](https://dblp.org/pid/61/4041.html), [Haojie Zhao](https://dblp.org/pid/216/7590.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Honggang Zhang](https://dblp.org/pid/82/1228-2.html), [Horst Possegger](https://dblp.org/pid/135/4917.html), [Houqiang Li](https://dblp.org/pid/59/7017.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Hui Zhi](https://dblp.org/pid/46/1382.html), [Huiyun Li](https://dblp.org/pid/55/3543.html), [Hyemin Lee](https://dblp.org/pid/188/7676.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Isabela Drummond](https://dblp.org/pid/45/3169.html), [Jack Valmadre](https://dblp.org/pid/50/8535.html), [Jaime Spencer Martin](https://dblp.org/pid/234/0071.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Javaan Singh Chahl](https://dblp.org/pid/12/797.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jin Young Choi](https://dblp.org/pid/30/1428-2.html), [Jing Li](https://dblp.org/pid/l/JingLi36.html), [Jinqiao Wang](https://dblp.org/pid/67/4236.html), [Jinqing Qi](https://dblp.org/pid/09/287.html), [Jinyoung Sung](https://dblp.org/pid/220/3313.html), [Joakim Johnander](https://dblp.org/pid/202/2479.html), [João F. Henriques](https://dblp.org/pid/31/8617.html), [Jongwon Choi](https://dblp.org/pid/126/0675-2.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jorge Rodríguez Herranz](https://dblp.org/pid/233/9954.html), [José M. Martínez](https://dblp.org/pid/47/3503.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Junfei Zhuang](https://dblp.org/pid/213/4212.html), [Junyu Gao](https://dblp.org/pid/153/4522-2.html), [Klemen Grm](https://dblp.org/pid/178/5048.html), [Lichao Zhang](https://dblp.org/pid/126/8027-1.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Lingxiao Yang](https://dblp.org/pid/56/7126.html), [Litu Rout](https://dblp.org/pid/206/6445.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Liu Si](https://dblp.org/pid/234/0053.html), [Luca Bertinetto](https://dblp.org/pid/154/1351.html), [Lutao Chu](https://dblp.org/pid/234/0100.html), [Manqiang Che](https://dblp.org/pid/224/4651.html), [Mario Edoardo Maresca](https://dblp.org/pid/133/9429.html), Martin Danelljan, [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Myunggu Kang](https://dblp.org/pid/76/8374.html), [Namhoon Lee](https://dblp.org/pid/63/5359.html), [Ning Wang](https://dblp.org/pid/46/2005-20.html), [Ondrej Miksik](https://dblp.org/pid/85/9964.html), [Payman Moallem](https://dblp.org/pid/63/5378.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pablo Vicente-Moñivar](https://dblp.org/pid/234/0077.html), [Pedro Senna](https://dblp.org/pid/170/3084.html), [Peixia Li](https://dblp.org/pid/213/5896.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Priya Mariam Raju](https://dblp.org/pid/233/9987.html), [Ruihe Qian](https://dblp.org/pid/179/2622.html), [Qiang Wang](https://dblp.org/pid/64/5630-51.html), [Qin Zhou](https://dblp.org/pid/80/7814-2.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rafael Martin Nieto](https://dblp.org/pid/136/0491.html), [Rama Krishna Sai Subrahmanyam Gorthi](https://dblp.org/pid/45/7595.html), [Ran Tao](https://dblp.org/pid/99/955-4.html), [Richard Bowden](https://dblp.org/pid/b/RichardBowden.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Richard M. Everson](https://dblp.org/pid/07/6331.html), [Runling Wang](https://dblp.org/pid/224/4642.html), [Sangdoo Yun](https://dblp.org/pid/124/3009.html), [Seokeon Choi](https://dblp.org/pid/214/2200.html), [Sergio Vivas](https://dblp.org/pid/233/9963.html), [Shuai Bai](https://dblp.org/pid/208/8033.html), [Shuangping Huang](https://dblp.org/pid/26/7950.html), [Sihang Wu](https://dblp.org/pid/234/0006.html), [Simon Hadfield](https://dblp.org/pid/33/10771.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Siwen Wang](https://dblp.org/pid/176/5066.html), [Stuart Golodetz](https://dblp.org/pid/34/4052.html), [Ming Tang](https://dblp.org/pid/73/4373-1.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Tobias Fischer](https://dblp.org/pid/181/3897.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Vincenzo Santopietro](https://dblp.org/pid/188/7799.html), [Vitomir Struc](https://dblp.org/pid/47/4796.html), [Wei Wang](https://dblp.org/pid/35/7092-335.html), [Wangmeng Zuo](https://dblp.org/pid/93/2671.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wei Wu](https://dblp.org/pid/95/6985-21.html), [Wei Zou](https://dblp.org/pid/10/328.html), [Weiming Hu](https://dblp.org/pid/41/6824-4.html), [Wengang Zhou](https://dblp.org/pid/22/4544-1.html), [Wenjun Zeng](https://dblp.org/pid/57/145.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaofan Zhang](https://dblp.org/pid/28/9804-2.html), [Xiaohe Wu](https://dblp.org/pid/20/3663.html), [Xiao-Jun Wu](https://dblp.org/pid/13/5168-1.html), [Xinmei Tian](https://dblp.org/pid/03/5204-1.html), [Yan Li](https://dblp.org/pid/87/660-14.html), [Yan Lu](https://dblp.org/pid/15/4830-1.html), [Yee Wei Law](https://dblp.org/pid/62/4404.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Wu](https://dblp.org/pid/44/3684-1.html), [Yiannis Demiris](https://dblp.org/pid/47/1473.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yicai Yang](https://dblp.org/pid/233/9957.html), [Yifan Jiao](https://dblp.org/pid/214/4159.html), [Yuhong Li](https://dblp.org/pid/82/6387.html), [Yunhua Zhang](https://dblp.org/pid/60/9627.html), [Yuxuan Sun](https://dblp.org/pid/194/3079-3.html), [Zheng Zhang](https://dblp.org/pid/181/2621-22.html), [Zheng Zhu](https://dblp.org/pid/29/4319.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhihui Wang](https://dblp.org/pid/65/2749-1.html), [Zhiqun He](https://dblp.org/pid/213/4141.html):

The Sixth Visual Object Tracking VOT2018 Challenge Results. [ECCV Workshops (1)2018](https://dblp.org/db/conf/eccv/eccv2018w1.html#conf/eccv/KristanLMFPZVBL18): 3-53
- ![](https://dblp.org/img/n.png)

\[c22\]
[Joakim Johnander](https://dblp.org/pid/202/2479.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

On the Optimization of Advanced DCF-Trackers. [ECCV Workshops (1)2018](https://dblp.org/db/conf/eccv/eccv2018w1.html#conf/eccv/JohnanderBDKF18): 54-69
- ![](https://dblp.org/img/n.png)

\[c21\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), [Joakim Johnander](https://dblp.org/pid/202/2479.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Unveiling the Power of Deep Tracking. [ECCV (2)2018](https://dblp.org/db/conf/eccv/eccv2018-2.html#conf/eccv/BhatJDKF18): 493-509
- ![](https://dblp.org/img/n.png)

\[i13\]
[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Per-Erik Forssén](https://dblp.org/pid/84/306.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Density Adaptive Point Set Registration. [CoRRabs/1804.01495](https://dblp.org/db/journals/corr/corr1804.html#journals/corr/abs-1804-01495) (2018)
- ![](https://dblp.org/img/n.png)

\[i12\]
[Goutam Bhat](https://dblp.org/pid/190/7682.html), [Joakim Johnander](https://dblp.org/pid/202/2479.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Unveiling the Power of Deep Tracking. [CoRRabs/1804.06833](https://dblp.org/db/journals/corr/corr1804.html#journals/corr/abs-1804-06833) (2018)
- ![](https://dblp.org/img/n.png)

\[i11\]
[Lichao Zhang](https://dblp.org/pid/126/8027-1.html), [Abel Gonzalez-Garcia](https://dblp.org/pid/156/0213.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html):

Synthetic data generation for end-to-end thermal infrared tracking. [CoRRabs/1806.01013](https://dblp.org/db/journals/corr/corr1806.html#journals/corr/abs-1806-01013) (2018)
- ![](https://dblp.org/img/n.png)

\[i10\]
Martin Danelljan, [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

ATOM: Accurate Tracking by Overlap Maximization. [CoRRabs/1811.07628](https://dblp.org/db/journals/corr/corr1811.html#journals/corr/abs-1811-07628) (2018)
- ![](https://dblp.org/img/n.png)

\[i9\]
[Joakim Johnander](https://dblp.org/pid/202/2479.html), Martin Danelljan, [Emil Brissman](https://dblp.org/pid/230/7851.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

A Generative Appearance Model for End-to-end Video Object Segmentation. [CoRRabs/1811.11611](https://dblp.org/db/journals/corr/corr1811.html#journals/corr/abs-1811-11611) (2018)
- 2017
- ![](https://dblp.org/img/n.png)

\[j1\]
Martin Danelljan, [Gustav Häger](https://dblp.org/pid/157/3602.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Discriminative Scale Space Tracking. [IEEE Trans. Pattern Anal. Mach. Intell.39(8)](https://dblp.org/db/journals/pami/pami39.html#journals/pami/DanelljanHKF17): 1561-1575 (2017)
- ![](https://dblp.org/img/n.png)

\[c20\]
[Joakim Johnander](https://dblp.org/pid/202/2479.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

DCCO: Towards Deformable Continuous Convolution Operators for Visual Tracking. [CAIP (1)2017](https://dblp.org/db/conf/caip/caip2017-1.html#conf/caip/JohnanderDKF17): 55-67
- ![](https://dblp.org/img/n.png)

\[c19\]
[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), Martin Danelljan, [Patrik Tosteberg](https://dblp.org/pid/200/8154.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Deep Projective 3D Semantic Segmentation. [CAIP (1)2017](https://dblp.org/db/conf/caip/caip2017-1.html#conf/caip/LawinDTBKF17): 95-107
- ![](https://dblp.org/img/n.png)

\[c18\]
Martin Danelljan, [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

ECO: Efficient Convolution Operators for Tracking. [CVPR2017](https://dblp.org/db/conf/cvpr/cvpr2017.html#conf/cvpr/DanelljanBKF17): 6931-6939
- ![](https://dblp.org/img/n.png)

\[c17\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Tomas Vojir](https://dblp.org/pid/142/5749.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Abdelrahman Eldesokey](https://dblp.org/pid/154/9080.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Álvaro García-Martín](https://dblp.org/pid/39/1542.html), [Andrej Muhic](https://dblp.org/pid/119/0869.html), [Alfredo Petrosino](https://dblp.org/pid/20/3145.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Andrea Vedaldi](https://dblp.org/pid/99/2825.html), [Antoine Manzanera](https://dblp.org/pid/73/2951.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Antoine Tran](https://dblp.org/pid/173/8869.html), [A. Aydin Alatan](https://dblp.org/pid/08/4639.html), [Bogdan Mocanu](https://dblp.org/pid/182/4766.html), [Boyu Chen](https://dblp.org/pid/166/5205.html), [Chang Huang](https://dblp.org/pid/17/2241.html), [Changsheng Xu](https://dblp.org/pid/85/1301.html), [Chong Sun](https://dblp.org/pid/56/2576.html), [Dalong Du](https://dblp.org/pid/159/2057.html), [David Zhang](https://dblp.org/pid/z/DavidZhang.html), [Dawei Du](https://dblp.org/pid/51/6958.html), [Deepak Mishra](https://dblp.org/pid/65/6758-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Erhan Gundogdu](https://dblp.org/pid/147/4597.html), [Erik Velasco-Salido](https://dblp.org/pid/213/4199.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Francesco Battistone](https://dblp.org/pid/167/1252.html), [Gorthi R. K. Sai Subrahmanyam](https://dblp.org/pid/45/7595.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Guan Huang](https://dblp.org/pid/93/10768-3.html), [Guilherme Sousa Bastos](https://dblp.org/pid/166/2034.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guna Seetharaman](https://dblp.org/pid/38/5099.html), [Hongliang Zhang](https://dblp.org/pid/77/10205.html), [Houqiang Li](https://dblp.org/pid/59/7017.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Isabela Drummond](https://dblp.org/pid/45/3169.html), [Jack Valmadre](https://dblp.org/pid/50/8535.html), [Jae-chan Jeong](https://dblp.org/pid/157/3590.html), [Jaeil Cho](https://dblp.org/pid/24/8639.html), [Jae-Yeong Lee](https://dblp.org/pid/19/7743.html), [Jana Noskova](https://dblp.org/pid/142/5723.html), [Jianke Zhu](https://dblp.org/pid/10/4016.html), [Jin Gao](https://dblp.org/pid/13/1653.html), [Jingyu Liu](https://dblp.org/pid/43/6883-4.html), [Ji-Wan Kim](https://dblp.org/pid/174/1015.html), [João F. Henriques](https://dblp.org/pid/31/8617.html), [José M. Martínez](https://dblp.org/pid/47/3503.html), [Junfei Zhuang](https://dblp.org/pid/213/4212.html), [Junliang Xing](https://dblp.org/pid/43/7659.html), [Junyu Gao](https://dblp.org/pid/153/4522-2.html), [Kai Chen](https://dblp.org/pid/c/KaiChen23.html), [Kannappan Palaniappan](https://dblp.org/pid/21/700.html), [Karel Lebeda](https://dblp.org/pid/128/7873.html), [Ke Gao](https://dblp.org/pid/81/2423-3.html), [Kris M. Kitani](https://dblp.org/pid/42/163.html), [Lei Zhang](https://dblp.org/pid/64/5666-6.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Lingxiao Yang](https://dblp.org/pid/56/7126.html), [Longyin Wen](https://dblp.org/pid/119/1468.html), [Luca Bertinetto](https://dblp.org/pid/154/1351.html), [Mahdieh Poostchi](https://dblp.org/pid/87/5622.html), Martin Danelljan, [Matthias Mueller](https://dblp.org/pid/169/4686-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mengdan Zhang](https://dblp.org/pid/172/9514.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Nianhao Xie](https://dblp.org/pid/213/4181.html), [Ning Wang](https://dblp.org/pid/46/2005-20.html), [Ondrej Miksik](https://dblp.org/pid/85/9964.html), [Payman Moallem](https://dblp.org/pid/63/5378.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pallavi M. Venugopal](https://dblp.org/pid/204/9669.html), [Pedro Senna](https://dblp.org/pid/170/3084.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Qiang Wang](https://dblp.org/pid/64/5630-51.html), [Qifeng Yu](https://dblp.org/pid/38/251.html), [Qingming Huang](https://dblp.org/pid/68/4388.html), [Rafael Martin Nieto](https://dblp.org/pid/136/0491.html), [Richard Bowden](https://dblp.org/pid/b/RichardBowden.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Risheng Liu](https://dblp.org/pid/82/8066.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ruxandra Tapu](https://dblp.org/pid/45/10237.html), [Simon Hadfield](https://dblp.org/pid/33/10771.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Siwei Lyu](https://dblp.org/pid/51/4482.html), [Stuart Golodetz](https://dblp.org/pid/34/4052.html), [Sunglok Choi](https://dblp.org/pid/53/7746.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Titus Zaharia](https://dblp.org/pid/45/100.html), [Vincenzo Santopietro](https://dblp.org/pid/188/7799.html), [Wei Zou](https://dblp.org/pid/10/328.html), [Weiming Hu](https://dblp.org/pid/41/6824-4.html), [Wenbing Tao](https://dblp.org/pid/73/188.html), [Wenbo Li](https://dblp.org/pid/51/3185-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wengang Zhou](https://dblp.org/pid/22/4544-1.html), [Xianguo Yu](https://dblp.org/pid/187/9163.html), [Xiao Bian](https://dblp.org/pid/116/5018.html), [Yang Li](https://dblp.org/pid/37/4190-41.html), [Yifan Xing](https://dblp.org/pid/93/10423.html), [Yingruo Fan](https://dblp.org/pid/213/4195.html), [Zheng Zhu](https://dblp.org/pid/29/4319.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Zhiqun He](https://dblp.org/pid/213/4141.html):

The Visual Object Tracking VOT2017 Challenge Results. [ICCV Workshops2017](https://dblp.org/db/conf/iccvw/iccvw2017.html#conf/iccvw/KristanLMFPZVHL17): 1949-1972
- ![](https://dblp.org/img/n.png)

\[i8\]
[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), Martin Danelljan, [Patrik Tosteberg](https://dblp.org/pid/200/8154.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Deep Projective 3D Semantic Segmentation. [CoRRabs/1705.03428](https://dblp.org/db/journals/corr/corr1705.html#journals/corr/LawinDTBKF17) (2017)
- ![](https://dblp.org/img/n.png)

\[i7\]
[Joakim Johnander](https://dblp.org/pid/202/2479.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

DCCO: Towards Deformable Continuous Convolution Operators. [CoRRabs/1706.02888](https://dblp.org/db/journals/corr/corr1706.html#journals/corr/JohnanderDKF17) (2017)
- 2016
- ![](https://dblp.org/img/n.png)

\[c16\]
Martin Danelljan, [Gustav Häger](https://dblp.org/pid/157/3602.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Adaptive Decontamination of the Training Set: A Unified Formulation for Discriminative Visual Tracking. [CVPR2016](https://dblp.org/db/conf/cvpr/cvpr2016.html#conf/cvpr/DanelljanHKF16): 1430-1438
- ![](https://dblp.org/img/n.png)

\[c15\]
Martin Danelljan, [Giulia Meneghetti](https://dblp.org/pid/163/4432.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

A Probabilistic Framework for Color-Based Point Set Registration. [CVPR2016](https://dblp.org/db/conf/cvpr/cvpr2016.html#conf/cvpr/DanelljanMKF16): 1818-1826
- ![](https://dblp.org/img/n.png)

\[c14\]
Martin Danelljan, [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Beyond Correlation Filters: Learning Continuous Convolution Operators for Visual Tracking. [ECCV (5)2016](https://dblp.org/db/conf/eccv/eccv2016-5.html#conf/eccv/DanelljanRKF16): 472-488
- ![](https://dblp.org/img/n.png)

\[c13\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Luka Cehovin](https://dblp.org/pid/19/8654.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tomás Vojír](https://dblp.org/pid/142/5749.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Abhinav Gupta](https://dblp.org/pid/36/7024-1.html), [Alfredo Petrosino](https://dblp.org/pid/20/3145.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Álvaro García-Martín](https://dblp.org/pid/39/1542.html), [Andrés Solís Montero](https://dblp.org/pid/36/8379.html), [Andrea Vedaldi](https://dblp.org/pid/99/2825.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Andy Jinhua Ma](https://dblp.org/pid/119/1514.html), [Anton Varfolomieiev](https://dblp.org/pid/188/7504.html)![](https://dblp.org/img/orcid-mark.12x12.png), [A. Aydin Alatan](https://dblp.org/pid/08/4639.html), [Aykut Erdem](https://dblp.org/pid/04/1832.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bernard Ghanem](https://dblp.org/pid/37/2516.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bin Liu](https://dblp.org/pid/35/837-14.html), [Bohyung Han](https://dblp.org/pid/73/4880.html), [Brais Martínez](https://dblp.org/pid/14/111.html), [Chang-Ming Chang](https://dblp.org/pid/188/7581.html), [Changsheng Xu](https://dblp.org/pid/85/1301.html), [Chong Sun](https://dblp.org/pid/56/2576.html), [Daijin Kim](https://dblp.org/pid/k/DaijinKim.html), [Dapeng Chen](https://dblp.org/pid/04/3068.html), [Dawei Du](https://dblp.org/pid/51/6958.html), [Deepak Mishra](https://dblp.org/pid/65/6758-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dit-Yan Yeung](https://dblp.org/pid/41/5668.html), [Erhan Gundogdu](https://dblp.org/pid/147/4597.html), [Erkut Erdem](https://dblp.org/pid/79/6569.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Fatih Porikli](https://dblp.org/pid/p/FatihMuratPorikli.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fei Zhao](https://dblp.org/pid/21/6180-8.html), [Filiz Bunyak](https://dblp.org/pid/06/3172.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Francesco Battistone](https://dblp.org/pid/167/1252.html), [Gao Zhu](https://dblp.org/pid/139/3887.html), [Giorgio Roffo](https://dblp.org/pid/123/2925.html), [Gorthi R. K. Sai Subrahmanyam](https://dblp.org/pid/45/7595.html), [Guilherme Sousa Bastos](https://dblp.org/pid/166/2034.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Guna Seetharaman](https://dblp.org/pid/38/5099.html), [Henry Medeiros](https://dblp.org/pid/62/8630.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Honggang Qi](https://dblp.org/pid/48/4237.html), [Horst Bischof](https://dblp.org/pid/69/3793.html), [Horst Possegger](https://dblp.org/pid/135/4917.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Hyemin Lee](https://dblp.org/pid/188/7676.html), [Hyeonseob Nam](https://dblp.org/pid/150/4248.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Isabela Drummond](https://dblp.org/pid/45/3169.html), [Jack Valmadre](https://dblp.org/pid/50/8535.html), [Jae-chan Jeong](https://dblp.org/pid/157/3590.html), [Jaeil Cho](https://dblp.org/pid/24/8639.html), [Jae-Yeong Lee](https://dblp.org/pid/19/7743.html), [Jianke Zhu](https://dblp.org/pid/10/4016.html), [Jiayi Feng](https://dblp.org/pid/176/1403.html), [Jin Gao](https://dblp.org/pid/13/1653.html), [Jin Young Choi](https://dblp.org/pid/30/1428-2.html), [Jingjing Xiao](https://dblp.org/pid/121/0292.html), [Ji-Wan Kim](https://dblp.org/pid/174/1015.html), [Jiyeoup Jeong](https://dblp.org/pid/152/5790.html), [João F. Henriques](https://dblp.org/pid/31/8617.html), [Jochen Lang](https://dblp.org/pid/34/2622.html), [Jongwon Choi](https://dblp.org/pid/126/0675-2.html), [José M. Martínez](https://dblp.org/pid/47/3503.html), [Junliang Xing](https://dblp.org/pid/43/7659.html), [Junyu Gao](https://dblp.org/pid/153/4522-2.html), [Kannappan Palaniappan](https://dblp.org/pid/21/700.html), [Karel Lebeda](https://dblp.org/pid/128/7873.html), [Ke Gao](https://dblp.org/pid/81/2423-3.html), [Krystian Mikolajczyk](https://dblp.org/pid/96/433.html), [Lei Qin](https://dblp.org/pid/20/1306.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Longyin Wen](https://dblp.org/pid/119/1468.html), [Luca Bertinetto](https://dblp.org/pid/154/1351.html), [Madan Kumar Rapuru](https://dblp.org/pid/188/7542.html), [Mahdieh Poostchi](https://dblp.org/pid/87/5622.html), [Mario Edoardo Maresca](https://dblp.org/pid/133/9429.html), Martin Danelljan, [Matthias Mueller](https://dblp.org/pid/169/4686-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mengdan Zhang](https://dblp.org/pid/172/9514.html), [Michael Arens](https://dblp.org/pid/69/5391.html), [Michel F. Valstar](https://dblp.org/pid/00/2794.html), [Ming Tang](https://dblp.org/pid/73/4373-1.html), [Mooyeol Baek](https://dblp.org/pid/185/0822.html), [Muhammad Haris Khan](https://dblp.org/pid/155/3076.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Naiyan Wang](https://dblp.org/pid/31/9922.html), [Nana Fan](https://dblp.org/pid/146/8400.html), [Noor Al-Shakarji](https://dblp.org/pid/188/7419.html), [Ondrej Miksik](https://dblp.org/pid/85/9964.html), [Osman Akin](https://dblp.org/pid/155/3117.html), [Payman Moallem](https://dblp.org/pid/63/5378.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Pedro Senna](https://dblp.org/pid/170/3084.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Pong C. Yuen](https://dblp.org/pid/y/PongChiYuen.html), [Qingming Huang](https://dblp.org/pid/68/4388.html), [Rafael Martin Nieto](https://dblp.org/pid/136/0491.html), [Rengarajan Pelapur](https://dblp.org/pid/70/11224.html), [Richard Bowden](https://dblp.org/pid/b/RichardBowden.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Robert Laganière](https://dblp.org/pid/32/1448.html), [Rustam Stolkin](https://dblp.org/pid/72/2344.html), [Ryan Walsh](https://dblp.org/pid/188/7715.html), [Sebastian Bernd Krah](https://dblp.org/pid/147/3405.html), [Shengkun Li](https://dblp.org/pid/188/7561.html), [Shengping Zhang](https://dblp.org/pid/60/1866.html), [Shizeng Yao](https://dblp.org/pid/188/7638.html), [Simon Hadfield](https://dblp.org/pid/33/10771.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Simone Melzi](https://dblp.org/pid/160/2770.html), [Siwei Lyu](https://dblp.org/pid/51/4482.html), [Siyi Li](https://dblp.org/pid/96/10161.html), [Stefan Becker](https://dblp.org/pid/62/7091.html), [Stuart Golodetz](https://dblp.org/pid/34/4052.html), [Sumithra Kakanuru](https://dblp.org/pid/188/7777.html), [Sunglok Choi](https://dblp.org/pid/53/7746.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tao Hu](https://dblp.org/pid/41/5865-11.html), [Thomas Mauthner](https://dblp.org/pid/95/6646.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Tony P. Pridmore](https://dblp.org/pid/19/6645.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Vincenzo Santopietro](https://dblp.org/pid/188/7799.html), [Weiming Hu](https://dblp.org/pid/41/6824-4.html), [Wenbo Li](https://dblp.org/pid/51/3185-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wolfgang Hübner](https://dblp.org/pid/97/2668-1.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Xiaomeng Wang](https://dblp.org/pid/35/6677.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Yang Li](https://dblp.org/pid/37/4190-41.html), [Yiannis Demiris](https://dblp.org/pid/47/1473.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yifan Wang](https://dblp.org/pid/47/6959-4.html), [Yuankai Qi](https://dblp.org/pid/136/5491.html), [Zejian Yuan](https://dblp.org/pid/26/455.html), [Zexiong Cai](https://dblp.org/pid/188/7533.html), [Zhan Xu](https://dblp.org/pid/26/5600.html), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Zhizhen Chi](https://dblp.org/pid/188/7596.html):

The Visual Object Tracking VOT2016 Challenge Results. [ECCV Workshops (2)2016](https://dblp.org/db/conf/eccv/eccv2016w2.html#conf/eccv/KristanLMFPCVHL16): 777-823
- ![](https://dblp.org/img/n.png)

\[c12\]
[Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Matej Kristan](https://dblp.org/pid/79/1648.html), [Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Amanda Berg](https://dblp.org/pid/163/4511.html), [Abdelrahman Eldesokey](https://dblp.org/pid/154/9080.html), [Jörgen Ahlberg](https://dblp.org/pid/a/JorgenAhlberg.html), [Luka Cehovin](https://dblp.org/pid/19/8654.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Tomás Vojír](https://dblp.org/pid/142/5749.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Alfredo Petrosino](https://dblp.org/pid/20/3145.html), [Álvaro García-Martín](https://dblp.org/pid/39/1542.html), [Andrés Solís Montero](https://dblp.org/pid/36/8379.html), [Anton Varfolomieiev](https://dblp.org/pid/188/7504.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Aykut Erdem](https://dblp.org/pid/04/1832.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bohyung Han](https://dblp.org/pid/73/4880.html), [Chang-Ming Chang](https://dblp.org/pid/188/7581.html), [Dawei Du](https://dblp.org/pid/51/6958.html), [Erkut Erdem](https://dblp.org/pid/79/6569.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Fatih Porikli](https://dblp.org/pid/p/FatihMuratPorikli.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Fei Zhao](https://dblp.org/pid/21/6180-8.html), [Filiz Bunyak](https://dblp.org/pid/06/3172.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Francesco Battistone](https://dblp.org/pid/167/1252.html), [Gao Zhu](https://dblp.org/pid/139/3887.html), [Guna Seetharaman](https://dblp.org/pid/38/5099.html), [Hongdong Li](https://dblp.org/pid/59/4859.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Honggang Qi](https://dblp.org/pid/48/4237.html), [Horst Bischof](https://dblp.org/pid/69/3793.html), [Horst Possegger](https://dblp.org/pid/135/4917.html), [Hyeonseob Nam](https://dblp.org/pid/150/4248.html), [Jack Valmadre](https://dblp.org/pid/50/8535.html), [Jianke Zhu](https://dblp.org/pid/10/4016.html), [Jiayi Feng](https://dblp.org/pid/176/1403.html), [Jochen Lang](https://dblp.org/pid/34/2622.html), [José M. Martínez](https://dblp.org/pid/47/3503.html), [Kannappan Palaniappan](https://dblp.org/pid/21/700.html), [Karel Lebeda](https://dblp.org/pid/128/7873.html), [Ke Gao](https://dblp.org/pid/81/2423-3.html), [Krystian Mikolajczyk](https://dblp.org/pid/96/433.html), [Longyin Wen](https://dblp.org/pid/119/1468.html), [Luca Bertinetto](https://dblp.org/pid/154/1351.html), [Mahdieh Poostchi](https://dblp.org/pid/87/5622.html), [Mario Edoardo Maresca](https://dblp.org/pid/133/9429.html), Martin Danelljan, [Michael Arens](https://dblp.org/pid/69/5391.html), [Ming Tang](https://dblp.org/pid/73/4373-1.html), [Mooyeol Baek](https://dblp.org/pid/185/0822.html), [Nana Fan](https://dblp.org/pid/146/8400.html), [Noor Al-Shakarji](https://dblp.org/pid/188/7419.html), [Ondrej Miksik](https://dblp.org/pid/85/9964.html), [Osman Akin](https://dblp.org/pid/155/3117.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Qingming Huang](https://dblp.org/pid/68/4388.html), [Rafael Martin Nieto](https://dblp.org/pid/136/0491.html), [Rengarajan Pelapur](https://dblp.org/pid/70/11224.html), [Richard Bowden](https://dblp.org/pid/b/RichardBowden.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Robert Laganière](https://dblp.org/pid/32/1448.html), [Sebastian Bernd Krah](https://dblp.org/pid/147/3405.html), [Shengkun Li](https://dblp.org/pid/188/7561.html), [Shizeng Yao](https://dblp.org/pid/188/7638.html), [Simon Hadfield](https://dblp.org/pid/33/10771.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Siwei Lyu](https://dblp.org/pid/51/4482.html), [Stefan Becker](https://dblp.org/pid/62/7091.html), [Stuart Golodetz](https://dblp.org/pid/34/4052.html), [Tao Hu](https://dblp.org/pid/41/5865-11.html), [Thomas Mauthner](https://dblp.org/pid/95/6646.html), [Vincenzo Santopietro](https://dblp.org/pid/188/7799.html), [Wenbo Li](https://dblp.org/pid/51/3185-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wolfgang Hübner](https://dblp.org/pid/97/2668-1.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Yang Li](https://dblp.org/pid/37/4190-41.html), [Zhan Xu](https://dblp.org/pid/26/5600.html), [Zhenyu He](https://dblp.org/pid/57/6240-1.html):

The Thermal Infrared Visual Object Tracking VOT-TIR2016 Challenge Results. [ECCV Workshops (2)2016](https://dblp.org/db/conf/eccv/eccv2016w2.html#conf/eccv/FelsbergKMLPHBE16): 824-849
- ![](https://dblp.org/img/n.png)

\[c11\]
Martin Danelljan, [Giulia Meneghetti](https://dblp.org/pid/163/4432.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Aligning the dissimilar: A probabilistic method for feature-based point set registration. [ICPR2016](https://dblp.org/db/conf/icpr/icpr2016.html#conf/icpr/DanelljanMKF16): 247-252
- ![](https://dblp.org/img/n.png)

\[c10\]
[Susanna Gladh](https://dblp.org/pid/192/1542.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Deep motion features for visual tracking. [ICPR2016](https://dblp.org/db/conf/icpr/icpr2016.html#conf/icpr/GladhDKF16): 1243-1248
- ![](https://dblp.org/img/n.png)

\[c9\]
[Gustav Häger](https://dblp.org/pid/157/3602.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Piotr Rudol](https://dblp.org/pid/44/101.html), [Patrick Doherty](https://dblp.org/pid/81/3618.html):

Combining Visual Tracking and Person Detection for Long Term Tracking on a UAV. [ISVC (1)2016](https://dblp.org/db/conf/isvc/isvc2016-1.html#conf/isvc/HagerBDKFRD16): 557-568
- ![](https://dblp.org/img/n.png)

\[i6\]
Martin Danelljan, [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Beyond Correlation Filters: Learning Continuous Convolution Operators for Visual Tracking. [CoRRabs/1608.03773](https://dblp.org/db/journals/corr/corr1608.html#journals/corr/DanelljanRKF16) (2016)
- ![](https://dblp.org/img/n.png)

\[i5\]
Martin Danelljan, [Gustav Häger](https://dblp.org/pid/157/3602.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Learning Spatially Regularized Correlation Filters for Visual Tracking. [CoRRabs/1608.05571](https://dblp.org/db/journals/corr/corr1608.html#journals/corr/DanelljanHKF16) (2016)
- ![](https://dblp.org/img/n.png)

\[i4\]
Martin Danelljan, [Gustav Häger](https://dblp.org/pid/157/3602.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Adaptive Decontamination of the Training Set: A Unified Formulation for Discriminative Visual Tracking. [CoRRabs/1609.06118](https://dblp.org/db/journals/corr/corr1609.html#journals/corr/DanelljanHKF16a) (2016)
- ![](https://dblp.org/img/n.png)

\[i3\]
Martin Danelljan, [Gustav Häger](https://dblp.org/pid/157/3602.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Discriminative Scale Space Tracking. [CoRRabs/1609.06141](https://dblp.org/db/journals/corr/corr1609.html#journals/corr/DanelljanHKF16b) (2016)
- ![](https://dblp.org/img/n.png)

\[i2\]
Martin Danelljan, [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

ECO: Efficient Convolution Operators for Tracking. [CoRRabs/1611.09224](https://dblp.org/db/journals/corr/corr1611.html#journals/corr/DanelljanBKF16) (2016)
- ![](https://dblp.org/img/n.png)

\[i1\]
[Susanna Gladh](https://dblp.org/pid/192/1542.html), Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Deep Motion Features for Visual Tracking. [CoRRabs/1612.06615](https://dblp.org/db/journals/corr/corr1612.html#journals/corr/GladhDKF16) (2016)
- 2015
- ![](https://dblp.org/img/n.png)

\[c8\]
Martin Danelljan, [Gustav Häger](https://dblp.org/pid/157/3602.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Learning Spatially Regularized Correlation Filters for Visual Tracking. [ICCV2015](https://dblp.org/db/conf/iccv/iccv2015.html#conf/iccv/DanelljanHKF15): 4310-4318
- ![](https://dblp.org/img/n.png)

\[c7\]
Martin Danelljan, [Gustav Häger](https://dblp.org/pid/157/3602.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Convolutional Features for Correlation Filter Based Visual Tracking. [ICCV Workshops2015](https://dblp.org/db/conf/iccvw/iccvw2015.html#conf/iccvw/DanelljanHKF15): 621-629
- ![](https://dblp.org/img/n.png)

\[c6\]
Martin Danelljan, [Gustav Häger](https://dblp.org/pid/157/3602.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Coloring Channel Representations for Visual Tracking. [SCIA2015](https://dblp.org/db/conf/scia/scia2015.html#conf/scia/DanelljanHKF15): 117-129
- ![](https://dblp.org/img/n.png)

\[c5\]
[Giulia Meneghetti](https://dblp.org/pid/163/4432.html), Martin Danelljan, [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Klas Nordberg](https://dblp.org/pid/94/5686.html):

Image Alignment for Panorama Stitching in Sparsely Structured Environments. [SCIA2015](https://dblp.org/db/conf/scia/scia2015.html#conf/scia/MeneghettiDFN15): 428-439
- 2014
- ![](https://dblp.org/img/n.png)

\[c4\]
Martin Danelljan, [Gustav Häger](https://dblp.org/pid/157/3602.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html):

Accurate Scale Estimation for Robust Visual Tracking. [BMVC2014](https://dblp.org/db/conf/bmvc/bmvc2014.html#conf/bmvc/DanelljanHKF14)
- ![](https://dblp.org/img/n.png)

\[c3\]
Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Joost van de Weijer](https://dblp.org/pid/67/3379.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Adaptive Color Attributes for Real-Time Visual Tracking. [CVPR2014](https://dblp.org/db/conf/cvpr/cvpr2014.html#conf/cvpr/DanelljanKFW14): 1090-1097
- ![](https://dblp.org/img/n.png)

\[c2\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luka Cehovin](https://dblp.org/pid/19/8654.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Georg Nebehay](https://dblp.org/pid/129/4056.html), [Tomás Vojír](https://dblp.org/pid/142/5749.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Aleksandar Dimitriev](https://dblp.org/pid/160/3686.html), [Alfredo Petrosino](https://dblp.org/pid/20/3145.html), [Amir Saffari](https://dblp.org/pid/71/310.html), [Bo Li](https://dblp.org/pid/50/3402-114.html), [Bohyung Han](https://dblp.org/pid/73/4880.html), [Cherkeng Heng](https://dblp.org/pid/49/9606.html), [Christophe Garcia](https://dblp.org/pid/26/6493.html), [Dominik Pangersic](https://dblp.org/pid/160/3593.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Franci Oven](https://dblp.org/pid/160/3716.html), [Horst Possegger](https://dblp.org/pid/135/4917.html), [Horst Bischof](https://dblp.org/pid/69/3793.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hyeonseob Nam](https://dblp.org/pid/150/4248.html), [Jianke Zhu](https://dblp.org/pid/10/4016.html), [Jijia Li](https://dblp.org/pid/135/1024.html), [Jin Young Choi](https://dblp.org/pid/30/1428-2.html), [Jinwoo Choi](https://dblp.org/pid/47/2621-1.html), [João F. Henriques](https://dblp.org/pid/31/8617.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jorge Batista](https://dblp.org/pid/26/4565.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Karel Lebeda](https://dblp.org/pid/128/7873.html), [Kristoffer Öfjäll](https://dblp.org/pid/157/3586.html), [Kwang Moo Yi](https://dblp.org/pid/30/5082.html), [Lei Qin](https://dblp.org/pid/20/1306.html), [Longyin Wen](https://dblp.org/pid/119/1468.html), [Mario Edoardo Maresca](https://dblp.org/pid/133/9429.html), Martin Danelljan, [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ming-Ming Cheng](https://dblp.org/pid/45/7592.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Qingming Huang](https://dblp.org/pid/68/4388.html), [Richard Bowden](https://dblp.org/pid/b/RichardBowden.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sam Hare](https://dblp.org/pid/79/10771.html), [Samantha YueYing Lim](https://dblp.org/pid/160/3756.html), [Seunghoon Hong](https://dblp.org/pid/142/3014.html), [Shengcai Liao](https://dblp.org/pid/16/8313.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Simon Hadfield](https://dblp.org/pid/33/10771.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Stan Z. Li](https://dblp.org/pid/l/StanZLi.html), [Stefan Duffner](https://dblp.org/pid/64/6849.html), [Stuart Golodetz](https://dblp.org/pid/34/4052.html), [Thomas Mauthner](https://dblp.org/pid/95/6646.html), [Vibhav Vineet](https://dblp.org/pid/02/8067.html), [Weiyao Lin](https://dblp.org/pid/42/6095.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yang Li](https://dblp.org/pid/37/4190-41.html), [Yuankai Qi](https://dblp.org/pid/136/5491.html), [Zhen Lei](https://dblp.org/pid/55/112-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhi Heng Niu](https://dblp.org/pid/80/3992.html):

The Visual Object Tracking VOT2014 Challenge Results. [ECCV Workshops (2)2014](https://dblp.org/db/conf/eccv/eccv2014w2.html#conf/eccv/KristanPLMCNVFL14): 191-217
- ![](https://dblp.org/img/n.png)

\[c1\]
Martin Danelljan, [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Karl Granström](https://dblp.org/pid/58/10006.html), [Fredrik Heintz](https://dblp.org/pid/86/6319.html), [Piotr Rudol](https://dblp.org/pid/44/101.html), [Mariusz Wzorek](https://dblp.org/pid/89/4943.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jonas Kvarnström](https://dblp.org/pid/05/3470.html), [Patrick Doherty](https://dblp.org/pid/81/3618.html):

A Low-Level Active Vision Framework for Collaborative Unmanned Aircraft Systems. [ECCV Workshops (1)2014](https://dblp.org/db/conf/eccv/eccv2014w1.html#conf/eccv/DanelljanKFGHRW14): 223-237
- _no results_

automatic loading of the coauthor graph disabled due to its size.

**click here to**
**load the graph.**

Note that this feature is _work in progress_ and that it is still far from being perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/151/8848.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[2](https://dblp.org/pid/151/8848.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Maria Isabel Agea](https://dblp.org/pid/355/2674.html)

[\[c101\]](https://dblp.org/pid/151/8848.html#c101) [\[i81\]](https://dblp.org/pid/151/8848.html#i81)

[3](https://dblp.org/pid/151/8848.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jörgen Ahlberg](https://dblp.org/pid/a/JorgenAhlberg.html)

[\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[4](https://dblp.org/pid/151/8848.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Namhyuk Ahn](https://dblp.org/pid/217/1998.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[5](https://dblp.org/pid/151/8848.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Osman Akin](https://dblp.org/pid/155/3117.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[6](https://dblp.org/pid/151/8848.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kazutoshi Akita](https://dblp.org/pid/260/3239.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52) [\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[7](https://dblp.org/pid/151/8848.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Noor Al-Shakarji](https://dblp.org/pid/188/7419.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[8](https://dblp.org/pid/151/8848.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Alexandre Alahi](https://dblp.org/pid/48/3455.html)

[\[c39\]](https://dblp.org/pid/151/8848.html#c39) [\[i29\]](https://dblp.org/pid/151/8848.html#i29)

[9](https://dblp.org/pid/151/8848.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[A. Aydin Alatan](https://dblp.org/pid/08/4639.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[10](https://dblp.org/pid/151/8848.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dong An](https://dblp.org/pid/02/7028.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[11](https://dblp.org/pid/151/8848.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Michael Arens](https://dblp.org/pid/69/5391.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[12](https://dblp.org/pid/151/8848.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[George De Ath](https://dblp.org/pid/220/3209.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[13](https://dblp.org/pid/151/8848.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sung-Ho Bae](https://dblp.org/pid/76/2068.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[14](https://dblp.org/pid/151/8848.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mooyeol Baek](https://dblp.org/pid/185/0822.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[15](https://dblp.org/pid/151/8848.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bing Bai](https://dblp.org/pid/54/5260.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[16](https://dblp.org/pid/151/8848.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dongwoon Bai](https://dblp.org/pid/07/2673.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[17](https://dblp.org/pid/151/8848.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haoran Bai](https://dblp.org/pid/235/9510.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[18](https://dblp.org/pid/151/8848.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hongliang Bai](https://dblp.org/pid/34/5268.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[19](https://dblp.org/pid/151/8848.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shuai Bai](https://dblp.org/pid/208/8033.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[20](https://dblp.org/pid/151/8848.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiang Bai](https://dblp.org/pid/59/2741.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[21](https://dblp.org/pid/151/8848.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lukasz Bala](https://dblp.org/pid/264/5872.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[22](https://dblp.org/pid/151/8848.html?view=joint&param=22 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=2)

[Alvard Barseghyan](https://dblp.org/pid/365/4108.html)

[\[i96\]](https://dblp.org/pid/151/8848.html#i96)

[23](https://dblp.org/pid/151/8848.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Guilherme Sousa Bastos](https://dblp.org/pid/166/2034.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[24](https://dblp.org/pid/151/8848.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jorge P. Batista](https://dblp.org/pid/26/4565.html)

aka: Jorge Batista 0001

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[25](https://dblp.org/pid/151/8848.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Francesco Battistone](https://dblp.org/pid/167/1252.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[26](https://dblp.org/pid/151/8848.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Stefan Becker](https://dblp.org/pid/62/7091.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[27](https://dblp.org/pid/151/8848.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sefi Bell-Kligler](https://dblp.org/pid/249/2218.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[28](https://dblp.org/pid/151/8848.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kang Ben](https://dblp.org/pid/340/0959.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[29](https://dblp.org/pid/151/8848.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Amanda Berg](https://dblp.org/pid/163/4511.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[30](https://dblp.org/pid/151/8848.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Luca Bertinetto](https://dblp.org/pid/154/1351.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[31](https://dblp.org/pid/151/8848.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jesús Bescós](https://dblp.org/pid/97/2333.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[32](https://dblp.org/pid/151/8848.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Vineeth S. Bhaskara](https://dblp.org/pid/197/6505.html)

aka: Vineeth Bhaskara

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[33](https://dblp.org/pid/151/8848.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[c86\]](https://dblp.org/pid/151/8848.html#c86) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c74\]](https://dblp.org/pid/151/8848.html#c74) [\[i69\]](https://dblp.org/pid/151/8848.html#i69) [\[i63\]](https://dblp.org/pid/151/8848.html#i63) [\[c70\]](https://dblp.org/pid/151/8848.html#c70) [\[c66\]](https://dblp.org/pid/151/8848.html#c66) [\[c64\]](https://dblp.org/pid/151/8848.html#c64) [\[c59\]](https://dblp.org/pid/151/8848.html#c59) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[i59\]](https://dblp.org/pid/151/8848.html#i59) [\[i57\]](https://dblp.org/pid/151/8848.html#i57) [\[i52\]](https://dblp.org/pid/151/8848.html#i52) [\[i49\]](https://dblp.org/pid/151/8848.html#i49) [\[c45\]](https://dblp.org/pid/151/8848.html#c45) [\[c44\]](https://dblp.org/pid/151/8848.html#c44) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c40\]](https://dblp.org/pid/151/8848.html#c40) [\[i39\]](https://dblp.org/pid/151/8848.html#i39) [\[i38\]](https://dblp.org/pid/151/8848.html#i38) [\[j3\]](https://dblp.org/pid/151/8848.html#j3) [\[c36\]](https://dblp.org/pid/151/8848.html#c36) [\[c33\]](https://dblp.org/pid/151/8848.html#c33) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[i22\]](https://dblp.org/pid/151/8848.html#i22) [\[i16\]](https://dblp.org/pid/151/8848.html#i16) [\[c25\]](https://dblp.org/pid/151/8848.html#c25) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c22\]](https://dblp.org/pid/151/8848.html#c22) [\[c21\]](https://dblp.org/pid/151/8848.html#c21) [\[i12\]](https://dblp.org/pid/151/8848.html#i12) [\[i10\]](https://dblp.org/pid/151/8848.html#i10) [\[c19\]](https://dblp.org/pid/151/8848.html#c19) [\[c18\]](https://dblp.org/pid/151/8848.html#c18) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[i8\]](https://dblp.org/pid/151/8848.html#i8) [\[c9\]](https://dblp.org/pid/151/8848.html#c9) [\[i2\]](https://dblp.org/pid/151/8848.html#i2)

[34](https://dblp.org/pid/151/8848.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiao Bian](https://dblp.org/pid/116/5018.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[35](https://dblp.org/pid/151/8848.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tolga Birdal](https://dblp.org/pid/143/7056.html)

[\[c114\]](https://dblp.org/pid/151/8848.html#c114)

[36](https://dblp.org/pid/151/8848.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Horst Bischof](https://dblp.org/pid/69/3793.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[37](https://dblp.org/pid/151/8848.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Johanna Björklund](https://dblp.org/pid/75/5525.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[38](https://dblp.org/pid/151/8848.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Philippe Blatter](https://dblp.org/pid/309/5966.html)

[\[c95\]](https://dblp.org/pid/151/8848.html#c95) [\[i41\]](https://dblp.org/pid/151/8848.html#i41)

[39](https://dblp.org/pid/151/8848.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Richard Bowden](https://dblp.org/pid/b/RichardBowden.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[40](https://dblp.org/pid/151/8848.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Emil Brissman](https://dblp.org/pid/230/7851.html)

[\[j8\]](https://dblp.org/pid/151/8848.html#j8) [\[c65\]](https://dblp.org/pid/151/8848.html#c65) [\[i25\]](https://dblp.org/pid/151/8848.html#i25) [\[c35\]](https://dblp.org/pid/151/8848.html#c35) [\[i9\]](https://dblp.org/pid/151/8848.html#i9)

[41](https://dblp.org/pid/151/8848.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sebastian Bullinger](https://dblp.org/pid/197/9724.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[42](https://dblp.org/pid/151/8848.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Filiz Bunyak](https://dblp.org/pid/06/3172.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[43](https://dblp.org/pid/151/8848.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dingding Cai](https://dblp.org/pid/198/1127.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[44](https://dblp.org/pid/151/8848.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jie Cai 0001](https://dblp.org/pid/95/3916-1.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[45](https://dblp.org/pid/151/8848.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zexiong Cai](https://dblp.org/pid/188/7533.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[46](https://dblp.org/pid/151/8848.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yizhen Cao](https://dblp.org/pid/202/4950.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[47](https://dblp.org/pid/151/8848.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yun Cao 0002](https://dblp.org/pid/40/2407-2.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[48](https://dblp.org/pid/151/8848.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuntian Cao](https://dblp.org/pid/327/3208.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[49](https://dblp.org/pid/151/8848.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Alexandre Carlier](https://dblp.org/pid/271/0428.html)

[\[c39\]](https://dblp.org/pid/151/8848.html#c39) [\[i29\]](https://dblp.org/pid/151/8848.html#i29)

[50](https://dblp.org/pid/151/8848.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[51](https://dblp.org/pid/151/8848.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Llukman Cerkezi](https://dblp.org/pid/208/1312.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[52](https://dblp.org/pid/151/8848.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hakan Çevikalp](https://dblp.org/pid/14/6210.html)

aka: Hakan Cevikalp

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[53](https://dblp.org/pid/151/8848.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Javaan S. Chahl](https://dblp.org/pid/12/797.html)

aka: Javaan Singh Chahl

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[54](https://dblp.org/pid/151/8848.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Antoni B. Chan](https://dblp.org/pid/55/5814.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[55](https://dblp.org/pid/151/8848.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yui-Lam Chan](https://dblp.org/pid/04/2096.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[56](https://dblp.org/pid/151/8848.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chang-Ming Chang](https://dblp.org/pid/188/7581.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[57](https://dblp.org/pid/151/8848.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hong Chang 0001](https://dblp.org/pid/02/2689-1.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[58](https://dblp.org/pid/151/8848.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[59](https://dblp.org/pid/151/8848.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shijie Chang](https://dblp.org/pid/277/8125.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[60](https://dblp.org/pid/151/8848.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Manqiang Che](https://dblp.org/pid/224/4651.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[61](https://dblp.org/pid/151/8848.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bao Xin Chen](https://dblp.org/pid/153/1895.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[62](https://dblp.org/pid/151/8848.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Boyu Chen](https://dblp.org/pid/166/5205.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[63](https://dblp.org/pid/151/8848.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Cheng Chen](https://dblp.org/pid/10/217.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[64](https://dblp.org/pid/151/8848.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dapeng Chen](https://dblp.org/pid/04/3068.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[65](https://dblp.org/pid/151/8848.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Deming Chen](https://dblp.org/pid/37/1234.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[66](https://dblp.org/pid/151/8848.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Guangqi Chen](https://dblp.org/pid/178/8116.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[67](https://dblp.org/pid/151/8848.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hanyuan Chen](https://dblp.org/pid/363/8621.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[68](https://dblp.org/pid/151/8848.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiaye Chen](https://dblp.org/pid/116/2901.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[69](https://dblp.org/pid/151/8848.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jie Chen](https://dblp.org/pid/92/6289.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[70](https://dblp.org/pid/151/8848.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Junyang Chen 0001](https://dblp.org/pid/196/7893.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[71](https://dblp.org/pid/151/8848.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kai Chen 0023](https://dblp.org/pid/c/KaiChen23.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[72](https://dblp.org/pid/151/8848.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lei Chen](https://dblp.org/pid/09/3666.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[73](https://dblp.org/pid/151/8848.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Liang Chen](https://dblp.org/pid/01/5394.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[74](https://dblp.org/pid/151/8848.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Long Chen 0005](https://dblp.org/pid/64/5725-5.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[75](https://dblp.org/pid/151/8848.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Meiya Chen](https://dblp.org/pid/13/8141.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[76](https://dblp.org/pid/151/8848.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[77](https://dblp.org/pid/151/8848.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shuhao Chen](https://dblp.org/pid/43/2127.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[78](https://dblp.org/pid/151/8848.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Siang Chen](https://dblp.org/pid/260/2691.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[79](https://dblp.org/pid/151/8848.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenbin Chen](https://dblp.org/pid/181/2912.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[80](https://dblp.org/pid/151/8848.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xi Chen](https://dblp.org/pid/16/3283.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[81](https://dblp.org/pid/151/8848.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xier Chen](https://dblp.org/pid/260/3035.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[82](https://dblp.org/pid/151/8848.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xihao Chen](https://dblp.org/pid/40/304.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[83](https://dblp.org/pid/151/8848.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xilin Chen 0001](https://dblp.org/pid/c/XilinChen.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[84](https://dblp.org/pid/151/8848.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[85](https://dblp.org/pid/151/8848.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xingyu Chen](https://dblp.org/pid/59/7651.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[86](https://dblp.org/pid/151/8848.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiuyi Chen](https://dblp.org/pid/218/7190.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[87](https://dblp.org/pid/151/8848.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yan Chen 0017](https://dblp.org/pid/88/2827-17.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[88](https://dblp.org/pid/151/8848.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yanan Chen](https://dblp.org/pid/78/10104.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[89](https://dblp.org/pid/151/8848.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yanjie Chen](https://dblp.org/pid/02/7548.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[90](https://dblp.org/pid/151/8848.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yiwei Chen](https://dblp.org/pid/28/2965.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[91](https://dblp.org/pid/151/8848.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yu-Hsi Chen](https://dblp.org/pid/127/3933.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[92](https://dblp.org/pid/151/8848.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhenyu Chen 0001](https://dblp.org/pid/86/541-1.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[93](https://dblp.org/pid/151/8848.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhihao Chen 0004](https://dblp.org/pid/50/505-4.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[94](https://dblp.org/pid/151/8848.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhixing Chen](https://dblp.org/pid/62/3074.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[95](https://dblp.org/pid/151/8848.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jian Cheng 0001](https://dblp.org/pid/14/6145-1.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[96](https://dblp.org/pid/151/8848.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kaihua Cheng](https://dblp.org/pid/264/5745.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[97](https://dblp.org/pid/151/8848.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Li Cheng 0001](https://dblp.org/pid/13/4938-1.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[98](https://dblp.org/pid/151/8848.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Miao Cheng](https://dblp.org/pid/79/7377.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[99](https://dblp.org/pid/151/8848.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ming-Ming Cheng](https://dblp.org/pid/45/7592.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[100](https://dblp.org/pid/151/8848.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shen Cheng](https://dblp.org/pid/176/7871.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[101](https://dblp.org/pid/151/8848.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yangming Cheng](https://dblp.org/pid/340/1285.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[102](https://dblp.org/pid/151/8848.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ziyi Cheng](https://dblp.org/pid/290/9342.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[103](https://dblp.org/pid/151/8848.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ajad Chhatkuli](https://dblp.org/pid/149/7655.html)

[\[c82\]](https://dblp.org/pid/151/8848.html#c82) [\[i48\]](https://dblp.org/pid/151/8848.html#i48)

[104](https://dblp.org/pid/151/8848.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhizhen Chi](https://dblp.org/pid/188/7596.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[105](https://dblp.org/pid/151/8848.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yu-Chen Chiu](https://dblp.org/pid/199/2494.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[106](https://dblp.org/pid/151/8848.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jaeil Cho](https://dblp.org/pid/24/8639.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[107](https://dblp.org/pid/151/8848.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wooyeong Cho](https://dblp.org/pid/227/6116.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[108](https://dblp.org/pid/151/8848.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jin Young Choi 0002](https://dblp.org/pid/30/1428-2.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[109](https://dblp.org/pid/151/8848.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jinwoo Choi 0001](https://dblp.org/pid/47/2621-1.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[110](https://dblp.org/pid/151/8848.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jongwon Choi 0002](https://dblp.org/pid/126/0675-2.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[111](https://dblp.org/pid/151/8848.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jun-Ho Choi](https://dblp.org/pid/139/4714.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[112](https://dblp.org/pid/151/8848.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Seokeon Choi](https://dblp.org/pid/214/2200.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[113](https://dblp.org/pid/151/8848.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sunglok Choi](https://dblp.org/pid/53/7746.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[114](https://dblp.org/pid/151/8848.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hisham Cholakkal](https://dblp.org/pid/129/2046.html)

[\[c91\]](https://dblp.org/pid/151/8848.html#c91) [\[i65\]](https://dblp.org/pid/151/8848.html#i65)

[115](https://dblp.org/pid/151/8848.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lutao Chu](https://dblp.org/pid/234/0100.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[116](https://dblp.org/pid/151/8848.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Se Young Chun](https://dblp.org/pid/85/2542.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[117](https://dblp.org/pid/151/8848.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Angelo Ciaramella](https://dblp.org/pid/37/6845.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[118](https://dblp.org/pid/151/8848.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ozgun Cirakman](https://dblp.org/pid/86/8843.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[119](https://dblp.org/pid/151/8848.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Edo Collins](https://dblp.org/pid/176/2794.html)

[\[c99\]](https://dblp.org/pid/151/8848.html#c99) [\[i90\]](https://dblp.org/pid/151/8848.html#i90)

[120](https://dblp.org/pid/151/8848.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[121](https://dblp.org/pid/151/8848.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[122](https://dblp.org/pid/151/8848.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dengxin Dai](https://dblp.org/pid/98/8616.html)

[\[c105\]](https://dblp.org/pid/151/8848.html#c105) [\[j4\]](https://dblp.org/pid/151/8848.html#j4) [\[c85\]](https://dblp.org/pid/151/8848.html#c85) [\[c82\]](https://dblp.org/pid/151/8848.html#c82) [\[i73\]](https://dblp.org/pid/151/8848.html#i73) [\[i53\]](https://dblp.org/pid/151/8848.html#i53) [\[i48\]](https://dblp.org/pid/151/8848.html#i48)

[123](https://dblp.org/pid/151/8848.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kenan Dai](https://dblp.org/pid/250/4445.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[124](https://dblp.org/pid/151/8848.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[125](https://dblp.org/pid/151/8848.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yiannis Demiris](https://dblp.org/pid/47/1473.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[126](https://dblp.org/pid/151/8848.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chunyuan Deng](https://dblp.org/pid/154/4071.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[127](https://dblp.org/pid/151/8848.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[128](https://dblp.org/pid/151/8848.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wei Deng](https://dblp.org/pid/69/508.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[129](https://dblp.org/pid/151/8848.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zijun Deng](https://dblp.org/pid/222/7952.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[130](https://dblp.org/pid/151/8848.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Debajyoti Dhar](https://dblp.org/pid/128/3182.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[131](https://dblp.org/pid/151/8848.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shangzhe Di](https://dblp.org/pid/304/1344.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[132](https://dblp.org/pid/151/8848.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Aleksandar Dimitriev](https://dblp.org/pid/160/3686.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[133](https://dblp.org/pid/151/8848.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Henghui Ding](https://dblp.org/pid/230/1216.html)

[\[c106\]](https://dblp.org/pid/151/8848.html#c106) [\[c104\]](https://dblp.org/pid/151/8848.html#c104) [\[i89\]](https://dblp.org/pid/151/8848.html#i89) [\[i88\]](https://dblp.org/pid/151/8848.html#i88) [\[c79\]](https://dblp.org/pid/151/8848.html#c79) [\[c76\]](https://dblp.org/pid/151/8848.html#c76) [\[i67\]](https://dblp.org/pid/151/8848.html#i67) [\[i66\]](https://dblp.org/pid/151/8848.html#i66)

[134](https://dblp.org/pid/151/8848.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiaming Ding](https://dblp.org/pid/274/2850.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[135](https://dblp.org/pid/151/8848.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yifu Ding](https://dblp.org/pid/219/1995.html)

[\[c96\]](https://dblp.org/pid/151/8848.html#c96)

[136](https://dblp.org/pid/151/8848.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Patrick Doherty 0001](https://dblp.org/pid/81/3618.html)

[\[c9\]](https://dblp.org/pid/151/8848.html#c9) [\[c1\]](https://dblp.org/pid/151/8848.html#c1)

[137](https://dblp.org/pid/151/8848.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chao Dong 0005](https://dblp.org/pid/16/1278-5.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[138](https://dblp.org/pid/151/8848.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiahua Dong 0001](https://dblp.org/pid/247/5746.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[139](https://dblp.org/pid/151/8848.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xingping Dong](https://dblp.org/pid/156/3020.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[140](https://dblp.org/pid/151/8848.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuan Dong](https://dblp.org/pid/66/875.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[141](https://dblp.org/pid/151/8848.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[142](https://dblp.org/pid/151/8848.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Isabela Drummond](https://dblp.org/pid/45/3169.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[143](https://dblp.org/pid/151/8848.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dalong Du](https://dblp.org/pid/159/2057.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[144](https://dblp.org/pid/151/8848.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[145](https://dblp.org/pid/151/8848.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dawei Du](https://dblp.org/pid/51/6958.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[146](https://dblp.org/pid/151/8848.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hao Du 0006](https://dblp.org/pid/13/6441-6.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[147](https://dblp.org/pid/151/8848.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Akshay Dudhane](https://dblp.org/pid/213/7979.html)

[\[c91\]](https://dblp.org/pid/151/8848.html#c91) [\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i65\]](https://dblp.org/pid/151/8848.html#i65)

[148](https://dblp.org/pid/151/8848.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Stefan Duffner](https://dblp.org/pid/64/6849.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[149](https://dblp.org/pid/151/8848.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[150](https://dblp.org/pid/151/8848.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Benjamin Dzubur](https://dblp.org/pid/340/1520.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[151](https://dblp.org/pid/151/8848.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Johan Edstedt](https://dblp.org/pid/289/1724.html)

[\[c81\]](https://dblp.org/pid/151/8848.html#c81) [\[i56\]](https://dblp.org/pid/151/8848.html#i56) [\[i46\]](https://dblp.org/pid/151/8848.html#i46)

[152](https://dblp.org/pid/151/8848.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mostafa El-Khamy](https://dblp.org/pid/00/4303.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[153](https://dblp.org/pid/151/8848.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Abdelrahman Eldesokey](https://dblp.org/pid/154/9080.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[154](https://dblp.org/pid/151/8848.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Aykut Erdem](https://dblp.org/pid/04/1832.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[155](https://dblp.org/pid/151/8848.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Erkut Erdem](https://dblp.org/pid/79/6569.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[156](https://dblp.org/pid/151/8848.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Richard M. Everson](https://dblp.org/pid/07/6331.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[157](https://dblp.org/pid/151/8848.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haoqiang Fan](https://dblp.org/pid/143/7181.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[158](https://dblp.org/pid/151/8848.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Heng Fan 0001](https://dblp.org/pid/20/10120-1.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[159](https://dblp.org/pid/151/8848.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Nana Fan](https://dblp.org/pid/146/8400.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[160](https://dblp.org/pid/151/8848.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yingruo Fan](https://dblp.org/pid/213/4195.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[161](https://dblp.org/pid/151/8848.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chen Fang](https://dblp.org/pid/60/2548.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[162](https://dblp.org/pid/151/8848.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[j8\]](https://dblp.org/pid/151/8848.html#j8) [\[j7\]](https://dblp.org/pid/151/8848.html#j7) [\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c81\]](https://dblp.org/pid/151/8848.html#c81) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c65\]](https://dblp.org/pid/151/8848.html#c65) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[i56\]](https://dblp.org/pid/151/8848.html#i56) [\[i46\]](https://dblp.org/pid/151/8848.html#i46) [\[i42\]](https://dblp.org/pid/151/8848.html#i42) [\[c47\]](https://dblp.org/pid/151/8848.html#c47) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c40\]](https://dblp.org/pid/151/8848.html#c40) [\[i40\]](https://dblp.org/pid/151/8848.html#i40) [\[i38\]](https://dblp.org/pid/151/8848.html#i38) [\[i25\]](https://dblp.org/pid/151/8848.html#i25) [\[j3\]](https://dblp.org/pid/151/8848.html#j3) [\[c36\]](https://dblp.org/pid/151/8848.html#c36) [\[c35\]](https://dblp.org/pid/151/8848.html#c35) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[i21\]](https://dblp.org/pid/151/8848.html#i21) [\[c25\]](https://dblp.org/pid/151/8848.html#c25) [\[c24\]](https://dblp.org/pid/151/8848.html#c24) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c22\]](https://dblp.org/pid/151/8848.html#c22) [\[c21\]](https://dblp.org/pid/151/8848.html#c21) [\[i13\]](https://dblp.org/pid/151/8848.html#i13) [\[i12\]](https://dblp.org/pid/151/8848.html#i12) [\[i10\]](https://dblp.org/pid/151/8848.html#i10) [\[i9\]](https://dblp.org/pid/151/8848.html#i9) [\[j1\]](https://dblp.org/pid/151/8848.html#j1) [\[c20\]](https://dblp.org/pid/151/8848.html#c20) [\[c19\]](https://dblp.org/pid/151/8848.html#c19) [\[c18\]](https://dblp.org/pid/151/8848.html#c18) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[i8\]](https://dblp.org/pid/151/8848.html#i8) [\[i7\]](https://dblp.org/pid/151/8848.html#i7) [\[c16\]](https://dblp.org/pid/151/8848.html#c16) [\[c15\]](https://dblp.org/pid/151/8848.html#c15) [\[c14\]](https://dblp.org/pid/151/8848.html#c14) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c11\]](https://dblp.org/pid/151/8848.html#c11) [\[c10\]](https://dblp.org/pid/151/8848.html#c10) [\[c9\]](https://dblp.org/pid/151/8848.html#c9) [\[i6\]](https://dblp.org/pid/151/8848.html#i6) [\[i5\]](https://dblp.org/pid/151/8848.html#i5) [\[i4\]](https://dblp.org/pid/151/8848.html#i4) [\[i3\]](https://dblp.org/pid/151/8848.html#i3) [\[i2\]](https://dblp.org/pid/151/8848.html#i2) [\[i1\]](https://dblp.org/pid/151/8848.html#i1) [\[c8\]](https://dblp.org/pid/151/8848.html#c8) [\[c7\]](https://dblp.org/pid/151/8848.html#c7) [\[c6\]](https://dblp.org/pid/151/8848.html#c6) [\[c5\]](https://dblp.org/pid/151/8848.html#c5) [\[c4\]](https://dblp.org/pid/151/8848.html#c4) [\[c3\]](https://dblp.org/pid/151/8848.html#c3) [\[c2\]](https://dblp.org/pid/151/8848.html#c2) [\[c1\]](https://dblp.org/pid/151/8848.html#c1)

[163](https://dblp.org/pid/151/8848.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiayi Feng](https://dblp.org/pid/176/1403.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[164](https://dblp.org/pid/151/8848.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wei Feng 0005](https://dblp.org/pid/17/1152-5.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[165](https://dblp.org/pid/151/8848.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[166](https://dblp.org/pid/151/8848.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhiyong Feng 0001](https://dblp.org/pid/48/195-1.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[167](https://dblp.org/pid/151/8848.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[168](https://dblp.org/pid/151/8848.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Vittorio Ferrari](https://dblp.org/pid/16/3608.html)

[\[c107\]](https://dblp.org/pid/151/8848.html#c107) [\[i62\]](https://dblp.org/pid/151/8848.html#i62)

[169](https://dblp.org/pid/151/8848.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tobias Fischer 0001](https://dblp.org/pid/181/3897.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[170](https://dblp.org/pid/151/8848.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tobias Fischer 0004](https://dblp.org/pid/249/9213.html)

[\[c106\]](https://dblp.org/pid/151/8848.html#c106) [\[c103\]](https://dblp.org/pid/151/8848.html#c103) [\[i88\]](https://dblp.org/pid/151/8848.html#i88) [\[i80\]](https://dblp.org/pid/151/8848.html#i80)

[171](https://dblp.org/pid/151/8848.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Gian Luca Foresti](https://dblp.org/pid/93/5522.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[172](https://dblp.org/pid/151/8848.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Per-Erik Forssén](https://dblp.org/pid/84/306.html)

[\[c24\]](https://dblp.org/pid/151/8848.html#c24) [\[i13\]](https://dblp.org/pid/151/8848.html#i13)

[173](https://dblp.org/pid/151/8848.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Manuel Fritsche](https://dblp.org/pid/228/6850.html)

[\[c29\]](https://dblp.org/pid/151/8848.html#c29) [\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[174](https://dblp.org/pid/151/8848.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jianlong Fu](https://dblp.org/pid/83/8692.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[175](https://dblp.org/pid/151/8848.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[176](https://dblp.org/pid/151/8848.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dario Fuoli](https://dblp.org/pid/260/3093.html)

[\[c94\]](https://dblp.org/pid/151/8848.html#c94) [\[i74\]](https://dblp.org/pid/151/8848.html#i74) [\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33) [\[c26\]](https://dblp.org/pid/151/8848.html#c26)

[177](https://dblp.org/pid/151/8848.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hamed Kiani Galoogahi](https://dblp.org/pid/119/0363.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[178](https://dblp.org/pid/151/8848.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ruipeng Gang](https://dblp.org/pid/252/5526.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[179](https://dblp.org/pid/151/8848.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jian Gao 0008](https://dblp.org/pid/02/563-8.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[180](https://dblp.org/pid/151/8848.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jie Gao](https://dblp.org/pid/181/2794.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[181](https://dblp.org/pid/151/8848.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jin Gao](https://dblp.org/pid/13/1653.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[182](https://dblp.org/pid/151/8848.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Junyu Gao 0002](https://dblp.org/pid/153/4522-2.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[183](https://dblp.org/pid/151/8848.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ke Gao 0003](https://dblp.org/pid/81/2423-3.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[184](https://dblp.org/pid/151/8848.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shang Gao 0012](https://dblp.org/pid/28/435-12.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[185](https://dblp.org/pid/151/8848.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xinbo Gao 0001](https://dblp.org/pid/99/4522.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28) [\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[186](https://dblp.org/pid/151/8848.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Christophe Garcia](https://dblp.org/pid/26/6493.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[187](https://dblp.org/pid/151/8848.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Álvaro García-Martín](https://dblp.org/pid/39/1542.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[188](https://dblp.org/pid/151/8848.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Efstratios Gavves](https://dblp.org/pid/03/8693.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[189](https://dblp.org/pid/151/8848.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shiming Ge](https://dblp.org/pid/93/8104.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[190](https://dblp.org/pid/151/8848.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Awet Haileslassie Gebrehiwot](https://dblp.org/pid/284/2554.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[191](https://dblp.org/pid/151/8848.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wafa Al Ghallabi](https://dblp.org/pid/326/6543.html)

[\[c91\]](https://dblp.org/pid/151/8848.html#c91) [\[i65\]](https://dblp.org/pid/151/8848.html#i65)

[192](https://dblp.org/pid/151/8848.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hossein Ghanei-Yakhdan](https://dblp.org/pid/188/5964.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[193](https://dblp.org/pid/151/8848.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bernard Ghanem](https://dblp.org/pid/37/2516.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[194](https://dblp.org/pid/151/8848.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Susanna Gladh](https://dblp.org/pid/192/1542.html)

[\[j3\]](https://dblp.org/pid/151/8848.html#j3) [\[c10\]](https://dblp.org/pid/151/8848.html#c10) [\[i1\]](https://dblp.org/pid/151/8848.html#i1)

[195](https://dblp.org/pid/151/8848.html?view=joint&param=195 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Stuart Golodetz](https://dblp.org/pid/34/4052.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[196](https://dblp.org/pid/151/8848.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rui Gong](https://dblp.org/pid/75/1938.html)

[\[c116\]](https://dblp.org/pid/151/8848.html#c116) [\[c105\]](https://dblp.org/pid/151/8848.html#c105) [\[i84\]](https://dblp.org/pid/151/8848.html#i84) [\[c82\]](https://dblp.org/pid/151/8848.html#c82) [\[i48\]](https://dblp.org/pid/151/8848.html#i48)

[197](https://dblp.org/pid/151/8848.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Abel Gonzalez-Garcia](https://dblp.org/pid/156/0213.html)

aka: Abel González-García

[\[j2\]](https://dblp.org/pid/151/8848.html#j2) [\[c34\]](https://dblp.org/pid/151/8848.html#c34) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c31\]](https://dblp.org/pid/151/8848.html#c31) [\[i19\]](https://dblp.org/pid/151/8848.html#i19) [\[i18\]](https://dblp.org/pid/151/8848.html#i18) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[i11\]](https://dblp.org/pid/151/8848.html#i11)

[198](https://dblp.org/pid/151/8848.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c119\]](https://dblp.org/pid/151/8848.html#c119) [\[c116\]](https://dblp.org/pid/151/8848.html#c116) [\[c115\]](https://dblp.org/pid/151/8848.html#c115) [\[c114\]](https://dblp.org/pid/151/8848.html#c114) [\[c113\]](https://dblp.org/pid/151/8848.html#c113) [\[c109\]](https://dblp.org/pid/151/8848.html#c109) [\[c108\]](https://dblp.org/pid/151/8848.html#c108) [\[c107\]](https://dblp.org/pid/151/8848.html#c107) [\[i94\]](https://dblp.org/pid/151/8848.html#i94) [\[i93\]](https://dblp.org/pid/151/8848.html#i93) [\[i92\]](https://dblp.org/pid/151/8848.html#i92) [\[j6\]](https://dblp.org/pid/151/8848.html#j6) [\[c105\]](https://dblp.org/pid/151/8848.html#c105) [\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c99\]](https://dblp.org/pid/151/8848.html#c99) [\[c95\]](https://dblp.org/pid/151/8848.html#c95) [\[c94\]](https://dblp.org/pid/151/8848.html#c94) [\[i90\]](https://dblp.org/pid/151/8848.html#i90) [\[i87\]](https://dblp.org/pid/151/8848.html#i87) [\[i84\]](https://dblp.org/pid/151/8848.html#i84) [\[i79\]](https://dblp.org/pid/151/8848.html#i79) [\[i77\]](https://dblp.org/pid/151/8848.html#i77) [\[j4\]](https://dblp.org/pid/151/8848.html#j4) [\[c93\]](https://dblp.org/pid/151/8848.html#c93) [\[c91\]](https://dblp.org/pid/151/8848.html#c91) [\[c87\]](https://dblp.org/pid/151/8848.html#c87) [\[c86\]](https://dblp.org/pid/151/8848.html#c86) [\[c85\]](https://dblp.org/pid/151/8848.html#c85) [\[c84\]](https://dblp.org/pid/151/8848.html#c84) [\[c83\]](https://dblp.org/pid/151/8848.html#c83) [\[c82\]](https://dblp.org/pid/151/8848.html#c82) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c78\]](https://dblp.org/pid/151/8848.html#c78) [\[c77\]](https://dblp.org/pid/151/8848.html#c77) [\[c75\]](https://dblp.org/pid/151/8848.html#c75) [\[c73\]](https://dblp.org/pid/151/8848.html#c73) [\[i76\]](https://dblp.org/pid/151/8848.html#i76) [\[i75\]](https://dblp.org/pid/151/8848.html#i75) [\[i74\]](https://dblp.org/pid/151/8848.html#i74) [\[i73\]](https://dblp.org/pid/151/8848.html#i73) [\[i72\]](https://dblp.org/pid/151/8848.html#i72) [\[i71\]](https://dblp.org/pid/151/8848.html#i71) [\[i70\]](https://dblp.org/pid/151/8848.html#i70) [\[i69\]](https://dblp.org/pid/151/8848.html#i69) [\[i68\]](https://dblp.org/pid/151/8848.html#i68) [\[i65\]](https://dblp.org/pid/151/8848.html#i65) [\[i64\]](https://dblp.org/pid/151/8848.html#i64) [\[i62\]](https://dblp.org/pid/151/8848.html#i62) [\[c72\]](https://dblp.org/pid/151/8848.html#c72) [\[c69\]](https://dblp.org/pid/151/8848.html#c69) [\[c67\]](https://dblp.org/pid/151/8848.html#c67) [\[c66\]](https://dblp.org/pid/151/8848.html#c66) [\[c64\]](https://dblp.org/pid/151/8848.html#c64) [\[c63\]](https://dblp.org/pid/151/8848.html#c63) [\[c62\]](https://dblp.org/pid/151/8848.html#c62) [\[c61\]](https://dblp.org/pid/151/8848.html#c61) [\[c60\]](https://dblp.org/pid/151/8848.html#c60) [\[c59\]](https://dblp.org/pid/151/8848.html#c59) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c57\]](https://dblp.org/pid/151/8848.html#c57) [\[c56\]](https://dblp.org/pid/151/8848.html#c56) [\[i61\]](https://dblp.org/pid/151/8848.html#i61) [\[i60\]](https://dblp.org/pid/151/8848.html#i60) [\[i59\]](https://dblp.org/pid/151/8848.html#i59) [\[i58\]](https://dblp.org/pid/151/8848.html#i58) [\[i57\]](https://dblp.org/pid/151/8848.html#i57) [\[i55\]](https://dblp.org/pid/151/8848.html#i55) [\[i54\]](https://dblp.org/pid/151/8848.html#i54) [\[i53\]](https://dblp.org/pid/151/8848.html#i53) [\[i50\]](https://dblp.org/pid/151/8848.html#i50) [\[i49\]](https://dblp.org/pid/151/8848.html#i49) [\[i48\]](https://dblp.org/pid/151/8848.html#i48) [\[i47\]](https://dblp.org/pid/151/8848.html#i47) [\[i44\]](https://dblp.org/pid/151/8848.html#i44) [\[i41\]](https://dblp.org/pid/151/8848.html#i41) [\[c48\]](https://dblp.org/pid/151/8848.html#c48) [\[c45\]](https://dblp.org/pid/151/8848.html#c45) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c42\]](https://dblp.org/pid/151/8848.html#c42) [\[c41\]](https://dblp.org/pid/151/8848.html#c41) [\[c40\]](https://dblp.org/pid/151/8848.html#c40) [\[c38\]](https://dblp.org/pid/151/8848.html#c38) [\[i39\]](https://dblp.org/pid/151/8848.html#i39) [\[i38\]](https://dblp.org/pid/151/8848.html#i38) [\[i37\]](https://dblp.org/pid/151/8848.html#i37) [\[i32\]](https://dblp.org/pid/151/8848.html#i32) [\[i31\]](https://dblp.org/pid/151/8848.html#i31) [\[i30\]](https://dblp.org/pid/151/8848.html#i30) [\[i27\]](https://dblp.org/pid/151/8848.html#i27) [\[i26\]](https://dblp.org/pid/151/8848.html#i26) [\[i23\]](https://dblp.org/pid/151/8848.html#i23) [\[c37\]](https://dblp.org/pid/151/8848.html#c37) [\[c33\]](https://dblp.org/pid/151/8848.html#c33) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[i22\]](https://dblp.org/pid/151/8848.html#i22)

[199](https://dblp.org/pid/151/8848.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[200](https://dblp.org/pid/151/8848.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rama Krishna Sai S. Gorthi](https://dblp.org/pid/45/7595.html)

aka: Rama Krishna Sai Subrahmanyam Gorthi

aka: Gorthi R. K. Sai Subrahmanyam

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[201](https://dblp.org/pid/151/8848.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Eric Granger](https://dblp.org/pid/86/2306.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[202](https://dblp.org/pid/151/8848.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Karl Granström](https://dblp.org/pid/58/10006.html)

[\[c1\]](https://dblp.org/pid/151/8848.html#c1)

[203](https://dblp.org/pid/151/8848.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Klemen Grm](https://dblp.org/pid/178/5048.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[204](https://dblp.org/pid/151/8848.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Q. H. Gu](https://dblp.org/pid/340/1209.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[205](https://dblp.org/pid/151/8848.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shuhang Gu](https://dblp.org/pid/126/1028.html)

[\[c69\]](https://dblp.org/pid/151/8848.html#c69) [\[i31\]](https://dblp.org/pid/151/8848.html#i31) [\[c29\]](https://dblp.org/pid/151/8848.html#c29) [\[c28\]](https://dblp.org/pid/151/8848.html#c28) [\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[c26\]](https://dblp.org/pid/151/8848.html#c26) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[206](https://dblp.org/pid/151/8848.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yan Gu](https://dblp.org/pid/174/1818.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[207](https://dblp.org/pid/151/8848.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yang Gu](https://dblp.org/pid/01/5858.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[208](https://dblp.org/pid/151/8848.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuzhang Gu](https://dblp.org/pid/122/3790.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[209](https://dblp.org/pid/151/8848.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shuosen Guan](https://dblp.org/pid/245/8954.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[210](https://dblp.org/pid/151/8848.html?view=joint&param=210 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Erhan Gundogdu](https://dblp.org/pid/147/4597.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[211](https://dblp.org/pid/151/8848.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bilge Günsel](https://dblp.org/pid/47/5125.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[212](https://dblp.org/pid/151/8848.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Leida Guo](https://dblp.org/pid/249/8242.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[213](https://dblp.org/pid/151/8848.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qing Guo 0005](https://dblp.org/pid/25/3038-5.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[214](https://dblp.org/pid/151/8848.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Taian Guo](https://dblp.org/pid/254/9326.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[215](https://dblp.org/pid/151/8848.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhenhua Guo 0001](https://dblp.org/pid/41/294-1.html)

[\[c111\]](https://dblp.org/pid/151/8848.html#c111) [\[i82\]](https://dblp.org/pid/151/8848.html#i82)

[216](https://dblp.org/pid/151/8848.html?view=joint&param=216 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Abhinav Gupta 0001](https://dblp.org/pid/36/7024-1.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[217](https://dblp.org/pid/151/8848.html?view=joint&param=217 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Deepak Gupta](https://dblp.org/pid/65/2751.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[218](https://dblp.org/pid/151/8848.html?view=joint&param=218 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Himanshu Gupta 0003](https://dblp.org/pid/330/0760-3.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[219](https://dblp.org/pid/151/8848.html?view=joint&param=219 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Filiz Gurkan](https://dblp.org/pid/202/7040.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[220](https://dblp.org/pid/151/8848.html?view=joint&param=220 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fredrik Gustafsson](https://dblp.org/pid/394/4497.html)

[\[c54\]](https://dblp.org/pid/151/8848.html#c54) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[221](https://dblp.org/pid/151/8848.html?view=joint&param=221 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fredrik K. Gustafsson](https://dblp.org/pid/80/1759.html)

[\[j5\]](https://dblp.org/pid/151/8848.html#j5) [\[i91\]](https://dblp.org/pid/151/8848.html#i91) [\[c92\]](https://dblp.org/pid/151/8848.html#c92) [\[c68\]](https://dblp.org/pid/151/8848.html#c68) [\[i45\]](https://dblp.org/pid/151/8848.html#i45) [\[c53\]](https://dblp.org/pid/151/8848.html#c53) [\[c44\]](https://dblp.org/pid/151/8848.html#c44) [\[i35\]](https://dblp.org/pid/151/8848.html#i35) [\[i24\]](https://dblp.org/pid/151/8848.html#i24) [\[i20\]](https://dblp.org/pid/151/8848.html#i20) [\[i16\]](https://dblp.org/pid/151/8848.html#i16)

[222](https://dblp.org/pid/151/8848.html?view=joint&param=222 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Simon Hadfield](https://dblp.org/pid/33/10771.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[223](https://dblp.org/pid/151/8848.html?view=joint&param=223 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Gustav Häger](https://dblp.org/pid/157/3602.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[j1\]](https://dblp.org/pid/151/8848.html#j1) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c16\]](https://dblp.org/pid/151/8848.html#c16) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c9\]](https://dblp.org/pid/151/8848.html#c9) [\[i5\]](https://dblp.org/pid/151/8848.html#i5) [\[i4\]](https://dblp.org/pid/151/8848.html#i4) [\[i3\]](https://dblp.org/pid/151/8848.html#i3) [\[c8\]](https://dblp.org/pid/151/8848.html#c8) [\[c7\]](https://dblp.org/pid/151/8848.html#c7) [\[c6\]](https://dblp.org/pid/151/8848.html#c6) [\[c4\]](https://dblp.org/pid/151/8848.html#c4) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[224](https://dblp.org/pid/151/8848.html?view=joint&param=224 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bohyung Han](https://dblp.org/pid/73/4880.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[225](https://dblp.org/pid/151/8848.html?view=joint&param=225 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rui-Ze Han](https://dblp.org/pid/205/4022.html)

aka: Ruize Han

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[226](https://dblp.org/pid/151/8848.html?view=joint&param=226 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wencheng Han](https://dblp.org/pid/280/3348.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[227](https://dblp.org/pid/151/8848.html?view=joint&param=227 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Cong Hao](https://dblp.org/pid/129/2059.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[228](https://dblp.org/pid/151/8848.html?view=joint&param=228 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zeqi Hao](https://dblp.org/pid/348/8961.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[229](https://dblp.org/pid/151/8848.html?view=joint&param=229 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sam Hare](https://dblp.org/pid/79/10771.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[230](https://dblp.org/pid/151/8848.html?view=joint&param=230 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Muhammad Haris 0002](https://dblp.org/pid/142/1614-2.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[231](https://dblp.org/pid/151/8848.html?view=joint&param=231 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Alex Hauptmann 0001](https://dblp.org/pid/h/AlexanderGHauptmann.html)

aka: Alexander G. Hauptmann

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[232](https://dblp.org/pid/151/8848.html?view=joint&param=232 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Anfeng He](https://dblp.org/pid/188/1205.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[233](https://dblp.org/pid/151/8848.html?view=joint&param=233 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bin He](https://dblp.org/pid/78/4523.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[234](https://dblp.org/pid/151/8848.html?view=joint&param=234 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chunming He](https://dblp.org/pid/251/5104.html)

[\[c111\]](https://dblp.org/pid/151/8848.html#c111) [\[i82\]](https://dblp.org/pid/151/8848.html#i82)

[235](https://dblp.org/pid/151/8848.html?view=joint&param=235 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dongliang He](https://dblp.org/pid/167/0539.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[236](https://dblp.org/pid/151/8848.html?view=joint&param=236 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jianfeng He](https://dblp.org/pid/93/8352.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[237](https://dblp.org/pid/151/8848.html?view=joint&param=237 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jingwen He](https://dblp.org/pid/14/2195.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[238](https://dblp.org/pid/151/8848.html?view=joint&param=238 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jun-Yan He](https://dblp.org/pid/173/3747.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[239](https://dblp.org/pid/151/8848.html?view=joint&param=239 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Keji He](https://dblp.org/pid/319/4518.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[240](https://dblp.org/pid/151/8848.html?view=joint&param=240 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Linbo He](https://dblp.org/pid/26/741.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[241](https://dblp.org/pid/151/8848.html?view=joint&param=241 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiangyu He](https://dblp.org/pid/173/4661.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[242](https://dblp.org/pid/151/8848.html?view=joint&param=242 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhenyu He 0001](https://dblp.org/pid/57/6240-1.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[243](https://dblp.org/pid/151/8848.html?view=joint&param=243 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhiqun He](https://dblp.org/pid/213/4141.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[244](https://dblp.org/pid/151/8848.html?view=joint&param=244 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fredrik Heintz](https://dblp.org/pid/86/6319.html)

[\[c1\]](https://dblp.org/pid/151/8848.html#c1)

[245](https://dblp.org/pid/151/8848.html?view=joint&param=245 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Majed El Helou](https://dblp.org/pid/214/9598.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[246](https://dblp.org/pid/151/8848.html?view=joint&param=246 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Cherkeng Heng](https://dblp.org/pid/49/9606.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[247](https://dblp.org/pid/151/8848.html?view=joint&param=247 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[João F. Henriques](https://dblp.org/pid/31/8617.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[248](https://dblp.org/pid/151/8848.html?view=joint&param=248 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jorge Rodríguez Herranz](https://dblp.org/pid/233/9954.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[249](https://dblp.org/pid/151/8848.html?view=joint&param=249 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chiu Man Ho](https://dblp.org/pid/228/8363.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[250](https://dblp.org/pid/151/8848.html?view=joint&param=250 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Seunghoon Hong](https://dblp.org/pid/142/3014.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[251](https://dblp.org/pid/151/8848.html?view=joint&param=251 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dmitry Hrybov](https://dblp.org/pid/264/5801.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[252](https://dblp.org/pid/151/8848.html?view=joint&param=252 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chih-Chung Hsu](https://dblp.org/pid/35/547.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[253](https://dblp.org/pid/151/8848.html?view=joint&param=253 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tao Hu 0011](https://dblp.org/pid/41/5865-11.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[254](https://dblp.org/pid/151/8848.html?view=joint&param=254 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Weiming Hu](https://dblp.org/pid/41/6824.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[255](https://dblp.org/pid/151/8848.html?view=joint&param=255 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Weiming Hu 0004](https://dblp.org/pid/41/6824-4.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[256](https://dblp.org/pid/151/8848.html?view=joint&param=256 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiantao Hu](https://dblp.org/pid/160/8016.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[257](https://dblp.org/pid/151/8848.html?view=joint&param=257 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chang Huang](https://dblp.org/pid/17/2241.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[258](https://dblp.org/pid/151/8848.html?view=joint&param=258 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Guan Huang 0003](https://dblp.org/pid/93/10768-3.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[259](https://dblp.org/pid/151/8848.html?view=joint&param=259 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jie Huang 0017](https://dblp.org/pid/29/6643-17.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[260](https://dblp.org/pid/151/8848.html?view=joint&param=260 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kaer Huang](https://dblp.org/pid/317/0780.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[261](https://dblp.org/pid/151/8848.html?view=joint&param=261 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Liufeng Huang](https://dblp.org/pid/327/3404.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[262](https://dblp.org/pid/151/8848.html?view=joint&param=262 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qingming Huang](https://dblp.org/pid/68/4388.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[263](https://dblp.org/pid/151/8848.html?view=joint&param=263 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shuangping Huang](https://dblp.org/pid/26/7950.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[264](https://dblp.org/pid/151/8848.html?view=joint&param=264 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Thomas E. Huang](https://dblp.org/pid/260/6642.html)

[\[c79\]](https://dblp.org/pid/151/8848.html#c79) [\[i67\]](https://dblp.org/pid/151/8848.html#i67)

[265](https://dblp.org/pid/151/8848.html?view=joint&param=265 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yan Huang 0008](https://dblp.org/pid/75/6434-8.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[266](https://dblp.org/pid/151/8848.html?view=joint&param=266 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yanyan Huang](https://dblp.org/pid/88/4316.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[267](https://dblp.org/pid/151/8848.html?view=joint&param=267 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuanfei Huang](https://dblp.org/pid/207/5397.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[268](https://dblp.org/pid/151/8848.html?view=joint&param=268 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuqing Huang](https://dblp.org/pid/134/5853.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[269](https://dblp.org/pid/151/8848.html?view=joint&param=269 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhiwu Huang](https://dblp.org/pid/47/7711.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33) [\[c26\]](https://dblp.org/pid/151/8848.html#c26)

[270](https://dblp.org/pid/151/8848.html?view=joint&param=270 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhongjian Huang](https://dblp.org/pid/251/0619.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[271](https://dblp.org/pid/151/8848.html?view=joint&param=271 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wolfgang Hübner 0001](https://dblp.org/pid/97/2668-1.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[272](https://dblp.org/pid/151/8848.html?view=joint&param=272 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=2)

[Vahan Huroyan](https://dblp.org/pid/200/8385.html)

[\[i96\]](https://dblp.org/pid/151/8848.html#i96)

[273](https://dblp.org/pid/151/8848.html?view=joint&param=273 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiwon Hwang](https://dblp.org/pid/157/7832.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[274](https://dblp.org/pid/151/8848.html?view=joint&param=274 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Álvaro Iglesias-Arias](https://dblp.org/pid/234/0091.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[275](https://dblp.org/pid/151/8848.html?view=joint&param=275 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Michal Irani](https://dblp.org/pid/04/3190.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27)

[276](https://dblp.org/pid/151/8848.html?view=joint&param=276 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shipra Jain](https://dblp.org/pid/143/8973.html)

[\[c62\]](https://dblp.org/pid/151/8848.html#c62) [\[i23\]](https://dblp.org/pid/151/8848.html#i23)

[277](https://dblp.org/pid/151/8848.html?view=joint&param=277 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Deepak Jangid](https://dblp.org/pid/340/1460.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[278](https://dblp.org/pid/151/8848.html?view=joint&param=278 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sajid Javed](https://dblp.org/pid/143/2961.html)

[\[j7\]](https://dblp.org/pid/151/8848.html#j7) [\[i42\]](https://dblp.org/pid/151/8848.html#i42)

[279](https://dblp.org/pid/151/8848.html?view=joint&param=279 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Geun-Woo Jeon](https://dblp.org/pid/274/3180.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[280](https://dblp.org/pid/151/8848.html?view=joint&param=280 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jae-chan Jeong](https://dblp.org/pid/157/3590.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[281](https://dblp.org/pid/151/8848.html?view=joint&param=281 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiyeoup Jeong](https://dblp.org/pid/152/5790.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[282](https://dblp.org/pid/151/8848.html?view=joint&param=282 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Allan Douglas Jepson](https://dblp.org/pid/93/4241.html)

aka: Allan D. Jepson

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[283](https://dblp.org/pid/151/8848.html?view=joint&param=283 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[284](https://dblp.org/pid/151/8848.html?view=joint&param=284 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[285](https://dblp.org/pid/151/8848.html?view=joint&param=285 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaozhong Ji](https://dblp.org/pid/237/9544.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[286](https://dblp.org/pid/151/8848.html?view=joint&param=286 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiaya Jia](https://dblp.org/pid/31/5649.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[287](https://dblp.org/pid/151/8848.html?view=joint&param=287 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lanpeng Jia](https://dblp.org/pid/248/9198.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[288](https://dblp.org/pid/151/8848.html?view=joint&param=288 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[289](https://dblp.org/pid/151/8848.html?view=joint&param=289 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiande Jiang](https://dblp.org/pid/264/5784.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[290](https://dblp.org/pid/151/8848.html?view=joint&param=290 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Junjun Jiang](https://dblp.org/pid/119/0230.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[291](https://dblp.org/pid/151/8848.html?view=joint&param=291 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kui Jiang](https://dblp.org/pid/124/2034.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[292](https://dblp.org/pid/151/8848.html?view=joint&param=292 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yi Jiang 0004](https://dblp.org/pid/66/3172-4.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[293](https://dblp.org/pid/151/8848.html?view=joint&param=293 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[294](https://dblp.org/pid/151/8848.html?view=joint&param=294 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yifan Jiao](https://dblp.org/pid/214/4159.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[295](https://dblp.org/pid/151/8848.html?view=joint&param=295 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[C. Victor Jiji](https://dblp.org/pid/75/3033.html)

aka: C. V. Jiji

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[296](https://dblp.org/pid/151/8848.html?view=joint&param=296 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Longcun Jin](https://dblp.org/pid/51/7090.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[297](https://dblp.org/pid/151/8848.html?view=joint&param=297 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Youngsu Jo](https://dblp.org/pid/327/3609.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[298](https://dblp.org/pid/151/8848.html?view=joint&param=298 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Joakim Johnander](https://dblp.org/pid/202/2479.html)

[\[j8\]](https://dblp.org/pid/151/8848.html#j8) [\[c81\]](https://dblp.org/pid/151/8848.html#c81) [\[c65\]](https://dblp.org/pid/151/8848.html#c65) [\[i56\]](https://dblp.org/pid/151/8848.html#i56) [\[i46\]](https://dblp.org/pid/151/8848.html#i46) [\[i25\]](https://dblp.org/pid/151/8848.html#i25) [\[c35\]](https://dblp.org/pid/151/8848.html#c35) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c22\]](https://dblp.org/pid/151/8848.html#c22) [\[c21\]](https://dblp.org/pid/151/8848.html#c21) [\[i12\]](https://dblp.org/pid/151/8848.html#i12) [\[i9\]](https://dblp.org/pid/151/8848.html#i9) [\[c20\]](https://dblp.org/pid/151/8848.html#c20) [\[i7\]](https://dblp.org/pid/151/8848.html#i7)

[299](https://dblp.org/pid/151/8848.html?view=joint&param=299 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Nam Hyung Joon](https://dblp.org/pid/254/1586.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[300](https://dblp.org/pid/151/8848.html?view=joint&param=300 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[301](https://dblp.org/pid/151/8848.html?view=joint&param=301 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ho Min Jung](https://dblp.org/pid/36/5839.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[302](https://dblp.org/pid/151/8848.html?view=joint&param=302 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sumithra Kakanuru](https://dblp.org/pid/188/7777.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[303](https://dblp.org/pid/151/8848.html?view=joint&param=303 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[304](https://dblp.org/pid/151/8848.html?view=joint&param=304 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Menelaos Kanakis](https://dblp.org/pid/208/1757.html)

[\[c95\]](https://dblp.org/pid/151/8848.html#c95) [\[i41\]](https://dblp.org/pid/151/8848.html#i41)

[305](https://dblp.org/pid/151/8848.html?view=joint&param=305 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Praveen Kandula](https://dblp.org/pid/228/6711.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28) [\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[306](https://dblp.org/pid/151/8848.html?view=joint&param=306 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ben Kang](https://dblp.org/pid/340/1671.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[307](https://dblp.org/pid/151/8848.html?view=joint&param=307 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jung Heum Kang](https://dblp.org/pid/274/1655.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[308](https://dblp.org/pid/151/8848.html?view=joint&param=308 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Myunggu Kang](https://dblp.org/pid/76/8374.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[309](https://dblp.org/pid/151/8848.html?view=joint&param=309 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sukju Kang](https://dblp.org/pid/327/3219.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[310](https://dblp.org/pid/151/8848.html?view=joint&param=310 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ze Kang](https://dblp.org/pid/340/1063.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[311](https://dblp.org/pid/151/8848.html?view=joint&param=311 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jani Käpylä](https://dblp.org/pid/244/2529.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[312](https://dblp.org/pid/151/8848.html?view=joint&param=312 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Daniya Kareem](https://dblp.org/pid/340/1779.html)

[\[c91\]](https://dblp.org/pid/151/8848.html#c91)

[313](https://dblp.org/pid/151/8848.html?view=joint&param=313 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shohreh Kasaei](https://dblp.org/pid/78/5062.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[314](https://dblp.org/pid/151/8848.html?view=joint&param=314 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Iason Kastanis](https://dblp.org/pid/52/4455.html)

[\[c108\]](https://dblp.org/pid/151/8848.html#c108) [\[i87\]](https://dblp.org/pid/151/8848.html#i87) [\[c83\]](https://dblp.org/pid/151/8848.html#c83) [\[i68\]](https://dblp.org/pid/151/8848.html#i68)

[315](https://dblp.org/pid/151/8848.html?view=joint&param=315 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lei Ke](https://dblp.org/pid/26/5225.html)

[\[c117\]](https://dblp.org/pid/151/8848.html#c117) [\[c115\]](https://dblp.org/pid/151/8848.html#c115) [\[c113\]](https://dblp.org/pid/151/8848.html#c113) [\[c112\]](https://dblp.org/pid/151/8848.html#c112) [\[i94\]](https://dblp.org/pid/151/8848.html#i94) [\[i92\]](https://dblp.org/pid/151/8848.html#i92) [\[c106\]](https://dblp.org/pid/151/8848.html#c106) [\[c104\]](https://dblp.org/pid/151/8848.html#c104) [\[c102\]](https://dblp.org/pid/151/8848.html#c102) [\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c98\]](https://dblp.org/pid/151/8848.html#c98) [\[c97\]](https://dblp.org/pid/151/8848.html#c97) [\[i89\]](https://dblp.org/pid/151/8848.html#i89) [\[i88\]](https://dblp.org/pid/151/8848.html#i88) [\[i86\]](https://dblp.org/pid/151/8848.html#i86) [\[i85\]](https://dblp.org/pid/151/8848.html#i85) [\[i83\]](https://dblp.org/pid/151/8848.html#i83) [\[i78\]](https://dblp.org/pid/151/8848.html#i78) [\[c88\]](https://dblp.org/pid/151/8848.html#c88) [\[c76\]](https://dblp.org/pid/151/8848.html#c76) [\[i66\]](https://dblp.org/pid/151/8848.html#i66) [\[c55\]](https://dblp.org/pid/151/8848.html#c55) [\[i51\]](https://dblp.org/pid/151/8848.html#i51) [\[i43\]](https://dblp.org/pid/151/8848.html#i43)

[316](https://dblp.org/pid/151/8848.html?view=joint&param=316 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiao Ke](https://dblp.org/pid/78/9040.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[317](https://dblp.org/pid/151/8848.html?view=joint&param=317 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=2)

[Hrant Khachatrian](https://dblp.org/pid/20/10360.html)

[\[i96\]](https://dblp.org/pid/151/8848.html#i96)

[318](https://dblp.org/pid/151/8848.html?view=joint&param=318 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Javad Khaghani](https://dblp.org/pid/233/0334.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[319](https://dblp.org/pid/151/8848.html?view=joint&param=319 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)

[\[c118\]](https://dblp.org/pid/151/8848.html#c118) [\[i95\]](https://dblp.org/pid/151/8848.html#i95) [\[j7\]](https://dblp.org/pid/151/8848.html#j7) [\[c91\]](https://dblp.org/pid/151/8848.html#c91) [\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[c81\]](https://dblp.org/pid/151/8848.html#c81) [\[i65\]](https://dblp.org/pid/151/8848.html#i65) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[i56\]](https://dblp.org/pid/151/8848.html#i56) [\[i46\]](https://dblp.org/pid/151/8848.html#i46) [\[i42\]](https://dblp.org/pid/151/8848.html#i42) [\[c50\]](https://dblp.org/pid/151/8848.html#c50) [\[c47\]](https://dblp.org/pid/151/8848.html#c47) [\[i40\]](https://dblp.org/pid/151/8848.html#i40) [\[i36\]](https://dblp.org/pid/151/8848.html#i36) [\[j3\]](https://dblp.org/pid/151/8848.html#j3) [\[j2\]](https://dblp.org/pid/151/8848.html#j2) [\[c36\]](https://dblp.org/pid/151/8848.html#c36) [\[c35\]](https://dblp.org/pid/151/8848.html#c35) [\[c34\]](https://dblp.org/pid/151/8848.html#c34) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c31\]](https://dblp.org/pid/151/8848.html#c31) [\[i21\]](https://dblp.org/pid/151/8848.html#i21) [\[i19\]](https://dblp.org/pid/151/8848.html#i19) [\[i18\]](https://dblp.org/pid/151/8848.html#i18) [\[c25\]](https://dblp.org/pid/151/8848.html#c25) [\[c24\]](https://dblp.org/pid/151/8848.html#c24) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c22\]](https://dblp.org/pid/151/8848.html#c22) [\[c21\]](https://dblp.org/pid/151/8848.html#c21) [\[i13\]](https://dblp.org/pid/151/8848.html#i13) [\[i12\]](https://dblp.org/pid/151/8848.html#i12) [\[i11\]](https://dblp.org/pid/151/8848.html#i11) [\[i10\]](https://dblp.org/pid/151/8848.html#i10) [\[i9\]](https://dblp.org/pid/151/8848.html#i9) [\[j1\]](https://dblp.org/pid/151/8848.html#j1) [\[c20\]](https://dblp.org/pid/151/8848.html#c20) [\[c19\]](https://dblp.org/pid/151/8848.html#c19) [\[c18\]](https://dblp.org/pid/151/8848.html#c18) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[i8\]](https://dblp.org/pid/151/8848.html#i8) [\[i7\]](https://dblp.org/pid/151/8848.html#i7) [\[c16\]](https://dblp.org/pid/151/8848.html#c16) [\[c15\]](https://dblp.org/pid/151/8848.html#c15) [\[c14\]](https://dblp.org/pid/151/8848.html#c14) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c11\]](https://dblp.org/pid/151/8848.html#c11) [\[c10\]](https://dblp.org/pid/151/8848.html#c10) [\[c9\]](https://dblp.org/pid/151/8848.html#c9) [\[i6\]](https://dblp.org/pid/151/8848.html#i6) [\[i5\]](https://dblp.org/pid/151/8848.html#i5) [\[i4\]](https://dblp.org/pid/151/8848.html#i4) [\[i3\]](https://dblp.org/pid/151/8848.html#i3) [\[i2\]](https://dblp.org/pid/151/8848.html#i2) [\[i1\]](https://dblp.org/pid/151/8848.html#i1) [\[c8\]](https://dblp.org/pid/151/8848.html#c8) [\[c7\]](https://dblp.org/pid/151/8848.html#c7) [\[c6\]](https://dblp.org/pid/151/8848.html#c6) [\[c4\]](https://dblp.org/pid/151/8848.html#c4) [\[c3\]](https://dblp.org/pid/151/8848.html#c3) [\[c2\]](https://dblp.org/pid/151/8848.html#c2) [\[c1\]](https://dblp.org/pid/151/8848.html#c1)

[320](https://dblp.org/pid/151/8848.html?view=joint&param=320 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Muhammad Haris Khan](https://dblp.org/pid/155/3076.html)

[\[j7\]](https://dblp.org/pid/151/8848.html#j7) [\[i42\]](https://dblp.org/pid/151/8848.html#i42) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[321](https://dblp.org/pid/151/8848.html?view=joint&param=321 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Salman H. Khan 0001](https://dblp.org/pid/32/11535-1.html)

aka: Salman Khan 0001

[\[c118\]](https://dblp.org/pid/151/8848.html#c118) [\[i95\]](https://dblp.org/pid/151/8848.html#i95) [\[c91\]](https://dblp.org/pid/151/8848.html#c91) [\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i65\]](https://dblp.org/pid/151/8848.html#i65)

[322](https://dblp.org/pid/151/8848.html?view=joint&param=322 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Amin Kheradmand](https://dblp.org/pid/93/9199.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[323](https://dblp.org/pid/151/8848.html?view=joint&param=323 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Byeong Hak Kim](https://dblp.org/pid/214/8978.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[324](https://dblp.org/pid/151/8848.html?view=joint&param=324 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Changick Kim](https://dblp.org/pid/40/5999.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[325](https://dblp.org/pid/151/8848.html?view=joint&param=325 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dae-Shik Kim](https://dblp.org/pid/25/2348.html)

aka: Daeshik Kim

[\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[326](https://dblp.org/pid/151/8848.html?view=joint&param=326 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Daijin Kim 0001](https://dblp.org/pid/k/DaijinKim.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[327](https://dblp.org/pid/151/8848.html?view=joint&param=327 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Guisik Kim](https://dblp.org/pid/197/6673.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[328](https://dblp.org/pid/151/8848.html?view=joint&param=328 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Gwantae Kim](https://dblp.org/pid/264/5954.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[329](https://dblp.org/pid/151/8848.html?view=joint&param=329 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ji-Wan Kim](https://dblp.org/pid/174/1015.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[330](https://dblp.org/pid/151/8848.html?view=joint&param=330 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jun-Hyuk Kim](https://dblp.org/pid/193/6547.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[331](https://dblp.org/pid/151/8848.html?view=joint&param=331 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kang-Wook Kim 0004](https://dblp.org/pid/16/9584-4.html)

aka: Kang-wook Kim 0004

[\[c90\]](https://dblp.org/pid/151/8848.html#c90)

[332](https://dblp.org/pid/151/8848.html?view=joint&param=332 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Min Young Kim 0003](https://dblp.org/pid/34/5733-3.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[333](https://dblp.org/pid/151/8848.html?view=joint&param=333 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sohyeong Kim](https://dblp.org/pid/184/5475.html)

[\[i93\]](https://dblp.org/pid/151/8848.html#i93) [\[c26\]](https://dblp.org/pid/151/8848.html#c26)

[334](https://dblp.org/pid/151/8848.html?view=joint&param=334 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Younggeun Kim](https://dblp.org/pid/294/6642.html)

[\[c90\]](https://dblp.org/pid/151/8848.html#c90)

[335](https://dblp.org/pid/151/8848.html?view=joint&param=335 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Youngwoo Kim](https://dblp.org/pid/90/8739.html)

aka: Yongwoo Kim

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[336](https://dblp.org/pid/151/8848.html?view=joint&param=336 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Madhu Kiran](https://dblp.org/pid/39/10281.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[337](https://dblp.org/pid/151/8848.html?view=joint&param=337 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kris Makoto Kitani](https://dblp.org/pid/42/163.html)

aka: Kris M. Kitani

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[338](https://dblp.org/pid/151/8848.html?view=joint&param=338 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[339](https://dblp.org/pid/151/8848.html?view=joint&param=339 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hanseok Ko](https://dblp.org/pid/67/5314.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[340](https://dblp.org/pid/151/8848.html?view=joint&param=340 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuki Kondo](https://dblp.org/pid/53/3635.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[341](https://dblp.org/pid/151/8848.html?view=joint&param=341 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiangtao Kong](https://dblp.org/pid/274/3262.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[342](https://dblp.org/pid/151/8848.html?view=joint&param=342 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiangzhen Kong](https://dblp.org/pid/80/531.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[343](https://dblp.org/pid/151/8848.html?view=joint&param=343 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sebastian Bernd Krah](https://dblp.org/pid/147/3405.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[344](https://dblp.org/pid/151/8848.html?view=joint&param=344 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[345](https://dblp.org/pid/151/8848.html?view=joint&param=345 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hari Chandana Kuchibhotla](https://dblp.org/pid/284/2570.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[346](https://dblp.org/pid/151/8848.html?view=joint&param=346 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Michal Kudelski](https://dblp.org/pid/50/6979.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[347](https://dblp.org/pid/151/8848.html?view=joint&param=347 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Alina Kuznetsova](https://dblp.org/pid/117/5897.html)

[\[c107\]](https://dblp.org/pid/151/8848.html#c107) [\[i62\]](https://dblp.org/pid/151/8848.html#i62)

[348](https://dblp.org/pid/151/8848.html?view=joint&param=348 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jonas Kvarnström](https://dblp.org/pid/05/3470.html)

[\[c1\]](https://dblp.org/pid/151/8848.html#c1)

[349](https://dblp.org/pid/151/8848.html?view=joint&param=349 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dokyeong Kwon](https://dblp.org/pid/242/3552.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[350](https://dblp.org/pid/151/8848.html?view=joint&param=350 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Robert Laganière](https://dblp.org/pid/32/1448.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[351](https://dblp.org/pid/151/8848.html?view=joint&param=351 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Simiao Lai](https://dblp.org/pid/282/1954.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[352](https://dblp.org/pid/151/8848.html?view=joint&param=352 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Julien Lamour](https://dblp.org/pid/260/3181.html)

[\[c29\]](https://dblp.org/pid/151/8848.html#c29)

[353](https://dblp.org/pid/151/8848.html?view=joint&param=353 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jin-Peng Lan](https://dblp.org/pid/332/1033.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[354](https://dblp.org/pid/151/8848.html?view=joint&param=354 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rushi Lan](https://dblp.org/pid/44/8845.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[355](https://dblp.org/pid/151/8848.html?view=joint&param=355 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[356](https://dblp.org/pid/151/8848.html?view=joint&param=356 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jochen Lang 0001](https://dblp.org/pid/34/2622.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[357](https://dblp.org/pid/151/8848.html?view=joint&param=357 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhiqiang Lang](https://dblp.org/pid/238/0425.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[358](https://dblp.org/pid/151/8848.html?view=joint&param=358 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yee Wei Law](https://dblp.org/pid/62/4404.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[359](https://dblp.org/pid/151/8848.html?view=joint&param=359 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c47\]](https://dblp.org/pid/151/8848.html#c47) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c40\]](https://dblp.org/pid/151/8848.html#c40) [\[i40\]](https://dblp.org/pid/151/8848.html#i40) [\[i38\]](https://dblp.org/pid/151/8848.html#i38) [\[i21\]](https://dblp.org/pid/151/8848.html#i21) [\[c24\]](https://dblp.org/pid/151/8848.html#c24) [\[i13\]](https://dblp.org/pid/151/8848.html#i13) [\[c19\]](https://dblp.org/pid/151/8848.html#c19) [\[i8\]](https://dblp.org/pid/151/8848.html#i8)

[360](https://dblp.org/pid/151/8848.html?view=joint&param=360 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Karel Lebeda](https://dblp.org/pid/128/7873.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[361](https://dblp.org/pid/151/8848.html?view=joint&param=361 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bruno Lecouat](https://dblp.org/pid/215/4371.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[362](https://dblp.org/pid/151/8848.html?view=joint&param=362 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dongwook Lee](https://dblp.org/pid/25/6543.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[363](https://dblp.org/pid/151/8848.html?view=joint&param=363 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hankyeol Lee](https://dblp.org/pid/234/0073.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[364](https://dblp.org/pid/151/8848.html?view=joint&param=364 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hyemin Lee](https://dblp.org/pid/188/7676.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[365](https://dblp.org/pid/151/8848.html?view=joint&param=365 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hyungjun Lee](https://dblp.org/pid/324/8911.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[366](https://dblp.org/pid/151/8848.html?view=joint&param=366 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hyunjeong Lee](https://dblp.org/pid/00/3423.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[367](https://dblp.org/pid/151/8848.html?view=joint&param=367 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jae-Yeong Lee](https://dblp.org/pid/19/7743.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[368](https://dblp.org/pid/151/8848.html?view=joint&param=368 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jae-Young Lee](https://dblp.org/pid/46/985.html)

[\[c90\]](https://dblp.org/pid/151/8848.html#c90)

[369](https://dblp.org/pid/151/8848.html?view=joint&param=369 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jaehoon Lee](https://dblp.org/pid/95/386.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[370](https://dblp.org/pid/151/8848.html?view=joint&param=370 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jong Hyuk Lee](https://dblp.org/pid/39/2874.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[371](https://dblp.org/pid/151/8848.html?view=joint&param=371 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jong-Seok Lee](https://dblp.org/pid/70/1152.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[372](https://dblp.org/pid/151/8848.html?view=joint&param=372 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jun Ha Lee](https://dblp.org/pid/260/2774.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[373](https://dblp.org/pid/151/8848.html?view=joint&param=373 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jun-Hyun Lee](https://dblp.org/pid/155/8661.html)

aka: Junhyun Lee

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[374](https://dblp.org/pid/151/8848.html?view=joint&param=374 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jungwon Lee](https://dblp.org/pid/87/381.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[375](https://dblp.org/pid/151/8848.html?view=joint&param=375 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kanghyu Lee](https://dblp.org/pid/218/1511.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[376](https://dblp.org/pid/151/8848.html?view=joint&param=376 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Namhoon Lee](https://dblp.org/pid/63/5359.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[377](https://dblp.org/pid/151/8848.html?view=joint&param=377 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Seohyung Lee](https://dblp.org/pid/210/4662.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[378](https://dblp.org/pid/151/8848.html?view=joint&param=378 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yunsung Lee](https://dblp.org/pid/227/9311.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[379](https://dblp.org/pid/151/8848.html?view=joint&param=379 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhen Lei 0001](https://dblp.org/pid/55/112-1.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[380](https://dblp.org/pid/151/8848.html?view=joint&param=380 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[381](https://dblp.org/pid/151/8848.html?view=joint&param=381 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Cong Leng](https://dblp.org/pid/147/9188.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[382](https://dblp.org/pid/151/8848.html?view=joint&param=382 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[383](https://dblp.org/pid/151/8848.html?view=joint&param=383 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Alex Levinshtein](https://dblp.org/pid/40/6950.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[384](https://dblp.org/pid/151/8848.html?view=joint&param=384 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bi Li 0005](https://dblp.org/pid/174/9761.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[385](https://dblp.org/pid/151/8848.html?view=joint&param=385 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bing Li 0001](https://dblp.org/pid/13/2692-1.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[386](https://dblp.org/pid/151/8848.html?view=joint&param=386 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bo Li 0114](https://dblp.org/pid/50/3402-114.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[387](https://dblp.org/pid/151/8848.html?view=joint&param=387 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chao Li 0034](https://dblp.org/pid/66/190-34.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[388](https://dblp.org/pid/151/8848.html?view=joint&param=388 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chenghua Li](https://dblp.org/pid/70/10190.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[389](https://dblp.org/pid/151/8848.html?view=joint&param=389 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chenglong Li 0002](https://dblp.org/pid/83/7820-2.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[390](https://dblp.org/pid/151/8848.html?view=joint&param=390 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chenyang Li 0007](https://dblp.org/pid/15/1523-7.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[391](https://dblp.org/pid/151/8848.html?view=joint&param=391 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chu-Tak Li](https://dblp.org/pid/235/0657.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[392](https://dblp.org/pid/151/8848.html?view=joint&param=392 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fangya Li](https://dblp.org/pid/300/7266.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[393](https://dblp.org/pid/151/8848.html?view=joint&param=393 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Feng Li 0031](https://dblp.org/pid/92/2954-31.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[394](https://dblp.org/pid/151/8848.html?view=joint&param=394 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fu Li 0003](https://dblp.org/pid/37/4556-3.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[395](https://dblp.org/pid/151/8848.html?view=joint&param=395 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Guanju Li](https://dblp.org/pid/251/5559.html)

[\[c26\]](https://dblp.org/pid/151/8848.html#c26)

[396](https://dblp.org/pid/151/8848.html?view=joint&param=396 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Guoxuan Li](https://dblp.org/pid/121/6265.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[397](https://dblp.org/pid/151/8848.html?view=joint&param=397 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hao Li 0058](https://dblp.org/pid/17/5705-58.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[398](https://dblp.org/pid/151/8848.html?view=joint&param=398 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haojie Li](https://dblp.org/pid/61/4041.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[399](https://dblp.org/pid/151/8848.html?view=joint&param=399 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hongdong Li](https://dblp.org/pid/59/4859.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[400](https://dblp.org/pid/151/8848.html?view=joint&param=400 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Houqiang Li](https://dblp.org/pid/59/7017.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[401](https://dblp.org/pid/151/8848.html?view=joint&param=401 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[402](https://dblp.org/pid/151/8848.html?view=joint&param=402 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Huiyun Li](https://dblp.org/pid/55/3543.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[403](https://dblp.org/pid/151/8848.html?view=joint&param=403 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiahao Li 0005](https://dblp.org/pid/150/5524-5.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[404](https://dblp.org/pid/151/8848.html?view=joint&param=404 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiakun Li](https://dblp.org/pid/69/7673.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[405](https://dblp.org/pid/151/8848.html?view=joint&param=405 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jianhua Li](https://dblp.org/pid/93/3389.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[406](https://dblp.org/pid/151/8848.html?view=joint&param=406 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jie Li 0001](https://dblp.org/pid/17/2703-1.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[407](https://dblp.org/pid/151/8848.html?view=joint&param=407 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jijia Li](https://dblp.org/pid/135/1024.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[408](https://dblp.org/pid/151/8848.html?view=joint&param=408 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jing Li 0036](https://dblp.org/pid/l/JingLi36.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[409](https://dblp.org/pid/151/8848.html?view=joint&param=409 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jinjing Li](https://dblp.org/pid/91/8541.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[410](https://dblp.org/pid/151/8848.html?view=joint&param=410 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kai Li 0012](https://dblp.org/pid/l/KaiLi12.html)

[\[c111\]](https://dblp.org/pid/151/8848.html#c111) [\[i82\]](https://dblp.org/pid/151/8848.html#i82)

[411](https://dblp.org/pid/151/8848.html?view=joint&param=411 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ming Li 0010](https://dblp.org/pid/l/MingLi10.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[412](https://dblp.org/pid/151/8848.html?view=joint&param=412 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Muchen Li](https://dblp.org/pid/122/2666.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[413](https://dblp.org/pid/151/8848.html?view=joint&param=413 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ning Li 0044](https://dblp.org/pid/14/5410-44.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[414](https://dblp.org/pid/151/8848.html?view=joint&param=414 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Peixia Li](https://dblp.org/pid/213/5896.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[415](https://dblp.org/pid/151/8848.html?view=joint&param=415 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shengkun Li](https://dblp.org/pid/188/7561.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[416](https://dblp.org/pid/151/8848.html?view=joint&param=416 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shihu Li](https://dblp.org/pid/242/1376.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[417](https://dblp.org/pid/151/8848.html?view=joint&param=417 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shikun Li](https://dblp.org/pid/255/0117.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[418](https://dblp.org/pid/151/8848.html?view=joint&param=418 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Siyao Li](https://dblp.org/pid/163/8053.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[419](https://dblp.org/pid/151/8848.html?view=joint&param=419 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Siyi Li](https://dblp.org/pid/96/10161.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[420](https://dblp.org/pid/151/8848.html?view=joint&param=420 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Siyuan Li 0008](https://dblp.org/pid/63/9705-8.html)

[\[c115\]](https://dblp.org/pid/151/8848.html#c115) [\[c113\]](https://dblp.org/pid/151/8848.html#c113) [\[i94\]](https://dblp.org/pid/151/8848.html#i94) [\[i92\]](https://dblp.org/pid/151/8848.html#i92) [\[c106\]](https://dblp.org/pid/151/8848.html#c106) [\[c102\]](https://dblp.org/pid/151/8848.html#c102) [\[i88\]](https://dblp.org/pid/151/8848.html#i88) [\[i83\]](https://dblp.org/pid/151/8848.html#i83) [\[c79\]](https://dblp.org/pid/151/8848.html#c79) [\[i67\]](https://dblp.org/pid/151/8848.html#i67)

[421](https://dblp.org/pid/151/8848.html?view=joint&param=421 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Stan Z. Li](https://dblp.org/pid/l/StanZLi.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[422](https://dblp.org/pid/151/8848.html?view=joint&param=422 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wangkai Li](https://dblp.org/pid/340/1456.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[423](https://dblp.org/pid/151/8848.html?view=joint&param=423 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wen Li 0001](https://dblp.org/pid/06/721-1.html)

[\[c69\]](https://dblp.org/pid/151/8848.html#c69) [\[i31\]](https://dblp.org/pid/151/8848.html#i31)

[424](https://dblp.org/pid/151/8848.html?view=joint&param=424 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenbo Li 0001](https://dblp.org/pid/51/3185-1.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[425](https://dblp.org/pid/151/8848.html?view=joint&param=425 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenbo Li 0002](https://dblp.org/pid/51/3185-2.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[426](https://dblp.org/pid/151/8848.html?view=joint&param=426 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xi Li 0001](https://dblp.org/pid/46/2311-1.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[427](https://dblp.org/pid/151/8848.html?view=joint&param=427 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xia Li 0005](https://dblp.org/pid/97/30-5.html)

[\[c88\]](https://dblp.org/pid/151/8848.html#c88) [\[c55\]](https://dblp.org/pid/151/8848.html#c55) [\[i51\]](https://dblp.org/pid/151/8848.html#i51) [\[i43\]](https://dblp.org/pid/151/8848.html#i43)

[428](https://dblp.org/pid/151/8848.html?view=joint&param=428 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[429](https://dblp.org/pid/151/8848.html?view=joint&param=429 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiao Li](https://dblp.org/pid/66/2069.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[430](https://dblp.org/pid/151/8848.html?view=joint&param=430 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaochuan Li 0001](https://dblp.org/pid/10/8076-1.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[431](https://dblp.org/pid/151/8848.html?view=joint&param=431 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaodi Li](https://dblp.org/pid/63/7279.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[432](https://dblp.org/pid/151/8848.html?view=joint&param=432 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xin Li 0034](https://dblp.org/pid/09/1365-34.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[433](https://dblp.org/pid/151/8848.html?view=joint&param=433 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiu Li 0001](https://dblp.org/pid/13/1206-1.html)

[\[c111\]](https://dblp.org/pid/151/8848.html#c111) [\[i82\]](https://dblp.org/pid/151/8848.html#i82)

[434](https://dblp.org/pid/151/8848.html?view=joint&param=434 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yan Li 0014](https://dblp.org/pid/87/660-14.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[435](https://dblp.org/pid/151/8848.html?view=joint&param=435 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yang Li 0041](https://dblp.org/pid/37/4190-41.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[436](https://dblp.org/pid/151/8848.html?view=joint&param=436 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yawei Li 0001](https://dblp.org/pid/32/6740-1.html)

[\[c69\]](https://dblp.org/pid/151/8848.html#c69) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i31\]](https://dblp.org/pid/151/8848.html#i31) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[437](https://dblp.org/pid/151/8848.html?view=joint&param=437 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yingping Li](https://dblp.org/pid/172/4240.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[438](https://dblp.org/pid/151/8848.html?view=joint&param=438 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Youwei Li](https://dblp.org/pid/61/3956.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[439](https://dblp.org/pid/151/8848.html?view=joint&param=439 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuezhou Li](https://dblp.org/pid/284/2562.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[440](https://dblp.org/pid/151/8848.html?view=joint&param=440 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuhong Li](https://dblp.org/pid/82/6387.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[441](https://dblp.org/pid/151/8848.html?view=joint&param=441 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yunkun Li](https://dblp.org/pid/260/2938.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[442](https://dblp.org/pid/151/8848.html?view=joint&param=442 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zechao Li](https://dblp.org/pid/51/8693.html)

[\[c90\]](https://dblp.org/pid/151/8848.html#c90) [\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[443](https://dblp.org/pid/151/8848.html?view=joint&param=443 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhe Li 0008](https://dblp.org/pid/11/751-8.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[444](https://dblp.org/pid/151/8848.html?view=joint&param=444 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yanchao Lian](https://dblp.org/pid/253/3698.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[445](https://dblp.org/pid/151/8848.html?view=joint&param=445 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jingyun Liang](https://dblp.org/pid/210/5052.html)

[\[c63\]](https://dblp.org/pid/151/8848.html#c63) [\[i50\]](https://dblp.org/pid/151/8848.html#i50)

[446](https://dblp.org/pid/151/8848.html?view=joint&param=446 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shengcai Liao](https://dblp.org/pid/16/8313.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[447](https://dblp.org/pid/151/8848.html?view=joint&param=447 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Samantha YueYing Lim](https://dblp.org/pid/160/3756.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[448](https://dblp.org/pid/151/8848.html?view=joint&param=448 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chia-Hsiang Lin](https://dblp.org/pid/71/660.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[449](https://dblp.org/pid/151/8848.html?view=joint&param=449 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Liting Lin](https://dblp.org/pid/227/2204.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[450](https://dblp.org/pid/151/8848.html?view=joint&param=450 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Weiyao Lin](https://dblp.org/pid/42/6095.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[451](https://dblp.org/pid/151/8848.html?view=joint&param=451 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haibin Ling](https://dblp.org/pid/93/3488.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[452](https://dblp.org/pid/151/8848.html?view=joint&param=452 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Alexander Liniger](https://dblp.org/pid/162/5560.html)

[\[j4\]](https://dblp.org/pid/151/8848.html#j4) [\[c85\]](https://dblp.org/pid/151/8848.html#c85) [\[i73\]](https://dblp.org/pid/151/8848.html#i73) [\[i53\]](https://dblp.org/pid/151/8848.html#i53)

[453](https://dblp.org/pid/151/8848.html?view=joint&param=453 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bin Liu 0014](https://dblp.org/pid/35/837-14.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[454](https://dblp.org/pid/151/8848.html?view=joint&param=454 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[455](https://dblp.org/pid/151/8848.html?view=joint&param=455 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[456](https://dblp.org/pid/151/8848.html?view=joint&param=456 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chenming Liu](https://dblp.org/pid/321/0688.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[457](https://dblp.org/pid/151/8848.html?view=joint&param=457 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hanwen Liu](https://dblp.org/pid/178/1112.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[458](https://dblp.org/pid/151/8848.html?view=joint&param=458 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jie Liu 0040](https://dblp.org/pid/03/2134-40.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[459](https://dblp.org/pid/151/8848.html?view=joint&param=459 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jing Liu 0031](https://dblp.org/pid/72/2590-31.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[460](https://dblp.org/pid/151/8848.html?view=joint&param=460 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jingen Liu](https://dblp.org/pid/10/5849.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[461](https://dblp.org/pid/151/8848.html?view=joint&param=461 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jingtuo Liu](https://dblp.org/pid/164/5911.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[462](https://dblp.org/pid/151/8848.html?view=joint&param=462 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jingyu Liu 0004](https://dblp.org/pid/43/6883-4.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[463](https://dblp.org/pid/151/8848.html?view=joint&param=463 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kaiwen Liu](https://dblp.org/pid/231/4262.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[464](https://dblp.org/pid/151/8848.html?view=joint&param=464 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lei Liu 0049](https://dblp.org/pid/21/2715-49.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[465](https://dblp.org/pid/151/8848.html?view=joint&param=465 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Li Liu 0036](https://dblp.org/pid/33/4528-36.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[466](https://dblp.org/pid/151/8848.html?view=joint&param=466 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pengyu Liu 0005](https://dblp.org/pid/73/7783-5.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[467](https://dblp.org/pid/151/8848.html?view=joint&param=467 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qingjie Liu 0001](https://dblp.org/pid/72/10584.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[468](https://dblp.org/pid/151/8848.html?view=joint&param=468 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Risheng Liu](https://dblp.org/pid/82/8066.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[469](https://dblp.org/pid/151/8848.html?view=joint&param=469 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shuai Liu 0009](https://dblp.org/pid/76/5789-0009.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[470](https://dblp.org/pid/151/8848.html?view=joint&param=470 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shuaicheng Liu](https://dblp.org/pid/49/8652.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[471](https://dblp.org/pid/151/8848.html?view=joint&param=471 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Si Liu 0001](https://dblp.org/pid/60/7642.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[472](https://dblp.org/pid/151/8848.html?view=joint&param=472 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenyu Liu 0001](https://dblp.org/pid/42/4110-1.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[473](https://dblp.org/pid/151/8848.html?view=joint&param=473 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xianglong Liu 0001](https://dblp.org/pid/55/7901-1.html)

[\[c110\]](https://dblp.org/pid/151/8848.html#c110) [\[c97\]](https://dblp.org/pid/151/8848.html#c97) [\[c96\]](https://dblp.org/pid/151/8848.html#c96)

[474](https://dblp.org/pid/151/8848.html?view=joint&param=474 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaohong Liu 0001](https://dblp.org/pid/95/2454-1.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[475](https://dblp.org/pid/151/8848.html?view=joint&param=475 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yang Liu 0003](https://dblp.org/pid/51/3710-3.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[476](https://dblp.org/pid/151/8848.html?view=joint&param=476 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yifan Liu 0001](https://dblp.org/pid/23/4955-1.html)

[\[c98\]](https://dblp.org/pid/151/8848.html#c98) [\[c96\]](https://dblp.org/pid/151/8848.html#c96) [\[i86\]](https://dblp.org/pid/151/8848.html#i86)

[477](https://dblp.org/pid/151/8848.html?view=joint&param=477 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yue Liu](https://dblp.org/pid/74/1932.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[478](https://dblp.org/pid/151/8848.html?view=joint&param=478 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhenbing Liu](https://dblp.org/pid/19/7578.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[479](https://dblp.org/pid/151/8848.html?view=joint&param=479 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhisong Liu](https://dblp.org/pid/144/8750.html)

aka: Zhi-Song Liu

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[480](https://dblp.org/pid/151/8848.html?view=joint&param=480 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhuoming Liu 0004](https://dblp.org/pid/289/2864-4.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[481](https://dblp.org/pid/151/8848.html?view=joint&param=481 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zikun Liu 0001](https://dblp.org/pid/172/9824-1.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[482](https://dblp.org/pid/151/8848.html?view=joint&param=482 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ziluan Liu](https://dblp.org/pid/158/4864.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52) [\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[483](https://dblp.org/pid/151/8848.html?view=joint&param=483 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Andong Lu](https://dblp.org/pid/245/2878.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[484](https://dblp.org/pid/151/8848.html?view=joint&param=484 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Cewu Lu](https://dblp.org/pid/96/10571.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[485](https://dblp.org/pid/151/8848.html?view=joint&param=485 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[486](https://dblp.org/pid/151/8848.html?view=joint&param=486 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Liying Lu](https://dblp.org/pid/152/5445.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[487](https://dblp.org/pid/151/8848.html?view=joint&param=487 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wei Lu](https://dblp.org/pid/98/6613.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[488](https://dblp.org/pid/151/8848.html?view=joint&param=488 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wen Lu 0004](https://dblp.org/pid/31/6140-4.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28) [\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[489](https://dblp.org/pid/151/8848.html?view=joint&param=489 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiankai Lu](https://dblp.org/pid/153/2122.html)

[\[c42\]](https://dblp.org/pid/151/8848.html#c42) [\[i30\]](https://dblp.org/pid/151/8848.html#i30)

[490](https://dblp.org/pid/151/8848.html?view=joint&param=490 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yan Lu 0001](https://dblp.org/pid/15/4830-1.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[491](https://dblp.org/pid/151/8848.html?view=joint&param=491 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yunhua Lu](https://dblp.org/pid/45/2957.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[492](https://dblp.org/pid/151/8848.html?view=joint&param=492 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Andreas Lugmayr](https://dblp.org/pid/249/2710.html)

[\[c90\]](https://dblp.org/pid/151/8848.html#c90) [\[c84\]](https://dblp.org/pid/151/8848.html#c84) [\[c73\]](https://dblp.org/pid/151/8848.html#c73) [\[i75\]](https://dblp.org/pid/151/8848.html#i75) [\[c72\]](https://dblp.org/pid/151/8848.html#c72) [\[c71\]](https://dblp.org/pid/151/8848.html#c71) [\[c63\]](https://dblp.org/pid/151/8848.html#c63) [\[i58\]](https://dblp.org/pid/151/8848.html#i58) [\[i50\]](https://dblp.org/pid/151/8848.html#i50) [\[i44\]](https://dblp.org/pid/151/8848.html#i44) [\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[c41\]](https://dblp.org/pid/151/8848.html#c41) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[i32\]](https://dblp.org/pid/151/8848.html#i32) [\[c30\]](https://dblp.org/pid/151/8848.html#c30) [\[c29\]](https://dblp.org/pid/151/8848.html#c29) [\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i17\]](https://dblp.org/pid/151/8848.html#i17) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[493](https://dblp.org/pid/151/8848.html?view=joint&param=493 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jonathon Luiten](https://dblp.org/pid/211/7992.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[494](https://dblp.org/pid/151/8848.html?view=joint&param=494 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[495](https://dblp.org/pid/151/8848.html?view=joint&param=495 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bin Luo 0008](https://dblp.org/pid/36/4256-8.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[496](https://dblp.org/pid/151/8848.html?view=joint&param=496 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chong Luo 0001](https://dblp.org/pid/79/3712-1.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[497](https://dblp.org/pid/151/8848.html?view=joint&param=497 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ping Luo 0002](https://dblp.org/pid/54/4989-2.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[498](https://dblp.org/pid/151/8848.html?view=joint&param=498 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaotong Luo](https://dblp.org/pid/169/3960.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[499](https://dblp.org/pid/151/8848.html?view=joint&param=499 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhao Luo](https://dblp.org/pid/187/1232.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[500](https://dblp.org/pid/151/8848.html?view=joint&param=500 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhengxiong Luo 0001](https://dblp.org/pid/253/1632-1.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[501](https://dblp.org/pid/151/8848.html?view=joint&param=501 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ziwei Luo 0002](https://dblp.org/pid/166/7005-2.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[502](https://dblp.org/pid/151/8848.html?view=joint&param=502 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Siwei Lyu](https://dblp.org/pid/51/4482.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[503](https://dblp.org/pid/151/8848.html?view=joint&param=503 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Andy Jinhua Ma](https://dblp.org/pid/119/1514.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[504](https://dblp.org/pid/151/8848.html?view=joint&param=504 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bingpeng Ma](https://dblp.org/pid/62/1822.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[505](https://dblp.org/pid/151/8848.html?view=joint&param=505 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chao Ma 0004](https://dblp.org/pid/79/1552-4.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[506](https://dblp.org/pid/151/8848.html?view=joint&param=506 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiayi Ma 0001](https://dblp.org/pid/96/9989.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[507](https://dblp.org/pid/151/8848.html?view=joint&param=507 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[508](https://dblp.org/pid/151/8848.html?view=joint&param=508 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xudong Ma](https://dblp.org/pid/19/2951.html)

[\[c97\]](https://dblp.org/pid/151/8848.html#c97)

[509](https://dblp.org/pid/151/8848.html?view=joint&param=509 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yinchao Ma](https://dblp.org/pid/189/1326.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[510](https://dblp.org/pid/151/8848.html?view=joint&param=510 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ziang Ma](https://dblp.org/pid/165/9621.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[511](https://dblp.org/pid/151/8848.html?view=joint&param=511 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Takahiro Maeda 0001](https://dblp.org/pid/26/5679-1.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[512](https://dblp.org/pid/151/8848.html?view=joint&param=512 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhijun Mai](https://dblp.org/pid/247/9401.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[513](https://dblp.org/pid/151/8848.html?view=joint&param=513 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Julien Mairal](https://dblp.org/pid/49/6555.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[514](https://dblp.org/pid/151/8848.html?view=joint&param=514 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Julio Delgado Mangas](https://dblp.org/pid/351/0410.html)

[\[c116\]](https://dblp.org/pid/151/8848.html#c116) [\[i84\]](https://dblp.org/pid/151/8848.html#i84)

[515](https://dblp.org/pid/151/8848.html?view=joint&param=515 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Antoine Manzanera](https://dblp.org/pid/73/2951.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[516](https://dblp.org/pid/151/8848.html?view=joint&param=516 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mario Edoardo Maresca](https://dblp.org/pid/133/9429.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[517](https://dblp.org/pid/151/8848.html?view=joint&param=517 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Nikolay Marin](https://dblp.org/pid/407/2079.html)

[\[c116\]](https://dblp.org/pid/151/8848.html#c116)

[518](https://dblp.org/pid/151/8848.html?view=joint&param=518 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jaime Spencer Martin](https://dblp.org/pid/234/0071.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[519](https://dblp.org/pid/151/8848.html?view=joint&param=519 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[520](https://dblp.org/pid/151/8848.html?view=joint&param=520 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Brais Martínez](https://dblp.org/pid/14/111.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[521](https://dblp.org/pid/151/8848.html?view=joint&param=521 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Éric Marty](https://dblp.org/pid/222/9632.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[522](https://dblp.org/pid/151/8848.html?view=joint&param=522 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Steven Marty](https://dblp.org/pid/274/2797.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[523](https://dblp.org/pid/151/8848.html?view=joint&param=523 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Seyed Mojtaba Marvasti-Zadeh](https://dblp.org/pid/188/6262.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[524](https://dblp.org/pid/151/8848.html?view=joint&param=524 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[j7\]](https://dblp.org/pid/151/8848.html#j7) [\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[i42\]](https://dblp.org/pid/151/8848.html#i42) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[525](https://dblp.org/pid/151/8848.html?view=joint&param=525 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Thomas Mauthner](https://dblp.org/pid/95/6646.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[526](https://dblp.org/pid/151/8848.html?view=joint&param=526 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c107\]](https://dblp.org/pid/151/8848.html#c107) [\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c91\]](https://dblp.org/pid/151/8848.html#c91) [\[c86\]](https://dblp.org/pid/151/8848.html#c86) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c78\]](https://dblp.org/pid/151/8848.html#c78) [\[i70\]](https://dblp.org/pid/151/8848.html#i70) [\[i69\]](https://dblp.org/pid/151/8848.html#i69) [\[i65\]](https://dblp.org/pid/151/8848.html#i65) [\[i62\]](https://dblp.org/pid/151/8848.html#i62) [\[c60\]](https://dblp.org/pid/151/8848.html#c60) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[i55\]](https://dblp.org/pid/151/8848.html#i55)

[527](https://dblp.org/pid/151/8848.html?view=joint&param=527 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Henry Medeiros 0001](https://dblp.org/pid/62/8630.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[528](https://dblp.org/pid/151/8848.html?view=joint&param=528 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Nancy Mehta](https://dblp.org/pid/305/3859.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[529](https://dblp.org/pid/151/8848.html?view=joint&param=529 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Gerhard Ingmar Meijer](https://dblp.org/pid/46/5951.html)

aka: Ingmar Meijer

[\[c101\]](https://dblp.org/pid/151/8848.html#c101) [\[i81\]](https://dblp.org/pid/151/8848.html#i81)

[530](https://dblp.org/pid/151/8848.html?view=joint&param=530 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Simone Melzi](https://dblp.org/pid/160/2770.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[531](https://dblp.org/pid/151/8848.html?view=joint&param=531 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[532](https://dblp.org/pid/151/8848.html?view=joint&param=532 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Giulia Meneghetti](https://dblp.org/pid/163/4432.html)

[\[c15\]](https://dblp.org/pid/151/8848.html#c15) [\[c11\]](https://dblp.org/pid/151/8848.html#c11) [\[c5\]](https://dblp.org/pid/151/8848.html#c5)

[533](https://dblp.org/pid/151/8848.html?view=joint&param=533 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zibo Meng](https://dblp.org/pid/126/8042.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[534](https://dblp.org/pid/151/8848.html?view=joint&param=534 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Deshui Miao](https://dblp.org/pid/307/5501.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[535](https://dblp.org/pid/151/8848.html?view=joint&param=535 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pablo Navarrete Michelini](https://dblp.org/pid/63/1474.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[536](https://dblp.org/pid/151/8848.html?view=joint&param=536 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[i52\]](https://dblp.org/pid/151/8848.html#i52) [\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[i28\]](https://dblp.org/pid/151/8848.html#i28) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[537](https://dblp.org/pid/151/8848.html?view=joint&param=537 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Krystian Mikolajczyk](https://dblp.org/pid/96/433.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[538](https://dblp.org/pid/151/8848.html?view=joint&param=538 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ondrej Miksik](https://dblp.org/pid/85/9964.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[539](https://dblp.org/pid/151/8848.html?view=joint&param=539 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Deepak Mishra 0002](https://dblp.org/pid/65/6758-2.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[540](https://dblp.org/pid/151/8848.html?view=joint&param=540 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xuan Mo](https://dblp.org/pid/09/7643.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[541](https://dblp.org/pid/151/8848.html?view=joint&param=541 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Payman Moallem](https://dblp.org/pid/63/5378.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[542](https://dblp.org/pid/151/8848.html?view=joint&param=542 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bogdan Cosmin Mocanu](https://dblp.org/pid/182/4766.html)

aka: Bogdan Mocanu

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[543](https://dblp.org/pid/151/8848.html?view=joint&param=543 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Andres Solis Montero](https://dblp.org/pid/36/8379.html)

aka: Andrés Solís Montero

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[544](https://dblp.org/pid/151/8848.html?view=joint&param=544 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lucas Morin](https://dblp.org/pid/309/7785.html)

[\[c101\]](https://dblp.org/pid/151/8848.html#c101) [\[i81\]](https://dblp.org/pid/151/8848.html#i81)

[545](https://dblp.org/pid/151/8848.html?view=joint&param=545 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Marcin Mozejko](https://dblp.org/pid/228/6840.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[546](https://dblp.org/pid/151/8848.html?view=joint&param=546 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Andrej Muhic](https://dblp.org/pid/119/0869.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[547](https://dblp.org/pid/151/8848.html?view=joint&param=547 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Matthias Müller 0011](https://dblp.org/pid/169/4686-1.html)

aka: Matthias Mueller 0001

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[548](https://dblp.org/pid/151/8848.html?view=joint&param=548 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Abdul Muqeet](https://dblp.org/pid/245/0047.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[549](https://dblp.org/pid/151/8848.html?view=joint&param=549 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Asen Nachkov](https://dblp.org/pid/354/6217.html)

[\[c119\]](https://dblp.org/pid/151/8848.html#c119) [\[i77\]](https://dblp.org/pid/151/8848.html#i77)

[550](https://dblp.org/pid/151/8848.html?view=joint&param=550 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Daniya Najiha](https://dblp.org/pid/326/6241.html)

[\[i65\]](https://dblp.org/pid/151/8848.html#i65)

[551](https://dblp.org/pid/151/8848.html?view=joint&param=551 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chihiro Nakatani](https://dblp.org/pid/300/2074.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[552](https://dblp.org/pid/151/8848.html?view=joint&param=552 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hyeonseob Nam](https://dblp.org/pid/150/4248.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[553](https://dblp.org/pid/151/8848.html?view=joint&param=553 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yoonchan Nam](https://dblp.org/pid/327/3722.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[554](https://dblp.org/pid/151/8848.html?view=joint&param=554 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Nan Nan](https://dblp.org/pid/26/3712.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[555](https://dblp.org/pid/151/8848.html?view=joint&param=555 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[556](https://dblp.org/pid/151/8848.html?view=joint&param=556 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ahmed S. Nassar](https://dblp.org/pid/321/9993.html)

[\[c101\]](https://dblp.org/pid/151/8848.html#c101) [\[i81\]](https://dblp.org/pid/151/8848.html#i81)

[557](https://dblp.org/pid/151/8848.html?view=joint&param=557 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Georg Nebehay](https://dblp.org/pid/129/4056.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[558](https://dblp.org/pid/151/8848.html?view=joint&param=558 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[559](https://dblp.org/pid/151/8848.html?view=joint&param=559 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Meng Ni](https://dblp.org/pid/174/2809.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[560](https://dblp.org/pid/151/8848.html?view=joint&param=560 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zihan Ni](https://dblp.org/pid/187/9123.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[561](https://dblp.org/pid/151/8848.html?view=joint&param=561 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiangtao Nie](https://dblp.org/pid/252/4948.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[562](https://dblp.org/pid/151/8848.html?view=joint&param=562 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rafael Martin Nieto](https://dblp.org/pid/136/0491.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[563](https://dblp.org/pid/151/8848.html?view=joint&param=563 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuzhen Niu](https://dblp.org/pid/28/7442.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[564](https://dblp.org/pid/151/8848.html?view=joint&param=564 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhiheng Niu](https://dblp.org/pid/80/3992.html)

aka: Zhi Heng Niu

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[565](https://dblp.org/pid/151/8848.html?view=joint&param=565 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mubashir Noman](https://dblp.org/pid/192/3732.html)

[\[c91\]](https://dblp.org/pid/151/8848.html#c91) [\[i65\]](https://dblp.org/pid/151/8848.html#i65)

[566](https://dblp.org/pid/151/8848.html?view=joint&param=566 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Klas Nordberg](https://dblp.org/pid/94/5686.html)

[\[c5\]](https://dblp.org/pid/151/8848.html#c5)

[567](https://dblp.org/pid/151/8848.html?view=joint&param=567 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jana Noskova](https://dblp.org/pid/142/5723.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[568](https://dblp.org/pid/151/8848.html?view=joint&param=568 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Evangelos Ntavelis](https://dblp.org/pid/262/6311.html)

[\[c108\]](https://dblp.org/pid/151/8848.html#c108) [\[c99\]](https://dblp.org/pid/151/8848.html#c99) [\[i90\]](https://dblp.org/pid/151/8848.html#i90) [\[i87\]](https://dblp.org/pid/151/8848.html#i87) [\[c83\]](https://dblp.org/pid/151/8848.html#c83) [\[i68\]](https://dblp.org/pid/151/8848.html#i68)

[569](https://dblp.org/pid/151/8848.html?view=joint&param=569 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Takeru Oba](https://dblp.org/pid/282/8759.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[570](https://dblp.org/pid/151/8848.html?view=joint&param=570 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kristoffer Öfjäll](https://dblp.org/pid/157/3586.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[571](https://dblp.org/pid/151/8848.html?view=joint&param=571 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pavel Ostyakov](https://dblp.org/pid/227/2398.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[572](https://dblp.org/pid/151/8848.html?view=joint&param=572 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Franci Oven](https://dblp.org/pid/160/3716.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[573](https://dblp.org/pid/151/8848.html?view=joint&param=573 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kannappan Palaniappan](https://dblp.org/pid/21/700.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[574](https://dblp.org/pid/151/8848.html?view=joint&param=574 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Naveen Paluru](https://dblp.org/pid/260/3261.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[575](https://dblp.org/pid/151/8848.html?view=joint&param=575 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jinshan Pan](https://dblp.org/pid/06/10816.html)

[\[c90\]](https://dblp.org/pid/151/8848.html#c90) [\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[576](https://dblp.org/pid/151/8848.html?view=joint&param=576 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Siyang Pan](https://dblp.org/pid/250/5753.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[577](https://dblp.org/pid/151/8848.html?view=joint&param=577 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bo Pang 0003](https://dblp.org/pid/16/6344-3.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[578](https://dblp.org/pid/151/8848.html?view=joint&param=578 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dominik Pangersic](https://dblp.org/pid/160/3593.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[579](https://dblp.org/pid/151/8848.html?view=joint&param=579 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[ChangBeom Park](https://dblp.org/pid/340/0926.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[580](https://dblp.org/pid/151/8848.html?view=joint&param=580 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hancheol Park](https://dblp.org/pid/161/3495.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[581](https://dblp.org/pid/151/8848.html?view=joint&param=581 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c119\]](https://dblp.org/pid/151/8848.html#c119) [\[c99\]](https://dblp.org/pid/151/8848.html#c99) [\[i90\]](https://dblp.org/pid/151/8848.html#i90) [\[i77\]](https://dblp.org/pid/151/8848.html#i77) [\[c86\]](https://dblp.org/pid/151/8848.html#c86) [\[c82\]](https://dblp.org/pid/151/8848.html#c82) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c75\]](https://dblp.org/pid/151/8848.html#c75) [\[i76\]](https://dblp.org/pid/151/8848.html#i76) [\[i69\]](https://dblp.org/pid/151/8848.html#i69) [\[c62\]](https://dblp.org/pid/151/8848.html#c62) [\[c60\]](https://dblp.org/pid/151/8848.html#c60) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[i55\]](https://dblp.org/pid/151/8848.html#i55) [\[i48\]](https://dblp.org/pid/151/8848.html#i48) [\[i23\]](https://dblp.org/pid/151/8848.html#i23)

[582](https://dblp.org/pid/151/8848.html?view=joint&param=582 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Matthieu Paul](https://dblp.org/pid/255/6113.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c86\]](https://dblp.org/pid/151/8848.html#c86) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c78\]](https://dblp.org/pid/151/8848.html#c78) [\[i70\]](https://dblp.org/pid/151/8848.html#i70) [\[i69\]](https://dblp.org/pid/151/8848.html#i69) [\[c56\]](https://dblp.org/pid/151/8848.html#c56) [\[i60\]](https://dblp.org/pid/151/8848.html#i60)

[583](https://dblp.org/pid/151/8848.html?view=joint&param=583 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bala Suraj Pedasingu](https://dblp.org/pid/260/3120.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[584](https://dblp.org/pid/151/8848.html?view=joint&param=584 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rengarajan Pelapur](https://dblp.org/pid/70/11224.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[585](https://dblp.org/pid/151/8848.html?view=joint&param=585 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[586](https://dblp.org/pid/151/8848.html?view=joint&param=586 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Asanka G. Perera](https://dblp.org/pid/231/9229.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[587](https://dblp.org/pid/151/8848.html?view=joint&param=587 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Alfredo Petrosino](https://dblp.org/pid/20/3145.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[588](https://dblp.org/pid/151/8848.html?view=joint&param=588 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[589](https://dblp.org/pid/151/8848.html?view=joint&param=589 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Luigi Piccinelli](https://dblp.org/pid/328/8549.html)

[\[c115\]](https://dblp.org/pid/151/8848.html#c115) [\[c113\]](https://dblp.org/pid/151/8848.html#c113) [\[i94\]](https://dblp.org/pid/151/8848.html#i94) [\[i92\]](https://dblp.org/pid/151/8848.html#i92)

[590](https://dblp.org/pid/151/8848.html?view=joint&param=590 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Marc Pollefeys](https://dblp.org/pid/p/MarcPollefeys.html)

[\[c103\]](https://dblp.org/pid/151/8848.html#c103) [\[i80\]](https://dblp.org/pid/151/8848.html#i80)

[591](https://dblp.org/pid/151/8848.html?view=joint&param=591 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jean Ponce](https://dblp.org/pid/p/JeanPonce.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[592](https://dblp.org/pid/151/8848.html?view=joint&param=592 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mahdieh Poostchi](https://dblp.org/pid/87/5622.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[593](https://dblp.org/pid/151/8848.html?view=joint&param=593 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fatih Porikli](https://dblp.org/pid/p/FatihMuratPorikli.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[594](https://dblp.org/pid/151/8848.html?view=joint&param=594 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Horst Possegger](https://dblp.org/pid/135/4917.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[595](https://dblp.org/pid/151/8848.html?view=joint&param=595 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Janis Postels](https://dblp.org/pid/246/4950.html)

[\[c93\]](https://dblp.org/pid/151/8848.html#c93) [\[i64\]](https://dblp.org/pid/151/8848.html#i64)

[596](https://dblp.org/pid/151/8848.html?view=joint&param=596 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kalpesh Prajapati](https://dblp.org/pid/264/5768.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[597](https://dblp.org/pid/151/8848.html?view=joint&param=597 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tony P. Pridmore](https://dblp.org/pid/19/6645.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[598](https://dblp.org/pid/151/8848.html?view=joint&param=598 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kuldeep Purohit](https://dblp.org/pid/191/2655.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28) [\[c28\]](https://dblp.org/pid/151/8848.html#c28) [\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[599](https://dblp.org/pid/151/8848.html?view=joint&param=599 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Densen Puthussery](https://dblp.org/pid/264/5624.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[600](https://dblp.org/pid/151/8848.html?view=joint&param=600 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Honggang Qi](https://dblp.org/pid/48/4237.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[601](https://dblp.org/pid/151/8848.html?view=joint&param=601 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jinqing Qi](https://dblp.org/pid/09/287.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[602](https://dblp.org/pid/151/8848.html?view=joint&param=602 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuankai Qi](https://dblp.org/pid/136/5491.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[603](https://dblp.org/pid/151/8848.html?view=joint&param=603 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chen Qian 0001](https://dblp.org/pid/70/3604-1.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[604](https://dblp.org/pid/151/8848.html?view=joint&param=604 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chen Qian 0006](https://dblp.org/pid/70/3604-6.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[605](https://dblp.org/pid/151/8848.html?view=joint&param=605 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ruihe Qian](https://dblp.org/pid/179/2622.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[606](https://dblp.org/pid/151/8848.html?view=joint&param=606 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zekun Qian](https://dblp.org/pid/315/4066.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[607](https://dblp.org/pid/151/8848.html?view=joint&param=607 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yu Qiao 0001](https://dblp.org/pid/q/YuQiao1.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[608](https://dblp.org/pid/151/8848.html?view=joint&param=608 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haotong Qin](https://dblp.org/pid/262/3626.html)

[\[c110\]](https://dblp.org/pid/151/8848.html#c110) [\[c97\]](https://dblp.org/pid/151/8848.html#c97) [\[c96\]](https://dblp.org/pid/151/8848.html#c96)

[609](https://dblp.org/pid/151/8848.html?view=joint&param=609 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lei Qin](https://dblp.org/pid/20/1306.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[610](https://dblp.org/pid/151/8848.html?view=joint&param=610 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shoumeng Qiu](https://dblp.org/pid/284/2537.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[611](https://dblp.org/pid/151/8848.html?view=joint&param=611 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xi Qiu](https://dblp.org/pid/115/5698.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[612](https://dblp.org/pid/151/8848.html?view=joint&param=612 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yanyun Qu](https://dblp.org/pid/03/3500.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[613](https://dblp.org/pid/151/8848.html?view=joint&param=613 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Gani Rahmon](https://dblp.org/pid/291/7224.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[614](https://dblp.org/pid/151/8848.html?view=joint&param=614 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[A. N. Rajagopalan 0001](https://dblp.org/pid/73/3473.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28) [\[c28\]](https://dblp.org/pid/151/8848.html#c28) [\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[615](https://dblp.org/pid/151/8848.html?view=joint&param=615 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Frano Rajic](https://dblp.org/pid/331/2107.html)

[\[c117\]](https://dblp.org/pid/151/8848.html#c117) [\[i85\]](https://dblp.org/pid/151/8848.html#i85)

[616](https://dblp.org/pid/151/8848.html?view=joint&param=616 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Aravindh Rajiv](https://dblp.org/pid/307/9144.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[617](https://dblp.org/pid/151/8848.html?view=joint&param=617 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Priya Mariam Raju](https://dblp.org/pid/233/9987.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[618](https://dblp.org/pid/151/8848.html?view=joint&param=618 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Muhammad Rana](https://dblp.org/pid/276/0222.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[619](https://dblp.org/pid/151/8848.html?view=joint&param=619 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Madan Kumar Rapuru](https://dblp.org/pid/188/7542.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[620](https://dblp.org/pid/151/8848.html?view=joint&param=620 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haoyu Ren](https://dblp.org/pid/53/8616.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[621](https://dblp.org/pid/151/8848.html?view=joint&param=621 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c47\]](https://dblp.org/pid/151/8848.html#c47) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c40\]](https://dblp.org/pid/151/8848.html#c40) [\[i40\]](https://dblp.org/pid/151/8848.html#i40) [\[i38\]](https://dblp.org/pid/151/8848.html#i38) [\[i21\]](https://dblp.org/pid/151/8848.html#i21) [\[c14\]](https://dblp.org/pid/151/8848.html#c14) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[i6\]](https://dblp.org/pid/151/8848.html#i6)

[622](https://dblp.org/pid/151/8848.html?view=joint&param=622 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Giorgio Roffo](https://dblp.org/pid/123/2925.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[623](https://dblp.org/pid/151/8848.html?view=joint&param=623 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Andrés Romero](https://dblp.org/pid/29/641.html)

[\[c84\]](https://dblp.org/pid/151/8848.html#c84) [\[i75\]](https://dblp.org/pid/151/8848.html#i75)

[624](https://dblp.org/pid/151/8848.html?view=joint&param=624 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Litu Rout](https://dblp.org/pid/206/6445.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[625](https://dblp.org/pid/151/8848.html?view=joint&param=625 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Piotr Rudol](https://dblp.org/pid/44/101.html)

[\[c9\]](https://dblp.org/pid/151/8848.html#c9) [\[c1\]](https://dblp.org/pid/151/8848.html#c1)

[626](https://dblp.org/pid/151/8848.html?view=joint&param=626 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hrishikesh P. S](https://dblp.org/pid/264/5454.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[627](https://dblp.org/pid/151/8848.html?view=joint&param=627 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Amir Saffari](https://dblp.org/pid/71/310.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[628](https://dblp.org/pid/151/8848.html?view=joint&param=628 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[José María Martínez Sanchez](https://dblp.org/pid/47/3503.html)

aka: José M. Martínez 0001

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[629](https://dblp.org/pid/151/8848.html?view=joint&param=629 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Vincenzo Santopietro](https://dblp.org/pid/188/7799.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[630](https://dblp.org/pid/151/8848.html?view=joint&param=630 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hasan Saribas](https://dblp.org/pid/225/3263.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[631](https://dblp.org/pid/151/8848.html?view=joint&param=631 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Norbert Scherer-Negenborn](https://dblp.org/pid/45/8662.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[632](https://dblp.org/pid/151/8848.html?view=joint&param=632 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Aron Schmied](https://dblp.org/pid/355/5910.html)

[\[c103\]](https://dblp.org/pid/151/8848.html#c103) [\[i80\]](https://dblp.org/pid/151/8848.html#i80)

[633](https://dblp.org/pid/151/8848.html?view=joint&param=633 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Thomas B. Schön](https://dblp.org/pid/85/4891.html)

[\[j5\]](https://dblp.org/pid/151/8848.html#j5) [\[i91\]](https://dblp.org/pid/151/8848.html#i91) [\[c92\]](https://dblp.org/pid/151/8848.html#c92) [\[c68\]](https://dblp.org/pid/151/8848.html#c68) [\[i45\]](https://dblp.org/pid/151/8848.html#i45) [\[c54\]](https://dblp.org/pid/151/8848.html#c54) [\[c53\]](https://dblp.org/pid/151/8848.html#c53) [\[c44\]](https://dblp.org/pid/151/8848.html#c44) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[i35\]](https://dblp.org/pid/151/8848.html#i35) [\[i24\]](https://dblp.org/pid/151/8848.html#i24) [\[i20\]](https://dblp.org/pid/151/8848.html#i20) [\[i16\]](https://dblp.org/pid/151/8848.html#i16)

[634](https://dblp.org/pid/151/8848.html?view=joint&param=634 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Guna Seetharaman](https://dblp.org/pid/38/5099.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[635](https://dblp.org/pid/151/8848.html?view=joint&param=635 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mattia Segù](https://dblp.org/pid/245/2565.html)

[\[c115\]](https://dblp.org/pid/151/8848.html#c115) [\[c113\]](https://dblp.org/pid/151/8848.html#c113) [\[i94\]](https://dblp.org/pid/151/8848.html#i94) [\[i92\]](https://dblp.org/pid/151/8848.html#i92)

[636](https://dblp.org/pid/151/8848.html?view=joint&param=636 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pedro Senna](https://dblp.org/pid/170/3084.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[637](https://dblp.org/pid/151/8848.html?view=joint&param=637 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yonghyeok Seo](https://dblp.org/pid/227/2546.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[638](https://dblp.org/pid/151/8848.html?view=joint&param=638 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mohamad Shahbazi](https://dblp.org/pid/236/6647.html)

[\[c108\]](https://dblp.org/pid/151/8848.html#c108) [\[c99\]](https://dblp.org/pid/151/8848.html#c99) [\[i90\]](https://dblp.org/pid/151/8848.html#i90) [\[i87\]](https://dblp.org/pid/151/8848.html#i87) [\[c83\]](https://dblp.org/pid/151/8848.html#c83) [\[c75\]](https://dblp.org/pid/151/8848.html#c75) [\[i76\]](https://dblp.org/pid/151/8848.html#i76) [\[i68\]](https://dblp.org/pid/151/8848.html#i68)

[639](https://dblp.org/pid/151/8848.html?view=joint&param=639 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Abdelrahman M. Shaker](https://dblp.org/pid/250/0334.html)

[\[c118\]](https://dblp.org/pid/151/8848.html#c118) [\[i95\]](https://dblp.org/pid/151/8848.html#i95)

[640](https://dblp.org/pid/151/8848.html?view=joint&param=640 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Gregory Shakhnarovich](https://dblp.org/pid/17/1926.html)

aka: Greg Shakhnarovich

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[641](https://dblp.org/pid/151/8848.html?view=joint&param=641 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[642](https://dblp.org/pid/151/8848.html?view=joint&param=642 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[643](https://dblp.org/pid/151/8848.html?view=joint&param=643 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pengcheng Shao](https://dblp.org/pid/364/8295.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[644](https://dblp.org/pid/151/8848.html?view=joint&param=644 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yihang She](https://dblp.org/pid/294/4508.html)

[\[c74\]](https://dblp.org/pid/151/8848.html#c74) [\[i63\]](https://dblp.org/pid/151/8848.html#i63)

[645](https://dblp.org/pid/151/8848.html?view=joint&param=645 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mohamed S. Shehata](https://dblp.org/pid/33/2495.html)

aka: Mohamed Shehata 0001

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[646](https://dblp.org/pid/151/8848.html?view=joint&param=646 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Furao Shen](https://dblp.org/pid/80/4685.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[647](https://dblp.org/pid/151/8848.html?view=joint&param=647 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jianbing Shen](https://dblp.org/pid/38/5435.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c42\]](https://dblp.org/pid/151/8848.html#c42) [\[i30\]](https://dblp.org/pid/151/8848.html#i30)

[648](https://dblp.org/pid/151/8848.html?view=joint&param=648 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaoyong Shen](https://dblp.org/pid/71/11418.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[649](https://dblp.org/pid/151/8848.html?view=joint&param=649 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dongseok Shim](https://dblp.org/pid/274/0985.html)

[\[c90\]](https://dblp.org/pid/151/8848.html#c90)

[650](https://dblp.org/pid/151/8848.html?view=joint&param=650 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wooksu Shin](https://dblp.org/pid/327/3602.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[651](https://dblp.org/pid/151/8848.html?view=joint&param=651 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Assaf Shocher](https://dblp.org/pid/211/8006.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27)

[652](https://dblp.org/pid/151/8848.html?view=joint&param=652 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Samarth Shukla](https://dblp.org/pid/220/4107.html)

[\[c77\]](https://dblp.org/pid/151/8848.html#c77) [\[i71\]](https://dblp.org/pid/151/8848.html#i71)

[653](https://dblp.org/pid/151/8848.html?view=joint&param=653 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Liu Si](https://dblp.org/pid/234/0053.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[654](https://dblp.org/pid/151/8848.html?view=joint&param=654 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[655](https://dblp.org/pid/151/8848.html?view=joint&param=655 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wan-Chi Siu](https://dblp.org/pid/61/5203.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[656](https://dblp.org/pid/151/8848.html?view=joint&param=656 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Arnold W. M. Smeulders](https://dblp.org/pid/15/5400.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[657](https://dblp.org/pid/151/8848.html?view=joint&param=657 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kyung-Ah Sohn](https://dblp.org/pid/65/3835.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[658](https://dblp.org/pid/151/8848.html?view=joint&param=658 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Elham Soltanikazemi](https://dblp.org/pid/318/1851.html)

aka: Elham Soltani Kazemi

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[659](https://dblp.org/pid/151/8848.html?view=joint&param=659 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sanghyeok Son](https://dblp.org/pid/294/4695.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[660](https://dblp.org/pid/151/8848.html?view=joint&param=660 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dejia Song](https://dblp.org/pid/260/2975.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[661](https://dblp.org/pid/151/8848.html?view=joint&param=661 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ge Song](https://dblp.org/pid/86/2187.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[662](https://dblp.org/pid/151/8848.html?view=joint&param=662 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ki-Ung Song](https://dblp.org/pid/318/8996.html)

[\[c90\]](https://dblp.org/pid/151/8848.html#c90)

[663](https://dblp.org/pid/151/8848.html?view=joint&param=663 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tianhui Song](https://dblp.org/pid/181/8738.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[664](https://dblp.org/pid/151/8848.html?view=joint&param=664 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[665](https://dblp.org/pid/151/8848.html?view=joint&param=665 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhichao Song](https://dblp.org/pid/169/4022.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[666](https://dblp.org/pid/151/8848.html?view=joint&param=666 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Peter W. J. Staar](https://dblp.org/pid/136/7966.html)

[\[c101\]](https://dblp.org/pid/151/8848.html#c101) [\[i81\]](https://dblp.org/pid/151/8848.html#i81)

[667](https://dblp.org/pid/151/8848.html?view=joint&param=667 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rainer Stiefelhagen](https://dblp.org/pid/31/4699.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[668](https://dblp.org/pid/151/8848.html?view=joint&param=668 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rustam Stolkin](https://dblp.org/pid/72/2344.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[669](https://dblp.org/pid/151/8848.html?view=joint&param=669 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Vitomir Struc](https://dblp.org/pid/47/4796.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[670](https://dblp.org/pid/151/8848.html?view=joint&param=670 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dewei Su](https://dblp.org/pid/249/5714.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[671](https://dblp.org/pid/151/8848.html?view=joint&param=671 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[M. Subrahmanyam 0001](https://dblp.org/pid/61/10849.html)

aka: Subrahmanyam Murala

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[672](https://dblp.org/pid/151/8848.html?view=joint&param=672 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Maitreya Suin](https://dblp.org/pid/254/1457.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28) [\[c28\]](https://dblp.org/pid/151/8848.html#c28) [\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[673](https://dblp.org/pid/151/8848.html?view=joint&param=673 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chao Sun](https://dblp.org/pid/54/3957.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[674](https://dblp.org/pid/151/8848.html?view=joint&param=674 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chong Sun](https://dblp.org/pid/56/2576.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[675](https://dblp.org/pid/151/8848.html?view=joint&param=675 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Han Sun](https://dblp.org/pid/49/6614.html)

[\[c116\]](https://dblp.org/pid/151/8848.html#c116) [\[i84\]](https://dblp.org/pid/151/8848.html#i84)

[676](https://dblp.org/pid/151/8848.html?view=joint&param=676 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jian Sun 0001](https://dblp.org/pid/68/4942-1.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i52\]](https://dblp.org/pid/151/8848.html#i52) [\[c50\]](https://dblp.org/pid/151/8848.html#c50) [\[i36\]](https://dblp.org/pid/151/8848.html#i36)

[677](https://dblp.org/pid/151/8848.html?view=joint&param=677 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jingna Sun](https://dblp.org/pid/255/0702.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[678](https://dblp.org/pid/151/8848.html?view=joint&param=678 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Long Sun](https://dblp.org/pid/151/4095.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[679](https://dblp.org/pid/151/8848.html?view=joint&param=679 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rui Sun 0006](https://dblp.org/pid/01/3595-6.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[680](https://dblp.org/pid/151/8848.html?view=joint&param=680 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenyu Sun](https://dblp.org/pid/92/6021.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[681](https://dblp.org/pid/151/8848.html?view=joint&param=681 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaopeng Sun](https://dblp.org/pid/74/9057.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[682](https://dblp.org/pid/151/8848.html?view=joint&param=682 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xing Sun 0001](https://dblp.org/pid/90/2719-1.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[683](https://dblp.org/pid/151/8848.html?view=joint&param=683 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuxuan Sun 0003](https://dblp.org/pid/194/3079-3.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[684](https://dblp.org/pid/151/8848.html?view=joint&param=684 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jinyoung Sung](https://dblp.org/pid/220/3313.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[685](https://dblp.org/pid/151/8848.html?view=joint&param=685 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ying Tai](https://dblp.org/pid/158/1384.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[686](https://dblp.org/pid/151/8848.html?view=joint&param=686 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yu-Wing Tai](https://dblp.org/pid/40/566.html)

[\[c117\]](https://dblp.org/pid/151/8848.html#c117) [\[c104\]](https://dblp.org/pid/151/8848.html#c104) [\[c102\]](https://dblp.org/pid/151/8848.html#c102) [\[c98\]](https://dblp.org/pid/151/8848.html#c98) [\[c97\]](https://dblp.org/pid/151/8848.html#c97) [\[i89\]](https://dblp.org/pid/151/8848.html#i89) [\[i86\]](https://dblp.org/pid/151/8848.html#i86) [\[i85\]](https://dblp.org/pid/151/8848.html#i85) [\[i83\]](https://dblp.org/pid/151/8848.html#i83) [\[c88\]](https://dblp.org/pid/151/8848.html#c88) [\[c76\]](https://dblp.org/pid/151/8848.html#c76) [\[i66\]](https://dblp.org/pid/151/8848.html#i66) [\[c55\]](https://dblp.org/pid/151/8848.html#c55) [\[i51\]](https://dblp.org/pid/151/8848.html#i51) [\[i43\]](https://dblp.org/pid/151/8848.html#i43) [\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[687](https://dblp.org/pid/151/8848.html?view=joint&param=687 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=2)

[Hakob Tamazyan](https://dblp.org/pid/365/3819.html)

[\[i96\]](https://dblp.org/pid/151/8848.html#i96)

[688](https://dblp.org/pid/151/8848.html?view=joint&param=688 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chi-Keung Tang](https://dblp.org/pid/34/4366.html)

[\[c117\]](https://dblp.org/pid/151/8848.html#c117) [\[c104\]](https://dblp.org/pid/151/8848.html#c104) [\[c102\]](https://dblp.org/pid/151/8848.html#c102) [\[c98\]](https://dblp.org/pid/151/8848.html#c98) [\[c97\]](https://dblp.org/pid/151/8848.html#c97) [\[i89\]](https://dblp.org/pid/151/8848.html#i89) [\[i86\]](https://dblp.org/pid/151/8848.html#i86) [\[i85\]](https://dblp.org/pid/151/8848.html#i85) [\[i83\]](https://dblp.org/pid/151/8848.html#i83) [\[c88\]](https://dblp.org/pid/151/8848.html#c88) [\[c76\]](https://dblp.org/pid/151/8848.html#c76) [\[i66\]](https://dblp.org/pid/151/8848.html#i66) [\[c55\]](https://dblp.org/pid/151/8848.html#c55) [\[i51\]](https://dblp.org/pid/151/8848.html#i51) [\[i43\]](https://dblp.org/pid/151/8848.html#i43)

[689](https://dblp.org/pid/151/8848.html?view=joint&param=689 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chuanming Tang](https://dblp.org/pid/237/6254.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[690](https://dblp.org/pid/151/8848.html?view=joint&param=690 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jie Tang 0006](https://dblp.org/pid/181/2702-6.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[691](https://dblp.org/pid/151/8848.html?view=joint&param=691 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jin Tang 0001](https://dblp.org/pid/56/4951-1.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[692](https://dblp.org/pid/151/8848.html?view=joint&param=692 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jinhui Tang 0001](https://dblp.org/pid/75/1030.html)

[\[c90\]](https://dblp.org/pid/151/8848.html#c90) [\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[693](https://dblp.org/pid/151/8848.html?view=joint&param=693 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ming Tang 0001](https://dblp.org/pid/73/4373-1.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[694](https://dblp.org/pid/151/8848.html?view=joint&param=694 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenjie Tang](https://dblp.org/pid/87/7879.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[695](https://dblp.org/pid/151/8848.html?view=joint&param=695 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xu Tang](https://dblp.org/pid/123/7064.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[696](https://dblp.org/pid/151/8848.html?view=joint&param=696 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[697](https://dblp.org/pid/151/8848.html?view=joint&param=697 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dacheng Tao](https://dblp.org/pid/46/3391.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[698](https://dblp.org/pid/151/8848.html?view=joint&param=698 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ran Tao 0004](https://dblp.org/pid/99/955-4.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[699](https://dblp.org/pid/151/8848.html?view=joint&param=699 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenbing Tao](https://dblp.org/pid/73/188.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[700](https://dblp.org/pid/151/8848.html?view=joint&param=700 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xin Tao 0001](https://dblp.org/pid/98/7443-1.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[701](https://dblp.org/pid/151/8848.html?view=joint&param=701 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ruxandra Tapu](https://dblp.org/pid/45/10237.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[702](https://dblp.org/pid/151/8848.html?view=joint&param=702 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhu Teng](https://dblp.org/pid/132/2247.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[703](https://dblp.org/pid/151/8848.html?view=joint&param=703 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jean-Philippe Thiran](https://dblp.org/pid/t/JeanPhilippeThiran.html)

[\[i93\]](https://dblp.org/pid/151/8848.html#i93)

[704](https://dblp.org/pid/151/8848.html?view=joint&param=704 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Cheng Tian](https://dblp.org/pid/76/8808.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[705](https://dblp.org/pid/151/8848.html?view=joint&param=705 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xinmei Tian 0001](https://dblp.org/pid/03/5204-1.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[706](https://dblp.org/pid/151/8848.html?view=joint&param=706 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[i93\]](https://dblp.org/pid/151/8848.html#i93) [\[j6\]](https://dblp.org/pid/151/8848.html#j6) [\[c94\]](https://dblp.org/pid/151/8848.html#c94) [\[i87\]](https://dblp.org/pid/151/8848.html#i87) [\[c90\]](https://dblp.org/pid/151/8848.html#c90) [\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[c84\]](https://dblp.org/pid/151/8848.html#c84) [\[c83\]](https://dblp.org/pid/151/8848.html#c83) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c77\]](https://dblp.org/pid/151/8848.html#c77) [\[c73\]](https://dblp.org/pid/151/8848.html#c73) [\[i75\]](https://dblp.org/pid/151/8848.html#i75) [\[i74\]](https://dblp.org/pid/151/8848.html#i74) [\[i71\]](https://dblp.org/pid/151/8848.html#i71) [\[i68\]](https://dblp.org/pid/151/8848.html#i68) [\[c72\]](https://dblp.org/pid/151/8848.html#c72) [\[c71\]](https://dblp.org/pid/151/8848.html#c71) [\[c70\]](https://dblp.org/pid/151/8848.html#c70) [\[c69\]](https://dblp.org/pid/151/8848.html#c69) [\[c67\]](https://dblp.org/pid/151/8848.html#c67) [\[c66\]](https://dblp.org/pid/151/8848.html#c66) [\[c64\]](https://dblp.org/pid/151/8848.html#c64) [\[c63\]](https://dblp.org/pid/151/8848.html#c63) [\[c59\]](https://dblp.org/pid/151/8848.html#c59) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c57\]](https://dblp.org/pid/151/8848.html#c57) [\[c56\]](https://dblp.org/pid/151/8848.html#c56) [\[i61\]](https://dblp.org/pid/151/8848.html#i61) [\[i60\]](https://dblp.org/pid/151/8848.html#i60) [\[i59\]](https://dblp.org/pid/151/8848.html#i59) [\[i58\]](https://dblp.org/pid/151/8848.html#i58) [\[i57\]](https://dblp.org/pid/151/8848.html#i57) [\[i52\]](https://dblp.org/pid/151/8848.html#i52) [\[i50\]](https://dblp.org/pid/151/8848.html#i50) [\[i49\]](https://dblp.org/pid/151/8848.html#i49) [\[i47\]](https://dblp.org/pid/151/8848.html#i47) [\[i44\]](https://dblp.org/pid/151/8848.html#i44) [\[c54\]](https://dblp.org/pid/151/8848.html#c54) [\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[c49\]](https://dblp.org/pid/151/8848.html#c49) [\[c48\]](https://dblp.org/pid/151/8848.html#c48) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[c45\]](https://dblp.org/pid/151/8848.html#c45) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c41\]](https://dblp.org/pid/151/8848.html#c41) [\[c40\]](https://dblp.org/pid/151/8848.html#c40) [\[c39\]](https://dblp.org/pid/151/8848.html#c39) [\[c38\]](https://dblp.org/pid/151/8848.html#c38) [\[i39\]](https://dblp.org/pid/151/8848.html#i39) [\[i38\]](https://dblp.org/pid/151/8848.html#i38) [\[i37\]](https://dblp.org/pid/151/8848.html#i37) [\[i35\]](https://dblp.org/pid/151/8848.html#i35) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[i33\]](https://dblp.org/pid/151/8848.html#i33) [\[i32\]](https://dblp.org/pid/151/8848.html#i32) [\[i31\]](https://dblp.org/pid/151/8848.html#i31) [\[i29\]](https://dblp.org/pid/151/8848.html#i29) [\[i28\]](https://dblp.org/pid/151/8848.html#i28) [\[i27\]](https://dblp.org/pid/151/8848.html#i27) [\[i26\]](https://dblp.org/pid/151/8848.html#i26) [\[c37\]](https://dblp.org/pid/151/8848.html#c37) [\[c33\]](https://dblp.org/pid/151/8848.html#c33) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c30\]](https://dblp.org/pid/151/8848.html#c30) [\[c29\]](https://dblp.org/pid/151/8848.html#c29) [\[c28\]](https://dblp.org/pid/151/8848.html#c28) [\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[c26\]](https://dblp.org/pid/151/8848.html#c26) [\[i22\]](https://dblp.org/pid/151/8848.html#i22) [\[i17\]](https://dblp.org/pid/151/8848.html#i17) [\[i15\]](https://dblp.org/pid/151/8848.html#i15) [\[i14\]](https://dblp.org/pid/151/8848.html#i14)

[707](https://dblp.org/pid/151/8848.html?view=joint&param=707 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Federico Tombari](https://dblp.org/pid/16/3539.html)

[\[c93\]](https://dblp.org/pid/151/8848.html#c93) [\[i64\]](https://dblp.org/pid/151/8848.html#i64)

[708](https://dblp.org/pid/151/8848.html?view=joint&param=708 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Alessio Tonioni](https://dblp.org/pid/203/8831.html)

[\[c99\]](https://dblp.org/pid/151/8848.html#c99) [\[i90\]](https://dblp.org/pid/151/8848.html#i90)

[709](https://dblp.org/pid/151/8848.html?view=joint&param=709 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[710](https://dblp.org/pid/151/8848.html?view=joint&param=710 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Patrik Tosteberg](https://dblp.org/pid/200/8154.html)

[\[c19\]](https://dblp.org/pid/151/8848.html#c19) [\[i8\]](https://dblp.org/pid/151/8848.html#i8)

[711](https://dblp.org/pid/151/8848.html?view=joint&param=711 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Imad Eddine Toubal](https://dblp.org/pid/292/6360.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[712](https://dblp.org/pid/151/8848.html?view=joint&param=712 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Antoine Tran](https://dblp.org/pid/173/8869.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[713](https://dblp.org/pid/151/8848.html?view=joint&param=713 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Khanh-Tung Tran](https://dblp.org/pid/359/3793.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[714](https://dblp.org/pid/151/8848.html?view=joint&param=714 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ardhendu Shekhar Tripathi](https://dblp.org/pid/141/9949.html)

[\[c77\]](https://dblp.org/pid/151/8848.html#c77) [\[i71\]](https://dblp.org/pid/151/8848.html#i71) [\[c57\]](https://dblp.org/pid/151/8848.html#c57) [\[i26\]](https://dblp.org/pid/151/8848.html#i26) [\[c37\]](https://dblp.org/pid/151/8848.html#c37) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[715](https://dblp.org/pid/151/8848.html?view=joint&param=715 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Prune Truong](https://dblp.org/pid/247/5738.html)

[\[j6\]](https://dblp.org/pid/151/8848.html#j6) [\[c87\]](https://dblp.org/pid/151/8848.html#c87) [\[i72\]](https://dblp.org/pid/151/8848.html#i72) [\[c67\]](https://dblp.org/pid/151/8848.html#c67) [\[c61\]](https://dblp.org/pid/151/8848.html#c61) [\[i61\]](https://dblp.org/pid/151/8848.html#i61) [\[i54\]](https://dblp.org/pid/151/8848.html#i54) [\[i47\]](https://dblp.org/pid/151/8848.html#i47) [\[c49\]](https://dblp.org/pid/151/8848.html#c49) [\[c38\]](https://dblp.org/pid/151/8848.html#c38) [\[i27\]](https://dblp.org/pid/151/8848.html#i27) [\[i14\]](https://dblp.org/pid/151/8848.html#i14)

[716](https://dblp.org/pid/151/8848.html?view=joint&param=716 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[717](https://dblp.org/pid/151/8848.html?view=joint&param=717 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Stavros Tsogkas](https://dblp.org/pid/119/1444.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[718](https://dblp.org/pid/151/8848.html?view=joint&param=718 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[John K. Tsotsos](https://dblp.org/pid/t/JohnKTsotsos.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[719](https://dblp.org/pid/151/8848.html?view=joint&param=719 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Norimichi Ukita](https://dblp.org/pid/46/5881.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i52\]](https://dblp.org/pid/151/8848.html#i52) [\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[720](https://dblp.org/pid/151/8848.html?view=joint&param=720 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rao Muhammad Umer](https://dblp.org/pid/248/9258.html)

[\[i52\]](https://dblp.org/pid/151/8848.html#i52) [\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[721](https://dblp.org/pid/151/8848.html?view=joint&param=721 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bedirhan Uzun](https://dblp.org/pid/247/8937.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[722](https://dblp.org/pid/151/8848.html?view=joint&param=722 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jack Valmadre](https://dblp.org/pid/50/8535.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[723](https://dblp.org/pid/151/8848.html?view=joint&param=723 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Michel F. Valstar](https://dblp.org/pid/00/2794.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[724](https://dblp.org/pid/151/8848.html?view=joint&param=724 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=2)

[Ani Vanyan](https://dblp.org/pid/313/5252.html)

[\[i96\]](https://dblp.org/pid/151/8848.html#i96)

[725](https://dblp.org/pid/151/8848.html?view=joint&param=725 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Anton Varfolomieiev](https://dblp.org/pid/188/7504.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[726](https://dblp.org/pid/151/8848.html?view=joint&param=726 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Andrea Vedaldi](https://dblp.org/pid/99/2825.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[727](https://dblp.org/pid/151/8848.html?view=joint&param=727 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Erik Velasco-Salido](https://dblp.org/pid/213/4199.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[728](https://dblp.org/pid/151/8848.html?view=joint&param=728 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pallavi M. Venugopal](https://dblp.org/pid/204/9669.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[729](https://dblp.org/pid/151/8848.html?view=joint&param=729 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Om Prakash Verma](https://dblp.org/pid/61/8145.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[730](https://dblp.org/pid/151/8848.html?view=joint&param=730 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pablo Vicente-Moñivar](https://dblp.org/pid/234/0077.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[731](https://dblp.org/pid/151/8848.html?view=joint&param=731 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Vibhav Vineet](https://dblp.org/pid/02/8067.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[732](https://dblp.org/pid/151/8848.html?view=joint&param=732 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jash Vira](https://dblp.org/pid/364/8266.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[733](https://dblp.org/pid/151/8848.html?view=joint&param=733 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sergio Vivas](https://dblp.org/pid/233/9963.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[734](https://dblp.org/pid/151/8848.html?view=joint&param=734 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Paul Voigtlaender](https://dblp.org/pid/166/6430.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[735](https://dblp.org/pid/151/8848.html?view=joint&param=735 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tomás Vojír](https://dblp.org/pid/142/5749.html)

aka: Tomas Vojir

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[736](https://dblp.org/pid/151/8848.html?view=joint&param=736 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xuan-Son Vu](https://dblp.org/pid/151/8673.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[737](https://dblp.org/pid/151/8848.html?view=joint&param=737 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Stéphane Vujasinovic](https://dblp.org/pid/237/5053.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[738](https://dblp.org/pid/151/8848.html?view=joint&param=738 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ryan Walsh](https://dblp.org/pid/188/7715.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[739](https://dblp.org/pid/151/8848.html?view=joint&param=739 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Cheng Wan 0006](https://dblp.org/pid/118/7267-6.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[740](https://dblp.org/pid/151/8848.html?view=joint&param=740 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jia Wan 0001](https://dblp.org/pid/13/6504-1.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[741](https://dblp.org/pid/151/8848.html?view=joint&param=741 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Cong Wang 0018](https://dblp.org/pid/18/2771-18.html)

[\[c90\]](https://dblp.org/pid/151/8848.html#c90)

[742](https://dblp.org/pid/151/8848.html?view=joint&param=742 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[743](https://dblp.org/pid/151/8848.html?view=joint&param=743 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fei Wang 0032](https://dblp.org/pid/52/3194-32.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[744](https://dblp.org/pid/151/8848.html?view=joint&param=744 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Feifan Wang](https://dblp.org/pid/213/0685.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[745](https://dblp.org/pid/151/8848.html?view=joint&param=745 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Guangting Wang](https://dblp.org/pid/227/7195.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[746](https://dblp.org/pid/151/8848.html?view=joint&param=746 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haicheng Wang](https://dblp.org/pid/150/4188.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[747](https://dblp.org/pid/151/8848.html?view=joint&param=747 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[He Wang 0028](https://dblp.org/pid/01/6368-28.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[748](https://dblp.org/pid/151/8848.html?view=joint&param=748 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hua Wang 0015](https://dblp.org/pid/33/3535-15.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[749](https://dblp.org/pid/151/8848.html?view=joint&param=749 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Huibing Wang](https://dblp.org/pid/150/0713.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[750](https://dblp.org/pid/151/8848.html?view=joint&param=750 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jinqiao Wang](https://dblp.org/pid/67/4236.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[751](https://dblp.org/pid/151/8848.html?view=joint&param=751 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kangkang Wang](https://dblp.org/pid/03/9859.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[752](https://dblp.org/pid/151/8848.html?view=joint&param=752 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Li-Wen Wang](https://dblp.org/pid/33/10711.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[753](https://dblp.org/pid/151/8848.html?view=joint&param=753 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Liang Wang 0001](https://dblp.org/pid/56/4499-1.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[754](https://dblp.org/pid/151/8848.html?view=joint&param=754 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[755](https://dblp.org/pid/151/8848.html?view=joint&param=755 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[756](https://dblp.org/pid/151/8848.html?view=joint&param=756 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[757](https://dblp.org/pid/151/8848.html?view=joint&param=757 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Linyuan Wang](https://dblp.org/pid/138/5963.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[758](https://dblp.org/pid/151/8848.html?view=joint&param=758 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Naiyan Wang](https://dblp.org/pid/31/9922.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[759](https://dblp.org/pid/151/8848.html?view=joint&param=759 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ning Wang 0020](https://dblp.org/pid/46/2005-20.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[760](https://dblp.org/pid/151/8848.html?view=joint&param=760 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qiang Wang 0023](https://dblp.org/pid/64/5630-23.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[761](https://dblp.org/pid/151/8848.html?view=joint&param=761 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qiang Wang 0051](https://dblp.org/pid/64/5630-51.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[762](https://dblp.org/pid/151/8848.html?view=joint&param=762 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qin Wang 0013](https://dblp.org/pid/35/1647-13.html)

[\[c105\]](https://dblp.org/pid/151/8848.html#c105)

[763](https://dblp.org/pid/151/8848.html?view=joint&param=763 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Runling Wang](https://dblp.org/pid/224/4642.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[764](https://dblp.org/pid/151/8848.html?view=joint&param=764 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shuangquan Wang](https://dblp.org/pid/23/5003.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[765](https://dblp.org/pid/151/8848.html?view=joint&param=765 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Siwen Wang](https://dblp.org/pid/176/5066.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[766](https://dblp.org/pid/151/8848.html?view=joint&param=766 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Song Wang 0002](https://dblp.org/pid/62/3151-2.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[767](https://dblp.org/pid/151/8848.html?view=joint&param=767 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tiancai Wang](https://dblp.org/pid/179/0530.html)

[\[c50\]](https://dblp.org/pid/151/8848.html#c50) [\[i36\]](https://dblp.org/pid/151/8848.html#i36)

[768](https://dblp.org/pid/151/8848.html?view=joint&param=768 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wei Wang 0335](https://dblp.org/pid/35/7092-335.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[769](https://dblp.org/pid/151/8848.html?view=joint&param=769 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Weizhao Wang](https://dblp.org/pid/39/2359.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[770](https://dblp.org/pid/151/8848.html?view=joint&param=770 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenguan Wang](https://dblp.org/pid/145/1078.html)

[\[i48\]](https://dblp.org/pid/151/8848.html#i48) [\[c42\]](https://dblp.org/pid/151/8848.html#c42) [\[i30\]](https://dblp.org/pid/151/8848.html#i30)

[771](https://dblp.org/pid/151/8848.html?view=joint&param=771 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenhao Wang](https://dblp.org/pid/57/9813.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[772](https://dblp.org/pid/151/8848.html?view=joint&param=772 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenyi Wang 0005](https://dblp.org/pid/79/2722-5.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[773](https://dblp.org/pid/151/8848.html?view=joint&param=773 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaomeng Wang](https://dblp.org/pid/35/6677.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[774](https://dblp.org/pid/151/8848.html?view=joint&param=774 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xuehui Wang](https://dblp.org/pid/78/6531.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[775](https://dblp.org/pid/151/8848.html?view=joint&param=775 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yaowei Wang 0001](https://dblp.org/pid/68/2992-1.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[776](https://dblp.org/pid/151/8848.html?view=joint&param=776 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yifan Wang 0004](https://dblp.org/pid/47/6959-4.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[777](https://dblp.org/pid/151/8848.html?view=joint&param=777 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ying-Ming Wang](https://dblp.org/pid/59/605.html)

aka: Yingming Wang

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[778](https://dblp.org/pid/151/8848.html?view=joint&param=778 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[779](https://dblp.org/pid/151/8848.html?view=joint&param=779 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yunhong Wang 0001](https://dblp.org/pid/95/6251.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[780](https://dblp.org/pid/151/8848.html?view=joint&param=780 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zeyu Wang 0008](https://dblp.org/pid/132/7882-8.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[781](https://dblp.org/pid/151/8848.html?view=joint&param=781 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zezhou Wang](https://dblp.org/pid/204/1179.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[782](https://dblp.org/pid/151/8848.html?view=joint&param=782 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhepeng Wang 0002](https://dblp.org/pid/242/8456-2.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[783](https://dblp.org/pid/151/8848.html?view=joint&param=783 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhihui Wang 0001](https://dblp.org/pid/65/2749-1.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[784](https://dblp.org/pid/151/8848.html?view=joint&param=784 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhongyuan Wang 0001](https://dblp.org/pid/84/6394-1.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[785](https://dblp.org/pid/151/8848.html?view=joint&param=785 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Syed Talal Wasim](https://dblp.org/pid/344/4424.html)

[\[c118\]](https://dblp.org/pid/151/8848.html#c118) [\[i95\]](https://dblp.org/pid/151/8848.html#i95)

[786](https://dblp.org/pid/151/8848.html?view=joint&param=786 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Valéry Weber](https://dblp.org/pid/86/5323.html)

[\[c101\]](https://dblp.org/pid/151/8848.html#c101) [\[i81\]](https://dblp.org/pid/151/8848.html#i81)

[787](https://dblp.org/pid/151/8848.html?view=joint&param=787 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dongyoon Wee](https://dblp.org/pid/234/0087.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[788](https://dblp.org/pid/151/8848.html?view=joint&param=788 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wei Wei 0008](https://dblp.org/pid/24/4105-8.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[789](https://dblp.org/pid/151/8848.html?view=joint&param=789 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Joost van de Weijer 0001](https://dblp.org/pid/67/3379.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[j2\]](https://dblp.org/pid/151/8848.html#j2) [\[c34\]](https://dblp.org/pid/151/8848.html#c34) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c31\]](https://dblp.org/pid/151/8848.html#c31) [\[i19\]](https://dblp.org/pid/151/8848.html#i19) [\[i18\]](https://dblp.org/pid/151/8848.html#i18) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[i11\]](https://dblp.org/pid/151/8848.html#i11) [\[c3\]](https://dblp.org/pid/151/8848.html#c3) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[790](https://dblp.org/pid/151/8848.html?view=joint&param=790 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Longyin Wen](https://dblp.org/pid/119/1468.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[791](https://dblp.org/pid/151/8848.html?view=joint&param=791 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shilei Wen](https://dblp.org/pid/159/2939.html)

[\[c52\]](https://dblp.org/pid/151/8848.html#c52) [\[i33\]](https://dblp.org/pid/151/8848.html#i33)

[792](https://dblp.org/pid/151/8848.html?view=joint&param=792 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhihong Wen](https://dblp.org/pid/216/7668.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[793](https://dblp.org/pid/151/8848.html?view=joint&param=793 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Valentin Wolf](https://dblp.org/pid/283/5347.html)

[\[c72\]](https://dblp.org/pid/151/8848.html#c72) [\[i58\]](https://dblp.org/pid/151/8848.html#i58)

[794](https://dblp.org/pid/151/8848.html?view=joint&param=794 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yu Seung Won](https://dblp.org/pid/254/1498.html)

[\[c27\]](https://dblp.org/pid/151/8848.html#c27) [\[i15\]](https://dblp.org/pid/151/8848.html#i15)

[795](https://dblp.org/pid/151/8848.html?view=joint&param=795 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Baoyuan Wu](https://dblp.org/pid/73/7781.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[796](https://dblp.org/pid/151/8848.html?view=joint&param=796 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chenyan Wu](https://dblp.org/pid/76/1190.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[797](https://dblp.org/pid/151/8848.html?view=joint&param=797 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[798](https://dblp.org/pid/151/8848.html?view=joint&param=798 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Guangyang Wu](https://dblp.org/pid/254/8240.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[799](https://dblp.org/pid/151/8848.html?view=joint&param=799 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haoning Wu 0001](https://dblp.org/pid/264/5802-1.html)

aka: Timothy Haoning Wu 0001

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[800](https://dblp.org/pid/151/8848.html?view=joint&param=800 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiannan Wu](https://dblp.org/pid/277/0616.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[801](https://dblp.org/pid/151/8848.html?view=joint&param=801 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jingjing Wu](https://dblp.org/pid/27/2384.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[802](https://dblp.org/pid/151/8848.html?view=joint&param=802 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jinlin Wu](https://dblp.org/pid/123/7200.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[803](https://dblp.org/pid/151/8848.html?view=joint&param=803 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qi Wu 0017](https://dblp.org/pid/96/3446-17.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[804](https://dblp.org/pid/151/8848.html?view=joint&param=804 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qiangqiang Wu](https://dblp.org/pid/193/1415.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[805](https://dblp.org/pid/151/8848.html?view=joint&param=805 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sihang Wu](https://dblp.org/pid/234/0006.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[806](https://dblp.org/pid/151/8848.html?view=joint&param=806 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wei Wu 0021](https://dblp.org/pid/95/6985-21.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[807](https://dblp.org/pid/151/8848.html?view=joint&param=807 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaohe Wu](https://dblp.org/pid/20/3663.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[808](https://dblp.org/pid/151/8848.html?view=joint&param=808 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

aka: Xiao-Jun Wu 0001

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[809](https://dblp.org/pid/151/8848.html?view=joint&param=809 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yi Wu 0001](https://dblp.org/pid/44/3684-1.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[810](https://dblp.org/pid/151/8848.html?view=joint&param=810 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhirong Wu](https://dblp.org/pid/147/5025.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[811](https://dblp.org/pid/151/8848.html?view=joint&param=811 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mariusz Wzorek](https://dblp.org/pid/89/4943.html)

[\[c1\]](https://dblp.org/pid/151/8848.html#c1)

[812](https://dblp.org/pid/151/8848.html?view=joint&param=812 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Anqi Xiao](https://dblp.org/pid/307/8649.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[813](https://dblp.org/pid/151/8848.html?view=joint&param=813 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jingjing Xiao](https://dblp.org/pid/121/0292.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[814](https://dblp.org/pid/151/8848.html?view=joint&param=814 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zeyu Xiao](https://dblp.org/pid/276/3139.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[815](https://dblp.org/pid/151/8848.html?view=joint&param=815 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[816](https://dblp.org/pid/151/8848.html?view=joint&param=816 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jinxia Xie](https://dblp.org/pid/294/3376.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[817](https://dblp.org/pid/151/8848.html?view=joint&param=817 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Nianhao Xie](https://dblp.org/pid/213/4181.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[818](https://dblp.org/pid/151/8848.html?view=joint&param=818 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tangxin Xie](https://dblp.org/pid/255/7347.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[819](https://dblp.org/pid/151/8848.html?view=joint&param=819 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Junliang Xing](https://dblp.org/pid/43/7659.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[820](https://dblp.org/pid/151/8848.html?view=joint&param=820 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tengfei Xing](https://dblp.org/pid/82/1822.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[821](https://dblp.org/pid/151/8848.html?view=joint&param=821 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yifan Xing](https://dblp.org/pid/93/10423.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[822](https://dblp.org/pid/151/8848.html?view=joint&param=822 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Changzhen Xiong](https://dblp.org/pid/14/965.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[823](https://dblp.org/pid/151/8848.html?view=joint&param=823 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dongliang Xiong](https://dblp.org/pid/192/3737.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[824](https://dblp.org/pid/151/8848.html?view=joint&param=824 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhiwei Xiong](https://dblp.org/pid/54/6827.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[825](https://dblp.org/pid/151/8848.html?view=joint&param=825 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Changsheng Xu](https://dblp.org/pid/85/1301.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[826](https://dblp.org/pid/151/8848.html?view=joint&param=826 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chenlong Xu](https://dblp.org/pid/315/8714.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[827](https://dblp.org/pid/151/8848.html?view=joint&param=827 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jingtao Xu](https://dblp.org/pid/119/1746.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[828](https://dblp.org/pid/151/8848.html?view=joint&param=828 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Min Xu 0001](https://dblp.org/pid/09/0-1.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[829](https://dblp.org/pid/151/8848.html?view=joint&param=829 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pengfei Xu 0013](https://dblp.org/pid/04/383-13.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[830](https://dblp.org/pid/151/8848.html?view=joint&param=830 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Rongjian Xu](https://dblp.org/pid/193/0865.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[831](https://dblp.org/pid/151/8848.html?view=joint&param=831 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ruikang Xu](https://dblp.org/pid/292/4088.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[832](https://dblp.org/pid/151/8848.html?view=joint&param=832 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[833](https://dblp.org/pid/151/8848.html?view=joint&param=833 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wei Xu 0017](https://dblp.org/pid/32/1213-17.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[834](https://dblp.org/pid/151/8848.html?view=joint&param=834 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenjie Xu](https://dblp.org/pid/25/1820.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[835](https://dblp.org/pid/151/8848.html?view=joint&param=835 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiang Xu](https://dblp.org/pid/126/2962.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[836](https://dblp.org/pid/151/8848.html?view=joint&param=836 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xuemiao Xu](https://dblp.org/pid/74/6722.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[837](https://dblp.org/pid/151/8848.html?view=joint&param=837 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yinda Xu](https://dblp.org/pid/254/1072.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[838](https://dblp.org/pid/151/8848.html?view=joint&param=838 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yong Xu 0007](https://dblp.org/pid/07/4630-7.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[839](https://dblp.org/pid/151/8848.html?view=joint&param=839 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuanyou Xu](https://dblp.org/pid/248/7663.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[840](https://dblp.org/pid/151/8848.html?view=joint&param=840 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yufei Xu](https://dblp.org/pid/43/7400.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[841](https://dblp.org/pid/151/8848.html?view=joint&param=841 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhan Xu](https://dblp.org/pid/26/5600.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[842](https://dblp.org/pid/151/8848.html?view=joint&param=842 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[843](https://dblp.org/pid/151/8848.html?view=joint&param=843 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zizheng Xun](https://dblp.org/pid/340/1441.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[844](https://dblp.org/pid/151/8848.html?view=joint&param=844 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[845](https://dblp.org/pid/151/8848.html?view=joint&param=845 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qiong Yan](https://dblp.org/pid/122/4814.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[846](https://dblp.org/pid/151/8848.html?view=joint&param=846 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[847](https://dblp.org/pid/151/8848.html?view=joint&param=847 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Youliang Yan](https://dblp.org/pid/135/5316.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[848](https://dblp.org/pid/151/8848.html?view=joint&param=848 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Biao Yang](https://dblp.org/pid/26/103.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[849](https://dblp.org/pid/151/8848.html?view=joint&param=849 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dawei Yang](https://dblp.org/pid/22/1038.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[850](https://dblp.org/pid/151/8848.html?view=joint&param=850 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fan Yang 0035](https://dblp.org/pid/29/3081-35.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[851](https://dblp.org/pid/151/8848.html?view=joint&param=851 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fuzhi Yang](https://dblp.org/pid/264/5783.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[852](https://dblp.org/pid/151/8848.html?view=joint&param=852 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jialin Yang](https://dblp.org/pid/52/5406.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[853](https://dblp.org/pid/151/8848.html?view=joint&param=853 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[854](https://dblp.org/pid/151/8848.html?view=joint&param=854 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kang Yang](https://dblp.org/pid/86/8501.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[855](https://dblp.org/pid/151/8848.html?view=joint&param=855 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lingxiao Yang](https://dblp.org/pid/56/7126.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[856](https://dblp.org/pid/151/8848.html?view=joint&param=856 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ming-Hsuan Yang 0001](https://dblp.org/pid/79/3711.html)

[\[c118\]](https://dblp.org/pid/151/8848.html#c118) [\[c107\]](https://dblp.org/pid/151/8848.html#c107) [\[i95\]](https://dblp.org/pid/151/8848.html#i95) [\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[i62\]](https://dblp.org/pid/151/8848.html#i62) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[857](https://dblp.org/pid/151/8848.html?view=joint&param=857 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Subin Yang](https://dblp.org/pid/144/2910.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[858](https://dblp.org/pid/151/8848.html?view=joint&param=858 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tianyu Yang 0003](https://dblp.org/pid/120/8076-3.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[859](https://dblp.org/pid/151/8848.html?view=joint&param=859 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tong Yang 0005](https://dblp.org/pid/44/7710-5.html)

[\[c50\]](https://dblp.org/pid/151/8848.html#c50) [\[i36\]](https://dblp.org/pid/151/8848.html#i36)

[860](https://dblp.org/pid/151/8848.html?view=joint&param=860 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[861](https://dblp.org/pid/151/8848.html?view=joint&param=861 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wentao Yang 0003](https://dblp.org/pid/65/9079-3.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[862](https://dblp.org/pid/151/8848.html?view=joint&param=862 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenyan Yang](https://dblp.org/pid/119/2426.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[863](https://dblp.org/pid/151/8848.html?view=joint&param=863 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[864](https://dblp.org/pid/151/8848.html?view=joint&param=864 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xin Yang 0009](https://dblp.org/pid/44/1152-9.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[865](https://dblp.org/pid/151/8848.html?view=joint&param=865 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yi Yang 0001](https://dblp.org/pid/33/4854-1.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[866](https://dblp.org/pid/151/8848.html?view=joint&param=866 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yicai Yang](https://dblp.org/pid/233/9957.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[867](https://dblp.org/pid/151/8848.html?view=joint&param=867 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yichun Yang](https://dblp.org/pid/249/9678.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[868](https://dblp.org/pid/151/8848.html?view=joint&param=868 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yung-Hsu Yang](https://dblp.org/pid/288/0092.html)

[\[c113\]](https://dblp.org/pid/151/8848.html#c113) [\[i92\]](https://dblp.org/pid/151/8848.html#i92)

[869](https://dblp.org/pid/151/8848.html?view=joint&param=869 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhongbao Yang](https://dblp.org/pid/327/3472.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[870](https://dblp.org/pid/151/8848.html?view=joint&param=870 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zongxin Yang](https://dblp.org/pid/249/5456.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[871](https://dblp.org/pid/151/8848.html?view=joint&param=871 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mingde Yao](https://dblp.org/pid/253/9580.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[872](https://dblp.org/pid/151/8848.html?view=joint&param=872 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shizeng Yao](https://dblp.org/pid/188/7638.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[873](https://dblp.org/pid/151/8848.html?view=joint&param=873 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuncon Yao](https://dblp.org/pid/284/2556.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[874](https://dblp.org/pid/151/8848.html?view=joint&param=874 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fuma Yasue](https://dblp.org/pid/327/3315.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[875](https://dblp.org/pid/151/8848.html?view=joint&param=875 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Botao Ye](https://dblp.org/pid/227/4610.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[876](https://dblp.org/pid/151/8848.html?view=joint&param=876 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mingqiao Ye](https://dblp.org/pid/285/9253.html)

[\[c112\]](https://dblp.org/pid/151/8848.html#c112) [\[c102\]](https://dblp.org/pid/151/8848.html#c102) [\[c98\]](https://dblp.org/pid/151/8848.html#c98) [\[i86\]](https://dblp.org/pid/151/8848.html#i86) [\[i83\]](https://dblp.org/pid/151/8848.html#i83) [\[i78\]](https://dblp.org/pid/151/8848.html#i78)

[877](https://dblp.org/pid/151/8848.html?view=joint&param=877 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yu Ye 0004](https://dblp.org/pid/129/0969-4.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[878](https://dblp.org/pid/151/8848.html?view=joint&param=878 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dit-Yan Yeung](https://dblp.org/pid/41/5668.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[879](https://dblp.org/pid/151/8848.html?view=joint&param=879 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Eunu Yi](https://dblp.org/pid/260/3303.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[880](https://dblp.org/pid/151/8848.html?view=joint&param=880 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kwang Moo Yi](https://dblp.org/pid/30/5082.html)

[\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[881](https://dblp.org/pid/151/8848.html?view=joint&param=881 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Peng Yi 0002](https://dblp.org/pid/98/1202-2.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[882](https://dblp.org/pid/151/8848.html?view=joint&param=882 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[J. Yin](https://dblp.org/pid/51/2242.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[883](https://dblp.org/pid/151/8848.html?view=joint&param=883 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jun Yin 0003](https://dblp.org/pid/58/5423-3.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[884](https://dblp.org/pid/151/8848.html?view=joint&param=884 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xuanwu Yin](https://dblp.org/pid/119/0001.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[885](https://dblp.org/pid/151/8848.html?view=joint&param=885 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jaejun Yoo 0001](https://dblp.org/pid/141/8878-1.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[886](https://dblp.org/pid/151/8848.html?view=joint&param=886 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chenyu You](https://dblp.org/pid/191/9432.html)

[\[c111\]](https://dblp.org/pid/151/8848.html#c111)

[887](https://dblp.org/pid/151/8848.html?view=joint&param=887 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shan You](https://dblp.org/pid/179/2548.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[888](https://dblp.org/pid/151/8848.html?view=joint&param=888 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fisher Yu 0001](https://dblp.org/pid/117/6314.html)

[\[c117\]](https://dblp.org/pid/151/8848.html#c117) [\[c115\]](https://dblp.org/pid/151/8848.html#c115) [\[c112\]](https://dblp.org/pid/151/8848.html#c112) [\[c111\]](https://dblp.org/pid/151/8848.html#c111) [\[c110\]](https://dblp.org/pid/151/8848.html#c110) [\[c109\]](https://dblp.org/pid/151/8848.html#c109) [\[i94\]](https://dblp.org/pid/151/8848.html#i94) [\[c106\]](https://dblp.org/pid/151/8848.html#c106) [\[c104\]](https://dblp.org/pid/151/8848.html#c104) [\[c103\]](https://dblp.org/pid/151/8848.html#c103) [\[c102\]](https://dblp.org/pid/151/8848.html#c102) [\[c101\]](https://dblp.org/pid/151/8848.html#c101) [\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c98\]](https://dblp.org/pid/151/8848.html#c98) [\[c97\]](https://dblp.org/pid/151/8848.html#c97) [\[c96\]](https://dblp.org/pid/151/8848.html#c96) [\[i89\]](https://dblp.org/pid/151/8848.html#i89) [\[i88\]](https://dblp.org/pid/151/8848.html#i88) [\[i86\]](https://dblp.org/pid/151/8848.html#i86) [\[i85\]](https://dblp.org/pid/151/8848.html#i85) [\[i83\]](https://dblp.org/pid/151/8848.html#i83) [\[i82\]](https://dblp.org/pid/151/8848.html#i82) [\[i81\]](https://dblp.org/pid/151/8848.html#i81) [\[i80\]](https://dblp.org/pid/151/8848.html#i80) [\[i78\]](https://dblp.org/pid/151/8848.html#i78) [\[c88\]](https://dblp.org/pid/151/8848.html#c88) [\[c87\]](https://dblp.org/pid/151/8848.html#c87) [\[c86\]](https://dblp.org/pid/151/8848.html#c86) [\[c84\]](https://dblp.org/pid/151/8848.html#c84) [\[c82\]](https://dblp.org/pid/151/8848.html#c82) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c79\]](https://dblp.org/pid/151/8848.html#c79) [\[c76\]](https://dblp.org/pid/151/8848.html#c76) [\[c74\]](https://dblp.org/pid/151/8848.html#c74) [\[c73\]](https://dblp.org/pid/151/8848.html#c73) [\[i75\]](https://dblp.org/pid/151/8848.html#i75) [\[i72\]](https://dblp.org/pid/151/8848.html#i72) [\[i69\]](https://dblp.org/pid/151/8848.html#i69) [\[i67\]](https://dblp.org/pid/151/8848.html#i67) [\[i66\]](https://dblp.org/pid/151/8848.html#i66) [\[i63\]](https://dblp.org/pid/151/8848.html#i63) [\[c64\]](https://dblp.org/pid/151/8848.html#c64) [\[c61\]](https://dblp.org/pid/151/8848.html#c61) [\[c55\]](https://dblp.org/pid/151/8848.html#c55) [\[i54\]](https://dblp.org/pid/151/8848.html#i54) [\[i51\]](https://dblp.org/pid/151/8848.html#i51) [\[i49\]](https://dblp.org/pid/151/8848.html#i49) [\[i48\]](https://dblp.org/pid/151/8848.html#i48) [\[i44\]](https://dblp.org/pid/151/8848.html#i44) [\[i43\]](https://dblp.org/pid/151/8848.html#i43)

[889](https://dblp.org/pid/151/8848.html?view=joint&param=889 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hongyuan Yu](https://dblp.org/pid/232/2265.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[890](https://dblp.org/pid/151/8848.html?view=joint&param=890 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jia Yu 0018](https://dblp.org/pid/86/3457-18.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[891](https://dblp.org/pid/151/8848.html?view=joint&param=891 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiaqian Yu](https://dblp.org/pid/164/7325.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[892](https://dblp.org/pid/151/8848.html?view=joint&param=892 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kaicheng Yu](https://dblp.org/pid/198/0861.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[893](https://dblp.org/pid/151/8848.html?view=joint&param=893 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lei Yu](https://dblp.org/pid/01/2775.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[894](https://dblp.org/pid/151/8848.html?view=joint&param=894 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qianjin Yu](https://dblp.org/pid/53/10179.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[895](https://dblp.org/pid/151/8848.html?view=joint&param=895 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qifeng Yu](https://dblp.org/pid/38/251.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[896](https://dblp.org/pid/151/8848.html?view=joint&param=896 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Weichen Yu](https://dblp.org/pid/325/1209.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[897](https://dblp.org/pid/151/8848.html?view=joint&param=897 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xianguo Yu](https://dblp.org/pid/187/9163.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[898](https://dblp.org/pid/151/8848.html?view=joint&param=898 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yongsheng Yuan](https://dblp.org/pid/364/8163.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[899](https://dblp.org/pid/151/8848.html?view=joint&param=899 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zehuan Yuan](https://dblp.org/pid/227/3298.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[900](https://dblp.org/pid/151/8848.html?view=joint&param=900 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zejian Yuan](https://dblp.org/pid/26/455.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[901](https://dblp.org/pid/151/8848.html?view=joint&param=901 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pong C. Yuen](https://dblp.org/pid/y/PongChiYuen.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[902](https://dblp.org/pid/151/8848.html?view=joint&param=902 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Sangdoo Yun](https://dblp.org/pid/124/3009.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[903](https://dblp.org/pid/151/8848.html?view=joint&param=903 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jan-Nico Zaech](https://dblp.org/pid/217/2208.html)

[\[c114\]](https://dblp.org/pid/151/8848.html#c114) [\[i79\]](https://dblp.org/pid/151/8848.html#i79) [\[j4\]](https://dblp.org/pid/151/8848.html#j4) [\[c85\]](https://dblp.org/pid/151/8848.html#c85) [\[i73\]](https://dblp.org/pid/151/8848.html#i73) [\[i53\]](https://dblp.org/pid/151/8848.html#i53)

[904](https://dblp.org/pid/151/8848.html?view=joint&param=904 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Titus Zaharia](https://dblp.org/pid/45/100.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[905](https://dblp.org/pid/151/8848.html?view=joint&param=905 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Syed Waqas Zamir](https://dblp.org/pid/140/7811.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[906](https://dblp.org/pid/151/8848.html?view=joint&param=906 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kang Ze](https://dblp.org/pid/340/1107.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[907](https://dblp.org/pid/151/8848.html?view=joint&param=907 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenjun Zeng 0001](https://dblp.org/pid/57/145.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[908](https://dblp.org/pid/151/8848.html?view=joint&param=908 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lin Zha](https://dblp.org/pid/133/3991.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[909](https://dblp.org/pid/151/8848.html?view=joint&param=909 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiang Zhai](https://dblp.org/pid/291/9340.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[910](https://dblp.org/pid/151/8848.html?view=joint&param=910 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Baopeng Zhang](https://dblp.org/pid/22/3524.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[911](https://dblp.org/pid/151/8848.html?view=joint&param=911 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chengquan Zhang](https://dblp.org/pid/163/1795.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[912](https://dblp.org/pid/151/8848.html?view=joint&param=912 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[913](https://dblp.org/pid/151/8848.html?view=joint&param=913 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chunhu Zhang](https://dblp.org/pid/292/0953.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[914](https://dblp.org/pid/151/8848.html?view=joint&param=914 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[915](https://dblp.org/pid/151/8848.html?view=joint&param=915 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Cong Zhang](https://dblp.org/pid/18/2908.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[916](https://dblp.org/pid/151/8848.html?view=joint&param=916 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[David Zhang 0001](https://dblp.org/pid/z/DavidZhang.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[917](https://dblp.org/pid/151/8848.html?view=joint&param=917 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fangyi Zhang](https://dblp.org/pid/10/8496.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[918](https://dblp.org/pid/151/8848.html?view=joint&param=918 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haitao Zhang](https://dblp.org/pid/19/6669.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[919](https://dblp.org/pid/151/8848.html?view=joint&param=919 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Honggang Zhang 0002](https://dblp.org/pid/82/1228-2.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[920](https://dblp.org/pid/151/8848.html?view=joint&param=920 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hongliang Zhang](https://dblp.org/pid/77/10205.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[921](https://dblp.org/pid/151/8848.html?view=joint&param=921 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiangtao Zhang](https://dblp.org/pid/38/8912.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[922](https://dblp.org/pid/151/8848.html?view=joint&param=922 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jianlin Zhang 0001](https://dblp.org/pid/37/1545-1.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[923](https://dblp.org/pid/151/8848.html?view=joint&param=923 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jianxing Zhang](https://dblp.org/pid/62/7794.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[924](https://dblp.org/pid/151/8848.html?view=joint&param=924 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jinyue Zhang](https://dblp.org/pid/10/2874.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[925](https://dblp.org/pid/151/8848.html?view=joint&param=925 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kai Zhang 0008](https://dblp.org/pid/55/957-8.html)

[\[c109\]](https://dblp.org/pid/151/8848.html#c109) [\[c69\]](https://dblp.org/pid/151/8848.html#c69) [\[c63\]](https://dblp.org/pid/151/8848.html#c63) [\[i50\]](https://dblp.org/pid/151/8848.html#i50) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i31\]](https://dblp.org/pid/151/8848.html#i31) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[926](https://dblp.org/pid/151/8848.html?view=joint&param=926 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[927](https://dblp.org/pid/151/8848.html?view=joint&param=927 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kangkai Zhang](https://dblp.org/pid/260/2990.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[928](https://dblp.org/pid/151/8848.html?view=joint&param=928 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lei Zhang 0006](https://dblp.org/pid/64/5666-6.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[929](https://dblp.org/pid/151/8848.html?view=joint&param=929 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Li Zhang 0040](https://dblp.org/pid/89/5992-40.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[930](https://dblp.org/pid/151/8848.html?view=joint&param=930 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lichao Zhang 0001](https://dblp.org/pid/126/8027-1.html)

[\[j2\]](https://dblp.org/pid/151/8848.html#j2) [\[c34\]](https://dblp.org/pid/151/8848.html#c34) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c31\]](https://dblp.org/pid/151/8848.html#c31) [\[i19\]](https://dblp.org/pid/151/8848.html#i19) [\[i18\]](https://dblp.org/pid/151/8848.html#i18) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[i11\]](https://dblp.org/pid/151/8848.html#i11)

[931](https://dblp.org/pid/151/8848.html?view=joint&param=931 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lu Zhang 0053](https://dblp.org/pid/82/10609-53.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[932](https://dblp.org/pid/151/8848.html?view=joint&param=932 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Mengdan Zhang](https://dblp.org/pid/172/9514.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[933](https://dblp.org/pid/151/8848.html?view=joint&param=933 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pengfei Zhang 0005](https://dblp.org/pid/58/4525-5.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[934](https://dblp.org/pid/151/8848.html?view=joint&param=934 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pengyu Zhang](https://dblp.org/pid/33/4816.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[935](https://dblp.org/pid/151/8848.html?view=joint&param=935 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qi Zhang](https://dblp.org/pid/52/323.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[936](https://dblp.org/pid/151/8848.html?view=joint&param=936 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ruohan Zhang](https://dblp.org/pid/160/9929.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[937](https://dblp.org/pid/151/8848.html?view=joint&param=937 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shengping Zhang](https://dblp.org/pid/60/1866.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[938](https://dblp.org/pid/151/8848.html?view=joint&param=938 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shuohao Zhang](https://dblp.org/pid/11/2195.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[939](https://dblp.org/pid/151/8848.html?view=joint&param=939 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tianzhu Zhang 0001](https://dblp.org/pid/15/7643-1.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13)

[940](https://dblp.org/pid/151/8848.html?view=joint&param=940 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ting Zhang 0006](https://dblp.org/pid/06/5919-6.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[941](https://dblp.org/pid/151/8848.html?view=joint&param=941 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wenkang Zhang](https://dblp.org/pid/340/0966.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[942](https://dblp.org/pid/151/8848.html?view=joint&param=942 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiangyu Zhang 0005](https://dblp.org/pid/95/3760-5.html)

[\[c50\]](https://dblp.org/pid/151/8848.html#c50) [\[i36\]](https://dblp.org/pid/151/8848.html#i36)

[943](https://dblp.org/pid/151/8848.html?view=joint&param=943 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaofan Zhang 0002](https://dblp.org/pid/28/9804-2.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[944](https://dblp.org/pid/151/8848.html?view=joint&param=944 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaohan Zhang](https://dblp.org/pid/96/6053.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[945](https://dblp.org/pid/151/8848.html?view=joint&param=945 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xiaolin Zhang](https://dblp.org/pid/99/2516.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[946](https://dblp.org/pid/151/8848.html?view=joint&param=946 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xinyu Zhang 0020](https://dblp.org/pid/58/4582-20.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[947](https://dblp.org/pid/151/8848.html?view=joint&param=947 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yachao Zhang 0001](https://dblp.org/pid/40/10584-1.html)

[\[c111\]](https://dblp.org/pid/151/8848.html#c111) [\[i82\]](https://dblp.org/pid/151/8848.html#i82)

[948](https://dblp.org/pid/151/8848.html?view=joint&param=948 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yi Zhang](https://dblp.org/pid/64/6544.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[949](https://dblp.org/pid/151/8848.html?view=joint&param=949 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yulun Zhang 0001](https://dblp.org/pid/166/2763-1.html)

[\[c111\]](https://dblp.org/pid/151/8848.html#c111) [\[c110\]](https://dblp.org/pid/151/8848.html#c110) [\[c109\]](https://dblp.org/pid/151/8848.html#c109) [\[c96\]](https://dblp.org/pid/151/8848.html#c96) [\[i82\]](https://dblp.org/pid/151/8848.html#i82)

[950](https://dblp.org/pid/151/8848.html?view=joint&param=950 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yunhua Zhang](https://dblp.org/pid/60/9627.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[951](https://dblp.org/pid/151/8848.html?view=joint&param=951 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yushan Zhang](https://dblp.org/pid/50/10702.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c43\]](https://dblp.org/pid/151/8848.html#c43)

[952](https://dblp.org/pid/151/8848.html?view=joint&param=952 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhaoliang Zhang](https://dblp.org/pid/81/7883.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[953](https://dblp.org/pid/151/8848.html?view=joint&param=953 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zheng Zhang 0022](https://dblp.org/pid/181/2621-22.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[954](https://dblp.org/pid/151/8848.html?view=joint&param=954 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[955](https://dblp.org/pid/151/8848.html?view=joint&param=955 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhilu Zhang 0001](https://dblp.org/pid/220/3795-1.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[956](https://dblp.org/pid/151/8848.html?view=joint&param=956 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhipeng Zhang](https://dblp.org/pid/49/4941.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[957](https://dblp.org/pid/151/8848.html?view=joint&param=957 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[958](https://dblp.org/pid/151/8848.html?view=joint&param=958 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bin Zhao](https://dblp.org/pid/73/4325.html)

[\[c59\]](https://dblp.org/pid/151/8848.html#c59) [\[i59\]](https://dblp.org/pid/151/8848.html#i59)

[959](https://dblp.org/pid/151/8848.html?view=joint&param=959 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fei Zhao](https://dblp.org/pid/21/6180.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[960](https://dblp.org/pid/151/8848.html?view=joint&param=960 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Fei Zhao 0008](https://dblp.org/pid/21/6180-8.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[961](https://dblp.org/pid/151/8848.html?view=joint&param=961 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Guodongfang Zhao](https://dblp.org/pid/364/8196.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[962](https://dblp.org/pid/151/8848.html?view=joint&param=962 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haojie Zhao](https://dblp.org/pid/216/7590.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[963](https://dblp.org/pid/151/8848.html?view=joint&param=963 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hengyuan Zhao](https://dblp.org/pid/260/3042.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[964](https://dblp.org/pid/151/8848.html?view=joint&param=964 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jie Zhao 0014](https://dblp.org/pid/23/3168-14.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[965](https://dblp.org/pid/151/8848.html?view=joint&param=965 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shanshan Zhao 0003](https://dblp.org/pid/02/7781-3.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[966](https://dblp.org/pid/151/8848.html?view=joint&param=966 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

aka: Shaochuan Zhao

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[967](https://dblp.org/pid/151/8848.html?view=joint&param=967 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Shengwei Zhao](https://dblp.org/pid/155/9654.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[968](https://dblp.org/pid/151/8848.html?view=joint&param=968 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tongtong Zhao](https://dblp.org/pid/191/5253.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i34\]](https://dblp.org/pid/151/8848.html#i34) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[969](https://dblp.org/pid/151/8848.html?view=joint&param=969 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuzhi Zhao](https://dblp.org/pid/240/3833.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[970](https://dblp.org/pid/151/8848.html?view=joint&param=970 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zhihao Zhao](https://dblp.org/pid/144/0233.html)

[\[c90\]](https://dblp.org/pid/151/8848.html#c90)

[971](https://dblp.org/pid/151/8848.html?view=joint&param=971 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zixiang Zhao](https://dblp.org/pid/65/5420.html)

[\[c110\]](https://dblp.org/pid/151/8848.html#c110)

[972](https://dblp.org/pid/151/8848.html?view=joint&param=972 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ming Zhen](https://dblp.org/pid/307/8430.html)

[\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[973](https://dblp.org/pid/151/8848.html?view=joint&param=973 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Feng Zheng 0001](https://dblp.org/pid/39/800-1.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[974](https://dblp.org/pid/151/8848.html?view=joint&param=974 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haixia Zheng](https://dblp.org/pid/119/1585.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[975](https://dblp.org/pid/151/8848.html?view=joint&param=975 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Linyu Zheng](https://dblp.org/pid/210/2313.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[976](https://dblp.org/pid/151/8848.html?view=joint&param=976 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Min Zheng](https://dblp.org/pid/23/328.html)

[\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[977](https://dblp.org/pid/151/8848.html?view=joint&param=977 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Pengkun Zheng](https://dblp.org/pid/260/2752.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[978](https://dblp.org/pid/151/8848.html?view=joint&param=978 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qian Zheng](https://dblp.org/pid/28/8138.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[979](https://dblp.org/pid/151/8848.html?view=joint&param=979 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yaozong Zheng](https://dblp.org/pid/344/6907.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[980](https://dblp.org/pid/151/8848.html?view=joint&param=980 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Hui Zhi](https://dblp.org/pid/46/1382.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[981](https://dblp.org/pid/151/8848.html?view=joint&param=981 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[982](https://dblp.org/pid/151/8848.html?view=joint&param=982 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Gaofeng Zhou](https://dblp.org/pid/258/5676.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89)

[983](https://dblp.org/pid/151/8848.html?view=joint&param=983 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Lijun Zhou](https://dblp.org/pid/14/1719.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[984](https://dblp.org/pid/151/8848.html?view=joint&param=984 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Qin Zhou 0002](https://dblp.org/pid/80/7814-2.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23)

[985](https://dblp.org/pid/151/8848.html?view=joint&param=985 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ruofan Zhou](https://dblp.org/pid/205/3902.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[986](https://dblp.org/pid/151/8848.html?view=joint&param=986 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Tianfei Zhou](https://dblp.org/pid/150/6710.html)

[\[c42\]](https://dblp.org/pid/151/8848.html#c42) [\[i30\]](https://dblp.org/pid/151/8848.html#i30)

[987](https://dblp.org/pid/151/8848.html?view=joint&param=987 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wengang Zhou 0001](https://dblp.org/pid/22/4544-1.html)

[\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[988](https://dblp.org/pid/151/8848.html?view=joint&param=988 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yu Zhou 0016](https://dblp.org/pid/36/2728-16.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[989](https://dblp.org/pid/151/8848.html?view=joint&param=989 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yuanbo Zhou](https://dblp.org/pid/262/5471.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[990](https://dblp.org/pid/151/8848.html?view=joint&param=990 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Chen Zhu](https://dblp.org/pid/59/10522.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[991](https://dblp.org/pid/151/8848.html?view=joint&param=991 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Dan Zhu](https://dblp.org/pid/50/6054.html)

[\[c28\]](https://dblp.org/pid/151/8848.html#c28)

[992](https://dblp.org/pid/151/8848.html?view=joint&param=992 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Gao Zhu](https://dblp.org/pid/139/3887.html)

[\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12)

[993](https://dblp.org/pid/151/8848.html?view=joint&param=993 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jianke Zhu](https://dblp.org/pid/10/4016.html)

[\[c17\]](https://dblp.org/pid/151/8848.html#c17) [\[c13\]](https://dblp.org/pid/151/8848.html#c13) [\[c12\]](https://dblp.org/pid/151/8848.html#c12) [\[c2\]](https://dblp.org/pid/151/8848.html#c2)

[994](https://dblp.org/pid/151/8848.html?view=joint&param=994 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58)

[995](https://dblp.org/pid/151/8848.html?view=joint&param=995 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80) [\[c58\]](https://dblp.org/pid/151/8848.html#c58) [\[c43\]](https://dblp.org/pid/151/8848.html#c43) [\[c32\]](https://dblp.org/pid/151/8848.html#c32)

[996](https://dblp.org/pid/151/8848.html?view=joint&param=996 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yu Zhu 0004](https://dblp.org/pid/38/5267-4.html)

[\[c46\]](https://dblp.org/pid/151/8848.html#c46) [\[i28\]](https://dblp.org/pid/151/8848.html#i28)

[997](https://dblp.org/pid/151/8848.html?view=joint&param=997 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Zheng Zhu](https://dblp.org/pid/29/4319.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[998](https://dblp.org/pid/151/8848.html?view=joint&param=998 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Junfei Zhuang](https://dblp.org/pid/213/4212.html)

[\[c32\]](https://dblp.org/pid/151/8848.html#c32) [\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[999](https://dblp.org/pid/151/8848.html?view=joint&param=999 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Yueting Zhuang](https://dblp.org/pid/218/7793.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100) [\[c80\]](https://dblp.org/pid/151/8848.html#c80)

[1000](https://dblp.org/pid/151/8848.html?view=joint&param=1000 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Haijie Zhuo](https://dblp.org/pid/209/2325.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[1001](https://dblp.org/pid/151/8848.html?view=joint&param=1001 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Magauiya Zhussip](https://dblp.org/pid/222/2064.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i52\]](https://dblp.org/pid/151/8848.html#i52)

[1002](https://dblp.org/pid/151/8848.html?view=joint&param=1002 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[ChengAo Zong](https://dblp.org/pid/364/8208.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[1003](https://dblp.org/pid/151/8848.html?view=joint&param=1003 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Ziyao Zong](https://dblp.org/pid/264/5589.html)

[\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[1004](https://dblp.org/pid/151/8848.html?view=joint&param=1004 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wei Zou](https://dblp.org/pid/10/328.html)

[\[c23\]](https://dblp.org/pid/151/8848.html#c23) [\[c17\]](https://dblp.org/pid/151/8848.html#c17)

[1005](https://dblp.org/pid/151/8848.html?view=joint&param=1005 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Xueyi Zou](https://dblp.org/pid/150/8081.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[i52\]](https://dblp.org/pid/151/8848.html#i52) [\[c51\]](https://dblp.org/pid/151/8848.html#c51) [\[i34\]](https://dblp.org/pid/151/8848.html#i34)

[1006](https://dblp.org/pid/151/8848.html?view=joint&param=1006 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Kunlong Zuo](https://dblp.org/pid/354/8493.html)

[\[c100\]](https://dblp.org/pid/151/8848.html#c100)

[1007](https://dblp.org/pid/151/8848.html?view=joint&param=1007 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/151/8848.html?view=group&param=1)

[Wangmeng Zuo](https://dblp.org/pid/93/2671.html)

[\[c89\]](https://dblp.org/pid/151/8848.html#c89) [\[c23\]](https://dblp.org/pid/151/8848.html#c23)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/151/8848.html#) [\[–\]](https://dblp.org/pid/151/8848.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/151/8848.html#) [\[–\]](https://dblp.org/pid/151/8848.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/151/8848.html#) [\[–\]](https://dblp.org/pid/151/8848.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/151/8848.html#) [\[–\]](https://dblp.org/pid/151/8848.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/151/8848.html#) [\[–\]](https://dblp.org/pid/151/8848.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)