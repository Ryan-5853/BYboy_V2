> 抓取来源：https://dblp.org/pid/248/7663.html

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

- [highly cited coauthors](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+coauthors+of+Yuanyou+Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fcoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F248%2F7663%3E+%7D%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A++OPTIONAL+%7B+%3Fcoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fpubl+dblp%3Aomid+%3Fomid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fomid+.%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcoauthor%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited other authors](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Yuanyou+Xu+do+also+cite+author+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F248%2F7663%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29+.%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [non-coauthors with many coauthors in common](https://sparql.dblp.org/?exec=true&query=%23%23+Non-coauthors+of+Yuanyou+Xu+with+many+coauthors+in+common%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28DISTINCT+%3Fcoauthor%29+AS+%3Fcount%29+%28%3Fcocoauthor+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F248%2F7663%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcoauthor+%29+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcoauthor+.%0A++%3Fcopubl+dblp%3AauthoredBy+%3Fcocoauthor+.%0A++FILTER+%28+%3Fauthor+%21%3D+%3Fcocoauthor+%29+.%0A++MINUS+%7B+%3Fcocopubl+dblp%3AauthoredBy+%3Fauthor+.+%3Fcocopubl+dblp%3AauthoredBy+%3Fcocoauthor+%7D%0A++%3Fcocoauthor+rdfs%3Alabel+%3Fname+.%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fcocoauthor+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fcocoauthor%0AORDER+BY+DESC%28%3Fcount%29%0ALIMIT+10)
- [highly cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Highly+cited+publications+by+Yuanyou+Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fcite%29+as+%3Fcites%29+%28%3Fpubl+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+WHERE+%7B%0A++VALUES+%3Fauthor+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F248%2F7663%3E+%7D%0A++%3Fpubl+dblp%3AauthoredBy+%3Fauthor+.%0A++%3Fpubl+rdfs%3Alabel+%3Flabel+.%0A++%3Fpubl+dblp%3Aomid+%3Fomids+.%0A++OPTIONAL+%7B+%3Fcite+cito%3AhasCitedEntity+%3Fomids+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++OPTIONAL+%7B+%3Fpubl+dblp%3Adoi+%3Fdois+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fpubl%0AORDER+BY+DESC%28%3Fcites%29%0ALIMIT+10)
- [co-cited publications](https://sparql.dblp.org/?exec=true&query=%23%23+Papers+that+cite+Yuanyou+Xu+do+also+cite+paper+...%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+schema%3A+%3Chttps%3A%2F%2Fschema.org%2F%3E%0ASELECT+%3Flabel+%3Fyear+%28COUNT%28DISTINCT+%3Fother_cite%29+as+%3Ffreq%29+%28%3Fother_publ+as+%3Fdblp%29+%28SAMPLE%28%3Fdois%29+as+%3Fdoi%29+%3Furl+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F248%2F7663%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fthis_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitingEntity+%3Fsource_omid+.%0A++%3Fother_cite+cito%3AhasCitedEntity+%3Fother_omid+.%0A++FILTER%28+%3Fother_omid+%21%3D+%3Fthis_omid+%29+.%0A++OPTIONAL+%7B%0A++++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++++%3Fother_publ+rdfs%3Alabel+%3Flabel+.%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3AyearOfPublication+%3Fyear+.+%7D%0A++++OPTIONAL+%7B+%3Fother_publ+dblp%3Adoi+%3Fdois+.+%7D%0A++%7D%0A++MINUS+%7B+%3Fother_publ+dblp%3AauthoredBy+%3Fthis_pers+.+%7D%0A++OPTIONAL+%7B+%3Fother_omid+schema%3Aurl+%3Furl+.+%7D%0A%7D%0AGROUP+BY+%3Flabel+%3Fyear+%3Fother_publ+%3Furl%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [authors citing this author](https://sparql.dblp.org/?exec=true&query=%23%23+Who+is+citing+Yuanyou+Xu%3F%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0APREFIX+cito%3A+%3Chttp%3A%2F%2Fpurl.org%2Fspar%2Fcito%2F%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0ASELECT+%3Fname+%3Faffiliation+%28COUNT%28%3Fother_pers%29+as+%3Ffreq%29+%28%3Fother_pers+as+%3Fdblp%29+%28SAMPLE%28%3Forcids%29+as+%3Forcid%29+WHERE+%7B%0A++VALUES+%3Fthis_pers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F248%2F7663%3E+%7D+.%0A++%3Fthis_publ+dblp%3AauthoredBy+%3Fthis_pers+.%0A++%3Fthis_publ+dblp%3Aomid+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitedEntity+%3Fthis_omid+.%0A++%3Fcite+cito%3AhasCitingEntity+%3Fother_omid+.%0A++%3Fother_publ+dblp%3Aomid+%3Fother_omid+.%0A++%3Fother_publ+dblp%3AauthoredBy+%3Fother_pers+.%0A++FILTER%28+%3Fother_pers+%21%3D+%3Fthis_pers+%29%0A++%3Fother_pers+dblp%3AprimaryCreatorName+%3Fname+.%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3AprimaryAffiliation+%3Faffiliation+.+%7D%0A++OPTIONAL+%7B+%3Fother_pers+dblp%3Aorcid+%3Forcids+.+%7D%0A%7D%0AGROUP+BY+%3Fname+%3Faffiliation+%3Fother_pers%0AORDER+BY+DESC%28%3Ffreq%29%0ALIMIT+10)
- [number of authors per paper](https://sparql.dblp.org/?exec=true&query=%23%23+Number-of-authors+statistic+for+Yuanyou+Xu%0APREFIX+dblp%3A+%3Chttps%3A%2F%2Fdblp.org%2Frdf%2Fschema%23%3E%0ASELECT+%3Fnumber_of_authors+%28COUNT%28%3Fnumber_of_authors%29+AS+%3Ffreq%29+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F248%2F7663%3E+%7D+.%0A++%3Fpubl+dblp%3AauthoredBy+%3Fpers+.%0A++%3Fpubl+dblp%3AnumberOfCreators+%3Fnumber_of_authors+.%0A%7D%0AGROUP+BY+%3Fnumber_of_authors%0AORDER+BY+%3Fnumber_of_authors)

[_or build your own?_](https://sparql.dblp.org/?query=SELECT+%2A+WHERE+%7B%0A++VALUES+%3Fpers+%7B+%3Chttps%3A%2F%2Fdblp.org%2Fpid%2F248%2F7663%3E+%7D+.%0A%0A%7D)

_showing all13 records_

2016202652019: 12022: 12023: 92023: 92024: 12025: 1

**refine by search term**

![](https://dblp.org/img/clear-mark.medium.16x16.png)![filter active](https://dblp.org/img/filter-mark.12x12.png)

**refine by type**

- [ ] Conference and Workshop Papers(only)
- [ ] Informal and Other Publications(only)

- select all \| deselect all

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by coauthor**

- ![](https://dblp.org/img/add-mark.12x12.png)Zongxin Yang (12)
- ![](https://dblp.org/img/add-mark.12x12.png)Yi Yang 0001 (12)
- ![](https://dblp.org/img/add-mark.12x12.png)Yueting Zhuang (4)
- ![](https://dblp.org/img/add-mark.12x12.png)Jiahao Li 0005 (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Yangming Cheng (3)
- ![](https://dblp.org/img/add-mark.12x12.png)Keji He (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Dawei Yang (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Hyung Jin Chang (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Zhongqun Zhang (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Yushan Zhang (2)

- _230 more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by orcid**

- ![](https://dblp.org/img/add-mark.12x12.png)no orcid (13)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by venue**

- ![](https://dblp.org/img/add-mark.12x12.png)Comput. Res. Repos. (7)
- ![](https://dblp.org/img/add-mark.12x12.png)ICCV (2)
- ![](https://dblp.org/img/add-mark.12x12.png)ECCV (2)
- ![](https://dblp.org/img/add-mark.12x12.png)Lect. Notes Comput. Sci. (2)
- ![](https://dblp.org/img/add-mark.12x12.png)CVPR (1)
- ![](https://dblp.org/img/add-mark.12x12.png)IJCAI (1)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

**refine by access**![](https://dblp.org/img/faq-mark.dark.12x12.png)

- ![](https://dblp.org/img/add-mark.12x12.png)open (9)
- ![](https://dblp.org/img/add-mark.12x12.png)closed (4)

- _more options_

- _no options_

- ![](https://dblp.org/img/waiting.anim.gif)

- _temporarily not available_

![](https://dblp.org/img/waiting.anim.gif)

- 2025
- ![](https://dblp.org/img/n.png)

\[c6\]
Yuanyou Xu, [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html):

SKDream: Controllable Multi-view and 3D Generation with Arbitrary Skeletons. [CVPR2025](https://dblp.org/db/conf/cvpr/cvpr2025.html#conf/cvpr/XuY025): 314-325
- 2024
- ![](https://dblp.org/img/n.png)

\[c5\]
Yuanyou Xu, [Zongxin Yang](https://dblp.org/pid/249/5456.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yi Yang](https://dblp.org/pid/33/4854-1.html):

Photorealistic Text-to-3D Avatar Generation with Constrained Geometry and Appearance. [ECCV Workshops (12)2024](https://dblp.org/db/conf/eccv/eccv2024-w12.html#conf/eccv/XuYY24): 397-405
- 2023
- ![](https://dblp.org/img/n.png)

\[c4\]
Yuanyou Xu, [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html):

Integrating Boxes and Masks: A Multi-Object Framework for Unified Visual Tracking and Segmentation. [ICCV2023](https://dblp.org/db/conf/iccv/iccv2023.html#conf/iccv/XuYY23): 9704-9717
- ![](https://dblp.org/img/n.png)

\[c3\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Khanh-Tung Tran](https://dblp.org/pid/359/3793.html), [Xuan-Son Vu](https://dblp.org/pid/151/8673.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Lei Ke](https://dblp.org/pid/26/5225.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Noor Al-Shakarji](https://dblp.org/pid/188/7419.html), [Dong An](https://dblp.org/pid/02/7028.html), [Michael Arens](https://dblp.org/pid/69/5391.html), [Stefan Becker](https://dblp.org/pid/62/7091.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Sebastian Bullinger](https://dblp.org/pid/197/9724.html), [Antoni B. Chan](https://dblp.org/pid/55/5814.html), [Shijie Chang](https://dblp.org/pid/277/8125.html), [Hanyuan Chen](https://dblp.org/pid/363/8621.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Yan Chen](https://dblp.org/pid/88/2827-17.html), [Zhenyu Chen](https://dblp.org/pid/86/541-1.html), [Yangming Cheng](https://dblp.org/pid/340/1285.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Chunyuan Deng](https://dblp.org/pid/154/4071.html), [Jiahua Dong](https://dblp.org/pid/247/5746.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Wei Feng](https://dblp.org/pid/17/1152-5.html), [Jianlong Fu](https://dblp.org/pid/83/8692.html), [Jie Gao](https://dblp.org/pid/181/2794.html), [Ruize Han](https://dblp.org/pid/205/4022.html), [Zeqi Hao](https://dblp.org/pid/348/8961.html), [Jun-Yan He](https://dblp.org/pid/173/3747.html), [Keji He](https://dblp.org/pid/319/4518.html), [Zhenyu He](https://dblp.org/pid/57/6240-1.html), [Xiantao Hu](https://dblp.org/pid/160/8016.html), [Kaer Huang](https://dblp.org/pid/317/0780.html), [Yuqing Huang](https://dblp.org/pid/134/5853.html), [Yi Jiang](https://dblp.org/pid/66/3172-4.html), [Ben Kang](https://dblp.org/pid/340/1671.html), [Jin-Peng Lan](https://dblp.org/pid/332/1033.html), [Hyungjun Lee](https://dblp.org/pid/324/8911.html), [Chenyang Li](https://dblp.org/pid/15/1523-7.html), [Jiahao Li](https://dblp.org/pid/150/5524-5.html), [Ning Li](https://dblp.org/pid/14/5410-44.html), [Wangkai Li](https://dblp.org/pid/340/1456.html), [Xiaodi Li](https://dblp.org/pid/63/7279.html), [Xin Li](https://dblp.org/pid/09/1365-34.html), [Pengyu Liu](https://dblp.org/pid/73/7783-5.html), [Yue Liu](https://dblp.org/pid/74/1932.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Bin Luo](https://dblp.org/pid/36/4256-8.html), [Ping Luo](https://dblp.org/pid/54/4989-2.html), [Yinchao Ma](https://dblp.org/pid/189/1326.html), [Deshui Miao](https://dblp.org/pid/307/5501.html), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Kannappan Palaniappan](https://dblp.org/pid/21/700.html), [Hancheol Park](https://dblp.org/pid/161/3495.html), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Zekun Qian](https://dblp.org/pid/315/4066.html), [Gani Rahmon](https://dblp.org/pid/291/7224.html), [Norbert Scherer-Negenborn](https://dblp.org/pid/45/8662.html), [Pengcheng Shao](https://dblp.org/pid/364/8295.html), [Wooksu Shin](https://dblp.org/pid/327/3602.html), [Elham Soltani Kazemi](https://dblp.org/pid/318/1851.html), [Tianhui Song](https://dblp.org/pid/181/8738.html), [Rainer Stiefelhagen](https://dblp.org/pid/31/4699.html), [Rui Sun](https://dblp.org/pid/01/3595-6.html), [Chuanming Tang](https://dblp.org/pid/237/6254.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html), [Imad Eddine Toubal](https://dblp.org/pid/292/6360.html), [Jack Valmadre](https://dblp.org/pid/50/8535.html), [Joost van de Weijer](https://dblp.org/pid/67/3379.html), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Jash Vira](https://dblp.org/pid/364/8266.html), [Stéphane Vujasinovic](https://dblp.org/pid/237/5053.html), [Cheng Wan](https://dblp.org/pid/118/7267-6.html), [Jia Wan](https://dblp.org/pid/13/6504-1.html), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Feifan Wang](https://dblp.org/pid/213/0685.html), [He Wang](https://dblp.org/pid/01/6368-28.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Song Wang](https://dblp.org/pid/62/3151-2.html), [Yaowei Wang](https://dblp.org/pid/68/2992-1.html), [Zhepeng Wang](https://dblp.org/pid/242/8456-2.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Jiannan Wu](https://dblp.org/pid/277/0616.html), [Qiangqiang Wu](https://dblp.org/pid/193/1415.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Anqi Xiao](https://dblp.org/pid/307/8649.html), [Jinxia Xie](https://dblp.org/pid/294/3376.html), [Chenlong Xu](https://dblp.org/pid/315/8714.html), [Min Xu](https://dblp.org/pid/09/0-1.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), Yuanyou Xu, [Bin Yan](https://dblp.org/pid/92/786-4.html), [Dawei Yang](https://dblp.org/pid/22/1038.html), [Ming-Hsuan Yang](https://dblp.org/pid/79/3711.html), [Tianyu Yang](https://dblp.org/pid/120/8076-3.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Xuanwu Yin](https://dblp.org/pid/119/0001.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Qianjin Yu](https://dblp.org/pid/53/10179.html), [Weichen Yu](https://dblp.org/pid/325/1209.html), [Yongsheng Yuan](https://dblp.org/pid/364/8163.html), [Zehuan Yuan](https://dblp.org/pid/227/3298.html), [Jianlin Zhang](https://dblp.org/pid/37/1545-1.html), [Lu Zhang](https://dblp.org/pid/82/10609-53.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Guodongfang Zhao](https://dblp.org/pid/364/8196.html), [Shaochuan Zhao](https://dblp.org/pid/260/3125.html), [Yaozong Zheng](https://dblp.org/pid/344/6907.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html), [ChengAo Zong](https://dblp.org/pid/364/8208.html), [Kunlong Zuo](https://dblp.org/pid/354/8493.html):

The First Visual Object Tracking Segmentation VOTS2023 Challenge Results. [ICCV (Workshops)2023](https://dblp.org/db/conf/iccvw/iccvw2023.html#conf/iccvw/KristanMDFCZLDZ23): 1788-1810
- ![](https://dblp.org/img/n.png)

\[c2\]
Yuanyou Xu, [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html):

Video Object Segmentation in Panoptic Wild Scenes. [IJCAI2023](https://dblp.org/db/conf/ijcai/ijcai2023.html#conf/ijcai/XuYY23): 1604-1612
- ![](https://dblp.org/img/n.png)

\[i7\]
Yuanyou Xu, [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html):

Video Object Segmentation in Panoptic Wild Scenes. [CoRRabs/2305.04470](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-04470) (2023)
- ![](https://dblp.org/img/n.png)

\[i6\]
[Yangming Cheng](https://dblp.org/pid/340/1285.html), [Liulei Li](https://dblp.org/pid/295/8925.html), Yuanyou Xu, [Xiaodi Li](https://dblp.org/pid/63/7279.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Wenguan Wang](https://dblp.org/pid/145/1078.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html):

Segment and Track Anything. [CoRRabs/2305.06558](https://dblp.org/db/journals/corr/corr2305.html#journals/corr/abs-2305-06558) (2023)
- ![](https://dblp.org/img/n.png)

\[i5\]
[Jiahao Li](https://dblp.org/pid/150/5524-5.html), Yuanyou Xu, [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html):

ZJU ReLER Submission for EPIC-KITCHEN Challenge 2023: Semi-Supervised Video Object Segmentation. [CoRRabs/2307.02010](https://dblp.org/db/journals/corr/corr2307.html#journals/corr/abs-2307-02010) (2023)
- ![](https://dblp.org/img/n.png)

\[i4\]
Yuanyou Xu, [Jiahao Li](https://dblp.org/pid/150/5524-5.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html):

ZJU ReLER Submission for EPIC-KITCHEN Challenge 2023: TREK-150 Single Object Tracking. [CoRRabs/2307.02508](https://dblp.org/db/journals/corr/corr2307.html#journals/corr/abs-2307-02508) (2023)
- ![](https://dblp.org/img/n.png)

\[i3\]
Yuanyou Xu, [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html):

Integrating Boxes and Masks: A Multi-Object Framework for Unified Visual Tracking and Segmentation. [CoRRabs/2308.13266](https://dblp.org/db/journals/corr/corr2308.html#journals/corr/abs-2308-13266) (2023)
- ![](https://dblp.org/img/n.png)

\[i2\]
Yuanyou Xu, [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html):

SEEAvatar: Photorealistic Text-to-3D Avatar Generation with Constrained Geometry and Appearance. [CoRRabs/2312.08889](https://dblp.org/db/journals/corr/corr2312.html#journals/corr/abs-2312-08889) (2023)
- 2022
- ![](https://dblp.org/img/n.png)

\[c1\]
[Matej Kristan](https://dblp.org/pid/79/1648.html), [Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html), [Jirí Matas](https://dblp.org/pid/m/JiriMatas.html), [Michael Felsberg](https://dblp.org/pid/00/78.html), [Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html), [Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Hyung Jin Chang](https://dblp.org/pid/96/3551.html), [Martin Danelljan](https://dblp.org/pid/151/8848.html), [Luka Cehovin Zajc](https://dblp.org/pid/19/8654.html), [Alan Lukezic](https://dblp.org/pid/160/3679.html), [Ondrej Drbohlav](https://dblp.org/pid/79/5367.html), [Johanna Björklund](https://dblp.org/pid/75/5525.html), [Yushan Zhang](https://dblp.org/pid/50/10702.html), [Zhongqun Zhang](https://dblp.org/pid/237/8882.html), [Song Yan](https://dblp.org/pid/58/6692.html), [Wenyan Yang](https://dblp.org/pid/119/2426.html), [Dingding Cai](https://dblp.org/pid/198/1127.html), [Christoph Mayer](https://dblp.org/pid/163/0032-7.html), [Gustavo Fernández](https://dblp.org/pid/160/3616.html), [Kang Ben](https://dblp.org/pid/340/0959.html), [Goutam Bhat](https://dblp.org/pid/190/7682.html), [Hong Chang](https://dblp.org/pid/02/2689-1.html), [Guangqi Chen](https://dblp.org/pid/178/8116.html), [Jiaye Chen](https://dblp.org/pid/116/2901.html), [Shengyong Chen](https://dblp.org/pid/93/2479.html), [Xilin Chen](https://dblp.org/pid/c/XilinChen.html), [Xin Chen](https://dblp.org/pid/24/1518-32.html), [Xiuyi Chen](https://dblp.org/pid/218/7190.html), [Yiwei Chen](https://dblp.org/pid/28/2965.html), [Yu-Hsi Chen](https://dblp.org/pid/127/3933.html), [Zhixing Chen](https://dblp.org/pid/62/3074.html), [Yangming Cheng](https://dblp.org/pid/340/1285.html), [Angelo Ciaramella](https://dblp.org/pid/37/6845.html), [Yutao Cui](https://dblp.org/pid/255/2385.html), [Benjamin Dzubur](https://dblp.org/pid/340/1520.html), [Mohana Murali Dasari](https://dblp.org/pid/277/5901.html), [Qili Deng](https://dblp.org/pid/246/9797.html), [Debajyoti Dhar](https://dblp.org/pid/128/3182.html), [Shangzhe Di](https://dblp.org/pid/304/1344.html), [Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Daniel K. Du](https://dblp.org/pid/05/10727.html), [Matteo Dunnhofer](https://dblp.org/pid/209/8650.html), [Heng Fan](https://dblp.org/pid/20/10120-1.html), [Zhenhua Feng](https://dblp.org/pid/348/7584-1.html), [Zhihong Fu](https://dblp.org/pid/203/1795.html), [Shang Gao](https://dblp.org/pid/28/435-12.html), [Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html), [Eric Granger](https://dblp.org/pid/86/2306.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Q. H. Gu](https://dblp.org/pid/340/1209.html), [Himanshu Gupta](https://dblp.org/pid/330/0760-3.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Jianfeng He](https://dblp.org/pid/93/8352.html), [Keji He](https://dblp.org/pid/319/4518.html), [Yan Huang](https://dblp.org/pid/75/6434-8.html), [Deepak Jangid](https://dblp.org/pid/340/1460.html), [Rongrong Ji](https://dblp.org/pid/86/5681.html), [Cheng Jiang](https://dblp.org/pid/15/11195-5.html), [Yingjie Jiang](https://dblp.org/pid/214/0119.html), [Felix Järemo Lawin](https://dblp.org/pid/185/0985.html), [Ze Kang](https://dblp.org/pid/340/1063.html), [Madhu Kiran](https://dblp.org/pid/39/10281.html), [Josef Kittler](https://dblp.org/pid/k/JosefKittler.html), [Simiao Lai](https://dblp.org/pid/282/1954.html), [Xiangyuan Lan](https://dblp.org/pid/151/8902.html), [Dongwook Lee](https://dblp.org/pid/25/6543.html), [Hyunjeong Lee](https://dblp.org/pid/00/3423.html), [Seohyung Lee](https://dblp.org/pid/210/4662.html), [Hui Li](https://dblp.org/pid/66/3387-37.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Ming Li](https://dblp.org/pid/l/MingLi10.html), [Wangkai Li](https://dblp.org/pid/340/1456.html), [Xi Li](https://dblp.org/pid/46/2311-1.html), [Xianxian Li](https://dblp.org/pid/81/4000.html), [Xiao Li](https://dblp.org/pid/66/2069.html), [Zhe Li](https://dblp.org/pid/11/751-8.html), [Liting Lin](https://dblp.org/pid/227/2204.html), [Haibin Ling](https://dblp.org/pid/93/3488.html), [Bo Liu](https://dblp.org/pid/58/2670-5.html), [Chang Liu](https://dblp.org/pid/52/5716-71.html), [Si Liu](https://dblp.org/pid/60/7642.html), [Huchuan Lu](https://dblp.org/pid/64/6896.html), [Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html), [Bingpeng Ma](https://dblp.org/pid/62/1822.html), [Chao Ma](https://dblp.org/pid/79/1552-4.html), [Jie Ma](https://dblp.org/pid/62/5110.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Yinchao Ma](https://dblp.org/pid/189/1326.html), [Niki Martinel](https://dblp.org/pid/56/10105.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Alireza Memarmoghadam](https://dblp.org/pid/69/6460.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Christian Micheloni](https://dblp.org/pid/28/38.html), [Payman Moallem](https://dblp.org/pid/63/5378.html), [Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html), [Siyang Pan](https://dblp.org/pid/250/5753.html), [ChangBeom Park](https://dblp.org/pid/340/0926.html), [Danda Pani Paudel](https://dblp.org/pid/151/8836.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Matthieu Paul](https://dblp.org/pid/255/6113.html), [Houwen Peng](https://dblp.org/pid/133/1706.html), [Andreas Robinson](https://dblp.org/pid/158/5786.html), [Litu Rout](https://dblp.org/pid/206/6445.html), [Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html), [Kristian Simonato](https://dblp.org/pid/307/8603.html), [Tianhui Song](https://dblp.org/pid/181/8738.html), [Xiaoning Song](https://dblp.org/pid/82/6511.html), [Chao Sun](https://dblp.org/pid/54/3957.html), [Jingna Sun](https://dblp.org/pid/255/0702.html), [Zhangyong Tang](https://dblp.org/pid/236/3195.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Radu Timofte](https://dblp.org/pid/24/8616.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Luc Van Gool](https://dblp.org/pid/61/5017.html), [Om Prakash Verma](https://dblp.org/pid/61/8145.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Dong Wang](https://dblp.org/pid/40/3934-4.html), [Fei Wang](https://dblp.org/pid/52/3194-32.html), [Liang Wang](https://dblp.org/pid/56/4499-1.html), [Liangliang Wang](https://dblp.org/pid/16/5766.html), [Lijun Wang](https://dblp.org/pid/96/6702.html), [Limin Wang](https://dblp.org/pid/68/6610-2.html), [Qiang Wang](https://dblp.org/pid/64/5630-23.html), [Gangshan Wu](https://dblp.org/pid/78/1123.html), [Jinlin Wu](https://dblp.org/pid/123/7200.html), [Xiaojun Wu](https://dblp.org/pid/13/5168-1.html), [Fei Xie](https://dblp.org/pid/51/1316.html), [Tianyang Xu](https://dblp.org/pid/169/4627.html), [Wei Xu](https://dblp.org/pid/32/1213-17.html), [Yong Xu](https://dblp.org/pid/07/4630-7.html), Yuanyou Xu, [Wanli Xue](https://dblp.org/pid/153/8037.html)![](https://dblp.org/img/orcid-mark.12x12.png), [Zizheng Xun](https://dblp.org/pid/340/1441.html), [Bin Yan](https://dblp.org/pid/92/786-4.html), [Dawei Yang](https://dblp.org/pid/22/1038.html), [Jinyu Yang](https://dblp.org/pid/138/6456.html), [Wankou Yang](https://dblp.org/pid/99/3602.html), [Xiaoyun Yang](https://dblp.org/pid/54/230.html), [Yi Yang](https://dblp.org/pid/33/4854-1.html), [Yichun Yang](https://dblp.org/pid/249/9678.html), [Zongxin Yang](https://dblp.org/pid/249/5456.html), [Botao Ye](https://dblp.org/pid/227/4610.html), [Fisher Yu](https://dblp.org/pid/117/6314.html), [Hongyuan Yu](https://dblp.org/pid/232/2265.html), [Jiaqian Yu](https://dblp.org/pid/164/7325.html), [Qianjin Yu](https://dblp.org/pid/53/10179.html), [Weichen Yu](https://dblp.org/pid/325/1209.html), [Kang Ze](https://dblp.org/pid/340/1107.html), [Jiang Zhai](https://dblp.org/pid/291/9340.html), [Chengwei Zhang](https://dblp.org/pid/129/0954-1.html), [Chunhu Zhang](https://dblp.org/pid/292/0953.html), [Kaihua Zhang](https://dblp.org/pid/84/8017-1.html), [Tianzhu Zhang](https://dblp.org/pid/15/7643-1.html), [Wenkang Zhang](https://dblp.org/pid/340/0966.html), [Zhibin Zhang](https://dblp.org/pid/85/1218.html), [Zhipeng Zhang](https://dblp.org/pid/49/4941.html), [Jie Zhao](https://dblp.org/pid/23/3168-14.html), [Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html), [Feng Zheng](https://dblp.org/pid/39/800-1.html), [Haixia Zheng](https://dblp.org/pid/119/1585.html), [Min Zheng](https://dblp.org/pid/23/328.html), [Bineng Zhong](https://dblp.org/pid/25/1637-1.html), [Jiawen Zhu](https://dblp.org/pid/135/5123-3.html), [Xuefeng Zhu](https://dblp.org/pid/70/6628-3.html), [Yueting Zhuang](https://dblp.org/pid/218/7793.html):

The Tenth Visual Object Tracking VOT2022 Challenge Results. [ECCV Workshops (8)2022](https://dblp.org/db/conf/eccv/eccv2022-w8.html#conf/eccv/KristanLMFPKCDZLDBZZYYCMFBBCCCCCCCCCCC22): 431-460
- _no results_

![](https://dblp.org/img/waiting.anim.gif)

- 2019
- ![](https://dblp.org/img/n.png)

\[i1\]
Yuanyou Xu, [Kaiwei Wang](https://dblp.org/pid/45/11142.html), [Kailun Yang](https://dblp.org/pid/190/9526.html), [Dongming Sun](https://dblp.org/pid/05/7843.html), [Jia Fu](https://dblp.org/pid/33/4686-1.html):

Semantic Segmentation of Panoramic Images Using a Synthetic Dataset. [CoRRabs/1909.00532](https://dblp.org/db/journals/corr/corr1909.html#journals/corr/abs-1909-00532) (2019)
- _no results_

![maximize](https://dblp.org/img/maximize.dark.16x16.png)

Note that this feature is a _work in progress_ and that it is still far from perfect.

![](https://dblp.org/img/waiting.anim.gif)

[1](https://dblp.org/pid/248/7663.html?view=joint&param=1 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Noor Al-Shakarji](https://dblp.org/pid/188/7419.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[2](https://dblp.org/pid/248/7663.html?view=joint&param=2 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Dong An](https://dblp.org/pid/02/7028.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[3](https://dblp.org/pid/248/7663.html?view=joint&param=3 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Michael Arens](https://dblp.org/pid/69/5391.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[4](https://dblp.org/pid/248/7663.html?view=joint&param=4 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Stefan Becker](https://dblp.org/pid/62/7091.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[5](https://dblp.org/pid/248/7663.html?view=joint&param=5 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Kang Ben](https://dblp.org/pid/340/0959.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[6](https://dblp.org/pid/248/7663.html?view=joint&param=6 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Goutam Bhat](https://dblp.org/pid/190/7682.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[7](https://dblp.org/pid/248/7663.html?view=joint&param=7 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Johanna Björklund](https://dblp.org/pid/75/5525.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[8](https://dblp.org/pid/248/7663.html?view=joint&param=8 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Sebastian Bullinger](https://dblp.org/pid/197/9724.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[9](https://dblp.org/pid/248/7663.html?view=joint&param=9 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Dingding Cai](https://dblp.org/pid/198/1127.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[10](https://dblp.org/pid/248/7663.html?view=joint&param=10 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Luka Cehovin](https://dblp.org/pid/19/8654.html)

aka: Luka Cehovin Zajc

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[11](https://dblp.org/pid/248/7663.html?view=joint&param=11 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Antoni B. Chan](https://dblp.org/pid/55/5814.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[12](https://dblp.org/pid/248/7663.html?view=joint&param=12 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Hong Chang 0001](https://dblp.org/pid/02/2689-1.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[13](https://dblp.org/pid/248/7663.html?view=joint&param=13 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Hyung Jin Chang](https://dblp.org/pid/96/3551.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[14](https://dblp.org/pid/248/7663.html?view=joint&param=14 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Shijie Chang](https://dblp.org/pid/277/8125.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[15](https://dblp.org/pid/248/7663.html?view=joint&param=15 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Guangqi Chen](https://dblp.org/pid/178/8116.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[16](https://dblp.org/pid/248/7663.html?view=joint&param=16 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Hanyuan Chen](https://dblp.org/pid/363/8621.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[17](https://dblp.org/pid/248/7663.html?view=joint&param=17 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jiaye Chen](https://dblp.org/pid/116/2901.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[18](https://dblp.org/pid/248/7663.html?view=joint&param=18 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Shengyong Chen](https://dblp.org/pid/93/2479.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[19](https://dblp.org/pid/248/7663.html?view=joint&param=19 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xilin Chen 0001](https://dblp.org/pid/c/XilinChen.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[20](https://dblp.org/pid/248/7663.html?view=joint&param=20 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xin Chen 0032](https://dblp.org/pid/24/1518-32.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[21](https://dblp.org/pid/248/7663.html?view=joint&param=21 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xiuyi Chen](https://dblp.org/pid/218/7190.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[22](https://dblp.org/pid/248/7663.html?view=joint&param=22 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yan Chen 0017](https://dblp.org/pid/88/2827-17.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[23](https://dblp.org/pid/248/7663.html?view=joint&param=23 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yiwei Chen](https://dblp.org/pid/28/2965.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[24](https://dblp.org/pid/248/7663.html?view=joint&param=24 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yu-Hsi Chen](https://dblp.org/pid/127/3933.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[25](https://dblp.org/pid/248/7663.html?view=joint&param=25 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zhenyu Chen 0001](https://dblp.org/pid/86/541-1.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[26](https://dblp.org/pid/248/7663.html?view=joint&param=26 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zhixing Chen](https://dblp.org/pid/62/3074.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[27](https://dblp.org/pid/248/7663.html?view=joint&param=27 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yangming Cheng](https://dblp.org/pid/340/1285.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[i6\]](https://dblp.org/pid/248/7663.html#i6) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[28](https://dblp.org/pid/248/7663.html?view=joint&param=28 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Angelo Ciaramella](https://dblp.org/pid/37/6845.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[29](https://dblp.org/pid/248/7663.html?view=joint&param=29 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Rafael M. O. Cruz](https://dblp.org/pid/05/10069.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[30](https://dblp.org/pid/248/7663.html?view=joint&param=30 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yutao Cui](https://dblp.org/pid/255/2385.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[31](https://dblp.org/pid/248/7663.html?view=joint&param=31 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Martin Danelljan](https://dblp.org/pid/151/8848.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[32](https://dblp.org/pid/248/7663.html?view=joint&param=32 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Mohana Murali Dasari](https://dblp.org/pid/277/5901.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[33](https://dblp.org/pid/248/7663.html?view=joint&param=33 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Chunyuan Deng](https://dblp.org/pid/154/4071.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[34](https://dblp.org/pid/248/7663.html?view=joint&param=34 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Qili Deng](https://dblp.org/pid/246/9797.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[35](https://dblp.org/pid/248/7663.html?view=joint&param=35 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Debajyoti Dhar](https://dblp.org/pid/128/3182.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[36](https://dblp.org/pid/248/7663.html?view=joint&param=36 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Shangzhe Di](https://dblp.org/pid/304/1344.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[37](https://dblp.org/pid/248/7663.html?view=joint&param=37 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jiahua Dong 0001](https://dblp.org/pid/247/5746.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[38](https://dblp.org/pid/248/7663.html?view=joint&param=38 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Ondrej Drbohlav](https://dblp.org/pid/79/5367.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[39](https://dblp.org/pid/248/7663.html?view=joint&param=39 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Daniel K. Du](https://dblp.org/pid/05/10727.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[40](https://dblp.org/pid/248/7663.html?view=joint&param=40 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Matteo Dunnhofer](https://dblp.org/pid/209/8650.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[41](https://dblp.org/pid/248/7663.html?view=joint&param=41 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Benjamin Dzubur](https://dblp.org/pid/340/1520.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[42](https://dblp.org/pid/248/7663.html?view=joint&param=42 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Heng Fan 0001](https://dblp.org/pid/20/10120-1.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[43](https://dblp.org/pid/248/7663.html?view=joint&param=43 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Michael Felsberg](https://dblp.org/pid/00/78.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[44](https://dblp.org/pid/248/7663.html?view=joint&param=44 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Wei Feng 0005](https://dblp.org/pid/17/1152-5.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[45](https://dblp.org/pid/248/7663.html?view=joint&param=45 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zhenhua Feng 0001](https://dblp.org/pid/348/7584-1.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[46](https://dblp.org/pid/248/7663.html?view=joint&param=46 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Gustavo Fernández](https://dblp.org/pid/160/3616.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[47](https://dblp.org/pid/248/7663.html?view=joint&param=47 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jia Fu 0001](https://dblp.org/pid/33/4686-1.html)

[\[i1\]](https://dblp.org/pid/248/7663.html#i1)

[48](https://dblp.org/pid/248/7663.html?view=joint&param=48 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jianlong Fu](https://dblp.org/pid/83/8692.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[49](https://dblp.org/pid/248/7663.html?view=joint&param=49 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zhihong Fu](https://dblp.org/pid/203/1795.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[50](https://dblp.org/pid/248/7663.html?view=joint&param=50 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jie Gao](https://dblp.org/pid/181/2794.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[51](https://dblp.org/pid/248/7663.html?view=joint&param=51 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Shang Gao 0012](https://dblp.org/pid/28/435-12.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[52](https://dblp.org/pid/248/7663.html?view=joint&param=52 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Luc Van Gool](https://dblp.org/pid/61/5017.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[53](https://dblp.org/pid/248/7663.html?view=joint&param=53 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Rama Krishna Gorthi](https://dblp.org/pid/307/8696.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[54](https://dblp.org/pid/248/7663.html?view=joint&param=54 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Eric Granger](https://dblp.org/pid/86/2306.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[55](https://dblp.org/pid/248/7663.html?view=joint&param=55 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Q. H. Gu](https://dblp.org/pid/340/1209.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[56](https://dblp.org/pid/248/7663.html?view=joint&param=56 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Himanshu Gupta 0003](https://dblp.org/pid/330/0760-3.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[57](https://dblp.org/pid/248/7663.html?view=joint&param=57 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Rui-Ze Han](https://dblp.org/pid/205/4022.html)

aka: Ruize Han

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[58](https://dblp.org/pid/248/7663.html?view=joint&param=58 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zeqi Hao](https://dblp.org/pid/348/8961.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[59](https://dblp.org/pid/248/7663.html?view=joint&param=59 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jianfeng He](https://dblp.org/pid/93/8352.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[60](https://dblp.org/pid/248/7663.html?view=joint&param=60 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jun-Yan He](https://dblp.org/pid/173/3747.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[61](https://dblp.org/pid/248/7663.html?view=joint&param=61 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Keji He](https://dblp.org/pid/319/4518.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[62](https://dblp.org/pid/248/7663.html?view=joint&param=62 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zhenyu He 0001](https://dblp.org/pid/57/6240-1.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[63](https://dblp.org/pid/248/7663.html?view=joint&param=63 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xiantao Hu](https://dblp.org/pid/160/8016.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[64](https://dblp.org/pid/248/7663.html?view=joint&param=64 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Kaer Huang](https://dblp.org/pid/317/0780.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[65](https://dblp.org/pid/248/7663.html?view=joint&param=65 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yan Huang 0008](https://dblp.org/pid/75/6434-8.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[66](https://dblp.org/pid/248/7663.html?view=joint&param=66 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yuqing Huang](https://dblp.org/pid/134/5853.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[67](https://dblp.org/pid/248/7663.html?view=joint&param=67 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Deepak Jangid](https://dblp.org/pid/340/1460.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[68](https://dblp.org/pid/248/7663.html?view=joint&param=68 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Rongrong Ji](https://dblp.org/pid/86/5681.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[69](https://dblp.org/pid/248/7663.html?view=joint&param=69 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Cheng Jiang 0005](https://dblp.org/pid/15/11195-5.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[70](https://dblp.org/pid/248/7663.html?view=joint&param=70 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yi Jiang 0004](https://dblp.org/pid/66/3172-4.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[71](https://dblp.org/pid/248/7663.html?view=joint&param=71 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yingjie Jiang](https://dblp.org/pid/214/0119.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[72](https://dblp.org/pid/248/7663.html?view=joint&param=72 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Joni-Kristian Kämäräinen](https://dblp.org/pid/k/JoniKristianKamarainen.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[73](https://dblp.org/pid/248/7663.html?view=joint&param=73 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Ben Kang](https://dblp.org/pid/340/1671.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[74](https://dblp.org/pid/248/7663.html?view=joint&param=74 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Ze Kang](https://dblp.org/pid/340/1063.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[75](https://dblp.org/pid/248/7663.html?view=joint&param=75 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Lei Ke](https://dblp.org/pid/26/5225.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[76](https://dblp.org/pid/248/7663.html?view=joint&param=76 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Madhu Kiran](https://dblp.org/pid/39/10281.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[77](https://dblp.org/pid/248/7663.html?view=joint&param=77 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Josef Kittler](https://dblp.org/pid/k/JosefKittler.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[78](https://dblp.org/pid/248/7663.html?view=joint&param=78 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Matej Kristan](https://dblp.org/pid/79/1648.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[79](https://dblp.org/pid/248/7663.html?view=joint&param=79 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Simiao Lai](https://dblp.org/pid/282/1954.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[80](https://dblp.org/pid/248/7663.html?view=joint&param=80 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jin-Peng Lan](https://dblp.org/pid/332/1033.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[81](https://dblp.org/pid/248/7663.html?view=joint&param=81 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xiangyuan Lan](https://dblp.org/pid/151/8902.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[82](https://dblp.org/pid/248/7663.html?view=joint&param=82 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Felix Järemo Lawin](https://dblp.org/pid/185/0985.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[83](https://dblp.org/pid/248/7663.html?view=joint&param=83 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Dongwook Lee](https://dblp.org/pid/25/6543.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[84](https://dblp.org/pid/248/7663.html?view=joint&param=84 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Hyungjun Lee](https://dblp.org/pid/324/8911.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[85](https://dblp.org/pid/248/7663.html?view=joint&param=85 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Hyunjeong Lee](https://dblp.org/pid/00/3423.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[86](https://dblp.org/pid/248/7663.html?view=joint&param=86 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Seohyung Lee](https://dblp.org/pid/210/4662.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[87](https://dblp.org/pid/248/7663.html?view=joint&param=87 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Ales Leonardis](https://dblp.org/pid/l/AlesLeonardis.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[88](https://dblp.org/pid/248/7663.html?view=joint&param=88 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Chenyang Li 0007](https://dblp.org/pid/15/1523-7.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[89](https://dblp.org/pid/248/7663.html?view=joint&param=89 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Hui Li 0037](https://dblp.org/pid/66/3387-37.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[90](https://dblp.org/pid/248/7663.html?view=joint&param=90 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jiahao Li 0005](https://dblp.org/pid/150/5524-5.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[i5\]](https://dblp.org/pid/248/7663.html#i5) [\[i4\]](https://dblp.org/pid/248/7663.html#i4)

[91](https://dblp.org/pid/248/7663.html?view=joint&param=91 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Liulei Li](https://dblp.org/pid/295/8925.html)

[\[i6\]](https://dblp.org/pid/248/7663.html#i6)

[92](https://dblp.org/pid/248/7663.html?view=joint&param=92 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Ming Li 0010](https://dblp.org/pid/l/MingLi10.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[93](https://dblp.org/pid/248/7663.html?view=joint&param=93 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Ning Li 0044](https://dblp.org/pid/14/5410-44.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[94](https://dblp.org/pid/248/7663.html?view=joint&param=94 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Wangkai Li](https://dblp.org/pid/340/1456.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[95](https://dblp.org/pid/248/7663.html?view=joint&param=95 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xi Li 0001](https://dblp.org/pid/46/2311-1.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[96](https://dblp.org/pid/248/7663.html?view=joint&param=96 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xianxian Li](https://dblp.org/pid/81/4000.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[97](https://dblp.org/pid/248/7663.html?view=joint&param=97 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xiao Li](https://dblp.org/pid/66/2069.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[98](https://dblp.org/pid/248/7663.html?view=joint&param=98 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xiaodi Li](https://dblp.org/pid/63/7279.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[i6\]](https://dblp.org/pid/248/7663.html#i6)

[99](https://dblp.org/pid/248/7663.html?view=joint&param=99 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xin Li 0034](https://dblp.org/pid/09/1365-34.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[100](https://dblp.org/pid/248/7663.html?view=joint&param=100 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zhe Li 0008](https://dblp.org/pid/11/751-8.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[101](https://dblp.org/pid/248/7663.html?view=joint&param=101 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Liting Lin](https://dblp.org/pid/227/2204.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[102](https://dblp.org/pid/248/7663.html?view=joint&param=102 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Haibin Ling](https://dblp.org/pid/93/3488.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[103](https://dblp.org/pid/248/7663.html?view=joint&param=103 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Bo Liu 0005](https://dblp.org/pid/58/2670-5.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[104](https://dblp.org/pid/248/7663.html?view=joint&param=104 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Chang Liu 0071](https://dblp.org/pid/52/5716-71.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[105](https://dblp.org/pid/248/7663.html?view=joint&param=105 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Pengyu Liu 0005](https://dblp.org/pid/73/7783-5.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[106](https://dblp.org/pid/248/7663.html?view=joint&param=106 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Si Liu 0001](https://dblp.org/pid/60/7642.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[107](https://dblp.org/pid/248/7663.html?view=joint&param=107 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yue Liu](https://dblp.org/pid/74/1932.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[108](https://dblp.org/pid/248/7663.html?view=joint&param=108 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Huchuan Lu](https://dblp.org/pid/64/6896.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[109](https://dblp.org/pid/248/7663.html?view=joint&param=109 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Alan Lukezic](https://dblp.org/pid/160/3679.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[110](https://dblp.org/pid/248/7663.html?view=joint&param=110 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Bin Luo 0008](https://dblp.org/pid/36/4256-8.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[111](https://dblp.org/pid/248/7663.html?view=joint&param=111 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Ping Luo 0002](https://dblp.org/pid/54/4989-2.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[112](https://dblp.org/pid/248/7663.html?view=joint&param=112 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Bingpeng Ma](https://dblp.org/pid/62/1822.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[113](https://dblp.org/pid/248/7663.html?view=joint&param=113 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Chao Ma 0004](https://dblp.org/pid/79/1552-4.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[114](https://dblp.org/pid/248/7663.html?view=joint&param=114 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jie Ma](https://dblp.org/pid/62/5110.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[115](https://dblp.org/pid/248/7663.html?view=joint&param=115 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yinchao Ma](https://dblp.org/pid/189/1326.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[116](https://dblp.org/pid/248/7663.html?view=joint&param=116 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Niki Martinel](https://dblp.org/pid/56/10105.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[117](https://dblp.org/pid/248/7663.html?view=joint&param=117 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jiri Matas](https://dblp.org/pid/m/JiriMatas.html)

aka: Jirí Matas

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[118](https://dblp.org/pid/248/7663.html?view=joint&param=118 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Christoph Mayer 0007](https://dblp.org/pid/163/0032-7.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[119](https://dblp.org/pid/248/7663.html?view=joint&param=119 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Alireza Memarmoghaddam](https://dblp.org/pid/69/6460.html)

aka: Alireza Memarmoghadam

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[120](https://dblp.org/pid/248/7663.html?view=joint&param=120 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Deshui Miao](https://dblp.org/pid/307/5501.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[121](https://dblp.org/pid/248/7663.html?view=joint&param=121 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Christian Micheloni](https://dblp.org/pid/28/38.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[122](https://dblp.org/pid/248/7663.html?view=joint&param=122 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Payman Moallem](https://dblp.org/pid/63/5378.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[123](https://dblp.org/pid/248/7663.html?view=joint&param=123 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Emanuel Di Nardo](https://dblp.org/pid/198/9412.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[124](https://dblp.org/pid/248/7663.html?view=joint&param=124 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Le Thanh Nguyen-Meidine](https://dblp.org/pid/216/4088.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[125](https://dblp.org/pid/248/7663.html?view=joint&param=125 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Kannappan Palaniappan](https://dblp.org/pid/21/700.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[126](https://dblp.org/pid/248/7663.html?view=joint&param=126 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Siyang Pan](https://dblp.org/pid/250/5753.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[127](https://dblp.org/pid/248/7663.html?view=joint&param=127 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[ChangBeom Park](https://dblp.org/pid/340/0926.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[128](https://dblp.org/pid/248/7663.html?view=joint&param=128 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Hancheol Park](https://dblp.org/pid/161/3495.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[129](https://dblp.org/pid/248/7663.html?view=joint&param=129 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Danda Pani Paudel](https://dblp.org/pid/151/8836.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[130](https://dblp.org/pid/248/7663.html?view=joint&param=130 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Matthieu Paul](https://dblp.org/pid/255/6113.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[131](https://dblp.org/pid/248/7663.html?view=joint&param=131 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Houwen Peng](https://dblp.org/pid/133/1706.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[132](https://dblp.org/pid/248/7663.html?view=joint&param=132 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Roman P. Pflugfelder](https://dblp.org/pid/35/2836.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[133](https://dblp.org/pid/248/7663.html?view=joint&param=133 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zekun Qian](https://dblp.org/pid/315/4066.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[134](https://dblp.org/pid/248/7663.html?view=joint&param=134 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Gani Rahmon](https://dblp.org/pid/291/7224.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[135](https://dblp.org/pid/248/7663.html?view=joint&param=135 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Andreas Robinson](https://dblp.org/pid/158/5786.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[136](https://dblp.org/pid/248/7663.html?view=joint&param=136 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Litu Rout](https://dblp.org/pid/206/6445.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[137](https://dblp.org/pid/248/7663.html?view=joint&param=137 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Norbert Scherer-Negenborn](https://dblp.org/pid/45/8662.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[138](https://dblp.org/pid/248/7663.html?view=joint&param=138 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Shiguang Shan](https://dblp.org/pid/s/ShiguangShan.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[139](https://dblp.org/pid/248/7663.html?view=joint&param=139 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Pengcheng Shao](https://dblp.org/pid/364/8295.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[140](https://dblp.org/pid/248/7663.html?view=joint&param=140 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Wooksu Shin](https://dblp.org/pid/327/3602.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[141](https://dblp.org/pid/248/7663.html?view=joint&param=141 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Kristian Simonato](https://dblp.org/pid/307/8603.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[142](https://dblp.org/pid/248/7663.html?view=joint&param=142 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Elham Soltanikazemi](https://dblp.org/pid/318/1851.html)

aka: Elham Soltani Kazemi

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[143](https://dblp.org/pid/248/7663.html?view=joint&param=143 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Tianhui Song](https://dblp.org/pid/181/8738.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[144](https://dblp.org/pid/248/7663.html?view=joint&param=144 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xiaoning Song](https://dblp.org/pid/82/6511.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[145](https://dblp.org/pid/248/7663.html?view=joint&param=145 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Rainer Stiefelhagen](https://dblp.org/pid/31/4699.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[146](https://dblp.org/pid/248/7663.html?view=joint&param=146 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Chao Sun](https://dblp.org/pid/54/3957.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[147](https://dblp.org/pid/248/7663.html?view=joint&param=147 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Dongming Sun](https://dblp.org/pid/05/7843.html)

[\[i1\]](https://dblp.org/pid/248/7663.html#i1)

[148](https://dblp.org/pid/248/7663.html?view=joint&param=148 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jingna Sun](https://dblp.org/pid/255/0702.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[149](https://dblp.org/pid/248/7663.html?view=joint&param=149 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Rui Sun 0006](https://dblp.org/pid/01/3595-6.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[150](https://dblp.org/pid/248/7663.html?view=joint&param=150 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Chuanming Tang](https://dblp.org/pid/237/6254.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[151](https://dblp.org/pid/248/7663.html?view=joint&param=151 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zhangyong Tang](https://dblp.org/pid/236/3195.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[152](https://dblp.org/pid/248/7663.html?view=joint&param=152 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Radu Timofte](https://dblp.org/pid/24/8616.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[153](https://dblp.org/pid/248/7663.html?view=joint&param=153 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Imad Eddine Toubal](https://dblp.org/pid/292/6360.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[154](https://dblp.org/pid/248/7663.html?view=joint&param=154 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Khanh-Tung Tran](https://dblp.org/pid/359/3793.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[155](https://dblp.org/pid/248/7663.html?view=joint&param=155 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Chi-Yi Tsai](https://dblp.org/pid/25/1650.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[156](https://dblp.org/pid/248/7663.html?view=joint&param=156 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jack Valmadre](https://dblp.org/pid/50/8535.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[157](https://dblp.org/pid/248/7663.html?view=joint&param=157 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Om Prakash Verma](https://dblp.org/pid/61/8145.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[158](https://dblp.org/pid/248/7663.html?view=joint&param=158 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jash Vira](https://dblp.org/pid/364/8266.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[159](https://dblp.org/pid/248/7663.html?view=joint&param=159 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xuan-Son Vu](https://dblp.org/pid/151/8673.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[160](https://dblp.org/pid/248/7663.html?view=joint&param=160 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Stéphane Vujasinovic](https://dblp.org/pid/237/5053.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[161](https://dblp.org/pid/248/7663.html?view=joint&param=161 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Cheng Wan 0006](https://dblp.org/pid/118/7267-6.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[162](https://dblp.org/pid/248/7663.html?view=joint&param=162 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jia Wan 0001](https://dblp.org/pid/13/6504-1.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[163](https://dblp.org/pid/248/7663.html?view=joint&param=163 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Dong Wang 0004](https://dblp.org/pid/40/3934-4.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[164](https://dblp.org/pid/248/7663.html?view=joint&param=164 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Fei Wang 0032](https://dblp.org/pid/52/3194-32.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[165](https://dblp.org/pid/248/7663.html?view=joint&param=165 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Feifan Wang](https://dblp.org/pid/213/0685.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[166](https://dblp.org/pid/248/7663.html?view=joint&param=166 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[He Wang 0028](https://dblp.org/pid/01/6368-28.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[167](https://dblp.org/pid/248/7663.html?view=joint&param=167 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Kaiwei Wang](https://dblp.org/pid/45/11142.html)

[\[i1\]](https://dblp.org/pid/248/7663.html#i1)

[168](https://dblp.org/pid/248/7663.html?view=joint&param=168 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Liang Wang 0001](https://dblp.org/pid/56/4499-1.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[169](https://dblp.org/pid/248/7663.html?view=joint&param=169 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Liangliang Wang](https://dblp.org/pid/16/5766.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[170](https://dblp.org/pid/248/7663.html?view=joint&param=170 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Lijun Wang](https://dblp.org/pid/96/6702.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[171](https://dblp.org/pid/248/7663.html?view=joint&param=171 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Limin Wang 0002](https://dblp.org/pid/68/6610-2.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[172](https://dblp.org/pid/248/7663.html?view=joint&param=172 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Qiang Wang 0023](https://dblp.org/pid/64/5630-23.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[173](https://dblp.org/pid/248/7663.html?view=joint&param=173 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Song Wang 0002](https://dblp.org/pid/62/3151-2.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[174](https://dblp.org/pid/248/7663.html?view=joint&param=174 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Wenguan Wang](https://dblp.org/pid/145/1078.html)

[\[i6\]](https://dblp.org/pid/248/7663.html#i6)

[175](https://dblp.org/pid/248/7663.html?view=joint&param=175 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yaowei Wang 0001](https://dblp.org/pid/68/2992-1.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[176](https://dblp.org/pid/248/7663.html?view=joint&param=176 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zhepeng Wang 0002](https://dblp.org/pid/242/8456-2.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[177](https://dblp.org/pid/248/7663.html?view=joint&param=177 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Joost van de Weijer 0001](https://dblp.org/pid/67/3379.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[178](https://dblp.org/pid/248/7663.html?view=joint&param=178 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Gangshan Wu](https://dblp.org/pid/78/1123.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[179](https://dblp.org/pid/248/7663.html?view=joint&param=179 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jiannan Wu](https://dblp.org/pid/277/0616.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[180](https://dblp.org/pid/248/7663.html?view=joint&param=180 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jinlin Wu](https://dblp.org/pid/123/7200.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[181](https://dblp.org/pid/248/7663.html?view=joint&param=181 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Qiangqiang Wu](https://dblp.org/pid/193/1415.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[182](https://dblp.org/pid/248/7663.html?view=joint&param=182 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xiaojun Wu 0001](https://dblp.org/pid/13/5168-1.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[183](https://dblp.org/pid/248/7663.html?view=joint&param=183 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Anqi Xiao](https://dblp.org/pid/307/8649.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[184](https://dblp.org/pid/248/7663.html?view=joint&param=184 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Fei Xie](https://dblp.org/pid/51/1316.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[185](https://dblp.org/pid/248/7663.html?view=joint&param=185 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jinxia Xie](https://dblp.org/pid/294/3376.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[186](https://dblp.org/pid/248/7663.html?view=joint&param=186 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Chenlong Xu](https://dblp.org/pid/315/8714.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[187](https://dblp.org/pid/248/7663.html?view=joint&param=187 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Min Xu 0001](https://dblp.org/pid/09/0-1.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[188](https://dblp.org/pid/248/7663.html?view=joint&param=188 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Tianyang Xu 0001](https://dblp.org/pid/169/4627.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[189](https://dblp.org/pid/248/7663.html?view=joint&param=189 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Wei Xu 0017](https://dblp.org/pid/32/1213-17.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[190](https://dblp.org/pid/248/7663.html?view=joint&param=190 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yong Xu 0007](https://dblp.org/pid/07/4630-7.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[191](https://dblp.org/pid/248/7663.html?view=joint&param=191 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Wanli Xue](https://dblp.org/pid/153/8037.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[192](https://dblp.org/pid/248/7663.html?view=joint&param=192 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zizheng Xun](https://dblp.org/pid/340/1441.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[193](https://dblp.org/pid/248/7663.html?view=joint&param=193 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Bin Yan 0004](https://dblp.org/pid/92/786-4.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[194](https://dblp.org/pid/248/7663.html?view=joint&param=194 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Song Yan](https://dblp.org/pid/58/6692.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[195](https://dblp.org/pid/248/7663.html?view=joint&param=195 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Dawei Yang](https://dblp.org/pid/22/1038.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[196](https://dblp.org/pid/248/7663.html?view=joint&param=196 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jinyu Yang](https://dblp.org/pid/138/6456.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[197](https://dblp.org/pid/248/7663.html?view=joint&param=197 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Kailun Yang 0001](https://dblp.org/pid/190/9526.html)

[\[i1\]](https://dblp.org/pid/248/7663.html#i1)

[198](https://dblp.org/pid/248/7663.html?view=joint&param=198 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Ming-Hsuan Yang 0001](https://dblp.org/pid/79/3711.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[199](https://dblp.org/pid/248/7663.html?view=joint&param=199 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Tianyu Yang 0003](https://dblp.org/pid/120/8076-3.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[200](https://dblp.org/pid/248/7663.html?view=joint&param=200 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Wankou Yang](https://dblp.org/pid/99/3602.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[201](https://dblp.org/pid/248/7663.html?view=joint&param=201 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Wenyan Yang](https://dblp.org/pid/119/2426.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[202](https://dblp.org/pid/248/7663.html?view=joint&param=202 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xiaoyun Yang](https://dblp.org/pid/54/230.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[203](https://dblp.org/pid/248/7663.html?view=joint&param=203 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yi Yang 0001](https://dblp.org/pid/33/4854-1.html)

[\[c6\]](https://dblp.org/pid/248/7663.html#c6) [\[c5\]](https://dblp.org/pid/248/7663.html#c5) [\[c4\]](https://dblp.org/pid/248/7663.html#c4) [\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c2\]](https://dblp.org/pid/248/7663.html#c2) [\[i7\]](https://dblp.org/pid/248/7663.html#i7) [\[i6\]](https://dblp.org/pid/248/7663.html#i6) [\[i5\]](https://dblp.org/pid/248/7663.html#i5) [\[i4\]](https://dblp.org/pid/248/7663.html#i4) [\[i3\]](https://dblp.org/pid/248/7663.html#i3) [\[i2\]](https://dblp.org/pid/248/7663.html#i2) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[204](https://dblp.org/pid/248/7663.html?view=joint&param=204 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yichun Yang](https://dblp.org/pid/249/9678.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[205](https://dblp.org/pid/248/7663.html?view=joint&param=205 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zongxin Yang](https://dblp.org/pid/249/5456.html)

[\[c6\]](https://dblp.org/pid/248/7663.html#c6) [\[c5\]](https://dblp.org/pid/248/7663.html#c5) [\[c4\]](https://dblp.org/pid/248/7663.html#c4) [\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c2\]](https://dblp.org/pid/248/7663.html#c2) [\[i7\]](https://dblp.org/pid/248/7663.html#i7) [\[i6\]](https://dblp.org/pid/248/7663.html#i6) [\[i5\]](https://dblp.org/pid/248/7663.html#i5) [\[i4\]](https://dblp.org/pid/248/7663.html#i4) [\[i3\]](https://dblp.org/pid/248/7663.html#i3) [\[i2\]](https://dblp.org/pid/248/7663.html#i2) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[206](https://dblp.org/pid/248/7663.html?view=joint&param=206 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Botao Ye](https://dblp.org/pid/227/4610.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[207](https://dblp.org/pid/248/7663.html?view=joint&param=207 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xuanwu Yin](https://dblp.org/pid/119/0001.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[208](https://dblp.org/pid/248/7663.html?view=joint&param=208 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Fisher Yu 0001](https://dblp.org/pid/117/6314.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[209](https://dblp.org/pid/248/7663.html?view=joint&param=209 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Hongyuan Yu](https://dblp.org/pid/232/2265.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[210](https://dblp.org/pid/248/7663.html?view=joint&param=210 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jiaqian Yu](https://dblp.org/pid/164/7325.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[211](https://dblp.org/pid/248/7663.html?view=joint&param=211 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Qianjin Yu](https://dblp.org/pid/53/10179.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[212](https://dblp.org/pid/248/7663.html?view=joint&param=212 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Weichen Yu](https://dblp.org/pid/325/1209.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[213](https://dblp.org/pid/248/7663.html?view=joint&param=213 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yongsheng Yuan](https://dblp.org/pid/364/8163.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[214](https://dblp.org/pid/248/7663.html?view=joint&param=214 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zehuan Yuan](https://dblp.org/pid/227/3298.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[215](https://dblp.org/pid/248/7663.html?view=joint&param=215 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Kang Ze](https://dblp.org/pid/340/1107.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[216](https://dblp.org/pid/248/7663.html?view=joint&param=216 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jiang Zhai](https://dblp.org/pid/291/9340.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[217](https://dblp.org/pid/248/7663.html?view=joint&param=217 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Chengwei Zhang 0001](https://dblp.org/pid/129/0954-1.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[218](https://dblp.org/pid/248/7663.html?view=joint&param=218 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Chunhu Zhang](https://dblp.org/pid/292/0953.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[219](https://dblp.org/pid/248/7663.html?view=joint&param=219 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jianlin Zhang 0001](https://dblp.org/pid/37/1545-1.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[220](https://dblp.org/pid/248/7663.html?view=joint&param=220 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Kaihua Zhang 0001](https://dblp.org/pid/84/8017-1.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[221](https://dblp.org/pid/248/7663.html?view=joint&param=221 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Lu Zhang 0053](https://dblp.org/pid/82/10609-53.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[222](https://dblp.org/pid/248/7663.html?view=joint&param=222 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Tianzhu Zhang 0001](https://dblp.org/pid/15/7643-1.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[223](https://dblp.org/pid/248/7663.html?view=joint&param=223 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Wenkang Zhang](https://dblp.org/pid/340/0966.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[224](https://dblp.org/pid/248/7663.html?view=joint&param=224 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yushan Zhang](https://dblp.org/pid/50/10702.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[225](https://dblp.org/pid/248/7663.html?view=joint&param=225 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zhibin Zhang](https://dblp.org/pid/85/1218.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[226](https://dblp.org/pid/248/7663.html?view=joint&param=226 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zhipeng Zhang](https://dblp.org/pid/49/4941.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[227](https://dblp.org/pid/248/7663.html?view=joint&param=227 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Zhongqun Zhang](https://dblp.org/pid/237/8882.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[228](https://dblp.org/pid/248/7663.html?view=joint&param=228 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Guodongfang Zhao](https://dblp.org/pid/364/8196.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[229](https://dblp.org/pid/248/7663.html?view=joint&param=229 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jie Zhao 0014](https://dblp.org/pid/23/3168-14.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[230](https://dblp.org/pid/248/7663.html?view=joint&param=230 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Shao-Chuan Zhao](https://dblp.org/pid/260/3125.html)

aka: Shaochuan Zhao

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[231](https://dblp.org/pid/248/7663.html?view=joint&param=231 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Feng Zheng 0001](https://dblp.org/pid/39/800-1.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[232](https://dblp.org/pid/248/7663.html?view=joint&param=232 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Haixia Zheng](https://dblp.org/pid/119/1585.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[233](https://dblp.org/pid/248/7663.html?view=joint&param=233 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Min Zheng](https://dblp.org/pid/23/328.html)

[\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[234](https://dblp.org/pid/248/7663.html?view=joint&param=234 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yaozong Zheng](https://dblp.org/pid/344/6907.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[235](https://dblp.org/pid/248/7663.html?view=joint&param=235 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Bineng Zhong 0001](https://dblp.org/pid/25/1637-1.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[236](https://dblp.org/pid/248/7663.html?view=joint&param=236 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Jiawen Zhu 0003](https://dblp.org/pid/135/5123-3.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[237](https://dblp.org/pid/248/7663.html?view=joint&param=237 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Xuefeng Zhu 0003](https://dblp.org/pid/70/6628-3.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[238](https://dblp.org/pid/248/7663.html?view=joint&param=238 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Yueting Zhuang](https://dblp.org/pid/218/7793.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3) [\[i5\]](https://dblp.org/pid/248/7663.html#i5) [\[i4\]](https://dblp.org/pid/248/7663.html#i4) [\[c1\]](https://dblp.org/pid/248/7663.html#c1)

[239](https://dblp.org/pid/248/7663.html?view=joint&param=239 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[ChengAo Zong](https://dblp.org/pid/364/8208.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

[240](https://dblp.org/pid/248/7663.html?view=joint&param=240 "show joint publications")

[![1](https://dblp.org/img/n.png)](https://dblp.org/pid/248/7663.html?view=group&param=1)

[Kunlong Zuo](https://dblp.org/pid/354/8493.html)

[\[c3\]](https://dblp.org/pid/248/7663.html#c3)

_no results_

![](https://dblp.org/img/cog.dark.24x24.png)

**manage site settings**

To protect your privacy, all features that rely on external API calls from your browser are _turned off by default_. You need to opt-in for them to become active. All settings here will be stored as cookies with your web browser. For more information [see our F.A.Q.](https://dblp.org/faq/15696107)

[\[+\]](https://dblp.org/pid/248/7663.html#) [\[–\]](https://dblp.org/pid/248/7663.html#) _Unpaywalled article links_

Add open access links from [![unpaywall.org](https://dblp.org/img/unpaywall-logo.80x16.png)](https://unpaywall.org/) to the list of external document links (if available).

**load links from unpaywall.org**

Privacy notice: By enabling the option above, your browser will contact the API of _unpaywall.org_ to load hyperlinks to open access articles. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Unpaywall privacy policy](http://unpaywall.org/legal/privacy).

[\[+\]](https://dblp.org/pid/248/7663.html#) [\[–\]](https://dblp.org/pid/248/7663.html#) _Archived links via Wayback Machine_

For web page which are no longer available, try to retrieve content from the [![web.archive.org](https://dblp.org/img/wayback-logo.72x14.png)](https://web.archive.org/) of the Internet Archive (if available).

**load content from archive.org**

Privacy notice: By enabling the option above, your browser will contact the API of _archive.org_ to check for archived content of web pages that are no longer available. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Internet Archive privacy policy](https://archive.org/about/terms.php).

[\[+\]](https://dblp.org/pid/248/7663.html#) [\[–\]](https://dblp.org/pid/248/7663.html#) _Reference lists_

Add a list of references from [![crossref.org](https://dblp.org/img/crossref-logo.60x15.png)](https://crossref.org/), [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/), and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load references from crossref.org and opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the APIs of _crossref.org_, _opencitations.net_, and _semanticscholar.org_ to load article reference information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [Crossref privacy policy](https://www.crossref.org/privacy/) and the [OpenCitations privacy policy](https://opencitations.net/about), as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/248/7663.html#) [\[–\]](https://dblp.org/pid/248/7663.html#) _Citation data_

Add a list of citing articles from [![opencitations.net](https://dblp.org/img/opencitations-logo.112x14.png)](https://opencitations.net/) and [![semanticscholar.org](https://dblp.org/img/semanticscholar-logo.128x16.png)](https://semanticscholar.org/) to record detail pages.

**load citations from opencitations.net**

Privacy notice: By enabling the option above, your browser will contact the API of _opencitations.net_ and _semanticscholar.org_ to load citation information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the [OpenCitations privacy policy](https://opencitations.net/about) as well as the [AI2 Privacy Policy](https://allenai.org/privacy-policy) covering Semantic Scholar.

[\[+\]](https://dblp.org/pid/248/7663.html#) [\[–\]](https://dblp.org/pid/248/7663.html#) _OpenAlex data_![](https://dblp.org/img/new.blue.24x12.png)

Load additional information about publications from [![openalex.org](https://dblp.org/img/openalex-logo.69x18.png)](https://openalex.org/).

**load data from openalex.org**

Privacy notice: By enabling the option above, your browser will contact the API of _openalex.org_ to load additional information. Although we do not have any reason to believe that your call will be tracked, we do not have any control over how the remote server uses your data. So please proceed with care and consider checking the information given by [OpenAlex](https://openalex.org/about).

![](https://dblp.org/img/new-feature-top-right.156x64.png)