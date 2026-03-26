> 抓取来源：https://dblp.org/pid/336/7530.html

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

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Jianhao+Yuan%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F336%2F7530%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Jianhao+Yuan+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F336%2F7530%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Jianhao+Yuan+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F336%2F7530%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Jianhao+Yuan%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F336%2F7530%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Jianhao+Yuan+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F336%2F7530%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Jianhao+Yuan%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F336%2F7530%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Jianhao+Yuan%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F336%2F7530%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F336%2F7530%3E+%7D+.%0A%0A%7D)

_showing all20 records_

20162026102022: 12023: 32023: 32024: 122024: 122024: 122025: 32025: 32026: 1

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

- ![](https://dblp.org/img/add-mark.12x12.png)Philip Torr 0001 (9)
- ![](https://dblp.org/img/add-mark.12x12.png)Bo Zhao 0037 (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Shuyang Sun (7)
- ![](https://dblp.org/img/add-mark.12x12.png)Paul Newman 0001 (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Francesco Pinto (5)
- ![](https://dblp.org/img/add-mark.12x12.png)Matthew Gadd (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Adam Davies (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Lars Kunze (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Nicolas Beltran-Velez (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Tom A. Lamb (2)

- _40 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (20)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (13)
- ![](https://dblp.org/img/add-mark.12x12.png)ICML (1)
- ![](https://dblp.org/img/add-mark.12x12.png)PMLR (1)
- ![](https://dblp.org/img/add-mark.12x12.png)NeurIPS (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Trans. Mach. Learn. Res. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IROS (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ICLR (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ICRA (1)
- ![](https://dblp.org/img/add-mark.12x12.png)RSS (1)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)open (17)
- ![](https://dblp.org/img/add-mark.12x12.png)closed (3)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[i13\]
Jianhao Yuan, [Xiaofeng Zhang](https://dblp.org/pid/61/3976.html), [Felix Friedrich](https://dblp.org/pid/18/4626.html), [Nicolas Beltran-Velez](https://dblp.org/pid/376/9930.html), [Melissa Hall](https://dblp.org/pid/287/5067.html), [Reyhane Askari Hemmat](https://dblp.org/pid/190/7658.html), [Xiaochuang Han](https://dblp.org/pid/216/6755.html), [Nicolas Ballas](https://dblp.org/pid/120/9066.html), [Michal Drozdzal](https://dblp.org/pid/24/9794.html), [Adriana Romero-Soriano](https://dblp.org/pid/235/5885.html):

Inference-time Physics Alignment of Video Generative Models with Latent World Models. [CoRRabs/2601.10553](https://dblp.org/db/journals/corr/corr2601.html#journals/corr/abs-2601-10553) (2026)
- 2025
- ![](https://dblp.org/img/n.png)

\[c6\]
[Wenxiao Cai](https://dblp.org/pid/348/4892.html), [Iaroslav Ponomarenko](https://dblp.org/pid/372/4375.html), Jianhao Yuan, [Xiaoqi Li](https://dblp.org/pid/357/1937.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Hao Dong](https://dblp.org/pid/14/1525-3.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html):

SpatialBot: Precise Spatial Understanding with Vision Language Models. [ICRA2025](https://dblp.org/db/conf/icra/icra2025.html#conf/icra/CaiPYLYDZ25): 9490-9498
- ![](https://dblp.org/img/n.png)

\[i12\]
Jianhao Yuan, [Fabio Pizzati](https://dblp.org/pid/241/5366.html), [Francesco Pinto](https://dblp.org/pid/281/7477.html), [Lars Kunze](https://dblp.org/pid/20/8428.html), [Ivan Laptev](https://dblp.org/pid/41/1854.html), [Paul Newman](https://dblp.org/pid/79/1187-1.html), [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Daniele De Martini](https://dblp.org/pid/14/8216.html):

LikePhys: Evaluating Intuitive Physics Understanding in Video Diffusion Models via Likelihood Preference. [CoRRabs/2510.11512](https://dblp.org/db/journals/corr/corr2510.html#journals/corr/abs-2510-11512) (2025)
- ![](https://dblp.org/img/n.png)

\[i11\]
Jianhao Yuan, [Xiaofeng Zhang](https://dblp.org/pid/61/3976.html), [Felix Friedrich](https://dblp.org/pid/18/4626.html), [Nicolas Beltran-Velez](https://dblp.org/pid/376/9930.html), [Melissa Hall](https://dblp.org/pid/287/5067.html), [Reyhane Askari Hemmat](https://dblp.org/pid/190/7658.html), [Xiaochuang Han](https://dblp.org/pid/216/6755.html), [Nicolas Ballas](https://dblp.org/pid/120/9066.html), [Michal Drozdzal](https://dblp.org/pid/24/9794.html), [Adriana Romero-Soriano](https://dblp.org/pid/235/5885.html):

Improving the Physics of Video Generation with VJEPA-2 Reward Signal. [CoRRabs/2510.21840](https://dblp.org/db/journals/corr/corr2510.html#journals/corr/abs-2510-21840) (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j1\]
[Zhongrui Gui](https://dblp.org/pid/375/1465.html), [Shuyang Sun](https://dblp.org/pid/40/504.html), [Runjia Li](https://dblp.org/pid/352/5264.html), Jianhao Yuan, [Zhaochong An](https://dblp.org/pid/274/7063.html), [Karsten Roth](https://dblp.org/pid/234/7803.html), [Ameya Prabhu](https://dblp.org/pid/181/4512.html), [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html):

kNN-CLIP: Retrieval Enables Training-Free Segmentation on Continually Expanding Large Vocabularies. [Trans. Mach. Learn. Res.2024](https://dblp.org/db/journals/tmlr/tmlr2024.html#journals/tmlr/GuiSLYARP024) (2024)
- ![](https://dblp.org/img/n.png)

\[c5\]
Jianhao Yuan, [Jie Zhang](https://dblp.org/pid/84/6889-50.html), [Shuyang Sun](https://dblp.org/pid/40/504.html), [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html):

Real-Fake: Effective Training Data Synthesis Through Distribution Matching. [ICLR2024](https://dblp.org/db/conf/iclr/iclr2024.html#conf/iclr/YuanZS0Z24)
- ![](https://dblp.org/img/n.png)

\[c4\]
Jianhao Yuan, [Francesco Pinto](https://dblp.org/pid/281/7477.html), [Adam Davies](https://dblp.org/pid/42/8281.html), [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html):

Not Just Pretty Pictures: Toward Interventional Data Augmentation Using Text-to-Image Generators. [ICML2024](https://dblp.org/db/conf/icml/icml2024.html#conf/icml/YuanPD024): 57924-57952
- ![](https://dblp.org/img/n.png)

\[c3\]
[Arshia Hemmat](https://dblp.org/pid/393/1859.html), [Adam Davies](https://dblp.org/pid/42/8281.html), [Tom A. Lamb](https://dblp.org/pid/348/9410.html), Jianhao Yuan, [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Ashkan Khakzar](https://dblp.org/pid/201/0889.html), [Francesco Pinto](https://dblp.org/pid/281/7477.html):

Hidden in Plain Sight: Evaluating Abstract Shape Recognition in Vision-Language Models. [NeurIPS2024](https://dblp.org/db/conf/nips/neurips2024.html#conf/nips/HemmatDLY0KP24)
- ![](https://dblp.org/img/n.png)

\[c2\]
Jianhao Yuan, [Shuyang Sun](https://dblp.org/pid/40/504.html), [Daniel Omeiza](https://dblp.org/pid/230/3471.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html), [Paul Newman](https://dblp.org/pid/79/1187-1.html), [Lars Kunze](https://dblp.org/pid/20/8428.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Matthew Gadd](https://dblp.org/pid/164/8450.html):

RAG-Driver: Generalisable Driving Explanations with Retrieval-Augmented In-Context Multi-Modal Large Language Model Learning. [Robotics: Science and Systems2024](https://dblp.org/db/conf/rss/rss2024.html#conf/rss/YuanSOZ0KG24)
- ![](https://dblp.org/img/n.png)

\[i10\]
Jianhao Yuan, [Shuyang Sun](https://dblp.org/pid/40/504.html), [Daniel Omeiza](https://dblp.org/pid/230/3471.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html), [Paul Newman](https://dblp.org/pid/79/1187-1.html), [Lars Kunze](https://dblp.org/pid/20/8428.html), [Matthew Gadd](https://dblp.org/pid/164/8450.html):

RAG-Driver: Generalisable Driving Explanations with Retrieval-Augmented In-Context Learning in Multi-Modal Large Language Model. [CoRRabs/2402.10828](https://dblp.org/db/journals/corr/corr2402.html#journals/corr/abs-2402-10828) (2024)
- ![](https://dblp.org/img/n.png)

\[i9\]
[Muyang He](https://dblp.org/pid/192/6181.html), [Yexin Liu](https://dblp.org/pid/255/8704.html), [Boya Wu](https://dblp.org/pid/149/1290.html), Jianhao Yuan, [Yueze Wang](https://dblp.org/pid/335/2676.html), [Tiejun Huang](https://dblp.org/pid/h/TiejunHuang.html), [Bo Zhao](https://dblp.org/pid/94/4810-15.html):

Efficient Multimodal Learning from Data-centric Perspective. [CoRRabs/2402.11530](https://dblp.org/db/journals/corr/corr2402.html#journals/corr/abs-2402-11530) (2024)
- ![](https://dblp.org/img/n.png)

\[i8\]
[Bin Cao](https://dblp.org/pid/17/1169.html), Jianhao Yuan, [Yexin Liu](https://dblp.org/pid/255/8704.html), [Jian Li](https://dblp.org/pid/33/5448.html), [Shuyang Sun](https://dblp.org/pid/40/504.html), [Jing Liu](https://dblp.org/pid/72/2590-1.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html):

SynArtifact: Classifying and Alleviating Artifacts in Synthetic Images via Vision-Language Model. [CoRRabs/2402.18068](https://dblp.org/db/journals/corr/corr2402.html#journals/corr/abs-2402-18068) (2024)
- ![](https://dblp.org/img/n.png)

\[i7\]
[Zhongrui Gui](https://dblp.org/pid/375/1465.html), [Shuyang Sun](https://dblp.org/pid/40/504.html), [Runjia Li](https://dblp.org/pid/352/5264.html), Jianhao Yuan, [Zhaochong An](https://dblp.org/pid/274/7063.html), [Karsten Roth](https://dblp.org/pid/234/7803.html), [Ameya Prabhu](https://dblp.org/pid/181/4512.html), [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html):

kNN-CLIP: Retrieval Enables Training-Free Segmentation on Continually Expanding Large Vocabularies. [CoRRabs/2404.09447](https://dblp.org/db/journals/corr/corr2404.html#journals/corr/abs-2404-09447) (2024)
- ![](https://dblp.org/img/n.png)

\[i6\]
[Yichen Ouyang](https://dblp.org/pid/345/0749.html), Jianhao Yuan, [Hao Zhao](https://dblp.org/pid/08/3737.html), [Gaoang Wang](https://dblp.org/pid/176/7523.html), [Bo Zhao](https://dblp.org/pid/94/4810-10.html):

FlexiFilm: Long Video Generation with Flexible Conditions. [CoRRabs/2404.18620](https://dblp.org/db/journals/corr/corr2404.html#journals/corr/abs-2404-18620) (2024)
- ![](https://dblp.org/img/n.png)

\[i5\]
[Wenxiao Cai](https://dblp.org/pid/348/4892.html), [Yaroslav Ponomarenko](https://dblp.org/pid/380/2248.html), Jianhao Yuan, [Xiaoqi Li](https://dblp.org/pid/357/1937.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Hao Dong](https://dblp.org/pid/14/1525-3.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html):

SpatialBot: Precise Spatial Understanding with Vision Language Models. [CoRRabs/2406.13642](https://dblp.org/db/journals/corr/corr2406.html#journals/corr/abs-2406-13642) (2024)
- ![](https://dblp.org/img/n.png)

\[i4\]
[Arshia Hemmat](https://dblp.org/pid/393/1859.html), [Adam Davies](https://dblp.org/pid/42/8281.html), [Tom A. Lamb](https://dblp.org/pid/348/9410.html), Jianhao Yuan, [Philip Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Ashkan Khakzar](https://dblp.org/pid/201/0889.html), [Francesco Pinto](https://dblp.org/pid/281/7477.html):

Hidden in Plain Sight: Evaluating Abstract Shape Recognition in Vision-Language Models. [CoRRabs/2411.06287](https://dblp.org/db/journals/corr/corr2411.html#journals/corr/abs-2411-06287) (2024)
- 2023
- ![](https://dblp.org/img/n.png)

\[c1\]
Jianhao Yuan, [Paul Newman](https://dblp.org/pid/79/1187-1.html), [Matthew Gadd](https://dblp.org/pid/164/8450.html):

Off the Radar: Uncertainty-Aware Radar Place Recognition with Introspective Querying and Map Maintenance. [IROS2023](https://dblp.org/db/conf/iros/iros2023.html#conf/iros/Yuan0G23): 1350-1357
- ![](https://dblp.org/img/n.png)

\[i3\]
Jianhao Yuan, [Paul Newman](https://dblp.org/pid/79/1187-1.html), [Matthew Gadd](https://dblp.org/pid/164/8450.html):

Off the Radar: Uncertainty-Aware Radar Place Recognition with Introspective Querying and Map Maintenance. [CoRRabs/2306.12556](https://dblp.org/db/journals/corr/corr2306.html#journals/corr/abs-2306-12556) (2023)
- ![](https://dblp.org/img/n.png)

\[i2\]
Jianhao Yuan, [Jie Zhang](https://dblp.org/pid/84/6889-50.html), [Shuyang Sun](https://dblp.org/pid/40/504.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Bo Zhao](https://dblp.org/pid/94/4810-37.html):

Real-Fake: Effective Training Data Synthesis Through Distribution Matching. [CoRRabs/2310.10402](https://dblp.org/db/journals/corr/corr2310.html#journals/corr/abs-2310-10402) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[i1\]
Jianhao Yuan, [Francesco Pinto](https://dblp.org/pid/281/7477.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Adam Davies](https://dblp.org/pid/42/8281.html), [Aarushi Gupta](https://dblp.org/pid/294/6515.html), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html):

Not Just Pretty Pictures: Text-to-Image Generators Enable Interpretable Interventions for Robust Representations. [CoRRabs/2212.11237](https://dblp.org/db/journals/corr/corr2212.html#journals/corr/abs-2212-11237) (2022)
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/336/7530.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Zhaochong An](https://dblp.org/pid/274/7063.html)

[\[j1\]](https://dblp.org/pid/336/7530.html#j1) [\[i7\]](https://dblp.org/pid/336/7530.html#i7)

[2](https://dblp.org/pid/336/7530.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Nicolas Ballas](https://dblp.org/pid/120/9066.html)

[\[i13\]](https://dblp.org/pid/336/7530.html#i13) [\[i11\]](https://dblp.org/pid/336/7530.html#i11)

[3](https://dblp.org/pid/336/7530.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Nicolas Beltran-Velez](https://dblp.org/pid/376/9930.html)

[\[i13\]](https://dblp.org/pid/336/7530.html#i13) [\[i11\]](https://dblp.org/pid/336/7530.html#i11)

[4](https://dblp.org/pid/336/7530.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Wenxiao Cai](https://dblp.org/pid/348/4892.html)

[\[c6\]](https://dblp.org/pid/336/7530.html#c6) [\[i5\]](https://dblp.org/pid/336/7530.html#i5)

[5](https://dblp.org/pid/336/7530.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Bin Cao](https://dblp.org/pid/17/1169.html)

[\[i8\]](https://dblp.org/pid/336/7530.html#i8)

[6](https://dblp.org/pid/336/7530.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Adam Davies](https://dblp.org/pid/42/8281.html)

[\[c4\]](https://dblp.org/pid/336/7530.html#c4) [\[c3\]](https://dblp.org/pid/336/7530.html#c3) [\[i4\]](https://dblp.org/pid/336/7530.html#i4) [\[i1\]](https://dblp.org/pid/336/7530.html#i1)

[7](https://dblp.org/pid/336/7530.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Hao Dong 0003](https://dblp.org/pid/14/1525-3.html)

[\[c6\]](https://dblp.org/pid/336/7530.html#c6) [\[i5\]](https://dblp.org/pid/336/7530.html#i5)

[8](https://dblp.org/pid/336/7530.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Michal Drozdzal](https://dblp.org/pid/24/9794.html)

[\[i13\]](https://dblp.org/pid/336/7530.html#i13) [\[i11\]](https://dblp.org/pid/336/7530.html#i11)

[9](https://dblp.org/pid/336/7530.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Felix Friedrich](https://dblp.org/pid/18/4626.html)

[\[i13\]](https://dblp.org/pid/336/7530.html#i13) [\[i11\]](https://dblp.org/pid/336/7530.html#i11)

[10](https://dblp.org/pid/336/7530.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Matthew Gadd](https://dblp.org/pid/164/8450.html)

[\[c2\]](https://dblp.org/pid/336/7530.html#c2) [\[i10\]](https://dblp.org/pid/336/7530.html#i10) [\[c1\]](https://dblp.org/pid/336/7530.html#c1) [\[i3\]](https://dblp.org/pid/336/7530.html#i3)

[11](https://dblp.org/pid/336/7530.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Zhongrui Gui](https://dblp.org/pid/375/1465.html)

[\[j1\]](https://dblp.org/pid/336/7530.html#j1) [\[i7\]](https://dblp.org/pid/336/7530.html#i7)

[12](https://dblp.org/pid/336/7530.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Aarushi Gupta](https://dblp.org/pid/294/6515.html)

[\[i1\]](https://dblp.org/pid/336/7530.html#i1)

[13](https://dblp.org/pid/336/7530.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Melissa Hall](https://dblp.org/pid/287/5067.html)

[\[i13\]](https://dblp.org/pid/336/7530.html#i13) [\[i11\]](https://dblp.org/pid/336/7530.html#i11)

[14](https://dblp.org/pid/336/7530.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Xiaochuang Han](https://dblp.org/pid/216/6755.html)

[\[i13\]](https://dblp.org/pid/336/7530.html#i13) [\[i11\]](https://dblp.org/pid/336/7530.html#i11)

[15](https://dblp.org/pid/336/7530.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Muyang He](https://dblp.org/pid/192/6181.html)

[\[i9\]](https://dblp.org/pid/336/7530.html#i9)

[16](https://dblp.org/pid/336/7530.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Arshia Hemmat](https://dblp.org/pid/393/1859.html)

[\[c3\]](https://dblp.org/pid/336/7530.html#c3) [\[i4\]](https://dblp.org/pid/336/7530.html#i4)

[17](https://dblp.org/pid/336/7530.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Reyhane Askari Hemmat](https://dblp.org/pid/190/7658.html)

[\[i13\]](https://dblp.org/pid/336/7530.html#i13) [\[i11\]](https://dblp.org/pid/336/7530.html#i11)

[18](https://dblp.org/pid/336/7530.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Tiejun Huang 0001](https://dblp.org/pid/h/TiejunHuang.html)

[\[i9\]](https://dblp.org/pid/336/7530.html#i9)

[19](https://dblp.org/pid/336/7530.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Ashkan Khakzar](https://dblp.org/pid/201/0889.html)

[\[c3\]](https://dblp.org/pid/336/7530.html#c3) [\[i4\]](https://dblp.org/pid/336/7530.html#i4)

[20](https://dblp.org/pid/336/7530.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Lars Kunze](https://dblp.org/pid/20/8428.html)

[\[i12\]](https://dblp.org/pid/336/7530.html#i12) [\[c2\]](https://dblp.org/pid/336/7530.html#c2) [\[i10\]](https://dblp.org/pid/336/7530.html#i10)

[21](https://dblp.org/pid/336/7530.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Tom A. Lamb](https://dblp.org/pid/348/9410.html)

[\[c3\]](https://dblp.org/pid/336/7530.html#c3) [\[i4\]](https://dblp.org/pid/336/7530.html#i4)

[22](https://dblp.org/pid/336/7530.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Ivan Laptev](https://dblp.org/pid/41/1854.html)

[\[i12\]](https://dblp.org/pid/336/7530.html#i12)

[23](https://dblp.org/pid/336/7530.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Jian Li](https://dblp.org/pid/33/5448.html)

[\[i8\]](https://dblp.org/pid/336/7530.html#i8)

[24](https://dblp.org/pid/336/7530.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Runjia Li](https://dblp.org/pid/352/5264.html)

[\[j1\]](https://dblp.org/pid/336/7530.html#j1) [\[i7\]](https://dblp.org/pid/336/7530.html#i7)

[25](https://dblp.org/pid/336/7530.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Xiaoqi Li 0020](https://dblp.org/pid/357/1937.html)

[\[c6\]](https://dblp.org/pid/336/7530.html#c6) [\[i5\]](https://dblp.org/pid/336/7530.html#i5)

[26](https://dblp.org/pid/336/7530.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Jing Liu 0001](https://dblp.org/pid/72/2590-1.html)

[\[i8\]](https://dblp.org/pid/336/7530.html#i8)

[27](https://dblp.org/pid/336/7530.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Yexin Liu](https://dblp.org/pid/255/8704.html)

[\[i9\]](https://dblp.org/pid/336/7530.html#i9) [\[i8\]](https://dblp.org/pid/336/7530.html#i8)

[28](https://dblp.org/pid/336/7530.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Daniele De Martini](https://dblp.org/pid/14/8216.html)

[\[i12\]](https://dblp.org/pid/336/7530.html#i12)

[29](https://dblp.org/pid/336/7530.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Paul Newman 0001](https://dblp.org/pid/79/1187-1.html)

[\[i12\]](https://dblp.org/pid/336/7530.html#i12) [\[c2\]](https://dblp.org/pid/336/7530.html#c2) [\[i10\]](https://dblp.org/pid/336/7530.html#i10) [\[c1\]](https://dblp.org/pid/336/7530.html#c1) [\[i3\]](https://dblp.org/pid/336/7530.html#i3)

[30](https://dblp.org/pid/336/7530.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Daniel Omeiza](https://dblp.org/pid/230/3471.html)

[\[c2\]](https://dblp.org/pid/336/7530.html#c2) [\[i10\]](https://dblp.org/pid/336/7530.html#i10)

[31](https://dblp.org/pid/336/7530.html?view=joint&param=31 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=2)

[Yichen Ouyang](https://dblp.org/pid/345/0749.html)

[\[i6\]](https://dblp.org/pid/336/7530.html#i6)

[32](https://dblp.org/pid/336/7530.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Francesco Pinto](https://dblp.org/pid/281/7477.html)

[\[i12\]](https://dblp.org/pid/336/7530.html#i12) [\[c4\]](https://dblp.org/pid/336/7530.html#c4) [\[c3\]](https://dblp.org/pid/336/7530.html#c3) [\[i4\]](https://dblp.org/pid/336/7530.html#i4) [\[i1\]](https://dblp.org/pid/336/7530.html#i1)

[33](https://dblp.org/pid/336/7530.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Fabio Pizzati](https://dblp.org/pid/241/5366.html)

[\[i12\]](https://dblp.org/pid/336/7530.html#i12)

[34](https://dblp.org/pid/336/7530.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Iaroslav Ponomarenko](https://dblp.org/pid/372/4375.html)

[\[c6\]](https://dblp.org/pid/336/7530.html#c6)

[35](https://dblp.org/pid/336/7530.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Yaroslav Ponomarenko](https://dblp.org/pid/380/2248.html)

[\[i5\]](https://dblp.org/pid/336/7530.html#i5)

[36](https://dblp.org/pid/336/7530.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Ameya Prabhu](https://dblp.org/pid/181/4512.html)

[\[j1\]](https://dblp.org/pid/336/7530.html#j1) [\[i7\]](https://dblp.org/pid/336/7530.html#i7)

[37](https://dblp.org/pid/336/7530.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Adriana Romero-Soriano](https://dblp.org/pid/235/5885.html)

[\[i13\]](https://dblp.org/pid/336/7530.html#i13) [\[i11\]](https://dblp.org/pid/336/7530.html#i11)

[38](https://dblp.org/pid/336/7530.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Karsten Roth](https://dblp.org/pid/234/7803.html)

[\[j1\]](https://dblp.org/pid/336/7530.html#j1) [\[i7\]](https://dblp.org/pid/336/7530.html#i7)

[39](https://dblp.org/pid/336/7530.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Shuyang Sun](https://dblp.org/pid/40/504.html)

[\[j1\]](https://dblp.org/pid/336/7530.html#j1) [\[c5\]](https://dblp.org/pid/336/7530.html#c5) [\[c2\]](https://dblp.org/pid/336/7530.html#c2) [\[i10\]](https://dblp.org/pid/336/7530.html#i10) [\[i8\]](https://dblp.org/pid/336/7530.html#i8) [\[i7\]](https://dblp.org/pid/336/7530.html#i7) [\[i2\]](https://dblp.org/pid/336/7530.html#i2)

[40](https://dblp.org/pid/336/7530.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[i12\]](https://dblp.org/pid/336/7530.html#i12) [\[j1\]](https://dblp.org/pid/336/7530.html#j1) [\[c5\]](https://dblp.org/pid/336/7530.html#c5) [\[c4\]](https://dblp.org/pid/336/7530.html#c4) [\[c3\]](https://dblp.org/pid/336/7530.html#c3) [\[i7\]](https://dblp.org/pid/336/7530.html#i7) [\[i4\]](https://dblp.org/pid/336/7530.html#i4) [\[i2\]](https://dblp.org/pid/336/7530.html#i2) [\[i1\]](https://dblp.org/pid/336/7530.html#i1)

[41](https://dblp.org/pid/336/7530.html?view=joint&param=41 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=2)

[Gaoang Wang](https://dblp.org/pid/176/7523.html)

[\[i6\]](https://dblp.org/pid/336/7530.html#i6)

[42](https://dblp.org/pid/336/7530.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Yueze Wang](https://dblp.org/pid/335/2676.html)

[\[i9\]](https://dblp.org/pid/336/7530.html#i9)

[43](https://dblp.org/pid/336/7530.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Boya Wu](https://dblp.org/pid/149/1290.html)

[\[i9\]](https://dblp.org/pid/336/7530.html#i9)

[44](https://dblp.org/pid/336/7530.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c6\]](https://dblp.org/pid/336/7530.html#c6) [\[i5\]](https://dblp.org/pid/336/7530.html#i5)

[45](https://dblp.org/pid/336/7530.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Jie Zhang 0050](https://dblp.org/pid/84/6889-50.html)

[\[c5\]](https://dblp.org/pid/336/7530.html#c5) [\[i2\]](https://dblp.org/pid/336/7530.html#i2)

[46](https://dblp.org/pid/336/7530.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Xiaofeng Zhang](https://dblp.org/pid/61/3976.html)

[\[i13\]](https://dblp.org/pid/336/7530.html#i13) [\[i11\]](https://dblp.org/pid/336/7530.html#i11)

[47](https://dblp.org/pid/336/7530.html?view=joint&param=47 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=2)

[Bo Zhao 0010](https://dblp.org/pid/94/4810-10.html)

[\[i6\]](https://dblp.org/pid/336/7530.html#i6)

[48](https://dblp.org/pid/336/7530.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Bo Zhao 0015](https://dblp.org/pid/94/4810-15.html)

[\[i9\]](https://dblp.org/pid/336/7530.html#i9)

[49](https://dblp.org/pid/336/7530.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=1)

[Bo Zhao 0037](https://dblp.org/pid/94/4810-37.html)

[\[c6\]](https://dblp.org/pid/336/7530.html#c6) [\[c5\]](https://dblp.org/pid/336/7530.html#c5) [\[c2\]](https://dblp.org/pid/336/7530.html#c2) [\[i10\]](https://dblp.org/pid/336/7530.html#i10) [\[i8\]](https://dblp.org/pid/336/7530.html#i8) [\[i5\]](https://dblp.org/pid/336/7530.html#i5) [\[i2\]](https://dblp.org/pid/336/7530.html#i2)

[50](https://dblp.org/pid/336/7530.html?view=joint&param=50 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/336/7530.html?view=group&param=2)

[Hao Zhao](https://dblp.org/pid/08/3737.html)

[\[i6\]](https://dblp.org/pid/336/7530.html#i6)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/336/7530.html#) [\[–\]](https://dblp.org/pid/336/7530.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/336/7530.html#) [\[–\]](https://dblp.org/pid/336/7530.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/336/7530.html#) [\[–\]](https://dblp.org/pid/336/7530.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/336/7530.html#) [\[–\]](https://dblp.org/pid/336/7530.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/336/7530.html#) [\[–\]](https://dblp.org/pid/336/7530.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)