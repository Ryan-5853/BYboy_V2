> 抓取来源：https://dblp.org/pid/247/8937.html

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

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Bedirhan+Uzun%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F247%2F8937%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Bedirhan+Uzun+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F247%2F8937%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Bedirhan+Uzun+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F247%2F8937%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Bedirhan+Uzun%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F247%2F8937%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Bedirhan+Uzun+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F247%2F8937%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Bedirhan+Uzun%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F247%2F8937%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Bedirhan+Uzun%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F247%2F8937%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F247%2F8937%3E+%7D+.%0A%0A%7D)

_showing all12 records_

2016202652019: 22020: 22020: 22021: 32021: 32021: 32022: 22022: 22023: 22025: 1

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

- ![](https://dblp.org/img/add-mark.12x12.png)Hakan Çevikalp (12)
- ![](https://dblp.org/img/add-mark.12x12.png)Hasan Saribas (10)
- ![](https://dblp.org/img/add-mark.12x12.png)Okan Köpüklü (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Xuefeng Zhu 0003 (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Zhenhua Feng 0001 (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Jun Yin 0003 (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Christian Micheloni (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Yuzhang Gu (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Chi-Yi Tsai (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Linyuan Wang (2)

- _177 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (12)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Pattern Recognit. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)SIU (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Neural Networks Learn. Syst. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ECCV (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Neurocomputing (1)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ICCV (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IEEE Trans. Pattern Anal. Mach. Intell. (1)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (9)
- ![](https://dblp.org/img/add-mark.12x12.png)open (3)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[j5\]
[Hakan Cevikalp](https://dblp.org/pid/14/6210.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hasan Saribas](https://dblp.org/pid/225/3263.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bedirhan Uzun:

Reaching Nirvana: Maximizing the Margin in Both Euclidean and Angular Spaces for Deep Neural Network Classification. [IEEE Trans. Neural Networks Learn. Syst.36(5)](https://dblp.org/db/journals/tnn/tnn36.html#journals/tnn/CevikalpSU25): 8178-8191 (2025)
- 2023
- ![](https://dblp.org/img/n.png)

\[j4\]
Bedirhan Uzun, [Hakan Cevikalp](https://dblp.org/pid/14/6210.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hasan Saribas](https://dblp.org/pid/225/3263.html):

Deep Discriminative Feature Models (DDFMs) for Set Based Face Recognition and Distance Metric Learning. [IEEE Trans. Pattern Anal. Mach. Intell.45(5)](https://dblp.org/db/journals/pami/pami45.html#journals/pami/UzunCS23): 5594-5608 (2023)
- ![](https://dblp.org/img/n.png)

\[j3\]
[Hakan Cevikalp](https://dblp.org/pid/14/6210.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bedirhan Uzun, [Yusuf Salk](https://dblp.org/pid/328/4380.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Okan Köpüklü](https://dblp.org/pid/218/6295.html):

From anomaly detection to open set recognition: Bridging the gap. [Pattern Recognit.138](https://dblp.org/db/journals/pr/pr138.html#journals/pr/CevikalpUSSK23): 109385 (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[j2\]
[Hasan Saribas](https://dblp.org/pid/225/3263.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Okan Köpüklü](https://dblp.org/pid/218/6295.html), Bedirhan Uzun:

TRAT: Tracking by attention using spatio-temporal features. [Neurocomputing492](https://dblp.org/db/journals/ijon/ijon492.html#journals/ijon/SaribasCKU22): 150-161 (2022)
- ![](https://dblp.org/img/n.png)

\[c5\]
[Yusuf Salk](https://dblp.org/pid/328/4380.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bedirhan Uzun, [Hakan Çevikalp](https://dblp.org/pid/14/6210.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html):

Anomaly Detection with Deep Compact Hypersphere. [SIU2022](https://dblp.org/db/conf/siu/siu2022.html#conf/siu/SalkUCS22): 1-4
- 2021
- ![](https://dblp.org/img/n.png)

\[j1\]
[Hakan Cevikalp](https://dblp.org/pid/14/6210.html), Bedirhan Uzun, [Okan Köpüklü](https://dblp.org/pid/218/6295.html), [Gürkan Öztürk](https://dblp.org/pid/39/3242.html):

Deep compact polyhedral conic classifier for open and closed set recognition. [Pattern Recognit.119](https://dblp.org/db/journals/pr/pr119.html#journals/pr/CevikalpUKO21): 108080 (2021)
- ![](https://dblp.org/img/n.png)

\[c4\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Yu-Chen Chiu](https://dblp.org/pid/199/2494.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Xingping Dong](https://dblp.org/pid/156/3020.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Bilge Günsel](https://dblp.org/pid/47/5125.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Wencheng Han](https://dblp.org/pid/280/3348.html), [Yanyan Huang](https://dblp.org/pid/88/4316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [J. Yin](https://dblp.org/pid/51/2242.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Jingen Liu](https://dblp.org/pid/10/5849.html), [Li Liu](https://dblp.org/pid/33/4528-36.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Jonathon Luiten](https://dblp.org/pid/211/7992.html), [Jie Ma](https://dblp.org/pid/62/5110.html), [Ziang Ma](https://dblp.org/pid/165/9621.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Yuzhen Niu](https://dblp.org/pid/28/7442.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Aravindh Rajiv](https://dblp.org/pid/307/9144.html), [Muhammad Rana](https://dblp.org/pid/276/0222.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Ling Shao](https://dblp.org/pid/75/1281.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furao Shen](https://dblp.org/pid/80/4685.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), Bedirhan Uzun, [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Paul Voigtlaender](https://dblp.org/pid/166/6430.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html), [Chenyan Wu](https://dblp.org/pid/76/1190.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang Xu](https://dblp.org/pid/126/2962.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Xiaohan Zhang](https://dblp.org/pid/96/6053.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Ming Zhen](https://dblp.org/pid/307/8430.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html):

The Ninth Visual Object Tracking VOT2021 Challenge Results. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/KristanMLFPKCDZ21): 2711-2738
- ![](https://dblp.org/img/n.png)

\[i2\]
[Hakan Cevikalp](https://dblp.org/pid/14/6210.html), Bedirhan Uzun, [Okan Köpüklü](https://dblp.org/pid/218/6295.html), [Gürkan Öztürk](https://dblp.org/pid/39/3242.html):

Deep Compact Polyhedral Conic Classifier for Open and Closed Set Recognition. [CoRRabs/2102.12570](https://dblp.org/db/journals/corr/corr2102.html#journals/corr/abs-2102-12570) (2021)
- 2020
- ![](https://dblp.org/img/n.png)

\[c3\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Linbo He](https://dblp.org/pid/26/741.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Alexander G. Hauptmann](https://dblp.org/pid/h/AlexanderGHauptmann.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Álvaro García-Martín](https://dblp.org/pid/39/1542.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Anton Varfolomieiev](https://dblp.org/pid/188/7504.html), [Awet Haileslassie Gebrehiwot](https://dblp.org/pid/284/2554.html), Bedirhan Uzun, [Bin Yan](https://dblp.org/pid/92/786-4.html), [Bing Li](https://dblp.org/pid/13/2692-1.html), [Chen Qian](https://dblp.org/pid/70/3604-6.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Fredrik Gustafsson](https://dblp.org/pid/394/4497.html), [Gian Luca Foresti](https://dblp.org/pid/93/5522.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Haojie Zhao](https://dblp.org/pid/216/7590.html), [Haoran Bai](https://dblp.org/pid/235/9510.html), [Hari Chandana Kuchibhotla](https://dblp.org/pid/284/2570.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Hossein Ghanei-Yakhdan](https://dblp.org/pid/188/5964.html), [Houqiang Li](https://dblp.org/pid/59/7017.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Javad Khaghani](https://dblp.org/pid/233/0334.html), [Jesús Bescós](https://dblp.org/pid/97/2333.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Jianlong Fu](https://dblp.org/pid/83/8692.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Jingtao Xu](https://dblp.org/pid/119/1746.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Junhyun Lee](https://dblp.org/pid/155/8661.html), [Kaicheng Yu](https://dblp.org/pid/198/0861.html), [Kaiwen Liu](https://dblp.org/pid/231/4262.html), [Kang Yang](https://dblp.org/pid/86/8501.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Li Cheng](https://dblp.org/pid/13/4938-1.html), [Li Zhang](https://dblp.org/pid/89/5992-40.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Luca Bertinetto](https://dblp.org/pid/154/1351.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Ning Wang](https://dblp.org/pid/46/2005-20.html), [Pengyu Zhang](https://dblp.org/pid/33/4816.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Qiang Wang](https://dblp.org/pid/64/5630-51.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Rama Krishna Sai Subrahmanyam Gorthi](https://dblp.org/pid/45/7595.html), [Seokeon Choi](https://dblp.org/pid/214/2200.html), [Seyed Mojtaba Marvasti-Zadeh](https://dblp.org/pid/188/6262.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Shohreh Kasaei](https://dblp.org/pid/78/5062.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Shuhao Chen](https://dblp.org/pid/43/2127.html), [Thomas B. Schön](https://dblp.org/pid/85/4891.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Weiming Hu](https://dblp.org/pid/41/6824-4.html), [Wengang Zhou](https://dblp.org/pid/22/4544-1.html), [Xi Qiu](https://dblp.org/pid/115/5698.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Xiao-Jun Wu](https://dblp.org/pid/13/5168-1.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Yingming Wang](https://dblp.org/pid/59/605.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yuncon Yao](https://dblp.org/pid/284/2556.html), [Yunsung Lee](https://dblp.org/pid/227/9311.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Zezhou Wang](https://dblp.org/pid/204/1179.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhijun Mai](https://dblp.org/pid/247/9401.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Zhirong Wu](https://dblp.org/pid/147/5025.html), [Ziang Ma](https://dblp.org/pid/165/9621.html):

The Eighth Visual Object Tracking VOT2020 Challenge Results. [ECCV Workshops (5)2020](https://dblp.org/db/conf/eccv/eccv2020-w5.html#conf/eccv/KristanLMFPKDZL20): 547-601
- ![](https://dblp.org/img/n.png)

\[i1\]
[Hasan Saribas](https://dblp.org/pid/225/3263.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Okan Köpüklü](https://dblp.org/pid/218/6295.html), Bedirhan Uzun:

TRAT: Tracking by Attention Using Spatio-Temporal Features. [CoRRabs/2011.09524](https://dblp.org/db/journals/corr/corr2011.html#journals/corr/abs-2011-09524) (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[c2\]
[Hasan Saribas](https://dblp.org/pid/225/3263.html), Bedirhan Uzun, [Burak Benligiray](https://dblp.org/pid/119/9508.html), [Onur Eker](https://dblp.org/pid/180/7146.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html):

A Hybrid Method for Tracking of Objects by UAVs. [CVPR Workshops2019](https://dblp.org/db/conf/cvpr/cvprw2019.html#conf/cvpr/SaribasUBEC19): 563-572
- ![](https://dblp.org/img/n.png)

\[c1\]
Bedirhan Uzun, [Onur Eker](https://dblp.org/pid/180/7146.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Hakan Çevikalp](https://dblp.org/pid/14/6210.html):

Detection Based Tracking of Unmanned Aerial Vehicles. [SIU2019](https://dblp.org/db/conf/siu/siu2019.html#conf/siu/UzunESC19): 1-4
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/247/8937.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[2](https://dblp.org/pid/247/8937.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Haoran Bai](https://dblp.org/pid/235/9510.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[3](https://dblp.org/pid/247/8937.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Burak Benligiray](https://dblp.org/pid/119/9508.html)

[\[c2\]](https://dblp.org/pid/247/8937.html#c2)

[4](https://dblp.org/pid/247/8937.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Luca Bertinetto](https://dblp.org/pid/154/1351.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[5](https://dblp.org/pid/247/8937.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jesús Bescós](https://dblp.org/pid/97/2333.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[6](https://dblp.org/pid/247/8937.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[7](https://dblp.org/pid/247/8937.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[8](https://dblp.org/pid/247/8937.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Llukman Cerkezi](https://dblp.org/pid/208/1312.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[9](https://dblp.org/pid/247/8937.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Hakan Çevikalp](https://dblp.org/pid/14/6210.html)

aka: Hakan Cevikalp

[\[j5\]](https://dblp.org/pid/247/8937.html#j5) [\[j4\]](https://dblp.org/pid/247/8937.html#j4) [\[j3\]](https://dblp.org/pid/247/8937.html#j3) [\[j2\]](https://dblp.org/pid/247/8937.html#j2) [\[c5\]](https://dblp.org/pid/247/8937.html#c5) [\[j1\]](https://dblp.org/pid/247/8937.html#j1) [\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[i2\]](https://dblp.org/pid/247/8937.html#i2) [\[c3\]](https://dblp.org/pid/247/8937.html#c3) [\[i1\]](https://dblp.org/pid/247/8937.html#i1) [\[c2\]](https://dblp.org/pid/247/8937.html#c2) [\[c1\]](https://dblp.org/pid/247/8937.html#c1)

[10](https://dblp.org/pid/247/8937.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[11](https://dblp.org/pid/247/8937.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Guangqi Chen](https://dblp.org/pid/178/8116.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[12](https://dblp.org/pid/247/8937.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[13](https://dblp.org/pid/247/8937.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Shuhao Chen](https://dblp.org/pid/43/2127.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[14](https://dblp.org/pid/247/8937.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[15](https://dblp.org/pid/247/8937.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yiwei Chen](https://dblp.org/pid/28/2965.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[16](https://dblp.org/pid/247/8937.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Li Cheng 0001](https://dblp.org/pid/13/4938-1.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[17](https://dblp.org/pid/247/8937.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Miao Cheng](https://dblp.org/pid/79/7377.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[18](https://dblp.org/pid/247/8937.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Ziyi Cheng](https://dblp.org/pid/290/9342.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[19](https://dblp.org/pid/247/8937.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yu-Chen Chiu](https://dblp.org/pid/199/2494.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[20](https://dblp.org/pid/247/8937.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Seokeon Choi](https://dblp.org/pid/214/2200.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[21](https://dblp.org/pid/247/8937.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Ozgun Cirakman](https://dblp.org/pid/86/8843.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[22](https://dblp.org/pid/247/8937.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[23](https://dblp.org/pid/247/8937.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Kenan Dai](https://dblp.org/pid/250/4445.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[24](https://dblp.org/pid/247/8937.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[25](https://dblp.org/pid/247/8937.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[26](https://dblp.org/pid/247/8937.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[27](https://dblp.org/pid/247/8937.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xingping Dong](https://dblp.org/pid/156/3020.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[28](https://dblp.org/pid/247/8937.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[29](https://dblp.org/pid/247/8937.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[30](https://dblp.org/pid/247/8937.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[31](https://dblp.org/pid/247/8937.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Onur Eker](https://dblp.org/pid/180/7146.html)

[\[c2\]](https://dblp.org/pid/247/8937.html#c2) [\[c1\]](https://dblp.org/pid/247/8937.html#c1)

[32](https://dblp.org/pid/247/8937.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Heng Fan 0001](https://dblp.org/pid/20/10120-1.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[33](https://dblp.org/pid/247/8937.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[34](https://dblp.org/pid/247/8937.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[35](https://dblp.org/pid/247/8937.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Zhiyong Feng 0001](https://dblp.org/pid/48/195-1.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[36](https://dblp.org/pid/247/8937.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[37](https://dblp.org/pid/247/8937.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Gian Luca Foresti](https://dblp.org/pid/93/5522.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[38](https://dblp.org/pid/247/8937.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jianlong Fu](https://dblp.org/pid/83/8692.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[39](https://dblp.org/pid/247/8937.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[40](https://dblp.org/pid/247/8937.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Álvaro García-Martín](https://dblp.org/pid/39/1542.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[41](https://dblp.org/pid/247/8937.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Shiming Ge](https://dblp.org/pid/93/8104.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[42](https://dblp.org/pid/247/8937.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Awet Haileslassie Gebrehiwot](https://dblp.org/pid/284/2554.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[43](https://dblp.org/pid/247/8937.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Hossein Ghanei-Yakhdan](https://dblp.org/pid/188/5964.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[44](https://dblp.org/pid/247/8937.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[45](https://dblp.org/pid/247/8937.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[46](https://dblp.org/pid/247/8937.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Rama Krishna Sai S. Gorthi](https://dblp.org/pid/45/7595.html)

aka: Rama Krishna Sai Subrahmanyam Gorthi

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[47](https://dblp.org/pid/247/8937.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yuzhang Gu](https://dblp.org/pid/122/3790.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[48](https://dblp.org/pid/247/8937.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Bilge Günsel](https://dblp.org/pid/47/5125.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[49](https://dblp.org/pid/247/8937.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Qing Guo 0005](https://dblp.org/pid/25/3038-5.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[50](https://dblp.org/pid/247/8937.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Filiz Gurkan](https://dblp.org/pid/202/7040.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[51](https://dblp.org/pid/247/8937.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Fredrik Gustafsson](https://dblp.org/pid/394/4497.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[52](https://dblp.org/pid/247/8937.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Gustav Häger](https://dblp.org/pid/157/3602.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[53](https://dblp.org/pid/247/8937.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Wencheng Han](https://dblp.org/pid/280/3348.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[54](https://dblp.org/pid/247/8937.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Alex Hauptmann 0001](https://dblp.org/pid/h/AlexanderGHauptmann.html)

aka: Alexander G. Hauptmann

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[55](https://dblp.org/pid/247/8937.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Linbo He](https://dblp.org/pid/26/741.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[56](https://dblp.org/pid/247/8937.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Weiming Hu 0004](https://dblp.org/pid/41/6824-4.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[57](https://dblp.org/pid/247/8937.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yanyan Huang](https://dblp.org/pid/88/4316.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[58](https://dblp.org/pid/247/8937.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[59](https://dblp.org/pid/247/8937.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[60](https://dblp.org/pid/247/8937.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[61](https://dblp.org/pid/247/8937.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[62](https://dblp.org/pid/247/8937.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[63](https://dblp.org/pid/247/8937.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[64](https://dblp.org/pid/247/8937.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jani Käpylä](https://dblp.org/pid/244/2529.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[65](https://dblp.org/pid/247/8937.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Shohreh Kasaei](https://dblp.org/pid/78/5062.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[66](https://dblp.org/pid/247/8937.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xiao Ke](https://dblp.org/pid/78/9040.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[67](https://dblp.org/pid/247/8937.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Javad Khaghani](https://dblp.org/pid/233/0334.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[68](https://dblp.org/pid/247/8937.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[69](https://dblp.org/pid/247/8937.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Byeong Hak Kim](https://dblp.org/pid/214/8978.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[70](https://dblp.org/pid/247/8937.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[71](https://dblp.org/pid/247/8937.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Okan Köpüklü](https://dblp.org/pid/218/6295.html)

[\[j3\]](https://dblp.org/pid/247/8937.html#j3) [\[j2\]](https://dblp.org/pid/247/8937.html#j2) [\[j1\]](https://dblp.org/pid/247/8937.html#j1) [\[i2\]](https://dblp.org/pid/247/8937.html#i2) [\[i1\]](https://dblp.org/pid/247/8937.html#i1)

[72](https://dblp.org/pid/247/8937.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[73](https://dblp.org/pid/247/8937.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Hari Chandana Kuchibhotla](https://dblp.org/pid/284/2570.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[74](https://dblp.org/pid/247/8937.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[75](https://dblp.org/pid/247/8937.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[76](https://dblp.org/pid/247/8937.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jun Ha Lee](https://dblp.org/pid/260/2774.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[77](https://dblp.org/pid/247/8937.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jun-Hyun Lee](https://dblp.org/pid/155/8661.html)

aka: Junhyun Lee

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[78](https://dblp.org/pid/247/8937.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yunsung Lee](https://dblp.org/pid/227/9311.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[79](https://dblp.org/pid/247/8937.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[80](https://dblp.org/pid/247/8937.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[81](https://dblp.org/pid/247/8937.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Bing Li 0001](https://dblp.org/pid/13/2692-1.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[82](https://dblp.org/pid/247/8937.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Houqiang Li](https://dblp.org/pid/59/7017.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[83](https://dblp.org/pid/247/8937.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[84](https://dblp.org/pid/247/8937.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jianhua Li](https://dblp.org/pid/93/3389.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[85](https://dblp.org/pid/247/8937.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[86](https://dblp.org/pid/247/8937.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yuezhou Li](https://dblp.org/pid/284/2562.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[87](https://dblp.org/pid/247/8937.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Haibin Ling](https://dblp.org/pid/93/3488.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[88](https://dblp.org/pid/247/8937.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[89](https://dblp.org/pid/247/8937.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[90](https://dblp.org/pid/247/8937.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jingen Liu](https://dblp.org/pid/10/5849.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[91](https://dblp.org/pid/247/8937.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Kaiwen Liu](https://dblp.org/pid/231/4262.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[92](https://dblp.org/pid/247/8937.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Li Liu 0036](https://dblp.org/pid/33/4528-36.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[93](https://dblp.org/pid/247/8937.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Qingjie Liu 0001](https://dblp.org/pid/72/10584.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[94](https://dblp.org/pid/247/8937.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[95](https://dblp.org/pid/247/8937.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Wei Lu](https://dblp.org/pid/98/6613.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[96](https://dblp.org/pid/247/8937.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jonathon Luiten](https://dblp.org/pid/211/7992.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[97](https://dblp.org/pid/247/8937.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[98](https://dblp.org/pid/247/8937.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[99](https://dblp.org/pid/247/8937.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Ziang Ma](https://dblp.org/pid/165/9621.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[100](https://dblp.org/pid/247/8937.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Zhijun Mai](https://dblp.org/pid/247/9401.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[101](https://dblp.org/pid/247/8937.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[102](https://dblp.org/pid/247/8937.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Seyed Mojtaba Marvasti-Zadeh](https://dblp.org/pid/188/6262.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[103](https://dblp.org/pid/247/8937.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[104](https://dblp.org/pid/247/8937.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[105](https://dblp.org/pid/247/8937.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[106](https://dblp.org/pid/247/8937.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[107](https://dblp.org/pid/247/8937.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yuzhen Niu](https://dblp.org/pid/28/7442.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[108](https://dblp.org/pid/247/8937.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Gürkan Öztürk](https://dblp.org/pid/39/3242.html)

[\[j1\]](https://dblp.org/pid/247/8937.html#j1) [\[i2\]](https://dblp.org/pid/247/8937.html#i2)

[109](https://dblp.org/pid/247/8937.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[110](https://dblp.org/pid/247/8937.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[111](https://dblp.org/pid/247/8937.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[112](https://dblp.org/pid/247/8937.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Chen Qian 0006](https://dblp.org/pid/70/3604-6.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[113](https://dblp.org/pid/247/8937.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Shoumeng Qiu](https://dblp.org/pid/284/2537.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[114](https://dblp.org/pid/247/8937.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xi Qiu](https://dblp.org/pid/115/5698.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[115](https://dblp.org/pid/247/8937.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Aravindh Rajiv](https://dblp.org/pid/307/9144.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[116](https://dblp.org/pid/247/8937.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Muhammad Rana](https://dblp.org/pid/276/0222.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[117](https://dblp.org/pid/247/8937.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[118](https://dblp.org/pid/247/8937.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yusuf Salk](https://dblp.org/pid/328/4380.html)

[\[j3\]](https://dblp.org/pid/247/8937.html#j3) [\[c5\]](https://dblp.org/pid/247/8937.html#c5)

[119](https://dblp.org/pid/247/8937.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Hasan Saribas](https://dblp.org/pid/225/3263.html)

[\[j5\]](https://dblp.org/pid/247/8937.html#j5) [\[j4\]](https://dblp.org/pid/247/8937.html#j4) [\[j3\]](https://dblp.org/pid/247/8937.html#j3) [\[j2\]](https://dblp.org/pid/247/8937.html#j2) [\[c5\]](https://dblp.org/pid/247/8937.html#c5) [\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3) [\[i1\]](https://dblp.org/pid/247/8937.html#i1) [\[c2\]](https://dblp.org/pid/247/8937.html#c2) [\[c1\]](https://dblp.org/pid/247/8937.html#c1)

[120](https://dblp.org/pid/247/8937.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Thomas B. Schön](https://dblp.org/pid/85/4891.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[121](https://dblp.org/pid/247/8937.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[122](https://dblp.org/pid/247/8937.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Mohamed S. Shehata](https://dblp.org/pid/33/2495.html)

aka: Mohamed Shehata 0001

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[123](https://dblp.org/pid/247/8937.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Furao Shen](https://dblp.org/pid/80/4685.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[124](https://dblp.org/pid/247/8937.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jianbing Shen](https://dblp.org/pid/38/5435.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[125](https://dblp.org/pid/247/8937.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[126](https://dblp.org/pid/247/8937.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[127](https://dblp.org/pid/247/8937.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[128](https://dblp.org/pid/247/8937.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[129](https://dblp.org/pid/247/8937.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[130](https://dblp.org/pid/247/8937.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[131](https://dblp.org/pid/247/8937.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Anton Varfolomieiev](https://dblp.org/pid/188/7504.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[132](https://dblp.org/pid/247/8937.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Paul Voigtlaender](https://dblp.org/pid/166/6430.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[133](https://dblp.org/pid/247/8937.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[134](https://dblp.org/pid/247/8937.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Fei Wang 0032](https://dblp.org/pid/52/3194-32.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[135](https://dblp.org/pid/247/8937.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Guangting Wang](https://dblp.org/pid/227/7195.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[136](https://dblp.org/pid/247/8937.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[137](https://dblp.org/pid/247/8937.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[138](https://dblp.org/pid/247/8937.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[139](https://dblp.org/pid/247/8937.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Linyuan Wang](https://dblp.org/pid/138/5963.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[140](https://dblp.org/pid/247/8937.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Ning Wang 0020](https://dblp.org/pid/46/2005-20.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[141](https://dblp.org/pid/247/8937.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Qiang Wang 0051](https://dblp.org/pid/64/5630-51.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[142](https://dblp.org/pid/247/8937.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Ying-Ming Wang](https://dblp.org/pid/59/605.html)

aka: Yingming Wang

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[143](https://dblp.org/pid/247/8937.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[144](https://dblp.org/pid/247/8937.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yunhong Wang 0001](https://dblp.org/pid/95/6251.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[145](https://dblp.org/pid/247/8937.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Zezhou Wang](https://dblp.org/pid/204/1179.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[146](https://dblp.org/pid/247/8937.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Chenyan Wu](https://dblp.org/pid/76/1190.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[147](https://dblp.org/pid/247/8937.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[148](https://dblp.org/pid/247/8937.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

aka: Xiao-Jun Wu 0001

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[149](https://dblp.org/pid/247/8937.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Zhirong Wu](https://dblp.org/pid/147/5025.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[150](https://dblp.org/pid/247/8937.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[151](https://dblp.org/pid/247/8937.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jingtao Xu](https://dblp.org/pid/119/1746.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[152](https://dblp.org/pid/247/8937.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[153](https://dblp.org/pid/247/8937.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xiang Xu](https://dblp.org/pid/126/2962.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[154](https://dblp.org/pid/247/8937.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[155](https://dblp.org/pid/247/8937.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[156](https://dblp.org/pid/247/8937.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[157](https://dblp.org/pid/247/8937.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[158](https://dblp.org/pid/247/8937.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Kang Yang](https://dblp.org/pid/86/8501.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[159](https://dblp.org/pid/247/8937.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[160](https://dblp.org/pid/247/8937.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[161](https://dblp.org/pid/247/8937.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yuncon Yao](https://dblp.org/pid/284/2556.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[162](https://dblp.org/pid/247/8937.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yu Ye 0004](https://dblp.org/pid/129/0969-4.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[163](https://dblp.org/pid/247/8937.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[J. Yin](https://dblp.org/pid/51/2242.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[164](https://dblp.org/pid/247/8937.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jun Yin 0003](https://dblp.org/pid/58/5423-3.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[165](https://dblp.org/pid/247/8937.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jiaqian Yu](https://dblp.org/pid/164/7325.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[166](https://dblp.org/pid/247/8937.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Kaicheng Yu](https://dblp.org/pid/198/0861.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[167](https://dblp.org/pid/247/8937.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[168](https://dblp.org/pid/247/8937.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[169](https://dblp.org/pid/247/8937.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Haitao Zhang](https://dblp.org/pid/19/6669.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[170](https://dblp.org/pid/247/8937.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[171](https://dblp.org/pid/247/8937.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Kangkai Zhang](https://dblp.org/pid/260/2990.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[172](https://dblp.org/pid/247/8937.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Li Zhang 0040](https://dblp.org/pid/89/5992-40.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[173](https://dblp.org/pid/247/8937.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Pengyu Zhang](https://dblp.org/pid/33/4816.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[174](https://dblp.org/pid/247/8937.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xiaohan Zhang](https://dblp.org/pid/96/6053.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[175](https://dblp.org/pid/247/8937.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xiaolin Zhang](https://dblp.org/pid/99/2516.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[176](https://dblp.org/pid/247/8937.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xinyu Zhang 0020](https://dblp.org/pid/58/4582-20.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[177](https://dblp.org/pid/247/8937.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Yushan Zhang](https://dblp.org/pid/50/10702.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[178](https://dblp.org/pid/247/8937.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[179](https://dblp.org/pid/247/8937.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Zhipeng Zhang](https://dblp.org/pid/49/4941.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[180](https://dblp.org/pid/247/8937.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[181](https://dblp.org/pid/247/8937.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Haojie Zhao](https://dblp.org/pid/216/7590.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[182](https://dblp.org/pid/247/8937.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[183](https://dblp.org/pid/247/8937.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Ming Zhen](https://dblp.org/pid/307/8430.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[184](https://dblp.org/pid/247/8937.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[185](https://dblp.org/pid/247/8937.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Wengang Zhou 0001](https://dblp.org/pid/22/4544-1.html)

[\[c3\]](https://dblp.org/pid/247/8937.html#c3)

[186](https://dblp.org/pid/247/8937.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4)

[187](https://dblp.org/pid/247/8937.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/247/8937.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c4\]](https://dblp.org/pid/247/8937.html#c4) [\[c3\]](https://dblp.org/pid/247/8937.html#c3)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/247/8937.html#) [\[–\]](https://dblp.org/pid/247/8937.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/247/8937.html#) [\[–\]](https://dblp.org/pid/247/8937.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/247/8937.html#) [\[–\]](https://dblp.org/pid/247/8937.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/247/8937.html#) [\[–\]](https://dblp.org/pid/247/8937.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/247/8937.html#) [\[–\]](https://dblp.org/pid/247/8937.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)