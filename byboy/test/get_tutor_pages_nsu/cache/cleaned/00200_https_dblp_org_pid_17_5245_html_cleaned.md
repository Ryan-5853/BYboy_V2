> 抓取来源：https://dblp.org/pid/17/5245.html

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

This is just a _disambiguation page_, and is not intended to be the bibliography of an actual person. The links to all actual bibliographies of persons of the same or a similar name can be found below. Any publication listed on this page has not been assigned to an actual author yet. If you know the true author of one of the publications listed below, you are welcome to [contact us.](https://dblp.org/db/about/team.html)

- [Haifeng Zhao 0001](https://dblp.org/pid/17/5245-1.html)![[0000-0002-5300-0683]](https://dblp.org/img/orcid-mark.12x12.png) — Anhui University, School of Computer Science and Technology, China
- [Haifeng Zhao 0002](https://dblp.org/pid/17/5245-2.html)![[0000-0002-5196-4921]](https://dblp.org/img/orcid-mark.12x12.png) — Jinling Institute of Technology, School of Software Engineering, Nanjing, China (and 1 more)
- [Haifeng Zhao 0003](https://dblp.org/pid/17/5245-3.html)![[0000-0002-3051-6417]](https://dblp.org/img/orcid-mark.12x12.png) — University of Melbourne, Department of Infrastructure Engineering, VIC, Australia
- [Haifeng Zhao 0004](https://dblp.org/pid/17/5245-4.html) — University of California, Davis, Computer Science Department, CA, USA

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Haifeng+Zhao%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F17%2F5245%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Haifeng+Zhao+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F17%2F5245%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Haifeng+Zhao+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F17%2F5245%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Haifeng+Zhao%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F17%2F5245%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Haifeng+Zhao+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F17%2F5245%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Haifeng+Zhao%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F17%2F5245%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Haifeng+Zhao%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F17%2F5245%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F17%2F5245%3E+%7D+.%0A%0A%7D)

_showing all56 records_

2007202652007: 22008: 42008: 42010: 22010: 22011: 32011: 32012: 32012: 32013: 32013: 32014: 32014: 32016: 22017: 22019: 32019: 32020: 22020: 22021: 12022: 32022: 32023: 92023: 92024: 42024: 42025: 92025: 92025: 92026: 1

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

- ![](https://dblp.org/img/add-mark.12x12.png)Lan Du 0002 (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Ruinan Mu (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Xiaomin Mu (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Omid Kavehei (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Alistair Lee McEwan (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Zhibin Pan (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Yuan Tian 0016 (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Shulin Liu (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Jianrong Wang (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Bo Cheng (2)

- _163 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (53)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0001-7730-6890 (1)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0001-5761-4941 (1)
- ![](https://dblp.org/img/add-mark.12x12.png)0000-0003-4234-5894 (1)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)SITIS (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Sensors (2)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (2)
- ![](https://dblp.org/img/add-mark.12x12.png)ADMA (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Wirel. Pers. Commun. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)IET Wirel. Sens. Syst. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ISSPA (1)
- ![](https://dblp.org/img/add-mark.12x12.png)J. Appl. Math. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)Microelectron. J. (1)

- _42 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (46)
- ![](https://dblp.org/img/add-mark.12x12.png)open (10)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[j26\]
Haifeng Zhao, [Xiangbo Zhao](https://dblp.org/pid/425/9748.html), [Xuan Zhang](https://dblp.org/pid/36/31.html), [Wenjuan Du](https://dblp.org/pid/246/2632.html), [Tianmin Zhang](https://dblp.org/pid/425/9858.html), [Hao Zhang](https://dblp.org/pid/55/2270.html):

Application of VIBE sequences for visualization and assessing cartilaginous endplate damage in low back pain patients. [BMC Medical Imaging26(1)](https://dblp.org/db/journals/bmcmi/bmcmi26.html#journals/bmcmi/ZhaoZZDZZ26): 23 (2026)
- 2025
- ![](https://dblp.org/img/n.png)

\[j25\]
[Yao Zeng](https://dblp.org/pid/76/2826.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zheng Sun](https://dblp.org/pid/36/2849.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Mengfei Wang](https://dblp.org/pid/253/2113.html), [Zhuo Li](https://dblp.org/pid/51/4015.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ao Liu](https://dblp.org/pid/182/7579.html), [Meixiu Pan](https://dblp.org/pid/413/9763.html), Haifeng Zhao, [Yuehua Li](https://dblp.org/pid/145/2817.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Expanding point cloud statistical shape model applications: Generalized vascular modeling for population-level hemodynamic simulations. [Comput. Methods Programs Biomed.269](https://dblp.org/db/journals/cmpb/cmpb269.html#journals/cmpb/ZengSWLLPZL25): 108924 (2025)
- ![](https://dblp.org/img/n.png)

\[j24\]
[Ziying Li](https://dblp.org/pid/142/6230.html), Haifeng Zhao, [Hiromitsu Nishizaki](https://dblp.org/pid/87/1050.html), [Chee Siang Leow](https://dblp.org/pid/232/2856.html), [Xingfa Shen](https://dblp.org/pid/07/4044.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Chinese Character Recognition based on Swin Transformer-Encoder. [Digit. Signal Process.161](https://dblp.org/db/journals/dsp/dsp161.html#journals/dsp/LiZNLS25): 105080 (2025)
- ![](https://dblp.org/img/n.png)

\[j23\]
[Chengcheng Shen](https://dblp.org/pid/55/11102.html), Haifeng Zhao, [Jian Jiao](https://dblp.org/pid/29/265.html):

A multi-subnets physics-informed neural network (Ms-PINN) model for transient heat transfer analysis in materials with heterogeneous microstructures. [Eng. Comput.41(5)](https://dblp.org/db/journals/ewc/ewc41.html#journals/ewc/ShenZJ25): 3695-3717 (2025)
- ![](https://dblp.org/img/n.png)

\[j22\]
[Lizhi Pan](https://dblp.org/pid/133/5474.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhongyi Ding](https://dblp.org/pid/309/9697.html), Haifeng Zhao, [Ruinan Mu](https://dblp.org/pid/357/6815.html), [Jianmin Li](https://dblp.org/pid/71/5930.html):

Comparing on-line continuous movement decoding with joints unconstrained and constrained based on a generic musculoskeletal model. [Medical Biol. Eng. Comput.63(2)](https://dblp.org/db/journals/mbec/mbec63.html#journals/mbec/PanDZML25): 525-533 (2025)
- ![](https://dblp.org/img/n.png)

\[c28\]
[Jun Gao](https://dblp.org/pid/82/4977.html), Haifeng Zhao, [Guohao Zong](https://dblp.org/pid/402/4266.html), [Shunxiang Gao](https://dblp.org/pid/383/1897.html), [Yan Zhang](https://dblp.org/pid/04/3348.html), [Lan Du](https://dblp.org/pid/98/1504-2.html):

MoleNovo: A Casanovo-Based De Novo Molecular Generation Framework. [ADMA (3)2025](https://dblp.org/db/conf/adma/adma2025-3.html#conf/adma/GaoZZGZD25): 97-111
- ![](https://dblp.org/img/n.png)

\[c27\]
[Wei Tan](https://dblp.org/pid/73/6520.html), [Dan Nguyen](https://dblp.org/pid/62/1355.html), [Chen Li](https://dblp.org/pid/164/3294.html), [Wray L. Buntine](https://dblp.org/pid/72/3885.html), Haifeng Zhao, [Lan Du](https://dblp.org/pid/98/1504-2.html):

Leveraging Deep AUC Maximisation for Enhanced Active Learning in Named Entity Recognition. [ADMA (2)2025](https://dblp.org/db/conf/adma/adma2025-2.html#conf/adma/TanNLBZD25): 287-302
- ![](https://dblp.org/img/n.png)

\[c26\]
[Bo Cheng](https://dblp.org/pid/05/2700.html), [Jueqing Lu](https://dblp.org/pid/276/5821.html), [Yuan Tian](https://dblp.org/pid/39/5423-16.html), Haifeng Zhao, [Yi Chang](https://dblp.org/pid/02/5438.html), [Lan Du](https://dblp.org/pid/98/1504-2.html):

CGMatch: A Different Perspective of Semi-supervised Learning. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/ChengLTZ0D25): 15381-15391
- ![](https://dblp.org/img/n.png)

\[i2\]
[Xue Han](https://dblp.org/pid/17/6400.html), [Haodong Yao](https://dblp.org/pid/158/7464.html), [Fei Zhan](https://dblp.org/pid/142/3023.html), [Xueqi Song](https://dblp.org/pid/400/8968.html), [Junfang Zhao](https://dblp.org/pid/24/8626.html), Haifeng Zhao:

A new framework for X-ray absorption spectroscopy data analysis based on machine learning: XASDAML. [CoRRabs/2502.16665](https://dblp.org/db/journals/corr/corr2502.html#journals/corr/abs-2502-16665) (2025)
- ![](https://dblp.org/img/n.png)

\[i1\]
[Bo Cheng](https://dblp.org/pid/05/2700.html), [Jueqing Lu](https://dblp.org/pid/276/5821.html), [Yuan Tian](https://dblp.org/pid/39/5423-16.html), Haifeng Zhao, [Yi Chang](https://dblp.org/pid/02/5438.html), [Lan Du](https://dblp.org/pid/98/1504-2.html):

CGMatch: A Different Perspective of Semi-supervised Learning. [CoRRabs/2503.02231](https://dblp.org/db/journals/corr/corr2503.html#journals/corr/abs-2503-02231) (2025)
- 2024
- ![](https://dblp.org/img/n.png)

\[j21\]
[Zhaocai Wang](https://dblp.org/pid/91/3147.html), Haifeng Zhao, [Xiaoguang Bao](https://dblp.org/pid/87/719.html), [Tunhua Wu](https://dblp.org/pid/27/10618.html):

Multi-objective optimal allocation of water resources based on improved marine predator algorithm and entropy weighting method. [Earth Sci. Informatics17(2)](https://dblp.org/db/journals/esi/esi17.html#journals/esi/WangZBW24): 1483-1499 (2024)
- ![](https://dblp.org/img/n.png)

\[j20\]
[Lisha Yao](https://dblp.org/pid/225/7489.html)![](https://dblp.org/img/orcid-mark.12x12.png), Haifeng Zhao:

Correction to: Deep Learning Method of Facial Expression Recognition Based on Gabor Filter Bank Combined with PCNN. [Wirel. Pers. Commun.134(3)](https://dblp.org/db/journals/wpc/wpc134.html#journals/wpc/YaoZ24): 1915-1916 (2024)
- ![](https://dblp.org/img/n.png)

\[c25\]
[Chuhao Xu](https://dblp.org/pid/330/7863.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yiyu Liu](https://dblp.org/pid/263/7231.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zijun Li](https://dblp.org/pid/44/10301-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Quan Chen](https://dblp.org/pid/40/3858-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Han Zhao](https://dblp.org/pid/03/3520-5.html), [Deze Zeng](https://dblp.org/pid/08/5937.html), [Qian Peng](https://dblp.org/pid/67/6523.html), [Xueqi Wu](https://dblp.org/pid/200/2643.html), Haifeng Zhao![](https://dblp.org/img/orcid-mark.12x12.png), [Senbo Fu](https://dblp.org/pid/48/10194.html), [Minyi Guo](https://dblp.org/pid/99/6797.html):

FaaSMem: Improving Memory Efficiency of Serverless Computing with Memory Pool Architecture. [ASPLOS (3)2024](https://dblp.org/db/conf/asplos/asplos2024-3.html#conf/asplos/XuLLCZZPWZFG24): 331-348
- ![](https://dblp.org/img/n.png)

\[c24\]
[Lizhi Pan](https://dblp.org/pid/133/5474.html), [Zhongyi Ding](https://dblp.org/pid/309/9697.html), [Chengjun Li](https://dblp.org/pid/16/953.html), Haifeng Zhao, [Ruinan Mu](https://dblp.org/pid/357/6815.html), [Jianmin Li](https://dblp.org/pid/71/5930.html), [Jinhua Li](https://dblp.org/pid/73/5899.html):

Compensating for the Effect of Absence of Joint Movements in EMG-based Continuous Movement Decoding with a Deep Learning Approach. [M2VIP2024](https://dblp.org/db/conf/m2vip/m2vip2024.html#conf/m2vip/PanDLZMLL24): 1-6
- 2023
- ![](https://dblp.org/img/n.png)

\[j19\]
[Lei Shi](https://dblp.org/pid/29/563.html), [Yimin Zhou](https://dblp.org/pid/63/2223-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Juan Wang](https://dblp.org/pid/74/3634-17.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zuli Wang](https://dblp.org/pid/187/9462.html), [Ding Chen](https://dblp.org/pid/78/3806.html), Haifeng Zhao, [Wankou Yang](https://dblp.org/pid/99/3602.html), [Edward Szczerbicki](https://dblp.org/pid/25/345.html):

Compact global association based adaptive routing framework for personnel behavior understanding. [Future Gener. Comput. Syst.141](https://dblp.org/db/journals/fgcs/fgcs141.html#journals/fgcs/ShiZWWCZYS23): 514-525 (2023)
- ![](https://dblp.org/img/n.png)

\[j18\]
[Hebing Nie](https://dblp.org/pid/353/9606.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Qun Wu](https://dblp.org/pid/54/2083.html), Haifeng Zhao, [Weiping Ding](https://dblp.org/pid/133/0292-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Muhammet Deveci](https://dblp.org/pid/136/0546.html):

Flexible Adaptive Graph Embedding for Semi-supervised Dimension Reduction. [Inf. Fusion99](https://dblp.org/db/journals/inffus/inffus99.html#journals/inffus/NieWZDD23): 101872 (2023)
- ![](https://dblp.org/img/n.png)

\[j17\]
[Yuan Quan](https://dblp.org/pid/128/9916.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ke Wang](https://dblp.org/pid/181/2613-46.html), [Chong Zhao](https://dblp.org/pid/32/3558.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Congmin Lv](https://dblp.org/pid/217/4896.html), Haifeng Zhao, [Hongyu Lv](https://dblp.org/pid/301/5688.html):

Obstacle avoidance method for fixed trajectory of a seven-degree-of-freedom manipulator. [Robotica41(5)](https://dblp.org/db/journals/robotica/robotica41.html#journals/robotica/QuanWZLZL23): 1515-1535 (2023)
- ![](https://dblp.org/img/n.png)

\[j16\]
Haifeng Zhao, [Xiaorui Zhang](https://dblp.org/pid/97/7654.html), [Dengpan Jiang](https://dblp.org/pid/368/3709.html), [Jin Gu](https://dblp.org/pid/33/6358.html):

Research on Rotating Machinery Fault Diagnosis Based on an Improved Eulerian Video Motion Magnification. [Sensors23(23)](https://dblp.org/db/journals/sensors/sensors23.html#journals/sensors/ZhaoZJG23): 9582 (2023)
- ![](https://dblp.org/img/n.png)

\[j15\]
Haifeng Zhao![](https://dblp.org/img/orcid-mark.12x12.png), [Petra Karlsson](https://dblp.org/pid/205/6643.html), [Darryl Chiu](https://dblp.org/pid/355/2928.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Carter Sun](https://dblp.org/pid/355/3235.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Omid Kavehei](https://dblp.org/pid/41/9830.html), [Alistair Lee McEwan](https://dblp.org/pid/84/10611.html):

Wearable augmentative and alternative communication (wAAC): a novel solution for people with complex communication needs. [Virtual Real.27(3)](https://dblp.org/db/journals/vr/vr27.html#journals/vr/ZhaoKCSKM23): 2441-2459 (2023)
- ![](https://dblp.org/img/n.png)

\[j14\]
[Lisha Yao](https://dblp.org/pid/225/7489.html)![](https://dblp.org/img/orcid-mark.12x12.png), Haifeng Zhao:

Deep Learning Method of Facial Expression Recognition Based on Gabor Filter Bank Combined with PCNN. [Wirel. Pers. Commun.131(2)](https://dblp.org/db/journals/wpc/wpc131.html#journals/wpc/YaoZ23): 955-971 (2023)
- ![](https://dblp.org/img/n.png)

\[c23\]
Haifeng Zhao, [Ziyi Feng](https://dblp.org/pid/189/3855.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Shenglin Hao](https://dblp.org/pid/365/0421.html), [Huiling Tan](https://dblp.org/pid/81/7821.html), [Shikun Zhan](https://dblp.org/pid/291/5077.html), [Wei Liu](https://dblp.org/pid/49/3283.html), [Yong Lu](https://dblp.org/pid/72/2700.html), [Chunyan Cao](https://dblp.org/pid/137/6294.html):

A Virtual Reality (VR) based Comprehensive Freezing of Gait (FOG) Neuro-electrophysiologic Evaluation System for People with Parkinson's Disease (PD). [EMBC2023](https://dblp.org/db/conf/embc/embc2023.html#conf/embc/ZhaoFHTZLLC23): 1-5
- ![](https://dblp.org/img/n.png)

\[c22\]
[Hao Zeng](https://dblp.org/pid/59/6515.html), [Keyan Huo](https://dblp.org/pid/355/8709.html), [Yilun Hong](https://dblp.org/pid/263/9568.html), Haifeng Zhao:

Design and Analysis of an All-terrain Robotic Rover for Planetary Lava Tube Exploration. [ICARM2023](https://dblp.org/db/conf/icarm/icarm2023.html#conf/icarm/ZengHHZ23): 930-935
- ![](https://dblp.org/img/n.png)

\[c21\]
[Jiafeng Yang](https://dblp.org/pid/329/4050.html), [Xihan Li](https://dblp.org/pid/357/6957.html), [Zhibin Tian](https://dblp.org/pid/357/6837.html), [Zhiqiang Wang](https://dblp.org/pid/67/187.html), [Rujin Han](https://dblp.org/pid/357/7003.html), [Zihao Yuan](https://dblp.org/pid/198/1286.html), [Ruinan Mu](https://dblp.org/pid/357/6815.html), Haifeng Zhao:

Design of a Lunar Regolith Sampling System for Large-Scale Rover Traversals. [RCAR2023](https://dblp.org/db/conf/rcar/rcar2023.html#conf/rcar/YangLTWHYMZ23): 87-92
- 2022
- ![](https://dblp.org/img/n.png)

\[j13\]
[Ying Zhang](https://dblp.org/pid/13/6769.html), Haifeng Zhao:

A multi-agent model for decision making on environmental regulation in urban agglomeration. [J. Supercomput.78(4)](https://dblp.org/db/journals/tjs/tjs78.html#journals/tjs/ZhangZ22): 5588-5609 (2022)
- ![](https://dblp.org/img/n.png)

\[c20\]
[Haixia Zhao](https://dblp.org/pid/92/4900.html), Haifeng Zhao, [Yijie Zhang](https://dblp.org/pid/185/9892.html):

Petrophysical Properties and Seismic Wave Propagation of Loess Medium in Northwest China. [IGARSS2022](https://dblp.org/db/conf/igarss/igarss2022.html#conf/igarss/ZhaoZZ22): 6157-6160
- ![](https://dblp.org/img/n.png)

\[c19\]
[Zhixiang Chen](https://dblp.org/pid/332/6603.html), Haifeng Zhao, [Yan Zhang](https://dblp.org/pid/04/3348.html), [Guozi Sun](https://dblp.org/pid/91/1406.html), [Tianjian Wu](https://dblp.org/pid/332/6501.html):

Self-supervised Learning for Sketch-Based 3D Shape Retrieval. [PRCV (1)2022](https://dblp.org/db/conf/prcv/prcv2022-1.html#conf/prcv/ChenZZSW22): 318-329
- 2021
- ![](https://dblp.org/img/n.png)

\[c18\]
Haifeng Zhao, [Petra Karlsson](https://dblp.org/pid/205/6643.html), [Omid Kavehei](https://dblp.org/pid/41/9830.html), [Alistair Lee McEwan](https://dblp.org/pid/84/10611.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Augmentative and Alternative Communication with Eye-gaze Technology and Augmented Reality: Reflections from Engineers, People with Cerebral Palsy and Caregivers. [IEEE SENSORS2021](https://dblp.org/db/conf/ieeesensors/ieeesensors2021.html#conf/ieeesensors/ZhaoKKM21): 1-4
- 2020
- ![](https://dblp.org/img/n.png)

\[j12\]
[Raquib-ul Alam](https://dblp.org/pid/279/7503.html)![](https://dblp.org/img/orcid-mark.12x12.png), Haifeng Zhao, [Andrew J. Goodwin](https://dblp.org/pid/285/6212.html), [Omid Kavehei](https://dblp.org/pid/41/9830.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alistair Lee McEwan](https://dblp.org/pid/84/10611.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Differences in Power Spectral Densities and Phase Quantities Due to Processing of EEG Signals. [Sensors20(21)](https://dblp.org/db/journals/sensors/sensors20.html#journals/sensors/AlamZGKM20): 6285 (2020)
- ![](https://dblp.org/img/n.png)

\[c17\]
[Xiangdong Guo](https://dblp.org/pid/266/7083.html), Haifeng Zhao, [Zhenyu Tang](https://dblp.org/pid/72/4431.html):

An Improved Deep Learning Approach for Thyroid Nodule Diagnosis. [ISBI2020](https://dblp.org/db/conf/isbi/isbi2020.html#conf/isbi/GuoZT20): 296-299
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[j11\]
[Shuo Li](https://dblp.org/pid/49/595.html), [Song Li](https://dblp.org/pid/67/2580-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), Haifeng Zhao, [Yuan An](https://dblp.org/pid/54/323.html):

Design and implementation of state-of-charge estimation based on back-propagation neural network for smart uninterruptible power system. [Int. J. Distributed Sens. Networks15(12)](https://dblp.org/db/journals/ijdsn/ijdsn15.html#journals/ijdsn/LiLZA19) (2019)
- ![](https://dblp.org/img/n.png)

\[j10\]
[Feng Li](https://dblp.org/pid/92/2954-42.html), [Lixiang Xu](https://dblp.org/pid/09/10206.html), [Shihui Duan](https://dblp.org/pid/168/1893.html), [Wenfu Wu](https://dblp.org/pid/69/8546.html), Haifeng Zhao, [Qiang Ling](https://dblp.org/pid/99/4581-1.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Improving hierarchical mobile video caching through distributed cross-layer coordination. [Multim. Tools Appl.78(5)](https://dblp.org/db/journals/mta/mta78.html#journals/mta/LiXDWZL19): 6049-6071 (2019)
- ![](https://dblp.org/img/n.png)

\[c16\]
Haifeng Zhao, [Xingjun Wang](https://dblp.org/pid/82/3752.html):

Bi-Group Bayesian Personalized Ranking from Implicit Feedback. [CSSE2019](https://dblp.org/db/conf/csse/csse2019.html#conf/csse/ZhaoW19): 35-39
- 2017
- ![](https://dblp.org/img/n.png)

\[c15\]
Haifeng Zhao, [Weijia Jiang](https://dblp.org/pid/64/7674.html):

Research on the Growth of Engineering Science and Technology Talents from the Perspective of Complex Science. [GSKI (2)2017](https://dblp.org/db/conf/gski/gski2017-2.html#conf/gski/ZhaoJ17): 736-745
- ![](https://dblp.org/img/n.png)

\[c14\]
[Danyang Zhang](https://dblp.org/pid/87/1243.html), [Li Yao](https://dblp.org/pid/83/6976.html), Haifeng Zhao:

Signal Processing of Ultrasonic Testing of Hardened Layer Depth Based on Wavelet Transform Theory. [ICVIP2017](https://dblp.org/db/conf/icvip/icvip2017.html#conf/icvip/ZhangYZ17): 39-43
- 2016
- ![](https://dblp.org/img/n.png)

\[j9\]
Haifeng Zhao, [Zhibin Pan](https://dblp.org/pid/97/2574.html):

Distributed relay selection strategy based on physical-layer fairness for amplify-and-forward relaying systems. [IET Commun.10(17)](https://dblp.org/db/journals/iet-com/iet-com10.html#journals/iet-com/ZhaoP16): 2261-2268 (2016)
- ![](https://dblp.org/img/n.png)

\[j8\]
Haifeng Zhao, [Zhibin Pan](https://dblp.org/pid/97/2574.html):

Average relay transmit-power analysis in dual-hop amplify-and-forward relaying systems. [IET Wirel. Sens. Syst.6(6)](https://dblp.org/db/journals/iet-wss/iet-wss6.html#journals/iet-wss/ZhaoP16): 206-210 (2016)
- 2014
- ![](https://dblp.org/img/n.png)

\[j7\]
Haifeng Zhao, [Bin Lin](https://dblp.org/pid/11/1186-3.html), [Chongqing Guo](https://dblp.org/pid/146/8466.html):

A Mathematics Model for Quantitative Analysis of Demand Disruption Caused by Rumor Spreading. [Int. J. Inf. Technol. Decis. Mak.13(3)](https://dblp.org/db/journals/ijitdm/ijitdm13.html#journals/ijitdm/ZhaoLG14): 585-602 (2014)
- ![](https://dblp.org/img/n.png)

\[j6\]
Haifeng Zhao, [Bin Lin](https://dblp.org/pid/11/1186-3.html), [Wanqing Mao](https://dblp.org/pid/146/9288.html), [Yang Ye](https://dblp.org/pid/417/1568.html):

Differential Game Analyses of Logistics Service Supply Chain Coordination by Cost Sharing Contract. [J. Appl. Math.2014](https://dblp.org/db/journals/jam/jam2014.html#journals/jam/ZhaoLMY14): 842409:1-842409:10 (2014)
- ![](https://dblp.org/img/n.png)

\[c13\]
Haifeng Zhao, [Yan Guo](https://dblp.org/pid/68/6846.html), [Ya Zhang](https://dblp.org/pid/85/3714.html), [Shizhong Li](https://dblp.org/pid/139/7009.html):

Penetration signal adaptive cognitive filtering model based on wavelet analysis. [ICCI\*CC2014](https://dblp.org/db/conf/IEEEicci/IEEEicci2014.html#conf/IEEEicci/ZhaoGZL14): 514-519
- 2013
- ![](https://dblp.org/img/n.png)

\[j5\]
Haifeng Zhao, [Liang Yan](https://dblp.org/pid/69/2422-2.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jijun Liu](https://dblp.org/pid/06/3767.html):

On the interface identification of free boundary problem by method of fundamental solution. [Numer. Linear Algebra Appl.20(2)](https://dblp.org/db/journals/nla/nla20.html#journals/nla/ZhaoYL13): 385-396 (2013)
- ![](https://dblp.org/img/n.png)

\[c12\]
[Tianrui Zhang](https://dblp.org/pid/09/10447.html), [Yuanxing Dai](https://dblp.org/pid/138/5182.html), [Caixiu Lu](https://dblp.org/pid/138/5112.html), Haifeng Zhao, [Tianbiao Yu](https://dblp.org/pid/70/6893.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Analysis of TBM Monitoring Data Based on Grey Theory and Neural Network. [BIC-TA2013](https://dblp.org/db/conf/bic-ta/bic-ta2013.html#conf/bic-ta/ZhangDLZY13): 1071-1080
- ![](https://dblp.org/img/n.png)

\[c11\]
Haifeng Zhao, [Haomin Gao](https://dblp.org/pid/156/6806.html), [Xiao Liang](https://dblp.org/pid/06/4676.html), [Xiaomin Mu](https://dblp.org/pid/63/6561.html):

Joint design of spectrum sensing and data transmission for cognitive radio networks. [BMEI2013](https://dblp.org/db/conf/bmei/bmei2013.html#conf/bmei/ZhaoGLM13): 792-796
- 2012
- ![](https://dblp.org/img/n.png)

\[j4\]
[Shulin Liu](https://dblp.org/pid/25/8004.html), [Rui Ma](https://dblp.org/pid/85/5058.html), [Rui Cong](https://dblp.org/pid/121/8434.html), [Hui Wang](https://dblp.org/pid/39/721.html), Haifeng Zhao:

A new approach for embedding dimension determination based on empirical mode decomposition. [Kybernetes41(9)](https://dblp.org/db/journals/kybernetes/kybernetes41.html#journals/kybernetes/LiuMCWZ12): 1176-1184 (2012)
- ![](https://dblp.org/img/n.png)

\[c10\]
[Deguang Kong](https://dblp.org/pid/53/1448.html), [Chris H. Q. Ding](https://dblp.org/pid/d/CHQDing.html), [Heng Huang](https://dblp.org/pid/03/281.html), Haifeng Zhao:

Multi-label ReliefF and F-statistic feature selections for image annotation. [CVPR2012](https://dblp.org/db/conf/cvpr/cvpr2012.html#conf/cvpr/KongDHZ12): 2352-2359
- ![](https://dblp.org/img/n.png)

\[c9\]
[Li Gao](https://dblp.org/pid/18/4703.html), Haifeng Zhao, [Xiaomin Mu](https://dblp.org/pid/63/6561.html), [Yanhui Lu](https://dblp.org/pid/120/6157.html):

A joint design of spectrum sharing and admission control in cognitive radio networks. [WCSP2012](https://dblp.org/db/conf/wcsp/wcsp2012.html#conf/wcsp/GaoZML12): 1-5
- 2011
- ![](https://dblp.org/img/n.png)

\[j3\]
[Didier Sébilleau](https://dblp.org/pid/10/10210.html), [Calogero Natoli](https://dblp.org/pid/37/10210.html), [George M. Gavaza](https://dblp.org/pid/31/10211.html), Haifeng Zhao![](https://dblp.org/img/orcid-mark.12x12.png), [Fabiana Da Pieve](https://dblp.org/pid/61/10210.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Keisuke Hatada](https://dblp.org/pid/13/10210.html)![](https://dblp.org/img/orcid-mark.12x12.png):

MsSpec-1.0: A multiple scattering package for electron spectroscopies in material science. [Comput. Phys. Commun.182(12)](https://dblp.org/db/journals/cphysics/cphysics182.html#journals/cphysics/SebilleauNGZPH11): 2567-2579 (2011)
- ![](https://dblp.org/img/n.png)

\[c8\]
[Qian Zhang](https://dblp.org/pid/04/2024.html), [Yilan Kang](https://dblp.org/pid/57/10132.html), [Zongxi Cai](https://dblp.org/pid/52/10133.html), [Yu Zhao](https://dblp.org/pid/57/2056.html), Haifeng Zhao, [Pengcheng Su](https://dblp.org/pid/62/7626.html):

A nonlinear multiple regression model for load identification of shield machine combined with mechanical analysis. [FSKD2011](https://dblp.org/db/conf/fskd/fskd2011.html#conf/fskd/ZhangKCZZS11): 1212-1216
- ![](https://dblp.org/img/n.png)

\[c7\]
[Weiwei Cui](https://dblp.org/pid/34/2915.html), Haifeng Zhao, [Xiaomin Mu](https://dblp.org/pid/63/6561.html):

Throughput Analysis in Cooperative Sensing Networks over Imperfect Reporting Channel. [CMC2011](https://dblp.org/db/conf/ieeecmc/ieeecmc2011.html#conf/ieeecmc/CuiZM11): 290-293
- 2010
- ![](https://dblp.org/img/n.png)

\[j2\]
[Yu Wang](https://dblp.org/pid/02/5889.html), [Xiaoyan Xu](https://dblp.org/pid/16/5989.html), Haifeng Zhao, [Zhongsheng Hua](https://dblp.org/pid/65/6081.html)![](https://dblp.org/img/orcid-mark.12x12.png):

Semi-supervised learning based on nearest neighbor rule and cut edges. [Knowl. Based Syst.23(6)](https://dblp.org/db/journals/kbs/kbs23.html#journals/kbs/WangXZH10): 547-554 (2010)
- ![](https://dblp.org/img/n.png)

\[c6\]
Haifeng Zhao, [Zijie Qi](https://dblp.org/pid/03/1031.html):

Hierarchical Agglomerative Clustering with Ordering Constraints. [WKDD2010](https://dblp.org/db/conf/wkdd/wkdd2010.html#conf/wkdd/ZhaoQ10): 195-199
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2008
- ![](https://dblp.org/img/n.png)

\[j1\]
[Wenhui Lu](https://dblp.org/pid/59/8447.html), [Hang Song](https://dblp.org/pid/89/494.html), [Yixin Jin](https://dblp.org/pid/03/5178.html), Haifeng Zhao, [Zhiming Li](https://dblp.org/pid/69/2834.html), [Hong Jiang](https://dblp.org/pid/16/3631.html), [Guoqing Miao](https://dblp.org/pid/43/3110.html):

Improved field emission characteristic of carbon nanotubes by an Ag micro-particle intermediation layer. [Microelectron. J.39(5)](https://dblp.org/db/journals/mj/mj39.html#journals/mj/LuSJZLJM08): 782-785 (2008)
- ![](https://dblp.org/img/n.png)

\[c5\]
[Shuang Liang](https://dblp.org/pid/20/1080.html), [Xingyu Jiang](https://dblp.org/pid/23/4062.html), [Jianrong Wang](https://dblp.org/pid/49/5065.html), Haifeng Zhao, [Ye Zhang](https://dblp.org/pid/147/0497.html), [Wanshan Wang](https://dblp.org/pid/03/1026.html):

Study on negotiation model of collaborative design based on Customer Satisfaction. [CSCWD2008](https://dblp.org/db/conf/cscwd/cscwd2008.html#conf/cscwd/LiangJWZZW08): 962-966
- ![](https://dblp.org/img/n.png)

\[c4\]
[Jianrong Wang](https://dblp.org/pid/49/5065.html), Haifeng Zhao, [Jianwei Du](https://dblp.org/pid/83/2174.html), [Tianbiao Yu](https://dblp.org/pid/70/6893.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Wanshan Wang](https://dblp.org/pid/03/1026.html):

Neural Network Model Based Job Scheduling and Its Implementation in Networked Manufacturing. [ICNC (3)2008](https://dblp.org/db/conf/icnc/icnc2008-3.html#conf/icnc/WangZDYW08): 480-484
- ![](https://dblp.org/img/n.png)

\[c3\]
[Jianqiao Feng](https://dblp.org/pid/79/1380.html), Haifeng Zhao, [Wenhua Jia](https://dblp.org/pid/120/4605.html):

A New Adaptive Distance Computation Technique for Query-by-Multiple-Example System. [SITIS2008](https://dblp.org/db/conf/sitis/sitis2008.html#conf/sitis/FengZJ08): 504-510
- 2007
- ![](https://dblp.org/img/n.png)

\[c2\]
[Shulin Liu](https://dblp.org/pid/25/8004.html), Haifeng Zhao, [Hui Wang](https://dblp.org/pid/39/721.html), [Rui Ma](https://dblp.org/pid/85/5058.html):

Application of improved EMD algorithm for the fault diagnosis of reciprocating pump valves with spring failure. [ISSPA2007](https://dblp.org/db/conf/isspa/isspa2007.html#conf/isspa/LiuZWM07): 1-4
- ![](https://dblp.org/img/n.png)

\[c1\]
Haifeng Zhao, [Wenhua Jia](https://dblp.org/pid/120/4605.html):

An Adaptive Fuzzy Clustering Method for Query-by-Multiple-Example Image Retrieval. [SITIS2007](https://dblp.org/db/conf/sitis/sitis2007.html#conf/sitis/ZhaoJ07): 997-1004
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/17/5245.html?view=joint&param=1 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=2)

[Raquib-ul Alam](https://dblp.org/pid/279/7503.html)

[\[j12\]](https://dblp.org/pid/17/5245.html#j12)

[2](https://dblp.org/pid/17/5245.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yuan An](https://dblp.org/pid/54/323.html)

[\[j11\]](https://dblp.org/pid/17/5245.html#j11)

[3](https://dblp.org/pid/17/5245.html?view=joint&param=3 "show joint publications")

[![5](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=5)

[Xiaoguang Bao](https://dblp.org/pid/87/719.html)

[\[j21\]](https://dblp.org/pid/17/5245.html#j21)

[4](https://dblp.org/pid/17/5245.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Wray L. Buntine](https://dblp.org/pid/72/3885.html)

[\[c27\]](https://dblp.org/pid/17/5245.html#c27)

[5](https://dblp.org/pid/17/5245.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zongxi Cai](https://dblp.org/pid/52/10133.html)

[\[c8\]](https://dblp.org/pid/17/5245.html#c8)

[6](https://dblp.org/pid/17/5245.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Chunyan Cao](https://dblp.org/pid/137/6294.html)

[\[c23\]](https://dblp.org/pid/17/5245.html#c23)

[7](https://dblp.org/pid/17/5245.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yi Chang 0001](https://dblp.org/pid/02/5438.html)

[\[c26\]](https://dblp.org/pid/17/5245.html#c26) [\[i1\]](https://dblp.org/pid/17/5245.html#i1)

[8](https://dblp.org/pid/17/5245.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Ding Chen](https://dblp.org/pid/78/3806.html)

[\[j19\]](https://dblp.org/pid/17/5245.html#j19)

[9](https://dblp.org/pid/17/5245.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Quan Chen 0002](https://dblp.org/pid/40/3858-2.html)

[\[c25\]](https://dblp.org/pid/17/5245.html#c25)

[10](https://dblp.org/pid/17/5245.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zhixiang Chen 0017](https://dblp.org/pid/332/6603.html)

[\[c19\]](https://dblp.org/pid/17/5245.html#c19)

[11](https://dblp.org/pid/17/5245.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Bo Cheng](https://dblp.org/pid/05/2700.html)

[\[c26\]](https://dblp.org/pid/17/5245.html#c26) [\[i1\]](https://dblp.org/pid/17/5245.html#i1)

[12](https://dblp.org/pid/17/5245.html?view=joint&param=12 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=2)

[Darryl Chiu](https://dblp.org/pid/355/2928.html)

[\[j15\]](https://dblp.org/pid/17/5245.html#j15)

[13](https://dblp.org/pid/17/5245.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Rui Cong](https://dblp.org/pid/121/8434.html)

[\[j4\]](https://dblp.org/pid/17/5245.html#j4)

[14](https://dblp.org/pid/17/5245.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Weiwei Cui](https://dblp.org/pid/34/2915.html)

[\[c7\]](https://dblp.org/pid/17/5245.html#c7)

[15](https://dblp.org/pid/17/5245.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yuanxing Dai](https://dblp.org/pid/138/5182.html)

[\[c12\]](https://dblp.org/pid/17/5245.html#c12)

[16](https://dblp.org/pid/17/5245.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Muhammet Deveci](https://dblp.org/pid/136/0546.html)

[\[j18\]](https://dblp.org/pid/17/5245.html#j18)

[17](https://dblp.org/pid/17/5245.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Chris Ding](https://dblp.org/pid/d/CHQDing.html)

aka: Chris H. Q. Ding

[\[c10\]](https://dblp.org/pid/17/5245.html#c10)

[18](https://dblp.org/pid/17/5245.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Weiping Ding 0001](https://dblp.org/pid/133/0292-1.html)

[\[j18\]](https://dblp.org/pid/17/5245.html#j18)

[19](https://dblp.org/pid/17/5245.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zhongyi Ding](https://dblp.org/pid/309/9697.html)

[\[j22\]](https://dblp.org/pid/17/5245.html#j22) [\[c24\]](https://dblp.org/pid/17/5245.html#c24)

[20](https://dblp.org/pid/17/5245.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Jianwei Du](https://dblp.org/pid/83/2174.html)

[\[c4\]](https://dblp.org/pid/17/5245.html#c4)

[21](https://dblp.org/pid/17/5245.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Lan Du 0002](https://dblp.org/pid/98/1504-2.html)

[\[c28\]](https://dblp.org/pid/17/5245.html#c28) [\[c27\]](https://dblp.org/pid/17/5245.html#c27) [\[c26\]](https://dblp.org/pid/17/5245.html#c26) [\[i1\]](https://dblp.org/pid/17/5245.html#i1)

[22](https://dblp.org/pid/17/5245.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Wenjuan Du](https://dblp.org/pid/246/2632.html)

[\[j26\]](https://dblp.org/pid/17/5245.html#j26)

[23](https://dblp.org/pid/17/5245.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Shihui Duan](https://dblp.org/pid/168/1893.html)

[\[j10\]](https://dblp.org/pid/17/5245.html#j10)

[24](https://dblp.org/pid/17/5245.html?view=joint&param=24 "show joint publications")

[![6](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=6)

[Jianqiao Feng](https://dblp.org/pid/79/1380.html)

[\[c3\]](https://dblp.org/pid/17/5245.html#c3)

[25](https://dblp.org/pid/17/5245.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Ziyi Feng](https://dblp.org/pid/189/3855.html)

[\[c23\]](https://dblp.org/pid/17/5245.html#c23)

[26](https://dblp.org/pid/17/5245.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Senbo Fu](https://dblp.org/pid/48/10194.html)

[\[c25\]](https://dblp.org/pid/17/5245.html#c25)

[27](https://dblp.org/pid/17/5245.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Haomin Gao](https://dblp.org/pid/156/6806.html)

[\[c11\]](https://dblp.org/pid/17/5245.html#c11)

[28](https://dblp.org/pid/17/5245.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Jun Gao](https://dblp.org/pid/82/4977.html)

[\[c28\]](https://dblp.org/pid/17/5245.html#c28)

[29](https://dblp.org/pid/17/5245.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Li Gao](https://dblp.org/pid/18/4703.html)

[\[c9\]](https://dblp.org/pid/17/5245.html#c9)

[30](https://dblp.org/pid/17/5245.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Shunxiang Gao](https://dblp.org/pid/383/1897.html)

[\[c28\]](https://dblp.org/pid/17/5245.html#c28)

[31](https://dblp.org/pid/17/5245.html?view=joint&param=31 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=4)

[George M. Gavaza](https://dblp.org/pid/31/10211.html)

[\[j3\]](https://dblp.org/pid/17/5245.html#j3)

[32](https://dblp.org/pid/17/5245.html?view=joint&param=32 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=2)

[Andrew J. Goodwin](https://dblp.org/pid/285/6212.html)

[\[j12\]](https://dblp.org/pid/17/5245.html#j12)

[33](https://dblp.org/pid/17/5245.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Jin Gu](https://dblp.org/pid/33/6358.html)

[\[j16\]](https://dblp.org/pid/17/5245.html#j16)

[34](https://dblp.org/pid/17/5245.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Chongqing Guo](https://dblp.org/pid/146/8466.html)

[\[j7\]](https://dblp.org/pid/17/5245.html#j7)

[35](https://dblp.org/pid/17/5245.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Minyi Guo](https://dblp.org/pid/99/6797.html)

[\[c25\]](https://dblp.org/pid/17/5245.html#c25)

[36](https://dblp.org/pid/17/5245.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xiangdong Guo](https://dblp.org/pid/266/7083.html)

[\[c17\]](https://dblp.org/pid/17/5245.html#c17)

[37](https://dblp.org/pid/17/5245.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yan Guo](https://dblp.org/pid/68/6846.html)

[\[c13\]](https://dblp.org/pid/17/5245.html#c13)

[38](https://dblp.org/pid/17/5245.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Rujin Han](https://dblp.org/pid/357/7003.html)

[\[c21\]](https://dblp.org/pid/17/5245.html#c21)

[39](https://dblp.org/pid/17/5245.html?view=joint&param=39 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=3)

[Xue Han](https://dblp.org/pid/17/6400.html)

[\[i2\]](https://dblp.org/pid/17/5245.html#i2)

[40](https://dblp.org/pid/17/5245.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Shenglin Hao](https://dblp.org/pid/365/0421.html)

[\[c23\]](https://dblp.org/pid/17/5245.html#c23)

[41](https://dblp.org/pid/17/5245.html?view=joint&param=41 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=4)

[Keisuke Hatada](https://dblp.org/pid/13/10210.html)

[\[j3\]](https://dblp.org/pid/17/5245.html#j3)

[42](https://dblp.org/pid/17/5245.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yilun Hong](https://dblp.org/pid/263/9568.html)

[\[c22\]](https://dblp.org/pid/17/5245.html#c22)

[43](https://dblp.org/pid/17/5245.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zhongsheng Hua](https://dblp.org/pid/65/6081.html)

[\[j2\]](https://dblp.org/pid/17/5245.html#j2)

[44](https://dblp.org/pid/17/5245.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Heng Huang 0001](https://dblp.org/pid/03/281.html)

[\[c10\]](https://dblp.org/pid/17/5245.html#c10)

[45](https://dblp.org/pid/17/5245.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Keyan Huo](https://dblp.org/pid/355/8709.html)

[\[c22\]](https://dblp.org/pid/17/5245.html#c22)

[46](https://dblp.org/pid/17/5245.html?view=joint&param=46 "show joint publications")

[![6](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=6)

[Wenhua Jia](https://dblp.org/pid/120/4605.html)

[\[c3\]](https://dblp.org/pid/17/5245.html#c3) [\[c1\]](https://dblp.org/pid/17/5245.html#c1)

[47](https://dblp.org/pid/17/5245.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Dengpan Jiang](https://dblp.org/pid/368/3709.html)

[\[j16\]](https://dblp.org/pid/17/5245.html#j16)

[48](https://dblp.org/pid/17/5245.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Hong Jiang](https://dblp.org/pid/16/3631.html)

[\[j1\]](https://dblp.org/pid/17/5245.html#j1)

[49](https://dblp.org/pid/17/5245.html?view=joint&param=49 "show joint publications")

[Weijia Jiang](https://dblp.org/pid/64/7674.html)

[\[c15\]](https://dblp.org/pid/17/5245.html#c15)

[50](https://dblp.org/pid/17/5245.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xingyu Jiang](https://dblp.org/pid/23/4062.html)

[\[c5\]](https://dblp.org/pid/17/5245.html#c5)

[51](https://dblp.org/pid/17/5245.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Jian Jiao](https://dblp.org/pid/29/265.html)

[\[j23\]](https://dblp.org/pid/17/5245.html#j23)

[52](https://dblp.org/pid/17/5245.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yixin Jin](https://dblp.org/pid/03/5178.html)

[\[j1\]](https://dblp.org/pid/17/5245.html#j1)

[53](https://dblp.org/pid/17/5245.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yilan Kang](https://dblp.org/pid/57/10132.html)

[\[c8\]](https://dblp.org/pid/17/5245.html#c8)

[54](https://dblp.org/pid/17/5245.html?view=joint&param=54 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=2)

[Petra Karlsson](https://dblp.org/pid/205/6643.html)

[\[j15\]](https://dblp.org/pid/17/5245.html#j15) [\[c18\]](https://dblp.org/pid/17/5245.html#c18)

[55](https://dblp.org/pid/17/5245.html?view=joint&param=55 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=2)

[Omid Kavehei](https://dblp.org/pid/41/9830.html)

[\[j15\]](https://dblp.org/pid/17/5245.html#j15) [\[c18\]](https://dblp.org/pid/17/5245.html#c18) [\[j12\]](https://dblp.org/pid/17/5245.html#j12)

[56](https://dblp.org/pid/17/5245.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Deguang Kong](https://dblp.org/pid/53/1448.html)

[\[c10\]](https://dblp.org/pid/17/5245.html#c10)

[57](https://dblp.org/pid/17/5245.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Chee Siang Leow](https://dblp.org/pid/232/2856.html)

[\[j24\]](https://dblp.org/pid/17/5245.html#j24)

[58](https://dblp.org/pid/17/5245.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Chen Li](https://dblp.org/pid/164/3294.html)

[\[c27\]](https://dblp.org/pid/17/5245.html#c27)

[59](https://dblp.org/pid/17/5245.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Chengjun Li](https://dblp.org/pid/16/953.html)

[\[c24\]](https://dblp.org/pid/17/5245.html#c24)

[60](https://dblp.org/pid/17/5245.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Feng Li 0042](https://dblp.org/pid/92/2954-42.html)

[\[j10\]](https://dblp.org/pid/17/5245.html#j10)

[61](https://dblp.org/pid/17/5245.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Jianmin Li](https://dblp.org/pid/71/5930.html)

[\[j22\]](https://dblp.org/pid/17/5245.html#j22) [\[c24\]](https://dblp.org/pid/17/5245.html#c24)

[62](https://dblp.org/pid/17/5245.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Jinhua Li](https://dblp.org/pid/73/5899.html)

[\[c24\]](https://dblp.org/pid/17/5245.html#c24)

[63](https://dblp.org/pid/17/5245.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Shizhong Li](https://dblp.org/pid/139/7009.html)

[\[c13\]](https://dblp.org/pid/17/5245.html#c13)

[64](https://dblp.org/pid/17/5245.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Shuo Li](https://dblp.org/pid/49/595.html)

[\[j11\]](https://dblp.org/pid/17/5245.html#j11)

[65](https://dblp.org/pid/17/5245.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Song Li 0001](https://dblp.org/pid/67/2580-1.html)

[\[j11\]](https://dblp.org/pid/17/5245.html#j11)

[66](https://dblp.org/pid/17/5245.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xihan Li 0004](https://dblp.org/pid/357/6957.html)

[\[c21\]](https://dblp.org/pid/17/5245.html#c21)

[67](https://dblp.org/pid/17/5245.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yuehua Li](https://dblp.org/pid/145/2817.html)

[\[j25\]](https://dblp.org/pid/17/5245.html#j25)

[68](https://dblp.org/pid/17/5245.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zhiming Li](https://dblp.org/pid/69/2834.html)

[\[j1\]](https://dblp.org/pid/17/5245.html#j1)

[69](https://dblp.org/pid/17/5245.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zhuo Li](https://dblp.org/pid/51/4015.html)

[\[j25\]](https://dblp.org/pid/17/5245.html#j25)

[70](https://dblp.org/pid/17/5245.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zijun Li 0001](https://dblp.org/pid/44/10301-1.html)

[\[c25\]](https://dblp.org/pid/17/5245.html#c25)

[71](https://dblp.org/pid/17/5245.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Ziying Li](https://dblp.org/pid/142/6230.html)

[\[j24\]](https://dblp.org/pid/17/5245.html#j24)

[72](https://dblp.org/pid/17/5245.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Shuang Liang](https://dblp.org/pid/20/1080.html)

[\[c5\]](https://dblp.org/pid/17/5245.html#c5)

[73](https://dblp.org/pid/17/5245.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xiao Liang](https://dblp.org/pid/06/4676.html)

[\[c11\]](https://dblp.org/pid/17/5245.html#c11)

[74](https://dblp.org/pid/17/5245.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Bin Lin 0003](https://dblp.org/pid/11/1186-3.html)

[\[j7\]](https://dblp.org/pid/17/5245.html#j7) [\[j6\]](https://dblp.org/pid/17/5245.html#j6)

[75](https://dblp.org/pid/17/5245.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Qiang Ling 0001](https://dblp.org/pid/99/4581-1.html)

[\[j10\]](https://dblp.org/pid/17/5245.html#j10)

[76](https://dblp.org/pid/17/5245.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Ao Liu](https://dblp.org/pid/182/7579.html)

[\[j25\]](https://dblp.org/pid/17/5245.html#j25)

[77](https://dblp.org/pid/17/5245.html?view=joint&param=77 "show joint publications")

[![7](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=7)

[Jijun Liu](https://dblp.org/pid/06/3767.html)

[\[j5\]](https://dblp.org/pid/17/5245.html#j5)

[78](https://dblp.org/pid/17/5245.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Shulin Liu](https://dblp.org/pid/25/8004.html)

[\[j4\]](https://dblp.org/pid/17/5245.html#j4) [\[c2\]](https://dblp.org/pid/17/5245.html#c2)

[79](https://dblp.org/pid/17/5245.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Wei Liu](https://dblp.org/pid/49/3283.html)

[\[c23\]](https://dblp.org/pid/17/5245.html#c23)

[80](https://dblp.org/pid/17/5245.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yiyu Liu](https://dblp.org/pid/263/7231.html)

[\[c25\]](https://dblp.org/pid/17/5245.html#c25)

[81](https://dblp.org/pid/17/5245.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Caixiu Lu](https://dblp.org/pid/138/5112.html)

[\[c12\]](https://dblp.org/pid/17/5245.html#c12)

[82](https://dblp.org/pid/17/5245.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Jueqing Lu](https://dblp.org/pid/276/5821.html)

[\[c26\]](https://dblp.org/pid/17/5245.html#c26) [\[i1\]](https://dblp.org/pid/17/5245.html#i1)

[83](https://dblp.org/pid/17/5245.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Wenhui Lu](https://dblp.org/pid/59/8447.html)

[\[j1\]](https://dblp.org/pid/17/5245.html#j1)

[84](https://dblp.org/pid/17/5245.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yanhui Lu](https://dblp.org/pid/120/6157.html)

[\[c9\]](https://dblp.org/pid/17/5245.html#c9)

[85](https://dblp.org/pid/17/5245.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yong Lu](https://dblp.org/pid/72/2700.html)

[\[c23\]](https://dblp.org/pid/17/5245.html#c23)

[86](https://dblp.org/pid/17/5245.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Cong-Min Lv](https://dblp.org/pid/217/4896.html)

aka: Congmin Lv

[\[j17\]](https://dblp.org/pid/17/5245.html#j17)

[87](https://dblp.org/pid/17/5245.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Hongyu Lv](https://dblp.org/pid/301/5688.html)

[\[j17\]](https://dblp.org/pid/17/5245.html#j17)

[88](https://dblp.org/pid/17/5245.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Rui Ma](https://dblp.org/pid/85/5058.html)

[\[j4\]](https://dblp.org/pid/17/5245.html#j4) [\[c2\]](https://dblp.org/pid/17/5245.html#c2)

[89](https://dblp.org/pid/17/5245.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Wanqing Mao](https://dblp.org/pid/146/9288.html)

[\[j6\]](https://dblp.org/pid/17/5245.html#j6)

[90](https://dblp.org/pid/17/5245.html?view=joint&param=90 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=2)

[Alistair Lee McEwan](https://dblp.org/pid/84/10611.html)

[\[j15\]](https://dblp.org/pid/17/5245.html#j15) [\[c18\]](https://dblp.org/pid/17/5245.html#c18) [\[j12\]](https://dblp.org/pid/17/5245.html#j12)

[91](https://dblp.org/pid/17/5245.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Guoqing Miao](https://dblp.org/pid/43/3110.html)

[\[j1\]](https://dblp.org/pid/17/5245.html#j1)

[92](https://dblp.org/pid/17/5245.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Ruinan Mu](https://dblp.org/pid/357/6815.html)

[\[j22\]](https://dblp.org/pid/17/5245.html#j22) [\[c24\]](https://dblp.org/pid/17/5245.html#c24) [\[c21\]](https://dblp.org/pid/17/5245.html#c21)

[93](https://dblp.org/pid/17/5245.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xiaomin Mu](https://dblp.org/pid/63/6561.html)

[\[c11\]](https://dblp.org/pid/17/5245.html#c11) [\[c9\]](https://dblp.org/pid/17/5245.html#c9) [\[c7\]](https://dblp.org/pid/17/5245.html#c7)

[94](https://dblp.org/pid/17/5245.html?view=joint&param=94 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=4)

[Calogero Natoli](https://dblp.org/pid/37/10210.html)

[\[j3\]](https://dblp.org/pid/17/5245.html#j3)

[95](https://dblp.org/pid/17/5245.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Dan Nguyen](https://dblp.org/pid/62/1355.html)

[\[c27\]](https://dblp.org/pid/17/5245.html#c27)

[96](https://dblp.org/pid/17/5245.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Hebing Nie](https://dblp.org/pid/353/9606.html)

[\[j18\]](https://dblp.org/pid/17/5245.html#j18)

[97](https://dblp.org/pid/17/5245.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Hiromitsu Nishizaki](https://dblp.org/pid/87/1050.html)

[\[j24\]](https://dblp.org/pid/17/5245.html#j24)

[98](https://dblp.org/pid/17/5245.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Lizhi Pan](https://dblp.org/pid/133/5474.html)

[\[j22\]](https://dblp.org/pid/17/5245.html#j22) [\[c24\]](https://dblp.org/pid/17/5245.html#c24)

[99](https://dblp.org/pid/17/5245.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Meixiu Pan](https://dblp.org/pid/413/9763.html)

[\[j25\]](https://dblp.org/pid/17/5245.html#j25)

[100](https://dblp.org/pid/17/5245.html?view=joint&param=100 "show joint publications")

[Zhibin Pan](https://dblp.org/pid/97/2574.html)

[\[j9\]](https://dblp.org/pid/17/5245.html#j9) [\[j8\]](https://dblp.org/pid/17/5245.html#j8)

[101](https://dblp.org/pid/17/5245.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Qian Peng](https://dblp.org/pid/67/6523.html)

[\[c25\]](https://dblp.org/pid/17/5245.html#c25)

[102](https://dblp.org/pid/17/5245.html?view=joint&param=102 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=4)

[Fabiana Da Pieve](https://dblp.org/pid/61/10210.html)

[\[j3\]](https://dblp.org/pid/17/5245.html#j3)

[103](https://dblp.org/pid/17/5245.html?view=joint&param=103 "show joint publications")

[Zijie Qi](https://dblp.org/pid/03/1031.html)

[\[c6\]](https://dblp.org/pid/17/5245.html#c6)

[104](https://dblp.org/pid/17/5245.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yuan Quan](https://dblp.org/pid/128/9916.html)

[\[j17\]](https://dblp.org/pid/17/5245.html#j17)

[105](https://dblp.org/pid/17/5245.html?view=joint&param=105 "show joint publications")

[![4](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=4)

[Didier Sébilleau](https://dblp.org/pid/10/10210.html)

[\[j3\]](https://dblp.org/pid/17/5245.html#j3)

[106](https://dblp.org/pid/17/5245.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Chengcheng Shen](https://dblp.org/pid/55/11102.html)

[\[j23\]](https://dblp.org/pid/17/5245.html#j23)

[107](https://dblp.org/pid/17/5245.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xingfa Shen](https://dblp.org/pid/07/4044.html)

[\[j24\]](https://dblp.org/pid/17/5245.html#j24)

[108](https://dblp.org/pid/17/5245.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Lei Shi](https://dblp.org/pid/29/563.html)

[\[j19\]](https://dblp.org/pid/17/5245.html#j19)

[109](https://dblp.org/pid/17/5245.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Hang Song](https://dblp.org/pid/89/494.html)

[\[j1\]](https://dblp.org/pid/17/5245.html#j1)

[110](https://dblp.org/pid/17/5245.html?view=joint&param=110 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=3)

[Xueqi Song](https://dblp.org/pid/400/8968.html)

[\[i2\]](https://dblp.org/pid/17/5245.html#i2)

[111](https://dblp.org/pid/17/5245.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Pengcheng Su](https://dblp.org/pid/62/7626.html)

[\[c8\]](https://dblp.org/pid/17/5245.html#c8)

[112](https://dblp.org/pid/17/5245.html?view=joint&param=112 "show joint publications")

[![2](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=2)

[Carter Sun](https://dblp.org/pid/355/3235.html)

[\[j15\]](https://dblp.org/pid/17/5245.html#j15)

[113](https://dblp.org/pid/17/5245.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Guozi Sun](https://dblp.org/pid/91/1406.html)

[\[c19\]](https://dblp.org/pid/17/5245.html#c19)

[114](https://dblp.org/pid/17/5245.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zheng Sun](https://dblp.org/pid/36/2849.html)

[\[j25\]](https://dblp.org/pid/17/5245.html#j25)

[115](https://dblp.org/pid/17/5245.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Edward Szczerbicki](https://dblp.org/pid/25/345.html)

[\[j19\]](https://dblp.org/pid/17/5245.html#j19)

[116](https://dblp.org/pid/17/5245.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Huiling Tan](https://dblp.org/pid/81/7821.html)

[\[c23\]](https://dblp.org/pid/17/5245.html#c23)

[117](https://dblp.org/pid/17/5245.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Wei Tan](https://dblp.org/pid/73/6520.html)

[\[c27\]](https://dblp.org/pid/17/5245.html#c27)

[118](https://dblp.org/pid/17/5245.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zhenyu Tang](https://dblp.org/pid/72/4431.html)

[\[c17\]](https://dblp.org/pid/17/5245.html#c17)

[119](https://dblp.org/pid/17/5245.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yuan Tian 0016](https://dblp.org/pid/39/5423-16.html)

[\[c26\]](https://dblp.org/pid/17/5245.html#c26) [\[i1\]](https://dblp.org/pid/17/5245.html#i1)

[120](https://dblp.org/pid/17/5245.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zhibin Tian](https://dblp.org/pid/357/6837.html)

[\[c21\]](https://dblp.org/pid/17/5245.html#c21)

[121](https://dblp.org/pid/17/5245.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Hui Wang](https://dblp.org/pid/39/721.html)

[\[j4\]](https://dblp.org/pid/17/5245.html#j4) [\[c2\]](https://dblp.org/pid/17/5245.html#c2)

[122](https://dblp.org/pid/17/5245.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Jianrong Wang](https://dblp.org/pid/49/5065.html)

[\[c5\]](https://dblp.org/pid/17/5245.html#c5) [\[c4\]](https://dblp.org/pid/17/5245.html#c4)

[123](https://dblp.org/pid/17/5245.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Juan Wang 0017](https://dblp.org/pid/74/3634-17.html)

[\[j19\]](https://dblp.org/pid/17/5245.html#j19)

[124](https://dblp.org/pid/17/5245.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Ke Wang 0046](https://dblp.org/pid/181/2613-46.html)

[\[j17\]](https://dblp.org/pid/17/5245.html#j17)

[125](https://dblp.org/pid/17/5245.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Mengfei Wang](https://dblp.org/pid/253/2113.html)

[\[j25\]](https://dblp.org/pid/17/5245.html#j25)

[126](https://dblp.org/pid/17/5245.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Wanshan Wang](https://dblp.org/pid/03/1026.html)

[\[c5\]](https://dblp.org/pid/17/5245.html#c5) [\[c4\]](https://dblp.org/pid/17/5245.html#c4)

[127](https://dblp.org/pid/17/5245.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xingjun Wang](https://dblp.org/pid/82/3752.html)

[\[c16\]](https://dblp.org/pid/17/5245.html#c16)

[128](https://dblp.org/pid/17/5245.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yu Wang](https://dblp.org/pid/02/5889.html)

[\[j2\]](https://dblp.org/pid/17/5245.html#j2)

[129](https://dblp.org/pid/17/5245.html?view=joint&param=129 "show joint publications")

[![5](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=5)

[Zhaocai Wang](https://dblp.org/pid/91/3147.html)

[\[j21\]](https://dblp.org/pid/17/5245.html#j21)

[130](https://dblp.org/pid/17/5245.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zhiqiang Wang](https://dblp.org/pid/67/187.html)

[\[c21\]](https://dblp.org/pid/17/5245.html#c21)

[131](https://dblp.org/pid/17/5245.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zuli Wang 0001](https://dblp.org/pid/187/9462.html)

[\[j19\]](https://dblp.org/pid/17/5245.html#j19)

[132](https://dblp.org/pid/17/5245.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Qun Wu](https://dblp.org/pid/54/2083.html)

[\[j18\]](https://dblp.org/pid/17/5245.html#j18)

[133](https://dblp.org/pid/17/5245.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Tianjian Wu](https://dblp.org/pid/332/6501.html)

[\[c19\]](https://dblp.org/pid/17/5245.html#c19)

[134](https://dblp.org/pid/17/5245.html?view=joint&param=134 "show joint publications")

[![5](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=5)

[Tunhua Wu](https://dblp.org/pid/27/10618.html)

[\[j21\]](https://dblp.org/pid/17/5245.html#j21)

[135](https://dblp.org/pid/17/5245.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Wenfu Wu](https://dblp.org/pid/69/8546.html)

[\[j10\]](https://dblp.org/pid/17/5245.html#j10)

[136](https://dblp.org/pid/17/5245.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xueqi Wu](https://dblp.org/pid/200/2643.html)

[\[c25\]](https://dblp.org/pid/17/5245.html#c25)

[137](https://dblp.org/pid/17/5245.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Chuhao Xu](https://dblp.org/pid/330/7863.html)

[\[c25\]](https://dblp.org/pid/17/5245.html#c25)

[138](https://dblp.org/pid/17/5245.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Lixiang Xu](https://dblp.org/pid/09/10206.html)

[\[j10\]](https://dblp.org/pid/17/5245.html#j10)

[139](https://dblp.org/pid/17/5245.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xiaoyan Xu](https://dblp.org/pid/16/5989.html)

[\[j2\]](https://dblp.org/pid/17/5245.html#j2)

[140](https://dblp.org/pid/17/5245.html?view=joint&param=140 "show joint publications")

[![7](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=7)

[Liang Yan 0002](https://dblp.org/pid/69/2422-2.html)

[\[j5\]](https://dblp.org/pid/17/5245.html#j5)

[141](https://dblp.org/pid/17/5245.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Jiafeng Yang](https://dblp.org/pid/329/4050.html)

[\[c21\]](https://dblp.org/pid/17/5245.html#c21)

[142](https://dblp.org/pid/17/5245.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[j19\]](https://dblp.org/pid/17/5245.html#j19)

[143](https://dblp.org/pid/17/5245.html?view=joint&param=143 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=3)

[Haodong Yao](https://dblp.org/pid/158/7464.html)

[\[i2\]](https://dblp.org/pid/17/5245.html#i2)

[144](https://dblp.org/pid/17/5245.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Li Yao](https://dblp.org/pid/83/6976.html)

[\[c14\]](https://dblp.org/pid/17/5245.html#c14)

[145](https://dblp.org/pid/17/5245.html?view=joint&param=145 "show joint publications")

[Lisha Yao](https://dblp.org/pid/225/7489.html)

[\[j20\]](https://dblp.org/pid/17/5245.html#j20) [\[j14\]](https://dblp.org/pid/17/5245.html#j14)

[146](https://dblp.org/pid/17/5245.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yang Ye](https://dblp.org/pid/417/1568.html)

[\[j6\]](https://dblp.org/pid/17/5245.html#j6)

[147](https://dblp.org/pid/17/5245.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Tianbiao Yu](https://dblp.org/pid/70/6893.html)

[\[c12\]](https://dblp.org/pid/17/5245.html#c12) [\[c4\]](https://dblp.org/pid/17/5245.html#c4)

[148](https://dblp.org/pid/17/5245.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Zihao Yuan](https://dblp.org/pid/198/1286.html)

[\[c21\]](https://dblp.org/pid/17/5245.html#c21)

[149](https://dblp.org/pid/17/5245.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Deze Zeng](https://dblp.org/pid/08/5937.html)

[\[c25\]](https://dblp.org/pid/17/5245.html#c25)

[150](https://dblp.org/pid/17/5245.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Hao Zeng](https://dblp.org/pid/59/6515.html)

[\[c22\]](https://dblp.org/pid/17/5245.html#c22)

[151](https://dblp.org/pid/17/5245.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yao Zeng](https://dblp.org/pid/76/2826.html)

[\[j25\]](https://dblp.org/pid/17/5245.html#j25)

[152](https://dblp.org/pid/17/5245.html?view=joint&param=152 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=3)

[Fei Zhan](https://dblp.org/pid/142/3023.html)

[\[i2\]](https://dblp.org/pid/17/5245.html#i2)

[153](https://dblp.org/pid/17/5245.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Shikun Zhan](https://dblp.org/pid/291/5077.html)

[\[c23\]](https://dblp.org/pid/17/5245.html#c23)

[154](https://dblp.org/pid/17/5245.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Danyang Zhang](https://dblp.org/pid/87/1243.html)

[\[c14\]](https://dblp.org/pid/17/5245.html#c14)

[155](https://dblp.org/pid/17/5245.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Hao Zhang](https://dblp.org/pid/55/2270.html)

[\[j26\]](https://dblp.org/pid/17/5245.html#j26)

[156](https://dblp.org/pid/17/5245.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Qian Zhang](https://dblp.org/pid/04/2024.html)

[\[c8\]](https://dblp.org/pid/17/5245.html#c8)

[157](https://dblp.org/pid/17/5245.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Tianmin Zhang](https://dblp.org/pid/425/9858.html)

[\[j26\]](https://dblp.org/pid/17/5245.html#j26)

[158](https://dblp.org/pid/17/5245.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Tianrui Zhang](https://dblp.org/pid/09/10447.html)

[\[c12\]](https://dblp.org/pid/17/5245.html#c12)

[159](https://dblp.org/pid/17/5245.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xiaorui Zhang](https://dblp.org/pid/97/7654.html)

[\[j16\]](https://dblp.org/pid/17/5245.html#j16)

[160](https://dblp.org/pid/17/5245.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xuan Zhang](https://dblp.org/pid/36/31.html)

[\[j26\]](https://dblp.org/pid/17/5245.html#j26)

[161](https://dblp.org/pid/17/5245.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Ya Zhang](https://dblp.org/pid/85/3714.html)

[\[c13\]](https://dblp.org/pid/17/5245.html#c13)

[162](https://dblp.org/pid/17/5245.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yan Zhang](https://dblp.org/pid/04/3348.html)

[\[c28\]](https://dblp.org/pid/17/5245.html#c28) [\[c19\]](https://dblp.org/pid/17/5245.html#c19)

[163](https://dblp.org/pid/17/5245.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Ye Zhang](https://dblp.org/pid/147/0497.html)

[\[c5\]](https://dblp.org/pid/17/5245.html#c5)

[164](https://dblp.org/pid/17/5245.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yijie Zhang](https://dblp.org/pid/185/9892.html)

[\[c20\]](https://dblp.org/pid/17/5245.html#c20)

[165](https://dblp.org/pid/17/5245.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Ying Zhang](https://dblp.org/pid/13/6769.html)

[\[j13\]](https://dblp.org/pid/17/5245.html#j13)

[166](https://dblp.org/pid/17/5245.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Chong Zhao](https://dblp.org/pid/32/3558.html)

[\[j17\]](https://dblp.org/pid/17/5245.html#j17)

[167](https://dblp.org/pid/17/5245.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Haixia Zhao](https://dblp.org/pid/92/4900.html)

[\[c20\]](https://dblp.org/pid/17/5245.html#c20)

[168](https://dblp.org/pid/17/5245.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Han Zhao 0005](https://dblp.org/pid/03/3520-5.html)

[\[c25\]](https://dblp.org/pid/17/5245.html#c25)

[169](https://dblp.org/pid/17/5245.html?view=joint&param=169 "show joint publications")

[![3](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=3)

[Junfang Zhao](https://dblp.org/pid/24/8626.html)

[\[i2\]](https://dblp.org/pid/17/5245.html#i2)

[170](https://dblp.org/pid/17/5245.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Xiangbo Zhao](https://dblp.org/pid/425/9748.html)

[\[j26\]](https://dblp.org/pid/17/5245.html#j26)

[171](https://dblp.org/pid/17/5245.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yu Zhao](https://dblp.org/pid/57/2056.html)

[\[c8\]](https://dblp.org/pid/17/5245.html#c8)

[172](https://dblp.org/pid/17/5245.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Yimin Zhou 0002](https://dblp.org/pid/63/2223-2.html)

[\[j19\]](https://dblp.org/pid/17/5245.html#j19)

[173](https://dblp.org/pid/17/5245.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/17/5245.html?view=group&param=1)

[Guohao Zong](https://dblp.org/pid/402/4266.html)

[\[c28\]](https://dblp.org/pid/17/5245.html#c28)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/17/5245.html#) [\[–\]](https://dblp.org/pid/17/5245.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/17/5245.html#) [\[–\]](https://dblp.org/pid/17/5245.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/17/5245.html#) [\[–\]](https://dblp.org/pid/17/5245.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/17/5245.html#) [\[–\]](https://dblp.org/pid/17/5245.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/17/5245.html#) [\[–\]](https://dblp.org/pid/17/5245.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)