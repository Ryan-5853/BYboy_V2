> 抓取来源：https://dblp.org/pid/225/3263.html

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

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Hasan+Saribas%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F225%2F3263%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Hasan+Saribas+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F225%2F3263%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Hasan+Saribas+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F225%2F3263%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Hasan+Saribas%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F225%2F3263%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Hasan+Saribas+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F225%2F3263%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Hasan+Saribas%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F225%2F3263%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Hasan+Saribas%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F225%2F3263%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F225%2F3263%3E+%7D+.%0A%0A%7D)

_showing all24 records_

2016202652018: 22019: 52020: 22020: 22021: 12022: 32022: 32022: 32023: 82023: 82023: 82024: 22025: 1

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

- ![](https://dblp.org/img/add-mark.12x12.png)Hakan Çevikalp (20)
- ![](https://dblp.org/img/add-mark.12x12.png)Bedirhan Uzun (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Chi-Yi Tsai (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Burak Benligiray (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Goutam Bhat (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Joni-Kristian Kämäräinen (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Roman P. Pflugfelder (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Luc Van Gool (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Okan Köpüklü (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Christian Micheloni (3)

- _310 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (22)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0001-8709-9872 (2)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (6)
- ![](https://dblp.org/img/add-mark.12x12.png)SIU (5)
- ![](https://dblp.org/img/add-mark.12x12.png)ICCV (3)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Neurocomputing (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Mach. Vis. Appl. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Pattern Anal. Mach. Intell. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)SCIA (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Pattern Recognit. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ACML (1)

- _3 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (15)
- ![](https://dblp.org/img/add-mark.12x12.png)open (9)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[j5\]
[Hakan Cevikalp](https://dblp.org/pid/14/6210.html)![](https://dblp.org/img/orcid-mark.12x12.png), Hasan Saribas![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html):

Reaching Nirvana: Maximizing the Margin in Both Euclidean and Angular Spaces for Deep Neural Network Classification. [IEEE Trans. Neural Networks Learn. Syst.36(5)](https://dblp.org/db/journals/tnn/tnn36.html#journals/tnn/CevikalpSU25): 8178-8191 (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[i6\]
[Furkan Durmus](https://dblp.org/pid/334/1382.html), Hasan Saribas, [Said Aldemir](https://dblp.org/pid/379/6036.html), [Junyan Yang](https://dblp.org/pid/52/6890.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html):

Pairwise Ranking Loss for Multi-Task Learning in Recommender Systems. [CoRRabs/2406.02163](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-02163) (2024)
- ![](https://dblp.org/img/n.png)

\[i5\]
[Beyza Türkmen](https://dblp.org/pid/362/2171.html), [Ramazan Tarik Türksoy](https://dblp.org/pid/362/2299.html), Hasan Saribas, [Hakan Cevikalp](https://dblp.org/pid/14/6210.html):

Polyhedral Conic Classifier for CTR Prediction. [CoRRabs/2406.03892](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-03892) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[j4\]
Hasan Saribas, [Hakan Cevikalp](https://dblp.org/pid/14/6210.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Sinem Kahvecioglu](https://dblp.org/pid/225/3132.html):

Visual object tracking by using ranking loss and spatial-temporal features. [Mach. Vis. Appl.34(2)](https://dblp.org/db/journals/mva/mva34.html#journals/mva/SaribasCK23): 30 (2023)
- ![](https://dblp.org/img/n.png)

\[j3\]
[Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html)![](https://dblp.org/img/orcid-mark.12x12.png), Hasan Saribas:

Deep Discriminative Feature Models (DDFMs) for Set Based Face Recognition and Distance Metric Learning. [IEEE Trans. Pattern Anal. Mach. Intell.45(5)](https://dblp.org/db/journals/pami/pami45.html#journals/pami/UzunCS23): 5594-5608 (2023)
- ![](https://dblp.org/img/n.png)

\[j2\]
[Hakan Cevikalp](https://dblp.org/pid/14/6210.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Yusuf Salk](https://dblp.org/pid/328/4380.html)![](https://dblp.org/img/orcid-mark.12x12.png), Hasan Saribas, [Okan Köpüklü](https://dblp.org/pid/218/6295.html):

From anomaly detection to open set recognition: Bridging the gap. [Pattern Recognit.138](https://dblp.org/db/journals/pr/pr138.html#journals/pr/CevikalpUSSK23): 109385 (2023)
- ![](https://dblp.org/img/n.png)

\[c13\]
[Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Hasan Serhan Yavuz](https://dblp.org/pid/18/5588.html), Hasan Saribas:

Deep Uniformly Distributed Centers on a Hypersphere for Open Set Recognition. [ACML2023](https://dblp.org/db/conf/acml/acml2023.html#conf/acml/CevikalpYS23): 217-230
- ![](https://dblp.org/img/n.png)

\[c12\]
[Hakan Cevikalp](https://dblp.org/pid/14/6210.html)![](https://dblp.org/img/orcid-mark.12x12.png), Hasan Saribas![](https://dblp.org/img/orcid-mark.12x12.png):

Deep Simplex Classifier for Maximizing the Margin in Both Euclidean and Angular Spaces. [SCIA (2)2023](https://dblp.org/db/conf/scia/scia2023-2.html#conf/scia/CevikalpS23): 91-107
- ![](https://dblp.org/img/n.png)

\[c11\]
[Ergun Biçici](https://dblp.org/pid/15/4891.html)![](https://dblp.org/img/orcid-mark.12x12.png), Hasan Saribas:

Calibrating Neural Networks for CTR Prediction. [SIU2023](https://dblp.org/db/conf/siu/siu2023.html#conf/siu/BiciciS23): 1-4
- ![](https://dblp.org/img/n.png)

\[i4\]
Hasan Saribas, [Cagri Yesil](https://dblp.org/pid/09/10719.html), [Serdarcan Dilbaz](https://dblp.org/pid/355/4549.html), [Halit Orenbas](https://dblp.org/pid/225/2951.html):

MMBAttn: Max-Mean and Bit-wise Attention for CTR Prediction. [CoRRabs/2308.13187](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-13187) (2023)
- ![](https://dblp.org/img/n.png)

\[i3\]
[Serdarcan Dilbaz](https://dblp.org/pid/355/4549.html), Hasan Saribas:

STEC: See-Through Transformer-based Encoder for CTR Prediction. [CoRRabs/2308.15033](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-15033) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j1\]
Hasan Saribas, [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Okan Köpüklü](https://dblp.org/pid/218/6295.html), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html):

TRAT: Tracking by attention using spatio-temporal features. [Neurocomputing492](https://dblp.org/db/journals/ijon/ijon492.html#journals/ijon/SaribasCKU22): 150-161 (2022)
- ![](https://dblp.org/img/n.png)

\[c10\]
[Yusuf Salk](https://dblp.org/pid/328/4380.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Hakan Çevikalp](https://dblp.org/pid/14/6210.html), Hasan Saribas:

Anomaly Detection with Deep Compact Hypersphere. [SIU2022](https://dblp.org/db/conf/siu/siu2022.html#conf/siu/SalkUCS22): 1-4
- ![](https://dblp.org/img/n.png)

\[i2\]
[Hakan Cevikalp](https://dblp.org/pid/14/6210.html), Hasan Saribas:

Deep Simplex Classifier for Maximizing the Margin in Both Euclidean and Angular Spaces. [CoRRabs/2212.11747](https://dblp.org/db/journals/corr/corr2212.html#journals/corr/abs-2212-11747) (2022)
- 2021
- ![](https://dblp.org/img/n.png)

\[c9\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Yu-Chen Chiu](https://dblp.org/pid/199/2494.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Xingping Dong](https://dblp.org/pid/156/3020.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Bilge Günsel](https://dblp.org/pid/47/5125.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Wencheng Han](https://dblp.org/pid/280/3348.html), [Yanyan Huang](https://dblp.org/pid/88/4316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [J. Yin](https://dblp.org/pid/51/2242.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Jingen Liu](https://dblp.org/pid/10/5849.html), [Li Liu](https://dblp.org/pid/33/4528-36.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Jonathon Luiten](https://dblp.org/pid/211/7992.html), [Jie Ma](https://dblp.org/pid/62/5110.html), [Ziang Ma](https://dblp.org/pid/165/9621.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Yuzhen Niu](https://dblp.org/pid/28/7442.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Aravindh Rajiv](https://dblp.org/pid/307/9144.html), [Muhammad Rana](https://dblp.org/pid/276/0222.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), Hasan Saribas, [Ling Shao](https://dblp.org/pid/75/1281.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furao Shen](https://dblp.org/pid/80/4685.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Paul Voigtlaender](https://dblp.org/pid/166/6430.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html), [Chenyan Wu](https://dblp.org/pid/76/1190.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang Xu](https://dblp.org/pid/126/2962.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Xiaohan Zhang](https://dblp.org/pid/96/6053.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Ming Zhen](https://dblp.org/pid/307/8430.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html):

The Ninth Visual Object Tracking VOT2021 Challenge Results. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/KristanMLFPKCDZ21): 2711-2738
- 2020
- ![](https://dblp.org/img/n.png)

\[c8\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Linbo He](https://dblp.org/pid/26/741.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Alexander G. Hauptmann](https://dblp.org/pid/h/AlexanderGHauptmann.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Álvaro García-Martín](https://dblp.org/pid/39/1542.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Anton Varfolomieiev](https://dblp.org/pid/188/7504.html), [Awet Haileslassie Gebrehiwot](https://dblp.org/pid/284/2554.html), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Bing Li](https://dblp.org/pid/13/2692-1.html), [Chen Qian](https://dblp.org/pid/70/3604-6.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Fredrik Gustafsson](https://dblp.org/pid/394/4497.html), [Gian Luca Foresti](https://dblp.org/pid/93/5522.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Haojie Zhao](https://dblp.org/pid/216/7590.html), [Haoran Bai](https://dblp.org/pid/235/9510.html), [Hari Chandana Kuchibhotla](https://dblp.org/pid/284/2570.html), Hasan Saribas, [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Hossein Ghanei-Yakhdan](https://dblp.org/pid/188/5964.html), [Houqiang Li](https://dblp.org/pid/59/7017.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Javad Khaghani](https://dblp.org/pid/233/0334.html), [Jesús Bescós](https://dblp.org/pid/97/2333.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Jianlong Fu](https://dblp.org/pid/83/8692.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Jingtao Xu](https://dblp.org/pid/119/1746.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Junhyun Lee](https://dblp.org/pid/155/8661.html), [Kaicheng Yu](https://dblp.org/pid/198/0861.html), [Kaiwen Liu](https://dblp.org/pid/231/4262.html), [Kang Yang](https://dblp.org/pid/86/8501.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Li Cheng](https://dblp.org/pid/13/4938-1.html), [Li Zhang](https://dblp.org/pid/89/5992-40.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Luca Bertinetto](https://dblp.org/pid/154/1351.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Ning Wang](https://dblp.org/pid/46/2005-20.html), [Pengyu Zhang](https://dblp.org/pid/33/4816.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Qiang Wang](https://dblp.org/pid/64/5630-51.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rama Krishna Sai Subrahmanyam Gorthi](https://dblp.org/pid/45/7595.html), [Seokeon Choi](https://dblp.org/pid/214/2200.html), [Seyed Mojtaba Marvasti-Zadeh](https://dblp.org/pid/188/6262.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Shohreh Kasaei](https://dblp.org/pid/78/5062.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Shuhao Chen](https://dblp.org/pid/43/2127.html), [Thomas B. Schön](https://dblp.org/pid/85/4891.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Weiming Hu](https://dblp.org/pid/41/6824-4.html), [Wengang Zhou](https://dblp.org/pid/22/4544-1.html), [Xi Qiu](https://dblp.org/pid/115/5698.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Xiao-Jun Wu](https://dblp.org/pid/13/5168-1.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Yingming Wang](https://dblp.org/pid/59/605.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuncon Yao](https://dblp.org/pid/284/2556.html), [Yunsung Lee](https://dblp.org/pid/227/9311.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Zezhou Wang](https://dblp.org/pid/204/1179.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhijun Mai](https://dblp.org/pid/247/9401.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Zhirong Wu](https://dblp.org/pid/147/5025.html), [Ziang Ma](https://dblp.org/pid/165/9621.html):

The Eighth Visual Object Tracking VOT2020 Challenge Results. [ECCV Workshops (5)2020](https://dblp.org/db/conf/eccv/eccv2020-w5.html#conf/eccv/KristanLMFPKDZL20): 547-601
- ![](https://dblp.org/img/n.png)

\[i1\]
Hasan Saribas, [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Okan Köpüklü](https://dblp.org/pid/218/6295.html), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html):

TRAT: Tracking by Attention Using Spatio-Temporal Features. [CoRRabs/2011.09524](https://dblp.org/db/journals/corr/corr2011.html#journals/corr/abs-2011-09524) (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[c7\]
[Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Burak Benligiray](https://dblp.org/pid/119/9508.html), [Ömer Nezih Gerek](https://dblp.org/pid/48/4641.html), Hasan Saribas:

Semi-Supervised Robust Deep Neural Networks for Multi-Label Classification. [CVPR Workshops2019](https://dblp.org/db/conf/cvpr/cvprw2019.html#conf/cvpr/CevikalpBGS19): 9-17
- ![](https://dblp.org/img/n.png)

\[c6\]
Hasan Saribas, [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Burak Benligiray](https://dblp.org/pid/119/9508.html), [Onur Eker](https://dblp.org/pid/180/7146.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html):

A Hybrid Method for Tracking of Objects by UAVs. [CVPR Workshops2019](https://dblp.org/db/conf/cvpr/cvprw2019.html#conf/cvpr/SaribasUBEC19): 563-572
- ![](https://dblp.org/img/n.png)

\[c5\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Amanda Berg](https://dblp.org/pid/163/4511.html), [Linyu Zheng](https://dblp.org/pid/210/2313.html), [Litu Rout](https://dblp.org/pid/206/6445.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Luca Bertinetto](https://dblp.org/pid/154/1351.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Meng Ni](https://dblp.org/pid/174/2809.html), [Min Young Kim](https://dblp.org/pid/34/5733-3.html), [Ming Tang](https://dblp.org/pid/73/4373-1.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Abdelrahman Eldesokey](https://dblp.org/pid/154/9080.html), [Naveen Paluru](https://dblp.org/pid/260/3261.html), [Niki Martinel](https://dblp.org/pid/56/10105.html), [Pengfei Xu](https://dblp.org/pid/04/383-13.html), [Pengfei Zhang](https://dblp.org/pid/58/4525-5.html), [Pengkun Zheng](https://dblp.org/pid/260/2752.html), [Pengyu Zhang](https://dblp.org/pid/33/4816.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Qi Zhang](https://dblp.org/pid/52/323.html), [Qiang Wang](https://dblp.org/pid/64/5630-51.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Radu Timofte](https://dblp.org/pid/24/8616.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Rama Krishna Sai Subrahmanyam Gorthi](https://dblp.org/pid/45/7595.html), [Richard M. Everson](https://dblp.org/pid/07/6331.html), [Ruize Han](https://dblp.org/pid/205/4022.html), [Ruohan Zhang](https://dblp.org/pid/160/9929.html), [Shan You](https://dblp.org/pid/179/2548.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Shengwei Zhao](https://dblp.org/pid/155/9654.html), [Shihu Li](https://dblp.org/pid/242/1376.html), [Shikun Li](https://dblp.org/pid/255/0117.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Shuai Bai](https://dblp.org/pid/208/8033.html), [Shuosen Guan](https://dblp.org/pid/245/8954.html), [Tengfei Xing](https://dblp.org/pid/82/1822.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Tianyu Yang](https://dblp.org/pid/120/8076-3.html), [Ting Zhang](https://dblp.org/pid/06/5919-6.html), [Tomás Vojír](https://dblp.org/pid/142/5749.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Weiming Hu](https://dblp.org/pid/41/6824.html), [Weizhao Wang](https://dblp.org/pid/39/2359.html), [Abel Gonzalez-Garcia](https://dblp.org/pid/156/0213.html), [Wenjie Tang](https://dblp.org/pid/87/7879.html), [Wenjun Zeng](https://dblp.org/pid/57/145.html), [Wenyu Liu](https://dblp.org/pid/42/4110-1.html), [Xi Chen](https://dblp.org/pid/16/3283.html), [Xi Qiu](https://dblp.org/pid/115/5698.html), [Xiang Bai](https://dblp.org/pid/59/2741.html), [Xiao-Jun Wu](https://dblp.org/pid/13/5168-1.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Xier Chen](https://dblp.org/pid/260/3035.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xing Sun](https://dblp.org/pid/90/2719-1.html), [Xingyu Chen](https://dblp.org/pid/59/7651.html), [Xinmei Tian](https://dblp.org/pid/03/5204-1.html), [Xu Tang](https://dblp.org/pid/123/7064.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yan Huang](https://dblp.org/pid/75/6434-8.html), [Yanan Chen](https://dblp.org/pid/78/10104.html), [Yanchao Lian](https://dblp.org/pid/253/3698.html), [Yang Gu](https://dblp.org/pid/01/5858.html), [Yang Liu](https://dblp.org/pid/51/3710-3.html), [Andong Lu](https://dblp.org/pid/245/2878.html), [Yanjie Chen](https://dblp.org/pid/02/7548.html), [Yi Zhang](https://dblp.org/pid/64/6544.html), [Yinda Xu](https://dblp.org/pid/254/1072.html), [Yingming Wang](https://dblp.org/pid/59/605.html), [Yingping Li](https://dblp.org/pid/172/4240.html), [Yu Zhou](https://dblp.org/pid/36/2728-16.html), [Yuan Dong](https://dblp.org/pid/66/875.html), [Yufei Xu](https://dblp.org/pid/43/7400.html), [Yunhua Zhang](https://dblp.org/pid/60/9627.html), [Yunkun Li](https://dblp.org/pid/260/2938.html), [Anfeng He](https://dblp.org/pid/188/1205.html), [Zeyu Wang](https://dblp.org/pid/132/7882-8.html), [Zhao Luo](https://dblp.org/pid/187/1232.html), [Zhaoliang Zhang](https://dblp.org/pid/81/7883.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Zhichao Song](https://dblp.org/pid/169/4022.html), [Zhihao Chen](https://dblp.org/pid/50/505-4.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Zhirong Wu](https://dblp.org/pid/147/5025.html), [Zhiwei Xiong](https://dblp.org/pid/54/6827.html), [Zhongjian Huang](https://dblp.org/pid/251/0619.html), [Anton Varfolomieiev](https://dblp.org/pid/188/7504.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhu Teng](https://dblp.org/pid/132/2247.html), [Zihan Ni](https://dblp.org/pid/187/9123.html), [Antoni B. Chan](https://dblp.org/pid/55/5814.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Ardhendu Shekhar Tripathi](https://dblp.org/pid/141/9949.html), [Arnold W. M. Smeulders](https://dblp.org/pid/15/5400.html), [Bala Suraj Pedasingu](https://dblp.org/pid/260/3120.html), [Bao Xin Chen](https://dblp.org/pid/153/1895.html), [Baopeng Zhang](https://dblp.org/pid/22/3524.html), [Baoyuan Wu](https://dblp.org/pid/73/7781.html), [Bi Li](https://dblp.org/pid/174/9761.html), [Bin He](https://dblp.org/pid/78/4523.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Bing Bai](https://dblp.org/pid/54/5260.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Bing Li](https://dblp.org/pid/13/2692-1.html), [Bo Li](https://dblp.org/pid/50/3402-114.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Chao Ma](https://dblp.org/pid/79/1552-4.html), [Chen Fang](https://dblp.org/pid/60/2548.html), [Chen Qian](https://dblp.org/pid/70/3604-1.html), [Cheng Chen](https://dblp.org/pid/10/217.html), [Chenglong Li](https://dblp.org/pid/83/7820-2.html), [Chengquan Zhang](https://dblp.org/pid/163/1795.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html), [Michael Felsberg](https://dblp.org/pid/00/78.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chong Luo](https://dblp.org/pid/79/3712-1.html), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Dacheng Tao](https://dblp.org/pid/46/3391.html), [Deepak Gupta](https://dblp.org/pid/65/2751.html), [Dejia Song](https://dblp.org/pid/260/2975.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Efstratios Gavves](https://dblp.org/pid/03/8693.html), [Eunu Yi](https://dblp.org/pid/260/3303.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Fangyi Zhang](https://dblp.org/pid/10/8496.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Fei Zhao](https://dblp.org/pid/21/6180.html), [George De Ath](https://dblp.org/pid/220/3209.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Guoxuan Li](https://dblp.org/pid/121/6265.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Hao Du](https://dblp.org/pid/13/6441-6.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Haojie Zhao](https://dblp.org/pid/216/7590.html), Hasan Saribas, [Ho Min Jung](https://dblp.org/pid/36/5839.html), [Hongliang Bai](https://dblp.org/pid/34/5268.html), [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jiakun Li](https://dblp.org/pid/69/7673.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Jianlong Fu](https://dblp.org/pid/83/8692.html), [Jie Chen](https://dblp.org/pid/92/6289.html), [Jie Gao](https://dblp.org/pid/181/2794.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Jin Tang](https://dblp.org/pid/56/4951-1.html), [Jing Li](https://dblp.org/pid/l/JingLi36.html), [Jingjing Wu](https://dblp.org/pid/27/2384.html), [Jingtuo Liu](https://dblp.org/pid/164/5911.html), [Jinqiao Wang](https://dblp.org/pid/67/4236.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jinqing Qi](https://dblp.org/pid/09/287.html), [Jinyue Zhang](https://dblp.org/pid/10/2874.html), [John K. Tsotsos](https://dblp.org/pid/t/JohnKTsotsos.html), [Jong Hyuk Lee](https://dblp.org/pid/39/2874.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Junfei Zhuang](https://dblp.org/pid/213/4212.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Kangkang Wang](https://dblp.org/pid/03/9859.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Lei Chen](https://dblp.org/pid/09/3666.html), [Lei Liu](https://dblp.org/pid/21/2715-49.html), [Leida Guo](https://dblp.org/pid/249/8242.html), [Li Zhang](https://dblp.org/pid/89/5992-40.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lichao Zhang](https://dblp.org/pid/126/8027-1.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Lijun Zhou](https://dblp.org/pid/14/1719.html):

The Seventh Visual Object Tracking VOT2019 Challenge Results. [ICCV Workshops2019](https://dblp.org/db/conf/iccvw/iccvw2019.html#conf/iccvw/KristanBZRGBDDN19): 2206-2241
- ![](https://dblp.org/img/n.png)

\[c4\]
[Hakan Cevikalp](https://dblp.org/pid/14/6210.html), Hasan Saribas, [Burak Benligiray](https://dblp.org/pid/119/9508.html), [Sinem Kahvecioglu](https://dblp.org/pid/225/3132.html):

Visual Object Tracking by Using Ranking Loss. [ICCV Workshops2019](https://dblp.org/db/conf/iccvw/iccvw2019.html#conf/iccvw/CevikalpSBK19): 2271-2280
- ![](https://dblp.org/img/n.png)

\[c3\]
[Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Onur Eker](https://dblp.org/pid/180/7146.html), Hasan Saribas, [Hakan Çevikalp](https://dblp.org/pid/14/6210.html):

Detection Based Tracking of Unmanned Aerial Vehicles. [SIU2019](https://dblp.org/db/conf/siu/siu2019.html#conf/siu/UzunESC19): 1-4
- 2018
- ![](https://dblp.org/img/n.png)

\[c2\]
Hasan Saribas, [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Sinem Kahvecioglu](https://dblp.org/pid/225/3132.html):

Car detection in images taken from unmanned aerial vehicles. [SIU2018](https://dblp.org/db/conf/siu/siu2018.html#conf/siu/SaribasCK18): 1-4
- ![](https://dblp.org/img/n.png)

\[c1\]
Hasan Saribas, [Ali Tatli](https://dblp.org/pid/225/3382.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Atilla Onrat](https://dblp.org/pid/225/3165.html):

Control of unmanned aerial vehicles using self tuning fuzzy PID. [SIU2018](https://dblp.org/db/conf/siu/siu2018.html#conf/siu/SaribasTO18): 1-4
- _no results_

automatic loading of the coauthor graph disabled due to its size.

**click here to**
**load the graph.**

Note that this feature is _work in progress_ and that it is still far from being perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/225/3263.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[2](https://dblp.org/pid/225/3263.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Said Aldemir](https://dblp.org/pid/379/6036.html)

[\[i6\]](https://dblp.org/pid/225/3263.html#i6)

[3](https://dblp.org/pid/225/3263.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[George De Ath](https://dblp.org/pid/220/3209.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[4](https://dblp.org/pid/225/3263.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bing Bai](https://dblp.org/pid/54/5260.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[5](https://dblp.org/pid/225/3263.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Haoran Bai](https://dblp.org/pid/235/9510.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[6](https://dblp.org/pid/225/3263.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Hongliang Bai](https://dblp.org/pid/34/5268.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[7](https://dblp.org/pid/225/3263.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shuai Bai](https://dblp.org/pid/208/8033.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[8](https://dblp.org/pid/225/3263.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xiang Bai](https://dblp.org/pid/59/2741.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[9](https://dblp.org/pid/225/3263.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Burak Benligiray](https://dblp.org/pid/119/9508.html)

[\[c7\]](https://dblp.org/pid/225/3263.html#c7) [\[c6\]](https://dblp.org/pid/225/3263.html#c6) [\[c4\]](https://dblp.org/pid/225/3263.html#c4)

[10](https://dblp.org/pid/225/3263.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Amanda Berg](https://dblp.org/pid/163/4511.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[11](https://dblp.org/pid/225/3263.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Luca Bertinetto](https://dblp.org/pid/154/1351.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[12](https://dblp.org/pid/225/3263.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jesús Bescós](https://dblp.org/pid/97/2333.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[13](https://dblp.org/pid/225/3263.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[14](https://dblp.org/pid/225/3263.html?view=joint&param=14 "show joint publications")

[Ergun Biçici](https://dblp.org/pid/15/4891.html)

[\[c11\]](https://dblp.org/pid/225/3263.html#c11)

[15](https://dblp.org/pid/225/3263.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[16](https://dblp.org/pid/225/3263.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Llukman Cerkezi](https://dblp.org/pid/208/1312.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[17](https://dblp.org/pid/225/3263.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Hakan Çevikalp](https://dblp.org/pid/14/6210.html)

aka: Hakan Cevikalp

[\[j5\]](https://dblp.org/pid/225/3263.html#j5) [\[i6\]](https://dblp.org/pid/225/3263.html#i6) [\[i5\]](https://dblp.org/pid/225/3263.html#i5) [\[j4\]](https://dblp.org/pid/225/3263.html#j4) [\[j3\]](https://dblp.org/pid/225/3263.html#j3) [\[j2\]](https://dblp.org/pid/225/3263.html#j2) [\[c13\]](https://dblp.org/pid/225/3263.html#c13) [\[c12\]](https://dblp.org/pid/225/3263.html#c12) [\[j1\]](https://dblp.org/pid/225/3263.html#j1) [\[c10\]](https://dblp.org/pid/225/3263.html#c10) [\[i2\]](https://dblp.org/pid/225/3263.html#i2) [\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[i1\]](https://dblp.org/pid/225/3263.html#i1) [\[c7\]](https://dblp.org/pid/225/3263.html#c7) [\[c6\]](https://dblp.org/pid/225/3263.html#c6) [\[c5\]](https://dblp.org/pid/225/3263.html#c5) [\[c4\]](https://dblp.org/pid/225/3263.html#c4) [\[c3\]](https://dblp.org/pid/225/3263.html#c3) [\[c2\]](https://dblp.org/pid/225/3263.html#c2)

[18](https://dblp.org/pid/225/3263.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Antoni B. Chan](https://dblp.org/pid/55/5814.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[19](https://dblp.org/pid/225/3263.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[20](https://dblp.org/pid/225/3263.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bao Xin Chen](https://dblp.org/pid/153/1895.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[21](https://dblp.org/pid/225/3263.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Cheng Chen](https://dblp.org/pid/10/217.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[22](https://dblp.org/pid/225/3263.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Guangqi Chen](https://dblp.org/pid/178/8116.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[23](https://dblp.org/pid/225/3263.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jie Chen](https://dblp.org/pid/92/6289.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[24](https://dblp.org/pid/225/3263.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Lei Chen](https://dblp.org/pid/09/3666.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[25](https://dblp.org/pid/225/3263.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[26](https://dblp.org/pid/225/3263.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shuhao Chen](https://dblp.org/pid/43/2127.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[27](https://dblp.org/pid/225/3263.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xi Chen](https://dblp.org/pid/16/3283.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[28](https://dblp.org/pid/225/3263.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xier Chen](https://dblp.org/pid/260/3035.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[29](https://dblp.org/pid/225/3263.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[30](https://dblp.org/pid/225/3263.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xingyu Chen](https://dblp.org/pid/59/7651.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[31](https://dblp.org/pid/225/3263.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yanan Chen](https://dblp.org/pid/78/10104.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[32](https://dblp.org/pid/225/3263.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yanjie Chen](https://dblp.org/pid/02/7548.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[33](https://dblp.org/pid/225/3263.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yiwei Chen](https://dblp.org/pid/28/2965.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[34](https://dblp.org/pid/225/3263.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhihao Chen 0004](https://dblp.org/pid/50/505-4.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[35](https://dblp.org/pid/225/3263.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Li Cheng 0001](https://dblp.org/pid/13/4938-1.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[36](https://dblp.org/pid/225/3263.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Miao Cheng](https://dblp.org/pid/79/7377.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[37](https://dblp.org/pid/225/3263.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ziyi Cheng](https://dblp.org/pid/290/9342.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[38](https://dblp.org/pid/225/3263.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yu-Chen Chiu](https://dblp.org/pid/199/2494.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[39](https://dblp.org/pid/225/3263.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Seokeon Choi](https://dblp.org/pid/214/2200.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[40](https://dblp.org/pid/225/3263.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ozgun Cirakman](https://dblp.org/pid/86/8843.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[41](https://dblp.org/pid/225/3263.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[42](https://dblp.org/pid/225/3263.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Kenan Dai](https://dblp.org/pid/250/4445.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[43](https://dblp.org/pid/225/3263.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[44](https://dblp.org/pid/225/3263.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[45](https://dblp.org/pid/225/3263.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[46](https://dblp.org/pid/225/3263.html?view=joint&param=46 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=2)

[Serdarcan Dilbaz](https://dblp.org/pid/355/4549.html)

[\[i4\]](https://dblp.org/pid/225/3263.html#i4) [\[i3\]](https://dblp.org/pid/225/3263.html#i3)

[47](https://dblp.org/pid/225/3263.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xingping Dong](https://dblp.org/pid/156/3020.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[48](https://dblp.org/pid/225/3263.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yuan Dong](https://dblp.org/pid/66/875.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[49](https://dblp.org/pid/225/3263.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[50](https://dblp.org/pid/225/3263.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[51](https://dblp.org/pid/225/3263.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Hao Du 0006](https://dblp.org/pid/13/6441-6.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[52](https://dblp.org/pid/225/3263.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[53](https://dblp.org/pid/225/3263.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Furkan Durmus](https://dblp.org/pid/334/1382.html)

[\[i6\]](https://dblp.org/pid/225/3263.html#i6)

[54](https://dblp.org/pid/225/3263.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Onur Eker](https://dblp.org/pid/180/7146.html)

[\[c6\]](https://dblp.org/pid/225/3263.html#c6) [\[c3\]](https://dblp.org/pid/225/3263.html#c3)

[55](https://dblp.org/pid/225/3263.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Abdelrahman Eldesokey](https://dblp.org/pid/154/9080.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[56](https://dblp.org/pid/225/3263.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Richard M. Everson](https://dblp.org/pid/07/6331.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[57](https://dblp.org/pid/225/3263.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Heng Fan 0001](https://dblp.org/pid/20/10120-1.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[58](https://dblp.org/pid/225/3263.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chen Fang](https://dblp.org/pid/60/2548.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[59](https://dblp.org/pid/225/3263.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[60](https://dblp.org/pid/225/3263.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Wei Feng 0005](https://dblp.org/pid/17/1152-5.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[61](https://dblp.org/pid/225/3263.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[62](https://dblp.org/pid/225/3263.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhiyong Feng 0001](https://dblp.org/pid/48/195-1.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[63](https://dblp.org/pid/225/3263.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[64](https://dblp.org/pid/225/3263.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Gian Luca Foresti](https://dblp.org/pid/93/5522.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[65](https://dblp.org/pid/225/3263.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jianlong Fu](https://dblp.org/pid/83/8692.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[66](https://dblp.org/pid/225/3263.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[67](https://dblp.org/pid/225/3263.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jie Gao](https://dblp.org/pid/181/2794.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[68](https://dblp.org/pid/225/3263.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Álvaro García-Martín](https://dblp.org/pid/39/1542.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[69](https://dblp.org/pid/225/3263.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Efstratios Gavves](https://dblp.org/pid/03/8693.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[70](https://dblp.org/pid/225/3263.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shiming Ge](https://dblp.org/pid/93/8104.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[71](https://dblp.org/pid/225/3263.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Awet Haileslassie Gebrehiwot](https://dblp.org/pid/284/2554.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[72](https://dblp.org/pid/225/3263.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ömer Nezih Gerek](https://dblp.org/pid/48/4641.html)

[\[c7\]](https://dblp.org/pid/225/3263.html#c7)

[73](https://dblp.org/pid/225/3263.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Hossein Ghanei-Yakhdan](https://dblp.org/pid/188/5964.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[74](https://dblp.org/pid/225/3263.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Abel Gonzalez-Garcia](https://dblp.org/pid/156/0213.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[75](https://dblp.org/pid/225/3263.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[76](https://dblp.org/pid/225/3263.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[77](https://dblp.org/pid/225/3263.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Rama Krishna Sai S. Gorthi](https://dblp.org/pid/45/7595.html)

aka: Rama Krishna Sai Subrahmanyam Gorthi

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[78](https://dblp.org/pid/225/3263.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yang Gu](https://dblp.org/pid/01/5858.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[79](https://dblp.org/pid/225/3263.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yuzhang Gu](https://dblp.org/pid/122/3790.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[80](https://dblp.org/pid/225/3263.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shuosen Guan](https://dblp.org/pid/245/8954.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[81](https://dblp.org/pid/225/3263.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bilge Günsel](https://dblp.org/pid/47/5125.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[82](https://dblp.org/pid/225/3263.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Leida Guo](https://dblp.org/pid/249/8242.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[83](https://dblp.org/pid/225/3263.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Qing Guo 0005](https://dblp.org/pid/25/3038-5.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[84](https://dblp.org/pid/225/3263.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Deepak Gupta](https://dblp.org/pid/65/2751.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[85](https://dblp.org/pid/225/3263.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Filiz Gurkan](https://dblp.org/pid/202/7040.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[86](https://dblp.org/pid/225/3263.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Fredrik Gustafsson](https://dblp.org/pid/394/4497.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[87](https://dblp.org/pid/225/3263.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Gustav Häger](https://dblp.org/pid/157/3602.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[88](https://dblp.org/pid/225/3263.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Rui-Ze Han](https://dblp.org/pid/205/4022.html)

aka: Ruize Han

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[89](https://dblp.org/pid/225/3263.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Wencheng Han](https://dblp.org/pid/280/3348.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[90](https://dblp.org/pid/225/3263.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Alex Hauptmann 0001](https://dblp.org/pid/h/AlexanderGHauptmann.html)

aka: Alexander G. Hauptmann

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[91](https://dblp.org/pid/225/3263.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Anfeng He](https://dblp.org/pid/188/1205.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[92](https://dblp.org/pid/225/3263.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bin He](https://dblp.org/pid/78/4523.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[93](https://dblp.org/pid/225/3263.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Linbo He](https://dblp.org/pid/26/741.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[94](https://dblp.org/pid/225/3263.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhenyu He 0001](https://dblp.org/pid/57/6240-1.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[95](https://dblp.org/pid/225/3263.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Weiming Hu](https://dblp.org/pid/41/6824.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[96](https://dblp.org/pid/225/3263.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Weiming Hu 0004](https://dblp.org/pid/41/6824-4.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[97](https://dblp.org/pid/225/3263.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yan Huang 0008](https://dblp.org/pid/75/6434-8.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[98](https://dblp.org/pid/225/3263.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yanyan Huang](https://dblp.org/pid/88/4316.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[99](https://dblp.org/pid/225/3263.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhongjian Huang](https://dblp.org/pid/251/0619.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[100](https://dblp.org/pid/225/3263.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[101](https://dblp.org/pid/225/3263.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[102](https://dblp.org/pid/225/3263.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[103](https://dblp.org/pid/225/3263.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[104](https://dblp.org/pid/225/3263.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[105](https://dblp.org/pid/225/3263.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ho Min Jung](https://dblp.org/pid/36/5839.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[106](https://dblp.org/pid/225/3263.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Sinem Kahvecioglu](https://dblp.org/pid/225/3132.html)

[\[j4\]](https://dblp.org/pid/225/3263.html#j4) [\[c4\]](https://dblp.org/pid/225/3263.html#c4) [\[c2\]](https://dblp.org/pid/225/3263.html#c2)

[107](https://dblp.org/pid/225/3263.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[108](https://dblp.org/pid/225/3263.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jani Käpylä](https://dblp.org/pid/244/2529.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[109](https://dblp.org/pid/225/3263.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shohreh Kasaei](https://dblp.org/pid/78/5062.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[110](https://dblp.org/pid/225/3263.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xiao Ke](https://dblp.org/pid/78/9040.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[111](https://dblp.org/pid/225/3263.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Javad Khaghani](https://dblp.org/pid/233/0334.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[112](https://dblp.org/pid/225/3263.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[113](https://dblp.org/pid/225/3263.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Byeong Hak Kim](https://dblp.org/pid/214/8978.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[114](https://dblp.org/pid/225/3263.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Min Young Kim 0003](https://dblp.org/pid/34/5733-3.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[115](https://dblp.org/pid/225/3263.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[116](https://dblp.org/pid/225/3263.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Okan Köpüklü](https://dblp.org/pid/218/6295.html)

[\[j2\]](https://dblp.org/pid/225/3263.html#j2) [\[j1\]](https://dblp.org/pid/225/3263.html#j1) [\[i1\]](https://dblp.org/pid/225/3263.html#i1)

[117](https://dblp.org/pid/225/3263.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[118](https://dblp.org/pid/225/3263.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Hari Chandana Kuchibhotla](https://dblp.org/pid/284/2570.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[119](https://dblp.org/pid/225/3263.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[120](https://dblp.org/pid/225/3263.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[121](https://dblp.org/pid/225/3263.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jong Hyuk Lee](https://dblp.org/pid/39/2874.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[122](https://dblp.org/pid/225/3263.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jun Ha Lee](https://dblp.org/pid/260/2774.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[123](https://dblp.org/pid/225/3263.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jun-Hyun Lee](https://dblp.org/pid/155/8661.html)

aka: Junhyun Lee

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[124](https://dblp.org/pid/225/3263.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yunsung Lee](https://dblp.org/pid/227/9311.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[125](https://dblp.org/pid/225/3263.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[126](https://dblp.org/pid/225/3263.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[127](https://dblp.org/pid/225/3263.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bi Li 0005](https://dblp.org/pid/174/9761.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[128](https://dblp.org/pid/225/3263.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bing Li 0001](https://dblp.org/pid/13/2692-1.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[129](https://dblp.org/pid/225/3263.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bo Li 0114](https://dblp.org/pid/50/3402-114.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[130](https://dblp.org/pid/225/3263.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chenglong Li 0002](https://dblp.org/pid/83/7820-2.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[131](https://dblp.org/pid/225/3263.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Guoxuan Li](https://dblp.org/pid/121/6265.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[132](https://dblp.org/pid/225/3263.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Houqiang Li](https://dblp.org/pid/59/7017.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[133](https://dblp.org/pid/225/3263.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[134](https://dblp.org/pid/225/3263.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jiakun Li](https://dblp.org/pid/69/7673.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[135](https://dblp.org/pid/225/3263.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jianhua Li](https://dblp.org/pid/93/3389.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[136](https://dblp.org/pid/225/3263.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jing Li 0036](https://dblp.org/pid/l/JingLi36.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[137](https://dblp.org/pid/225/3263.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shihu Li](https://dblp.org/pid/242/1376.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[138](https://dblp.org/pid/225/3263.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shikun Li](https://dblp.org/pid/255/0117.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[139](https://dblp.org/pid/225/3263.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[140](https://dblp.org/pid/225/3263.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xin Li 0034](https://dblp.org/pid/09/1365-34.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[141](https://dblp.org/pid/225/3263.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yingping Li](https://dblp.org/pid/172/4240.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[142](https://dblp.org/pid/225/3263.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yuezhou Li](https://dblp.org/pid/284/2562.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[143](https://dblp.org/pid/225/3263.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yunkun Li](https://dblp.org/pid/260/2938.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[144](https://dblp.org/pid/225/3263.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yanchao Lian](https://dblp.org/pid/253/3698.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[145](https://dblp.org/pid/225/3263.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Haibin Ling](https://dblp.org/pid/93/3488.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[146](https://dblp.org/pid/225/3263.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[147](https://dblp.org/pid/225/3263.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[148](https://dblp.org/pid/225/3263.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jingen Liu](https://dblp.org/pid/10/5849.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[149](https://dblp.org/pid/225/3263.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jingtuo Liu](https://dblp.org/pid/164/5911.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[150](https://dblp.org/pid/225/3263.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Kaiwen Liu](https://dblp.org/pid/231/4262.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[151](https://dblp.org/pid/225/3263.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Lei Liu 0049](https://dblp.org/pid/21/2715-49.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[152](https://dblp.org/pid/225/3263.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Li Liu 0036](https://dblp.org/pid/33/4528-36.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[153](https://dblp.org/pid/225/3263.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Qingjie Liu 0001](https://dblp.org/pid/72/10584.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[154](https://dblp.org/pid/225/3263.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Wenyu Liu 0001](https://dblp.org/pid/42/4110-1.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[155](https://dblp.org/pid/225/3263.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yang Liu 0003](https://dblp.org/pid/51/3710-3.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[156](https://dblp.org/pid/225/3263.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Andong Lu](https://dblp.org/pid/245/2878.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[157](https://dblp.org/pid/225/3263.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[158](https://dblp.org/pid/225/3263.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Wei Lu](https://dblp.org/pid/98/6613.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[159](https://dblp.org/pid/225/3263.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jonathon Luiten](https://dblp.org/pid/211/7992.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[160](https://dblp.org/pid/225/3263.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[161](https://dblp.org/pid/225/3263.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chong Luo 0001](https://dblp.org/pid/79/3712-1.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[162](https://dblp.org/pid/225/3263.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhao Luo](https://dblp.org/pid/187/1232.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[163](https://dblp.org/pid/225/3263.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chao Ma 0004](https://dblp.org/pid/79/1552-4.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[164](https://dblp.org/pid/225/3263.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[165](https://dblp.org/pid/225/3263.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ziang Ma](https://dblp.org/pid/165/9621.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[166](https://dblp.org/pid/225/3263.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhijun Mai](https://dblp.org/pid/247/9401.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[167](https://dblp.org/pid/225/3263.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[168](https://dblp.org/pid/225/3263.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Seyed Mojtaba Marvasti-Zadeh](https://dblp.org/pid/188/6262.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[169](https://dblp.org/pid/225/3263.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[170](https://dblp.org/pid/225/3263.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[171](https://dblp.org/pid/225/3263.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[172](https://dblp.org/pid/225/3263.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[173](https://dblp.org/pid/225/3263.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Meng Ni](https://dblp.org/pid/174/2809.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[174](https://dblp.org/pid/225/3263.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zihan Ni](https://dblp.org/pid/187/9123.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[175](https://dblp.org/pid/225/3263.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yuzhen Niu](https://dblp.org/pid/28/7442.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[176](https://dblp.org/pid/225/3263.html?view=joint&param=176 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=3)

[Atilla Onrat](https://dblp.org/pid/225/3165.html)

[\[c1\]](https://dblp.org/pid/225/3263.html#c1)

[177](https://dblp.org/pid/225/3263.html?view=joint&param=177 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=2)

[Halit Orenbas](https://dblp.org/pid/225/2951.html)

[\[i4\]](https://dblp.org/pid/225/3263.html#i4)

[178](https://dblp.org/pid/225/3263.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Naveen Paluru](https://dblp.org/pid/260/3261.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[179](https://dblp.org/pid/225/3263.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[180](https://dblp.org/pid/225/3263.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bala Suraj Pedasingu](https://dblp.org/pid/260/3120.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[181](https://dblp.org/pid/225/3263.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[182](https://dblp.org/pid/225/3263.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[183](https://dblp.org/pid/225/3263.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jinqing Qi](https://dblp.org/pid/09/287.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[184](https://dblp.org/pid/225/3263.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chen Qian 0001](https://dblp.org/pid/70/3604-1.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[185](https://dblp.org/pid/225/3263.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chen Qian 0006](https://dblp.org/pid/70/3604-6.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[186](https://dblp.org/pid/225/3263.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shoumeng Qiu](https://dblp.org/pid/284/2537.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[187](https://dblp.org/pid/225/3263.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xi Qiu](https://dblp.org/pid/115/5698.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[188](https://dblp.org/pid/225/3263.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Aravindh Rajiv](https://dblp.org/pid/307/9144.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[189](https://dblp.org/pid/225/3263.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Muhammad Rana](https://dblp.org/pid/276/0222.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[190](https://dblp.org/pid/225/3263.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[191](https://dblp.org/pid/225/3263.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Litu Rout](https://dblp.org/pid/206/6445.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[192](https://dblp.org/pid/225/3263.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yusuf Salk](https://dblp.org/pid/328/4380.html)

[\[j2\]](https://dblp.org/pid/225/3263.html#j2) [\[c10\]](https://dblp.org/pid/225/3263.html#c10)

[193](https://dblp.org/pid/225/3263.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Thomas B. Schön](https://dblp.org/pid/85/4891.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[194](https://dblp.org/pid/225/3263.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[195](https://dblp.org/pid/225/3263.html?view=joint&param=195 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Mohamed S. Shehata](https://dblp.org/pid/33/2495.html)

aka: Mohamed Shehata 0001

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[196](https://dblp.org/pid/225/3263.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Furao Shen](https://dblp.org/pid/80/4685.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[197](https://dblp.org/pid/225/3263.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jianbing Shen](https://dblp.org/pid/38/5435.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[198](https://dblp.org/pid/225/3263.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[199](https://dblp.org/pid/225/3263.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Arnold W. M. Smeulders](https://dblp.org/pid/15/5400.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[200](https://dblp.org/pid/225/3263.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Dejia Song](https://dblp.org/pid/260/2975.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[201](https://dblp.org/pid/225/3263.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[202](https://dblp.org/pid/225/3263.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhichao Song](https://dblp.org/pid/169/4022.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[203](https://dblp.org/pid/225/3263.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xing Sun 0001](https://dblp.org/pid/90/2719-1.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[204](https://dblp.org/pid/225/3263.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jin Tang 0001](https://dblp.org/pid/56/4951-1.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[205](https://dblp.org/pid/225/3263.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ming Tang 0001](https://dblp.org/pid/73/4373-1.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[206](https://dblp.org/pid/225/3263.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Wenjie Tang](https://dblp.org/pid/87/7879.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[207](https://dblp.org/pid/225/3263.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xu Tang](https://dblp.org/pid/123/7064.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[208](https://dblp.org/pid/225/3263.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[209](https://dblp.org/pid/225/3263.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Dacheng Tao](https://dblp.org/pid/46/3391.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[210](https://dblp.org/pid/225/3263.html?view=joint&param=210 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=3)

[Ali Tatli](https://dblp.org/pid/225/3382.html)

[\[c1\]](https://dblp.org/pid/225/3263.html#c1)

[211](https://dblp.org/pid/225/3263.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhu Teng](https://dblp.org/pid/132/2247.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[212](https://dblp.org/pid/225/3263.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xinmei Tian 0001](https://dblp.org/pid/03/5204-1.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[213](https://dblp.org/pid/225/3263.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[214](https://dblp.org/pid/225/3263.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[215](https://dblp.org/pid/225/3263.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ardhendu Shekhar Tripathi](https://dblp.org/pid/141/9949.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[216](https://dblp.org/pid/225/3263.html?view=joint&param=216 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[217](https://dblp.org/pid/225/3263.html?view=joint&param=217 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[John K. Tsotsos](https://dblp.org/pid/t/JohnKTsotsos.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[218](https://dblp.org/pid/225/3263.html?view=joint&param=218 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Beyza Türkmen](https://dblp.org/pid/362/2171.html)

[\[i5\]](https://dblp.org/pid/225/3263.html#i5)

[219](https://dblp.org/pid/225/3263.html?view=joint&param=219 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ramazan Tarik Türksoy](https://dblp.org/pid/362/2299.html)

[\[i5\]](https://dblp.org/pid/225/3263.html#i5)

[220](https://dblp.org/pid/225/3263.html?view=joint&param=220 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bedirhan Uzun](https://dblp.org/pid/247/8937.html)

[\[j5\]](https://dblp.org/pid/225/3263.html#j5) [\[j3\]](https://dblp.org/pid/225/3263.html#j3) [\[j2\]](https://dblp.org/pid/225/3263.html#j2) [\[j1\]](https://dblp.org/pid/225/3263.html#j1) [\[c10\]](https://dblp.org/pid/225/3263.html#c10) [\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[i1\]](https://dblp.org/pid/225/3263.html#i1) [\[c6\]](https://dblp.org/pid/225/3263.html#c6) [\[c3\]](https://dblp.org/pid/225/3263.html#c3)

[221](https://dblp.org/pid/225/3263.html?view=joint&param=221 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Anton Varfolomieiev](https://dblp.org/pid/188/7504.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[222](https://dblp.org/pid/225/3263.html?view=joint&param=222 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Paul Voigtlaender](https://dblp.org/pid/166/6430.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[223](https://dblp.org/pid/225/3263.html?view=joint&param=223 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Tomás Vojír](https://dblp.org/pid/142/5749.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[224](https://dblp.org/pid/225/3263.html?view=joint&param=224 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[225](https://dblp.org/pid/225/3263.html?view=joint&param=225 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Fei Wang 0032](https://dblp.org/pid/52/3194-32.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[226](https://dblp.org/pid/225/3263.html?view=joint&param=226 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Guangting Wang](https://dblp.org/pid/227/7195.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[227](https://dblp.org/pid/225/3263.html?view=joint&param=227 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jinqiao Wang](https://dblp.org/pid/67/4236.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[228](https://dblp.org/pid/225/3263.html?view=joint&param=228 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Kangkang Wang](https://dblp.org/pid/03/9859.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[229](https://dblp.org/pid/225/3263.html?view=joint&param=229 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Liang Wang 0001](https://dblp.org/pid/56/4499-1.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[230](https://dblp.org/pid/225/3263.html?view=joint&param=230 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[231](https://dblp.org/pid/225/3263.html?view=joint&param=231 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[232](https://dblp.org/pid/225/3263.html?view=joint&param=232 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[233](https://dblp.org/pid/225/3263.html?view=joint&param=233 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Linyuan Wang](https://dblp.org/pid/138/5963.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[234](https://dblp.org/pid/225/3263.html?view=joint&param=234 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ning Wang 0020](https://dblp.org/pid/46/2005-20.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[235](https://dblp.org/pid/225/3263.html?view=joint&param=235 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Qiang Wang 0051](https://dblp.org/pid/64/5630-51.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[236](https://dblp.org/pid/225/3263.html?view=joint&param=236 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Weizhao Wang](https://dblp.org/pid/39/2359.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[237](https://dblp.org/pid/225/3263.html?view=joint&param=237 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ying-Ming Wang](https://dblp.org/pid/59/605.html)

aka: Yingming Wang

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[238](https://dblp.org/pid/225/3263.html?view=joint&param=238 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[239](https://dblp.org/pid/225/3263.html?view=joint&param=239 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yunhong Wang 0001](https://dblp.org/pid/95/6251.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[240](https://dblp.org/pid/225/3263.html?view=joint&param=240 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zeyu Wang 0008](https://dblp.org/pid/132/7882-8.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[241](https://dblp.org/pid/225/3263.html?view=joint&param=241 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zezhou Wang](https://dblp.org/pid/204/1179.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[242](https://dblp.org/pid/225/3263.html?view=joint&param=242 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Joost van de Weijer 0001](https://dblp.org/pid/67/3379.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[243](https://dblp.org/pid/225/3263.html?view=joint&param=243 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Baoyuan Wu](https://dblp.org/pid/73/7781.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[244](https://dblp.org/pid/225/3263.html?view=joint&param=244 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chenyan Wu](https://dblp.org/pid/76/1190.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[245](https://dblp.org/pid/225/3263.html?view=joint&param=245 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[246](https://dblp.org/pid/225/3263.html?view=joint&param=246 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jingjing Wu](https://dblp.org/pid/27/2384.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[247](https://dblp.org/pid/225/3263.html?view=joint&param=247 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

aka: Xiao-Jun Wu 0001

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[248](https://dblp.org/pid/225/3263.html?view=joint&param=248 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhirong Wu](https://dblp.org/pid/147/5025.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[249](https://dblp.org/pid/225/3263.html?view=joint&param=249 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[250](https://dblp.org/pid/225/3263.html?view=joint&param=250 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Tengfei Xing](https://dblp.org/pid/82/1822.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[251](https://dblp.org/pid/225/3263.html?view=joint&param=251 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhiwei Xiong](https://dblp.org/pid/54/6827.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[252](https://dblp.org/pid/225/3263.html?view=joint&param=252 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jingtao Xu](https://dblp.org/pid/119/1746.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[253](https://dblp.org/pid/225/3263.html?view=joint&param=253 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Pengfei Xu 0013](https://dblp.org/pid/04/383-13.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[254](https://dblp.org/pid/225/3263.html?view=joint&param=254 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[255](https://dblp.org/pid/225/3263.html?view=joint&param=255 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xiang Xu](https://dblp.org/pid/126/2962.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[256](https://dblp.org/pid/225/3263.html?view=joint&param=256 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yinda Xu](https://dblp.org/pid/254/1072.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[257](https://dblp.org/pid/225/3263.html?view=joint&param=257 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yufei Xu](https://dblp.org/pid/43/7400.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[258](https://dblp.org/pid/225/3263.html?view=joint&param=258 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[259](https://dblp.org/pid/225/3263.html?view=joint&param=259 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[260](https://dblp.org/pid/225/3263.html?view=joint&param=260 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[261](https://dblp.org/pid/225/3263.html?view=joint&param=261 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[262](https://dblp.org/pid/225/3263.html?view=joint&param=262 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Junyan Yang](https://dblp.org/pid/52/6890.html)

[\[i6\]](https://dblp.org/pid/225/3263.html#i6)

[263](https://dblp.org/pid/225/3263.html?view=joint&param=263 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Kang Yang](https://dblp.org/pid/86/8501.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[264](https://dblp.org/pid/225/3263.html?view=joint&param=264 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ming-Hsuan Yang 0001](https://dblp.org/pid/79/3711.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[265](https://dblp.org/pid/225/3263.html?view=joint&param=265 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Tianyu Yang 0003](https://dblp.org/pid/120/8076-3.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[266](https://dblp.org/pid/225/3263.html?view=joint&param=266 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[267](https://dblp.org/pid/225/3263.html?view=joint&param=267 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[268](https://dblp.org/pid/225/3263.html?view=joint&param=268 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yuncon Yao](https://dblp.org/pid/284/2556.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[269](https://dblp.org/pid/225/3263.html?view=joint&param=269 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Hasan Serhan Yavuz](https://dblp.org/pid/18/5588.html)

[\[c13\]](https://dblp.org/pid/225/3263.html#c13)

[270](https://dblp.org/pid/225/3263.html?view=joint&param=270 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yu Ye 0004](https://dblp.org/pid/129/0969-4.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[271](https://dblp.org/pid/225/3263.html?view=joint&param=271 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=2)

[Cagri Yesil](https://dblp.org/pid/09/10719.html)

[\[i4\]](https://dblp.org/pid/225/3263.html#i4)

[272](https://dblp.org/pid/225/3263.html?view=joint&param=272 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Eunu Yi](https://dblp.org/pid/260/3303.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[273](https://dblp.org/pid/225/3263.html?view=joint&param=273 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[J. Yin](https://dblp.org/pid/51/2242.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[274](https://dblp.org/pid/225/3263.html?view=joint&param=274 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jun Yin 0003](https://dblp.org/pid/58/5423-3.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[275](https://dblp.org/pid/225/3263.html?view=joint&param=275 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shan You](https://dblp.org/pid/179/2548.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[276](https://dblp.org/pid/225/3263.html?view=joint&param=276 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Hongyuan Yu](https://dblp.org/pid/232/2265.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[277](https://dblp.org/pid/225/3263.html?view=joint&param=277 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jiaqian Yu](https://dblp.org/pid/164/7325.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[278](https://dblp.org/pid/225/3263.html?view=joint&param=278 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Kaicheng Yu](https://dblp.org/pid/198/0861.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[279](https://dblp.org/pid/225/3263.html?view=joint&param=279 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Wenjun Zeng 0001](https://dblp.org/pid/57/145.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[280](https://dblp.org/pid/225/3263.html?view=joint&param=280 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Baopeng Zhang](https://dblp.org/pid/22/3524.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[281](https://dblp.org/pid/225/3263.html?view=joint&param=281 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chengquan Zhang](https://dblp.org/pid/163/1795.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[282](https://dblp.org/pid/225/3263.html?view=joint&param=282 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[283](https://dblp.org/pid/225/3263.html?view=joint&param=283 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[284](https://dblp.org/pid/225/3263.html?view=joint&param=284 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Fangyi Zhang](https://dblp.org/pid/10/8496.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[285](https://dblp.org/pid/225/3263.html?view=joint&param=285 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Haitao Zhang](https://dblp.org/pid/19/6669.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[286](https://dblp.org/pid/225/3263.html?view=joint&param=286 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jinyue Zhang](https://dblp.org/pid/10/2874.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[287](https://dblp.org/pid/225/3263.html?view=joint&param=287 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[288](https://dblp.org/pid/225/3263.html?view=joint&param=288 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Kangkai Zhang](https://dblp.org/pid/260/2990.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[289](https://dblp.org/pid/225/3263.html?view=joint&param=289 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Li Zhang 0040](https://dblp.org/pid/89/5992-40.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[290](https://dblp.org/pid/225/3263.html?view=joint&param=290 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Lichao Zhang 0001](https://dblp.org/pid/126/8027-1.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[291](https://dblp.org/pid/225/3263.html?view=joint&param=291 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Pengfei Zhang 0005](https://dblp.org/pid/58/4525-5.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[292](https://dblp.org/pid/225/3263.html?view=joint&param=292 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Pengyu Zhang](https://dblp.org/pid/33/4816.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[293](https://dblp.org/pid/225/3263.html?view=joint&param=293 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Qi Zhang](https://dblp.org/pid/52/323.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[294](https://dblp.org/pid/225/3263.html?view=joint&param=294 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ruohan Zhang](https://dblp.org/pid/160/9929.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[295](https://dblp.org/pid/225/3263.html?view=joint&param=295 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ting Zhang 0006](https://dblp.org/pid/06/5919-6.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[296](https://dblp.org/pid/225/3263.html?view=joint&param=296 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xiaohan Zhang](https://dblp.org/pid/96/6053.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[297](https://dblp.org/pid/225/3263.html?view=joint&param=297 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xiaolin Zhang](https://dblp.org/pid/99/2516.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[298](https://dblp.org/pid/225/3263.html?view=joint&param=298 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xinyu Zhang 0020](https://dblp.org/pid/58/4582-20.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[299](https://dblp.org/pid/225/3263.html?view=joint&param=299 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yi Zhang](https://dblp.org/pid/64/6544.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[300](https://dblp.org/pid/225/3263.html?view=joint&param=300 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yunhua Zhang](https://dblp.org/pid/60/9627.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[301](https://dblp.org/pid/225/3263.html?view=joint&param=301 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yushan Zhang](https://dblp.org/pid/50/10702.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[302](https://dblp.org/pid/225/3263.html?view=joint&param=302 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhaoliang Zhang](https://dblp.org/pid/81/7883.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[303](https://dblp.org/pid/225/3263.html?view=joint&param=303 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[304](https://dblp.org/pid/225/3263.html?view=joint&param=304 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhipeng Zhang](https://dblp.org/pid/49/4941.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[305](https://dblp.org/pid/225/3263.html?view=joint&param=305 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[306](https://dblp.org/pid/225/3263.html?view=joint&param=306 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Fei Zhao](https://dblp.org/pid/21/6180.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[307](https://dblp.org/pid/225/3263.html?view=joint&param=307 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Haojie Zhao](https://dblp.org/pid/216/7590.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[308](https://dblp.org/pid/225/3263.html?view=joint&param=308 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jie Zhao 0014](https://dblp.org/pid/23/3168-14.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[309](https://dblp.org/pid/225/3263.html?view=joint&param=309 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[310](https://dblp.org/pid/225/3263.html?view=joint&param=310 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Shengwei Zhao](https://dblp.org/pid/155/9654.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[311](https://dblp.org/pid/225/3263.html?view=joint&param=311 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Ming Zhen](https://dblp.org/pid/307/8430.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[312](https://dblp.org/pid/225/3263.html?view=joint&param=312 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Linyu Zheng](https://dblp.org/pid/210/2313.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[313](https://dblp.org/pid/225/3263.html?view=joint&param=313 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Pengkun Zheng](https://dblp.org/pid/260/2752.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[314](https://dblp.org/pid/225/3263.html?view=joint&param=314 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[315](https://dblp.org/pid/225/3263.html?view=joint&param=315 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Lijun Zhou](https://dblp.org/pid/14/1719.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[316](https://dblp.org/pid/225/3263.html?view=joint&param=316 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Wengang Zhou 0001](https://dblp.org/pid/22/4544-1.html)

[\[c8\]](https://dblp.org/pid/225/3263.html#c8)

[317](https://dblp.org/pid/225/3263.html?view=joint&param=317 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Yu Zhou 0016](https://dblp.org/pid/36/2728-16.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[318](https://dblp.org/pid/225/3263.html?view=joint&param=318 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9)

[319](https://dblp.org/pid/225/3263.html?view=joint&param=319 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c9\]](https://dblp.org/pid/225/3263.html#c9) [\[c8\]](https://dblp.org/pid/225/3263.html#c8) [\[c5\]](https://dblp.org/pid/225/3263.html#c5)

[320](https://dblp.org/pid/225/3263.html?view=joint&param=320 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/225/3263.html?view=group&param=1)

[Junfei Zhuang](https://dblp.org/pid/213/4212.html)

[\[c5\]](https://dblp.org/pid/225/3263.html#c5)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/225/3263.html#) [\[–\]](https://dblp.org/pid/225/3263.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/225/3263.html#) [\[–\]](https://dblp.org/pid/225/3263.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/225/3263.html#) [\[–\]](https://dblp.org/pid/225/3263.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/225/3263.html#) [\[–\]](https://dblp.org/pid/225/3263.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/225/3263.html#) [\[–\]](https://dblp.org/pid/225/3263.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)