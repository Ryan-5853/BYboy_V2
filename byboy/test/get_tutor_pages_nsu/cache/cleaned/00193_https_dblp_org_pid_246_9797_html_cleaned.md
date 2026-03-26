> 抓取来源：https://dblp.org/pid/246/9797.html

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

- [Qi-Lie Deng](https://dblp.org/pid/360/0413.html)
- [Qiliang Deng](https://dblp.org/pid/190/1273.html)
- [Qilin Deng](https://dblp.org/pid/74/6524.html) — _disambiguation page_
- [Qiling Deng](https://dblp.org/pid/290/9810.html)

**run query for this person**

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Qili+Deng%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F246%2F9797%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Qili+Deng+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F246%2F9797%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Qili+Deng+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F246%2F9797%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Qili+Deng%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F246%2F9797%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Qili+Deng+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F246%2F9797%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Qili+Deng%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F246%2F9797%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Qili+Deng%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F246%2F9797%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F246%2F9797%3E+%7D+.%0A%0A%7D)

_showing all8 records_

2016202652018: 12020: 32020: 32021: 12022: 22026: 1

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

- ![](https://dblp.org/img/add-mark.12x12.png)Daniel K. Du (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Radu Timofte (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Ziling Huang (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Zhihong Fu (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Chung-En Sun (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Bo Liu 0005 (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Hongyu Zhou (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Po-Min Hsu (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Murari Mandal (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Mingzhao Yu (2)

- _299 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (8)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (3)
- ![](https://dblp.org/img/add-mark.12x12.png)ECCV (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)CAAI Trans. Intell. Technol. (1)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (1)
- ![](https://dblp.org/img/add-mark.12x12.png)ICCV (1)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)closed (4)
- ![](https://dblp.org/img/add-mark.12x12.png)open (4)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2026
- ![](https://dblp.org/img/n.png)

\[i2\]
[Huichao Zhang](https://dblp.org/pid/204/1974.html), [Liao Qu](https://dblp.org/pid/299/1491.html), [Yiheng Liu](https://dblp.org/pid/232/3139.html), [Hang Chen](https://dblp.org/pid/87/3677.html), [Yangyang Song](https://dblp.org/pid/57/7453.html), [Yongsheng Dong](https://dblp.org/pid/70/9613.html), [Shikun Sun](https://dblp.org/pid/293/2733.html), [Xian Li](https://dblp.org/pid/82/1763.html), [Xu Wang](https://dblp.org/pid/181/2815.html), [Yi Jiang](https://dblp.org/pid/66/3172.html), [Hu Ye](https://dblp.org/pid/201/8427.html), [Bo Chen](https://dblp.org/pid/89/5615.html), [Yiming Gao](https://dblp.org/pid/370/7119.html), [Peng Liu](https://dblp.org/pid/21/6121.html), [Akide Liu](https://dblp.org/pid/323/5463.html), [Zhipeng Yang](https://dblp.org/pid/18/1726.html), Qili Deng, [Linjie Xing](https://dblp.org/pid/182/2172.html), [Jiyang Liu](https://dblp.org/pid/222/7550.html), [Zhao Wang](https://dblp.org/pid/86/981.html), [Yang Zhou](https://dblp.org/pid/07/4580.html), [Mingcong Liu](https://dblp.org/pid/228/8844.html), [Yi Zhang](https://dblp.org/pid/64/6544.html), [Qian He](https://dblp.org/pid/69/6357.html), [Xiwei Hu](https://dblp.org/pid/255/6325.html), [Zhongqi Qi](https://dblp.org/pid/365/8222.html), [Jie Shao](https://dblp.org/pid/02/5139.html), [Zhiye Fu](https://dblp.org/pid/311/1840.html), [Shuai Wang](https://dblp.org/pid/42/1503.html), [Fangmin Chen](https://dblp.org/pid/320/5863.html), [Xuezhi Chai](https://dblp.org/pid/02/10433.html), [Zhihua Wu](https://dblp.org/pid/81/6301.html), [Yitong Wang](https://dblp.org/pid/58/111.html), [Zehuan Yuan](https://dblp.org/pid/227/3298.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Xinglong Wu](https://dblp.org/pid/269/4913.html):

NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation. [CoRRabs/2601.02204](https://dblp.org/db/journals/corr/corr2601.html#journals/corr/abs-2601-02204) (2026)
- 2022
- ![](https://dblp.org/img/n.png)

\[c5\]
[Wei Xu](https://dblp.org/pid/32/1213-17.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Zhixing Chen](https://dblp.org/pid/62/3074.html), Qili Deng, [Mingtao Fu](https://dblp.org/pid/254/1780.html), [Xijin Zhang](https://dblp.org/pid/242/9085.html), [Yuan Gao](https://dblp.org/pid/76/2452.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Min Zheng](https://dblp.org/pid/23/328.html):

HiFace: Hybrid Task Learning for Face Reconstruction from Single Image. [ECCV Workshops (5)2022](https://dblp.org/db/conf/eccv/eccv2022-w5.html#conf/eccv/XuFCDFZGDZ22): 382-391
- ![](https://dblp.org/img/n.png)

\[c4\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Wenyan Yang](https://dblp.org/pid/119/2426.html), [Dingding Cai](https://dblp.org/pid/198/1127.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Kang Ben](https://dblp.org/pid/340/0959.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Hong Chang](https://dblp.org/pid/02/2689-1.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Jiaye Chen](https://dblp.org/pid/116/2901.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xilin Chen](https://dblp.org/pid/c/XilinChen.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Xiuyi Chen](https://dblp.org/pid/218/7190.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu-Hsi Chen](https://dblp.org/pid/127/3933.html), [Zhixing Chen](https://dblp.org/pid/62/3074.html), [Yangming Cheng](https://dblp.org/pid/340/1285.html), [Angelo Ciaramella](https://dblp.org/pid/37/6845.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Benjamin Dzubur](https://dblp.org/pid/340/1520.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), Qili Deng, [Debajyoti Dhar](https://dblp.org/pid/128/3182.html), [Shangzhe Di](https://dblp.org/pid/304/1344.html), [Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shang Gao](https://dblp.org/pid/28/435-12.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Eric Granger](https://dblp.org/pid/86/2306.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Q. H. Gu](https://dblp.org/pid/340/1209.html), [Himanshu Gupta](https://dblp.org/pid/330/0760-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianfeng He](https://dblp.org/pid/93/8352.html), [Keji He](https://dblp.org/pid/319/4518.html), [Yan Huang](https://dblp.org/pid/75/6434-8.html), [Deepak Jangid](https://dblp.org/pid/340/1460.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Ze Kang](https://dblp.org/pid/340/1063.html), [Madhu Kiran](https://dblp.org/pid/39/10281.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Simiao Lai](https://dblp.org/pid/282/1954.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Dongwook Lee](https://dblp.org/pid/25/6543.html), [Hyunjeong Lee](https://dblp.org/pid/00/3423.html), [Seohyung Lee](https://dblp.org/pid/210/4662.html), [Hui Li](https://dblp.org/pid/66/3387-37.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ming Li](https://dblp.org/pid/l/MingLi10.html), [Wangkai Li](https://dblp.org/pid/340/1456.html), [Xi Li](https://dblp.org/pid/46/2311-1.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Xiao Li](https://dblp.org/pid/66/2069.html), [Zhe Li](https://dblp.org/pid/11/751-8.html), [Liting Lin](https://dblp.org/pid/227/2204.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Si Liu](https://dblp.org/pid/60/7642.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html), [Bingpeng Ma](https://dblp.org/pid/62/1822.html), [Chao Ma](https://dblp.org/pid/79/1552-4.html), [Jie Ma](https://dblp.org/pid/62/5110.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yinchao Ma](https://dblp.org/pid/189/1326.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Payman Moallem](https://dblp.org/pid/63/5378.html), [Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html), [Siyang Pan](https://dblp.org/pid/250/5753.html), [ChangBeom Park](https://dblp.org/pid/340/0926.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Litu Rout](https://dblp.org/pid/206/6445.html), [Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Tianhui Song](https://dblp.org/pid/181/8738.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Chao Sun](https://dblp.org/pid/54/3957.html), [Jingna Sun](https://dblp.org/pid/255/0702.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Om Prakash Verma](https://dblp.org/pid/61/8145.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Qiang Wang](https://dblp.org/pid/64/5630-23.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Jinlin Wu](https://dblp.org/pid/123/7200.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Xu](https://dblp.org/pid/32/1213-17.html), [Yong Xu](https://dblp.org/pid/07/4630-7.html), [Yuanyou Xu](https://dblp.org/pid/248/7663.html), [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zizheng Xun](https://dblp.org/pid/340/1441.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Dawei Yang](https://dblp.org/pid/22/1038.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Yichun Yang](https://dblp.org/pid/249/9678.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Botao Ye](https://dblp.org/pid/227/4610.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Qianjin Yu](https://dblp.org/pid/53/10179.html), [Weichen Yu](https://dblp.org/pid/325/1209.html), [Kang Ze](https://dblp.org/pid/340/1107.html), [Jiang Zhai](https://dblp.org/pid/291/9340.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhu Zhang](https://dblp.org/pid/292/0953.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Haixia Zheng](https://dblp.org/pid/119/1585.html), [Min Zheng](https://dblp.org/pid/23/328.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html):

The Tenth Visual Object Tracking VOT2022 Challenge Results. [ECCV Workshops (8)2022](https://dblp.org/db/conf/eccv/eccv2022-w8.html#conf/eccv/KristanLMFPKCDZLDBZZYYCMFBBCCCCCCCCCCC22): 431-460
- 2021
- ![](https://dblp.org/img/n.png)

\[c3\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Jani Käpylä](https://dblp.org/pid/244/2529.html), [Gustav Häger](https://dblp.org/pid/157/3602.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Llukman Cerkezi](https://dblp.org/pid/208/1312.html), [Hakan Cevikalp](https://dblp.org/pid/14/6210.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Miao Cheng](https://dblp.org/pid/79/7377.html), [Ziyi Cheng](https://dblp.org/pid/290/9342.html), [Yu-Chen Chiu](https://dblp.org/pid/199/2494.html), [Ozgun Cirakman](https://dblp.org/pid/86/8843.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Kenan Dai](https://dblp.org/pid/250/4445.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), Qili Deng, [Xingping Dong](https://dblp.org/pid/156/3020.html), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhiyong Feng](https://dblp.org/pid/48/195-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shiming Ge](https://dblp.org/pid/93/8104.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Yuzhang Gu](https://dblp.org/pid/122/3790.html), [Bilge Günsel](https://dblp.org/pid/47/5125.html), [Qing Guo](https://dblp.org/pid/25/3038-5.html), [Filiz Gurkan](https://dblp.org/pid/202/7040.html), [Wencheng Han](https://dblp.org/pid/280/3348.html), [Yanyan Huang](https://dblp.org/pid/88/4316.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Juefei-Xu](https://dblp.org/pid/35/11103.html), [J. Yin](https://dblp.org/pid/51/2242.html), [Xiao Ke](https://dblp.org/pid/78/9040.html), [Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html), [Byeong Hak Kim](https://dblp.org/pid/214/8978.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Jun Ha Lee](https://dblp.org/pid/260/2774.html), [Bastian Leibe](https://dblp.org/pid/41/1228.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hui Li](https://dblp.org/pid/66/3387-37.html), [Jianhua Li](https://dblp.org/pid/93/3389.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Yuezhou Li](https://dblp.org/pid/284/2562.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Jingen Liu](https://dblp.org/pid/10/5849.html), [Li Liu](https://dblp.org/pid/33/4528-36.html), [Qingjie Liu](https://dblp.org/pid/72/10584.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Wei Lu](https://dblp.org/pid/98/6613.html), [Jonathon Luiten](https://dblp.org/pid/211/7992.html), [Jie Ma](https://dblp.org/pid/62/5110.html), [Ziang Ma](https://dblp.org/pid/165/9621.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Yuzhen Niu](https://dblp.org/pid/28/7442.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Shoumeng Qiu](https://dblp.org/pid/284/2537.html), [Aravindh Rajiv](https://dblp.org/pid/307/9144.html), [Muhammad Rana](https://dblp.org/pid/276/0222.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Hasan Saribas](https://dblp.org/pid/225/3263.html), [Ling Shao](https://dblp.org/pid/75/1281.html), [Mohamed Shehata](https://dblp.org/pid/33/2495.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Furao Shen](https://dblp.org/pid/80/4685.html), [Jianbing Shen](https://dblp.org/pid/38/5435.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Philip H. S. Torr](https://dblp.org/pid/t/PhilipHSTorr.html), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Bedirhan Uzun](https://dblp.org/pid/247/8937.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Paul Voigtlaender](https://dblp.org/pid/166/6430.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Guangting Wang](https://dblp.org/pid/227/7195.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Linyuan Wang](https://dblp.org/pid/138/5963.html), [Yong Wang](https://dblp.org/pid/84/2694-32.html), [Yunhong Wang](https://dblp.org/pid/95/6251.html), [Chenyan Wu](https://dblp.org/pid/76/1190.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiang Xu](https://dblp.org/pid/126/2962.html), [Wanli Xue](https://dblp.org/pid/153/8037.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yu Ye](https://dblp.org/pid/129/0969-4.html), [Jun Yin](https://dblp.org/pid/58/5423-3.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhui Zhang](https://dblp.org/pid/62/3401-1.html), [Haitao Zhang](https://dblp.org/pid/19/6669.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Kangkai Zhang](https://dblp.org/pid/260/2990.html), [Xiaohan Zhang](https://dblp.org/pid/96/6053.html), [Xiaolin Zhang](https://dblp.org/pid/99/2516.html), [Xinyu Zhang](https://dblp.org/pid/58/4582-20.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Ming Zhen](https://dblp.org/pid/307/8430.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html):

The Ninth Visual Object Tracking VOT2021 Challenge Results. [ICCVW2021](https://dblp.org/db/conf/iccvw/iccvw2021.html#conf/iccvw/KristanMLFPKCDZ21): 2711-2738
- 2020
- ![](https://dblp.org/img/n.png)

\[c2\]
[Codruta O. Ancuti](https://dblp.org/pid/89/5661.html), [Cosmin Ancuti](https://dblp.org/pid/82/3581.html), [Florin-Alexandru Vasluianu](https://dblp.org/pid/264/5871.html), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jing Liu](https://dblp.org/pid/72/2590-31.html), [Haiyan Wu](https://dblp.org/pid/11/3756.html), [Yuan Xie](https://dblp.org/pid/157/8128-6.html), [Yanyun Qu](https://dblp.org/pid/03/3500.html), [Lizhuang Ma](https://dblp.org/pid/10/4950.html), [Ziling Huang](https://dblp.org/pid/150/6487.html), Qili Deng, [Ju-Chin Chao](https://dblp.org/pid/264/5933.html), [Tsung-Shan Yang](https://dblp.org/pid/220/4388.html), [Peng-Wen Chen](https://dblp.org/pid/51/6708-1.html), [Po-Min Hsu](https://dblp.org/pid/137/4146.html), [Tzu-Yi Liao](https://dblp.org/pid/76/7881.html), [Chung-En Sun](https://dblp.org/pid/264/5788.html), [Pei-Yuan Wu](https://dblp.org/pid/75/9983.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jeonghyeok Do](https://dblp.org/pid/264/5902.html), [Jongmin Park](https://dblp.org/pid/50/6848.html), [Munchurl Kim](https://dblp.org/pid/84/4965.html), [Kareem M. Metwaly](https://dblp.org/pid/199/8217.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xuelu Li](https://dblp.org/pid/52/8508.html), [Tiantong Guo](https://dblp.org/pid/198/9637.html), [Vishal Monga](https://dblp.org/pid/73/1467.html), [Mingzhao Yu](https://dblp.org/pid/190/9384.html), [Venkateswararao Cherukuri](https://dblp.org/pid/223/6285.html), [Shiue-Yuan Chuang](https://dblp.org/pid/264/5905.html), [Tsung-Nan Lin](https://dblp.org/pid/67/859.html), [David Lee](https://dblp.org/pid/76/1630.html), [Jerome Chang](https://dblp.org/pid/166/0846.html), [Zhan-Han Wang](https://dblp.org/pid/264/5909.html), [Yu-Bang Chang](https://dblp.org/pid/137/3561.html), [Chang-Hong Lin](https://dblp.org/pid/117/7803.html), [Yu Dong](https://dblp.org/pid/03/1299.html), [Hongyu Zhou](https://dblp.org/pid/76/7825.html), [Xiangzhen Kong](https://dblp.org/pid/80/531.html), [Sourya Dipta Das](https://dblp.org/pid/217/1530.html), [Saikat Dutta](https://dblp.org/pid/146/7991-2.html), [Xuan Zhao](https://dblp.org/pid/24/3533.html), [Bing Ouyang](https://dblp.org/pid/169/0821.html), [Dennis Estrada](https://dblp.org/pid/264/5849.html), [Meiqi Wang](https://dblp.org/pid/225/1521.html), [Tianqi Su](https://dblp.org/pid/217/7200.html), [Siyi Chen](https://dblp.org/pid/195/3147-4.html), [Bangyong Sun](https://dblp.org/pid/182/4739.html), [Vincent Jacob Whannou de Dravo](https://dblp.org/pid/182/4665.html), [Zhe Yu](https://dblp.org/pid/32/9128.html), [Pratik Narang](https://dblp.org/pid/132/9397.html), [Aryan Mehra](https://dblp.org/pid/264/5889.html), [Navaneeth Raghunath](https://dblp.org/pid/264/5782.html), [Murari Mandal](https://dblp.org/pid/175/8628.html)![](https://dblp.org/img/orcid-mark.12x12.png):

NTIRE 2020 Challenge on NonHomogeneous Dehazing. [CVPR Workshops2020](https://dblp.org/db/conf/cvpr/cvprw2020.html#conf/cvpr/AncutiAVTLWXQMH20): 2029-2044
- ![](https://dblp.org/img/n.png)

\[c1\]
Qili Deng, [Ziling Huang](https://dblp.org/pid/150/6487.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chung-Chi Tsai](https://dblp.org/pid/52/10137.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chia-Wen Lin](https://dblp.org/pid/l/ChiaWenLin.html)![](https://dblp.org/img/orcid-mark.12x12.png):

HardGAN: A Haze-Aware Representation Distillation GAN for Single Image Dehazing. [ECCV (6)2020](https://dblp.org/db/conf/eccv/eccv2020-6.html#conf/eccv/DengHTL20): 722-738
- ![](https://dblp.org/img/n.png)

\[i1\]
[Codruta O. Ancuti](https://dblp.org/pid/89/5661.html), [Cosmin Ancuti](https://dblp.org/pid/82/3581.html), [Florin-Alexandru Vasluianu](https://dblp.org/pid/264/5871.html), [Radu Timofte](https://dblp.org/pid/24/8616.html), [Jing Liu](https://dblp.org/pid/72/2590-31.html), [Haiyan Wu](https://dblp.org/pid/11/3756.html), [Yuan Xie](https://dblp.org/pid/157/8128-6.html), [Yanyun Qu](https://dblp.org/pid/03/3500.html), [Lizhuang Ma](https://dblp.org/pid/10/4950.html), [Ziling Huang](https://dblp.org/pid/150/6487.html), Qili Deng, [Ju-Chin Chao](https://dblp.org/pid/264/5933.html), [Tsung-Shan Yang](https://dblp.org/pid/220/4388.html), [Peng-Wen Chen](https://dblp.org/pid/51/6708-1.html), [Po-Min Hsu](https://dblp.org/pid/137/4146.html), [Tzu-Yi Liao](https://dblp.org/pid/76/7881.html), [Chung-En Sun](https://dblp.org/pid/264/5788.html), [Pei-Yuan Wu](https://dblp.org/pid/75/9983.html), [Jeonghyeok Do](https://dblp.org/pid/264/5902.html), [Jongmin Park](https://dblp.org/pid/50/6848.html), [Munchurl Kim](https://dblp.org/pid/84/4965.html), [Kareem M. Metwaly](https://dblp.org/pid/199/8217.html), [Xuelu Li](https://dblp.org/pid/52/8508.html), [Tiantong Guo](https://dblp.org/pid/198/9637.html), [Vishal Monga](https://dblp.org/pid/73/1467.html), [Mingzhao Yu](https://dblp.org/pid/190/9384.html), [Venkateswararao Cherukuri](https://dblp.org/pid/223/6285.html), [Shiue-Yuan Chuang](https://dblp.org/pid/264/5905.html), [Tsung-Nan Lin](https://dblp.org/pid/67/859.html), [David Lee](https://dblp.org/pid/76/1630.html), [Jerome Chang](https://dblp.org/pid/166/0846.html), [Zhan-Han Wang](https://dblp.org/pid/264/5909.html), [Yu-Bang Chang](https://dblp.org/pid/137/3561.html), [Chang-Hong Lin](https://dblp.org/pid/117/7803.html), [Yu Dong](https://dblp.org/pid/03/1299.html), [Hongyu Zhou](https://dblp.org/pid/76/7825.html), [Xiangzhen Kong](https://dblp.org/pid/80/531.html), [Sourya Dipta Das](https://dblp.org/pid/217/1530.html), [Saikat Dutta](https://dblp.org/pid/146/7991-2.html), [Xuan Zhao](https://dblp.org/pid/24/3533.html), [Bing Ouyang](https://dblp.org/pid/169/0821.html), [Dennis Estrada](https://dblp.org/pid/264/5849.html), [Meiqi Wang](https://dblp.org/pid/225/1521.html), [Tianqi Su](https://dblp.org/pid/217/7200.html), [Siyi Chen](https://dblp.org/pid/195/3147-4.html), [Bangyong Sun](https://dblp.org/pid/182/4739.html), [Vincent Jacob Whannou de Dravo](https://dblp.org/pid/182/4665.html), [Zhe Yu](https://dblp.org/pid/32/9128.html), [Pratik Narang](https://dblp.org/pid/132/9397.html), [Aryan Mehra](https://dblp.org/pid/264/5889.html), [Navaneeth Raghunath](https://dblp.org/pid/264/5782.html), [Murari Mandal](https://dblp.org/pid/175/8628.html):

NTIRE 2020 Challenge on NonHomogeneous Dehazing. [CoRRabs/2005.03457](https://dblp.org/db/journals/corr/corr2005.html#journals/corr/abs-2005-03457) (2020)
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2018
- ![](https://dblp.org/img/n.png)

\[j1\]
Qili Deng, [Shuai Wu](https://dblp.org/pid/37/5253-1.html), [Jie Wen](https://dblp.org/pid/77/3796-1.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yong Xu](https://dblp.org/pid/07/4630-1.html):

Multi-level image representation for large-scale image-based instance retrieval. [CAAI Trans. Intell. Technol.3(1)](https://dblp.org/db/journals/caaitrit/caaitrit3.html#journals/caaitrit/DengWWX18): 33-39 (2018)
- _no results_

automatic loading of the coauthor graph disabled due to its size.

**click here to**
**load the graph.**

Note that this feature is _work in progress_ and that it is still far from being perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/246/9797.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Mohamed H. Abdelpakey](https://dblp.org/pid/227/2772.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[2](https://dblp.org/pid/246/9797.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Codruta O. Ancuti](https://dblp.org/pid/89/5661.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[3](https://dblp.org/pid/246/9797.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Cosmin Ancuti](https://dblp.org/pid/82/3581.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[4](https://dblp.org/pid/246/9797.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Kang Ben](https://dblp.org/pid/340/0959.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[5](https://dblp.org/pid/246/9797.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[6](https://dblp.org/pid/246/9797.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Johanna Björklund](https://dblp.org/pid/75/5525.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[7](https://dblp.org/pid/246/9797.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Dingding Cai](https://dblp.org/pid/198/1127.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[8](https://dblp.org/pid/246/9797.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[9](https://dblp.org/pid/246/9797.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Llukman Cerkezi](https://dblp.org/pid/208/1312.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[10](https://dblp.org/pid/246/9797.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Hakan Çevikalp](https://dblp.org/pid/14/6210.html)

aka: Hakan Cevikalp

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[11](https://dblp.org/pid/246/9797.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xuezhi Chai](https://dblp.org/pid/02/10433.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[12](https://dblp.org/pid/246/9797.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Hong Chang 0001](https://dblp.org/pid/02/2689-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[13](https://dblp.org/pid/246/9797.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[14](https://dblp.org/pid/246/9797.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jerome Chang](https://dblp.org/pid/166/0846.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[15](https://dblp.org/pid/246/9797.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yu-Bang Chang](https://dblp.org/pid/137/3561.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[16](https://dblp.org/pid/246/9797.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Ju-Chin Chao](https://dblp.org/pid/264/5933.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[17](https://dblp.org/pid/246/9797.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Bo Chen](https://dblp.org/pid/89/5615.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[18](https://dblp.org/pid/246/9797.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Fangmin Chen](https://dblp.org/pid/320/5863.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[19](https://dblp.org/pid/246/9797.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Guangqi Chen](https://dblp.org/pid/178/8116.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[20](https://dblp.org/pid/246/9797.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Hang Chen](https://dblp.org/pid/87/3677.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[21](https://dblp.org/pid/246/9797.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jiaye Chen](https://dblp.org/pid/116/2901.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[22](https://dblp.org/pid/246/9797.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Peng-Wen Chen 0001](https://dblp.org/pid/51/6708-1.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[23](https://dblp.org/pid/246/9797.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[24](https://dblp.org/pid/246/9797.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Siyi Chen 0004](https://dblp.org/pid/195/3147-4.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[25](https://dblp.org/pid/246/9797.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xilin Chen 0001](https://dblp.org/pid/c/XilinChen.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[26](https://dblp.org/pid/246/9797.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[27](https://dblp.org/pid/246/9797.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiuyi Chen](https://dblp.org/pid/218/7190.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[28](https://dblp.org/pid/246/9797.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yiwei Chen](https://dblp.org/pid/28/2965.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[29](https://dblp.org/pid/246/9797.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yu-Hsi Chen](https://dblp.org/pid/127/3933.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[30](https://dblp.org/pid/246/9797.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhixing Chen](https://dblp.org/pid/62/3074.html)

[\[c5\]](https://dblp.org/pid/246/9797.html#c5) [\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[31](https://dblp.org/pid/246/9797.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Miao Cheng](https://dblp.org/pid/79/7377.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[32](https://dblp.org/pid/246/9797.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yangming Cheng](https://dblp.org/pid/340/1285.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[33](https://dblp.org/pid/246/9797.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Ziyi Cheng](https://dblp.org/pid/290/9342.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[34](https://dblp.org/pid/246/9797.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Venkateswararao Cherukuri](https://dblp.org/pid/223/6285.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[35](https://dblp.org/pid/246/9797.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yu-Chen Chiu](https://dblp.org/pid/199/2494.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[36](https://dblp.org/pid/246/9797.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shiue-Yuan Chuang](https://dblp.org/pid/264/5905.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[37](https://dblp.org/pid/246/9797.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Angelo Ciaramella](https://dblp.org/pid/37/6845.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[38](https://dblp.org/pid/246/9797.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Ozgun Cirakman](https://dblp.org/pid/86/8843.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[39](https://dblp.org/pid/246/9797.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[40](https://dblp.org/pid/246/9797.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[41](https://dblp.org/pid/246/9797.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Kenan Dai](https://dblp.org/pid/250/4445.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[42](https://dblp.org/pid/246/9797.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[43](https://dblp.org/pid/246/9797.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Sourya Dipta Das](https://dblp.org/pid/217/1530.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[44](https://dblp.org/pid/246/9797.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[45](https://dblp.org/pid/246/9797.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Debajyoti Dhar](https://dblp.org/pid/128/3182.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[46](https://dblp.org/pid/246/9797.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shangzhe Di](https://dblp.org/pid/304/1344.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[47](https://dblp.org/pid/246/9797.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jeonghyeok Do](https://dblp.org/pid/264/5902.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[48](https://dblp.org/pid/246/9797.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xingping Dong](https://dblp.org/pid/156/3020.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[49](https://dblp.org/pid/246/9797.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yongsheng Dong](https://dblp.org/pid/70/9613.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[50](https://dblp.org/pid/246/9797.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yu Dong](https://dblp.org/pid/03/1299.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[51](https://dblp.org/pid/246/9797.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Vincent Jacob Whannou de Dravo](https://dblp.org/pid/182/4665.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[52](https://dblp.org/pid/246/9797.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[53](https://dblp.org/pid/246/9797.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2) [\[c5\]](https://dblp.org/pid/246/9797.html#c5) [\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[54](https://dblp.org/pid/246/9797.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[55](https://dblp.org/pid/246/9797.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Saikat Dutta 0002](https://dblp.org/pid/146/7991-2.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[56](https://dblp.org/pid/246/9797.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Benjamin Dzubur](https://dblp.org/pid/340/1520.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[57](https://dblp.org/pid/246/9797.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Dennis Estrada](https://dblp.org/pid/264/5849.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[58](https://dblp.org/pid/246/9797.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Heng Fan 0001](https://dblp.org/pid/20/10120-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[59](https://dblp.org/pid/246/9797.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[60](https://dblp.org/pid/246/9797.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[61](https://dblp.org/pid/246/9797.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhiyong Feng 0001](https://dblp.org/pid/48/195-1.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[62](https://dblp.org/pid/246/9797.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[63](https://dblp.org/pid/246/9797.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Mingtao Fu](https://dblp.org/pid/254/1780.html)

[\[c5\]](https://dblp.org/pid/246/9797.html#c5)

[64](https://dblp.org/pid/246/9797.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c5\]](https://dblp.org/pid/246/9797.html#c5) [\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[65](https://dblp.org/pid/246/9797.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhiye Fu](https://dblp.org/pid/311/1840.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[66](https://dblp.org/pid/246/9797.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shang Gao 0012](https://dblp.org/pid/28/435-12.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[67](https://dblp.org/pid/246/9797.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yiming Gao](https://dblp.org/pid/370/7119.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[68](https://dblp.org/pid/246/9797.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yuan Gao](https://dblp.org/pid/76/2452.html)

[\[c5\]](https://dblp.org/pid/246/9797.html#c5)

[69](https://dblp.org/pid/246/9797.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shiming Ge](https://dblp.org/pid/93/8104.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[70](https://dblp.org/pid/246/9797.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[71](https://dblp.org/pid/246/9797.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[72](https://dblp.org/pid/246/9797.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Eric Granger](https://dblp.org/pid/86/2306.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[73](https://dblp.org/pid/246/9797.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Q. H. Gu](https://dblp.org/pid/340/1209.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[74](https://dblp.org/pid/246/9797.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yuzhang Gu](https://dblp.org/pid/122/3790.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[75](https://dblp.org/pid/246/9797.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Bilge Günsel](https://dblp.org/pid/47/5125.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[76](https://dblp.org/pid/246/9797.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Qing Guo 0005](https://dblp.org/pid/25/3038-5.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[77](https://dblp.org/pid/246/9797.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Tiantong Guo](https://dblp.org/pid/198/9637.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[78](https://dblp.org/pid/246/9797.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Himanshu Gupta 0003](https://dblp.org/pid/330/0760-3.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[79](https://dblp.org/pid/246/9797.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Filiz Gurkan](https://dblp.org/pid/202/7040.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[80](https://dblp.org/pid/246/9797.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Gustav Häger](https://dblp.org/pid/157/3602.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[81](https://dblp.org/pid/246/9797.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Wencheng Han](https://dblp.org/pid/280/3348.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[82](https://dblp.org/pid/246/9797.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jianfeng He](https://dblp.org/pid/93/8352.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[83](https://dblp.org/pid/246/9797.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Keji He](https://dblp.org/pid/319/4518.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[84](https://dblp.org/pid/246/9797.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Qian He](https://dblp.org/pid/69/6357.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[85](https://dblp.org/pid/246/9797.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Po-Min Hsu](https://dblp.org/pid/137/4146.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[86](https://dblp.org/pid/246/9797.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiwei Hu](https://dblp.org/pid/255/6325.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[87](https://dblp.org/pid/246/9797.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yan Huang 0008](https://dblp.org/pid/75/6434-8.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[88](https://dblp.org/pid/246/9797.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yanyan Huang](https://dblp.org/pid/88/4316.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[89](https://dblp.org/pid/246/9797.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Ziling Huang](https://dblp.org/pid/150/6487.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[c1\]](https://dblp.org/pid/246/9797.html#c1) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[90](https://dblp.org/pid/246/9797.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Deepak Jangid](https://dblp.org/pid/340/1460.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[91](https://dblp.org/pid/246/9797.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shang-Jhih Jhang](https://dblp.org/pid/254/4535.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[92](https://dblp.org/pid/246/9797.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[93](https://dblp.org/pid/246/9797.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[94](https://dblp.org/pid/246/9797.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yi Jiang](https://dblp.org/pid/66/3172.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[95](https://dblp.org/pid/246/9797.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[96](https://dblp.org/pid/246/9797.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Felix Juefei-Xu](https://dblp.org/pid/35/11103.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[97](https://dblp.org/pid/246/9797.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[98](https://dblp.org/pid/246/9797.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Ze Kang](https://dblp.org/pid/340/1063.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[99](https://dblp.org/pid/246/9797.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jani Käpylä](https://dblp.org/pid/244/2529.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[100](https://dblp.org/pid/246/9797.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiao Ke](https://dblp.org/pid/78/9040.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[101](https://dblp.org/pid/246/9797.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Fahad Shahbaz Khan](https://dblp.org/pid/05/8618.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[102](https://dblp.org/pid/246/9797.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Byeong Hak Kim](https://dblp.org/pid/214/8978.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[103](https://dblp.org/pid/246/9797.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Munchurl Kim](https://dblp.org/pid/84/4965.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[104](https://dblp.org/pid/246/9797.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Madhu Kiran](https://dblp.org/pid/39/10281.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[105](https://dblp.org/pid/246/9797.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[106](https://dblp.org/pid/246/9797.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiangzhen Kong](https://dblp.org/pid/80/531.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[107](https://dblp.org/pid/246/9797.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[108](https://dblp.org/pid/246/9797.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Simiao Lai](https://dblp.org/pid/282/1954.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[109](https://dblp.org/pid/246/9797.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[110](https://dblp.org/pid/246/9797.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[111](https://dblp.org/pid/246/9797.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[David Lee](https://dblp.org/pid/76/1630.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[112](https://dblp.org/pid/246/9797.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Dongwook Lee](https://dblp.org/pid/25/6543.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[113](https://dblp.org/pid/246/9797.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Hyunjeong Lee](https://dblp.org/pid/00/3423.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[114](https://dblp.org/pid/246/9797.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jun Ha Lee](https://dblp.org/pid/260/2774.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[115](https://dblp.org/pid/246/9797.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Seohyung Lee](https://dblp.org/pid/210/4662.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[116](https://dblp.org/pid/246/9797.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Bastian Leibe](https://dblp.org/pid/41/1228.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[117](https://dblp.org/pid/246/9797.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[118](https://dblp.org/pid/246/9797.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[119](https://dblp.org/pid/246/9797.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jianhua Li](https://dblp.org/pid/93/3389.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[120](https://dblp.org/pid/246/9797.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Ming Li 0010](https://dblp.org/pid/l/MingLi10.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[121](https://dblp.org/pid/246/9797.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Wangkai Li](https://dblp.org/pid/340/1456.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[122](https://dblp.org/pid/246/9797.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xi Li 0001](https://dblp.org/pid/46/2311-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[123](https://dblp.org/pid/246/9797.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xian Li](https://dblp.org/pid/82/1763.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[124](https://dblp.org/pid/246/9797.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[125](https://dblp.org/pid/246/9797.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiao Li](https://dblp.org/pid/66/2069.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[126](https://dblp.org/pid/246/9797.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xuelu Li](https://dblp.org/pid/52/8508.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[127](https://dblp.org/pid/246/9797.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yuezhou Li](https://dblp.org/pid/284/2562.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[128](https://dblp.org/pid/246/9797.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhe Li 0008](https://dblp.org/pid/11/751-8.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[129](https://dblp.org/pid/246/9797.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Tzu-Yi Liao](https://dblp.org/pid/76/7881.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[130](https://dblp.org/pid/246/9797.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chang-Hong Lin](https://dblp.org/pid/117/7803.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[131](https://dblp.org/pid/246/9797.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chia-Wen Lin](https://dblp.org/pid/l/ChiaWenLin.html)

[\[c1\]](https://dblp.org/pid/246/9797.html#c1)

[132](https://dblp.org/pid/246/9797.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Liting Lin](https://dblp.org/pid/227/2204.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[133](https://dblp.org/pid/246/9797.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Tsungnan Lin](https://dblp.org/pid/67/859.html)

aka: Tsung-Nan Lin

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[134](https://dblp.org/pid/246/9797.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Haibin Ling](https://dblp.org/pid/93/3488.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[135](https://dblp.org/pid/246/9797.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Akide Liu](https://dblp.org/pid/323/5463.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[136](https://dblp.org/pid/246/9797.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[137](https://dblp.org/pid/246/9797.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[138](https://dblp.org/pid/246/9797.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jing Liu 0031](https://dblp.org/pid/72/2590-31.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[139](https://dblp.org/pid/246/9797.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jingen Liu](https://dblp.org/pid/10/5849.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[140](https://dblp.org/pid/246/9797.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jiyang Liu](https://dblp.org/pid/222/7550.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[141](https://dblp.org/pid/246/9797.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Li Liu 0036](https://dblp.org/pid/33/4528-36.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[142](https://dblp.org/pid/246/9797.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Mingcong Liu](https://dblp.org/pid/228/8844.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[143](https://dblp.org/pid/246/9797.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Peng Liu](https://dblp.org/pid/21/6121.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[144](https://dblp.org/pid/246/9797.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Qingjie Liu 0001](https://dblp.org/pid/72/10584.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[145](https://dblp.org/pid/246/9797.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Si Liu 0001](https://dblp.org/pid/60/7642.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[146](https://dblp.org/pid/246/9797.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yiheng Liu](https://dblp.org/pid/232/3139.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[147](https://dblp.org/pid/246/9797.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[148](https://dblp.org/pid/246/9797.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Wei Lu](https://dblp.org/pid/98/6613.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[149](https://dblp.org/pid/246/9797.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jonathon Luiten](https://dblp.org/pid/211/7992.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[150](https://dblp.org/pid/246/9797.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[151](https://dblp.org/pid/246/9797.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Bingpeng Ma](https://dblp.org/pid/62/1822.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[152](https://dblp.org/pid/246/9797.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chao Ma 0004](https://dblp.org/pid/79/1552-4.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[153](https://dblp.org/pid/246/9797.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[154](https://dblp.org/pid/246/9797.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Lizhuang Ma](https://dblp.org/pid/10/4950.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[155](https://dblp.org/pid/246/9797.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yinchao Ma](https://dblp.org/pid/189/1326.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[156](https://dblp.org/pid/246/9797.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Ziang Ma](https://dblp.org/pid/165/9621.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[157](https://dblp.org/pid/246/9797.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Murari Mandal](https://dblp.org/pid/175/8628.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[158](https://dblp.org/pid/246/9797.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[159](https://dblp.org/pid/246/9797.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[160](https://dblp.org/pid/246/9797.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[161](https://dblp.org/pid/246/9797.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Aryan Mehra](https://dblp.org/pid/264/5889.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[162](https://dblp.org/pid/246/9797.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[163](https://dblp.org/pid/246/9797.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Kareem M. Metwaly](https://dblp.org/pid/199/8217.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[164](https://dblp.org/pid/246/9797.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[165](https://dblp.org/pid/246/9797.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Payman Moallem](https://dblp.org/pid/63/5378.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[166](https://dblp.org/pid/246/9797.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Vishal Monga](https://dblp.org/pid/73/1467.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[167](https://dblp.org/pid/246/9797.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Pratik Narang](https://dblp.org/pid/132/9397.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[168](https://dblp.org/pid/246/9797.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[169](https://dblp.org/pid/246/9797.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[170](https://dblp.org/pid/246/9797.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yuzhen Niu](https://dblp.org/pid/28/7442.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[171](https://dblp.org/pid/246/9797.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Bing Ouyang](https://dblp.org/pid/169/0821.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[172](https://dblp.org/pid/246/9797.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Siyang Pan](https://dblp.org/pid/250/5753.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[173](https://dblp.org/pid/246/9797.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[ChangBeom Park](https://dblp.org/pid/340/0926.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[174](https://dblp.org/pid/246/9797.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jongmin Park](https://dblp.org/pid/50/6848.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[175](https://dblp.org/pid/246/9797.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[176](https://dblp.org/pid/246/9797.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Matthieu Paul](https://dblp.org/pid/255/6113.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[177](https://dblp.org/pid/246/9797.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[178](https://dblp.org/pid/246/9797.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[179](https://dblp.org/pid/246/9797.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhongqi Qi](https://dblp.org/pid/365/8222.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[180](https://dblp.org/pid/246/9797.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shoumeng Qiu](https://dblp.org/pid/284/2537.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[181](https://dblp.org/pid/246/9797.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Liao Qu](https://dblp.org/pid/299/1491.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[182](https://dblp.org/pid/246/9797.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yanyun Qu](https://dblp.org/pid/03/3500.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[183](https://dblp.org/pid/246/9797.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Navaneeth Raghunath](https://dblp.org/pid/264/5782.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[184](https://dblp.org/pid/246/9797.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Aravindh Rajiv](https://dblp.org/pid/307/9144.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[185](https://dblp.org/pid/246/9797.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Muhammad Rana](https://dblp.org/pid/276/0222.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[186](https://dblp.org/pid/246/9797.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[187](https://dblp.org/pid/246/9797.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Litu Rout](https://dblp.org/pid/206/6445.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[188](https://dblp.org/pid/246/9797.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Hasan Saribas](https://dblp.org/pid/225/3263.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[189](https://dblp.org/pid/246/9797.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[190](https://dblp.org/pid/246/9797.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jie Shao](https://dblp.org/pid/02/5139.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[191](https://dblp.org/pid/246/9797.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Ling Shao 0001](https://dblp.org/pid/75/1281.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[192](https://dblp.org/pid/246/9797.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Mohamed S. Shehata](https://dblp.org/pid/33/2495.html)

aka: Mohamed Shehata 0001

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[193](https://dblp.org/pid/246/9797.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Furao Shen](https://dblp.org/pid/80/4685.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[194](https://dblp.org/pid/246/9797.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jianbing Shen](https://dblp.org/pid/38/5435.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[195](https://dblp.org/pid/246/9797.html?view=joint&param=195 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[196](https://dblp.org/pid/246/9797.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Tianhui Song](https://dblp.org/pid/181/8738.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[197](https://dblp.org/pid/246/9797.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[198](https://dblp.org/pid/246/9797.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yangyang Song](https://dblp.org/pid/57/7453.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[199](https://dblp.org/pid/246/9797.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Tianqi Su](https://dblp.org/pid/217/7200.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[200](https://dblp.org/pid/246/9797.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Bangyong Sun](https://dblp.org/pid/182/4739.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[201](https://dblp.org/pid/246/9797.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chao Sun](https://dblp.org/pid/54/3957.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[202](https://dblp.org/pid/246/9797.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chung-En Sun](https://dblp.org/pid/264/5788.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[203](https://dblp.org/pid/246/9797.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jingna Sun](https://dblp.org/pid/255/0702.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[204](https://dblp.org/pid/246/9797.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shikun Sun](https://dblp.org/pid/293/2733.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[205](https://dblp.org/pid/246/9797.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[206](https://dblp.org/pid/246/9797.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3) [\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[207](https://dblp.org/pid/246/9797.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Philip Torr 0001](https://dblp.org/pid/t/PhilipHSTorr.html)

aka: Philip H. S. Torr

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[208](https://dblp.org/pid/246/9797.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[209](https://dblp.org/pid/246/9797.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chung-Chi Tsai](https://dblp.org/pid/52/10137.html)

[\[c1\]](https://dblp.org/pid/246/9797.html#c1)

[210](https://dblp.org/pid/246/9797.html?view=joint&param=210 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Bedirhan Uzun](https://dblp.org/pid/247/8937.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[211](https://dblp.org/pid/246/9797.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Florin-Alexandru Vasluianu](https://dblp.org/pid/264/5871.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[212](https://dblp.org/pid/246/9797.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Om Prakash Verma](https://dblp.org/pid/61/8145.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[213](https://dblp.org/pid/246/9797.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Paul Voigtlaender](https://dblp.org/pid/166/6430.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[214](https://dblp.org/pid/246/9797.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[215](https://dblp.org/pid/246/9797.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Fei Wang 0032](https://dblp.org/pid/52/3194-32.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[216](https://dblp.org/pid/246/9797.html?view=joint&param=216 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Guangting Wang](https://dblp.org/pid/227/7195.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[217](https://dblp.org/pid/246/9797.html?view=joint&param=217 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Liang Wang 0001](https://dblp.org/pid/56/4499-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[218](https://dblp.org/pid/246/9797.html?view=joint&param=218 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[219](https://dblp.org/pid/246/9797.html?view=joint&param=219 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[220](https://dblp.org/pid/246/9797.html?view=joint&param=220 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[221](https://dblp.org/pid/246/9797.html?view=joint&param=221 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Linyuan Wang](https://dblp.org/pid/138/5963.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[222](https://dblp.org/pid/246/9797.html?view=joint&param=222 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Meiqi Wang](https://dblp.org/pid/225/1521.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[223](https://dblp.org/pid/246/9797.html?view=joint&param=223 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Qiang Wang 0023](https://dblp.org/pid/64/5630-23.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[224](https://dblp.org/pid/246/9797.html?view=joint&param=224 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shuai Wang](https://dblp.org/pid/42/1503.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[225](https://dblp.org/pid/246/9797.html?view=joint&param=225 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xu Wang](https://dblp.org/pid/181/2815.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[226](https://dblp.org/pid/246/9797.html?view=joint&param=226 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yitong Wang](https://dblp.org/pid/58/111.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[227](https://dblp.org/pid/246/9797.html?view=joint&param=227 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yong Wang 0032](https://dblp.org/pid/84/2694-32.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[228](https://dblp.org/pid/246/9797.html?view=joint&param=228 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yunhong Wang 0001](https://dblp.org/pid/95/6251.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[229](https://dblp.org/pid/246/9797.html?view=joint&param=229 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhan-Han Wang](https://dblp.org/pid/264/5909.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[230](https://dblp.org/pid/246/9797.html?view=joint&param=230 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhao Wang](https://dblp.org/pid/86/981.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[231](https://dblp.org/pid/246/9797.html?view=joint&param=231 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jie Wen 0001](https://dblp.org/pid/77/3796-1.html)

[\[j1\]](https://dblp.org/pid/246/9797.html#j1)

[232](https://dblp.org/pid/246/9797.html?view=joint&param=232 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chenyan Wu](https://dblp.org/pid/76/1190.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[233](https://dblp.org/pid/246/9797.html?view=joint&param=233 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[234](https://dblp.org/pid/246/9797.html?view=joint&param=234 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Haiyan Wu](https://dblp.org/pid/11/3756.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[235](https://dblp.org/pid/246/9797.html?view=joint&param=235 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jinlin Wu](https://dblp.org/pid/123/7200.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[236](https://dblp.org/pid/246/9797.html?view=joint&param=236 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Pei Yuan Wu](https://dblp.org/pid/75/9983.html)

aka: Pei-Yuan Wu

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[237](https://dblp.org/pid/246/9797.html?view=joint&param=237 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shuai Wu 0001](https://dblp.org/pid/37/5253-1.html)

[\[j1\]](https://dblp.org/pid/246/9797.html#j1)

[238](https://dblp.org/pid/246/9797.html?view=joint&param=238 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[239](https://dblp.org/pid/246/9797.html?view=joint&param=239 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xinglong Wu](https://dblp.org/pid/269/4913.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[240](https://dblp.org/pid/246/9797.html?view=joint&param=240 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhihua Wu](https://dblp.org/pid/81/6301.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[241](https://dblp.org/pid/246/9797.html?view=joint&param=241 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[242](https://dblp.org/pid/246/9797.html?view=joint&param=242 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yuan Xie 0006](https://dblp.org/pid/157/8128-6.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[243](https://dblp.org/pid/246/9797.html?view=joint&param=243 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Linjie Xing](https://dblp.org/pid/182/2172.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[244](https://dblp.org/pid/246/9797.html?view=joint&param=244 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[245](https://dblp.org/pid/246/9797.html?view=joint&param=245 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Wei Xu 0017](https://dblp.org/pid/32/1213-17.html)

[\[c5\]](https://dblp.org/pid/246/9797.html#c5) [\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[246](https://dblp.org/pid/246/9797.html?view=joint&param=246 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiang Xu](https://dblp.org/pid/126/2962.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[247](https://dblp.org/pid/246/9797.html?view=joint&param=247 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yong Xu 0001](https://dblp.org/pid/07/4630-1.html)

[\[j1\]](https://dblp.org/pid/246/9797.html#j1)

[248](https://dblp.org/pid/246/9797.html?view=joint&param=248 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yong Xu 0007](https://dblp.org/pid/07/4630-7.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[249](https://dblp.org/pid/246/9797.html?view=joint&param=249 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yuanyou Xu](https://dblp.org/pid/248/7663.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[250](https://dblp.org/pid/246/9797.html?view=joint&param=250 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[251](https://dblp.org/pid/246/9797.html?view=joint&param=251 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zizheng Xun](https://dblp.org/pid/340/1441.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[252](https://dblp.org/pid/246/9797.html?view=joint&param=252 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[253](https://dblp.org/pid/246/9797.html?view=joint&param=253 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[254](https://dblp.org/pid/246/9797.html?view=joint&param=254 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Dawei Yang](https://dblp.org/pid/22/1038.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[255](https://dblp.org/pid/246/9797.html?view=joint&param=255 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[256](https://dblp.org/pid/246/9797.html?view=joint&param=256 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Tsung-Shan Yang](https://dblp.org/pid/220/4388.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[257](https://dblp.org/pid/246/9797.html?view=joint&param=257 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[258](https://dblp.org/pid/246/9797.html?view=joint&param=258 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Wenyan Yang](https://dblp.org/pid/119/2426.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[259](https://dblp.org/pid/246/9797.html?view=joint&param=259 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[260](https://dblp.org/pid/246/9797.html?view=joint&param=260 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yi Yang 0001](https://dblp.org/pid/33/4854-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[261](https://dblp.org/pid/246/9797.html?view=joint&param=261 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yichun Yang](https://dblp.org/pid/249/9678.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[262](https://dblp.org/pid/246/9797.html?view=joint&param=262 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhipeng Yang](https://dblp.org/pid/18/1726.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[263](https://dblp.org/pid/246/9797.html?view=joint&param=263 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zongxin Yang](https://dblp.org/pid/249/5456.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[264](https://dblp.org/pid/246/9797.html?view=joint&param=264 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Botao Ye](https://dblp.org/pid/227/4610.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[265](https://dblp.org/pid/246/9797.html?view=joint&param=265 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Hu Ye](https://dblp.org/pid/201/8427.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[266](https://dblp.org/pid/246/9797.html?view=joint&param=266 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yu Ye 0004](https://dblp.org/pid/129/0969-4.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[267](https://dblp.org/pid/246/9797.html?view=joint&param=267 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[J. Yin](https://dblp.org/pid/51/2242.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[268](https://dblp.org/pid/246/9797.html?view=joint&param=268 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jun Yin 0003](https://dblp.org/pid/58/5423-3.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[269](https://dblp.org/pid/246/9797.html?view=joint&param=269 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Fisher Yu 0001](https://dblp.org/pid/117/6314.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[270](https://dblp.org/pid/246/9797.html?view=joint&param=270 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Hongyuan Yu](https://dblp.org/pid/232/2265.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[271](https://dblp.org/pid/246/9797.html?view=joint&param=271 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jiaqian Yu](https://dblp.org/pid/164/7325.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[272](https://dblp.org/pid/246/9797.html?view=joint&param=272 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Mingzhao Yu](https://dblp.org/pid/190/9384.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[273](https://dblp.org/pid/246/9797.html?view=joint&param=273 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Qianjin Yu](https://dblp.org/pid/53/10179.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[274](https://dblp.org/pid/246/9797.html?view=joint&param=274 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Weichen Yu](https://dblp.org/pid/325/1209.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[275](https://dblp.org/pid/246/9797.html?view=joint&param=275 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhe Yu](https://dblp.org/pid/32/9128.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[276](https://dblp.org/pid/246/9797.html?view=joint&param=276 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zehuan Yuan](https://dblp.org/pid/227/3298.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[277](https://dblp.org/pid/246/9797.html?view=joint&param=277 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Kang Ze](https://dblp.org/pid/340/1107.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[278](https://dblp.org/pid/246/9797.html?view=joint&param=278 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jiang Zhai](https://dblp.org/pid/291/9340.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[279](https://dblp.org/pid/246/9797.html?view=joint&param=279 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[280](https://dblp.org/pid/246/9797.html?view=joint&param=280 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chunhu Zhang](https://dblp.org/pid/292/0953.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[281](https://dblp.org/pid/246/9797.html?view=joint&param=281 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Chunhui Zhang 0001](https://dblp.org/pid/62/3401-1.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[282](https://dblp.org/pid/246/9797.html?view=joint&param=282 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Haitao Zhang](https://dblp.org/pid/19/6669.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[283](https://dblp.org/pid/246/9797.html?view=joint&param=283 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Huichao Zhang](https://dblp.org/pid/204/1974.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[284](https://dblp.org/pid/246/9797.html?view=joint&param=284 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[285](https://dblp.org/pid/246/9797.html?view=joint&param=285 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Kangkai Zhang](https://dblp.org/pid/260/2990.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[286](https://dblp.org/pid/246/9797.html?view=joint&param=286 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Tianzhu Zhang 0001](https://dblp.org/pid/15/7643-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[287](https://dblp.org/pid/246/9797.html?view=joint&param=287 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Wenkang Zhang](https://dblp.org/pid/340/0966.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[288](https://dblp.org/pid/246/9797.html?view=joint&param=288 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiaohan Zhang](https://dblp.org/pid/96/6053.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[289](https://dblp.org/pid/246/9797.html?view=joint&param=289 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xiaolin Zhang](https://dblp.org/pid/99/2516.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[290](https://dblp.org/pid/246/9797.html?view=joint&param=290 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xijin Zhang](https://dblp.org/pid/242/9085.html)

[\[c5\]](https://dblp.org/pid/246/9797.html#c5)

[291](https://dblp.org/pid/246/9797.html?view=joint&param=291 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xinyu Zhang 0020](https://dblp.org/pid/58/4582-20.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[292](https://dblp.org/pid/246/9797.html?view=joint&param=292 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yi Zhang](https://dblp.org/pid/64/6544.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[293](https://dblp.org/pid/246/9797.html?view=joint&param=293 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yushan Zhang](https://dblp.org/pid/50/10702.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[294](https://dblp.org/pid/246/9797.html?view=joint&param=294 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[295](https://dblp.org/pid/246/9797.html?view=joint&param=295 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhipeng Zhang](https://dblp.org/pid/49/4941.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[296](https://dblp.org/pid/246/9797.html?view=joint&param=296 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[297](https://dblp.org/pid/246/9797.html?view=joint&param=297 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jie Zhao 0014](https://dblp.org/pid/23/3168-14.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[298](https://dblp.org/pid/246/9797.html?view=joint&param=298 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[299](https://dblp.org/pid/246/9797.html?view=joint&param=299 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xuan Zhao](https://dblp.org/pid/24/3533.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[300](https://dblp.org/pid/246/9797.html?view=joint&param=300 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Ming Zhen](https://dblp.org/pid/307/8430.html)

[\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[301](https://dblp.org/pid/246/9797.html?view=joint&param=301 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Feng Zheng 0001](https://dblp.org/pid/39/800-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[302](https://dblp.org/pid/246/9797.html?view=joint&param=302 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Haixia Zheng](https://dblp.org/pid/119/1585.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[303](https://dblp.org/pid/246/9797.html?view=joint&param=303 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Min Zheng](https://dblp.org/pid/23/328.html)

[\[c5\]](https://dblp.org/pid/246/9797.html#c5) [\[c4\]](https://dblp.org/pid/246/9797.html#c4)

[304](https://dblp.org/pid/246/9797.html?view=joint&param=304 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[305](https://dblp.org/pid/246/9797.html?view=joint&param=305 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Hongyu Zhou](https://dblp.org/pid/76/7825.html)

[\[c2\]](https://dblp.org/pid/246/9797.html#c2) [\[i1\]](https://dblp.org/pid/246/9797.html#i1)

[306](https://dblp.org/pid/246/9797.html?view=joint&param=306 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yang Zhou](https://dblp.org/pid/07/4580.html)

[\[i2\]](https://dblp.org/pid/246/9797.html#i2)

[307](https://dblp.org/pid/246/9797.html?view=joint&param=307 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[308](https://dblp.org/pid/246/9797.html?view=joint&param=308 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4) [\[c3\]](https://dblp.org/pid/246/9797.html#c3)

[309](https://dblp.org/pid/246/9797.html?view=joint&param=309 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/246/9797.html?view=group&param=1)

[Yueting Zhuang](https://dblp.org/pid/218/7793.html)

[\[c4\]](https://dblp.org/pid/246/9797.html#c4)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/246/9797.html#) [\[–\]](https://dblp.org/pid/246/9797.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/246/9797.html#) [\[–\]](https://dblp.org/pid/246/9797.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/246/9797.html#) [\[–\]](https://dblp.org/pid/246/9797.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/246/9797.html#) [\[–\]](https://dblp.org/pid/246/9797.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/246/9797.html#) [\[–\]](https://dblp.org/pid/246/9797.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)